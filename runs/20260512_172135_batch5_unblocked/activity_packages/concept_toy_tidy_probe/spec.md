# Toy Tidy Challenge -- Authoring Spec

> CAT5 resolved capability-probe package . Mechanic: `sort` . Product contract override: `minimum_unblock_allowed`

## Premise

Child sorts toys or household objects using a simple cleanup rule. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat5
- **Mechanic:** `sort`
- **Role title:** Tidy Sort Captain
- **Entity role:** catalyst
- **Progression axis:** connection, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child sorts toys or household objects using a simple cleanup rule.
- **Canonical mechanic:** `sort`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Parent starts a tidy-up mission and the child has several visible toys or household items.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** no_assets. No image/display asset is required.
- **Product capability flags:** requires_ui_state,before_after_risk.
- **Scaffold fit:** Discovery / `field_experiment` gives the child a role, escalating turns, and a payoff while preserving `sort`.
- **Round shape:** Choose a tidy rule -> Sort the first group -> Finish and check.

## Selection Trigger

Start when: Parent starts a tidy-up mission and the child has several visible toys or household items. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** it creates an earned Step 4 reveal: a cleanup map grouped by the child's sorting rule.

## Resolved Product Contract Notes

- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
- **Before/after evidence:** Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Runtime Detail Floor Notes

- **Distinct round design:** Choose a tidy rule, Sort the first group, Finish and check are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a cleanup map grouped by the child's sorting rule; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `toy_tidy`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `sort` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Form, Connection, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `sort`; Discovery/field_experiment frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
