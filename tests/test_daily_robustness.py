"""Regression tests for the recurring daily-update failures (runs 41122642510 and 41235403615).

Root cause: the scheduled run verified by running the whole unit-test suite against live data, so any value that
moves with GitHub (hook gaps for new repos, history_total vs stars drift) failed the run and discarded the day's
update. The daily run now validates data only (tools/data_checks.py): hard errors fail, API timing drift warns.
It also retries rate limits / 5xx with backoff and retries the push when main moved.
"""
import copy
import io
import json
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import data_checks  # noqa: E402
import risers_core as core  # noqa: E402
import update_stars  # noqa: E402
import verify  # noqa: E402

WF = (ROOT / ".github/workflows/daily-update.yml").read_text("utf-8")


def growth(gained=10, days_=(7, 30, 365)):
    return {k: {"window_days": d, "gained": gained, "effective_days": d, "per_day": gained / d, "young": False}
            for k, d in zip(("week", "month", "year"), days_)}


def project(name, stars=1000, total=None, **kw):
    p = {"name": name, "ok": True, "stars": stars, "growth": growth(), "history_complete": True,
         "history_total": stars if total is None else total}
    p.update(kw)
    return p


def world(rows):
    stats = {"today_utc": "2026-11-01", "projects": rows}
    projects = [{"name": r["name"]} for r in rows]
    snaps = {r["name"]: {"2026-11-01": r.get("stars")} for r in rows if r.get("ok")}
    return stats, projects, snaps


class DataCheckTests(unittest.TestCase):
    def check(self, rows):
        return data_checks.check(*world(rows))

    def test_clean_data_has_no_errors_or_warnings(self):
        self.assertEqual(self.check([project("a/a"), project("b/b")]), ([], []))

    def test_small_history_drift_warns_but_never_fails(self):
        for drift in (3, 5, 9, 40):  # run 41235403615: affaan-m/ECC was off by 3
            errors, warnings = self.check([project("a/a", total=1000 - drift) if drift > 5
                                           else project("a/a", total=1000 + drift)])
            self.assertEqual(errors, [], drift)
            self.assertEqual(bool(warnings), drift > core.HISTORY_TOTAL_STAR_SLACK, drift)

    def test_drift_inside_slack_is_silent(self):
        self.assertEqual(self.check([project("a/a", total=1003)]), ([], []))

    def test_large_history_gap_is_a_real_error(self):
        errors, _ = self.check([project("a/a", stars=1000, total=800)])
        self.assertTrue(any("history_total 800" in e for e in errors))
        big = project("b/b", stars=400000, total=400000 - 3000)  # 1 % of 400k is 4000: still a warning
        self.assertEqual(self.check([big])[0], [])
        big = project("b/b", stars=400000, total=400000 - 5000)
        self.assertTrue(self.check([big])[0])

    def test_hard_limit_floor_and_share(self):
        self.assertEqual(core.history_total_hard_limit(1000), 50)
        self.assertEqual(core.history_total_hard_limit(400000), 4000)

    def test_real_data_errors_still_fail(self):
        bad = project("a/a")
        bad["growth"]["week"]["gained"] = -1
        self.assertTrue(self.check([bad])[0])
        bad = project("a/a")
        bad["growth"]["month"]["per_day"] = 99
        self.assertTrue(self.check([bad])[0])
        bad = project("a/a")
        del bad["growth"]["year"]
        self.assertTrue(self.check([bad])[0])
        stats, projects, snaps = world([project("a/a")])
        snaps["a/a"] = {}
        self.assertTrue(data_checks.check(stats, projects, snaps)[0])  # no snapshot for today
        stats, projects, snaps = world([project("a/a")])
        self.assertTrue(data_checks.check(stats, projects + [{"name": "x/x"}], snaps)[0])  # project list mismatch

    def test_one_missing_repo_warns_an_outage_fails(self):
        gone = {"name": "c/c", "ok": False, "error": "HTTP 404: Not Found"}
        errors, warnings = self.check([project("a/a"), project("b/b"), project("d/d"), project("e/e"), gone])
        self.assertEqual(errors, [])
        self.assertTrue(any("c/c" in w for w in warnings))
        rows = [project("a/a")] + [dict(gone, name=f"m/{i}") for i in range(3)]  # 75 % missing: rate limit / outage
        self.assertTrue(any("outage" in e for e in self.check(rows)[0]))
        self.assertTrue(self.check([{"name": "c/c", "ok": False}, project("a/a"), project("b/b"), project("d/d"),
                                    project("e/e")])[0])  # missing without an error message

    def test_committed_data_passes(self):
        self.assertEqual(data_checks.main(ROOT), 0)

    def test_main_prints_actions_annotations(self):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch("sys.stdout", out), mock.patch("sys.stderr", err):
            self.assertEqual(data_checks.main(ROOT), 0)
        self.assertIn("data check passed", out.getvalue())


class VerifyModeTests(unittest.TestCase):
    def joined(self, daily):
        cmds = verify.commands(ROOT, daily=daily)
        for c in cmds:
            self.assertEqual(c[0], sys.executable)
        return [" ".join(c[1:]) for c in cmds]

    def test_default_runs_the_unit_tests(self):
        j = self.joined(False)
        self.assertTrue(any("unittest discover" in x for x in j))
        self.assertFalse(any("data_checks" in x for x in j))

    def test_daily_runs_data_checks_not_the_unit_tests(self):
        j = self.joined(True)
        self.assertFalse(any("unittest" in x for x in j))
        self.assertTrue(any("tools/data_checks.py" in x for x in j))
        self.assertTrue(any("render_readme.py --check" in x for x in j))

    def test_daily_flag_reaches_commands(self):
        with mock.patch.object(verify, "commands", return_value=[]) as c:
            self.assertEqual(verify.main(["--daily"]), 0)
            self.assertTrue(c.call_args.kwargs["daily"])
            verify.main([])
            self.assertFalse(c.call_args.kwargs["daily"])


class WorkflowRobustnessTests(unittest.TestCase):
    def test_scheduled_paths_verify_data_not_live_unit_tests(self):
        self.assertIn("tools/verify.py --daily", WF)
        self.assertNotIn("run: python3 tools/verify.py\n", WF)
        sh = (ROOT / "tools/local_daily.sh").read_text("utf-8")
        self.assertIn('"$PY" tools/verify.py --daily', sh)
        ci = (ROOT / ".github/workflows/ci.yml").read_text("utf-8")
        self.assertIn("python3 tools/verify.py\n", ci)  # CI still runs every unit test
        self.assertNotIn("--daily", ci)

    def test_runs_never_overlap_and_are_not_cancelled(self):
        self.assertIn("group: daily-update", WF)
        self.assertIn("cancel-in-progress: false", WF)

    def test_push_retries_after_rebasing_onto_main(self):
        self.assertIn("for attempt in 1 2 3 4 5", WF)
        self.assertIn("git pull --rebase origin main", WF)
        self.assertLess(WF.index("git commit"), WF.index("git pull --rebase"))


class RetryTests(unittest.TestCase):
    def http_error(self, code, headers=None):
        return urllib.error.HTTPError("https://api.github.com/x", code, "err", headers or {}, io.BytesIO(b"{}"))

    def test_retry_wait_policy(self):
        self.assertEqual(update_stars.retry_wait(503, {}, 0), 2)
        self.assertEqual(update_stars.retry_wait(502, {}, 2), 8)
        self.assertEqual(update_stars.retry_wait(429, {}, 0), 2)
        self.assertEqual(update_stars.retry_wait(403, {"Retry-After": "10"}, 0), 11)
        self.assertEqual(update_stars.retry_wait(403, {"Retry-After": "9999"}, 0), update_stars.MAX_WAIT)
        with mock.patch("time.time", return_value=1000):
            h = {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1030"}
            self.assertEqual(update_stars.retry_wait(403, h, 0), 31)
        self.assertIsNone(update_stars.retry_wait(403, {}, 0))  # plain forbidden is final
        self.assertIsNone(update_stars.retry_wait(404, {}, 0))
        self.assertIsNone(update_stars.retry_wait(422, {}, 0))

    def test_api_get_waits_out_a_rate_limit_then_succeeds(self):
        ok = mock.MagicMock()
        ok.__enter__.return_value.read.return_value = b'{"stargazers_count": 7}'
        calls = [self.http_error(403, {"Retry-After": "3"}), self.http_error(503), ok]
        with mock.patch("urllib.request.urlopen", side_effect=calls), mock.patch("time.sleep") as sleep:
            self.assertEqual(update_stars.api_get("/repos/a/b", "t"), {"stargazers_count": 7})
        self.assertEqual([c.args[0] for c in sleep.call_args_list], [4, 4])

    def test_api_get_gives_up_on_final_errors_without_sleeping(self):
        with mock.patch("urllib.request.urlopen", side_effect=self.http_error(404)), mock.patch("time.sleep") as sleep:
            with self.assertRaises(update_stars.GitHubError) as cm:
                update_stars.api_get("/repos/a/gone", "t")
        self.assertEqual(cm.exception.status, 404)
        sleep.assert_not_called()

    def test_api_get_retries_network_errors_then_raises(self):
        err = urllib.error.URLError("boom")
        with mock.patch("urllib.request.urlopen", side_effect=err) as u, mock.patch("time.sleep"):
            with self.assertRaises(update_stars.GitHubError):
                update_stars.api_get("/x", "t", retries=3)
        self.assertEqual(u.call_count, 3)


if __name__ == "__main__":
    unittest.main()
