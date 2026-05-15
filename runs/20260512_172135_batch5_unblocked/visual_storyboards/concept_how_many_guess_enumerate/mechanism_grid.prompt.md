# Mechanism Storyboard Prompt - concept_how_many_guess_enumerate

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Guess Then Count" (concept_how_many_guess_enumerate); category=cat1; tier=T1; mechanic=enumerate; pillar=Discovery; style=prediction_lab; focal=estimate_then_count.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A card shows seven shells. The child guesses first, then touches or counts each shell with the AI.
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Here is the rule: I give you one small challenge, you answer, and...
3. Child Action: The repeated mechanic is enumerate: Round 1 -- Make a Guess | [focused playful tone] "Do not count yet. How many d...
4. Feedback Loop: [curious] "Seven is your estimate. I am saving it before we count, so it stays a real guess." | [warm redirect] "T...
5. Variation: Round 2 -- Count Carefully | [focused playful tone] "Now count each object one by one. What number do we reach?" |...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Careful Counter badge. You used Form by noticin...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A card shows seven shells. The child guesses first, then touches or counts each shell with the AI. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Here is the rule: I give you one small challenge, you answer, and we save one progress to... | Ideal: "Okay." | Unexpected: "Can I do it my w... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is enumerate: Round 1 -- Make a Guess | [focused playful tone] "Do not count yet. How many do you think are here?" | Ideal: "seven." | Unexpected: "twenty." | No response: Child looks at... _(source: Round 1 -- Make a Guess)_
- **4. Feedback Loop** - [curious] "Seven is your estimate. I am saving it before we count, so it stays a real guess." | [warm redirect] "Twenty is a big guess. This card looks smaller, so pick a number near seven." _(source: Round 1 -- Make a Guess)_
- **5. Variation** - Round 2 -- Count Carefully | [focused playful tone] "Now count each object one by one. What number do we reach?" | Ideal: "seven." | Unexpected: "I lost track." | No response: Child looks a... _(source: Round 2 -- Count Carefully)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Careful Counter badge. You used Form by noticing the important part, and C... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
