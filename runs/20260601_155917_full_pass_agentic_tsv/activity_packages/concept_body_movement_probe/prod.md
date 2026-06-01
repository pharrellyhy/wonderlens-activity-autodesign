## Simple Body Movement Guide

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Simple Body Movement Guide |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | language_expression (primary), observation, language expression |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

The AI guides one simple body movement at a time with safety limits.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `motion_voice` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Parent starts a short movement prompt and the child has enough space.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Simple Body Movement Guide. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the simple body movement guide player role, notices the starter cue, or names something connected to the first safe movement.
2. (Unexpected) Child asks for another game, starts the safe sound or movement before the Simple Body Movement Guide mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Simple Body Movement Guide title/trigger card without taking the simple body movement guide player role yet.

**AI follow-up:**

1. Name the simple body movement guide player role, connect it to the starter cue, and preview the first safe sound or movement.
2. Acknowledge the request, return to the Simple Body Movement Guide promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Simple Body Movement Guide role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the safe sound or movement loop for Simple Body Movement Guide or asks for the easiest version.
2. (Unexpected) Child tries to skip the first safe movement, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Simple Body Movement Guide rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Simple Body Movement Guide loop as AI prompt, child safe sound or movement, saved token, and show the first response slot.
2. Keep the rule tied to the first safe movement, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Simple Body Movement Guide rule in one sentence and ask for yes, a point, or the first chance to try a safe sound or movement.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `body_movement_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If movement cards or safety gating are unavailable, block at Phase 0.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI guides one simple body movement at a time with safety limits. Ask the child to move or voice safely in the first small turn.

**Example AI line:** "Let us start: The AI guides one simple body movement at a time with safety limits. What is your first try?"

**Child responses:**

1. (Ideal) The child tries the first safe movement with safe volume, space, or body control.
2. (Unexpected) Child makes the first safe movement too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the first safe movement cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the first safe movement, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the first safe movement.
3. [wait 2s] Demonstrate the smallest safe version of the first safe movement, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `body_movement_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If movement cards or safety gating are unavailable, block at Phase 0.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second motion_voice turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child tries the changed speed or size movement with safe volume, space, or body control.
2. (Unexpected) Child makes the changed speed or size movement too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the changed speed or size movement cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the changed speed or size movement, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the changed speed or size movement.
3. [wait 2s] Demonstrate the smallest safe version of the changed speed or size movement, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `body_movement_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If movement cards or safety gating are unavailable, block at Phase 0.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child tries the movement recap with safe volume, space, or body control.
2. (Unexpected) Child makes the movement recap too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the movement recap cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the movement recap, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the movement recap.
3. [wait 2s] Demonstrate the smallest safe version of the movement recap, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `body_movement_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If movement cards or safety gating are unavailable, block at Phase 0.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the movement recap changed the Simple Body Movement Guide board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Simple Body Movement Guide payoff or ignores how the saved safe sound or movement turns connect.
3. (No response) Child watches the Simple Body Movement Guide reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's safe sound or movement turns, name one concrete saved token, and invite a short reflection.
2. Hold the Simple Body Movement Guide reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Simple Body Movement Guide board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Simple Body Movement Guide moment, asks to play again, or watches the simple body movement recap badge.
2. (Unexpected) Child shifts topic before the recap names the safe sound or movement skill or Form and Perspective.
3. (No response) Child stays on the Simple Body Movement Guide recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same motion_voice mechanic and the simple body movement frame.
2. Close Simple Body Movement Guide first, name the practiced safe sound or movement, and then offer one next-round seed.
3. [wait 2s] Read the Simple Body Movement Guide badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `motion_voice`, focal attribute `simple_body_movement`, and next-step hint.
