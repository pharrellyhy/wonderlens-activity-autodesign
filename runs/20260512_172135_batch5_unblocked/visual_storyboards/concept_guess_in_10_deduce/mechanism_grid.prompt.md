# Mechanism Storyboard Prompt - concept_guess_in_10_deduce

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Guess in 10" (concept_guess_in_10_deduce); category=cat1; tier=T1; mechanic=deduce; pillar=Mystery; style=mystery_lens; focal=clue_evidence.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Child enters guessing mode; the AI secretly chooses "duck" and gives clues about water, a beak, and waddling. The...
2. Prompt: Step 2: Rule Introduction -- Clue Detective | [clear guide tone] "You are the Clue Detective. I give a clue. You m...
3. Child Action: The repeated mechanic is deduce: Round 1 -- Function Clue | [secret clue tone] "Clue one: this mystery thing can m...
4. Feedback Loop: [intrigued] "Good evidence guess. It could move in water. Let's collect another clue." | [kind redirect] "Good thi...
5. Variation: Round 2 -- Form Clue | [careful clue tone] "Clue two: it has a beak. Now what is your best guess?" | Ideal: "Duck!...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You did it, Clue Detective. You used Function. You thought abo...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Child enters guessing mode; the AI secretly chooses "duck" and gives clues about water, a beak, and waddling. The child may guess fish first, then revise when the beak clue appears, and the... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction -- Clue Detective | [clear guide tone] "You are the Clue Detective. I give a clue. You make a guess. New clues make the mystery e... | Ideal: "Okay!" / "I can gues... _(source: Step 2: Rule Introduction -- Clue Detective)_
- **3. Child Action** - The repeated mechanic is deduce: Round 1 -- Function Clue | [secret clue tone] "Clue one: this mystery thing can move in water. What could it be?" | Ideal: "Duck!" / "Fish!" / "Boat!" | Unexpected: "Car." / "I... _(source: Round 1 -- Function Clue)_
- **4. Feedback Loop** - [intrigued] "Good evidence guess. It could move in water. Let's collect another clue." | [kind redirect] "Good thinking. Mystery clues can feel tricky. This one likes water. Try animal or b... _(source: Round 1 -- Function Clue)_
- **5. Variation** - Round 2 -- Form Clue | [careful clue tone] "Clue two: it has a beak. Now what is your best guess?" | Ideal: "Duck!" / "Bird!" | Unexpected: "Dog." / "A spoon." | No response: Child looks un... _(source: Round 2 -- Form Clue)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You did it, Clue Detective. You used Function. You thought about what it does. You used F... | Ideal: "Another mystery!" / "I solved it!"... _(source: Step 5: Closing + IB Concepts)_
