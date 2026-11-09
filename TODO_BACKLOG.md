# TODO_BACKLOG.md

## Now

- [x] Verified delayed automatic update and same-day duplicate skip on 2026-11-08 (runs 42487291739 and 42490659376); another real update succeeded on 2026-11-09 (42659639717)
- [ ] Developer Tools new-repo board: 15 of 20 entries were flagged ⚠ in the last run because star-farmed repos use `cli` / `developer-tools`; decide whether to add a quality signal (owner call)
- [ ] Design and Data new-repo boards are thin (0-2 entries): widen with specific topics only (no generic ones; `tests/test_spam.py` guards that)

## Next

- [ ] Add explicit English-output detection for non-English sources beyond CJK; PLAN-009 covers all-category detail/hook gating separately from fail-safe raw-data refresh

- [ ] Acceleration column (stars/day this week vs. previous week) from `data/stars.json` snapshots
- [ ] Add more tracked projects (needs five-language `desc`)

## Later

- [ ] Owner can copy `docs/github-profile-draft.md` into `jammyfu/jammyfu` if they choose to publish it
- [x] Owner set the GitHub About description to daily
- [ ] Candidate discovery for tracked projects with owner approval

## Risks / Blockers

- [ ] GitHub may change or rate-limit `stargazers/history` (documented max 30 weeks/page, page <= 100)
- [ ] If Actions cannot run (billing, quota), use `tools/local_daily.sh`
- [ ] The search API is index-based and can lag by minutes; thin categories can be empty in one run
