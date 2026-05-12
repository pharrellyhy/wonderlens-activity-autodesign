## Simple Body Movement Guide

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Simple Body Movement Guide |
| Activity Category | cat1 |
| Recommended Tier | T0 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | language expression (naming and explaining), focus (listening and turn-taking), collaboration (following shared safety rules) |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

AI guides one simple body movement at a time with safety limits. The child acts as the Safe Move Leader and completes 2 safe movement turns before seeing two low-risk movement prompts: hands and freeze.

**2. Educational Purpose (KUD)**

- **K (Know):** A movement guide uses only low-risk prompts, caregiver space checks, and clear stop options.
- **U (Understand):** Form helps the child notice body shape, and Perspective lets the child choose a safe version that feels right.
- **D (Do):** Try two safe movement prompts, self-report completion, simplify risky moves, and review the movement trail.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `body_movement_cards_01` in `center_pose_card`; fallback: Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible.

**4. Typical Scenario**

Trigger: A parent starts a short movement prompt and confirms enough space. The AI offers only low-risk hand, reach, and freeze prompts, accepts self-report, and keeps the stop button visible.

### C. Interaction Flow

> Recommended Tier: T0

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "Safe Move Leader, ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I show. You try."
2. [flexible] "I can make it smaller. Point, say, or move."
3. [wait 2s] [gentle] "Easiest version first."

**Screen:** Shows title, setup cue, safety/fallback chip, and 2 empty progress slots.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Rule: tiny safe moves only."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. First step saved."
2. [scaffolded] "Pause if not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `body_movement_cards_01` in `center_pose_card`; fallback: Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Hello hands:**

**AI says:** [round-1 guide] "Small wave or hand stretch."

**Child responses:**

1. (Ideal) "Wave."
2. (Unexpected) Starts running
3. (No response) No response

**AI follow-up:**

1. [specific] "Small wave is safe."
2. [redirect] "Running is outside this activity. Stay in one safe spot."
3. [wait 2s] [gentle hint] "Try a tiny hand wave."

**Screen:** Movement card shows hand wave, space check, and stop button.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.
**Round 2 -- Freeze statue:**

**AI says:** [round-2 guide] "Freeze and breathe."

**Child responses:**

1. (Ideal) "Freeze."
2. (Unexpected) Risky balance pose
3. (No response) Child sits

**AI follow-up:**

1. [specific] "Seated freeze counts. Breathe in, breathe out."
2. [redirect] "Feet down, or sit. Safety first."
3. [wait 2s] [gentle hint] "Freeze hands for one breath."

**Screen:** Recap shows two safe movements, not motion-quality verification.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Your safe move trail opened."

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made this trail."
2. [honest repair] "This version is saved."
3. [wait 2s] [soft recap] "I show each turn."

**Screen:** Shows the specific payoff for Simple Body Movement Guide: two low-risk movement prompts: hands and freeze. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "Form and Perspective badge."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "New theme next time."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Safe Move badge saved."

**Screen:** Recap badge shows the 2-turn trail, focal attribute `body_movement`, asset/fallback note when relevant, and one next-step hint.
