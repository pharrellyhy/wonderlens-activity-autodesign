## Guided Drawing

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guided Drawing |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Function and Change |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | creative thinking (making original choices), planning (sequencing steps), language expression (naming and explaining) |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The child uses paper or a drawing surface to follow three simple sketch beats: make a big shape, add one detail, and show or self-report a finish without the AI judging drawing quality.

**2. Educational Purpose (KUD)**

- **K (Know):** A drawing can be built from a few safe, simple steps: shape, detail, and finish.
- **U (Understand):** Function helps each line do a job, and Change shows how small marks become a picture.
- **D (Do):** Prepare paper, follow the drawing steps at the child's pace, self-report the attempt, and describe one finished detail.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `guided_drawing_step_cards_01` in `center_card_area`; fallback: If step cards are unavailable, use voice-only step descriptions with caregiver setup, self-report completion, and no drawing-quality assessment.

**4. Typical Scenario**

Trigger: A child has paper and pencil ready and chooses a simple object as the drawing theme. The AI paces each mark, accepts caregiver/self-report evidence, and falls back to voice-only steps if cards are unavailable.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a guided drawing mission. You are the Step Sketch Coach. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

**Photo capture timing:** No photo capture happens in Step 1. The child prepares for drawing after the AI prompt; any finished-work photo waits until Round 3.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Step Sketch Coach rule: draw the largest simple shape from the card or my voice clue. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `guided_drawing_step_cards_01` in `center_card_area`; fallback: If step cards are unavailable, use voice-only step descriptions with caregiver setup, self-report completion, and no drawing-quality assessment.

**Photo capture timing:** No photo capture happens in Step 2. The rule prompt sets up drawing steps; photo evidence is only requested for the finished drawing in Round 3.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Draw the big shape:**

**AI says:** [round-1 guide] "Round 1: draw the largest simple shape from the card or voice clue."

**Child responses:**

1. (Ideal) "I drew a circle body."
2. (Unexpected) "Mine is messy."
3. (No response) Child is still drawing

**AI follow-up:**

1. [specific] "A big circle body is enough for step one."
2. [redirect] "Messy counts. We care about trying the shape, not perfect copying."
3. [wait 2s] [gentle hint] "Make one big shape and tell me done."

**Screen:** If `guided_drawing_step_cards_01` is available, step card 1 stays in center. Fallback: voice-only step cue with no card claim. A timer says "drawing time"; no quality score appears.

**Photo capture timing:** No photo capture happens in Round 1. The child draws after the AI prompt and responds by saying or self-reporting that the big shape is done.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 2 -- Add one useful detail:**

**AI says:** [round-2 guide] "Round 2: add one detail that makes the drawing recognizable."

**Child responses:**

1. (Ideal) "I added ears."
2. (Unexpected) Child cannot find pencil/material
3. (No response) Child asks grown-up for help

**AI follow-up:**

1. [specific] "Ears make it easier to recognize. Step two is saved."
2. [redirect] "Pause and ask a grown-up for paper or use a voice-only pretend drawing."
3. [wait 2s] [gentle hint] "Add any one detail: ear, wheel, stem, or window."

**Screen:** If cards are available, step card 2 appears. Fallback: voice-only detail cue with no card claim. Material-help chip is visible for caregiver setup.

**Photo capture timing:** No photo capture happens in Round 2. The child adds one detail after the AI prompt and reports completion verbally or by gesture.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 3 -- Show the finish:**

**AI says:** [round-3 guide] "Round 3: photograph or describe the finished drawing."

**Child responses:**

1. (Ideal) "Here is my drawing."
2. (Unexpected) Photo is blurry or child refuses photo
3. (No response) Child only describes it

**AI follow-up:**

1. [specific] "I will save this as your finished drawing photo."
2. [redirect] "No problem. We can use your description and not claim I saw it clearly."
3. [wait 2s] [gentle hint] "Say one thing your drawing has."

**Screen:** Final-work slot is marked photo, description, or skipped; no visual assessment claim is made.

**Photo capture timing:** If the child chooses the photo path, the finished-drawing photo is captured after the Round 3 AI prompt and before the child response is saved. If the photo is blurry, refused, or skipped, the follow-up switches to description/self-report instead of requiring another capture.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a child-made drawing built from a big shape, detail, and finish photo/self-report. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Guided Drawing: a child-made drawing built from a big shape, detail, and finish photo/self-report. Resolved contract chips remain visible for reviewer traceability.

**Photo capture timing:** No new photo capture happens in Step 4. The reveal uses the Round 3 finished photo when available, or the child's description/self-report when not.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Function and Change today. You used your own build action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Step Sketch Coach badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `guided_drawing`, asset/fallback note when relevant, and one next-step hint.

**Photo capture timing:** No new photo capture happens in Step 5. The badge saves the existing finished-work evidence.
