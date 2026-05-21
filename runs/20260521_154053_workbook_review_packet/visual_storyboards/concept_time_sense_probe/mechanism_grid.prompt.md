# Mechanism Storyboard Prompt - concept_time_sense_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Time Sense Challenge" (concept_time_sense_probe); category=cat1; tier=T1; mechanic=predict; pillar=Discovery; style=field_experiment; focal=time_sense.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child can sit safely for a ten-second challenge. The AI gives a clear start signal, records the child's...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Time Guesser rule: predict when ten seconds have passed. I only save...
3. Child Action: The repeated mechanic is predict: Round 1 -- Make a short guess | [round-1 guide] "Round 1: predict when ten secon...
4. Feedback Loop: Ideal: [specific] "Good. Your guess is locked before the timer." | Unexpected: [redirect] "Let us keep it short: t...
5. Variation: Round 2 -- Check the result | [round-2 guide] "Round 2: compare the guess with the timer result." | Ideal: "I was...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Causation and Change today. You used your own predict...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child can sit safely for a ten-second challenge. The AI gives a clear start signal, records the child's stop guess, reveals the elapsed result, and keeps the second estimate low-... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Time Guesser rule: predict when ten seconds have passed. I only save what you choose, say... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is predict: Round 1 -- Make a short guess | [round-1 guide] "Round 1: predict when ten seconds have passed." | Ideal: "I will say stop." | Unexpected: Wants a long timer | No response: No... _(source: Round 1 -- Make a short guess)_
- **4. Feedback Loop** - Ideal: [specific] "Good. Your guess is locked before the timer." | Unexpected: [redirect] "Let us keep it short: ten seconds is safer for this game." | No response: [wait 2s] [gentle hint]... _(source: Round 1 -- Make a short guess)_
- **5. Variation** - Round 2 -- Check the result | [round-2 guide] "Round 2: compare the guess with the timer result." | Ideal: "I was early." | Unexpected: Argues the timer is wrong | No response: No response... _(source: Round 2 -- Check the result)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Causation and Change today. You used your own predict action to make the result." | Ideal: "Again!" / names a favorite part. | Un... _(source: Step 5: Closing + IB Concepts)_
