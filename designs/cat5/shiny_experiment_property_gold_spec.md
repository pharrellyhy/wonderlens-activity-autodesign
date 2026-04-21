# Activity Design: Shiny Experiment + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Shiny Experiment

### A. Basic Info

- **Activity Name**: The Shiny Experiment
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Form**, **Causation**
- **Related Concepts (Discipline)**: Structure, Discovery, Properties, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity where AI detects a shiny/reflective surface OR a matte/dull surface
- **Trigger Scene**: Child photographs any object where AI can visually assess shininess — reflective, glossy, metallic surfaces are SHINY; matte, rough, fabric, paper surfaces are DULL
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{shininess}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_1.appearance.shine_level                 # e.g., crayons
  - tier_1.appearance.reflective_strips           # e.g., raincoat
  - tier_2.appearance.surface_finish_glossiness   # e.g., raincoat
  - tier_1.appearance.scale_shimmer_pattern       # e.g., goldfish
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI assesses its shininess from the photo — is the surface reflective, glossy, metallic (SHINY) or matte, rough, textured (DULL)? The AI announces the assessment with excitement and then poses a big question: "Are MOST things around here SHINY or DULL?" The child becomes a "Shine Scientist" who first PREDICTS whether the majority of nearby objects are shiny or dull, then collects evidence by photographing 3 more objects. The AI is the property assessor — it examines each photo and announces "SHINY!" or "DULL!" based on visual evidence. The child does NOT self-report. At the end, the AI tallies results and reveals whether the child's prediction was right or surprising.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn surface vocabulary — "shiny," "dull," "reflective," "matte," "glossy," "rough," "smooth," "surface." Learn that shiny things reflect light (metal, glass, polished surfaces) and dull things absorb or scatter light (fabric, wood, paper, matte surfaces). Learn that "material" and "surface" determine how much something shines.
  - **U (Understand)**: Objects have surface properties (Form) that determine whether they appear shiny or dull — smooth, polished surfaces reflect light while rough, textured surfaces scatter it. WHY some things shine and others don't comes down to their material and how their surface is made (Causation). A prediction can be tested by collecting and counting real evidence.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph objects for AI to assess shininess visually; react to AI's assessments and watch the tally build; compare results to a hypothesis; reflect on WHY some things are shiny and some are dull.

- **③ Design Highlight**: The "Shine Scientist" metaphor turns any environment into a surface laboratory. The child commits to a hypothesis BEFORE exploring — "I think most things are SHINY!" — creating genuine stakes. The AI is the property assessor: it examines each photo and announces "I can see this is SHINY — it's reflecting light!" or "This looks DULL — no shine at all!" — the child does NOT self-report. Each photo adds a tally mark to either the "Shiny" or "Dull" column. The magic moment is the final count: "Shiny: 2, Dull: 3 — SURPRISE!" Shininess is highly visually verifiable from photos — reflective surfaces, metallic gleam, and glossy coatings are easy for AI to assess, as are matte textures, rough grains, and fabric weaves.

- **④ Typical Scenario**: Child photographs a shiny doorknob. AI notices the reflection and announces "That doorknob is SO shiny — I can almost see my reflection!" Then proposes a hypothesis: are most things in this room shiny like the doorknob, or more dull? Child commits to a prediction, photographs 3 more objects. AI examines each photo and announces "SHINY!" or "DULL!" with visual evidence. After all 3, AI tallies the final score against the prediction and reveals the result.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object (e.g., a shiny doorknob) with no prior conversation. AI assesses the surface shininess from the photo.
>
> **AI says**: "*(delighted, curious tone)* Whoa — look at that doorknob! It's SO shiny — I can almost see a reflection in it! That's because the surface is smooth and polished. Shiny things bounce light back like a tiny mirror! But wait... I'm looking around and I have a BIG question. Is EVERYTHING here SHINY like this doorknob? Or are some things more DULL? What do you think?"
>
> **Possible child responses**:
> 1. (Ideal) "Some things are dull!" / "The carpet is not shiny!" / "I think most things are shiny!"
> 2. (Unexpected) "I don't know what shiny means." / "I like doorknobs!"
> 3. (No response) Child looks around the room or at the screen.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already noticed! This doorknob is definitely SHINY — smooth and reflective. But I wonder about the OTHER things around you. Are most of them shiny too, or more dull and rough? I think we should find out for REAL!"
> 2. "*(warm, explaining)* Shiny means it SPARKLES — it bounces light back at you! Like this doorknob — see how it glows? Some things are shiny, and some things are DULL — they don't sparkle at all, like a towel or a book. I have a fun idea to figure out which ones are around here!"
> 3. *(wait 2s)* "*(inviting)* This doorknob is super shiny — smooth and glowing! But look around you. Are ALL the things here shiny? Or are some of them dull and rough? I bet we can find out together!"
>
> **Screen**: Child's object photo centered with a subtle sparkle highlight effect on the reflective surface. A small "SHINY!" label with a star icon appears near the object surface.

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay — here is my big question. Out of ALL the things around you, do you think MOST of them are SHINY... or MOST of them are DULL? Shiny things sparkle and reflect — like mirrors and metal and glass. Dull things don't sparkle — like fabric and wood and paper. This is your PREDICTION. What do you think — mostly SHINY, or mostly DULL?"
>
> **Possible child responses**:
> 1. (Ideal — picks shiny) "Shiny!" / "I think most things are shiny!" / "Everything sparkles!"
> 2. (Ideal — picks dull) "Dull!" / "I think most things are not shiny!" / "More rough things!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY SHINY — got it! I'm writing that down. Now here's the deal — you are a Shine Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll look really closely to see if it's SHINY or DULL. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 2. "*(locking it in)* You predict MOSTLY DULL — interesting! I'm writing that down. Now here's the deal — you are a Shine Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll look really closely to see if it's SHINY or DULL. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 3. "*(encouraging)* A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST things around you are SHINY and sparkly, or DULL and rough? Just pick one!"
>
> **Screen**: Scientist-themed mission card with "Shine Scientist" badge (a magnifying glass with a sparkle). A tally board appears with two columns: "Shiny" (with a sparkle/star icon) and "Dull" (with a matte circle icon). The trigger object photo is already placed under "Shiny" with a "1" tally. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Shiny / Dull]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., a fabric cushion)*
>
> **AI says**: "*(eager scientist voice)* Evidence number two! Oh, let me look closely at this photo... *(examining)* Hmm, I can see it's soft and textured — there's no sparkle, no reflection at all. This surface is rough and it absorbs all the light. I'm calling it — this is DULL! Fabric is almost always dull because it's made of tiny threads that scatter the light everywhere. That goes in the DULL column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's not shiny at all!" / "It's soft!" / "I thought it might be shiny because of the color!"
> 2. (Unexpected) "I like that pillow!" / "It's blue!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* Great observation! Soft and not shiny — definitely dull! The tally so far: Shiny has 1, Dull has 1. It's a TIE right now! Your prediction says mostly [shiny/dull]... let's see what happens next! Two more to find, Scientist!"
> 2. "*(validating)* Blue — yes! And even though it's a bright blue, it's still DULL — no sparkle, no reflection. Color doesn't mean shiny! Tally update: Shiny 1, Dull 1. It's TIED! Two more, Scientist!"
> 3. *(wait 2s)* "*(announcing)* So that's DULL — no shine at all! The tally is tied: Shiny 1, Dull 1! Two more to go. Find another thing and take a photo!"
>
> **Screen**: New photo slides into slot 2. The tally board updates with an animation: a tally mark appears in the "Dull" column. Running score displays: "Shiny: 1 | Dull: 1." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a glass window or a metal spoon)*
>
> **AI says**: "*(curious, building suspense)* Evidence number three! Let me examine this one... *(looking closely)* Oh WOW — I can see light bouncing right off the surface! It's smooth and [clear like glass / gleaming like metal]. This is definitely SHINY! [Glass is transparent and reflects light like a mirror / Metal is polished and catches every bit of light]! SHINY column gets another one!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's super shiny!" / "I can see myself in it!" / "I thought it would be shiny!"
> 2. (Unexpected) "I like looking through windows!" / "It's a spoon!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* SHINY! Tally update: Shiny [N], Dull [M]. [Shiny is WINNING! / It's still tied! / Dull is still ahead!] If your prediction was mostly [shiny/dull]... it's getting [exciting / tricky]! One more piece of evidence, Scientist!"
> 2. "*(playful)* A spoon — great find! And from the photo, I can see light bouncing right off it — definitely SHINY! Tally: Shiny [N], Dull [M]. One more, Scientist!"
> 3. *(wait 2s)* "*(announcing result)* I'm calling it — SHINY! Tally: Shiny [N], Dull [M]. One more to go! Find one last thing!"
>
> **Screen**: Third photo slides into slot 3. Tally board updates with animation. Running score: "Shiny: [N] | Dull: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child can't find something):
>
> **AI says**: "*(helpful, specific)* Look for something you can touch! Try looking at what's on the table — is it shiny or dull? What about the floor? Or your shoes? Even your shirt — is it shiny or dull? Everything has a surface!"
>
> **Screen**: A soft pulsing hint bubble with suggestions: "Try: what's on the table? What's on the floor? What are you wearing?"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final object — e.g., a wooden table, a paper book, a plastic toy)*
>
> **AI says**: "*(building to the climax)* Evidence number four — the LAST piece! Let me look very carefully... *(dramatic pause)* I see [description of surface visual cues — smooth/rough, reflecting/absorbing light, glossy/matte]. I think this is... [SHINY / DULL]! [It's catching the light beautifully! / There's no sparkle at all — just a soft, quiet surface.] This is the one that might decide everything!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I knew it!" / "I thought it was the opposite!"
> 2. (Unexpected) "I don't know if it's shiny!" / "It's brown!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic intake of breath)* [Shiny/Dull]! Okay, Scientist... I'm adding it to the tally. Let me count everything up... are you ready for the BIG RESULT?"
> 2. "*(warm)* Brown, yes! And from looking closely at the photo, I can see [it's reflecting a bit of light — SHINY / it's rough and matte — DULL]! Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That's [SHINY / DULL]! Adding it to the board... the final tally is coming, Scientist! Ready?"
>
> **Screen**: Final photo slides into slot 4 with a bigger celebration animation. All 4 photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Shine Scientist — time for the BIG REVEAL! You predicted that most things around you would be... MOSTLY [SHINY / DULL]! Let's count the evidence!"
>
> *(AI tallies aloud)*
>
> "The doorknob — SHINY! That's one for shiny. The [find 1] — [SHINY/DULL]! The [find 2] — [SHINY/DULL]! The [find 3] — [SHINY/DULL]!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Shiny [N], Dull [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [mostly shiny / mostly dull]! Shine Scientist, your eyes are AMAZING!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Shiny [N], Dull [M]! Your prediction was mostly [shiny/dull], but SURPRISE — you got TRICKED! More things are actually [shiny/dull] than you expected! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"
>
> **If it's a TIE (2 and 2)**:
> "*(amazed)* The final count: Shiny 2, Dull 2! It's a PERFECT TIE! Nobody could have predicted that — this place has BOTH equally! That's a surprise result, Scientist!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know there were so many dull things!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But I thought that one was shiny!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That's what scientists DO — they guess, then check, and find out for real! You collected the evidence all by yourself. Now here's a cool question — WHY do you think some things are shiny and some are dull? What makes something sparkle?"
> 2. "*(enthusiastic)* You want MORE evidence? That's what real scientists say! The more you collect, the better your answer gets. But think about this — why are some things shiny and some dull? Why not make everything sparkly?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You tested a real question with real evidence. Here's one more thing to think about — why do you think some things around you are shiny and some are dull? What's different about them?"
>
> **Screen**: Full tally board with all 4 photos displayed in two columns (Shiny vs. Dull). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sparkle sound effects. A large final score displays: "Shiny: [N] | Dull: [M]."

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what's really interesting? Things are shiny or dull because of what they're MADE of and how their surface is built! Metal and glass are SMOOTH — light bounces right off like a ball off a wall. But fabric and wood are ROUGH — light hits all those tiny bumps and goes flying in every direction, so you don't see a sparkle. The smoother the surface, the shinier it is! Which one surprised you the most today — a shiny thing or a dull thing?"
>
> **Possible child responses**:
> 1. (Ideal) "The cushion! I thought it might be shiny because it was colorful!" / "The spoon — it was SO shiny!" / "I didn't know wood was dull!"
> 2. (Unexpected) "I like shiny things best!" / "I want to test another room!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* That surprised you — and now you KNOW! Color doesn't make something shiny — the SURFACE does. That's what happens when you test things for real instead of just guessing. Your experiment showed you something new!"
> 2. "*(encouraging)* Another room — yes! A bathroom might be mostly SHINY (mirrors, tiles, faucets), but a bedroom might be mostly DULL (pillows, blankets, stuffed animals). You could test them all!"
> 3. *(wait 2s)* "*(gentle)* Smooth surfaces bounce light — that's shiny. Rough surfaces scatter light — that's dull. Your experiment helped you see the difference!"
>
> **Screen**: All 4 photos displayed with "Shiny" or "Dull" labels. Animated arrows connect each photo to a "why" bubble: "smooth surface = bounces light," "rough surface = scatters light," "polished metal = mirror-like," "fabric threads = no reflection." The collection feels like a science poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Shine Scientist! You did real science today! You looked closely at the Form of every object — how its surface looks, whether it sparkles or stays quiet. And you discovered the Causation — WHY some things are shiny and some are dull. Smooth surfaces reflect light. Rough surfaces scatter it. The material and the surface tell the whole story! You earned your Shine Scientist Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to test more rooms, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you're in a different room, try the experiment again! Bathrooms, kitchens, classrooms — every place has a different shiny-to-dull mix. Predict first, then count. See you on the next experiment, Scientist!"
> 2. "*(warm)* Your badge is saved! You're a real Shine Scientist now. Bye for now, Scientist!"
> 3. *(wait 2s)* "*(soft)* Your Scientist Badge is glowing — how shiny! Great experiment today!"
>
> **Screen**: Golden "Shine Scientist Badge" shaped like a magnifying glass with a sparkle inside and a tally chart reflected in its lens. The trigger object photo sits at center with collection photos as insets. "Form" in bold crystalline letters with surface texture swatches (smooth mirror vs. rough fabric) and "Causation" in arrow-shaped dynamic letters float artistically. The final tally result ("Shiny: [N] | Dull: [M]") glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Shininess assessment is done through AI's visual analysis of photos — reflective surfaces, metallic gleam, glossy coatings vs. matte textures, rough grains, fabric weaves are all highly visually identifiable from standard photos. |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("Whoa — look at that doorknob! It's SO shiny — I can almost see a reflection") and sensory wonder, not knowledge testing. Activity grows naturally from noticing one object's shininess to wondering about all surrounding surfaces. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (table, floor, clothing, shoes). Step 2 handles uncertainty about what a "prediction" is. Wait times specified for all silence branches. Round 1 addresses potential confusion between color and shininess. |
| 4 | IB Completeness | PASS | Form + Causation as Key Concepts — Form maps to surface property observation (shiny vs. dull), Causation maps to "why some things shine and others don't" (material, surface smoothness). KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5–8 words in key prompts. Concrete vocabulary (shiny, dull, sparkle, smooth, rough, reflect, surface). Binary property (shiny/dull) is simpler than material categories — very accessible for ages 4–6. 2–3 step tasks (predict, photograph, watch tally). AI announces shininess assessment in simple language. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says. AI's assessments always cite visible evidence ("I can see light bouncing off the surface" / "no sparkle, no reflection"). |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: tally board with two columns (Shiny with sparkle icon vs. Dull with matte icon), photo slots, prediction banner, suspense animation, final score reveal, badge design. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — parameterized by detected shininess/dullness property, not a specific entity mapping. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child doesn't know the verdict until AI announces each surface assessment from the photo. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. High replayability (different rooms/environments give different ratios). Potential for surprising discovers (colorful but dull, plain but shiny). |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts → commits → collects evidence → tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as another pillar — the hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — Ready for 教研 review
