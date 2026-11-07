# CURRENT_PLAN.md

## Plan ID

PLAN-008

## Goal

Make the public GitHub first screen easier for visitors to understand, open the live boards, and star the project, while adding a profile README draft and aligning leftover twice-daily public copy.

## In Scope

- Generated README first-screen copy via `tools/i18n.py` and `tools/render_readme.py`
- Folded star-history charts on README boards
- `docs/github-profile-draft.md` unpublished draft for a `jammyfu/jammyfu` profile
- Public cadence wording in `llms.txt`, `docs/llms.txt`, and `CITATION.cff`
- Tests and governance records for those copy changes

## Out of Scope

- Ranking, star-fetch, and workflow logic
- Hand-editing ranking data or history snapshots
- Merging to `main`
- Creating `jammyfu/jammyfu` or changing the GitHub About field by API
- Private repositories, star farming, invented usage or capability claims

## Tasks

- [x] Confirm README vs About cadence: README stays daily without clocks; About is owner-managed and already daily
- [x] First screen: clear value, live-board entry, quick use; fold README star-history charts
- [x] Add `docs/github-profile-draft.md` (Chinese and English; verified public projects only)
- [x] Align leftover public twice-daily wording in `llms.txt` and `CITATION.cff`
- [x] Run `python3 tools/verify.py` and `python3 tools/next_plan.py --check`
- [x] Open an unmerged pull request (https://github.com/jammyfu/github-risers/pull/21; not merged)

## Verification

- `python3 tools/verify.py`
- `python3 tools/next_plan.py --check`

## Next Candidates

- Owner may copy `docs/github-profile-draft.md` into `jammyfu/jammyfu` if they choose to publish it
- Observe the next unattended daily update after any authorized merge
- Do not treat a failed profile-repo fetch as proof that the repository is missing
