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

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Capture The Color:**

**Runtime AI instruction:** Start from the child color before showing artworks.

**Example AI line:** "You found yellow. Let us open the art shelf for yellow pictures."

**Child responses:**

1. (Ideal) The child names or confirms the color.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Use the color as the artwork search key.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Meet The First Artwork:**

**Runtime AI instruction:** Show one approved artwork where the color is dominant and give a child-safe background note.

**Example AI line:** "This artwork uses yellow to feel bright and warm. What yellow part do you notice first?"

**Child responses:**

1. (Ideal) The child points or describes the color.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm visible color evidence and add one simple background note.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Compare More Art:**

**Runtime AI instruction:** Show another approved artwork with the same color and ask what feels same or different.

**Example AI line:** "Here is another yellow artwork. Does this yellow feel sunny, soft, or bold?"

**Child responses:**

1. (Ideal) The child chooses or describes a mood.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Connect the child color to several artworks.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `color_artwork_set_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `color_in_famous_art`, and next-step hint.
