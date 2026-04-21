# Activity Design: Playground + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: The Playground Material Detective

### A. Basic Info

- **Activity Name**: The Playground Material Detective
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Form, Causation
- **Related Concepts (Discipline)**: Structure, Discovery, Safety, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Playground (child is at a real playground)
- **Trigger Scene**: Child photographs a piece of playground equipment (e.g., a slide) while physically present at the playground
- **Mapping Source**: none
- **IB Theme**: How the World Works

### A.1 Entity Attributes Covered

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

### A.2 Constellation Adaptation Notes

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

- **① Brief Description**: After photographing the slide, the AI marvels at how shiny and hard the metal surface is and wonders — is MOST of the playground made of metal, or something else? The child becomes a "Playground Scientist" who first PREDICTS whether most playground equipment is made of metal or not-metal (plastic, wood, rubber), then collects evidence by photographing 3 more pieces of equipment and reporting what each one is made of. At the end, the AI tallies the real data and reveals whether the child's prediction was right or surprising.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "metal," "plastic," "wood," "rubber," "material." Learn that playgrounds use different materials for different reasons — metal is strong, plastic is smooth, rubber is soft for safety, wood holds up outdoors.
  - **U (Understand)**: Different parts of a playground are made of different materials for specific reasons (Causation) — the material's properties (Form) determine where it is used. A prediction can be tested by collecting and counting real evidence.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph playground equipment for AI to assess materials visually; react to AI's assessments and watch the tally build; compare results to a hypothesis.

- **③ Design Highlight**: The "Material Detective" metaphor turns the playground into a science lab. The child commits to a hypothesis BEFORE exploring — "I think most things are metal!" — creating genuine stakes. Each find adds a tally mark to either the "metal" or "not-metal" column, building suspense. The magic moment is the final count: "Metal: 2, Not-metal: 3 — SURPRISE! More things are NOT metal! Your prediction was close but the playground tricked you!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar.

- **④ Typical Scenario**: Child photographs a metal slide, AI notices the shiny metal surface, proposes a hypothesis about whether most playground things are metal or not-metal, child commits to a prediction, then finds 3 more pieces of equipment, reports the material of each, and the AI tallies the final score against the prediction.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a slide (or other playground equipment) at the playground with no prior conversation.
>
> **AI says**: "*(delighted, curious tone)* Whoa — feel that slide! It's so shiny and hard. That's METAL! Metal is strong and smooth — that's why you zoom down so fast. But wait... I'm looking around this playground and I have a BIG question. Is EVERYTHING here made of metal? Or are some things made of something else? What do you think?"
>
> **Possible child responses**:
> 1. (Ideal) "Some things are different!" / "The swings are metal too!" / "I think it's all metal!"
> 2. (Unexpected) "I don't know what metal is." / "I like the slide!"
> 3. (No response) Child looks at the playground or the screen.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already have ideas! This slide is definitely metal — hard and shiny. But I wonder about the OTHER things. Are most of them metal too, or made of something different like plastic or wood? I think we should find out for REAL!"
> 2. "*(warm, explaining)* Metal is the hard, shiny stuff — like this slide! If you knock on it, it goes CLANG. Some things at playgrounds are metal, and some are made of other stuff — like plastic, which is smooth, or wood, which feels rough. I have a fun idea to figure out what THIS playground is made of!"
> 3. *(wait 2s)* "*(inviting)* This slide is metal — hard, shiny, and cold to touch! But look around. Are ALL the playground things metal? Or are some made of something else? I bet we can find out together!"
>
> **Screen**: Child's slide photo centered with a subtle metallic sheen highlight effect. A small "METAL" label with a shiny icon appears near the slide surface.

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay — here is my big question. Out of ALL the playground things, do you think MOST of them are made of metal... or MOST of them are made of something else — like plastic, wood, or rubber? This is your PREDICTION. What do you think — mostly metal, or mostly NOT metal?"
>
> **Possible child responses**:
> 1. (Ideal — picks metal) "Metal!" / "I think most are metal!" / "Everything is shiny!"
> 2. (Ideal — picks not-metal) "Not metal!" / "I think plastic!" / "Wood!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY METAL — got it! I'm writing that down. Now here's the deal — you are a Playground Scientist! Your job: find 3 more playground things, take a photo of each one, and tell me what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 2. "*(locking it in)* You predict MOSTLY NOT METAL — interesting! I'm writing that down. Now here's the deal — you are a Playground Scientist! Your job: find 3 more playground things, take a photo of each one, and tell me what it's made of. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 3. "*(encouraging)* A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST playground things are metal, or mostly something else like plastic or wood? Just pick one!"
>
> **Screen**: Scientist-themed mission card with "Playground Scientist" badge. A tally board appears with two columns: "Metal" (with a shiny metallic icon) and "Not Metal" (with icons for plastic, wood, rubber). The slide photo is already placed under "Metal" with a "1" tally. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Metal / Not Metal]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3–4 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., the swings)*
>
> **AI says**: "*(eager scientist voice)* Evidence number two! Oh, I see the swings! Let me look closely at this photo... *(examining)* The seat looks dark and soft — not shiny like metal at all. I think that's RUBBER! Rubber is soft so it doesn't hurt when you sit. That goes in the NOT METAL column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it IS rubber!" / "I thought it was plastic!" / "The chain is metal though!"
> 2. (Unexpected) "I like swinging!" / "It's black!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* Great observation! The tally so far: Metal has 1, Not Metal has 1. It's a TIE right now! Your prediction says mostly [metal/not-metal]... let's see what happens next! Two more to find, Scientist!"
> 2. "*(validating)* Black — yes! And that black, bendy-looking seat is rubber. NOT metal! Tally update: Metal 1, Not Metal 1. It's TIED! Two more, Scientist!"
> 3. *(wait 2s)* "*(announcing)* So that's rubber — NOT metal! The tally is tied: Metal 1, Not Metal 1! Two more to go. Find another playground thing and take a photo!"
>
> **Screen**: New photo slides into slot 2. The tally board updates with an animation: a tally mark appears in the appropriate column. Running score displays: "Metal: 1 | Not Metal: 1." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a climbing structure or a bench)*
>
> **AI says**: "*(curious, building suspense)* Evidence number three! Let me examine this one... *(looking closely)* I can see it's [brown with visible grain lines / colorful and smooth / shiny and reflective]. That looks like [WOOD / PLASTIC / METAL] to me! [Wood has those lines and that warm brown color / Plastic is smooth and comes in bright colors / Metal is shiny and you can almost see your reflection]!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's wood!" / "I think you're right!" / "I thought it was something else!"
> 2. (Unexpected) "I found a bench!" / "It's brown!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* [Material] — that's [METAL / NOT METAL]! Tally update: Metal [N], Not Metal [M]. [Metal is catching up! / Not Metal is WINNING!] If your prediction was mostly [metal/not-metal]... it's getting [exciting / tricky]! One more piece of evidence, Scientist!"
> 2. "*(playful)* A bench — great find! Benches count too! And from the photo, I can see it's [material]. Tally: Metal [N], Not Metal [M]. One more, Scientist!"
> 3. *(wait 2s)* "*(announcing result)* I'm calling it — that's [material]! Tally: Metal [N], Not Metal [M]. One more to go! Find one last playground thing!"
>
> **Screen**: Third photo slides into slot 3. Tally board updates with animation. Running score: "Metal: [N] | Not Metal: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child can't find something):
>
> **AI says**: "*(helpful, specific)* Look for something you can sit on, climb on, or hang from! Try near the sandbox — there might be a wooden border. Or look at the ground under the swings — is there rubber? Every playground thing counts!"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final piece — e.g., a plastic tunnel, rubber ground mat, wooden fence, seesaw)*
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
> 2. "*(warm)* Red, yes! And from looking at the photo, I can see it's [material] — [smooth and colorful like plastic / soft and squishy like rubber / shiny like metal]! Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That's [material]! Adding it to the board... the final tally is coming, Scientist! Ready?"
>
> **Screen**: Final photo slides into slot 4 with a bigger celebration animation. All 4 photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Playground Scientist — time for the BIG REVEAL! You predicted that most playground things would be... MOSTLY [METAL / NOT METAL]! Let's count the evidence!"
>
> *(AI tallies aloud)*
>
> "The slide — METAL! That's one for metal. The [find 1] — [material]! The [find 2] — [material]! The [find 3] — [material]!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Metal [N], Not Metal [M]! Your prediction was... RIGHT! You KNEW it! Most things at this playground really ARE [mostly metal / mostly not-metal]! Playground Scientist, your instincts are amazing!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Metal [N], Not Metal [M]! Your prediction was mostly [metal/not-metal], but SURPRISE — the playground TRICKED you! More things are actually [metal/not-metal] than you expected! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"
>
> **If it's a TIE (2 and 2)**:
> "*(amazed)* The final count: Metal 2, Not Metal 2! It's a PERFECT TIE! Nobody could have predicted that — the playground uses BOTH equally! That's a surprise result, Scientist!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know there was so much [material]!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But I thought the swing was metal!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That's what scientists DO — they guess, then check, and find out for real! You collected the evidence all by yourself. Now here's a cool question — WHY do you think playgrounds use [the winning material] so much? Why not just make everything out of one material?"
> 2. "*(enthusiastic)* You want MORE evidence? That's what real scientists say! The more you collect, the better your answer gets. But think about this — why do playgrounds use different materials? Why not make EVERYTHING out of metal?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You tested a real question with real evidence. Here's one more thing to think about — why do you think playgrounds use DIFFERENT materials? Why not just one?"
>
> **Screen**: Full tally board with all 4 photos displayed in two columns (Metal vs. Not Metal). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sound effects. A large final score displays: "Metal: [N] | Not Metal: [M]."

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what's really smart about playgrounds? They use DIFFERENT materials on purpose! The slide is metal because metal is smooth — that helps you zoom. The ground under the swings is rubber because rubber is soft — that keeps you safe if you fall. And [example from child's finds]. Every material has a REASON! Which material surprised you the most today?"
>
> **Possible child responses**:
> 1. (Ideal) "Rubber! I didn't know it was under the swings!" / "Wood — I thought everything was plastic!" / "Metal! There's less than I thought!"
> 2. (Unexpected) "I like metal best!" / "I want to test another playground!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* [Material] surprised you — and now you KNOW! That's what happens when you test things for real instead of just guessing. Your experiment showed you something new about this playground!"
> 2. "*(encouraging)* Another playground — yes! Every playground might have a DIFFERENT answer. Some might be mostly metal, some mostly plastic. You could test them all!"
> 3. *(wait 2s)* "*(gentle)* Every material is here for a reason — smooth for speed, soft for safety, strong for climbing. Your experiment helped you see that!"
>
> **Screen**: All 4 photos displayed with material labels. Animated arrows connect each photo to a "reason" bubble: "smooth = speed," "soft = safety," "strong = climbing," "rough = grip." The collection feels like a science poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Playground Scientist! You did real science today! You looked closely at the Form of every piece — what it's made of, how it feels, what it looks like. And you discovered the Causation — WHY each material is there. Metal for strength. Rubber for safety. Wood for grip. Every material has a reason! You earned your Playground Scientist Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to test more playgrounds, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you visit a playground, try the experiment again! Predict first, then count. Every playground might have a different answer. See you on the next experiment, Scientist!"
> 2. "*(warm)* Your badge is saved! You're a real Playground Scientist now. Bye for now, Scientist!"
> 3. *(wait 2s)* "*(soft)* Your Scientist Badge is glowing. Great experiment today!"
>
> **Screen**: Golden "Playground Scientist Badge" shaped like a magnifying glass with a tally chart inside. The slide photo sits at center with collection photos as insets. "Form" in bold crystalline letters with material texture swatches and "Causation" in arrow-shaped dynamic letters float artistically. The final tally result ("Metal: [N] | Not Metal: [M]") glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Material identification is done through AI's visual assessment of photos — material type (metal/plastic/wood/rubber) is reliably identifiable from visual cues (shine, color, grain, surface texture visible in photos). |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("Whoa — feel that slide! It's so shiny and hard") and sensory wonder, not knowledge testing. Activity grows naturally from noticing the slide's material to wondering about all playground materials. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (sandbox border, rubber under swings). Step 2 handles uncertainty about what a "prediction" is. Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Form + Causation as Key Concepts — Form maps to material observation, Causation maps to "why this material here." KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5–8 words in key prompts. Concrete vocabulary (metal, plastic, wood, rubber, shiny, hard, soft, rough). 2–3 step tasks (predict, photograph, watch tally). AI announces material assessment in simple language. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: tally board with two columns, photo slots, prediction banner, suspense animation, final score reveal, badge design. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in this assignment. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child doesn't know the tally until AI announces each material from the photo. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. High replayability (different playgrounds give different results). |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts → commits → collects evidence → tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as another pillar — the hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — Ready for 教研 review
