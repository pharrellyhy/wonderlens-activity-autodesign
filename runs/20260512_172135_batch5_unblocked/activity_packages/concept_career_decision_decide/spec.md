# Helper Choice Desk -- Authoring Spec

> CAT1 concept package . Concept source: `source_career_decision` . Mechanic: `decide`

## Premise

The child helps choose what a helper or professional should do in a simple scenario. The activity turns that source promise into a cat1 runtime package where the child becomes the Helpful Decision Maker. The repeated action is `decide`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `decide`
- **Entity role:** catalyst
- **Progression axis:** responsibility, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child helps choose what a helper or professional should do in a simple scenario.
- **Canonical mechanic:** `decide`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child sees a professional role, tool, uniform, vehicle, or story character connected to work.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `career_portrait_cards_01` is optional card_set support; fallback behavior is documented.
- **Product capability flags:** none; optional card display has a voice-only fallback.
- **Scaffold fit:** acceptable. Nurture / `care_station` supplies the emotional payoff while `decide` remains the child-action contract.
- **Assumptions:** Treat the entity or picture as a catalyst for decision-making rather than a fixed career lesson.

## Selection Trigger

Start when Child sees a professional role, tool, uniform, vehicle, or story character connected to work. If optional visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Nurture
- **Game style:** `care_station`
- **Why this scaffold:** The package keeps roles broad and inclusive; the child decides actions rather than memorizing career facts.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Choose the Helper, Round 2 -- Choose the Tool, and Round 3 -- Choose the First Action each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The help plan lights up: helper, tool, and first action become one responsible choice.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| career_portrait_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide inclusive helper-role visuals for scenario decisions. | Create a set of inclusive child-friendly helper-role cards, including doctor, firefighter, chef, gardener, bus driver, teacher, engineer, and artist. Show one adult character per card with one simple tool, plain background, no text, no stereotypes, and no brands. | Show one role card before asking what the helper should do. | If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person. | Avoid gender, race, or class stereotypes; no emergency gore; no real person photos. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| career_portrait_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide inclusive helper-role visuals for scenario decisions. | new_ai_generated_asset | Show one role card before asking what the helper should do. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person. |

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `career_portrait_cards_01`, `helpful_action_choice`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `decide` mechanic.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `decide` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
