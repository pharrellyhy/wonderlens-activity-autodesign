## The Fluffy Expedition

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Fluffy Expedition |
| Activity Category | Catalog Collection Exploration |
| Recommended Tier | T0 (ages 2-4) |
| Core IB Key Concepts | Connection, Form |
| Related Concepts | Discovery, Sensory Awareness, Nature, Texture |
| ATL Skills Focus | Research Skills (observation, data collection), Communication Skills (describing, naming) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The AI introduces a dandelion seed puff as the first fluffy friend. The child becomes a "Fluffy Expedition Explorer" and chooses 3 illustrated catalog cards that show soft, fuzzy, puffy, or fluffy textures. For each choice, the child says the texture clue out loud, gives the fluffy friend a small name, and helps make a tiny story about the soft friends meeting.

**2. Educational Purpose (KUD)**

- **K (Know):** Learn that dandelion seeds can look fluffy and light. Learn that "soft" comes in many forms: fuzzy, silky, puffy, woolly, and feathery.
- **U (Understand):** Understand that different things can be connected by a shared texture clue. A dandelion puff, moss, yarn, and a feather can all belong in the same soft-texture group.
- **D (Do):** Practice choosing examples from a catalog, describing visible texture evidence, comparing softness words, naming objects as characters, and building a simple story from selected cards.

**3. Design Highlight**

The quest_collector synthesis turns a texture collection into character creation and storytelling. Each soft card earns a texture-inspired name the child invents, such as "Cloud Puff," "Fuzzy Friend," or "Woolly Star." The final story moment asks what the fluffy friends do when they meet, letting even a very young child turn texture observation into narrative.

**4. Typical Scenario**

Dandelion seed puff appears -> AI marvels at fluffy texture -> child becomes a Fluffy Expedition Explorer -> child chooses 3 soft/fluffy catalog cards -> child says texture clues and names the finds -> child tells a tiny meeting story -> AI awards the Fluffy Expedition Explorer badge.

**5. Runtime Asset Notes**

- Required scene assets: `activity_icon`, `intro_scene`, `rules_scene`, `round_1_scene`, `round_2_scene`, `round_3_scene`, `synthesis_scene`, `celebrate_scene`, and `closing_scene`.
- Required catalog cards for `fluffy_soft_texture`: `fluffy_dandelion_puff`, `fuzzy_moss_patch`, `woolly_yarn_ball`, and `soft_feather`.
- Optional distractor cards: `smooth_pebble` and `plain_wood_block`.
- The demo must not claim to verify real-world touch, arbitrary photos, or whether a nearby object is truly soft. The proof is the approved catalog card plus the child's spoken texture evidence.

### C. Interaction Flow

> Recommended Tier: T0 (ages 2-4)

#### Step 1: Transition Bridge

**AI says:** [delighted gasp] "Ooh! Look at this dandelion puff. It looks like tiny fluffy parachutes! What soft word would you use for it?"

**Child responses:**

1. (Ideal) "Fluffy!" / "Soft!" / "Like a cloud!"
2. (Unexpected) "It's a flower!" / "White!" / "It can fly!"
3. (No response) Child looks quietly.

**AI follow-up:**

1. [amazed] "Fluffy like a cloud! That is our first soft clue."
2. [warm, accepting] "Yes, it is a flower friend. And those little seeds look so soft and fluffy."
3. [wait 2s] [soft, playful] "I see tiny cloud fluff. I wonder if we can find more fluffy friends."

**Screen:** `intro_scene` fills the round screen. The dandelion seed puff sits inside the central safe area with gentle floating seed motion. If unavailable, show a neutral pale background and keep the dandelion catalog card visible.

#### Step 2: Rule Introduction + Demo

**AI says:** [excited, playful] "You are a Fluffy Expedition Explorer! Let's choose 3 cards that look soft, fuzzy, or fluffy. When you pick one, tell me the soft clue you see."

**Child responses:**

1. (Ideal) "Yeah!" / "I want the fluffy one!" / child taps a card
2. (Unexpected) "What's fluffy?" / "Which one?"
3. (No response) Child scans the cards slowly.

**AI follow-up:**

1. [cheering] "Go go, Explorer! Look for puff, fuzz, wool, or feathery softness."
2. [helpful, warm] "Fluffy means soft-looking, like clouds or dandelion seeds. Can you find a card that looks soft?"
3. [wait 2s] [encouraging] "I see some soft-looking friends. Which one should join our expedition first?"

**Screen:** `rules_scene` appears behind a simple catalog grid. The mission strip shows four collection slots: the dandelion exemplar slot is filled, and three empty fluffy-friend slots wait for choices. The progress indicator shows "0 of 3 friends chosen" as runtime UI text, not baked into art.

#### Step 3: Multi-Round Interaction

**Round 1 - First Fluffy Friend**

*(Runtime presents correct and distractor catalog cards. Child chooses one soft/fluffy card.)*

**AI says:** [excited discovery] "Ooh! You chose a soft-looking friend. What makes it look fluffy or soft?"

**Child responses:**

1. (Ideal) "It has fuzz!" / "It looks puffy!" / "It has soft feathers!"
2. (Unexpected) "It's green!" / "I like it!" / child names color or preference
3. (No response) Child taps a card but says nothing.

**AI follow-up:**

1. [delighted] "Yes, that soft clue belongs in our expedition. First fluffy friend found."
2. [warm, scaffolding] "You like it. Now look closely: is it fuzzy, puffy, woolly, or feathery?"
3. [wait 2s] [warm] "I see a soft clue on that card. Maybe fuzzy? You found your first fluffy friend."

**Screen:** `round_1_scene` appears. The selected card slides into the first empty collection slot. Progress updates to "1 of 3 friends chosen."

**Round 2 - Second Fluffy Friend**

*(Runtime keeps the first selected card visible and presents another small catalog spread.)*

**AI says:** [curious] "Another soft friend is hiding here. Which card has a soft clue too?"

**Child responses:**

1. (Ideal) "This one!" / "This one is fuzzier!" / child compares texture
2. (Unexpected) "It's pretty!" / "This one is big!" / child names another feature
3. (No response) Child points or taps silently.

**AI follow-up:**

1. [amazed] "Fuzzier! Soft can look different in different friends. Two fluffy friends are in your team."
2. [warm, guiding] "Pretty, yes. Does it also look soft, fuzzy, puffy, woolly, or feathery?"
3. [wait 2s] [gentle] "Let's compare it with your first card. Which one looks fuzzier?"

**Screen:** `round_2_scene` appears. The second selected card slides into the next slot. Progress updates to "2 of 3 friends chosen."

**Round 3 - Third Fluffy Friend**

*(Runtime presents the final selection spread.)*

**AI says:** [thrilled] "One more fluffy friend for the expedition. Which card should join, and what should we call it?"

**Child responses:**

1. (Ideal) "Cloud Puff!" / "Fuzzy Moss!" / "Softie!" / child invents a name
2. (Unexpected) "It's soft!" / "I found it!" / child does not name it
3. (No response) Child taps a correct card and smiles.

**AI follow-up:**

1. [celebrating] "[Name]! I love that. All 3 fluffy friends are here."
2. [warm, scaffolding] "So soft. What name fits this fluffy friend? Maybe Puffy, Cloudy, or Woolly?"
3. [wait 2s] [playful] "This fluffy friend needs a tiny name. I can call it Cloud Puff unless you pick one."

**Screen:** `round_3_scene` appears. The third selected card slides into the last slot with a gentle burst. Progress shows "3 of 3 friends chosen."

**STUCK BRANCH:** "Try one of the cards that looks soft, fuzzy, puffy, woolly, or feathery. Which one has a fluffy clue?"

#### Step 4: Celebration (Synthesis)

**AI says:** [amazed, storytelling voice] "Look at your fluffy team. Each friend has a soft clue. Would you like to give them tiny texture names?"

**Child responses:**

1. (Ideal) "Cloud Puff!" / "Fuzzy Friend!" / child names the cards
2. (Unexpected) "They're all soft!" / "I like them!"
3. (No response) Child looks at the collection quietly.

**AI follow-up:**

1. [delighted, narrating] "Cloud Puff, Fuzzy Friend, and [Name 3]. Three fluffy friends. What happens when they all meet?"
2. [warm, scaffolding] "All soft. Maybe this fuzzy one is Fuzzy Friend, and this puffy one is Cloud Puff. What do they do together?"
3. [wait 2s] [gentle, playful] "I think the fluffy friends might have a soft picnic. What do you think they do?"

**Child tells a tiny story** (or AI scaffolds): "They play!" / "They have a soft party!" / "They cuddle!"

**AI response to story:** [celebrating] "A fluffy party! Your soft friends met because they all share a fluffy clue."

**Screen:** `synthesis_scene` appears. The three selected cards and the dandelion exemplar form a small story path. `celebrate_scene` badge animates into the center after the child's story response.

**AI says:** [proud, ceremonial] "You are officially a Fluffy Expedition Explorer. You found a soft connection between different friends."

**Child responses:**

1. (Ideal) "Yay!" / "I'm an explorer!" / "More fluffy!"
2. (Unexpected) "Can we find rough things?" / "I like this one best."
3. (No response) Child smiles or claps while looking at the collection.

**AI follow-up:**

1. [celebration] "The best Fluffy Expedition Explorer. You found softness in your card team."
2. [warm, extending] "Rough things can be a new expedition. Today your soft friends made a fluffy team."
3. [wait 2s] [gentle] "What a wonderful expedition. You noticed so many soft clues."

**Screen:** Badge remains in the badge area. Selected cards stay visible as small insets. Use runtime UI text for the badge title if text is needed.

#### Step 5: Closing + IB Concepts

**AI says:** [warm, proud] "Fluffy Expedition Explorer, you did something amazing. You found different friends connected by one texture clue: fluffiness. That's Connection: noticing how different things can share something."

**Child responses:**

1. (Ideal) "Soft is everywhere!" / "I want more!" / "Fluffy!"
2. (Unexpected) "I want rough things!" / "Bye dandelion!"
3. (No response) Child waves or smiles at the screen.

**AI follow-up:**

1. [warm] "Softness can be in many places. Bye bye, Fluffy Explorer."
2. [warm, clear] "Rough things can be next. Today you found the soft connection. Bye bye, Fluffy Explorer."
3. [wait 2s] [gentle] "You were a wonderful explorer today. Bye bye, Fluffy Explorer."

**Screen:** `closing_scene` fills the round screen with the dandelion exemplar and selected fluffy cards arranged as a quiet collection. If unavailable, show selected card thumbnails and the spoken recap only.
