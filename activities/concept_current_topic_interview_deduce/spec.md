# Reason Reporter Interview -- Authoring Spec

> CAT1 concept package . Concept source: `source_current_topic_interview` . Mechanic: `deduce`

## Premise

The child discusses an age-appropriate topic by giving an opinion and a reason. The activity turns that source promise into a cat1 runtime package where the child becomes the Reason Reporter. The repeated action is `deduce`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T2
- **Activity category:** cat1
- **Mechanic:** `deduce`
- **Entity role:** catalyst
- **Progression axis:** perspective, level 3

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child discusses an age-appropriate topic by giving an opinion and a reason.
- **Canonical mechanic:** `deduce`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Older child and parent select an age-appropriate news, school, community, or nature topic.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Mystery / `mystery_lens` supplies the emotional payoff while `deduce` remains the child-action contract.
- **Assumptions:** The repeated action is infer, justify, and revise with new evidence.

## Selection Trigger

Start when an older child and parent select an age-appropriate school, community, or nature topic. No asset support is required; avoid live-news claims unless the parent provides the topic.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** Topics must be parent-selected and age-appropriate. The AI asks for reasons and evidence instead of live-news claims.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Give an Opinion, Round 2 -- Add a Reason, and Round 3 -- Use a New Clue each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The notebook shows opinion, reason, and new clue together, so the child sees reasoning grow.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T2 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The loop has escalating rounds and a visible payoff earned from the child's repeated action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `deduce` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- reviewer-agent pass by Averroes after package-quality edits.
