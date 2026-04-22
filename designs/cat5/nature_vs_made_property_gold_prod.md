## The Nature vs Made Survey

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Nature vs Made Survey |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | Origin, Design, Classification, Pattern |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, analysis), Communication Skills (expressing) |
| Game Style | field_experiment |
| Design Version | 1.0 |
| Last Updated | 2026-04-21 |

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

**① Brief Description**

After photographing any outdoor object, the AI identifies whether it is natural (made by nature) or man-made (made by people) and wonders — are MOST things around here natural or man-made? The child becomes a "Nature Detective" who first PREDICTS whether most nearby things are natural or man-made, then collects evidence by photographing 3 more items. The AI ASSESSES each photo (natural vs man-made is highly reliably identifiable visually). At the end, the AI tallies the data and reveals whether the child's prediction was right or surprising.

**② Educational Purpose (KUD)**

- **K (Know):** "Natural" means made by nature (trees, rocks, water, flowers, animals); "man-made" means built by people (benches, fences, signs, cars, buildings); some things combine both (a wooden bench uses natural wood shaped by people)
- **U (Understand):** Things around us have different origins — some made by nature, some made by people — that is Form (what they are made of); the reason something is natural or man-made tells us about Causation (who/what created it and why)
- **D (Do):** Make a prediction and commit before collecting data; photograph items for AI to assess visually as natural or man-made; compare final results to a hypothesis

**③ Design Highlight**

The child commits to a hypothesis BEFORE exploring — creating genuine stakes. Each find adds a tally mark to "Natural" or "Man-Made," building suspense. The AI is the property assessor — it examines each photo and announces its verdict, so the child does not self-report. The magic moment is the final count reveal against the prediction. Works universally outdoors — parks, streets, backyards, schoolyards all produce different results.

**④ Typical Scenario**

A child in a park photographs a wooden bench, AI notices it is man-made, proposes a hypothesis about whether most things around here are natural or man-made, child commits to a prediction, then photographs 3 more items (a tree, a rock, a lamppost), AI assesses each from the photo, and the AI tallies the final score against the prediction.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** (delighted, curious) "Ooh, look at that bench! Someone BUILT this — they took wood, cut it into pieces, and put it all together so people could sit here. That is MAN-MADE — a person made it! But wait... I see trees and rocks and grass too. Those are NATURAL — nobody made those, they just grew! I have a BIG question. Are most things around here natural, or man-made? What do you think?"

**Child responses:**

1. (Ideal) "Natural!" / "Man-made!" / "I see more trees!"
2. (Unexpected) "I like the bench!" / "What does man-made mean?"
3. (No response) Child looks around at the environment.

**AI follow-up:**

1. (intrigued) "Interesting — you already have ideas! The bench is definitely man-made. But all those trees and rocks? Nature made those all by itself! I think we should find out what MOST things around here really are!"
2. (warm, explaining) "Great question! Man-made means a person BUILT it — like this bench! Natural means nature made it all by itself — like a tree growing from a seed. Nobody built the tree — it just grew! I have a fun idea to figure out what this place is mostly made of!"
3. (wait 2s) (inviting) "This bench is man-made — a person built it! But see those trees? Nobody built those — they grew by themselves! That is natural. I wonder which kind there is MORE of around here. Want to find out?"

**Screen:** Photo centered with "MAN-MADE" or "NATURAL" label and appropriate icon (hammer or leaf).


#### Step 2: Rule Introduction + Demo

**AI says:** (excited scientist) "Okay, Nature Detective — here is my big question! Out of ALL the things around here, do you think MOST of them are NATURAL — made by nature, like trees and rocks? Or MOST of them are MAN-MADE — built by people, like benches and signs? This is your PREDICTION. What do you think — mostly natural, or mostly man-made?"

**Child responses:**

1. (Ideal — picks natural) "Natural!" / "I think more nature!"
2. (Ideal — picks man-made) "Man-made!" / "I see lots of buildings!"
3. (Uncertain) "I don't know!" / "Maybe both?" / "What's a prediction?"

**AI follow-up:**

1. (locking it in) "You predict MOSTLY NATURAL — got it! I am writing that down. You are a Nature Detective! Find 3 more things, take a photo of each, and I will tell you if it is natural or man-made. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
2. (locking it in) "You predict MOSTLY MAN-MADE — interesting! I am writing that down. You are a Nature Detective! Find 3 more things, take a photo of each, and I will tell you if it is natural or man-made. At the end, we will see if your prediction was RIGHT. Ready, Detective?"
3. (encouraging) "A prediction is your BEST GUESS before you check! Do you think MOST things here are natural — like trees and rocks — or man-made — like benches and signs? Just pick one!"

**Screen:** "Nature Detective" badge with magnifying glass (leaf/gear split). Tally board with "Natural" and "Man-Made" columns. First photo placed in correct column with "1" tally. Prediction stamped at top. Three empty slots below.


#### Step 3: Multi-Round Interaction

**Round 1:**

*(Child photographs something — e.g., a tree)*

**AI says:** (eager scientist) "Evidence number two! Let me look at this photo closely... I see a big trunk, branches spreading out, green leaves all over. That is a TREE! Did anyone build this? Nope — it grew from a tiny seed all by itself. That is NATURAL!"

**Child responses:**

1. (Ideal) "Yeah, trees are natural!" / "Nobody built a tree!"
2. (Unexpected) "I like climbing it!" / "It's really big!"
3. (No response) Looks at the tally.

**AI follow-up:**

1. (excited) "The tally so far: Natural [N], Man-Made [M]. [Natural is winning! / They are tied! / Man-Made is still ahead!] Two more to find, Detective!"
2. (playful) "It IS big — nature made it grow tall! And that big tree is definitely NATURAL. Tally update: Natural [N], Man-Made [M]. Two more, Detective!"
3. (wait 2s) (announcing) "That tree is NATURAL! Tally: Natural [N], Man-Made [M]! Two more to go — find another thing and take a photo!"

**Screen:** Photo slides into slot 2, tally updates with animation. Running score: "Natural: [N] | Man-Made: [M]." Prediction banner stays visible.

**Round 2 — "The Second Find":** Child photographs another item; AI examines visual cues in the photo (texture, shape, material, color) and announces whether it is natural or man-made. Tally updates. One more to find.

**Round 3 — "The Final Piece":** Child photographs last item; AI examines photo with dramatic buildup, announces verdict. "CALCULATING..." animation plays. Includes stuck branch — AI suggests looking up (clouds = natural), looking down (path = man-made or dirt = natural), or checking nearby objects.


#### Step 4: Celebration

**AI says:** (drumroll voice) "Okay Nature Detective — time for the BIG REVEAL! You predicted that most things around here would be... MOSTLY [NATURAL / MAN-MADE]! Let us count the evidence!"

*(AI tallies aloud — each item and its classification)*

**If prediction was RIGHT:**
(triumphant) "The final count: Natural [N], Man-Made [M]! Your prediction was... RIGHT! You KNEW it! This place really IS mostly [natural/man-made]! Nature Detective, your instincts are incredible!"

**If prediction was WRONG:**
(gasping with delight) "The final count: Natural [N], Man-Made [M]! SURPRISE — this place TRICKED you! There are actually more [natural/man-made] things than you expected! That is what makes exploring so cool — sometimes the world surprises you!"

**If it's a TIE:**
(amazed) "The final count: Natural 2, Man-Made 2! A PERFECT TIE! This place has an equal mix of nature things and people things. What a discovery!"

**AI follow-up:**

(celebrating) "That is what detectives DO — they guess, then check, and find out for real! Now here is a cool thought — do you think a DIFFERENT place would have a different answer? Like a forest, or a city street?"

**AI says:** (warm, wonder-filled) "You know what is really interesting? Nature and people-things are MIXED together almost everywhere! The tree is natural — it grew from a seed. But the bench NEXT to the tree is man-made — someone put it there so people could sit and enjoy the tree! They share the same space! Which one surprised you the most today?"

**Child responses:**

1. (Ideal) "The rock!" / "The fence — I didn't know someone built it!"
2. (Unexpected) "I like nature more!" / "I want to go to a forest and check!"

**AI follow-up:**

1. (delighted) "That one surprised you — and now you NOTICE it! You start seeing whether nature made it or people made it, and you wonder WHY it is here!"
2. (encouraging) "A forest would probably be MOSTLY natural. But a city street would be mostly man-made! Every place has its own answer. You could be a Nature Detective EVERYWHERE you go!"

**Screen:** All 4 photos in two columns (Natural vs Man-Made). Prediction banner lights up green (RIGHT!) or flashes orange (SURPRISE!). Animated tally marks count up. Final score: "Natural: [N] | Man-Made: [M]." Golden star on favorite item.


#### Step 5: Closing + IB Concepts

**AI says:** (proud, warm celebration) "Congratulations, Nature Detective! You did real detective work today! You looked closely at the Form of every thing — what it is made of, what it looks like, where it came from. And you discovered the Causation — WHO or WHAT made it! Nature grew the trees and rocks all by itself. People built the benches and fences on purpose. Every single thing has a maker — either nature or a person! You earned your Nature Detective Badge!"

**Screen:** Golden "Nature Detective Badge" — magnifying glass with leaf/gear split design. "Form" in natural-green letters and "Causation" in warm amber arrow-shaped letters. Four collection photos as insets. Final tally result glows beneath.
