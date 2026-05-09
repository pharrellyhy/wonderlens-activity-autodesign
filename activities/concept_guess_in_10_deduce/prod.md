## Guess in 10

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guess in 10 |
| Activity Category | 1 -- Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Function and Form |
| Related Concepts | Evidence, Clues, Inference, Mystery |
| ATL Skills Focus | Thinking Skills (logical reasoning), Research Skills (using evidence), Communication Skills (explaining guesses) |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The AI hides a common animal or object and gives clues one by one. The child guesses, uses evidence, and gets easier hints if stuck.

**2. Educational Purpose (KUD)**

- **K (Know):** Clues can describe what something does, looks like, or where it belongs; guesses can change when new evidence appears; a reveal checks the evidence.
- **U (Understand):** Function helps us infer what something is used for. Form helps us use shape and features as clues.
- **D (Do):** Listen to clues, make a guess from evidence, and revise a guess after a new clue.

**3. Design Highlight**

The child experiences real suspense: each clue narrows the mystery, but the answer stays hidden until the reveal. Optional cards support the child only when available.

**4. Typical Scenario**

Child enters guessing mode; the AI secretly chooses "duck" and gives clues about water, waddling, and a beak.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** [mysterious whisper] "I have a secret answer. It is hiding behind three clues. Put on your detective ears. Ready to guess?"

**Child responses:**

1. (Ideal) "Ready!" / "Yes!"
2. (Unexpected) "Is it my toy?" / "Tell me now."
3. (No response) Child listens silently.

**AI follow-up:**

1. [excited detective tone] "Good. First clue is coming."
2. [playful validation] "Maybe, maybe not. Clues will help us know."
3. [wait 2s] [gentle suspense tone] "I will start easy. You can guess any time."

**Screen:** A mystery curtain covers a question-mark badge. Three empty clue pips sit below it. No reference card is shown yet.

#### Step 2: Rule Introduction -- Clue Detective

**AI says:** [clear guide tone] "You are the Clue Detective. I give a clue. You make a guess. New clues make the mystery easier."

**Child responses:**

1. (Ideal) "Okay!" / "I can guess."
2. (Unexpected) "What if I am wrong?" / "Can I see it?"
3. (No response) Child waits.

**AI follow-up:**

1. [cheering] "Perfect. Every guess helps the detective work."
2. [reassuring] "Wrong guesses are clues too. We just keep thinking."
3. [wait 2s] [soft model tone] "Listen first. Then say one animal or thing."

**Screen:** A "Clue Detective" badge appears. If `guess_reference_cards_01` is available, a closed card deck icon sits in the corner; otherwise only the clue pips and curtain appear.

#### Step 3: Multi-Round Clue Guessing

**Round 1 -- Function Clue:**

**AI says:** [secret clue tone] "Clue one: this mystery thing can move in water. What could it be?"

**Child responses:**

1. (Ideal) "Duck!" / "Fish!" / "Boat!"
2. (Unexpected) "Car." / "I do not know."
3. (No response) Child waits.

**AI follow-up:**

1. [intrigued] "Good evidence guess. It could move in water. Let's collect another clue."
2. [kind redirect] "Good thinking. Mystery clues can feel tricky. This one likes water. Try animal or boat."
3. [wait 2s] [soft hint tone] "Think of something wet. It swims, floats, or waddles near water."

**Screen:** Clue pip 1 lights up with a water ripple icon. If cards are available and the child is stuck, show a partial hint card from `guess_reference_cards_01`; if unavailable, keep the curtain and use voice only.

**Round 2 -- Form Clue:**

**AI says:** [careful clue tone] "Clue two: it has a beak. Now what is your best guess?"

**Child responses:**

1. (Ideal) "Duck!" / "Bird!"
2. (Unexpected) "Dog." / "A spoon."
3. (No response) Child looks unsure.

**AI follow-up:**

1. [warmer tone] "Smart guess. A beak is strong evidence. One more clue will help."
2. [validating then focusing] "Dogs are great. This mystery has a beak, so think bird."
3. [wait 2s] [gentle hint tone] "It says quack in many stories. What might it be?"

**Screen:** Clue pip 2 lights up with a beak shape. The curtain lifts a tiny amount but does not reveal the answer. Optional hint card behavior remains tied to `guess_reference_cards_01`.

**Round 3 -- Sound/Behavior Clue:**

**AI says:** [building suspense] "Final clue: it waddles and says quack. Make your final detective guess."

**Child responses:**

1. (Ideal) "Duck!"
2. (Unexpected) "Bird." / "Chicken."
3. (No response) Child stays quiet.

**AI follow-up:**

1. [dramatic reveal tone] "You solved it. The answer is duck."
2. [gentle narrowing tone] "Very close. It is a bird that waddles and quacks. The answer is duck."
3. [wait 2s] [kind reveal tone] "I will reveal it. The water-beak-quack mystery is duck."

**Screen:** Clue pip 3 lights up. The curtain opens. If `guess_reference_cards_01` is available, show the duck card now; if unavailable, show a simple question-mark badge turning into the word "duck" with a duck-footprint icon.

#### Step 4: Magic Moment -- Mystery Reveal

**AI says:** [celebration whisper] "Mystery solved! Water clue, beak clue, quack clue. They all pointed to duck. Your evidence trail worked."

**Child responses:**

1. (Ideal) "I knew it!" / "Duck!"
2. (Unexpected) "I guessed fish first." / "I like ducks."
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud detective tone] "Yes. You used clues like a detective."
2. [warmly validating] "Fish was a smart first guess. New clues changed the answer."
3. [wait 2s] [soft recap tone] "Look at the three clues. They made one answer."

**Screen:** The three clue pips connect into a glowing evidence trail. A "Mystery Solved" stamp lands on the duck reveal.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You did it, Clue Detective. You used Function. You thought about what it does. You used Form too. You used beak clues to solve."

**Child responses:**

1. (Ideal) "Another mystery!" / "I solved it!"
2. (Unexpected) "Can it be a cat next?" / "Show the duck again."
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide tone] "Your detective ears are sharp. Next time, solve a harder mystery."
2. [delighted] "A cat mystery can come next. Your duck case is closed."
3. [wait 2s] [soft goodbye tone] "Your Clue Detective badge is saved. The evidence trail is complete."

**Screen:** A "Clue Detective" badge appears with three clue pips. The words "Function" and "Form" glow beside the evidence trail. A next-step card says, "Next: use two clues before guessing."
