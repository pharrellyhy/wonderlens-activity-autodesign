## The Playground Material Detective

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Playground Material Detective |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | Structure, Discovery, Safety, Pattern |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing) |
| Game Style | field_experiment |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/buildings_places/play_areas.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.senses.ground_feel
  - tier_1.appearance.slide_surface_shine
  - tier_1.senses.sun_warmed_parts
  - tier_1.structure.bolts_and_joints
  - tier_1.structure.swing_chain_links
  - tier_2.appearance.texture_mix_on_surfaces
```

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Playground (e.g., swing, slide, seesaw, sandbox, climbing frame) —
these are PARTS of a playground photographed in isolation. The neighbor list,
bridge type, and initial bridge prompt live in `data/constellation_map.yaml`
under `mapped_entity: playground` — this section describes how The Playground
Material Detective adapts mechanically for a bridged entity.

**Preserve** — must not change across neighbors:
- The "Playground Scientist" role_title and the PREDICT → COLLECT 3 → TALLY REVEAL arc — hypothesis-before-evidence is the Discovery pillar's engine.
- The metal-vs-not-metal classification frame with running tally — the binary choice is what makes the prediction testable at T1.
- The Causation closing ("metal for strength, rubber for safety, wood for grip") — every material has a reason, and the child must walk away with that insight.

**Swap** — re-phrase for the bridged entity:
- Transition Bridge "Feel that slide! It's METAL!" → anchor the bridge prompt on the specific part the child photographed (swing: "Those chains are METAL — feel them!"; sandbox: "Those wooden borders — feel how WOOD holds up outdoors!"; climbing frame: "That bar is METAL and SO strong!"). Seed the first tally mark with whatever material the photographed part shows.
- Step 2 Prediction framing "are MOST playground things metal or not-metal?" stays verbatim — the swing, slide, etc. all live inside a playground, so the question's scope is identical.
- Round 1–3 evidence gathering still expects the child to walk around the playground — the seed part changes which column gets the starting tally (slide → metal; sandbox → not-metal; rubber mat under swing → not-metal).
- Closing line "the slide is metal because metal is smooth" → the child's actual seed part (seesaw: "because metal is strong and holds two riders"; sandbox: "because wood stands up to weather").

**Watch** — gotchas to avoid:
- For neighbors that are ambiguous-material (a climbing frame can be metal OR molded plastic), let the child's photo assessment seed the tally — don't hardcode "metal" as the starter.
- If the child photographs the sandbox specifically, the seed tally may land in Not-Metal, which inverts which prediction feels "surprising" — the game still works but the AI's lines about "shiny zoom" need to swap to material properties that actually apply.
- Never drop the prediction lock-in — a playground survey without a committed guess is just a scavenger hunt, not science. If the child refuses to predict, the AI must propose a default ("Let's predict mostly metal — lock it in?").

### B. Activity Overview

**① Brief Description**

After photographing the slide, the AI marvels at how shiny and hard the metal surface is and wonders — is MOST of the playground made of metal, or something else? The child becomes a "Playground Scientist" who first PREDICTS whether most playground equipment is made of metal or not-metal (plastic, wood, rubber), then collects evidence by photographing 3 more pieces of equipment and reporting what each one is made of. At the end, the AI tallies the real data and reveals whether the child's prediction was right or surprising.

**② Educational Purpose (KUD)**

- **K (Know):** Learn the vocabulary "metal," "plastic," "wood," "rubber," "material." Learn that playgrounds use different materials for different reasons — metal is strong, plastic is smooth, rubber is soft for safety, wood holds up outdoors.
- **U (Understand):** Different parts of a playground are made of different materials for specific reasons (Causation) — the material's properties (Form) determine where it is used. A prediction can be tested by collecting and counting real evidence.
- **D (Do):** Make a prediction and commit to it before collecting data; photograph playground equipment for AI to assess materials; react to AI's assessments and watch the tally build; compare results to a hypothesis.

**③ Design Highlight**

The "Material Detective" metaphor turns the playground into a science lab. The child commits to a hypothesis BEFORE exploring — "I think most things are metal!" — creating genuine stakes. Each find adds a tally mark to either the "metal" or "not-metal" column, building suspense. The magic moment is the final count: "Metal: 2, Not-metal: 3 — SURPRISE! More things are NOT metal! Your prediction was close but the playground tricked you!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar.

**④ Typical Scenario**

Child photographs a metal slide, AI notices the shiny metal surface, proposes a hypothesis about whether most playground things are metal or not-metal, child commits to a prediction, then finds 3 more pieces of equipment, reports the material of each, and the AI tallies the final score against the prediction.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted, curious) "Whoa — feel that slide! It's so shiny and hard. That's METAL! Metal is strong and smooth — that's why you zoom down so fast. But wait... I'm looking around this playground and I have a BIG question. Is EVERYTHING here made of metal? Or are some things made of something else? What do you think?"

**Child responses:**

1. (Ideal) "Some things are different!" / "The swings are metal too!" / "I think it's all metal!"
2. (Unexpected) "I don't know what metal is." / "I like the slide!"
3. (No response) Child looks at the playground or the screen.

**AI follow-up:**

1. (intrigued) "Interesting — you already have ideas! This slide is definitely metal — hard and shiny. But I wonder about the OTHER things. Are most of them metal too, or made of something different like plastic or wood? I think we should find out for REAL!"
2. (warm, explaining) "Metal is the hard, shiny stuff — like this slide! If you knock on it, it goes CLANG. Some things at playgrounds are metal, and some are made of other stuff — like plastic, which is smooth, or wood, which feels rough. I have a fun idea to figure out what THIS playground is made of!"
3. (wait 2s) (inviting) "This slide is metal — hard, shiny, and cold to touch! But look around. Are ALL the playground things metal? Or are some made of something else? I bet we can find out together!"

**Screen:** Slide photo centered with metallic sheen highlight and a small "METAL" label with shiny icon near the surface.


#### Step 2: Rule Introduction + Demo

**AI says:** (excited scientist) "Okay — here is my big question. Out of ALL the playground things, do you think MOST of them are made of metal... or MOST of them are made of something else — like plastic, wood, or rubber? This is your PREDICTION. What do you think — mostly metal, or mostly NOT metal?"

**Child responses:**

1. (Ideal — picks metal) "Metal!" / "I think most are metal!" / "Everything is shiny!"
2. (Ideal — picks not-metal) "Not metal!" / "I think plastic!" / "Wood!"
3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"

**AI follow-up:**

1. (locking it in) "You predict MOSTLY METAL — got it! I'm writing that down. Now here's the deal — you are a Playground Scientist! Your job: find 3 more playground things, take a photo of each one, and tell me what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
2. (locking it in) "You predict MOSTLY NOT METAL — interesting! I'm writing that down. Now here's the deal — you are a Playground Scientist! Your job: find 3 more playground things, take a photo of each one, and tell me what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
3. (encouraging) "A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST playground things are metal, or mostly something else like plastic or wood? Just pick one!"

**Screen:** Scientist mission card with "Playground Scientist" badge. Tally board with two columns: "Metal" (shiny icon) and "Not Metal" (plastic/wood/rubber icons). Slide photo under "Metal" with "1" tally. Prediction banner at top: "My prediction: Mostly [Metal / Not Metal]!" Three empty photo slots below.


#### Step 3: Multi-Round Interaction

**Round 1 — First Evidence:**

*(Child photographs something — e.g., the swings)*

**AI says:** (eager scientist) "Evidence number two! Oh, I see the swings! Let me look closely at this photo... (examining) The seat looks dark and soft — not shiny like metal at all. I think that's RUBBER! Rubber is soft so it doesn't hurt when you sit. That goes in the NOT METAL column!"

**Child responses:**

1. (Ideal) "Yeah, it IS rubber!" / "I thought it was plastic!" / "The chain is metal though!"
2. (Unexpected) "I like swinging!" / "It's black!"
3. (No response) Looks at the tally.

**AI follow-up:**

1. (writing it down excitedly) "Great observation! The tally so far: Metal has 1, Not Metal has 1. It's a TIE right now! Your prediction says mostly [metal/not-metal]... let's see what happens next! Two more to find, Scientist!"
2. (validating) "Black — yes! And that black, bendy-looking seat is rubber. NOT metal! Tally update: Metal 1, Not Metal 1. It's TIED! Two more, Scientist!"
3. (wait 2s) (announcing) "So that's rubber — NOT metal! The tally is tied: Metal 1, Not Metal 1! Two more to go. Find another playground thing and take a photo!"

**Screen:** New photo in slot 2. Tally board updates with animated tally mark. Running score: "Metal: 1 | Not Metal: 1." Prediction banner stays visible at top.

**Round 2 — Second Evidence:** Child photographs another piece (climbing structure, bench, etc.). AI examines the photo and announces the material: "Let me look... I can see [visual cues]. That's [MATERIAL]!" AI updates tally dramatically: "Not Metal is WINNING!" or "Metal is catching up!" One more piece of evidence to go.

**Round 3 — Third Evidence (Final Piece):** Child photographs final piece (tunnel, rubber mat, fence, seesaw). AI builds to climax: "The LAST piece! Let me look very carefully..." AI assesses material from photo and announces result. Adds final tally mark and announces the BIG RESULT is coming. Includes stuck branch: "Look near the sandbox for a wooden border, or check the ground under the swings for rubber!"


#### Step 4: Celebration

**AI says:** (drumroll voice) "Okay Playground Scientist — time for the BIG REVEAL! You predicted that most playground things would be... MOSTLY [METAL / NOT METAL]! Let's count the evidence!"

*(AI tallies aloud)*

"The slide — METAL! That's one for metal. The [find 1] — [material]! The [find 2] — [material]! The [find 3] — [material]!"

**If prediction was RIGHT**: (triumphant fanfare) "The final count: Metal [N], Not Metal [M]! Your prediction was... RIGHT! You KNEW it! Most things at this playground really ARE [mostly metal / mostly not-metal]! Playground Scientist, your instincts are amazing!"

**If prediction was WRONG**: (gasping with delight) "The final count: Metal [N], Not Metal [M]! Your prediction was mostly [metal/not-metal], but SURPRISE — the playground TRICKED you! More things are actually [metal/not-metal] than you expected! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"

**If it's a TIE**: (amazed) "The final count: Metal 2, Not Metal 2! It's a PERFECT TIE! Nobody could have predicted that — the playground uses BOTH equally! That's a surprise result, Scientist!"

**AI says:** (warm, wonder-filled) "You know what's really smart about playgrounds? They use DIFFERENT materials on purpose! The slide is metal because metal is smooth — that helps you zoom. The ground under the swings is rubber because rubber is soft — that keeps you safe if you fall. Every material has a REASON! Which material surprised you the most today?"

**Child responses:**

1. (Ideal) "I was right!" / "Rubber! I didn't know it was under the swings!" / "I want to test another playground!"
2. (Unexpected) "I like metal best!" / "But I thought the swing was metal!"
3. (No response) Child looks at the tally screen.

**AI follow-up:**

1. (delighted) "That's what scientists DO — they guess, then check, and find out for real! Your experiment showed you something new about this playground!"
2. (enthusiastic) "Great observation! The swing CHAIN is metal, but the SEAT is rubber. One piece of equipment can have DIFFERENT materials — that's a scientist-level discovery!"
3. (wait 2s) (gentle) "Every material is here for a reason — smooth for speed, soft for safety, strong for climbing. Your experiment helped you see that!"

**Screen:** Full tally board with all 4 photos in two columns (Metal vs. Not Metal). Prediction banner lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one. Large final score: "Metal: [N] | Not Metal: [M]." Reason arrows connect each photo to a purpose bubble.


#### Step 5: Closing + IB Concepts

**AI says:** (proud celebration) "Congratulations, Playground Scientist! You did real science today! You looked closely at the Form of every piece — what it's made of, how it feels, what it looks like. And you discovered the Causation — WHY each material is there. Metal for strength. Rubber for safety. Wood for grip. Every material has a reason! You earned your Playground Scientist Badge!"

**Child responses:**

1. (Engaged) Cheers, talks about wanting to test more playgrounds, or asks about the badge.
2. (Quiet) Smiles or says nothing.
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (encouraging) "Next time you visit a playground, try the experiment again! Predict first, then count. Every playground might have a different answer. See you on the next experiment, Scientist!"
2. (warm) "Your badge is saved! You're a real Playground Scientist now. Bye for now, Scientist!"
3. (wait 2s) (soft) "Your Scientist Badge is glowing. Great experiment today!"

**Screen:** Golden "Playground Scientist Badge" shaped like a magnifying glass with tally chart inside. Slide photo at center with collection photos as insets. "Form" in crystalline letters with material texture swatches and "Causation" in arrow-shaped dynamic letters float artistically. Final tally result glows beneath.
