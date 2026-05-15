# Mechanism Storyboard Prompt - concept_guided_drawing_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Guided Drawing" (concept_guided_drawing_probe); category=cat3; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=guided_drawing.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child has paper and pencil ready and chooses a simple object as the drawing theme. The AI paces each ma...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Step Sketch Coach rule: draw the largest simple shape from the card o...
3. Child Action: The repeated mechanic is build: Round 1 -- Draw the big shape | [round-1 guide] "Round 1: draw the largest simple...
4. Feedback Loop: [specific] "A big circle body is enough for step one." | [redirect] "Messy counts. We care about trying the shape,...
5. Variation: Round 2 -- Add one useful detail | [round-2 guide] "Round 2: add one detail that makes the drawing recognizable."...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build act...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child has paper and pencil ready and chooses a simple object as the drawing theme. The AI paces each mark, accepts caregiver/self-report evidence, and falls back to voice-only st... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Step Sketch Coach rule: draw the largest simple shape from the card or my voice clue. I o... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Draw the big shape | [round-1 guide] "Round 1: draw the largest simple shape from the card or voice clue." | Ideal: "I drew a circle body." | Unexpected: "Mine is mes... _(source: Round 1 -- Draw the big shape)_
- **4. Feedback Loop** - [specific] "A big circle body is enough for step one." | [redirect] "Messy counts. We care about trying the shape, not perfect copying." _(source: Round 1 -- Draw the big shape)_
- **5. Variation** - Round 2 -- Add one useful detail | [round-2 guide] "Round 2: add one detail that makes the drawing recognizable." | Ideal: "I added ears." | Unexpected: Child cannot find pencil/material |... _(source: Round 2 -- Add one useful detail)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build action to make the result." | Ideal: "Again!" / names a favorite part. | Unexp... _(source: Step 5: Closing + IB Concepts)_
