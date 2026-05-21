# Color In Famous Art -- Authoring Spec

> CAT1 resolved capability-probe package . Mechanic: `enumerate` . Product contract override: `minimum_unblock_allowed`

## Premise

Child starts from a photographed or chosen color, then explores approved artworks where that color is dominant or important. This workbook review-packet run treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `enumerate`
- **Role title:** Color Curator
- **Entity role:** catalyst
- **Progression axis:** form, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child's photographed or chosen color leads to approved artworks that use the same color strongly.
- **Canonical mechanic:** `enumerate`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child photographs or names a clear color, and the screen can show approved public-domain artwork with known color metadata.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** required_prebuilt. Asset `color_artwork_set_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** Discovery / `field_experiment` gives the child a role, escalating turns, and a payoff while preserving `enumerate`.
- **Round shape:** Capture the child color -> Match approved artworks -> Choose the best color match.

## Selection Trigger

Start when: Child photographs or names a clear color, and screen can show approved public-domain artwork with known color metadata. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** it creates an earned Step 4 reveal: the child's real-world color connected to matched approved artworks.

## Resolved Product Contract Notes

- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| color_artwork_set_01 | reference_image | required | display_existing | prod.step_2; prod.step_3.round_1-3 | split_or_center_artwork_panel | Provide approved artworks with known dominant color metadata for matching the child's starter color. | No image generation prompt. Use a curated, rights-cleared artwork set with dominant color metadata and child-safe notes about visible colors, shapes, and mood. | Show two or more artworks that match the child's starter color and ask the child to point to visible evidence. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. | Use rights-cleared, age-appropriate artworks only; no graphic violence, explicit content, or complex sensitive context. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| color_artwork_set_01 | reference_image | required | display_existing | prod.step_2; prod.step_3.round_1-3 | split_or_center_artwork_panel | Provide approved artworks with known dominant color metadata for matching the child's starter color. | approved_public_domain_or_licensed_artwork_set | Show two or more artworks that match the child's starter color and ask the child to point to visible evidence. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. |

## Runtime Detail Floor Notes

- **Distinct round design:** Capture the child color, match approved artworks, and choose the best color match are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals the child's real-world color connected to matched approved artworks; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `color_artwork_set_01`, `color_famous_art`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `enumerate` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Form, Function, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `enumerate`; Discovery/field_experiment frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
