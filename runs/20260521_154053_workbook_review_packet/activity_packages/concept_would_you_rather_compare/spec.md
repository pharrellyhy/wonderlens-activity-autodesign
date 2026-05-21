# Two-Choice Compare Chat -- Authoring Spec

> CAT1 concept package . Concept source: `source_would_you_rather` . Mechanic: `compare`

## Premise

The child chooses between two playful options and explains the preference or tradeoff. The activity turns that source promise into a cat1 runtime package where the child becomes the Choice Comparator. The repeated action is `compare`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `compare`
- **Entity role:** catalyst
- **Progression axis:** perspective, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child chooses between two playful options and explains the preference or tradeoff.
- **Canonical mechanic:** `compare`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Conversation break, story reflection, or choice-making activity.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Discovery / `field_experiment` supplies the emotional payoff while `compare` remains the child-action contract.
- **Assumptions:** The repeated action is compare two options, choose one, and name why.

## Selection Trigger

Start during a conversation break, story reflection, or choice-making activity. No asset support is required; the runtime can use simple choice bubbles or voice-only prompts.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** Choices stay safe, silly, and non-shaming. The repeated action is compare, choose, and explain.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Pick One, Round 2 -- Say Why, and Round 3 -- Compare the Tradeoff each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The final screen shows the chosen side and the fair reason for the other side, making preference feel thoughtful.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `preference_tradeoff`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `compare` mechanic.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `compare` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
