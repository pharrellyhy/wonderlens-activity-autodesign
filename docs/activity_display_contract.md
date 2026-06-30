# Activity Display Contract V1

This guide defines the package-local runtime display contract for WonderLens
activity packages:

```text
activities/<activity_id>/activity_display_contract_v1.yaml
runs/<run_id>/activity_packages/<activity_id>/activity_display_contract_v1.yaml
```

Runtime-ready packages use this file to declare what the app shows, which
control surface the child uses, how the backend verifies the child action, and
which sound, lighting, and haptic feedback profile should apply. Do not put
this app display metadata in `tag_block.yaml`; `tag_block.yaml` remains the
matcher, recap, and dashboard metadata contract.

The contract is frame-level. A single activity can use one display shape for an
intro, a different shape for a choice round, and a third shape for a closing
badge.

## Package Shape

```yaml
activity_id: concept_recognition_pop_probe
version: 1
contract: activity_display_contract_v1
display_assets:
  - display_asset_id: red_apple_target
    kind: option
    asset_manifest_id: apple
    label: Red apple
    metadata:
      accepted_aliases: [apple, red apple]
frames:
  - frame_id: step_3_round_1
    step_ref: prod.step_3.round_1
    layout_id: two_image_options
    display_asset_id: red_apple_target
    control_mode: binary_choice
    input_affordance:
      select: wheel
      confirm: press
    options:
      - option_id: apple
        label: Red apple
        display_asset_id: red_apple_target
        is_correct: true
      - option_id: car
        label: Blue car
        display_asset_id: blue_car_distractor
        is_correct: false
    verification_policy:
      type: choice_match
      required: true
      target:
        type: option
        option_id: apple
      evidence: [selected_option_id, transcript]
    effect_profile:
      id: choice_confirm
      sound_effects: [focus_tick, confirm_chime]
      lighting_effects: [focus_ring, success_ring]
      haptic_feedback: [wheel_tick, confirm_pulse]
```

Concrete bitmap assets use `asset_manifest_id` to reference
`asset_manifest.yaml`. Abstract cues such as a phoneme target, number target,
story gate, category board, or word cue are declared directly in
`display_assets[].metadata`. Every `kind: item` display asset must declare
`metadata.entity_name` so the runtime can expose the represented object without
guessing from labels or asset IDs. Entity-targeted image assets, such as animal
cards that declare `metadata.target_animal`, must also declare
`metadata.entity_name`.

## Decision Order

Choose values in this order:

1. Identify the child action for the frame.
2. Count the bounded options the child can select.
3. Check whether displayed images reference real package assets or abstract
   display cues.
4. Choose `layout_id`.
5. Choose `control_mode`.
6. Declare `input_affordance` for hardware selection and confirmation.
7. Bind `verification_policy` to the displayed asset or displayed option.
8. Declare English-only `effect_profile` fields.

If a frame does not fit the five layout IDs below, it is unsupported for this
contract until a new app layout is approved.

## Layout IDs

Use only these app-facing values:

| `layout_id` | Use when | Typical controls |
|---|---|---|
| `single_image` | One centered image, prompt card, cue, scene, or open-ended task. | `voice_only`, `camera_capture`, `replay_only`, `step_confirm`, `reveal_control`, `self_report` |
| `two_image_options` | Exactly two object, card, text, or image choices. | `binary_choice` |
| `two_direction_options` | Exactly two spatial/path choices. | `binary_choice` |
| `two_number_options` | Exactly two numeric choices. | `number_choice` or `binary_choice` |
| `multi_option_carousel` | Three or more bounded options or sortable candidates. | `carousel_choice`, `sort_pick_place` |

Do not create activity-specific variants such as `phoneme_camera`,
`sort_board`, `partial_reveal`, or `word_echo`. Those are control modes,
verification policies, or state inside one of the five approved layouts.

## Control Modes

Allowed `control_mode` values:

| `control_mode` | Use when | Required app/backend evidence |
|---|---|---|
| `voice_only` | Child answers freely by speech. | `transcript` and any normalized semantic fields. |
| `binary_choice` | Child selects one of exactly two options. | `selected_option_id`; optional `transcript`. |
| `carousel_choice` | Child selects one of three or more options. | `selected_option_id`; optional `transcript`. |
| `number_choice` | Child selects or says a number. | `selected_number` or `spoken_number`. |
| `step_confirm` | Child confirms a task step as done/not yet. | `self_reported_done`; optional `transcript`. |
| `camera_capture` | Child takes a photo as the core action. | `photo_id` plus any vision-derived fields. |
| `replay_only` | Child listens, echoes, imitates, or repeats. | `transcript` or participation event. |
| `reveal_control` | Child guesses or requests another clue/reveal stage. | `transcript`, `reveal_stage`, optional control event. |
| `sort_pick_place` | Child places an item into a target group. | `selected_item_id` or `selected_option_id`, plus `sort_target_id`. |
| `self_report` | Child reports completion, readiness, or preference. | `self_reported_done` or equivalent event. |

## Input Affordance

`input_affordance` is required on every frame. It records the physical input
surface separately from the semantic `control_mode`:

| Control mode | `select` | `confirm` |
|---|---|---|
| `binary_choice`, `carousel_choice`, `number_choice`, `sort_pick_place` | `wheel` | `press` |
| `step_confirm`, `camera_capture`, `reveal_control`, `self_report` | `none` | `press` |
| `voice_only`, `replay_only` | `none` | `voice` |

Use `wheel` only when the child rotates/navigates among displayed options. Use
`press` when the device button confirms a selected option, advances a reveal,
confirms a step, or captures a photo. Use `voice` when the spoken response is
the only confirmation evidence.

## Verification Policies

Every verifiable frame must declare one policy. The policy must be bound to the
displayed asset or displayed option, not only to prose, package ID, or activity
title.

| Policy | Required binding |
|---|---|
| `choice_match` | `target.type: option` and `target.option_id` matching a frame option with `is_correct: true`. |
| `number_match` | `target.type: display_asset`; target display asset has `metadata.expected_number`. |
| `category_match` | `target.type: display_asset`; target display asset has `metadata.target_category_id`. |
| `alias_match` | `target.type: display_asset`; target display asset has `metadata.accepted_aliases`. |
| `echo_match` | `target.type: display_asset`; target display asset has `metadata.target_phrase` or `metadata.accepted_aliases`. |
| `photo_object_initial_sound` | `target.type: display_asset`; target display asset is the frame display asset and has `metadata.target_initial_sound`. Evidence includes `photo_id`. |
| `semantic_llm_judge` | `target.type: display_asset`; target display asset has `metadata.semantic_rubric`. |
| `self_report` | `target.type: display_asset`; evidence includes `self_reported_done`. |
| `accept_any_participation` | Participation is recorded without right/wrong judgment. |

Use `required: false` for non-gating clue guesses, open-ended predictions,
voice imitation, story participation, or child-chosen categories. Do not grade
quality when the package only promises participation or self-report.

## Effect Profile

`effect_profile` declares feedback intent; final device rendering stays in the
app. Use English-only field names and effect IDs:

```yaml
effect_profile:
  id: photo_sound_check
  sound_effects: [camera_ready, sound_match_chime]
  lighting_effects: [capture_glow, success_ring]
  haptic_feedback: [capture_pulse, confirm_pulse]
```

Do not use localized effect names, prose-only fields such as `SFX`, or old
single-string `effect_profile` values.

## Current Twelve Mapping

| Activity | Layout/control | Verification |
|---|---|---|
| `concept_animal_sound_motion_voice` | `single_image` / `replay_only` | `accept_any_participation` |
| `concept_career_decision_decide` | `two_image_options` / `binary_choice` | `choice_match` |
| `concept_constellation_star_count_enumerate` | `single_image` / `voice_only` | `number_match` |
| `concept_emotion_reader_care` | `single_image` / `voice_only` | `semantic_llm_judge` |
| `concept_guided_drawing_probe` | `single_image` / `step_confirm`; final photo prompt | `self_report` |
| `concept_partial_reveal_deduce` | `single_image` / `reveal_control` | non-gating `alias_match` until final answer |
| `concept_phoneme_hunt_collect` | `single_image` / `camera_capture` | `photo_object_first_letter` against runtime-selected letter badge |
| `concept_recognition_pop_probe` | `two_image_options` or `multi_option_carousel` | `choice_match` |
| `concept_story_unlock_probe` | `single_image` / `voice_only` or `replay_only` | `alias_match`, `accept_any_participation`, `echo_match` |
| `concept_travel_planner_predict` | `two_image_options` / `binary_choice` only when abstract options are authored | `accept_any_participation` unless a factual correct option is authored |
| `concept_vegetable_sort_sort` | `multi_option_carousel` / `sort_pick_place` | `category_match` for authored category rounds; participation for child-chosen rule |
| `concept_word_echo_remember` | `single_image` / `replay_only` | `echo_match` when target phrases are authored in display metadata |

## Validation

Schema:

```text
activities/_schema/activity_display_contract_v1.schema.json
```

Focused validator:

```bash
python3 scripts/validate_activity_display_contract.py activities
python3 scripts/validate_activity_display_contract.py runs/<run_id>/activity_packages
```

The validator rejects unknown layouts, missing display-asset bindings for
verifiable policies, missing `photo_id` evidence for photo sound checks,
manifest asset references that do not exist, and non-English effect terms.
