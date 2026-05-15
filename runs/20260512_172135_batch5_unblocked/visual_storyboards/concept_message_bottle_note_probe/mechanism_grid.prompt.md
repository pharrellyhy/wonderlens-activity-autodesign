# Mechanism Storyboard Prompt - concept_message_bottle_note_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Message Bottle Note" (concept_message_bottle_note_probe); category=cat3; tier=T1; mechanic=care; pillar=Discovery; style=field_experiment; focal=message_bottle_note.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: A parent starts a kindness-note activity with paper optional. The AI avoids private contact details, asks...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Kind Message Maker rule: name who the kindness message is for. I only...
3. Child Action: The repeated mechanic is care: Round 1 -- Choose the person | [round-1 guide] "Round 1: name who the kindness mess...
4. Feedback Loop: [specific] "Grandma is your recipient." | [redirect] "Use first name or role only; no private address or phone det...
5. Variation: Round 2 -- Build the message | [round-2 guide] "Round 2: say one kind sentence or draw one symbol." | Ideal: "Than...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your ow...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: A parent starts a kindness-note activity with paper optional. The AI avoids private contact details, asks the child to speak any written text aloud, and never claims OCR or externa... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Kind Message Maker rule: name who the kindness message is for. I only save what you choos... | Ideal: Child confirms the role or starts round on... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is care: Round 1 -- Choose the person | [round-1 guide] "Round 1: name who the kindness message is for." | Ideal: "For Grandma." | Unexpected: Names someone private or unsafe | No respons... _(source: Round 1 -- Choose the person)_
- **4. Feedback Loop** - [specific] "Grandma is your recipient." | [redirect] "Use first name or role only; no private address or phone details." _(source: Round 1 -- Choose the person)_
- **5. Variation** - Round 2 -- Build the message | [round-2 guide] "Round 2: say one kind sentence or draw one symbol." | Ideal: "Thank you for helping me." | Unexpected: Writes but expects AI to read it | No... _(source: Round 2 -- Build the message)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Responsibility and Perspective today. You used your own care action to make the r... | Ideal: "Again!" / names a favorite part. |... _(source: Step 5: Closing + IB Concepts)_
