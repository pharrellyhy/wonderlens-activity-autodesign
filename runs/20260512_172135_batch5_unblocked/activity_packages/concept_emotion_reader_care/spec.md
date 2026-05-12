# Feeling Helper Station -- Authoring Spec

> CAT1 concept package . Concept source: `source_emotion_reader` . Mechanic: `care`

## Premise

The child notices an obvious expression or body cue, names a possible need with "might" language, and chooses gentle help. The activity turns that source promise into a cat1 runtime package where the child becomes the Feeling Helper. The repeated action is `care`, and the payoff is visible comfort tied to the child's own choices.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `care`
- **Entity role:** catalyst
- **Progression axis:** responsibility, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child notices a visible cue, names a possible need without diagnosing, and chooses gentle care.
- **Canonical mechanic:** `care`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** A character, animal, or story moment shows an obvious emotional expression.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `emotion_expression_cards_01` is optional card_set support; fallback behavior is documented.
- **Product capability flags:** none; optional card display has a voice-only story fallback.
- **Scaffold fit:** acceptable. Nurture / `care_station` supplies the emotional payoff while `care` remains the child-action contract.
- **Assumptions:** Avoid claiming to diagnose a real person's emotion. Use "might feel" language and ask the child for evidence.

## Selection Trigger

Start when a character, animal, or story moment shows an obvious emotional expression. If optional visual support is unavailable, use the fallback behavior from the Asset Brief and keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Nurture
- **Game style:** `care_station`
- **Why this scaffold:** The copy uses might-feel language and asks for visible evidence, avoiding diagnosis while preserving the care mechanic.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Worried Hands Need, Round 2 -- Tired Body Need, and Round 3 -- Brave Try Need each follow the care adapter: visible cue, possible need, child care idea, visible comfort response.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The child's three care choices become a comfort path: ask first, quiet rest, safe try.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| emotion_expression_cards_01 | card_set | optional | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide simple character expressions that children can interpret with evidence. | Create a set of friendly illustrated character expression cards for children ages 4-7. Include happy, worried, proud, tired, surprised, and frustrated expressions. Use one character per card, clear face and body cue, plain background, no text, no stereotypes, and no real people. | Show one expression card when asking what the character might feel. | If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. | No real child faces, no intense distress, no medical or mental-health diagnosis framing. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| emotion_expression_cards_01 | card_set | optional | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide simple character expressions that children can interpret with evidence. | new_ai_generated_asset | Show one expression card when asking what the character might feel. Persist or hide behavior: keep visible only through prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. |

## Extensibility Notes

- Reusable slots: `{story_character}`, `{visible_feeling_cue}`, `{possible_feeling}`, and `emotion_expression_cards_01`.
- Retarget by replacing approved expression cards or story cues while preserving might-feel language and care suggestions.
- Retargeting guardrail: never infer or diagnose a real person from camera input; cues must be prebuilt/story-provided or child-described.

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `care` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
