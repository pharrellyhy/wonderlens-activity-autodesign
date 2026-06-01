## Children's Yoga

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Children's Yoga |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | language_expression (primary), observation, language expression |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

The AI guides a short, child-safe pose routine using animal or object metaphors.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `motion_voice` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Parent selects a calm movement routine and the child has enough space.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Children's Yoga starter cue, name the child as children's yoga player, and preview the first safe yoga pose turn.

**Example AI line:** "Children's Yoga starts now. You are the children's yoga player; I will help one child-safe yoga pose turn at a time."

**Child responses:**

1. (Ideal) The child accepts the children's yoga player role, notices the starter cue, or names something connected to the first child-safe pose.
2. (Unexpected) Child asks for another game, starts the safe sound or movement before the Children's Yoga mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Children's Yoga title/trigger card without taking the children's yoga player role yet.

**AI follow-up:**

1. Name the children's yoga player role, connect it to the starter cue, and preview the first safe sound or movement.
2. Acknowledge the request, return to the Children's Yoga promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Children's Yoga role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one child-safe yoga pose cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the safe sound or movement loop for Children's Yoga or asks for the easiest version.
2. (Unexpected) Child tries to skip the first child-safe pose, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Children's Yoga rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Children's Yoga loop as AI prompt, child safe sound or movement, saved token, and show the first response slot.
2. Keep the rule tied to the first child-safe pose, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Children's Yoga rule in one sentence and ask for yes, a point, or the first chance to try a safe sound or movement.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `childrens_yoga_pose_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If pose cards or motion safety rules are unavailable, block at Phase 0.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI guides a short, child-safe pose routine using animal or object metaphors. Ask the child to move or voice safely in the first small turn.

**Example AI line:** "Let us start: The AI guides a short, child-safe pose routine using animal or object metaphors. Try the first safe pose now."

**Child responses:**

1. (Ideal) The child tries the first child-safe pose with safe volume, space, or body control.
2. (Unexpected) Child makes the first child-safe pose too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the first child-safe pose cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the first child-safe pose, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the first child-safe pose.
3. [wait 2s] Demonstrate the smallest safe version of the first child-safe pose, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and child-safe yoga pose cue. Use `childrens_yoga_pose_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If pose cards or motion safety rules are unavailable, block at Phase 0.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second motion_voice turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child tries the second pose with a small variation with safe volume, space, or body control.
2. (Unexpected) Child makes the second pose with a small variation too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the second pose with a small variation cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the second pose with a small variation, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the second pose with a small variation.
3. [wait 2s] Demonstrate the smallest safe version of the second pose with a small variation, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and child-safe yoga pose cue. Use `childrens_yoga_pose_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If pose cards or motion safety rules are unavailable, block at Phase 0.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your child-safe yoga pose turns?"

**Child responses:**

1. (Ideal) The child tries the calm finish pose with safe volume, space, or body control.
2. (Unexpected) Child makes the calm finish pose too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the calm finish pose cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the calm finish pose, save the performance token, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the calm finish pose.
3. [wait 2s] Demonstrate the smallest safe version of the calm finish pose, then ask the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and child-safe yoga pose cue. Use `childrens_yoga_pose_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If pose cards or motion safety rules are unavailable, block at Phase 0.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your child-safe yoga pose turns are saved: we started Children's Yoga, practiced child-safe yoga pose, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the calm finish pose changed the Children's Yoga board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Children's Yoga payoff or ignores how the saved safe sound or movement turns connect.
3. (No response) Child watches the Children's Yoga reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's safe sound or movement turns, name one concrete saved token, and invite a short reflection.
2. Hold the Children's Yoga reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Children's Yoga board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Children's Yoga moment, asks to play again, or watches the childrens yoga recap badge.
2. (Unexpected) Child shifts topic before the recap names the safe sound or movement skill or Form and Perspective.
3. (No response) Child stays on the Children's Yoga recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same motion_voice mechanic and the childrens yoga frame.
2. Close Children's Yoga first, name the practiced safe sound or movement, and then offer one next-round seed.
3. [wait 2s] Read the Children's Yoga badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `motion_voice`, focal attribute `childrens_yoga`, and next-step hint.
