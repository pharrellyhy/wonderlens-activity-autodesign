# Mechanism Storyboard Prompt - concept_scavenger_hunt_collect

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Shared Clue Scavenger Hunt" (concept_scavenger_hunt_collect); category=cat5; tier=T1; mechanic=collect; pillar=Adventure; style=quest_collector; focal={shared_feature}.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Child photographs a round blue ball; the AI chooses the clue "round," and the child hunts for three more round thi...
2. Prompt: Step 2: Mission Briefing -- Shared Clue Scout | [adventurous guide tone] "You are the Shared Clue Scout. Find thre...
3. Child Action: The repeated mechanic is collect: Round 1 -- First Matching Find | [curious scout tone] "First photo is in. Let me...
4. Feedback Loop: [triumphant] "Scout verdict: MATCH! I can see the clue. Find 1 of 3. What should we call it?" | [kind redirect] "I...
5. Variation: Round 2 -- Second Matching Find | [playful detective tone] "Second scout photo! I need the same clue: {shared_feat...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You did it, Shared Clue Scout. You used Form today. You notice...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Child photographs a round blue ball; the AI chooses the clue "round," and the child hunts for three more round things nearby. If one find is only "maybe" round, it can sit beside the trail... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Mission Briefing -- Shared Clue Scout | [adventurous guide tone] "You are the Shared Clue Scout. Find three things with {shared_feature}. Snap each m... | Ideal: "Ready!" / "I know... _(source: Step 2: Mission Briefing -- Shared Clue Scout)_
- **3. Child Action** - The repeated mechanic is collect: Round 1 -- First Matching Find | [curious scout tone] "First photo is in. Let me check the shared clue. Does this one match {shared_feature}?" | Ideal: "Yes, it matches!" / "I... _(source: Round 1 -- First Matching Find)_
- **4. Feedback Loop** - [triumphant] "Scout verdict: MATCH! I can see the clue. Find 1 of 3. What should we call it?" | [kind redirect] "It is a cool find. This mission needs the shared clue. Does any part show {s... _(source: Round 1 -- First Matching Find)_
- **5. Variation** - Round 2 -- Second Matching Find | [playful detective tone] "Second scout photo! I need the same clue: {shared_feature}. Is it hiding here too?" | Ideal: "Yes!" / "It is the same color." | U... _(source: Round 2 -- Second Matching Find)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You did it, Shared Clue Scout. You used Form today. You noticed what things were like. Yo... | Ideal: "I want another clue!" / "I did it!... _(source: Step 5: Closing + IB Concepts)_
