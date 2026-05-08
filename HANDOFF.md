# HANDOFF

## Current Status

- Status: mechanic-first activity concept adaptation workflow implemented in authoring docs
- Date: 2026-05-08
- Workspace: `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign`

## Latest Changes

- Added `program.md` Phase 0 for Activity Concept Adaptation Briefs.
- Made `activity_signature.mechanic` the primary activity-intent signal; pillar and `game_style` remain required scaffold metadata.
- Documented formal assignment types: `entity_activity`, `activity_concept`, `match_pattern`, and `capability_probe`.
- Documented three input modes: `mapping_informed`, `parameterized`, and `concept_only`.
- Clarified that entity mapping YAML is useful for grounding and matchability, but not mandatory for concept-only or parameterized briefs.
- Added mechanic adapters to `templates.md` so Template 0 composes as mechanic-first before category and pillar/style scaffolding.
- Updated `run.md` to stop on `blocked_until_product_decision` instead of forcing package generation.
- Marked `transform.md` and `transform_run.md` as legacy-only and not applicable to activity concept adaptation.
- Updated `README.md` to reflect concept-led assignment shape, adaptation brief behavior, and the detailed input data source model.
- Defined `MAPPING_ROOT=data/mappings_dev20_0318` across the current authoring docs so future mapping-path moves have a named setting to update.
- Added `examples/` with concrete examples for each input data source and Phase 0 input mode.
- Added `GOAL.md` as the Codex `/goal` objective and success criteria contract.
- Synced `docs/activity_vocabulary.md`, `docs/game_styles.md`, `entity_guidance.md`, and `conversation_bridge.md` to the assignment-type / `concept_only` / mechanic-first workflow.

## Verification

- `git diff --check`
  - Result: clean
- Targeted consistency scan across `program.md`, `templates.md`, `run.md`, `transform.md`, `transform_run.md`, `README.md`, and `HANDOFF.md`
  - Result: no stale Dimension 10 rubric name or template-first guidance outside expected historical changelog text and runtime-placeholder warnings
- Targeted README scan for input-source terms: `Input Data Sources`, `assignment_type`, `activity_concept`, `mapping_informed`, `parameterized`, `concept_only`, `product_capabilities`, and `mappings_dev20_0318`
  - Result: expected references present
- Targeted mapping-root scan across active workflow docs and migrated package provenance text
  - Result: load instructions use `MAPPING_ROOT`; remaining literal mapping path references are the root definition and project tree location
- Runtime placeholder scan on touched migrated `prod.md` files
  - Result: no exact forbidden condensed-round placeholders found
- Targeted examples scan for all data-source and mode headings
  - Result: expected example coverage present
- Targeted goal and assignment-type scan across `GOAL.md`, `README.md`, `program.md`, `run.md`, `assignments.md`, and `examples/`
  - Result: `/goal` command, success criteria, `assignment_type`, `activity_concept`, and all four assignment type names are documented
- Legacy naming scan for `pm_idea=`, `PM-lightweight`, `pm_only`, and related old terms
  - Result: `pm_idea=` appears only as a documented legacy alias; old `PM-lightweight` / `pm_only` terms are absent from active docs
- Targeted sync scan for `docs/activity_vocabulary.md`, `docs/game_styles.md`, `entity_guidance.md`, and `conversation_bridge.md`
  - Result: new assignment-type, input-mode, `MAPPING_ROOT`, and mechanic-first references are present; old PM-lightweight terms are absent
- Targeted diff review of the changed docs
  - Result: changes are limited to the mechanic-first activity concept adaptation workflow and related documentation state

## Residual Risk

- The existing `results.tsv` header predates the migrated package loop and is not changed in this pass.
- `d10_pillar_fidelity` remains the documented log column name for compatibility, but it now records Dimension 10 Mechanic Fidelity + Scaffold Honesty.
- No schema enum changes were made; unsupported mechanics still need future schema/template work.

## Next Immediate Actions

- Review the mechanic-first workflow wording with PM / 教研.
- If accepted, use concept rows as `assignment_type=activity_concept, activity_concept=...` assignments and let Phase 0 decide whether to generate, assume, or block.
