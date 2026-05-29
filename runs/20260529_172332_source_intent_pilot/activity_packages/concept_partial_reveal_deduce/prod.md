## Partial Reveal Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Partial Reveal Guess |
| Activity Category | 1 -- Visual Deduction Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | visible part, whole animal, evidence |
| ATL Skills Focus | observing, inferring, explaining |
| Experience Pillar | Mystery |
| Game Style | clue_detective |

### B. Activity Overview

**1. Brief Description**

The child sees one distinctive animal part at a time and guesses the whole animal using visible evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The required screen dependency stays explicit: the card is the clue, and voice fallback must admit when no image is visible.

**4. Typical Scenario**

Child solves rabbit ears, tiger tail, and elephant trunk cards, explaining the evidence rather than hearing generic riddles.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Invite Evidence Guessing

**Runtime AI instruction:** Goal: frame the game as looking at one visible animal part and guessing the whole animal from evidence. Constraint: T1 max two sentences; no voice-only clues before the first card appears. Tone: curious mystery guide. Progress evidence: child agrees, asks to see the part, or points to the screen. Branch behavior: open the first card when ready, reject voice-only guessing as the main path, and model looking for shape when quiet. Frame/source guardrail: visible partial asset is required for the main flow.

**Example AI line:** [curious] "I will show only one animal part. Look closely, then guess the whole animal."

**Child responses:**
1. (Ideal) Child says "show me", "I can guess", or points to the closed mystery card.
2. (Unexpected) Child asks for only spoken clues or wants the full animal first.
3. (No response) Child watches the closed card without answering.

**AI follow-up policy:**
1. (Ideal) [open] "Here comes the first picture part. We will use what we can see."
2. (Unexpected) [anchor] "The picture part is the clue in this game; I will not reveal the whole animal yet."
3. (No response) [model] "I will look for shape, color, and texture before guessing."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Closed mystery card state; no animal answer visible yet.
#### Step 2: Show The First Part

**Runtime AI instruction:** Goal: display rabbit_ears_reveal_card and ask what whole animal it might be. Constraint: do not show or say the answer before the child guesses. Tone: playful detective. Progress evidence: child says rabbit, bunny, ears, or gives evidence. Branch behavior: accept rabbit/bunny, ask for evidence on unrelated guesses, and offer rabbit versus fish after silence. Frame/source guardrail: child deduces from visible evidence, not generic riddles.

**Example AI line:** [detective] "Look at these long soft ears. What animal could be hiding?"

**Child responses:**
1. (Ideal) Child guesses rabbit or bunny, or says "long ears" as evidence.
2. (Unexpected) Child guesses fish, tiger, or another animal without pointing to an ear clue.
3. (No response) Child looks at rabbit_ears_reveal_card but gives no guess.

**AI follow-up policy:**
1. (Ideal) [validate] "Yes, long soft ears are strong rabbit evidence; now we can mark rabbit solved."
2. (Unexpected) [evidence] "Show me the clue that made you think that. I see long ears, so try a guess that uses ears."
3. (No response) [choice] "Could long ears belong to a rabbit or a fish?"

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=rabbit_ears_reveal_card full screen inside the round safe area.
#### Step 3: Try A Different Part

**Round 1 -- Second Partial Clue:**

**Runtime AI instruction:** Goal: display tiger_tail_reveal_card and ask for a new whole-animal guess using visible stripes and tail shape. Constraint: one guess plus one evidence detail. Tone: excited detective. Progress evidence: child says tiger, striped tail, cat, or points to stripes. Branch behavior: accept tiger, treat big cat as near-miss and ask for stripes, and hint tiger after silence. Frame/source guardrail: maintain partial reveal image flow across multiple rounds.

**Example AI line:** [excited] "Now I see a striped tail curling in. Which animal might own this part?"

**Child responses:**
1. (Ideal) Child guesses tiger or says striped tail as the evidence.
2. (Unexpected) Child says cat, snake, or another near miss without mentioning stripes.
3. (No response) Child stares at tiger_tail_reveal_card without guessing.

**AI follow-up policy:**
1. (Ideal) [connect] "The orange stripes and tail shape support tiger; tiger solved."
2. (Unexpected) [repair] "Cat is close, but these bold stripes are the important clue. What striped animal fits?"
3. (No response) [hint] "A tiger has bold orange-and-dark stripes like this tail."

**Photo capture timing:** No photo capture.

**Screen/state:** Replace first card with asset_id=tiger_tail_reveal_card; keep a small solved rabbit badge.
#### Step 4: Final Part Challenge

**Runtime AI instruction:** Goal: display elephant_trunk_reveal_card and let the child use shape evidence for the final guess. Constraint: T1 max two sentences; no full animal reveal before answer. Tone: gentle suspense. Progress evidence: child says elephant, trunk, long nose, or points. Branch behavior: accept elephant, ask for visible clue on wrong guesses, and model trunk-to-elephant after silence. Frame/source guardrail: do not replace this with generic animal trivia.

**Example AI line:** [suspense] "Last mystery part: a long trunk shape. What whole animal could it be?"

**Child responses:**
1. (Ideal) Child guesses elephant or says trunk/long nose as evidence.
2. (Unexpected) Child guesses snake, whale, or another animal without using the trunk clue.
3. (No response) Child watches elephant_trunk_reveal_card with no guess.

**AI follow-up policy:**
1. (Ideal) [celebrate] "That trunk evidence points to elephant; final mystery solved."
2. (Unexpected) [evidence] "Look at the long trunk shape. Which animal is famous for a trunk?"
3. (No response) [model] "A long trunk makes me think elephant."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=elephant_trunk_reveal_card; three-card progress shows two solved badges.
#### Step 5: Close The Evidence Gallery

**Runtime AI instruction:** Goal: recap each visible part and the whole animal guessed from it. Constraint: max two sentences; no new card. Tone: proud and observant. Progress evidence: child names one animal or clue. Branch behavior: save any named solved card, boundary requests for more cards, and close quietly if no reply. Frame/source guardrail: keep the visible evidence source central to the ending.

**Example AI line:** [proud] "You solved animals from parts: ears, stripes, and trunk. That is evidence guessing."

**Child responses:**
1. (Ideal) Child names rabbit ears, tiger stripes, elephant trunk, or one solved animal.
2. (Unexpected) Child asks for a new animal before the recap or wants full pictures instead of parts.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [badge] "Evidence saved: you used parts to solve whole animals."
2. (Unexpected) [boundary] "More part cards can be another round; this gallery closes with the clues we solved."
3. (No response) [quiet close] "I will save rabbit ears, tiger tail, and elephant trunk in the evidence gallery."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show three solved thumbnails using the same asset_ids; no new generated image.
