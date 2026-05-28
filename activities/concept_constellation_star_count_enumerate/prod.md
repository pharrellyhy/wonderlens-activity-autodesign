## Constellation Number Reveal

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Constellation Number Reveal |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | count, constellation, pattern, evidence |
| ATL Skills Focus | number choice, observation, listening |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child chooses between two possible star-count numbers, then sees a real approved constellation card matching the selected number and hears one short background introduction.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that an approved constellation card can have a name, a visible guide-star count, and a simple background clue.
- **U (Understand):** Children understand that a number choice can connect to a real sky pattern when the card metadata supports it.
- **D (Do):** Children choose one star-count number, notice the revealed constellation name, and repeat either the number, name, or background clue.

**3. Design Highlight**

The activity preserves the source flow: number choice first, matching real constellation reveal second, short background introduction third.

**4. Typical Scenario**

The screen offers two number choices. The child chooses one, and the device opens an approved real constellation card whose metadata matches that count.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have two star numbers. Pick one, and it will open a real constellation card."

**Child responses:**

1. (Ideal) "Yes" or names a number.
2. (Unexpected) "I want to count the picture" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. First choose a number, then we reveal the constellation that matches it."
2. [friendly boundary] "Counting is useful, but this mission starts with choosing one of two star numbers."
3. [wait 2s] [gentle] "You can say the first number or the second number."

**Screen:** The activity badge "Constellation Number Scout" appears with three empty progress tokens. Do not show the constellation card yet. If `constellation_count_cards_01` is unavailable, use the documented voice-only fallback and do not claim a card is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Scout rule: choose one star number, open the matching constellation card, then listen for one tiny sky clue."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I pick both?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Both are interesting. For this reveal, choose one number first."
3. [wait 2s] [modeling] "I will offer two choices, and you can copy one if you want."

**Screen:** A simple rule strip appears: Choose number, reveal card, hear clue. Token 1 pulses. The screen prepares two number chips from approved card metadata.

#### Step 3: Core Loop

**Round 1 -- Choose The Star Number:**

**AI says:** [focused playful tone] "Choose one star number: {count_choice_a} or {count_choice_b}?"

**Child responses:**

1. (Ideal) Child chooses one offered number.
2. (Unexpected) Child says a number not offered.
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "{selected_star_count} is your number. Token 1 is saved."
2. [warm redirect] "That is a big sky number. For this card, choose {count_choice_a} or {count_choice_b}."
3. [wait 2s] [gentle hint] "Try one with me: {count_choice_a}."

**Screen:** Show two large number chips. Highlight the child's selected chip and keep the constellation card hidden until Round 2.

**Round 2 -- Reveal The Matching Constellation:**

**AI says:** [delighted reveal] "{selected_star_count} opens this real constellation card: {constellation_name}."

**Child responses:**

1. (Ideal) Child says the constellation name, points, or says "wow."
2. (Unexpected) Child invents a different constellation or wants to redraw it.
3. (No response) Child watches the card.

**AI follow-up:**

1. [specific praise] "Yes, this card is {constellation_name}. Token 2 is saved."
2. [validate then anchor] "Pretend constellations are fun. This card uses the approved {constellation_name} pattern, so we keep its stars in place."
3. [wait 2s] [gentle model] "I notice the name {constellation_name} on the card."

**Screen:** Reveal one approved real constellation card from `constellation_count_cards_01` whose `star_count` metadata equals `{selected_star_count}`. Show the name label when available. Do not add stars, remove stars, or alter the approved layout.

**Round 3 -- Hear The Background Clue:**

**AI says:** [wonder tone] "Tiny sky clue: {constellation_fact_child_safe}. What can you remember: the number, the name, or one clue?"

**Child responses:**

1. (Ideal) Child repeats the selected number, constellation name, or one fact.
2. (Unexpected) Child gives an unsupported astronomy fact.
3. (No response) Child stays quiet after the clue.

**AI follow-up:**

1. [specific praise] "You remembered a real clue from the card. Token 3 is saved."
2. [warm repair] "Maybe. I will stay with the approved clue on this card: {constellation_fact_child_safe}."
3. [wait 2s] [gentle hint] "Try the name with me: {constellation_name}."

**Screen:** Keep the selected constellation card visible. Add a small metadata panel with `{selected_star_count}`, `{constellation_name}`, and the approved short clue.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Your number became a constellation reveal. {selected_star_count} opened {constellation_name}, and the card gave us one real sky clue."

**Child responses:**

1. (Ideal) "I opened it" or repeats the name.
2. (Unexpected) "Can we count all the stars now?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your number choice opened this card."
2. [next-round invitation] "That can be a next mission. This round was the number-choice reveal."
3. [wait 2s] [soft recap] "I will read the three tokens back: number, constellation, clue."

**Screen:** The three tokens expand into a final board labeled "Constellation Number Scout". The selected card remains visible with its name and metadata. No extra non-approved facts appear.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You earned the Constellation Number Scout badge. You used Form by noticing the card's star pattern, and Connection by linking your number, the constellation name, and the sky clue."

**Child responses:**

1. (Ideal) "Again" or names a favorite part.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Next time we can choose a different number and open a different approved constellation card."
2. [flexible] "That can be the next mission. This badge saves what you did today."
3. [wait 2s] [gentle goodbye] "Your Constellation Number Scout badge is saved."

**Screen:** The badge, selected number, selected constellation card, and one approved clue remain visible. Next-step card: "Try a new star number next time."
