# Guided Drawing -- Authoring Spec

> CAT3 resolved capability-probe package . Mechanic: `build` . Product contract override: `minimum_unblock_allowed`

## Premise

AI guides the child to use paper and pencil to complete a simple drawing step by step, then the child photographs the finished work. This workbook review-packet run treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat3
- **Mechanic:** `build`
- **Role title:** Step Sketch Coach
- **Entity role:** catalyst
- **Progression axis:** change, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** AI guides the child to use paper and pencil to complete a simple drawing step by step, then the child photographs the finished work.
- **Canonical mechanic:** `build`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child is indoors and photographs an object that could become a drawing theme.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** optional_support. Asset `guided_drawing_step_cards_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_materials,before_after_risk.
- **Scaffold fit:** Creation / `inventor_workshop` gives the child a role, escalating turns, and a payoff while preserving `build`.
- **Round shape:** Draw the big shape -> Add one useful detail -> Show the finish.

## Selection Trigger

Start when: Child is indoors and photographs an object that could become a drawing theme. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Creation
- **Game style:** `inventor_workshop`
- **Why this scaffold:** it creates an earned Step 4 reveal: a child-made drawing built from a big shape, detail, and finish photo/self-report.

## Resolved Product Contract Notes

- **Cat3 material workflow:** Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
- **Before/after evidence:** Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| guided_drawing_step_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide optional visual steps for a simple drawing task. | Create a set of step-by-step drawing cards for children ages 4-6. Show how to draw a simple friendly object in 4 clear steps using thick black sketch lines, large shapes, no text, minimal details, and a plain white background. | Show one step card at a time while the AI leaves enough time for the child to draw on paper. | If step cards are unavailable, use voice-only step descriptions with caregiver setup, self-report completion, and no drawing-quality assessment. | No real child photos, no fine-copying requirement, and only simple non-dangerous drawing themes. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| guided_drawing_step_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide optional visual steps for a simple drawing task. | new_ai_generated_asset | Show one step card at a time while the AI leaves enough time for the child to draw on paper. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | If step cards are unavailable, use voice-only step descriptions with caregiver setup, self-report completion, and no drawing-quality assessment. |

## Runtime Detail Floor Notes

- **Distinct round design:** Draw the big shape, Add one useful detail, Show the finish are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a child-made drawing built from a big shape, detail, and finish photo/self-report; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `guided_drawing_step_cards_01`, `guided_drawing`, and `{runtime_tier}`.
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

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
