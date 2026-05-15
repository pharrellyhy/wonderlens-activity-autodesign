# Mechanism Storyboard Prompt - concept_travel_planner_predict

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Pretend Trip Planner" (concept_travel_planner_predict); category=cat1; tier=T1; mechanic=predict; pillar=Discovery; style=prediction_lab; focal=pretend_trip_prediction.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: The child plans a pretend trip to a rainy forest. They predict the needed item, travel helper, and surprise plan b...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Here is the rule: predict before I flip the card, then we save wha...
3. Child Action: The repeated mechanic is predict: Round 1 -- Predict What We Need | [focused playful tone] "Before the rainy revea...
4. Feedback Loop: [reveal tone] "The reveal is raindrops. Raincoat matches, so token 1 becomes a dry-trip stamp." | [warm redirect]...
5. Variation: Round 2 -- Predict How to Travel | [focused playful tone] "Before I reveal the path, predict what travel helps cro...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Trip Predictor badge. You used Causation by pre...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - The child plans a pretend trip to a rainy forest. They predict the needed item, travel helper, and surprise plan before each hidden card flips. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Here is the rule: predict before I flip the card, then we save what the reveal shows." | Ideal: "Okay." | Unexpected: "Can I do it my way?" |... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is predict: Round 1 -- Predict What We Need | [focused playful tone] "Before the rainy reveal, predict what we will need first: raincoat, snack, or sunglas... | Ideal: "raincoat." | Unexp... _(source: Round 1 -- Predict What We Need)_
- **4. Feedback Loop** - [reveal tone] "The reveal is raindrops. Raincoat matches, so token 1 becomes a dry-trip stamp." | [warm redirect] "A swimsuit is fun for water play. The reveal is raindrops, so choose somet... _(source: Round 1 -- Predict What We Need)_
- **5. Variation** - Round 2 -- Predict How to Travel | [focused playful tone] "Before I reveal the path, predict what travel helps cross a wide puddle: walking, bus... | Ideal: "boat." | Unexpected: "rocket."... _(source: Round 2 -- Predict How to Travel)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Trip Predictor badge. You used Causation by predicting what each clue woul... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
