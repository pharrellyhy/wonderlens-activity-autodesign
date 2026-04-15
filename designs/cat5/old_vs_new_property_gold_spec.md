# Activity Design: Old vs New + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Old vs New Survey

### A. Basic Info

- **Activity Name**: The Old vs New Survey
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Change** (How is it changing?)
- **Related Concepts (Discipline)**: Time, Transformation, Evidence, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing ideas)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity where AI detects visible age/wear
- **Trigger Scene**: Child photographs any object where AI detects visible signs of age or newness — a rusty fence, a faded sign, a shiny new toy, a cracked sidewalk, a brand-new backpack, etc.
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works
- **Template Parameters**: `{age_appearance}` — detected age/wear category (old-looking or new-looking). Old-looking visual cues: rust, cracks, peeling paint, faded colors, rounded edges from wear, moss/lichen, stains, scratches. New-looking visual cues: bright colors, clean surfaces, sharp edges, shiny, no scratches. Example value used throughout: **old-looking** (worn wooden bench trigger).

### B. Activity Overview

- **① Brief Description**: After photographing any object, the AI examines the photo and detects visible signs of age or newness — for example, worn wood, faded paint, and scratches on an old bench. The AI marvels at the evidence of time and wonders — are MOST things around here old-looking or new-looking? The child becomes a "Time Detective" who first PREDICTS whether most nearby things are old-looking or new-looking, then collects evidence by photographing 3 more items. The AI is the property assessor: it examines each photo for visual age cues (rust, cracks, fading, moss vs. bright colors, clean surfaces, sharp edges, shine) and announces its verdict. At the end, the AI tallies the real data and reveals whether the child's prediction was right or surprising. The insight: "Old things have STORIES — every scratch is an adventure they had! New things are just starting their adventures!"

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "old-looking," "new-looking," "faded," "worn," "rusty," "cracked," "shiny," "bright," "scratched," "smooth." Learn that you can tell how long something has been around by looking at its surface — rust, cracks, and fading mean it has been here a long time; bright colors and clean surfaces mean it is newer.
  - **U (Understand)**: Things have a **Form** that includes visible signs of age — rust, fading, cracks, moss, and worn edges are clues about how long something has existed. Things **Change** over time — surfaces fade, paint peels, metal rusts, edges round off, and moss grows. The way something looks NOW tells a story about its past.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph items for AI to assess visually as old-looking or new-looking; react to AI's assessments and watch the tally build; compare final results to a hypothesis.

- **③ Design Highlight**: The "Time Detective" metaphor turns any environment into a time-travel investigation. The child commits to a hypothesis BEFORE exploring — "I think most things here are old-looking!" — creating genuine stakes. Each find adds a tally mark to either the "Old-looking" or "New-looking" column, building suspense. The AI is the property assessor — it examines each photo for visual age cues (rust, cracks, faded colors, peeling paint, moss vs. bright colors, sharp edges, clean surfaces, shine) and announces its verdict, so the child does not self-report. These visual cues are among the most reliably identifiable properties in photos. The magic moment is the final count: "Old: 3, New: 2 — you were RIGHT! Most things here HAVE been around a long time!" The insight at the end — "Old things have STORIES — every scratch is an adventure!" — gives emotional depth. This creates the authentic "Was I right?!" feeling that defines the Discovery pillar.

- **④ Typical Scenario**: Child photographs an old wooden bench → AI notices worn surface, faded paint, scratches → "Your bench looks like it has been here a LONG time!" → proposes hypothesis about whether most things are old-looking or new-looking → child commits to a prediction → photographs 3 more items (a shiny new sign, a cracked sidewalk, a rusty fence) → AI assesses each from the photo → AI tallies the final score against the prediction.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object with visible age/wear cues (e.g., an old wooden bench with faded paint and scratches) with no prior conversation.
>
> **AI says**: "*(delighted, curious tone)* Ooh, look at that bench! See those scratches all over it? And the paint is all faded — it used to be brighter, but the sun and rain made it pale! And look — the edges are all smooth and worn, like LOTS of people have sat on it. This bench has been here a LONG time! But wait... I am looking around and I have a BIG question. Are MOST things around here old-looking like this bench? Or are most things new-looking — bright and shiny and clean? What do you think?"
>
> **Possible child responses**:
> 1. (Ideal) "Old!" / "New!" / "I see some old stuff!" / "That sign looks new!"
> 2. (Unexpected) "I like the bench!" / "What does old-looking mean?" / "I don't know."
> 3. (No response) Child looks around at the environment.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already have ideas! This bench is definitely old-looking — all that faded paint and those scratches. But I wonder about the OTHER things. Are they old-looking too, or new and shiny? I think we should find out for REAL!"
> 2. "*(warm, explaining)* Great question! Old-looking means it has clues that it has been here for a while — like scratches, faded colors, cracks, or rust. See how this bench paint is pale and worn? That is old-looking! New-looking means it is bright, shiny, clean, and smooth — like it was JUST made! I have a fun idea to figure out what this place is mostly like!"
> 3. *(wait 2s)* "*(inviting)* This bench has scratches and faded paint — it has been here a LONG time! But look around. Are ALL the things here old-looking? Or are some shiny and new? I bet we can find out together!"
>
> **Screen**: Child's photo centered with a subtle "aging" highlight effect — the scratches and faded areas gently glow to draw attention to the age cues. A small "OLD-LOOKING" label with a clock icon appears near the worn surface.

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay, Time Detective — here is my big question! Out of ALL the things around here, do you think MOST of them are OLD-LOOKING — scratched, faded, worn, rusty, cracked? Or do you think MOST of them are NEW-LOOKING — bright, shiny, clean, smooth? This is your PREDICTION. What do you think — mostly old-looking, or mostly new-looking?"
>
> **Possible child responses**:
> 1. (Ideal — picks old) "Old-looking!" / "I think old!" / "Everything looks worn!"
> 2. (Ideal — picks new) "New-looking!" / "I think shiny!" / "Most stuff is new!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY OLD-LOOKING — got it! I am writing that down. Now here is the deal — you are a Time Detective! Your job: find 3 more things around here, take a photo of each one, and I will look at the photo REALLY closely for clues — scratches, rust, fading, cracks for old, or bright colors, clean surfaces, and sharp edges for new. I will keep count. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
> 2. "*(locking it in)* You predict MOSTLY NEW-LOOKING — interesting! I am writing that down. Now here is the deal — you are a Time Detective! Your job: find 3 more things around here, take a photo of each one, and I will look at the photo REALLY closely for clues. I will keep count. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
> 3. "*(encouraging)* A prediction is your BEST GUESS before you check! Like saying 'I think it will rain today' before you look outside. So — take your best guess. Do you think MOST things here are old-looking — scratched and faded — or new-looking — bright and clean? Just pick one!"
>
> **Screen**: Detective-themed mission card with "Time Detective" badge — a magnifying glass with a clock face inside. A tally board appears with two columns: "Old-Looking" (with a cracked-clock icon) and "New-Looking" (with a sparkle icon). The bench photo is already placed under "Old-Looking" with a "1" tally. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Old-Looking / New-Looking]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3-4 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., a shiny new street sign)*
>
> **AI says**: "*(eager scientist voice)* Evidence number two! Oh, let me look at this photo closely... *(examining)* I can see bright paint — no fading at all! The edges are sharp and clean. The surface is smooth — no scratches, no rust, no cracks. This sign looks like it was put here RECENTLY! That is NEW-LOOKING! Into the New-Looking column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it IS new!" / "The colors are so bright!" / "I thought it would be old!"
> 2. (Unexpected) "I like the sign!" / "It says STOP!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* The tally so far: Old-Looking has 1, New-Looking has 1. It is a TIE right now! Your prediction says mostly [old/new]-looking... let us see what happens next! Two more to find, Detective!"
> 2. "*(playful)* It does say stop — and those bright red letters are SO clean and sharp! Definitely new-looking. Tally update: Old-Looking 1, New-Looking 1. It is TIED! Two more, Detective!"
> 3. *(wait 2s)* "*(announcing)* Those bright colors and sharp edges mean new-looking! The tally is tied: Old-Looking 1, New-Looking 1! Two more to go. Find another thing and take a photo!"
>
> **Screen**: New photo slides into slot 2. The tally board updates with an animation: a tally mark appears in the appropriate column. Running score displays: "Old-Looking: 1 | New-Looking: 1." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a cracked sidewalk with moss in the cracks)*
>
> **AI says**: "*(curious, building suspense)* Evidence number three! Let me examine this one... *(looking closely)* Ohhh — I can see BIG cracks running through the surface! And look — there is GREEN MOSS growing inside the cracks! Moss takes a long time to grow, so those cracks have been there for ages. The edges of the concrete are all rounded and worn. This sidewalk is definitely OLD-LOOKING!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's all cracked!" / "The moss is cool!" / "That changes things!"
> 2. (Unexpected) "I like stepping on cracks!" / "It's just the ground!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* Old-looking — another mark! Tally update: Old-Looking [N], New-Looking [M]. [Old-looking is pulling ahead! / It is neck and neck!] Your prediction of mostly [old/new]-looking is looking [strong / shaky / right on track]! One more piece of evidence, Detective!"
> 2. "*(validating)* Stepping on cracks — fun! And from the photo, I can see those cracks have been there a long time — moss is growing in them! That is OLD-LOOKING. Tally: Old-Looking [N], New-Looking [M]. One more, Detective!"
> 3. *(wait 2s)* "*(announcing result)* Those cracks and that moss mean it has been here a LONG time — OLD-LOOKING! Tally: Old-Looking [N], New-Looking [M]. One more to go! Find one last thing!"
>
> **Screen**: Third photo slides into slot 3. Tally board updates with animation. Running score: "Old-Looking: [N] | New-Looking: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child cannot find something):
>
> **AI says**: "*(helpful, specific)* Look for clues of TIME! Is there a fence or railing nearby — check for rust! Look at the ground — any cracks? Check the buildings — is the paint peeling or bright? Even look at a tree trunk — is it covered in scratches and bumps? Old and new are EVERYWHERE!"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final item — e.g., a rusty fence, a new playground, a faded poster)*
>
> **AI says**: "*(building to the climax)* Evidence number four — the LAST piece! Let me look very carefully at this photo... *(dramatic pause)* I see [description of visual age/wear cues — e.g., orange-brown rust flaking off the metal, or bright colorful plastic with smooth clean surfaces]. I think this is... [OLD-LOOKING / NEW-LOOKING]! [The rust tells me it has been here for years / Those bright colors and clean surfaces tell me it is brand new]! This is the one that might decide everything!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I knew it!" / "That changes everything!"
> 2. (Unexpected) "I don't know if it is old or new!" / "It's kind of both!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic intake of breath)* [Old-looking / New-looking]! Okay, Detective... I am adding it to the tally. Let me count everything up... are you ready for the BIG RESULT?"
> 2. "*(warm, thoughtful)* That is a great thought! Some things CAN be tricky — like a new bench with old stickers on it. But from the photo, the biggest clues point to [old-looking / new-looking] — I see [specific visual evidence]. Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That is [old-looking / new-looking]! Adding it to the board... the final tally is coming, Detective! Ready?"
>
> **Screen**: Final photo slides into slot 4 with a bigger celebration animation. All 4 photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Time Detective — time for the BIG REVEAL! You predicted that most things around here would be... MOSTLY [OLD-LOOKING / NEW-LOOKING]! Let us count the evidence!"
>
> *(AI tallies aloud)*
>
> "The bench — OLD-LOOKING! That is one for old. The [find 1] — [old/new]-looking! The [find 2] — [old/new]-looking! The [find 3] — [old/new]-looking!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Old-Looking [N], New-Looking [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [old/new]-looking! Time Detective, your instincts are amazing!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Old-Looking [N], New-Looking [M]! Your prediction was mostly [old/new]-looking, but SURPRISE — this place TRICKED you! More things are actually [old/new]-looking than you expected! That is what makes exploring so cool — sometimes the world surprises you!"
>
> **If it's a TIE (2 and 2)**:
> "*(amazed)* The final count: Old-Looking 2, New-Looking 2! It is a PERFECT TIE! This place has a mix of things that have been here a LONG time AND things that are brand new! What a discovery!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know there were so many old things!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But I think that sign was actually old!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That is what detectives DO — they guess, then check, and find out for real! You collected the evidence all by yourself. Now here is a cool thought — old things have STORIES! Every scratch, every crack, every bit of rust is a clue about something that happened to it. The wind, the rain, people touching it, the sun shining on it — all those things left their mark!"
> 2. "*(enthusiastic)* You want MORE evidence? That is what real detectives say! Every new thing you check gives you a better answer. But think about this — WHY do some things look old faster than others?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You tested a real question with real evidence. Here is a cool secret — every scratch and crack is like a DIARY. The old things have been writing their stories on their surfaces for years!"
>
> **Screen**: Full tally board with all 4 photos displayed in two columns (Old-Looking vs New-Looking). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sound effects. A large final score displays: "Old-Looking: [N] | New-Looking: [M]."

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what is really amazing? Old things have STORIES — every scratch is an adventure they had! Every crack is a chapter. Every bit of rust is a memory. That bench? All those scratches came from years and years of people sitting on it — kids like you! And new things? They are just starting their adventures! That shiny [new item]? Its story is just beginning — it has no scratches YET! Which one surprised you the most today — something old-looking or something new-looking?"
>
> **Possible child responses**:
> 1. (Ideal) "The sidewalk! I didn't know moss means it's old!" / "The sign! I thought everything was old!" / "The fence — it was SO rusty!"
> 2. (Unexpected) "I like old things!" / "I want to check my house!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* That one surprised you — and now you KNOW how to spot it! Moss, rust, cracks, faded colors — they are all clues about time. You are a real Time Detective now — you can read the stories on things!"
> 2. "*(encouraging)* Your house — yes! I bet your house has BOTH old-looking AND new-looking things. You could do a whole survey there! The doorknobs might be old-looking — scratched from thousands of turns. But the fridge might be new-looking — still shiny!"
> 3. *(wait 2s)* "*(gentle)* Every thing around you has a time story — rust, cracks, and fading tell you it has been here a while. Bright colors and clean surfaces tell you it is newer. Your survey helped you read those stories!"
>
> **Screen**: All 4 photos displayed with "Old-Looking" or "New-Looking" labels. Animated timeline arrows connect each photo to a "time story" bubble: "scratches from years of use," "bright paint = just installed," "moss grows slowly over years," "rust from rain and air." The collection feels like a time-travel field poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Time Detective! You did real detective work today! You looked closely at the **Form** of every thing — the scratches, the rust, the cracks, the bright paint, the clean surfaces. All those visual clues told you a story! And you discovered **Change** — things do not stay the same forever! Paint fades in the sun. Metal rusts in the rain. Surfaces get scratched from use. Everything is SLOWLY changing, all the time — and now you can SEE it! You earned your Time Detective Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to survey more places, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you go somewhere new, try the survey again! Predict first, then count. A brand-new mall would be VERY different from an old park! Every place has its own time story. See you on the next survey, Detective!"
> 2. "*(warm)* Your badge is saved! You are a real Time Detective now. Bye for now, Detective!"
> 3. *(wait 2s)* "*(soft)* Your Time Detective Badge is glowing. Great survey today!"
>
> **Screen**: Golden "Time Detective Badge" shaped like a magnifying glass with a clock face inside. The bench photo sits at center with collection photos as insets. **"Form"** in bold crystalline letters with texture-and-surface detail swatches and **"Change"** in arrow-shaped dynamic letters showing a transformation motif (bright color fading, sharp edge rounding, clean surface gaining scratches) float artistically. The final tally result ("Old-Looking: [N] | New-Looking: [M]") glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Age/wear assessment is done through AI's visual analysis of photos — rust, cracks, fading, moss vs. bright colors, clean surfaces, sharp edges are among the most reliably identifiable visual properties. No comparison between photos required. |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("See those scratches? The paint is all faded!") and sensory wonder, not knowledge testing. Activity grows naturally from noticing one item's age/wear to wondering about all nearby items. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (check fences for rust, ground for cracks, buildings for peeling paint, trees for bumps). Step 2 handles uncertainty about what a "prediction" is. Round 3 handles the "it's kind of both" edge case (new bench with old stickers). Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Form + Change as Key Concepts — Form maps to visual age/wear observation (scratches, rust, fading, brightness, clean surfaces), Change maps to temporal transformation (things do not stay the same — paint fades, metal rusts, surfaces wear). NOTE: IB Key Concept is Change (not Causation) because the game is about temporal transformation, not about why materials age differently. KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5-8 words in key prompts. Concrete vocabulary (old-looking, new-looking, scratched, faded, rusty, cracked, shiny, bright, clean, smooth). 2-3 step tasks (predict, photograph, watch tally). AI announces age assessment in simple language with specific visual evidence. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says with specific visual observations ("I see BIG cracks and GREEN MOSS growing inside them"). |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: aging highlight effect, tally board with two columns, photo slots, prediction banner, suspense animation, final score reveal, badge design with transformation motif. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — trigger is any entity with visible age/wear, not a specific entity. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child does not self-report, AI determines old-looking vs new-looking from the photo using specific visual evidence. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. The "Old things have STORIES" insight adds emotional depth. High replayability — different locations (old neighborhood, new mall, park, school) give very different results. |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts, commits, collects evidence, tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as Adventure (no quest criterion per find), Creation (no invention), Mystery (no hidden pattern), Performance (no audience), or Nurture (no rescue). The hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — property-bridge field_experiment template triggered by visible age/wear (old-looking vs new-looking). AI assesses age appearance from visual cues in each photo — rust, cracks, fading, moss vs. bright colors, clean surfaces, sharp edges.
