## Art Critic Tournament

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Art Critic Tournament |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | observation (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child compares two approved artworks at a time, chooses a favorite, and keeps the winner moving until a final favorite wins.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `compare` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Two rights-cleared artworks appear side by side each round and the child decides which one continues.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Art Critic Tournament. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the art critic tournament player role, notices the starter cue, or names something connected to the first artwork match.
2. (Unexpected) Child asks for another game, starts the comparison choice before the Art Critic Tournament mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Art Critic Tournament title/trigger card without taking the art critic tournament player role yet.

**AI follow-up:**

1. Name the art critic tournament player role, connect it to the starter cue, and preview the first comparison choice.
2. Acknowledge the request, return to the Art Critic Tournament promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Art Critic Tournament role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the comparison choice loop for Art Critic Tournament or asks for the easiest version.
2. (Unexpected) Child tries to skip the first artwork match, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Art Critic Tournament rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Art Critic Tournament loop as AI prompt, child comparison choice, saved token, and show the first response slot.
2. Keep the rule tied to the first artwork match, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Art Critic Tournament rule in one sentence and ask for yes, a point, or the first chance to compare the visible options.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Match 1:**

**Runtime AI instruction:** Show two approved artworks and ask which one should stay.

**Example AI line:** "Which artwork wins this match: the left picture or the right picture?"

**Child responses:**

1. (Ideal) The child compares the visible options for the first artwork match and chooses or explains one.
2. (Unexpected) Child responds to only one side of the first artwork match, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the first artwork match options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the first artwork match, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the first artwork match, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Match 2:**

**Runtime AI instruction:** Bring in a new challenger against the current winner.

**Example AI line:** "Your winner meets a new artwork. Which one should continue?"

**Child responses:**

1. (Ideal) The child compares the visible options for the new challenger match and chooses or explains one.
2. (Unexpected) Child responds to only one side of the new challenger match, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the new challenger match options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the new challenger match, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the new challenger match, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Match 3:**

**Runtime AI instruction:** Repeat with another approved challenger.

**Example AI line:** "Look at color, shape, or feeling. Which artwork wins this round?"

**Child responses:**

1. (Ideal) The child compares the visible options for the color, shape, or feeling criterion and chooses or explains one.
2. (Unexpected) Child responds to only one side of the color, shape, or feeling criterion, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the color, shape, or feeling criterion options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the color, shape, or feeling criterion, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the color, shape, or feeling criterion, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 4 -- Match 4:**

**Runtime AI instruction:** Continue the tournament with child-led criteria.

**Example AI line:** "This is the semifinal. Which picture do you want to keep?"

**Child responses:**

1. (Ideal) The child compares the visible options for the semifinal keep-or-release choice and chooses or explains one.
2. (Unexpected) Child responds to only one side of the semifinal keep-or-release choice, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the semifinal keep-or-release choice options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the semifinal keep-or-release choice, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the semifinal keep-or-release choice, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 5 -- Final Match:**

**Runtime AI instruction:** Show the final comparison and declare the winner.

**Example AI line:** "Final round. Which artwork becomes your champion?"

**Child responses:**

1. (Ideal) The child compares the visible options for the final champion choice and chooses or explains one.
2. (Unexpected) Child responds to only one side of the final champion choice, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the final champion choice options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the final champion choice, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the final champion choice, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `artwork_tournament_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-5; fallback: If the artwork set or tournament state is unavailable, block at Phase 0.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final champion choice changed the Art Critic Tournament board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Art Critic Tournament payoff or ignores how the saved comparison choice turns connect.
3. (No response) Child watches the Art Critic Tournament reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's comparison choice turns, name one concrete saved token, and invite a short reflection.
2. Hold the Art Critic Tournament reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Art Critic Tournament board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Art Critic Tournament moment, asks to play again, or watches the art critic tournament recap badge.
2. (Unexpected) Child shifts topic before the recap names the comparison choice skill or Form and Perspective.
3. (No response) Child stays on the Art Critic Tournament recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same compare mechanic and the art critic tournament frame.
2. Close Art Critic Tournament first, name the practiced comparison choice, and then offer one next-round seed.
3. [wait 2s] Read the Art Critic Tournament badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `compare`, focal attribute `art_critic_tournament`, and next-step hint.
