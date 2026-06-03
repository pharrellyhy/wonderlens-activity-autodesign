# B-Sound Treasure Hunt Spec

## Premise

The activity turns a beginning sound into a one-object scavenger hunt. The AI introduces `/b/`, the child finds one indoor treasure, and the accepted evidence is the combination of a real object/photo plus the child's spoken or typed object name.

## Target

- Activity ID: `concept_phoneme_hunt_collect`
- Source concept: `Phoneme Treasure Hunt`
- Source baseline: `inputs/original_activity_concepts_2026-05-29.tsv`
- Normalized helper: `inputs/source_activity_concepts.md#source_phoneme_hunt`
- Template type: `cat5`
- Pillar / Game Style: Adventure / `quest_collector`
- Canonical mechanic: `collect`
- Primary tier: T1
- Demo support status: `degraded`

## Adaptation Rationale

- **Core promise:** The AI introduces a target beginning sound, then the child finds one object whose word starts with that sound.
- **Workbook lock:** The target sound for this run is `/b/ /b/ /b/`, and the child is asked to find one such "treasure" to show the device.
- **Input mode:** `parameterized`; no entity mapping is needed because the package is a reusable language pattern.
- **Canonical mechanic:** `collect`; the repeated action is find/show/name one matching treasure.
- **Category:** Cat5 because the child searches the room and uses a photo/show action outside the device conversation.
- **Readiness:** `generate_with_assumptions`; current V1 cannot infer a beginning phoneme from an image alone, so the runtime asks the child to name the object.
- **Source-promise alignment:** aligned. The runtime sequence remains sound first, then search, then photo/show, then name/evidence check.
- **Scaffold choice:** Adventure / `quest_collector` gives the child a small mission without changing the sound-matching mechanic.
- **Mapping use:** not mapping-informed.
- **Asset dependency:** optional letter support plus required full-pass scene and item assets for the demo. The letter cue is handled as an app-owned `/b/` or B overlay on a generated text-free backing, or voice-only fallback.
- **Consumer boundary:** downstream consumers must load/convert this package as written. LLM-assisted rewrites are not acceptable evidence that the package is strong enough.

## Resolved Product Contract Notes

- Beginning-sound judgment is product-sensitive because a still image alone does not provide phoneme evidence.
- The minimum accepted contract is child-provided object name evidence. Runtime instructions explicitly judge the word the child says or enters, not OCR or image-only sound inference.
- Demo support is `degraded` with `cat5_judgment` because the current demo can represent the collection flow but cannot guarantee live phoneme judgment from photo pixels alone.
- The workbook note says the screen may show the corresponding letter. Generated PNGs do not bake letters or words; `b_sound_letter_cue` is a text-free backing for app-owned `/b/` or B overlay. If that overlay is unavailable, the AI uses voice-only fallback and does not claim a letter is visible.

## Selection Trigger

Child enters language treasure-hunt mode or photographs an everyday indoor object that can naturally launch a sound hunt.

## Asset Brief

| asset_id | asset_type | role | requiredness | generation timing | use step | display location | purpose | prompt/source summary | display behavior | fallback |
|---|---|---|---|---|---|---|---|---|---|---|
| `activity_icon` | icon | activity_preview | required | post-package build | activity preview | round device screen | Identify the activity without revealing the answer. | Listening-and-search icon with mouth/sound-wave cue and search path, no text or letters. | Display before launch. | Use a plain preview tile and do not claim the icon is visible. |
| `intro_scene` | scene_background | story_scene | required | post-package build | Step 1 | round device screen | Start the search mood. | Same child in a plausible indoor room listening to the device before the sound is named. | Show during transition bridge. | Voice-only intro. |
| `rules_scene` | scene_background | story_scene | required | post-package build | Step 2 | round device screen | Support the sound rule. | Same child practicing the beginning sound with mouth/speech cues and sound waves. | Show while modeling `/b/`. | Voice-only rule. |
| `round_1_scene` | scene_background | story_scene | required | post-package build | Step 3 Round 1 | round device screen | Practice the sound before search. | Child rehearses the target sound; no baked example objects. | Show with optional app overlay. | Voice-only sound model. |
| `round_2_scene` | scene_background | story_scene | required | post-package build | Step 3 Round 2 | round device screen | Invite the indoor search. | Same child safely searching the room with a subtle sound-wave trail; no answer object revealed. | Show while camera/photo UI is app-owned overlay. | Voice-only search prompt. |
| `round_3_scene` | scene_background | story_scene | required | post-package build | Step 3 Round 3 | round device screen | Show naming and evidence check. | Child names the found object toward the device; runtime overlays accepted photo/name separately. | Show while app overlays accepted photo/name. | Voice-only evidence check. |
| `synthesis_scene` | scene_background | story_scene | required | post-package build | Step 4 | round device screen | Connect photo/name to the sound rule. | Sound-wave ribbon connects the child-provided word evidence to the beginning-sound pattern. | Show during synthesis. | Voice-only synthesis. |
| `celebrate_scene` | scene_background | story_scene | required | post-package build | Step 5 celebration | round device screen | Celebrate after synthesis. | Same child celebrates the listening/speaking success with sound-wave ribbons. | Show briefly after synthesis. | Voice-only celebration. |
| `closing_scene` | scene_background | story_scene | required | post-package build | Step 5 closing | round device screen | Close without new task. | Calm finishing moment in the same room with the sound-wave ribbon fading. | Show during recap close. | Voice-only close. |
| `b_sound_letter_cue` | ui_overlay | ui_overlay | optional | post-package build | Step 2; Step 3 Round 1 | round device screen support tile | Provide visual support for a runtime-owned `/b/` or B overlay. | Text-free listening tile with mouth/sound-wave pictogram, no readable marks. | Show only if runtime overlays the actual letter/sound separately. | Repeat `/b/` by voice and do not claim a letter card is visible. |
| `ball_object` | icon | collection_correct | required | post-package build | example/picker support | package `assets/items/` | Correct B example. | One centered ball object, no text. | Optional example sprite or picker item. | Use voice-only examples. |
| `banana_object` | icon | collection_correct | required | post-package build | example/picker support | package `assets/items/` | Correct B example. | One centered banana object, no text. | Optional example sprite or picker item. | Use voice-only examples. |
| `book_object` | icon | collection_correct | required | post-package build | example/picker support | package `assets/items/` | Correct B example. | One centered closed book object, no text. | Optional example sprite or picker item. | Use voice-only examples. |
| `box_object` | icon | collection_correct | required | post-package build | example/picker support | package `assets/items/` | Correct B example. | One centered plain box object, no text. | Optional example sprite or picker item. | Use voice-only examples. |
| `cup_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered plain cup object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `sock_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Second nonmatching contrast example. | One centered soft sock object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `apple_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered apple object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `car_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered toy car object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `hat_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered hat object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `mug_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered mug object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `shoe_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered shoe object, no text. | Optional contrast sprite. | Use voice-only contrast. |
| `spoon_object` | icon | collection_distractor | required | post-package build | contrast/picker support | package `assets/items/` | Nonmatching contrast example. | One centered spoon object, no text. | Optional contrast sprite. | Use voice-only contrast. |

## Asset Usage Timeline

| asset_id | load/generate moment | first display | visible range | interaction/use | persistence/hide behavior | fallback |
|---|---|---|---|---|---|---|
| `activity_icon` | post-package imagegen/build | preview | before Step 1 | Identifies the activity. | Hidden once activity starts. | Plain app preview. |
| `intro_scene` | post-package imagegen/build | Step 1 | Step 1 only | Supports the warm hook. | Replaced by rules scene. | Voice-only hook. |
| `rules_scene` | post-package imagegen/build | Step 2 | Step 2 only | Supports `/b/` modeling. | Replaced by round scene. | Voice-only rule. |
| `b_sound_letter_cue` | post-package imagegen/build | Step 2 | Step 2 and Round 1 when overlay exists | Text-free backing for app-owned `/b/` or B overlay. | Hidden before search if not needed. | Voice-only `/b/` model. |
| `round_1_scene` | post-package imagegen/build | Step 3 Round 1 | Round 1 only | Sound practice before search. | Replaced by search scene. | Voice-only practice. |
| `round_2_scene` | post-package imagegen/build | Step 3 Round 2 | Round 2 only | Search prompt while app owns camera UI. | Replaced by evidence scene. | Voice-only search prompt. |
| `round_3_scene` | post-package imagegen/build | Step 3 Round 3 | Round 3 only | Evidence check with app-owned photo/name overlay. | Replaced by synthesis scene. | Voice-only evidence check. |
| `synthesis_scene` | post-package imagegen/build | Step 4 | Step 4 only | Shows abstract connection between treasure and sound. | Replaced by celebration/closing. | Voice-only synthesis. |
| `celebrate_scene` | post-package imagegen/build | Step 5 | brief celebration | Celebrates completed action. | Replaced by closing scene. | Voice-only celebration. |
| `closing_scene` | post-package imagegen/build | Step 5 close | closing | Calms the activity and recaps. | Ends activity. | Voice-only close. |
| `ball_object` | post-package imagegen/build | optional Round 1/picker | optional example only | Correct B example. | Kept out of scene backgrounds. | Voice-only example. |
| `banana_object` | post-package imagegen/build | optional Round 1/picker | optional example only | Correct B example. | Kept out of scene backgrounds. | Voice-only example. |
| `book_object` | post-package imagegen/build | optional Round 1/picker | optional example only | Correct B example. | Kept out of scene backgrounds. | Voice-only example. |
| `box_object` | post-package imagegen/build | optional Round 1/picker | optional example only | Correct B example. | Kept out of scene backgrounds. | Voice-only example. |
| `cup_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `sock_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `apple_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `car_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `hat_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `mug_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `shoe_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |
| `spoon_object` | post-package imagegen/build | optional contrast/picker | optional contrast only | Non-B contrast. | Kept out of scene backgrounds. | Voice-only contrast. |

## Extensibility Notes

- Reusable slots are `{target_sound}`, `{target_letter_overlay}`, `{candidate_object_name}`, and `{accepted_photo_id}`.
- Retargeting from `/b/` to another sound requires changing example words, optional item sprites, runtime overlay, and sound-specific dialogue together.
- Do not retarget by only swapping a letter image; the child action and evidence rule must stay aligned with the target sound.
- The current package is concept/workbook grounded and should not invent entity-specific mapping facts.

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, pose, IMU, state-change, or image-only phoneme inference is required; phoneme judgment uses child-provided object name evidence and degraded demo support. |
| 2 | Hook & Transition | PASS | Step 1 opens with a playful sound mission, not a quiz; Step 2 naturally names the sound rule. |
| 3 | Edge Case Coverage | PASS | Every live beat includes ideal, unexpected, and no-response branches, including cannot-find and non-B-object cases. |
| 4 | IB Completeness | PASS | Form and Connection, KUD, related concepts, and ATL skills all match beginning-sound evidence. |
| 5 | Tier Appropriateness | PASS | T1 instructions use short concrete sentences, one-object search, and low-pressure correction. |
| 6 | Dialogue Specificity | PASS | Every runtime instruction includes goal, constraints, tone, progress evidence, branch behavior, source guardrail, example line, and screen behavior. |
| 7 | Screen & UI Completeness | PASS | Each step names screen state; app-owned UI, letter overlay, camera slot, and accepted photo/name are separate from PNGs; item assets are declared separately. |
| 8 | Entity Mapping Alignment | N/A | No mapping is required for this concept-only/parameterized source row. |
| 9 | Game Feel | PASS | The child gets a small mission, uncertainty while searching, and an earned synthesis when the word and object match. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves collect/show/name as the repeated action, and Adventure framing does not replace the sound-hunt mechanic. |

**Overall**: ALL PASS - ready for independent review.
