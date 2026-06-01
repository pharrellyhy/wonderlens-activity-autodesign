## Toy Tidy Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Toy Tidy Challenge |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | classification (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child starts from a toy-area photo, agrees to a short tidy mission, receives tips during the timer, and confirms the after state.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `sort` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A toy area becomes a two-minute tidy sprint with child or caregiver confirmation.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Toy Tidy Challenge. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the toy tidy challenge player role, notices the starter cue, or names something connected to the first tiny tidy target.
2. (Unexpected) Child asks for another game, starts the sorting move before the Toy Tidy Challenge mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Toy Tidy Challenge title/trigger card without taking the toy tidy challenge player role yet.

**AI follow-up:**

1. Name the toy tidy challenge player role, connect it to the starter cue, and preview the first sorting move.
2. Acknowledge the request, return to the Toy Tidy Challenge promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Toy Tidy Challenge role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the sorting move loop for Toy Tidy Challenge or asks for the easiest version.
2. (Unexpected) Child tries to skip the first tiny tidy target, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Toy Tidy Challenge rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Toy Tidy Challenge loop as AI prompt, child sorting move, saved token, and show the first response slot.
2. Keep the rule tied to the first tiny tidy target, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Toy Tidy Challenge rule in one sentence and ask for yes, a point, or the first chance to place one item by the rule.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Agree To Tidy:**

**Runtime AI instruction:** Ask the child to accept a short tidy sprint.

**Example AI line:** "Toy Captain, are you ready for a two-minute tidy sprint?"

**Child responses:**

1. (Ideal) The child places or names an item according to the first tiny tidy target rule.
2. (Unexpected) Child mixes rules for the first tiny tidy target, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the first tiny tidy target without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the first tiny tidy target.
3. [wait 2s] Model placing one item by the first tiny tidy target rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Sort One Group:**

**Runtime AI instruction:** Give a tip while the child physically tidies.

**Example AI line:** "Put one kind of toy together first: blocks, cars, dolls, or books. Which group will you move?"

**Child responses:**

1. (Ideal) The child places or names an item according to the timer tip during the mission rule.
2. (Unexpected) Child mixes rules for the timer tip during the mission, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the timer tip during the mission without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the timer tip during the mission.
3. [wait 2s] Model placing one item by the timer tip during the mission rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Confirm After State:**

**Runtime AI instruction:** Ask for child or caregiver confirmation; do not infer cleanup from images.

**Example AI line:** "Time. What looks a little better now, or can you show the after picture?"

**Child responses:**

1. (Ideal) The child places or names an item according to the after-state confirmation rule.
2. (Unexpected) Child mixes rules for the after-state confirmation, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the after-state confirmation without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the after-state confirmation.
3. [wait 2s] Model placing one item by the after-state confirmation rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the after-state confirmation changed the Toy Tidy Challenge board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Toy Tidy Challenge payoff or ignores how the saved sorting move turns connect.
3. (No response) Child watches the Toy Tidy Challenge reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's sorting move turns, name one concrete saved token, and invite a short reflection.
2. Hold the Toy Tidy Challenge reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Toy Tidy Challenge board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Toy Tidy Challenge moment, asks to play again, or watches the toy tidy challenge recap badge.
2. (Unexpected) Child shifts topic before the recap names the sorting move skill or Form.
3. (No response) Child stays on the Toy Tidy Challenge recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same sort mechanic and the toy tidy challenge frame.
2. Close Toy Tidy Challenge first, name the practiced sorting move, and then offer one next-round seed.
3. [wait 2s] Read the Toy Tidy Challenge badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `toy_tidy_challenge`, and next-step hint.
