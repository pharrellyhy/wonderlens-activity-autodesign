## Scavenger Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Scavenger Hunt |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | evidence_collection (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

Find several things that share a color, shape, or category.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `collect` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child photographs an object with a clear color, shape, or category feature.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Scavenger Hunt. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the scavenger hunt player role, notices the starter cue, or names something connected to the first matching object.
2. (Unexpected) Child asks for another game, starts the matching-item hunt before the Scavenger Hunt mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Scavenger Hunt title/trigger card without taking the scavenger hunt player role yet.

**AI follow-up:**

1. Name the scavenger hunt player role, connect it to the starter cue, and preview the first matching-item hunt.
2. Acknowledge the request, return to the Scavenger Hunt promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Scavenger Hunt role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the matching-item hunt loop for Scavenger Hunt or asks for the easiest version.
2. (Unexpected) Child tries to skip the first matching object, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Scavenger Hunt rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Scavenger Hunt loop as AI prompt, child matching-item hunt, saved token, and show the first response slot.
2. Keep the rule tied to the first matching object, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Scavenger Hunt rule in one sentence and ask for yes, a point, or the first chance to find or show one match.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: Find several things that share a color, shape, or category. Ask the child to find or match in the first small turn.

**Example AI line:** "Let us start: Find several things that share a color, shape, or category. What is your first try?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the first matching object and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the first matching object, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the first matching object but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the first matching object, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the first matching object.
3. [wait 2s] Give one concrete example that would count for the first matching object, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second collect turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the second object from the same rule and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the second object from the same rule, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the second object from the same rule but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the second object from the same rule, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the second object from the same rule.
3. [wait 2s] Give one concrete example that would count for the second object from the same rule, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the collection rule recap and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the collection rule recap, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the collection rule recap but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the collection rule recap, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the collection rule recap.
3. [wait 2s] Give one concrete example that would count for the collection rule recap, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the collection rule recap changed the Scavenger Hunt board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Scavenger Hunt payoff or ignores how the saved matching-item hunt turns connect.
3. (No response) Child watches the Scavenger Hunt reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's matching-item hunt turns, name one concrete saved token, and invite a short reflection.
2. Hold the Scavenger Hunt reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Scavenger Hunt board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Connection. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Scavenger Hunt moment, asks to play again, or watches the scavenger hunt recap badge.
2. (Unexpected) Child shifts topic before the recap names the matching-item hunt skill or Form and Connection.
3. (No response) Child stays on the Scavenger Hunt recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same collect mechanic and the scavenger hunt frame.
2. Close Scavenger Hunt first, name the practiced matching-item hunt, and then offer one next-round seed.
3. [wait 2s] Read the Scavenger Hunt badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `collect`, focal attribute `scavenger_hunt`, and next-step hint.
