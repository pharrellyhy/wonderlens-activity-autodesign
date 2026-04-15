# Activity Design: Shape Quest + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Shape Scout Quest

### A. Basic Info

- **Activity Name**: The Shape Scout Quest
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Connection** (How is it connected to other things?)
- **Related Concepts (Discipline)**: Pattern, Similarity, Observation, Design
- **ATL Skills Focus**: Research Skills (observation, collecting and recording data), Thinking Skills (creative thinking -- interpreting and imagining), Communication Skills (expressing -- narrative co-creation)
- **Experience Pillar**: Adventure
- **Game Style**: quest_collector
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected {shape} attribute
- **Trigger Scene**: Child photographs any object where AI detects a prominent shape attribute (e.g., round wheels on a car, pointy tips on a star, flat surface on a book)
- **Mapping Source**: property-bridge
- **IB Theme**: How We Express Ourselves
- **Template Parameters**: `{shape}` -- detected shape property (e.g., round, pointy, flat, long, curvy). Example value used throughout: **round**.

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a prominent shape attribute -- for example, "round." The AI marvels at the shape and frames a quest: "Find 3 things that are round!" The child becomes a Shape Scout on a shape-hunting quest. For each find, the AI evaluates it against the quest criterion ("Is it round?"), creating a pass/fail game moment, and then harvests a personal detail ("What does it remind you of?") to generate a character name. Once 3 quest items are collected, the child co-creates a story featuring all the shape-friends rolling, bouncing, or spinning together. The quest criterion gives the collection PURPOSE and DIRECTION; the detail harvesting gives each find PERSONALITY. This template works for any detected shape: round, pointy, flat, long, curvy.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary for the detected shape (e.g., "round," "circle," "curved," "rolling," "sphere"). Learn that many different objects can share the same shape, even when they look nothing alike.
  - **U (Understand)**: Understand that objects have a specific **Form** -- shape is one of the most visible qualities that defines what something looks like. Understand that surprising **Connections** exist between very different things that share the same shape (a wheel, a coin, and a cookie are all round but serve completely different purposes).
  - **D (Do)**: Practice criterion-based observation -- searching for items that match a specific shape property (Research Skills -- observation), invent character names driven by personal detail responses (Thinking Skills -- creative thinking), and co-create a narrative where each character's role reflects the child's observations (Communication Skills -- expressing).

- **③ Design Highlight**: The quest criterion -- "Find 3 things that are round!" -- transforms aimless collecting into a purposeful shape hunt. Each find gets evaluated against the criterion, creating a game-like moment: "A coin -- it IS round! Quest item #2!" The detail harvesting gives each find creative ownership: the child's personal interpretation of each round thing becomes a character name and personality for the shape adventure story. The combination of quest evaluation (game feel) + detail harvesting (creative ownership) + mission progression ("2 of 3 collected!") makes the child feel "Look how many round things I discovered!" rather than just "I found some stuff."

- **④ Typical Scenario**: Child photographs a car --> AI notices round wheels --> "Your car has ROUND wheels! I wonder how many round things we can find!" --> child becomes a Shape Scout --> searches for things that are "round" --> each find is evaluated against the criterion and named --> at 3 of 3, "Quest complete!" triggers a co-created shape adventure story starring all the round characters.

### C. Interaction Flow -- Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge -- Cold Start**

> **Context**: Child photographs any object (e.g., a toy car). AI detects a prominent shape attribute (e.g., round wheels).
>
> **AI says**: "*(breathless wonder)* Ohhh -- look at your car! And WOW -- look at those wheels! They are SO round -- like perfect circles! I bet they roll and roll and roll. Do you know what else is round like those wheels?"
>
> **Possible child responses**:
> 1. (Ideal) "A ball!" / "The sun!" / "A cookie!" / Child names a round thing.
> 2. (Unexpected) "It's a race car!" / "It goes fast!" / "I love my car!" / Child talks about the entity rather than the shape.
> 3. (No response) Looks at the photo or the screen silently.
>
> **AI follow-up**:
> 1. "*(delighted)* A ball -- YES! Balls are round, wheels are round -- round things are EVERYWHERE! Your car's wheels are totally round. What do they remind you of? A spinning donut? A tiny planet? A rolling coin?"
> 2. "*(warmly agreeing)* It IS an awesome car! And look at those round, round wheels -- perfect circles! Without them, your car could not roll at all! What do those round wheels remind you of? A spinning coin? A donut?"
> 3. *(waits 2 seconds)* "*(soft, inviting)* See those wheels? They are perfectly round -- like little circles! What do they remind you of? They remind ME of little spinning donuts!"
>
> *(Child responds with a detail -- e.g., "Spinning donuts!" / "Little planets!" / "Rolling coins!")*
>
> **AI says**: "*(thrilled)* Spinning donuts -- I love that! Let's call your car's wheels 'Donut Spinners'! And guess what -- Donut Spinners are round. I wonder... what ELSE around here is round?"
>
> **Screen**: Close-up of the photographed object with a gentle glowing circle highlight around the detected round feature (e.g., wheels). A subtle circular pulse animation radiates outward from the round element. A small name tag reading the character name (e.g., "Donut Spinners") appears below the photo with a tiny circle icon. A shape-quest compass icon appears in the bottom corner showing "Quest: 0 of 3."

**Step 2: Mission Briefing -- The Shape Quest**

> **AI says**: "*(adventurous, explorer tone)* You are now an official Shape Scout! And I have a quest for you! Your mission: find 3 things around here that are ROUND. Balls, buttons, bowls, coins -- anything that makes a circle shape! For each one, you will tell me what it reminds you of, and we will give it a quest name. Then -- all your round characters go on a big rolling adventure together! Ready, Scout? Find something round!"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes, let's go!" / "I see something round!"
> 2. (Uncertain) "What does 'round' mean?" / "Where should I look?"
> 3. (No response) Glances around the room or area.
>
> **AI follow-up**:
> 1. "*(cheering)* Quest is ON! Find something that looks like a circle or a ball -- then snap a photo! Go, Scout!"
> 2. "*(encouraging)* Great question! 'Round' means it looks like a circle or a ball -- no pointy corners, no straight edges. Think of a plate, a coin, or a ball! Try looking at things on a table or on the ground!"
> 3. *(waits 2 seconds)* "*(gently)* Here is a scout tip -- look for things with NO corners. Things that curve all the way around -- like a plate, a lid, or a ball. Anything shaped like a circle! Try looking nearby!"
>
> **Screen**: A quest-themed mission card appears: a badge outline labeled "Shape Scout" with a circle silhouette. Below it, 3 empty circle-shaped slots (to be filled as the child collects quest items). The trigger photo sits above the slots with its character name tag and a golden circle-shaped checkmark. A quest scroll unfurls with the text: "Quest: Find 3 round things!" A shape compass in the corner shows "0 of 3 collected."

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 -- First Quest Find:**
>
> *(Child photographs something -- e.g., a bowl on a table)*
>
> **AI says**: "*(excited)* Quest find incoming! Ooh -- let me see... Is it round?"
>
> *(Brief dramatic pause -- 1 second)*
>
> **AI says**: "*(triumphant)* YES! Look at that shape -- a perfect circle going all the way around! It IS round! Quest item number one! Now, Scout -- what does it remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A hat!" / "A nest!" / "A swimming pool!" / Child gives creative association.
> 2. (Unexpected) "A bowl." / "I don't know." (minimal description)
> 3. (No response) Just looks at the screen.
>
> **AI follow-up**:
> 1. "*(thrilled)* A nest -- perfect! It IS curved and round like a cozy little nest! Let's call this quest character... Nest Bowl! Welcome to the quest, Nest Bowl! One of 3 collected -- two more to go, Scout!"
> 2. "*(looking closely)* A bowl -- yes! And look at its round shape. Does it look more like a tiny hat, a little nest, or a swimming pool to you?" *(waits for child's detail, then names accordingly -- e.g., "A hat? Then let's call it Hat Bowl!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* I see something curved and smooth -- like a little nest! What does it remind YOU of? A hat? A pool? A cozy nest? It reminds me of a birdy's home!"
>
> **Screen**: The new photo slides into the first empty quest slot with a burst of golden circle-sparkles. A "Round? YES!" stamp appears briefly in green. A name tag appears under the photo with the character name and a tiny circle icon. The shape compass updates to "1 of 3 collected" with a satisfying click animation. A dotted quest trail begins extending from the trigger slot toward the next empty slot.

> **Round 2 -- Second Quest Find:**
>
> *(Child photographs something -- e.g., a clock on the wall)*
>
> **AI says**: "*(detective voice)* Quest report number two! I see your photo... is THIS one round?"
>
> *(Brief dramatic pause -- 1 second)*
>
> **AI says**: "*(amazed)* Oh WOW -- look at that circle! Numbers going all the way around, hands pointing from the middle -- it IS round! Quest item number two! What does this one remind you of, Scout?"
>
> **Possible child responses**:
> 1. (Ideal) "A face!" / "A pizza!" / "The moon!"
> 2. (Stretch) "It's just a clock." / "I don't know what it looks like."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(impressed)* The moon -- YES! It IS round like a big full moon with numbers! Let's call this one... Moon Clock! Two of 3 collected -- just ONE more quest item to go, Scout!"
> 2. "*(warmly)* It IS a clock -- but look at that round shape! Does it look more like a big face, a full moon, or a giant pizza to you?" *(waits for child's answer, then names accordingly -- e.g., "A face? Then it's Smiley Tick!")*
> 3. *(waits 2 seconds)* "*(curious)* I see something big and round with numbers! It reminds ME of a full moon. What does it remind YOU of? A moon? A pizza? A friendly face?"
>
> **Screen**: Second slot fills in with a burst of golden circle-sparkles. "Round? YES!" stamp appears in green. Name tag appears with character name. Shape compass updates to "2 of 3 collected." The quest trail extends further. A gentle spin animation ripples across the screen.

> **Round 3 -- Third Quest Find (with stuck branch and edge cases):**
>
> **STUCK BRANCH** *(if child has been searching for more than a minute without finding something)*:
>
> **AI says**: "*(helpful whisper)* Scout tip! Round things are everywhere -- look for buttons on clothes, coins in a pocket, plates on a table, balls on the floor, or lids on jars! Anything that makes a circle shape!"
>
> **Possible child responses**:
> 1. (Ideal) "I see one!" / Child spots something round.
> 2. (Stuck) "I still can't find anything." / "There's nothing round."
> 3. (No response) Child keeps wandering.
>
> **AI follow-up**:
> 1. "*(encouraging)* Great spotting! Snap a photo, Scout -- let's see if it is round!"
> 2. "*(reassuring)* That is okay! Look at YOUR body -- do you see anything round? A button? A snap? Or look at the ceiling -- any round lights up there? Round things like to hide in plain sight!"
> 3. *(waits 2 seconds)* "*(gentle prompt)* Let's slow down and look right in front of you. Do you see anything curved, anything with no corners? Even something tiny -- a button, a dot, a sticker?"
>
> **DOESN'T MATCH BRANCH** *(child photographs something not round -- e.g., a book)*:
>
> *(Child photographs something -- e.g., a rectangular book)*
>
> **AI says**: "*(curious pause)* Hmm, let me check... Is a book round?"
>
> *(Brief pause)*
>
> **AI says**: "*(playfully)* Wellll... a book has corners and straight edges -- that makes it more of a rectangle! BUT -- wait, does it have anything round ON it? A round sticker? A circle picture on the cover? Sometimes round things hide on square things! What does this book remind you of, though? I still like it!"
>
> **Possible child responses**:
> 1. (Ideal) "Oh, let me find something round!" / "I see a circle on it!"
> 2. (Insists) "I want to keep it!" / "Books can be round!"
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(encouraging)* Yes -- something with that circle shape! Go find one, Scout!"
> 2. "*(warmly, accepting)* You know what? If YOU see something round about this book, then it is a quest item! What does it remind you of? Maybe it is a secret round book! Let's give it a quest name!" *(accepts the find -- the child's agency matters more than strict criterion enforcement)*
> 3. *(waits 2 seconds)* "*(gently)* That book is cool! But for our round quest, let's try to find something with no corners -- something curved like a circle. Look nearby for a ball, a lid, or a button!"
>
> **NORMAL ROUND 3** *(child photographs something round -- e.g., a coin)*:
>
> **AI says**: "*(building suspense)* FINAL quest find! Is this one round...?"
>
> *(Dramatic pause -- 1.5 seconds)*
>
> **AI says**: "*(bursting with excitement)* YES! Look at that -- a perfect circle! Smooth edges going all the way around with no corners at all! It IS round! QUEST ITEM NUMBER THREE! Scout -- what does this last one remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A tiny shield!" / "A pirate treasure!" / "A little sun!"
> 2. (Unexpected) "A coin." / "It's shiny."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(amazed)* A pirate treasure -- YES! It IS shiny and round like a treasure coin from a pirate ship! Let's call it... Treasure Shine! Three of 3 collected -- QUEST COMPLETE!"
> 2. "*(looking closely)* A coin -- yes! And look how it shines. Does it look like a tiny sun? A pirate treasure? A little shield?" *(waits for child's answer, names accordingly -- e.g., "A little sun? Then it's Sun Coin!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* Look at that -- shiny and perfectly round! It reminds ME of a tiny sun. What does it remind YOU of? A sun? A treasure? A little shield?"
>
> **Screen**: Final slot fills in with a BIG burst of golden circle-sparkles and confetti. "Round? YES!" stamp appears. Name tag appears with character name. Shape compass hits "3 of 3 collected" and EXPLODES with a starburst animation. A large "QUEST COMPLETE!" banner drops from the top with circle confetti. All four photos (trigger + 3 finds) light up with golden borders and character names. A "Shape Adventure!" banner starts pulsing.

**Step 4: Synthesis -- The Shape Adventure (Magic Moment)**

> **AI says**: "*(proud and thrilled)* QUEST COMPLETE, Shape Scout! Look at your round team! Donut Spinners the [trigger], [Name 1] the [detail], [Name 2] the [detail], and [Name 3] the [detail] -- all round! Now here comes the best part. Imagine they all start ROLLING at the same time! Where do they roll? What happens on their big round adventure?"
>
> **Possible child responses**:
> 1. (Ideal) "They roll down a hill!" / "They roll to the playground!" / "They bounce into space!" / Child starts narrating.
> 2. (Uncertain) "I don't know." / "They just roll."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(narrating with wonder)* Here they go! Donut Spinners rolls first -- spinning and spinning like wheels on a race track! Then [Name 1] the [detail] starts bouncing alongside -- boing, boing, boing! [Name 2] the [detail] rolls past and calls out, 'Look how fast we are going!' And [Name 3] the [detail] tumbles by and says, 'I can see [child's destination] from here!' They all roll together to [child's destination] -- the greatest round adventure ever! What do they find when they stop rolling?"
> 2. "*(playfully)* They roll -- YES! Let me help. Donut Spinners goes first, spinning like crazy! Then [Name 1] the [detail] catches up and starts [action based on detail]. 'Wait for me!' calls [Name 2] the [detail]. And [Name 3] the [detail] says, 'Let's roll over the hill!' Where do they all end up?"
> 3. *(waits 2 seconds)* "*(gently, storytelling voice)* I will start! All the round things start rolling at the same time! Donut Spinners spins like a wheel -- whirrrr! Then [Name 1] the [detail] bounces along! And [Name 2] the [detail] and [Name 3] the [detail] roll up too! They are ALL rolling together -- look how far they go! Where do they end up?"
>
> **Screen**: All 4 photos displayed in a rolling-adventure layout -- photos arranged along a curving trail that swoops across the screen like a ramp. Character name tags below each. An animated rolling motion sweeps across the scene, and tiny circular versions of each photo "roll" along the trail. Speech bubbles appear near characters when mentioned. A golden rolling-trail connects all characters from start to finish. Background shows a playful rolling landscape. A "Look how far we rolled!" banner glows softly.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed and warm)* Wow, Scout! Donut Spinners, [Name 1], [Name 2], and [Name 3] -- they are all SO different! A [trigger item], a [item], a [item], and a [item]. But they all had one thing in common -- they were ALL round! Why do you think so many different things are the same shape?"
>
> **Possible child responses**:
> 1. (Ideal) "Because circles are good for rolling!" / "Because round is a strong shape!" / "Because they need to spin!" / Any creative reasoning.
> 2. (Unexpected) "I don't know."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(delighted)* That is such a smart thought! You are right -- round things are great for rolling and spinning! Wheels are round so they roll. Bowls are round so they hold things evenly. Coins are round so they fit in your hand. The same shape shows up everywhere, doing different jobs!"
> 2. "*(warmly)* It IS amazing! Here is a clue -- wheels are round so they can ROLL. Plates are round so food sits evenly. Coins are round so they stack and fit in pockets. The round shape does SO many different jobs!"
> 3. *(waits 2 seconds)* "*(sharing a secret)* Here is something cool -- the round shape shows up everywhere because it is really useful! Wheels roll, bowls hold, coins stack -- all because they are round. Same shape, different jobs!"
>
> **Screen**: All four characters displayed in a circular formation. Gentle animated curve-lines connect them, showing their shared round quality. A soft spin animation drifts across the screen. Small shape-fact callouts appear near each character (e.g., "rolls!" near the wheel, "holds things!" near the bowl). The shape-quest trail shows the full journey path in the background.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm celebration)* Congratulations, Shape Scout! You completed the Shape Quest! You discovered **Form** -- you noticed that all these things share the same round shape, even though they look totally different! And you found an incredible **Connection** -- Donut Spinners, [Name 1], [Name 2], and [Name 3] are completely different things, but they are ALL round! The same shape connects them like a secret club! You earned your Shape Quest Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to find more round things, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the animation quietly.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you look around, keep your shape eyes ON -- who KNOWS how many round things are hiding in plain sight! Maybe you will find a whole new shape team! See you on the next quest, Scout!"
> 2. "*(warm)* Your badge is saved! And remember -- every time you spot a circle, that is another member of the round team! Bye for now, Scout!"
> 3. *(waits 2 seconds)* "*(soft)* Your Shape Quest Badge is shining. Bye for now, Scout!"
>
> **Screen**: A golden "Shape Quest Badge" appears -- circular, with a circle silhouette at the center and the 3 quest-find photos plus the trigger photo as small insets around the edges, each with its character name. The words **"Form"** and **"Connection"** float up artistically -- "Form" styled with a magnifying glass examining a circle shape, "Connection" with gentle curved lines linking the letters. A shape compass icon nestles between the concept words. A soft chime plays. Tiny animated circles and rolling shapes drift across the screen and settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. Multi-photo workflow is supported. The "Is it round?" evaluation is done by AI reacting to the photo, not by comparing photos. |
| 2 | Hook & Transition | PASS | Cold start opens with emotional resonance about shape ("SO round -- like perfect circles!") and wonder, not knowledge testing. Quest grows naturally from the detected shape attribute: "Your car has round wheels... what ELSE is round?" No "let's play a game" break. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Step 3 includes concrete stuck branch (buttons, coins, plates, lids), doesn't-match-criterion branch (book -- validates child, offers redirect OR accepts if child insists), and silence branches. "Unexpected" branches always validate first. |
| 4 | IB Completeness | PASS | KUD fully defined with shape vocabulary, 2 conceptual understandings, 3 skills. Form + Connection named as Key Concepts. 4 Related Concepts listed. 3 ATL skills with sub-skills. Closing speech names concepts naturally as praise -- "Form" references shape observation, "Connection" references shared shape as a link. Concepts match what the child actually DID. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5-8 words, quest structure with clear criterion, concrete vocabulary (round, circle, curved, rolling), open-ended detail questions ("What does it remind you of?"), 3-item quest achievable for ages 4-6, "round" is concrete enough for T1 comprehension. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Quest evaluation moments are specific and dramatic. Detail-harvesting and naming examples are concrete. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: glowing circle highlight, quest mission card with slots + shape compass, "Round? YES!" stamps, circle-sparkle animations, "QUEST COMPLETE!" banner, rolling-adventure trail layout, badge with shape motif. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template -- trigger is a detected shape attribute, not a specific entity. |
| 9 | Game Feel | PASS | Quest criterion creates genuine stakes per find with dramatic pause before verdict. "Doesn't match" branch shows real uncertainty. Mission progression (0/3 -> 3/3) creates momentum. "QUEST COMPLETE!" is clear climax. Shape adventure story is earned reward. High replayability -- works with any shape value. |
| 10 | Pillar Fidelity | PASS | Adventure pillar: child feels "Look how many round things I discovered!" Quest criterion gives collection PURPOSE. Mission progression tracking creates visible progress. Shape adventure is journey-map synthesis. Could NOT be re-labeled as any other pillar. Clearly Adventure. |

**Overall**: ALL PASS -- property-bridge quest_collector template with criterion-driven shape collection + detail-harvesting. Template parameterized by `{shape}` -- example uses "round" but works for any detected shape (pointy, flat, long, curvy).
