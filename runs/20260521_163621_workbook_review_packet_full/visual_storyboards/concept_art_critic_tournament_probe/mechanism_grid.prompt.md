# Mechanism Storyboard Prompt - concept_art_critic_tournament_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Art Critic Tournament" (concept_art_critic_tournament_probe); category=cat1; tier=T1; mechanic=compare; pillar=Mystery; style=mystery_lens; focal=art_critic_tournament.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Two rights-cleared artworks appear side by side each round and the child decides which one continues.
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is compare: Round 1 -- Match 1 | Show two approved artworks and ask which one should stay. |...
4. Feedback Loop: Ideal: Name the comparison evidence, save the selected option, and keep the next comparison state clear. | Unexpec...
5. Variation: Round 2 -- Match 2 | Bring in a new challenger against the current winner. | Ideal: The child compares the visible...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Two rights-cleared artworks appear side by side each round and the child decides which one continues. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child agrees to the comparison choice loop for Art Critic Tournament... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is compare: Round 1 -- Match 1 | Show two approved artworks and ask which one should stay. | Ideal: The child compares the visible options for the first artwork match and chooses or expla... _(source: Round 1 -- Match 1)_
- **4. Feedback Loop** - Ideal: Name the comparison evidence, save the selected option, and keep the next comparison state clear. | Unexpected: Restate the two visible options and the comparison lens for the first... _(source: Round 1 -- Match 1)_
- **5. Variation** - Round 2 -- Match 2 | Bring in a new challenger against the current winner. | Ideal: The child compares the visible options for the new challenger match and chooses or explains one. | Une...... _(source: Round 2 -- Match 2)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child names a favorite Art Critic Tournament moment, asks to play again, or wat... _(source: Step 5: Closing + IB Concepts)_
