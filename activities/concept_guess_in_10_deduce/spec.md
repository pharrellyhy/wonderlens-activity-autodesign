# Guess in 10 -- Authoring Spec

> Category 1 (Sustained Verbal Interaction) . Concept-only guessing mode . Mechanic: `deduce`

## Premise

The AI starts a mystery game with one hidden answer, such as a cat, duck, ball, spoon, or backpack. The child hears clues one by one and guesses from evidence. Each round adds a clearer clue, and if the child is stuck, the AI offers a soft hint rather than treating the answer as wrong. Optional reference cards can appear after a reveal or as a stuck hint, but the activity works fully by voice.

## Target

- **Primary tier:** T1 (ages 4-6)
- **Activity category:** Cat1, sustained in-device verbal interaction
- **Mechanic:** `deduce`
- **Entity role:** catalyst; a toy/photo or guessing mode starts the mystery
- **Progression axis:** Function, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** preserve the source clue-by-clue guessing game and frustration-reducing hints.
- **Canonical mechanic:** `deduce`; Step 3's repeated child action is hear clue, infer a guess, and explain or revise from evidence.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** child photographs an animal toy, animal picture, or enters guessing mode.
- **Mapping use:** no entity mapping is required. The package uses common mystery answers and avoids entity-specific facts.
- **Asset dependency:** optional support. `guess_reference_cards_01` may show reference or hint cards, but the runtime must remain honest and voice-led if cards are unavailable.
- **Product capability flags:** `requires_assets` only for optional visual support.
- **Scaffold fit:** strong. Mystery / `mystery_lens` directly supports clue, guess, evidence, and reveal.
- **Assumptions:** the runtime package uses three clue rounds instead of ten to stay concise for T1 while preserving the "Guess in 10" source concept. Hidden answers come from a small safe set of common animals and household objects.

## Selection Trigger

Start this activity when the child asks for a guessing game, enters guessing mode, or photographs an animal toy/object that can catalyze a mystery. The initial photo is optional inspiration; the hidden answer does not need to be the photographed object.

## Experience Pillar & Game Style

- **Pillar:** Mystery
- **Game style:** `mystery_lens`
- **Why this scaffold:** the child deduces a hidden answer from progressive clues, with suspense and a reveal as the magic moment.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|
| guess_reference_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | Provide optional reference pictures before or after a clue round to reduce frustration. | prompt_en: Create a set of friendly reference cards for common animals and household objects for a children's guessing game. Use one centered object per card, plain light background, clear recognizable shapes, soft colors, no text, no scary expressions. Source: new_ai_generated_asset. | Show the matching card after the answer is revealed, or show a partial hint card if the child is stuck. | If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture. | No real child photos, friendly animal expressions, and no dangerous scenes. |

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md` Mystery + Cat1 rules, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The game uses voice clues, child guesses, and optional prebuilt cards. It does not require OCR, face/expression/pose detection, IMU sensing, non-speech audio detection, or before/after state comparison. |
| 2 | Hook & Transition | PASS | Step 1 opens with mystery excitement and a hidden answer, not knowledge testing. |
| 3 | Edge Case Coverage | PASS | Every dialogue step includes ideal, unexpected, and no-response branches with 2s waits; unexpected branches validate before redirecting, and stuck hints are explicit. |
| 4 | IB Completeness | PASS | Function and Form are named, KUD is specific, related concepts and ATL skills are present, and the closing connects clue evidence to the concepts. |
| 5 | Tier Appropriateness | PASS | T1 children hear short clues, make guesses, and use simple evidence language with optional hint support. |
| 6 | Dialogue Specificity | PASS | AI lines are concrete spoken dialogue with tone markers and no abstract runtime instructions. |
| 7 | Screen & UI Completeness | PASS | Every step includes concrete screen states, optional reference-card behavior, voice-only fallback, clue pips, and reveal badge. |
| 8 | Entity Mapping Alignment | N/A | Concept-only package with no `mapping=` assignment and no entity-specific mapping claims. |
| 9 | Game Feel | PASS | Progressive clues create uncertainty, wrong guesses stay playful, and the reveal produces a clear mystery payoff. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | `deduce` is preserved in Step 3 and tag metadata; optional cards and the three-round adaptation are disclosed. |

**Overall**: ALL PASS -- one reviewer issue found and fixed: Round 1's unexpected follow-up now validates uncertainty before redirecting.
