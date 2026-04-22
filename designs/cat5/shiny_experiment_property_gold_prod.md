## The Shiny Experiment

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Shiny Experiment |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | Structure, Discovery, Properties, Pattern |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing) |
| Game Style | field_experiment |
| Trigger Entity | Any entity where AI detects shiny/reflective or matte/dull surface |
| Mapping Source | property-bridge |
| Design Version | 1.0 |
| Last Updated | 2026-04-21 |

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{shininess}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_1.appearance.shine_level                 # e.g., crayons
  - tier_1.appearance.reflective_strips           # e.g., raincoat
  - tier_2.appearance.surface_finish_glossiness   # e.g., raincoat
  - tier_1.appearance.scale_shimmer_pattern       # e.g., goldfish
```

### B. Activity Overview

**① Brief Description**

After the child photographs any object, the AI assesses its shininess from the photo — is the surface reflective, glossy, metallic (SHINY) or matte, rough, textured (DULL)? The AI announces the assessment with excitement and then poses a big question: "Are MOST things around here SHINY or DULL?" The child becomes a "Shine Scientist" who first PREDICTS whether the majority is shiny or dull, then collects evidence by photographing 3 more objects. The AI is the property assessor — it examines each photo and announces "SHINY!" or "DULL!" based on visual evidence. The child does NOT self-report. At the end, the AI tallies results and reveals whether the child's prediction was right or surprising.

**② Educational Purpose (KUD)**

- **K (Know):** Learn surface vocabulary — "shiny," "dull," "reflective," "matte," "glossy," "rough," "smooth," "surface." Shiny things reflect light (metal, glass, polished surfaces); dull things absorb or scatter light (fabric, wood, paper, matte surfaces). Material and surface determine how much something shines.
- **U (Understand):** Objects have surface properties (Form) that determine whether they appear shiny or dull — smooth polished surfaces reflect light while rough textured surfaces scatter it. WHY some things shine and others don't comes down to material and surface construction (Causation). A prediction can be tested by collecting and counting real evidence.
- **D (Do):** Make a prediction and commit to it before collecting data; photograph objects for AI to assess shininess visually; react to AI's assessments and watch the tally build; compare results to a hypothesis; reflect on why some things are shiny and some are dull.

**③ Design Highlight**

The "Shine Scientist" metaphor turns any environment into a surface laboratory. The child commits to a hypothesis BEFORE exploring — "I think most things are SHINY!" — creating genuine stakes. The AI is the property assessor: it examines each photo and announces "SHINY!" or "DULL!" with visual evidence. Shininess is highly visually verifiable from photos — reflective gleam, metallic sheen, and glossy coatings vs. matte textures, rough grains, and fabric weaves. The magic moment is the final count and the discovery of WHY surfaces behave differently.

**④ Typical Scenario**

Child photographs a shiny doorknob. AI notices the reflection, announces "SO shiny — I can almost see my reflection!" and proposes a hypothesis: are most things in this room shiny or dull? Child commits to a prediction, photographs 3 more objects. AI examines each photo and assesses shininess visually. After all 3, AI tallies the final score against the prediction and reveals the result.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted, curious) "Whoa — look at that doorknob! It's SO shiny — I can almost see a reflection in it! That's because the surface is smooth and polished. Shiny things bounce light back like a tiny mirror! But wait... is EVERYTHING here SHINY like this doorknob? Or are some things more DULL? What do you think?"

**Child responses:**

1. (Ideal) "Some things are dull!" / "The carpet is not shiny!" / "I think most things are shiny!"
2. (Unexpected) "I don't know what shiny means." / "I like doorknobs!"
3. (No response) Child looks around the room or at the screen.

**AI follow-up:**

1. (intrigued) "Interesting — you already noticed! This doorknob is definitely SHINY — smooth and reflective. But I wonder about the OTHER things around you. Are most of them shiny too, or more dull and rough? I think we should find out for REAL!"
2. (warm, explaining) "Shiny means it SPARKLES — it bounces light back at you! Like this doorknob. Some things are shiny, and some are DULL — they don't sparkle at all, like a towel or a book. I have a fun idea to figure out which ones are around here!"
3. (wait 2s) (inviting) "This doorknob is super shiny — smooth and glowing! But look around you. Are ALL things here shiny? Or are some dull and rough? I bet we can find out together!"

**Screen:** Object photo centered with sparkle highlight on reflective surface. Small "SHINY!" label with star icon near the object.


#### Step 2: Rule Introduction + Demo

**AI says:** (excited scientist) "Okay — here is my big question. Out of ALL the things around you, do you think MOST of them are SHINY... or MOST of them are DULL? Shiny things sparkle and reflect — like mirrors and metal. Dull things don't sparkle — like fabric and wood. This is your PREDICTION. What do you think — mostly SHINY, or mostly DULL?"

**Child responses:**

1. (Ideal — picks shiny) "Shiny!" / "I think most things are shiny!" / "Everything sparkles!"
2. (Ideal — picks dull) "Dull!" / "I think most things are not shiny!" / "More rough things!"
3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"

**AI follow-up:**

1. (locking it in) "You predict MOSTLY SHINY — got it! I'm writing that down. Now here's the deal — you are a Shine Scientist! Your job: find 3 more things, take a photo of each one, and I'll look really closely to see if it's SHINY or DULL. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
2. (locking it in) "You predict MOSTLY DULL — interesting! I'm writing that down. Now here's the deal — you are a Shine Scientist! Your job: find 3 more things, take a photo, and I'll check if they're SHINY or DULL. I'll keep count. Ready, Scientist?"
3. (encouraging) "A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — do you think MOST things around you are SHINY and sparkly, or DULL and rough? Just pick one!"

**Screen:** Scientist mission card with "Shine Scientist" badge (magnifying glass with sparkle). Tally board with two columns: "Shiny" (sparkle icon) and "Dull" (matte circle icon). Object photo under "Shiny" with "1" tally. Prediction banner: "My prediction: Mostly [Shiny / Dull]!" Three empty photo slots below.


#### Step 3: Multi-Round Interaction

**Round 1 — First Evidence:**

*(Child photographs something — e.g., a fabric cushion)*

**AI says:** (eager scientist) "Evidence number two! Let me look closely at this photo... (examining) Hmm, I can see it's soft and textured — no sparkle, no reflection at all. The surface is rough and absorbs all the light. I'm calling it — this is DULL! Fabric is almost always dull because tiny threads scatter the light. That goes in the DULL column!"

**Child responses:**

1. (Ideal) "Yeah, it's not shiny at all!" / "It's soft!" / "I thought it might be shiny because of the color!"
2. (Unexpected) "I like that pillow!" / "It's blue!"
3. (No response) Looks at the tally.

**AI follow-up:**

1. (writing it down) "Great observation! Soft and not shiny — DULL! The tally so far: Shiny 1, Dull 1. It's a TIE! Your prediction says mostly [shiny/dull]... two more to find, Scientist!"
2. (validating) "Blue — yes! But even bright blue can be DULL — no sparkle, no reflection. Color doesn't mean shiny! Tally: Shiny 1, Dull 1. TIED! Two more!"
3. (wait 2s) (announcing) "That's DULL — no shine! Tally tied: Shiny 1, Dull 1! Two more to go!"

**Screen:** New photo in slot 2. Tally board updates with animated tally mark. Running score: "Shiny: 1 | Dull: 1." Prediction banner stays visible.

**Round 2 — Second Evidence:** Child photographs another object (window, spoon, toy, table). AI examines photo closely and announces assessment: "I can see light bouncing off — SHINY!" or "No reflection, rough surface — DULL!" Updates tally dramatically: "Shiny is WINNING!" or "Dull is pulling ahead!" One more piece of evidence.

**Round 3 — Third Evidence (Final Piece):** Child photographs final object (book, towel, metal fixture, plastic bottle). AI builds to climax: "The LAST piece! Let me look very carefully..." AI assesses shininess from photo, adds final tally mark, announces the BIG RESULT is coming. Includes stuck branch: "Look at what's on the table, what's under your feet, or what you're wearing — everything has a surface!"


#### Step 4: Celebration

**AI says:** (drumroll voice) "Okay Shine Scientist — time for the BIG REVEAL! You predicted that most things around you would be... MOSTLY [SHINY / DULL]! Let's count the evidence!"

*(AI tallies aloud)*

"The doorknob — SHINY! That's one for shiny. The [find 1] — [SHINY/DULL]! The [find 2] — [SHINY/DULL]! The [find 3] — [SHINY/DULL]!"

**If prediction was RIGHT**: (triumphant fanfare) "The final count: Shiny [N], Dull [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [mostly shiny / mostly dull]! Shine Scientist, your eyes are AMAZING!"

**If prediction was WRONG**: (gasping with delight) "The final count: Shiny [N], Dull [M]! Your prediction was mostly [shiny/dull], but SURPRISE — you got TRICKED! More things are actually [shiny/dull] than you expected! That's what makes science so cool — sometimes you discover the unexpected!"

**If it's a TIE**: (amazed) "The final count: Shiny 2, Dull 2! It's a PERFECT TIE! This place has BOTH equally! That's a surprise result, Scientist!"

**AI says:** (warm, wonder-filled) "You know what's really interesting? Things are shiny or dull because of what they're MADE of! Metal and glass are SMOOTH — light bounces right off. But fabric and wood are ROUGH — light hits tiny bumps and scatters everywhere. The smoother the surface, the shinier! Which one surprised you the most?"

**Child responses:**

1. (Ideal) "I was right!" / "The cushion! I thought color made things shiny!" / "I want to test the bathroom!"
2. (Unexpected) "I like shiny things best!" / "But I thought that one was shiny!"
3. (No response) Child looks at the tally screen.

**AI follow-up:**

1. (delighted) "That's what scientists DO — guess, check, and discover for real! Color doesn't make things shiny — the SURFACE does. Your experiment showed you something new!"
2. (enthusiastic) "Great observation! Some things can LOOK like they might be shiny but actually be dull. That's a scientist-level discovery!"
3. (wait 2s) (gentle) "Smooth surfaces bounce light — shiny. Rough surfaces scatter light — dull. Your experiment helped you see the difference!"

**Screen:** Full tally board with all 4 photos in two columns (Shiny vs. Dull). Prediction banner lights up green (RIGHT!) or flashes orange ("SURPRISE!"). Animated tally marks count up with sparkle effects. Large final score: "Shiny: [N] | Dull: [M]." Reason arrows connect each photo to a "why" bubble.


#### Step 5: Closing + IB Concepts

**AI says:** (proud celebration) "Congratulations, Shine Scientist! You did real science today! You looked closely at the Form of every object — how its surface looks, whether it sparkles or stays quiet. And you discovered the Causation — WHY some things are shiny and some are dull. Smooth surfaces reflect light. Rough surfaces scatter it. The material and the surface tell the whole story! You earned your Shine Scientist Badge!"

**Child responses:**

1. (Engaged) Cheers, talks about wanting to test more rooms, or asks about the badge.
2. (Quiet) Smiles or says nothing.
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (encouraging) "Next time you're in a different room, try the experiment again! Bathrooms, kitchens, classrooms — every place has a different shiny-to-dull mix. Predict first, then count. See you on the next experiment, Scientist!"
2. (warm) "Your badge is saved! You're a real Shine Scientist now. Bye for now, Scientist!"
3. (wait 2s) (soft) "Your Scientist Badge is glowing — how shiny! Great experiment today!"

**Screen:** Golden "Shine Scientist Badge" shaped like a magnifying glass with a sparkle inside and tally chart reflected in its lens. Object photo at center with collection photos as insets. "Form" in crystalline letters with surface texture swatches (smooth mirror vs. rough fabric) and "Causation" in arrow-shaped dynamic letters float artistically. Final tally result glows beneath.
