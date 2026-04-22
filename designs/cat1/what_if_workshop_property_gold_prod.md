## What-If Workshop

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | What-If Workshop |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Function, Change |
| Related Concepts | Properties, Imagination, Creativity, Transformation |
| ATL Skills Focus | Thinking Skills (creative, divergent), Communication Skills (expressing, listening), Self-Management Skills (focus, engagement) |
| Game Style | inventor_workshop |
| Trigger Entity | Any entity with detected {property} attributes |
| Mapping Source | property-bridge |
| Design Version | 1.0 |
| Last Updated | 2026-04-21 |

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{property}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Any one of these supplies the property to invert in the what-if flip.
  - tier_0.appearance.shape         # invert shape ("round -> square")
  - tier_0.appearance.size          # invert size ("big -> tiny")
  - tier_0.senses.touch_feel        # invert texture ("shiny -> fuzzy")
  - tier_1.appearance.shine_level   # invert shininess
```

### B. Activity Overview

**① Brief Description**

After the child photographs an everyday object, the AI detects several physical properties — shiny, hard, small, smooth, etc. The child becomes a "What-If Inventor" in a magical flip-workshop. Each round, the AI names ONE detected property, celebrates it, then flips it to its OPPOSITE and asks the child to imagine the consequences. Each round flips a different property. In the grand finale, ALL flipped properties combine into a "Super [Entity]" — the child hears the full ridiculous creation described in one breathless, delightful reveal.

**② Educational Purpose (KUD)**

- **K (Know)**: Learn the names of physical properties — shiny, hard, small, smooth, fuzzy, squishy, enormous, bumpy. Learn that familiar objects have specific properties you can name and describe.
- **U (Understand)**: Understand that every object has properties that help it do its job — that is Function. Understand that when we change a property to its opposite, the whole object transforms — that is Change.
- **D (Do)**: Practice identifying and naming physical properties. Practice imagining consequences of changing properties (divergent thinking). Practice building on ideas across multiple rounds.

**③ Design Highlight**

The property-bridge mechanic turns AI detection into a game engine — each detected property becomes a round of play. The CONTRAST flip (shiny to fuzzy, hard to squishy) creates genuine comedy because the child must imagine a familiar object behaving in an absurd way. The escalation is built into the structure: each round stacks another flipped property, so by the finale the object is wildly, impossibly transformed. The "Super [Entity]" reveal with ALL opposite properties combined creates a "we made THIS?!" moment.

**④ Typical Scenario**

Child photographs a shiny metal spoon in the kitchen. AI detects shiny, hard, small, and smooth. Child becomes a What-If Inventor who flips each property one at a time — fuzzy spoon, squishy spoon, enormous spoon — imagining the hilarious consequences. Finale: SUPER SPOON — fuzzy, squishy, and enormous!

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (amazed, delighted gasp) "Whoa, look at this spoon! It is SO shiny — like a tiny mirror! I can practically see my face in it! Have you ever noticed how shiny your spoon is?"

**Child responses:**

1. (Ideal) "Yeah, it's really shiny!" / "I can see myself in it!" / "It's my favorite spoon!"
2. (Unexpected) "I eat cereal with it!" / "It's silver!" / "My mom has a bigger one!"
3. (No response) Child looks at the screen silently.

**AI follow-up:**

1. (impressed, conspiratorial) "You CAN see yourself — like a spoon-mirror! Your spoon has so many cool things about it. Want to play a game where we FLIP them all upside down?"
2. (warm, enthusiastic) "Cereal spoon — nice! You know what is cool about your spoon? It is shiny AND hard AND smooth. What if we changed ALL of that? Want to try something wild?"
3. (wait 2s) (soft, inviting) "Your spoon is really interesting! It is shiny, it is hard, it is smooth. I have a silly game — what if we made it the OPPOSITE of all those things? Want to play?"

**Screen:** Entity photo centered with gentle metallic shimmer animation and tiny sparkle particles radiating outward.

#### Step 2: Rule Introduction + Demo

**AI says:** (excited, playful) "Okay, here is how it works! You are a What-If Inventor! I tell you something about your spoon — a property, like shiny or hard. Then we FLIP it to the OPPOSITE! Watch — your spoon is smooth, right? What if it was... PRICKLY? A prickly spoon! Ouch! Would NOT want to eat soup with THAT! See how that works? Now YOUR turn — you imagine what happens when we flip! Ready, Inventor?"

**Child responses:**

1. (Ideal) "Ready!" / "Yeah!" / "That would be so funny!" / giggles
2. (Unexpected) "Prickly!" / "Ouch!" / "That's silly!"
3. (No response) Child is quiet, possibly processing.

**AI follow-up:**

1. (thrilled) "What-If Inventor is READY! Here comes the first flip!"
2. (delighted, laughing) "It IS silly — that is the whole point! Silly is how inventors start! Here comes your first REAL flip..."
3. (wait 2s) (encouraging, gentle) "It is easy — I tell you a thing about your spoon, then we flip it to the opposite! You just imagine! Here comes the first one..."

**Screen:** Entity photo on the left; "FLIP WORKSHOP" banner on the right with animated flip-arrows spinning playfully, a "What-If Inventor" badge at the top, and a demo animation showing "SMOOTH" flipping to "PRICKLY!" with a cartoon cactus-spoon.

#### Step 3: Multi-Round Interaction

**Round 1 — "Shiny → Fuzzy!":** (tactile flip — simple, high comedy)

**AI says:** (marveling) "First up! Your spoon is SO shiny — it gleams and sparkles like a little mirror! But WHAT IF... it was FUZZY instead? A fuzzy spoon! What would happen if you tried to eat soup with a fuzzy spoon?"

**Child responses:**

1. (Ideal) "The soup would get stuck in the fuzz!" / "It would tickle my mouth!" / "The fuzz would get all soupy!"
2. (Unexpected) "Eww!" / "Fuzzy like a teddy bear!" / says something unrelated
3. (No response) Child is quiet, thinking.

**AI follow-up:**

1. (cracking up) "YES! [Child's answer]! A fuzzy spoon — you dip it in the soup and SCHLOOP, all the soup gets stuck in the fuzz! You would have to squeeze your spoon like a sponge! One property flipped!"
2. (validating, giggling) "Fuzzy like a teddy bear — exactly! Imagine petting your spoon before dinner! And when you dip it in the soup — SCHLOOP! Fuzzy soup spoon! One property flipped!"
3. (wait 2s) (playful prompt) "Imagine — you dip your fuzzy spoon in the soup and... SCHLOOP! All the soup sticks to the fuzz! Would you eat with a fuzzy spoon?"

**Screen:** Entity photo with animated fuzz texture overlay. "SHINY" flips to "FUZZY!" in fluffy letters. Property tracker: [SHINY → FUZZY ✓].

**Round 2 — "Hard → Squishy!":** Structural flip — AI celebrates the spoon's hard metal, then flips to squishy. Child imagines a floppy jelly-spoon that bends and wobbles. AI stacks both modifications: fuzzy AND squishy. Property tracker updates with both flips checked.

**Round 3 — "Small → Enormous!":** Scale flip — AI celebrates the spoon's small size, then flips to enormous. Child imagines a spoon bigger than they are. AI stacks all three: fuzzy, squishy, AND enormous. All three flips now visible on screen, leading into the Super Entity reveal.

#### Step 4: Celebration

**AI says:** (breathless, building to maximum excitement) "Ready for the BIG reveal? Your spoon started as shiny, hard, and small. But YOU flipped EVERYTHING! It is now... FUZZY — covered in soft fluffy fuzz! SQUISHY — wobbling and flopping like jelly! And ENORMOUS — bigger than you, bigger than me, bigger than the whole kitchen! It is... SUPER SPOON! The FUZZIEST, SQUISHIEST, most GINORMOUS spoon in the ENTIRE WORLD! You invented it!"

**Child responses:**

1. (Ideal) "SUPER SPOON!" / "I made it!" / "That's so funny!" / giggles and cheers
2. (Unexpected) "Again!" / "More flips!" / "It's so silly!"
3. (No response) Child watches with wide eyes or smiles.

**AI follow-up:**

1. (pure celebration) "YOU invented Super Spoon! The wildest spoon ever created! Nobody else in the whole world has a fuzzy, squishy, enormous spoon — only YOU! Best What-If Inventor EVER!"
2. (joyful) "It IS the silliest thing ever! And YOU made it — flip by flip! The greatest invention of all time — SUPER SPOON!"
3. (wait 2s) (warm, proud) "Look at it! SUPER SPOON! Fuzzy, squishy, enormous! You flipped every single property. That is amazing!"

**Screen:** Grand reveal — entity with ALL flipped properties (fuzz texture, wobble animation, exaggerated scale) center-screen, "SUPER SPOON!" in bouncy rainbow letters, confetti burst and sparkle animations. Property cascade: "SHINY → FUZZY! HARD → SQUISHY! SMALL → ENORMOUS!"

#### Step 5: Closing + IB Concepts

**AI says:** (warm, proud) "You looked at your spoon and noticed its properties — shiny, hard, small. Properties are what make things work! A spoon is hard so it can scoop — that is Function. Then you CHANGED every property to its opposite — fuzzy, squishy, enormous. You transformed your spoon into something totally new! That is Change! You are a What-If Inventor — you understand how things work AND how to change them!"

**Child responses:**

1. (Ideal) "Function!" / "Change!" / "I'm a What-If Inventor!" / smiles
2. (Unexpected) "Can we do another one?" / "Bye Super Spoon!" / "I want to flip more things!"
3. (No response) Child is quiet or smiling.

**AI follow-up:**

1. (celebrating) "Function and Change — you GOT it! The best What-If Inventor! Your Super Spoon will live forever in the Flip Workshop!"
2. (warm, encouraging) "You want to flip MORE things? That is what real inventors do — they never stop asking 'what if!' See you next time, Inventor!"
3. (wait 2s) (gentle close) "What-If Inventor — great job today! You flipped, you imagined, you created! See you next time!"

**Screen:** "What-If Inventor" badge with flip-arrow-and-lightbulb icon; "Function" with gear icon and "Change" with transformation arrow in playful lettering; property flips listed beneath; Super Entity floating behind the badge with soft golden glow.
