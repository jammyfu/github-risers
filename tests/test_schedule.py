import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import schedule_guard as sg  # noqa: E402

LA = "America/Los_Angeles"


def utc(y, m, d, h, mi=0):
    return dt.datetime(y, m, d, h, mi, tzinfo=dt.timezone.utc)


class LocalHourTests(unittest.TestCase):
    def test_pdt_midnight_is_0700_utc(self):  # PDT = UTC-7
        self.assertTrue(sg.is_local_hour(utc(2026, 10, 29, 7), LA, 0))
        self.assertTrue(sg.is_local_hour(utc(2026, 10, 29, 7, 59), LA, 0))
        self.assertFalse(sg.is_local_hour(utc(2026, 10, 29, 8), LA, 0))  # 01:00 PDT

    def test_pst_midnight_is_0800_utc(self):  # PST = UTC-8
        self.assertTrue(sg.is_local_hour(utc(2026, 12, 15, 8), LA, 0))
        self.assertFalse(sg.is_local_hour(utc(2026, 12, 15, 7), LA, 0))  # 23:00 PST the day before

    def test_dst_boundaries_2026(self):
        # spring forward Sun 2026-03-08 10:00 UTC (02:00 PST -> 03:00 PDT)
        self.assertTrue(sg.is_local_hour(utc(2026, 3, 8, 8), LA, 0))      # still PST: 00:00
        self.assertFalse(sg.is_local_hour(utc(2026, 3, 8, 7), LA, 0))     # 23:00 PST on Mar 7
        self.assertTrue(sg.is_local_hour(utc(2026, 3, 9, 7), LA, 0))      # PDT from here on
        # fall back Sun 2026-11-01 09:00 UTC (02:00 PDT -> 01:00 PST)
        self.assertTrue(sg.is_local_hour(utc(2026, 11, 1, 7), LA, 0))     # 00:00 PDT
        self.assertFalse(sg.is_local_hour(utc(2026, 11, 1, 8), LA, 0))    # 01:00 PDT
        self.assertTrue(sg.is_local_hour(utc(2026, 11, 2, 8), LA, 0))     # 00:00 PST

    def test_exactly_one_la_slot_passes_every_day_of_the_year(self):
        day = dt.date(2026, 1, 1)
        while day.year == 2026:
            passes = [h for h in (7, 8) if sg.is_local_hour(utc(day.year, day.month, day.day, h), LA, 0)]
            self.assertEqual(len(passes), 1, f"{day}: {passes}")
            day += dt.timedelta(days=1)

    def test_beijing_slot_is_1600_utc_all_year(self):
        for month in (1, 4, 7, 10):
            self.assertTrue(sg.is_local_hour(utc(2026, month, 15, 16), "Asia/Shanghai", 0))
            self.assertFalse(sg.is_local_hour(utc(2026, month, 15, 15), "Asia/Shanghai", 0))

    def test_naive_datetime_rejected(self):
        with self.assertRaises(ValueError):
            sg.local_hour(dt.datetime(2026, 10, 29, 7), LA)


class CliTests(unittest.TestCase):
    def run_guard(self, now):
        return subprocess.run([sys.executable, str(ROOT / "tools/schedule_guard.py"), "--tz", LA,
                               "--hour", "0", "--now", now], capture_output=True, text=True)

    def test_exit_codes(self):
        run = self.run_guard("2026-10-29T07:05:00Z")
        self.assertEqual(run.returncode, 0, run.stdout)
        self.assertIn("run:", run.stdout)
        skip = self.run_guard("2026-10-29T08:05:00Z")
        self.assertEqual(skip.returncode, 1)
        self.assertIn("skip:", skip.stdout)


class DailyStateTests(unittest.TestCase):
    def run_daily(self, now, state):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "stats.json"
            if state is not None:
                path.write_text(json.dumps(state), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(ROOT / "tools/schedule_guard.py"), "--tz", LA,
                 "--daily-state", str(path), "--now", now], capture_output=True, text=True)

    def test_seven_hour_delay_still_refreshes_stale_data(self):
        r = self.run_daily("2026-11-06T15:26:58Z", {"generated_at": "2026-11-04T23:50:00Z"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("run:", r.stdout)

    def test_second_delayed_trigger_skips_same_la_day(self):
        r = self.run_daily("2026-11-06T16:26:58Z", {"generated_at": "2026-11-06T15:26:58Z"})
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn("skip:", r.stdout)

    def test_utc_date_change_does_not_count_as_a_new_la_day(self):
        r = self.run_daily("2026-11-07T07:00:00Z", {"generated_at": "2026-11-06T15:26:58Z"})
        self.assertEqual(r.returncode, 1, r.stderr)

    def test_la_midnight_starts_a_new_day_across_dst_changes(self):
        cases = [
            ("2026-03-08T08:00:00Z", "2026-03-07T08:00:00Z"),
            ("2026-03-09T07:00:00Z", "2026-03-08T08:00:00Z"),
            ("2026-11-01T07:00:00Z", "2026-10-31T07:00:00Z"),
            ("2026-11-02T08:00:00Z", "2026-11-01T07:00:00Z"),
        ]
        for now, previous in cases:
            with self.subTest(now=now):
                r = self.run_daily(now, {"generated_at": previous})
                self.assertEqual(r.returncode, 0, r.stderr)

    def test_missing_state_allows_initial_refresh(self):
        r = self.run_daily("2026-11-06T15:26:58Z", None)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_bad_and_future_state_are_errors_not_successful_skips(self):
        for state in ({}, [], {"generated_at": "invalid"},
                      {"generated_at": "2026-11-06T08:00:00"},
                      {"generated_at": "2026-11-07T08:00:00Z"}):
            with self.subTest(state=state):
                r = self.run_daily("2026-11-06T15:26:58Z", state)
                self.assertEqual(r.returncode, 2, r.stderr)
                self.assertIn("error:", r.stderr)


class WorkflowGateBehaviorTests(unittest.TestCase):
    def run_gate(self, event, state):
        workflow = (ROOT / ".github/workflows/daily-update.yml").read_text("utf-8")
        gate = workflow.split("        run: |\n", 1)[1].split("      # Optional:", 1)[0]
        script = "\n".join(line[10:] for line in gate.splitlines())
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "tools").mkdir()
            shutil.copy(ROOT / "tools/schedule_guard.py", root / "tools/schedule_guard.py")
            (root / "data").mkdir()
            (root / "data/stats.json").write_text(json.dumps(state), encoding="utf-8")
            output = root / "output"
            env = dict(os.environ, EVENT=event, GITHUB_OUTPUT=str(output),
                       ATLAS_NOW_UTC="2026-11-06T15:26:58Z")
            r = subprocess.run(["/bin/bash", "-e", "-c", script], cwd=root, env=env,
                               capture_output=True, text=True)
            return r, output.read_text() if output.exists() else ""

    def test_delayed_schedule_fetches_and_duplicate_skips(self):
        r, output = self.run_gate("schedule", {"generated_at": "2026-11-04T23:50:00Z"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("run=true", output)
        self.assertIn("slot=pt", output)
        r, output = self.run_gate("schedule", {"generated_at": "2026-11-06T09:00:00Z"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("run=false", output)

    def test_bad_state_fails_the_workflow_instead_of_reporting_success(self):
        r, output = self.run_gate("schedule", {"generated_at": "invalid"})
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertNotIn("run=false", output)

    def test_manual_dispatch_always_proceeds(self):
        r, output = self.run_gate("workflow_dispatch", {"generated_at": "invalid"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("run=true", output)
        self.assertIn("slot=auto", output)


class LocalScriptTests(unittest.TestCase):
    def run_script(self, now, slot):
        env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN")}
        env["ATLAS_NOW_UTC"] = now
        return subprocess.run(["bash", str(ROOT / "tools/local_daily.sh"), "--slot", slot],
                              capture_output=True, text=True, env=env, cwd=ROOT)

    def test_la_slot_skips_outside_midnight_without_touching_anything(self):
        r = self.run_script("2026-10-29T08:30:00Z", "la")  # 01:30 PDT
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("skip:", r.stdout)
        self.assertNotIn("error", r.stderr)

    def test_beijing_slot_skips_outside_midnight(self):
        r = self.run_script("2026-10-29T15:30:00Z", "beijing")  # 23:30 Beijing
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("skip:", r.stdout)

    def test_unknown_slot_rejected(self):
        r = self.run_script("2026-10-29T07:30:00Z", "mars")
        self.assertEqual(r.returncode, 2)


class WorkflowScheduleTests(unittest.TestCase):
    wf = (ROOT / ".github/workflows/daily-update.yml").read_text("utf-8")

    def test_two_la_crons(self):
        crons = re.findall(r"- cron: '([^']+)'", self.wf)
        self.assertEqual(sorted(crons), sorted(["0 7 * * *", "0 8 * * *"]))
        self.assertNotIn("0 16 * * *", self.wf)

    def test_la_guard_wired_and_steps_gated(self):
        self.assertIn("tools/schedule_guard.py --tz America/Los_Angeles --daily-state data/stats.json", self.wf)
        self.assertEqual(self.wf.count("if: steps.gate.outputs.run == 'true'"), 4)  # install CLI, fetch, verify, commit
        self.assertNotIn("slot=cn", self.wf)  # scheduled production is pt only
        self.assertIn("slot=pt", self.wf)
        self.assertIn("slot=auto", self.wf)
        self.assertIn('--slot "$SLOT"', self.wf)
        self.assertIn("git add data rankings latest README*.md", self.wf)


if __name__ == "__main__":
    unittest.main()
