# Star-farm filter

The "hottest new repos (7 days)" boards are found by GitHub search, so they are the boards a star farm can
reach. On 2026-11-14 the AI and Web boards were flooded by one farm: hundreds of throwaway accounts each
published the same repo, `<account>/ai--manus` ("AI Manus is a general-purpose AI Agent system ..."), all
created within minutes on 2026-11-13, ~270 stars each, 0 forks, owner accounts one month old with 0 followers.
GitHub search returned 547 copies.

Code: `tools/antiabuse.py`. Thresholds: `data/anti_abuse.json` (edit there, not in code).
Tests: `tests/test_antiabuse.py`. Only fields the GitHub API already returns are used
(search, `GET /repos/{r}`, `GET /users/{u}`); nothing is estimated and nothing is sent anywhere.

## Rules

Screened **before** the `GET /repos` refresh budget is spent, so a flood cannot push real repos out:

| Rule | Condition (defaults) | Result |
|---|---|---|
| Blocklist | `blocklist.repos` / `owners` / `names` (regex, full match, case-insensitive) | dropped, on **every** board |
| Clone cluster | same normalized description (>= 24 letters) under >= 2 owners, or same name **and** description under >= 2 owners, or same normalized name under >= 3 owners | every member dropped, except the earliest member whose owner is credible (account >= 365 days and >= 50 followers); none credible -> all dropped |
| Stars nobody forks (extreme) | stars >= 150 and stars / (forks + 1) >= 500 | dropped |

After the refresh (needs `subscribers_count` and the owner account):

| Rule | Condition (defaults) | Result |
|---|---|---|
| Fake watchers | watchers (`subscribers_count`) >= 40 % of stars, stars >= 100 | dropped |
| Fresh throwaway owner + low forks | user account < 60 days old at repo creation, < 5 followers, and stars / (forks + 1) >= 100 | dropped |
| Low forks | stars >= 150 and stars / (forks + 1) >= 100 | ⚠ kept, ranked last, never a leader |
| Fresh throwaway owner | user account < 60 days old at repo creation, < 5 followers | ⚠ kept, ranked last, never a leader |
| Fork farm | forks >= 90 % of stars, stars >= 100 | ⚠ kept, ranked last, never a leader |

- A cluster or a dropped repo seen in one category is dropped from the later categories too.
- Owner lookups are cached and capped (`owner_lookup_budget`, default 150 per run). An owner that cannot be
  read never triggers an owner rule (fail open), and a missing `forks_count` never triggers a fork rule.
- Tracked projects (week / month / year / total boards) are hand-picked in `data/projects.json`; only the
  blocklist applies to them (`blocked` in `stats.json`, never ranked, still fetched).

## Report

Dropped repos never reach a README, `latest/` or a ranking page. Each run records them in
`data/stats.json` (and the history snapshot) under `newcomers.categories.<id>.anti_abuse`:
`dropped_count`, `by_reason`, `clusters` (key, size, owners, kept), `bulk_sample` (20 names from clusters and
the blocklist) and `dropped` (every other dropped repo with its reason, up to 200). `newcomers.anti_abuse` has the run totals and the number of owner lookups. The update log prints the
same summary.

## Calibration

The thresholds were replayed against every new-repo board committed under `rankings/` (408 repos, re-read
from the API on 2026-11-14): 74 repos would have been dropped (38 `ai--manus` copies, 26 repos with ~1,100 or
~300 stars and 0-1 forks, 4 fake-watcher repos, ...), none of them a repo with normal fork / watcher numbers.
8 repos would only be flagged ⚠, see the pull request for the list. Real hot newcomers (for example
`FrigadeHQ/yogurt`, `opencoredev/islandcn`, `alexeyw/lot-map`, `HolyArrs/HolyArrs`) have forks at 5-15 % of
stars and watchers under 10 %, far from every threshold.

To silence a farm by hand, add it to `blocklist` in `data/anti_abuse.json`. To relax a rule, change its
threshold there and run `python3 tools/verify.py`.
