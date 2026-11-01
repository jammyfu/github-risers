#!/usr/bin/env python3
"""Validate the freshly generated data (data/stats.json, data/stars.json) after a daily update.

The scheduled run used to "verify" by running the whole unit-test suite against live data. Any value that
drifts with GitHub (a few stars between /stargazers/history and /repos, a new repo without a hook yet)
then failed the run and threw away the whole day's update. That happened twice in three days
(runs 41122642510 and 41235403615). Code tests belong to CI; the daily run only validates the data, with
two severities:

* errors  - the data is wrong or incomplete: the run fails and nothing is committed.
* warnings - the data is fine but not perfect (small history/star drift, a few repos fetched as missing):
             printed as GitHub Actions ``::warning::`` lines, the run stays green.

    python3 tools/data_checks.py            # exit 1 only on errors
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import risers_core as core  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# Above this share of tracked projects fetched as missing the run is treated as an API outage / rate-limit
# problem: publishing it would replace real numbers with "missing", so it fails instead of committing.
MAX_MISSING_SHARE = 0.25


def check(stats: dict[str, Any], projects: list[dict], snaps: dict[str, dict[str, int]]) -> tuple[list[str], list[str]]:
    """Return (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []
    rows = stats.get("projects") or []
    if [p.get("name") for p in rows] != [p["name"] for p in projects]:
        errors.append("stats.json projects do not match data/projects.json (names or order)")
    missing = [p for p in rows if not p.get("ok")]
    if rows and len(missing) / len(rows) > MAX_MISSING_SHARE:
        errors.append(f"{len(missing)}/{len(rows)} projects fetched as missing (> {MAX_MISSING_SHARE:.0%}): "
                      "looks like an API outage or rate limit; not publishing")
    elif missing:
        warnings.append(f"{len(missing)} project(s) fetched as missing: " + ", ".join(p["name"] for p in missing))
    for p in rows:
        name = p.get("name")
        if not p.get("ok"):
            if not p.get("error"):
                errors.append(f"{name}: missing without an error message")
            continue
        for key, days in core.WINDOWS.items():
            g = (p.get("growth") or {}).get(key)
            if not g:
                errors.append(f"{name}: no {key} growth")
                continue
            if g["window_days"] != days:
                errors.append(f"{name}: {key} window_days {g['window_days']} != {days}")
            if g["gained"] < 0:
                errors.append(f"{name}: negative {key} gain {g['gained']}")
            if g["effective_days"] > days:
                errors.append(f"{name}: {key} effective_days {g['effective_days']} > {days}")
            elif g["effective_days"] > 0 and abs(g["per_day"] - g["gained"] / g["effective_days"]) > 0.01:
                errors.append(f"{name}: {key} per_day does not match gained/effective_days")
        if p.get("history_complete") and p.get("history_total") is not None:
            total, stars = p["history_total"], p["stars"]
            if not core.history_total_within_hard_limit(total, stars):
                errors.append(f"{name}: history_total {total} vs stars {stars} differ by more than "
                              f"{core.history_total_hard_limit(stars)}")
            elif not core.history_total_within_slack(total, stars):
                warnings.append(f"{name}: history_total {total} vs stars {stars} drift by {abs(total - stars)} "
                                f"(> {core.HISTORY_TOTAL_STAR_SLACK}; GitHub history lags the live count)")
        if snaps.get(name, {}).get(stats.get("today_utc")) != p["stars"]:
            errors.append(f"{name}: data/stars.json has no snapshot for {stats.get('today_utc')}")
    return errors, warnings


def main(root: Path = ROOT) -> int:
    stats = json.loads((root / "data/stats.json").read_text("utf-8"))
    projects = json.loads((root / "data/projects.json").read_text("utf-8"))
    snaps = json.loads((root / "data/stars.json").read_text("utf-8"))
    errors, warnings = check(stats, projects, snaps)
    for w in warnings:
        print(f"::warning title=data check::{w}")
    for e in errors:
        print(f"::error title=data check::{e}", file=sys.stderr)
    if errors:
        print(f"data check failed: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"data check passed: {len(stats.get('projects') or [])} projects, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
