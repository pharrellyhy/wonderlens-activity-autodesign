## Word Build Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Word Build Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Perspective and Function |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | decision making (choosing between options), language expression (naming and explaining), logical reasoning (using evidence) |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child uses age-approved clues and letter choices to grow a word one step at a time, with a voice-only clue-riddle fallback when letter UI state is unavailable.

**2. Educational Purpose (KUD)**

- **K (Know):** A word puzzle grows from approved clues and visible/voice letter choices, without punishment imagery.
- **U (Understand):** Function lets each clue or letter do a job, and Perspective helps the child choose a clue path and explain why.
- **D (Do):** Hear a clue, choose a letter or answer, reveal safe word progress, and explain the final word.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `word_growth_ui_01` in `top_prompt_or_progress_overlay`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: A parent selects a reading level and a safe target word such as plant, moon, or cake. The AI reveals clue progress only inside the declared word-state contract and avoids hangman or shame imagery.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a word build guess mission. You are the Word Grower. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Word Grower rule: choose between two clue paths for the hidden word. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `word_growth_ui_01` in `top_prompt_or_progress_overlay`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Hear the clue:**

**AI says:** [round-1 guide] "Round 1: choose between two clue paths for the hidden word."

**Child responses:**

1. (Ideal) "Animal clue."
2. (Unexpected) Wants hard spelling
3. (No response) No response

**AI follow-up:**

1. [specific] "Animal clue chosen. I will reveal one safe hint."
2. [redirect] "We keep reading level gentle. Choose sound clue or picture clue."
3. [wait 2s] [gentle hint] "Pick sound or picture."

**Screen:** Word-growth overlay shows blank tiles only under resolved state contract.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Grow the word:**

**AI says:** [round-2 guide] "Round 2: pick a letter sound or answer a clue to reveal part of the word."

**Child responses:**

1. (Ideal) "/k/ sound."
2. (Unexpected) Guesses random letters rapidly
3. (No response) No response

**AI follow-up:**

1. [specific] "The /k/ sound grows the first tile."
2. [redirect] "One choice at a time helps the word grow."
3. [wait 2s] [gentle hint] "Say one sound or ask for a picture clue."

**Screen:** One tile fills; no hangman or punishment imagery.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Guess and explain:**

**AI says:** [round-3 guide] "Round 3: say the word and one clue that helped."

**Child responses:**

1. (Ideal) "Cat, because /k/ and animal."
2. (Unexpected) Cannot read word
3. (No response) No response

**AI follow-up:**

1. [specific] "Cat fits your clue path."
2. [redirect] "You can listen instead of read. I will say the sounds again."
3. [wait 2s] [gentle hint] "Say the animal you think it is."

**Screen:** Final word reveal pairs spoken answer with clue evidence.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a word revealed through clue choices and one final explanation. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Word Build Guess: a word revealed through clue choices and one final explanation. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Perspective and Function today. You used your own decide action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Word Grower badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `word_build_guess`, asset/fallback note when relevant, and one next-step hint.
