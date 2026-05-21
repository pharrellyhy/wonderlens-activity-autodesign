## Echo Word Stage

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Echo Word Stage |
| Activity Category | cat1 |
| Recommended Tier | T0 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | sound_pattern, word, echo, memory |
| ATL Skills Focus | language expression (naming and explaining), focus (listening and turn-taking), pattern recognition (noticing repeats) |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

The AI says a simple word or phrase and the child repeats it back in a playful echo round.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that a word can be repeated as a single word or a doubled echo.
- **U (Understand):** Children understand that keeping the word pattern connected helps the echo ladder grow.
- **D (Do):** Children listen, repeat, and recall a short echo without pressure.

**3. Design Highlight**

The activity keeps recall low-pressure while adding a tiny memory challenge: the card or word cue appears, hides for one beat, and the child brings the echo back. Optional cards support the word cue, but the runtime can stay voice-only.

**4. Typical Scenario**

A child asks what a {target_word} is called. The AI turns {target_word} and {target_word}-{target_word} into two playful echo rounds.

### C. Interaction Flow

> Recommended Tier: T0

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "Words can bounce back. Be Echo Keeper?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. I say it. You echo."
2. [friendly] "It is an echo mission. I speak. You copy."
3. [wait 2s] [gentle] "Just listen first. One word works."

**Screen:** The activity badge "Echo Word Keeper" appears with two empty progress tokens. If `word_echo_cards_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Hear. Say. Save. Make a word ladder."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I do it my way?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Yes, you can add style. Keep the same word."
3. [wait 2s] [modeling] "Copy my first word."

**Screen:** A simple rule strip appears: Listen or look, answer, save a token. Token 1 pulses.

#### Step 3: Core Loop

**Round 1 -- Tiny Hide Echo:**

**AI says:** [focused playful tone] "Look, listen: {target_word}. I hide it. Echo it back."

**Child responses:**

1. (Ideal) "{target_word}." after the hide.
2. (Unexpected) "I say mug."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "The stage lights up. {target_word} came back. Token 1 saved."
2. [warm redirect] "Mug is nearby. Echo {target_word}."
3. [wait 2s] [gentle hint] "Try: {target_word}."

**Screen:** If `word_echo_cards_01` is available, Echo 1 shows the {target_word} picture cue, hides for one beat, then glows when the child echoes. Fallback: voice-only cue, no picture claim. Token 1 fills with the returned word.

**Round 2 -- Double Pattern Echo:**

**AI says:** [focused playful tone] "Two beats: {target_word}-{target_word}. Soft mouse voice."

**Child responses:**

1. (Ideal) "{target_word} {target_word}."
2. (Unexpected) "I squeak anything else."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "Two echoes landed. Token 2 saved."
2. [warm redirect] "That squeak was playful. Keep both words together."
3. [wait 2s] [gentle hint] "Try: {target_word} {target_word}."

**Screen:** Echo 2 adds two bouncing sound dots when visual support is available; fallback uses voice rhythm only. The two dots line up before the word ladder opens; token 2 fills with the child's pattern.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Look at that. Tokens made a ladder. Stage echoes back."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your answers opened it."
2. [replay invitation] "Great next-round idea. This path stays."
3. [wait 2s] [soft recap] "I read both tokens."

**Screen:** The two tokens expand into a final board labeled "Echo Word Keeper". Token 1 and token 2 pulse in the child's order, then a tiny curtain opens on the completed word ladder.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "Echo Keeper badge earned. Form and Connection badge."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "New echo next time."
2. [flexible] "Next mission can use that. This badge saves today."
3. [wait 2s] [gentle goodbye] "Echo Keeper badge saved."

**Screen:** The badge, the two round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
