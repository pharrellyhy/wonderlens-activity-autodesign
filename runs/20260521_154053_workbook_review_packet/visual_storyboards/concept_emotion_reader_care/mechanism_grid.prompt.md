# Mechanism Storyboard Prompt - concept_emotion_reader_care

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "Feeling Helper Station" (concept_emotion_reader_care); category=cat1; tier=T1; mechanic=care; pillar=Nurture; style=care_station; focal=visible_feeling_cue.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
1. Setup: A story animal looks worried on a card. The child notices tight hands, offers a gentle check-in, then sees the ani...
2. Prompt: Step 2: Rule Introduction | [clear guide tone] "Helper rule: notice the cue, say what they might need, then choose...
3. Child Action: The repeated mechanic is care: Round 1 -- Worried Hands Need | [focused helper tone] "Look at the tight hands and...
4. Feedback Loop: Ideal: [specific praise] "Asking first is gentle care. The hands loosen a little. Token 1 is saved." | Unexpected:...
5. Variation: Round 2 -- Tired Body Need | [soft helper tone] "Now the shoulders droop and the eyes look sleepy. This character...
6. Completion: Step 5: Closing + IB Concepts | [warm celebration] "You earned the Feeling Helper badge. You used Perspective by a...
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image.
```

## Panel Captions

- **1. Setup** - A story animal looks worried on a card. The child notices tight hands, offers a gentle check-in, then sees the animal relax a little before the next need appears. _(source: Step 1: Transition Bridge)_
- **2. Prompt** - Step 2: Rule Introduction | [clear guide tone] "Helper rule: notice the cue, say what they might need, then choose one gentle help." | Ideal: "Okay." | Unexpected: "Can I do it my way?" | N... _(source: Step 2: Rule Introduction)_
- **3. Child Action** - The repeated mechanic is care: Round 1 -- Worried Hands Need | [focused helper tone] "Look at the tight hands and high eyebrows. This character might feel worried. What gen... | Ideal: "Ask if it wants help."... _(source: Round 1 -- Worried Hands Need)_
- **4. Feedback Loop** - Ideal: [specific praise] "Asking first is gentle care. The hands loosen a little. Token 1 is saved." | Unexpected: [warm redirect] "Candy might be fun later. First care is safer when we ask... _(source: Round 1 -- Worried Hands Need)_
- **5. Variation** - Round 2 -- Tired Body Need | [soft helper tone] "Now the shoulders droop and the eyes look sleepy. This character might need rest. What ca... | Ideal: "Give it a quiet blanket." / "Let it r... _(source: Round 2 -- Tired Body Need)_
- **6. Completion** - Step 5: Closing + IB Concepts | [warm celebration] "You earned the Feeling Helper badge. You used Perspective by asking what the character mi... | Ideal: "Again" or names a favorite round.... _(source: Step 5: Closing + IB Concepts)_
