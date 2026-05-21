# Generated Asset Pilot Prompt - phoneme_letter_card_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_phoneme_hunt_collect (concept_phoneme_hunt_collect)
Mechanic: collect
Asset: phoneme_letter_card_01 (card_set); requiredness=optional; timing=pre_generated
Runtime use: prod.step_2; prod.step_3.round_1-3
Display location: center_card_area
Purpose: Give the child a visual reminder of the target sound and letter.

Source asset prompt:
Create a simple child-friendly phonics card for the /b/ sound. Show uppercase B and lowercase b in large rounded letters, include one small friendly picture of a ball and one banana, use a clean light background, no extra words, suitable for children ages 4-6.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: sunny phonics desk, rounded letter-card design, cheerful yellow and sky-blue accents.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_phoneme_hunt_collect`
- Asset: `phoneme_letter_card_01`
- Requiredness: `optional`
- Timing: `pre_generated`
- Use step: `prod.step_2; prod.step_3.round_1-3`
- Display location: `center_card_area`
- Fallback: If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter.
