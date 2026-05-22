# Mechanism Storyboard Prompt - concept_color_famous_art_probe

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Color In Famous Art" (concept_color_famous_art_probe); category=cat1; tier=T1; mechanic=enumerate; pillar=Discovery; style=field_experiment; focal=color_in_famous_art.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A photographed yellow, blue, red, or green object becomes the bridge to rights-cleared artworks with matching colo...
2. Prompt: Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Idea...
3. Child Action: The repeated mechanic is enumerate: Round 1 -- Capture The Color | Start from the child color before showing artwo...
4. Feedback Loop: Ideal: Repeat the counted evidence, mark the number/name token, and show what set will be checked next. | Unexpect...
5. Variation: Round 2 -- Meet The First Artwork | Show one approved artwork where the color is dominant and give a child-safe ba...
6. Completion: Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The chil...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A photographed yellow, blue, red, or green object becomes the bridge to rights-cleared artworks with matching color metadata. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Role And Rules | Explain the rule as an action loop and name any required asset or honest fallback. | Ideal: The child agrees to the counting or naming step loop for Color In Famous... _(source: Step 2: Role And Rules)_
- **3. Child Action** - The repeated mechanic is enumerate: Round 1 -- Capture The Color | Start from the child color before showing artworks. | Ideal: The child counts, names, or checks the items required for the real-world color sa... _(source: Round 1 -- Capture The Color)_
- **4. Feedback Loop** - Ideal: Repeat the counted evidence, mark the number/name token, and show what set will be checked next. | Unexpected: Return attention to the target set for the real-world color sample, cou... _(source: Round 1 -- Capture The Color)_
- **5. Variation** - Round 2 -- Meet The First Artwork | Show one approved artwork where the color is dominant and give a child-safe background note. | Ideal: The child counts, names, or checks the items requir... _(source: Round 2 -- Meet The First Artwork)_
- **6. Completion** - Step 5: Closing + IB Concepts | Close with the two key concepts and one parent-reviewable recap. | Ideal: The child names a favorite Color In Famous Art moment, asks to play again, or watch... _(source: Step 5: Closing + IB Concepts)_
