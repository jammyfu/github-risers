"""Anti star-farming filters for the "hottest new repos" boards, plus a blocklist for every board.

Star farms create many throwaway accounts that each publish the same repo (same name and/or the same
description, e.g. hundreds of `<account>/ai--manus`) and pump them with bought stars, or push one repo
with stars nobody forks or with fake watchers. The rules below only read fields the GitHub API already
returns (search / GET /repos/{r} / GET /users/{u}); thresholds live in data/anti_abuse.json and are
documented in docs/ANTI_ABUSE.md. tests/test_antiabuse.py pins them.

Two outcomes:
  drop    -> removed from the board, recorded under newcomers.categories.<id>.anti_abuse (never in a README)
  flag    -> kept with `suspicious: <reason>`, shown with ⚠, ranked after every normal repo, never a leader
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data/anti_abuse.json"

DEFAULTS: dict[str, Any] = {
    "clone_clusters": {"enabled": True, "name_min_owners": 3, "desc_min_owners": 2,
                       "name_and_desc_min_owners": 2, "min_desc_chars": 24, "keep_check_earliest": 3},
    "credible_owner": {"min_account_days": 365, "min_followers": 50},
    "new_owner": {"max_account_days": 60, "max_followers": 5},
    "low_fork": {"min_stars": 150, "flag_ratio": 100, "drop_ratio": 500},
    "watch_farm": {"min_stars": 100, "share": 0.4},
    "fork_farm": {"min_stars": 100, "share": 0.9},
    "owner_lookup_budget": 150,
    "blocklist": {"repos": [], "owners": [], "names": []},
}
REPORT_CAP = 200  # single drops listed per category (counts are always exact)
SAMPLE_CAP = 20   # names listed for clone-cluster / blocklist drops

Api = Callable[[str], Any]


def load_config(path: Path | None = None) -> dict[str, Any]:
    """data/anti_abuse.json merged over DEFAULTS (missing file -> defaults)."""
    cfg = json.loads(json.dumps(DEFAULTS))
    p = path or CONFIG_PATH
    if p.exists():
        raw = json.loads(p.read_text("utf-8"))
        for k, v in raw.items():
            if k.startswith("_"):
                continue
            if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                cfg[k].update({kk: vv for kk, vv in v.items() if not kk.startswith("_")})
            else:
                cfg[k] = v
    return cfg


def _parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def split_name(full_name: str) -> tuple[str, str]:
    owner, _, name = (full_name or "").partition("/")
    return owner, name


def norm_name(name: str) -> str:
    """Repo name without case and separators: 'AI--Manus', 'ai_manus' -> 'aimanus'."""
    return re.sub(r"[^0-9a-z]+", "", (name or "").lower())


def norm_desc(desc: str | None) -> str:
    """Description without case, digits, punctuation or spacing, so '... 2026 ...' variants still match."""
    return re.sub(r"[\W\d_]+", "", (desc or "").lower())


# ---------------------------------------------------------------- blocklist (every board)

def blocked_reason(full_name: str, cfg: dict[str, Any]) -> str | None:
    bl = cfg.get("blocklist") or {}
    owner, name = split_name(full_name)
    if full_name.lower() in {r.lower() for r in bl.get("repos") or []}:
        return "blocklist:repo"
    if owner.lower() in {o.lower() for o in bl.get("owners") or []}:
        return "blocklist:owner"
    for pat in bl.get("names") or []:
        if re.fullmatch(pat, name, flags=re.I):
            return f"blocklist:name:{pat}"
    return None


def filter_blocked_projects(projects: list[dict], cfg: dict[str, Any]) -> tuple[list[dict], list[dict]]:
    """Tracked projects (week / month / year / total boards) minus blocklisted ones."""
    kept, dropped = [], []
    for p in projects:
        reason = blocked_reason(p.get("name", ""), cfg)
        if reason:
            dropped.append({"name": p.get("name"), "reason": reason})
        else:
            kept.append(p)
    return kept, dropped


# ---------------------------------------------------------------- clone clusters

def find_clone_clusters(repos: list[dict], cfg: dict[str, Any]) -> list[dict[str, Any]]:
    """Group repos from different owners that share a normalized name or description.

    Returns [{"key", "members": [repo, ...] (oldest first), "owners": n}] for groups that pass the
    configured owner thresholds. A repo is in at most one cluster (union of name and description links).
    """
    cc = cfg["clone_clusters"]
    if not cc.get("enabled", True) or not repos:
        return []
    parent = list(range(len(repos)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    by_name: dict[str, list[int]] = {}
    by_desc: dict[str, list[int]] = {}
    for i, r in enumerate(repos):
        _, name = split_name(r.get("full_name", ""))
        if norm_name(name):
            by_name.setdefault(norm_name(name), []).append(i)
        d = norm_desc(r.get("description"))
        if len(d) >= int(cc["min_desc_chars"]):
            by_desc.setdefault(d, []).append(i)
    for idx in list(by_name.values()) + list(by_desc.values()):
        for j in idx[1:]:
            union(idx[0], j)

    groups: dict[int, list[int]] = {}
    for i in range(len(repos)):
        groups.setdefault(find(i), []).append(i)

    out = []
    for members in groups.values():
        if len(members) < 2:
            continue
        owners = {split_name(repos[i].get("full_name", ""))[0].lower() for i in members}
        if len(owners) < 2:
            continue
        names = {norm_name(split_name(repos[i].get("full_name", ""))[1]) for i in members}
        descs = {norm_desc(repos[i].get("description")) for i in members
                 if len(norm_desc(repos[i].get("description"))) >= int(cc["min_desc_chars"])}
        # owners per shared name / shared description
        name_owners = max(len({split_name(repos[i]["full_name"])[0].lower() for i in members
                               if norm_name(split_name(repos[i]["full_name"])[1]) == n}) for n in names)
        desc_owners = max((len({split_name(repos[i]["full_name"])[0].lower() for i in members
                                if norm_desc(repos[i].get("description")) == d}) for d in descs), default=0)
        both = 0
        for n in names:
            for d in descs:
                both = max(both, len({split_name(repos[i]["full_name"])[0].lower() for i in members
                                      if norm_name(split_name(repos[i]["full_name"])[1]) == n
                                      and norm_desc(repos[i].get("description")) == d}))
        if (name_owners >= int(cc["name_min_owners"]) or desc_owners >= int(cc["desc_min_owners"])
                or both >= int(cc["name_and_desc_min_owners"])):
            ms = sorted((repos[i] for i in members), key=lambda r: (r.get("created_at") or "", r["full_name"].lower()))
            key = split_name(ms[0]["full_name"])[1].lower()
            out.append({"key": key, "members": ms, "owners": len(owners)})
    return out


# ---------------------------------------------------------------- per-repo signals

def owner_age_days(repo: dict, owner: dict | None) -> float | None:
    created, ocreated = _parse_ts(repo.get("created_at")), _parse_ts((owner or {}).get("created_at"))
    if not created or not ocreated:
        return None
    return (created - ocreated).total_seconds() / 86400


def is_new_owner(repo: dict, owner: dict | None, cfg: dict[str, Any]) -> bool:
    if not owner or owner.get("type") != "User":
        return False
    age = owner_age_days(repo, owner)
    no = cfg["new_owner"]
    return (age is not None and age < float(no["max_account_days"])
            and int(owner.get("followers") or 0) < int(no["max_followers"]))


def is_credible_owner(owner: dict | None, now: dt.datetime, cfg: dict[str, Any]) -> bool:
    if not owner:
        return False
    created = _parse_ts(owner.get("created_at"))
    co = cfg["credible_owner"]
    return bool(created and (now - created).days >= int(co["min_account_days"])
                and int(owner.get("followers") or 0) >= int(co["min_followers"]))


def repo_signals(repo: dict, owner: dict | None, cfg: dict[str, Any]) -> tuple[str | None, str | None]:
    """(drop_reason, flag_reason) for one repo. subscribers_count is only on GET /repos/{r}."""
    stars = int(repo.get("stargazers_count") or 0)
    has_forks = repo.get("forks_count") is not None  # always present in real API payloads; unknown -> no fork rule
    forks = int(repo.get("forks_count") or 0)
    lf, wf, ff = cfg["low_fork"], cfg["watch_farm"], cfg["fork_farm"]
    ratio = stars / (forks + 1)
    low_fork = has_forks and stars >= int(lf["min_stars"]) and ratio >= float(lf["flag_ratio"])
    new_owner = is_new_owner(repo, owner, cfg)
    subs = repo.get("subscribers_count")
    if subs is not None and stars >= int(wf["min_stars"]) and int(subs) >= float(wf["share"]) * stars:
        return f"watch-farm:{int(subs)} watchers/{stars} stars", None
    if has_forks and stars >= int(lf["min_stars"]) and ratio >= float(lf["drop_ratio"]):
        return f"low-fork:{stars} stars/{forks} forks", None
    if low_fork and new_owner:
        return f"new-owner+low-fork:{stars} stars/{forks} forks", None
    if low_fork:
        return None, f"low-fork:{stars} stars/{forks} forks"
    if new_owner:
        return None, "new-owner"
    if has_forks and stars >= int(ff["min_stars"]) and forks >= float(ff["share"]) * stars:
        return None, f"fork-farm:{forks} forks/{stars} stars"
    return None, None


# ---------------------------------------------------------------- run state

class Guard:
    """One per daily run: config, a cached / budgeted owner lookup, cross-category memory and the report."""

    def __init__(self, api: Api | None, now: dt.datetime, cfg: dict[str, Any] | None = None):
        self.api = api
        self.now = now
        self.cfg = cfg or load_config()
        self.owners: dict[str, dict | None] = {}
        self.lookups = 0
        self.cluster_keys: set[str] = set()  # norm names / descs of clusters seen in earlier categories
        self.dropped_names: set[str] = set()

    def owner(self, login: str) -> dict | None:
        key = login.lower()
        if key in self.owners:
            return self.owners[key]
        if self.api is None or self.lookups >= int(self.cfg.get("owner_lookup_budget", 0)):
            return None  # fail open: unknown owner never triggers an owner rule
        self.lookups += 1
        try:
            data = self.api(f"/users/{login}")
            self.owners[key] = data if isinstance(data, dict) else None
        except Exception:
            self.owners[key] = None
        return self.owners[key]

    def _remembered(self, repo: dict) -> bool:
        _, name = split_name(repo.get("full_name", ""))
        d = norm_desc(repo.get("description"))
        return (repo.get("full_name", "").lower() in self.dropped_names
                or ("n:" + norm_name(name)) in self.cluster_keys
                or (len(d) >= int(self.cfg["clone_clusters"]["min_desc_chars"]) and ("d:" + d) in self.cluster_keys))

    def screen_candidates(self, cands: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
        """Before the GET /repos refresh: blocklist, clone clusters, extreme low-fork (search fields only).

        Returns (kept, dropped [{name, reason}], clusters [{key, owners, size, kept}]).
        """
        dropped: list[dict] = []
        kept: list[dict] = []
        for r in cands:
            reason = blocked_reason(r.get("full_name", ""), self.cfg)
            if not reason and self._remembered(r):
                reason = "clone-cluster:seen in an earlier category"
            if reason:
                dropped.append({"name": r["full_name"], "reason": reason})
            else:
                kept.append(r)
        clusters_out = []
        drop_ids: set[str] = set()
        for cl in find_clone_clusters(kept, self.cfg):
            keep = None
            for m in cl["members"][: int(self.cfg["clone_clusters"]["keep_check_earliest"])]:
                if is_credible_owner(self.owner(split_name(m["full_name"])[0]), self.now, self.cfg):
                    keep = m
                    break
            for m in cl["members"]:
                if m is keep:
                    continue
                drop_ids.add(m["full_name"].lower())
                dropped.append({"name": m["full_name"],
                                "reason": f"clone-cluster:{cl['key']} ({cl['owners']} owners)"})
                _, name = split_name(m["full_name"])
                self.cluster_keys.add("n:" + norm_name(name))
                d = norm_desc(m.get("description"))
                if len(d) >= int(self.cfg["clone_clusters"]["min_desc_chars"]):
                    self.cluster_keys.add("d:" + d)
            clusters_out.append({"key": cl["key"], "owners": cl["owners"], "size": len(cl["members"]),
                                 "kept": keep["full_name"] if keep else None})
        kept = [r for r in kept if r["full_name"].lower() not in drop_ids]
        final = []
        for r in kept:
            drop, _ = repo_signals({k: v for k, v in r.items() if k != "subscribers_count"}, None, self.cfg)
            if drop:
                dropped.append({"name": r["full_name"], "reason": drop})
            else:
                final.append(r)
        self.dropped_names |= {d["name"].lower() for d in dropped}
        return final, dropped, clusters_out

    def screen_refreshed(self, repo: dict) -> tuple[str | None, str | None]:
        """After GET /repos/{r}: watcher / fork / owner signals (one cached owner lookup)."""
        reason = blocked_reason(repo.get("full_name", ""), self.cfg)
        if reason:
            return reason, None
        owner = self.owner(split_name(repo.get("full_name", ""))[0])
        drop, flag = repo_signals(repo, owner, self.cfg)
        if drop:
            self.dropped_names.add(repo["full_name"].lower())
        return drop, flag


def report(dropped: list[dict], clusters: list[dict]) -> dict[str, Any]:
    """Compact log for stats.json: counts by reason, clusters (with a sample), and every other drop by name."""
    reasons: dict[str, int] = {}
    for d in dropped:
        k = d["reason"].split(":")[0]
        reasons[k] = reasons.get(k, 0) + 1
    bulk = [d for d in dropped if d["reason"].startswith(("clone-cluster", "blocklist"))]
    single = [d for d in dropped if not d["reason"].startswith(("clone-cluster", "blocklist"))]
    return {
        "dropped_count": len(dropped),
        "by_reason": dict(sorted(reasons.items())),
        "clusters": sorted(clusters, key=lambda c: -c["size"]),
        "bulk_sample": sorted({d["name"] for d in bulk}, key=str.lower)[:SAMPLE_CAP],
        "dropped": sorted(single, key=lambda d: d["name"].lower())[:REPORT_CAP],
    }
