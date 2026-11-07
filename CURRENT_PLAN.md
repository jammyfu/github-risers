# CURRENT_PLAN.md

## Plan ID

PLAN-007

## Goal

Complete every missing detailed translation and one-line hook in the current ranking across all five languages, while preserving existing translations and all API-derived data.

## In Scope

- Current-source entries in `data/translation_library.json`
- Generated README and details pages via `tools/render_readme.py`
- Completeness, terminology, existing-entry preservation and publication checks

## Out of Scope

- Star data, ranking order, historical snapshot data, source descriptions, existing translations, model configuration, unrelated copy or automation redesign

## Tasks

- [x] Audit repository requirements, current source hashes and missing language/hook fields
- [x] Fill the missing detailed translations and short hooks using the glossary and existing guards
- [x] Independently review all new wording and prove no old translated field changed
- [x] Regenerate pages and verify zero translation/hook gaps across all current categories
- [ ] Publish the completed content and verify CI and Pages on the resulting commit

## Verification

- `python3 tools/i18n_pipeline.py --translate --hooks --dry-run`
- `python3 tools/newcomer_i18n.py --strict`
- `python3 tools/verify.py`
- `python3 tools/verify.py --daily`
- `python3 tools/next_plan.py --check`
- Compare all previously stored translation fields and API data with the base commit

## Next Candidates

- Observe the next unattended scheduled update and same-day duplicate suppression
- Consider making the operator completeness check cover hooks as well as translations without blocking raw-data refreshes
- Thin newcomer boards and the acceleration column remain in `TODO_BACKLOG.md`
