# Pretend Trip Planner -- Authoring Spec

> CAT1 concept package . Concept source: `source_travel_planner` . Mechanic: `predict`

## Premise

The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen. The activity turns that source promise into a cat1 runtime package where the child becomes the Trip Predictor. The repeated action is `predict`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `predict`
- **Entity role:** catalyst
- **Progression axis:** causation, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child helps plan a pretend trip by predicting what hidden trip cards will need before each reveal.
- **Canonical mechanic:** `predict`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child asks about a place, weather, vehicle, animal habitat, or character journey.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `travel_planning_cards_01` is optional `card_set` support; fallback behavior is documented.
- **Product capability flags:** none; optional card display has a voice-only fallback.
- **Scaffold fit:** acceptable. Discovery / `prediction_lab` supplies the emotional payoff while `predict` remains the child-action contract.
- **Assumptions:** Use commit-before-reveal prediction and pretend planning, not factual itinerary generation.

## Selection Trigger

Start when Child asks about a place, weather, vehicle, animal habitat, or character journey. If optional visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `prediction_lab`
- **Why this scaffold:** The package avoids real booking or location claims and keeps the activity in pretend planning and prediction.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Predict What We Need, Round 2 -- Predict How to Travel, and Round 3 -- Predict a Surprise each require a child prediction before the hidden card reveal.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The final board shows prediction -> reveal -> plan for raincoat, boat, and boots, making the payoff depend on the child's commitments.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| travel_planning_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Support pretend trip planning with visual choices. | Create a set of pretend travel planning cards for children. Include suitcase, water bottle, map, train, bus, walking shoes, raincoat, snack, and camera. Use simple friendly illustrations, plain background, no text, no brands, and no real travel booking interface. | Show a small group of cards when asking what to pack or how to travel. | If cards are unavailable, run the planning conversation by voice only. | No real booking, no unsafe travel instructions, no location tracking, and no brands. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| travel_planning_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Support pretend trip planning with visual choices. | new_ai_generated_asset | Show a small group of cards when asking what to pack or how to travel. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, run the planning conversation by voice only. |

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `travel_planning_cards_01`, `pretend_trip_prediction`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `predict` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T1 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The loop has escalating rounds and a visible payoff earned from the child's repeated action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `predict` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
