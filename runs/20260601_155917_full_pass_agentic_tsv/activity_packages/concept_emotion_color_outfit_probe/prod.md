## Emotion Color Outfit

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Emotion Color Outfit |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy (primary), observation, language expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `care` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child names a mood or chooses a color to represent a feeling.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Emotion Color Outfit starter cue, name the child as emotion color outfit player, and preview the first emotion-color outfit choice turn.

**Example AI line:** "Emotion Color Outfit starts now. You are the emotion color outfit player; I will help one emotion-color outfit choice turn at a time."

**Child responses:**

1. (Ideal) The child accepts the emotion color outfit player role, notices the starter cue, or names something connected to the feeling color.
2. (Unexpected) Child asks for another game, starts the kind response before the Emotion Color Outfit mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Emotion Color Outfit title/trigger card without taking the emotion color outfit player role yet.

**AI follow-up:**

1. Name the emotion color outfit player role, connect it to the starter cue, and preview the first kind response.
2. Acknowledge the request, return to the Emotion Color Outfit promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Emotion Color Outfit role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one emotion-color outfit choice cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the kind response loop for Emotion Color Outfit or asks for the easiest version.
2. (Unexpected) Child tries to skip the feeling color, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Emotion Color Outfit rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Emotion Color Outfit loop as AI prompt, child kind response, saved token, and show the first response slot.
2. Keep the rule tied to the feeling color, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Emotion Color Outfit rule in one sentence and ask for yes, a point, or the first chance to choose a kind response.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `emotion_color_character_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If recoloring is unavailable, block at Phase 0 or run a voice-only emotion-color conversation without claiming the outfit changed.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling. Ask the child to notice a need and help in the first small turn.

**Example AI line:** "Let us start: The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling. Try the first feeling color choice now."

**Child responses:**

1. (Ideal) The child notices the feeling color cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the feeling color cue, or offers help that does not fit the need.
3. (No response) Child watches the feeling color cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the feeling color, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the feeling color, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and emotion-color outfit choice cue. Use `emotion_color_character_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If recoloring is unavailable, block at Phase 0 or run a voice-only emotion-color conversation without claiming the outfit changed.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second care turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child notices the outfit color choice cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the outfit color choice cue, or offers help that does not fit the need.
3. (No response) Child watches the outfit color choice cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the outfit color choice, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the outfit color choice, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and emotion-color outfit choice cue. Use `emotion_color_character_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If recoloring is unavailable, block at Phase 0 or run a voice-only emotion-color conversation without claiming the outfit changed.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your emotion-color outfit choice turns?"

**Child responses:**

1. (Ideal) The child notices the care-and-color recap cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the care-and-color recap cue, or offers help that does not fit the need.
3. (No response) Child watches the care-and-color recap cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the care-and-color recap, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the care-and-color recap, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and emotion-color outfit choice cue. Use `emotion_color_character_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If recoloring is unavailable, block at Phase 0 or run a voice-only emotion-color conversation without claiming the outfit changed.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your emotion-color outfit choice turns are saved: we started Emotion Color Outfit, practiced emotion-color outfit choice, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the care-and-color recap changed the Emotion Color Outfit board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Emotion Color Outfit payoff or ignores how the saved kind response turns connect.
3. (No response) Child watches the Emotion Color Outfit reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's kind response turns, name one concrete saved token, and invite a short reflection.
2. Hold the Emotion Color Outfit reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Emotion Color Outfit board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Emotion Color Outfit moment, asks to play again, or watches the emotion color outfit recap badge.
2. (Unexpected) Child shifts topic before the recap names the kind response skill or Form and Responsibility.
3. (No response) Child stays on the Emotion Color Outfit recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same care mechanic and the emotion color outfit frame.
2. Close Emotion Color Outfit first, name the practiced kind response, and then offer one next-round seed.
3. [wait 2s] Read the Emotion Color Outfit badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `emotion_color_outfit`, and next-step hint.
