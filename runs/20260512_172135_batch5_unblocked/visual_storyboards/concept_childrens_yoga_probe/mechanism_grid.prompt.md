# Mechanism Storyboard Prompt - concept_childrens_yoga_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Children's Yoga" (concept_childrens_yoga_probe); category=cat1; tier=T0; mechanic=motion_voice; pillar=Performance; style=voice_stage; focal=childrens_yoga.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent selects a calm routine and confirms enough space. The AI uses stable two-feet poses, breath cues...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Rule: stable gentle poses." | Ideal: Child confirms the role or start...
3. Child Action: The repeated mechanic is motion_voice: Round 1 -- Tree reach | [round-1 guide] "Tree reach. Feet down." | Ideal: "...
4. Feedback Loop: [specific] "Two feet stay safe." | [redirect] "Keep both feet down. We are doing child-safe tree."
5. Variation: Round 2 -- Butterfly rest | [round-2 guide] "Gentle butterfly rest." | Ideal: "Butterfly." | Unexpected: Extreme s...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "Form and Perspective badge." | Ideal: "Again!" / names a favorite pa...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent selects a calm routine and confirms enough space. The AI uses stable two-feet poses, breath cues, and a stop option, with pose cards shown only when the approved card set... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Rule: stable gentle poses." | Ideal: Child confirms the role or starts round one. | Unexpected: Child needs materials, space, asset help, o... |... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is motion_voice: Round 1 -- Tree reach | [round-1 guide] "Tree reach. Feet down." | Ideal: "Tree." / reaches arms | Unexpected: Tries one-foot balance | No response: No response | [specif... _(source: Round 1 -- Tree reach)_
- **4. Feedback Loop** - [specific] "Two feet stay safe." | [redirect] "Keep both feet down. We are doing child-safe tree." _(source: Round 1 -- Tree reach)_
- **5. Variation** - Round 2 -- Butterfly rest | [round-2 guide] "Gentle butterfly rest." | Ideal: "Butterfly." | Unexpected: Extreme stretch | No response: Child lies down tired | [specific] "Gentle butterfly... _(source: Round 2 -- Butterfly rest)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "Form and Perspective badge." | Ideal: "Again!" / names a favorite part. | Unexpected: "That was hard." / wants another theme. | No response:...... _(source: Step 5: Closing + IB Concepts)_
