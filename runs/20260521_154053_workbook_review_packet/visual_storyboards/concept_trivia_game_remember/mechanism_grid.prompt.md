# Mechanism Storyboard Prompt - concept_trivia_game_remember

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Tiny Trivia Trail" (concept_trivia_game_remember); category=cat1; tier=T1; mechanic=remember; pillar=Mystery; style=mystery_lens; focal=remembered_fact_clue.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: After learning about plants, the AI asks three tiny questions such as what leaves help plants do, then explains ge...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Here is the rule: I give you one small challenge, you answer, and...
3. Child Action: The repeated mechanic is remember: Round 1 -- Remember One Detail | [focused playful tone] "What did we learn leav...
4. Feedback Loop: Ideal: [warm recall tone] "Yes, leaves catch sunlight. I am saving that as clue one." | Unexpected: [gentle correc...
5. Variation: Round 2 -- Choose the Better Answer | [focused playful tone] "Which fits: roots drink water, or roots fly?" | Idea...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Trivia Trail Finder badge. You used Connection...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - After learning about plants, the AI asks three tiny questions such as what leaves help plants do, then explains gently. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Here is the rule: I give you one small challenge, you answer, and we save one progress to... | Ideal: "Okay." | Unexpected: "Can I do it my w... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is remember: Round 1 -- Remember One Detail | [focused playful tone] "What did we learn leaves help a plant do?" | Ideal: "catch sunlight." | Unexpected: "sleep." | No response: Child loo... _(source: Round 1 -- Remember One Detail)_
- **4. Feedback Loop** - Ideal: [warm recall tone] "Yes, leaves catch sunlight. I am saving that as clue one." | Unexpected: [gentle correction] "Sleep is a cozy idea. This clue is about sunlight, so leaves catch s... _(source: Round 1 -- Remember One Detail)_
- **5. Variation** - Round 2 -- Choose the Better Answer | [focused playful tone] "Which fits: roots drink water, or roots fly?" | Ideal: "drink water." | Unexpected: "fly." | No response: Child looks at the sc... _(source: Round 2 -- Choose the Better Answer)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Trivia Trail Finder badge. You used Connection by noticing the important p... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
