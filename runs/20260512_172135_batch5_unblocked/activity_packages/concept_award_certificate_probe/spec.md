# Award Certificate -- Authoring Spec

> CAT3 resolved capability-probe package . Mechanic: `care` . Product contract override: `minimum_unblock_allowed`

## Premise

Child makes or designs an award for someone who helped tried hard or deserves appreciation. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat3
- **Mechanic:** `care`
- **Role title:** Appreciation Designer
- **Entity role:** catalyst
- **Progression axis:** responsibility, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child makes or designs an award for someone who helped tried hard or deserves appreciation.
- **Canonical mechanic:** `care`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child names someone who helped tried hard or deserves appreciation.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** optional_support. Asset `award_inspiration_badges_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_materials,requires_asset_display,before_after_risk.
- **Scaffold fit:** Discovery / `field_experiment` gives the child a role, escalating turns, and a payoff while preserving `care`.
- **Round shape:** Choose the honoree -> Pick the award reason -> Say the certificate line.

## Selection Trigger

Start when: Child names someone who helped tried hard or deserves appreciation. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** it creates an earned Step 4 reveal: an award reason, badge choice, and spoken certificate line.

## Resolved Product Contract Notes

- **Cat3 material workflow:** Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
- **Before/after evidence:** Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| award_inspiration_badges_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide simple positive badge ideas for an award certificate. | Create a set of friendly award badge illustrations for children. Include badges for kindness, trying hard, helping, bravery, creativity, and teamwork. Use simple shapes, warm colors, no text, no medals with military styling, and no brands. | Show badges only as inspiration if certificate creation support exists. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. | No competitive ranking, no shaming, no real child photos, and no exclusionary imagery. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| award_inspiration_badges_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide simple positive badge ideas for an award certificate. | new_ai_generated_asset | Show badges only as inspiration if certificate creation support exists. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. |

## Runtime Detail Floor Notes

- **Distinct round design:** Choose the honoree, Pick the award reason, Say the certificate line are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals an award reason, badge choice, and spoken certificate line; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `award_inspiration_badges_01`, `award_certificate`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `care` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Responsibility, Perspective, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `care`; Discovery/field_experiment frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
