# Two-Door Story Quest -- Authoring Spec

> Category 1 (Sustained Verbal Interaction) . Concept-only story mode . Mechanic: `decide`

## Premise

The AI turns a toy, object, or story-mode request into a short voice-led adventure. The child becomes the Story Path Chooser. In each round, the AI describes a small scene and offers two clear next steps. The child decides, and the story changes because of that choice. The payoff is a final path map showing the child's three decisions as one adventure.

## Target

- **Primary tier:** T1 (ages 4-6)
- **Activity category:** Cat1, sustained in-device verbal interaction
- **Mechanic:** `decide`
- **Entity role:** catalyst; the photographed toy or object starts the story but does not supply factual claims
- **Progression axis:** Perspective, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** preserve the source concept's choice-point story loop.
- **Canonical mechanic:** `decide`; Step 3's repeated child action is choosing between two story paths.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** child enters story mode or photographs a toy or object that can become a story character.
- **Mapping use:** no entity mapping is required. The package avoids entity-specific facts.
- **Asset dependency:** `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Adventure / `time_traveler` supports a journey with visible choice points, but this is a general branching story rather than literal time travel.
- **Assumptions:** branching remains voice-led and authored. The runtime does not need a complex branching UI; it only tracks three spoken choices and displays simple path tokens.

## Selection Trigger

Start this activity when the child enters story mode, asks for a story game, or photographs a toy/object that can become a story starter. If the photo is unclear, the AI can say "Let's make the mystery thing our hero" instead of naming it.

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `time_traveler`
- **Why this scaffold:** the child travels through a sequence of story moments, makes a decision at each stop, and sees the whole path assembled at the end.

## Runtime Detail Floor Notes

- **Distinct round design:** The three decisions affect different story layers: world entry, helper/tool, and ending destination. Each choice changes the next visual state instead of only filling a token.
- **Branch specificity:** Unexpected child ideas are handled as story material when possible; the AI validates the idea, then maps it back to one of the two available choices so the runtime does not need an open-ended branching engine.
- **Earned magic moment:** The final map displays the chosen door, helper, and ending as a connected route. The child sees a story world that exists because of their decisions.
- **Residual risk:** The package is authored branching, not dynamic narrative planning. It preserves agency through three clear consequences rather than unlimited story generation.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `story_choice_path`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `decide` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md` Adventure + Cat1 rules, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The activity uses voice dialogue and simple on-screen choice tokens. It does not require OCR, face/expression/pose detection, IMU sensing, non-speech audio detection, or before/after state comparison. |
| 2 | Hook & Transition | PASS | Step 1 opens with story wonder, not testing, and turns the starter object or mode into a path-choice game. |
| 3 | Edge Case Coverage | PASS | Every dialogue step includes ideal, unexpected, and no-response branches with 2s waits; unexpected branches validate before redirecting to a choice. |
| 4 | IB Completeness | PASS | Perspective and Causation are named, KUD is specific, related concepts and ATL skills are present, and the closing connects choices to viewpoints and consequences. |
| 5 | Tier Appropriateness | PASS | T1 children make three two-option choices, hear short scenes, and can answer with one word or a phrase. |
| 6 | Dialogue Specificity | PASS | AI lines are concrete spoken dialogue with tone markers and no abstract runtime instructions. |
| 7 | Screen & UI Completeness | PASS | Every step includes specific screen states: two doors, path tokens, reaction marks, and final path map. |
| 8 | Entity Mapping Alignment | N/A | Concept-only package with no `mapping=` assignment and no entity-specific mapping claims. |
| 9 | Game Feel | PASS | Each choice has uncertainty and a distinct revealed consequence: door changes the world, helper changes the road, and ending changes the payoff. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | `decide` is preserved in Step 3 and tag metadata; each decision applies a consequence while the voice-led branching and time_traveler scaffold compromise are disclosed. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
