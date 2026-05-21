## Tiny Trivia Trail

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Tiny Trivia Trail |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Connection and Function |
| Related Concepts | memory, question, clue, explanation |
| ATL Skills Focus | focus (listening and turn-taking), logical reasoning (using evidence), language expression (naming and explaining) |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child answers short memory or knowledge questions and receives a simple explanation.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that leaves help with sunlight, roots help with water, and a remembered fact can become a clue.
- **U (Understand):** Children understand that recall is not a test for speed; each remembered detail connects to a bigger topic map.
- **D (Do):** Children recall one fact, choose the better answer, and retell one remembered idea in their own words.

**3. Design Highlight**

Trivia is framed as recall with explanation, not pressure. Optional reward visuals are only used when stateful display exists.

**4. Typical Scenario**

After learning about plants, the AI asks three tiny questions such as what leaves help plants do, then explains gently.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I found a perfect moment for Tiny Trivia Trail. You can be the Trivia Trail Finder today. Ready for a tiny mission?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. I will keep it short and playful."
2. [friendly] "Good question. I will show one tiny choice at a time."
3. [wait 2s] [gentle] "You can answer with one word, a point, or a small idea."

**Screen:** The activity badge "Trivia Trail Finder" appears with three empty progress tokens. If `trivia_reward_board_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Here is the rule: I give you one small challenge, you answer, and we save one progress token. Three tokens make the final reveal."

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

**Round 1 -- Remember One Detail:**

**AI says:** [focused playful tone] "What did we learn leaves help a plant do?"

**Child responses:**

1. (Ideal) "catch sunlight."
2. (Unexpected) "sleep."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [warm recall tone] "Yes, leaves catch sunlight. I am saving that as clue one."
2. [gentle correction] "Sleep is a cozy idea. This clue is about sunlight, so leaves catch sunlight."
3. [wait 2s] [gentle hint] "Think of the bright sky. Leaves catch sunlight."

**Screen:** A clue leaf icon appears beside the question. Token 1 fills with a short label from the child's response.

**Round 2 -- Choose the Better Answer:**

**AI says:** [focused playful tone] "Which fits: roots drink water, or roots fly?"

**Child responses:**

1. (Ideal) "drink water."
2. (Unexpected) "fly."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [confirming] "Drink water. The root clue connects to the drop."
2. [playful redirect] "Flying roots would be a funny story. Real roots help drink water."
3. [wait 2s] [gentle hint] "Pick the one roots really do: drink water."

**Screen:** A root clue connects to a water drop. Token 2 fills with a short label from the child's response.

**Round 3 -- Explain in Your Words:**

**AI says:** [focused playful tone] "Tell me one thing you remember about the topic."

**Child responses:**

1. (Ideal) "plants need water."
2. (Unexpected) "I do not know."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [listening] "Plants need water. I will put your words on the trail."
2. [no-pressure] "That is okay. Use one clue we already found: plants need water."
3. [wait 2s] [gentle hint] "You can repeat after me: plants need water."

**Screen:** The memory trail saves one child phrase. Token 3 fills with a short label from the child's response.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Look at that. Your three tokens made something new: The trail reveals three remembered clues and turns them into a tiny topic map."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your answers caused this reveal."
2. [replay invitation] "That is a great next-round idea. This version shows the path you made first."
3. [wait 2s] [soft recap] "I will read the three tokens back so you can see your path."

**Screen:** The three tokens expand into a final board labeled "Trivia Trail Finder". Each token stays visible so the payoff is earned by the child's earlier actions.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You earned the Trivia Trail Finder badge. You used Connection by noticing the important part, and Function by connecting your answers to what happened next."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Next time we can make a new path with a new answer."
2. [flexible] "That can be the next mission. This badge saves what you did today."
3. [wait 2s] [gentle goodbye] "Your Trivia Trail Finder badge is saved."

**Screen:** The badge, the three round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
