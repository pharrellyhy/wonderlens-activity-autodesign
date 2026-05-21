# Mechanism Storyboard Prompt - concept_award_certificate_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Award Certificate" (concept_award_certificate_probe); category=cat3; tier=T1; mechanic=care; pillar=Nurture; style=care_station; focal=award_certificate.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A family story or photographed object inspires a handmade award such as Best Helper or Best Mom.
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is care: Round 1 -- Choose The Person | Ask who receives the award and why. | Ideal: The chi...
4. Feedback Loop: Ideal: [specific] Reflect the appreciation reason. | Unexpected: [redirect] Validate the idea, restate the safe ru...
5. Variation: Round 2 -- Design The Badge | Guide a paper-and-pencil badge with one color and one kind phrase. | Ideal: The chil...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A family story or photographed object inspires a handmade award such as Best Helper or Best Mom. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child confirms the rule or asks for a smaller version. | Unexpected:... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is care: Round 1 -- Choose The Person | Ask who receives the award and why. | Ideal: The child names a person. | Unexpected: Child gives an unrelated answer, unsafe action, or asks to cha... _(source: Round 1 -- Choose The Person)_
- **4. Feedback Loop** - Ideal: [specific] Reflect the appreciation reason. | Unexpected: [redirect] Validate the idea, restate the safe rule, and offer one easier choice. | No response: [wait 2s] [gentle] Model a... _(source: Round 1 -- Choose The Person)_
- **5. Variation** - Round 2 -- Design The Badge | Guide a paper-and-pencil badge with one color and one kind phrase. | Ideal: The child draws or names a color. | Unexpected: Child gives an unrelated answer, un... _(source: Round 2 -- Design The Badge)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child says again, names a favorite part, or quietly watches the recap. | Unexpe... _(source: Step 5: Closing + IB Concepts)_
