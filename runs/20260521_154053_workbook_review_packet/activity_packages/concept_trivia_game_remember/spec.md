# Tiny Trivia Trail -- Authoring Spec

> CAT1 concept package . Concept source: `source_trivia_game` . Mechanic: `remember`

## Premise

The child answers short memory or knowledge questions and receives a simple explanation. The activity turns that source promise into a cat1 runtime package where the child becomes the Trivia Trail Finder. The repeated action is `remember`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `remember`
- **Entity role:** catalyst
- **Progression axis:** connection, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child answers short memory or knowledge questions and receives a simple explanation.
- **Canonical mechanic:** `remember`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child has just explored a topic and can answer short fact or memory questions.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `trivia_reward_board_01` is optional `ui_overlay` support; fallback behavior is documented.
- **Product capability flags:** none; optional reward-board display has a voice-only fallback.
- **Scaffold fit:** acceptable. Mystery / `mystery_lens` supplies the emotional payoff while `remember` remains the child-action contract.
- **Assumptions:** Keep questions brief and age-appropriate. If no reward board exists, use verbal celebration only.

## Selection Trigger

Start when Child has just explored a topic and can answer short fact or memory questions. If optional visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** Trivia is framed as recall with explanation, not pressure. Optional reward visuals are only used when stateful display exists.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Remember One Detail, Round 2 -- Choose the Better Answer, and Round 3 -- Explain in Your Words each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The trail reveals three remembered clues and turns them into a tiny topic map.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| trivia_reward_board_01 | ui_overlay | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | support_panel | Optionally visualize progress through trivia rounds. | Create a simple child-friendly trivia progress board with five empty star spaces and a small castle or clubhouse outline at the end. Use warm colors, clean shapes, no text, no competitive ranking, no brands, and enough blank space for runtime stars. | Show progress only if product can update state after each answer. | If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added. | No leaderboards, no shame states, no gambling-like reward visuals, and no brands. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| trivia_reward_board_01 | ui_overlay | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | support_panel | Optionally visualize progress through trivia rounds. | new_ai_generated_asset | Show progress only if product can update state after each answer. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added. |

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `trivia_reward_board_01`, `remembered_fact_clue`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `remember` mechanic.
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `remember` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
