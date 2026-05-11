## Two-Color Mix Lab

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Two-Color Mix Lab |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Causation and Change |
| Related Concepts | color, mix, prediction, result |
| ATL Skills Focus | prediction, observation, creative_thinking |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child chooses or finds two colors, predicts what they make together, and compares against the mixed result.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that two chosen colors can combine into a different result color.
- **U (Understand):** Children understand that the selected color pair causes the mix result.
- **D (Do):** Children choose two colors, predict the result, and compare the reveal to their guess.

**3. Design Highlight**

The loop preserves collection of color inputs while adding a prediction reveal. The optional board supports the moment; voice-only fallback still works.

**4. Typical Scenario**

The child finds red and yellow nearby. The AI asks for a prediction, names orange as the mix result, and stores the pair on a lab board.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "Two colors are ready for a tiny experiment. Want to be the Color Mix Tester?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. We will collect two colors, then make a guess before the reveal."
2. [friendly] "It is a color lab mission. You choose the colors, then predict the mix."
3. [wait 2s] [gentle] "You can point to a color or say its name."

**Screen:** The activity badge "Color Mix Tester" appears with three empty progress tokens. If `color_mixing_board_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Lab rule: collect color one, collect color two, then guess the mix before I reveal it."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I do it my way?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Yes, your way can help. We will still save two color choices before the result."
3. [wait 2s] [modeling] "I will start, and you can copy my first answer if you want."

**Screen:** A simple rule strip appears: Listen or look, answer, save a token. Token 1 pulses.

#### Step 3: Core Loop

**Round 1 -- Collect Color One:**

**AI says:** [focused playful tone] "Find or name the first color for the lab."

**Child responses:**

1. (Ideal) "red."
2. (Unexpected) "banana."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "Red is our first color. Token 1 is saved."
2. [warm redirect] "Banana gives us a clue. Its color is yellow, but this round starts with red."
3. [wait 2s] [gentle hint] "Try this short answer with me: red."

**Screen:** The first color circle fills or is named red. Token 1 fills with a short label from the child's response.

**Round 2 -- Collect Color Two:**

**AI says:** [focused playful tone] "Now choose a second color to mix with it."

**Child responses:**

1. (Ideal) "yellow."
2. (Unexpected) "same color again."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "Yellow joins red on the lab board. Token 2 is saved."
2. [warm redirect] "Same color would make a repeat. Choose a different mixer: yellow."
3. [wait 2s] [gentle hint] "Try this short answer with me: yellow."

**Screen:** The second color circle fills or is named yellow. Token 2 fills with a short label from the child's response.

**Round 3 -- Predict the Result:**

**AI says:** [focused playful tone] "Before I reveal, what color might red and yellow make together?"

**Child responses:**

1. (Ideal) "orange."
2. (Unexpected) "purple."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "Orange is the mix prediction for red plus yellow. Token 3 is saved."
2. [warm redirect] "Purple is a real mix for other colors. Red plus yellow points us to orange."
3. [wait 2s] [gentle hint] "Try this short answer with me: orange."

**Screen:** The result circle waits, then glows with the named result. Token 3 fills with a short label from the child's response.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Look at that. Your red token and yellow token flow into orange. Your choices caused the color change."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your answers caused this reveal."
2. [replay invitation] "That is a great next-round idea. This version shows the path you made first."
3. [wait 2s] [soft recap] "I will read the three tokens back so you can see your path."

**Screen:** The three tokens expand into a final board labeled "Color Mix Tester". Each token stays visible so the payoff is earned by the child's earlier actions.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You earned the Color Mix Tester badge. You used Causation by choosing red plus yellow, and Change by predicting orange."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Next time we can make a new path with a new answer."
2. [flexible] "That can be the next mission. This badge saves what you did today."
3. [wait 2s] [gentle goodbye] "Your Color Mix Tester badge is saved."

**Screen:** The badge, the three round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
