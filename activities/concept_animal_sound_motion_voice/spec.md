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
- **Product capability flags:** `requires_assets` only for optional visual support.
- **Scaffold fit:** strong. Performance / `voice_stage` supports animal sounds, audience reaction, and encore.
- **Assumptions:** T0 runtime uses two rounds, not three, to keep call-and-response short. The system must not claim it verifies sound quality, volume, or exact animal imitation; all attempts are accepted.

## Selection Trigger

Start this activity when the child photographs an animal toy, animal picture, or asks for animal-sound play. If the photo is unclear, the AI can launch with common animals by voice only.

## Experience Pillar & Game Style

- **Pillar:** Performance
- **Game style:** `voice_stage`
- **Why this scaffold:** the child performs short animal sounds for a friendly audience and receives an encore-style payoff.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|
| animal_sound_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-2 | Help the child recognize the animal they are about to imitate. | prompt_en: Create a set of friendly animal picture cards for toddlers and preschoolers. Include common animals such as cat, dog, cow, duck, sheep, and lion. Use a plain bright background, simple expressive illustrations, one animal per card, no text, no scary poses. Source: new_ai_generated_asset. | Show one animal card each round while the AI invites the child to imitate its sound. | If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. | No real child photos, no attack or predation scenes, and friendly animal poses only. |

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

**Overall**: ALL PASS -- one reviewer issue found and fixed: Step 3 now uses hidden animal reveals and stable `animal_sound_cards_01` references.
