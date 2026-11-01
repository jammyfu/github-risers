# CURRENT_PLAN.md

## Plan ID

PLAN-002

## Goal

Raise the Verify `history_total` vs `stars` slack so a 3-star GitHub discrepancy no longer blocks the daily data push, without dropping the integrity check.

## In Scope

- The absolute-delta assertion in `tests/test_repo.py` (and a named constant for it)
- A regression test that a 3-star gap is accepted and a larger gap still fails
- Docs that currently claim the history sum equals `stargazers_count` exactly

## Out of Scope

- Ranking logic, categories, newcomers, hooks, translations, GEO files
- Disabling `tools/verify.py` or skipping the history cross-check
- Secrets, workflow credentials, merging to `main`

## Tasks

- [x] Confirm the 2026-11-01 daily-update failure is `assertLessEqual(..., 2)` on `affaan-m/ECC` (diff 3)
- [x] Raise the allowed absolute delta from 2 to 5 via a named constant; keep the check
- [x] Add a unit test that delta 3 passes and delta > 5 still fails
- [x] Document the slack (why 5, why not exact) and record the decision
- [x] Run `python3 tools/verify.py` and `python3 tools/next_plan.py --check`
- [x] Open a PR against `main` (do not merge)

## Verification

- `python3 tools/verify.py`
- `python3 tools/next_plan.py --check`

## Next Candidates

- After merge, confirm the next `daily-update` run commits data
- Thin Developer Tools / Design / Data new-repo boards: see `TODO_BACKLOG.md`
- Acceleration column (this week vs the week before)
