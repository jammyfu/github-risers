# CURRENT_PLAN.md

## Plan ID

PLAN-003

## Goal

Polish the generated README first screen and stop baking an update date into the badge URL; the date must come from `data/stats.json` and refresh on every daily-update run.

## In Scope

- `tools/render_readme.py` and `tools/i18n.py` (README / HOW_IT_WORKS / DETAILS copy)
- Regenerated `README*.md` (and the other generated pages the renderer writes)
- Tests that the update badge is dynamic and the stamp text is filled from `stats.json`
- Concise first-screen copy: what the list is, the Actions schedule, how numbers are computed, how to use or contribute, links

## Out of Scope

- Ranking logic, categories, the ⚠ suspected-crack rules, `data/stats.json` numbers
- Secrets, the daily-update cron times, GEO files (`docs/FAQ.md`, `docs/FACTS.md`, `CITATION.cff`, social preview)
- Merging to `main`

## Tasks

- [x] Replace the static `updated-YYYY--MM--DD` shields badge with a dynamic badge that reads `today_utc` from `data/stats.json`
- [x] Keep the stamp line filled from `stats.generated_at` on every `render_readme` / daily-update run
- [x] Add two first-screen FAQ items (how numbers are computed; how to use or contribute) linking existing `docs/FAQ.md` anchors
- [x] Add a test that templates contain no hard-coded update date and that the rendered stamp follows `generated_at`
- [ ] Owner reviews the PR; merge only with approval

## Verification

- `python3 tools/verify.py`
- `python3 tools/next_plan.py --check`

## Next Candidates

- After merge, confirm the next `daily-update` run commits data
- Thin Developer Tools / Design / Data new-repo boards: see `TODO_BACKLOG.md`
- Acceleration column (this week vs the week before)
