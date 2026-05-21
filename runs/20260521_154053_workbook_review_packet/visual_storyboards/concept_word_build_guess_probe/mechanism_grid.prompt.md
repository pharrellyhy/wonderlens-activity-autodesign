# Mechanism Storyboard Prompt - concept_word_build_guess_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Word Build Guess" (concept_word_build_guess_probe); category=cat1; tier=T1; mechanic=decide; pillar=Adventure; style=time_traveler; focal=word_build_guess.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent selects a reading level and a safe target word such as plant, moon, or cake. The AI reveals clue...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Word Grower rule: choose between two clue paths for the hidden word....
3. Child Action: The repeated mechanic is decide: Round 1 -- Hear the clue | [round-1 guide] "Round 1: choose between two clue path...
4. Feedback Loop: Ideal: [specific] "Animal clue chosen. I will reveal one safe hint." | Unexpected: [redirect] "We keep reading lev...
5. Variation: Round 2 -- Grow the word | [round-2 guide] "Round 2: pick a letter sound or answer a clue to reveal part of the wo...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Perspective and Function today. You used your own deci...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent selects a reading level and a safe target word such as plant, moon, or cake. The AI reveals clue progress only inside the declared word-state contract and avoids hangman o... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Word Grower rule: choose between two clue paths for the hidden word. I only save what you... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is decide: Round 1 -- Hear the clue | [round-1 guide] "Round 1: choose between two clue paths for the hidden word." | Ideal: "Animal clue." | Unexpected: Wants hard spelling | No response... _(source: Round 1 -- Hear the clue)_
- **4. Feedback Loop** - Ideal: [specific] "Animal clue chosen. I will reveal one safe hint." | Unexpected: [redirect] "We keep reading level gentle. Choose sound clue or picture clue." | No response: [wait 2s] [ge... _(source: Round 1 -- Hear the clue)_
- **5. Variation** - Round 2 -- Grow the word | [round-2 guide] "Round 2: pick a letter sound or answer a clue to reveal part of the word." | Ideal: "/k/ sound." | Unexpected: Guesses random letters rapidly | N... _(source: Round 2 -- Grow the word)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Perspective and Function today. You used your own decide action to make the resul... | Ideal: "Again!" / names a favorite part. |... _(source: Step 5: Closing + IB Concepts)_
