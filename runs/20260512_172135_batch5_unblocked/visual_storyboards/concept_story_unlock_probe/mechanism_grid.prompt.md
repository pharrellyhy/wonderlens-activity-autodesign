# Mechanism Storyboard Prompt - concept_story_unlock_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Story Challenge Unlock" (concept_story_unlock_probe); category=cat1; tier=T1; mechanic=imagine; pillar=Adventure; style=time_traveler; focal=story_unlock.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child is in a story mode and reaches a door, bridge, or path marker. The AI uses the child's spoken ide...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Story Key Maker rule: choose which path the character tries. I only s...
3. Child Action: The repeated mechanic is imagine: Round 1 -- Pick the story door | [round-1 guide] "Round 1: choose which path the...
4. Feedback Loop: [specific] "Moon door chosen. It glows because you picked it." | [redirect] "Let us keep it safe and playful: moon...
5. Variation: Round 2 -- Make the unlock action | [round-2 guide] "Round 2: say a magic word, gesture, or tiny answer to help th...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Perspective and Connection today. You used your own im...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child is in a story mode and reaches a door, bridge, or path marker. The AI uses the child's spoken idea as the unlock evidence and avoids claiming persistent UI state when the f... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Story Key Maker rule: choose which path the character tries. I only save what you choose,... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is imagine: Round 1 -- Pick the story door | [round-1 guide] "Round 1: choose which path the character tries." | Ideal: "The moon door." | Unexpected: "Both doors explode." | No response:... _(source: Round 1 -- Pick the story door)_
- **4. Feedback Loop** - [specific] "Moon door chosen. It glows because you picked it." | [redirect] "Let us keep it safe and playful: moon door or forest door." _(source: Round 1 -- Pick the story door)_
- **5. Variation** - Round 2 -- Make the unlock action | [round-2 guide] "Round 2: say a magic word, gesture, or tiny answer to help the character." | Ideal: "Shine, moon!" | Unexpected: Child gives unrelated n... _(source: Round 2 -- Make the unlock action)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Perspective and Connection today. You used your own imagine action to make the re... | Ideal: "Again!" / names a favorite part. |... _(source: Step 5: Closing + IB Concepts)_
