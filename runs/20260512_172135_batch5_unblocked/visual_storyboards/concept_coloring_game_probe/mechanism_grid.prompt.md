# Mechanism Storyboard Prompt - concept_coloring_game_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Coloring Game" (concept_coloring_game_probe); category=cat5; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=coloring_game.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child photographs a toy car or flower, selects a big region, then adds a contrast color and accent. If...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Palette Builder rule: choose the photographed object for the line-art...
3. Child Action: The repeated mechanic is build: Round 1 -- Pick the coloring subject | [round-1 guide] "Round 1: choose the photog...
4. Feedback Loop: [specific] "Good choice. I will turn that object into simple regions." | [redirect] "We can only use safe, origina...
5. Variation: Round 2 -- Fill the big region | [round-2 guide] "Round 2: photograph or choose a real-world color for the biggest...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build act...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child photographs a toy car or flower, selects a big region, then adds a contrast color and accent. If generated line art or fillable regions are unavailable, the session display... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Palette Builder rule: choose the photographed object for the line-art page. I only save w... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Pick the coloring subject | [round-1 guide] "Round 1: choose the photographed object for the line-art page." | Ideal: "My toy car." / "This flower." | Unexpected: "Ma... _(source: Round 1 -- Pick the coloring subject)_
- **4. Feedback Loop** - [specific] "Good choice. I will turn that object into simple regions." | [redirect] "We can only use safe, original objects. Pick this photo or another everyday object." _(source: Round 1 -- Pick the coloring subject)_
- **5. Variation** - Round 2 -- Fill the big region | [round-2 guide] "Round 2: photograph or choose a real-world color for the biggest region." | Ideal: "Red from my cup." | Unexpected: Chooses two colors at o... _(source: Round 2 -- Fill the big region)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build action to make the result." | Ideal: "Again!" / names a favorite part. | Unexp... _(source: Step 5: Closing + IB Concepts)_
