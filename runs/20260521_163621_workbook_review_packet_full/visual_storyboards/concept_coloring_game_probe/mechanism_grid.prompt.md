# Mechanism Storyboard Prompt - concept_coloring_game_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Coloring Game" (concept_coloring_game_probe); category=cat5; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=coloring_game.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A simple line-art picture waits for colors gathered from the child environment.
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is build: Round 1 -- Choose A Region | Show a line-art region before asking for a real-world...
4. Feedback Loop: Ideal: [specific] Record the intended color and region. | Unexpected: [redirect] Validate the idea, restate the sa...
5. Variation: Round 2 -- Apply Or Describe The Color | Fill the region only if coloring UI exists; otherwise describe the intend...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A simple line-art picture waits for colors gathered from the child environment. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child confirms the rule or asks for a smaller version. | Unexpected:... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Choose A Region | Show a line-art region before asking for a real-world color source. | Ideal: The child provides a color source. | Unexpected: Child gives an unrelat... _(source: Round 1 -- Choose A Region)_
- **4. Feedback Loop** - Ideal: [specific] Record the intended color and region. | Unexpected: [redirect] Validate the idea, restate the safe rule, and offer one easier choice. | No response: [wait 2s] [gentle] Mod... _(source: Round 1 -- Choose A Region)_
- **5. Variation** - Round 2 -- Apply Or Describe The Color | Fill the region only if coloring UI exists; otherwise describe the intended fill. | Ideal: The child confirms or adjusts. | Unexpected: Child gives... _(source: Round 2 -- Apply Or Describe The Color)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child says again, names a favorite part, or quietly watches the recap. | Unexpe... _(source: Step 5: Closing + IB Concepts)_
