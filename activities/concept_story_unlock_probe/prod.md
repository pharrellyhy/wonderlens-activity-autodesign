# Story Challenge Unlock

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Story Challenge Unlock |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | imagination, observation, language_expression |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

A fox unlocks story gates with a moon-door color, a quiet owl sound, and the word bonjour.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Story Challenge Unlock.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `imagine` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Story Challenge Unlock with story_challenge_unlock as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Story Challenge Unlock. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the story gate unlocker role, notices the starter cue, or names something connected to the moon door color challenge.
2. (Unexpected) Child asks for another game, starts the story unlock response before the Story Challenge Unlock mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Story Challenge Unlock opening moment without taking the story gate unlocker role yet.

**AI follow-up:**

1. Name the story gate unlocker role, connect it to the starter cue, and preview the first story unlock response.
2. Acknowledge the request, return to the Story Challenge Unlock promise, and offer the smallest supported first action.
3. [wait 2s] Name the Story Challenge Unlock role and the first moment, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Here is how it goes: I share a story moment, you give one little answer, and a gate opens each turn."

**Child responses:**

1. (Ideal) The child agrees to the story unlock response loop for Story Challenge Unlock or asks for the easiest version.
2. (Unexpected) Child tries to skip the moon door color challenge, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Story Challenge Unlock rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Story Challenge Unlock loop as a story moment, the child's little answer, an opened gate, and invite the first response.
2. Keep the rule tied to the moon door color challenge, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Say the Story Challenge Unlock idea in one sentence and ask, would you like to give the first little answer?

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `story_unlock_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Unlock The Moon Door:**

**Runtime AI instruction:** Tell the story beat before the task, then pause for a color challenge.

**Example AI line:** "The fox reaches a moon door. Can you name or show silver, white, or blue so it opens?"

**Child responses:**

1. (Ideal) The child names or shows silver, white, or blue for the moon door.
2. (Unexpected) Child answers before the moon-door story pause, gives an unrelated color/object, or tries to open the door without the color challenge.
3. (No response) Child watches the locked moon door without naming or showing a moon-color item.

**AI follow-up:**

1. Open the moon door, narrate the fox stepping through, and keep the color saved.
2. Return to the moon-door cliffhanger, repeat the allowed colors, and ask for one named or shown color.
3. [wait 2s] Name the moon door colors, model "blue opens it," and invite the child to say or show one color.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `story_unlock_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Wake The Owl Bridge:**

**Runtime AI instruction:** Continue the story, then pause for a soft animal sound challenge.

**Example AI line:** "The fox finds a sleepy owl bridge. Can you make a quiet hoo-hoo?"

**Child responses:**

1. (Ideal) The child makes a soft owl sound or says a gentle hello to wake the bridge.
2. (Unexpected) Child shouts, switches animals, or talks about the bridge without trying the owl sound challenge.
3. (No response) Child stays at the sleepy owl bridge without making a sound or greeting.

**AI follow-up:**

1. Wake the owl bridge softly, narrate the fox crossing, and keep the sound saved.
2. Keep the sleepy-owl scene, lower the volume target, and offer "hoo-hoo" or "hello owl" as the two safe responses.
3. [wait 2s] Make one quiet "hoo-hoo" example, then ask the child to copy it or whisper hello.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `story_unlock_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Echo The Star Word:**

**Runtime AI instruction:** Continue to the final gate, then ask for one echo word.

**Example AI line:** "A star page asks for bonjour. Can you echo bonjour?"

**Child responses:**

1. (Ideal) The child echoes "bonjour" or tries a close pronunciation for the star page.
2. (Unexpected) Child answers with a different word, asks to skip the word gate, or treats the page as a quiz answer instead of an echo.
3. (No response) Child looks at the star-word page without repeating the word.

**AI follow-up:**

1. Let the star page glow, repeat the echoed word once in the story, and keep the word saved.
2. Stay in the final gate scene, say the target word again slowly, and accept a tiny echo attempt.
3. [wait 2s] Say "bon-jour" in two beats and invite the child to copy just one beat if needed.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `story_unlock_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the star-word echo challenge changed the Story Challenge Unlock board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Story Challenge Unlock payoff or ignores how the saved story unlock response turns connect.
3. (No response) Child watches the Story Challenge Unlock reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's story unlock response turns, name one concrete saved moment, and invite a short reflection.
2. Hold the Story Challenge Unlock reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Story Challenge Unlock board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Story Challenge Unlock moment, asks to play again, or watches the story challenge unlock recap badge.
2. (Unexpected) Child shifts topic before the recap names the story unlock response skill or Form and Perspective.
3. (No response) Child stays on the Story Challenge Unlock recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same imagine mechanic and the story challenge unlock frame.
2. Close Story Challenge Unlock first, name the practiced story unlock response, and then offer one next-round seed.
3. [wait 2s] Read the Story Challenge Unlock badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `imagine`, focal attribute `story_challenge_unlock`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
