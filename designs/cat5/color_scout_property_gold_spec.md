# Activity Design: Color Scout + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Color Scout Quest

### A. Basic Info

- **Activity Name**: The Color Scout Quest
- **Activity Category**: 5 -- Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Connection** (How is it connected to other things?)
- **Related Concepts (Discipline)**: Pattern, Similarity, Observation, Identity
- **ATL Skills Focus**: Research Skills (observation, collecting and recording data), Thinking Skills (creative thinking -- interpreting and imagining), Communication Skills (expressing -- narrative co-creation)
- **Experience Pillar**: Adventure
- **Game Style**: quest_collector
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected {color} attribute
- **Trigger Scene**: Child photographs any object where AI detects a prominent color (e.g., a bright red toy, a blue backpack, a green leaf)
- **Mapping Source**: property-bridge
- **IB Theme**: How We Express Ourselves
- **Template Parameters**: `{color}` -- detected color property (e.g., red, blue, green, yellow, brown, orange, purple, pink, white, black). Example value used throughout: **red**.

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{color}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.appearance.color         # most common path (raincoat, crayon, piano, libraries, etc.)
  - tier_0.appearance.body_color    # e.g., rubber_duck, toy_robot, goldfish, lion, bird
  - tier_0.appearance.wing_color    # e.g., butterfly
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a prominent color -- for example, "red." The AI marvels at the color and frames a quest: "Find 3 red things!" The child becomes a Color Scout on a color-hunting quest. For each find, the AI evaluates it against the quest criterion ("Is it red?"), creating a pass/fail game moment, and then harvests a personal detail ("What does it remind you of?") to generate a character name. Once 3 quest items are collected, the child co-creates a story featuring the "Red Team" (or whatever color) going on an adventure together. The quest criterion gives the collection PURPOSE and DIRECTION; the detail harvesting gives each find PERSONALITY. This template works for any detected color: red, blue, green, yellow, brown, orange, purple, pink, etc.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary for the detected color and its shades (e.g., "red," "scarlet," "crimson," "bright," "dark red"). Learn that many different objects can share the same color, even when they serve completely different purposes.
  - **U (Understand)**: Understand that objects have a specific **Form** -- color is one of the most visible qualities that defines what something looks like and how we experience it. Understand that surprising **Connections** exist between very different things that share the same color (a fire truck, a strawberry, and a ladybug are all red but have nothing else in common).
  - **D (Do)**: Practice criterion-based observation -- searching for items that match a specific color property (Research Skills -- observation), invent character names driven by personal detail responses (Thinking Skills -- creative thinking), and co-create a narrative where each character's role reflects the child's observations (Communication Skills -- expressing).

- **③ Design Highlight**: The quest criterion -- "Find 3 red things!" -- transforms aimless collecting into a purposeful color hunt. Each find gets evaluated against the criterion, creating a game-like moment: "A strawberry -- it IS red! Quest item #2!" The detail harvesting gives each find creative ownership: the child's personal interpretation of each red thing becomes a character name and personality for the color adventure story. The combination of quest evaluation (game feel) + detail harvesting (creative ownership) + mission progression ("2 of 3 collected!") makes the child feel "Look at my amazing Red Team!" rather than just "I found some stuff."

- **④ Typical Scenario**: Child photographs a red toy --> AI notices bright red color --> "Your toy is SO red! I wonder if there are more red things hiding around here!" --> child becomes a Color Scout --> searches for things that are "red" --> each find is evaluated against the criterion and named --> at 3 of 3, "Quest complete!" triggers a co-created color adventure story starring the Red Team.

### C. Interaction Flow -- Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge -- Cold Start**

> **Context**: Child photographs any object (e.g., a red toy fire truck). AI detects a prominent color (e.g., bright red).
>
> **AI says**: "*(breathless wonder)* Ohhh -- look at your fire truck! And WOW -- it is SO red! Like the reddest red I have ever seen! Bright and bold and beautiful. I LOVE red. Do you know what else is red like your fire truck?"
>
> **Possible child responses**:
> 1. (Ideal) "A strawberry!" / "An apple!" / "A ladybug!" / Child names a red thing.
> 2. (Unexpected) "It has a ladder!" / "It goes nee-naw!" / "Firefighters ride it!" / Child talks about the entity rather than the color.
> 3. (No response) Looks at the photo or the screen silently.
>
> **AI follow-up**:
> 1. "*(delighted)* A strawberry -- YES! Strawberries are red, fire trucks are red -- red things are EVERYWHERE! Your fire truck is totally, completely red. What does it remind you of? A big red dragon? A fire-breathing superhero? A speedy tomato?"
> 2. "*(warmly agreeing)* It DOES go nee-naw! And it is SO bright and red -- you can see it from far away! That red color is like a shout -- LOOK AT ME! What does all that bright red remind you of? A dragon? A superhero cape?"
> 3. *(waits 2 seconds)* "*(soft, inviting)* Look at all that red! So bright and bold! What does it remind you of? It reminds ME of a big red dragon -- all fiery and brave!"
>
> *(Child responds with a detail -- e.g., "A big red dragon!" / "A superhero!" / "A tomato!")*
>
> **AI says**: "*(thrilled)* A big red dragon -- I love that! Let's call your fire truck 'Red Dragon'! And guess what -- Red Dragon is SUPER red. I wonder... what ELSE around here is red?"
>
> **Screen**: Close-up of the photographed object with a gentle glowing color highlight around the most prominently red area. A subtle red shimmer animation radiates outward from the object. A small name tag reading the character name (e.g., "Red Dragon") appears below the photo with a tiny red paint-drop icon. A color-quest compass icon appears in the bottom corner showing "Quest: 0 of 3."

**Step 2: Mission Briefing -- The Color Quest**

> **AI says**: "*(adventurous, explorer tone)* You are now an official Color Scout! And I have a quest for you! Your mission: find 3 things around here that are RED. Toys, clothes, flowers, food -- anything that is bright and red! For each one, you will tell me what it reminds you of, and we will give it a quest name. Then -- all your red characters join the Red Team and go on a big color adventure together! Ready, Scout? Find something red!"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes, let's go!" / "I see something red!"
> 2. (Uncertain) "What if it is only a little bit red?" / "Where should I look?"
> 3. (No response) Glances around the room or area.
>
> **AI follow-up**:
> 1. "*(cheering)* Quest is ON! Find something that has red on it -- then snap a photo! Go, Scout!"
> 2. "*(encouraging)* Great question! Even if it is only a LITTLE bit red, it still counts! A red stripe, a red dot, a red button -- any red at all! Try looking at your clothes, on the table, or near the door!"
> 3. *(waits 2 seconds)* "*(gently)* Here is a scout tip -- red things love to hide! Look at clothes, book covers, food packages, or toys. Even a tiny red sticker counts! Try looking nearby!"
>
> **Screen**: A quest-themed mission card appears: a badge outline labeled "Color Scout" with a red paint-drop silhouette. Below it, 3 empty circle-shaped slots (to be filled as the child collects quest items). The trigger photo sits above the slots with its character name tag and a golden red-bordered checkmark. A quest scroll unfurls with the text: "Quest: Find 3 red things!" A color compass in the corner shows "0 of 3 collected."

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 -- First Quest Find:**
>
> *(Child photographs something -- e.g., a red apple on the counter)*
>
> **AI says**: "*(excited)* Quest find incoming! Ooh -- let me see... Is it red?"
>
> *(Brief dramatic pause -- 1 second)*
>
> **AI says**: "*(triumphant)* YES! Look at that beautiful bright red color -- shiny and smooth and SO red! It IS red! Quest item number one! Now, Scout -- what does it remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A planet!" / "A bouncy ball!" / "A ruby jewel!" / Child gives creative association.
> 2. (Unexpected) "An apple." / "I don't know." (minimal description)
> 3. (No response) Just looks at the screen.
>
> **AI follow-up**:
> 1. "*(thrilled)* A ruby jewel -- perfect! It IS shiny and red like a precious ruby! Let's call this quest character... Ruby Crunch! Welcome to the Red Team, Ruby Crunch! One of 3 collected -- two more to go, Scout!"
> 2. "*(looking closely)* An apple -- yes! And look at that shiny red color. Does it look more like a bouncy ball, a ruby jewel, or a little red planet to you?" *(waits for child's detail, then names accordingly -- e.g., "A bouncy ball? Then let's call it Bouncy Red!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* I see something shiny and red -- like a little ruby! What does it remind YOU of? A jewel? A planet? A bouncy ball? It reminds me of a tiny treasure!"
>
> **Screen**: The new photo slides into the first empty quest slot with a burst of red sparkles and golden highlights. A "Red? YES!" stamp appears briefly in green. A name tag appears under the photo with the character name and a tiny red paint-drop icon. The color compass updates to "1 of 3 collected" with a satisfying click animation. A dotted quest trail begins extending from the trigger slot toward the next empty slot.

> **Round 2 -- Second Quest Find:**
>
> *(Child photographs something -- e.g., a red crayon)*
>
> **AI says**: "*(detective voice)* Quest report number two! I see your photo... is THIS one red?"
>
> *(Brief dramatic pause -- 1 second)*
>
> **AI says**: "*(amazed)* Oh WOW -- that is REALLY red! Deep and rich and bold -- like someone dipped it in a bucket of red paint! It IS red! Quest item number two! What does this one remind you of, Scout?"
>
> **Possible child responses**:
> 1. (Ideal) "A rocket!" / "A magic wand!" / "A little fire stick!"
> 2. (Stretch) "It's just a crayon." / "I don't know what it looks like."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(impressed)* A rocket -- YES! It IS long and pointy like a tiny red rocket, ready to blast off! Let's call this one... Red Rocket! Two of 3 collected -- just ONE more quest item to go, Scout!"
> 2. "*(warmly)* It IS a crayon -- but look at that amazing red color! Does it look more like a tiny rocket, a magic wand, or a little fire stick to you?" *(waits for child's answer, then names accordingly -- e.g., "A magic wand? Then it's Wand of Red!")*
> 3. *(waits 2 seconds)* "*(curious)* I see something long and red! It reminds ME of a tiny rocket. What does it remind YOU of? A rocket? A magic wand? A fire stick?"
>
> **Screen**: Second slot fills in with a burst of red sparkles and golden highlights. "Red? YES!" stamp appears in green. Name tag appears with character name. Color compass updates to "2 of 3 collected." The quest trail extends further. A gentle red shimmer animation ripples across the screen.

> **Round 3 -- Third Quest Find (with stuck branch and edge cases):**
>
> **STUCK BRANCH** *(if child has been searching for more than a minute without finding something)*:
>
> **AI says**: "*(helpful whisper)* Scout tip! Red things love to hide in plain sight! Look at your shirt -- any red? Check book covers, food labels, toy bins, or look for red buttons, red lids, or red stickers! Even a tiny bit of red counts!"
>
> **Possible child responses**:
> 1. (Ideal) "I see one!" / Child spots something red.
> 2. (Stuck) "I still can't find anything." / "There's nothing red."
> 3. (No response) Child keeps wandering.
>
> **AI follow-up**:
> 1. "*(encouraging)* Great spotting! Snap a photo, Scout -- let's see if it is red!"
> 2. "*(reassuring)* That is okay! Look really carefully at things you already see. Sometimes there is a red stripe, a red dot, or a red label that you did not notice at first. Red hides in tiny places!"
> 3. *(waits 2 seconds)* "*(gentle prompt)* Let's slow down and look right in front of you. Do you see ANY red -- even a tiny spot? A red letter? A red button? A red pattern on something?"
>
> **DOESN'T MATCH BRANCH** *(child photographs something not red -- e.g., a blue ball)*:
>
> *(Child photographs something -- e.g., a blue ball)*
>
> **AI says**: "*(curious pause)* Hmm, let me check... Is a blue ball red?"
>
> *(Brief pause)*
>
> **AI says**: "*(playfully)* Wellll... that looks more blue to me! Blue is a GREAT color, but our quest is looking for RED right now. BUT -- wait, does it have anything red ON it? A red stripe? A red dot? Sometimes red hides on other-colored things! What does this blue ball remind you of, though? I still like it!"
>
> **Possible child responses**:
> 1. (Ideal) "Oh, let me find something red!" / "I see a red stripe on it!"
> 2. (Insists) "I want to keep it!" / "It has a little red!"
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(encouraging)* Yes -- something bright and red! Go find one, Scout!"
> 2. "*(warmly, accepting)* You know what? If YOU see red on it, then it is a quest item! What does it remind you of? Maybe it is a secret red thing! Let's give it a quest name!" *(accepts the find -- the child's agency matters more than strict criterion enforcement)*
> 3. *(waits 2 seconds)* "*(gently)* That ball is cool! But for our red quest, let's try to find something that is mostly red. Look nearby for a red toy, a red cloth, or a red wrapper!"
>
> **NORMAL ROUND 3** *(child photographs something red -- e.g., a red sock)*:
>
> **AI says**: "*(building suspense)* FINAL quest find! Is this one red...?"
>
> *(Dramatic pause -- 1.5 seconds)*
>
> **AI says**: "*(bursting with excitement)* YES! Look at that -- red from top to bottom! Bright and bold and totally, completely RED! It IS red! QUEST ITEM NUMBER THREE! Scout -- what does this last one remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A superhero glove!" / "A sleeping bag for a mouse!" / "A red flag!"
> 2. (Unexpected) "A sock." / "It's soft."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(amazed)* A superhero glove -- YES! It IS all red and stretchy like a glove for a tiny superhero! Let's call it... Super Sock! Three of 3 collected -- QUEST COMPLETE!"
> 2. "*(looking closely)* A sock -- yes! And look at all that red. Does it look like a sleeping bag for a tiny mouse? A superhero glove? A little red flag?" *(waits for child's answer, names accordingly -- e.g., "A flag? Then it's Flag Red!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* Look at that -- so soft and SO red! It reminds ME of a tiny superhero glove. What does it remind YOU of? A glove? A sleeping bag? A little flag?"
>
> **Screen**: Final slot fills in with a BIG burst of red sparkles and golden confetti. "Red? YES!" stamp appears. Name tag appears with character name. Color compass hits "3 of 3 collected" and EXPLODES with a starburst animation. A large "QUEST COMPLETE!" banner drops from the top with red confetti. All four photos (trigger + 3 finds) light up with red-and-gold borders and character names. A "Red Team Adventure!" banner starts pulsing.

**Step 4: Synthesis -- The Red Team Adventure (Magic Moment)**

> **AI says**: "*(proud and thrilled)* QUEST COMPLETE, Color Scout! Look at your Red Team! Red Dragon the [trigger], [Name 1] the [detail], [Name 2] the [detail], and [Name 3] the [detail] -- all red! Now here comes the best part. The Red Team has a mission -- they are going on a big adventure together! What happens? Where does the Red Team go?"
>
> **Possible child responses**:
> 1. (Ideal) "They go to a castle!" / "They fly to the volcano!" / "They have a race!" / Child starts narrating.
> 2. (Uncertain) "I don't know." / "They just go."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(narrating with wonder)* The Red Team is GO! Red Dragon charges ahead first -- VROOM! Then [Name 1] the [detail] bounces alongside -- boing, boing! [Name 2] the [detail] zooms past and calls out, 'Follow me, Red Team!' And [Name 3] the [detail] dashes up and says, 'I can see [child's destination] from here -- it is so red and shiny!' They all arrive at [child's destination] together -- the greatest Red Team adventure EVER! What do they find there?"
> 2. "*(playfully)* They go -- YES! Let me help. Red Dragon leads the way -- VROOM! Then [Name 1] the [detail] catches up and starts [action based on detail]. 'Wait for me!' calls [Name 2] the [detail]. And [Name 3] the [detail] says, 'Red Team forever!' Where do they all end up?"
> 3. *(waits 2 seconds)* "*(gently, storytelling voice)* I will start! The Red Team sets off! Red Dragon goes first -- VROOM! Then [Name 1] the [detail] races after! And [Name 2] the [detail] and [Name 3] the [detail] catch up! They are ALL charging ahead together -- the whole Red Team! Where do they end up?"
>
> **Screen**: All 4 photos displayed in a team-adventure layout -- photos arranged along a swooping red trail that curves across the screen. Character name tags below each. An animated red energy trail sweeps across the scene, and tiny red-bordered versions of each photo "charge" along the trail. Speech bubbles appear near characters when mentioned. A golden-red trail connects all characters from start to finish. Background shifts from warm orange to deep red, showing adventure energy. A "Go, Red Team!" banner glows softly.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed and warm)* Wow, Scout! Red Dragon, [Name 1], [Name 2], and [Name 3] -- they are all SO different! A [trigger item], a [item], a [item], and a [item]. But they all had one thing in common -- they were ALL red! Why do you think so many different things are the same color?"
>
> **Possible child responses**:
> 1. (Ideal) "Because red is bright!" / "Because people like red!" / "Because red means stop!" / Any creative reasoning.
> 2. (Unexpected) "I don't know."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(delighted)* That is such a smart thought! You are right -- red IS bright and bold! Fire trucks are red so you can see them coming. Strawberries are red so birds and people know they are ripe. Stop signs are red so drivers pay attention. Red is a color that says LOOK AT ME!"
> 2. "*(warmly)* It IS amazing! Here is a clue -- red is one of the first colors people notice because it is SO bright. Fire trucks use red to be seen. Strawberries use red to say 'I am ready to eat!' The same color means different things on different things!"
> 3. *(waits 2 seconds)* "*(sharing a secret)* Here is something cool -- red shows up on SO many different things for different reasons! Fire trucks are red to be noticed. Apples turn red when they are ripe. Red is a color that tells you something important!"
>
> **Screen**: All four characters displayed in a circular formation. Gentle animated red color-wave lines connect them, showing their shared red quality. A soft warm shimmer drifts across the screen. Small color-fact callouts appear near each character (e.g., "bright and bold!" near the fire truck, "ripe and ready!" near the apple). The color-quest trail shows the full journey path in the background.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm celebration)* Congratulations, Color Scout! You completed the Color Quest! You discovered **Form** -- you noticed that all these things share the same red color, even though they look totally different! And you found an incredible **Connection** -- Red Dragon, [Name 1], [Name 2], and [Name 3] are completely different things, but they are ALL red! The same color connects them like a secret team! You earned your Color Quest Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to find more red things, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the animation quietly.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you look around, keep your color eyes ON -- who KNOWS how many red things are hiding in plain sight! Maybe you will find a whole new Red Team! See you on the next quest, Scout!"
> 2. "*(warm)* Your badge is saved! And remember -- every time you spot something red, that is another member of the Red Team! Bye for now, Scout!"
> 3. *(waits 2 seconds)* "*(soft)* Your Color Quest Badge is shining bright red. Bye for now, Scout!"
>
> **Screen**: A golden "Color Quest Badge" appears -- circular, with a red paint-drop silhouette at the center and the 3 quest-find photos plus the trigger photo as small insets around the edges, each with its character name. The words **"Form"** and **"Connection"** float up artistically -- "Form" styled with a magnifying glass examining a red color swatch, "Connection" with gentle red-tinted lines linking the letters. A color compass icon nestles between the concept words. A soft chime plays. Tiny animated red paint-drops and color-sparkles drift across the screen and settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. Multi-photo workflow is supported. The "Is it red?" evaluation is done by AI reacting to the photo, not by comparing photos. |
| 2 | Hook & Transition | PASS | Cold start opens with emotional resonance about color ("SO red -- like the reddest red I have ever seen!") and wonder, not knowledge testing. Quest grows naturally from the detected color attribute: "Your fire truck is SO red... what ELSE is red?" No "let's play a game" break. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Step 3 includes concrete stuck branch (clothes, book covers, food labels, toy bins), doesn't-match-criterion branch (blue ball -- validates child, offers redirect OR accepts if child insists), and silence branches. "Unexpected" branches always validate first. |
| 4 | IB Completeness | PASS | KUD fully defined with color vocabulary, 2 conceptual understandings, 3 skills. Form + Connection named as Key Concepts. 4 Related Concepts listed. 3 ATL skills with sub-skills. Closing speech names concepts naturally as praise -- "Form" references color observation, "Connection" references shared color as a link. Concepts match what the child actually DID. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5-8 words, quest structure with clear criterion, concrete vocabulary (red, bright, bold, shiny), open-ended detail questions ("What does it remind you of?"), 3-item quest achievable for ages 4-6, "red" is concrete enough for T1 comprehension. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Quest evaluation moments are specific and dramatic. Detail-harvesting and naming examples are concrete. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: glowing color highlight, quest mission card with slots + color compass, "Red? YES!" stamps, red sparkle animations, "QUEST COMPLETE!" banner, team-adventure trail layout, badge with color motif. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template -- trigger is a detected color attribute, not a specific entity. |
| 9 | Game Feel | PASS | Quest criterion creates genuine stakes per find with dramatic pause before verdict. "Doesn't match" branch shows real uncertainty. Mission progression (0/3 -> 3/3) creates momentum. "QUEST COMPLETE!" is clear climax. Red Team adventure story is earned reward. High replayability -- works with any color value. |
| 10 | Pillar Fidelity | PASS | Adventure pillar: child feels "Look at my amazing Red Team!" Quest criterion gives collection PURPOSE. Mission progression tracking creates visible progress. Color team adventure is journey-map synthesis. Could NOT be re-labeled as any other pillar. Clearly Adventure. |

**Overall**: ALL PASS -- property-bridge quest_collector template with criterion-driven color collection + detail-harvesting. Template parameterized by `{color}` -- example uses "red" but works for any detected color (blue, green, yellow, brown, orange, purple, pink, etc.).
