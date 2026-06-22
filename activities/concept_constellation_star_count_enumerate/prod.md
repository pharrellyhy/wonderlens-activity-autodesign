# Constellation Star Count

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Constellation Star Count |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | counting, observation, language_expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The screen shows a small constellation or star group, and the child counts how many stars are visible.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Constellation Star Count.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `enumerate` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Constellation Star Count with constellation_star_count as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Constellation Star Count. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the star counter role, notices the starter cue, or names something connected to the first star group.
2. (Unexpected) Child asks for another game, starts the counting or naming step before the Constellation Star Count mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Constellation Star Count opening moment without taking the star counter role yet.

**AI follow-up:**

1. Name the star counter role, connect it to the starter cue, and preview the first counting or naming step.
2. Acknowledge the request, return to the Constellation Star Count promise, and offer the smallest supported first action.
3. [wait 2s] Name the Star Counter role and the first little group of stars, then model one tiny gentle response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Here is how we play: I ask, you count the stars, and we light up one star on our path each turn."

**Child responses:**

1. (Ideal) The child agrees to the counting or naming step loop for Constellation Star Count or asks for the easiest version.
2. (Unexpected) Child tries to skip the first star group, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Constellation Star Count rule without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Constellation Star Count loop as AI asks, child counts the stars, one star lights up, and show where the first answer goes.
2. Keep the rule tied to the first star group, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Say the Constellation Star Count rule in one sentence and ask if they would like to count the first little group of stars together.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `constellation_count_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a voice-only imaginary star-counting riddle and do not claim a constellation is displayed. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- First Star Group:**

**Runtime AI instruction:** Preserve the workbook promise: the child counts the visible stars in a constellation or simplified star pattern. Invite the child to count the first small group of stars.

**Example AI line:** "Let us begin counting the stars in this little group. Would you like to tell me how many you see?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the stars in the first star group.
2. (Unexpected) Child guesses the first star group without looking, counts unrelated things, or changes which stars to count.
3. (No response) Child looks at the first star group without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted stars, light up the number you heard, and show which stars come next.
2. Bring attention back to the first star group, count one star aloud, and invite the child to keep going.
3. [wait 2s] Name the first star in the first group, say "one," and invite the child to say the next number.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `constellation_count_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a voice-only imaginary star-counting riddle and do not claim a constellation is displayed. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Second Star Pattern:**

**Runtime AI instruction:** Keep the same source frame and ask for a second enumerate turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the second star group or pattern.
2. (Unexpected) Child guesses the second star group or pattern without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the second star group or pattern without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted stars, light up the number you heard, and show which stars come next.
2. Bring attention back to the second star group or pattern, count one star aloud, and invite the child to keep going.
3. [wait 2s] Name the first star in the second group or pattern, say "one," and invite the child to say the next number.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `constellation_count_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a voice-only imaginary star-counting riddle and do not claim a constellation is displayed. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Final Constellation Count:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What changed after your turns, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the total constellation recap.
2. (Unexpected) Child guesses the total constellation recap without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the total constellation recap without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted stars, light up the number you heard, and show which stars come next.
2. Bring attention back to the total constellation recap, count one star aloud, and invite the child to keep going.
3. [wait 2s] Name the first star in the whole constellation, say "one," and invite the child to say the next number.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `constellation_count_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a voice-only imaginary star-counting riddle and do not claim a constellation is displayed. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the total constellation recap changed the Constellation Star Count board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Constellation Star Count payoff or ignores how the saved counting or naming step turns connect.
3. (No response) Child watches the Constellation Star Count reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's counting or naming step turns, name one star group they counted, and invite a short reflection.
2. Hold the Constellation Star Count reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Constellation Star Count board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Constellation Star Count moment, asks to play again, or watches the constellation star count recap badge.
2. (Unexpected) Child shifts topic before the recap names the counting or naming step skill or Form.
3. (No response) Child stays on the Constellation Star Count recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same enumerate mechanic and the constellation star count frame.
2. Close Constellation Star Count first, name the practiced counting or naming step, and then offer one next-round seed.
3. [wait 2s] Read the Constellation Star Count badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `constellation_star_count`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
