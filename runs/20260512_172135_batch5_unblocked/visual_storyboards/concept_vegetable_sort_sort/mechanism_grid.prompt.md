# Mechanism Storyboard Prompt - concept_vegetable_sort_sort

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Vegetable Sort Stand" (concept_vegetable_sort_sort); category=cat1; tier=T1; mechanic=sort; pillar=Adventure; style=quest_collector; focal=vegetable_sort_rule.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: The screen shows carrot, broccoli, tomato, and potato cards. The child sorts by color first, then by plant part or...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Sorter rule: choose the grouping rule, use it on the cards, then n...
3. Child Action: The repeated mechanic is sort: Round 1 -- Pick a Rule | [focused playful tone] "Choose the stand rule: color, shap...
4. Feedback Loop: [specific praise] "That is a clear sorting rule. Token 1 is saved." | [warm redirect] "Yummy is an opinion rule. P...
5. Variation: Round 2 -- Place Two Vegetables | [sorting tone] "Use your rule on carrot and tomato. If your rule is color, where...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Veggie Sorter badge. You used Connection by gro...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - The screen shows carrot, broccoli, tomato, and potato cards. The child sorts by color first, then by plant part or cooking use. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Sorter rule: choose the grouping rule, use it on the cards, then name one group." | Ideal: "Okay." | Unexpected: "Can I do it my way?" | No r... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is sort: Round 1 -- Pick a Rule | [focused playful tone] "Choose the stand rule: color, shape, or part we eat. Which rule should run this round... | Ideal: "color" / "shape" / "part we ea... _(source: Round 1 -- Pick a Rule)_
- **4. Feedback Loop** - [specific praise] "That is a clear sorting rule. Token 1 is saved." | [warm redirect] "Yummy is an opinion rule. Pick a rule the cards can show: color, shape, or part we eat." _(source: Round 1 -- Pick a Rule)_
- **5. Variation** - Round 2 -- Place Two Vegetables | [sorting tone] "Use your rule on carrot and tomato. If your rule is color, where do they go? If it is part we... | Ideal: "orange and red groups" / "roots... _(source: Round 2 -- Place Two Vegetables)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Veggie Sorter badge. You used Connection by grouping foods by one rule, an... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
