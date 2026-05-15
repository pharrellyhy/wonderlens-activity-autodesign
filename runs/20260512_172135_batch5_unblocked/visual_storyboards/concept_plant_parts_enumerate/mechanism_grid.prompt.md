# Mechanism Storyboard Prompt - concept_plant_parts_enumerate

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Plant Parts Field Scout" (concept_plant_parts_enumerate); category=cat5; tier=T1; mechanic=enumerate; pillar=Discovery; style=field_experiment; focal=visible_plant_part.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A child photographs a potted plant. The AI asks them to find leaf, stem, and one special part, then makes a labele...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Scout rule: point or name a visible part, then we pin it on the pl...
3. Child Action: The repeated mechanic is enumerate: Round 1 -- Leaf Evidence Hunt | [field-guide tone] "Find a leaf clue: flat sha...
4. Feedback Loop: [specific praise] "Flat green shape is leaf evidence. Leaf token saved." | [warm redirect] "The pot is not a plant...
5. Variation: Round 2 -- Stem Path Hunt | [investigator tone] "Trace the path that holds the plant up. Is it a stem, stalk, or b...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Plant Parts Scout badge. You used Form by namin...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A child photographs a potted plant. The AI asks them to find leaf, stem, and one special part, then makes a labeled plant map. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Scout rule: point or name a visible part, then we pin it on the plant map." | Ideal: "Okay." | Unexpected: "Can I do it my way?" | No respons... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is enumerate: Round 1 -- Leaf Evidence Hunt | [field-guide tone] "Find a leaf clue: flat shape, edge, or green part. What proves it is a leaf?" | Ideal: "Leaf, flat green shape." | Unexpe... _(source: Round 1 -- Leaf Evidence Hunt)_
- **4. Feedback Loop** - [specific praise] "Flat green shape is leaf evidence. Leaf token saved." | [warm redirect] "The pot is not a plant part. If no leaf is visible, say leaf not visible." _(source: Round 1 -- Leaf Evidence Hunt)_
- **5. Variation** - Round 2 -- Stem Path Hunt | [investigator tone] "Trace the path that holds the plant up. Is it a stem, stalk, or branch?" | Ideal: "stem." | Unexpected: "Stick." / stem is hidden. | No resp... _(source: Round 2 -- Stem Path Hunt)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Plant Parts Scout badge. You used Form by naming visible parts, and Functi... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
