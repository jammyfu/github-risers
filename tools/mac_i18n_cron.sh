#!/usr/bin/env bash
# Owner's-Mac job: translate the new-repo descriptions (and write their one-line hooks) that the GitHub Actions
# daily-update could not, because translation needs a signed-in agent CLI and the repo has no CURSOR_API_KEY secret.
# Runs from launchd once a day ~1–2h after the Los Angeles midnight Actions slot
# (Beijing 17:15; see tools/com.jammyfu.risers-i18n.plist).
#
#   tools/mac_i18n_cron.sh            # pull, translate if anything is missing, render, verify, commit, push to main
#   tools/mac_i18n_cron.sh --no-push  # same, but commit locally only
#
# Backend: Antigravity CLI (`agy`, your signed-in session, model I18N_TRANSLATE_MODEL / POLISH_MODEL, default
# gemini-3.8-flash-medium). No key is read, stored or printed. Needs a dedicated clone on main; refuses to run on
# a dirty tree. Only data files are committed. A push rejected because Actions pushed meanwhile is retried:
# the new translations are kept, the generated files are re-rendered on top of the new origin/main.
# Log: ~/Library/Logs/risers-i18n.log (written by launchd).
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

todo() {  # number of ranked new-repo descriptions still needing a translation (hooks ride along, but a hook that
          # keeps breaking the length rule must not wake the agent on every run)
  "$PY" tools/i18n_pipeline.py --translate --dry-run | tail -1 | "$PY" -c \
    'import json,sys; d=json.loads(sys.stdin.read()); print(sum(int(v.get("todo",0)) for v in d.values() if isinstance(v,dict)))'
}

n="$(todo)"
say "missing translations: $n"
if [ "$n" = "0" ]; then say "nothing to do"; exit 0; fi

"$PY" tools/i18n_pipeline.py --translate --hooks
"$PY" tools/render_readme.py >/dev/null
"$PY" tools/verify.py --daily
if [ -z "$(git status --porcelain)" ]; then say "no changes"; exit 0; fi
say "still missing after run: $(todo)"

commit() {
  git add data rankings latest README*.md docs/HOW_IT_WORKS*.md docs/DETAILS*.md
  git commit -q -m "chore(i18n): translate new-repo descriptions $(date +%F)"
}
commit
[ "$PUSH" = 1 ] || { say "committed locally (no push)"; exit 0; }

for attempt in 1 2 3 4 5; do
  if git push -q origin HEAD:main; then say "pushed $(git rev-parse --short HEAD)"; exit 0; fi
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
  commit
  sleep $((attempt * 5))
done
say "error: could not push after 5 attempts"; exit 1
