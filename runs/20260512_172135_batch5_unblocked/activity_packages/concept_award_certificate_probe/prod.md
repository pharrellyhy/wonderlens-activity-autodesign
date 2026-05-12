## Award Certificate

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Award Certificate |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Responsibility and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | empathy (noticing needs), perspective taking (considering another view), language expression (naming and explaining) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child chooses someone to appreciate, selects a non-shaming award reason, and creates one spoken certificate line with an optional badge inspiration card.

**2. Educational Purpose (KUD)**

- **K (Know):** An appreciation award names a person, a kind reason, and one spoken certificate line.
- **U (Understand):** Responsibility keeps the award non-shaming, and Perspective focuses on what the honoree did or needed.
- **D (Do):** Choose the honoree, select a positive reason, make a spoken line, and present the award without ranking others.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `award_inspiration_badges_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: A child wants to thank a helper, teammate, sibling, or grown-up. The AI keeps the certificate appreciative rather than competitive and does not promise printing or template editing in fallback mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have an award certificate mission. You are the Appreciation Designer. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Appreciation Designer rule: name someone who helped, tried hard, or deserves appreciation. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `award_inspiration_badges_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose the honoree:**

**AI says:** [round-1 guide] "Round 1: name someone who helped, tried hard, or deserves appreciation."

**Child responses:**

1. (Ideal) "My sister."
2. (Unexpected) Wants a best/worst contest
3. (No response) No response

**AI follow-up:**

1. [specific] "Your sister is the honoree."
2. [redirect] "This award is appreciation, not ranking. Pick one helper."
3. [wait 2s] [gentle hint] "Say someone who helped."

**Screen:** Honoree chip appears; no competitive leaderboard.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 2 -- Pick the award reason:**

**AI says:** [round-2 guide] "Round 2: choose kindness, trying hard, helping, bravery, creativity, or teamwork."

**Child responses:**

1. (Ideal) "Helping, because she cleaned."
2. (Unexpected) Chooses a shame reason
3. (No response) No response

**AI follow-up:**

1. [specific] "Helping is a strong award reason."
2. [redirect] "Awards should be kind. Pick helping, trying, or teamwork."
3. [wait 2s] [gentle hint] "Pick one kind reason."

**Screen:** Badge card appears from `award_inspiration_badges_01` if available.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 3 -- Say the certificate line:**

**AI says:** [round-3 guide] "Round 3: create one spoken appreciation sentence."

**Child responses:**

1. (Ideal) "I award you for helping me."
2. (Unexpected) Wants printed certificate
3. (No response) No response

**AI follow-up:**

1. [specific] "That line is ready for the certificate."
2. [redirect] "Printing is not part of this fallback. We can save the spoken line."
3. [wait 2s] [gentle hint] "Try: I award you for ___."

**Screen:** Certificate preview or voice-only recap shows the line and badge reason.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: an award reason, badge choice, and spoken certificate line. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Award Certificate: an award reason, badge choice, and spoken certificate line. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Responsibility and Perspective today. You used your own care action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Appreciation Designer badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `award_certificate`, asset/fallback note when relevant, and one next-step hint.
