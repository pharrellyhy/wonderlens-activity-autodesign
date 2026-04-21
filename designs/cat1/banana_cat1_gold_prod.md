## The Banana Time Machine

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Banana Time Machine |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Change, Causation |
| Related Concepts | Journey, Growth, Systems, Discovery |
| ATL Skills Focus | Thinking Skills (creative, transfer), Communication Skills (expressing, listening), Research Skills (observation) |
| Game Style | time_traveler |
| Design Version | 2.0 |
| Last Updated | 2026-04-01 |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/food/tropical_fruits.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.color
  - tier_0.appearance.shape
  - tier_1.appearance.peel_spots
  - tier_1.context.store_display
  - tier_1.context.kitchen_counter_ripening
  - tier_1.function.cooking_mashing
  - tier_1.structure.fruit_sections
  - tier_2.appearance.curve_direction_and_reason
  - tier_2.change.brown_spots_sugar_change
  - tier_2.context.shipping_and_green_harvest
  - tier_2.context.bunch_position_effect
```

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Banana (e.g., plantain, fruit bowl, mango, pear) instead of a
banana itself. The neighbor list, bridge type, and initial bridge prompt live
in `data/constellation_map.yaml` under `mapped_entity: banana` — this section
describes how The Banana Time Machine adapts mechanically for a bridged entity.

**Preserve** — must not change across neighbors:
- The "Time Pilot" role_title and the 5-stop past→future timeline ("3 months ago → 6 weeks ago → 2 weeks ago → yesterday → tomorrow") — the journey-map magic moment depends on this span.
- The branching CHOICE POINT in Round 3 — the child's decision must genuinely route which Round 4 scene plays (Adventure pillar dies without real stakes).
- The "*WHOOOOSH!* spinning the time dial" transition between rounds — this ritual sound-cue makes each time-jump feel like piloting, not a slideshow.

**Swap** — re-phrase for the bridged entity:
- "Tropical jungle" origin → neighbor-appropriate origin (mango: "a mango tree in a warm orchard"; pear: "a pear tree in an autumn orchard"; plantain: "a tall plantain plant in the tropics"; fruit bowl: "each fruit in its own starting place" — becomes a multi-origin montage).
- Ripening-during-voyage plot ("green → yellow on the ship") → neighbor's ripening signature (mango: "green → golden-red, getting softer"; pear: "hard green → speckled and juicy"; plantain: rarely ripens to yellow for eating — swap to "gets even starchier, ready for frying").
- Round 3 CHOICE POINT "fruit bowl vs. blender" → two fates that make sense for the neighbor (mango: "sliced fresh vs. frozen in smoothies"; pear: "baked pie vs. raw crunch"; fruit bowl: "shared at a family snack vs. packed for a picnic").
- Round 1 "green banana gang on the plant, called a 'hand'" → neighbor's cluster/single-fruit reality (mango: "heavy single fruit hanging alone"; pear: "two or three pears swaying together").

**Watch** — gotchas to avoid:
- Fruit bowl is a CONTAINER, not one fruit — run the time machine for ONE featured fruit inside the bowl (let the child pick), or narrate parallel timelines (risk: too abstract for T1; default to picking one).
- Plantain's culinary path is usually cooked-green, not eaten-yellow — don't recycle the banana's ripening script wholesale; the "cold ship ripens it yellow" beat misleads for plantain.
- Never collapse the CHOICE POINT into a single pre-chosen path — if the neighbor has only one plausible fate, invent a fork (e.g., "eaten today vs. saved for tomorrow") so Causation still lands.

### B. Activity Overview

**① Brief Description**: The child becomes a "Time Pilot" who flies a magical time machine powered by the banana. Together, they travel backward and forward through time — visiting the banana months ago when it was a tiny green flower on a tropical plant, weeks ago when it was a plump green banana sailing across the ocean, yesterday when it sat on a store shelf hoping to be picked, and then forward to tomorrow and beyond. At a critical moment, the child makes a choice that branches the banana's future. At the end, the child sees the whole timeline assembled as a journey map — every stop the banana made through time.

**② Educational Purpose (KUD)**:
- **K (Know)**: (1) Bananas start as small flowers on a tropical plant, (2) green bananas slowly turn yellow as they ripen, (3) bananas travel across oceans on ships before reaching stores, (4) "tropical" means warm and rainy, (5) bananas grow in bunches called "hands"
- **U (Understand)**: (1) Living things change over time — what something looks like NOW is just one moment in a long journey (Change), (2) Each change happens for a reason — the sun makes it grow, the ocean voyage makes it ripen, your choice changes its future (Causation)
- **D (Do)**: (1) Sequence events across a timeline from past to future, (2) Make and justify a choice about what happens next, (3) Describe how something looks and feels at different points in time

**③ Design Highlight**: The banana is the "fuel" for a time machine. Each round is a specific TIME PERIOD — not just "the next chapter" but a distinct moment with a date/timeframe anchor ("Three months ago...", "Yesterday...", "Tomorrow..."). A genuine branching choice point ("Does your banana go to the fruit bowl or the blender?") creates real stakes — the child's decision determines what time period comes next. The magic moment is seeing all time stops assembled into a connected timeline map.

**④ Typical Scenario**: A child photographs a banana in the kitchen. The AI launches a time machine adventure, traveling backward to the banana's origins and forward to its future, with the child imagining each era and making a choice that changes the banana's destiny.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (amazed whisper) "Whoa... you found a banana! Look at that — so bright and yellow, like a little golden boomerang. But here's a secret... this banana hasn't always looked like this. A long, long time ago, it looked TOTALLY different. What do you think this banana looked like before it was yellow?"

**Child responses:**

1. (Ideal) "It was green!" / "It was small!" / "It was on a tree!"
2. (Unexpected) "It was always yellow!" / "I don't know!" / "I want to eat it!"
3. (No response) Child is silent or looking at the screen.

**AI follow-up:**

1. (excited) "Yes! This banana used to be SO different! It's changed a lot to get here. What if we could go back in time and SEE it? I know a way..."
2. (playful, warm) "You know what's funny? This banana actually WAS different before! It had a whole secret life. What if we could travel back in time and find out?"
3. (wait 3s) (gentle) "I'll tell you a secret — this banana used to be tiny and green, way up on a tall plant in a hot, rainy jungle! Want to go see it?"

**Screen:** Banana photo centered with golden glow pulsing around it. Faint clock hands spin in background. Tiny sparkles drift across the image.

#### Step 2: Rule Introduction + Demo

**AI says:** (conspiratorial excitement) "Guess what — your banana is actually a TIME MACHINE! If we hold on tight, it can take us zooming through time. Here's how it works — I'll spin the time dial, and we'll land at a different time. You tell me what you see! Ready? Let me show you... *WHOOOOSH!* We just landed THREE MONTHS AGO! The banana isn't a banana yet. It's a teeny tiny green flower, smaller than your thumb, on a BIG tall plant in a hot, rainy jungle. Rain is dripping everywhere. Can you hear it? *pitter-patter-pitter-patter.* What do you think this tiny flower feels like in all that rain?"

**Child responses:**

1. (Ideal) "It feels wet!" / "It's warm!" / "It feels small!" / "It's happy in the rain!"
2. (Unexpected) "That's not a banana!" / "I don't like rain." / "Flowers are pink!"
3. (No response) Child is quiet.

**AI follow-up:**

1. (delighted) "Yes! The little flower is {child's answer}! It's SO tiny but it's growing every single day because of all that rain and sunshine. That's where YOUR banana started! Now let's spin the time dial again and see what happens next..."
2. (warm, validating) "You're right, it doesn't LOOK like a banana yet! That's the wild thing about time — things change SO much. This tiny flower is going to slowly, slowly turn into the banana on your table. Let's spin the time dial and watch!"
3. (wait 3s) (encouraging) "I think the flower might say, 'Ooh, the rain tickles!' It's warm and wet in the jungle. This tiny flower is going to grow into YOUR banana! Let's spin the time dial and see..."

**Screen:** Banana photo shrinks to top-right corner. Main area shows illustrated jungle with a tiny green flower highlighted on a tall banana plant. Rain drops animated. TIME DIAL spinner shows "3 MONTHS AGO." Dotted timeline begins forming at bottom with first stop marked.

#### Step 3: Multi-Round Interaction

**Round 1 — "Six Weeks Ago: The Green Gang":**

**AI says:** (whooshing sound effect) "*WHOOOOSH!* Spinning the time dial... we landed SIX WEEKS AGO! Oh look — the flower is gone! Now there's a bunch of green bananas hanging together. They look like a big green hand with banana fingers! Your banana is one of them — chubby, green, and NOT yellow yet. It's hanging upside down with all its banana brothers and sisters. They're all stuck together. Six weeks ago, what do you think your banana and its brothers are talking about up there?"

**Child responses:**

1. (Ideal) "They're saying 'don't let go!'" / "They're talking about the birds!" / "They want to be yellow!"
2. (Unexpected) "Bananas don't talk!" / "I have a brother too!" / "Green is yucky!"
3. (No response) Child is quiet.

**AI follow-up:**

1. (laughing) "Ha! I love that — '{child's answer}!' The green banana gang, all hanging together, chattering away. Did you know they're called a 'hand' of bananas? Your banana is one finger of that hand! But something big is about to happen — someone is coming to pick them..."
2. (playful, connecting) "That's so cool that you have a brother! Just like the banana has banana brothers! They all hang together in a bunch called a 'hand.' But soon, someone is going to come and pick the whole hand..."
3. (wait 3s) (prompting) "Maybe they're saying, 'I wonder what it's like to be yellow!' or 'Don't let go!' They're all holding on tight. But guess what — someone is about to pick the whole bunch..."

**Screen:** Illustrated bunch of green bananas on a plant, drawn like cartoon friends. One banana (the child's) has a subtle glow. TIME DIAL shows "6 WEEKS AGO." Timeline at bottom has two stops: flower → green bunch, connected by dotted line.

**Round 2 — "Two Weeks Ago: The Big Ocean Trip":** The banana is on a huge cargo ship crossing the ocean in a cold, dark room with thousands of other bananas. The child imagines what the banana sees when it peeks at the ocean. AI reveals the banana is slowly turning from green to yellow during the voyage — the cold ship is what makes it ripen.

**Round 3 — "Yesterday: The Big Choice" (CHOICE POINT):** The banana arrives at the store, gets picked by the child's family, and comes home to the kitchen. The child faces a genuine choice: does the banana go to the **fruit bowl** (where it waits, ripens more, gets spotty) or the **blender** (where it becomes a smoothie immediately)? The choice determines what the next time stop looks like. Two illustrated option buttons appear on screen.

**Round 4 — "Tomorrow: What Comes Next?":** On the fruit bowl path, the banana is a little more spotty and sweet, waiting to be eaten — the child imagines what it says before the first bite. On the blender path, the smoothie is gone but the banana's energy is inside someone, making them strong — the child imagines what that person is doing tomorrow. Both paths celebrate how the journey continues.

#### Step 4: Celebration

**AI says:** (grand, awestruck) "Time Pilot... look at this. LOOK AT THIS! *ding ding ding!* You just traveled through the banana's WHOLE life — from the very beginning to tomorrow! Let's see the whole journey..."

*(dramatic pause — 2 seconds)*

(proud narration) "It started as a teeny tiny green flower in a hot, rainy jungle... then it grew into a green banana hanging with its brothers and sisters... then it sailed across a huge ocean on a big ship, slowly turning yellow... then it came to the store and YOUR family picked it up... then YOU chose — {fruit bowl / smoothie}! And tomorrow — {the next part of its story}! FIVE stops through time. That is ONE amazing journey for one little banana!"

**Child responses:**

1. (Ideal) Child gasps, laughs, or says "Wow!" / "That's so cool!" / "We went so far!"
2. (Unexpected) "Can we do it again?" / "What about next year?" / "I want to go further!"
3. (No response) Child watches the screen with wide eyes.

**AI follow-up:**

1. (beaming) "We traveled through time together! From the past all the way to tomorrow! And YOU were the pilot. You decided where the banana's story went!"
2. (excited) "You want to go FURTHER in time? I love it! That's what great Time Pilots do — they always wonder what's next. But for now — look at this incredible timeline you built!"
3. (wait 3s) (warm) "Pretty amazing, right? All those stops, all those changes. You flew through time and made it happen. That's your banana's timeline — and YOU built it!"

**Screen:** Full TIMELINE MAP stretching left to right with five stops: (1) tiny green flower/jungle — "3 MONTHS AGO," (2) green banana bunch — "6 WEEKS AGO," (3) ship on ocean — "2 WEEKS AGO," (4) store/kitchen with chosen path icon — "YESTERDAY," (5) tomorrow scene — "TOMORROW." Golden line connects all stops with an animated banana character flying along it. Child's original photo inset at center with "YOU ARE HERE" marker. Stars, confetti, and chime.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective) "You are officially a Time Pilot! You flew through time with one little banana and saw something amazing — this banana CHANGED at every single stop. It went from a flower, to green, to yellow, to {fruit bowl/smoothie} — always changing. That's the magic of Change — nothing stays the same forever, and every version is part of the story. And you know what else? Every change happened for a REASON. The rain made it grow. The ship made it ripen. And YOUR choice decided what happened next! That's called Causation — when one thing makes another thing happen. Pretty powerful for one little banana and one awesome Time Pilot, huh?"

**Child responses:**

1. (Ideal) "Yeah!" / "I'm a Time Pilot!" / "Change is cool!"
2. (Unexpected) "What about other fruits?" / "Can I go to the future?" / "I want to play again!"
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (warm closing) "The best Time Pilot I've ever flown with! Next time you see something — an apple, a flower, even a rock — you can wonder: what was its journey through time? See you next time, Time Pilot!"
2. (encouraging) "Great idea! Everything around you has a timeline — a journey through time. You can be a Time Pilot for ANYTHING. See you on the next flight!"
3. (wait 3s) (gentle closing) "Every single thing around you has a timeline — a story of how it changed. You helped this banana tell its story. See you next time, Time Pilot!"

**Screen:** "TIME PILOT" badge centered with golden banana-shaped compass rose. "Change" and "Causation" in large hand-drawn lettering below. "Change" has green-to-yellow gradient animation. "Causation" has small illustrated arrows connecting icons: rain → growth, ship → ripening, choice → destiny. Miniaturized timeline map at bottom. Gold confetti and warm chime.
