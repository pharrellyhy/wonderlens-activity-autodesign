## Tiny Curator

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Tiny Curator |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | classification (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `sort` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child is at home or outdoors with several objects that can be grouped or compared.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Tiny Curator starter cue, name the child as tiny curator player, and preview the first sorting move turn.

**Example AI line:** "Tiny Curator starts now. You are the tiny curator player; I will help one curator sorting turn at a time."

**Child responses:**

1. (Ideal) The child accepts the tiny curator player role, notices the starter cue, or names something connected to the first exhibition object.
2. (Unexpected) Child asks for another game, starts the sorting move before the Tiny Curator mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Tiny Curator title/trigger card without taking the tiny curator player role yet.

**AI follow-up:**

1. Name the tiny curator player role, connect it to the starter cue, and preview the first sorting move.
2. Acknowledge the request, return to the Tiny Curator promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Tiny Curator role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one curator sorting cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the sorting move loop for Tiny Curator or asks for the easiest version.
2. (Unexpected) Child tries to skip the first exhibition object, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Tiny Curator rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Tiny Curator loop as AI prompt, child sorting move, saved token, and show the first response slot.
2. Keep the rule tied to the first exhibition object, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Tiny Curator rule in one sentence and ask for yes, a point, or the first chance to place one item by the rule.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the active curator sorting cue.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule. Ask the child to group or organize in the first small turn.

**Example AI line:** "Let us start: The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule. Try the first curator sorting move now."

**Child responses:**

1. (Ideal) The child places or names an item according to the first exhibition object rule.
2. (Unexpected) Child mixes rules for the first exhibition object, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the first exhibition object without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the first exhibition object.
3. [wait 2s] Model placing one item by the first exhibition object rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and curator sorting cue. No prebuilt asset is required; show progress tokens and the active curator sorting cue.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second sort turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child places or names an item according to the second or third grouped object rule.
2. (Unexpected) Child mixes rules for the second or third grouped object, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the second or third grouped object without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the second or third grouped object.
3. [wait 2s] Model placing one item by the second or third grouped object rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and curator sorting cue. No prebuilt asset is required; show progress tokens and the active curator sorting cue.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your curator sorting turns?"

**Child responses:**

1. (Ideal) The child places or names an item according to the exhibit rule explanation rule.
2. (Unexpected) Child mixes rules for the exhibit rule explanation, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the exhibit rule explanation without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the exhibit rule explanation.
3. [wait 2s] Model placing one item by the exhibit rule explanation rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and curator sorting cue. No prebuilt asset is required; show progress tokens and the active curator sorting cue.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your curator sorting turns are saved: we started Tiny Curator, practiced curator sorting, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the exhibit rule explanation changed the Tiny Curator board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Tiny Curator payoff or ignores how the saved sorting move turns connect.
3. (No response) Child watches the Tiny Curator reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's sorting move turns, name one concrete saved token, and invite a short reflection.
2. Hold the Tiny Curator reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Tiny Curator board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Tiny Curator moment, asks to play again, or watches the tiny curator recap badge.
2. (Unexpected) Child shifts topic before the recap names the sorting move skill or Form.
3. (No response) Child stays on the Tiny Curator recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same sort mechanic and the tiny curator frame.
2. Close Tiny Curator first, name the practiced sorting move, and then offer one next-round seed.
3. [wait 2s] Read the Tiny Curator badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `tiny_curator`, and next-step hint.
