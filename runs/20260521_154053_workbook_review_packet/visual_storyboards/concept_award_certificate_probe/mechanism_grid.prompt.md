# Mechanism Storyboard Prompt - concept_award_certificate_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Award Certificate" (concept_award_certificate_probe); category=cat3; tier=T1; mechanic=care; pillar=Discovery; style=field_experiment; focal=award_certificate.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A child wants to thank a helper, teammate, sibling, or grown-up. The AI keeps the certificate appreciativ...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Appreciation Designer rule: name someone who helped, tried hard, or d...
3. Child Action: The repeated mechanic is care: Round 1 -- Choose the honoree | [round-1 guide] "Round 1: name someone who helped,...
4. Feedback Loop: Ideal: [specific] "Your sister is the honoree." | Unexpected: [redirect] "This award is appreciation, not ranking....
5. Variation: Round 2 -- Pick the award reason | [round-2 guide] "Round 2: choose kindness, trying hard, helping, bravery, creat...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your ow...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A child wants to thank a helper, teammate, sibling, or grown-up. The AI keeps the certificate appreciative rather than competitive and supports paper drawing, simple on-screen desi... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Appreciation Designer rule: name someone who helped, tried hard, or deserves appreciation... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is care: Round 1 -- Choose the honoree | [round-1 guide] "Round 1: name someone who helped, tried hard, or deserves appreciation." | Ideal: "My sister." | Unexpected: Wants a best/worst c... _(source: Round 1 -- Choose the honoree)_
- **4. Feedback Loop** - Ideal: [specific] "Your sister is the honoree." | Unexpected: [redirect] "This award is appreciation, not ranking. Pick one helper." | No response: [wait 2s] [gentle hint] "Say someone who... _(source: Round 1 -- Choose the honoree)_
- **5. Variation** - Round 2 -- Pick the award reason | [round-2 guide] "Round 2: choose kindness, trying hard, helping, bravery, creativity, or teamwork." | Ideal: "Helping, because she cleaned." | Unexpected:... _(source: Round 2 -- Pick the award reason)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your own care action to make the r... | Ideal: "Again!" / names a favorite part. |... _(source: Step 5: Closing + IB Concepts)_
