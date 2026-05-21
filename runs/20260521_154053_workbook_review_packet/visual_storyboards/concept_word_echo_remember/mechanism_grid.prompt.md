# Mechanism Storyboard Prompt - concept_word_echo_remember

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Echo Word Stage" (concept_word_echo_remember); category=cat1; tier=T0; mechanic=remember; pillar=Performance; style=voice_stage; focal=echo_word_pattern.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A child asks what a {target_word} is called. The AI turns {target_word} and {target_word}-{target_word} into two p...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Hear. Say. Save. Make a word ladder." | Ideal: "Okay." | Unexpecte...
3. Child Action: The repeated mechanic is remember: Round 1 -- Tiny Hide Echo | [focused playful tone] "Look, listen: {target_word}...
4. Feedback Loop: Ideal: [specific praise] "The stage lights up. {target_word} came back. Token 1 saved." | Unexpected: [warm redire...
5. Variation: Round 2 -- Double Pattern Echo | [focused playful tone] "Two beats: {target_word}-{target_word}. Soft mouse voice....
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "Echo Keeper badge earned. Form and Connection badge." | Ideal:...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A child asks what a {target_word} is called. The AI turns {target_word} and {target_word}-{target_word} into two playful echo rounds. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Hear. Say. Save. Make a word ladder." | Ideal: "Okay." | Unexpected: "Can I do it my way?" | No response: Child hesitates. | Ideal: [encourag... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is remember: Round 1 -- Tiny Hide Echo | [focused playful tone] "Look, listen: {target_word}. I hide it. Echo it back." | Ideal: "{target_word}." after the hide. | Unexpected: "I say mug.... _(source: Round 1 -- Tiny Hide Echo)_
- **4. Feedback Loop** - Ideal: [specific praise] "The stage lights up. {target_word} came back. Token 1 saved." | Unexpected: [warm redirect] "Mug is nearby. Echo {target_word}." | No response: [wait 2s] [gentle h... _(source: Round 1 -- Tiny Hide Echo)_
- **5. Variation** - Round 2 -- Double Pattern Echo | [focused playful tone] "Two beats: {target_word}-{target_word}. Soft mouse voice." | Ideal: "{target_word} {target_word}." | Unexpected: "I squeak anything... _(source: Round 2 -- Double Pattern Echo)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "Echo Keeper badge earned. Form and Connection badge." | Ideal: "Again" or names a favorite round. | Unexpected: Child asks for a differen... _(source: Step 5: Closing + IB Concepts)_
