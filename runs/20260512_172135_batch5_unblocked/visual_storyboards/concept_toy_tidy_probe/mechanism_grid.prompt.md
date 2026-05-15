# Mechanism Storyboard Prompt - concept_toy_tidy_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Toy Tidy Challenge" (concept_toy_tidy_probe); category=cat5; tier=T1; mechanic=sort; pillar=Discovery; style=field_experiment; focal=toy_tidy.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent starts tidy mode near cars, blocks, soft toys, books, or household objects. The AI uses child/ca...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Tidy Sort Captain rule: pick one sorting rule such as soft things, wh...
3. Child Action: The repeated mechanic is sort: Round 1 -- Choose a tidy rule | [round-1 guide] "Round 1: pick one sorting rule suc...
4. Feedback Loop: [specific] "Cars together is a clear rule." | [redirect] "We can use any safe visible objects or pause tidy mode."
5. Variation: Round 2 -- Sort the first group | [round-2 guide] "Round 2: move or name the first group and explain the rule." |...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Connection today. You used your own sort acti...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent starts tidy mode near cars, blocks, soft toys, books, or household objects. The AI uses child/caregiver confirmation for progress and does not claim full-room before/after... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Tidy Sort Captain rule: pick one sorting rule such as soft things, wheels, or blocks. I o... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is sort: Round 1 -- Choose a tidy rule | [round-1 guide] "Round 1: pick one sorting rule such as soft things, wheels, or blocks." | Ideal: "Cars go together." | Unexpected: No toys nearby... _(source: Round 1 -- Choose a tidy rule)_
- **4. Feedback Loop** - [specific] "Cars together is a clear rule." | [redirect] "We can use any safe visible objects or pause tidy mode." _(source: Round 1 -- Choose a tidy rule)_
- **5. Variation** - Round 2 -- Sort the first group | [round-2 guide] "Round 2: move or name the first group and explain the rule." | Ideal: "Cars in the basket." | Unexpected: Child mixes blocks and cars | No... _(source: Round 2 -- Sort the first group)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Connection today. You used your own sort action to make the result." | Ideal: "Again!" / names a favorite part. | Unexpe... _(source: Step 5: Closing + IB Concepts)_
