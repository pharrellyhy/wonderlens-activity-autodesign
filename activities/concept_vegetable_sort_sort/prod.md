# Vegetable Sort

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Vegetable Sort |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | classification, observation, language_expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child uses tap/select vegetable cards to sort by a visible or meaningful rule such as color, shape, edible part, or cooking use.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Vegetable Sort.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `sort` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Vegetable Sort with vegetable_sort as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Vegetable Sort. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the vegetable sorter role, notices the starter cue, or names something connected to the first vegetable group.
2. (Unexpected) Child asks for another game, starts the sorting move before the Vegetable Sort mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Vegetable Sort opening moment without taking the vegetable sorter role yet.

**AI follow-up:**

1. Name the vegetable sorter role, connect it to the starter cue, and preview the first sorting move.
2. Acknowledge the request, return to the Vegetable Sort promise, and offer the smallest supported first action.
3. [wait 2s] Name the Vegetable Sort role and the first vegetable group, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I invite a turn, you try the activity action, and we save your idea for each turn."

**Child responses:**

1. (Ideal) The child agrees to the sorting move loop for Vegetable Sort or asks for the easiest version.
2. (Unexpected) Child tries to skip the first vegetable group, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Vegetable Sort rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Vegetable Sort loop as AI prompt, child sorting move, saved idea, and show the first response slot.
2. Keep the rule tied to the first vegetable group, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Vegetable Sort rule in one sentence and ask for a yes or the first chance to place one item by the rule.

**Screen:** Shows the rule strip, current round token, and tap/select vegetable cards. Use `round_1_scene` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching group. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Color Basket Sort:**

**Runtime AI instruction:** Preserve the workbook promise: the child sorts the vegetables by a visible or meaningful rule. Invite the child to group or organize the vegetables in the first small turn.

**Example AI line:** "Let us start by sorting these vegetables by a rule we can see. Which ones would you like to group together first?"

**Child responses:**

1. (Ideal) The child places or names an item according to the first vegetable group rule.
2. (Unexpected) Child mixes rules for the first vegetable group, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the first vegetable group without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the first vegetable group.
3. [wait 2s] Model placing one item by the first vegetable group rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and tap/select vegetable cards. Use `round_1_scene` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching group. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Shape Or Edible Part Basket Sort:**

**Runtime AI instruction:** Keep the same source frame and ask for a second sort turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child places or names an item according to the new sorting rule rule.
2. (Unexpected) Child mixes rules for the new sorting rule, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the new sorting rule without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the new sorting rule.
3. [wait 2s] Model placing one item by the new sorting rule rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and tap/select vegetable cards. Use `round_1_scene` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching group. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Cooking Use Or Child-Chosen Basket Rule:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What changed after your turns, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child places or names an item according to the final sorting rule explanation rule.
2. (Unexpected) Child mixes rules for the final sorting rule explanation, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the final sorting rule explanation without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the final sorting rule explanation.
3. [wait 2s] Model placing one item by the final sorting rule explanation rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and tap/select vegetable cards. Use `round_1_scene` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching group. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final sorting rule explanation changed the Vegetable Sort board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Vegetable Sort payoff or ignores how the saved sorting move turns connect.
3. (No response) Child watches the Vegetable Sort reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's sorting move turns, name one concrete saved idea, and invite a short reflection.
2. Hold the Vegetable Sort reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Vegetable Sort board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Vegetable Sort moment, asks to play again, or watches the vegetable sort recap badge.
2. (Unexpected) Child shifts topic before the recap names the sorting move skill or Form.
3. (No response) Child stays on the Vegetable Sort recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same sort mechanic and the vegetable sort frame.
2. Close Vegetable Sort first, name the practiced sorting move, and then offer one next-round seed.
3. [wait 2s] Read the Vegetable Sort badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `vegetable_sort`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
