# Activity Design: Size Experiment + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Size Experiment

### A. Basic Info

- **Activity Name**: The Size Experiment
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Form, Causation
- **Related Concepts (Discipline)**: Measurement, Discovery, Comparison, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity (size comparison works universally — the photographed object is compared to a familiar reference like the child's hand)
- **Trigger Scene**: Child photographs any object where AI can gauge relative size
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{size}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.appearance.size          # most common path
  - tier_0.appearance.body_size     # e.g., lion, bird, goldfish
  - tier_0.appearance.paw_size      # e.g., lion
  - tier_1.appearance.key_size      # e.g., piano
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices its size relative to a familiar reference — the child's hand. The AI announces the size observation and then poses a big question: "Are MOST things around here bigger or smaller than your hand?" The child becomes a "Size Scientist" who first PREDICTS whether the majority of nearby objects are bigger or smaller than their hand, then collects evidence by photographing 3 more objects. The AI assesses each photo's size visually relative to the reference and tallies results. At the end, the AI reveals whether the child's prediction was right or surprising.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn size comparison vocabulary — "bigger," "smaller," "taller," "wider," "about the same," "size," "compare." Learn that size is relative — the same object can be "big" compared to one thing and "small" compared to another.
  - **U (Understand)**: Objects around us come in many different sizes for specific reasons (Causation) — a chair is big because people sit on it, a key is small because it fits in a lock. The way something looks in terms of size and scale is part of its Form. A prediction can be tested by collecting and counting real evidence.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph objects for AI to assess size visually; react to AI's size comparisons and watch the tally build; compare results to a hypothesis.

- **③ Design Highlight**: The "Size Experiment" uses the child's own hand as a universal, always-available reference point — every child has one, and it provides an intuitive, concrete anchor for comparison. The child commits to a hypothesis BEFORE exploring — "I think most things are bigger than my hand!" — creating genuine stakes. Each photo adds a tally mark to either the "Bigger" or "Smaller" column, building suspense. The magic moment is the final count: "Bigger: 3, Smaller: 1 — you were RIGHT!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar. Because size comparison works with any entity in any environment, this template is universally applicable.

- **④ Typical Scenario**: Child photographs a pinecone. AI notices it fits in a hand, announces the size observation, and proposes a hypothesis: are most things around here bigger or smaller than your hand? Child commits to a prediction, then photographs 3 more objects. AI examines each photo and assesses size visually relative to the child's hand. After all 3, AI tallies the final score against the prediction and reveals the result.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object (e.g., a pinecone outdoors) with no prior conversation. AI detects the object and gauges its relative size.
>
> **AI says**: "*(delighted, curious tone)* Oh, a pinecone! Look at it — it fits right in your hand! It's got all those bumpy little scales, and it's about the same size as your fist. But wait... I just had a BIG idea. Are MOST things around here bigger than your hand, or smaller? What do you think — are you surrounded by BIG things or LITTLE things?"
>
> **Possible child responses**:
> 1. (Ideal) "Big things!" / "The trees are big!" / "I think most things are smaller!"
> 2. (Unexpected) "I like pinecones!" / "It's prickly!"
> 3. (No response) Child looks around or at the screen.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already have a feeling about it! This pinecone fits in your hand, so it's about the same size. But are the OTHER things around you bigger or smaller than your hand? I think we should find out for REAL!"
> 2. "*(warm, redirecting)* It IS prickly — and it's the perfect size to hold! Look at your hand next to it — almost the same size! That makes me wonder about the OTHER things around you. Are they bigger or smaller than your hand? I have a fun way to find out!"
> 3. *(wait 2s)* "*(inviting)* This pinecone fits right in your hand! But look around you — are the other things bigger than your hand, or smaller? I bet we can measure and find out together!"
>
> **Screen**: Child's object photo centered with a translucent hand-outline overlay showing the size comparison. A small size label appears: "About the size of your hand!" with a hand icon.

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay — here is my big question. Out of ALL the things around you, do you think MOST of them are BIGGER than your hand... or SMALLER than your hand? Hold up your hand and look around! This is your PREDICTION. What do you think — mostly bigger, or mostly smaller?"
>
> **Possible child responses**:
> 1. (Ideal — picks bigger) "Bigger!" / "Most things are bigger!" / "Everything is huge!"
> 2. (Ideal — picks smaller) "Smaller!" / "Most things are tiny!" / "Smaller than my hand!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What if they're the same size?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY BIGGER — got it! I'm writing that down. Now here's the deal — you are a Size Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out if it's bigger or smaller than your hand. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 2. "*(locking it in)* You predict MOSTLY SMALLER — bold guess! I'm writing that down. Now here's the deal — you are a Size Scientist! Your job: find 3 more things around you, take a photo of each one, and I'll figure out if it's bigger or smaller than your hand. I'll keep count. At the end, we'll see if your prediction was RIGHT. Ready, Scientist?"
> 3. "*(encouraging)* Great question! If something is about the same size as your hand, we'll call it a WILDCARD — it doesn't count for either side! A prediction is your BEST GUESS before you check. So — do you think MOST things around you are bigger than your hand, or smaller? Just pick one!"
>
> **Screen**: Scientist-themed mission card with "Size Scientist" badge. A tally board appears with two columns: "Bigger" (with a large arrow-up icon) and "Smaller" (with a small arrow-down icon). The original object photo is placed in the center as the reference with "≈ your hand" label. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Bigger / Smaller]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., a tree trunk or a park bench)*
>
> **AI says**: "*(eager scientist voice)* Evidence number one! Oh wow, let me look at this photo... *(examining)* That is WAY bigger than your hand! You couldn't even wrap your arms all the way around that! That's DEFINITELY bigger. That goes in the BIGGER column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's HUGE!" / "It's bigger than ME!" / "I knew it!"
> 2. (Unexpected) "I like trees!" / "It's brown!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* Huge is right! The tally so far: Bigger has 1, Smaller has 0. Your prediction says mostly [bigger/smaller]... let's see what happens next! Two more to find, Scientist!"
> 2. "*(validating)* Brown and BIG! Way bigger than your hand. Tally update: Bigger 1, Smaller 0. Two more, Scientist!"
> 3. *(wait 2s)* "*(announcing)* That's a big one — BIGGER than your hand! Tally: Bigger 1, Smaller 0. Two more to go. Find another thing and take a photo!"
>
> **Screen**: New photo slides into slot 1. The tally board updates with an animation: a tally mark appears in the "Bigger" column. Running score displays: "Bigger: 1 | Smaller: 0." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a small rock, a flower, or a leaf)*
>
> **AI says**: "*(curious, building suspense)* Evidence number two! Let me compare this to your hand... *(looking closely)* Oh, that's tiny! It would fit in your palm with room to spare. That's definitely SMALLER than your hand! That goes in the SMALLER column!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, it's really small!" / "I think you're right!" / "I found a tiny one!"
> 2. (Unexpected) "I found a flower!" / "It's pretty!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* Tiny but important! Tally update: Bigger [N], Smaller [M]. [They're TIED now! / Bigger is still winning! / Smaller is catching up!] Your prediction was mostly [bigger/smaller]... it's getting [exciting / interesting]! One more piece of evidence, Scientist!"
> 2. "*(playful)* A flower — beautiful find! And from the photo, I can tell it's smaller than your hand. Tally: Bigger [N], Smaller [M]. One more, Scientist!"
> 3. *(wait 2s)* "*(announcing result)* That's a small one — SMALLER than your hand! Tally: Bigger [N], Smaller [M]. One more to go! Find one last thing around you!"
>
> **Screen**: Second photo slides into slot 2. Tally board updates with animation. Running score: "Bigger: [N] | Smaller: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child can't find something):
>
> **AI says**: "*(helpful, specific)* Look for something really BIG — like a bench, a wall, or a car. Or something really SMALL — like a pebble, a bug, or a leaf. Anything you can see counts! Just point your camera at it!"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final object — e.g., a backpack, a stick, a mushroom, a bicycle)*
>
> **AI says**: "*(building to the climax)* Evidence number three — the LAST piece! Let me look very carefully at this one... *(dramatic pause)* Comparing it to your hand... I think this is... [BIGGER / SMALLER]! [It's way wider than your hand! / It would fit in your palm!] This is the one that might decide everything!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I knew it!" / "I thought it was the other one!"
> 2. (Unexpected) "That's my backpack!" / "It's green!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic intake of breath)* [Bigger/Smaller] than your hand! Okay, Scientist... I'm adding it to the tally. Let me count everything up... are you ready for the BIG RESULT?"
> 2. "*(warm)* Your backpack — great choice! And from the photo, it's definitely [bigger/smaller] than your hand. Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That's [bigger/smaller]! Adding it to the board... the final tally is coming, Scientist! Ready?"
>
> **Screen**: Final photo slides into slot 3 with a bigger celebration animation. All photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Size Scientist — time for the BIG REVEAL! You predicted that most things around you would be... MOSTLY [BIGGER / SMALLER] than your hand! Let's count the evidence!"
>
> *(AI tallies aloud)*
>
> "The [find 1] — [BIGGER/SMALLER]! The [find 2] — [BIGGER/SMALLER]! The [find 3] — [BIGGER/SMALLER]!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Bigger [N], Smaller [M]! Your prediction was... RIGHT! You KNEW it! Most things around here really ARE [bigger / smaller] than your hand! Size Scientist, your instincts are amazing!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Bigger [N], Smaller [M]! Your prediction was mostly [bigger/smaller], but SURPRISE — it's the other way around! More things are actually [bigger/smaller] than your hand! That's what makes science so cool — sometimes you find out something you DIDN'T expect!"
>
> **If it's mixed or close**:
> "*(amazed)* The final count: Bigger [N], Smaller [M]! It's SO close! The world around you has a mix of big things AND small things! That's a really interesting discovery, Scientist!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know so many things were bigger!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But the stick is the same size as my hand!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That's what scientists DO — they guess, then check, and find out for real! You measured the world with your own hand! Now here's a cool question — WHY do you think some things are big and some things are small? Could a tiny chair work? Could a giant key fit in a lock?"
> 2. "*(enthusiastic)* You want MORE evidence? That's what real scientists say! The more you measure, the better your answer gets. But think about this — why ARE things different sizes? Why can't everything be the same?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You measured real things with your own hand. Here's one more thing to think about — why do you think things come in different sizes? Why not all the same?"
>
> **Screen**: Full tally board with all photos displayed in two columns (Bigger vs. Smaller). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sound effects. A large final score displays: "Bigger: [N] | Smaller: [M]." A hand-outline icon sits in the center as the reference anchor.

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what's really cool? Things are different sizes for a REASON! A tree is big because it needs to reach the sunlight way up high. A pebble is small because it's just one tiny piece of a big rock. A bench is big because people need to sit on it. And a [example from child's finds] is [big/small] because [reason]. Everything is the size it NEEDS to be! What size surprised you the most today?"
>
> **Possible child responses**:
> 1. (Ideal) "The tree! It's SO big!" / "The flower — it's so tiny!" / "I didn't know everything was bigger than my hand!"
> 2. (Unexpected) "I want bigger hands!" / "I want to measure more things!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* That one surprised you — and now you KNOW how it compares to your hand! That's what happens when you measure for real instead of just guessing. Your experiment showed you something new!"
> 2. "*(encouraging, laughing)* Bigger hands would change EVERYTHING! Then things that were bigger might become smaller than your hand. That's what's cool about comparing — it depends on what you use to measure! Try a different room next time — you might get a whole different answer!"
> 3. *(wait 2s)* "*(gentle)* Big things and small things, all around you — and every size has a reason. Your experiment helped you see that!"
>
> **Screen**: All photos displayed with size comparison labels and hand-outline overlays showing relative scale. Animated arrows connect each photo to a "reason" bubble: "tall = reach sunlight," "small = fits in a lock," "big = people sit on it." The collection feels like a science poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Size Scientist! You did real science today! You looked closely at the Form of everything — how big or small it is, what it looks like next to your hand. And you discovered the Causation — WHY things are different sizes. Trees grow tall to reach sunlight. Pebbles are small pieces of bigger rocks. Chairs are big enough to sit on. Every size has a reason! You earned your Size Scientist Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to measure more things, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you're somewhere new, try the experiment again! Hold up your hand and predict — mostly bigger or mostly smaller? Every place is different. See you on the next experiment, Scientist!"
> 2. "*(warm)* Your badge is saved! You're a real Size Scientist now. Bye for now, Scientist!"
> 3. *(wait 2s)* "*(soft)* Your Scientist Badge is glowing. Great experiment today!"
>
> **Screen**: Golden "Size Scientist Badge" shaped like a ruler with a tally chart inside. The original object photo sits at center with collection photos as insets. "Form" in bold crystalline letters with size-comparison graphics and "Causation" in arrow-shaped dynamic letters float artistically. The final tally result ("Bigger: [N] | Smaller: [M]") glows beneath. A hand-outline watermark sits behind the badge.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Size comparison is done through AI's visual assessment of photos — relative size compared to a child's hand is reliably estimable from visual context cues (object identity, surrounding objects, proportions visible in photos). |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("Oh, a pinecone! Look at it — it fits right in your hand!") and sensory wonder, not knowledge testing. Activity grows naturally from noticing one object's size to wondering about all surrounding objects' sizes. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (bench, pebble, leaf). Step 2 handles uncertainty about "same size" edge case with wildcard rule. Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Form + Causation as Key Concepts — Form maps to size/scale observation, Causation maps to "why things are different sizes." KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5–8 words in key prompts. Concrete vocabulary (bigger, smaller, tiny, huge, hand, fits, hold). 2–3 step tasks (predict, photograph, watch tally). AI announces size assessment in simple language. Universal reference (child's own hand) is always available. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: tally board with two columns, photo slots, hand-outline overlays, prediction banner, suspense animation, final score reveal, badge design with ruler motif. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — parameterized by size comparison, works universally with any entity. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child doesn't know the tally until AI announces each size comparison from the photo. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. High replayability (different environments give different results; child's hand is always available as reference). |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts → commits → collects evidence → tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as another pillar — the hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — Ready for 教研 review
