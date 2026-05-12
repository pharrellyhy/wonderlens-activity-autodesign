## Children's Yoga

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Children's Yoga |
| Activity Category | cat1 |
| Recommended Tier | T0 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | language expression (naming and explaining), focus (listening and turn-taking), collaboration (following shared safety rules) |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

AI guides a short child-safe pose routine using animal or object metaphors. The child acts as the Calm Pose Guide and completes 2 safe pose-and-breath turns before seeing a two-pose calm routine with breath and rest.

**2. Educational Purpose (KUD)**

- **K (Know):** Calm poses for children stay stable, short, and easy to stop.
- **U (Understand):** Form helps the child notice body shape, and Perspective connects breath/rest choices to calm feeling.
- **D (Do):** Try two safe pose metaphors, use a breath cue, stop or simplify when needed, and name a favorite calm move.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `childrens_yoga_pose_cards_01` in `center_pose_card`; fallback: Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible.

**4. Typical Scenario**

Trigger: A parent selects a calm routine and confirms enough space. The AI uses stable two-feet poses, breath cues, and a stop option, with pose cards shown only when the approved card set is available.

### C. Interaction Flow

> Recommended Tier: T0

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "Calm Pose Guide, ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I show. You try."
2. [flexible] "I can make it smaller. Point, say, or pose."
3. [wait 2s] [gentle] "Easiest version first."

**Screen:** Shows title, setup cue, safety/fallback chip, and 2 empty progress slots.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Rule: stable gentle poses."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. First pose saved."
2. [scaffolded] "Pause if not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `childrens_yoga_pose_cards_01` in `center_pose_card`; fallback: Use voice-only safe movement prompts with caregiver space check, or stop the movement activity without claiming a pose card is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Tree reach:**

**AI says:** [round-1 guide] "Tree reach. Feet down."

**Child responses:**

1. (Ideal) "Tree." / reaches arms
2. (Unexpected) Tries one-foot balance
3. (No response) No response

**AI follow-up:**

1. [specific] "Two feet stay safe."
2. [redirect] "Keep both feet down. We are doing child-safe tree."
3. [wait 2s] [gentle hint] "Reach arms up like branches."

**Screen:** If `childrens_yoga_pose_cards_01` is available, pose card shows two-feet tree. Fallback: voice-only pose cue with no card claim. Stop/pause remains visible.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.
**Round 2 -- Butterfly rest:**

**AI says:** [round-2 guide] "Gentle butterfly rest."

**Child responses:**

1. (Ideal) "Butterfly."
2. (Unexpected) Extreme stretch
3. (No response) Child lies down tired

**AI follow-up:**

1. [specific] "Gentle butterfly is enough. Breathe slowly."
2. [redirect] "No extreme stretches. Tiny wings instead."
3. [wait 2s] [gentle hint] "Hands can be butterfly wings."

**Screen:** If cards are available, pose card shows gentle rest. Fallback: voice-only rest cue with no card claim. Recap saves calm routine, not pose quality.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum motion policy: caregiver gating, space check, low-risk movement set, and prohibited motions are documented.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Your calm routine opened."

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made calm turns."
2. [honest repair] "This version is saved."
3. [wait 2s] [soft recap] "I show each turn."

**Screen:** Shows the specific payoff for Children's Yoga: a two-pose calm routine with breath and rest. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "Form and Perspective badge."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "New calm pose next."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Calm Pose badge saved."

**Screen:** Recap badge shows the 2-turn trail, focal attribute `childrens_yoga`, asset/fallback note when relevant, and one next-step hint.
