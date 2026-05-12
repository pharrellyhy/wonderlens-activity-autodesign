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
- **Core promise:** The child recognizes a picture card, names what they see, and answers one tiny feature/function follow-up.
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

- **Distinct round design:** Round 1 -- Name the Picture and Round 2 -- Answer a Tiny Follow-Up each ask for a different child contribution and update a different progress token, keeping the T0 loop to two rounds.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The card turns into a named picture badge with one action clue the child answered.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| generic_flashcard_library_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_card_area | Provide simple picture-first recognition cards. | Create a generic children's flashcard library for common objects, colors, shapes, animals, and foods. Use one clear subject per card, plain light background, no extra text except optional single-word labels in a separate variant, no brands, and consistent friendly illustration style. | Show one card at a time and ask the child to name or identify it. | If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card. | No real child photos, no copyrighted characters, no dangerous objects, and no cluttered scenes. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| generic_flashcard_library_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_card_area | Provide simple picture-first recognition cards. | new_ai_generated_asset | Show one card at a time and ask the child to name or identify it. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-2, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card. |

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `generic_flashcard_library_01`, `picture_card_target`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `enumerate` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language, answer length, and the two-round task load match T0 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The loop has escalating rounds and a visible payoff earned from the child's repeated action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `enumerate` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
