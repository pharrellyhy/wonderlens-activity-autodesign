## Art Critic Tournament

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Art Critic Tournament |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | observation (noticing visible evidence), quantity comparison (same/different amount), language expression (naming and explaining) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child compares rights-cleared artwork pairs, chooses a favorite using visible color/shape/feeling evidence, and crowns a small bracket winner with the child's reason attached.

**2. Educational Purpose (KUD)**

- **K (Know):** An art preference can use visible evidence such as color, shape, subject, line, or feeling.
- **U (Understand):** Form supports looking closely, and Perspective makes the favorite a child-owned choice rather than a right answer.
- **D (Do):** Compare approved artwork pairs, name one visible reason, advance a favorite, and crown a gallery pick.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `artwork_tournament_set_01` in `split_or_center_artwork_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: The approved artwork set can show two age-safe images side by side. The AI asks for visible reasons, supports ties, and avoids outside artist claims unless metadata supplies them.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have an art critic tournament mission. You are the Gallery Chooser. We will do 3 small turns, and each one changes the ending. Ready?"

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

**AI says:** [clear guide tone] "Gallery Chooser rule: choose a favorite artwork and name one visible reason. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `artwork_tournament_set_01` in `split_or_center_artwork_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Compare pair one:**

**AI says:** [round-1 guide] "Round 1: choose a favorite artwork and name one visible reason."

**Child responses:**

1. (Ideal) "I pick the blue one because waves."
2. (Unexpected) Says artist is famous
3. (No response) No response

**AI follow-up:**

1. [specific] "Blue waves is visible evidence. Artwork A advances."
2. [redirect] "Famous is outside our card metadata. Use color, shape, or feeling."
3. [wait 2s] [gentle hint] "Pick A or B and one thing you see."

**Screen:** Two approved artworks appear side by side; bracket slot one fills.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Compare the winner:**

**AI says:** [round-2 guide] "Round 2: put the winner against another approved artwork."

**Child responses:**

1. (Ideal) "This one feels calmer."
2. (Unexpected) Wants unapproved art
3. (No response) No response

**AI follow-up:**

1. [specific] "Calmer is your perspective, and the soft colors are evidence."
2. [redirect] "We only use approved artworks in this set."
3. [wait 2s] [gentle hint] "Choose the one you want to keep."

**Screen:** Bracket shows previous winner vs new challenger.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Crown the gallery pick:**

**AI says:** [round-3 guide] "Round 3: explain the final favorite with color, shape, or feeling evidence."

**Child responses:**

1. (Ideal) "The blue waves win because they feel peaceful."
2. (Unexpected) Cannot choose
3. (No response) No response

**AI follow-up:**

1. [specific] "That is a complete critic reason."
2. [redirect] "You can choose tie and name one thing from each."
3. [wait 2s] [gentle hint] "Say color, shape, or feeling."

**Screen:** Winner frame appears with reason label and no ranking of the child.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a tiny bracket winner chosen from visible art evidence. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Art Critic Tournament: a tiny bracket winner chosen from visible art evidence. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Form and Perspective today. You used your own compare action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Gallery Chooser badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `art_critic_tournament`, asset/fallback note when relevant, and one next-step hint.
