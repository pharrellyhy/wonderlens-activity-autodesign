# Plant State Evidence Lab -- Authoring Spec

> CAT5 concept package . Concept source: `source_plant_state_compare` . Mechanic: `compare`

## Premise

The child compares visible plant clues and state-word options, such as fresh versus changed evidence and healthy versus wilting. The activity turns that source promise into a cat5 runtime package where the child becomes the Plant State Investigator. The repeated action is `compare`, and the payoff is a visible evidence strip tied to the child's comparisons.

## Target

- **Primary tier:** T1
- **Activity category:** cat5
- **Mechanic:** `compare`
- **Entity role:** subject
- **Progression axis:** change, level 2

## Adaptation Rationale

- **Input mode:** parameterized.
- **Core promise:** The child compares visible plant evidence and state-word options before making a likely state claim.
- **Canonical mechanic:** `compare`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** A plant photo shows a clear state, such as blooming, wilting, dried, or after watering.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Discovery / `field_experiment` supplies the emotional payoff while `compare` remains the child-action contract.
- **Assumptions:** Mapping improves vocabulary and lifecycle facts, but the child action should remain compare, describe evidence, and explain a likely state.

## Selection Trigger

Start when a plant photo shows a clear state, such as blooming, wilting, dried, or newly sprouting. If the photo is unclear, ask for a closer plant view or switch to a voice-only "likely plant state" example without claiming screen evidence.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** The package keeps comparison visible in every round and uses likely language; it does not diagnose invisible plant health.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Fresh Clue vs Changed Clue, Round 2 -- State Word vs State Word, and Round 3 -- Stronger Evidence Check each require the child to compare two visible or named options.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The final evidence strip shows clue-vs-clue, state-vs-state, and strongest-evidence comparisons, so the likely plant state is earned by repeated comparison.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `compare` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- reviewer-agent pass by Dalton after package-quality edits.
