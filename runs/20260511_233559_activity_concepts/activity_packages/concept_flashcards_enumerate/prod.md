## Picture Pop Cards

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Picture Pop Cards |
| Activity Category | cat1 |
| Recommended Tier | T0 |
| Core IB Key Concepts | Form and Function |
| Related Concepts | name, picture, feature, category |
| ATL Skills Focus | observation, language_expression, focus |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child recognizes a picture card, names what they see, and answers one tiny follow-up.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know a picture can have a name and one simple action or use clue.
- **U (Understand):** Children understand that naming and answering one tiny clue make a picture easier to remember and talk about.
- **D (Do):** Children name one card and answer one feature/function follow-up.

**3. Design Highlight**

The package is picture-first and does not require text reading. If cards are unavailable, it can pivot to a photographed object.

**4. Typical Scenario**

The screen shows a duck card. The child names it, notices one feature, and answers one tiny follow-up.

### C. Interaction Flow

> Recommended Tier: T0

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "Picture pop time. Be Picture Namer?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Yes. One card first."
2. [friendly] "A picture will pop."
3. [wait 2s] [gentle] "Point or say one word."

**Screen:** The activity badge "Picture Namer" appears with two empty progress tokens. If `generic_flashcard_library_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Name it. Pick one."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I do it my way?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Your way can help."
3. [wait 2s] [modeling] "Copy me: duck."

**Screen:** A simple rule strip appears: Look, name, answer. Token 1 pulses; token 2 waits.

#### Step 3: Core Loop

**Round 1 -- Name the Picture:**

**AI says:** [focused playful tone] "What do you see on this card?"

**Child responses:**

1. (Ideal) "duck."
2. (Unexpected) "yellow thing."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [bright] "Duck. Token one pops."
2. [warm redirect] "Yellow thing is close. It is a duck."
3. [wait 2s] [gentle hint] "Say duck, or point."

**Screen:** The card pops forward with one clear picture. Token 1 fills with a short label from the child's response.

**Round 2 -- Answer a Tiny Follow-Up:**

**AI says:** [focused playful tone] "Does a duck swim or drive a car?"

**Child responses:**

1. (Ideal) "swim."
2. (Unexpected) "drive."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [playful] "Swim. The water icon glows."
2. [silly redirect] "A driving duck is pretend. This duck swims."
3. [wait 2s] [gentle hint] "Choose swim or car."

**Screen:** Two simple icons appear, and swim glows after the answer. Token 2 fills with a short label from the child's response.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Pop! Duck badge made. Swim clue saved."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. You made it."
2. [replay invitation] "Good idea. First we save this."
3. [wait 2s] [soft recap] "Duck and swim. Saved."

**Screen:** The two tokens expand into a final board labeled "Picture Namer". Each token stays visible so the payoff is earned by the child's earlier actions.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "Picture Namer badge earned. You used Form. You used Function."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Again can be next."
2. [flexible] "New topic next. Badge saved."
3. [wait 2s] [gentle goodbye] "Picture Namer is saved."

**Screen:** The badge, the two round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
