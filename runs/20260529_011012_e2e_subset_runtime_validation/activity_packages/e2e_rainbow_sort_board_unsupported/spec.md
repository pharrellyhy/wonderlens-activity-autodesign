# Rainbow Sort Board Spec

## Premise

The child would sort several color tiles into persistent rainbow lanes, but the current demo must gate it.

## Target

- Activity ID: `e2e_rainbow_sort_board_unsupported`
- Template type: `cat5`
- Pillar / Game Style: Discovery / `field_experiment`
- Canonical mechanic: `sort`
- Demo support status: `unsupported`

## Adaptation Rationale

- **Core promise:** child would drag or place multiple color tiles into persistent rainbow lanes; current runtime must not fake it.
- **Readiness:** `blocked_until_product_decision`. Trigger condition: Operator selects unsupported UI-heavy validation slice.
- **Canonical mechanic:** `sort` remains the primary child action; `field_experiment` is scaffold metadata only.
- **Mapping use:** not mapping-informed; blocked concept-only package.
- **Product capability flags:** requires_persistent_sorting_board, requires_drag_drop_or_multi_slot_state.
- **Asset dependency:** `no_assets` - no runtime assets because package is unsupported and ui_template=none.
- **Demo support:** `unsupported` with `ui_template: none`; requires={'generated_assets': False, 'real_camera': False, 'runtime_judgment': False, 'device_round_screen': True}.
- **Scaffold fit:** Approved `Discovery` / `field_experiment` vocabulary is used without changing the promised child action. Unsupported or weak-fit cases are disclosed instead of being forced into a misleading style.
- **Assumptions:** Current Cat1/Cat5 demos cannot preserve multi-item sorting as the repeated action.; Gating is the correct consumer behavior..

## Selection Trigger

Operator selects this package as part of the fresh E2E subset runtime validation run. Consumers must bind the declared default entity and must not substitute another activity when an exact package ID is selected.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | no asset generation | no playable step | none | unsupported gated preview | no prompt/source because asset_manifest.assets is empty | no runtime display | no fallback needed | do not invent cards, lanes, or fake board assets for unsupported sorting board |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| none | none | none | none | unsupported package has no runtime image dependency | no asset fallback needed |

## Unsupported Product Contract Notes

This package is structurally valid but not playable in current demos. The source promise requires persistent multi-item sorting; demo_support.yaml records `unsupported` and `ui_template: none` so consumers can gate honestly.

## Extensibility Notes

- Reusable after product adds persistent board primitive.
- Keep mechanic=sort and do not convert to collect/describe.
- Future assets should be tile/lane UI assets, not collection cards.
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
