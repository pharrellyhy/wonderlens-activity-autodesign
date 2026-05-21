# Mechanism Storyboard Prompt - concept_color_famous_art_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Color In Famous Art" (concept_color_famous_art_probe); category=cat1; tier=T1; mechanic=enumerate; pillar=Discovery; style=field_experiment; focal=color_famous_art.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: The child photographs a clear color or chooses one from a safe object, and the product can display a cura...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Color Curator rule: start with your color, then find artworks where t...
3. Child Action: The repeated mechanic is enumerate: Round 1 -- Capture the child color | [round-1 guide] "Round 1: show or name on...
4. Feedback Loop: Ideal: [specific] "Yellow is our color clue." | Unexpected: [redirect] "Choose a safe everyday color we can talk a...
5. Variation: Round 2 -- Match approved artworks | [round-2 guide] "Round 2: look at two approved artworks. Where do you see you...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Function today. You used your own enumerate a...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: The child photographs a clear color or chooses one from a safe object, and the product can display a curated public-domain or licensed artwork set with color metadata. The AI discu... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Color Curator rule: start with your color, then find artworks where that color is importa... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is enumerate: Round 1 -- Capture the child color | [round-1 guide] "Round 1: show or name one color from your object. That color will become our art-search clue... | Ideal: "Bright yellow... _(source: Round 1 -- Capture the child color)_
- **4. Feedback Loop** - Ideal: [specific] "Yellow is our color clue." | Unexpected: [redirect] "Choose a safe everyday color we can talk about without private details." | No response: [wait 2s] [gentle hint] "Poin... _(source: Round 1 -- Capture the child color)_
- **5. Variation** - Round 2 -- Match approved artworks | [round-2 guide] "Round 2: look at two approved artworks. Where do you see your yellow color showing strongly?" | Ideal: "This painting has yellow in the... _(source: Round 2 -- Match approved artworks)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Function today. You used your own enumerate action to make the result." | Ideal: "Again!" / names a favorite part. | Une... _(source: Step 5: Closing + IB Concepts)_
