# Generated Asset Pilot Prompt - guided_drawing_step_cards_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_guided_drawing_probe (concept_guided_drawing_probe)
Mechanic: build
Asset: guided_drawing_step_cards_01 (card_set); requiredness=optional; timing=pre_generated
Runtime use: prod.step_2; prod.step_3.round_1-3
Display location: center_card_area
Purpose: Provide optional visual steps for a simple drawing task.

Source asset prompt:
Create a set of step-by-step drawing cards for children ages 4-6. Show how to draw a simple friendly object in 4 clear steps using thick black sketch lines, large shapes, no text, minimal details, and a plain white background.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: simple sketch workshop, drawing-step cards, black line art with pastel tabs.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_guided_drawing_probe`
- Asset: `guided_drawing_step_cards_01`
- Requiredness: `optional`
- Timing: `pre_generated`
- Use step: `prod.step_2; prod.step_3.round_1-3`
- Display location: `center_card_area`
- Fallback: If step cards are unavailable, use voice-only step descriptions with caregiver setup, self-report completion, and no drawing-quality assessment.
