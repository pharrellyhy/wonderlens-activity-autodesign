# Asset Pipeline Smoke

## Basic Info

| Field | Value |
|---|---|
| Activity ID | smoke_asset_pipeline_collect |
| Activity Name | Asset Pipeline Smoke |
| Category | cat5 |
| Tier | T1 |
| Pillar | Discovery |
| Game Style | scavenger_hunt |
| Mechanic | collect |

## Adaptation Rationale

This package is a scoped feature-branch smoke test for `asset_build=generate_and_curate`. The child plays a tiny Cat5 collection loop: use the generated moss token as a guide, capture one real-world moss-like clue with the camera, then open a source-faithful Orion constellation reward card. The package is intentionally simple so WonderLens AI and the fullstack demo can import the same package and compare runtime YAML, asset paths, camera timing, and Cat5 collection behavior.

## Runtime Detail Floor Notes

- Step 1 introduces the mission and keeps the child role concrete: moss explorer.
- Step 2 previews the moss token and sets the real-world collection rule.
- Step 3 uses camera capture as the Cat5 collection action, with ideal, unexpected, and no-response branches plus a retry path.
- Step 4 opens the accurate Orion card only after the token is collected.
- Step 5 closes with a recap that references both assets without adding unsupported facts.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| moss_token | icon | required | pre_generated | prod.step_2; prod.step_3 | round_device_screen center | Show the guide token for the real-world collection. | Soft 3D educational toy illustration of a fuzzy moss patch token, no text. | Show before and during the camera collection beat; pulse once the real-world clue is accepted. | If missing, describe the moss token aloud and mark demo readiness degraded. |
| orion_card | card | required | pre_generated | prod.step_4 | round_device_screen center | Show an accurate Orion reward card. | NSF NOIRLab / IAU and Sky & Telescope Orion source image; preserve star-chart layout. | Reveal after the moss token is collected; do not alter the constellation layout. | If missing, do not claim the card is visible; use a voice-only reward. |

## Asset Usage Timeline

| Step | Asset | Loaded | Displayed | Hidden/Persisted | Child Action |
|---|---|---|---|---|---|
| Step 2 | moss_token | Before Step 2 | Center of round device screen | Persists into Step 3 | Child chooses one clue to hunt for. |
| Step 3 | moss_token | Already loaded | Beside captured real-world photo, then collected state | Persists as a small collected token | Child captures one real-world clue photo and names the match. |
| Step 4 | orion_card | Before reveal | Center of round device screen | Persists through reward beat | Child answers one simple Orion card clue. |

## Learning Design

- Key Concepts: Form, Connection
- Related Concepts: texture, pattern, evidence
- KUD:
  - Know: Moss can look soft, fuzzy, and green.
  - Understand: A collected clue can unlock a related reward.
  - Do: Capture one real-world clue, name the matching detail, and answer one simple visual clue.
- ATL skills: observing, describing, connecting

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the feature-branch asset pipeline smoke goal.

| # | Dimension | Score | Notes |
|---|---|---|---|
| 1 | V1 Technical Compliance | PASS | Uses static package-local assets, one ordinary camera capture, and speech/dialogue only; no unsupported before/after comparison or OCR. |
| 2 | Hook & Transition | PASS | Opens as a tiny explorer mission and bridges directly into a one-photo collection. |
| 3 | Edge Case Coverage | PASS | Every runtime beat has ideal, unexpected, and no-response handling with validating redirects and 2s wait timing. |
| 4 | IB Completeness | PASS | Concepts, related concepts, KUD, and ATL skills match the actual observe-and-collect task. |
| 5 | Tier Appropriateness | PASS | T1 language is short, concrete, and answerable with one detail. |
| 6 | Dialogue Specificity | PASS | Runtime lines are child-facing and branch-specific. |
| 7 | Screen & UI Completeness | PASS | Each step states what appears and what changes on screen. |
| 8 | Entity Mapping Alignment | N/A | Smoke package is concept-only and does not claim mapping-derived facts. |
| 9 | Game Feel | PASS | The moss token guides a real-world collection action and unlocks the Orion reward. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The child collects one real-world photo clue; the Orion card is honestly reference-bound. |
