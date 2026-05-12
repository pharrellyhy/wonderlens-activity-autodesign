# Reason Reporter Interview -- Authoring Spec

> CAT1 concept package . Concept source: `source_current_topic_interview` . Mechanic: `deduce`

## Premise

The child investigates the concrete safe sample topic "should the class plant flowers first or vegetables first?" by using clues to infer a reasoned conclusion. The package remains retargetable to other parent-approved topics, but `prod.md` is executable without unresolved placeholders.

## Target

- **Primary tier:** T2
- **Activity category:** cat1
- **Mechanic:** `deduce`
- **Entity role:** catalyst
- **Progression axis:** perspective, level 3

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child uses clues from an age-appropriate topic to infer a conclusion and explain the reason.
- **Canonical mechanic:** `deduce`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Older child and parent select an age-appropriate news, school, community, or nature topic.
- **Mapping use:** no required mapping for this package; the runtime uses a concrete school-garden sample while the extensibility notes define retargeting guardrails.
- **Asset dependency:** `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Mystery / `mystery_lens` supplies the emotional payoff while `deduce` remains the child-action contract.
- **Assumptions:** The repeated action is clue -> conclusion -> reason, with a final revision when timing evidence changes the best answer.

## Selection Trigger

Start when an older child and parent select an age-appropriate school, community, or nature topic. No asset support is required; avoid live-news claims unless the parent provides the topic.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** Topics must be parent-selected and age-appropriate. The AI uses safe fictional clues and asks for evidence-based inference instead of live-news claims.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Use the First Clue, Round 2 -- Add a Reason From Evidence, and Round 3 -- Make the Final Deduction each ask the child to infer from clue evidence and update a different notebook token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The notebook resolves the clue chain into "flowers first now, vegetables later," so the child sees how evidence changed the conclusion.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Extensibility Notes

- Reusable slots: `{safe_topic_question}`, `{opinion_a}`, `{opinion_b}`, `{safe_topic_clue_2}`, `{safe_topic_clue_3}`, and `{runtime_tier}`.
- Retarget by replacing the school-garden sample with a parent-approved topic that has two age-safe options, at least two evidence clues, and one timing or priority clue that can justify revision.
- Retargeting guardrail: `prod.md` must never ship with raw placeholders in child-facing dialogue; instantiate the topic before package approval.

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

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
