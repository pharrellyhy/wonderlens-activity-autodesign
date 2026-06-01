## Color In Famous Art

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Color In Famous Art |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | counting (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child photographs or names a real-world color, then sees several approved artworks where that color is dominant or important.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `enumerate` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A photographed yellow, blue, red, or green object becomes the bridge to rights-cleared artworks with matching color metadata.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Color In Famous Art. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the color in famous art player role, notices the starter cue, or names something connected to the real-world color sample.
2. (Unexpected) Child asks for another game, starts the counting or naming step before the Color In Famous Art mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Color In Famous Art title/trigger card without taking the color in famous art player role yet.

**AI follow-up:**

1. Name the color in famous art player role, connect it to the starter cue, and preview the first counting or naming step.
2. Acknowledge the request, return to the Color In Famous Art promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Color In Famous Art role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the counting or naming step loop for Color In Famous Art or asks for the easiest version.
2. (Unexpected) Child tries to skip the real-world color sample, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Color In Famous Art rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Color In Famous Art loop as AI prompt, child counting or naming step, saved token, and show the first response slot.
2. Keep the rule tied to the real-world color sample, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Color In Famous Art rule in one sentence and ask for yes, a point, or the first chance to count or name the target set.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Capture The Color:**

**Runtime AI instruction:** Start from the child color before showing artworks.

**Example AI line:** "You found yellow. Let us open the art shelf for yellow pictures."

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the real-world color sample.
2. (Unexpected) Child guesses the real-world color sample without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the real-world color sample display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the real-world color sample, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the real-world color sample, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.

**Round 2 -- Meet The First Artwork:**

**Runtime AI instruction:** Show one approved artwork where the color is dominant and give a child-safe background note.

**Example AI line:** "This artwork uses yellow to feel bright and warm. What yellow part do you notice first?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the artwork where the color appears.
2. (Unexpected) Child guesses the artwork where the color appears without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the artwork where the color appears display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the artwork where the color appears, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the artwork where the color appears, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.

**Round 3 -- Compare More Art:**

**Runtime AI instruction:** Show another approved artwork with the same color and ask what feels same or different.

**Example AI line:** "Here is another yellow artwork. Does this yellow feel sunny, soft, or bold?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the favorite use of that color.
2. (Unexpected) Child guesses the favorite use of that color without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the favorite use of that color display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the favorite use of that color, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the favorite use of that color, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the favorite use of that color changed the Color In Famous Art board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Color In Famous Art payoff or ignores how the saved counting or naming step turns connect.
3. (No response) Child watches the Color In Famous Art reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's counting or naming step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Color In Famous Art reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Color In Famous Art board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Color In Famous Art moment, asks to play again, or watches the color in famous art recap badge.
2. (Unexpected) Child shifts topic before the recap names the counting or naming step skill or Form.
3. (No response) Child stays on the Color In Famous Art recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same enumerate mechanic and the color in famous art frame.
2. Close Color In Famous Art first, name the practiced counting or naming step, and then offer one next-round seed.
3. [wait 2s] Read the Color In Famous Art badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `color_in_famous_art`, and next-step hint.
