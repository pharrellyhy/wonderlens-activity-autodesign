## Coloring Game

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Coloring Game |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Function and Change |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | creative thinking (making original choices), planning (sequencing steps), language expression (naming and explaining) |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The child turns a safe photographed object into a simple coloring plan, chooses real-world colors for named regions, and sees the palette build into a shareable artwork or honest no-image color plan.

**2. Educational Purpose (KUD)**

- **K (Know):** Coloring choices can come from safe real objects, and each selected color belongs to a named artwork region.
- **U (Understand):** Function connects each region to a color job, and Change shows how the page grows as regions fill.
- **D (Do):** Choose the subject, pick color sources, assign colors to regions, and explain the finished palette.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `runtime_coloring_line_art_01` in `full_screen_canvas`; fallback: Use a no-image color-plan fallback: the child names colors and regions verbally, and the screen shows text/color chips without claiming generated line art exists.

**4. Typical Scenario**

Trigger: A child photographs a toy car or flower, selects a big region, then adds a contrast color and accent. If generated line art or fillable regions are unavailable, the session displays only color chips and spoken region names.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a coloring game mission. You are the Palette Builder. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum runtime-image policy: use the declared asset prompt, safety rules, latency cap, and no-image fallback instead of blocking the package.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Palette Builder rule: choose the photographed object for the line-art page. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `runtime_coloring_line_art_01` in `full_screen_canvas`; fallback: Use a no-image color-plan fallback: the child names colors and regions verbally, and the screen shows text/color chips without claiming generated line art exists.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Pick the coloring subject:**

**AI says:** [round-1 guide] "Round 1: choose the photographed object for the line-art page."

**Child responses:**

1. (Ideal) "My toy car." / "This flower."
2. (Unexpected) "Make it Elsa." / chooses copyrighted character
3. (No response) Child points at the starter photo

**AI follow-up:**

1. [specific] "Good choice. I will turn that object into simple regions."
2. [redirect] "We can only use safe, original objects. Pick this photo or another everyday object."
3. [wait 2s] [gentle hint] "Point to the object you want to color."

**Screen:** Canvas shows `runtime_coloring_line_art_01` as 3-5 large regions, or fallback color chips if no generated line art exists.

> RESOLVED BLOCKER: Approved minimum runtime-image policy: use the declared asset prompt, safety rules, latency cap, and no-image fallback instead of blocking the package.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Fill the big region:**

**AI says:** [round-2 guide] "Round 2: photograph or choose a real-world color for the biggest region."

**Child responses:**

1. (Ideal) "Red from my cup."
2. (Unexpected) Chooses two colors at once
3. (No response) Child shows a color but says nothing

**AI follow-up:**

1. [specific] "Red fills the biggest region. I saved cup-red."
2. [redirect] "Two colors are exciting. Pick one for this big region first."
3. [wait 2s] [gentle hint] "Say one color, or show one object color."

**Screen:** Region 1 fills with the selected color; the source photo/color chip remains visible.

> RESOLVED BLOCKER: Approved minimum runtime-image policy: use the declared asset prompt, safety rules, latency cap, and no-image fallback instead of blocking the package.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Add contrast and accent:**

**AI says:** [round-3 guide] "Round 3: choose a contrast color plus one tiny accent."

**Child responses:**

1. (Ideal) "Blue for wheels, yellow star."
2. (Unexpected) Wants to erase everything
3. (No response) Child wants to stop

**AI follow-up:**

1. [specific] "Blue and yellow finish the palette."
2. [redirect] "We can revise one saved region if the state contract allows it; otherwise we save this version."
3. [wait 2s] [gentle hint] "We can finish with two colors and call it a mini palette."

**Screen:** Canvas shows named regions and a saved three-color palette strip.

> RESOLVED BLOCKER: Approved minimum runtime-image policy: use the declared asset prompt, safety rules, latency cap, and no-image fallback instead of blocking the package.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a saved color plan. If line art is available, it becomes a fillable page. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Coloring Game: saved color regions and palette; if line art is available, show the fillable page. Fallback: voice-only color plan with no generated-image claim. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Function and Change today. You used your own build action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Palette Builder badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `coloring_game`, asset/fallback note when relevant, and one next-step hint.
