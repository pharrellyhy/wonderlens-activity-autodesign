# Activity Display Contract V1 Implementation Plan

Date: 2026-06-23

Status: Planned

## Goal

Define and backfill the producer-side display contract that lets WonderLens
activity packages declare exactly what the app should show, how the child can
respond, what the backend should verify, and which sound, lighting, and haptic
feedback profiles apply.

This plan owns `wonderlens-activity-autodesign` only. Runtime consumption and
Activity WebSocket verification are tracked in the WonderLens AI companion
plan:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-23-activity-display-runtime-verification.md
```

## Current Evidence

Current migrated activity packages can contain `asset_manifest.yaml` and
`demo_support.yaml`, but they do not have a machine-readable per-frame display
contract. Downstream consumers therefore infer layout, wheel/button behavior,
verification rules, and effects from activity prose, package IDs, or current
runtime heuristics.

Local analysis found an existing display-contract reference document:

```text
docs/activity_display_contract.md
```

That document should be promoted from guidance into the basis for a concrete
package-local file:

```text
activities/<activity_id>/activity_display_contract_v1.yaml
```

The visual design document at:

```text
/Users/pharrelly/Downloads/活动库视觉规范(1).docx
```

defines exactly five supported layouts. Backend and package metadata must use
only those five layouts; previous discussions of twelve layout variants should
be treated as authoring heuristics, not app-facing IDs.

## Settled Decisions

- Use a new package-local `activity_display_contract_v1.yaml`; do not overload
  `tag_block.yaml`, `demo_support.yaml`, or prose in `prod.md`.
- The contract is general for future packages. The current twelve activities
  are only the first migration and regression set.
- Verification must be bound to the displayed asset or displayed option, not
  to loose activity prose or an activity ID.
- App-facing layout IDs are limited to the five design-doc layouts:
  - `single_image`
  - `two_image_options`
  - `two_direction_options`
  - `two_number_options`
  - `multi_option_carousel`
- Use English-only effect fields:
  - `sound_effects`
  - `lighting_effects`
  - `haptic_feedback`
- The design doc does not define sound, lighting, or haptic behavior. Those
  should be authored effect profiles with safe defaults, not claims copied from
  the visual spec.
- For concrete bitmap assets, `display_asset_id` must reference
  `asset_manifest.yaml`. For abstract cues such as a phoneme target, number, or
  story gate, the contract must declare a display asset entry with metadata
  rather than pretending it is a bitmap manifest asset.
- Generated and run-local packages should use the same contract shape.

## Package Contract

Recommended package-local file:

```yaml
activity_id: concept_recognition_pop_probe
version: 1
contract: activity_display_contract_v1
display_assets:
  - display_asset_id: round_1_scene
    kind: image
    asset_manifest_id: round_1_scene
  - display_asset_id: option_apple
    kind: option
    label: Apple
    aliases: [apple]
frames:
  - frame_id: step_3_round_1
    step_ref: prod.step_3.round_1
    layout_id: two_image_options
    display_asset_id: round_1_scene
    control_mode: binary_choice
    options:
      - option_id: apple
        label: Apple
        display_asset_id: option_apple
        is_correct: true
      - option_id: car
        label: Car
        display_asset_id: option_car
        is_correct: false
    verification_policy:
      type: choice_match
      required: true
      evidence: [selected_option_id, transcript]
    effect_profile:
      id: choice_confirm
      sound_effects: [focus_tick, confirm_chime]
      lighting_effects: [focus_ring, success_ring]
      haptic_feedback: [wheel_tick, confirm_pulse]
```

The implementation may refine exact enum names, but it must preserve these
semantics:

- `frames` are the unit of app display and backend verification.
- `frame_id` is stable inside one package.
- `layout_id` is one of the five allowed values.
- `control_mode` tells the app which input surface to render.
- `options` use stable `option_id` values so app events do not depend on label
  text.
- `verification_policy` tells the runtime how to judge app action, transcript,
  or photo evidence against the active displayed asset.
- `effect_profile` declares feedback intent while leaving final device
  rendering to the app.

## Layout Mapping Rules

Use these app-facing layout IDs only:

| `layout_id` | Use When | Typical Controls |
| --- | --- | --- |
| `single_image` | One centered image, prompt card, scene, cue, or open-ended task. | Voice, camera, reveal, replay, or self-report. |
| `two_image_options` | Two visual choices with images or cards. | Wheel/button selection or voice fallback. |
| `two_direction_options` | Left/right or path-style branch choice. | Wheel/button selection or voice fallback. |
| `two_number_options` | Two numeric choices. | Wheel/button number choice or voice fallback. |
| `multi_option_carousel` | Three or more options, category items, or carousel choices. | Wheel carousel, button selection, or voice fallback. |

Do not emit separate activity-specific layout variants. If a future activity
does not fit these layouts, mark it unsupported for this app contract until a
new design-doc layout is approved.

## Control Modes

The implementation should define a compact enum that covers the current
product needs without encoding layout variants:

- `voice_only`
- `binary_choice`
- `carousel_choice`
- `number_choice`
- `step_confirm`
- `camera_capture`
- `replay_only`
- `reveal_control`
- `sort_pick_place`
- `self_report`

The app may render these with wheel, button, voice, or mixed controls, but the
runtime must receive stable events such as `selected_option_id`,
`display_asset_id`, `spoken_text`, `photo_id`, or `sort_target_id`.

## Verification Policies

Author packages with one explicit policy per verifiable frame:

- `choice_match`: selected option must match the displayed frame's correct
  option or accepted option set.
- `number_match`: spoken or selected number must match displayed count
  metadata.
- `category_match`: selected or placed item must match the displayed category
  or sort target.
- `alias_match`: transcript must match displayed answer aliases.
- `echo_match`: transcript must match the displayed word or phrase cue.
- `photo_object_initial_sound`: vision-recognized object name must satisfy the
  displayed sound target, such as `/b/`.
- `semantic_llm_judge`: transcript is judged against an asset-specific rubric
  when deterministic matching is not enough, such as emotion reading.
- `self_report`: child reports completion or readiness; do not grade quality.
- `accept_any_participation`: record participation without right/wrong
  judgment.

Policies should include any required metadata, for example `expected_number`,
`accepted_aliases`, `target_initial_sound`, `target_category_id`, or
`semantic_rubric`.

## Current Twelve Migration

Backfill the current twelve concept packages as the first migration set:

| Activity | Layout | Control | Verification |
| --- | --- | --- | --- |
| `concept_animal_sound_motion_voice` | `single_image` | `replay_only` | `accept_any_participation` or future animal-sound voice check. |
| `concept_career_decision_decide` | `two_image_options` | `binary_choice` | `choice_match` against displayed tool/action options. |
| `concept_constellation_star_count_enumerate` | `single_image`; optional `two_number_options` fallback | `voice_only` or `number_choice` | `number_match` against displayed `star_count`. |
| `concept_emotion_reader_care` | `single_image` | `voice_only` | `semantic_llm_judge` against displayed expression/body-cue card. |
| `concept_guided_drawing_probe` | `single_image` | `step_confirm` | `self_report`; final photo may verify presence only, not drawing quality. |
| `concept_partial_reveal_deduce` | `single_image` | `reveal_control` | `alias_match` against displayed reveal answer metadata. |
| `concept_phoneme_hunt_collect` | `single_image` | `camera_capture` | `photo_object_initial_sound` against the displayed sound target. |
| `concept_recognition_pop_probe` | `two_image_options` or `multi_option_carousel` | `binary_choice` or `carousel_choice` | `choice_match` against displayed target/distractors. |
| `concept_story_unlock_probe` | `single_image`; optional `two_direction_options` | `voice_only` or `binary_choice` | `alias_match`, `choice_match`, or `accept_any_participation` by frame. |
| `concept_travel_planner_predict` | `two_image_options` | `binary_choice` | `accept_any_participation` or `choice_match` when authored as a factual/safety choice. |
| `concept_vegetable_sort_sort` | `multi_option_carousel` | `sort_pick_place` | `category_match` against displayed item and group. |
| `concept_word_echo_remember` | `single_image` | `replay_only` | `echo_match` against displayed word/phrase cue. |

If a package lacks concrete metadata needed for deterministic verification
after inspection, the migration should add that metadata rather than relying on
runtime inference.

## Implementation Areas

- Update `docs/activity_display_contract.md` to become the stable contract
  reference for `activity_display_contract_v1`.
- Update `activities/README.md`, `program.md`, `run.md`, `GOAL.md`, and
  `README.md` so demo/runtime-ready package generation includes the new file.
- Add `activities/_schema/activity_display_contract_v1.schema.json`.
- Add `scripts/validate_activity_display_contract.py`.
- Add validator tests and valid/invalid fixtures.
- Backfill `activities/<current_12>/activity_display_contract_v1.yaml`.
- Backfill the current run-local package seed if it remains the WonderLens AI
  import source:

```text
runs/20260604_144222_wonderlens_ai_runtime_ready_12/activity_packages/<activity_id>/activity_display_contract_v1.yaml
```

## Validation

Run the existing package checks:

```bash
python3 scripts/validate_demo_package_contract.py activities
python3 -m unittest tests.test_demo_package_contract_validator -v
python3 -c "
import json, yaml, pathlib, sys
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
ok = True
for p in sorted(pathlib.Path('activities').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK  ' if not errs else 'FAIL'), p)
    for e in errs:
        ok = False
        print(f'  {list(e.absolute_path)}: {e.message}')
sys.exit(0 if ok else 1)
"
```

Add and run the new focused checks:

```bash
python3 -m unittest tests.test_activity_display_contract_validator -v
python3 scripts/validate_activity_display_contract.py activities
python3 scripts/validate_activity_display_contract.py runs/20260604_144222_wonderlens_ai_runtime_ready_12/activity_packages
git diff --check
```

If the run-local directory is unavailable or superseded, document the selected
import seed and validate that path instead.

## Non-Goals

- Do not implement WonderLens AI runtime loading or WebSocket verification in
  this repo.
- Do not change the app visual design beyond the five approved layout IDs.
- Do not invent sound, lighting, or haptic requirements from the design doc.
- Do not classify unsupported activity mechanics as playable.
- Do not require every legacy package in the repo to be fully migrated before
  the current twelve are validated.
- Do not edit secrets, local credentials, or production data.

## Risks

- Some `prod.md` files mention prose-only bundle IDs that are not present in
  `asset_manifest.yaml`; these need explicit display asset declarations or real
  manifest assets.
- `semantic_llm_judge` can become too vague if authoring omits a per-asset
  rubric. The schema should require enough rubric text and accepted evidence to
  avoid generic correctness guesses.
- `effect_profile` can become unbounded. Start with an enum-like `id` and
  permissive arrays for `sound_effects`, `lighting_effects`, and
  `haptic_feedback`, then tighten once app support stabilizes.
- The consumer repo must reject or ignore unknown layouts. Producer validation
  should catch unsupported layout IDs before handoff.

## Ordering

1. Add schema, validator, and fixtures for the new contract.
2. Update authoring/generation docs to require the contract for
   runtime-ready packages.
3. Backfill the current twelve packages using real asset IDs or explicit
   display asset declarations.
4. Run focused producer validation.
5. Implement the WonderLens AI companion plan against this stable contract.
