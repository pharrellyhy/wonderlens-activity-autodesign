## Story Challenge Unlock

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Story Challenge Unlock |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Perspective and Connection |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | imagination (inventing details), narrative expression (building story beats), language expression (naming and explaining) |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

A story pauses at a locked gate, the child invents a key action and one sensory detail, and the next scene opens from that imagined contribution rather than a generic unlock effect.

**2. Educational Purpose (KUD)**

- **K (Know):** A story can pause for a small challenge, and the child's idea can unlock the next beat.
- **U (Understand):** Connection links the challenge answer to the story path, and Perspective lets the child choose how the character continues.
- **D (Do):** Pick the challenge response, add an imagination detail, and choose the next scene direction.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `story_unlock_cards_01` in `center_card_area`; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.

**4. Typical Scenario**

Trigger: A child is in a story mode and reaches a door, bridge, or path marker. The AI uses the child's spoken idea as the unlock evidence and avoids claiming persistent UI state when the fallback is voice-only.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a story challenge unlock mission. You are the Story Key Maker. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Story Key Maker rule: choose which path the character tries. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `story_unlock_cards_01` in `center_card_area`; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Pick the story door:**

**AI says:** [round-1 guide] "Round 1: choose which path the character tries."

**Child responses:**

1. (Ideal) "The moon door."
2. (Unexpected) "Both doors explode."
3. (No response) Child waits

**AI follow-up:**

1. [specific] "Moon door chosen. It glows because you picked it."
2. [redirect] "Let us keep it safe and playful: moon door or forest door."
3. [wait 2s] [gentle hint] "Point to one door or say moon."

**Screen:** If `story_unlock_cards_01` is available, show two safe door cards. Fallback: voice-only door choices with no card claim. State chip records chosen path when supported.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 2 -- Make the unlock action:**

**AI says:** [round-2 guide] "Round 2: say a magic word, gesture, or tiny answer to help the character."

**Child responses:**

1. (Ideal) "Shine, moon!"
2. (Unexpected) Child gives unrelated noise
3. (No response) No response

**AI follow-up:**

1. [specific] "That word becomes the story key."
2. [redirect] "Funny sound. Now make it a helper word for the door."
3. [wait 2s] [gentle hint] "Try: shine, moon."

**Screen:** Door card changes to half-open only if state is supported; otherwise voice narration says it creaks open.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 3 -- Choose what happens next:**

**AI says:** [round-3 guide] "Round 3: choose the first thing seen after the door opens."

**Child responses:**

1. (Ideal) "A tiny owl."
2. (Unexpected) Wants scary monster
3. (No response) Child says "I do not know"

**AI follow-up:**

1. [specific] "Tiny owl joins the next scene."
2. [redirect] "Let us keep it friendly: owl, star path, or sleepy fox."
3. [wait 2s] [gentle hint] "Pick owl or star path."

**Screen:** If cards are available, the next-scene card appears. Fallback: voice-only scene reveal with no card claim. Progress trail shows choice -> action -> scene when state is supported.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a next story scene unlocked by the child's imagined action. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Story Challenge Unlock: a next story scene unlocked by the child's imagined action. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Perspective and Connection today. You used your own imagine action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Story Key Maker badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `story_unlock`, asset/fallback note when relevant, and one next-step hint.
