# Recognition Pop Challenge Spec

## Premise

The child compares changing pictures against a target rule; target and distractor sprites are separate from scene backgrounds.

## Target

- Activity ID: `concept_recognition_pop_probe`
- Source concept: `Recognition Pop Challenge` from `inputs/source_activity_concepts.md#source_whack_a_mole_recognition` and TSV source row 31
- Template type: `cat1`
- Pillar / Game Style: Mystery / `mystery_lens`
- Canonical mechanic: `compare`
- Demo support status: `degraded`

## Adaptation Rationale

- **Core promise:** After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.
- **Readiness:** `generate_with_assumptions` under `product_contract_override=minimum_unblock_allowed`.
- **Canonical mechanic:** `compare` controls the repeated child action; pillar/style is scaffold only.
- **Mapping use:** not mapping-informed; this package is concept/workbook grounded.
- **Asset dependency:** `generate_and_curate` with separate 512x512 runtime PNGs after text package writing.
- **Source baseline:** `inputs/original_activity_concepts_2026-05-29.tsv` controls over normalized helper text if they differ.
- **No content improvement fallback:** consumer conversion must load this package as written; downstream rewrites are recorded as consumer findings.

## Minimum Product Contract Notes

- Known capability risk is represented honestly by `demo_support.yaml` and runtime instructions.
- `prod.md` intentionally contains no raw blocker markers and no claim that unsupported vision, tap timing, or photo verification is available.
- Guided Drawing uses text-guided child/caregiver self-report only; Recognition Pop preserves target/distractor timing without pretending a generic dialogue is equivalent.

## Selection Trigger

Product has a tap-based recognition game surface.

## Asset Brief

| asset_id | role | requiredness | accuracy mode | timing | prompt or source | fallback |
|---|---|---|---|---|---|---|
| `activity_icon` | activity_preview | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge activity icon motif, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If activity_icon is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `intro_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge intro moment, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If intro_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `rules_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge rule explanation moment, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If rules_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_1_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge first round scene, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If round_1_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_2_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge second round scene, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If round_2_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_3_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge third round scene, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If round_3_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `celebrate_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge celebration moment, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If celebrate_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `closing_scene` | story_scene | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: Recognition Pop Challenge closing recap moment, source-aligned but free of app-owned interface elements, abstract play surface with no dog, fox, wolf, cat, or duplicate selectable animal. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If closing_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `dog_target` | collection_correct | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered friendly dog target sprite. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If dog_target is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `fox_distractor` | collection_distractor | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered friendly fox distractor sprite. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If fox_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `wolf_distractor` | collection_distractor | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered friendly wolf distractor sprite. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If wolf_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `cat_distractor` | collection_distractor | required | illustrative | post-package build | Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: one centered friendly cat distractor sprite. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites. | If cat_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |

## Asset Usage Timeline

| asset_id | load/generate moment | first display | visible range | use | fallback |
|---|---|---|---|---|---|
| `activity_icon` | post-package asset build | referenced runtime beat | beat-specific only | activity icon motif | If activity_icon is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `intro_scene` | post-package asset build | referenced runtime beat | beat-specific only | intro moment | If intro_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `rules_scene` | post-package asset build | referenced runtime beat | beat-specific only | rule explanation moment | If rules_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_1_scene` | post-package asset build | referenced runtime beat | beat-specific only | first round scene | If round_1_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_2_scene` | post-package asset build | referenced runtime beat | beat-specific only | second round scene | If round_2_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `round_3_scene` | post-package asset build | referenced runtime beat | beat-specific only | third round scene | If round_3_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `celebrate_scene` | post-package asset build | referenced runtime beat | beat-specific only | celebration moment | If celebrate_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `closing_scene` | post-package asset build | referenced runtime beat | beat-specific only | closing recap moment | If closing_scene is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `dog_target` | post-package asset build | referenced runtime beat | beat-specific only | one centered friendly dog target sprite | If dog_target is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `fox_distractor` | post-package asset build | referenced runtime beat | beat-specific only | one centered friendly fox distractor sprite | If fox_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `wolf_distractor` | post-package asset build | referenced runtime beat | beat-specific only | one centered friendly wolf distractor sprite | If wolf_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |
| `cat_distractor` | post-package asset build | referenced runtime beat | beat-specific only | one centered friendly cat distractor sprite | If cat_distractor is unavailable, keep the runtime beat honest and use voice-only fallback without claiming this image is visible. |

## Extensibility Notes

- Retarget only by replacing the source promise, runtime evidence rule, and package-owned assets together.
- Keep `activity_id`, `tag_block.yaml`, `demo_support.yaml`, and `asset_manifest.yaml` aligned before consumer conversion.
- Do not use generated assets to change the mechanic, reveal timing, or source play frame.

## Self-Evaluation Scorecard

| # | Dimension | Result | Why |
|---|---|---|---|
| 1 | V1 technical compliance | PASS | Runtime claims match demo support and do not assert unsupported visual assessment or hidden UI. |
| 2 | Hook quality | PASS | Step 1 opens from the trigger and activity promise rather than a cold quiz. |
| 3 | Transition quality | PASS | Step 2 names the evidence rule before the core loop. |
| 4 | Edge-case handling | PASS | Every live beat has ideal, unexpected, and no-response branches. |
| 5 | IB alignment | PASS | Key concepts and ATL skills match the child action. |
| 6 | Tier fit | PASS | Runtime instructions constrain the AI to short T1 language. |
| 7 | Dialogue/runtime contract | PASS | Every live beat includes goal/action, constraint, tone, progress evidence, branch behavior, source guardrail, example line, and screen/state behavior. |
| 8 | Screen/state specificity | PASS | `prod.md` names asset IDs and separates app-owned UI from image files. |
| 9 | Mapping/source integrity | PASS | Workbook source intent is preserved; concept-only rows do not invent mapping facts. |
| 10 | Mechanic fidelity | PASS | Step 3 child action matches `compare` and the source promise. |
