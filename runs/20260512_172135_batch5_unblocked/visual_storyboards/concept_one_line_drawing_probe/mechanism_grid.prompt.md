# Mechanism Storyboard Prompt - concept_one_line_drawing_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "One-Line Drawing Challenge" (concept_one_line_drawing_probe); category=cat3; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=one_line_drawing.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child has paper or a drawing surface ready. The AI shows or describes one approved target, accepts self...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Line Path Explorer rule: plan the continuous path before drawing. I o...
3. Child Action: The repeated mechanic is build: Round 1 -- Trace the path in the air | [round-1 guide] "Round 1: plan the continuo...
4. Feedback Loop: [specific] "Starting at the roof gives your line a path." | [redirect] "Many lines are another drawing game. This...
5. Variation: Round 2 -- Draw without lifting | [round-2 guide] "Round 2: attempt the one-line target on paper or screen." | Ide...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build act...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child has paper or a drawing surface ready. The AI shows or describes one approved target, accepts self-report if the pencil lifts, and uses start/turn/end language instead of im... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Line Path Explorer rule: plan the continuous path before drawing. I only save what you ch... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Trace the path in the air | [round-1 guide] "Round 1: plan the continuous path before drawing." | Ideal: "Start at the roof." | Unexpected: Child wants many separate... _(source: Round 1 -- Trace the path in the air)_
- **4. Feedback Loop** - [specific] "Starting at the roof gives your line a path." | [redirect] "Many lines are another drawing game. This one uses one long path." _(source: Round 1 -- Trace the path in the air)_
- **5. Variation** - Round 2 -- Draw without lifting | [round-2 guide] "Round 2: attempt the one-line target on paper or screen." | Ideal: "I did it." | Unexpected: Lifts pencil halfway | No response: Child sel... _(source: Round 2 -- Draw without lifting)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Function and Change today. You used your own build action to make the result." | Ideal: "Again!" / names a favorite part. | Unexp... _(source: Step 5: Closing + IB Concepts)_
