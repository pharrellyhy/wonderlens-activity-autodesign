# One-Line Drawing Challenge -- Authoring Spec

> CAT3 resolved capability-probe package . Mechanic: `build` . Product contract override: `minimum_unblock_allowed`

## Premise

Child tries to draw a target without lifting the pencil or finger. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat3
- **Mechanic:** `build`
- **Role title:** Line Path Explorer
- **Entity role:** catalyst
- **Progression axis:** change, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child tries to draw a target without lifting the pencil or finger.
- **Canonical mechanic:** `build`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child has paper or a drawing surface and chooses a drawing challenge.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** required_prebuilt. Asset `one_line_drawing_cards_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_materials,requires_asset_display,before_after_risk.
- **Scaffold fit:** Creation / `inventor_workshop` gives the child a role, escalating turns, and a payoff while preserving `build`.
- **Round shape:** Trace the path in the air -> Draw without lifting -> Explain the path.

## Selection Trigger

Start when: Child has paper or a drawing surface and chooses a drawing challenge. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Creation
- **Game style:** `inventor_workshop`
- **Why this scaffold:** it creates an earned Step 4 reveal: one continuous-line attempt with start, turn, and finish explained.

## Resolved Product Contract Notes

- **Cat3 material workflow:** Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
- **Before/after evidence:** Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| one_line_drawing_cards_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show simple one-line drawing targets. | Create a set of one-line drawing challenge cards for children ages 5-8. Each card shows one simple object made from a continuous thick black line, such as a house, fish, flower, car, or snail. Use plain white background, no text, and easy-to-follow shapes. | Show one target before the child attempts the drawing. | Use a voice-only path-planning challenge and child self-report; do not claim a drawing card or drawing verification is available. | No fine-copying pressure, no copyrighted characters, and no unsafe drawing themes. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| one_line_drawing_cards_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show simple one-line drawing targets. | new_ai_generated_asset | Show one target before the child attempts the drawing. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use a voice-only path-planning challenge and child self-report; do not claim a drawing card or drawing verification is available. |

## Runtime Detail Floor Notes

- **Distinct round design:** Trace the path in the air, Draw without lifting, Explain the path are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals one continuous-line attempt with start, turn, and finish explained; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `one_line_drawing_cards_01`, `one_line_drawing`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `build` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Function, Change, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `build`; Creation/inventor_workshop frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
