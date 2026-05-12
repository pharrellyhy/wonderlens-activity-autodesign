## Color In Famous Art

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Color In Famous Art |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Function |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | observation (noticing visible evidence), counting (one-to-one tracking), language expression (naming and explaining) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child studies one approved artwork, names dominant and supporting colors from known metadata, and builds a color map with visible evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Approved artworks can be explored through dominant and supporting colors with known metadata.
- **U (Understand):** Form helps identify colors and shapes, and Function helps the child explain what each color does in the artwork.
- **D (Do):** Look at one approved artwork, name key colors, compare the strongest color, and recap the color evidence.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `color_artwork_set_01` in `split_or_center_artwork_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: The product can display a curated public-domain or licensed artwork with color metadata. The AI discusses only visible colors and child-safe context, with no live museum lookup required.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a color in famous art mission. You are the Color Curator. We will do 3 small turns, and each one changes the ending. Ready?"

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

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Color Curator rule: name the first color that stands out in the artwork. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `color_artwork_set_01` in `split_or_center_artwork_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Find the loudest color:**

**AI says:** [round-1 guide] "Round 1: name the first color that stands out in the artwork."

**Child responses:**

1. (Ideal) "Bright yellow."
2. (Unexpected) Names invisible color
3. (No response) No response

**AI follow-up:**

1. [specific] "Yellow is the loudest color you noticed."
2. [redirect] "Look again at the approved artwork card. Pick a color you can see."
3. [wait 2s] [gentle hint] "Point or say one color."

**Screen:** Artwork card remains visible with a color chip; metadata source is approved.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 2 -- Find repeated colors:**

**AI says:** [round-2 guide] "Round 2: point to or name where the color appears again."

**Child responses:**

1. (Ideal) "Yellow on the hat and window."
2. (Unexpected) Only says favorite color
3. (No response) No response

**AI follow-up:**

1. [specific] "Two yellow spots make a repeated color path."
2. [redirect] "Favorite can help, but show where it appears in the artwork."
3. [wait 2s] [gentle hint] "Find one more spot."

**Screen:** Color chip draws two small markers on visible areas.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
**Round 3 -- Choose the guide color:**

**AI says:** [round-3 guide] "Round 3: pick which visible color guides your eye most."

**Child responses:**

1. (Ideal) "Blue guides my eye."
2. (Unexpected) Makes factual artist claim
3. (No response) No response

**AI follow-up:**

1. [specific] "Blue guides your eye, so it has an important job."
2. [redirect] "We talk about what we see and feel, not unapproved art history."
3. [wait 2s] [gentle hint] "Which color guides your eye?"

**Screen:** Color map labels loudest, repeated, and guide colors.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: an approved artwork color map with loudest, repeated, and guide colors. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Color In Famous Art: an approved artwork color map with loudest, repeated, and guide colors. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Form and Function today. You used your own enumerate action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Color Curator badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `color_famous_art`, asset/fallback note when relevant, and one next-step hint.
