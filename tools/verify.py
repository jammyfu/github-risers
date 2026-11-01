#!/usr/bin/env python3
"""Single verification entry point (harness convention). Uses explicit interpreter paths,
no shell and no PATH lookups, so it also works under cron/launchd.

Steps: compile all Python, run unit tests, check generated READMEs are current.

``--daily`` is for the scheduled data run (Actions / tools/local_daily.sh): the unit tests are code tests and run in
CI on every pull request; the daily run only validates the data it just generated (tools/data_checks.py: hard
errors fail, small drift against the GitHub API only warns), so a value that moves with GitHub can never throw away a
day's update. See docs/DAILY_UPDATE.md.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def commands(root: Path, daily: bool = False) -> list[list[str]]:
    py = sys.executable
    tests = [] if daily else [[py, "-m", "unittest", "discover", "-s", "tests", "-v"]]
    data = [[py, "tools/data_checks.py"]] if daily else []
    return [
        [py, "-m", "compileall", "-q", "tools", "tests"],
        *tests,
        *data,
        [py, "tools/render_readme.py", "--check"],
        [py, "tools/newcomer_i18n.py"],  # lists untranslated new-repo descriptions; informational, never fails
    ]


def main(argv: list[str] | None = None) -> int:
    daily = "--daily" in (sys.argv[1:] if argv is None else argv)
    root = Path(__file__).resolve().parents[1]
    for cmd in commands(root, daily=daily):
        print(">>>", " ".join(cmd), flush=True)
        rc = subprocess.run(cmd, cwd=root).returncode
        if rc != 0:
            print(f"verification failed: {' '.join(cmd)}", file=sys.stderr)
            return rc
    print("All verification commands passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
