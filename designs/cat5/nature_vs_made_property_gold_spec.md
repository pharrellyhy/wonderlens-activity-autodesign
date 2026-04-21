# Activity Design: Nature vs Made + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Nature vs Made Survey

### A. Basic Info

- **Activity Name**: The Nature vs Made Survey
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?), **Causation** (Why is it like it is?)
- **Related Concepts (Discipline)**: Origin, Design, Classification, Pattern
- **ATL Skills Focus**: Research Skills (observation, data collection), Thinking Skills (critical thinking, analysis), Communication Skills (expressing ideas)
- **Experience Pillar**: Discovery
- **Game Style**: field_experiment
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with detected outdoor/environment attribute
- **Trigger Scene**: Child photographs any object outdoors — a bench, a rock, a fence, a tree, a car, a puddle, etc.
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{origin}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Natural-origin signals (living, habitat, growth)
  - tier_2.context.habitat_requirements   # e.g., butterfly, bird
  - tier_1.context.flower_visits          # e.g., butterfly
  - tier_2.change.full_metamorphosis      # e.g., insects
  # Made-origin signals (design, manufacture, storage)
  - tier_1.context.playroom               # e.g., toy_robot
  - tier_1.context.storage_spot           # e.g., crayons
  - tier_2.structure.modular_design       # e.g., toy_robot
```

### B. Activity Overview

- **① Brief Description**: After photographing any outdoor object, the AI identifies whether it is natural (made by nature) or man-made (made by people) and wonders — are MOST things around here natural or man-made? The child becomes a "Nature Detective" who first PREDICTS whether most nearby things are natural or man-made, then collects evidence by photographing 3 more items. The AI ASSESSES each photo (natural vs man-made is highly reliably identifiable visually — trees, rocks, puddles, clouds vs benches, fences, signs, cars). At the end, the AI tallies the real data and reveals whether the child's prediction was right or surprising.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "natural" and "man-made"; learn that natural things are made by nature (trees, rocks, water, soil, flowers, animals) and man-made things are built by people (benches, fences, signs, cars, buildings, paths); learn that some things combine both (a wooden bench uses natural wood shaped by people)
  - **U (Understand)**: Things around us have different origins — some were made by nature and some were made by people, and this is their Form (what they are made of and where they come from). The reason something is natural or man-made tells us about Causation — who or what created it and why it is here.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph items for AI to assess visually as natural or man-made; watch the tally build and react to each assessment; compare final results to a hypothesis

- **③ Design Highlight**: The "Nature Detective" metaphor turns any outdoor space into a survey zone. The child commits to a hypothesis BEFORE exploring — "I think most things here are natural!" — creating genuine stakes. Each find adds a tally mark to either the "Natural" or "Man-Made" column, building suspense. The AI is the property assessor — it examines each photo and announces its verdict, so the child does not self-report. The magic moment is the final count: "Natural: 3, Man-Made: 2 — you were RIGHT! Nature wins here!" This creates the authentic "Was I right?!" feeling that defines the Discovery pillar. Works universally outdoors — parks, streets, backyards, schoolyards all produce different and interesting results.

- **④ Typical Scenario**: Child photographs a wooden bench in a park, AI notices it is man-made from wood, proposes a hypothesis about whether most things around here are natural or man-made, child commits to a prediction, then photographs 3 more items (a tree, a rock, a lamppost), AI assesses each from the photo, and the AI tallies the final score against the prediction.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any outdoor object (e.g., a wooden bench) with no prior conversation.
>
> **AI says**: "*(delighted, curious tone)* Ooh, look at that bench! Someone BUILT this — they took wood, cut it into pieces, and put it all together so people could sit here. That means it is MAN-MADE — a person made it! But wait... I am looking around and I see trees and rocks and grass too. Those are NATURAL — nobody made those, they just grew! I have a BIG question. Are most things around here natural, or man-made? What do you think?"
>
> **Possible child responses**:
> 1. (Ideal) "Natural!" / "Man-made!" / "I see more trees!" / "There are lots of buildings!"
> 2. (Unexpected) "I like the bench!" / "What does man-made mean?" / "I don't know."
> 3. (No response) Child looks around at the environment.
>
> **AI follow-up**:
> 1. "*(intrigued)* Interesting — you already have ideas! The bench is definitely man-made — someone built it. But all those trees and rocks? Nature made those all by itself! I think we should find out what MOST things around here really are!"
> 2. "*(warm, explaining)* Great question! Man-made means a person BUILT it — like this bench! Someone cut the wood and put it together. Natural means nature made it all by itself — like a tree growing from a seed, or a rock that has been here for a long, long time. Nobody built the tree — it just grew! I have a fun idea to figure out what this place is mostly made of!"
> 3. *(wait 2s)* "*(inviting)* Look at this bench — a person built it from wood! That is man-made. But see those trees over there? Nobody built those — they grew by themselves! That is natural. I wonder which kind there is MORE of around here. Want to find out?"
>
> **Screen**: Child's photo centered with a subtle label appearing — "MAN-MADE" with a hammer icon (or "NATURAL" with a leaf icon, depending on what was photographed). The surrounding environment is softly visible, hinting at the survey to come.

**Step 2: Mission Briefing — Hypothesis + Setup**

> **AI says**: "*(excited scientist tone)* Okay, Nature Detective — here is my big question! Out of ALL the things around here, do you think MOST of them are NATURAL — made by nature, like trees and rocks and puddles? Or do you think MOST of them are MAN-MADE — built by people, like benches and fences and signs? This is your PREDICTION. What do you think — mostly natural, or mostly man-made?"
>
> **Possible child responses**:
> 1. (Ideal — picks natural) "Natural!" / "I think more nature!" / "Trees everywhere!"
> 2. (Ideal — picks man-made) "Man-made!" / "I see lots of buildings!" / "People made more stuff!"
> 3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"
>
> **AI follow-up**:
> 1. "*(locking it in)* You predict MOSTLY NATURAL — got it! I am writing that down. Now here is the deal — you are a Nature Detective! Your job: find 3 more things around here, take a photo of each one, and I will look at the photo and tell you if it is natural or man-made. I will keep count. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
> 2. "*(locking it in)* You predict MOSTLY MAN-MADE — interesting! I am writing that down. Now here is the deal — you are a Nature Detective! Your job: find 3 more things around here, take a photo of each one, and I will look at the photo and tell you if it is natural or man-made. I will keep count. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
> 3. "*(encouraging)* A prediction is your BEST GUESS before you check! Like saying 'I think it will be sunny today' before you look outside. So — take your best guess. Do you think MOST things here are natural — like trees and rocks — or man-made — like benches and signs? Just pick one!"
>
> **Screen**: Detective-themed mission card with "Nature Detective" badge — a magnifying glass with a leaf on one side and a gear on the other. A tally board appears with two columns: "Natural" (with a leaf icon) and "Man-Made" (with a hammer icon). The first photo is already placed under the correct column with a "1" tally. The child's prediction is stamped at the top in a speech bubble: "My prediction: Mostly [Natural / Man-Made]!" Three empty photo slots wait below.

**Step 3: Multi-Round Exploration (3-4 rounds)**

> **Round 1 — First Evidence:**
>
> *(Child photographs something — e.g., a tree)*
>
> **AI says**: "*(eager scientist voice)* Evidence number two! Oh wow, let me look at this photo closely... *(examining)* I see a big trunk going up, branches spreading out, and green leaves all over. That is a TREE! Did anyone build this? Nope — it grew from a tiny seed all by itself. That is NATURAL! Into the Natural column it goes!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah, trees are natural!" / "Nobody built a tree!" / "I knew that one!"
> 2. (Unexpected) "I like climbing it!" / "It's really big!"
> 3. (No response) Looks at the tally.
>
> **AI follow-up**:
> 1. "*(writing it down excitedly)* The tally so far: Natural has [N], Man-Made has [M]. [Natural is winning! / They are tied! / Man-Made is still ahead!] Your prediction says mostly [natural/man-made]... let us see what happens next! Two more to find, Detective!"
> 2. "*(playful)* It IS big — nature made it grow tall! And that big tree is definitely NATURAL. Tally update: Natural [N], Man-Made [M]. Two more to find, Detective!"
> 3. *(wait 2s)* "*(announcing)* That tree is NATURAL — nature made it grow all by itself! The tally is: Natural [N], Man-Made [M]! Two more to go. Find another thing and take a photo!"
>
> **Screen**: New photo slides into slot 2. The tally board updates with an animation: a tally mark appears in the appropriate column. Running score displays: "Natural: [N] | Man-Made: [M]." The child's prediction banner stays visible at the top.

> **Round 2 — Second Evidence:**
>
> *(Child photographs something — e.g., a lamppost, a rock, a fence)*
>
> **AI says**: "*(curious, building suspense)* Evidence number three! Let me examine this one... *(looking closely)* I can see [it is tall and metal with a light on top / it is rough and grey and heavy-looking / it has straight wooden boards in a row]. That looks like [a LAMPPOST — someone built that and put the light up there / a ROCK — nature made that, nobody built a rock / a FENCE — someone put those boards together in a line]! That is [MAN-MADE / NATURAL]!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I thought so!" / "That one surprised me!"
> 2. (Unexpected) "I found a big one!" / "It's really old!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic tally update)* [Natural/Man-Made] — another mark! Tally update: Natural [N], Man-Made [M]. [Natural is pulling ahead! / Man-Made is catching up! / It is neck and neck!] Your prediction of mostly [natural/man-made] is looking [strong / shaky / right on track]! One more piece of evidence, Detective!"
> 2. "*(validating)* Yes, and from the photo I can see it is [material/texture/shape] — that makes it [natural/man-made]! Tally: Natural [N], Man-Made [M]. One more, Detective!"
> 3. *(wait 2s)* "*(announcing result)* I am calling it — that is [NATURAL/MAN-MADE]! Tally: Natural [N], Man-Made [M]. One more to go! Find one last thing!"
>
> **Screen**: Third photo slides into slot 3. Tally board updates with animation. Running score: "Natural: [N] | Man-Made: [M]." A small suspense meter or "Prediction Check" indicator shows whether the tally currently matches or contradicts the child's prediction.
>
> **STUCK BRANCH** (if child cannot find something):
>
> **AI says**: "*(helpful, specific)* Look for ANYTHING around you! Is there a path or sidewalk under your feet? Man-made! What about the sky — any clouds? Natural! Even the ground counts — is it dirt or concrete? Look up, look down, look all around!"

> **Round 3 — Third Evidence (Final Piece):**
>
> *(Child photographs a final item — e.g., a puddle, a flower, a car, a sign, a stone wall)*
>
> **AI says**: "*(building to the climax)* Evidence number four — the LAST piece! Let me look very carefully at this photo... *(dramatic pause)* I see [description of visual cues]. I think this is... [NATURAL / MAN-MADE]! [Nature made this / A person built this]! This is the one that decides everything!"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah!" / "I knew it!" / "That changes everything!"
> 2. (Unexpected) "I don't know if that counts!" / "It's both!"
> 3. (No response) Child looks at the tally.
>
> **AI follow-up**:
> 1. "*(dramatic intake of breath)* [Natural/Man-Made]! Okay, Detective... I am adding it to the tally. Let me count everything up... are you ready for the BIG RESULT?"
> 2. "*(warm, thoughtful)* That is a great thought! Some things CAN be tricky — like a wooden bench uses natural wood but a person built it. But from the photo, I think overall this one is [natural/man-made]. Adding it to the tally. Are you READY for the final count?"
> 3. *(wait 2s)* "*(excited)* That is [natural/man-made]! Adding it to the board... the final tally is coming, Detective! Ready?"
>
> **Screen**: Final photo slides into slot 4 with a bigger celebration animation. All 4 photos now fill the tally board. A "CALCULATING..." animation plays briefly, building suspense before the reveal in Step 4.

**Step 4: Synthesis — The Magic Moment (Hypothesis Result Reveal)**

> **AI says**: "*(drumroll voice)* Okay Nature Detective — time for the BIG REVEAL! You predicted that most things around here would be... MOSTLY [NATURAL / MAN-MADE]! Let us count the evidence!"
>
> *(AI tallies aloud)*
>
> "The [first item] — [NATURAL/MAN-MADE]! The [find 1] — [NATURAL/MAN-MADE]! The [find 2] — [NATURAL/MAN-MADE]! The [find 3] — [NATURAL/MAN-MADE]!"
>
> **If prediction was RIGHT**:
> "*(triumphant fanfare voice)* The final count: Natural [N], Man-Made [M]! Your prediction was... RIGHT! You KNEW it! This place really IS mostly [natural / man-made]! Nature Detective, your instincts are incredible!"
>
> **If prediction was WRONG (the surprise)**:
> "*(gasping with delight)* The final count: Natural [N], Man-Made [M]! Your prediction was mostly [natural/man-made], but SURPRISE — this place TRICKED you! There are actually more [natural/man-made] things than you expected! That is what makes exploring so cool — sometimes the world surprises you!"
>
> **If it's a TIE (2 and 2)**:
> "*(amazed)* The final count: Natural 2, Man-Made 2! It is a PERFECT TIE! This place has an equal mix of nature things and people things. Nobody could have predicted that — what a discovery!"
>
> **Possible child responses**:
> 1. (Ideal) "I was right!" / "I was wrong!" / "I didn't know there were so many [natural/man-made] things!" / Cheers or laughs
> 2. (Unexpected) "I want to find more!" / "But I think that rock was man-made!"
> 3. (No response) Child looks at the tally screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That is what detectives DO — they guess, then check, and find out for real! You collected the evidence all by yourself. Now here is a cool thought — look at where you are standing right now. Is it natural ground or a man-made path? Nature and people-things are EVERYWHERE together!"
> 2. "*(enthusiastic)* You want MORE evidence? That is what real detectives say! The more you collect, the better your answer gets. But think about this — why do you think there are so many [natural/man-made] things HERE? What kind of place is this?"
> 3. *(wait 2s)* "*(warm prompt)* Look at all that data! You tested a real question with real evidence. Here is one more thing to think about — do you think a DIFFERENT place would have a different answer? Like your house, or a forest?"
>
> **Screen**: Full tally board with all 4 photos displayed in two columns (Natural vs Man-Made). The prediction banner at top lights up green (RIGHT!) or flashes orange with "SURPRISE!" text. Animated tally marks count up one by one with sound effects. A large final score displays: "Natural: [N] | Man-Made: [M]."

**Step 5: Discovery Celebration — The "Why" Reflection**

> **AI says**: "*(warm, wonder-filled)* You know what is really interesting? Nature and people-things are MIXED together almost everywhere! The tree is natural — it grew from a seed. But the bench NEXT to the tree is man-made — someone put it there so people could sit and enjoy the tree! And [example from child's finds]. People put their things right next to nature's things. They share the same space! Which one surprised you the most today — something natural or something man-made?"
>
> **Possible child responses**:
> 1. (Ideal) "The rock! I didn't think about where it came from!" / "The fence — I didn't know someone built it!" / "The puddle — it just appeared!"
> 2. (Unexpected) "I like nature more!" / "I want to go to a forest and check!"
> 3. (No response) Child looks at the collection.
>
> **AI follow-up**:
> 1. "*(delighted)* That one surprised you — and now you NOTICE it! That is what happens when you really look at things. You start seeing whether nature made it or people made it, and you wonder WHY it is here!"
> 2. "*(encouraging)* A forest — yes! A forest would probably be MOSTLY natural. But a city street would be mostly man-made! Every place has its own answer. You could be a Nature Detective EVERYWHERE you go!"
> 3. *(wait 2s)* "*(gentle)* Every thing around you has a story — nature grew it, or a person built it. Your survey helped you see that story! Now you will notice it everywhere."
>
> **Screen**: All 4 photos displayed with "Natural" or "Man-Made" labels. Animated connections show nature and man-made items coexisting: a tree next to a bench, a rock beside a path. The collection feels like a field survey poster.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud celebration)* Congratulations, Nature Detective! You did real detective work today! You looked closely at the Form of every thing — what it is made of, what it looks like, where it came from. And you discovered the Causation — WHO or WHAT made it! Nature grew the trees and rocks all by itself. People built the benches and fences on purpose. Every single thing has a maker — either nature or a person! You earned your Nature Detective Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to survey more places, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you go somewhere new, try the survey again! Predict first, then count. A park, a street, your backyard — every place has a different answer. See you on the next survey, Detective!"
> 2. "*(warm)* Your badge is saved! You are a real Nature Detective now. Bye for now, Detective!"
> 3. *(wait 2s)* "*(soft)* Your Detective Badge is glowing. Great survey today!"
>
> **Screen**: Golden "Nature Detective Badge" shaped like a magnifying glass with a split design — one half shows a leaf (natural) and the other half shows a gear (man-made). The first photo sits at center with collection photos as insets. "Form" in bold natural-green letters and "Causation" in warm amber arrow-shaped letters float artistically. The final tally result ("Natural: [N] | Man-Made: [M]") glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection. Each photo processed independently. Natural vs man-made classification is done through AI's visual assessment of photos — the distinction (tree/rock/cloud vs bench/sign/car) is among the most reliably identifiable visual properties. |
| 2 | Hook & Transition | PASS | Opens with emotional resonance ("Ooh, look at that bench! Someone BUILT this") and sensory wonder, not knowledge testing. Activity grows naturally from noticing the origin of one item to wondering about all nearby items. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 gives specific hints (look up at clouds, look down at ground, check the path). Step 2 handles uncertainty about what a "prediction" is. Round 3 handles the "both" edge case (wooden bench = natural material, man-made object). Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Form + Causation as Key Concepts — Form maps to material/origin observation, Causation maps to "who/what made this." KUD fully specified. 4 Related Concepts. 3 ATL skills with sub-skills. Closing names both Key Concepts naturally as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: Sentences 5-8 words in key prompts. Concrete vocabulary (natural, man-made, built, grew, tree, rock, bench, sign). 2-3 step tasks (predict, photograph, watch tally). AI announces assessment in simple language. |
| 6 | Dialogue Specificity | PASS | All AI lines are concrete dialogue with tone markers. Zero abstract instructions. Every response is actual words the AI says. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: tally board with two columns, photo slots, prediction banner, suspense animation, final score reveal, badge design. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — works for any entity outdoors. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise — child does not self-report, AI determines natural vs man-made from the photo. Uncertainty builds across 3 rounds. The result reveal is a real dramatic moment. High replayability — different locations (park, street, backyard, schoolyard) give very different results. |
| 10 | Pillar Fidelity | PASS | Discovery pillar: child predicts, commits, collects evidence, tally reveals result. The "Was I right?!" moment is the emotional climax. Core loop uses predict-commit-reveal-score mechanic (not generic Q&A). Could NOT be re-labeled as another pillar — the hypothesis and tally are definitional. A blind reader would identify this as Discovery immediately. |

**Overall**: ALL PASS — Ready for review
