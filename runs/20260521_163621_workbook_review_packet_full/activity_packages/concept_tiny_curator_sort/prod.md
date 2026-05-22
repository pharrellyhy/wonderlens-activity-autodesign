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

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Tiny Curator. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child veers away from "Transition Bridge" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Transition Bridge", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Transition Bridge".
3. [wait 2s] [gentle] Model one tiny sorting step for "Transition Bridge", then invite the child to copy or choose.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child veers away from "Role And Rules" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Role And Rules", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Role And Rules".
3. [wait 2s] [gentle] Model one tiny sorting step for "Role And Rules", then invite the child to copy or choose.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule.. Ask the child to group or organize in the first small turn.

**Example AI line:** "Let us start: The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule. What is your first try?"

**Child responses:**

1. (Ideal) The child gives the first source-aligned action.
2. (Unexpected) Child veers away from "Start The Source Action" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Start The Source Action", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Confirm the action and name how it matches the source rule.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Start The Source Action".
3. [wait 2s] [gentle] Model one tiny sorting step for "Start The Source Action", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second sort turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child repeats the same mechanic with a variation.
2. (Unexpected) Child veers away from "Repeat With A Variation" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Repeat With A Variation", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Connect the variation back to the same play frame.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Repeat With A Variation".
3. [wait 2s] [gentle] Model one tiny sorting step for "Repeat With A Variation", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child recaps or reacts.
2. (Unexpected) Child veers away from "Complete The Loop" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Complete The Loop", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Summarize the child action and source-specific payoff.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Complete The Loop".
3. [wait 2s] [gentle] Model one tiny sorting step for "Complete The Loop", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child veers away from "Magic Moment" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Magic Moment", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Magic Moment".
3. [wait 2s] [gentle] Model one tiny sorting step for "Magic Moment", then invite the child to copy or choose.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child veers away from "Closing + IB Concepts" in Tiny Curator, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Closing + IB Concepts", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate briefly, keep the Tiny Curator frame, and offer one safe choice that still completes "Closing + IB Concepts".
3. [wait 2s] [gentle] Model one tiny sorting step for "Closing + IB Concepts", then invite the child to copy or choose.

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `tiny_curator`, and next-step hint.
