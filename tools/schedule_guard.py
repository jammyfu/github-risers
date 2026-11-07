#!/usr/bin/env python3
"""Gate refreshes by local hour (local fallback) or by last successful data date (Actions).

Actions can start hours late. --daily-state compares generated_at from the committed data
with the current date in --tz; only a successful refresh on that local date suppresses it.
The two UTC cron entries still target LA midnight across DST. Workflow concurrency and
checkout of current main ensure a later trigger observes the earlier committed refresh.

  python3 tools/schedule_guard.py --tz America/Los_Angeles --daily-state data/stats.json
  python3 tools/schedule_guard.py --tz America/Los_Angeles --hour 0

Exit codes: 0 = run, 1 = intentional skip, 2 = invalid state/configuration.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path
from zoneinfo import ZoneInfo


def local_hour(now_utc: dt.datetime, tz: str) -> int:
    if now_utc.tzinfo is None:
        raise ValueError("now_utc must be timezone-aware")
    return now_utc.astimezone(ZoneInfo(tz)).hour


def is_local_hour(now_utc: dt.datetime, tz: str, hour: int) -> bool:
    return local_hour(now_utc, tz) == hour


def parse_now(value: str | None) -> dt.datetime:
    if not value:
        return dt.datetime.now(dt.timezone.utc)
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed.astimezone(dt.timezone.utc)


def daily_update_due(now_utc: dt.datetime, tz: str, state_path: Path) -> bool:
    if now_utc.tzinfo is None:
        raise ValueError("now_utc must be timezone-aware")
    zone = ZoneInfo(tz)
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return True
    generated = state["generated_at"]
    if not isinstance(generated, str) or not generated:
        raise ValueError("generated_at must be a nonempty timezone-aware timestamp")
    previous = parse_now(generated)
    if previous > now_utc:
        raise ValueError("generated_at is in the future")
    return previous.astimezone(zone).date() < now_utc.astimezone(zone).date()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tz", required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--hour", type=int)
    mode.add_argument("--daily-state", type=Path, help="committed stats.json used for once-per-local-day refresh")
    ap.add_argument("--now", default=os.environ.get("ATLAS_NOW_UTC"),
                    help="override current time (ISO 8601, UTC); also read from ATLAS_NOW_UTC")
    args = ap.parse_args(argv)
    try:
        now = parse_now(args.now)
        if args.daily_state is not None:
            due = daily_update_due(now, args.tz, args.daily_state)
            day = now.astimezone(ZoneInfo(args.tz)).date()
            if due:
                print(f"run: no committed refresh for {day} in {args.tz}; late runs may catch up")
                return 0
            print(f"skip: committed data already refreshed on {day} in {args.tz}")
            return 1
        h = local_hour(now, args.tz)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"error: cannot decide refresh: {exc}", file=sys.stderr)
        return 2
    if h == args.hour:
        print(f"run: {now:%Y-%m-%d %H:%M}Z is {args.hour:02d}:xx in {args.tz}")
        return 0
    print(f"skip: {now:%Y-%m-%d %H:%M}Z is {h:02d}:xx in {args.tz}, not {args.hour:02d}:xx")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
