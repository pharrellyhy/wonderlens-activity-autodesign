# Generated Asset Pilot Prompt - recognition_challenge_cards_01

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: concept_recognition_pop_probe (concept_recognition_pop_probe)
Mechanic: compare
Asset: recognition_challenge_cards_01 (target_card_set); requiredness=required; timing=pre_generated
Runtime use: prod.step_2; prod.step_3.round_1-3
Display location: center_card_area
Purpose: Provide target and distractor images for a tap-based recognition challenge.

Source asset prompt:
Create a set of simple recognition challenge cards for children. Include target and distractor objects with clear differences in shape, color, or category. Use one object per card, plain background, no text, no brands, and consistent friendly style.

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: recognition challenge board, target and distractor object cards, crisp teal and red accents.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards.
```

## Runtime Placement

- Activity: `concept_recognition_pop_probe`
- Asset: `recognition_challenge_cards_01`
- Requiredness: `required`
- Timing: `pre_generated`
- Use step: `prod.step_2; prod.step_3.round_1-3`
- Display location: `center_card_area`
- Fallback: If tap UI or state timing is unavailable, block at Phase 0 rather than converting to dialogue.
