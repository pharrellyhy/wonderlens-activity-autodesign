# Activity Display Contract

This guide defines how activity authors choose the runtime display contract for
WonderLens device activities. It is intended for package generation and review
in this repository, and for downstream normalization in WonderLens AI.

The contract is decided per frame or round, not only per activity. A single
activity can use one display shape for the hook, another for a round, and a
third for celebration.

## Contract shape

Future package metadata should carry a frame-level display declaration like:

```yaml
activity_id: concept_recognition_pop_probe
version: 1
frames:
  round_1:
    layout_type: two_image_choice
    control_mode: binary_choice
    effect_profile: choice_confirm
    assets:
      primary: round_1_scene
    options:
      - id: apple
        label: Apple
        asset_id: apple
      - id: car
        label: Car
        asset_id: car
    state:
      round_number: 1
      total_rounds: 3
```

`layout_type` is the visual shell. It must align with the five layouts in the
WonderLens visual specification. `control_mode` tells the app how wheel, button,
camera, and voice input should behave. `effect_profile` selects a normalized
sound, light, and haptic bundle.

Do not invent a new layout type to express camera capture, reveal masks,
progress, echo, or sorting. Those are controls, state, or effects inside one of
the five approved layout shells.

## Decision order

Choose values in this order:

1. Identify the child action for the frame.
2. Count the valid choices the child can select.
3. Check whether every choice has a real package asset.
4. Apply product and safety constraints.
5. Choose `layout_type`.
6. Choose `control_mode`.
7. Choose `effect_profile` from the state transition.

The deterministic rule is:

```text
child action + number of choices + asset availability + product constraints
= layout_type + control_mode + effect_profile
```

If a frame does not fit the available enums, first try to degrade it into one of
the five supported layouts. Add a new enum only after the product and app teams
approve a new display behavior.

## Layout types

`layout_type` is the only layout enum the app should treat as a visual shell.
The approved values are:

```yaml
layout_type:
  - single_image
  - two_image_choice
  - two_direction_choice
  - two_number_choice
  - multi_choice
```

### `single_image`

Use when the frame presents one object, one scene, one prompt, one camera hint,
one step, one clue, or one voice cue.

Typical uses:

- Open-ended voice questions.
- Emotion or care scenes.
- Animal imitation cards.
- Echo/repeat/memory cue cards.
- Guided drawing or building steps.
- Partial reveal or mystery clue screens.
- Story gates or locked story scenes.
- Cat5 photo capture hints.
- Badge, recap, intro, rules, and closing scenes.

Required authoring:

- At least one scene or object asset when the screen claims a visual is shown.
- `state` fields for specialized behavior, such as `step_number`,
  `reveal_stage`, `progress_slots`, or `capture_count`.

Allowed controls:

- `voice_only`
- `replay_only`
- `step_confirm`
- `camera_capture`
- `reveal_control`

Avoid:

- Using `single_image` for bounded visual choices when real option assets exist.
- Burying a selectable two-card or carousel decision inside an unstructured scene.
- Claiming a photo, card, reveal, or progress marker is visible when no asset or
  state exists to render it.

### `two_image_choice`

Use when the child chooses between exactly two visual options and the options are
not spatial directions or pure numbers.

Typical uses:

- Choose apple or car.
- Choose water hose or cooking oil.
- Choose sunny trip or rainy trip.
- Choose happy face or confused face, when the product allows screen choice.

Required authoring:

- Exactly two `options`.
- Each option should have either `asset_id` or an approved text/icon fallback.
- The selected option is rendered as the larger bubble; the other option remains
  smaller.

Allowed controls:

- `binary_choice`

Avoid:

- Using this layout for left/right path choices. Use `two_direction_choice`.
- Using this layout for numeric choices. Use `two_number_choice`.
- Using this layout if there are more than two choices. Use `multi_choice`.

### `two_direction_choice`

Use when the child chooses between exactly two spatial or path options.

Typical uses:

- Left path or right path.
- Up route or down route.
- Door A on the left or door B on the right.
- Branching story paths with direction as the point of the choice.

Required authoring:

- Exactly two `options`.
- Each option should declare a direction-like `id`, such as `left`, `right`,
  `up`, `down`, `near`, or `far`.
- Option assets should show the path or destination, not unrelated objects.

Allowed controls:

- `binary_choice`

Avoid:

- Using direction labels for a normal object choice.
- Making a child physically move left or right unless the product safety brief
  explicitly supports the movement.

### `two_number_choice`

Use when the child chooses between exactly two numbers.

Typical uses:

- Choose whether the star card has 7 or 29 stars.
- Choose between two count estimates.
- Choose a quantity answer after a voice-first counting prompt needs fallback.

Required authoring:

- Exactly two `options`.
- Each option must include a numeric `value`.
- The selected number should be shown as the yellow circle specified by the
  visual design.

Allowed controls:

- `binary_choice`

Avoid:

- Using this layout for non-numeric text labels.
- Offering large or developmentally implausible numbers without a clear reason.
- Replacing a good voice counting interaction with a number choice too early.

### `multi_choice`

Use when the child chooses among more than two bounded options.

Typical uses:

- Three or more object cards.
- Vegetable or animal carousels.
- Picker lists.
- Sorting candidates.
- Multi-option memory or recognition rounds.

Required authoring:

- Three or more `options`.
- Every option should have a real `asset_id` when the prompt says the child can
  look at cards or objects.
- Current option is rendered as the larger center bubble; side options are
  smaller and may be partially visible.

Allowed controls:

- `carousel_choice`
- `sort_pick_place`

Avoid:

- Using `multi_choice` for open-ended answers.
- Showing distractor cards that the activity does not actually accept as
  selectable options.
- Using a carousel when the child should explain freely by voice.

## Control modes

`control_mode` defines interaction behavior. Choice modes may still allow voice
as an alternate input, but the mode tells the app what wheel/button affordance
is expected.

```yaml
control_mode:
  - voice_only
  - replay_only
  - binary_choice
  - carousel_choice
  - step_confirm
  - camera_capture
  - reveal_control
  - sort_pick_place
```

### `voice_only`

Use when the child answers freely by speech.

Good fits:

- Open-ended explanations.
- Emotion/care responses.
- Story imagination.
- Counting spoken aloud.
- Guessing when valid answers are not all visible choices.

App behavior:

- Do not show wheel answer selection.
- A replay button is optional only if the app has a standard prompt-replay affordance.
- Server evaluates the spoken turn.

Avoid:

- Using `voice_only` when the frame asks the child to choose from visible cards.
- Asking the child to tap, point, or wheel-select when the product copy says not
  to use touch.

### `replay_only`

Use when the main action is to imitate, echo, listen again, or repeat.

Good fits:

- Animal sound imitation.
- Word echo.
- Memory repeat.
- Voice-stage prompts.

App behavior:

- Button can replay the prompt or cue sound.
- Wheel should not select an answer.
- Optional done/again affordance is allowed only when the runtime needs manual
  pacing.

Avoid:

- Treating replay as answer confirmation.
- Using loud or startling replay effects.

### `binary_choice`

Use when exactly two bounded options are visible.

Good fits:

- `two_image_choice`
- `two_direction_choice`
- `two_number_choice`

App behavior:

- Wheel toggles between the two options with no endpoint.
- Current option is visibly selected.
- Pressing the wheel/button confirms the selected option.
- Speaking the option should be accepted as an alternate input when supported.

Required event:

```yaml
type: user_action
action: select_option
option_id: <option id>
```

Avoid:

- Using `binary_choice` with one option or more than two options.
- Using it for free-form speech answers.

### `carousel_choice`

Use when three or more bounded options are visible.

Good fits:

- Object card carousels.
- Recognition games with three or more candidates.
- Multi-option preference or selection prompts.

App behavior:

- Wheel cycles options continuously; no start/end endpoint.
- Center/current option is the large bubble.
- Pressing the wheel/button confirms the current option.
- Spoken option labels can be accepted as alternate input when supported.

Required event:

```yaml
type: user_action
action: select_option
option_id: <option id>
```

Avoid:

- Using a carousel for an unbounded category, such as "name any animal."
- Using a carousel when options lack assets and the child needs to inspect visual
  differences.

### `step_confirm`

Use when the child reports whether a step is complete.

Good fits:

- Guided drawing.
- Building or craft steps.
- "Done / not yet" progress checks.

App behavior:

- Wheel toggles `done` and `not_yet`.
- Pressing the wheel/button confirms.
- Voice "yes", "done", "not yet", or equivalent should be accepted.

Required options:

```yaml
options:
  - id: done
    label: Done
  - id: not_yet
    label: Not yet
```

Avoid:

- Treating `not_yet` as wrong or failed.
- Using this mode for knowledge questions.

### `camera_capture`

Use when the child must take or upload a photo as the core action.

Good fits:

- Cat5 collection rounds.
- Runtime visual verification.
- Photo-based synthesis inputs.

App behavior:

- Show camera shutter/capture affordance.
- Do not use wheel selection for the answer.
- Send the captured `photo_id` or upload event to the server.

Required event:

```yaml
type: user_action
action: capture_photo
photo_id: <photo id>
```

Avoid:

- Treating package example assets as proof that the child found the target.
- Skipping server-side visual or spoken-label verification when the outcome
  depends on a real-world object.

### `reveal_control`

Use when the child can control whether to reveal another clue or answer now.

Good fits:

- Partial reveal.
- Mystery clue stages.
- "I know" versus "show me more."

App behavior:

- Optional wheel toggles `reveal_next` and `i_know`.
- Pressing confirms the selected control.
- Voice guesses should remain supported.

Required state:

```yaml
state:
  reveal_stage: 1
  reveal_total: 3
  mask: soft_circle
```

Avoid:

- Hiding information needed for safety or instructions.
- Making reveal control mandatory when voice guessing alone is enough.

### `sort_pick_place`

Use when the child chooses an item and places it into a group, basket, order, or
category.

Good fits:

- Vegetable sorting.
- Grouping natural/man-made items.
- Matching an item to a category.

App behavior:

- Wheel can cycle candidate items, then cycle target groups if needed.
- Button selects or places.
- Server receives both selected item and selected target when placement is
  explicit.

Required event:

```yaml
type: user_action
action: place_item
item_id: <item id>
target_id: <group id>
```

Avoid:

- Using sort placement when the child is only naming one item by voice.
- Displaying groups without a declared sorting rule.

## Effect profiles

`effect_profile` chooses normalized sound, light, and haptic behavior. It should
reflect the state transition, not the activity title.

```yaml
effect_profile:
  - calm_voice
  - choice_confirm
  - camera_collect
  - collect_success
  - count_twinkle
  - craft_step
  - mystery_reveal
  - story_unlock
  - sort_place
  - echo_memory
  - celebration
```

### `calm_voice`

Use for gentle, speech-led frames.

Good fits:

- Emotion and care.
- Voice-only explanation.
- Low-stimulation listening.
- Sensitive retry/no-response prompts.

Typical effects:

- SFX: soft chime or listening cue.
- Light: warm slow pulse.
- Haptic: none or tiny tick.

Avoid:

- Strong vibration.
- Loud success/failure sounds.
- Flashing or high-energy lights for empathy prompts.

### `choice_confirm`

Use for option focus and confirmation.

Good fits:

- Binary choice.
- Carousel choice.
- Direction choice.
- Number choice fallback, if no count-specific effect is needed.

Typical effects:

- SFX: quiet focus tick, confirm chime.
- Light: focus ring, success ring.
- Haptic: wheel tick, confirm pulse.

Avoid:

- Harsh wrong-answer buzzes.
- Making unsafe or incorrect options look scary.

### `camera_collect`

Use for photo capture and scan behavior.

Good fits:

- Cat5 capture.
- Photo collection.
- Any camera-driven evidence step.

Typical effects:

- SFX: shutter, scan sweep.
- Light: capture flash, scan line.
- Haptic: camera click.

Avoid:

- Using this when no camera action occurs.
- Treating capture as success before server verification when verification is required.

### `collect_success`

Use when a collected item is accepted and added to progress.

Good fits:

- Cat5 accepted object.
- Collection slot filled.
- Progress marker earned.

Typical effects:

- SFX: slot-fill chime.
- Light: collected slot glow, success ring.
- Haptic: success bump.

Avoid:

- Playing this before acceptance.
- Using a failure-like retry effect when the object is valid but needs more detail.

### `count_twinkle`

Use for counting and number reveal.

Good fits:

- Stars lighting up.
- Count-by-one progress.
- Number choice confirmation.

Typical effects:

- SFX: star ping or small count tick.
- Light: twinkle step, number lights up.
- Haptic: tiny tick per count or on confirmation.

Avoid:

- Long animations that slow down counting.
- Strong haptics for every counted item.

### `craft_step`

Use for making, drawing, or building progress.

Good fits:

- Guided drawing.
- Build steps.
- Add-a-part activities.

Typical effects:

- SFX: pencil swish, gentle done chime.
- Light: step highlight, progress dot glow.
- Haptic: soft confirm.

Avoid:

- Treating unfinished work as failure.
- Judging drawing quality unless the activity explicitly has safe criteria.

### `mystery_reveal`

Use for clues, masks, and gradual reveal.

Good fits:

- Partial reveal.
- Deduction clues.
- Hidden animal or object.

Typical effects:

- SFX: clue pop, reveal whoosh.
- Light: reveal wipe, clue ring.
- Haptic: clue tick.

Avoid:

- Scary suspense.
- Fully revealing the answer before the child gets a chance to guess.

### `story_unlock`

Use when a correct action unlocks a story gate, door, path, or scene.

Good fits:

- Story challenge unlock.
- Branching path confirmation.
- Gate/lock payoff.

Typical effects:

- SFX: lock chime, unlock chime.
- Light: gate glow, unlock burst.
- Haptic: confirm pulse.

Avoid:

- Overusing unlock effects on ordinary choice confirmation.
- Loud lock sounds that feel punitive.

### `sort_place`

Use when an item is placed into a group, basket, or category.

Good fits:

- Sort board.
- Classification baskets.
- Matching item to group.

Typical effects:

- SFX: item place chime.
- Light: target basket glow.
- Haptic: place bump.

Avoid:

- Playing success before the item is actually placed.
- Hiding the sorting rule.

### `echo_memory`

Use for repeat, echo, and memory-token progress.

Good fits:

- Word echo.
- Listen-and-repeat.
- Memory trail.

Typical effects:

- SFX: echo ping, listening cue.
- Light: listening ripple, memory token lit.
- Haptic: soft tick after prompt or token.

Avoid:

- Loud repetition cues.
- Treating speech recognition uncertainty as failure.

### `celebration`

Use for badge, recap, and completed activity payoff.

Good fits:

- Badge award.
- Final collection recap.
- Completion scene.

Typical effects:

- SFX: badge award, short celebration.
- Light: sparkle burst, success sweep.
- Haptic: celebration pulse.

Avoid:

- Long celebration loops.
- Triggering celebration for partial progress unless the frame is explicitly a
  mini-reward.

## Mechanic defaults

These defaults help generation choose a first pass. Always override them when
the round-level child action, option count, assets, or product constraints say
otherwise.

| `activity_signature.mechanic` | Default layout | Default control | Default effect | Notes |
|---|---|---|---|---|
| `enumerate` | `single_image` | `voice_only` | `count_twinkle` | Use `two_number_choice` only as a scaffold or fallback. |
| `compare` | `two_image_choice` or `multi_choice` | `binary_choice` or `carousel_choice` | `choice_confirm` | Choose by option count and assets. |
| `collect` | `single_image` | `camera_capture` | `camera_collect` | For Cat5 photo collection; accepted item uses `collect_success`. |
| `sort` | `multi_choice` | `sort_pick_place` | `sort_place` | Use only when groups/targets are declared. |
| `deduce` | `single_image` | `voice_only` or `reveal_control` | `mystery_reveal` | Reveal controls are optional. |
| `build` | `single_image` | `step_confirm` | `craft_step` | Use `Done` / `Not yet`; do not grade quality by default. |
| `predict` | `two_image_choice` | `binary_choice` | `choice_confirm` | Use voice-only when predictions are open-ended. |
| `decide` | `two_image_choice` or `two_direction_choice` | `binary_choice` | `choice_confirm` | Use direction layout for path choices. |
| `remember` | `single_image` | `replay_only` | `echo_memory` | Use choice layouts only for visible recognition choices. |
| `imagine` | `single_image` | `voice_only` | `story_unlock` | Use `two_direction_choice` when imagination is a path decision. |
| `care` | `single_image` | `voice_only` | `calm_voice` | Avoid tap/wheel prompts unless the product brief explicitly allows them. |
| `motion_voice` | `single_image` | `replay_only` | `calm_voice` | Voice/motion imitation should not become option selection. |

## Asset rules

- A choice layout requires declared choices.
- If a choice is visual, each option should bind to an `asset_manifest.yaml`
  `assets[].id`.
- If only `round_1_scene`, `round_2_scene`, or other scene assets exist, treat
  them as scene support, not selectable object cards.
- If the activity prose says the child can choose from cards, but the package
  lacks item assets, either add the missing assets or degrade the frame to
  `single_image` plus voice.
- Example or hint assets are not proof of a Cat5 find. Cat5 collection still
  needs `camera_capture` and server-side photo or spoken-label verification when
  the result depends on the real photographed object.
- Do not include UI chrome, masks, progress dots, wheel controls, or labels
  baked into source assets. The app renders those from the display contract.

## Validation rules

Package validation should eventually enforce these rules:

- `layout_type` must be one of the five approved layout values.
- `control_mode` and `effect_profile` must be one of the values in this guide.
- `binary_choice` requires exactly two `options`.
- `carousel_choice` requires at least three `options`.
- `sort_pick_place` requires at least one item option and at least one target or
  group declaration.
- `step_confirm` requires `done` and `not_yet` options.
- `camera_capture` should use `layout_type: single_image`.
- `two_number_choice` options must carry numeric values.
- `two_direction_choice` options must be direction/path choices.
- Any `asset_id` in `assets`, `options`, or `state` must exist in
  `asset_manifest.yaml`.
- `effect_profile: celebration` should be used only for completion, badge, recap,
  or explicit mini-reward frames.
- Empathy/care frames should not use wheel/tap answer controls unless the product
  brief explicitly approves them.

## Example mappings

Recognition with two choices, then three choices:

```yaml
frames:
  round_1:
    layout_type: two_image_choice
    control_mode: binary_choice
    effect_profile: choice_confirm
    options:
      - id: apple
        asset_id: apple
      - id: car
        asset_id: car
  round_2:
    layout_type: multi_choice
    control_mode: carousel_choice
    effect_profile: choice_confirm
    options:
      - id: apple
        asset_id: apple
      - id: strawberry
        asset_id: strawberry
      - id: cherries
        asset_id: cherries
```

Emotion care, voice-first:

```yaml
frames:
  round_1:
    layout_type: single_image
    control_mode: voice_only
    effect_profile: calm_voice
    assets:
      primary: round_1_scene
```

Cat5 collection:

```yaml
frames:
  round_1:
    layout_type: single_image
    control_mode: camera_capture
    effect_profile: camera_collect
    assets:
      primary: round_1_scene
      hint: ball
    state:
      capture_count: 0
      capture_target_count: 3
  round_1_accepted:
    layout_type: single_image
    control_mode: voice_only
    effect_profile: collect_success
    state:
      capture_count: 1
      capture_target_count: 3
```

Guided drawing:

```yaml
frames:
  round_2:
    layout_type: single_image
    control_mode: step_confirm
    effect_profile: craft_step
    assets:
      primary: round_2_scene
    options:
      - id: done
        label: Done
      - id: not_yet
        label: Not yet
    state:
      step_number: 2
      total_steps: 3
```

## Current package seed mapping

The current twelve migrated concept packages are only the seed set for this
taxonomy. The rules above should apply to future activities as defaults.

| Activity | Main layout | Main control | Main effect |
|---|---|---|---|
| `concept_phoneme_hunt_collect` | `single_image` | `camera_capture` | `camera_collect`, then `collect_success` |
| `concept_animal_sound_motion_voice` | `single_image` | `replay_only` | `calm_voice` |
| `concept_career_decision_decide` | `two_image_choice` | `binary_choice` | `choice_confirm` |
| `concept_constellation_star_count_enumerate` | `single_image`, fallback `two_number_choice` | `voice_only`, fallback `binary_choice` | `count_twinkle` |
| `concept_emotion_reader_care` | `single_image` | `voice_only` | `calm_voice` |
| `concept_guided_drawing_probe` | `single_image` | `step_confirm` | `craft_step` |
| `concept_partial_reveal_deduce` | `single_image` | `reveal_control` | `mystery_reveal` |
| `concept_recognition_pop_probe` | `two_image_choice` / `multi_choice` | `binary_choice` / `carousel_choice` | `choice_confirm` |
| `concept_story_unlock_probe` | `single_image`, optional `two_direction_choice` | `voice_only` or `binary_choice` | `story_unlock` |
| `concept_travel_planner_predict` | `two_image_choice` | `binary_choice` | `choice_confirm` |
| `concept_vegetable_sort_sort` | `multi_choice` | `sort_pick_place` | `sort_place` |
| `concept_word_echo_remember` | `single_image` | `replay_only` | `echo_memory` |

## Ownership

Autodesign should author the concrete display contract for each generated
package. WonderLens AI should validate, normalize, and emit the contract to the
app over Activity WebSocket.

Short-term implementation can seed WonderLens AI with fallback mappings for
existing packages. Long-term, generated packages should carry explicit display
metadata so the runtime does not infer layout from activity IDs or prose.
