## Pattern Patrol

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Pattern Patrol |
| Activity Category | Collection/Tracking Exploration (Catalog Collection) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Form, Connection |
| Related Concepts | Pattern, Observation, Similarities and Differences |
| ATL Skills Focus | Research Skills (observation, evidence collection), Thinking Skills (comparison, classification) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**: The child becomes a Pattern Patrol Officer. The runtime supplies a target pattern, currently `polka_dots` or `stripes`, and the child chooses three catalog cards that show that pattern. Each choice asks the child to name the visible evidence, then the synthesis compares how the same pattern looks different across cards.

**2. Educational Purpose (KUD)**:
- **K (Know):** Patterns can be made from repeated dots, spots, lines, or stripes. The same pattern can appear on different objects.
- **U (Understand):** Form helps us notice the shape and arrangement of a pattern. Connection helps us link different things that share a visual clue.
- **D (Do):** Choose cards that match a target pattern, explain the visible evidence, compare how examples are similar and different, and turn the collection into a tiny patrol story.

**3. Design Highlight**: The patrol frame turns catalog selection into a mission. The child is not just tapping cards; they are collecting evidence for a pattern clue, naming what they see, and making a parade team from the completed set.

**4. Typical Scenario**: Runtime starts with a supported target pattern such as polka dots or stripes. The child chooses three matching cards from an approved catalog, explains the pattern evidence on each card, then compares and names the selected cards.

**5. Runtime Asset Notes**

- Required catalog assets are declared in `asset_manifest.yaml`.
- The runtime must select a supported `collection_catalog_id` from `{target_pattern_property}` before play.
- The demo must not claim to verify arbitrary camera photos. If the target property has no approved catalog with at least three correct cards, do not start this package.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** [delighted discovery] "Pattern Patrol is opening! Today's clue is {pattern_label}. Look closely: what do you notice about this kind of pattern?"

**Child responses:**

1. (Ideal) "Dots!" / "Lines!" / "They repeat!" / child names the target pattern
2. (Unexpected) "I like that card!" / "It's pretty!" / child comments on one object
3. (No response) Child looks quietly at the pattern clue.

**AI follow-up:**

1. [thrilled] "Yes! You spotted the clue. Your patrol job is to find three cards with {pattern_label}."
2. [warm, focusing] "It is a good-looking card. Now look at the pattern on it. Do you see {pattern_label}?"
3. [wait 2s] [gentle] "I will point to the clue: {pattern_label}. We are looking for cards that show that same kind of pattern."

**Screen:** `intro_scene` fills the round screen. The target pattern label is rendered by the app outside the PNG. A small target clue swatch appears as app UI.

#### Step 2: Rule Introduction + Demo

**AI says:** [adventurous] "You are a Pattern Patrol Officer. Pick three cards that match {pattern_label}. After each pick, tell me what pattern evidence you see."

**Child responses:**

1. (Ideal) "Okay!" / "I can find them!" / child is ready
2. (Unexpected) "Can I pick any card?" / "What if I like another one?"
3. (No response) Child waits or scans the catalog.

**AI follow-up:**

1. [cheering] "Officer ready! First, choose one card that clearly shows {pattern_label}."
2. [helpful] "You can like any card, but patrol evidence has to match the clue. Pick one that shows {pattern_label}."
3. [wait 2s] [encouraging] "Try one card first. Look for the pattern clue, not just your favorite object."

**Screen:** `rules_scene` shows the patrol setup. The app overlays a catalog grid filtered to the supported target set plus optional distractors.

#### Step 3: Multi-Round Interaction

**Round 1 -- First Pattern Card:**

**AI says:** [curious] "Choose your first {pattern_label} card. What makes this one match the clue?"

**Child responses:**

1. (Ideal) Child selects a correct card and says evidence such as "It has dots" or "It has stripes."
2. (Unexpected) Child selects a distractor or gives only the object name.
3. (No response) Child looks at the catalog without choosing.

**AI follow-up:**

1. [delighted] "Good evidence. I heard the pattern clue, so this card joins the patrol."
2. [gentle correction] "That object is interesting. For this mission, show me the pattern evidence. Do you see {pattern_label} on that card, or should we choose another?"
3. [wait 2s] [scaffolding] "Start with one card where the pattern is easy to see. I will keep the clue visible."

**Screen:** `round_1_scene` fills the background. The selected card moves into patrol slot 1 as app UI; the catalog remains available.

**Round 2 -- Second Pattern Card:**

**AI says:** [investigative] "Now choose a second card with {pattern_label}. How is this pattern a little different from your first card?"

**Child responses:**

1. (Ideal) Child selects another correct card and compares size, spacing, color, or direction.
2. (Unexpected) Child says "same" without comparing or chooses another distractor.
3. (No response) Child looks between the first card and catalog.

**AI follow-up:**

1. [impressed] "Nice comparison. Same clue, different look. That is strong patrol evidence."
2. [warm, guiding] "They share a clue, but look closely. Are these marks bigger, smaller, closer together, or going a different way?"
3. [wait 2s] [encouraging] "Your first card is saved. Choose one more card that also shows {pattern_label}."

**Screen:** `round_2_scene` fills the background. Patrol slots 1 and 2 stay visible as app overlays.

**Round 3 -- Third Pattern Card:**

**AI says:** [excited] "Final patrol pick. Choose one last card with {pattern_label}, then tell me the pattern evidence."

**Child responses:**

1. (Ideal) Child selects a third correct card and names the evidence.
2. (Unexpected) Child says "done" before explaining evidence.
3. (No response) Child pauses after seeing the remaining catalog cards.

**AI follow-up:**

1. [celebrating] "Evidence accepted. Three pattern cards are in the patrol."
2. [warm] "Almost complete. Tell me what pattern clue you see on this last card, and then the patrol set is ready."
3. [wait 2s] [gentle] "One more clear pattern card will finish the mission. I will keep the clue on screen."

**Screen:** `round_3_scene` fills the background. Patrol slot 3 fills; the app shows a mission-complete state.

#### Step 4: Synthesis + Celebration

**AI says:** [amazed] "Look at your three patrol cards together. They all show {pattern_label}, but they are not exactly the same. What is different between them?"

**Child responses:**

1. (Ideal) Child compares size, spacing, color, curve, direction, or object type.
2. (Unexpected) Child says only "They match" or names a favorite card.
3. (No response) Child looks at the completed set.

**AI follow-up:**

1. [impressed] "Yes. Same pattern clue, different forms. That is exactly what Pattern Patrol looks for."
2. [scaffolding] "They do match. Now look closer: is one pattern bigger, thinner, closer together, or on a different kind of object?"
3. [wait 2s] [gentle] "I see three matching cards, each with its own pattern style. That gives us a patrol team."

**AI says:** [storytelling] "Give each card a tiny patrol name, or I can help. Then the pattern team will march together."

**Child responses:**

1. (Ideal) Child names one or more selected cards.
2. (Unexpected) Child asks to skip naming.
3. (No response) Child smiles or watches the card row.

**AI follow-up:**

1. [delighted] "Those names fit the evidence. The patrol team is ready to move."
2. [warm] "We can skip names. The patrol team can still follow the pattern trail together."
3. [wait 2s] [soft narration] "I will give them quiet patrol names for now and send them down the pattern path."

**Screen:** `synthesis_scene` fills the background. The app overlays the three selected cards in a row with same/different comparison cues.

**AI says:** [ceremonial] "Pattern Patrol Officer, mission complete. You found the Form of the pattern and made a Connection between three different cards."

**Child responses:**

1. (Engaged) "Yay!" / "I found them!" / child celebrates.
2. (Unexpected) "Can I try stripes?" / "Can I try dots?" / child asks for another target.
3. (No response) Child watches the badge.

**AI follow-up:**

1. [proud] "You used careful eyes and strong evidence. Badge earned."
2. [warm] "Another pattern can be the next patrol. This mission is complete."
3. [wait 2s] [gentle] "The badge is shining for your careful pattern work."

**Screen:** `celebrate_scene` appears. The app overlays the completed patrol badge and selected-card thumbnails.

#### Step 5: Closing + IB Concepts

**AI says:** [warm, reflective] "Today you practiced Form by noticing what the pattern looks like, and Connection by finding different cards that share one clue. Keep your Pattern Patrol eyes ready for the next pattern."

**Child responses:**

1. (Engaged) "Bye!" / "I will find more patterns!" / child acknowledges.
2. (Unexpected) "Again!" / child wants another round.
3. (No response) Child waves or watches the closing screen.

**AI follow-up:**

1. [celebration] "Pattern Patrol complete. See you next time, Officer."
2. [gentle] "Another patrol can happen next time. This pattern team is complete."
3. [wait 2s] [gentle] "Great patrol today. The next pattern clue will wait for you."

**Screen:** `closing_scene` fills the background. The app shows the target pattern, selected-card row, and Form + Connection recap outside the PNG.
