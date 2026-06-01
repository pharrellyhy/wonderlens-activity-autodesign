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
