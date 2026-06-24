# Emotion Reader

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Emotion Reader |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy, observation, language_expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child notices an obvious expression or body cue and thinks about what feeling or help might fit.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Emotion Reader.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `care` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the active cue sequence, repeated care action, ideal/unexpected/no-response branches, honest visual fallback behavior, and transcript verification before advancing.

**4. Typical Scenario**

The child plays Emotion Reader with emotion_reader as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Emotion Reader. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the feeling helper role, notices the starter cue, or names something connected to the visible face or body cue.
2. (Unexpected) Child asks for another game, starts the kind response before the Emotion Reader mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Emotion Reader opening moment without taking the feeling helper role yet.

**AI follow-up:**

1. Name the feeling helper role, connect it to the starter cue, and preview the first kind response.
2. Acknowledge the request, return to the Emotion Reader promise, and offer the smallest supported first action.
3. [wait 2s] Name the Emotion Reader feeling helper role and the first cue, then model one tiny gentle response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Here is how it goes: I share a cue, you choose one kind response, and we save one for each turn."

**Child responses:**

1. (Ideal) The child agrees to the kind response loop for Emotion Reader or asks for the easiest version.
2. (Unexpected) Child tries to skip the visible face or body cue, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Emotion Reader rule without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Emotion Reader loop as a shared cue, a child kind response, and a saved turn, then show the first response slot.
2. Keep the rule tied to the visible face or body cue, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Say the Emotion Reader rule in one sentence and ask for yes, or the first chance to choose a kind response.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Worried Hands Cue:**

**Runtime AI instruction:** Preserve the workbook promise: the displayed cue shows worried hands. Ask the child to name a fitting feeling, need, or kind help action for that cue.

**Example AI line:** "Look at the worried hands. What might they feel or need?"

**Child responses:**

1. (Ideal) The child notices the worried hands cue and suggests a worried/nervous feeling, a need for comfort, or a fitting help action.
2. (Unexpected) Child judges the character, gives generic kindness without tying it to worried hands, or names a different round cue.
3. (No response) Child watches the worried hands cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness for this turn, and show the calmer or helped state.
2. Reframe without judging, name the worried hands cue, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for worried hands, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Sleepy Shoulders Cue:**

**Runtime AI instruction:** Keep the same source frame and ask for a second care turn about the sleepy shoulders cue.

**Example AI line:** "Now look at the sleepy shoulders. What might help someone who looks tired?"

**Child responses:**

1. (Ideal) The child notices the sleepy shoulders cue and suggests a tired/sleepy feeling, a need for rest, or a fitting help action.
2. (Unexpected) Child judges the character, gives generic kindness without tying it to sleepy shoulders, or names a different round cue.
3. (No response) Child watches the sleepy shoulders cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness for this turn, and show the calmer or helped state.
2. Reframe without judging, name the sleepy shoulders cue, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for sleepy shoulders, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Brave Try Cue:**

**Runtime AI instruction:** Ask the child to choose encouragement or help for the brave try cue so the source action has closure.

**Example AI line:** "This friend is trying bravely. What could you say or do to help them keep trying?"

**Child responses:**

1. (Ideal) The child notices the brave try cue and suggests encouragement, help, or a fitting feeling for someone trying.
2. (Unexpected) Child judges the character, gives generic kindness without tying it to the brave try, or names a different round cue.
3. (No response) Child watches the brave try cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness for this turn, and show the calmer or helped state.
2. Reframe without judging, name the brave try cue, and offer two encouragement choices.
3. [wait 2s] Model one caring sentence for brave trying, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the kind help choice changed the Emotion Reader board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Emotion Reader payoff or ignores how the saved kind response turns connect.
3. (No response) Child watches the Emotion Reader reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's kind response turns, name one concrete saved turn, and invite a short reflection.
2. Hold the Emotion Reader reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Emotion Reader board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

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

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `emotion_reader`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
