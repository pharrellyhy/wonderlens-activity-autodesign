# Fluffy Expedition Dandelion - Authoring Spec

> Migrated from `wonderlens-activity-fullstack-demo/backend/games/fluffy_expedition_dandelion.md` into the current activity package format.

## Premise

The dandelion becomes the first fluffy friend in a texture quest. In the demo-ready runtime, the child chooses three approved illustrated catalog cards that show soft, fuzzy, or fluffy textures, says the texture evidence out loud, gives each find a character name, and tells a tiny story about the fluffy friends meeting.

## Target

- **Template type:** cat5
- **Activity category:** Catalog Collection Exploration
- **Primary tier:** T0
- **Experience pillar:** Adventure
- **Game style:** `quest_collector`
- **Mechanic:** `collect`
- **Observation angle:** `texture`
- **Entity role:** `exemplar`

## Pedagogical Rationale

The original demo used naming_story. This conversion keeps the Adventure / quest_collector lineage, but changes the runtime contract from open-world tactile collection to supported catalog collection. The child still practices texture language, comparison, naming, and Connection, while the demo stays honest: it displays approved soft-texture cards and relies on the child's spoken evidence instead of camera intake, tactile sensing, or automated visual judgment.

## Selection Trigger

Use when the handoff or assignment targets `fluffy_soft_texture`, or when the authored dandelion exemplar is explicitly selected. Do not start this package for arbitrary texture properties unless an approved catalog with at least three correct cards exists.

## Demo Conversion Notes

This package is now a supported Cat5 catalog collection. The dandelion seed puff is the first exemplar, and the runtime catalog supplies additional soft-looking items such as fuzzy moss, woolly yarn, and a soft feather. The child chooses cards, explains the visible texture clue, and names each fluffy friend.

The package must not claim to verify real-world touch, arbitrary camera photos, or whether a child actually found a soft object nearby. If production later supports real camera/tactile verification, that should be added as a separate path with its own capability record.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `activity_icon` | icon | required | pre_generated | prod.step_2 | activity_preview | Show the expedition identity with a dandelion/fluffy texture motif. | See `asset_manifest.yaml`. | Display as the package icon and mission badge seed. | Use neutral Adventure badge treatment and voice-only title. | No text, letters, numbers, brands, watermark, insects close-up, or unsafe touching cues. |
| `intro_scene` | scene_background | required | pre_generated | prod.step_1 | round_device_screen | Establish the dandelion seed puff as the first fluffy exemplar. | See `asset_manifest.yaml`. | Display behind the opening wonder prompt. | Use voice-only intro with neutral background. | No readable text, no realistic allergens or medical claims. |
| `rules_scene` | scene_background | required | pre_generated | prod.step_2 | round_device_screen | Explain that the child will choose soft-looking catalog cards. | See `asset_manifest.yaml`. | Display during rule introduction. | Use simple card grid UI without decorative scene art. | No baked app chrome or text inside the art. |
| `round_1_scene` | scene_background | required | pre_generated | prod.step_3.round_1 | round_device_screen | Support the first soft-texture card choice. | See `asset_manifest.yaml`. | Display behind or beside the card spread. | Keep cards visible and guide by voice. | No unsafe touch instruction, no unsupported verification claim. |
| `round_2_scene` | scene_background | required | pre_generated | prod.step_3.round_2 | round_device_screen | Support texture comparison between selected cards. | See `asset_manifest.yaml`. | Display during second selection. | Keep selected card thumbnails visible and guide by voice. | No camera/photo claim. |
| `round_3_scene` | scene_background | required | pre_generated | prod.step_3.round_3 | round_device_screen | Support final fluffy friend naming. | See `asset_manifest.yaml`. | Display during third selection. | Use neutral completion screen and voice. | No unsupported tactile sensing. |
| `synthesis_scene` | scene_background | required | pre_generated | prod.step_4 | round_device_screen | Turn selected cards into a tiny fluffy-friend story. | See `asset_manifest.yaml`. | Display after all three catalog choices. | Use selected-card thumbnails and spoken synthesis. | No text baked into the art. |
| `celebrate_scene` | icon | required | pre_generated | prod.step_4 | badge_area | Award the Fluffy Expedition Explorer badge. | See `asset_manifest.yaml`. | Display as a badge after synthesis. | Use generic celebration treatment. | No readable text or logos. |
| `closing_scene` | scene_background | required | pre_generated | prod.step_5 | round_device_screen | Recap Connection through shared fluffy texture. | See `asset_manifest.yaml`. | Display during closing recap. | Close with selected-card thumbnails only. | No text baked into the art. |
| `fluffy_dandelion_puff`, `fuzzy_moss_patch`, `woolly_yarn_ball`, `soft_feather` | card_set | required | pre_generated | prod.step_3 | catalog_grid | Provide correct soft/fluffy catalog cards. | See `asset_manifest.yaml`. | Present as selectable card assets for the collection loop. | Do not start the catalog if fewer than three correct cards are available. | Gentle, clean item cards; no unsafe touching cues or realistic insect close-up. |
| `smooth_pebble`, `plain_wood_block` | card_set | optional | pre_generated | prod.step_3 | catalog_grid | Provide non-target distractors for comparison. | See `asset_manifest.yaml`. | Present only when the UI wants simple contrast cards. | Hide unavailable distractors. | Do not imply rough or hard items are bad or unsafe. |

## Asset Usage Timeline

| asset_id | timing | load/generate moment | first display | visible range | location | interaction/use | persistence/hide behavior | fallback |
|---|---|---|---|---|---|---|---|---|
| `activity_icon` | pre_generated | Load before package preview. | prod.step_2 | prod.step_2; prod.step_4 | activity_preview; badge_area | Identifies the mission and badge. | Hide when full scene or selected cards take focus. | Neutral Adventure badge. |
| `intro_scene` | pre_generated | Load before Step 1. | prod.step_1 | prod.step_1 | round_device_screen | Establishes dandelion fluff. | Replace with rules scene in Step 2. | Voice-only intro. |
| `rules_scene` | pre_generated | Load before Step 2. | prod.step_2 | prod.step_2 | round_device_screen | Introduces card collection rule. | Replace with round scene and catalog grid. | Plain card grid. |
| `round_1_scene` | pre_generated | Load before Step 3. | prod.step_3.round_1 | prod.step_3.round_1 | round_device_screen | Frames first card choice. | Keep selected card in slot after round. | Voice-guided card choice. |
| `round_2_scene` | pre_generated | Load before Step 3 round 2. | prod.step_3.round_2 | prod.step_3.round_2 | round_device_screen | Frames comparison. | Keep first two selected cards in slots. | Voice-guided comparison. |
| `round_3_scene` | pre_generated | Load before Step 3 round 3. | prod.step_3.round_3 | prod.step_3.round_3 | round_device_screen | Frames final choice and name. | Replace with synthesis after selection. | Voice-guided final choice. |
| `synthesis_scene` | pre_generated | Load after third correct selection. | prod.step_4 | prod.step_4 | round_device_screen | Turns selected cards into story characters. | Persist selected cards until closing. | Spoken synthesis over thumbnails. |
| `celebrate_scene` | pre_generated | Load after synthesis response. | prod.step_4 | prod.step_4 | badge_area | Shows earned badge. | Hide or shrink during closing. | Generic badge. |
| `closing_scene` | pre_generated | Load before Step 5. | prod.step_5 | prod.step_5 | round_device_screen | Recaps texture Connection. | End of activity. | Spoken recap only. |
| catalog item cards | pre_generated | Load before Step 3. | prod.step_3.round_1 | prod.step_3.round_1-3; prod.step_4 | catalog_grid; selected_slots | Child selects correct soft/fluffy cards and gives evidence. | Move selected cards into collection slots; hide unused distractors at synthesis. | Do not start if fewer than three correct cards are available. |

## Extensibility Notes

- Retarget only to texture properties that have approved catalog cards with at least three correct exemplars.
- Preserve `fluffy_soft_texture` as the authored default for the dandelion exemplar.
- Do not convert this package into open-ended real-world texture judging without a separate verified runtime capability.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `activities/README.md`, and `docs/game_styles.md`.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Uses approved catalog cards and child-stated evidence. It does not require camera capture, tactile sensing, OCR, face/pose detection, IMU sensing, audio-quality scoring, or before/after state verification. |
| 2 | Hook & Transition | PASS | Step 1 grows from the dandelion exemplar and opens with wonder before introducing the catalog mission. |
| 3 | Edge Case Coverage | PASS | Every runtime dialogue step includes ideal, unexpected, and no-response paths with wait-time prompts and Cat5 scaffold handling. |
| 4 | IB Completeness | PASS | The package defines key concepts, related concepts, KUD, ATL skills, and a closing that names Connection through the child's selected examples. |
| 5 | Tier Appropriateness | PASS | Rounds are short, concrete, card-based, and matched to T0/T1 children. |
| 6 | Dialogue Specificity | PASS | AI lines, child branches, and follow-ups are concrete enough to run without inventing missing beats. |
| 7 | Screen & UI Completeness | PASS | Each step has a specific screen state, progress treatment, catalog-card behavior, and asset fallback. |
| 8 | Entity Mapping Alignment | N/A | This is a demo-source migration, not a mapping-informed assignment requiring entity YAML grounding. |
| 9 | Game Feel | PASS | The activity has a role title, visible progress, differentiated rounds, naming, synthesis, and an earned badge. |
| 10 | Pillar Fidelity | PASS | The Adventure quest_collector structure remains intact while replacing unsupported open-world collection with a runnable catalog loop. |

**Overall**: ALL PASS - direct demo migration is structurally valid, demo-runnable, and honest about current runtime capabilities.
