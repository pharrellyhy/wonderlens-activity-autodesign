# B-Sound Treasure Collect Spec

## Premise

The child uses B-sound cards as clues, captures a real object, and says the object name for runtime judgment.

## Target

- Activity ID: `e2e_b_sound_treasure_collect`
- Template type: `cat5`
- Pillar / Game Style: Adventure / `quest_collector`
- Canonical mechanic: `collect`
- Demo support status: `degraded`

## Adaptation Rationale

- **Core promise:** child uses B-sound cards, captures a real object, and says/enters the object name so runtime can judge initial sound.
- **Readiness:** `degraded_demo`. Trigger condition: Operator selects Cat5 runtime-judgment validation slice.
- **Canonical mechanic:** `collect` remains the primary child action; `quest_collector` is scaffold metadata only.
- **Mapping use:** not mapping-informed; B-sound clue cards are concept-authored validation assets.
- **Product capability flags:** cat5_judgment, real_camera, photo_id_handoff, child_speech_or_name_evidence.
- **Asset dependency:** `required_prebuilt` - three B-sound correct cards plus one non-B distractor card; acceptance requires real photo_id plus spoken/name evidence.
- **Demo support:** `degraded` with `ui_template: cat5_judgment`; requires={'generated_assets': True, 'real_camera': True, 'runtime_judgment': True, 'device_round_screen': True}.
- **Scaffold fit:** Approved `Adventure` / `quest_collector` vocabulary is used without changing the promised child action. Unsupported or weak-fit cases are disclosed instead of being forced into a misleading style.
- **Assumptions:** The current demo cannot infer initial phoneme from image alone.; The activity is executable only when child name/speech evidence is collected..

## Selection Trigger

Operator selects this package as part of the fresh E2E subset runtime validation run. Consumers must bind the declared default entity and must not substitute another activity when an exact package ID is selected.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `ball` | collection_correct | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | round ball B-sound card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: round ball B-sound card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If ball is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |
| `book` | collection_correct | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | closed book B-sound card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: closed book B-sound card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If book is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |
| `banana` | collection_correct | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | curved banana B-sound card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: curved banana B-sound card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If banana is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |
| `cup` | collection_distractor | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | plain cup non-B distractor card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: plain cup non-B distractor card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If cup is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `ball` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `book` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `banana` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `cup` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

## Extensibility Notes

- Retarget to another initial sound only if speech/name evidence stays required.
- Keep degraded status unless runtime has honest phoneme judgment.
- Preserve distractor to show judgment boundary.
- Retargeting must preserve demo_support honesty, asset_manifest roles, and the runtime child action before package reuse.

## Self-Evaluation Scorecard

| # | Dimension | Result | Why |
|---|---|---|---|
| 1 | V1 technical compliance | PASS | Support status and runtime requirements match demo_support.yaml. |
| 2 | Hook quality | PASS | Step 1 frames the activity without a cold quiz. |
| 3 | Transition quality | PASS | Step 2 moves naturally into the child action. |
| 4 | Edge-case handling | PASS | Every runtime beat has ideal, unexpected, and no-response branches. |
| 5 | IB alignment | PASS | Key concepts match the focal attribute and child action. |
| 6 | Tier fit | PASS | Runtime constraints use short T1 language. |
| 7 | Dialogue/runtime contract | PASS | Runtime AI instructions include goal, constraint, tone, progress evidence, branch behavior, and guardrails. |
| 8 | Screen/state specificity | PASS | Screen states name asset IDs, photo slots, or gated state. |
| 9 | Mapping/source integrity | PASS | Concept-only validation does not claim unavailable mapping; source-bound Orion uses reference metadata. |
| 10 | Mechanic fidelity | PASS | Step 3 child action matches the activity mechanic and adaptation brief. |
