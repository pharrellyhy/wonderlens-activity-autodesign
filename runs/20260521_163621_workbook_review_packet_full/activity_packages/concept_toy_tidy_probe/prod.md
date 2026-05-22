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

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child veers away from "Transition Bridge" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Transition Bridge", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Transition Bridge".
3. [wait 2s] [gentle] Model one tiny sorting step for "Transition Bridge", then invite the child to copy or choose.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child veers away from "Role And Rules" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Role And Rules", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Role And Rules".
3. [wait 2s] [gentle] Model one tiny sorting step for "Role And Rules", then invite the child to copy or choose.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Agree To Tidy:**

**Runtime AI instruction:** Ask the child to accept a short tidy sprint.

**Example AI line:** "Toy Captain, are you ready for a two-minute tidy sprint?"

**Child responses:**

1. (Ideal) The child agrees or asks for a smaller task.
2. (Unexpected) Child veers away from "Agree To Tidy" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Agree To Tidy", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Start the mission and give one organizing tip.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Agree To Tidy".
3. [wait 2s] [gentle] Model one tiny sorting step for "Agree To Tidy", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 2 -- Sort One Group:**

**Runtime AI instruction:** Give a tip while the child physically tidies.

**Example AI line:** "Put one kind of toy together first: blocks, cars, dolls, or books. Which group will you move?"

**Child responses:**

1. (Ideal) The child names or moves a group.
2. (Unexpected) Child veers away from "Sort One Group" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Sort One Group", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Encourage the process without judging the room.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Sort One Group".
3. [wait 2s] [gentle] Model one tiny sorting step for "Sort One Group", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 3 -- Confirm After State:**

**Runtime AI instruction:** Ask for child or caregiver confirmation; do not infer cleanup from images.

**Example AI line:** "Time. What looks a little better now, or can you show the after picture?"

**Child responses:**

1. (Ideal) The child reports or shows the result.
2. (Unexpected) Child veers away from "Confirm After State" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Confirm After State", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Celebrate the tidy action without visual-verification claims.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Confirm After State".
3. [wait 2s] [gentle] Model one tiny sorting step for "Confirm After State", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child veers away from "Magic Moment" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Magic Moment", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Magic Moment".
3. [wait 2s] [gentle] Model one tiny sorting step for "Magic Moment", then invite the child to copy or choose.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child veers away from "Closing + IB Concepts" in Toy Tidy Challenge, skips the sorting action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Closing + IB Concepts", watches the current screen, or needs a first tiny sorting model.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate briefly, keep the Toy Tidy Challenge frame, and offer one safe choice that still completes "Closing + IB Concepts".
3. [wait 2s] [gentle] Model one tiny sorting step for "Closing + IB Concepts", then invite the child to copy or choose.

**Screen:** Recap badge lists title, mechanic `sort`, focal attribute `toy_tidy_challenge`, and next-step hint.
