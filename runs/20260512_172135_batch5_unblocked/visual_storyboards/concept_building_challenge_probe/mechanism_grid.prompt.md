# Mechanism Storyboard Prompt - concept_building_challenge_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Building Challenge" (concept_building_challenge_probe); category=cat3; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=building_challenge.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child has blocks, bricks, cups, or recycled materials within caregiver-approved reach. If materials are...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Build Planner rule: choose blocks or household materials and make a s...
3. Child Action: The repeated mechanic is build: Round 1 -- Choose the base | [round-1 guide] "Round 1: choose blocks or household...
4. Feedback Loop: [specific] "Two blocks can be the base. Slot one is saved." | [redirect] "Ask a grown-up for safe materials, or sw...
5. Variation: Round 2 -- Add a useful part | [round-2 guide] "Round 2: add one part that helps the build match the target." | Id...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build act...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child has blocks, bricks, cups, or recycled materials within caregiver-approved reach. If materials are missing, the AI pauses or turns the build into a verbal plan instead of pr... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Build Planner rule: choose blocks or household materials and make a stable base. I only s... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Choose the base | [round-1 guide] "Round 1: choose blocks or household materials and make a stable base." | Ideal: "I used two blocks." | Unexpected: No materials nea... _(source: Round 1 -- Choose the base)_
- **4. Feedback Loop** - [specific] "Two blocks can be the base. Slot one is saved." | [redirect] "Ask a grown-up for safe materials, or switch to a pretend build." _(source: Round 1 -- Choose the base)_
- **5. Variation** - Round 2 -- Add a useful part | [round-2 guide] "Round 2: add one part that helps the build match the target." | Ideal: "I made a roof." | Unexpected: Build falls over | No response: Child c... _(source: Round 2 -- Add a useful part)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build action to make the result." | Ideal: "Again!" / names a favorite part. | Unexp... _(source: Step 5: Closing + IB Concepts)_
