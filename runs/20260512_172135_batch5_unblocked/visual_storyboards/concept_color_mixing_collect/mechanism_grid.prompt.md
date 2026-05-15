# Mechanism Storyboard Prompt - concept_color_mixing_collect

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Two-Color Mix Lab" (concept_color_mixing_collect); category=cat1; tier=T1; mechanic=collect; pillar=Discovery; style=field_experiment; focal=two_color_mix.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: The child names or finds red plus yellow, blue plus yellow, and red plus blue. Each pair gets a prediction and a r...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Lab rule: collect a pair, guess the mix, save the result. Three pa...
3. Child Action: The repeated mechanic is collect: Round 1 -- Collect Red + Yellow | [focused lab tone] "First pair: collect red an...
4. Feedback Loop: [specific praise] "Red plus yellow is collected, and orange is the result guess. Token 1 is saved." | [warm redire...
5. Variation: Round 2 -- Collect Blue + Yellow | [curious lab tone] "Second pair: collect blue and yellow. Which result should t...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Color Mix Tester badge. You used Causation by c...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - The child names or finds red plus yellow, blue plus yellow, and red plus blue. Each pair gets a prediction and a result stamp on the lab board. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Lab rule: collect a pair, guess the mix, save the result. Three pairs make a color wheel." | Ideal: "Okay." | Unexpected: "Can I do it my way... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is collect: Round 1 -- Collect Red + Yellow | [focused lab tone] "First pair: collect red and yellow. Point to them, name them, or find objects with those... | Ideal: "Red and yellow make... _(source: Round 1 -- Collect Red + Yellow)_
- **4. Feedback Loop** - [specific praise] "Red plus yellow is collected, and orange is the result guess. Token 1 is saved." | [warm redirect] "Banana gives us yellow. We still need the red partner, then the mix po... _(source: Round 1 -- Collect Red + Yellow)_
- **5. Variation** - Round 2 -- Collect Blue + Yellow | [curious lab tone] "Second pair: collect blue and yellow. Which result should this pair make?" | Ideal: "Green." | Unexpected: "Orange again." / "I only f... _(source: Round 2 -- Collect Blue + Yellow)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Color Mix Tester badge. You used Causation by collecting color pairs, and... | Ideal: "Again" or names a favorite round. |... _(source: Step 5: Closing + IB Concepts)_
