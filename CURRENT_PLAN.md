# CURRENT_PLAN.md

## Plan ID

PLAN-006

## Goal

Recover the stale ranking data and let delayed GitHub schedule runs catch up once per Los Angeles calendar day without duplicate refreshes.

## In Scope

- `tools/schedule_guard.py`, `.github/workflows/daily-update.yml`, `tests/test_schedule.py`
- `docs/DAILY_UPDATE.md` and project governance records
- Manual execution and verification of the existing production data workflow

## Out of Scope

- Ranking calculations, generated data edits, translations, cron frequency, local launchd settings, merging to `main`

## Tasks

- [x] Diagnose skipped schedule runs and start the existing manual data update
- [x] Add regression tests for late runs, same-day deduplication, DST, invalid state and workflow error propagation
- [x] Gate scheduled refreshes on the committed data's Los Angeles date, preserving manual dispatch and local-hour mode
- [x] Run full verification and document operator behavior and follow-up
- [x] Verify production refresh run 42373937914 and committed data at `2656f40`
- [ ] Owner reviews the delayed-schedule PR; merge only with approval

## Verification

- `python3 tools/verify.py`
- `python3 tools/verify.py --daily`
- `python3 tools/next_plan.py --check`

## Next Candidates

- After owner-approved merge, verify a delayed scheduled run publishes data and the second trigger skips
- Monitor Pages freshness separately from the data workflow if the bot commit does not trigger deployment
- Thin newcomer boards and acceleration column remain in `TODO_BACKLOG.md`
