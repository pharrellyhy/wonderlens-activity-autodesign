# Entity Parameterized Package Authoring Plan

Date: 2026-06-05

Status: Planned

## Goal

Update WonderLens Activity Auto-Designer so generated and migrated activity
packages explicitly declare whether and how they bind to a discovered entity.

The producer-side contract must support all future valid entity-parameterized
and entity-agnostic activities, including the current twelve runtime-ready
activity set. It must prevent ambiguous packages where the backend has to guess
whether a handoff entity should retarget the activity, act only as a theme, or
be rejected as invalid.

The motivating example is Phoneme Treasure Hunt: if discovery captures or
uploads a cat, a valid generated phoneme hunt package should declare that the
runtime derives the target beginning sound from the handoff entity, so the
downstream WonderLens AI runtime asks for object names starting with `C`, not a
hard-coded `/b/` from the original design.

The consumer/runtime implementation is tracked separately in:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-05-activity-entity-parameterization-runtime.md
```

## Current Evidence

This repo already has package and demo-extension foundations:

- `program.md` requires migrated packages to include `spec.md`, `prod.md`,
  `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.
- Demo-targeted packages may include `demo_support.yaml` and
  `asset_manifest.yaml`.
- `program.md` already requires `demo_support.yaml` to declare explicit
  `entity_bindings` for supported and degraded demo packages.
- `scripts/validate_demo_package_contract.py` validates demo support and asset
  manifests.
- `activities/_schema/tag_block.schema.json` and `docs/activity_vocabulary.md`
  define closed metadata vocabularies consumed by downstream repos.
- Existing runtime/source plans call out that full-pass packages need
  machine-convertible runtime instructions and consumer validation.

The current gap is that entity binding does not describe parameterization
semantics. A package can say it has an entity binding, but it does not clearly
say whether the entity is a fixed exemplar, theme, runtime target, property
source, initial-sound source, word target, or invalid for that activity.

Current package evidence also shows the risk:

- many current generated activities use `entity_class_filter: []`, which means
  "wide match" but not "valid for every possible dynamic entity";
- `concept_phoneme_hunt_collect` is authored around
  `beginning_b_sound` and `/b/`;
- several activities contain fixed cards, clue sequences, story beats,
  reference content, or asset catalogs that cannot be safely retargeted without
  explicit slots and validation.

## Problem Statement

Without producer-declared parameterization metadata, downstream consumers must
infer behavior from activity IDs, prose, focal attributes, or broad match tags.
That creates incorrect handoffs:

- phoneme packages keep a fixed sound after dynamic entity handoff;
- fixed story or clue packages may be rewritten as if they supported arbitrary
  objects;
- selectors may offer packages for entities that cannot satisfy the authored
  mechanic;
- future package authors can accidentally claim entity-agnostic behavior with
  no executable runtime slots.

## Settled Decisions

- This is both a producer and consumer issue. This repo owns package authoring,
  generator instructions, schemas/validators, fixtures, and current package
  migration. WonderLens AI owns runtime resolution and enforcement.
- Do not mark every activity entity-agnostic by default.
- A package is valid for dynamic entity handoff only when it declares a
  supported parameterization mode and the required slots/derivations.
- Packages with fixed authored content may remain valid packages, but must be
  marked `fixed` or `entity_theme` rather than dynamic target modes.
- `entity_class_filter: []` remains broad match metadata, not proof that the
  activity can dynamically retarget.
- Future generated packages must put machine-readable parameterization metadata
  in package files, not only in prose notes.
- The producer contract should stay additive so older five-file packages remain
  valid authoring artifacts.

## Proposed Package Contract

Add a package-local parameterization declaration. The exact file placement may
be settled during implementation, but it should be available to both demo
support validation and downstream runtime conversion. Reasonable options are:

- a new top-level `parameterization` block in `demo_support.yaml`;
- a new optional `parameterization.yaml`;
- a strongly typed block in `tag_block.yaml` if the vocabulary/schema owner
  decides this is core matchability metadata.

Preferred MVP: place it in `demo_support.yaml` for demo/runtime-ready packages,
then mirror enough summary into `tag_block.yaml` or runtime conversion outputs
only if downstream selection needs it before demo support is loaded.

Recommended modes:

| Mode | Producer Meaning |
| --- | --- |
| `fixed` | Handoff entity does not change authored success criteria or target content. |
| `entity_theme` | Handoff entity may be named in hook/transition/context but does not change success criteria. |
| `entity_target` | Handoff entity becomes the target object/subject. |
| `property_target` | A discovered visual/taxonomy/property value becomes the target. |
| `initial_sound_from_entity` | The spoken entity label derives the phoneme/sound target. |
| `word_from_entity` | The entity label becomes the word-memory/echo target. |
| `asset_catalog_target` | Target/distractor behavior depends on declared package assets or catalogs. |

Recommended shape:

```yaml
parameterization:
  mode: initial_sound_from_entity
  validity:
    production_supported: true
    requires:
      - handoff.object_name_en
    allowed_entity_classes: []
    invalid_when:
      - entity_name_missing
  source_fields:
    entity_name:
      - handoff.object_name_en
      - handoff.object_name
      - demo_support.default_entity_binding.display_label
  derived_runtime_fields:
    accepted_initial_sound: first_spoken_letter
    collection_criterion_template: "Things whose spoken names begin with the {sound_label} sound"
  authored_constants:
    target_sound: dynamic
    reference_assets: fixed
  consumer_notes:
    wonderlens_ai: "Runtime must derive target sound from handoff entity before planning."
```

For `fixed` and `entity_theme`, the declaration must name which fields are safe
to vary and which authored constants must not change. That prevents a consumer
from turning a fixed fox/moon/owl story or fixed cat clue sequence into an
arbitrary dynamic activity without a real authored slot.

## Current Twelve Migration

Create a migration matrix for the current twelve runtime-ready/generated
activities. The implementation should inspect the latest canonical package set
and the run-local full-pass packages before editing, because not all twelve may
exist in the same root directory at all times.

The matrix should classify each activity as one of:

- `fixed`;
- `entity_theme`;
- `entity_target`;
- `property_target`;
- `initial_sound_from_entity`;
- `word_from_entity`;
- `asset_catalog_target`;
- `unsupported_until_parameterized`.

Minimum activities to classify:

```text
concept_animal_sound_motion_voice
concept_career_decision_decide
concept_constellation_star_count_enumerate
concept_emotion_reader_care
concept_guided_drawing_probe
concept_partial_reveal_deduce
concept_phoneme_hunt_collect
concept_recognition_pop_probe
concept_story_unlock_probe
concept_travel_planner_predict
concept_vegetable_sort_sort
concept_word_echo_remember
```

Expected classification guidance:

- Phoneme Treasure Hunt should support `initial_sound_from_entity` once target
  sound fields and runtime instructions are dynamic.
- Word Echo should support `word_from_entity` only if its prompts and branches
  use the handoff label as the word target.
- Guided Drawing and Recognition Pop can support dynamic targets only when
  assets/prompts/catalogs declare the target and distractor slots.
- Constellation and other reference-bound activities must not become arbitrary
  entity targets unless reference data/assets are declared.
- Career, travel, and story activities may often be `entity_theme`, but fixed
  scenario/story beats must remain authored constants unless slots are added.
- Vegetable Sort must declare valid categories/properties; arbitrary object
  handoff should be invalid unless a sort rule can be derived.

## Authoring Instruction Updates

Update authoring guidance so every generated demo/runtime-ready package answers:

- What role does the discovered entity play?
- Is the package valid for arbitrary objects, a bounded entity class, or only
  the authored exemplar?
- Which runtime fields are dynamic?
- Which authored constants must not change?
- What handoff inputs are required?
- What should a downstream consumer do if required inputs are missing?
- Which assets or catalogs are tied to the dynamic target?

Likely files:

- `program.md`
- `transform.md`
- `transform_run.md`
- `docs/activity_vocabulary.md`
- `activities/README.md`
- `activities/_schema/tag_block.schema.json` if the field lands there
- `scripts/validate_demo_package_contract.py`
- tests for contract validation and generation/asset pipeline fixtures

## Validator And Fixture Expectations

Validator changes should enforce:

- allowed parameterization modes;
- supported/degraded packages must declare parameterization;
- exactly one default entity binding remains required when demo support expects
  dynamic or thematic entity use;
- dynamic modes must declare required source fields and derived/target slots;
- fixed/thematic modes must declare authored constants or non-retargetable
  fields;
- `initial_sound_from_entity` must not simultaneously hard-code a conflicting
  static target sound;
- reference-bound or asset-catalog modes must require relevant asset/provenance
  declarations;
- unsupported packages may include parameterization notes but must not claim
  playable dynamic support.

Fixture coverage should include:

- valid `initial_sound_from_entity` phoneme package;
- invalid phoneme package with hard-coded `/b/` plus dynamic claim;
- valid `entity_theme` package with fixed success criteria;
- invalid arbitrary `entity_target` claim missing target slots/assets;
- valid `word_from_entity` or `asset_catalog_target` package if current package
  content supports it;
- current-twelve classification matrix fixture.

## Downstream Contract

The final producer metadata must be readable by WonderLens AI. The two repos
should agree on:

- field names;
- allowed mode values;
- missing-input behavior;
- how derived fields map to `runtime.yaml` and Activity WS session context;
- how selector/debug evidence distinguishes fixed, thematic, valid dynamic, and
  invalid combinations.

If the authoring and backend plans disagree during implementation, stop and
document the conflict before changing package behavior.

## Non-Goals

- Do not implement WonderLens AI runtime resolver logic in this repo.
- Do not generate package content at request time.
- Do not claim true phoneme support for complex English digraphs or non-English
  names unless a concrete phoneme derivation strategy is added.
- Do not rewrite all current packages as fully dynamic. Fixed and thematic
  classifications are valid outcomes when honest.
- Do not create broad formatting sweeps over generated package prose.

## Required Checks For Implementation

Minimum final checks:

```bash
git diff --check
python3 scripts/validate_demo_package_contract.py activities
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_generate_and_curate_asset_pipeline.py -q
```

If `activities/*/tag_block.yaml` or the tag-block schema changes, also run the
schema validation snippet from `AGENTS.md`.

If generation instructions change in a way that affects package output, run the
narrowest available fixture or pipeline test proving generated demo support and
asset manifests still validate.

## Rollout

1. Add the contract and validator support.
2. Update authoring instructions and examples.
3. Add fixtures for dynamic, thematic, fixed, and invalid cases.
4. Classify and migrate the current twelve package set.
5. Run downstream WonderLens AI conversion/runtime checks after the backend
   resolver contract lands or against a pinned compatible backend branch.

Until both repos are complete, do not claim all current twelve are
entity-agnostic. The accurate claim is that each valid package declares its
entity behavior, and invalid combinations are filtered by consumers.

## Open Risks

- Some current packages may need substantive authoring repairs before they can
  honestly move from `fixed` or `entity_theme` to a dynamic target mode.
- The source of truth for parameterization may need to be split between
  `demo_support.yaml` and `tag_block.yaml` if discovery selection needs the
  data before demo support loading.
- Current package directories and run-local package sets may differ; migration
  should explicitly identify which package set is being classified.
- First-letter sound derivation is an MVP approximation, not full phonetics.
