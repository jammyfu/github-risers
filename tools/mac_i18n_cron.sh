#!/usr/bin/env bash
# Owner's-Mac job: translate the new-repo descriptions (and write their one-line hooks) that the GitHub Actions
# daily-update could not, because translation needs a signed-in agent CLI and the repo has no CURSOR_API_KEY secret.
# The installed launchd job runs every hour at :15, retrying gaps left by earlier runs.
# tools/com.jammyfu.risers-i18n.plist is the older daily 17:15 installation template;
# this script does not change the installed schedule.
#
#   tools/mac_i18n_cron.sh            # pull, translate if anything is missing, render, verify, commit, push to main
#   tools/mac_i18n_cron.sh --no-push  # same, but commit locally only
#
# Backend: Antigravity CLI (`agy`, your signed-in session, model I18N_TRANSLATE_MODEL / POLISH_MODEL, default
# gemini-3.8-flash-medium). No key is read, stored or printed. Needs a dedicated clone on main; refuses to run on
# a dirty tree. Only data files are committed. A push rejected because Actions pushed meanwhile is retried:
# the new translations are kept, the generated files are re-rendered on top of the new origin/main.
# Log: ~/Library/Logs/risers-i18n.log (written by launchd).
# Exit 4 means valid results were kept, but description or hook gaps remain for the next run.
set -euo pipefail
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:${PATH:-}"
cd "$(dirname "$0")/.."

PUSH=1
[ "${1:-}" = "--no-push" ] && PUSH=0
say() { echo "[$(date '+%F %T %Z')] $*"; }

LOCK=/tmp/risers-i18n.lock
if ! mkdir "$LOCK" 2>/dev/null; then
  if [ -n "$(find "$LOCK" -maxdepth 0 -mmin +120 2>/dev/null)" ]; then rm -rf "$LOCK"; mkdir "$LOCK"
  else say "another run is active; exiting"; exit 0; fi
fi
trap 'rm -rf "$LOCK"' EXIT

PY="$(command -v python3)"
export I18N_TRANSLATE_BACKEND=agy I18N_HOOK_BACKEND=agy
export I18N_BUDGET_SEC="${I18N_BUDGET_SEC:-2400}" PYTHONUNBUFFERED=1
LIB=data/translation_library.json

[ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] || { say "error: not on main"; exit 3; }
[ -z "$(git status --porcelain)" ] || { say "error: working tree not clean; refusing to run"; exit 3; }
git pull --ff-only -q
command -v agy >/dev/null || { say "error: agy not installed"; exit 2; }

todo() {  # Count descriptions and hooks separately, using the same cache-aware stages as the real run.
  "$PY" tools/i18n_pipeline.py --translate --hooks --dry-run | tail -1 | "$PY" -c '
import json, sys
d = json.load(sys.stdin)
try:
    counts = [d[stage]["todo"] for stage in ("translate", "hooks")]
    if "error" in d or any(type(n) is not int or n < 0 for n in counts):
        raise ValueError("invalid counts")
except (KeyError, TypeError, ValueError):
    sys.exit("error: could not audit description and hook gaps: " + repr(d))
print(*counts)'
}

counts="$(todo)"
read -r descriptions hooks <<< "$counts"
say "missing gaps: descriptions=$descriptions, hooks=$hooks"
if [ "$descriptions" = 0 ] && [ "$hooks" = 0 ]; then say "nothing to do"; exit 0; fi

report_remaining() {
  counts="$(todo)"
  read -r descriptions hooks <<< "$counts"
  say "remaining gaps: descriptions=$descriptions, hooks=$hooks"
  RESULT=0
  if [ "$descriptions" != 0 ] || [ "$hooks" != 0 ]; then
    say "incomplete: remaining gaps will be retried on the next scheduled run"
    RESULT=4
  fi
}

"$PY" tools/i18n_pipeline.py --translate --hooks
"$PY" tools/render_readme.py >/dev/null
"$PY" tools/verify.py --daily
report_remaining
if [ -z "$(git status --porcelain)" ]; then say "no changes"; exit "$RESULT"; fi

commit() {
  git add data rankings latest README*.md docs/HOW_IT_WORKS*.md docs/DETAILS*.md
  git commit -q -m "chore(i18n): translate new-repo descriptions $(date +%F)"
}
commit
[ "$PUSH" = 1 ] || { say "committed locally (no push)"; exit "$RESULT"; }

for attempt in 1 2 3 4 5; do
  if git push -q origin HEAD:main; then say "pushed $(git rev-parse --short HEAD)"; exit "$RESULT"; fi
  say "push rejected (attempt $attempt); rebuilding on top of origin/main"
  cp "$LIB" /tmp/risers-i18n-mine.json
  git fetch -q origin main
  git reset -q --hard origin/main
  "$PY" - <<'PYEOF'
import json, sys
sys.path.insert(0, "tools")
import newcomer_i18n as nci
mine = json.load(open("/tmp/risers-i18n-mine.json", encoding="utf-8"))
lib = nci.load()
for repo, slots in mine.get("entries", {}).items():
    for h, slot in slots.items():
        dst = lib["entries"].setdefault(repo, {}).setdefault(h, {})
        for k, v in slot.items():
            if k not in dst:
                dst[k] = v
            elif isinstance(v, dict) and isinstance(dst[k], dict):
                for kk, vv in v.items():
                    dst[k].setdefault(kk, vv)
nci.save(lib)
PYEOF
  "$PY" tools/render_readme.py >/dev/null
  "$PY" tools/verify.py --daily
  report_remaining  # origin/main may now rank new repos; recheck without another model loop.
  if [ -n "$(git status --porcelain)" ]; then commit; fi  # another writer may already have filled our gaps
  sleep $((attempt * 5))
done
say "error: could not push after 5 attempts"; exit 1
