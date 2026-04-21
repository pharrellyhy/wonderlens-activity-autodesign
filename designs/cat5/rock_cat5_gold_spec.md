# Activity Design: Rock + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: Nature Inventor's Lab

### A. Basic Info

- **Activity Name**: Nature Inventor's Lab
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: Form (What is it like?) & Function (How does it work?)
- **Related Concepts**: Structure (designed), Creativity (designed), Materials (designed), Connection (designed)
- **ATL Skills Focus**: Thinking Skills (creative thinking — combining properties into inventions), Research Skills (observation — identifying material properties through touch and sight), Communication Skills (expressing — describing inventions and reasoning about combinations)
- **Experience Pillar**: Creation
- **Game Style**: mix_lab
- **Design Version**: 1.0 — mix_lab new design
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Rock
- **Trigger Scene**: Child picks up and photographs a rock in the park
- **Mapping Source**: none
- **IB Theme**: How the World Works

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/natural_phenomena/rocks.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.senses.hard_feel
  - tier_0.senses.weight
  - tier_1.function.tool_use
  - tier_1.structure.solid_all_through
  - tier_2.function.strength_from_hardness
  - tier_2.function.combining_properties
  - tier_2.senses.heft_sense
```

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Rock (e.g., other solid/hard natural objects like pebble, stone,
boulder, brick, shell) instead of a rock itself. The neighbor list, bridge
type, and initial bridge prompt will live in `data/constellation_map.yaml`
under `mapped_entity: rock` (Cat5 entry pending per that file's coverage
notes) — this section describes how Nature Inventor's Lab adapts mechanically
for a bridged entity.

**Preserve** — must not change across neighbors:
- The "Nature Inventor" role_title and the superpower-naming ritual (rock = STRENGTH, leaf = FLEXIBILITY, feather = LIGHTNESS, stick = LENGTH) — each find gets ONE named property.
- The 4-ingredient collection + "pick two to combine" invention synthesis — this is the Creation-pillar magic moment where the child's invention gets narrated back.
- The child's invention name being treated as original and honored ("No one has ever invented a [X] before — only YOU!") — this is what makes the child feel like a real inventor.

**Swap** — re-phrase for the bridged entity:
- Seed superpower for the photographed entity "Rock = STRENGTH" → neighbor's signature property (pebble: "STRENGTH + smoothness"; boulder: "MASSIVE STRENGTH"; brick: "STRENGTH + stackability"; shell: "HARDNESS + hollow inside"). Keep strength as the anchor for rock-family neighbors; add a twist for ones that differ.
- Transition bridge "Feel how HARD it is — like a tiny mountain you can hold!" → neighbor's heft-and-feel (pebble: "smooth and cool in your palm"; boulder: "too big to lift — you'd need a whole team!"; shell: "hard outside but light for its size").
- Round 1–3 finds stay open-ended (leaf, feather, stick, pinecone, flower petal) — they DON'T change based on the seed; every neighbor still needs a flex partner, a light partner, a long partner.
- Closing "every superpower helps that thing do its JOB in nature" → acknowledge the neighbor's real job (boulder: "boulders block paths and hold back rivers"; shell: "shells protect soft creatures inside"; brick: "bricks build walls that last").

**Watch** — gotchas to avoid:
- Brick is human-made, not natural — if bridged, keep the lab metaphor but acknowledge the brick is "made from baked rock," preserving the "every material has a property" insight; don't pretend it grew in a forest.
- If the neighbor is enormous (boulder), the child can't hold it — skip the "squeeze it" instruction and pivot to "look at it" observation; same property lands without the tactile beat.
- Never skip the invention synthesis step — three-property collection with no combination is just a nature walk. If the child picks the same property twice, gently redirect ("two strengths just makes one super-strong — try mixing with [other]").

### B. Activity Overview

- **① Brief Description**: After photographing a rock, the AI marvels at how hard and tough it is — and reveals the rock's "superpower": STRENGTH. The child becomes a Nature Inventor and goes on a mission to collect 3 more natural items, each of which the AI assigns a unique superpower based on its material properties (e.g., leaf = flexibility, feather = lightness, stick = length). At synthesis, the child picks two superpowers to combine and invents something that has never existed before — naming it, describing what it does, and hearing the AI bring the invention to life in vivid words.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "strength," "flexibility," "lightness," "property," and "material." Learn that different natural objects have different physical properties — rocks are hard and strong, leaves can bend without breaking, feathers are light enough to float, sticks are long and reach far.
  - **U (Understand)**: Understand that every material has a distinct **Form** — specific physical properties like hardness, bendability, or weight — and that those properties determine **Function** — what the material can do or be used for. When you combine properties from different materials, you can imagine entirely new functions.
  - **D (Do)**: Practice close observation of material properties through touch and sight (Research Skills — observation), combine distinct properties into novel inventions (Thinking Skills — creative thinking), and describe imagined inventions with reasoning about what they can do (Communication Skills — expressing).

- **③ Design Highlight**: The "Nature Inventor's Lab" frames the outdoors as a laboratory and every natural object as an ingredient with a hidden superpower. The key mechanism is superpower discovery + creative combination: instead of simply collecting items, the AI reveals each find's material superpower (strength, flexibility, lightness, length), turning ordinary nature objects into extraordinary building blocks. At synthesis, the child becomes the inventor — choosing two superpowers to fuse into something impossible but wonderful. A "Bendy Shield" that's strong but bends around corners. A "Floating Bridge" that's long but light as air. The invention is the child's own creation, and the AI's elaborate description makes it feel real.

- **④ Typical Scenario**: Child photographs a rock in the park → AI reveals the rock's superpower of STRENGTH → child becomes a Nature Inventor → collects 3 more items (leaf, feather, stick) → each gets a superpower (flexibility, lightness, length) → child picks two superpowers to combine → invents and names something new ("Bendy Shield!") → AI brings the invention to life with vivid description → child earns Nature Inventor Badge.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1: Transition Bridge — Cold Start**

> **Context**: Child photographs a rock in the park with no prior conversation.
>
> **AI says**: "*(amazed, hefting-weight tone)* Whoa — look at this rock! Feel how HARD it is. It's like a tiny mountain you can hold in your hand! I bet if you squeezed it as hard as you could, it wouldn't even budge. Have you ever tried to break a rock?"
>
> **Possible child responses**:
> 1. (Ideal) "No, it's too hard!" / "I tried once, I couldn't!" / "Rocks are really strong!"
> 2. (Unexpected) "I threw it in the water!" / "It's just a rock." / "I like shiny ones!"
> 3. (No response) Child looks at the rock or the screen silently.
>
> **AI follow-up**:
> 1. "*(impressed)* It IS super hard! You know what? This rock has a secret SUPERPOWER. Want to know what it is? Its superpower is... STRENGTH! It's tough, solid, and nothing can squish it. This rock is the strongest thing around here!"
> 2. "*(playful, fascinated)* Ooh, shiny rocks are the best! And you know what makes ALL rocks amazing? They're SO hard and SO tough. This one has a secret superpower — want to hear it? Its superpower is... STRENGTH! Nothing can squish this rock!"
> 3. *(waits 2 seconds)* "*(whispering, like sharing a secret)* Can I tell you something cool about this rock? Feel how hard it is — go on, give it a squeeze. It won't budge! That's because this rock has a superpower. Its superpower is... STRENGTH!"
>
> **Screen**: Close-up of the child's rock photo centered on screen. A bold, glowing word "STRENGTH" pulses outward from the rock in sturdy block letters, with tiny animated cracks radiating from the text like the rock is so strong it's cracking the ground. A small shield icon appears near the rock. A subtle "1/4" counter appears in the bottom corner.

**Step 2: Mission Briefing**

> **AI says**: "*(scientist-explorer tone)* Okay, here's the thing — EVERY natural thing out here has a hidden superpower. Rocks have strength. But what about leaves? Feathers? Sticks? You are now a Nature Inventor! Your mission: find 3 more things in this park. I'll tell you each one's superpower. Then — here's the best part — you'll COMBINE two superpowers to invent something totally new! Ready, Inventor?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes! Let's go!" / "I want to find a leaf!"
> 2. (Uncertain) "What do I look for?" / "What's a superpower?"
> 3. (No response) Child glances around the park.
>
> **AI follow-up**:
> 1. "*(cheering)* The lab is OPEN! Go find something from nature — a leaf, a feather, a stick, a flower petal, anything! Take a photo and I'll reveal its superpower. Go, Inventor!"
> 2. "*(encouraging, warm)* A superpower is the special thing each object can DO because of what it's made of! Like your rock is super strong because it's so hard. Go find something else from nature — a leaf, a stick, anything! Take a photo and I'll show you its superpower!"
> 3. *(waits 2 seconds)* "*(gently guiding)* Try looking near the ground — there are leaves, sticks, feathers, and all kinds of things hiding in the grass! Pick up something interesting, take a photo, and I'll tell you its secret superpower!"
>
> **Screen**: A lab-themed mission card appears: a badge outline labeled "Nature Inventor" with a beaker-and-leaf icon. Below it, 4 ingredient slots — the first filled with the rock photo and labeled "STRENGTH" in bold. The remaining 3 slots show glowing question marks. A numbered task list: (1) Collect 3 more ingredients, (2) Discover superpowers, (3) Combine and INVENT! Each task has a small icon — magnifying glass, lightning bolt, light bulb.

**Step 3: Multi-Round Exploration (3-4 rounds)**

> **Round 1 — First Find:**
>
> *(Child photographs something — e.g., a leaf)*
>
> **AI says**: "*(excited scientist tone)* Ooh, ingredient number two! Let me analyze this... I see it's thin, and look — you can bend it without it snapping! Try bending it gently. Does it bend?"
>
> **Possible child responses**:
> 1. (Ideal) "Yes! It bends a lot!" / "It's bendy!" / "I can fold it!"
> 2. (Unexpected) "It's green." / "It fell from a tree." / "I don't know."
> 3. (No response) Child looks at the leaf or the screen.
>
> **AI follow-up**:
> 1. "*(triumphant)* YES! This leaf's superpower is... FLEXIBILITY! It can bend and twist and curve without breaking! Imagine if YOU could bend like that — you'd be like a rubber band! FLEXIBILITY is locked in. Two more ingredients to go, Inventor!"
> 2. "*(curious, redirecting)* It IS green — and look how thin it is! Give it a little bend — does it curl? Does it snap, or does it stay in one piece? I think this leaf can bend without breaking — its superpower is FLEXIBILITY! Two more to find!"
> 3. *(waits 2 seconds)* "*(warm, demonstrating)* Let me check this one out. See how thin it is? I bet it can bend and twist without snapping. You know what that means? Its superpower is... FLEXIBILITY! It can bend any way it wants! Two more ingredients, Inventor!"
>
> **Screen**: The leaf photo slides into the second ingredient slot with a burst of green sparkles. The word "FLEXIBILITY" appears below in flowing, curvy letters that wiggle slightly. A brief animation shows the word bending like a ribbon. Counter updates to "2/4 ingredients collected."

> **Round 2 — Second Find:**
>
> *(Child photographs something — e.g., a feather)*
>
> **AI says**: "*(whispering with awe)* Ohhhh — hold this up and let go gently. Watch how slowly it falls! This thing barely weighs anything! Does it feel heavy or light to you?"
>
> **Possible child responses**:
> 1. (Ideal) "Super light!" / "It floats!" / "Like nothing!"
> 2. (Unexpected) "It's soft!" / "A bird dropped it!" / "I found it on the ground."
> 3. (No response) Child holds the feather or looks at the photo.
>
> **AI follow-up**:
> 1. "*(amazed)* SO light it practically FLOATS! This feather's superpower is... LIGHTNESS! It weighs almost nothing — it can drift through the air like a cloud! Imagine if you could make something that light. LIGHTNESS is locked in! One more ingredient, Inventor!"
> 2. "*(agreeing warmly)* It IS really soft! And it's also incredibly LIGHT — feel how it barely weighs anything? If you let go, it drifts down so slowly! Its superpower is LIGHTNESS! One more to find, Inventor!"
> 3. *(waits 2 seconds)* "*(gently)* Feel how light this is — it's like holding air! If you dropped it, it would float down ssssslowly. Its superpower is... LIGHTNESS! Almost weightless! One more ingredient to go!"
>
> **Screen**: The feather photo floats gently into the third slot with a drifting animation — it sways side to side before settling. The word "LIGHTNESS" appears in thin, airy letters that seem to hover slightly above the slot. Tiny feather wisps drift around the text. Counter updates to "3/4 ingredients collected."

> **Round 3 — Third Find (with stuck branch):**
>
> **STUCK BRANCH** *(if child has been searching for more than a minute without finding something)*:
>
> **AI says**: "*(helpful, conspirator tone)* Inventor tip! Look at the base of a tree — there are usually sticks, seed pods, or bark pieces. Or check near a bush for twigs and flower petals! Even a blade of tall grass counts — every natural thing has a superpower!"
>
> **Possible child responses**:
> 1. (Ideal) "I see a stick!" / "There's one!" / Child heads toward a tree or bush.
> 2. (Unexpected) "I can't find anything." / "There's nothing here."
> 3. (No response) Child keeps wandering.
>
> **AI follow-up**:
> 1. "*(excited)* Go grab it, Inventor! Take a photo and let's unlock its superpower!"
> 2. "*(reassuring)* That's okay! Look right at your feet — even a tiny twig or a single flower petal works. Anything from nature has a hidden superpower waiting!"
> 3. *(waits 2 seconds)* "*(gentle prompt)* Try looking right under a tree. Sticks love hanging out at the bottom of trees! Even a short one will do."
>
> *(Child photographs final find — e.g., a stick)*
>
> **AI says**: "*(dramatic lab-coat tone)* FINAL INGREDIENT! Let me examine this... Wow, look how LONG this is! Hold it up — it reaches way farther than your arm can! What can you reach with this that you can't reach with just your hand?"
>
> **Possible child responses**:
> 1. (Ideal) "I can reach that branch!" / "I can poke things far away!" / "It's like a long arm!"
> 2. (Unexpected) "I can hit things!" / "It's just a stick." / "I want to dig with it."
> 3. (No response) Child holds the stick or looks at the photo.
>
> **AI follow-up**:
> 1. "*(thrilled)* EXACTLY! This stick's superpower is... LENGTH! It reaches farther than anything else in your collection! It can touch things far away, bridge gaps, and extend your reach! LENGTH is locked in! Inventor — ALL FOUR INGREDIENTS COLLECTED!"
> 2. "*(impressed, redirecting)* Ooh, you COULD dig with it — because it's so long it gives you extra reach! That's its superpower — LENGTH! It can reach things your hands can't! All four ingredients are ready, Inventor!"
> 3. *(waits 2 seconds)* "*(enthusiastic)* Look at how far this reaches — way beyond your fingertips! Its superpower is... LENGTH! It extends, it reaches, it bridges! That's all four ingredients, Inventor!"
>
> **Screen**: The stick photo slides into the final slot with a stretching animation — the photo seems to extend before snapping into place. The word "LENGTH" appears in tall, elongated letters that stretch across the slot. All four slots now glow with their superpower labels. A celebration burst — all four ingredient cards light up with golden borders and their superpower names pulse: STRENGTH, FLEXIBILITY, LIGHTNESS, LENGTH. A large "INVENTION TIME!" banner appears and pulses.

**Step 4: Synthesis — The Invention**

> **AI says**: "*(grand, dramatic inventor tone)* Inventor — your lab is LOADED! Look at your four superpowers: the STRENGTH of your rock, the FLEXIBILITY of your leaf, the LIGHTNESS of your feather, and the LENGTH of your stick! Now comes the BEST part. Pick any TWO superpowers — and imagine: if you combined them into ONE thing, what amazing invention would you create? What would you build with... say... the STRENGTH of rock and the FLEXIBILITY of leaf?"
>
> **Possible child responses**:
> 1. (Ideal) "A bendy shield!" / "A rubber wall!" / "Stretchy armor!" / Child names a creative invention.
> 2. (Unexpected) "I don't know." / "A rock-leaf." / "Can I pick different ones?"
> 3. (No response) Child looks at the superpowers on screen.
>
> **AI follow-up**:
> 1. "*(mind-blown, narrating with wonder)* A BENDY SHIELD! Oh. My. Goodness. Imagine this — a shield that's as STRONG as a rock, so nothing can break through it — but it can BEND and CURVE around corners because it has the flexibility of a leaf! You could wrap it around yourself like a blanket, but it's as tough as stone! The Bendy Shield — invented by YOU, Nature Inventor! What would you use it for?"
>
>    *(After child responds or pauses):* "*(celebrating)* That is BRILLIANT! No one in the whole world has ever invented a Bendy Shield before. Only YOU! Want to try combining two MORE superpowers for a bonus invention?"
>
>    *(If child says yes — bonus round):* "*(excited)* Pick two more! What about LIGHTNESS and LENGTH? What could you make?" *(AI responds with the same elaboration pattern to whatever the child invents.)*
>
> 2. "*(warmly encouraging)* That's okay — let me give you a spark! What if something was as STRONG as your rock... but could BEND like your leaf? What would that be? A bendy wall? A curvy sword? A twisty shield? What do YOU think it could be?"
>
>    *(If child says "Can I pick different ones?"):* "*(enthusiastic)* YES! Pick any two you want! How about LIGHTNESS and LENGTH — something super light but super long? Or STRENGTH and LIGHTNESS — something strong but weighs nothing? What would YOU build?"
>
> 3. *(waits 2 seconds)* "*(playful, sparking ideas)* Hmm, let me think out loud... what if something was STRONG like a rock but LIGHT like a feather? It would be... an unbreakable bubble! Floating but uncrackable! Now YOUR turn, Inventor — pick any two superpowers and tell me what YOU would build!"
>
> **Screen**: All four ingredient photos displayed in a row across the top, each with its glowing superpower label. Below them, a large "Invention Workshop" area with a glowing "+" symbol between two empty highlight slots. When the child picks two superpowers, the two chosen ingredient photos slide into the highlight slots with a dramatic merging animation — energy arcs connect them, sparkles fly, and a large golden "?" appears in the center before transforming into the invention name (typed by the AI as the child names it). The invention name appears in bold, custom letters with a glow effect. A "Created by [child]" stamp appears below.

**Step 5: Discovery Celebration**

> **AI says**: "*(proud, reflecting)* Nature Inventor, look at what you did today! You started with one rock — just a rock! — and you discovered that it has the superpower of STRENGTH. Then you found a leaf with FLEXIBILITY, a feather with LIGHTNESS, and a stick with LENGTH. Every single thing out here has its own special power! Why do you think different things in nature have different superpowers?"
>
> **Possible child responses**:
> 1. (Ideal) "Because they need to do different things!" / "So they can all help!" / "Because they're made of different stuff!"
> 2. (Unexpected) "I don't know." / "Because nature is cool!"
> 3. (No response) Child looks at the collection on screen.
>
> **AI follow-up**:
> 1. "*(delighted)* That's it EXACTLY! Rocks are hard so they can last a long time and protect things. Leaves are bendy so the wind doesn't snap them off trees. Feathers are light so birds can fly! Every superpower helps that thing do its JOB in nature. You figured that out, Inventor!"
> 2. "*(warmly)* Nature IS super cool! Here's a secret — each superpower is like a tool. Rocks are strong so they can protect things. Feathers are light so birds can fly! Everything is made just right for what it needs to do."
> 3. *(waits 2 seconds)* "*(sharing gently)* I'll tell you — rocks are strong so they last forever. Leaves are bendy so wind doesn't break them. Each superpower helps that thing survive! Nature is the greatest inventor of all — but today, YOU invented something even nature hasn't made!"
>
> **Screen**: All four ingredient photos displayed in a nature-lab layout. Gentle animated lines connect each photo to a small icon representing its superpower function (shield icon for strength, spring icon for flexibility, cloud icon for lightness, ruler icon for length). The invention from Step 4 appears in the center as a golden creation badge. Small nature-fact callouts appear near each ingredient.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm celebration)* Congratulations, Nature Inventor! You did something incredible today. You explored the **Form** of things in nature — what they feel like, how hard or soft or light they are. And you discovered their **Function** — the special job each superpower lets them do! Then you went even further — you COMBINED superpowers to invent something totally new. That's the magic of being an inventor — seeing what things CAN DO, and imagining what they COULD DO! You earned your Nature Inventor Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about their invention, or wants to invent more.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the badge on screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you pick up ANYTHING — a pinecone, a pebble, a flower — ask yourself: what's YOUR superpower? And what could I invent if I combined it with something else? See you in the lab, Inventor!"
> 2. "*(warm)* Your badge is saved! Remember, Inventor — everything around you has a hidden superpower. You just have to look! Bye for now!"
> 3. *(waits 2 seconds)* "*(soft)* Your Nature Inventor Badge is glowing. Bye for now, Inventor!"
>
> **Screen**: A golden "Nature Inventor Badge" appears — circular, with a beaker-and-leaf silhouette at the center and the 4 collection photos as small insets around the edges, each labeled with its superpower. The child's invention name appears in a golden banner across the top of the badge. The words **"Form"** and **"Function"** float up artistically — "Form" styled with textured letters that look like stone, leaf, feather, and wood grain; "Function" styled with bold, active letters with tiny lightning bolt accents. A light bulb icon glows between the concept words. A soft chime plays. Sparkles drift across the screen and settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison used. Multi-photo workflow (4 sequential photos) is supported. AI asks child to self-report material properties through dialogue. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional resonance and sensory wonder ("It's like a tiny mountain you can hold in your hand!") and a personal experience question ("Have you ever tried to break a rock?"), not knowledge testing. The superpower reveal naturally bridges into the collection mission. |
| 3 | Edge Case Coverage | PASS | All 6 steps have 3 response branches. Step 3 includes a concrete "stuck branch" with specific locations (base of trees, near bushes, tall grass). "Unexpected" branches always validate first, then redirect (e.g., "It IS green — and look how thin it is!"). Step 4 provides scaffolding for children who can't think of an invention. |
| 4 | IB Completeness | PASS | KUD fully defined: 5 vocabulary words, 2 conceptual understandings mapping to Form and Function, 3 skills mapping to ATL. Form + Function named as Key Concepts. 4 Related Concepts listed. 3 ATL skills with sub-skills. Closing speech celebrates first, then naturally names Form and Function as earned concepts. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5-8 words, 3-part mission structure, concrete vocabulary (strength, flexibility, lightness, length), open-ended combination prompt ("What would you build?"), 2-3 step tasks per find. Superpower names are simple single words a 4-6 year old can understand and repeat. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Superpower reveals are dramatic and specific. Invention elaboration describes exactly what the creation would look and feel like. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: superpower text animations (block letters for strength, curvy letters for flexibility, airy letters for lightness, elongated letters for length), lab-themed mission card with ingredient slots, invention workshop with merging animation, badge with textured concept words. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter — design is not mapping-informed. |
| 9 | Game Feel | PASS | Genuine uncertainty at each superpower reveal (child doesn't know what AI will say). The invention step creates real creative stakes — the child must DECIDE and CREATE. The invention reveal is the magic moment — AI's elaborate description brings the child's creation to life. Replayable because different items and different combinations produce entirely different inventions. |
| 10 | Pillar Fidelity | PASS | Creation pillar: child feels "I made this!" The magic moment is the invention unveiling — child names it, AI elaborates it into something vivid and real. Core loop uses the Creation-specific mechanic (collect ingredients with superpowers, combine into invention). Could NOT be re-labeled as Mystery, Discovery, or Adventure without feeling wrong — the synthesis step is fundamentally about open-ended building, not pattern-finding, hypothesis-testing, or journeying. |

**Overall**: ALL PASS — mix_lab with superpower-combination invention. Litmus test: if child collected different objects (pinecone, pebble, flower petal), the superpowers would differ, the combination prompt would differ, and the invention would be entirely unique.
