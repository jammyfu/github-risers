# DECISIONS.md

## 2026-10-29

### Use `stargazers/history`, not `stargazers` + `starred_at`

- The stargazers list is restricted to admins/collaborators since July 2026 and returns 404 for these repos.
- `stargazers/history` returns daily counts per week without identities; the full history is checked against `stargazers_count` with slack `HISTORY_TOTAL_STAR_SLACK` (5). It is not required to match exactly: GitHub buckets can lag the live count (un-stars, same-day stars, week boundaries). Slack was 2 until run 41235403615 (2026-11-01), when `affaan-m/ECC` was off by 3 and Verify blocked the data push.

### Window definition

- Gain = sum of the N complete UTC days before today (today excluded), N = 7, 30, 365. Stars/day = gain / N.
- For repos younger than N days, divide by repo age (days since `created_at`, min 1) and flag with †.

### Drop `stars_note`

- The free-text notes ("recently very fast", "always near the top") were not verifiable from API data and were removed. Rankings show measured numbers only.

### Generated files

- `README*.md` and `data/stats.json` are generated; `tests/test_repo.py` fails if READMEs are stale.

## 2026-10-30

### Two LA crons plus a time-zone guard

- GitHub cron is UTC-only and LA midnight moves between 07:00 and 08:00 UTC with DST, so both are scheduled and `tools/schedule_guard.py` lets exactly one pass.

### Top 20 per ranking, 20+ tracked projects

- New projects follow the existing topic line (fast-rising AI agent / coding-agent related repos), chosen by measured 7-day growth from the API, not by total stars.

### History snapshots are real runs only

- A snapshot folder is written only by an actual run at that slot. Past slots are not back-filled, because the star count at that moment cannot be recovered from the API.

### New arrivals: hotness and dedup

- Hotness = stars / max(age days, 1); descriptions are the repo's own GitHub text (not translated).
- Dedup excludes tracked projects and all displayed top-20 repos, so no project is in two rankings; a repo must be added to `data/projects.json` by the owner to be tracked.

## 2026-10-30 (categories)

### Newcomers are found by topic only

- Keyword and language searches pulled in unrelated and star-farmed repos. A repo must carry one of the category's topics; generic topics are not used.

### Suspected cracked / pirated repos: keep, flag, rank last

- Owner decision: do not exclude them. They are marked ⚠, always rank after every normal repo and never lead a category or the leaders table. Rules in `tools/spam.py`, documented in `docs/CATEGORIES.md`.

### One code path for every scheduled run

- Beijing cron, both Los Angeles crons, `workflow_dispatch` and the local launchd jobs all end in `tools/update_stars.py --slot <slot>`, so the rules above apply to every run.

## 2026-10-30 (CoderSkills harness)

### Follow `continuous-project-loop` and `multi-project-program-management`; other CoderSkills skills do not apply

- Applied: standard file set, one plan entry, record order, verify hardening rule, dirty-worktree rule written into repo files, planning rules (one Goal, 3-7 tasks, Out of Scope, Next Candidates).
- Not adopted: `sync_or_queue.py` / LaunchAgent safe-sync tooling (this repo changes through pull requests; the only automated writer is the daily job), `docs/architecture/*ROADMAP*.md` (not a platform-core project), `git-autosync-signal` (supports only `dramaforge` and `clippipeline`).
- `readme-tech-visualizer`: audit only. The README stays the slim first screen; the header image belongs to the GEO work, so no hero or tech-badge block is generated.

## 2026-11-01

### `history_total` vs `stars` slack is 5, not 2

- The daily-update Verify step (`tests/test_repo.py`) still requires a full history sum to stay close to `stargazers_count`. The allowed absolute delta is now 5 (`tools/risers_core.py::HISTORY_TOTAL_STAR_SLACK`).
- A 3-star gap is accepted; a gap larger than 5 still fails. The check is not removed.

## 2026-11-01 (daily-update root cause)

### The daily run validates data; it does not run the unit tests against live data

- Failures: run 41122642510 (2026-10-30 20:22Z, hook test: new repos without a hook) and run 41235403615 (2026-10-31 19:41Z, `history_total` vs `stars` off by 3). Each fix raised one limit; the next live value would have failed again, and a failed run discards the whole day's update.
- Decision: `tools/verify.py --daily` = compile + `tools/data_checks.py` (hard errors fail, API-timing drift warns) + README freshness. Unit tests stay in CI (`ci.yml`) on every PR. Real data errors still fail.
- Plus: `api_get` retries 429 / rate-limited 403 / 5xx / network errors with capped backoff; the push step rebases and retries.

## 2026-11-01 (README update date)

### Do not bake the update date into the badge URL

- The `updated` badge used to be `img.shields.io/badge/updated-YYYY--MM--DD-…`, which froze the date in the generated README.
- It now reads `$.today_utc` from `data/stats.json` on `main` via shields.io dynamic JSON. When the daily job writes a new `today_utc`, the badge refreshes without anyone editing the README by hand.
- The stamp line still comes from `stats.generated_at` on every `tools/render_readme.py` run (the same path the daily-update workflow uses). Templates in `tools/i18n.py` contain `{ts}` only; no `YYYY-MM-DD` is typed in.
- First-screen FAQ grew by two items (how the numbers are computed; how to use or contribute). They link existing `docs/FAQ.md` anchors; the GEO FAQ file is not generated.

## 2026-11-06

### Once a day at America/Los_Angeles midnight

- Production cadence is one ranking update per day, not Beijing 00:00 plus Los Angeles 00:00.
- GitHub cron is still UTC-only, so both `0 7 * * *` (PDT) and `0 8 * * *` (PST) stay; `tools/schedule_guard.py` lets exactly one through. Historical `cn-0000` snapshots are kept; new scheduled runs write `pt-0000`.
- Public README / FAQ / FACTS / HOW_IT_WORKS copy only says the list is updated daily. Exact clocks stay in `docs/DAILY_UPDATE.md` for operators.


## 2026-11-07 — tolerate delayed GitHub schedules (PLAN-006)

- The target remains Los Angeles midnight with the existing two UTC crons. Use the committed `generated_at` converted to LA's calendar date to decide if a refresh is due, rather than the runner's current hour.
- Any successfully committed refresh on that LA date suppresses scheduled duplicates, including manual refreshes. Manual dispatch remains unconditional; local hour-gated fallback is unchanged.
- Keep workflow concurrency and fresh `main` checkout. Invalid/future state fails visibly; only exit 1 means an intentional skip. Do not backfill missed snapshots with today's numbers.
- The immediate refresh used the existing production workflow. The owner subsequently authorized merging PR #19 and correcting the stale Pages schedule copy. Public English and Simplified Chinese copy says daily without exact clock claims; visible text and structured metadata stay aligned.


## 2026-11-07 — translation completion is separate from data freshness

- A successful API refresh or permissive daily verification is not evidence that translation is complete. Completion requires zero missing detailed-description and hook languages across every current category, plus a source-language audit for English output.
- Translation-library edits fill missing fields under the exact source hash; existing translated text and original descriptions stay unchanged. Public tables use short hooks and details pages retain complete introductions.
- The existing CJK-only English-gap detector can miss Turkish/Vietnamese sources. Their missing English translations are filled explicitly in this round without changing the model configuration or weakening validators.
