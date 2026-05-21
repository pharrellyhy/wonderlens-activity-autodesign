# Mechanism Storyboard Prompt - concept_would_you_rather_compare

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Would You Rather" (concept_would_you_rather_compare); category=cat1; tier=T1; mechanic=compare; pillar=Mystery; style=mystery_lens; focal=would_you_rather.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Conversation break, story reflection, or choice-making activity.
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is compare: Round 1 -- Start The Source Action | Preserve the workbook promise: The child ch...
4. Feedback Loop: Ideal: [specific] Confirm the action and name how it matches the source rule. | Unexpected: [redirect] Validate th...
5. Variation: Round 2 -- Repeat With A Variation | Keep the same source frame and ask for a second compare turn with a small var...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Conversation break, story reflection, or choice-making activity. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child confirms the rule or asks for a smaller version. | Unexpected:... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is compare: Round 1 -- Start The Source Action | Preserve the workbook promise: The child chooses between two playful options and explains the preference or t... | Ideal: The child gives... _(source: Round 1 -- Start The Source Action)_
- **4. Feedback Loop** - Ideal: [specific] Confirm the action and name how it matches the source rule. | Unexpected: [redirect] Validate the idea, restate the safe rule, and offer one easier choice. | No response:... _(source: Round 1 -- Start The Source Action)_
- **5. Variation** - Round 2 -- Repeat With A Variation | Keep the same source frame and ask for a second compare turn with a small variation. | Ideal: The child repeats the same mechanic with a variation. | Un... _(source: Round 2 -- Repeat With A Variation)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child says again, names a favorite part, or quietly watches the recap. | Unexpe... _(source: Step 5: Closing + IB Concepts)_
