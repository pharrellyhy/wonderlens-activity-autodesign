# Generated Asset Pilot Prompt - animal_sound_cards_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_animal_sound_motion_voice (concept_animal_sound_motion_voice)
Mechanic: motion_voice
Asset: animal_sound_cards_01 (card_set); requiredness=optional; timing=pre_generated
Runtime use: prod.step_2; prod.step_3.round_1-2
Display location: center_card_area
Purpose: Help the child recognize the animal they are about to imitate.

Source asset prompt:
Create a set of friendly animal picture cards for toddlers and preschoolers. Include common animals such as cat, dog, cow, duck, sheep, and lion. Use a plain bright background, simple expressive illustrations, one animal per card, no text, no scary poses.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: tiny pretend stage, friendly animal cards, coral and mint accents.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_animal_sound_motion_voice`
- Asset: `animal_sound_cards_01`
- Requiredness: `optional`
- Timing: `pre_generated`
- Use step: `prod.step_2; prod.step_3.round_1-2`
- Display location: `center_card_area`
- Fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture.
