# Activity Design: Banana + Category 1 (Sustained Verbal Interaction)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: The Banana Time Machine

### A. Basic Info

- **Activity Name**: The Banana Time Machine
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Change, Causation
- **Related Concepts (Discipline)**: Journey, Growth, Systems, Discovery
- **ATL Skills Focus**: Thinking Skills (creative, transfer), Communication Skills (expressing, listening), Research Skills (observation)
- **Experience Pillar**: Adventure
- **Game Style**: `time_traveler`
- **Design Version**: 1.0
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Banana
- **Trigger Scene**: Child in the kitchen photographs a yellow banana sitting on the counter or table
- **Mapping Source**: none
- **IB Theme**: Where We Are in Place and Time (orientation, history, journeys)

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

- **① Brief Description**: The child becomes a "Time Pilot" who flies a magical time machine powered by the banana. Together, they travel backward and forward through time — visiting the banana months ago when it was a tiny green flower on a tropical plant, weeks ago when it was a plump green banana sailing across the ocean, yesterday when it sat on a store shelf hoping to be picked, and then forward to tomorrow and beyond. At a critical moment, the child makes a choice that branches the banana's future. At the end, the child sees the whole timeline assembled as a journey map — every stop the banana made through time.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: (1) Bananas start as small flowers on a tropical plant, (2) green bananas slowly turn yellow as they ripen, (3) bananas travel across oceans on ships before reaching stores, (4) "tropical" means warm and rainy, (5) bananas grow in bunches called "hands"
  - **U (Understand)**: (1) Living things change over time — what something looks like NOW is just one moment in a long journey (Change), (2) Each change happens for a reason — the sun makes it grow, the ocean voyage makes it ripen, your choice changes its future (Causation)
  - **D (Do)**: (1) Sequence events across a timeline from past to future, (2) Make and justify a choice about what happens next, (3) Describe how something looks and feels at different points in time

- **③ Design Highlight**: The banana is the "fuel" for a time machine. Each round is a specific TIME PERIOD — not just "the next chapter" but a distinct moment in time with a date/timeframe anchor ("Three months ago...", "Yesterday...", "Tomorrow..."). The child must imagine what the banana looked, felt, and experienced at EACH time stop. A genuine branching choice point ("Does your banana go to the fruit bowl or the smoothie machine?") creates real stakes — the child's decision determines what time period comes next. The magic moment is seeing all time stops assembled into a connected timeline map, giving the child the feeling of "Look how far we traveled through time!"

- **④ Typical Scenario**: A child photographs a banana in the kitchen. The AI launches a time machine adventure, traveling backward to the banana's origins and forward to its future, with the child imagining each era and making a choice that changes the banana's destiny. The timeline map at the end shows every stop.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a banana on the kitchen counter with no prior conversation.
>
> **AI says**: *(amazed whisper)* "Whoa... you found a banana! Look at that — so bright and yellow, like a little golden boomerang. But here's a secret... this banana hasn't always looked like this. A long, long time ago, it looked TOTALLY different. What do you think this banana looked like before it was yellow?"
>
> **Possible child responses**:
> 1. (Ideal) "It was green!" / "It was small!" / "It was on a tree!"
> 2. (Unexpected) "It was always yellow!" / "I don't know!" / "I want to eat it!"
> 3. (No response) Child is silent or looking at the screen.
>
> **AI follow-up**:
> 1. *(excited)* "Yes! This banana used to be SO different! It's changed a lot to get here. What if we could go back in time and SEE it? I know a way..."
> 2. *(playful, warm)* "You know what's funny? This banana actually WAS different before! It had a whole secret life. What if we could travel back in time and find out?"
> 3. *(wait 3 sec, then gentle prompt)* "I'll tell you a secret — this banana used to be tiny and green, way up on a tall plant in a hot, rainy jungle! Want to go see it?"
>
> **Screen**: Banana photo centered on screen with a soft golden glow pulsing around it. Faint clock hands spin slowly in the background. Tiny sparkles drift across the image.

**Step 2: Game Setup + Demo — "The Time Machine"**

> **AI says**: *(conspiratorial excitement)* "Guess what — your banana is actually a TIME MACHINE! If we hold on tight, it can take us zooming through time. Here's how it works — I'll spin the time dial, and we'll land at a different time. You tell me what you see! Ready? Let me show you... *WHOOOOSH!* We just landed THREE MONTHS AGO! The banana isn't a banana yet. It's a teeny tiny green flower, smaller than your thumb, on a BIG tall plant in a hot, rainy jungle. Rain is dripping everywhere. Can you hear it? *pitter-patter-pitter-patter.* What do you think this tiny flower feels like in all that rain?"
>
> **Possible child responses**:
> 1. (Ideal) "It feels wet!" / "It's warm!" / "It feels small!" / "It's happy in the rain!"
> 2. (Unexpected) "That's not a banana!" / "I don't like rain." / "Flowers are pink!"
> 3. (No response) Child is quiet.
>
> **AI follow-up**:
> 1. *(delighted)* "Yes! The little flower is {child's answer}! It's SO tiny but it's growing every single day because of all that rain and sunshine. That's where YOUR banana started! Now let's spin the time dial again and see what happens next..."
> 2. *(warm, validating)* "You're right, it doesn't LOOK like a banana yet! That's the wild thing about time — things change SO much. This tiny flower is going to slowly, slowly turn into the banana on your table. Let's spin the time dial and watch!"
> 3. *(wait 3 sec, encouraging)* "I think the flower might say, 'Ooh, the rain tickles!' It's warm and wet in the jungle. This tiny flower is going to grow into YOUR banana! Let's spin the time dial and see..."
>
> **Screen**: Screen splits — banana photo shrinks to top-right corner. Main area shows an illustrated jungle scene: a tall banana plant with a tiny green flower highlighted by a glowing circle. Rain drops animated falling. A "TIME DIAL" spinner graphic sits at the bottom of the screen showing "3 MONTHS AGO" in playful text. A dotted timeline begins forming at the very bottom of the screen with the first stop marked: a tiny flower icon.

**Step 3: Core Loop — Time Travel Rounds (3–4 rounds)**

> **Round 1 — "Six Weeks Ago: The Green Gang"**
>
> **AI says**: *(whooshing sound effect)* "*WHOOOOSH!* Spinning the time dial... we landed SIX WEEKS AGO! Oh look — the flower is gone! Now there's a bunch of green bananas hanging together. They look like a big green hand with banana fingers! Your banana is one of them — chubby, green, and NOT yellow yet. It's hanging upside down with all its banana brothers and sisters. They're all stuck together. Six weeks ago, what do you think your banana and its brothers are talking about up there?"
>
> **Possible child responses**:
> 1. (Ideal) "They're saying 'don't let go!'" / "They're talking about the birds!" / "They want to be yellow!"
> 2. (Unexpected) "Bananas don't talk!" / "I have a brother too!" / "Green is yucky!"
> 3. (No response) Child is quiet.
>
> **AI follow-up**:
> 1. *(laughing)* "Ha! I love that — '{child's answer}!' The green banana gang, all hanging together, chattering away. Did you know they're called a 'hand' of bananas? Your banana is one finger of that hand! But something big is about to happen — someone is coming to pick them..."
> 2. *(playful, connecting)* "That's so cool that you have a brother! Just like the banana has banana brothers! They all hang together in a bunch called a 'hand.' But soon, someone is going to come and pick the whole hand..."
> 3. *(wait 3 sec, prompting)* "Maybe they're saying, 'I wonder what it's like to be yellow!' or 'Don't let go!' They're all holding on tight. But guess what — someone is about to pick the whole bunch..."
>
> **Screen**: Illustrated scene: a bunch of green bananas hanging from a plant, drawn like cartoon friends with tiny faces. One banana (the child's) has a subtle glow. The TIME DIAL at the bottom shows "6 WEEKS AGO." The timeline at the bottom now has two stops: tiny flower → green bunch. A faint dotted line connects them.

> **Round 2 — "Two Weeks Ago: The Big Ocean Trip"**
>
> **AI says**: *(dramatic whoosh)* "*WHOOOOSH!* Time dial spinning... TWO WEEKS AGO! Whoa — your banana is on a HUGE ship, crossing the ocean! It's in a big, cold, dark room with thousands of other bananas. The ship rocks back and forth... *woooosh... woooosh.* The ocean is enormous and blue. And guess what's happening? Your banana is SLOWLY changing color. It's not all green anymore — it's starting to turn a little bit yellow! Like magic! Two weeks ago, on that big rocking ship, what do you think your banana sees when it peeks out at the ocean?"
>
> **Possible child responses**:
> 1. (Ideal) "It sees big waves!" / "Fish!" / "Other ships!" / "The sky is so big!"
> 2. (Unexpected) "I've been on a boat!" / "Bananas can't see!" / "I don't like the dark."
> 3. (No response) Child is silent.
>
> **AI follow-up**:
> 1. *(awed)* "Wow — {child's answer}! Your banana is having the ocean adventure of a lifetime! And the whole time, it's slowly turning yellow. The cold room on the ship is what makes it ripen. The cold is actually HELPING it change! Now let's spin ahead to see what happens next..."
> 2. *(warm, validating)* "You've been on a boat? Then you know what it's like — the rocking, the waves! Your banana is doing the same thing, rocking back and forth for days and days. And the whole time, it's slowly turning from green to yellow!"
> 3. *(wait 3 sec, painting the picture)* "I think the banana might peek out and see HUGE blue waves and maybe a dolphin jumping! And the whole time, it's slowly going from green... to greenish-yellow... to more yellow. The trip is changing it!"
>
> **Screen**: Illustrated cargo ship on a blue ocean with waves. A cross-section shows bananas inside, with the child's banana highlighted and a color gradient animation showing green slowly shifting toward yellow. TIME DIAL shows "2 WEEKS AGO." The timeline now has three stops: flower → green bunch → ship on ocean. Dotted lines connect them all. A subtle color bar under the banana icon shifts from green toward yellow.

> **Round 3 — "Yesterday: The Big Choice" (CHOICE POINT)**
>
> **AI says**: *(building suspense)* "*WHOOOOSH!* Time dial lands on... YESTERDAY! Your banana is in the store! It's sitting on a bright shelf under buzzy lights, all yellow and perfect. People walk by, looking at the fruit. Then — YOUR family walks in! They pick up your banana and put it in the cart. Hooray! But wait... when your banana gets home, something important happens. Your banana arrives at the kitchen and sees two places it could go. Over THERE is the fruit bowl — where it would sit and wait, getting even more ripe and sweet. And over HERE is the blender — where it could become a SMOOTHIE right away! Time Pilot, YOU get to decide — does your banana go to the **fruit bowl** or the **blender**?"
>
> **Possible child responses**:
> 1. (Choice A) "The fruit bowl!" / "It sits and waits!"
> 2. (Choice B) "The blender!" / "Smoothie!" / "I want a smoothie!"
> 3. (No response / unclear) Child is silent or says something unrelated.
>
> **AI follow-up**:
> 1. *(excited, honoring the choice)* "The FRUIT BOWL! Your banana sits proudly in the bowl, right on top, like the king of the fruit. It gets a little more ripe, a little more sweet, a tiny bit more spotty. It's been waiting all this time... and now it's waiting for YOU. It's sitting right here on your table, saying, 'Finally! I made it!' That's what you photographed — a banana that traveled through time to be RIGHT HERE."
> 2. *(excited, honoring the choice)* "The BLENDER! *BZZZZZZZZZ!* Your banana spins and whirls and mixes with milk and maybe some strawberries — WHOOOOSH — and it becomes a creamy, sweet, delicious smoothie! Your banana went from a tiny flower... to a green bunch... across the ocean... and now it's a SMOOTHIE! What a wild ending to its trip!"
> 3. *(wait 3 sec, offering the choice again gently)* "Hmm, this is the big decision! Your banana is standing at the kitchen counter. Should it go to the fruit bowl — *points left* — and wait to be eaten? Or should it jump in the blender — *points right* — and become a smoothie? Which one?"
>
> **Screen**:
> - Before choice: Store scene transitions to a kitchen. Two options displayed as large illustrated buttons — LEFT: a fruit bowl with the banana perched on top, glowing warmly; RIGHT: a blender with colorful fruit inside, whirring lines around it. Text above: "YOU DECIDE!" Both options pulse gently, inviting a tap or verbal answer.
> - After Choice A (Fruit bowl): The banana lands in the fruit bowl with a satisfied bounce. Small crown appears. The banana gets a few brown spots (ripening). The kitchen scene is warm and cozy.
> - After Choice B (Blender): The banana leaps into the blender with a *splash!* Whirling animation, colorful smoothie pours into a glass. Confetti pops. The smoothie glass has a little banana face smiling.
> - Timeline updates: fourth stop added — either "fruit bowl" icon or "smoothie" icon depending on choice. The line connects from ship → store shelf → chosen destiny.

> **Round 4 — "Tomorrow: What Comes Next?"**
>
> **AI says (Fruit Bowl path)**: *(curious, forward-looking)* "Now let's spin the time dial one MORE time... *WHOOOOSH!* TOMORROW! Your banana is still on the table. But it's a LITTLE bit different. It has a few more brown spots. It's softer. It's even sweeter than yesterday! Tomorrow, someone is going to pick it up and eat it. What do you think the banana will say right before someone takes the first bite?"
>
> **AI says (Blender path)**: *(curious, forward-looking)* "Now let's spin the time dial one MORE time... *WHOOOOSH!* TOMORROW! The smoothie glass is in the sink, all empty. But the banana's journey isn't over! The energy from that smoothie is inside someone's tummy, making them strong and fast. What do you think that person is doing tomorrow, powered by banana energy?"
>
> **Possible child responses (Fruit Bowl path)**:
> 1. (Ideal) "Eat me!" / "I'm yummy!" / "Thank you for waiting for me!"
> 2. (Unexpected) "I don't want it to be eaten!" / "Make banana bread!" / something unrelated
> 3. (No response) Child is silent.
>
> **Possible child responses (Blender path)**:
> 1. (Ideal) "Running fast!" / "Playing!" / "Being strong!"
> 2. (Unexpected) "I want a smoothie too!" / "Sleeping!" / something unrelated
> 3. (No response) Child is silent.
>
> **AI follow-up (Fruit Bowl path)**:
> 1. *(touched)* "Aww — '{child's answer}!' That banana traveled SO far and changed SO much, and now it gets to be part of YOU. Everything it went through — the jungle, the ship, the store — it all led to this moment!"
> 2. *(warm, validating)* "Ooh, {child's answer} — I love that idea! No matter what happens, this banana had the most amazing adventure. And tomorrow is just the next stop on its timeline!"
> 3. *(wait 3 sec, gentle)* "Maybe the banana says, 'I traveled SO far to get to you!' From a tiny flower to this moment — what a journey. And tomorrow is one more stop!"
>
> **AI follow-up (Blender path)**:
> 1. *(energetic)* "Yes! {child's answer}! All that banana energy — from the jungle sunshine, the ocean trip, the blender spin — it's all powering someone's big day tomorrow. The banana's journey keeps going, even as a smoothie!"
> 2. *(warm, playful)* "Ha — {child's answer}! Whatever they're doing, they've got banana power inside them. The banana traveled through so much time, and now its energy is still going!"
> 3. *(wait 3 sec, cheerful)* "I think someone is running around the playground tomorrow with banana energy! All that sunshine from the jungle is inside them now. The journey keeps going!"
>
> **Screen**:
> - Fruit Bowl path: The banana on the table with gentle morning light streaming in. A few brown spots visible. A hand reaches toward it. TIME DIAL shows "TOMORROW."
> - Blender path: An empty smoothie glass in a sunny kitchen. A child (silhouette) running/playing outside the window, with a subtle golden banana-shaped energy glow around them. TIME DIAL shows "TOMORROW."
> - Timeline updates: fifth stop added — "someone eating" icon or "running with energy" icon. The full timeline now stretches across the bottom of the screen with all five stops visible.

**Step 4: Payoff — The Magic Moment: "Your Banana's Timeline!"**

> **AI says**: *(grand, awestruck)* "Time Pilot... look at this. LOOK AT THIS! *ding ding ding!* You just traveled through the banana's WHOLE life — from the very beginning to tomorrow! Let's see the whole journey..."
>
> *(dramatic pause — 2 seconds)*
>
> *(proud narration)* "It started as a teeny tiny green flower in a hot, rainy jungle... then it grew into a green banana hanging with its brothers and sisters... then it sailed across a huge ocean on a big ship, slowly turning yellow... then it came to the store and YOUR family picked it up... then YOU chose — {fruit bowl / smoothie}! And tomorrow — {the next part of its story}! FIVE stops through time. That is ONE amazing journey for one little banana!"
>
> **Possible child responses**:
> 1. (Ideal) Child gasps, laughs, or says "Wow!" / "That's so cool!" / "We went so far!"
> 2. (Unexpected) "Can we do it again?" / "What about next year?" / "I want to go further!"
> 3. (No response) Child watches the screen with wide eyes.
>
> **AI follow-up**:
> 1. *(beaming)* "We traveled through time together! From the past all the way to tomorrow! And YOU were the pilot. You decided where the banana's story went!"
> 2. *(excited)* "You want to go FURTHER in time? I love it! That's what great Time Pilots do — they always wonder what's next. Maybe in a hundred years, banana plants will grow on the moon! But for now — look at this incredible timeline you built!"
> 3. *(wait 3 sec, warm)* "Pretty amazing, right? All those stops, all those changes. You flew through time and made it happen. That's your banana's timeline — and YOU built it!"
>
> **Screen**: This is the BIG MOMENT. The screen transforms into a full TIMELINE MAP stretching left to right:
> - **Stop 1** (far left): Tiny green flower on a tall plant, rain drops, jungle leaves. Label: "3 MONTHS AGO"
> - **Stop 2**: Green bunch of bananas hanging together like a hand. Label: "6 WEEKS AGO"
> - **Stop 3**: Cargo ship on blue ocean, banana turning yellow. Label: "2 WEEKS AGO"
> - **Stop 4**: Store shelf, then kitchen with the chosen path (fruit bowl OR blender). Label: "YESTERDAY"
> - **Stop 5** (far right): Tomorrow scene (eating OR banana energy). Label: "TOMORROW"
> - A glowing golden line connects all five stops, with a tiny animated banana character "flying" along the line from left to right, pausing at each stop.
> - Stars and sparkle effects burst when the banana reaches the final stop.
> - At the top: "THE BANANA'S TIMELINE" in bold, playful lettering.
> - The child's original banana photo is inset in the center, connected to Stop 4 with a "YOU ARE HERE" marker.
> - Celebration confetti falls. A gentle chime plays.

**Step 5: Celebration + IB Concepts**

> **AI says**: *(warm, reflective, then proud)* "You are officially a Time Pilot! You flew through time with one little banana and saw something amazing — this banana CHANGED at every single stop. It went from a flower, to green, to yellow, to {fruit bowl/smoothie} — always changing. That's the magic of Change — nothing stays the same forever, and every version is part of the story. And you know what else? Every change happened for a REASON. The rain made it grow. The ship made it ripen. And YOUR choice decided what happened next! That's called Causation — when one thing makes another thing happen. Pretty powerful for one little banana and one awesome Time Pilot, huh?"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I'm a Time Pilot!" / "Change is cool!"
> 2. (Unexpected) "What about other fruits?" / "Can I go to the future?" / "I want to play again!"
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. *(warm closing)* "The best Time Pilot I've ever flown with! Next time you see something — an apple, a flower, even a rock — you can wonder: what was its journey through time? See you next time, Time Pilot!"
> 2. *(encouraging)* "Great idea! Everything around you has a timeline — a journey through time. You can be a Time Pilot for ANYTHING. See you on the next flight!"
> 3. *(wait 3 sec, gentle closing)* "Every single thing around you has a timeline — a story of how it changed. You helped this banana tell its story. See you next time, Time Pilot!"
>
> **Screen**:
> - "TIME PILOT" badge appears center-screen with a golden banana-shaped compass rose, spinning gently.
> - Below the badge: "Change" and "Causation" in large, hand-drawn artistic lettering.
> - "Change" has an animated color gradient shifting from green to yellow to brown.
> - "Causation" has small illustrated arrows connecting icons: rain → growth, ship → ripening, choice → destiny.
> - The timeline map from Step 4 is miniaturized at the bottom as a keepsake.
> - Gold confetti drifts down. A warm chime sounds.
> - Final text fades in: "See you next time, Time Pilot!"

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state-change comparison, or non-speech audio detection required. All interaction is verbal. Single initial photo only. |
| 2 | Hook & Transition | PASS | Opens with emotional wonder ("like a little golden boomerang") and imaginative question ("what did it look like before?"), not knowledge testing. Transition to game grows naturally from curiosity about the banana's past. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 response branches (ideal, unexpected, no response). All unexpected responses are validated before redirecting. All no-response branches include wait time (3 sec) and gentle prompt. Choice point includes an unclear/no-response branch. |
| 4 | IB Completeness | PASS | Key Concepts: Change + Causation (both earned — child sees change at every stop and makes a causal choice). Related Concepts: Journey, Growth, Systems, Discovery. KUD fully specified with concrete items. ATL: Thinking (creative, transfer) + Communication (expressing, listening) + Research (observation). Closing names both concepts naturally as praise. |
| 5 | Tier Appropriateness | PASS | T1 (4–6): Sentences 5–8 words in AI prompts to child. Vocabulary is concrete (flower, green, yellow, ship, ocean, fruit bowl, blender). Tasks are 2–3 steps (listen to time period description → imagine → respond). Open-ended questions throughout. No abstract reasoning required. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. No abstract instructions like "AI guides" or "AI encourages." All responses are warm, playful, and child-appropriate. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animation, and visual elements. Timeline builds progressively. Choice point has before/after screens for both paths. Magic moment screen is richly detailed. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in assignment. |
| 9 | Game Feel | PASS | Genuine uncertainty at the choice point (fruit bowl vs. blender — child doesn't know what happens until they choose). The "WHOOOOSH" time travel creates drama and anticipation each round. The timeline assembly in Step 4 is a clear emotional climax ("wow, look how far we went!"). Replayable — different choice = different timeline. The time dial mechanic creates surprise at each landing. |
| 10 | Pillar Fidelity | PASS | Unmistakably Adventure pillar. Each round is a specific TIME PERIOD (3 months ago, 6 weeks ago, 2 weeks ago, yesterday, tomorrow) — not generic chapters. Genuine choice point branches the journey. Timeline visualization is the magic moment. Child feels "Look how far we traveled!" The emotional arc is journey + progress + destination. Could NOT be relabeled as another pillar — the time progression, choice branching, and timeline map are distinctively Adventure. |

**Overall**: ALL PASS — Ready for 教研 review

1 issue found and fixed during self-evaluation: Initial draft had Round 3 as a simple "store arrival" without a genuine choice point. Redesigned Round 3 as the CHOICE POINT (fruit bowl vs. blender) with branching consequences, making Round 4 path-dependent. This strengthened D9 (Game Feel) and D10 (Pillar Fidelity) by adding real stakes and genuine uncertainty.
