# Feeling Helper Station -- Authoring Spec

> CAT1 concept package . Concept source: `source_emotion_reader` . Mechanic: `care`

## Premise

The child notices an obvious expression or body cue and thinks about what feeling or help might fit. The activity turns that source promise into a cat1 runtime package where the child becomes the Feeling Helper. The repeated action is `care`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `care`
- **Entity role:** catalyst
- **Progression axis:** responsibility, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child notices an obvious expression or body cue and thinks about what feeling or help might fit.
- **Canonical mechanic:** `care`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** A character, animal, or story moment shows an obvious emotional expression.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `emotion_expression_cards_01` is optional card_set support; fallback behavior is documented.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** acceptable. Nurture / `care_station` supplies the emotional payoff while `care` remains the child-action contract.
- **Assumptions:** Avoid claiming to diagnose a real person's emotion. Use "might feel" language and ask the child for evidence.

## Selection Trigger

Start when A character, animal, or story moment shows an obvious emotional expression. If the required visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Nurture
- **Game style:** `care_station`
- **Why this scaffold:** The copy uses might-feel language and asks for visible evidence, avoiding diagnosis while preserving the care mechanic.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Notice the Cue, Round 2 -- Name the Evidence, and Round 3 -- Offer Help each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** Your noticing changed the scene: the character gets a comfort plan, not just a feeling label.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| Field | Value |
|---|---|
| asset_id | emotion_expression_cards_01 |
| asset_type | card_set |
| requiredness | optional |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose | Provide simple character expressions that children can interpret with evidence. |
| prompt_en | Create a set of friendly illustrated character expression cards for children ages 4-7. Include happy, worried, proud, tired, surprised, and frustrated expressions. Use one character per card, clear face and body cue, plain background, no text, no stereotypes, and no real people. |
| source | new_ai_generated_asset |
| display_behavior | Show one expression card when asking what the character might feel. |
| fallback_behavior | If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. |
| safety_constraints | No real child faces, no intense distress, no medical or mental-health diagnosis framing. |
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

**Overall**: ALL PASS -- reviewer-agent pass by Dalton after package-quality edits.
