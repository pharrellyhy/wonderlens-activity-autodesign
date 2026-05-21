# Simple Body Movement Guide -- Authoring Spec

> CAT1 resolved capability-probe package . Mechanic: `motion_voice` . Product contract override: `minimum_unblock_allowed`

## Premise

AI guides one simple body movement at a time with safety limits. This workbook review-packet run treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T0
- **Activity category:** cat1
- **Mechanic:** `motion_voice`
- **Role title:** Safe Move Leader
- **Entity role:** catalyst
- **Progression axis:** perspective, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** AI guides one simple body movement at a time with safety limits.
- **Canonical mechanic:** `motion_voice`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Parent starts a short movement prompt and the child has enough space.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** required_prebuilt. Asset `body_movement_cards_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_asset_display,requires_motion_safety.
- **Scaffold fit:** Performance / `voice_stage` gives the child a role, escalating turns, and a payoff while preserving `motion_voice`.
- **Round shape:** Hello hands -> Freeze statue.

## Selection Trigger

Start when: Parent starts a short movement prompt and the child has enough space. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Performance
- **Game style:** `voice_stage`
- **Why this scaffold:** it creates an earned Step 4 reveal: two low-risk movement prompts: hands and freeze.

## Resolved Product Contract Notes

- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
- **Motion safety:** Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| body_movement_cards_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_pose_card | Show simple safe movement prompts. | Create a set of simple movement cards using a friendly non-real child-like character. Include wave hands, reach up, touch shoulders, stomp feet softly, and freeze like a statue. Use clear poses, plain background, no text, no extreme flexibility, no jumping from height, and no unsafe props. | Show one movement card per round with short voice guidance. | Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible. | No real child photos, no risky balance, no running, no jumping from furniture, and no medical claims. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| body_movement_cards_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_pose_card | Show simple safe movement prompts. | new_ai_generated_asset | Show one movement card per round with short voice guidance. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-2, then summarize or hide at Step 4 according to the payoff. | Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible. |

## Runtime Detail Floor Notes

- **Distinct round design:** Hello hands, Freeze statue are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals two low-risk movement prompts: hands and freeze; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `body_movement_cards_01`, `body_movement`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `motion_voice` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Form, Perspective, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `motion_voice`; Performance/voice_stage frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
