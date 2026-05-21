# Generated Asset Pilot Prompt - emotion_expression_cards_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_emotion_reader_care (concept_emotion_reader_care)
Mechanic: care
Asset: emotion_expression_cards_01 (card_set); requiredness=optional; timing=pre_generated
Runtime use: prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4
Display location: center_card_area
Purpose: Provide simple character expressions that children can interpret with evidence.

Source asset prompt:
Create a set of friendly illustrated character expression cards for children ages 4-7. Include happy, worried, proud, tired, surprised, and frustrated expressions. Use one character per card, clear face and body cue, plain background, no text, no stereotypes, and no real people.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: calm feeling-helper station, expressive character cards, peach and soft blue accents.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_emotion_reader_care`
- Asset: `emotion_expression_cards_01`
- Requiredness: `optional`
- Timing: `pre_generated`
- Use step: `prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4`
- Display location: `center_card_area`
- Fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face.
