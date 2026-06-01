## Emotion Reader

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Emotion Reader |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy (primary), observation, language expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child notices an obvious expression or body cue and thinks about what feeling or help might fit.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `care` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A character, animal, or story moment shows an obvious emotional expression.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Emotion Reader. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the feeling helper role, notices the starter cue, or names something connected to the visible face or body cue.
2. (Unexpected) Child asks for another game, starts the kind response before the Emotion Reader mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Emotion Reader title/trigger card without taking the feeling helper role yet.

**AI follow-up:**

1. Name the feeling helper role, connect it to the starter cue, and preview the first kind response.
2. Acknowledge the request, return to the Emotion Reader promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Emotion Reader role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the kind response loop for Emotion Reader or asks for the easiest version.
2. (Unexpected) Child tries to skip the visible face or body cue, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Emotion Reader rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Emotion Reader loop as AI prompt, child kind response, saved token, and show the first response slot.
2. Keep the rule tied to the visible face or body cue, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Emotion Reader rule in one sentence and ask for yes, a point, or the first chance to choose a kind response.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `emotion_expression_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child notices an obvious expression or body cue and thinks about what feeling or help might fit. Ask the child to notice a need and help in the first small turn.

**Example AI line:** "Let us start: The child notices an obvious expression or body cue and thinks about what feeling or help might fit. What is your first try?"

**Child responses:**

1. (Ideal) The child notices the visible face or body cue cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the visible face or body cue cue, or offers help that does not fit the need.
3. (No response) Child watches the visible face or body cue cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the visible face or body cue, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the visible face or body cue, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `emotion_expression_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second care turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child notices the possible feeling cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the possible feeling cue, or offers help that does not fit the need.
3. (No response) Child watches the possible feeling cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the possible feeling, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the possible feeling, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `emotion_expression_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child notices the kind help choice cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the kind help choice cue, or offers help that does not fit the need.
3. (No response) Child watches the kind help choice cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the kind help choice, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the kind help choice, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `emotion_expression_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the kind help choice changed the Emotion Reader board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Emotion Reader payoff or ignores how the saved kind response turns connect.
3. (No response) Child watches the Emotion Reader reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's kind response turns, name one concrete saved token, and invite a short reflection.
2. Hold the Emotion Reader reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Emotion Reader board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Emotion Reader moment, asks to play again, or watches the emotion reader recap badge.
2. (Unexpected) Child shifts topic before the recap names the kind response skill or Form and Responsibility.
3. (No response) Child stays on the Emotion Reader recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same care mechanic and the emotion reader frame.
2. Close Emotion Reader first, name the practiced kind response, and then offer one next-round seed.
3. [wait 2s] Read the Emotion Reader badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `emotion_reader`, and next-step hint.
