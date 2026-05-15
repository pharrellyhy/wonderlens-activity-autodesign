# Mechanism Storyboard Prompt - concept_emotion_color_outfit_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Emotion Color Outfit" (concept_emotion_color_outfit_probe); category=cat1; tier=T1; mechanic=care; pillar=Nurture; style=care_station; focal=emotion_color_outfit.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child names a mood or points to a color. The AI asks for a visible cue, treats color meanings as person...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Feeling Stylist rule: use the character card or my voice cue, then sa...
3. Child Action: The repeated mechanic is care: Round 1 -- Notice the feeling cue | [round-1 guide] "Round 1: use the character cue...
4. Feedback Loop: [specific] "Might be worried is careful language. The shoulder clue helps." | [redirect] "Blue can come later. Fir...
5. Variation: Round 2 -- Choose a comfort color | [round-2 guide] "Round 2: choose a color that could help the character feel su...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your ow...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child names a mood or points to a color. The AI asks for a visible cue, treats color meanings as personal, and displays recoloring only when the approved character template and U... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Feeling Stylist rule: use the character card or my voice cue, then say what they might fe... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is care: Round 1 -- Notice the feeling cue | [round-1 guide] "Round 1: use the character cue and say what they might feel." | Ideal: "Maybe worried, shoulders are small." | Unexpected: "B... _(source: Round 1 -- Notice the feeling cue)_
- **4. Feedback Loop** - [specific] "Might be worried is careful language. The shoulder clue helps." | [redirect] "Blue can come later. First name what the character might feel." _(source: Round 1 -- Notice the feeling cue)_
- **5. Variation** - Round 2 -- Choose a comfort color | [round-2 guide] "Round 2: choose a color that could help the character feel supported." | Ideal: "Soft yellow because it feels warm." | Unexpected: Says... _(source: Round 2 -- Choose a comfort color)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your own care action to make the r... | Ideal: "Again!" / names a favorite part. |... _(source: Step 5: Closing + IB Concepts)_
