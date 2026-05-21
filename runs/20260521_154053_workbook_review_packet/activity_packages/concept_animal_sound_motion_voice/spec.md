# Animal Echo Stage -- Authoring Spec

> Category 1 (Sustained Verbal Interaction) . Concept-only animal-sound mode . Mechanic: `motion_voice`

## Premise

The AI invites a toddler or preschooler onto a tiny animal stage. The child hears a familiar animal prompt, then imitates the animal sound or speaks in the animal role. The AI acts as a warm audience and celebrates any attempt. Optional animal cards can help recognition, but the activity remains voice-led if cards are unavailable.

## Target

- **Primary tier:** T0 (ages 2-4)
- **Activity category:** Cat1, sustained in-device verbal interaction
- **Mechanic:** `motion_voice`
- **Entity role:** catalyst; an animal toy/photo or mode starts the stage game
- **Progression axis:** Perspective, level 1

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** preserve the source concept's animal sound imitation and role play.
- **Canonical mechanic:** `motion_voice`; Step 3's repeated child action is imitate a sound or speak in an animal role.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** child photographs an animal toy, animal picture, or enters animal-sound mode.
- **Mapping use:** no entity mapping is required. The package uses familiar animals and avoids entity-specific facts.
- **Asset dependency:** optional support. `animal_sound_cards_01` may show friendly animal cards, but the activity works by voice description if cards are unavailable.
- **Product capability flags:** none; optional visual support has a voice-only fallback.
- **Scaffold fit:** strong. Performance / `voice_stage` supports animal sounds, audience reaction, and encore.
- **Assumptions:** T0 runtime uses two rounds, not three, to keep call-and-response short. The system must not claim it verifies sound quality, volume, or exact animal imitation; all attempts are accepted.

## Selection Trigger

Start this activity when the child photographs an animal toy, animal picture, or asks for animal-sound play. If the photo is unclear, the AI can launch with common animals by voice only.

## Experience Pillar & Game Style

- **Pillar:** Performance
- **Game style:** `voice_stage`
- **Why this scaffold:** the child performs short animal sounds for a friendly audience and receives an encore-style payoff.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| animal_sound_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_card_area | Help the child recognize the animal they are about to imitate. | Create a set of friendly animal picture cards for toddlers and preschoolers. Include common animals such as cat, dog, cow, duck, sheep, and lion. Use a plain bright background, simple expressive illustrations, one animal per card, no text, no scary poses. | Show one animal card each round while the AI invites the child to imitate its sound. | If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. | No real child photos, no attack or predation scenes, and friendly animal poses only. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| animal_sound_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-2 | center_card_area | Help the child recognize the animal they are about to imitate. | new_ai_generated_asset | Show one animal card each round while the AI invites the child to imitate its sound. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-2, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. |

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 uses a sleeping cat and a tiny "meow" wake-up; Round 2 changes the sound, movement, and visual payoff to a hidden duck that wiggles. The child is not repeating a generic "make animal sound" prompt.
- **Branch specificity:** Unexpected responses are accepted as performance attempts first, then redirected to the animal sound. No branch asks the system to verify audio quality or movement accuracy.
- **Earned magic moment:** The encore audience appears only after both hidden animals have been woken by the child's sound attempts. The badge is a record of the child's stage turns, not a generic reward.
- **Residual risk:** Because ASR cannot verify non-speech animal sounds reliably, the AI treats any vocalization, word, or role-play attempt as valid participation.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `animal_sound_cards_01`, `animal_voice`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `motion_voice` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md` Performance + Cat1 rules, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The activity accepts any vocal or role-play attempt and does not require sound-quality detection, OCR, face/expression/pose detection, IMU sensing, or before/after state comparison. |
| 2 | Hook & Transition | PASS | Step 1 opens with stage excitement and animal play, not testing. |
| 3 | Edge Case Coverage | PASS | Every dialogue step includes ideal, unexpected, and no-response branches with 2s waits; unexpected branches validate before redirecting. |
| 4 | IB Completeness | PASS | Perspective and Form are named, KUD is specific, related concepts and ATL skills are present, and the closing connects role voice to the concepts. |
| 5 | Tier Appropriateness | PASS | T0 uses two rounds, short sentences, simple animals, sound words, and call-and-response. |
| 6 | Dialogue Specificity | PASS | AI lines are concrete spoken dialogue with tone markers and no abstract runtime instructions. |
| 7 | Screen & UI Completeness | PASS | Every step includes concrete screen states, optional `animal_sound_cards_01` behavior, voice-only fallback, stage lights, and encore badge. |
| 8 | Entity Mapping Alignment | N/A | Concept-only package with no `mapping=` assignment and no entity-specific mapping claims. |
| 9 | Game Feel | PASS | Each sound wakes a hidden stage guest, and the encore reveals a tiny surprise audience for a clear payoff. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | `motion_voice` is preserved in Step 3 and tag metadata; optional cards and T0 two-round adaptation are disclosed. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260521_154053_workbook_review_packet/review_notes.md`.
