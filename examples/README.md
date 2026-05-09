# Examples

Concrete examples for the mechanic-first activity concept adaptation workflow.

These files are reference inputs and expected brief shapes. They are not generated activity packages, and they should not be copied into `activities/` directly.

## Files

- `data_sources.md` shows one concrete example for each input data source described in `README.md`, including the Activity Concept Brief + Asset Requirements shape.
- `input_modes.md` shows one concrete Phase 0 example for each input mode: `mapping_informed`, `parameterized`, and `concept_only`, plus an asset-dependent concept-only example.
- `source_activity_concept_template.md` is the blank fillable template for source concepts and asset requirements.
- `source_activity_concept_briefs.md` contains selected source-provided concepts and asset requirement rows referenced by `assignments.md` Batch 4.

## How to use

1. For new concept-owner input, ask them to fill `source_activity_concept_template.md` or a copy of it.
2. Pick the example closest to the activity concept or entity request.
3. Copy the assignment row into `assignments.md`. If the example has asset rows, keep the companion Asset Requirements table/YAML available and reference it with `asset_requirements=...`.
4. Run the package loop from `run.md`.
5. For mapping-informed examples, keep `MAPPING_ROOT/_index.yaml` available and make sure the `mapping=` entity ID exists there.
