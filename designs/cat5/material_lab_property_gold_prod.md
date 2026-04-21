## The Material Lab

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Material Lab |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | Structure, Discovery, Properties, Pattern |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing) |
| Game Style | field_experiment |
| Trigger Entity | Any entity with detected material attribute |
| Mapping Source | property-bridge |

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{material}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.senses.rubber_feel              # e.g., rubber_duck
  - tier_0.senses.fabric_feel              # e.g., raincoat, plush_toys
  - tier_0.senses.hard_feel                # e.g., toy_robot (plastic)
  - tier_1.structure.stuffing_material     # e.g., plush_toys
  - tier_2.structure.key_surface_material  # e.g., piano
```

### B. Activity Overview

**① Brief Description**

After the child photographs any object, the AI notices what material it is made of — metal, wood, plastic, fabric, stone, or another visually identifiable material. The AI announces the material and then poses a big question: "Are MOST things around here made of {material}, or something else?" The child becomes a "Material Scientist" who first PREDICTS whether the majority of nearby objects share the same material, then collects evidence by photographing 3 more objects. The AI assesses each photo's material visually and tallies results. At the end, the AI reveals whether the child's prediction was right or surprising.

**② Educational Purpose (KUD)**

- **K (Know):** Learn material vocabulary — "metal," "wood," "plastic," "fabric," "stone," "natural," "material." Learn that different objects are made of different materials for different reasons — metal is strong and shiny, wood is warm and rough, plastic is light and smooth, fabric is soft and flexible.
- **U (Understand):** Objects around us are made of specific materials for specific reasons (Causation) — the material's visible and tactile properties (Form) determine where and how it is used. A prediction can be tested by collecting and counting real evidence.
- **D (Do):** Make a prediction and commit to it before collecting data; photograph objects for AI to assess materials visually; react to AI's assessments and watch the tally build; compare results to a hypothesis.

**③ Design Highlight**

The "Material Lab" metaphor turns any room or environment into a science laboratory. The child commits to a hypothesis BEFORE exploring — "I think most things are metal!" — creating genuine stakes. Each photo adds a tally mark to either the "{material}" or "not {material}" column, building suspense. The magic moment is the final count: "Metal: 2, Not Metal: 3 — SURPRISE!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar. Because the template is parameterized by any detected material, it works in kitchens (metal), playrooms (plastic), gardens (natural), bedrooms (fabric), and everywhere else.

**④ Typical Scenario**

Child photographs a metal fork. AI notices the shiny metallic surface, announces "That's METAL!", and proposes a hypothesis: are most things in your kitchen metal, or something else? Child commits to a prediction, then photographs 3 more objects. AI examines each photo and assesses the material visually. After all 3, AI tallies the final score against the prediction and reveals the result.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted, curious) "Ooh, look at that fork! It's so shiny and smooth. That's METAL! Metal is hard and strong — that's why we eat with it. But wait... I'm looking around and I have a BIG question. Is EVERYTHING here made of metal? Or are some things made of something else? What do you think?"

**Child responses:**

1. (Ideal) "Some things are different!" / "The table is wood!" / "I think most are metal!"
2. (Unexpected) "I don't know what metal is." / "I like forks!"
3. (No response) Child looks around the room or at the screen.

**AI follow-up:**

1. (intrigued) "Interesting — you already have ideas! This fork is definitely metal — hard and shiny. But I wonder about the OTHER things around you. Are most of them metal too, or made of something different like wood or plastic? I think we should find out for REAL!"
2. (warm, explaining) "Metal is the hard, shiny stuff — like this fork! If you tap it, it goes CLINK. Some things around you are metal, and some are made of other stuff — like wood, which feels rough, or plastic, which is smooth and light. I have a fun idea to figure out what things around here are REALLY made of!"
3. (wait 2s) (inviting) "This fork is metal — hard, shiny, and cool to touch! But look around you. Are ALL the things here metal? Or are some made of something else? I bet we can find out together!"

**Screen:** Object photo centered with material-appropriate highlight effect (metallic sheen for metal, warm grain for wood, smooth sheen for plastic). A small material label with icon near the object surface.


#### Step 2: Rule Introduction + Demo

**AI says:** (excited scientist) "Okay — here is my big question. Out of ALL the things around you, do you think MOST of them are made of metal... or MOST of them are made of something else — like wood, plastic, or fabric? This is your PREDICTION. What do you think — mostly metal, or mostly NOT metal?"

**Child responses:**

1. (Ideal — picks the detected material) "Metal!" / "I think most are metal!" / "Everything is shiny!"
2. (Ideal — picks not-material) "Not metal!" / "I think wood!" / "Plastic!"
3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"

**AI follow-up:**

1. (locking it in) "You predict MOSTLY METAL — got it! I'm writing that down. Now here's the deal — you are a Material Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
2. (locking it in) "You predict MOSTLY NOT METAL — interesting! I'm writing that down. Now here's the deal — you are a Material Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
3. (encouraging) "A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST things around you are metal, or mostly something else like wood or plastic? Just pick one!"

**Screen:** Scientist mission card with "Material Scientist" badge. Tally board with two columns: "Metal" (shiny icon) and "Not Metal" (wood/plastic/fabric icons). Object photo under "Metal" with "1" tally. Prediction banner at top: "My prediction: Mostly [Metal / Not Metal]!" Three empty photo slots below.


#### Step 3: Multi-Round Interaction

**Round 1 — First Evidence:**

*(Child photographs something — e.g., a wooden cutting board)*

**AI says:** (eager scientist) "Evidence number two! Oh, let me look closely at this photo... (examining) I can see it's brown with little lines running through it — those are wood grain lines! I think that's WOOD! Wood is warm and natural — it comes from trees. That goes in the NOT METAL column!"

**Child responses:**

1. (Ideal) "Yeah, it IS wood!" / "I thought it was plastic!" / "The handle is metal though!"
2. (Unexpected) "I like cutting things!" / "It's brown!"
3. (No response) Looks at the tally.

**AI follow-up:**

1. (writing it down excitedly) "Great observation! The tally so far: Metal has 1, Not Metal has 1. It's a TIE right now! Your prediction says mostly [metal/not-metal]... let's see what happens next! Two more to find, Scientist!"
2. (validating) "Brown — yes! And that brown, grainy surface is wood. NOT metal! Tally update: Metal 1, Not Metal 1. It's TIED! Two more, Scientist!"
3. (wait 2s) (announcing) "So that's wood — NOT metal! The tally is tied: Metal 1, Not Metal 1! Two more to go. Find another thing and take a photo!"

**Screen:** New photo in slot 2. Tally board updates with animated tally mark. Running score: "Metal: 1 | Not Metal: 1." Prediction banner stays visible at top.

**Round 2 — Second Evidence:** Child photographs another object (container, cup, chair, etc.). AI examines the photo and announces the material: "Let me look... I can see [visual cues]. That's [MATERIAL]!" AI updates tally dramatically: "Not Metal is WINNING!" or "Metal is catching up!" One more piece of evidence to go.

**Round 3 — Third Evidence (Final Piece):** Child photographs final object (towel, toy, countertop, shoe). AI builds to climax: "The LAST piece! Let me look very carefully..." AI assesses material from photo and announces result. Adds final tally mark and announces the BIG RESULT is coming. Includes stuck branch: "Look for something you can hold, sit on, or put things in! Try what's on the table, under your feet, or what you're wearing!"


#### Step 4: Celebration

**AI says:** (drumroll voice) "Okay Material Scientist — time for the BIG REVEAL! You predicted that most things around you would be... MOSTLY [METAL / NOT METAL]! Let's count the evidence!"

*(AI tallies aloud)*

"The fork — METAL! That's one for metal. The [find 1] — [material]! The [find 2] — [material]! The [find 3] — [material]!"

**If prediction was RIGHT**: (triumphant fanfare) "The final count: Metal [N], Not Metal [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [mostly metal / mostly not-metal]! Material Scientist, your instincts are amazing!"

**If prediction was WRONG**: (gasping with delight) "The final count: Metal [N], Not Metal [M]! Your prediction was mostly [metal/not-metal], but SURPRISE — you got TRICKED! More things are actually [metal/not-metal] than you expected! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"

**If it's a TIE**: (amazed) "The final count: Metal 2, Not Metal 2! It's a PERFECT TIE! Nobody could have predicted that — this place uses BOTH equally! That's a surprise result, Scientist!"

**AI says:** (warm, wonder-filled) "You know what's really smart about the things around us? People use DIFFERENT materials on purpose! The fork is metal because metal is strong — it won't break when you poke food. Every material has a REASON! Which material surprised you the most today?"

**Child responses:**

1. (Ideal) "I was right!" / "Wood! I didn't know that was wood!" / "I want to test another room!"
2. (Unexpected) "I like metal best!" / "But I thought the cup was metal!"
3. (No response) Child looks at the tally screen.

**AI follow-up:**

1. (delighted) "That's what scientists DO — they guess, then check, and find out for real! Your experiment showed you something new about this place!"
2. (enthusiastic) "Great observation! Some things can LOOK like metal but actually be plastic. That's a scientist-level discovery!"
3. (wait 2s) (gentle) "Every material is here for a reason — strong for eating, soft for sleeping, smooth for cleaning. Your experiment helped you see that!"

**Screen:** Full tally board with all 4 photos in two columns (Metal vs. Not Metal). Prediction banner lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one. Large final score: "Metal: [N] | Not Metal: [M]." Reason arrows connect each photo to a purpose bubble.


#### Step 5: Closing + IB Concepts

**AI says:** (proud celebration) "Congratulations, Material Scientist! You did real science today! You looked closely at the Form of every object — what it's made of, how it looks, how it feels. And you discovered the Causation — WHY each material is used. Metal for strength. Wood for warmth. Plastic for lightness. Every material has a reason! You earned your Material Scientist Badge!"

**Child responses:**

1. (Engaged) Cheers, talks about wanting to test more rooms, or asks about the badge.
2. (Quiet) Smiles or says nothing.
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (encouraging) "Next time you go to a different room, try the experiment again! Predict first, then count. Every room might have a different answer. See you on the next experiment, Scientist!"
2. (warm) "Your badge is saved! You're a real Material Scientist now. Bye for now, Scientist!"
3. (wait 2s) (soft) "Your Scientist Badge is glowing. Great experiment today!"

**Screen:** Golden "Material Scientist Badge" shaped like a beaker with tally chart inside. Object photo at center with collection photos as insets. "Form" in crystalline letters with material texture swatches and "Causation" in arrow-shaped dynamic letters float artistically. Final tally result glows beneath.
