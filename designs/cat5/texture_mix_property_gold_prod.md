## The Texture Mix Lab

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Texture Mix Lab |
| Activity Category | 5 -- Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | **Form** (What is it like?) & **Function** (How does it work?) |
| Related Concepts (Discipline) | Structure, Creativity, Materials, Connection |
| ATL Skills Focus | Thinking Skills (creative thinking), Research Skills (observation), Communication Skills (expressing) |
| Experience Pillar | Creation |
| Game Style | mix_lab |
| Trigger Entity | Any entity with detected {texture} attribute |
| Trigger Scene | Child photographs any object where AI detects a visible texture (e.g., rough bark, smooth metal, fuzzy fabric, bumpy stone) |
| Mapping Source | property-bridge |
| IB Theme | How the World Works |
| Design Version | 1.0 |
| Last Updated | 2026-04-08 |
| Template Parameters | `{texture}` -- detected visible texture property (e.g., rough, smooth, fuzzy, bumpy, shiny, ridged, grainy). Example: **rough** |

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a visible texture -- for example, "rough" on tree bark. The AI marvels at how the bark LOOKS in the photo -- all those bumps, lines, and ridges -- and reveals the texture's "superpower": GRIP. The child becomes a Texture Inventor and collects 3 more items with different visible textures, each assigned a unique superpower based on visual assessment (smooth-looking = SPEED, fuzzy-looking = WARMTH, bumpy-looking = ARMOR). At synthesis, the child picks two superpowers to combine and invents something new. All texture assessment is VISUAL -- the AI analyzes what the texture looks like in the photograph. This template works for any detected visible texture.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "texture," "rough," "smooth," "fuzzy," "bumpy," and "superpower." Learn that different surfaces have different visible textures that give them different abilities.
  - **U (Understand)**: Understand that every surface has a distinct Form -- a visible texture -- and that those textures determine Function -- what the surface can do. When you combine functions from different textures, you can imagine entirely new inventions.
  - **D (Do)**: Practice close visual observation of texture properties in photographs, combine distinct texture superpowers into novel inventions, and describe imagined inventions with reasoning.

- **③ Design Highlight**: The "Texture Mix Lab" frames the world as a laboratory where every surface has a hidden superpower determined by its visible texture. The AI visually assesses each texture from the photograph: bark LOOKS rough (visible grain, uneven surface), glass LOOKS smooth (reflective, even surface), moss LOOKS fuzzy (visible fibers), gravel LOOKS bumpy (visible rounded shapes). At synthesis, the child chooses two superpowers to fuse into something impossible but wonderful.

- **④ Typical Scenario**: Child photographs a tree --> AI notices rough-looking bark --> "Your tree has such ROUGH-looking bark! Roughness is a superpower: GRIP!" --> child becomes a Texture Inventor --> collects 3 more items (smooth rock, fuzzy moss, bumpy wall) --> each gets a visually assessed superpower (SPEED, WARMTH, ARMOR) --> child picks two superpowers to combine --> invents and names something new --> AI brings it to life --> child earns Texture Inventor Badge.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**Context**: Child photographs any object where AI detects a visible texture. Example: a tree with rough bark.

**AI says:** *(amazed, fascinated)* "Whoa -- look at your tree! And look at that BARK! See all those bumps and lines and ridges? It looks SO rough -- like a tiny mountain range covering the whole trunk! That bark looks like it could hold on to ANYTHING! Have you ever noticed how rough tree bark looks?"

**Child responses:**

1. (Ideal) "Yeah, it's really bumpy!" / "It looks scratchy!" / "The bark has lines everywhere!"
2. (Unexpected) "It's a big tree!" / "I like climbing trees." / "There's a bug on it!"
3. (No response) Child looks at the tree or the screen silently.

**AI follow-up:**

1. (impressed) "It IS really bumpy! All those ridges and grooves -- that's called TEXTURE! And that rough-looking texture has a secret SUPERPOWER. Its superpower is... GRIP! Things that look rough can hold on tight -- rain, bugs, climbing plants all grab onto those bumps. Rough means GRIPPY!"
2. (playful) "It IS a big tree! And look at the surface of that bark -- see all those lines and bumps? That rough-looking surface has a secret superpower -- GRIP! Those bumps and ridges help things hold on tight!"
3. (wait 2s) "Can I tell you something cool about this bark? Look at how rough it looks -- all those bumps and grooves! That rough-looking texture has a superpower. Its superpower is... GRIP! Rough surfaces hold on tight -- nothing slides off!"

**Screen:** Trigger photo centered with bold "GRIP" pulsing in rough-textured block letters, animated grip marks radiating outward, and a small hand-grip icon. "1/4" counter in bottom corner.

#### Step 2: Rule Introduction + Demo

**AI says:** *(scientist-explorer)* "Okay, here's the thing -- EVERY surface out here has a hidden superpower based on what it LOOKS like! Rough-looking things have GRIP. But what about smooth things? Fuzzy things? Bumpy things? You are now a Texture Inventor! Your mission: find 3 more things with DIFFERENT textures. I'll look at each photo and tell you its superpower. Then -- here's the best part -- you'll COMBINE two superpowers to invent something totally new! Ready, Inventor?"

**Child responses:**

1. (Ideal) "Ready!" / "Yes! Let's go!" / "I want to find something smooth!"
2. (Uncertain) "What's a texture?" / "What do I look for?"
3. (No response) Child glances around.

**AI follow-up:**

1. (cheering) "The lab is OPEN! Go find something with a different texture -- something that looks smooth, or fuzzy, or bumpy, or shiny! Take a photo and I'll reveal its superpower. Go, Inventor!"
2. (encouraging) "Texture is how a surface LOOKS -- is it rough with bumps? Or smooth and flat? Or fuzzy with little fibers? Take a photo of something that looks DIFFERENT from your bark, and I'll tell you its superpower!"
3. (wait 2s) "Try looking around for surfaces that look different from bark. A smooth rock, a fuzzy sweater, a bumpy wall -- anything! Take a photo and I'll tell you its secret superpower!"

**Screen:** Lab-themed mission card with "Texture Inventor" badge, 4 ingredient slots (first filled with trigger photo labeled "GRIP"), 3 glowing question marks, and a 3-step task list: Collect, Discover, Invent.

#### Step 3: Multi-Round Interaction

**Round 1 -- Something Smooth-Looking (e.g., a smooth rock) (full detail):**

**AI says:** *(excited scientist)* "Ooh, ingredient number two! Let me analyze this photo... I can see the surface is flat and even -- no bumps, no ridges. It looks SO smooth -- like it's been polished by a river! Light is bouncing right off it evenly."

**Child responses:**

1. (Ideal) "It's super smooth!" / "It's like glass!" / "So shiny and flat!"
2. (Unexpected) "It's a rock." / "I found it by the path." / "It's gray."
3. (No response) Child looks at the object or the screen.

**AI follow-up:**

1. (triumphant) "YES! Look how even and flat that surface looks -- not a bump in sight! This texture's superpower is... SPEED! Things that look smooth let other things slide right off -- whoooosh! Smooth means FAST! SPEED is locked in. Two more textures to find, Inventor!"
2. (curious, redirecting) "It IS a rock -- and look how EVEN that surface is! No bumps, no ridges, just flat and smooth. Its superpower is SPEED! Smooth surfaces let things slide right off! Two more textures to find!"
3. (wait 2s) "See how the surface looks flat and even? No bumps anywhere! That smooth-looking texture has a superpower -- SPEED! Things slide right off smooth surfaces! Two more ingredients, Inventor!"

**Screen:** Photo slides into second slot with silvery sparkles. "SPEED" in sleek, streamlined, sliding letters. Counter updates to "2/4."

**Round 2 -- Something Fuzzy-Looking (e.g., moss):** AI examines the photo and notices "all those tiny little fibers and soft-looking strands." Reveals superpower: WARMTH -- "fuzzy things trap air between their fibers like tiny blankets, keeping warmth inside!" Counter updates to 3/4.

**Round 3 -- Something Bumpy-Looking (e.g., stone wall), with stuck branch:** AI provides stuck hint: "Look at walls, sidewalks, or rocks -- many have bumpy surfaces! Or check a pinecone, gravel, or even a shoe sole." When child photographs bumpy surface, AI notices "all those bumps and lumps -- like tiny hills packed together." Reveals superpower: ARMOR -- "bumpy surfaces spread out force like tiny shields working together!" All four slots fill and "INVENTION TIME!" banner appears.

#### Step 4: Celebration

**AI says:** *(grand, dramatic inventor)* "Inventor -- your lab is LOADED! Look at your four texture superpowers: the GRIP of your rough bark, the SPEED of your smooth rock, the WARMTH of your fuzzy moss, and the ARMOR of your bumpy wall! Now comes the BEST part. Pick any TWO superpowers -- and imagine: if you combined them into ONE thing, what amazing invention would you create? What would you build with... say... the GRIP of rough and the SPEED of smooth?"

**Child responses:**

1. (Ideal) "Grippy racing shoes!" / "Sticky roller skates!" / "A fast rope!"
2. (Unexpected) "I don't know." / "A rough-smooth thing." / "Can I pick different ones?"

**AI follow-up:**

1. (mind-blown) "GRIPPY RACING SHOES! Imagine -- shoes that are as FAST as a smooth surface, so you zoom across the ground like lightning -- but the bottoms have the GRIP of rough bark, so you NEVER slip! You could run at super speed around corners, up hills, even on ice! The Grippy Racing Shoes -- invented by YOU, Texture Inventor! What would you use them for?" Then: "That is BRILLIANT! No one in the whole world has ever invented Grippy Racing Shoes before. Only YOU!"
2. (encouraging) "That's okay -- let me give you a spark! What if something had the GRIP of rough bark... but the SPEED of smooth stone? Maybe grippy roller skates? A fast climbing wall? What do YOU think?" If child asks for different ones: "YES! Pick any two you want! How about WARMTH and ARMOR -- something warm but protected?"

**AI says:** *(proud, reflecting)* "Texture Inventor, look at what you did today! You started with one tree -- just bark! -- and you discovered that its rough-looking texture has the superpower of GRIP. Then you found smooth SPEED, fuzzy WARMTH, and bumpy ARMOR. Every surface you see has a texture with a superpower! Why do you think different things have different textures?"

**AI follow-up:**

1. (delighted) "That's it EXACTLY! Bark is rough so rain sticks and feeds the roots. Pebbles are smooth so water flows over them. Fuzzy caterpillars trap warmth. Bumpy shells protect the animal inside! Every texture has a JOB."
2. (warmly) "They DO look different! And each texture does something special. Rough bark grips water. Smooth pebbles let water flow. Fuzzy things stay warm. Bumpy things stay protected. Textures aren't just how things look -- they're what things CAN DO!"

**Screen:** Four ingredient photos in a row with glowing superpower labels. Invention Workshop area below with "+" symbol; chosen superpowers merge with energy arcs and sparkles, invention name appears in bold golden letters with "Created by [child]" stamp. Texture-fact callouts near each ingredient.

#### Step 5: Closing + IB Concepts

**AI says:** *(warm celebration)* "Congratulations, Texture Inventor! You did something incredible today. You explored the **Form** of surfaces -- what they look like, how rough or smooth or fuzzy or bumpy they are. And you discovered their **Function** -- the special superpower each texture gives them! Then you went even further -- you COMBINED superpowers to invent something totally new. That's the magic of being an inventor -- seeing what textures CAN DO, and imagining what they COULD DO! You earned your Texture Inventor Badge!"

**Child responses:**

1. (Engaged) Cheers, talks about their invention, or wants to invent more.
2. (Quiet) Smiles or says nothing.

**AI follow-up:**

1. (encouraging) "Next time you see ANYTHING -- a leaf, a stone, a sweater, a wall -- look at its texture and ask: what's YOUR superpower? And what could I invent if I combined it with something else? See you in the lab, Inventor!"
2. (warm) "Your badge is saved! Remember, Inventor -- every surface around you has a texture with a hidden superpower. You just have to look! Bye for now!"

**Screen:** Golden "Texture Inventor Badge" with beaker-and-texture-swatch silhouette, 4 collection photos with superpower labels, invention name in golden banner. "Form" in textured rough/smooth/fuzzy/bumpy letters, "Function" in bold letters with lightning accents, light bulb icon between them.
