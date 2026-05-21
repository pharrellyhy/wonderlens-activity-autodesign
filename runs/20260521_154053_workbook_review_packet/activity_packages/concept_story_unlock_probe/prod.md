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

The AI tells a fixed adventure story, pauses at challenge gates, and asks the child to complete a small task so the next story beat can continue.

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

**AI says:** [warm invitation] "I have a tiny adventure story. You are the Story Key Maker. When the story pauses, your quick challenge unlocks the next page. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will tell the first story beat, then pause for your key challenge."
2. [flexible] "I can make it smaller. You can answer with one word, one sound, or one quick find."
3. [wait 2s] [gentle] "I will start the story, and you can help when it pauses."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Story Key Maker rule: listen to the story first. When I pause at a gate, do the little challenge, and I will continue the next story beat."

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

**Round 1 -- Unlock The Moon Door:**

**AI says:** [storyteller tone] "The little fox reaches a moon door in the quiet forest. The door whispers, 'Show me a moon color before I open.' Can you name or show something silver, white, or blue?"

**Child responses:**

1. (Ideal) "Silver." / shows a blue or white object.
2. (Unexpected) "Both doors explode."
3. (No response) Child waits

**AI follow-up:**

1. [specific] "Silver is a moon color. The moon door opens, and the fox steps onto a glowing path."
2. [redirect] "Let us keep it safe and story-friendly. Pick one moon color: silver, white, or blue."
3. [wait 2s] [gentle hint] "Try saying blue or pointing to something light."

**Screen:** If `story_unlock_cards_01` is available, show a moon-door card. Fallback: voice-only story gate with no card claim. State chip records the color key when supported.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 2 -- Wake The Owl Bridge:**

**AI says:** [storyteller tone] "Past the door, the fox finds a sleepy owl bridge. The bridge will rise only if it hears a friendly owl sound. Can you make a soft 'hoo-hoo' or say 'hello, owl'?"

**Child responses:**

1. (Ideal) "Hoo-hoo." / "Hello, owl."
2. (Unexpected) Child gives a loud monster roar.
3. (No response) No response.

**AI follow-up:**

1. [specific] "The owl hears you. The bridge stretches across the silver stream."
2. [redirect] "That sound is big. This owl needs a soft helper sound."
3. [wait 2s] [gentle hint] "Try a quiet hoo-hoo."

**Screen:** Door card changes to an owl-bridge card only if state is supported; otherwise voice narration continues the bridge scene.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 3 -- Echo The Star Word:**

**AI says:** [storyteller tone] "On the bridge, a tiny star page flutters down. It says the fox needs one echo word to open the picnic meadow: 'bonjour.' Can you echo 'bonjour'?"

**Child responses:**

1. (Ideal) "Bonjour."
2. (Unexpected) Wants a scary monster.
3. (No response) Child says "I do not know."

**AI follow-up:**

1. [specific] "The star page sparkles. The meadow opens, and the fox finds a moon picnic waiting."
2. [redirect] "Let us keep this page friendly. Echo the word, then we can continue."
3. [wait 2s] [gentle hint] "Try: bon-jour."

**Screen:** If cards are available, the next-scene card appears. Fallback: voice-only scene reveal with no card claim. Progress trail shows color key -> owl sound -> echo word when state is supported.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is the story you unlocked: the fox opened the moon door, crossed the owl bridge, and reached the moon picnic because of your color, sound, and echo word. Which part feels most like yours?"

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
