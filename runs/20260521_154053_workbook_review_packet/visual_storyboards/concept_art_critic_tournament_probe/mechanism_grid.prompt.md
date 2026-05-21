# Mechanism Storyboard Prompt - concept_art_critic_tournament_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Art Critic Tournament" (concept_art_critic_tournament_probe); category=cat1; tier=T1; mechanic=compare; pillar=Discovery; style=field_experiment; focal=art_critic_tournament.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Trigger: The approved artwork set can show two age-safe images side by side. The AI asks for visible reasons, supp...
2. Prompt: Step 2: Role And Rules | [clear guide tone] "Gallery Chooser rule: choose a favorite artwork and name one visible...
3. Child Action: The repeated mechanic is compare: Round 1 -- Compare pair one | [round-1 guide] "Round 1: choose a favorite artwor...
4. Feedback Loop: Ideal: [specific] "Blue waves is visible evidence. Artwork A advances." | Unexpected: [redirect] "Famous is outsid...
5. Variation: Round 2 -- Compare the winner | [round-2 guide] "Round 2: put the winner against another approved artwork." | Idea...
6. Completion: Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Perspective today. You used your own compare...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Trigger: The approved artwork set can show two age-safe images side by side. The AI asks for visible reasons, supports ties, and avoids outside artist claims unless metadata supplies them. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | [clear guide tone] "Gallery Chooser rule: choose a favorite artwork and name one visible reason. I only save... | Ideal: Child confirms the role or starts round one... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is compare: Round 1 -- Compare pair one | [round-1 guide] "Round 1: choose a favorite artwork and name one visible reason." | Ideal: "I pick the blue one because waves." | Unexpected: Say... _(source: Round 1 -- Compare pair one)_
- **4. Feedback Loop** - Ideal: [specific] "Blue waves is visible evidence. Artwork A advances." | Unexpected: [redirect] "Famous is outside our card metadata. Use color, shape, or feeling." | No response: [wait 2s... _(source: Round 1 -- Compare pair one)_
- **5. Variation** - Round 2 -- Compare the winner | [round-2 guide] "Round 2: put the winner against another approved artwork." | Ideal: "This one feels calmer." | Unexpected: Wants unapproved art | No respons... _(source: Round 2 -- Compare the winner)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm close] "You practiced Form and Perspective today. You used your own compare action to make the result." | Ideal: "Again!" / names a favorite part. | Un... _(source: Step 5: Closing + IB Concepts)_
