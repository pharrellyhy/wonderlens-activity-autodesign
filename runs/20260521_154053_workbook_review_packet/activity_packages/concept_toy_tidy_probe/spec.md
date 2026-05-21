# Toy Tidy Challenge -- Authoring Spec

> CAT5 resolved capability-probe package . Mechanic: `sort` . Product contract override: `minimum_unblock_allowed`

## Premise

The child starts from a toy area, accepts a short tidy-up mission, tidies one small group for a limited time, then confirms or shows what changed. This workbook-review run treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat5
- **Mechanic:** `sort`
- **Role title:** Tidy Sort Captain
- **Entity role:** catalyst
- **Progression axis:** connection, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child does a physical tidy-up process, not only a verbal sorting game: initial toy context, short timer, organizing tips, and after-state confirmation.
- **Canonical mechanic:** `sort`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Parent starts a tidy-up mission and the child has several visible toys or household items.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** no_assets. No image/display asset is required.
- **Product capability flags:** requires_ui_state,before_after_risk.
- **Scaffold fit:** Discovery / `field_experiment` gives the child a role, escalating turns, and a payoff while preserving `sort`.
- **Source intent lock:** Preserve the sequence: initial toy context, child agrees to tidy, short timed cleanup, organizing tips during the timer, and after-state confirmation. Do not reduce this to a purely verbal category-sorting game.
- **Round shape:** Start the tidy mission -> Tidy during the timer -> Confirm the after state.

## Selection Trigger

Start when: Parent starts a tidy-up mission and the child has several visible toys or household items. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** it creates an earned Step 4 reveal: a tidy sprint result grouped by the child's chosen toy group.

## Resolved Product Contract Notes

- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
- **Before/after evidence:** Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Runtime Detail Floor Notes

- **Distinct round design:** Start the tidy mission, Tidy during the timer, and Confirm the after state are distinct turns with physical child action, timer support, and honest confirmation state.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals the tidy sprint result: one toy group has a home and the next group is ready; it is not awarded before the child completes or confirms the work.
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

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
