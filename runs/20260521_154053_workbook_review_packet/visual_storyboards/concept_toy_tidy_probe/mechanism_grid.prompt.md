# Mechanism Storyboard Prompt - concept_toy_tidy_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Toy Tidy Challenge" (concept_toy_tidy_probe); category=cat5; tier=T1; mechanic=sort; pillar=Discovery; style=field_experiment; focal=toy_tidy.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent starts tidy mode near visible toys or a toy area. The AI uses child/caregiver confirmation for p...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Tidy Sort Captain rule: choose one toy group, tidy while I give simpl...
3. Child Action: The repeated mechanic is sort: Round 1 -- Start The Tidy Mission | [round-1 guide] "Round 1: look at the toy area...
4. Feedback Loop: Ideal: [specific] "Cars is a clear first group. Timer token 1 is ready." | Unexpected: [redirect] "We can use any...
5. Variation: Round 2 -- Tidy During The Timer | [round-2 guide] "Round 2: start moving that group to its home. I will give two...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Connection today. You used your own sort acti...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent starts tidy mode near visible toys or a toy area. The AI uses child/caregiver confirmation for progress and does not claim full-room before/after verification. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Tidy Sort Captain rule: choose one toy group, tidy while I give simple tips, then tell me... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is sort: Round 1 -- Start The Tidy Mission | [round-1 guide] "Round 1: look at the toy area and pick one small group to tidy first: cars, blocks, soft toy... | Ideal: "Cars." / "Blocks."... _(source: Round 1 -- Start The Tidy Mission)_
- **4. Feedback Loop** - Ideal: [specific] "Cars is a clear first group. Timer token 1 is ready." | Unexpected: [redirect] "We can use any safe visible objects or pause tidy mode." | No response: [wait 2s] [gentle... _(source: Round 1 -- Start The Tidy Mission)_
- **5. Variation** - Round 2 -- Tidy During The Timer | [round-2 guide] "Round 2: start moving that group to its home. I will give two tiny tips while you work: put... | Ideal: Child moves toys or says "Cars in... _(source: Round 2 -- Tidy During The Timer)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Connection today. You used your own sort action to make the result." | Ideal: "Again!" / names a favorite part. | Unexpe... _(source: Step 5: Closing + IB Concepts)_
