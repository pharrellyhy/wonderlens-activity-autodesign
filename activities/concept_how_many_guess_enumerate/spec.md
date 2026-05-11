# Guess Then Count -- Authoring Spec

> CAT1 concept package . Concept source: `source_how_many_guess` . Mechanic: `enumerate`

## Premise

The child estimates how many objects are visible, then counts together with the AI. The activity turns that source promise into a cat1 runtime package where the child becomes the Careful Counter. The repeated action is `enumerate`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `enumerate`
- **Entity role:** reference
- **Progression axis:** form, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child estimates how many objects are visible, then counts together with the AI.
- **Canonical mechanic:** `enumerate`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Screen can show a small set of objects or the camera sees countable items.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `how_many_count_cards_01` is required `card_set` support; fallback behavior is documented.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** acceptable. Discovery / `prediction_lab` supplies the emotional payoff while `enumerate` remains the child-action contract.
- **Assumptions:** The repeated action is estimate, count, and check.

## Selection Trigger

Start when Screen can show a small set of objects or the camera sees countable items. If the required visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `prediction_lab`
- **Why this scaffold:** The package preserves estimate-before-count and keeps counts low enough for T1.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Make a Guess, Round 2 -- Count Carefully, and Round 3 -- Compare Guess and Count each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The guess bubble and count answer snap together, turning a quick guess into checked evidence.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| Field | Value |
|---|---|
| asset_id | how_many_count_cards_01 |
| asset_type | card_set |
| requiredness | required |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose | Show small countable sets for estimate-then-count rounds. |
| prompt_en | Create a set of counting cards for children ages 4-6. Each card shows 3 to 10 identical or related objects, such as stars, apples, buttons, shells, or toy cars. Use clear spacing, plain background, no text, no overlapping objects, and high contrast for counting. |
| source | new_ai_generated_asset |
| display_behavior | Show one card, ask the child to guess how many, then count together. |
| fallback_behavior | If cards are unavailable, use real photographed countable items or voice-only counting and do not claim a card is displayed. |
| safety_constraints | No tiny choking hazard emphasis, no clutter, no brands, and no confusing overlapping objects. |
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `enumerate` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- reviewer-agent pass by Averroes after package-quality edits.
