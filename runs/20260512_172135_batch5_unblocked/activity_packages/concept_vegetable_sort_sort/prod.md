## Vegetable Sort Stand

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Vegetable Sort Stand |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Connection and Form |
| Related Concepts | classification, rule, food, evidence |
| ATL Skills Focus | classification (grouping by a rule), observation (noticing visible evidence), logical reasoning (using evidence) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know that vegetables can be grouped by visible rules such as color, shape, or edible part.
- **U (Understand):** Children understand that one sorting rule explains why items belong together or apart.
- **D (Do):** Children choose a rule, place vegetable cards, and name a group using evidence.

**3. Design Highlight**

Sorting stays the repeated action. The AI can suggest rules, but the child names and applies the grouping evidence.

**4. Typical Scenario**

The screen shows carrot, broccoli, tomato, and potato cards. The child sorts by color first, then by plant part or cooking use.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "The vegetable stand is mixed up. Want to be the Veggie Sorter?"

**Child responses:**

1. (Ideal) "Yes" or nods.
2. (Unexpected) "What mission?" or gives an unrelated idea.
3. (No response) Child watches or stays quiet.

**AI follow-up:**

1. [excited] "Great. We will pick a rule, place two vegetables, and name a group."
2. [friendly] "It is a sorting mission. Your rule tells each vegetable where to go."
3. [wait 2s] [gentle] "You can point to a basket or say one rule."

**Screen:** The activity badge "Veggie Sorter" appears with three empty progress tokens. If `vegetable_sort_cards_01` is available, show it as support; if not, use voice-only fallback and do not claim the asset is visible.

> RESOLVED BLOCKER: Approved minimum asset-display contract: use the declared asset ID, display timing, screen location, and no-display fallback instead of blocking the package.

#### Step 2: Rule Introduction

**AI says:** [clear guide tone] "Sorter rule: choose the grouping rule, use it on the cards, then name one group."

**Child responses:**

1. (Ideal) "Okay."
2. (Unexpected) "Can I do it my way?"
3. (No response) Child hesitates.

**AI follow-up:**

1. [encouraging] "Round one is ready."
2. [validating] "Yes, your way can help. We will still keep one clear sorting rule."
3. [wait 2s] [modeling] "I will start, and you can copy my first answer if you want."

**Screen:** A simple rule strip appears: Listen or look, answer, save a token. Token 1 pulses.

#### Step 3: Core Loop

**Round 1 -- Pick a Rule:**

**AI says:** [focused playful tone] "Choose the stand rule: color, shape, or part we eat. Which rule should run this round?"

**Child responses:**

1. (Ideal) "color" / "shape" / "part we eat."
2. (Unexpected) "yummy."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "That is a clear sorting rule. Token 1 is saved."
2. [warm redirect] "Yummy is an opinion rule. Pick a rule the cards can show: color, shape, or part we eat."
3. [wait 2s] [gentle hint] "Try: color, shape, or part."

**Screen:** The chosen rule sign appears above two baskets. The card set switches labels to match: color groups, shape groups, or edible-part groups.

**Round 2 -- Place Two Vegetables:**

**AI says:** [sorting tone] "Use your rule on carrot and tomato. If your rule is color, where do they go? If it is part we eat, where do they go?"

**Child responses:**

1. (Ideal) "orange and red groups" / "roots and fruits."
2. (Unexpected) "same basket because food."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "That placement follows your rule. Token 2 is saved."
2. [warm redirect] "Same basket uses a broad food rule. Your chosen rule needs color, shape, or plant-part evidence."
3. [wait 2s] [gentle hint] "Try one evidence label: red, orange, root, or fruit."

**Screen:** Carrot and tomato cards slide into groups based on the chosen rule; the screen labels the rule path instead of forcing color only.

**Round 3 -- Name the Group:**

**AI says:** [labeling tone] "Name one group using your rule. It could be red foods, round vegetables, roots, or fruits."

**Child responses:**

1. (Ideal) "red foods" / "roots" / "round vegetables."
2. (Unexpected) "vegetable team."
3. (No response) Child looks at the screen or waits.

**AI follow-up:**

1. [specific praise] "That label names the group by evidence. Token 3 is saved."
2. [warm redirect] "Vegetable team is friendly. A rule label tells what connects them: color, shape, or part."
3. [wait 2s] [gentle hint] "Try: red foods, round foods, or roots."

**Screen:** A label tag appears on the chosen group and carries the chosen rule type so the sort remains coherent.

#### Step 4: Magic Moment

**AI says:** [delighted reveal] "Look at that. Your three tokens opened the stand: your rule, sorted cards, and an evidence label."

**Child responses:**

1. (Ideal) "I made it" or explains the result.
2. (Unexpected) "Can we change one?"
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [celebrating] "Yes. Your answers caused this reveal."
2. [replay invitation] "That is a great next-round idea. This version shows the path you made first."
3. [wait 2s] [soft recap] "I will read the three tokens back so you can see your path."

**Screen:** The three tokens expand into a final board labeled "Veggie Sorter": chosen rule, two sorted vegetables, and one evidence label. A replay hint invites the child to try another rule next time.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You earned the Veggie Sorter badge. You used Connection by grouping foods by one rule, and Form by noticing color and shape clues."

**Child responses:**

1. (Ideal) "Again" or names a favorite round.
2. (Unexpected) Child asks for a different topic.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud guide] "Next time we can make a new path with a new answer."
2. [flexible] "That can be the next mission. This badge saves what you did today."
3. [wait 2s] [gentle goodbye] "Your Veggie Sorter badge is saved."

**Screen:** The badge, the three round tokens, and a next-step card remain visible. Next-step card: "Try one new answer next time."
