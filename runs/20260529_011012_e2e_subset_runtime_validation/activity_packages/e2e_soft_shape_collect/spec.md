# Soft Shape Collect Spec

## Premise

The child uses guide cards to choose a shape clue, then captures a real-world photo as the collection evidence.

## Target

- Activity ID: `e2e_soft_shape_collect`
- Template type: `cat5`
- Pillar / Game Style: Adventure / `quest_collector`
- Canonical mechanic: `collect`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** child chooses a guide card, captures one real-world matching shape photo, and names the matching evidence.
- **Readiness:** `ready_for_demo`. Trigger condition: Operator selects Cat5 simple collection supported validation slice.
- **Canonical mechanic:** `collect` remains the primary child action; `quest_collector` is scaffold metadata only.
- **Mapping use:** not mapping-informed; shape cards are concept-authored validation assets.
- **Product capability flags:** cat5_collection, real_camera, photo_id_handoff, package_asset_display.
- **Asset dependency:** `required_prebuilt` - three card assets with one collection_correct and two collection_distractor roles; cards guide but never replace photo_id evidence.
- **Demo support:** `supported` with `ui_template: cat5_collection`; requires={'generated_assets': True, 'real_camera': True, 'runtime_judgment': False, 'device_round_screen': True}.
- **Scaffold fit:** Approved `Adventure` / `quest_collector` vocabulary is used without changing the promised child action. Unsupported or weak-fit cases are disclosed instead of being forced into a misleading style.
- **Assumptions:** Guide cards can be displayed before capture.; A child-stated visible shape clue is acceptable evidence for this demo round..

## Selection Trigger

Operator selects this package as part of the fresh E2E subset runtime validation run. Consumers must bind the declared default entity and must not substitute another activity when an exact package ID is selected.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `round_shape` | collection_correct | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | round soft pebble guide card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: round soft pebble guide card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If round_shape is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |
| `corner_shape` | collection_distractor | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | corner block distractor card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: corner block distractor card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If corner_shape is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |
| `long_shape` | collection_distractor | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | long ribbon distractor card | Soft 3D educational toy illustration in the WonderLens activity style: warm white and mint prototype-device palette, soft sky blue, gentle coral, pale yellow, rounded clay or plastic forms, gentle studio lighting, square source art, primary subject inside the central circular safe area, simple full-bleed background to every edge, no text, no labels, no logo, no watermark, no device chrome, no circular mask, no border. Subject: long ribbon distractor card. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If long_shape is unavailable, keep the package gated or degraded instead of showing a substitute image. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `round_shape` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `corner_shape` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `long_shape` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

## Extensibility Notes

- Swap guide-card set while preserving collection_catalog_id uniqueness.
- Keep real photo capture between guide choice and acceptance.
- Retarget criterion to another visible non-judgment property.
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
