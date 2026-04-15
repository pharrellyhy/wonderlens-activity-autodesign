# Activity Design: What-If Workshop + Category 1 (Sustained Verbal Interaction)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: What-If Workshop

### A. Basic Info

- **Activity Name**: What-If Workshop
- **Activity Category**: Category 1 — Sustained Verbal Interaction (In-Device, Indoor)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Function, Change
- **Related Concepts**: Properties, Imagination, Creativity, Transformation
- **ATL Skills Focus**: Thinking Skills (creative thinking, divergent thinking), Communication Skills (expressing ideas, listening), Self-Management Skills (focus, engagement)
- **Experience Pillar**: Creation
- **Game Style**: inventor_workshop
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected {property} attributes (e.g., shiny metal spoon, soft stuffed bear, rough pinecone)
- **Trigger Scene**: Child photographs a familiar object with multiple detectable physical properties
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works (properties, change, function)

### B. Activity Overview

- **① Brief Description**: After the child photographs an everyday object, the AI detects several physical properties — shiny, hard, small, smooth, etc. The child becomes a "What-If Inventor" in a magical flip-workshop. Each round, the AI names ONE detected property, celebrates it, then flips it to its OPPOSITE and asks the child to imagine the consequences. "Your spoon is SO shiny! What if it was FUZZY instead?" The child imagines what would happen, describing the absurd result. Each round flips a different property. In the grand finale, ALL flipped properties combine into a "Super [Entity]" — the fuzziest, squishiest, most enormous version of the object — and the child hears the full ridiculous creation described in one breathless, delightful reveal.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the names of physical properties — shiny, hard, small, smooth, fuzzy, squishy, enormous, bumpy. Learn that familiar objects have specific properties you can name and describe.
  - **U (Understand)**: Understand that every object has properties that help it do its job — that is **Function** (what properties do). Understand that when we change a property to its opposite, the whole object transforms — that is **Change** (modifying properties transforms the entity).
  - **D (Do)**: Practice identifying and naming physical properties of objects. Practice imagining consequences of changing properties (divergent thinking). Practice building on ideas across multiple rounds (snowball creativity). Practice expressing creative ideas in sentences.

- **③ Design Highlight**: The property-bridge mechanic turns AI detection into a game engine — each detected property becomes a round of play. The CONTRAST flip (shiny → fuzzy, hard → squishy) creates genuine comedy because the child must imagine a familiar object behaving in an absurd way. The escalation is built into the structure: each round stacks another flipped property, so by the finale the object is wildly, impossibly transformed. The "Super [Entity]" reveal — with ALL opposite properties combined — creates a "we made THIS?!" moment that is impossible without the child's imagination at every step.

- **④ Typical Scenario**: Child photographs a shiny metal spoon in the kitchen. AI detects shiny, hard, small, and smooth. Child becomes a What-If Inventor who flips each property one at a time — fuzzy spoon, squishy spoon, enormous spoon — imagining the hilarious consequences. Finale: SUPER SPOON — fuzzy, squishy, and enormous!

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a familiar object (e.g., a shiny metal spoon) with no prior conversation. AI detects physical properties: shiny, hard, small, smooth.
>
> **AI says**: "*(amazed, delighted gasp)* Whoa, look at this spoon! It is SO shiny — like a tiny mirror! I can practically see my face in it! Have you ever noticed how shiny your spoon is?"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's really shiny!" / "I can see myself in it!" / "It's my favorite spoon!"
> 2. (Unexpected) "I eat cereal with it!" / "It's silver!" / "My mom has a bigger one!"
> 3. (No response) Child looks at the screen silently.
>
> **AI follow-up**:
> 1. "*(impressed, conspiratorial)* You CAN see yourself — like a spoon-mirror! Your spoon has so many cool things about it. Want to play a game where we FLIP them all upside down?"
> 2. "*(warm, enthusiastic)* Cereal spoon — nice! You know what is cool about your spoon? It is shiny AND hard AND smooth. What if we changed ALL of that? Want to try something wild?"
> 3. *(waits 2 seconds)* "*(soft, inviting)* Your spoon is really interesting! It is shiny, it is hard, it is smooth. I have a silly game — what if we made it the OPPOSITE of all those things? Want to play?"
>
> **Screen**: Entity photo (spoon) centered on screen with a gentle metallic shimmer animation. Tiny sparkle particles radiate outward from the object. Soft kitchen-scene background pattern with warm lighting.

**Step 2: Game Setup + Demo — "The Flip Workshop"**

> **AI says**: "*(excited, playful)* Okay, here is how it works! You are a What-If Inventor! I am going to tell you something about your spoon — a property, like shiny or hard. Then we FLIP it to the OPPOSITE! Watch — your spoon is smooth, right? What if it was... PRICKLY? A prickly spoon! Ouch! Would NOT want to eat soup with THAT! Ha! See how that works? Now YOUR turn — you imagine what happens when we flip! Ready, Inventor?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yeah!" / "That would be so funny!" / giggles
> 2. (Unexpected) "Prickly!" / "Ouch!" / "That's silly!" / repeats something
> 3. (No response) Child is quiet, possibly processing.
>
> **AI follow-up**:
> 1. "*(thrilled)* What-If Inventor is READY! Here comes the first flip! Listen carefully..."
> 2. "*(delighted, laughing)* It IS silly — that is the whole point! Silly is how inventors start! Here comes your first REAL flip..."
> 3. *(waits 2 seconds)* "*(encouraging, gentle)* It is easy — I tell you a thing about your spoon, then we flip it to the opposite! You just imagine! Here comes the first one..."
>
> **Screen**: Entity photo shifts to the left side. On the right, a colorful "FLIP WORKSHOP" banner appears with animated flip-arrows (↕) spinning playfully. A "What-If Inventor" badge glows at the top. A quick demo animation plays: the word "SMOOTH" appears, then flips over with a whoosh to reveal "PRICKLY!" with a cartoon cactus-spoon popping up and bouncing.

**Step 3: Core Loop (3 rounds)**

> **Round 1 — "Shiny → Fuzzy!" (tactile flip — simple, high comedy)**
>
> **AI says**: "*(marveling voice)* Okay, first up! Your spoon is SO shiny — it gleams and sparkles like a little mirror! But WHAT IF... it was FUZZY instead? A fuzzy spoon! What would happen if you tried to eat soup with a fuzzy spoon?"
>
> **Possible child responses**:
> 1. (Ideal) "The soup would get stuck in the fuzz!" / "It would be so fluffy!" / "It would tickle my mouth!" / "The fuzz would get all soupy!"
> 2. (Unexpected) "Eww!" / "That's gross!" / "Fuzzy like a teddy bear!" / says something unrelated
> 3. (No response) Child is quiet, thinking.
>
> **AI follow-up**:
> 1. "*(cracking up)* YES! [Child's answer]! A fuzzy spoon — you dip it in the soup and SCHLOOP, all the soup gets stuck in the fuzz! You would have to squeeze your spoon like a sponge! That is the most ridiculous spoon I have ever heard of! One property flipped!"
> 2. "*(validating, giggling)* Fuzzy like a teddy bear — exactly! Imagine petting your spoon before dinner! Stroking it like a little furry animal! And when you dip it in the soup — SCHLOOP! Fuzzy soup spoon! One property flipped!"
> 3. *(waits 2 seconds)* "*(playful prompt)* Imagine — you dip your fuzzy spoon in the soup and... SCHLOOP! All the soup sticks to the fuzz! You would have to SQUEEZE it out! Ha! What do you think — would you eat with a fuzzy spoon?"
>
> **Screen**: Entity photo with an animated fuzz texture overlay growing across the spoon surface. The word "SHINY" appears, flips with a whoosh animation, and becomes "FUZZY!" in fluffy letters. Tiny cartoon fuzz particles float off the spoon. A "FLIP 1 ✓" stamp appears in the corner. A property tracker bar shows: [SHINY → FUZZY] checked off.
>
> ---
>
> **Round 2 — "Hard → Squishy!" (structural flip — escalation, physical comedy)**
>
> **AI says**: "*(amazed, dramatic)* Flip number two! Your spoon is hard as METAL — solid, strong, firm! But WHAT IF... it was SQUISHY instead? Like a pillow! A squishy, bendy spoon! What would happen if you tried to scoop something with a squishy spoon?"
>
> **Possible child responses**:
> 1. (Ideal) "It would just flop over!" / "It would bend when you pick it up!" / "You couldn't scoop anything!" / "It would squish flat!"
> 2. (Unexpected) "Like jelly!" / "Boing boing!" / "Squishy!" / makes squishing sounds
> 3. (No response) Child is quiet.
>
> **AI follow-up**:
> 1. "*(howling with laughter)* [Child's answer]! A squishy spoon — you try to scoop your cereal and FLOP, the spoon just bends over like wet spaghetti! Cereal goes EVERYWHERE! You would need two hands just to hold it straight! And remember — it is ALREADY fuzzy from last round! A fuzzy, squishy spoon! Two properties flipped!"
> 2. "*(excited, bouncing)* Like jelly — YES! A jelly spoon! You pick it up and it goes wobble wobble wobble and FLOPS right back on the table! And it is already FUZZY! A fuzzy jelly spoon! Two properties flipped!"
> 3. *(waits 2 seconds)* "*(playful prompt)* Picture this — you grab your squishy spoon and... FLOP! It bends right over like a wet noodle! Squish squish! You cannot scoop ANYTHING! And it is already fuzzy! What do you think of your fuzzy, squishy spoon?"
>
> **Screen**: Entity photo now shows the spoon with fuzz texture (from Round 1) PLUS a new wobbly/jelly animation — the spoon gently wobbles and bends. "HARD" flips to "SQUISHY!" in bouncy, jiggly letters. Property tracker updates: [SHINY → FUZZY ✓] [HARD → SQUISHY ✓]. A "FLIP 2 ✓" stamp appears.
>
> ---
>
> **Round 3 — "Small → Enormous!" (scale flip — peak absurdity, visual comedy)**
>
> **AI says**: "*(building to peak excitement)* Last flip — this one is BIG! Literally! Your spoon is small — fits right in your hand, easy to hold. But WHAT IF... it was ENORMOUS? Bigger than YOU! The biggest spoon in the WORLD! What would you do with an enormous spoon?"
>
> **Possible child responses**:
> 1. (Ideal) "I would need a giant bowl!" / "I could eat a swimming pool of soup!" / "I couldn't even pick it up!" / "I would use it as a slide!"
> 2. (Unexpected) "Big spoon!" / "Like a shovel!" / "Whoa!" / giggles
> 3. (No response) Child is thinking or giggling.
>
> **AI follow-up**:
> 1. "*(absolutely losing it)* [Child's answer]! An ENORMOUS spoon — you could scoop up a BATHTUB of soup in one bite! You would need a crane to lift it! And remember — it is ALREADY fuzzy AND squishy! An enormous, fuzzy, squishy spoon! Imagine trying to eat dinner with THAT! Three properties flipped! ALL flipped! And now..."
> 2. "*(thrilled)* Like a SHOVEL — yes! A giant fuzzy squishy shovel-spoon! You would have to drag it behind you! And it would wobble and flop because it is squishy! Three properties flipped!"
> 3. *(waits 2 seconds)* "*(playful, wide-eyed)* Imagine — a spoon TALLER than you! And it is fuzzy, so it is covered in fuzz. And it is squishy, so it flops everywhere! ENORMOUS FUZZY SQUISHY SPOON! What would you even DO with that? Three properties flipped!"
>
> **Screen**: Entity photo dramatically scales up with a zoom animation — the spoon grows to fill the screen with exaggerated size lines and "WHOOOAA" text. Fuzz texture and wobble animation still visible from previous rounds. "SMALL" flips to "ENORMOUS!" in giant, bold letters that barely fit the screen. Property tracker: [SHINY → FUZZY ✓] [HARD → SQUISHY ✓] [SMALL → ENORMOUS ✓]. A "FLIP 3 ✓" stamp with extra sparkles.

**Step 4: Payoff — The Super Entity Reveal**

> **AI says**: "*(breathless, building to maximum excitement)* Ready for the BIG reveal? Your spoon started as shiny, hard, and small. But YOU flipped EVERYTHING! It is now... *(dramatic pause)* FUZZY — covered in soft fluffy fuzz! SQUISHY — wobbling and flopping like jelly! And ENORMOUS — bigger than you, bigger than me, bigger than the whole kitchen! It is... SUPER SPOON! *(explosion of joy)* The FUZZIEST, SQUISHIEST, most GINORMOUS spoon in the ENTIRE WORLD! You invented it! SUPER SPOON!"
>
> **Possible child responses**:
> 1. (Ideal) "SUPER SPOON!" / "I made it!" / "That's so funny!" / giggles and cheers
> 2. (Unexpected) "Again!" / "More flips!" / "It's so silly!"
> 3. (No response) Child watches with wide eyes or smiles.
>
> **AI follow-up**:
> 1. "*(pure celebration)* YOU invented Super Spoon! The wildest spoon ever created! Nobody else in the whole world has a fuzzy, squishy, enormous spoon — only YOU! Best What-If Inventor EVER!"
> 2. "*(joyful)* It IS the silliest thing ever! And YOU made it — flip by flip! The greatest invention of all time — SUPER SPOON!"
> 3. *(waits 2 seconds)* "*(warm, proud)* Look at it! SUPER SPOON! Fuzzy, squishy, enormous! You flipped every single property. That is amazing!"
>
> **Screen**: Grand reveal animation — entity photo transforms center-screen with ALL property modifications visible simultaneously: fuzz texture, wobble/jelly animation, exaggerated enormous scale. "SUPER SPOON!" text appears in bold, bouncy rainbow letters above, pulsing with each word. Confetti and sparkles burst from behind. The three property flips cascade down the side: "SHINY → FUZZY! HARD → SQUISHY! SMALL → ENORMOUS!" The entire screen pulses with warm golden light. Celebration sound effects (whoosh + sparkle chime + triumphant fanfare).

**Step 5: Celebration + IB Concepts**

> **AI says**: "*(warm, proud, reflective)* You know what you just did, Inventor? You looked at your spoon and noticed its properties — shiny, hard, small. Properties are what make things work! A spoon is hard so it can scoop — that is Function. Then you CHANGED every property to its opposite — fuzzy, squishy, enormous. You transformed your spoon into something totally new! That is Change — when you modify something, it becomes different! You are a What-If Inventor — you understand how things work AND how to change them!"
>
> **Possible child responses**:
> 1. (Ideal) "Function!" / "Change!" / "I'm a What-If Inventor!" / "I flipped everything!" / smiles
> 2. (Unexpected) "Can we do another one?" / "Bye Super Spoon!" / "I want to flip more things!"
> 3. (No response) Child is quiet or smiling.
>
> **AI follow-up**:
> 1. "*(celebrating)* Function and Change — you GOT it! The best What-If Inventor! Your Super Spoon will live forever in the Flip Workshop!"
> 2. "*(warm, encouraging)* You want to flip MORE things? That is what real inventors do — they never stop asking 'what if!' See you next time, Inventor!"
> 3. *(waits 2 seconds)* "*(gentle close)* What-If Inventor — great job today! You flipped, you imagined, you created! See you next time!"
>
> **Screen**: "What-If Inventor" badge centered with a flip-arrow-and-lightbulb icon. Below, "Function" appears with a small gear icon and "Change" appears with a transformation arrow icon — both styled in playful, colorful lettering. The three property flips are listed beneath: SHINY → FUZZY, HARD → SQUISHY, SMALL → ENORMOUS. The Super Entity (with all modifications) floats behind the badge. Soft golden glow and a final burst of tiny sparkles.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state-change detection, or non-speech audio required. All interaction is verbal. Property detection uses standard image classification. Single photo used throughout. |
| 2 | Hook & Transition | PASS | Step 1b opens with emotional delight about a detected property ("SO shiny — like a tiny mirror!"), not knowledge testing. Activity grows naturally from "want to play a game where we FLIP them?" — feels like play, not task assignment. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, silence). Unexpected responses always validated before redirecting. Silence branches include 2-second wait + gentle, specific prompt with concrete imagery. |
| 4 | IB Completeness | PASS | Key Concepts: Function + Change — both explicitly named in closing with concrete connection to what the child did. KUD fully defined with specific vocabulary. ATL skills: Thinking (creative, divergent), Communication (expressing, listening), Self-Management (focus). 4 Related Concepts listed. Closing celebrates first, then names concepts naturally. |
| 5 | Tier Appropriateness | PASS | T1: Sentences predominantly 5–10 words. Open-ended imagination questions ("What would happen if...?"). Vocabulary is concrete and age-appropriate (fuzzy, squishy, enormous, shiny, hard, smooth). Multi-step reasoning (hear property, imagine opposite, predict consequence). Achievable for ages 4–6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers in parentheses and italics. Zero abstract instructions. All responses are warm, playful, comedic, and sensory. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations (fuzz overlays, wobble/jelly, scale zoom, flip-arrow animations, property tracker bar), and visual elements (Flip Workshop banner, Inventor badge, property cascade, concept icons). Screens accumulate modifications across rounds. |
| 8 | Entity Mapping Alignment | PASS | Property-bridge: AI detects physical properties (shiny, hard, small, smooth) and uses them as the game engine — each detected property becomes a round. The contrast-flip mechanic is entirely driven by what the AI detects. Different entities with different properties yield completely different games. |
| 9 | Game Feel | PASS | Genuine uncertainty: child must imagine consequences of each flip — outcome unknown until child decides. Comedy escalation: each round stacks absurdity (fuzzy THEN squishy THEN enormous). Magic moment: Super Entity reveal with ALL opposite properties combined — dramatic, surprising, hilarious. Replayable: different objects have different properties = completely different game every time. |
| 10 | Pillar Fidelity | PASS | Creation pillar: "I invented this!" feeling clearly delivered. Magic moment is the "ta-da!" invention reveal (Super Entity with all flipped properties). Core loop is snowballing property-flips (not generic Q&A). Child's emotional arc: one flip → wilder flip → wildest flip → combined absurd creation unveiled. Could NOT be relabeled as another pillar — the snowballing invention mechanic is uniquely Creation. |

**Overall**: ALL PASS — Ready for 教研 review
