# Mechanism Storyboard Prompt - concept_recognition_pop_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Recognition Pop Challenge" (concept_recognition_pop_probe); category=cat1; tier=T1; mechanic=compare; pillar=Discovery; style=field_experiment; focal=recognition_pop.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: The product can show a target card with simple distractors. The AI gives tap, point, or spoken-choice opt...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Target Matcher rule: choose the picture that matches the spoken targe...
3. Child Action: The repeated mechanic is compare: Round 1 -- Find the target | [round-1 guide] "Round 1: choose the picture that m...
4. Feedback Loop: [specific] "Apple matches the target. Slot one pops." | [redirect] "Close. Banana is food too, but the target is a...
5. Variation: Round 2 -- Avoid the distractor | [round-2 guide] "Round 2: explain why a similar picture is not the target." | Id...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Perspective today. You used your own compare...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: The product can show a target card with simple distractors. The AI gives tap, point, or spoken-choice options and slows the game down if timing support is unavailable. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Target Matcher rule: choose the picture that matches the spoken target. I only save what... | Ideal: Child confirms the role or starts round one... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is compare: Round 1 -- Find the target | [round-1 guide] "Round 1: choose the picture that matches the spoken target." | Ideal: "I tapped the apple." | Unexpected: Taps a distractor | No... _(source: Round 1 -- Find the target)_
- **4. Feedback Loop** - [specific] "Apple matches the target. Slot one pops." | [redirect] "Close. Banana is food too, but the target is apple." _(source: Round 1 -- Find the target)_
- **5. Variation** - Round 2 -- Avoid the distractor | [round-2 guide] "Round 2: explain why a similar picture is not the target." | Ideal: "Pear is not apple; different shape." | Unexpected: Says all fruits co... _(source: Round 2 -- Avoid the distractor)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Perspective today. You used your own compare action to make the result." | Ideal: "Again!" / names a favorite part. | Un... _(source: Step 5: Closing + IB Concepts)_
