# Examples

Concrete examples for the mechanic-first activity concept adaptation workflow.

These files are reference inputs and expected brief shapes. They are not generated activity packages, and they should not be copied into `activities/` directly.

## Files

- `data_sources.md` shows one concrete example for each input data source described in `README.md`, including the Activity Concept Brief + Asset Requirements shape.
- `input_modes.md` shows one concrete Phase 0 example for each input mode: `mapping_informed`, `parameterized`, and `concept_only`, plus an asset-dependent concept-only example.

## How to use

1. Pick the example closest to the activity concept or entity request.
2. Copy the assignment row into `assignments.md`. If the example has asset rows, keep the companion Asset Requirements table/YAML available and reference it with `asset_requirements=...`.
3. Run the package loop from `run.md`.
4. For mapping-informed examples, keep `MAPPING_ROOT/_index.yaml` available and make sure the `mapping=` entity ID exists there.
