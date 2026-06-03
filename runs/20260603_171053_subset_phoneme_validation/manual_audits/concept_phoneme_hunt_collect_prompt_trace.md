# Prompt Trace: `concept_phoneme_hunt_collect`

Run id: `20260603_171053_subset_phoneme_validation`

## Scope

This trace compares:

- package runtime step instructions in `activity_packages/concept_phoneme_hunt_collect/prod.md`;
- downstream LLM/runtime prompt material, when available;
- package image descriptions in `asset_manifest.yaml`;
- exact accepted prompts sent to Codex built-in `image_gen`;
- generated source files copied into `generated_assets/inbox/concept_phoneme_hunt_collect/`.

No secrets or provider credentials are included.

## Runtime Step Instruction Trace

Downstream deterministic conversion has now run. No live child-session LLM call was made in this validation run; the "actual prompt material" below is the generated runtime instruction material that WonderLens AI and fullstack export would feed into runtime prompt composition.

| Runtime step | Package instruction source | Package instruction summary | Downstream prompt material |
|---|---|---|---|
| Step 1 Transition Bridge | `prod.md` Step 1 `Runtime AI instruction` | Open with playful sound-basket hook; introduce one sound treasure; do not quiz or claim image-only phoneme judgment. | WLAI runtime `downstream_reports/wonderlens_ai/activities/concept_phoneme_hunt_collect/runtime.yaml` `step_instructions.hook.goal`; fullstack export `downstream_reports/fullstack_demo/fullstack_export/concept_phoneme_hunt_collect.md`. |
| Step 2 Target Sound Rule | `prod.md` Step 2 `Runtime AI instruction` | Model `/b/ /b/ /b/`; optional text-free cue backing with app-owned overlay; voice-only fallback if overlay is unavailable. | WLAI runtime `step_instructions.transition.goal`; preserves voice-only fallback and app-owned `/b/` overlay guardrail. |
| Step 3 Round 1 | `prod.md` Round 1 `Runtime AI instruction` | Practice `/b/` once before search; do not require letter reading; do not bake examples into scene background. | WLAI runtime `step_instructions.rounds[0].goal`; fullstack package import keeps picker object sprites out of scene backgrounds. |
| Step 3 Round 2 | `prod.md` Round 2 `Runtime AI instruction` | Ask child to find exactly one indoor `/b/` treasure, show/photo it, and say its name. | WLAI runtime `step_instructions.rounds[1].goal`; preserves one-treasure search and no image-only phoneme inference. |
| Step 3 Round 3 | `prod.md` Round 3 `Runtime AI instruction` | Judge the child-provided object name against `/b/`, not image pixels alone. | WLAI runtime `step_instructions.rounds[2].goal`; preserves child-provided word evidence and accepted-photo/name overlay separation. |
| Step 4 Synthesis | `prod.md` Step 4 `Runtime AI instruction` | Connect accepted photo/name to the beginning-sound rule; no new required task. | WLAI runtime `step_instructions.synthesis.goal` and `step_instructions.celebrate.goal`; both preserve the shared beginning-sound rule payoff. |
| Step 5 Closing | `prod.md` Step 5 `Runtime AI instruction` | Celebrate first, then name Form and Connection; recap exact source action. | WLAI runtime `step_instructions.closing.goal`; preserves exact recap of AI introducing `/b/`, child finding one indoor treasure, child naming it, and AI connecting word to sound. |

## Imagegen Common Prompt Context

Every accepted image used Codex built-in `image_gen`, not SVG/vector/script output.

Each accepted prompt began with:

```text
Use the displayed style reference image and repo style brief `docs/asset_style_reference/wonderlens-activity-style.md` as the visual target.
```

The displayed reference image was:

```text
docs/asset_style_reference/style-reference-flat-nordic.png
```

All accepted generated sources were copied from:

```text
/Users/pharrelly/.codex/generated_images/019e8b62-1b0f-7af2-b322-8a6a004dc9a0/
```

and resized locally to exactly 512x512 before asset build.

## Accepted Imagegen Prompts

### `activity_icon`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/activity_icon.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens activity preview icon
Primary request: a single centered EMPTY soft treasure basket icon with three tiny abstract sound-wave marks above it. No items inside the basket.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, airy negative space, simple organic silhouette.
Composition/framing: one icon only, centered, generous padding, safe inside round device crop.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no border, no app UI, no progress dots, no camera slot, no contact sheet, no circular mask. Do not include any household objects or target/distractor objects: no books, no balls, no bananas, no cups, no boxes, no bags, no toys, no tools, no instruments, no plants.
```

### `intro_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/intro_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: quiet abstract indoor listening corner with one EMPTY soft treasure basket and gentle sound-spark shapes. Do not show shelves or any findable objects.
Scene/backdrop: airy nursery room made only of simple wall, floor, curtain, rug, and color-field shapes.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, generous negative space.
Composition/framing: full-bleed square scene, important elements centered and safe inside a round device crop.
Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no border, no app UI, no progress dots, no camera slot, no selectable objects, no contact sheet, no circular mask. Do not include household objects or target/distractor objects: no books, no balls, no bananas, no cups, no boxes, no bags, no shelves, no toys, no tools, no plants.
```

### `rules_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/rules_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: abstract text-free sound rule scene for a child listening to a beginning sound. Show only an empty soft basket, gentle abstract sound waves, and a blank rounded cue area.
Scene/backdrop: clean airy indoor nursery color field with simple wall/floor shapes only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, generous negative space.
Composition/framing: full-bleed square scene, important details inside central round safe area.
Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no app UI, no buttons, no progress dots, no camera slot, no contact sheet, no circular mask. Do not include any household objects or target/distractor objects: no books, no balls, no bananas, no cups, no boxes, no bags, no shelves, no toys, no plants.
```

### `round_1_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/round_1_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: abstract sound-practice scene before searching: one blank cue-card backing, one EMPTY treasure basket, and soft listening waves only. No example objects.
Scene/backdrop: soft indoor nursery color field with simple wall/floor/rug shapes only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, generous negative space.
Composition/framing: full-bleed square scene, centered and safe inside round device crop.
Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no app UI, no camera slot, no picker slots, no progress dots, no contact sheet, no circular mask. Do not include any target/distractor or household objects: no books, no balls, no bananas, no cups, no boxes, no bags, no shelves, no toys, no tools, no plants.
```

### `round_2_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/round_2_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: open indoor search path with an empty collection basket waiting for one treasure; it should feel like a child can go look around the room, but no actual findable object is shown.
Scene/backdrop: airy nursery room made of simple abstract wall, floor, and path shapes only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, generous negative space.
Composition/framing: full-bleed square scene, central safe area clear for app camera overlay.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no border, no app UI, no camera slot baked in, no picker objects, no progress markers, no contact sheet, no circular mask. Do not include target or distractor objects: no books, no balls, no bananas, no cups, no boxes, no bags, no shelves, no toys, no plants.
```

### `round_3_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/round_3_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: evidence acceptance scene with ONLY an empty woven basket and a small soft acceptance glow or sparkle near it. The scene should leave open negative space for runtime overlays, but must not draw any card, photo slot, panel, rectangle, frame, placeholder, or UI shape.
Scene/backdrop: clean indoor surface with abstract pastel floor and wall color fields only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, airy negative space.
Composition/framing: full-bleed square, central safe area clear, no actual object photo.
Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no app UI, no picker slots, no progress dots, no contact sheet, no circular mask. No blank rounded card, no photo slot, no rectangle panel, no framed placeholder, no border. Do not include target or distractor objects: no books, no balls, no bananas, no cups, no boxes, no bags, no shelves, no toys, no plants.
```

### `synthesis_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/synthesis_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: synthesis scene where one abstract treasure shape joins a soft sound wave into an empty basket, representing object plus spoken name becoming one beginning-sound rule.
Scene/backdrop: airy white indoor background with simple wall/floor color fields only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, airy negative space.
Composition/framing: full-bleed square, central safe area, gentle magic moment without UI.
Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no app UI, no accepted photo baked in, no target/distractor objects, no contact sheet, no circular mask. Do not include books, balls, bananas, cups, boxes, bags, shelves, toys, or plants.
```

### `celebrate_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/celebrate_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: calm celebration sparkle around a soft empty basket after a child completed one sound treasure hunt. Keep it abstract and source-aligned.
Scene/backdrop: warm clean indoor setting with simple wall/floor color fields only.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, airy negative space.
Composition/framing: full-bleed square, safe inside round device crop, no UI badge.
Constraints: no readable text, no letters, no numbers, no badges, no labels, no logos, no watermark, no buttons, no app UI, no progress dots, no duplicate picker objects, no contact sheet, no circular mask. Do not include books, balls, bananas, cups, boxes, bags, shelves, toys, or plants.
```

### `closing_scene`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/closing_scene.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: WonderLens runtime beat scene
Primary request: resting sound basket with one abstract glow, calm closing state after the sound hunt. No new task or extra objects.
Scene/backdrop: clean white airy nursery color field.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse tiny texture strokes, light colored-pencil grain, restrained boho pastels, generous negative space.
Composition/framing: full-bleed square, centered calm composition safe inside round crop.
Constraints: no readable text, no letters, no numbers, no badges, no labels, no logos, no watermark, no buttons, no app UI, no progress dots, no target/distractor objects, no contact sheet, no circular mask. Do not include books, balls, bananas, cups, boxes, bags, shelves, toys, or plants.
```

### `b_sound_letter_cue`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/b_sound_letter_cue.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: text-free cue-card backing
Primary request: one centered blank rounded cue card or listening tile for a runtime-owned target sound overlay. The generated image itself must contain no letters or words.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference, with restrained boho pastels, soft sage and terracotta accents, broad flat color fills, light paper grain, generous negative space.
Composition/framing: one centered card or tile only, generous padding, safe inside round crop.
Constraints: absolutely no readable text, no letters, no numbers, no symbols, no labels, no logos, no watermark, no app UI, no border, no progress dots, no contact sheet, no circular mask.
```

### `ball_object`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/ball_object.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: collection item sprite
Primary request: one centered round ball object as a correct /b/ beginning-sound example; no other objects.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse short texture strokes, light colored-pencil grain, restrained boho pastels, muted sage, dusty teal-blue, soft terracotta, warm ochre accents.
Composition/framing: one object only, centered with generous padding, safe inside round crop.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no app UI, no border, no contact sheet, no shadow-heavy realism, no extra objects, no circular mask.
```

### `banana_object`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/banana_object.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: collection item sprite
Primary request: one centered curved banana object as a correct /b/ beginning-sound example; no other objects.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse short texture strokes, light colored-pencil grain, restrained boho pastels, muted ochre banana with soft green-brown accents.
Composition/framing: one object only, centered with generous padding, safe inside round crop.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no app UI, no border, no contact sheet, no shadow-heavy realism, no extra objects, no circular mask.
```

### `book_object`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/book_object.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: collection item sprite
Primary request: one centered closed book object as a correct /b/ beginning-sound example. The book cover must be blank, with no readable marks.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse short texture strokes, light colored-pencil grain, restrained boho pastels, muted salmon and dusty blue cover shapes.
Composition/framing: one object only, centered with generous padding, safe inside round crop.
Constraints: no readable text, no letters, no numbers, no symbols, no logos, no watermark, no app UI, no border, no contact sheet, no shadow-heavy realism, no extra objects, no circular mask.
```

### `cup_object`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/cup_object.png
```

Actual accepted prompt body:

```text
Use case: illustration-story
Asset type: collection item sprite
Primary request: one centered plain cup object as a nonmatching sound contrast; no other objects.
Scene/backdrop: clean white.
Style/medium: flat Nordic children's illustration matching the reference: broad flat color fills, sparse short texture strokes, light colored-pencil grain, restrained boho pastels, muted sage ceramic and soft terracotta accent.
Composition/framing: one object only, centered with generous padding, safe inside round crop.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no app UI, no border, no contact sheet, no shadow-heavy realism, no extra objects, no circular mask.
```

### `sock_object`

Accepted source:

```text
runs/20260603_171053_subset_phoneme_validation/generated_assets/inbox/concept_phoneme_hunt_collect/sock_object.png
```

Actual accepted prompt body:

```text
Create a 512x512 square PNG source asset for a WonderLens child activity.
Asset type: collection item sprite.
Primary request: one centered soft sock object as a nonmatching /b/ sound contrast; no other objects.
Scene/backdrop: clean white.
Style: flat Nordic children's illustration matching a quiet white WonderLens prototype, with broad flat color fills, sparse pencil-grain texture, restrained boho pastels, warm porcelain background, muted sage, dusty teal-blue, soft terracotta accents, airy negative space, organic simple silhouette.
Composition: one sock only, centered with generous padding, safe inside a circular crop.
Constraints: no readable text, no letters, no numbers, no logos, no watermark, no app UI, no border, no contact sheet, no cards, no device frame, no picker slot, no progress marker.
```

## Rejected Imagegen Drafts

- `rules_scene`: the first draft included bookshelf-like objects, so it was rejected and replaced.
- `activity_icon`: the first draft included multiple object-like contents in the basket, so it was rejected and replaced.
- `intro_scene`: an earlier draft included object-like room details, so it was rejected and replaced.
- `round_1_scene`: an earlier draft included shelf/book shapes, so it was rejected and replaced.
- `round_3_scene`: an earlier draft included a blank rounded card/photo-slot shape, so it was rejected and replaced.
