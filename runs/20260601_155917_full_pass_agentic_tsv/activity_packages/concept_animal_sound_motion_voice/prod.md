## Animal Sound Imitation

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Animal Sound Imitation |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | language_expression (primary), observation, language expression |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `motion_voice` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child photographs an animal toy, animal picture, or enters animal-sound mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Animal Sound Imitation starter cue, name the child as animal voice performer, and preview the first animal sound or animal-role voice turn.

**Example AI line:** "Animal Sound Imitation starts now. You are the animal voice performer; I will help one animal sound turn at a time."

**Child responses:**

1. (Ideal) The child accepts the animal voice performer role, notices the starter cue, or names something connected to the first animal voice.
2. (Unexpected) Child asks for another game, starts the safe sound or movement before the Animal Sound Imitation mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Animal Sound Imitation title/trigger card without taking the animal voice performer role yet.

**AI follow-up:**

1. Name the animal voice performer role, connect it to the starter cue, and preview the first safe sound or movement.
2. Acknowledge the request, return to the Animal Sound Imitation promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Animal Sound Imitation role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one animal sound cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the safe sound or movement loop for Animal Sound Imitation or asks for the easiest version.
2. (Unexpected) Child tries to skip the first animal voice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Animal Sound Imitation rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Animal Sound Imitation loop as AI prompt, child safe sound or movement, saved token, and show the first response slot.
2. Keep the rule tied to the first animal voice, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Animal Sound Imitation rule in one sentence and ask for yes, a point, or the first chance to try a safe sound or movement.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `animal_sound_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role. Ask the child to move or voice safely in the first small turn.

**Example AI line:** "Let us start: The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role. Try the first animal sound now."

**Child responses:**

1. (Ideal) The child tries the first animal voice with safe volume, space, or body control.
2. (Unexpected) Child makes the first animal voice too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the first animal voice cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the first animal voice, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the first animal voice.
3. [wait 2s] Demonstrate the smallest safe version of the first animal voice, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and animal sound cue. Use `animal_sound_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second motion_voice turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child tries the changed animal voice or volume with safe volume, space, or body control.
2. (Unexpected) Child makes the changed animal voice or volume too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the changed animal voice or volume cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the changed animal voice or volume, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the changed animal voice or volume.
3. [wait 2s] Demonstrate the smallest safe version of the changed animal voice or volume, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and animal sound cue. Use `animal_sound_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your animal sound turns?"

**Child responses:**

1. (Ideal) The child tries the favorite animal-role line with safe volume, space, or body control.
2. (Unexpected) Child makes the favorite animal-role line too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the favorite animal-role line cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the favorite animal-role line, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the favorite animal-role line.
3. [wait 2s] Demonstrate the smallest safe version of the favorite animal-role line, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and animal sound cue. Use `animal_sound_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your animal sound turns are saved: we started Animal Sound Imitation, practiced animal sound, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the favorite animal-role line changed the Animal Sound Imitation board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Animal Sound Imitation payoff or ignores how the saved safe sound or movement turns connect.
3. (No response) Child watches the Animal Sound Imitation reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's safe sound or movement turns, name one concrete saved token, and invite a short reflection.
2. Hold the Animal Sound Imitation reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Animal Sound Imitation board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Animal Sound Imitation moment, asks to play again, or watches the animal sound imitation recap badge.
2. (Unexpected) Child shifts topic before the recap names the safe sound or movement skill or Form and Perspective.
3. (No response) Child stays on the Animal Sound Imitation recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same motion_voice mechanic and the animal sound imitation frame.
2. Close Animal Sound Imitation first, name the practiced safe sound or movement, and then offer one next-round seed.
3. [wait 2s] Read the Animal Sound Imitation badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `motion_voice`, focal attribute `animal_sound_imitation`, and next-step hint.
