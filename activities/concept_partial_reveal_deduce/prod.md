## Partial Reveal Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Partial Reveal Guess |
| Activity Category | 1 -- Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | Evidence, Inference, Part-Whole, Clue |
| ATL Skills Focus | Research Skills (observation), Thinking Skills (inference), Communication Skills (explaining evidence) |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child sees one cropped clue from a prebuilt card, guesses the hidden whole, and explains what evidence helped.

**2. Educational Purpose (KUD)**

- **K (Know):** A visible part can be evidence for a whole; guesses can change with new evidence; a reveal checks whether the clue fits.
- **U (Understand):** Form helps us notice shape, texture, and visible details. Connection helps us link a part to the whole.
- **D (Do):** Inspect a partial clue, make a guess, and explain which clue supported the guess.

**3. Design Highlight**

Each round starts with a mystery crop, not the full answer. If cards are unavailable, the same loop becomes a voice-only part riddle.

**4. Typical Scenario**

The screen shows long rabbit ears. The child guesses "rabbit" and says, "The ears helped."

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** [mystery whisper] "A whole animal is hiding, but one tiny part slipped out. Detective eyes ready?"

**Child responses:**

1. (Ideal) "Ready!" / "I can look."
2. (Unexpected) "Show me the whole thing." / "Is it a cat?"
3. (No response) Child watches the screen.

**AI follow-up:**

1. [excited whisper] "Good. We solve with evidence, one part at a time."
2. [playful suspense] "The whole stays hidden for now. Your guess might change after the clue."
3. [wait 2s] [gentle invite] "Look for shape, color, texture, or what the part might do."

**Screen:** A mystery curtain covers the answer. If `partial_reveal_cards_01` is available, a small card deck labeled "part clues" waits behind the curtain. If unavailable, show only clue pips and a voice-riddle badge.

#### Step 2: Rule Introduction -- Part-Spotter Detective

**AI says:** [clear guide tone] "You are the Part-Spotter Detective. I show or describe one part. You guess the whole and tell me the clue."

**Child responses:**

1. (Ideal) "Okay!" / "I will tell the clue."
2. (Unexpected) "What if I am wrong?" / "Can I guess fast?"
3. (No response) Child listens.

**AI follow-up:**

1. [cheering softly] "Perfect. A good detective uses the part as evidence."
2. [reassuring] "Wrong guesses are allowed. Evidence helps us try again."
3. [wait 2s] [soft model] "Say, 'I think it is ___ because I see ___.'"

**Screen:** A "Part-Spotter Detective" badge appears. If `partial_reveal_cards_01` is available, the first card back slides forward. If unavailable, the badge says "voice clue mode" and no picture is shown.

#### Step 3: Multi-Round Partial Reveal

**Round 1 -- Long Ears Clue:**

**AI says:** [quiet clue tone] "Clue one: I see two long ears. What whole animal could this be, and what clue tells you?"

**Child responses:**

1. (Ideal) "Rabbit, because ears." / "Bunny. I see long ears."
2. (Unexpected) "Dog." / "I do not know the clue."
3. (No response) Child keeps looking or listening.

**AI follow-up:**

1. [intrigued detective tone] "Strong evidence. You used the long ears to connect the part to rabbit."
2. [kind redirect] "Dogs can have ears too. Say what you notice: long ears, upright ears, or soft ears."
3. [wait 2s] [gentle hint] "Use this sentence: 'I think it is rabbit because I see long ears.'"

**Screen:** If `partial_reveal_cards_01` is available, show the rabbit-ears partial card full screen with the answer hidden. If unavailable, show clue pip 1 and the words "long ears" without any animal picture.

**Round 2 -- Webbed Feet Clue:**

**AI says:** [watery mystery tone] "Clue two: I see flat webbed feet. What whole animal might be hiding, and what evidence helps?"

**Child responses:**

1. (Ideal) "Duck, because webbed feet." / "Goose. The feet help."
2. (Unexpected) "Fish." / "Feet."
3. (No response) Child looks unsure.

**AI follow-up:**

1. [pleased] "Good evidence. You noticed webbed feet that can help an animal paddle."
2. [validating then focusing] "Fish live in water too, but your clue has feet. Say, 'I see feet,' then guess a water animal with feet."
3. [wait 2s] [soft hint] "Try: 'I think it is duck because I see webbed feet.'"

**Screen:** If `partial_reveal_cards_01` is available, show the duck-feet partial card with only the feet visible. If unavailable, show clue pip 2 and a ripple icon while the AI uses voice only.

**Round 3 -- Striped Tail Clue:**

**AI says:** [building suspense] "Final clue: I see an orange tail with dark stripes. What whole animal fits that part, and which clue proves it?"

**Child responses:**

1. (Ideal) "Tiger, because stripes." / "A big cat. Orange stripes."
2. (Unexpected) "Zebra." / "Snake."
3. (No response) Child waits.

**AI follow-up:**

1. [dramatic reveal tone] "Tiger is a strong detective guess. You used orange stripes as evidence."
2. [gentle narrowing] "Zebras have stripes too. Add the other evidence: orange, furry, and tail."
3. [wait 2s] [kind reveal setup] "Try: 'I think it is tiger because I see an orange striped tail.'"

**Screen:** If `partial_reveal_cards_01` is available, show the tiger-tail partial card and pulse the stripes. If unavailable, show clue pip 3, an orange stripe icon, and no animal picture.

#### Step 4: Magic Moment -- Part-to-Whole Reveal

**AI says:** [celebration whisper] "Reveal time! Long ears made rabbit. Webbed feet made duck. Striped tail made tiger. Tiny parts became whole answers."

**Child responses:**

1. (Ideal) "I solved them!" / "The ears helped."
2. (Unexpected) "I missed one." / "Show tiger again."
3. (No response) Child watches the reveal board.

**AI follow-up:**

1. [proud detective tone] "Yes. You used evidence from the parts."
2. [warmly validating] "Missing one is detective work too. New clues make guesses stronger."
3. [wait 2s] [soft recap] "Look at each part. Each one connects to a whole."

**Screen:** If `partial_reveal_cards_01` is available, reveal each full answer card beside its partial card. If unavailable, show a part-to-whole board with text labels and simple icons only.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You did it, Part-Spotter Detective. You used Form. You noticed shapes and details. You used Connection too. You linked each part to the whole."

**Child responses:**

1. (Ideal) "Another one!" / "I used clues."
2. (Unexpected) "Can I pick the animal?" / "Rabbit again."
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide tone] "Your clue eyes are sharp. Next time, tell which part helped most."
2. [delighted] "Yes. Choosing the mystery makes you an expert detective."
3. [wait 2s] [soft goodbye] "Your Part-Spotter badge is saved."

**Screen:** A "Part-Spotter Detective" badge appears with three clue pips. The words "Form" and "Connection" glow beside a part-to-whole arrow. A next-step card says, "Next: explain the strongest clue."
