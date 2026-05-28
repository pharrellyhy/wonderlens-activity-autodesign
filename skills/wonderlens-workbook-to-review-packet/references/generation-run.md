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
- Preserve source-promise alignment from the workbook row. Treat normalized source snapshots as helpers, not source-of-truth, when they omit workbook sequence, role, real/reference asset requirements, or background/context requirements.
- The child's repeated action must match the canonical mechanic, but the mechanic cannot override the workbook's play frame.
- For runtime AI behavior, prefer `Runtime AI instruction` plus `Example AI line` when the line should be generated dynamically. Use fixed `AI says` only when exact wording is intentionally required.
- Make unexpected and no-response branch policies beat- and round-specific. Do not reuse generic text across activities, do not keyword-substitute the activity title/mechanic/round title into a stock row, and do not repeat the same Step 3 branch policy across rounds. Name the likely off-track or quiet behavior for the current source action and redirect/scaffold back to the current role, challenge, asset/fallback, screen state, prior consequence, or completion target.
- Every generated package must have exactly five files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.
- Do not append `results.tsv` or mark an assignment complete until package validation, self-evaluation, and review have passed.
- Block product-dependent rows only when the product contract does not support them and no minimum acceptable version has been approved.
- If `minimum_unblock_allowed` is active, generate capability-probe rows as normal packages when the reduced version can preserve source intent. Record formerly blocking items as resolved blocker annotations.
- Do not fake unsupported features. Use explicit reduced-scope behavior: voice-only fallback, prebuilt/static assets, child or parent confirmation, process celebration without quality judgment, no motion detection, no live recoloring, no real cleanup verification, and no hidden UI state unless supported.
- Surface minimum-version assumptions in `spec.md`, `prod.md`, `run_manifest.yaml`, `review.html`, and later source comparison.

## Full-Pass Audit Requirement

Every new generation run from a workbook must include a full source-intent audit after package generation and before final completion. Do not rely only on the generation rubric or normalized source text; compare the runtime beats back to the original workbook intent. Every audit entry must include `workbook_evidence`, a short English note naming the workbook detail used to judge the original play frame.

Under `minimum_unblock_allowed`, the audit should not classify a row as `needs_product_decision` merely because it used an approved reduced-scope implementation. Classify it by source-intent fidelity: `aligned`, `minor_adaptation`, or `intent_drift`, unless the minimum version still leaves a real unresolved product question.

Validate workbook audits with `--strict-workbook-intent`.

## Checks

Use the focused checks required by the files touched. Common checks include metadata schema validation, targeted script unit tests when scripts change, `git diff --check`, review dashboard validation, source comparison validation, and export validation.
