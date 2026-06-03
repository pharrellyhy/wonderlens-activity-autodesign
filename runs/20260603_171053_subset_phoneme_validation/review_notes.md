# Review Notes

Run id: `20260603_171053_subset_phoneme_validation`

## Status

- Completed one assignment: `concept_phoneme_hunt_collect`.
- Package accepted after source-intent audit, package re-review, image QA repair/re-QA, local asset validation, WonderLens AI runtime validation, fullstack demo import/export validation, and runtime-equivalent dialogue QA reports.
- Built 22 runtime assets. Scene/support assets live under `assets/`; picker/object sprites live under `assets/items/`.
- Repaired the phoneme image set away from the earlier basket/blank-card/glow motif toward listening, speaking, searching, and evidence scenes.
- Expanded the consumer-parity picker catalog to four correct `/b/` objects (`ball`, `banana`, `book`, `box`) and eight distractors (`cup`, `sock`, `apple`, `car`, `hat`, `mug`, `shoe`, `spoon`) so fullstack picker catalogs use package assets instead of generic placeholder icons.
- Updated `scripts/repair_full_pass_asset_bundle.py` so the required bundle-repair check keeps phoneme assets focused on sound/action evidence rather than restoring a container metaphor.

## Validation Evidence

- `validate_demo_package_contract.py`: PASS.
- `validate_asset_build_outputs.py`: PASS.
- `validate_asset_granularity.py`: PASS.
- `validate_full_pass_asset_bundle.py`: PASS.
- `test_repair_full_pass_asset_bundle.py`: PASS.
- WonderLens AI runtime generation/check/load: PASS with `downstream_reports/wonderlens_ai/runtime_overrides.yaml`.
- WonderLens AI runtime-equivalent dialogue QA: PASS in `downstream_reports/wonderlens_ai/dialogue_qa_report.json`.
- Fullstack package import parse and placeholder rejection: PASS.
- Fullstack runtime-equivalent dialogue QA content: PASS, but overall report status is `downstream_owned_failure` because required-worktree import/load rejects source-preserving `collection_count=1`.
- WLAI fullstack export placeholder rejection: PASS.
- `generate_run_review.py --validate`: PASS.

## Residual Note

WonderLens AI's generic fullstack exporter does not currently derive collection catalog rows from `asset_manifest.yaml` item roles. This run uses a run-local override for that exporter; the fullstack demo package importer itself consumes the manifest and copies package item assets correctly.

Required fullstack-demo worktree import was attempted from `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`. The source-preserving import fails downstream because `Cat5CreativeSlots.collection_count` requires `>=2`, while the source promise and package require one indoor `/b/` treasure. A diagnostic-only probe with `collection_count=2` loads through `game_loader`, exposes the activity catalog entry, and sees all 22 public assets, confirming the remaining blocker is the downstream minimum-count constraint rather than missing package assets or placeholder routes.
