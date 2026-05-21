# Generation Run

Use this reference for a fresh generation run from workbook-derived assignments.

## Required Reading

Read the current versions of:

- `program.md`;
- `run.md`;
- `templates.md`;
- `docs/game_styles.md`;
- `activities/README.md`;
- `activities/_schema/tag_block.schema.json`;
- `docs/activity_vocabulary.md`;
- `docs/activity_tag_block_usage.md`;
- `docs/activity_tag_block_progression_guide.md`;
- `entity_guidance.md` and `conversation_bridge.md` when mapping or warm/cold bridge behavior applies.

## Run Setup

Follow `run.md` for run directory creation:

```text
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── activity_packages/
├── adaptation_briefs/
├── blocked_briefs/
├── blocked_designs/
├── review_notes.md
└── review.html
```

Use a clean activity ID from the workbook/assignment. Strip copied `_rYYYYMMDD_HHMMSS` suffixes from base IDs.

## Generation Rules

- Run Phase 0 adaptation before package writing.
- Preserve source-promise alignment from the workbook row.
- The child's repeated action must match the canonical mechanic, but the mechanic cannot override the workbook's play frame.
- For runtime AI behavior, prefer `Runtime AI instruction` plus `Example AI line` when the line should be generated dynamically. Use fixed `AI says` only when exact wording is intentionally required.
- Every generated package must have exactly five files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.
- Do not append `results.tsv` or mark an assignment complete until package validation, self-evaluation, and review have passed.
- Block product-dependent rows when the product contract does not support them. If `minimum_unblock_allowed` is active, record formerly blocking items as resolved blocker annotations.

## Full-Pass Audit Requirement

Every new generation run from a workbook must include a full source-intent audit after package generation and before final completion. Do not rely only on the generation rubric; compare the runtime beats back to the original workbook intent.

## Checks

Use the focused checks required by the files touched. Common checks include metadata schema validation, targeted script unit tests when scripts change, `git diff --check`, review dashboard validation, source comparison validation, and export validation.
