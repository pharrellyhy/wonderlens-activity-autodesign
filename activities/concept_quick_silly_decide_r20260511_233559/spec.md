# Quick Silly Choice Pop -- Authoring Spec

> CAT1 concept package . Concept source: `source_quick_silly_questions` . Mechanic: `decide`

## Premise

The child answers very short playful choice questions during a transition or warm-up. The activity turns that source promise into a cat1 runtime package where the child becomes the Silly Choice Sprinter. The repeated action is `decide`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T0
- **Activity category:** cat1
- **Mechanic:** `decide`
- **Entity role:** catalyst
- **Progression axis:** perspective, level 1

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child answers very short playful choice questions during a transition or warm-up.
- **Canonical mechanic:** `decide`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Light transition, waiting moment, or warm-up conversation.
- **Mapping use:** no required mapping for this package; parameterized placeholders avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** `quick_silly_countdown_01` is optional `ui_overlay` support; fallback behavior is documented.
- **Product capability flags:** requires_asset_display, requires_ui_state.
- **Scaffold fit:** acceptable. Adventure / `time_traveler` supplies the emotional payoff while `decide` remains the child-action contract.
- **Assumptions:** The repeated action is hear one prompt, decide quickly, and explain if the child wants.

## Selection Trigger

Start when Light transition, waiting moment, or warm-up conversation. If the required visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `time_traveler`
- **Why this scaffold:** The activity is fast and pressure-free. Optional countdown UI is decorative; voice-only works without claiming a timer.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Fast Favorite and Round 2 -- Fast Path each ask for a different child contribution and update a different progress token, keeping the T0 loop to two rounds.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The two silly choices become a tiny transition parade that ends the waiting moment.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| Field | Value |
|---|---|
| asset_id | quick_silly_countdown_01 |
| asset_type | ui_overlay |
| requiredness | optional |
| generation_timing | runtime_generated |
| use_step | prod.step_2; prod.step_3.round_1-2 |
| purpose | Optionally add a playful countdown or prompt card for quick silly questions. |
| prompt_en | Create a simple playful countdown overlay for children's quick questions. Use three large friendly countdown circles, bright but calm colors, no text except numerals 3, 2, 1, no brands, and enough blank space for a spoken prompt. |
| source | new_ai_generated_asset_or_runtime_ui |
| display_behavior | Show the countdown only if product supports short stateful prompt timing. |
| fallback_behavior | If countdown UI is unavailable, ask the quick questions by voice only and do not claim a timer is on screen. |
| safety_constraints | No pressure, no buzzer shame, no flashing effects, and no competitive scoring. |
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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `decide` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- reviewer-agent pass by Averroes after package-quality edits.
