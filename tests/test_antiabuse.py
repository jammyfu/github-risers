"""Star-farm filter (tools/antiabuse.py + data/anti_abuse.json).

Pins: the 2026-11-13 `<account>/ai--manus` clone flood is removed from every new-repo board (and does not
use up the refresh budget), the original of a cloned repo survives when its owner is credible, the per-repo
signals (stars nobody forks, fake watchers, fresh throwaway owners), the blocklist on every board, and that
normal hot repos measured from real history snapshots are untouched.
"""
import datetime as dt
import json
import sys
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import antiabuse as aa  # noqa: E402
import newcomers as nc  # noqa: E402
import risers_core as core  # noqa: E402

NOW = dt.datetime(2026, 11, 14, 8, 0, tzinfo=dt.timezone.utc)
NOSLEEP = lambda s: None  # noqa: E731
MANUS_DESC = ("AI Manus is a general-purpose AI Agent system that supports running various tools and "
              "operations in a sandbox environment.")
MANUS_OWNERS = ["AdmiralEmporium", "ApothecaryDesign", "ArcherAmplify", "Archiveeutrough", "ArcticPrawnEmporium",
                "armsworminterface", "armysystemsun", "Aspectnisafeguard", "BarrierCenter", "BladesmithPanel",
                "Boarddrunail", "Boardglacode", "ClampOverlord46", "Feathershosmash", "GryphonEmpress",
                "HurricaneMonarchDart", "TealAgentRevive", "TorusBarbarianMap9", "WinnerBrokerBarrow",
                "AdvisorShake", "AgentLobster", "AmplitudeBoss", "AtomEmissary", "StudentSeparate"]


def ts(days_ago: float) -> str:
    return (NOW - dt.timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def repo(name, stars, days_old=1.0, desc="a normal repo", topics=("ai", "web"), forks=None, subs=None, **kw):
    r = {"full_name": name, "id": abs(hash(name)) % 10**9, "html_url": f"https://github.com/{name}",
         "description": desc, "language": "TypeScript", "stargazers_count": stars, "created_at": ts(days_old),
         "fork": False, "archived": False, "private": False, "topics": list(topics),
         "forks_count": max(stars // 10, 1) if forks is None else forks}
    if subs is not None:
        r["subscribers_count"] = subs
    r.update(kw)
    return r


def cfg_no_blocklist():
    """Real thresholds, empty blocklist: proves the rules catch the flood without a hand-written entry."""
    return {**aa.load_config(), "blocklist": {"repos": [], "owners": [], "names": []}}


def user(login, account_days, followers, kind="User"):
    return {"login": login, "type": kind, "created_at": ts(account_days), "followers": followers}


def manus_pool():
    # exactly what the 2026-11-14 board showed: same name, same description, 0 forks, fresh 0-follower accounts
    return [repo(f"{o}/ai--manus", 266 + i % 3, 0.6, MANUS_DESC, forks=0, subs=1) for i, o in enumerate(MANUS_OWNERS)]


def fake_api(pool, users):
    def api(path):
        if path.startswith("/search/repositories"):
            q = parse_qs(urlparse(path).query)["q"][0]
            topic = q.split()[0].removeprefix("topic:")
            hits = sorted((r for r in pool if topic in r["topics"]), key=lambda r: -r["stargazers_count"])
            return {"total_count": len(hits), "items": hits}
        if path.startswith("/users/"):
            login = path.removeprefix("/users/")
            if login.lower() in users:
                return users[login.lower()]
            raise RuntimeError("404")
        return next(r for r in pool if r["full_name"] == path.removeprefix("/repos/"))
    return api


def default_users(pool):
    users = {}
    for r in pool:
        o = r["full_name"].split("/")[0]
        users[o.lower()] = user(o, 31, 0) if r["full_name"].endswith("ai--manus") else user(o, 2000, 120)
    return users


NORMAL = [  # shaped after real boards: yogurt, islandcn, lot-map, HolyArrs, serveros panel
    repo("FrigadeHQ/yogurt", 1368, 3.7, "Private AI meeting notes that stay on your computer", forks=71, subs=18),
    repo("opencoredev/islandcn", 587, 1.1, "The open-source Dynamic Island for React", forks=55, subs=0),
    repo("alexeyw/lot-map", 780, 4.8, "A live map beside the chat that shows what Claude is doing", forks=88, subs=6),
    repo("HolyArrs/HolyArrs", 1141, 4.6, "One self-hosted app for your shows, movies and music", forks=59, subs=3),
    repo("serveroshq/panel", 771, 5.5, "The open source ServerOS panel", forks=62, subs=2),
]


class CloneClusterTests(unittest.TestCase):
    def test_ai_manus_flood_is_one_cluster_and_fully_dropped(self):
        g = aa.Guard(fake_api([], default_users(manus_pool())), NOW, cfg_no_blocklist())
        kept, dropped, clusters = g.screen_candidates(manus_pool() + NORMAL)
        self.assertEqual({r["full_name"] for r in kept}, {r["full_name"] for r in NORMAL})
        self.assertEqual(len(dropped), len(MANUS_OWNERS))
        self.assertTrue(all(d["reason"].startswith("clone-cluster:ai--manus") for d in dropped))
        self.assertEqual(len(clusters), 1)
        self.assertIsNone(clusters[0]["kept"])
        self.assertEqual(clusters[0]["owners"], len(MANUS_OWNERS))

    def test_same_description_under_new_names_is_still_a_cluster(self):
        pool = [repo(f"farm{i}/agent-{i}", 300, 1, "Agent OS 2026: run every tool in a sandbox!!", forks=3)
                for i in range(2)]
        clusters = aa.find_clone_clusters(pool, aa.load_config())
        self.assertEqual(len(clusters), 1)

    def test_original_survives_when_its_owner_is_credible(self):
        orig = repo("realorg/cool-agent", 900, 5, "A cool agent framework with a long description", forks=80)
        copies = [repo(f"copy{i}/cool-agent", 300, 1, "A cool agent framework with a long description", forks=0)
                  for i in range(3)]
        users = {"realorg": user("realorg", 3000, 500, "Organization")}
        users.update({f"copy{i}": user(f"copy{i}", 10, 0) for i in range(3)})
        g = aa.Guard(fake_api([], users), NOW)
        kept, dropped, clusters = g.screen_candidates([orig] + copies)
        self.assertEqual([r["full_name"] for r in kept], ["realorg/cool-agent"])
        self.assertEqual(clusters[0]["kept"], "realorg/cool-agent")
        self.assertEqual(len(dropped), 3)

    def test_two_unrelated_repos_sharing_a_generic_name_are_kept(self):
        pool = [repo("alice/agent-skills", 400, 2, "Skills for Claude Code by Alice"),
                repo("bob/agent-skills", 300, 3, "My curated list of Codex prompts")]
        self.assertEqual(aa.find_clone_clusters(pool, aa.load_config()), [])

    def test_same_owner_duplicates_are_not_a_cluster(self):
        pool = [repo("me/dsh-go", 900, 2, "DeepSeek Harness in your pocket, runs on the phone"),
                repo("me/dsh-Go", 900, 2, "DeepSeek Harness in your pocket, runs on the phone")]
        self.assertEqual(aa.find_clone_clusters(pool, aa.load_config()), [])

    def test_name_normalization(self):
        self.assertEqual(aa.norm_name("AI--Manus"), aa.norm_name("ai_manus"))
        self.assertEqual(aa.norm_desc("Tool 2026: setup!"), aa.norm_desc("tool 2023 setup"))


class SignalTests(unittest.TestCase):
    cfg = aa.load_config()

    def test_stars_nobody_forks_are_dropped(self):
        drop, _ = aa.repo_signals(repo("x/rufus-usb-formatter", 1103, forks=0), user("x", 2000, 0), self.cfg)
        self.assertTrue(drop.startswith("low-fork"))

    def test_fake_watchers_are_dropped(self):
        drop, _ = aa.repo_signals(repo("x/Blender-AI-MCP-Studio", 272, forks=4, subs=195), None, self.cfg)
        self.assertTrue(drop.startswith("watch-farm"))

    def test_fresh_owner_plus_low_forks_is_dropped_alone_only_flagged(self):
        r = repo("x/cubase-studio-desktop", 300, forks=0)
        self.assertTrue(aa.repo_signals(r, user("x", 20, 0), self.cfg)[0].startswith("new-owner+low-fork"))
        drop, flag = aa.repo_signals(repo("x/thing", 300, forks=40), user("x", 20, 0), self.cfg)
        self.assertIsNone(drop)
        self.assertEqual(flag, "new-owner")

    def test_low_fork_alone_is_only_flagged(self):
        drop, flag = aa.repo_signals(repo("o/ChaosIntelligence", 428, forks=0), user("o", 3000, 3), self.cfg)
        self.assertIsNone(drop)
        self.assertTrue(flag.startswith("low-fork"))

    def test_normal_repos_have_no_signal(self):
        for r in NORMAL:
            with self.subTest(r["full_name"]):
                self.assertEqual(aa.repo_signals(r, user("o", 1500, 100), self.cfg), (None, None))

    def test_unknown_owner_and_missing_forks_never_trigger(self):
        r = repo("o/x", 5000)
        del r["forks_count"]
        self.assertEqual(aa.repo_signals(r, None, self.cfg), (None, None))

    def test_owner_lookup_budget_fails_open(self):
        calls = []
        g = aa.Guard(lambda p: calls.append(p) or user("x", 1, 0), NOW, {**aa.load_config(), "owner_lookup_budget": 1})
        g.owner("a")
        self.assertIsNone(g.owner("b"))
        self.assertEqual(len(calls), 1)


class BlocklistTests(unittest.TestCase):
    def test_blocklist_matches_repo_owner_and_name_pattern(self):
        cfg = {**aa.load_config(), "blocklist": {"repos": ["A/B"], "owners": ["evil"], "names": ["ai--manus"]}}
        self.assertEqual(aa.blocked_reason("a/b", cfg), "blocklist:repo")
        self.assertEqual(aa.blocked_reason("EVIL/x", cfg), "blocklist:owner")
        self.assertTrue(aa.blocked_reason("someone/AI--Manus", cfg).startswith("blocklist:name"))
        self.assertIsNone(aa.blocked_reason("Simpleyyt/ai-manus", cfg))

    def test_blocked_tracked_project_is_never_ranked_on_any_board(self):
        g = {"per_day": 1.0}
        projs = [{"name": "a/a", "ok": True, "stars": 10, "growth": {"week": g, "month": g, "year": g}},
                 {"name": "b/b", "ok": True, "stars": 99, "blocked": "blocklist:repo",
                  "growth": {"week": {"per_day": 9}, "month": {"per_day": 9}, "year": {"per_day": 9}}}]
        for key in ("week", "month", "year", "total"):
            self.assertEqual([p["name"] for p in core.rank(projs, key)], ["a/a"])

    def test_tracked_projects_are_not_blocklisted(self):
        cfg = aa.load_config()
        for p in json.loads((ROOT / "data/projects.json").read_text("utf-8")):
            self.assertIsNone(aa.blocked_reason(p["name"], cfg), p["name"])

    def test_config_file_is_valid(self):
        cfg = aa.load_config()
        for k in ("clone_clusters", "low_fork", "watch_farm", "new_owner", "blocklist"):
            self.assertIn(k, cfg)


class DiscoveryTests(unittest.TestCase):
    def test_board_backfills_with_normal_repos_and_reports_the_drop(self):
        pool = manus_pool() + NORMAL + [repo("dev/real-small", 150, 5, "A real small tool", forks=12, subs=2)]
        orig = nc.REFRESH_TOP
        nc.REFRESH_TOP = 6  # the flood must not eat the refresh budget
        try:
            api = fake_api(pool, default_users(pool))
            res = nc.discover_category(api, NOW, {"id": "ai", "topics": ["ai"]}, set(), NOSLEEP,
                                       aa.Guard(api, NOW, cfg_no_blocklist()))
        finally:
            nc.REFRESH_TOP = orig
        names = [i["name"] for i in res["items"]]
        self.assertFalse([n for n in names if n.endswith("ai--manus")])
        self.assertEqual(len(names), 6)
        self.assertEqual(names[0], "opencoredev/islandcn")
        self.assertEqual(res["anti_abuse"]["dropped_count"], len(MANUS_OWNERS))
        self.assertEqual(res["anti_abuse"]["by_reason"], {"clone-cluster": len(MANUS_OWNERS)})

    def test_every_category_board_is_clean(self):
        pool = manus_pool() + NORMAL
        cats = [{"id": "ai", "primary": True, "order": 0, "topics": ["ai"]},
                {"id": "web", "order": 1, "topics": ["web"]}]
        res = nc.discover_all(fake_api(pool, default_users(pool)), NOW, cats, [], [], core.rank, NOSLEEP)
        for cid, block in res["categories"].items():
            with self.subTest(cid):
                self.assertFalse([i for i in block["items"] if i["name"].endswith("ai--manus")])
        self.assertEqual(res["anti_abuse"]["dropped_total"], 2 * len(MANUS_OWNERS))

    def test_flagged_repo_is_ranked_last_with_reason(self):
        pool = NORMAL[:2] + [repo("o/zero-forks", 300, 1, "Something", forks=0, subs=0)]
        res = nc.discover_category(fake_api(pool, {"o": user("o", 3000, 3)} | {r["full_name"].split("/")[0].lower(): user("x", 3000, 90) for r in NORMAL}),
                                   NOW, {"id": "ai", "topics": ["ai"]}, set(), NOSLEEP)
        self.assertEqual(res["items"][-1]["name"], "o/zero-forks")
        self.assertTrue(res["items"][-1]["suspicious"].startswith("low-fork"))


class RenderTests(unittest.TestCase):
    def test_farm_flag_gets_its_own_note_in_every_language(self):
        import archive
        from i18n import S
        item = {"name": "o/x", "url": "u", "description": "d", "created_at": "2026-11-13T00:00:00Z", "stars": 300,
                "per_day": 300.0, "age_days": 1.0, "suspicious": "low-fork:300 stars/0 forks"}
        stats = {"generated_at": "2026-11-14T08:00:00Z", "today_utc": "2026-11-14", "projects": [],
                 "category_ids": ["ai"], "newcomers": {"ok": True, "categories": {"ai": {"ok": True, "items": [item]}}}}
        cats = [{"id": "ai", "primary": True, "order": 0, "name": {}, "topics": ["ai"]}]
        for lang in S:
            with self.subTest(lang):
                md = archive.render_rankings_md(stats, lang, cats)
                self.assertIn(S[lang]["farm_note"], md)
                self.assertNotIn(S[lang]["susp_note"], md)


class HistoryReplayTests(unittest.TestCase):
    """Committed boards: the clone rule never fires on a board without a real clone flood."""

    def test_history_boards_only_cluster_known_farms(self):
        cfg = aa.load_config()
        for f in sorted((ROOT / "rankings").glob("*/*/stats.json")):
            nc_root = json.loads(f.read_text("utf-8")).get("newcomers") or {}
            for cid, block in (nc_root.get("categories") or {"ai": nc_root}).items():
                repos = [{"full_name": i["name"], "description": i.get("description"), "created_at": i.get("created_at"),
                          "stargazers_count": i.get("stars")} for i in block.get("items") or []]
                for cl in aa.find_clone_clusters(repos, cfg):
                    for m in cl["members"]:
                        with self.subTest(f=str(f.relative_to(ROOT)), cid=cid, repo=m["full_name"]):
                            # every clustered member is either the ai--manus flood or already a ⚠ crack repo
                            item = next(i for i in block["items"] if i["name"] == m["full_name"])
                            self.assertTrue(m["full_name"].lower().endswith("/ai--manus") or item.get("suspicious")
                                            or "full working installer" in (item.get("description") or "").lower()
                                            or "standalone" in (item.get("description") or "").lower(),
                                            m["full_name"])


if __name__ == "__main__":
    unittest.main()
