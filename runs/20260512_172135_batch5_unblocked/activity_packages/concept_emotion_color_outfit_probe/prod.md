## Emotion Color Outfit

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Emotion Color Outfit |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Responsibility and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | empathy (noticing needs), perspective taking (considering another view), language expression (naming and explaining) |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child notices a character's possible feeling, chooses a comfort color for that character, and adds a caring action so the outfit idea stays empathy-led rather than decoration-only.

**2. Educational Purpose (KUD)**

- **K (Know):** Colors can represent feelings for one character, but they do not diagnose anyone.
- **U (Understand):** Perspective uses visible cues and "might feel" language; Responsibility adds a caring action after the color choice.
- **D (Do):** Notice a feeling cue, choose a comfort color, add a gentle support action, and review the care plan.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `emotion_color_character_01` in `support_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: A child names a mood or points to a color. The AI asks for a visible cue, treats color meanings as personal, and displays recoloring only when the approved character template and UI state are available.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have an emotion color outfit mission. You are the Feeling Stylist. We will do 3 small turns, and each one changes the ending. Ready?"

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
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Feeling Stylist rule: use the character card or my voice cue, then say what they might feel. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `emotion_color_character_01` in `support_panel`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Notice the feeling cue:**

**AI says:** [round-1 guide] "Round 1: use the character cue and say what they might feel."

**Child responses:**

1. (Ideal) "Maybe worried, shoulders are small."
2. (Unexpected) "Blue." only
3. (No response) No response

**AI follow-up:**

1. [specific] "Might be worried is careful language. The shoulder clue helps."
2. [redirect] "Blue can come later. First name what the character might feel."
3. [wait 2s] [gentle hint] "Say happy, worried, tired, or surprised."

**Screen:** If `emotion_color_character_01` is available, character card shows face/body cue. Fallback: voice-only cue with no card claim. Copy says "might feel," not diagnosis.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Choose a comfort color:**

**AI says:** [round-2 guide] "Round 2: choose a color that could help the character feel supported."

**Child responses:**

1. (Ideal) "Soft yellow because it feels warm."
2. (Unexpected) Says a color means everyone feels one way
3. (No response) Child points only

**AI follow-up:**

1. [specific] "Soft yellow becomes a comfort scarf."
2. [redirect] "Colors do not mean the same feeling for everyone. Tell what it means for this character."
3. [wait 2s] [gentle hint] "Pick one comfort color."

**Screen:** Outfit region recolors only if UI and the card are available. Fallback: voice-only color choice stored in the recap.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Add a caring action:**

**AI says:** [round-3 guide] "Round 3: name one thing that could help the character."

**Child responses:**

1. (Ideal) "A friend can sit with them."
2. (Unexpected) "Make them stop crying now."
3. (No response) No response

**AI follow-up:**

1. [specific] "Sitting with them is a caring action."
2. [redirect] "We cannot force feelings away. We can offer help."
3. [wait 2s] [gentle hint] "Try: ask if they want help."

**Screen:** If the card/state UI is available, final card shows feeling cue -> comfort color -> caring action. Fallback: voice-only recap with no card claim.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum coloring/recoloring contract: selectable regions, child color input, persistence rules, and a voice-only fallback are allowed.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a character support plan: feeling cue, comfort color, and caring action. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Emotion Color Outfit: a character support plan: feeling cue, comfort color, and caring action. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Responsibility and Perspective today. You used your own care action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Feeling Stylist badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `emotion_color_outfit`, asset/fallback note when relevant, and one next-step hint.
