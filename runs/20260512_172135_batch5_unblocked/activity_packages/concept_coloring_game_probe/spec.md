# Coloring Game -- Authoring Spec

> CAT5 resolved capability-probe package . Mechanic: `build` . Product contract override: `minimum_unblock_allowed`

## Premise

Screen shows line art; the child chooses colors by taking photos and AI fills regions to create a shareable artwork. This fresh Batch 5 rerun treats the minimum unblock decisions as allowed, so the activity is fully designed while former constraints remain visible as resolved blocker annotations.

## Target

- **Primary tier:** T1
- **Activity category:** cat5
- **Mechanic:** `build`
- **Role title:** Palette Builder
- **Entity role:** catalyst
- **Progression axis:** change, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** Screen shows line art; the child chooses colors by taking photos and AI fills regions to create a shareable artwork.
- **Canonical mechanic:** `build`; the repeated Step 3 child action stays faithful to the source.
- **Readiness:** resolved from `blocked_until_product_decision` by `product_contract_override=minimum_unblock_allowed`.
- **Trigger condition:** Child photographs an object with a clear color or enters coloring mode.
- **Mapping use:** no entity mapping is required; the package avoids entity-specific factual claims.
- **Asset dependency:** runtime_generated. Asset `runtime_coloring_line_art_01` is normalized to the current asset contract and documented below.
- **Product capability flags:** requires_generated_image,requires_coloring_ui,requires_ui_state.
- **Scaffold fit:** Creation / `inventor_workshop` gives the child a role, escalating turns, and a payoff while preserving `build`.
- **Round shape:** Pick the coloring subject -> Fill the big region -> Add contrast and accent.

## Selection Trigger

Start when: Child photographs an object with a clear color or enters coloring mode. If setup is unavailable, use the documented fallback and do not claim asset display, generated images, material completion, motion verification, OCR, or state persistence beyond the resolved contract.

## Experience Pillar & Game Style

- **Pillar:** Creation
- **Game style:** `inventor_workshop`
- **Why this scaffold:** it creates an earned Step 4 reveal: a fillable line-art page colored with the child's photo palette.

## Resolved Product Contract Notes

- **Runtime image generation:** Approved minimum runtime-image policy: use the declared asset prompt, safety rules, latency cap, and no-image fallback instead of blocking the package.
- **Coloring or recoloring UI:** Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
- **UI state or progress memory:** Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

These are resolved contract items for this run, not package failures. They remain visible so implementation can see the minimum-to-unblock assumptions.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| runtime_coloring_line_art_01 | line_art | required | runtime_generated | prod.step_2; prod.step_3.round_1-3 | full_screen_canvas | Convert a photographed object into a fillable line drawing and apply colors chosen from the child's photos. | Generate a simple coloring-page line drawing based on the photographed object. Use clean black outlines, 3 to 5 large enclosed regions for coloring, no shading, no text, no background clutter, child-friendly proportions, and clear separation between regions. | Show the line art at runtime and fill a selected region after each child color photo. | Use a no-image color-plan fallback: the child names colors and regions verbally, and the screen shows text/color chips without claiming generated line art exists. | Do not generate real child portraits, copyrighted characters, or detailed dangerous objects. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| runtime_coloring_line_art_01 | line_art | required | runtime_generated | prod.step_2; prod.step_3.round_1-3 | full_screen_canvas | Convert a photographed object into a fillable line drawing and apply colors chosen from the child's photos. | future_runtime_image_generation | Show the line art at runtime and fill a selected region after each child color photo. Persist or hide behavior: keep visible only through prod.step_2; prod.step_3.round_1-3, then summarize or hide at Step 4 according to the payoff. | Use a no-image color-plan fallback: the child names colors and regions verbally, and the screen shows text/color chips without claiming generated line art exists. |

## Runtime Detail Floor Notes

- **Distinct round design:** Pick the coloring subject, Fill the big region, Add contrast and accent are distinct turns with different child actions and screen states.
- **Branch specificity:** Every round has ideal, unexpected, and no-response handling; physical, movement, text, asset, and state constraints use honest fallbacks.
- **Earned magic moment:** Step 4 reveals a fillable line-art page colored with the child's photo palette; it is not awarded before the child completes the turns.
- **Resolved blocker visibility:** Former blockers remain in `prod.md` as `RESOLVED BLOCKER` notes near affected beats.
- **Residual risk:** Static review verifies package contracts; actual runtime implementation and asset availability remain product concerns.

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `runtime_coloring_line_art_01`, `coloring_game`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `build` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the product-contract override rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | PASS because former blockers are resolved by the recorded product contract and remain visible as review callouts. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a concrete child role without a cold quiz. |
| 3 | Edge Case Coverage | PASS | Every step and round covers ideal, unexpected, and no-response branches with fallback or wait timing. |
| 4 | IB Completeness | PASS | Key Concepts Function, Change, KUD, ATL skills, recap, and dashboard agree with the child action. |
| 5 | Tier Appropriateness | PASS | Round count, prompt length, and caregiver/fallback language fit the declared tier. |
| 6 | Dialogue Specificity | PASS | AI lines and follow-ups are concept-specific and executable. |
| 7 | Screen & UI Completeness | PASS | Each step names visible state, progress, asset use, fallback, and payoff behavior. |
| 8 | Entity Mapping Alignment | N/A | Concept-led package with no mapping source and no entity-specific factual claims. |
| 9 | Game Feel | PASS | Progress slots and a specific Step 4 reveal make the payoff earned by the child action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3 preserves `build`; Creation/inventor_workshop frames the activity without changing the mechanic. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
