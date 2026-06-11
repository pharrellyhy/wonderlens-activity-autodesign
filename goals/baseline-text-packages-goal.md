# Baseline Text Packages Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract for generating the
baseline text-only activity packages for the active assignment queue.

## Objective

Process the active assignment queue in `assignments.md`, produce run-local
text-only activity packages under `runs/<run_id>/activity_packages/`, and
record provenance for review, logging, and handoff. This goal does NOT generate
image assets, run downstream consumer checks, or perform integration validation.
Those phases are separate goals (`text-reviewer-goal.md`,
`asset-curator-goal.md`, `integration-owner-goal.md`) executed per activity
after the baseline exists.

## Run Settings

| Setting | Value | Notes |
|---|---|---|
| `demo_export` | `true` | Generated packages include `demo_support.yaml` and `asset_manifest.yaml`. |
| `asset_build` | `manifest_only` | Write asset manifests with nullable paths; do not create binary image files. |
| `full_pass_pipeline` | `false` | Consumer gates and asset builds are separate goals. |
| `product_contract_override` | `none` | Use `minimum_unblock_allowed` only when explicitly requested. |
| `package_scope` | `run_local` | Fresh packages go under `runs/<run_id>/activity_packages/`. |
| `mapping_root` | `data/mappings_dev20_0318` | Use when `mapping=` is supplied. |

## Source Documents

- `GOAL.md` — root objective and completion contract.
- `run.md` — execution loop.
- `program.md` — authoring contract, adaptation brief, Phase 2 output format, Phase 3 rubric.
- `templates.md` — Template 0 spine, mechanic adapters, category modifiers, pillar overlays.
- `docs/game_styles.md` — game-style taxonomy.
- `activities/README.md`, `activities/_schema/*.schema.json`, `docs/activity_vocabulary.md` — package and enum contracts.
- `entity_guidance.md`, `conversation_bridge.md` — only for mapping-informed rows.
- `inputs/original_activity_concepts_2026-05-29.tsv` — source-intent baseline for workbook rows.

## Hard Constraints

- Set `asset_build=manifest_only`; do not create binary image files.
- Do not run fullstack-demo, WonderLens AI, or any downstream consumer.
- Keep package writing text-only.
- Workbook-derived rows use the TSV as the source-intent baseline.
- Do not accept packages with unresolved `intent_drift`.
- Every generated package must pass the 10-dimension rubric and independent reviewer evidence before acceptance.
- Blocked rows do not produce valid runtime packages; write blocked briefs and constrained design previews.

## Required Scope

Produce:

- Run manifest (`run_manifest.yaml`) and assignment snapshot.
- Pre-package source-intent audits for source-derived rows.
- Adaptation briefs for concept-led or underspecified rows.
- Generated text-only activity packages (5 required files + 2 demo extension files).
- Per-package self-evaluation scorecards and independent reviewer evidence.
- Per-activity review status files at `runs/<run_id>/review_status/<activity_id>.yaml`, copied from `runs/_templates/review_status.yaml`.
- Post-package source-intent audit evidence.
- `generated_activity_ids.txt`, updated `assignments.md` checkboxes, appended `results.tsv` rows.
- Generated `review.html` dashboard and run manifest finalization.

## Mandatory Ordering

1. Confirm docs are present: `GOAL.md`, `run.md`, `program.md`, `templates.md`.
2. Create the run directory and initialize provenance files per `run.md` Setup.
3. For each active assignment row:
   a. Parse the row and load source context.
   b. Write the adaptation brief (Phase 0) when needed.
   c. Run pre-package source-intent audit for source-derived rows.
   d. Load entity mapping when the row is mapping-informed.
   e. Compose the scaffold from `templates.md`.
   f. Write the 5 required files plus `demo_support.yaml` and `asset_manifest.yaml`.
   g. Create `review_status/<activity_id>.yaml` by copying the template.
   h. Run 10-dimension self-evaluation and independent reviewer pass.
   i. Run post-package source-intent audit.
   j. Log accepted packages to `results.tsv`, mark assignment checkbox, update run manifest.
   k. For blocked rows: write blocked brief and constrained design preview, leave unchecked.
4. Generate `review.html` dashboard.
5. Finalize `run_manifest.yaml`.
6. Commit intended run artifacts.

## Required Checks

```bash
run_id="<run_id>"
python3 scripts/validate_demo_package_contract.py runs/${run_id}/activity_packages
python3 -c "
import json, yaml, pathlib
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
for p in sorted(pathlib.Path('runs/${run_id}/activity_packages').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK' if not errs else 'FAIL'), p)
"
rg -c '## Self-Evaluation Scorecard' runs/${run_id}/activity_packages/*/spec.md
rg -c '## Self-Evaluation Scorecard' runs/${run_id}/activity_packages/*/prod.md
ls runs/${run_id}/review_status/
python3 scripts/generate_run_review.py --validate runs/${run_id}
git diff --check
```

## Goal Invocation

```text
/goal Execute goals/baseline-text-packages-goal.md end to end.
```
