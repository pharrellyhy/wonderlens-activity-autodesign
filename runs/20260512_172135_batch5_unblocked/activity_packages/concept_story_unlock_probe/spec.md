# Story Challenge Unlock -- Authoring Spec

> CAT1 resolved capability-probe package . Mechanic: `imagine` . Product contract override: `minimum_unblock_allowed`

## Premise

A story pauses at a challenge point and the child completes a quick task to unlock the next beat. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `imagine`
- **Role title:** Story Key Maker
- **Entity role:** catalyst
- **Progression axis:** perspective, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** A story pauses at a challenge point and the child completes a quick task to unlock the next beat.
- **Canonical mechanic:** `imagine`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child reaches a story pause point and can complete a quick challenge to continue.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** optional_support. Asset `story_unlock_cards_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_ui_state,requires_asset_display.
- **Scaffold fit:** Adventure / `time_traveler` gives the child a role, escalating turns, and a payoff while preserving `imagine`.
- **Round shape:** Pick the story door -> Make the unlock action -> Choose what happens next.

## Selection Trigger

Start when: Child reaches a story pause point and can complete a quick challenge to continue. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `time_traveler`
- **Why this scaffold:** it creates an earned Step 4 reveal: a next story scene unlocked by the child's imagined action.

## Resolved Product Contract Notes

- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| story_unlock_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show a simple locked story door, token, or next-scene card during a story challenge. | Create a set of child-friendly story unlock cards. Each card shows a magical door, path marker, treasure token, or story page waiting to open. Use warm illustrated style, no text, no scary elements, and clear central object. | Show the card at a story pause point and change to the next scene only when product unlock state is supported. | If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. | No frightening doors, traps, weapons, or branded characters. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| story_unlock_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show a simple locked story door, token, or next-scene card during a story challenge. | new_ai_generated_asset | Show the card at a story pause point and change to the next scene only when product unlock state is supported. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. |

## Runtime Detail Floor Notes

- **Distinct round design:** Pick the story door, Make the unlock action, Choose what happens next are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a next story scene unlocked by the child's imagined action; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `story_unlock_cards_01`, `story_unlock`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `imagine` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Perspective, Connection, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `imagine`; Adventure/time_traveler frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
