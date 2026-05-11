# Tiny Poem Workshop -- Authoring Spec

> CAT1 concept package . Concept source: `source_little_poem_generator` . Mechanic: `build`

## Premise

The child contributes words, images, or feelings and co-creates a short poem with the AI. The activity turns that source promise into a cat1 runtime package where the child becomes the Tiny Poet Builder. The repeated action is `build`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `build`
- **Entity role:** reference
- **Progression axis:** connection, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child contributes words, images, or feelings and co-creates a short poem with the AI.
- **Canonical mechanic:** `build`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child photographs an object, chooses a feeling, or names a favorite topic.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Creation / `inventor_workshop` supplies the emotional payoff while `build` remains the child-action contract.
- **Assumptions:** The repeated action is add an ingredient, hear it woven into a poem, and choose the next ingredient.

## Selection Trigger

Start when the child photographs an object, chooses a feeling, or names a favorite topic. No asset support is required; the runtime may show simple word tiles or run voice-only.

## Experience Pillar & Game Style

- **Pillar:** Creation
- **Game style:** `inventor_workshop`
- **Why this scaffold:** The child contributes ingredients each round. The AI weaves, but the poem is visibly built from child choices.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Add a Seeing Word, Round 2 -- Add a Feeling Word, and Round 3 -- Add an Action Word each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The three ingredient tiles fold into a four-line poem that includes the child words.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `build` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- Reviewer B repaired the Step 4 poem reveal and rechecked package-local validation.
