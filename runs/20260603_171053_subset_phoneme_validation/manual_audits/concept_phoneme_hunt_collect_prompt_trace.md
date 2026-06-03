# Prompt Trace: `concept_phoneme_hunt_collect`

Run id: `20260603_171053_subset_phoneme_validation`

## Scope

This trace compares:

- package runtime step instructions in `activity_packages/concept_phoneme_hunt_collect/prod.md`;
- downstream deterministic runtime/export prompt material;
- package image descriptions in `asset_manifest.yaml`;
- image generation evidence for sources copied into
  `generated_assets/inbox/concept_phoneme_hunt_collect/`.

No secrets or provider credentials are included.

## Runtime Step Instruction Trace

Downstream deterministic conversion has run after repair. No live child-session
LLM call was made in this validation run; the "downstream prompt material" below
is the generated runtime instruction material that WonderLens AI and fullstack
export would feed into runtime prompt composition.

| Runtime step | Package instruction source | Package instruction summary | Downstream prompt material |
|---|---|---|---|
| Step 1 Transition Bridge | `prod.md` Step 1 `Runtime AI instruction` | Open with a playful listening-lens hook; introduce one sound treasure; do not quiz or claim image-only phoneme judgment. | WLAI runtime `downstream_reports/wonderlens_ai/activities/concept_phoneme_hunt_collect/runtime.yaml` `step_instructions.hook.goal`; fullstack export `downstream_reports/fullstack_demo/fullstack_export/concept_phoneme_hunt_collect.md`. |
| Step 2 Target Sound Rule | `prod.md` Step 2 `Runtime AI instruction` | Model `/b/ /b/ /b/`; optional text-free listening support with app-owned overlay; voice-only fallback if overlay is unavailable. | WLAI runtime `step_instructions.transition.goal`; preserves voice-only fallback and app-owned `/b/` overlay guardrail. |
| Step 3 Round 1 | `prod.md` Round 1 `Runtime AI instruction` | Practice `/b/` once before search; do not require letter reading; do not bake examples into scene background. | WLAI runtime `step_instructions.rounds[0].goal`; fullstack export keeps item sprites out of scene backgrounds. |
| Step 3 Round 2 | `prod.md` Round 2 `Runtime AI instruction` | Ask child to find exactly one indoor `/b/` treasure, show/photo it, and say its name. | WLAI runtime `step_instructions.rounds[1].goal`; preserves one-treasure search and no image-only phoneme inference. |
| Step 3 Round 3 | `prod.md` Round 3 `Runtime AI instruction` | Judge the child-provided object name against `/b/`, not image pixels alone. | WLAI runtime `step_instructions.rounds[2].goal`; preserves child-provided word evidence and accepted-photo/name overlay separation. |
| Step 4 Synthesis | `prod.md` Step 4 `Runtime AI instruction` | Connect accepted photo/name to the beginning-sound rule; no new required task. | WLAI runtime `step_instructions.synthesis.goal` and `step_instructions.celebrate.goal`; both preserve the shared beginning-sound rule payoff. |
| Step 5 Closing | `prod.md` Step 5 `Runtime AI instruction` | Celebrate first, then name Form and Connection; recap exact source action. | WLAI runtime `step_instructions.closing.goal`; preserves exact recap of AI introducing `/b/`, child finding one indoor treasure, child naming it, and AI connecting word to sound. |

## Imagegen Evidence

Every newly accepted or repaired source used Codex built-in `image_gen`, not
SVG, vector, placeholder, or script-generated substitute art. The built-in tool
saves generated files under:

```text
/Users/pharrelly/.codex/generated_images/019e8e3b-d03b-76a1-afe0-bad2264c6ace/
```

Provider-payload note: the built-in image tool does not expose a serialized
provider request payload or request id in the workspace. The prompts below are
the agent-recorded prompt text submitted through the built-in tool; accepted
outputs were copied into the run inbox and resized to 512x512 before build.

Review contact sheet:

```text
runs/20260603_171053_subset_phoneme_validation/image_qa/source_contact_sheet.png
```

## Regenerated Scene And Support Sources

| Asset | Accepted inbox source | Submitted prompt record |
|---|---|---|
| `activity_icon` | `generated_assets/inbox/concept_phoneme_hunt_collect/activity_icon.png` | Activity preview icon for B-Sound Treasure Hunt: child profile making sound waves toward a magnifying-glass search path and indoor search spark; flat Nordic style; no text, letters, UI, frame, circular mask, answer objects, or placeholder subject. |
| `b_sound_letter_cue` | `generated_assets/inbox/concept_phoneme_hunt_collect/b_sound_letter_cue.png` | Text-free listening support pictogram: centered unframed mouth-and-sound-wave cue for runtime-owned sound overlay; no card, tile, frame, text, letters, numbers, UI, dots, or container motif. |
| `intro_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/intro_scene.png` | Intro story scene: preschool child in a simple indoor room, seated near a small listening lens with hand cupped to ear before the target sound is named; flat Nordic room with rug, window, bare shelf; no visible catalog objects, text, UI, frame, or container motif. |
| `rules_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/rules_scene.png` | Rules scene: same child faces the listening lens and practices a beginning sound by voice; mouth cue and sound-wave arcs move from child to lens; no letters, example objects, card, panel, text, UI, or container motif. |
| `round_1_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_1_scene.png` | Practice scene: same child leans toward the lens with one hand near mouth and one near ear, repeating the beginning sound; sound-wave arcs show call-and-response; no baked ball/book/banana/box or other item examples. |
| `round_2_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_2_scene.png` | Search scene: same child safely searches the room, looking toward bare shelf/open floor while a subtle sound-wave trail guides the hunt; no answer object, camera UI, picker slot, text, or container motif. |
| `round_3_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_3_scene.png` | Evidence-check scene: child speaks toward the listening lens with smooth sound-wave arcs; small unframed open space is left for runtime photo/name overlay; no actual photo, card, panel, dots, text, or item object. |
| `synthesis_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/synthesis_scene.png` | Synthesis scene: child and lens share a smooth sound-wave ribbon; spoken-name evidence gathers into one beginning-sound pattern near the lens; no accepted photo, letters, labels, or item objects. |
| `celebrate_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/celebrate_scene.png` | Celebration scene: child smiles and cheers beside the listening lens while sound-wave ribbons celebrate listening/speaking success; no badge, button, text, item objects, or container motif. |
| `closing_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/closing_scene.png` | Closing scene: child sits calmly beside the listening lens after the sound hunt; a fading sound-wave ribbon shows the activity ending; no fresh task, app UI, text, or item objects. |

## New Catalog-Parity Sources

| Asset | Accepted inbox source | Submitted prompt record |
|---|---|---|
| `box_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/box_object.png` | One centered plain box object for a correct beginning-/b/ item; clean white background; flat Nordic style; no text, letters, numbers, symbols, shipping marks, UI, border, or extra objects. |
| `apple_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/apple_object.png` | One centered apple object as a nonmatching sound contrast; clean white background; flat Nordic style; no text, letters, numbers, symbols, UI, border, or extra objects. |
| `car_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/car_object.png` | One centered simple toy car object as a nonmatching sound contrast; clean white background; flat Nordic style; no text, letters, numbers, symbols, UI, border, or extra objects. |
| `hat_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/hat_object.png` | One centered soft hat object as a nonmatching sound contrast; clean white background; flat Nordic style; no text, letters, numbers, symbols, UI, border, or extra objects. |
| `mug_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/mug_object.png` | One centered plain mug object as a nonmatching sound contrast; clean white background; flat Nordic style; no steam, text, letters, numbers, symbols, UI, border, or extra objects. |
| `shoe_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/shoe_object.png` | One centered simple shoe object as a nonmatching sound contrast; clean white background; flat Nordic style; no text, letters, numbers, symbols, UI, border, or extra objects. |
| `spoon_object` | `generated_assets/inbox/concept_phoneme_hunt_collect/spoon_object.png` | One centered simple spoon object as a nonmatching sound contrast; clean white background; flat Nordic style; no text, letters, numbers, symbols, UI, border, or extra objects. |

## Retained Item Sources

These existing item sources were retained after visual inspection because they
are centered, text-free, and semantically readable:

- `ball_object`
- `banana_object`
- `book_object`
- `cup_object`
- `sock_object`

Their current package requirements are recorded in
`activity_packages/concept_phoneme_hunt_collect/asset_manifest.yaml`, and their
built runtime variants are included in `generated_assets/asset_outputs.yaml`.
