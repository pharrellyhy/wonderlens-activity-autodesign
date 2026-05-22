# Mechanism Storyboard Prompt - concept_guided_drawing_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Guided Drawing" (concept_guided_drawing_probe); category=cat3; tier=T1; mechanic=build; pillar=Creation; style=inventor_workshop; focal=guided_drawing.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Child is indoors and photographs an object that could become a drawing theme.
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is build: Round 1 -- Start The Source Action | Preserve the workbook promise: The AI guides...
4. Feedback Loop: Ideal: Name what the child added, show how it changes the creation, and cue the next build step. | Unexpected: Kee...
5. Variation: Round 2 -- Repeat With A Variation | Keep the same source frame and ask for a second build turn with a small varia...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Child is indoors and photographs an object that could become a drawing theme. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child agrees to the making step loop for Guided Drawing or asks for... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is build: Round 1 -- Start The Source Action | Preserve the workbook promise: The AI guides the child to use paper and pencil to complete a simple drawing s... | Ideal: The child adds the... _(source: Round 1 -- Start The Source Action)_
- **4. Feedback Loop** - Ideal: Name what the child added, show how it changes the creation, and cue the next build step. | Unexpected: Keep the target small, restate the one required first line or shape step, and... _(source: Round 1 -- Start The Source Action)_
- **5. Variation** - Round 2 -- Repeat With A Variation | Keep the same source frame and ask for a second build turn with a small variation. | Ideal: The child adds the requested second guided detail piece, mar... _(source: Round 2 -- Repeat With A Variation)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child names a favorite Guided Drawing moment, asks to play again, or watches th... _(source: Step 5: Closing + IB Concepts)_
