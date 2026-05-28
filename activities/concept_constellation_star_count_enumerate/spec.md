# Constellation Number Reveal -- Authoring Spec

> CAT1 concept package . Concept source: `source_constellation_star_count` . Mechanic: `enumerate`

## Premise

The child chooses between two possible star-count numbers. The device then reveals a real approved constellation card whose metadata matches the selected number and gives a short child-safe background introduction. The activity turns that source promise into a cat1 runtime package where the child becomes the Constellation Number Scout. The repeated action is `enumerate` through number choice and number-to-card matching, not through counting an arbitrary visible image from scratch.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `enumerate`
- **Entity role:** reference
- **Progression axis:** form, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child chooses a star-count number, sees a real approved constellation matching that number, and hears a short background introduction.
- **Canonical mechanic:** `enumerate`; Step 3's repeated child action preserves number sense by choosing, confirming, and recalling the selected count.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Child chooses a space theme or the screen can show an approved constellation card.
- **Mapping use:** no required mapping for this package; all constellation facts must come from approved asset metadata.
- **Asset dependency:** `constellation_count_cards_01` is required card_set support. Each card needs a real constellation name, visible guide-star count, and child-safe fact.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** acceptable. Discovery / `field_experiment` supplies the reveal payoff while `enumerate` remains the child-action contract.
- **Source intent lock:** Preserve this order: present two count choices, child chooses one, reveal a real approved constellation associated with that count, show the name label when available, then share a simple background fact. Do not reduce the activity to asking the child to count stars already shown, and do not present fictional star patterns as real constellations.

## Selection Trigger

Start when the child chooses a space theme or the screen can show approved real constellation cards. If approved card metadata is unavailable, use the fallback behavior from the Asset Brief or keep the interaction blocked rather than substituting a fictional counting card.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** The activity makes a number choice feel like a small field reveal: the chosen count opens a named real constellation card with one background clue.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 asks the child to choose between two counts, Round 2 reveals the matching constellation card, and Round 3 asks the child to recall either the constellation name or one background clue.
- **Branch specificity:** Unexpected answers are validated, then redirected to choosing one of the offered numbers or noticing the approved card metadata.
- **Earned magic moment:** The chosen number opens a named constellation card, showing that a number can connect to a real sky pattern and story clue.
- **Residual risk:** The package depends on approved real constellation metadata. If runtime only has arbitrary generated star pictures, the source promise is not satisfied.

## Asset Brief

| Field | Value |
|---|---|
| asset_id | constellation_count_cards_01 |
| asset_type | card_set |
| requiredness | required |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3; prod.step_4 |
| purpose | Provide approved real constellation cards keyed by visible guide-star count, with a name label and child-safe background fact. |
| prompt_en | Curate or redraw child-friendly real constellation cards from verified star-chart data. Each card includes one common constellation, visible key stars, thin connecting guide lines, optional name label, star_count metadata, and one short child-safe background fact. Preserve the approved star layout; do not invent fictional constellations. |
| source | approved_constellation_reference_set_or_verified_star_chart_redraw |
| display_behavior | After the child chooses a count, show one approved real constellation card whose metadata matches that selected number. If multiple cards share the count, choose one at random. |
| fallback_behavior | If approved real constellation cards or metadata are unavailable, do not run a direct star-counting image game. Use a voice-only number-to-constellation reveal without claiming a card is visible, or keep the assignment blocked until approved assets exist. |
| safety_constraints | No unsupported astronomy facts, no arbitrary AI-invented constellation layouts, no scary space imagery, and no dense star fields that make the guide-star count unclear. |

## Asset Usage Timeline

| asset_id | generation_timing | load/generate moment | first display step | visible range | display location | interaction/use | persistence/hide behavior | fallback |
|---|---|---|---|---|---|---|---|---|
| constellation_count_cards_01 | pre_generated | before Step 2 | Step 3 Round 2 | Step 3 Round 2 through Step 5 | round device screen | reveal the card matching the child's selected count and read approved metadata | keep selected card visible through the recap badge, then save only the session summary | use voice-only number-to-constellation reveal without claiming a visible card, or block until assets exist |

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or live astronomy verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a number-reveal role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T1 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify number choices, card reveal, metadata use, and fallback behavior. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source; all constellation claims are gated by asset metadata. |
| 9 | Game Feel | PASS | The loop has a number choice, a reveal, a background clue, and a payoff earned from the child's selected count. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `enumerate` while restoring the original number-choice reveal sequence. |

**Overall**: ALL PASS after source-intent repair for the constellation count-choice reveal flow.
