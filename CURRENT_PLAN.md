# CURRENT_PLAN.md

## Plan ID

PLAN-005

## Goal

Production ranking updates run once a day at America/Los_Angeles midnight; public README copy only says it updates daily, with no cron clocks or dual Beijing+PT schedule.

## In Scope

- `.github/workflows/daily-update.yml`, `tools/schedule_guard.py` wiring, `docs/launchd/`, `tools/local_daily.sh`, `tools/mac_i18n_cron.sh`, `tools/com.jammyfu.risers-i18n.plist`
- Public copy in `tools/i18n.py` (stamp / a3 / schedule / tagline), `docs/FAQ.md`, `docs/FACTS.md`; operator details in `docs/DAILY_UPDATE.md`
- Tests in `tests/test_schedule.py`, `tests/test_spam.py`, `tests/test_repo.py`; governance files

## Out of Scope

- Ranking logic, star-data fetch, translation pipeline, deleting historical `cn-0000` snapshots, merging to `main`

## Tasks

- [x] Drop the Beijing cron from `daily-update.yml`; keep the two LA UTC crons with `schedule_guard.py`, slot `pt`
- [x] Align local fallback (launchd / cron docs / i18n Mac job) to once daily after US midnight
- [x] Change README / HOW_IT_WORKS strings so readers only see daily update / 每天更新, not clocks
- [x] Update FAQ, FACTS, operator docs and tests that pinned twice-daily / Beijing 00:00
- [x] Re-render generated pages; `python3 tools/verify.py` and `python3 tools/next_plan.py --check` pass
- [x] Open a PR; do not merge

## Verification

- `python3 tools/verify.py`
- `python3 tools/next_plan.py --check`

## Next Candidates

- After merge, confirm the next scheduled `daily-update` run writes `rankings/<date>/pt-0000/`
- Thin Developer Tools / Design / Data new-repo boards: see `TODO_BACKLOG.md`
- Acceleration column (this week vs the week before)
