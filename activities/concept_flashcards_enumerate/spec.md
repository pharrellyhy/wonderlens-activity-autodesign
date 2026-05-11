# Picture Pop Cards -- Authoring Spec

> CAT1 concept package . Concept source: `source_flashcards` . Mechanic: `enumerate`

## Premise

The child recognizes a picture card, names what they see, and answers one tiny follow-up. The activity turns that source promise into a cat1 runtime package where the child becomes the Picture Namer. The repeated action is `enumerate`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T0
- **Activity category:** cat1
- **Mechanic:** `enumerate`
- **Entity role:** reference
- **Progression axis:** form, level 1

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child recognizes a picture card, names what they see, and answers one tiny follow-up.
- **Canonical mechanic:** `enumerate`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Parent selects a vocabulary, shape, color, animal, or object-recognition practice mode.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `generic_flashcard_library_01` is required `card_set` support; fallback behavior is documented.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** acceptable. Mystery / `mystery_lens` supplies the emotional payoff while `enumerate` remains the child-action contract.
- **Assumptions:** Keep each card to one clear recognition target and one optional extension question.

## Selection Trigger

Start when Parent selects a vocabulary, shape, color, animal, or object-recognition practice mode. If the required visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** The package is picture-first and does not require text reading. If cards are unavailable, it can pivot to a photographed object.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Name the Picture, Round 2 -- Notice One Feature, and Round 3 -- Answer a Tiny Follow-Up each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The card turns into a named picture badge with one feature the child noticed.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| Field | Value |
|---|---|
| asset_id | generic_flashcard_library_01 |
| asset_type | card_set |
| requiredness | required |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose | Provide simple picture-first recognition cards. |
| prompt_en | Create a generic children's flashcard library for common objects, colors, shapes, animals, and foods. Use one clear subject per card, plain light background, no extra text except optional single-word labels in a separate variant, no brands, and consistent friendly illustration style. |
| source | new_ai_generated_asset |
| display_behavior | Show one card at a time and ask the child to name or identify it. |
| fallback_behavior | If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card. |
| safety_constraints | No real child photos, no copyrighted characters, no dangerous objects, and no cluttered scenes. |
## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T0 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The loop has escalating rounds and a visible payoff earned from the child's repeated action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `enumerate` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- reviewer-agent pass by Averroes after package-quality edits.
