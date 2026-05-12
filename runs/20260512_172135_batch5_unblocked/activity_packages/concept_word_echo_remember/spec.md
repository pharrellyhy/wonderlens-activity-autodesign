# Echo Word Stage -- Authoring Spec

> CAT1 concept package . Concept source: `source_word_echo_practice` . Mechanic: `remember`

## Premise

The AI says a simple word or phrase and the child repeats it back in a playful echo round. The activity turns that source promise into a cat1 runtime package where the child becomes the Echo Word Keeper. The repeated action is `remember`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T0
- **Activity category:** cat1
- **Mechanic:** `remember`
- **Entity role:** catalyst
- **Progression axis:** form, level 1

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The AI says a simple word or phrase and the child repeats it back in a playful echo round.
- **Canonical mechanic:** `remember`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child enters language-practice mode, asks what an object is called, or photographs a familiar object whose name can be repeated safely.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `word_echo_cards_01` is optional card_set support; fallback behavior is documented.
- **Product capability flags:** none; optional display support has a voice-only fallback.
- **Scaffold fit:** acceptable. Performance / `voice_stage` supplies the emotional payoff while `remember` remains the child-action contract.
- **Assumptions:** The repeated child action is listen, echo, and try again with one word or one short doubled echo. If no card is shown, run voice-only and do not claim the screen displays text.

## Selection Trigger

Start when Child enters language-practice mode, asks what an object is called, or photographs a familiar object whose name can be repeated safely. If optional visual support is unavailable, use the fallback behavior from the Asset Brief and keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Performance
- **Game style:** `voice_stage`
- **Why this scaffold:** The activity keeps recall low-pressure: the child hears, repeats, and plays with one tiny word pattern at a time. Optional cards support the word cue, but the runtime can stay voice-only.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Tiny Hide Echo and Round 2 -- Double Pattern Echo ask for different child contributions and update different progress tokens, keeping the T0 runtime to two rounds.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The word ladder opens only after the child returns the single-word echo and the doubled pattern; the stage copies the child's pattern back as the payoff.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| word_echo_cards_01 | card_set | optional | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-2; prod.step_4 | center_card_area | Provide a simple picture cue for the word the child repeats. | Create a child-friendly vocabulary card set for common household objects. Each card shows one centered object, one large simple English word label, a clean light background, soft colors, and no extra text. | Show one card when introducing a word, then hide or keep it small while the child repeats by voice. | If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word. | No real child photos, no brands, no complex text, and no cluttered composition. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| word_echo_cards_01 | card_set | optional | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-2; prod.step_4 | center_card_area | Provide a simple picture cue for the word the child repeats. | new_ai_generated_asset | Show one card when introducing a word, then hide or keep it small while the child repeats by voice. Persist or hide behavior: keep visible only through prod.step_1; prod.step_2; prod.step_3.round_1-2; prod.step_4, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word. |

## Extensibility Notes

- Reusable slots: `{target_word}`, `{echo_pattern}`, `{target_phrase}`, and `word_echo_cards_01`.
- Retarget by replacing the picture/word card and echo pattern while keeping the listen -> repeat -> playful variation loop.
- Retargeting guardrail: do not claim audio-quality verification; audience reactions are fictional and based on participation.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T0 expectations with two short echo rounds and call-and-response prompts. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior for the optional card support. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The tiny hide, doubled pattern, and stage-copy reveal create uncertainty and an earned payoff without assessing pronunciation. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `remember` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
