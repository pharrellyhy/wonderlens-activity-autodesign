# Mechanism Storyboard Prompt - concept_color_famous_art_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Color In Famous Art" (concept_color_famous_art_probe); category=cat1; tier=T1; mechanic=enumerate; pillar=Discovery; style=field_experiment; focal=color_famous_art.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: The product can display a curated public-domain or licensed artwork with color metadata. The AI discusses...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Color Curator rule: name the first color that stands out in the artwo...
3. Child Action: The repeated mechanic is enumerate: Round 1 -- Find the loudest color | [round-1 guide] "Round 1: name the first c...
4. Feedback Loop: [specific] "Yellow is the loudest color you noticed." | [redirect] "Look again at the approved artwork card. Pick...
5. Variation: Round 2 -- Find repeated colors | [round-2 guide] "Round 2: point to or name where the color appears again." | Ide...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Function today. You used your own enumerate a...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: The product can display a curated public-domain or licensed artwork with color metadata. The AI discusses only visible colors and child-safe context, with no live museum lookup req... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Color Curator rule: name the first color that stands out in the artwork. I only save what... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is enumerate: Round 1 -- Find the loudest color | [round-1 guide] "Round 1: name the first color that stands out in the artwork." | Ideal: "Bright yellow." | Unexpected: Names invisible c... _(source: Round 1 -- Find the loudest color)_
- **4. Feedback Loop** - [specific] "Yellow is the loudest color you noticed." | [redirect] "Look again at the approved artwork card. Pick a color you can see." _(source: Round 1 -- Find the loudest color)_
- **5. Variation** - Round 2 -- Find repeated colors | [round-2 guide] "Round 2: point to or name where the color appears again." | Ideal: "Yellow on the hat and window." | Unexpected: Only says favorite color... _(source: Round 2 -- Find repeated colors)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Function today. You used your own enumerate action to make the result." | Ideal: "Again!" / names a favorite part. | Une... _(source: Step 5: Closing + IB Concepts)_
