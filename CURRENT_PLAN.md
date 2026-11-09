# CURRENT_PLAN.md

## Plan ID

PLAN-009

## Goal

Complete the latest GitHub API ranking in all five languages, including the unresolved short hooks, and make the existing Mac translation job retry hook-only gaps without changing the data-refresh workflow.

## In Scope

- Verify the real 2026-11-09 daily update, snapshots and deployment
- Fill missing exact-source translation-library fields and regenerate public pages
- Complete the previous ranking's 98 unresolved hook-language fields
- Fix and test the Mac job's completeness gate and incomplete-result reporting
- Preserve existing translations, numeric data, historical snapshots, model configuration and task cadence

## Out of Scope

- New ranking or discovery rules, project filtering and hand-edited star numbers
- Re-translating existing details, replacing valid hooks or changing model/backend credentials
- Changing installed launchd configuration or creating duplicate scheduled work

## Tasks

- [x] Verify latest automatic API refresh and measure all-category detail/hook gaps
- [x] Fill current missing detail translations and current/previous missing hooks with semantic review
- [x] Reproduce and fix the hook-only retry gap with isolated regression tests
- [x] Run full verification, daily checks and preservation audits
- [ ] Publish through a pull request and verify exact remote contents, CI and Pages deployment

## Verification

- `python3 tools/verify.py`
- `python3 tools/verify.py --daily`
- `python3 tools/next_plan.py --check`
- All-category exact-source detail and hook audit; all previous missing hooks filled
- Compare numeric data/history and pre-existing library fields with the base commit

## Next Candidates

- Observe the existing hourly Mac job after the authorized publication, without duplicate triggers
- Improve explicit English-language detection for non-CJK sources separately
- Owner decision on developer-tools newcomer quality signals remains outside this round
