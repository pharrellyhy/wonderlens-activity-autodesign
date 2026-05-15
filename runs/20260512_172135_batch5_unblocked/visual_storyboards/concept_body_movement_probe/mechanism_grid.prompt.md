# Mechanism Storyboard Prompt - concept_body_movement_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Simple Body Movement Guide" (concept_body_movement_probe); category=cat1; tier=T0; mechanic=motion_voice; pillar=Performance; style=voice_stage; focal=body_movement.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent starts a short movement prompt and confirms enough space. The AI offers only low-risk hand, reac...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Rule: tiny safe moves only." | Ideal: Child confirms the role or star...
3. Child Action: The repeated mechanic is motion_voice: Round 1 -- Hello hands | [round-1 guide] "Small wave or hand stretch." | Id...
4. Feedback Loop: [specific] "Small wave is safe." | [redirect] "Running is outside this activity. Stay in one safe spot."
5. Variation: Round 2 -- Freeze statue | [round-2 guide] "Freeze and breathe." | Ideal: "Freeze." | Unexpected: Risky balance po...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "Form and Perspective badge." | Ideal: "Again!" / names a favorite pa...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent starts a short movement prompt and confirms enough space. The AI offers only low-risk hand, reach, and freeze prompts, accepts self-report, and keeps the stop button visib... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Rule: tiny safe moves only." | Ideal: Child confirms the role or starts round one. | Unexpected: Child needs materials, space, asset help, o...... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is motion_voice: Round 1 -- Hello hands | [round-1 guide] "Small wave or hand stretch." | Ideal: "Wave." | Unexpected: Starts running | No response: No response | [specific] "Small wave i... _(source: Round 1 -- Hello hands)_
- **4. Feedback Loop** - [specific] "Small wave is safe." | [redirect] "Running is outside this activity. Stay in one safe spot." _(source: Round 1 -- Hello hands)_
- **5. Variation** - Round 2 -- Freeze statue | [round-2 guide] "Freeze and breathe." | Ideal: "Freeze." | Unexpected: Risky balance pose | No response: Child sits | [specific] "Seated freeze counts. Breathe in... _(source: Round 2 -- Freeze statue)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "Form and Perspective badge." | Ideal: "Again!" / names a favorite part. | Unexpected: "That was hard." / wants another theme. | No response:...... _(source: Step 5: Closing + IB Concepts)_
