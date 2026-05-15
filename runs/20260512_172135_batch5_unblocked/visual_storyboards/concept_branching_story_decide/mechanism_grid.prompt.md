# Mechanism Storyboard Prompt - concept_branching_story_decide

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Two-Door Story Quest" (concept_branching_story_decide); category=cat1; tier=T1; mechanic=decide; pillar=Adventure; style=time_traveler; focal=story_choice_path.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: Child photographs a toy turtle; the AI makes it the hero of a two-door adventure. A blue door creates a river path...
2. Prompt: Step 2: Rule Introduction -- You Choose the Path | [adventurous guide tone] "You are the Story Path Chooser. I wil...
3. Child Action: The repeated mechanic is decide: Round 1 -- Door Choice | [mysterious whisper] "The blue door hums softly. The gol...
4. Feedback Loop: [story reveal tone] "The door opens. If you chose blue, a river path appears. If you chose gold, a bell path appea...
5. Variation: Round 2 -- Helper Choice | [curious narrator tone] "Because of that door, two helpers appear. A sleepy cloud float...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You did it, Story Path Chooser. You used Perspective. You chos...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - Child photographs a toy turtle; the AI makes it the hero of a two-door adventure. A blue door creates a river path, a cloud helper builds a bridge, and the chosen ending becomes the final s... _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction -- You Choose the Path | [adventurous guide tone] "You are the Story Path Chooser. I will offer two next steps. You choose one. The st... | Ideal: "Okay!" / "I cho... _(source: Step 2: Rule Introduction -- You Choose the Path)_
- **3. Child Action** - The repeated mechanic is decide: Round 1 -- Door Choice | [mysterious whisper] "The blue door hums softly. The gold door jingles. Which door does {story_starter} open?" | Ideal: "Blue." / "Gold." | Unexpected:... _(source: Round 1 -- Door Choice)_
- **4. Feedback Loop** - [story reveal tone] "The door opens. If you chose blue, a river path appears. If you chose gold, a bell path appears." | [playful validation] "A red door would be wild. For this room, choos... _(source: Round 1 -- Door Choice)_
- **5. Variation** - Round 2 -- Helper Choice | [curious narrator tone] "Because of that door, two helpers appear. A sleepy cloud floats by. A tiny drum taps... | Ideal: "Cloud." / "Drum." | Unexpected: "A dino... _(source: Round 2 -- Helper Choice)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You did it, Story Path Chooser. You used Perspective. You chose what the hero should do.... | Ideal: "I want another path!" / "I chose it... _(source: Step 5: Closing + IB Concepts)_
