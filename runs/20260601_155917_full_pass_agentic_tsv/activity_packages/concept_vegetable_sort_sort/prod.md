## Vegetable Sort

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Vegetable Sort |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | classification (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `sort` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Screen can show vegetable cards or a child photographs several vegetables.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Vegetable Sort starter cue, name the child as vegetable sorter, and preview the first vegetable sorting turn.

**Example AI line:** "Vegetable Sort starts now. You are the vegetable sorter; I will help one vegetable sorting turn at a time."

**Child responses:**

1. (Ideal) The child accepts the vegetable sorter role, notices the starter cue, or names something connected to the first vegetable group.
2. (Unexpected) Child asks for another game, starts the sorting move before the Vegetable Sort mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Vegetable Sort title/trigger card without taking the vegetable sorter role yet.

**AI follow-up:**

1. Name the vegetable sorter role, connect it to the starter cue, and preview the first sorting move.
2. Acknowledge the request, return to the Vegetable Sort promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Vegetable Sort role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one vegetable sorting cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the sorting move loop for Vegetable Sort or asks for the easiest version.
2. (Unexpected) Child tries to skip the first vegetable group, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Vegetable Sort rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Vegetable Sort loop as AI prompt, child sorting move, saved token, and show the first response slot.
2. Keep the rule tied to the first vegetable group, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Vegetable Sort rule in one sentence and ask for yes, a point, or the first chance to place one item by the rule.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `vegetable_sort_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule. Ask the child to group or organize in the first small turn.

**Example AI line:** "Let us start: The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule. Try the first vegetable sort now."

**Child responses:**

1. (Ideal) The child places or names an item according to the first vegetable group rule.
2. (Unexpected) Child mixes rules for the first vegetable group, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the first vegetable group without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the first vegetable group.
3. [wait 2s] Model placing one item by the first vegetable group rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and vegetable sorting cue. Use `vegetable_sort_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown.

**Round 2 -- Repeat With A Variation:**

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

**Screen:** Shows the active round token, child response slot, and vegetable sorting cue. Use `vegetable_sort_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your vegetable sorting turns?"

**Child responses:**

1. (Ideal) The child places or names an item according to the final sorting rule explanation rule.
2. (Unexpected) Child mixes rules for the final sorting rule explanation, sorts by an invisible reason, or moves items without naming a grouping idea.
3. (No response) Child looks at the items for the final sorting rule explanation without placing or naming one group.

**AI follow-up:**

1. Name the grouping rule the child used, keep that group visible, and ask for the next item or rule check.
2. Hold the current groups still, compare two possible rules, and ask which one controls the final sorting rule explanation.
3. [wait 2s] Model placing one item by the final sorting rule explanation rule, then ask the child to place or name one more.

**Screen:** Shows the active round token, child response slot, and vegetable sorting cue. Use `vegetable_sort_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your vegetable sorting turns are saved: we started Vegetable Sort, practiced vegetable sorting, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the final sorting rule explanation changed the Vegetable Sort board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Vegetable Sort payoff or ignores how the saved sorting move turns connect.
3. (No response) Child watches the Vegetable Sort reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's sorting move turns, name one concrete saved token, and invite a short reflection.
2. Hold the Vegetable Sort reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Vegetable Sort board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

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

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `vegetable_sort`, and next-step hint.
