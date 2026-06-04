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
| `intro_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/intro_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `rules_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/rules_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `round_1_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_1_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `round_2_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_2_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `round_3_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/round_3_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `synthesis_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/synthesis_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `celebrate_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/celebrate_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |
| `closing_scene` | `generated_assets/inbox/concept_phoneme_hunt_collect/closing_scene.png` | Shared-stage prompt; exact accepted prompt recorded below. |

## Accepted Shared-Stage Scene Prompts

### `intro_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: intro_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child noticing the WonderLens device at the start of a sound hunt. The child is looking at the device with one hand cupped near the ear, waiting to hear the target sound. The room should feel searchable through open space and shelf placement, but do not show answer items. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, selectable target objects.
```

### `rules_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: rules_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child practicing the first sound with the WonderLens device. The child faces the device, mouth open in a clear speaking pose, with simple sound-wave arcs traveling from mouth to device. The device must be clearly visible as the listening partner. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, example objects used as answers, selectable target objects.
```

### `round_1_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: round_1_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show call-and-response sound practice before searching. The child leans toward the WonderLens device with one hand near the mouth and one near the ear, repeating the sound. Keep the focus on listening and speaking, not object selection. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, baked ball/book/banana/box examples, selectable target objects.
```

### `round_2_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: round_2_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child actively searching the playroom after hearing the sound. The child is standing or crouching near the shelf and rug, scanning the room with the WonderLens device in hand or nearby. The scene should clearly communicate: look around the room for a matching object. Do not show specific answer sprites like ball, banana, book, or box baked into the background. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, baked answer objects, selectable target objects.
```

### `round_3_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: round_3_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child speaking a found object's name toward the WonderLens device for checking. The child points naturally toward the clear unmarked open floor area beside the device where runtime can later overlay the actual item or photo. Do not draw the found object itself. Do not draw any outline, dotted oval, placeholder shape, slot, card, photo frame, or marked area. The action should read as: say its name to the listening device. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, any physical item object, specific answer objects such as ball, banana, book, box, selectable target objects.
```

### `synthesis_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: synthesis_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the WonderLens device connecting the child's spoken object name to the sound rule. The child speaks toward the device, the device listens, and one smooth sound ribbon connects the child's mouth to the device. The scene should read as spoken-name evidence being accepted through the sound ribbon only. No symbols, no checkmark, no badge, no letters, no labels, no item object, no photo. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, checkmarks, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, accepted photo, item objects, selectable target objects.
```

### `celebrate_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: celebrate_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child celebrating a successful sound hunt beside the WonderLens device. The celebration should be about listening and speaking success, with small sound-wave ribbons around the child and device, not generic sparkles around an unexplained object. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, item objects, selectable target objects.
```

### `closing_scene`

```text
Use case: illustration-story. Asset type: WonderLens activity scene background. Scene id: closing_scene. Shared stage: preschool child with brown hair, green sweater, blue pants, in a warm low-clutter playroom with window on the left, low shelf on the right, round rug in the center, one plant, and open floor only. No baskets, toy bins, loose toys, blocks, vehicles, books, or extra objects. The WonderLens device is a rounded rectangular handheld/tabletop tablet-like learning device with a teal rim, visible camera eye, small speaker marks, and a tiny stand; it must read as a device, not a flat circle, not a circular puck, not a coaster, not a button, and not a rug decoration. Primary request: Show the child calmly finishing the sound hunt with the WonderLens device still visible. The child sits relaxed beside the device. The room is settled, open, and quiet, and one faint sound-wave ribbon fades away from the device. No new search task starts. Style: flat Nordic children's illustration, broad flat color fills, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. Composition: 512x512 square source image, full-bleed scene, no app UI or frame. Avoid: readable text, letters, labels, numbers, logos, watermark, progress dots, buttons, badges, picker slots, baskets, treasure chests, blank cards, empty containers, generic glow-only subject, loose toys, item objects, selectable target objects.
```

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
