## Activity: The Old vs New Survey

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Old vs New Survey |
| Activity Category | 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | **Form** (What is it like?) & **Change** (How is it changing?) |
| Related Concepts (Discipline) | Time, Transformation, Evidence, Pattern |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, metacognition), Communication Skills (expressing ideas) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |
| Trigger Entity | Any entity where AI detects visible age/wear |
| Trigger Scene | Child photographs any object where AI detects visible signs of age or newness — a rusty fence, a faded sign, a shiny new toy, a cracked sidewalk, a brand-new backpack |
| Mapping Source | property-bridge |
| IB Theme | How the World Works |
| Design Version | 1.0 |
| Last Updated | 2026-04-08 |
| Template Parameters | `{age_appearance}` — detected age/wear category (old-looking or new-looking). Old cues: rust, cracks, peeling, fading, moss, scratches. New cues: bright colors, clean surfaces, sharp edges, shine. Example: **old-looking** (worn bench trigger) |

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{age_appearance}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_1.appearance.tip_wear                             # e.g., crayons
  - tier_2.change.waterproof_coating_wear                  # e.g., raincoat
  - tier_2.change.fur_matting_over_time                    # e.g., plush_toys
  - tier_2.change.cracks_and_peeling_in_rubbery_materials  # e.g., raincoat
  - tier_2.change.squeak_wears_out                         # e.g., bath_toys
```

### B. Activity Overview

- **① Brief Description**: After photographing any object, the AI examines the photo and detects visible signs of age or newness — for example, worn wood, faded paint, and scratches on an old bench. The AI marvels at the evidence of time and wonders — are MOST things around here old-looking or new-looking? The child becomes a "Time Detective" who first PREDICTS, then collects evidence by photographing 3 more items. The AI is the property assessor: it examines each photo for visual age cues and announces its verdict. At the end, the AI tallies results and reveals whether the child's prediction was right or surprising. Insight: "Old things have STORIES — every scratch is an adventure they had! New things are just starting their adventures!"

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "old-looking," "new-looking," "faded," "worn," "rusty," "cracked," "shiny," "bright," "scratched," "smooth." Learn that you can tell how long something has been around by looking at its surface.
  - **U (Understand)**: Things have a **Form** that includes visible signs of age — rust, fading, cracks, moss are clues about duration. Things **Change** over time — surfaces fade, paint peels, metal rusts. The way something looks NOW tells a story about its past.
  - **D (Do)**: Make a prediction and commit to it before collecting data; photograph items for AI to assess visually as old-looking or new-looking; watch the tally build; compare results to a hypothesis.

- **③ Design Highlight**: The "Time Detective" metaphor turns any environment into a time-travel investigation. The AI is the property assessor — it examines each photo for visual age cues (rust, cracks, faded colors, peeling paint, moss vs. bright colors, sharp edges, clean surfaces) and announces its verdict. These cues are among the most reliably identifiable properties in photos. The "Old things have STORIES" insight adds emotional depth beyond the tally result.

- **④ Typical Scenario**: Child photographs an old wooden bench --> AI notices worn surface, faded paint, scratches --> "Your bench has been here a LONG time!" --> proposes hypothesis --> child predicts --> photographs 3 more items --> AI assesses each --> tally reveals result.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1b: Transition Bridge -- Cold Start

**Context**: Child photographs any object with visible age/wear cues (e.g., an old wooden bench with faded paint and scratches). AI detects age/wear signs.

**AI says**: *(delighted, curious tone)* "Ooh, look at that bench! See those scratches all over it? And the paint is all faded — it used to be brighter, but the sun and rain made it pale! And look — the edges are all smooth and worn, like LOTS of people have sat on it. This bench has been here a LONG time! But wait... are MOST things around here old-looking like this bench? Or are most things new-looking — bright and shiny and clean? What do you think?"

**Possible child responses**:
1. (Ideal) "Old!" / "New!" / "I see some old stuff!" / "That sign looks new!"
2. (Unexpected) "I like the bench!" / "What does old-looking mean?" / "I don't know."
3. (No response) Child looks around at the environment.

**AI follow-up**:
1. *(intrigued)* "Interesting — you already have ideas! This bench is definitely old-looking — all that faded paint and those scratches. But I wonder about the OTHER things. I think we should find out for REAL!"
2. *(warm, explaining)* "Old-looking means it has clues that it has been here a while — scratches, faded colors, cracks, or rust. New-looking means bright, shiny, clean, smooth — like it was JUST made! I have a fun idea to figure out what this place is mostly like!"
3. *(wait 2s)* *(inviting)* "This bench has scratches and faded paint — old-looking! But are ALL the things here old-looking? Or are some shiny and new? Let us find out!"

**Screen**: Photo centered with subtle aging highlight effect — scratches and faded areas gently glow. "OLD-LOOKING" label with clock icon near the worn surface.

#### Step 2: Mission Briefing -- Hypothesis + Setup

**AI says**: *(excited scientist tone)* "Okay, Time Detective — here is my big question! Out of ALL the things around here, do you think MOST of them are OLD-LOOKING — scratched, faded, worn, rusty, cracked? Or do you think MOST of them are NEW-LOOKING — bright, shiny, clean, smooth? This is your PREDICTION. What do you think — mostly old-looking, or mostly new-looking?"

**Possible child responses**:
1. (Ideal -- picks old) "Old-looking!" / "I think old!" / "Everything looks worn!"
2. (Ideal -- picks new) "New-looking!" / "I think shiny!" / "Most stuff is new!"
3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"

**AI follow-up**:
1. *(locking it in)* "You predict MOSTLY OLD-LOOKING — got it! I am writing that down. You are a Time Detective! Your job: find 3 more things, take a photo of each, and I will look closely for clues — scratches, rust, fading for old, or bright colors, clean surfaces for new. I will keep count. At the end, we see if your prediction was RIGHT. Ready, Detective?"
2. *(locking it in)* "You predict MOSTLY NEW-LOOKING — interesting! I am writing that down. You are a Time Detective! Find 3 more things, snap photos, and I will check for age clues. Ready, Detective?"
3. *(encouraging)* "A prediction is your BEST GUESS before you check! Do you think MOST things here are old-looking — scratched and faded — or new-looking — bright and clean? Just pick one!"

**Screen**: Detective-themed mission card with "Time Detective" badge — magnifying glass with clock face. Tally board with two columns: "Old-Looking" (cracked-clock icon) and "New-Looking" (sparkle icon). Bench photo under "Old-Looking" with "1" tally. Prediction stamped at top: "My prediction: Mostly [Old-Looking / New-Looking]!" Three empty photo slots below.

#### Step 3: Multi-Round Exploration (3 rounds)

**Round 1 -- First Evidence:**

*(Child photographs something — e.g., a shiny new street sign)*

**AI says**: *(eager scientist voice)* "Evidence number two! Let me look closely... *(examining)* Bright paint — no fading! Sharp, clean edges. Smooth surface — no scratches, no rust, no cracks. This sign looks like it was put here RECENTLY! That is NEW-LOOKING!"

**Possible child responses**:
1. (Ideal) "Yeah, it IS new!" / "The colors are so bright!" / "I thought it would be old!"
2. (Unexpected) "I like the sign!" / "It says STOP!"
3. (No response)

**AI follow-up**:
1. *(writing it down excitedly)* "Tally so far: Old-Looking 1, New-Looking 1. It is a TIE! Your prediction says mostly [old/new]-looking... two more to find, Detective!"
2. *(playful)* "It does say stop — and those bright letters are SO clean and sharp! Definitely new-looking. Tally: Old-Looking 1, New-Looking 1. Two more, Detective!"
3. *(wait 2s)* "Bright colors and sharp edges — new-looking! The tally is tied! Two more to go!"

**Screen**: Photo slides into slot 2. Tally board updates with animation. Running score: "Old-Looking: 1 | New-Looking: 1." Prediction banner stays visible.

**Rounds 2-3**: Same structure. Round 2 builds suspense ("Evidence number three! Let me examine this one..."). Round 3 climaxes ("Evidence number four — the LAST piece!").

**Round 3 edge cases**:

- **STUCK BRANCH**: "Look for clues of TIME! Is there a fence or railing nearby — check for rust! Look at the ground — any cracks? Check the buildings — is the paint peeling or bright? Even a tree trunk — scratches and bumps mean old!"
- **"KIND OF BOTH" EDGE CASE** (e.g., a new bench with old stickers): "Some things CAN be tricky — like a new bench with old stickers on it. But from the photo, the biggest clues point to [old-looking / new-looking] — I see [specific visual evidence]."

**Screen at final evidence**: All 4 slots filled. "CALCULATING..." animation builds suspense.

#### Step 4: Synthesis -- The Magic Moment (Hypothesis Result Reveal)

**AI says**: *(drumroll voice)* "Okay Time Detective — time for the BIG REVEAL! You predicted that most things around here would be... MOSTLY [OLD-LOOKING / NEW-LOOKING]! Let us count the evidence!"

*(AI tallies aloud)*

"The bench — OLD-LOOKING! The [find 1] — [old/new]-looking! The [find 2] — [old/new]-looking! The [find 3] — [old/new]-looking!"

**If prediction was RIGHT**:
*(triumphant fanfare voice)* "The final count: Old-Looking [N], New-Looking [M]! Your prediction was... RIGHT! You KNEW it! Most things here really ARE [old/new]-looking! Time Detective, your instincts are amazing!"

**If prediction was WRONG (the surprise)**:
*(gasping with delight)* "The final count: Old-Looking [N], New-Looking [M]! Your prediction was mostly [old/new]-looking, but SURPRISE — this place TRICKED you! More things are actually [old/new]-looking than you expected! That is what makes exploring so cool — sometimes the world surprises you!"

**If it's a TIE (2 and 2)**:
*(amazed)* "The final count: Old-Looking 2, New-Looking 2! It is a PERFECT TIE! This place has a mix of things that have been here a LONG time AND things that are brand new! What a discovery!"

**AI follow-up**:
1. *(celebrating)* "That is what detectives DO — they guess, then check, and find out for real! Now here is a cool thought — old things have STORIES! Every scratch, every crack, every bit of rust is a clue about something that happened. The wind, the rain, people touching it — all those things left their mark!"
2. *(enthusiastic)* "You want MORE evidence? Every new thing you check gives you a better answer. But think about this — WHY do some things look old faster than others?"
3. *(wait 2s)* "Every scratch and crack is like a DIARY. The old things have been writing their stories on their surfaces for years!"

**Screen**: Full tally board with all 4 photos in two columns. Prediction banner lights up green (RIGHT!) or flashes orange (SURPRISE!). Tally marks count up one by one. Final score: "Old-Looking: [N] | New-Looking: [M]."

#### Step 5: Discovery Celebration -- The "Why" Reflection

**AI says**: *(warm, wonder-filled)* "You know what is really amazing? Old things have STORIES — every scratch is an adventure they had! Every crack is a chapter. Every bit of rust is a memory. That bench? All those scratches came from years and years of people sitting on it — kids like you! And new things? They are just starting their adventures! That shiny [new item]? Its story is just beginning — it has no scratches YET! Which one surprised you the most?"

**AI follow-up**:
1. *(delighted)* "That one surprised you — and now you KNOW how to spot it! Moss, rust, cracks, faded colors — they are all clues about time. You can read the stories on things!"
2. *(encouraging)* "Your house — yes! I bet it has BOTH old-looking AND new-looking things. The doorknobs might be scratched from thousands of turns. But the fridge might still be shiny!"
3. *(wait 2s)* "Every thing around you has a time story — rust, cracks, and fading tell you it has been here a while. Bright colors tell you it is newer. Now you notice it everywhere!"

**Screen**: All 4 photos with "Old-Looking" or "New-Looking" labels. Timeline arrows connect to "time story" bubbles: "scratches from years of use," "bright paint = just installed," "moss grows slowly." Collection feels like a time-travel field poster.

#### Step 6: Closing + IB Concepts

**AI says**: *(proud celebration)* "Congratulations, Time Detective! You did real detective work today! You looked closely at the **Form** of every thing — the scratches, the rust, the cracks, the bright paint, the clean surfaces. All those visual clues told you a story! And you discovered **Change** — things do not stay the same forever! Paint fades in the sun. Metal rusts in the rain. Surfaces get scratched from use. Everything is SLOWLY changing, all the time — and now you can SEE it! You earned your Time Detective Badge!"

**AI follow-up**:
1. *(encouraging)* "Next time you go somewhere new, try the survey again! A brand-new mall would be VERY different from an old park! See you on the next survey, Detective!"
2. *(warm)* "Your badge is saved! You are a real Time Detective now. Bye for now, Detective!"
3. *(wait 2s)* *(soft)* "Your Time Detective Badge is glowing. Great survey today!"

**Screen**: Golden "Time Detective Badge" — magnifying glass with clock face inside. Bench photo at center with collection photos as insets. **"Form"** in crystalline letters with texture swatches and **"Change"** in arrow-shaped letters showing transformation motif (bright fading, sharp rounding, clean gaining scratches). Final tally glows beneath.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. Age/wear assessed from visual cues in each photo — rust, cracks, fading, moss vs. bright colors, clean surfaces, sharp edges. |
| 2 | Hook & Transition | PASS | Opens with emotional wonder about visible age cues, not knowledge testing. Activity grows naturally from detected attribute. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Stuck branch, "kind of both" edge case, and silence branches included. |
| 4 | IB Completeness | PASS | KUD defined. Form + Change as Key Concepts. Change (not Causation) because the game is about temporal transformation. Closing names concepts as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: short sentences, concrete vocabulary (scratched, faded, rusty, shiny, bright), achievable 3-item survey for ages 4-6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers and specific visual observations. Zero "AI guides" placeholders. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with animations and visual elements. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — trigger is any entity with visible age/wear, not a specific entity. |
| 9 | Game Feel | PASS | Genuine stakes from committed prediction. AI-as-assessor preserves surprise using specific visual evidence. "Old things have STORIES" insight adds emotional depth. High replayability — different locations give different results. |
| 10 | Pillar Fidelity | PASS | Discovery pillar: predict, commit, collect evidence, tally reveals result. "Was I right?!" is the emotional climax. Hypothesis and tally are definitional. |

**Overall**: ALL PASS — property-bridge field_experiment template triggered by visible age/wear. AI assesses age appearance from visual cues — rust, cracks, fading, moss vs. bright colors, clean surfaces, sharp edges.
