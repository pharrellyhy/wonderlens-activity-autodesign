# Review Notes

Run: `20260601_155917_full_pass_agentic_tsv`

## Initialization

This run is the current full-pass agentic TSV execution. The source authority is `inputs/original_activity_concepts_2026-05-29.tsv`; `inputs/source_activity_concepts.md` is a normalized helper only.

The initial package workspace was seeded from `runs/20260521_163621_workbook_review_packet_full/activity_packages` and overlaid with the seven repaired packages from `runs/20260529_172332_source_intent_pilot/activity_packages`. These seed files are draft generated package inputs for the current run. No package is accepted until current-run source-intent, package, asset, fullstack, WonderLens AI, image, repair, and final-review gates pass.

## Known Current Gates

- Demo extension coverage must be repaired for all accepted packages.
- Runtime-facing `prod.md` files must be marker-free before downstream dialogue comparison.
- Prior high-risk source-intent drift rows must be re-audited against the TSV and repaired or recorded as product/downstream decisions.
- Asset build must produce `generated_assets/asset_outputs.yaml`, `reference_sources.yaml`, and `qa_notes.yaml`.
- Fullstack validation must use `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`.
- WonderLens AI validation must generate runtime packages into a local ignored `.artifacts/` path.

## Package Extension Pass - 2026-06-01

Added run-local `demo_support.yaml` and `asset_manifest.yaml` coverage for the package set without generating or editing PNG assets. New manifests use nullable variant paths so `scripts/build_activity_assets.py` can create work items and bind generated files later.

Reference-bound artwork packages still require approved public-domain, licensed, or internal source curation before asset build can succeed: `concept_art_critic_tournament_probe` and `concept_color_famous_art_probe`. Unsupported packages are intentionally gated with `ui_template: none` where the source mechanic depends on unavailable material, movement-safety, coloring, tap-game, word-puzzle, before/after, or tournament runtime capabilities.
