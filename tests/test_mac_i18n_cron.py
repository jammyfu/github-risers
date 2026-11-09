"""Run the Mac job in disposable repos with a local remote and a fake model CLI.

The real pipeline/cache and shell control flow run; no network, model, launchd,
owner checkout, or production lock is touched.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import newcomer_i18n as nci  # noqa: E402

LANGS = ("en", "zh-Hans", "zh-Hant", "ja", "ko")
SOURCE = "Does one thing."

FAKE_AGY = r'''
import json, os, subprocess, sys
from pathlib import Path
args = sys.argv[1:]
mode = os.environ.get("TEST_MODE", "success")
if args == ["models"]:
    print("gemini-3.8-flash-medium - Gemini 3.8 Flash (Medium)")
    raise SystemExit(0)
assert args[args.index("--model") + 1] == "gemini-3.8-flash-medium"
prompt = args[args.index("-p") + 1]
stage = "translate" if prompt.startswith("You translate") else "hooks"
items = json.loads(prompt.split("Input items: ", 1)[1].split("\nFor each item", 1)[0])
with open(os.environ["TEST_LOG"], "a") as f:
    f.write(json.dumps({"stage": stage, "items": items}) + "\n")
if mode == "fail":
    raise SystemExit(1)
if os.environ.get("TEST_ADVANCE_REMOTE"):
    subprocess.run(["/usr/bin/git", "-C", os.environ["TEST_ADVANCE_REMOTE"],
                    "push", "-q", "origin", "main"], check=True)
reply = {}
for item in items:
    reply[item["id"]] = {}
    for lang in item["langs"]:
        text = f"[{lang}] {item['src']}" if stage == "translate" else f"hook {lang}"
        if mode == "reject" or (mode == "partial" and stage == "hooks" and lang == "ko"):
            text = "x" * 200
        reply[item["id"]][lang] = text
print(json.dumps({"status": "SUCCESS", "response": json.dumps(reply)}))
'''


class MacI18nCronTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="risers-cron-test-")
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / "repo"
        self.home = self.base / "home"
        self.bin = self.home / ".local/bin"
        self.bin.mkdir(parents=True)
        self.bin.joinpath("python3").symlink_to(sys.executable)
        self.bin.joinpath("agy").write_text(f"#!{sys.executable}\n" + FAKE_AGY)
        self.bin.joinpath("agy").chmod(0o755)
        self.log = self.base / "calls.jsonl"
        self.lock = self.base / "job.lock"
        self.env = {"HOME": str(self.home), "PATH": os.defpath,
                    "AGY_BIN": str(self.bin / "agy"), "TEST_LOG": str(self.log),
                    "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}
        for name in ("tools", "data", "docs", "rankings", "latest"):
            (self.root / name).mkdir(parents=True)
        shutil.copy(ROOT / ".gitignore", self.root / ".gitignore")
        for name in ("i18n_pipeline.py", "llm.py", "newcomer_i18n.py", "hooks.py"):
            shutil.copy(ROOT / "tools" / name, self.root / "tools" / name)
        script = (ROOT / "tools/mac_i18n_cron.sh").read_text()
        script = script.replace("LOCK=/tmp/risers-i18n.lock", f'LOCK="{self.lock}"')
        script = script.replace("/tmp/risers-i18n-mine.json", str(self.base / "mine.json"))
        (self.root / "tools/mac_i18n_cron.sh").write_text(script)
        for name in ("render_readme.py", "verify.py"):
            (self.root / "tools" / name).write_text(
                "import json, os, sys\n"
                "with open(os.environ['TEST_LOG'], 'a') as f:\n"
                "    f.write(json.dumps({'tool': sys.argv}) + '\\n')\n")
        for name in ("README.md", "docs/HOW_IT_WORKS.md", "docs/DETAILS.md",
                     "rankings/.keep", "latest/.keep"):
            (self.root / name).touch()
        self.write_json("data/projects.json", [])
        self.write_json("data/categories.json", [])
        self.write_json("data/stats.json", {"newcomers": {"ok": True, "categories": {
            "ai": {"ok": True, "items": [{"name": "a/one", "description": SOURCE}]}}}})
        self.lib = nci.empty()
        for lang in LANGS[1:]:
            nci.put(self.lib, "a/one", SOURCE, lang, f"stored {lang}")
        for lang in LANGS[:-1]:
            nci.put_hook(self.lib, "a/one", SOURCE, lang, f"stored {lang}")
        self.write_json("data/translation_library.json", self.lib)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("init", "-q", "--bare", str(self.base / "remote.git"))
        self.git("remote", "add", "origin", str(self.base / "remote.git"))
        self.save_fixture()

    def git(self, *args, cwd=None):
        return subprocess.run(["/usr/bin/git", *args], cwd=cwd or self.root, env=self.env,
                              capture_output=True, text=True, check=True, timeout=15).stdout.strip()

    def write_json(self, path, value):
        (self.root / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    def save_fixture(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture", "--allow-empty")
        self.git("push", "-qu", "origin", "main")

    def run_job(self, mode="success", push=False):
        return subprocess.run(["/bin/bash", "tools/mac_i18n_cron.sh", *([] if push else ["--no-push"])],
                              cwd=self.root, env=dict(self.env, TEST_MODE=mode),
                              capture_output=True, text=True, timeout=20)

    def events(self):
        return [json.loads(line) for line in self.log.read_text().splitlines()] if self.log.exists() else []

    def model_calls(self):
        return [event for event in self.events() if "stage" in event]

    def test_hook_only_gap_runs_and_preserves_cached_texts(self):
        before = nci.lookup(self.lib, "a/one", SOURCE)
        run = self.run_job()
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        after = nci.lookup(nci.load(self.root / "data/translation_library.json"), "a/one", SOURCE)
        self.assertEqual(after["hook"].get("ko"), "hook ko")
        self.assertEqual({k: v for k, v in after.items() if k not in ("hook", "seen")},
                         {k: v for k, v in before.items() if k not in ("hook", "seen")})
        self.assertEqual({k: v for k, v in after["hook"].items() if k != "ko"}, before["hook"])
        self.assertEqual(self.model_calls(), [{"stage": "hooks", "items": [
            {"id": "a/one", "src": SOURCE, "langs": ["ko"]}]}])
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertIn("remaining gaps: descriptions=0, hooks=0", run.stdout)
        self.assertFalse(self.lock.exists())
        self.log.unlink()
        again = self.run_job()
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertIn("nothing to do", again.stdout)
        self.assertEqual(self.events(), [])  # no model, render, verify, or new commit for hits

    def test_no_progress_is_incomplete_and_retried_on_next_run(self):
        head = self.git("rev-parse", "HEAD")
        run = self.run_job(mode="fail")
        self.assertEqual(run.returncode, 4, run.stdout + run.stderr)
        self.assertIn("remaining gaps: descriptions=0, hooks=1", run.stdout)
        self.assertIn("incomplete", run.stdout)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertEqual(len(self.model_calls()), 1)
        self.assertFalse(self.lock.exists())
        again = self.run_job()
        self.assertEqual(again.returncode, 0, again.stdout + again.stderr)
        self.assertEqual(len(self.model_calls()), 2)

    def test_partial_results_are_committed_and_pushed_but_not_called_complete(self):
        entry = nci.lookup(self.lib, "a/one", SOURCE)
        del entry["ja"]
        del entry["hook"]["ja"]
        self.write_json("data/translation_library.json", self.lib)
        self.save_fixture()
        run = self.run_job(mode="partial", push=True)
        self.assertEqual(run.returncode, 4, run.stdout + run.stderr)
        self.assertIn("remaining gaps: descriptions=0, hooks=1", run.stdout)
        self.assertIn("incomplete", run.stdout)
        self.assertIn("pushed", run.stdout)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))
        entry = nci.lookup(nci.load(self.root / "data/translation_library.json"), "a/one", SOURCE)
        self.assertEqual(entry["ja"], "[ja] Does one thing.")
        self.assertEqual(entry["hook"]["ja"], "hook ja")
        self.assertNotIn("ko", entry["hook"])

    def test_audit_error_is_not_an_empty_queue(self):
        self.write_json("data/projects.json", None)  # run_safe returns an error object in the real CLI
        self.save_fixture()
        run = self.run_job()
        self.assertNotEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertNotIn("nothing to do", run.stdout)
        self.assertEqual(self.model_calls(), [])

    def test_push_race_rechecks_new_rankings_and_preserves_upstream_hooks(self):
        writer = self.base / "writer"
        self.git("clone", "-q", "-b", "main", str(self.base / "remote.git"), str(writer))
        self.git("config", "user.name", "Other writer", cwd=writer)
        self.git("config", "user.email", "other@example.invalid", cwd=writer)
        self.git("config", "commit.gpgsign", "false", cwd=writer)
        stats = json.loads((writer / "data/stats.json").read_text())
        stats["newcomers"]["categories"]["ai"]["items"].append(
            {"name": "b/two", "description": "Does another thing."})
        (writer / "data/stats.json").write_text(json.dumps(stats) + "\n")
        lib = nci.load(writer / "data/translation_library.json")
        nci.put_hook(lib, "a/one", SOURCE, "ko", "upstream ko")
        nci.save(lib, writer / "data/translation_library.json")
        self.git("add", "data", cwd=writer)
        self.git("commit", "-qm", "new ranking and concurrent hook", cwd=writer)
        self.env["TEST_ADVANCE_REMOTE"] = str(writer)
        run = self.run_job(push=True)
        self.assertEqual(run.returncode, 4, run.stdout + run.stderr)
        self.assertIn("push rejected", run.stdout)
        self.assertIn("remaining gaps: descriptions=1, hooks=1", run.stdout)
        self.assertEqual(len(self.model_calls()), 1)  # no unbounded translation loop after a race
        self.assertEqual(self.git("rev-parse", "HEAD"), self.git("rev-parse", "origin/main"))
        entry = nci.lookup(nci.load(self.root / "data/translation_library.json"), "a/one", SOURCE)
        self.assertEqual(entry["hook"]["ko"], "upstream ko")

    def test_active_lock_prevents_another_writer(self):
        self.lock.mkdir()
        run = self.run_job()
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("another run is active", run.stdout)
        self.assertTrue(self.lock.exists())
        self.assertEqual(self.events(), [])

    def test_dirty_checkout_still_refuses_to_run(self):
        (self.root / "README.md").write_text("uncommitted\n")
        run = self.run_job()
        self.assertEqual(run.returncode, 3, run.stderr)
        self.assertEqual(self.events(), [])
        self.assertFalse(self.lock.exists())


if __name__ == "__main__":
    unittest.main()
