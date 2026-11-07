# Daily update

Everything the atlas shows comes from the GitHub API (`tools/update_stars.py`). Nothing is estimated; a
project that cannot be fetched is listed under "Missing data" in the README.

## What a run does

1. `GET /repos/{owner}/{repo}` → `stargazers_count`, `created_at`.
2. `GET /repos/{owner}/{repo}/stargazers/history` (newest week first, 30 weeks per page) until one year is covered.
3. Re-discovers the "hottest new repos (last 7 days)" ranking with the GitHub search API (about 30 search requests, paced to the 30/min limit, so a run takes roughly 2 minutes; rules in [NEW_ARRIVALS.md](NEW_ARRIVALS.md)). Every production run (Los Angeles midnight, Actions or local) redoes it from scratch.
4. Writes `data/stats.json` (growth per project), archives it under `rankings/<date>/<slot>/` and `latest/`, appends today's star count to `data/stars.json`
   (snapshots, used for cross-checks over time), then regenerates the five READMEs.

Why `stargazers/history` and not `stargazers` + `starred_at`: since July 2026 GitHub returns 404 for
`GET /repos/{owner}/{repo}/stargazers` unless you are an admin or collaborator of the repo
([changelog](https://github.blog/changelog/2026-06-30-upcoming-access-restrictions-to-public-api-endpoints-and-ui-views/)).
The privacy-safe replacement is `stargazers/history`, which returns daily counts without user identities
([changelog](https://github.blog/changelog/2026-09-04-new-api-endpoint-provides-privacy-safe-star-history-data/)).
Cross-check built into the tests: for every repo whose full history was read,
`|history_total - stargazers_count|` must be ≤ `HISTORY_TOTAL_STAR_SLACK` (5).
GitHub's weekly buckets can lag the live count by a few stars (un-stars, same-day
stars, UTC vs bucket boundaries). Slack was 2 until 2026-11-01, when
`affaan-m/ECC` was off by 3 and the daily push was skipped
(run [41235403615](https://github.com/jammyfu/github-risers/actions/runs/41235403615)).

### One code path for every scheduled run

Both Los Angeles crons (`0 7`/`0 8 * * *`, gated by `tools/schedule_guard.py`),
`workflow_dispatch`, and the local launchd job (`docs/launchd/*.plist` -> `tools/local_daily.sh`) all end in the same
command: `python3 tools/update_stars.py --slot <slot>`. That calls `newcomers.discover_all` -> `newcomers.discover_category`,
so the topic-only category rules, the suspected-crack/pirated ordering (`tools/spam.py`, `newcomers.rank_items`) and the
leader exclusion (`render_readme.leaders`) apply to every run. `tests/test_spam.py::ScheduledPathTests` guards this.

## Where results go: history per time slot

Every run stores its result in its own folder and keeps it (nothing is overwritten except a re-run of the same slot):

```
rankings/<date>/pt-0000/   Los Angeles 00:00 run  (date = America/Los_Angeles date)  ← production
rankings/<date>/cn-0000/   optional Beijing 00:00 run (date = Asia/Shanghai date; kept for history)
rankings/<date>/manual-HHMM/   any other run, e.g. manual dispatch (date/time = UTC)
    stats.json     full API-derived data of that run, plus a "slot" block and the new-repos ranking (`newcomers`)
    rankings.md    top-20 tables for that run, new-repos table first (English, compact)
    rankings.<lang>.md   the same page in zh-Hans, zh-Hant, ja, ko
rankings/README.md   history index linking every snapshot, newest first (README.<lang>.md per language)
latest/stats.json, latest/rankings.md   copy of the newest run (latest/rankings.<lang>.md per language)
data/stats.json      what the READMEs are rendered from (same as the newest run)
```

The five READMEs show the latest ranking and link to the history index and `latest/rankings*.md` of their own language.
The pages are generated from `tools/i18n.py` (strings) and `stats.json` (data); never edit them by hand.
`tools/update_stars.py --slot cn|pt|manual|auto` picks the folder (`auto`, the default, uses pt if it is 00:xx in
Los Angeles, cn if 00:xx in Beijing, otherwise manual). The scheduled workflow always passes `pt`; `tools/local_daily.sh`
passes the slot itself.
`tools/verify.py` checks that `latest/`, the indexes and every snapshot's `rankings*.md` (all languages) match their data.

## New-repo description translations and polish

The new-repos table shows the repo's own GitHub description. `data/translation_library.json` holds its translation
into zh-Hans, zh-Hant, ja and ko (plus en when the source is Chinese), keyed by repo full name + hash of the original
text + language; it is shown only on a hit (the text is unchanged), otherwise the original is shown. Hits cost no model call.

Since the i18n pipeline, `tools/update_stars.py` fills this cache itself: after discovering the ranking it
translates every displayed description that has no current translation (already translated ones are skipped),
then renders. In CI this can use the Cursor CLI and the optional repository secret `CURSOR_API_KEY`; this repo has no
such secret on purpose, so the Actions run skips translation and carries on with the existing texts. The translation is done by the
owner's Mac: a launchd job (`tools/com.jammyfu.risers-i18n.plist`, Beijing 17:15, ~1–2h after the Los Angeles midnight Actions slot) runs
`tools/mac_i18n_cron.sh`, which pulls, translates what is missing with the signed-in Antigravity CLI (`agy`), renders, verifies,
commits `chore(i18n): ...` and pushes to main. Log: `~/Library/Logs/risers-i18n.log`. Polishing the copy is done on the owner's machine with
the Antigravity CLI (`tools/polish_local.sh`, or `tools/local_daily.sh`), never in CI. Details, guards and the manual commands are in
[I18N_PIPELINE.md](I18N_PIPELINE.md). `python3 tools/newcomer_i18n.py` still lists the gaps.

## Schedule: once a day at Los Angeles 00:00

| Slot | When | cron (UTC) |
|---|---|---|
| America/Los_Angeles 00:00, PDT (UTC-7) | 07:00 UTC | `0 7 * * *` |
| America/Los_Angeles 00:00, PST (UTC-8) | 08:00 UTC | `0 8 * * *` |

GitHub cron only knows UTC, so both LA entries fire every day. Actions uses
`tools/schedule_guard.py --tz America/Los_Angeles --daily-state data/stats.json` to compare
`generated_at` in the committed data with the current **Los Angeles calendar date**. If today's
refresh is missing, it runs even hours after midnight. Once a refresh for that date is committed,
the second trigger skips. A manual refresh on the same LA day also counts; manual
`workflow_dispatch` itself always runs when requested.

The `daily-update` concurrency group serializes runs, and each job checks out current `main`
before evaluating the gate. A failed fetch/verify/push does not advance the committed timestamp,
so the next trigger can retry. Missing state permits an initial refresh; corrupt, timezone-less or
future timestamps fail the job instead of appearing as a successful skip. Regression tests execute
the real gate shell with stale/current/invalid state and cover PST, PDT, and both DST transitions.
Local `--slot la` retains its hour-based guard; this change is for delayed GitHub Actions runs.

The cron times are targets, not guaranteed start times. On 2026-11-06 both jobs started roughly
seven hours late and the old hour-only guard skipped all data steps. Delayed runs now use their
actual execution day's `pt-0000` archive slot and record the real `generated_at`; no historical
counts or missed-day snapshots are invented. If GitHub drops both triggers entirely, use
`workflow_dispatch` (or `tools/local_daily.sh`) for a manual refresh.

## Option A: GitHub Actions (preferred when it runs)

`.github/workflows/daily-update.yml` regenerates the data, runs `tools/verify.py --daily`, and commits to `main` if anything changed.
It uses only first-party `actions/*` and the built-in `GITHUB_TOKEN`.

Why `--daily` (root cause of the 2026-10-30 and 2026-10-31 failures): the run used to execute the whole unit-test suite
against the data it had just fetched, so anything that moves with GitHub (a new repo without a hook yet, a 3-star gap between
`/stargazers/history` and `/repos`) failed the run and the day's update was lost. Now the daily run only validates the data
(`tools/data_checks.py`): **errors** fail (project list mismatch, negative or inconsistent growth, no snapshot for today,
history vs stars off by more than `max(50, 1 %)`, more than 25 % of repos fetched as missing) and **warnings** (history vs stars
off by more than `HISTORY_TOTAL_STAR_SLACK`, a few missing repos) show as `::warning::` annotations. The unit tests still run in
`ci.yml` on every pull request. API calls retry 5xx, network errors, `429` and rate-limited `403` with backoff (honouring
`Retry-After` / `X-RateLimit-Reset`, capped at 120 s); the push step rebases onto `main` and retries up to 5 times.
`.github/workflows/ci.yml` runs `tools/verify.py` on every pull request and push to `main` (no network).

Scheduled workflows run from the default branch only.

### Can Actions run for this account? (checked 2026-10-29, re-checked 2026-10-30)

The account has a billing problem, but it only affects private repos:

| Check | Result |
|---|---|
| `gh api repos/jammyfu/github-risers --jq .private` | `false` (public repo; standard hosted runners are free for public repos) |
| `gh api repos/jammyfu/github-risers/actions/permissions` | `{"enabled":true,"allowed_actions":"all"}` |
| Latest run of a **private** repo (`jammyfu/Tallyo`, run 40579601597, 2026-10-27) | failed in 3 s: "The job was not started because recent account payments have failed or your spending limit needs to be increased." |
| Latest run of a **public** repo (`jammyfu/open-game-skills`, run 40870933400, 2026-10-29) | `success`, ran 80 s on a GitHub-hosted runner |

So Actions should work here because the repo is public. If the repo is ever made private, or GitHub starts
blocking public repos too, the daily job will fail with the same payment message. Re-check with:

```bash
gh api repos/jammyfu/github-risers/actions/runs --jq '.workflow_runs[:5][]|[.created_at,.name,.conclusion]|@tsv'
# a payment failure shows up in the job annotation:
gh api repos/jammyfu/github-risers/check-runs/<job_id>/annotations --jq '.[].message'
```

## Option B: local script (always works)

```bash
GITHUB_TOKEN=$(gh auth token) python3 tools/update_stars.py   # fetch + render only
tools/local_daily.sh                  # update, verify (--daily), commit, push to main (any time)
tools/local_daily.sh --no-push        # update, verify, commit locally
tools/local_daily.sh --slot la        # only proceeds if it is 00:xx in America/Los_Angeles (DST-aware)
tools/local_daily.sh --slot beijing   # optional; only proceeds if it is 00:xx in Asia/Shanghai
```

`tools/local_daily.sh` reads `GITHUB_TOKEN` (falls back to `gh auth token`), refuses to run off `main` or
with a dirty tree, and sets its own `PATH` so it works from cron/launchd. The `--slot` check runs first and exits 0
with `skip: ...` without touching anything. `ATLAS_NOW_UTC=2026-10-29T08:30:00Z` overrides the clock for testing.

### cron (Linux / macOS, machine clock in Beijing time)

```cron
0 15,16 * * *   cd /path/to/github-risers && tools/local_daily.sh --slot la      >> /tmp/risers-daily.log 2>&1
```

Los Angeles midnight is 15:00 Beijing time in PDT and 16:00 in PST; the `la` slot fires at both and the guard picks the right one.
If the machine uses another time zone, run the `la` line hourly (`0 * * * *`) and the guard does the rest.
Do not commit a token. Put `GITHUB_TOKEN=...` at the top of the crontab, or leave it unset and rely on `gh auth login`.

### launchd (macOS, machine clock in Beijing time)

One agent: `docs/launchd/com.jammyfu.github-risers.la.plist` (15:00 and 16:00, guarded). Replace `/PATH/TO` with the clone path, then:

```bash
cp docs/launchd/com.jammyfu.github-risers.la.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.jammyfu.github-risers.la.plist
launchctl start com.jammyfu.github-risers.la     # test: prints "skip: ..." unless it is LA midnight
```

It relies on `gh auth login` for the token (launchd has no shell profile).

## Verify

```bash
python3 tools/verify.py
```
