# Shadow Story Seed Spec

## Premise

The child chooses one seed-like shadow and adds one story detail before hearing a tiny woven scene.

## Target

- Activity ID: `e2e_shadow_story_seed`
- Template type: `cat1`
- Pillar / Game Style: Adventure / `time_traveler`
- Canonical mechanic: `imagine`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** child chooses one shadow part and adds one story detail; AI weaves a tiny scene.
- **Readiness:** `generate_with_assumptions`. Trigger condition: Operator selects Cat1 simple supported validation slice.
- **Canonical mechanic:** `imagine` remains the primary child action; `time_traveler` is scaffold metadata only.
- **Mapping use:** not mapping-informed; concept-only validation package.
- **Product capability flags:** cat1_dialogue, package_asset_display, runtime_contract_conversion.
- **Asset dependency:** `required_prebuilt` - one illustrative story_scene asset shown before and during the story beats.
- **Demo support:** `supported` with `ui_template: cat1_dialogue`; requires={'generated_assets': True, 'real_camera': False, 'runtime_judgment': False, 'device_round_screen': True}.
- **Scaffold fit:** Approved `Adventure` / `time_traveler` vocabulary is used without changing the promised child action. Unsupported or weak-fit cases are disclosed instead of being forced into a misleading style.
- **Assumptions:** A single prebuilt story_scene asset is enough for the in-device story seed frame.; No camera or runtime visual judgment is required..

## Selection Trigger

Operator selects this package as part of the fresh E2E subset runtime validation run. Consumers must bind the declared default entity and must not substitute another activity when an exact package ID is selected.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `shadow_seed_scene` | story_scene | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | soft seed-shaped shadow prompt | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: soft seed-shaped shadow prompt. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If shadow_seed_scene is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `shadow_seed_scene` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

## Extensibility Notes

- Retarget entity noun and story prompt asset.
- Keep mechanic=imagine and one-detail story loop.
- Do not retarget into photo capture without changing category.
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
