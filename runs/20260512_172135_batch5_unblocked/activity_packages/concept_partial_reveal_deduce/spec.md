# Partial Reveal Guess -- Authoring Spec

> Category 1 (Sustained Verbal Interaction) . Concept-only partial-card mystery . Mechanic: `deduce`

## Premise

The AI shows one cropped, distinctive part from a prebuilt card set: rabbit ears, duck feet, fish scales, tiger tail, or a similar safe detail. The child guesses the whole animal or object and explains which visible clue helped. Each round uses the same loop: inspect the part, infer the whole, justify with evidence, then reveal.

## Target

- **Primary tier:** T1 (ages 4-6)
- **Activity category:** Cat1, sustained in-device verbal interaction
- **Mechanic:** `deduce`
- **Entity role:** reference; prebuilt partial cards provide the evidence source
- **Progression axis:** Form, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** preserve the source partial-reveal game: visible part first, child guess second, evidence explanation before or during reveal.
- **Canonical mechanic:** `deduce`; Step 3's repeated child action is inspect a partial clue, guess the whole, and explain evidence.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** child photographs an animal toy, animal picture, or enters partial-reveal guessing mode.
- **Mapping use:** no entity mapping is required. The card set supplies generic, safe reference clues.
- **Asset dependency:** required prebuilt support. `partial_reveal_cards_01` is required for the full visual experience and must be documented here. If cards are unavailable, the runtime switches to voice-only partial-clue riddles and must not claim the screen is showing a picture.
- **Product capability flags:** `requires_asset_display`.
- **Scaffold fit:** strong. Mystery / `mystery_lens` directly supports clue, guess, evidence, and reveal.
- **Assumptions:** the runtime uses three rounds rather than five to fit the T1 package length. Each card has a safe known answer and one distinctive part large enough for the child to inspect.

## Selection Trigger

Start this activity when the child enters partial-reveal guessing mode or photographs an animal toy, animal picture, or common object that can inspire a safe mystery. The photographed item is a catalyst only; the actual challenges come from `partial_reveal_cards_01`.

If `partial_reveal_cards_01` cannot be displayed, use voice-only part riddles such as "I am thinking of long ears" and keep screen states generic. Do not say "look at this picture" unless the card is actually visible.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** the child solves a hidden whole from visible evidence, and the reveal creates a clear "I figured it out" payoff.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| partial_reveal_cards_01 | card_set | required | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide visible partial evidence so the child can infer the whole animal or object. | Create a set of partial-reveal animal guessing cards for children ages 4-6. Each card should show only one distinctive part of a common animal, such as a tiger tail, rabbit ears, elephant trunk, duck feet, or fish scales. Use a consistent soft illustration style, plain light background, no text, no scary details, and keep the cropped part large and easy to inspect. | Show one partial-reveal card full screen each round. The child observes the part, guesses the whole, and explains the evidence. | If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. | No real child photos, no gore or scary details, no predation scenes, and clear inspectable cropped parts. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| partial_reveal_cards_01 | card_set | required | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide visible partial evidence so the child can infer the whole animal or object. | new_ai_generated_asset | Show one partial-reveal card full screen each round. The child observes the part, guesses the whole, and explains the evidence. Persist or hide behavior: keep visible only through prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4, then summarize or hide at Step 4 according to the payoff. | If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. |

## Runtime Detail Floor Notes

- **Distinct round design:** The three clues use different part-whole evidence types: ears, feet, and tail pattern. Each round asks the child to name both the whole and the clue that supports the guess.
- **Branch specificity:** Follow-ups separate guess quality from evidence quality. A near guess can still be praised for noticing a useful clue, then narrowed with a targeted hint.
- **Earned magic moment:** The final board pairs each cropped part with its full answer, so the child sees how small visible details became whole animals.
- **Residual risk:** The full visual experience depends on `partial_reveal_cards_01`; the voice-only fallback preserves deduction but is less inspectable than the card version.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `partial_reveal_cards_01`, `partial_visual_clue`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `deduce` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md` Mystery + Cat1 rules, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The activity uses prebuilt card display, dialogue, child guesses, and fallback voice riddles. It does not require OCR, face/expression/pose detection, IMU sensing, non-speech audio detection, or before/after state comparison. |
| 2 | Hook & Transition | PASS | Step 1 opens with a hidden-whole mystery and invites looking for evidence, not knowledge testing. |
| 3 | Edge Case Coverage | PASS | Every dialogue step includes ideal, unexpected, and no-response branches with 2s waits; unexpected guesses are validated before hints. |
| 4 | IB Completeness | PASS | Form and Connection are named, KUD is specific, related concepts and ATL skills are present, and the closing ties part-to-whole evidence to the concepts. |
| 5 | Tier Appropriateness | PASS | T1 children inspect one clear clue per round, make short guesses, and explain simple evidence with scaffolded sentence starters. |
| 6 | Dialogue Specificity | PASS | AI lines are concrete spoken dialogue with tone markers and no abstract runtime instructions. |
| 7 | Screen & UI Completeness | PASS | Every step includes concrete screen states for both card-display mode and voice-only fallback mode. |
| 8 | Entity Mapping Alignment | N/A | Concept-only package with no `mapping=` assignment and no entity-specific mapping claims. |
| 9 | Game Feel | PASS | Cropped clues, clue tokens, suspenseful reveals, and the final part-whole board create uncertainty and payoff. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | `deduce` is preserved in Step 3 and tag metadata; required prebuilt cards and fallback behavior are disclosed. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
