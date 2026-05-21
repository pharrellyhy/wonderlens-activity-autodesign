# Generated Asset Pilot Prompt - partial_reveal_cards_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_partial_reveal_deduce (concept_partial_reveal_deduce)
Mechanic: deduce
Asset: partial_reveal_cards_01 (card_set); requiredness=required; timing=pre_generated
Runtime use: prod.step_2; prod.step_3.round_1-3
Display location: center_card_area
Purpose: Provide visible partial evidence so the child can infer the whole animal or object.

Source asset prompt:
Create a set of partial-reveal animal guessing cards for children ages 4-6. Each card should show only one distinctive part of a common animal, such as a tiger tail, rabbit ears, elephant trunk, duck feet, or fish scales. Use a consistent soft illustration style, plain light background, no text, no scary details, and keep the cropped part large and easy to inspect.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: soft mystery clue table, cropped animal detail cards, lavender and teal accents.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_partial_reveal_deduce`
- Asset: `partial_reveal_cards_01`
- Requiredness: `required`
- Timing: `pre_generated`
- Use step: `prod.step_2; prod.step_3.round_1-3`
- Display location: `center_card_area`
- Fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.
