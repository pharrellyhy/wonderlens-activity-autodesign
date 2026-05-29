# Orion Number Reveal Spec

## Premise

The child chooses a number before reveal, then sees a source-faithful Orion card and hears background information.

## Target

- Activity ID: `e2e_orion_number_reveal`
- Template type: `cat1`
- Pillar / Game Style: Adventure / `time_traveler`
- Canonical mechanic: `decide`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** child chooses a number first, then sees the real Orion guide-star card and hears one background fact.
- **Readiness:** `ready_for_demo`. Trigger condition: Operator selects reference-bound asset validation slice.
- **Canonical mechanic:** `decide` remains the primary child action; `time_traveler` is scaffold metadata only.
- **Mapping use:** not mapping-informed; reference provenance is package-local source metadata.
- **Product capability flags:** cat1_dialogue, reference_bound_asset_display, runtime_contract_conversion.
- **Asset dependency:** `reference_bound` - one reference_bound story_scene asset with accepted source metadata, licensed source_type, and exactly seven visible guide-star components.
- **Demo support:** `supported` with `ui_template: cat1_dialogue`; requires={'generated_assets': True, 'real_camera': False, 'runtime_judgment': False, 'device_round_screen': True}.
- **Scaffold fit:** Approved `Adventure` / `time_traveler` vocabulary is used without changing the promised child action. Unsupported or weak-fit cases are disclosed instead of being forced into a misleading style.
- **Assumptions:** Number choice is an opener before reveal, not a promise to match star count.; The accepted NOIRLab source can be used as provenance for a simplified seven-guide-star redraw..

## Selection Trigger

Operator selects this package as part of the fresh E2E subset runtime validation run. Consumers must bind the declared default entity and must not substitute another activity when an exact package ID is selected.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `orion_seven_star_card` | story_scene | required | post-package asset_build=generate_and_curate | referenced in prod.md screen states | round device screen | Seven-star Orion reference card | Reference-bound asset. Source: NSF NOIRLab Orion chart based on IAU and Sky & Telescope artwork (https://noirlab.edu/public/media/archives/images/large/ori.jpg, CC BY 4.0, source_type=licensed_asset). Transformation policy: simplified_redraw. Runtime card must keep the verified constellation guide-star layout and must not add random stars or text. | shown only when the beat names this asset_id; Cat5 cards guide capture but do not replace photo evidence | If the accepted Orion source or simplified redraw is unavailable, do not reveal or describe the constellation card. | no text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path; keep subject inside central circular safe area |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `orion_seven_star_card` | prebuilt runtime PNG | loaded before the relevant display step | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

## Extensibility Notes

- Retarget to another constellation only with accepted source metadata.
- Keep choose-before-reveal order.
- Do not add count-the-image prompts or random background stars.
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
