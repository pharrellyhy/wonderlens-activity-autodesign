# Prompt Trace Audit - concept_phoneme_hunt_collect

Created: 2026-06-03
Run: `runs/20260603_110015_subset_agentic_validation`
Package: `activity_packages/concept_phoneme_hunt_collect`
Activity title: `B-Sound Treasure Hunt`

Purpose: list the package step instruction, the recorded downstream LLM prompt material, the package image description, and the recorded imagegen work-item prompt so the package can be manually checked from the beginning of the pipeline.

This audit does not regenerate assets and does not inspect a live provider request.

## Sources Reviewed

- Package production prompt: `runs/20260603_110015_subset_agentic_validation/activity_packages/concept_phoneme_hunt_collect/prod.md`
- Asset manifest: `runs/20260603_110015_subset_agentic_validation/activity_packages/concept_phoneme_hunt_collect/asset_manifest.yaml`
- Generated asset work items: `runs/20260603_110015_subset_agentic_validation/generated_assets/work_items/concept_phoneme_hunt_collect__*.md`
- Asset build output log: `runs/20260603_110015_subset_agentic_validation/generated_assets/asset_outputs.yaml`
- Fullstack export: `runs/20260603_110015_subset_agentic_validation/downstream_reports/fullstack_demo/exported_games/concept_phoneme_hunt_collect.md`
- WonderLens AI runtime package: `runs/20260603_110015_subset_agentic_validation/downstream_reports/wonderlens_ai/runtime_packages/concept_phoneme_hunt_collect/runtime.yaml`
- Source intent audit: `runs/20260603_110015_subset_agentic_validation/source_intent_audits/002_concept_phoneme_hunt_collect.md`

## Logging Limits

- Exact raw provider request payloads sent to the LLM were not found in this run. The closest recorded LLM prompt material is the converted `step_instructions` block in the fullstack export and WonderLens AI `runtime.yaml`.
- Exact raw `image_gen` API payloads were not found separately from the generated asset work items. The closest recorded image prompt material is each work item's `Prompt Or Source Requirement`, which mirrors the manifest `prompt_en`.
- Future runs should log provider request payloads when exact request-level audit is required.

## High-Signal Findings

1. The step-to-runtime LLM conversion mostly preserves the package `Runtime AI instruction` text. The WonderLens runtime and fullstack export both carry the same step goals under `step_instructions`.
2. The image prompts are text-only style prompts. They do not cite or embed the referenced style image/Markdown prompt files from the style-reference directory.
3. The image work items require generated 512x512 PNGs, but the resulting files are very small for 512x512 art, roughly 2.5 KB to 9 KB. This is a quality warning and should be checked visually.
4. Picker item/object assets are still built under package `assets/` paths, for example `assets/ball_object__round_512.png`, not under a separate `assets/items/` directory. This violates the hardened item-directory rule added after this package was produced.
5. The downstream fullstack export uses generic placeholder collection icons such as `/icons/green_apple.png`, not the package's `ball_object`, `banana_object`, `book_object`, and `cup_object` assets.
6. The WonderLens AI runtime has `asset_bindings: []`; its `collection_catalog` stores only accepted/rejected feature metadata, not item image bindings.
7. `celebrate_scene` is generated as a required story scene, but `prod.md` Step 4 uses `synthesis_scene`. The `celebrate_scene` image prompt says "Celebration scene" while its source beat context says `Use synthesis_scene`; this looks like inherited/mismatched prompt context.

## Step-by-Step Trace

### Step 1 - Transition Bridge

Instruction source in package:

```text
Goal: invite the child into Phoneme Treasure Hunt from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "Let us start B-Sound Treasure Hunt. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.hook.goal`
- Fullstack export: `step_instructions.hook.goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Intro scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `intro_scene` app-owned progress, choices, or camera slots are overlays and are not baked into the PNG. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/intro_scene__round_512.png`, 512x512, 5196 bytes.

### Step 2 - Rule Introduction

Instruction source in package:

```text
Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.transition.goal`
- Fullstack export: `step_instructions.transition.goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Rules scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `rules_scene`. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/rules_scene__round_512.png`, 512x512, 3654 bytes.

### Step 3 Round 1 - Hear The Target Sound

Instruction source in package:

```text
Goal: model the /b/ sound and show object examples without baked letters. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "Listen: /b/ like ball. Can you say /b/ with me?" Screen/state behavior: Use `round_1_scene`, optional object sprites, and the text-free `b_sound_letter_cue` backing only if the app overlays the actual `/b/` or B cue separately.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.rounds[0].goal`
- Fullstack export: `step_instructions.rounds[0].goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `round_1_scene`, optional object sprites, and the text-free `b_sound_letter_cue` backing only if the app overlays the actual `/b/` or B cue separately.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Round 1 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `round_1_scene` and optional object sprites app overlays any letter cue separately. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/round_1_scene__round_512.png`, 512x512, 3755 bytes.

### Step 3 Round 2 - Capture One Treasure

Instruction source in package:

```text
Goal: ask for one real photo_id of an indoor object whose spoken name starts with /b/. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "Find one treasure that starts with /b/. Take its picture, then tell me its name." Screen/state behavior: Use `round_2_scene`; app camera slot is separate from the PNG.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.rounds[1].goal`
- Fullstack export: `step_instructions.rounds[1].goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `round_2_scene`; app camera slot is separate from the PNG.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Round 2 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `round_2_scene` app camera slot is separate from the PNG. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/round_2_scene__round_512.png`, 512x512, 3687 bytes.

### Step 3 Round 3 - Name Evidence Check

Instruction source in package:

```text
Goal: judge the child-provided object name, not the image alone, and accept one B-sound treasure. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "You said ball. Ball begins with /b/. Treasure found." Screen/state behavior: Use `round_3_scene`; app overlays accepted photo/name evidence separately.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.rounds[2].goal`
- Fullstack export: `step_instructions.rounds[2].goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `round_3_scene`; app overlays accepted photo/name evidence separately.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Round 3 scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `round_3_scene` app overlays accepted photo/name evidence separately. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/round_3_scene__round_512.png`, 512x512, 3744 bytes.

### Step 4 - Synthesis And Magic Moment

Instruction source in package:

```text
Goal: synthesize the visual object and spoken name into a shared beginning-sound rule. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Do not end with generic completion; synthesize the collected evidence into a rule, summary, or story payoff. Example line: "Your photo and word worked together: ball belongs because it begins with /b/." Screen/state behavior: Use `synthesis_scene`; app overlays the accepted photo separately.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.celebrate.goal` and `step_instructions.synthesis.goal`
- Fullstack export: `step_instructions.celebrate.goal` and `step_instructions.synthesis.goal`
- Status: same instruction text as package Step 4, duplicated into both downstream `celebrate` and `synthesis` fields; exact provider request payload not logged.

Image description from package:

```text
Use `synthesis_scene`; app overlays the accepted photo separately.
```

Recorded imagegen work-item prompt for the step asset:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Synthesis scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `synthesis_scene` app overlays the accepted photo separately. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/synthesis_scene__round_512.png`, 512x512, 3842 bytes.

Related extra generated asset to review:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Celebration scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `synthesis_scene` app overlays the accepted photo separately. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Extra built asset: `assets/celebrate_scene__round_512.png`, 512x512, 3872 bytes.

Manual review concern: the extra prompt mixes "Celebration scene" with source context `Use synthesis_scene`.

### Step 5 - Closing + Concepts

Instruction source in package:

```text
Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Example line: "Today you practiced Form by using beginning sound evidence." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
```

Recorded downstream LLM prompt material:

- WonderLens AI: `step_instructions.closing.goal`
- Fullstack export: `step_instructions.closing.goal`
- Status: same instruction text as package `prod.md`; exact provider request payload not logged.

Image description from package:

```text
Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
```

Recorded imagegen work-item prompt:

```text
Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Closing scene for B-Sound Treasure Hunt. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `closing_scene`. Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects before the child supplies evidence. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.
```

Built asset: `assets/closing_scene__round_512.png`, 512x512, 3893 bytes.

## Non-Step Picker/Object Assets

These are needed because the activity has a picker/collection mechanic. They are separate asset IDs in the manifest, but this package writes them under the same `assets/` directory as scene assets.

### `ball_object`

Manifest role: `collection_correct`

Recorded imagegen work-item prompt:

```text
Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered round ball object for a beginning sound treasure. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites.
```

Built asset: `assets/ball_object__round_512.png`, 512x512, 3460 bytes.

### `banana_object`

Manifest role: `collection_correct`

Recorded imagegen work-item prompt:

```text
Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered curved banana object for a beginning sound treasure. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites.
```

Built asset: `assets/banana_object__round_512.png`, 512x512, 3618 bytes.

### `book_object`

Manifest role: `collection_correct`

Recorded imagegen work-item prompt:

```text
Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered closed book object for a beginning sound treasure. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites.
```

Built asset: `assets/book_object__round_512.png`, 512x512, 2581 bytes.

### `cup_object`

Manifest role: `collection_distractor`

Recorded imagegen work-item prompt:

```text
Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered plain cup object as a nonmatching sound contrast. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites.
```

Built asset: `assets/cup_object__round_512.png`, 512x512, 2972 bytes.

### `b_sound_letter_cue`

Manifest role: `ui_overlay`

Recorded imagegen work-item prompt:

```text
Use case: runtime-ui-backing. Asset type: WonderLens text-free overlay backing. Primary request: a blank cue-card backing for a runtime-owned target sound letter cue. Composition: single centered rounded square card or soft listening tile on a clean white background, no app UI; generate a 512x512 square source PNG; keep all details inside the central round-lens safe area. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, restrained boho pastels, soft sage and terracotta accents, light colored-pencil grain, airy negative space. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, device frame, circular mask, progress dots, buttons, chips, badges, or other app-owned interface state. The runtime may overlay /b/ or B text separately.
```

Built asset: `assets/b_sound_letter_cue__round_512.png`, 512x512, 9082 bytes.

Manual review concern: this is text-free and says runtime overlays `/b/` or B separately, but its role is `ui_overlay`; confirm whether it should be treated as runtime UI instead of generated activity art.

## Downstream Picker Catalog Trace

Fullstack export collection catalog:

```yaml
collection_catalog:
  correct:
  - id: green_apple
    label: Matching placeholder 1
    image: /icons/green_apple.png
  - id: dandelion
    label: Matching placeholder 2
    image: /icons/dandelion.png
  - id: ladybug
    label: Matching placeholder 3
    image: /icons/ladybug.png
  - id: smooth_pebble
    label: Matching placeholder 4
    image: /icons/smooth_pebble.png
  distractors:
  - id: straight_stick
    label: Distractor placeholder 1
    image: /icons/straight_stick.png
```

WonderLens AI runtime collection/catalog fields:

```yaml
asset_bindings: []
collection_catalog:
  accepted_features:
  - beginning sound evidence
  rejected_features: []
  visual_prompt_hint: Accept objects showing beginning sound evidence.
  criterion: Things with beginning sound evidence
```

Manual review concern: neither downstream file wires the manifest's item assets into the picker. If the runtime is supposed to show selectable item/object art, the problem appears to start in downstream conversion or binding, not in the manifest object prompts alone.

## Asset Output Summary

| Asset | Built path | Bytes | Manual review note |
| --- | --- | ---: | --- |
| `activity_icon` | `assets/activity_icon__round_512.png` | 3771 | Low byte count for 512x512; visually inspect. |
| `intro_scene` | `assets/intro_scene__round_512.png` | 5196 | Check no target objects or app UI baked in. |
| `rules_scene` | `assets/rules_scene__round_512.png` | 3654 | Check source-aligned visual context, not generic placeholder. |
| `round_1_scene` | `assets/round_1_scene__round_512.png` | 3755 | Check whether optional object sprites were incorrectly baked into the scene. |
| `round_2_scene` | `assets/round_2_scene__round_512.png` | 3687 | Check camera slot is not baked into the PNG. |
| `round_3_scene` | `assets/round_3_scene__round_512.png` | 3744 | Check accepted photo/name evidence is not baked into the PNG. |
| `synthesis_scene` | `assets/synthesis_scene__round_512.png` | 3842 | Check it reads as synthesis, not a generic ending. |
| `celebrate_scene` | `assets/celebrate_scene__round_512.png` | 3872 | Extra scene; prompt context mismatch with `synthesis_scene`. |
| `closing_scene` | `assets/closing_scene__round_512.png` | 3893 | Check final state has no badges, buttons, labels, or progress UI. |
| `ball_object` | `assets/ball_object__round_512.png` | 3460 | Should move to separate items directory in fresh run. |
| `banana_object` | `assets/banana_object__round_512.png` | 3618 | Should move to separate items directory in fresh run. |
| `book_object` | `assets/book_object__round_512.png` | 2581 | Should move to separate items directory in fresh run. |
| `cup_object` | `assets/cup_object__round_512.png` | 2972 | Should move to separate items directory in fresh run. |
| `b_sound_letter_cue` | `assets/b_sound_letter_cue__round_512.png` | 9082 | Confirm whether this belongs as generated art or app-owned UI. |

## Manual Verification Checklist

- Confirm whether raw provider payload logging is required before another live QA run.
- Confirm image prompts reference the approved style image/Markdown, not only a text phrase.
- Confirm each scene asset is visually distinct and tied to the exact beat.
- Confirm no scene bakes app UI, progress, picker slots, camera slots, badges, text, or labels.
- Confirm picker/object assets are generated as isolated items and stored under a separate items directory in a fresh package.
- Confirm downstream conversion binds `ball_object`, `banana_object`, `book_object`, and `cup_object` instead of generic placeholder icons.
- Confirm whether `celebrate_scene` should be removed, renamed, or given its own real step/source context.
