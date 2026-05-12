# Art Critic Tournament -- Authoring Spec

> CAT1 resolved capability-probe package . Mechanic: `compare` . Product contract override: `minimum_unblock_allowed`

## Premise

Child compares two approved artworks at a time and chooses a favorite until one wins. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `compare`
- **Role title:** Gallery Chooser
- **Entity role:** catalyst
- **Progression axis:** perspective, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child compares two approved artworks at a time and chooses a favorite until one wins.
- **Canonical mechanic:** `compare`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Product can show two approved artworks side by side and remember tournament progress.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** required_prebuilt. Asset `artwork_tournament_set_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_asset_display,requires_ui_state.
- **Scaffold fit:** Discovery / `field_experiment` gives the child a role, escalating turns, and a payoff while preserving `compare`.
- **Round shape:** Compare pair one -> Compare the winner -> Crown the gallery pick.

## Selection Trigger

Start when: Product can show two approved artworks side by side and remember tournament progress. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** it creates an earned Step 4 reveal: a tiny bracket winner chosen from visible art evidence.

## Resolved Product Contract Notes

- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| artwork_tournament_set_01 | reference_image | required | display_existing | prod.step_2; prod.step_3.round_1-3 | split_or_center_artwork_panel | Provide approved artwork pairs for comparison and tournament choice. | No image generation prompt. Use a curated, rights-cleared artwork set with metadata for artist, title, visual features, and child-safe discussion notes. | Show two artworks side by side only if product supports artwork display and tournament state. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. | Use rights-cleared, age-appropriate artworks only; no graphic violence, explicit content, or sensitive religious/political framing for young children. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| artwork_tournament_set_01 | reference_image | required | display_existing | prod.step_2; prod.step_3.round_1-3 | split_or_center_artwork_panel | Provide approved artwork pairs for comparison and tournament choice. | approved_public_domain_or_licensed_artwork_set | Show two artworks side by side only if product supports artwork display and tournament state. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. |

## Runtime Detail Floor Notes

- **Distinct round design:** Compare pair one, Compare the winner, Crown the gallery pick are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a tiny bracket winner chosen from visible art evidence; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `artwork_tournament_set_01`, `art_critic_tournament`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `compare` mechanic.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `compare`; Discovery/field_experiment frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
