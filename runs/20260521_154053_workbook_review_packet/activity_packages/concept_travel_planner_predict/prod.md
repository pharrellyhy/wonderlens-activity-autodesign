## Pretend Trip Planner

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Pretend Trip Planner |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Causation and Change |
| Related Concepts | plan, prediction, journey, need |
| ATL Skills Focus | prediction (commit before reveal), logical reasoning (using evidence), creative thinking (making original choices) |
| Experience Pillar | Discovery |
| Game Style | prediction_lab |

### B. Activity Overview

**1. Brief Description**

The child helps plan a pretend trip by predicting what the hidden trip cards will need before each reveal.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that a pretend trip plan can include a need, a travel choice, and a surprise plan.
- **U (Understand):** Children understand that predictions connect a situation to a likely consequence before the pretend reveal.
- **D (Do):** Children commit to a prediction, see the pretend reveal, and adjust the trip plan with evidence.

**3. Design Highlight**

The package avoids real booking or location claims and keeps the activity in pretend planning and prediction.

**4. Typical Scenario**

The child plans a pretend trip to a rainy forest. They predict the needed item, travel helper, and surprise plan before each hidden card flips.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I found a perfect moment for Pretend Trip Planner. You can be the Trip Predictor today. Ready for a tiny mission?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. I will keep it short and playful."
2. [friendly] "Good question. I will show one tiny choice at a time."
3. [wait 2s] [gentle] "You can answer with one word, a point, or a small idea."

**Screen:** The activity badge "Trip Predictor" appears with three empty progress tokens. If `travel_planning_cards_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Here is the rule: predict before I flip the card, then we save what the reveal shows."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I do it my way?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Yes, your idea can help. I will still keep each round easy to answer."
3. [wait 2s] [modeling] "I will start, and you can copy my first answer if you want."

**Screen:** A simple rule strip appears: Listen or look, answer, save a token. Token 1 pulses.

#### Step 3: Core Loop

**Round 1 -- Predict What We Need:**

**AI says:** [focused playful tone] "Before the rainy reveal, predict what we will need first: raincoat, snack, or sunglasses?"

**Child responses:**

1. (Ideal) "raincoat."
2. (Unexpected) "swimsuit."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [reveal tone] "The reveal is raindrops. Raincoat matches, so token 1 becomes a dry-trip stamp."
2. [warm redirect] "A swimsuit is fun for water play. The reveal is raindrops, so choose something that keeps us dry."
3. [wait 2s] [gentle hint] "Think rain before the reveal. Predict raincoat, boots, or umbrella."

**Screen:** If `travel_planning_cards_01` is available, a hidden route card flips to a rainy path. Fallback: voice-only rainy reveal with no card claim. A suitcase slot fills with the predicted item, and token 1 saves the match or correction.

**Round 2 -- Predict How to Travel:**

**AI says:** [focused playful tone] "Before I reveal the path, predict what travel helps cross a wide puddle: walking, bus, train, or boat?"

**Child responses:**

1. (Ideal) "boat."
2. (Unexpected) "rocket."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [route-building] "The path reveal is a wide puddle. Boat fits, so token 2 draws a little water route."
2. [pretend boundary] "Rocket is a funny pretend extra. The reveal is a puddle path, so pick boat or walking carefully."
3. [wait 2s] [gentle hint] "Predict one travel helper before the reveal. Boat is ready."

**Screen:** If cards are available, the hidden path card flips from gray to blue puddle. Fallback: voice-only puddle reveal with no card claim. The chosen travel icon moves onto the route, and token 2 records the prediction result.

**Round 3 -- Predict a Surprise:**

**AI says:** [focused playful tone] "Before the surprise reveal, predict what might block us and what plan helps."

**Child responses:**

1. (Ideal) "mud, wear boots."
2. (Unexpected) "a dragon eats us."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [cause-effect tone] "The surprise reveal is mud. Boots match your plan, so token 3 becomes the safe-step stamp."
2. [safety redirect] "A dragon can stay in a storybook. The safe reveal is mud, so predict boots or a careful step."
3. [wait 2s] [gentle hint] "Try a safe prediction: mud, wear boots."

**Screen:** If cards are available, the surprise cloud flips open to a muddy path. Fallback: voice-only mud reveal with no card claim. A boot icon lands on it, and token 3 keeps the prediction visible.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Look at that. Your three predictions made something new: raincoat matched rain, boat crossed the puddle, and boots solved the mud."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your answers caused this reveal."
2. [replay invitation] "That is a great next-round idea. This version shows the path you made first."
3. [wait 2s] [soft recap] "I will read the three tokens back so you can see your path."

**Screen:** The three tokens expand into a final board labeled "Trip Predictor". Each token shows prediction -> reveal -> plan, so the payoff is earned by the child's earlier commitments.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You earned the Trip Predictor badge. You used Causation by predicting what each clue would need, and Change by updating the trip after each reveal."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Next time we can make a new path with a new answer."
2. [flexible] "That can be the next mission. This badge saves what you did today."
3. [wait 2s] [gentle goodbye] "Your Trip Predictor badge is saved."

**Screen:** The badge, the three round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
