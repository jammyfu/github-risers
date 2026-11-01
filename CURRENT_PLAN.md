# CURRENT_PLAN.md

## Plan ID

PLAN-004

## Goal

Stop the recurring daily-update failures at the root: the scheduled run must validate the data it generated (hard errors fail, GitHub API timing drift warns) instead of running the unit-test suite against live data, and must survive rate limits and a moving `main`.

## In Scope

- `tools/data_checks.py`, `tools/verify.py --daily`, `.github/workflows/daily-update.yml`, `tools/local_daily.sh`
- `tools/update_stars.py` API retry/backoff, `tools/risers_core.py` hard limit for history drift
- Tests in `tests/test_daily_robustness.py`; docs in `docs/DAILY_UPDATE.md` and governance files

## Out of Scope

- Ranking logic, README copy, cron times, secrets, merging to `main`

## Tasks

- [x] Group the failed runs by cause (41122642510, 41235403615)
- [x] Add `tools/data_checks.py` with error and warning severities and `verify.py --daily`
- [x] Wire the workflow and `local_daily.sh` to `--daily`; unit tests stay in `ci.yml`
- [x] Retry 429 / rate-limited 403 / 5xx / network errors; retry the push after rebasing onto `main`
- [x] Regression tests for all of the above
- [ ] Owner reviews the PR; merge only with approval

## Verification

- `python3 tools/verify.py`
- `python3 tools/verify.py --daily`
- `python3 tools/next_plan.py --check`

## Next Candidates

- After merge, confirm the next scheduled `daily-update` run commits data
- Thin Developer Tools / Design / Data new-repo boards: see `TODO_BACKLOG.md`
- Acceleration column (this week vs the week before)
