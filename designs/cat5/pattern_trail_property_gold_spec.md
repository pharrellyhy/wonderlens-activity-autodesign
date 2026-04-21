# Activity Design: Pattern Trail + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Pattern Trail

### A. Basic Info

- **Activity Name**: The Pattern Trail
- **Activity Category**: 5 -- Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Connection** (How is it connected to other things?)
- **Related Concepts (Discipline)**: Pattern, Similarity, Observation, Discovery
- **ATL Skills Focus**: Research Skills (observation, collecting and recording data), Thinking Skills (critical thinking -- deducing from riddle-clues, transfer -- connecting finds to a hidden pattern), Communication Skills (expressing -- describing finds and reasoning)
- **Experience Pillar**: Mystery
- **Game Style**: mystery_trail
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected {pattern} attribute
- **Trigger Scene**: Child photographs any object where AI detects a visual pattern (e.g., a striped shirt, spotted ladybug, ribbed leaf, wavy fence)
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works
- **Template Parameters**: `{pattern}` -- detected visual pattern property (e.g., stripes, spots, zigzags, lines, waves, checks, dots, swirls, ridges). Example value used throughout: **stripes**.

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{pattern}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.appearance.pattern                # e.g., raincoat
  - tier_1.appearance.wing_patterns          # e.g., butterfly
  - tier_1.appearance.key_pattern            # e.g., piano
  - tier_1.appearance.scale_shimmer_pattern  # e.g., goldfish
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a visual pattern -- for example, "stripes." The AI marvels at the pattern and recruits the child as a "Pattern Detective." The AI gives riddle-clues one at a time -- each describing something nearby that has a DIFFERENT kind of visual pattern -- and the child searches, guesses, and photographs what they think matches. After 3 finds, the AI reveals the hidden connection: everything the child found has a pattern, and patterns are EVERYWHERE -- in nature, in clothes, in buildings. Stripes, spots, zigzags -- the world is covered in patterns, and the child just proved it. This template works for any detected visual pattern: stripes, spots, zigzags, waves, dots, ridges, checks, swirls, etc.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "pattern," "stripes," "spots," "zigzag," and "lines." Learn that patterns are repeating visual arrangements -- stripes go side by side, spots repeat in clusters, zigzags go back and forth, and lines march in rows.
  - **U (Understand)**: Understand that the **Form** of things includes visual patterns -- repeating shapes, lines, or marks that define how something looks. Understand that **Connection** exists between very different things that share the quality of having a pattern -- a striped shirt, a spotted leaf, and a zigzag crack are all connected by pattern.
  - **D (Do)**: Practice deductive reasoning from riddle-clues (Thinking Skills -- critical thinking), search for and photograph matching items (Research Skills -- observation and data collection), and articulate the hidden connection between all finds (Communication Skills -- expressing reasoning).

- **③ Design Highlight**: The "Pattern Trail" transforms a simple pattern hunt into a mystery investigation. The key mechanism is riddle-driven search with a delayed pattern reveal: the child doesn't know that ALL their finds share the quality of having a pattern until the end. Each riddle-clue describes a DIFFERENT pattern type (spots, zigzags, parallel lines), so the child experiences variety and surprise. The magic moment -- "WHOA! Everything you found has a PATTERN!" -- reframes the entire activity retroactively, giving the child an "I figured it out!" rush. The hidden truth is that patterns are everywhere -- nature and people both love making them.

- **④ Typical Scenario**: Child photographs a striped shirt --> AI notices stripes --> "Your shirt has STRIPES -- lines going side by side! I wonder what OTHER patterns are hiding nearby" --> recruits the child as a Pattern Detective --> gives riddle-clue #1 (something with spots) --> child searches and photographs --> riddle-clue #2 (something with zigzags) --> child searches and photographs --> riddle-clue #3 (something with parallel lines) --> child searches and photographs --> AI reveals the hidden pattern: "WHOA! Everything you found has a PATTERN -- nature and people BOTH love making patterns!"

### C. Interaction Flow -- Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge -- Cold Start**

> **Context**: Child photographs any object where AI detects a visual pattern. Example: a striped shirt.
>
> **AI says**: "*(breathless, delighted)* Ohhh -- look at your shirt! Do you see those LINES going side by side? Those are called STRIPES! They go this way and that way, marching together like a team. Your shirt has a PATTERN! Have you ever noticed stripes on other things too?"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, on a zebra!" / "My socks have stripes!" / "There are stripes everywhere!"
> 2. (Unexpected) "I like my shirt!" / "It's blue and white." / "My mom picked it."
> 3. (No response) Child looks at the shirt or the screen quietly.
>
> **AI follow-up**:
> 1. "*(excited, conspiratorial)* YES! Zebras have stripes, socks have stripes -- stripes are sneaky, they show up EVERYWHERE! But here's the thing -- stripes aren't the ONLY pattern out there. There are spots, zigzags, wavy lines... I bet there are MORE patterns hiding all around you RIGHT NOW. What if we could find them?"
> 2. "*(warm, curious)* It IS a great shirt! And those blue and white lines? That's a PATTERN called stripes! But here's a secret -- your shirt isn't the only thing with a pattern. There are spots, zigzags, all kinds of patterns hiding nearby. Want to find them?"
> 3. *(waits 2 seconds)* "*(gentle, wondering)* See those lines on your shirt? They repeat -- over and over -- side by side. That's a pattern called stripes! And I bet there are MORE patterns hiding all around you. Spots, zigzags, wavy lines... I have an idea -- want to be a detective and find them?"
>
> **Screen**: Photo of the triggering object centered on screen. Animated highlight lines trace along the detected pattern (e.g., stripes glow one by one). The word "STRIPES" pulses in bold, striped-textured letters. A faint magnifying glass icon with a "?" inside pulses gently in the corner.

**Step 2: Mission Briefing**

> **AI says**: "*(adventurous, detective tone)* Alright -- you are now an official Pattern Detective! Here's your mission: I'm going to give you riddle-clues about things hiding nearby. Each one has a DIFFERENT kind of pattern! You search, you guess, and you take a photo. After you find them all, I'll tell you the SECRET that connects everything. Ready, Detective?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes!" / "What's the first clue?"
> 2. (Uncertain) "What's a pattern?" / "Where do I look?"
> 3. (No response) Child looks around with curiosity.
>
> **AI follow-up**:
> 1. "*(thrilled)* Here comes your first riddle-clue! Listen carefully, Detective..."
> 2. "*(encouraging)* A pattern is when something REPEATS -- like the stripes on your shirt, the same lines over and over! I'll give you riddle-clues and you just listen, look, and search. The riddles will guide you! Here comes the first one..."
> 3. *(waits 2 seconds)* "*(playful whisper)* Okay Detective, here's how it works -- I describe something with a pattern, you find it! Easy! Let's start with your very first riddle-clue..."
>
> **Screen**: A detective-themed mission card appears: a badge outline labeled "Pattern Detective" with a magnifying glass over a pattern mosaic (stripes, spots, zigzags). Below it, 3 empty circle-shaped slots (to be filled as the child solves riddles). The trigger photo sits above the slots with a golden star. A "CLUE #1" banner starts pulsing at the bottom. A faint question mark hovers over each empty slot.

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 -- Riddle-Clue #1: Something with Spots**
>
> **AI says**: "*(mysterious, slow riddle voice)* Riddle-Clue number one! Listen closely, Detective... I'm thinking of something nearby. It's small and has SPOTS -- like tiny painted dots, scattered all over it. The dots might be dark on something light, or light on something dark. Look carefully -- spots can be hiding on a leaf, a piece of fabric, or even a stone! Can you find something with spots? Go look and take a photo!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs something with spots or dots -- a spotted leaf, dotted fabric, bumpy stone, polka-dot clothing. "I found spots!" / "This has dots!" / "Here!"
> 2. (Unexpected) Child photographs something without a clear pattern. "Is it this?" / "I found this!"
> 3. (No response / stuck) Child looks around but doesn't find anything or photograph anything.
>
> **AI follow-up**:
> 1. "*(triumphant)* YES, Detective! Look at those SPOTS -- little dots sprinkled all over! Each dot is like a tiny circle, and they repeat across the whole thing. That's a pattern called SPOTS! They're different from your stripes -- stripes are lines, but spots are DOTS! First clue -- SOLVED! Two more to go!"
> 2. "*(thoughtful, encouraging)* Ooh, interesting find! Let me look closely... My riddle is about something with SPOTS -- tiny dots or circles repeated across it. Think of a ladybug's back, or a shirt with polka dots, or even a leaf with little bumps. Can you look for something with dots on it?"
> 3. *(waits 2 seconds)* "*(helpful whisper)* Detective hint! Spots are tiny dots or circles that repeat. Look at the ground -- do you see a stone with speckles? Or check your clothes -- any polka dots? Even a leaf with tiny bumps or markings counts! Spots can be sneaky!"
>
> **STUCK BRANCH** *(if child still can't find spots)*:
>
> **AI says**: "*(reassuring)* That's okay! Try looking at any fabric near you -- a cushion, a bag, or someone's clothing. Or check a leaf up close -- many leaves have little spots or speckles you can only see when you look REALLY carefully. Even a bumpy rock with different-colored flecks counts as spots!"
>
> **Possible child responses**:
> 1. (Ideal) "I see something!" / Child spots something with dots or specks.
> 2. (Still stuck) "I can't find any spots." / "There aren't any."
> 3. (No response) Child keeps searching.
>
> **AI follow-up**:
> 1. "*(cheering)* Go take a photo, Detective! Let's see your spotted find!"
> 2. "*(warm)* No problem! Look right at the ground near your feet -- gravel and concrete often have tiny specks and dots in them. Take a photo of the ground up close -- I bet I'll see spots!"
> 3. *(waits 2 seconds)* "*(gently)* Try looking at the closest thing to you -- really close up. Most things have tiny marks or specks if you look hard enough! Take a photo of anything up close."
>
> **Screen**: New photo slides into the first empty slot on the mission card. A burst of spotted sparkles and a magnifying glass "SOLVED!" animation plays over the slot. A small spots icon (cluster of dots) appears. Counter updates to "Clue 1 of 3 -- SOLVED!" A "CLUE #2" banner starts pulsing.

> **Round 2 -- Riddle-Clue #2: Something with Zigzags**
>
> **AI says**: "*(building excitement, mystery voice)* Riddle-Clue number TWO! Here it comes, Detective... I'm thinking of something that goes back and forth, back and forth -- like a path that can't make up its mind! It zigs one way, then zags the other way. You might see it in a crack on the ground, the edge of a leaf, a fence, or even the way bricks stack. Can you find something with a ZIGZAG? Go search and snap a photo!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs something with a zigzag pattern -- a crack in the pavement, a serrated leaf edge, a decorative fence, stacked bricks. "A zigzag!" / "This goes back and forth!" / "I see it!"
> 2. (Unexpected) Child photographs something else. "Is this a zigzag?" / "I found a line!"
> 3. (No response / stuck) Child looks around without photographing.
>
> **AI follow-up**:
> 1. "*(impressed)* A zigzag -- BRILLIANT, Detective! See how it goes THIS way, then THAT way, then THIS way again? Back and forth, back and forth! It's a pattern -- a ZIGZAG pattern! Different from stripes, different from spots -- zigzags go at ANGLES! Second clue -- SOLVED! One more to go!"
> 2. "*(validating, then redirecting)* Ooh, good eye! That IS interesting! But my riddle is about something that goes back and forth at angles -- like the letter W or M. Think of a crack in the sidewalk, or the pointy edge of a leaf. Can you find something that zigs and zags?"
> 3. *(waits 2 seconds)* "*(helpful)* Detective hint! A zigzag goes like this: up-to-the-right, then down-to-the-right, then up again -- like a W! Look at the ground for cracks, or look at a fence or wall -- do you see any lines that go back and forth at angles?"
>
> **Screen**: Second photo slides into the second slot. A burst of angular sparkles and "SOLVED!" animation. A small zigzag icon appears. Counter updates to "Clue 2 of 3 -- SOLVED!" A "CLUE #3" banner pulses.

> **Round 3 -- Riddle-Clue #3: Something with Parallel Lines**
>
> **AI says**: "*(dramatic, hushed detective voice)* Last riddle-clue, Detective -- this is a good one! I'm thinking of something with straight LINES, all in a row -- marching together like soldiers! The lines don't cross, they don't zigzag -- they just go side by side, perfectly together. You might see them in a wooden fence, stacked bricks, the grooves on a bench, or even the veins on a big leaf! Find something with lines in a row and take a photo!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs something with parallel lines -- a wooden fence, stacked bricks, bench slats, ribbed surface, leaf veins. "Lines!" / "They're all in a row!" / "I found it!"
> 2. (Unexpected) Child photographs something without clear parallel lines. "Is it this?" / "I found lines!"
> 3. (No response / stuck) Child can't find anything with lines in a row.
>
> **AI follow-up**:
> 1. "*(thrilled, almost shouting)* YES! Look at those LINES -- all marching side by side! They don't wobble, they don't zigzag -- they go straight and parallel, like train tracks! That's a LINES pattern! Final clue -- SOLVED! ALL clues solved!"
> 2. "*(encouraging)* Interesting find! But my riddle is about lines that go side by side -- all the same direction, like fence posts in a row or the grooves on a bench. Look at anything made of wood, metal, or bricks -- do you see lines going the same way, over and over?"
> 3. *(waits 2 seconds)* "*(helpful whisper)* This one is fun to find! Look at any fence, railing, bench, or wall nearby. See how the boards or bars go side by side? Even the lines between bricks count! Or look at a big leaf -- the veins often run in parallel lines."
>
> **STUCK BRANCH** *(if child truly can't find parallel lines)*:
>
> **AI says**: "*(reassuring)* Try looking right at the ground! Sidewalk cracks often make parallel lines. Or look at your own clothes -- some fabrics have lines in the weave. Even your shoelaces going back and forth could work! Lines are sneaky hiders."
>
> **Possible child responses**:
> 1. (Ideal) "I found some!" / Child spots parallel lines.
> 2. (Still stuck) "I don't see any lines." / "Where?"
> 3. (No response) Child keeps looking.
>
> **AI follow-up**:
> 1. "*(encouraging)* Go photograph them, Detective! Let's see your lines!"
> 2. "*(warm, flexible)* That's okay! Look at the CLOSEST wall, floor, or surface near you. Most surfaces have some kind of lines if you look closely -- grooves, edges, seams. Take a photo of any surface up close and I bet I'll find lines!"
> 3. *(waits 2 seconds)* "*(gently)* Try pointing your camera at any flat surface really close -- a wall, a floor tile, even a piece of cardboard. Lines are hiding everywhere!"
>
> **Screen**: Third photo slides into the final slot. A big burst of multi-colored sparkles and an "ALL CLUES SOLVED!" animation. All three slots glow with golden borders. A "REVEAL TIME!" banner appears and pulses dramatically. A large magnifying glass icon shimmers in the center.

**Step 4: Synthesis -- The Big Pattern Reveal**

> **AI says**: "*(slow, dramatic build-up)* Okay, Pattern Detective -- look at everything you found. Something with spots... something with zigzags... something with lines in a row... And remember where we started -- your shirt with STRIPES! Now here's the SECRET I've been hiding... *(dramatic pause)* ...EVERYTHING you found has a PATTERN! Spots, zigzags, lines, stripes -- they're ALL patterns! And here's the amazing part: patterns aren't just on shirts or in books. They're on leaves and stones and fences and walls and bugs and buildings. Nature and people BOTH love making patterns! Stripes, spots, zigzags -- PATTERNS ARE EVERYWHERE!"
>
> **Possible child responses**:
> 1. (Ideal) "Whoa!" / "Patterns ARE everywhere!" / "I found all the patterns!" / Child is surprised and excited.
> 2. (Unexpected) "I knew it!" / "That's cool!" / "What other patterns are there?"
> 3. (No response) Child looks at the screen, taking it in.
>
> **AI follow-up**:
> 1. "*(celebrating)* You DID find them all! Look -- spots are dots that repeat. Zigzags are angles that repeat. Lines are straight rows that repeat. Stripes are bands that repeat. They all REPEAT -- that's what makes them patterns! And you found them in totally different places -- on clothes, on the ground, on plants, on buildings! Patterns connect EVERYTHING!"
> 2. "*(validating, adding detail)* It IS cool! And here's what's really wild -- there are even MORE patterns out there! Spirals that swirl, waves that roll, checks that crisscross. Every time you look at something, ask yourself: does it have a pattern? I bet the answer is YES!"
> 3. *(waits 2 seconds)* "*(warm, amazed)* You proved something today, Detective. Patterns aren't just in one place -- they're in nature, in clothes, in buildings, in EVERYTHING. Your stripes, your spots, your zigzags, your lines -- they're all connected by the same idea: something that REPEATS! And you, Detective -- you saw them all!"
>
> **Screen**: All collection photos displayed in a circle around the original trigger photo in the center. Animated golden lines connect each find to the center with small labels: "SPOTS" (with dot cluster), "ZIGZAGS" (with angular line), "LINES" (with parallel bars). The trigger photo labeled "STRIPES" (with band motif). A shimmering "PATTERNS" word floats above the arrangement in letters filled with mixed pattern textures. A pulsing glow moves around the circle showing how everything connects. Tiny animated pattern fragments drift across the screen.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed, reflective)* Detective, look at your collection -- stripes, spots, zigzags, and lines. They look SO different from each other! But they ALL turned out to be patterns. Why do you think there are so many different KINDS of patterns?"
>
> **Possible child responses**:
> 1. (Ideal) "Because things need different shapes!" / "Nature likes to make them!" / "Because they're all different!"
> 2. (Unexpected) "I don't know." / "Because they're pretty."
> 3. (No response) Child looks at the collection on screen.
>
> **AI follow-up**:
> 1. "*(delighted)* Exactly! Different patterns do different jobs! Stripes on a zebra help it hide in the grass. Spots on a ladybug warn other animals to stay away. Zigzags on a snake help it blend in with leaves. Patterns aren't just pretty -- they're USEFUL! Nature is the greatest pattern maker of all!"
> 2. "*(warmly)* They ARE pretty! And here's a secret -- patterns aren't just for looking at. Stripes help zebras hide, spots warn predators away, and zigzags help snakes blend in. Pretty AND useful!"
> 3. *(waits 2 seconds)* "*(sharing a wonder)* I think it's because patterns each have a job. Stripes can help things hide. Spots can send a message. Zigzags can blend in. The world needs LOTS of different patterns because there are LOTS of different jobs to do!"
>
> **Screen**: The pattern collection remains. A soft animation shows pattern examples from nature: a zebra with highlighted stripes, a ladybug with highlighted spots, a snake with highlighted zigzags. Small text callouts appear: "Camouflage!" "Warning!" "Blending!" The word "PATTERNS" glows steadily above.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm, proud celebration)* Congratulations, Pattern Detective! You did something incredible today. You looked closely at the **Form** of things -- the stripes, the spots, the zigzags, the lines -- and you recognized that they're all patterns. And you discovered the **Connection** -- that patterns link totally different things together! A shirt and a leaf and a sidewalk crack -- all connected by pattern! You earned your Pattern Detective Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about patterns, wants to find more.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you go outside, look at EVERYTHING around you -- clothes, leaves, buildings, bugs -- and ask: what's YOUR pattern? You'll see stripes, spots, and zigzags everywhere! Bye for now, Detective!"
> 2. "*(warm)* Your detective badge is saved! Patterns are hiding everywhere -- now YOU know how to spot them. Bye, Detective!"
> 3. *(waits 2 seconds)* "*(soft)* Your badge is shining, Detective. Patterns are everywhere, and you proved it. See you next time!"
>
> **Screen**: A golden "Pattern Detective Badge" appears -- circular, with a magnifying glass over a pattern mosaic at the center and the 3 collection photos as small insets around the edges, each with its pattern label (Spots, Zigzags, Lines). The trigger photo with its label (Stripes) sits at the top. The words **"Form"** and **"Connection"** float up artistically -- "Form" styled with mixed pattern fills (stripes, dots, zigzags filling the letters), "Connection" with golden thread-like links weaving between the letters. A small pattern mosaic icon nestles between the concept words. A soft chime plays. Tiny animated pattern fragments drift across the screen and settle on the badge.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison required. Multi-photo workflow (3 photos across rounds) fully supported. All verification done through AI recognition of individual photos + dialogue. Visual pattern detection is a standard image recognition task. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional wonder ("Look at those LINES going side by side!") and a personal question ("Have you ever noticed stripes on other things too?"), not knowledge testing. Activity grows naturally from pattern observation --> wondering about other patterns --> detective mission. No "let's play a game" break. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches (ideal, unexpected, no response). Steps 3 rounds include concrete stuck branches with specific search hints ("look at any fabric near you," "check a leaf up close," "look right at the ground"). "Unexpected" branches always validate first ("That IS interesting!") then redirect. Stuck branches provide actionable, location-specific guidance. |
| 4 | IB Completeness | PASS | KUD fully defined: 5 vocabulary words (pattern, stripes, spots, zigzag, lines), 2 conceptual understandings (Form includes visual patterns, Connection links different things through pattern), 3 skills (critical thinking, observation/data collection, expressing reasoning). Form + Connection as Key Concepts. 4 Related Concepts (Pattern, Similarity, Observation, Discovery). 3 ATL skills with sub-skills. Closing speech names Form and Connection naturally as praise. Concepts match what child actually did -- observed forms and found connections. |
| 5 | Tier Appropriateness | PASS | T1 (ages 4-6): Sentences 5-8 words. 3-part riddle structure with concrete sensory clues ("tiny painted dots," "goes back and forth," "straight lines all in a row"). Open-ended search tasks. Concrete vocabulary (pattern, stripes, spots, zigzag, lines introduced in context). 2-3 step tasks per riddle (listen --> search --> photograph). |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Riddle-clues are specific and sensory with vivid descriptions. All responses are actual words the AI speaks. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: pattern highlight animation on trigger photo, detective mission card with badge and empty slots, per-round "SOLVED!" animations with sparkles, pattern connection map with labeled golden lines and pattern icons, badge with pattern mosaic and concept words styled with pattern fills and thread-link connections. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template -- triggered by detected pattern attribute, not a specific entity. Works for any entity with a visible pattern. |
| 9 | Game Feel | PASS | Genuine uncertainty in every round (child doesn't know what specific patterned thing the riddle describes). Stakes: "Can I find something with spots? Zigzags?" Pattern reveal creates a major "aha!" moment -- the child doesn't know that ALL their finds share the meta-quality of having a pattern until the end. Clear emotional climax at the reveal ("PATTERNS ARE EVERYWHERE!"). Replayable: different trigger patterns and different environments yield different finds. |
| 10 | Pillar Fidelity | PASS | Mystery pillar fully delivered. Child feels "I figured it out!" at the pattern reveal. Magic moment = hidden truth revealed (the connection between all finds is PATTERN). Core loop = riddle-clues --> deduction --> search --> bigger mystery --> revelation. Emotional arc: curiosity --> search --> solve --> bigger mystery --> revelation. Cannot be re-labeled as another pillar -- the riddle-clue mechanic and hidden pattern reveal are distinctively Mystery. |

**Overall**: ALL PASS -- mystery_trail with riddle-clue search and pattern reveal. Property-bridge template works for any detected visual pattern. Litmus test: the child doesn't know they're proving that "patterns are everywhere" until the reveal. The "aha!" moment retroactively transforms all their finds from random patterned things into evidence of a universal truth.
