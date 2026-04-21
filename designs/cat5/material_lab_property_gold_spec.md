# Activity Design: Material Lab + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Material Lab

### A. Basic Info

- **Activity Name**: The Material Lab
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Form, Causation
- **Related Concepts (Discipline)**: Structure, Discovery, Properties, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected material attribute (metal, wood, plastic, natural, fabric, glass, stone, etc.)
- **Trigger Scene**: Child photographs any object where AI detects a clear material property
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works

### A.1 Entity Attributes Covered

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

- **① Brief Description**: After the child photographs any object, the AI notices what material it is made of — metal, wood, plastic, fabric, stone, or another visually identifiable material. The AI announces the material and then poses a big question: "Are MOST things around here made of {material}, or something else?" The child becomes a "Material Scientist" who first PREDICTS whether the majority of nearby objects share the same material, then collects evidence by photographing 3 more objects. The AI assesses each photo's material visually and tallies results. At the end, the AI reveals whether the child's prediction was right or surprising.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn material vocabulary — "metal," "wood," "plastic," "fabric," "stone," "natural," "material." Learn that different objects are made of different materials for different reasons — metal is strong and shiny, wood is warm and rough, plastic is light and smooth, fabric is soft and flexible.
  - **U (Understand)**: Objects around us are made of specific materials for specific reasons (Causation) — the material's visible and tactile properties (Form) determine where and how it is used. A prediction can be tested by collecting and counting real evidence.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph objects for AI to assess materials visually; react to AI's assessments and watch the tally build; compare results to a hypothesis.

- **③ Design Highlight**: The "Material Lab" metaphor turns any room or environment into a science laboratory. The child commits to a hypothesis BEFORE exploring — "I think most things are metal!" — creating genuine stakes. Each photo adds a tally mark to either the "{material}" or "not {material}" column, building suspense. The magic moment is the final count: "Metal: 2, Not Metal: 3 — SURPRISE!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar. Because the template is parameterized by any detected material, it works in kitchens (metal), playrooms (plastic), gardens (natural), bedrooms (fabric), and everywhere else.

- **④ Typical Scenario**: Child photographs a metal fork. AI notices the shiny metallic surface, announces "That's METAL!", and proposes a hypothesis: are most things in your kitchen metal, or something else? Child commits to a prediction, then photographs 3 more objects. AI examines each photo and assesses the material visually. After all 3, AI tallies the final score against the prediction and reveals the result.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object (e.g., a metal fork in the kitchen) with no prior conversation. AI detects the material from the photo.
>
> **AI says**: "*(delighted, curious tone)* Ooh, look at that fork! It's so shiny and smooth. That's METAL! Metal is hard and strong — that's why we eat with it. But wait... I'm looking around and I have a BIG question. Is EVERYTHING here made of metal? Or are some things made of something else? What do you think?"
>
> **Possible child responses**:
> 1. (Ideal) "Some things are different!" / "The table is wood!" / "I think most are metal!"
> 2. (Unexpected) "I don't know what metal is." / "I like forks!"
> 3. (No response) Child looks around the room or at the screen.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already have ideas! This fork is definitely metal — hard and shiny. But I wonder about the OTHER things around you. Are most of them metal too, or made of something different like wood or plastic? I think we should find out for REAL!"
> 2. "*(warm, explaining)* Metal is the hard, shiny stuff — like this fork! If you tap it, it goes CLINK. Some things around you are metal, and some are made of other stuff — like wood, which feels rough, or plastic, which is smooth and light. I have a fun idea to figure out what things around here are REALLY made of!"
> 3. *(wait 2s)* "*(inviting)* This fork is metal — hard, shiny, and cool to touch! But look around you. Are ALL the things here metal? Or are some made of something else? I bet we can find out together!"
>
> **Screen**: Child's object photo centered with a subtle material-appropriate highlight effect (metallic sheen for metal, warm grain for wood, smooth sheen for plastic). A small material label with an icon appears near the object surface (e.g., "METAL" with a shiny icon).

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay — here is my big question. Out of ALL the things around you, do you think MOST of them are made of metal... or MOST of them are made of something else — like wood, plastic, or fabric? This is your PREDICTION. What do you think — mostly metal, or mostly NOT metal?"
>
> **Possible child responses**:
> 1. (Ideal — picks the detected material) "Metal!" / "I think most are metal!" / "Everything is shiny!"
> 2. (Ideal — picks not-material) "Not metal!" / "I think wood!" / "Plastic!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY METAL — got it! I'm writing that down. Now here's the deal — you are a Material Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 2. "*(locking it in)* You predict MOSTLY NOT METAL — interesting! I'm writing that down. Now here's the deal — you are a Material Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 3. "*(encouraging)* A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST things around you are metal, or mostly something else like wood or plastic? Just pick one!"
>
> **Screen**: Scientist-themed mission card with "Material Scientist" badge. A tally board appears with two columns: "Metal" (with a shiny metallic icon) and "Not Metal" (with icons for wood, plastic, fabric). The original object photo is already placed under "Metal" with a "1" tally. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Metal / Not Metal]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., a wooden cutting board)*
>
> **AI says**: "*(eager scientist voice)* Evidence number two! Oh, let me look closely at this photo... *(examining)* I can see it's brown with little lines running through it — those are wood grain lines! I think that's WOOD! Wood is warm and natural — it comes from trees. That goes in the NOT METAL column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it IS wood!" / "I thought it was plastic!" / "The handle is metal though!"
> 2. (Unexpected) "I like cutting things!" / "It's brown!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* Great observation! The tally so far: Metal has 1, Not Metal has 1. It's a TIE right now! Your prediction says mostly [metal/not-metal]... let's see what happens next! Two more to find, Scientist!"
> 2. "*(validating)* Brown — yes! And that brown, grainy surface is wood. NOT metal! Tally update: Metal 1, Not Metal 1. It's TIED! Two more, Scientist!"
> 3. *(wait 2s)* "*(announcing)* So that's wood — NOT metal! The tally is tied: Metal 1, Not Metal 1! Two more to go. Find another thing and take a photo!"
>
> **Screen**: New photo slides into slot 2. The tally board updates with an animation: a tally mark appears in the appropriate column. Running score displays: "Metal: 1 | Not Metal: 1." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a plastic container or a glass cup)*
>
> **AI says**: "*(curious, building suspense)* Evidence number three! Let me examine this one... *(looking closely)* I can see it's [smooth and colorful / clear and see-through / soft and bendy]. That looks like [PLASTIC / GLASS / FABRIC] to me! [Plastic is smooth and comes in bright colors / Glass is clear and you can see right through it / Fabric is soft and you can fold it]!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's plastic!" / "I think you're right!" / "I thought it was something else!"
> 2. (Unexpected) "I found a cup!" / "It's blue!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* [Material] — that's [METAL / NOT METAL]! Tally update: Metal [N], Not Metal [M]. [Metal is catching up! / Not Metal is WINNING!] If your prediction was mostly [metal/not-metal]... it's getting [exciting / tricky]! One more piece of evidence, Scientist!"
> 2. "*(playful)* A cup — great find! Cups count too! And from the photo, I can see it's [material]. Tally: Metal [N], Not Metal [M]. One more, Scientist!"
> 3. *(wait 2s)* "*(announcing result)* I'm calling it — that's [material]! Tally: Metal [N], Not Metal [M]. One more to go! Find one last thing around you!"
>
> **Screen**: Third photo slides into slot 3. Tally board updates with animation. Running score: "Metal: [N] | Not Metal: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child can't find something):
>
> **AI says**: "*(helpful, specific)* Look for something you can hold, sit on, or put things in! Try looking at what's on the table, what's under your feet, or what you're wearing. Everything around you is made of SOMETHING!"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final object — e.g., a fabric towel, a plastic toy, a stone countertop)*
>
> **AI says**: "*(building to the climax)* Evidence number four — the LAST piece! Let me look very carefully... *(dramatic pause)* I see [description of visual material cues]. I think this is... [MATERIAL]! This is the one that might decide everything!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I knew it!" / "I thought it was something else!"
> 2. (Unexpected) "I don't know what it is!" / "It's red!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic intake of breath)* [Material]! Okay, Scientist... I'm adding it to the tally. Let me count everything up... are you ready for the BIG RESULT?"
> 2. "*(warm)* Red, yes! And from looking at the photo, I can see it's [material] — [smooth and colorful like plastic / soft and bendy like fabric / hard and shiny like metal]! Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That's [material]! Adding it to the board... the final tally is coming, Scientist! Ready?"
>
> **Screen**: Final photo slides into slot 4 with a bigger celebration animation. All 4 photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Material Scientist — time for the BIG REVEAL! You predicted that most things around you would be... MOSTLY [METAL / NOT METAL]! Let's count the evidence!"
>
> *(AI tallies aloud)*
>
> "The fork — METAL! That's one for metal. The [find 1] — [material]! The [find 2] — [material]! The [find 3] — [material]!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Metal [N], Not Metal [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [mostly metal / mostly not-metal]! Material Scientist, your instincts are amazing!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Metal [N], Not Metal [M]! Your prediction was mostly [metal/not-metal], but SURPRISE — you got TRICKED! More things are actually [metal/not-metal] than you expected! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"
>
> **If it's a TIE (2 and 2)**:
> "*(amazed)* The final count: Metal 2, Not Metal 2! It's a PERFECT TIE! Nobody could have predicted that — this place uses BOTH equally! That's a surprise result, Scientist!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know there was so much [material]!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But I thought the cup was metal!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That's what scientists DO — they guess, then check, and find out for real! You collected the evidence all by yourself. Now here's a cool question — WHY do you think people use [the winning material] so much around here? Why not just make everything out of one material?"
> 2. "*(enthusiastic)* You want MORE evidence? That's what real scientists say! The more you collect, the better your answer gets. But think about this — why do people use different materials? Why not make EVERYTHING out of metal?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You tested a real question with real evidence. Here's one more thing to think about — why do you think people use DIFFERENT materials for different things? Why not just one?"
>
> **Screen**: Full tally board with all 4 photos displayed in two columns (Metal vs. Not Metal). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sound effects. A large final score displays: "Metal: [N] | Not Metal: [M]."

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what's really smart about the things around us? People use DIFFERENT materials on purpose! The fork is metal because metal is strong — it won't break when you poke food. The [example from finds] is [material] because [material reason]. Every material has a REASON! Which material surprised you the most today?"
>
> **Possible child responses**:
> 1. (Ideal) "Wood! I didn't know that was wood!" / "Plastic — there's so much plastic!" / "Metal! There's less than I thought!"
> 2. (Unexpected) "I like metal best!" / "I want to test another room!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* [Material] surprised you — and now you KNOW! That's what happens when you test things for real instead of just guessing. Your experiment showed you something new about this place!"
> 2. "*(encouraging)* Another room — yes! Every room might have a DIFFERENT answer. The kitchen might be mostly metal, but the bedroom might be mostly fabric. You could test them all!"
> 3. *(wait 2s)* "*(gentle)* Every material is here for a reason — strong for eating, soft for sleeping, smooth for cleaning. Your experiment helped you see that!"
>
> **Screen**: All 4 photos displayed with material labels. Animated arrows connect each photo to a "reason" bubble: "strong = won't break," "soft = comfortable," "smooth = easy to clean," "light = easy to carry." The collection feels like a science poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Material Scientist! You did real science today! You looked closely at the Form of every object — what it's made of, how it looks, how it feels. And you discovered the Causation — WHY each material is used. Metal for strength. Wood for warmth. Plastic for lightness. Every material has a reason! You earned your Material Scientist Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to test more rooms, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you go to a different room, try the experiment again! Predict first, then count. Every room might have a different answer. See you on the next experiment, Scientist!"
> 2. "*(warm)* Your badge is saved! You're a real Material Scientist now. Bye for now, Scientist!"
> 3. *(wait 2s)* "*(soft)* Your Scientist Badge is glowing. Great experiment today!"
>
> **Screen**: Golden "Material Scientist Badge" shaped like a beaker with a tally chart inside. The original object photo sits at center with collection photos as insets. "Form" in bold crystalline letters with material texture swatches and "Causation" in arrow-shaped dynamic letters float artistically. The final tally result ("Metal: [N] | Not Metal: [M]") glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Material identification is done through AI's visual assessment of photos — material type (metal/plastic/wood/fabric/stone) is reliably identifiable from visual cues (shine, color, grain, surface texture visible in photos). |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("Ooh, look at that fork! It's so shiny and smooth") and sensory wonder, not knowledge testing. Activity grows naturally from noticing one object's material to wondering about all surrounding materials. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (table, floor, clothing). Step 2 handles uncertainty about what a "prediction" is. Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Form + Causation as Key Concepts — Form maps to material observation, Causation maps to "why this material here." KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5–8 words in key prompts. Concrete vocabulary (metal, wood, plastic, fabric, shiny, hard, soft, rough). 2–3 step tasks (predict, photograph, watch tally). AI announces material assessment in simple language. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: tally board with two columns, photo slots, prediction banner, suspense animation, final score reveal, badge design. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — parameterized by detected material, not a specific entity mapping. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child doesn't know the tally until AI announces each material from the photo. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. High replayability (different rooms/environments give different results). |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts → commits → collects evidence → tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as another pillar — the hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — Ready for 教研 review
