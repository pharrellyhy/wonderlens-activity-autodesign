# Emotion Color Outfit -- Authoring Spec

> CAT1 resolved capability-probe package . Mechanic: `care` . Product contract override: `minimum_unblock_allowed`

## Premise

Child uses colors to represent feelings then sees or imagines a character outfit matching that feeling. This workbook review-packet run treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `care`
- **Role title:** Feeling Stylist
- **Entity role:** catalyst
- **Progression axis:** responsibility, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Child uses colors to represent feelings then sees or imagines a character outfit matching that feeling.
- **Canonical mechanic:** `care`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child names a mood or chooses a color to represent a feeling.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** required_prebuilt. Asset `emotion_color_character_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_asset_display,requires_coloring_ui,requires_ui_state.
- **Scaffold fit:** Nurture / `care_station` gives the child a role, escalating turns, and a payoff while preserving `care`.
- **Round shape:** Notice the feeling cue -> Choose a comfort color -> Add a caring action.

## Selection Trigger

Start when: Child names a mood or chooses a color to represent a feeling. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Nurture
- **Game style:** `care_station`
- **Why this scaffold:** it creates an earned Step 4 reveal: a character support plan: feeling cue, comfort color, and caring action.

## Resolved Product Contract Notes

- **Prebuilt asset display:** Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
- **Coloring or recoloring UI:** Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| emotion_color_character_01 | character_image | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | support_panel | Show a character whose outfit can reflect the child's chosen emotion color. | Create a simple friendly character template for an emotion color activity. The character should have a plain outfit with large clean regions that can be recolored, neutral expression, light background, no text, no brands, and no complex details. | Show the character before the child chooses an emotion color, then update the outfit only if recoloring UI is supported. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. | No real child photos, no stereotypes about colors or feelings, and no mental-health diagnosis framing. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| emotion_color_character_01 | character_image | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | support_panel | Show a character whose outfit can reflect the child's chosen emotion color. | new_ai_generated_asset_or_future_avatar_renderer | Show the character before the child chooses an emotion color, then update the outfit only if recoloring UI is supported. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible. |

## Runtime Detail Floor Notes

- **Distinct round design:** Notice the feeling cue, Choose a comfort color, Add a caring action are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a character support plan: feeling cue, comfort color, and caring action; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `emotion_color_character_01`, `emotion_color_outfit`, and `{runtime_tier}`.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `care`; Nurture/care_station frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
