# HANDOFF

## Current Status

- Status: mechanic-first activity concept adaptation workflow with explicit asset dependency layer, run provenance layer, existing-package enrichment pass, and skip-and-continue blocker handling implemented in authoring docs
- Date: 2026-05-10
- Workspace: `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign`

## Latest Changes

- Added `program.md` Phase 0 for Activity Concept Adaptation Briefs.
- Made `activity_signature.mechanic` the primary activity-intent signal; pillar and `game_style` remain required scaffold metadata.
- Documented formal assignment types: `entity_activity`, `activity_concept`, `match_pattern`, and `capability_probe`.
- Documented three input modes: `mapping_informed`, `parameterized`, and `concept_only`.
- Clarified that entity mapping YAML is useful for grounding and matchability, but not mandatory for concept-only or parameterized briefs.
- Added mechanic adapters to `templates.md` so Template 0 composes as mechanic-first before category and pillar/style scaffolding.
- Updated `run.md` to block unsupported assignments at `blocked_until_product_decision` instead of forcing package generation.
- Marked `transform.md` and `transform_run.md` as legacy-only and not applicable to activity concept adaptation.
- Updated `README.md` to reflect concept-led assignment shape, adaptation brief behavior, and the detailed input data source model.
- Added the Activity Concept Brief + Asset Requirements source shape so concept owners and curriculum authors can declare visual assets, generation timing, use steps, prompts, display behavior, and fallbacks explicitly.
- Added `asset_policy` values: `no_assets`, `optional_support`, `required_prebuilt`, `runtime_generated`, and `blocked`.
- Wired `adaptation_brief.asset_dependency` through `program.md`, `run.md`, `GOAL.md`, `assignments.md`, `templates.md`, `activities/README.md`, `docs/activity_tag_block_usage.md`, and the examples.
- Documented that package generation writes asset briefs and direct English image prompts, but does not generate or store image files.
- Defined `MAPPING_ROOT=data/mappings_dev20_0318` across the current authoring docs so future mapping-path moves have a named setting to update.
- Added `examples/` with concrete examples for each input data source and Phase 0 input mode.
- Added `GOAL.md` as the Codex `/goal` objective and success criteria contract.
- Synced `docs/activity_vocabulary.md`, `docs/game_styles.md`, `entity_guidance.md`, and `conversation_bridge.md` to the assignment-type / `concept_only` / mechanic-first workflow.
- Added `runs/README.md` and documented per-run provenance directories under `runs/<run_id>/`.
- Updated `run.md` so each autonomous loop creates a run manifest, assignment snapshot, generated activity index, adaptation brief directory, blocked brief directory, and review notes before processing assignments.
- Updated `program.md`, `README.md`, and `GOAL.md` so generated packages remain under `activities/<activity_id>/` while run-level provenance lives under `runs/<run_id>/`.
- Added `docs/plans/2026-05-09-run-provenance-layer.md` as the design decision record for the run layer.
- Added `assignments.md` Batch 4 with selected typical source concepts from the local concept workbook, including ready concepts and capability probes.
- Added `examples/source_activity_concept_briefs.md` with companion source concept rows and English asset prompts for Batch 4.
- Documented `concept_source=file#id` and `asset_requirements=file#id` loading in `run.md`, `program.md`, `README.md`, `GOAL.md`, and `assignments.md`.
- Replaced direct source-team naming with neutral source-concept terminology and documented the English-only generated-output contract.
- Renamed Batch 4 activity IDs, concept source anchors, and companion file references away from direct source-team shorthand.
- Normalized Batch 4 assignment rows and source concept briefs to English so generated briefs and packages do not inherit Chinese source prose.
- Added `examples/source_activity_concept_template.md` as a blank fillable source-concept and asset-requirements template.
- Updated `README.md` and `examples/README.md` to point concept owners to the fillable template.
- Expanded the canonical `activity_signature.mechanic` enum from 10 to 12 values across `docs/activity_vocabulary.md`, `activities/_schema/tag_block.schema.json`, `program.md`, `templates.md`, `README.md`, examples, assignments, and migrated activity metadata.
- Retired `voice` in favor of `motion_voice`, retired `narrate` in favor of `imagine`, and added `decide` plus `remember`.
- Tightened the migrated package depth floor in `program.md`, `run.md`, `templates.md`, `GOAL.md`, and `activities/README.md`: compact five-file packages are allowed, but thin/generic `spec.md` or `prod.md` files should fail review.
- Added explicit standards that Steps 1, 2, 4, and 5 need executable dialogue/screen detail, Step 3 rounds must be distinct, magic moments must be earned by the child action, and reviewers should fail structurally valid but under-detailed packages.
- Re-ran the `/goal` loop as `runs/20260509_230616_activity_concepts`; current unchecked queue starts with Coloring Game, which blocked at Phase 0.
- Added `runs/20260509_230616_activity_concepts/blocked_briefs/001_coloring_game.yaml`; no package, `results.tsv` row, generated ID, or assignment checkoff was created for the blocked probe.
- Enriched all existing generated `activities/concept_*` packages to reflect the tightened depth floor: each `spec.md` now includes package-specific `## Runtime Detail Floor Notes`, and each `prod.md` overview has richer design-highlight / typical-scenario detail tied to progress, branch handling, and earned payoff.
- Updated the `/goal` command and success criteria so future runs audit checked-row existing `activities/<activity_id>/` packages before processing unchecked assignments.
- Added `run.md` Existing Package Enrichment Pass, including audit scope, allowed in-place enrichment, `results.tsv` non-logging rule, and `outputs.enriched_activities` run-manifest provenance.
- Updated `program.md` v1.14, `templates.md` v1.7, and `runs/README.md` to make enrichment mode part of the canonical package workflow.
- Updated `program.md` v1.15 to make blocked assignment handling non-terminal for the batch.
- Updated blocker handling in `GOAL.md`, `run.md`, `program.md`, `README.md`, `runs/README.md`, and `assignments.md`: product/design blockers now write blocked briefs, remain unchecked, and the run continues to later unchecked rows. Only hard workflow failures stop the batch.

## Verification

- `git diff --check`
  - Result: clean
- Targeted detail-floor diff review across `program.md`, `run.md`, `templates.md`, `GOAL.md`, `activities/README.md`, and `HANDOFF.md`
  - Result: migrated package generation now explicitly rejects thin/generic packages even when schema and structure are valid
- Current-run blocked-state audit for `runs/20260509_230616_activity_concepts`
  - Result: manifest status is `blocked`, `pending_at_start=2`, `generated_count=0`, `blocked_count=1`; Coloring Game remains unchecked, absent from `results.tsv`, absent from `generated_activity_ids.txt`, and has no activity package directory
- Completion audit evidence check for the active `/goal` run
  - Result: generation-ready rows are checked and have structurally valid packages; the first currently unchecked row is Coloring Game; that historical run stopped at its blocked Phase 0 brief under the previous terminal-blocker rule
- Concept package enrichment invariant check
  - Result: all seven `activities/concept_*` packages have exactly five files, matching tag/dashboard focal attributes, correct scorecard placement, no raw prompts in `prod.md`, no condensed-round placeholders, and `## Runtime Detail Floor Notes` in `spec.md`
- Migrated package tag-block schema validation after concept package enrichment
  - Result: all `activities/*/tag_block.yaml` files validate
- Targeted enrichment workflow scan across `GOAL.md`, `run.md`, `program.md`, `templates.md`, `runs/README.md`, and `HANDOFF.md`
  - Result: existing-package enrichment is now documented as a pre-loop `/goal` pass with provenance and no duplicate `results.tsv` logging
- Targeted blocker-handling scan across `GOAL.md`, `run.md`, `program.md`, `README.md`, `runs/README.md`, `assignments.md`, and `HANDOFF.md`
  - Result: product/design blockers are documented as per-row blocked briefs that do not halt later unchecked rows; `completed_with_blockers` is documented as the run status when blockers remain
- Targeted run-layer scan across `README.md`, `GOAL.md`, `program.md`, `run.md`, `runs/README.md`, `docs/plans/2026-05-09-run-provenance-layer.md`, and `HANDOFF.md`
  - Result: expected `runs/<run_id>`, `run_manifest`, `assignment_snapshot`, `generated_activity_ids`, `adaptation_briefs`, and `blocked_briefs` references are present
- Targeted source concept batch scan across `assignments.md`, `examples/source_activity_concept_briefs.md`, `run.md`, `program.md`, `README.md`, and `GOAL.md`
  - Result: `concept_source=file#id`, Batch 4 assignment rows, selected source concept IDs, and referenced asset IDs are present
- Assignment reference validation for unchecked rows
  - Result: 15 `concept_source` / `asset_requirements` file anchors checked; all referenced sections found
- Direct source-team naming scan across the repo
  - Result: no direct shorthand source-team terms remain
- English-only generation source scan across active assignment/example/generator docs
  - Result: no Chinese text remains in `assignments.md`, active source concept examples, `README.md`, `program.md`, `run.md`, `GOAL.md`, or `templates.md`
- Template reference scan
  - Result: `examples/source_activity_concept_template.md` is referenced from `README.md` and `examples/README.md`
- Mechanic enum drift check between `docs/activity_vocabulary.md` and `activities/_schema/tag_block.schema.json`
  - Result: the 12 mechanic tokens match exactly
- Migrated package tag-block schema validation
  - Result: all five migrated `activities/*/tag_block.yaml` files validate, including the `motion_voice` migration for `voice_stage_lion`
- Assignment/example mechanic validation
  - Result: checked 35 assignment, source-brief, and example mechanic values; all use the current enum
- Retired mechanic token scan
  - Result: no active assignment or tag-block use of retired `voice` / `narrate` mechanic values remains; old 10-value enum snippets are absent outside explicit migration notes
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
- Legacy naming scan for retired concept-source terms
  - Result: retired direct source-team terms are absent from active docs
- Targeted sync scan for `docs/activity_vocabulary.md`, `docs/game_styles.md`, `entity_guidance.md`, and `conversation_bridge.md`
  - Result: new assignment-type, input-mode, `MAPPING_ROOT`, and mechanic-first references are present; retired source-lightweight terms are absent
- Targeted asset-layer scan across active workflow docs and examples
  - Result: `asset_policy`, `asset_dependency`, `Asset Brief`, `prompt_en`, and asset requirement examples are present in the generation contract; stale `prompt_zh` references are absent
- Targeted diff review of the changed docs
  - Result: changes are limited to the mechanic-first activity concept adaptation workflow, run provenance layer, and related documentation state

## Residual Risk

- The existing `results.tsv` header predates the migrated package loop and is not changed in this pass.
- `d10_pillar_fidelity` remains the documented log column name for compatibility, but it now records Dimension 10 Mechanic Fidelity + Scaffold Honesty.
- Mechanic enum changes require matching updates in downstream consumer enum mirrors before new packages using `decide`, `remember`, `imagine`, or `motion_voice` can be consumed safely.
- Asset requirements are authoring-only in this pass; no runtime asset manifest file or tag-block schema field was added.
- Runtime image generation remains blocked unless a future product decision declares support.
- Run manifests are maintained by the agent workflow in this pass; there is no schema validator for `runs/<run_id>/run_manifest.yaml` yet, including the new enrichment audit/no-op/enriched counters and `enriched_activities` entries.
- Existing `activities/concept_*` packages now have a first enrichment pass, but they have not received a fresh independent reviewer pass after those editorial additions.

## Next Immediate Actions

- Review the Activity Concept Brief + Asset Requirements fields with concept owners and curriculum authors.
- For new concept rows, ask concept owners and curriculum authors to provide `asset_policy` and companion asset rows when they want AI pre-made images or screen-displayed visuals.
- On the next `/goal` run, confirm the generated `runs/<run_id>/run_manifest.yaml` enrichment fields are sufficient before adding a formal schema.
- Decide whether to run a fresh independent review pass on the enriched `activities/concept_*` packages before treating the enrichment as final curriculum signoff.
