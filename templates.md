# Activity Category Templates

> These templates define the **structural skeleton** for each activity category.
> The agent uses these as scaffolding — filling entity-specific content into the slots.
> This ensures consistency across activities within the same category while allowing creative variation in the entity-specific parts.
>
> **Structure**: 2 base templates (Cat1 + Cat5) × 6 Experience Pillar overlays = coverage for all 12 game styles. Each base template provides the step skeleton; each pillar overlay specifies the game mechanic, payoff, and creative variables that make the pillar distinctive.

---

## How Templates Work

Each template defines:
- **Fixed structure**: Step sequence, step purposes, UI patterns — these are CONSTANT across all entities within a category
- **Variable slots**: Marked with `{curly braces}` — these are entity-specific and must be invented fresh each time
- **Creative variables**: Universal variables (metaphor, role) + pillar-specific variables — these are where originality lives
- **Pillar overlays**: Each of the 6 Experience Pillars (Mystery, Creation, Performance, Discovery, Adventure, Nurture) provides specific guidance for Steps 2–4, which is where the pillar's identity is expressed

The agent should:
1. Read the **base template** for the assigned category (Template A for Cat1, Template B for Cat5)
2. Read the **pillar overlay** for the assigned experience pillar (within the base template)
3. Fill ALL `{variable}` slots with entity-specific content
4. Expand each step to full detail (dialogue, 3 response branches, screen descriptions) per program.md format
5. Ensure creative variables (universal + pillar-specific) are genuinely fresh — not recycled from exemplars

---

## Template A: Category 1 — Sustained Verbal Interaction (In-Device)

### Structural Constants

| Property | Value |
|---|---|
| Device relation | In-Device (no physical movement after initial photo) |
| Setting | Indoor, quiet environment |
| Step count | 5 |
| Round count | 3–5 in the core loop step |
| Camera use | Initial photo only — no additional photos required |
| Core mechanic | AI presents pillar-specific scenarios → child responds verbally → AI validates with pillar-specific game elements (reveals, scores, transformations, etc.) |

### Step Skeleton

```
STEP 1: Transition Bridge
  Purpose: Emotional hook. React to the photographed {entity} with delight.
           Ask an EMOTIONAL or IMAGINATIVE question (never knowledge-testing).
  Pattern: "Wow, {entity}! {emotional observation}. {imaginative question}?"
  Screen:  {entity} photo centered, with {ambient animation}.

  Note: Mapping-informed designs also include a warm start variant (Step 1a)
  per conversation_bridge.md.

STEP 2: Game Setup + Demo
  Purpose: Establish the PILLAR-SPECIFIC game mechanic through a quick DEMONSTRATION.
           AI models the expected behavior first, then invites child.
  Pattern: "Here's how it works: I'll {pillar_mechanic}. For example... {AI demos}.
            Got it? Let's go!"
  Screen:  Icons representing the game mechanic appear alongside {entity} photo.

  PILLAR-SPECIFIC SETUP:
    Mystery:     "I'm going to think of something hidden in your photo. I'll give you clues..."
    Creation:    "We're going to imagine wild changes to your {entity}. What if it had..."
    Performance: "Your {entity} is going on stage! I'll be the audience..."
    Discovery:   "I'll describe something that might happen. You guess what {entity} does..."
    Adventure:   "We're going to travel through time with your {entity}..."
    Nurture:     "Your {entity} needs help! I'll tell you what's wrong, you fix it..."

STEP 3: Core Loop (3–5 rounds)
  Purpose: Core gameplay. Each round uses the PILLAR-SPECIFIC mechanic.
           Rounds ESCALATE in complexity.
  Pattern per round:
    AI: "{pillar_prompt}. {specific question}?"
    Child responses: ideal / unexpected / silence — each with specific AI follow-up
    AI follow-up always: validates → extends → transitions to next
  Screen: Visual changes per round.

  PILLAR-SPECIFIC CORE LOOP:
    Mystery:     AI gives clue → child guesses → AI confirms/redirects with "warmer/colder"
    Creation:    AI asks "what if {modification}?" → child invents → AI elaborates and adds to creation
    Performance: AI sets challenge → child performs → AI reacts AS audience (cheers, gasps, laughter)
    Discovery:   AI describes scenario → child COMMITS prediction → AI reveals with drama + scores
    Adventure:   AI describes time period → child imagines → AI offers CHOICE POINT → child decides path
    Nurture:     AI describes need → child proposes solution → AI narrates VISIBLE TRANSFORMATION

  ESCALATION GUIDE:
    Round 1: Simple, obvious, high-success — build confidence
    Round 2: More complex — introduce a contrasting element
    Round 3: Surprising or funny — peak engagement
    Round 4–5 (if engaged): Open-ended — child leads

STEP 4: Payoff — The Magic Moment
  Purpose: The emotional climax specific to this pillar. This is what makes the
           game FEEL like this pillar and not another.

  PILLAR-SPECIFIC PAYOFF:
    Mystery:     Final reveal + "You figured it out!" celebration
    Creation:    "Super {entity}" unveiled with ALL modifications combined — the "ta-da!"
    Performance: Standing ovation — audience goes wild, encore request
    Discovery:   Final score tallied — "You got N out of M!" + surprise bonus
    Adventure:   Timeline/journey map assembled showing all stops — "Look how far we traveled!"
    Nurture:     Entity fully recovered, calls child by name, expresses deep gratitude

  Screen: Pillar-specific celebration animation.

STEP 5: Celebration + IB Concepts
  Purpose: Award role title + naturally name Key Concepts as praise.
  Pattern: "You just became a {role_title}! {concept_connection}. That's the magic of {Key_Concept}!"
  Screen: Badge/trophy animation with Key Concept words styled artistically.
```

### Creative Variables (MUST be unique per entity)

#### Universal Variables (all pillars)

| Variable | Description |
|---|---|
| `{metaphor}` | The imaginative frame that transforms education into play |
| `{role_title}` | Badge/title the child earns |
| `{escalation_axis}` | How rounds get progressively richer |

#### Pillar-Specific Variables

| Pillar | Variables | Description |
|---|---|---|
| Mystery | `{hidden_details}`, `{clue_types}`, `{reveal_drama}` | What's hidden in the photo, how clues are given (visual, textural, functional), how reveals happen (dramatic pause, zoom-in, sparkle) |
| Creation | `{modifications}`, `{combination_name}`, `{absurdity_escalation}` | What-if changes proposed each round, name of the final combined creation, how wild the modifications get |
| Performance | `{challenges}`, `{audience_character}`, `{twist_challenge}` | What the child performs each round, who reacts and how (judges, fans, animals), the surprise twist that changes the rules |
| Discovery | `{scenarios}`, `{scoring_system}`, `{reveal_drama}` | Cause-effect scenarios per round, how points are tracked and awarded, how each reveal is dramatized |
| Adventure | `{time_periods}`, `{choice_points}`, `{timeline_visualization}` | Journey stops (past, present, future), where the story branches based on child's choice, how the timeline is displayed at the end |
| Nurture | `{needs_escalation}`, `{transformation_arc}`, `{relationship_deepening}` | Need progression (physical → emotional → complex), how entity visibly improves per solution, how gratitude grows (by round 3, entity calls child by name) |

### Dimension Anchoring (mapping-informed designs)

Before brainstorming creative variables, select 2–3 **anchor dimensions** from the entity mapping that will supply the activity's core content (see entity_guidance.md §6).

**For Category 1 — Engagement-First anchoring:**

| Anchor Priority | Dimension Type | Purpose in Activity |
|----------------|----------------|---------------------|
| Primary anchor | emotions, imagination, narrative, or reasoning | Drives the game mechanic — what the child explores each round |
| Secondary anchor | relationship or another engagement dimension | Provides variety across rounds — comparison, storytelling, cause-effect |
| Physical ground | appearance, senses, or function | Gives the verbal game concrete, observable hooks from the real entity |

**How anchors shape creative variables:**
- `{metaphor}` should exercise the primary anchor dimension
- Pillar-specific round content should draw from primary + secondary anchors
- `{escalation_axis}` maps to the engagement skill in the anchor dimensions
- AI dialogue vocabulary comes from the physical ground dimension's `value` fields

### Entity Adaptation Checklist

When adapting to a new entity, verify:
- [ ] The pillar's magic moment is clearly present in Step 4
- [ ] The game element creates genuine stakes (uncertainty, surprise, or challenge)
- [ ] A blind reader could identify which pillar this design belongs to
- [ ] The pillar's specific game mechanic drives Step 3 (not generic Q&A)
- [ ] The metaphor makes sense for THIS entity (not forced/generic)
- [ ] The scenario types are plausible for THIS entity's real-world context
- [ ] The role title is specific to what the child actually DOES (not generic "explorer")
- [ ] Round escalation uses a dimension natural to THIS entity
- [ ] Screen visuals reference THIS entity's actual appearance/features
- [ ] Closing IB concepts are EARNED by what the child did, not pre-assigned
- [ ] (Mapping-informed) Anchor dimensions are identified and drive the creative variables
- [ ] (Mapping-informed) Vocabulary/facts in AI dialogue are traceable to mapping attributes

---

## Template B: Category 5 — Collection/Tracking Exploration (Out-of-Device)

### Structural Constants

| Property | Value |
|---|---|
| Device relation | Out-of-Device (child physically moves and explores) |
| Setting | Outdoor — park, yard, playground, nature |
| Step count | 5–6 |
| Round count | 3–4 photo-taking rounds in the exploration step |
| Camera use | Initial photo + 2–3 additional photos during collection |
| Core mechanic | AI identifies a VISUAL FEATURE → frames a pillar-specific COLLECTION MISSION around it → child explores and photographs finds → AI reacts with pillar-specific per-find interaction → child SYNTHESIZES the collection using pillar-specific mechanic |

### Step Skeleton

```
STEP 1: Transition Bridge
  Purpose: Emotional hook. React to the {entity}'s most STRIKING VISUAL FEATURE.
           Frame that feature with wonder, then ask what it reminds the child of.
  Pattern: "Look at {specific_visual_feature} on this {entity}! It's like {imaginative_comparison}.
            What does it remind YOU of?"
  Screen:  {entity} photo with {visual_feature} area subtly highlighted (soft glow/circle).

  Note: Mapping-informed designs also include a warm start variant (Step 1a)
  per conversation_bridge.md.

STEP 2: Mission Briefing
  Purpose: Transform into a COLLECTION MISSION with pillar-specific framing.
           Give 3 concrete sub-tasks.
  Pattern: "You are now a {role_title}! Your mission: {pillar_mission}."

  PILLAR-SPECIFIC MISSIONS:
    Mystery:     "Find things that match my riddle-clues!"
    Creation:    "Collect ingredients — each one has a superpower!"
    Performance: "Assemble your cast for the big show!"
    Discovery:   "Gather evidence to test our hypothesis!" (hypothesis MUST use visually-verifiable properties — see constraints below)
    Adventure:   "Find items that match your quest criterion!"
    Nurture:     "Find things that need your help!"

  Screen: Mission card with {role_title} badge, {N+1} empty slots (first filled with initial photo),
          and numbered task list with icons.

STEP 3: Multi-Round Exploration (3–4 rounds)
  Purpose: Child physically explores, finds items, photographs them.
           AI reacts to each find with PILLAR-SPECIFIC interaction.

  PILLAR-SPECIFIC PER-FIND INTERACTION:
    Mystery:     AI gives riddle-clue → child searches → AI confirms match or redirects
    Creation:    Child finds item → AI identifies its "superpower" (sticky, bouncy, etc.)
    Performance: Child finds item → AI asks "What sound would it make?" → child assigns voice
    Discovery:   Child photographs item → AI ASSESSES the hypothesis-relevant property from the photo → announces result → tallies (child does NOT self-report; AI is the assessor to preserve "Was I right?!" surprise)
    Adventure:   Child finds item → AI evaluates against quest criterion → harvests detail for naming
    Nurture:     Child finds item → AI identifies its "need" → child proposes care solution

  Per-find pattern:
    (Child takes a photo)
    AI: "{excited reaction}! {pillar-specific interaction question}?"
    Child responses: describes it / says nothing / item doesn't clearly match
    AI follow-up:
      - Match: "{validate + pillar-specific extension}. {N} more to go!"
      - No match: "{find something positive anyway}. That could count as {stretch}. {N} more to go!"
      - Silent: "I see {AI describes what it sees}! {pillar-specific prompt}?"
    Screen: New photo slides into next slot. Counter updates. Brief celebration animation.

  STUCK BRANCH (if child can't find something):
    AI: "{helpful, specific hint about WHERE to look for {collection_criterion}}.
         Try {concrete location suggestion}!"
    This is CRITICAL — never leave the child without a concrete next action.

STEP 4: Synthesis — The Magic Moment
  Purpose: Pillar-specific synthesis of the collection. This is the Cat5 equivalent
           of the payoff — the emotional climax.

  PILLAR-SPECIFIC SYNTHESIS:
    Mystery:     AI reveals the HIDDEN PATTERN connecting all finds
    Creation:    Child combines superpowers into an imaginary invention
    Performance: AI narrates the ensemble concert — each item performs, then all together
    Discovery:   AI tallies data against hypothesis — "Your prediction was RIGHT/SURPRISING!"
    Adventure:   Child co-creates quest story with detail-driven character roles
    Nurture:     Rescued items help EACH OTHER — mutual aid synthesis

  Pattern: "Your collection is complete! Now, {pillar_synthesis_prompt}?"
  Screen:  All photos displayed together (grid or lineup). Pillar-specific visualization
           (connections, scores, story flow, transformation arcs).

STEP 5: Discovery Celebration
  Purpose: Celebrate the collection AND the pattern/connection found.
  Pattern: "You found {N} things that {shared discovery}! Why do you think {reflective_question}?"
  Screen:  Collection displayed as a cohesive set. Animated connections between items.

STEP 6: Closing + IB Concepts
  Purpose: Name Key Concepts as praise.
  Pattern: "You discovered the {Key_Concept_1} of {feature} — {explanation}.
            And you found {Key_Concept_2} between {entity} and {other finds}.
            You earned your {badge_name}!"
  Screen:  Badge animation with collection photos as insets.
           Key Concept words styled artistically with entity-relevant imagery.
```

### Creative Variables (MUST be unique per entity)

#### Universal Variables (all pillars)

| Variable | Description |
|---|---|
| `{visual_feature}` | The specific observable feature that anchors the mission |
| `{collection_criterion}` | What the child looks for |
| `{metaphor}` | The frame that makes collecting meaningful |
| `{role_title}` | The child's mission role |
| `{stuck_hint}` | Where to look if child can't find items |
| `{reflective_question}` | The "why" question at the end |

#### Pillar-Specific Variables (Cat5)

| Pillar | Variables | Description |
|---|---|---|
| Mystery | `{riddle_clues}`, `{pattern_connection}`, `{reveal_narrative}` | Clues per find (texture, shape, function riddles), what connects all finds (the hidden pattern), how the reveal happens (dramatic unveiling) |
| Creation | `{superpowers_per_item}`, `{combination_prompt}`, `{invention_name}` | Property AI assigns per find (sticky, bouncy, smooth), how to combine them, what the invention is called |
| Performance | `{sound_per_item}`, `{ensemble_narrative}`, `{conductor_moments}` | Voice/sound child assigns per find, concert script (solos then ensemble), directing moments ("All together now!") |
| Discovery | `{hypothesis}`, `{data_property}`, `{tally_result}` | Question to test — **MUST be visually verifiable from a photo** (see allowed list below), what the AI assesses per find, how to present results (chart, score) |

**Discovery `field_experiment` visual verification constraint:**
- **Allowed hypothesis properties**: color, shape, material type (metal/wood/plastic/rubber), size (bigger/smaller than X), count, alive/not-alive, category membership (natural/man-made), position (above/below, near/far)
- **Banned hypothesis properties**: texture (rough/smooth), weight (heavy/light), temperature (warm/cold), sound, smell, taste, flexibility (bendy/stiff)
- **AI-as-assessor mechanic**: After each photo, the AI identifies the relevant property and announces it. The child reacts, but does NOT provide the data. This preserves genuine surprise at the tally. |
| Adventure | `{quest_criterion}`, `{detail_harvesting}`, `{quest_narrative}` | What to find ("things that used to be something else"), what to ask per find ("What does it remind you of?"), how the story weaves character details |
| Nurture | `{needs_per_item}`, `{care_solutions}`, `{mutual_aid_synthesis}` | Need AI identifies per find (dry, broken, lonely), care actions child proposes, how items help each other at synthesis |

### Dimension Anchoring (mapping-informed designs)

Before brainstorming creative variables, select 2–3 **anchor dimensions** from the entity mapping that will supply the activity's core content (see entity_guidance.md §6).

**For Category 5 — Physical-First anchoring:**

| Anchor Priority | Dimension Type | Purpose in Activity |
|----------------|----------------|---------------------|
| Primary anchor | appearance | Defines the collection criterion — the visual feature children look for |
| Secondary anchor | structure or senses | Adds depth to what children notice about each find |
| Engagement ground | relationship or reasoning | Drives the synthesis step — comparison, pattern-finding, "why" questions |

**How anchors shape creative variables:**
- `{visual_feature}` comes from the primary anchor's `attribute` + `value` fields
- `{collection_criterion}` generalizes the visual feature into a findable pattern
- Pillar-specific synthesis draws from the engagement ground dimension
- `{reflective_question}` draws from reasoning or relationship dimension prompts
- `{stuck_hint}` should reference WHERE the attribute naturally occurs (from context dimension if available)

### Entity Adaptation Checklist

When adapting to a new entity, verify:
- [ ] The pillar's magic moment is clearly present in Step 4
- [ ] The game element creates genuine stakes (uncertainty, surprise, or challenge)
- [ ] A blind reader could identify which pillar this design belongs to
- [ ] The pillar's specific game mechanic drives Step 3 (not generic Q&A)
- [ ] The stuck hint names REAL, SPECIFIC places to look (not "look around you")
- [ ] The synthesis step uses the pillar-specific mechanic (not generic)
- [ ] The reflective question has no single "correct" answer — it invites genuine wondering
- [ ] The visual feature is something a 4–6 year old can ACTUALLY OBSERVE on this entity
- [ ] The collection criterion is broad enough to find 3+ items in a typical outdoor setting
- [ ] The collection criterion is specific enough to feel like a real mission (not just "find anything")
- [ ] The metaphor makes sense for THIS entity (not forced/generic)
- [ ] The role title is specific to what the child actually DOES (not generic "explorer")
- [ ] Closing IB concepts are EARNED by what the child did, not pre-assigned
- [ ] (Mapping-informed) Anchor dimensions are identified and drive the creative variables
- [ ] (Mapping-informed) Visual feature and collection criterion trace to mapping attributes

---

## How the Agent Uses These Templates

1. **Read the base template** for the assigned category (Template A for Cat1, Template B for Cat5)
2. **Read the pillar overlay** for the assigned experience pillar (within the base template's pillar-specific sections)
3. **Brainstorm creative variables** — universal variables first, then pillar-specific variables. Use the Quick Entity Brainstorm Guide for inspiration, but always invent something FRESH. Never copy the example rows directly.
4. **Fill the step skeleton** with entity-specific content, expanding each step to full program.md format (complete dialogue, 3 response branches, screen descriptions)
5. **Verify with the Entity Adaptation Checklist** before moving to self-evaluation
6. **Run the 10-dimension rubric** (D1–D10) as normal

The base template ensures structural consistency across a category. The pillar overlay ensures each activity delivers the right emotional experience. The creative variables ensure every activity feels unique.

---

## Quick Entity Brainstorm Guide

The same entity can be designed under different pillars — the pillar determines the emotional shape of the experience. Use this table for inspiration, then invent something FRESH.

### How the Same Entity Works Across Pillars

| Entity | Pillar | Style | Metaphor Direction | Role Title Direction |
|---|---|---|---|---|
| Teddy bear | Nurture | `care_station` | "Teddy needs bedtime help" | "Bedtime Helper" |
| Teddy bear | Mystery | `mystery_lens` | "What's teddy hiding?" | "Teddy Detective" |
| Teddy bear | Creation | `inventor_workshop` | "Super Teddy modifications" | "Teddy Engineer" |
| Lion | Performance | `voice_stage` | "Jungle talent show" | "Roar Reporter" |
| Lion | Discovery | `prediction_lab` | "What will the lion do?" | "Lion Scientist" |
| Dandelion | Adventure | `quest_collector` | "Find things that transform" | "Wish Puff Scout" |
| Dandelion | Discovery | `field_experiment` | "Are most seeds fluffy?" | "Seed Scientist" |
| Playground | Discovery | `field_experiment` | "Test playground hypothesis" | "Playground Researcher" |
| Playground | Creation | `mix_lab` | "Combine equipment powers" | "Playground Inventor" |

### Entity Type Brainstorm by Pillar

| Entity Type | Natural Pillars | Why It Fits |
|---|---|---|
| Stuffed animals / toys | Nurture, Performance, Mystery | Rich emotional affordances — easy to care for, perform as, or investigate |
| Food items | Adventure, Discovery, Creation | Natural life journeys, cause-effect transformations, combinable properties |
| Vehicles (toy) | Adventure, Discovery | Destinations and time jumps; predict what happens on the route |
| Household objects | Mystery, Creation, Nurture | Hidden lives to investigate, mashup potential, "help it" scenarios |
| Animals (real or toy) | Performance, Discovery, Nurture | Expressive characters, observable behaviors to predict, care relationships |
| Nature items (outdoor) | All pillars (Cat5) | Visually rich, findable, varied — work for any collection mission |
