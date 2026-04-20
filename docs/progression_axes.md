# Progression Axes

> **Status**: v0.1 inaugural draft · 2026-04-20
> **Owns**: the 7-axis enum, the L1/L2/L3 progression ladder, and the detection cues the runtime uses to classify activities.
> **Consumed by**: `program.md` (tag-block generation), `templates.md` (Template 0 `progression` block), `docs/child_recap_preview.html` §04/§05, `docs/parent_growth_path_preview.html` §02/§03/§05/§07, `docs/template_0_preview.html` §04/§07.

---

## Introduction

### What a "topic axis" is

A **topic axis** is one of seven named trajectories along which a child's thinking about any entity can deepen. Every activity in the WonderLens catalog declares exactly one primary axis (and may claim a secondary — see [Axis interaction](#axis-interaction)) plus a difficulty rung 1–3. Together, axis × rung defines *where this activity lives on the child's map* — independent of the entity, pillar, category, or tier of the design.

An axis is not a topic. "Ladybug" is a topic; "Form" is an axis. A Form activity about a ladybug sits on the same ladder as a Form activity about a rock, a sunflower, or a rubber duck. That's the point: the child's growth story reads as *"she got deeper on Form this week"*, not *"she played three unrelated games"*.

### Why axes instead of a single ladder

An earlier draft of the progression model used a single flat ladder (`beginner → intermediate → advanced`) plus free-form `topic_axis` strings like `color_naming` or `pattern_recognition`. Two problems killed it:

1. **The axis strings drifted.** Designers invented new ones per activity. There was no bounded set, so downstream consumers (child recap, parent dashboard) couldn't render a coherent "curiosity profile".
2. **The ladder was too coarse.** Advancement on "colour" looks nothing like advancement on "empathy" — the same numeric rung meant different cognitive moves depending on the axis.

Fixing both: promote the IB PYP Key Concepts already in use as the activity's "thinking lens" (see `program.md` §1.4) to *also* be the progression axes. Same seven names; the thinking lens and the progression ladder share one vocabulary. Nothing new to memorize, and the axis set becomes bounded at 7.

Sub-cases of a concept — color, shape, texture, size, pattern — are all *specializations of a rung*, not axes themselves. A "color-naming" activity is Form-L1 on the color specialization. A "shape + pattern" activity is Form-L2. Keep the concept abstract; let the rung carry the specialization.

### Relationship to IB PYP Key Concepts

The seven axes map 1:1 to the seven IB PYP Key Concepts:

| Axis | IB Key Concept | Driving question |
| --- | --- | --- |
| Form | Form | What is it like? |
| Function | Function | How does it work? |
| Causation | Causation | Why is it like this? |
| Change | Change | How is it changing? |
| Connection | Connection | How is it connected? |
| Perspective | Perspective | Whose point of view? |
| Responsibility | Responsibility | What should we do? |

The `key_concepts` tag (parent-facing, 1–2 concepts per activity) and the `progression.topic_axis` tag (parent-facing, exactly 1 per activity) draw from the same vocabulary. They are *not* the same field, though. `key_concepts` names *which lenses the activity looked through*; `topic_axis` names *which lens the child is progressing along*. An activity can legitimately list Form + Connection under `key_concepts` while declaring `topic_axis: form` — the Form trajectory is what gets escalated round-by-round.

### Relationship to the `progression.topic_axis` tag-block field

Every Template 0 activity has a required `progression` block inside its tag block. The three fields are:

```yaml
progression:
  topic_axis:       {form|function|causation|change|connection|perspective|responsibility}
  difficulty_level: {1|2|3}
  next_step_hint:   "..."
```

- `topic_axis` is the axis this activity is working on. **Lowercase**, matching the enum in this doc.
- `difficulty_level` is the rung 1, 2, or 3 as a bare integer.
- `next_step_hint` is a one-line free-text suggestion for where the child could go next — either same axis at rung+1, or a sibling axis at rung−1 (see [Axis interaction](#axis-interaction)).

The canonical schema lives in `docs/template_0_preview.html` §04 (the tag block) and §03 (the Template 0 skeleton). This doc owns the semantics of the axis enum and the rung ladder; the HTML owns the literal YAML shape.

---

## The 7 axes

Axes appear in canonical order: **Form, Function, Causation, Change, Connection, Perspective, Responsibility.** This order is not arbitrary — it echoes the IB PYP Key Concept list (`program.md` §1.4) and the curiosity radial spoke layout (`docs/parent_growth_path_preview.html` §03). Keep the order stable; downstream views depend on it.

Each axis section below is structured identically:

1. **Header blockquote** — one-sentence definition, the IB Key Concept it maps to, and a *personality word* (used by the parent dashboard's curiosity-profile captions — see `docs/parent_growth_path_preview.html` §03).
2. **L1 / L2 / L3 progression signals** — concrete behaviors the child exhibits at each rung, with an example utterance.
3. **Detection cues** — phrases, verbs, and question patterns the runtime listens for to classify an activity onto this axis.
4. **Entity affinity** — which kinds of entities naturally anchor on this axis.
5. **Example dialogue — T0 / T1 / T2** — one short exchange per tier, showing how the rung reads at each age band.

The **L1/L2/L3 level legend** is constant across every axis:

- **L1 Notice** — observe, name, or identify one instance of the concept.
- **L2 Extend** — add more examples, more parts, more steps, or a related viewpoint.
- **L3 Reason** — explain why, predict what-if, or state the rule that ties the whole set together.

The exact rung labels differ per axis (Form-L1 = "name a dominant attribute"; Connection-L1 = "match one shared property"; Responsibility-L1 = "notice a need") but the cognitive shape is identical: **first observation → elaboration → explanation**. L1/L2/L3 is a *cognitive depth* axis and is **orthogonal to T0/T1/T2**, which adapts language register to age. A 4-year-old and a 7-year-old can both be on Form-L2; the rung is the same, the words differ.

---

### Form

> **Definition.** From naming one observable attribute of the entity to explaining why that attribute exists.
> **IB Key Concept.** Form — *what is it like?*
> **Personality word** (used by parent dashboard captions): *observer* / *attribute-namer*.

**L1 · Name a dominant attribute.**
The child picks one observable property and names it — color, shape, size, texture, pattern, or count. One property, one label.
- Example: *"The ladybug is red."* / *"It is round."* / *"It has spots."*

**L2 · Name multiple, locate each.**
The child names 2–3 attributes and places each on a specific part of the entity. Location matters — "spots on the back" beats "spots somewhere".
- Example: *"Red body, black spots, tiny black legs."*

**L3 · Explain why the attribute exists.**
The child reasons about purpose — warning, camouflage, ripeness, signaling, protection. The attribute stops being a label and starts being evidence.
- Example: *"Red warns birds not to eat it."*

**Detection cues.**
- Phrases: *"it is [color/shape/size]"*, *"this has [attribute]"*, *"look at its [part]"*.
- Verbs the AI uses to escalate: *name, notice, spot, compare, describe*.
- Question patterns: *"What color is it?"* · *"What do you see on its back?"* · *"Why might it be that color?"*

**Entity affinity.**
Any entity with salient visual properties: animals with distinctive markings (ladybug, butterfly, goldfish), fruits with ripeness cues (banana, apple), collectibles with sortable surface features (rocks, leaves, shells). Weak fit for entities whose interest is functional rather than visual (rubber duck in an inventor workshop → use Function).

**Example dialogue.**

- **T0 · Form-L2** (ladybug)
  > **AI**: "Big red back! Tiny black dots! One more thing — what about the legs?"
  > **Child**: "Tiny black legs!"
  > **AI**: "Red. Black. Black. So many parts, all named!"

- **T1 · Form-L2** (sunflower)
  > **AI**: "You found three things to tell me about the sunflower — what were they?"
  > **Child**: "Yellow petals, brown middle, long green stem."
  > **AI**: "Nice — you put each one on a part of the flower. Where did the petals come from on the flower?"

- **T2 · Form-L3** (ladybug)
  > **AI**: "You said the ladybug is red *and* has spots. Why do you think it has both, not just one?"
  > **Child**: "Red says 'stop' to birds, and the spots make it look bigger so birds think it's scary."
  > **AI**: "Two warning signals at once. That's called aposematism — a word for using color + pattern together to say 'don't eat me'."

---

### Function

> **Definition.** From pointing at the parts of an entity to predicting what happens when a part is missing.
> **IB Key Concept.** Function — *how does it work?*
> **Personality word**: *investigator* / *tinkerer*.

**L1 · Point to and name the parts.**
The child names the visible parts of the entity without explaining what they do. Just the inventory.
- Example: *"Wheels. Door. Window. Roof."*

**L2 · Explain what each part does.**
The child connects each part to its role. The part stops being a noun and becomes a verb.
- Example: *"Wheels roll. Door opens so people get in. Window lets you see out."*

**L3 · Predict what happens without a part.**
The child reasons counterfactually about a removed or broken part. Function becomes causal structure.
- Example: *"No wheels? It can't move. No door? Nobody gets in."*

**Detection cues.**
- Phrases: *"this part [does X]"*, *"the [part] is for [role]"*, *"if there was no [part]…"*.
- Verbs: *works, does, makes, lets, opens, closes, carries, holds*.
- Question patterns: *"What does this part do?"* · *"Why does it need [part]?"* · *"What if we took the [part] off?"*

**Entity affinity.**
Assembled or part-rich entities: vehicles (car, plane, bike), toys with visible mechanisms (rubber duck, wind-up toy, robot), bodies with obvious role-differentiated parts (butterfly wings/antennae, bird beak/feet). Weak fit for undifferentiated blobs (a pebble) — use Form or Change there.

**Example dialogue.**

- **T0 · Function-L1** (rubber duck)
  > **AI**: "Duck parts! Point, say. Go!"
  > **Child**: "Beak! Eye! Wing!"
  > **AI**: "Beak! Eye! Wing! Three parts spotted!"

- **T1 · Function-L2** (rubber duck)
  > **AI**: "You pointed at three parts. What do you think each part is *for*?"
  > **Child**: "The beak is for quacking. The eyes are for seeing. The wings are for flapping."
  > **AI**: "Three parts, three jobs. Good thinking about what each one does."

- **T2 · Function-L3** (toy robot)
  > **AI**: "If we took the wheels off this robot, what couldn't it do anymore?"
  > **Child**: "It couldn't roll around. But it could still wave its arms."
  > **AI**: "Exactly — the wheels do *moving*, the arms do *greeting*. Different parts, different jobs, and if one's gone only *that* job stops."

---

### Causation

> **Definition.** From describing what happened to explaining the underlying mechanism.
> **IB Key Concept.** Causation — *why is it like this?*
> **Personality word**: *investigator* / *explainer*.

**L1 · Describe what happened.**
The child narrates the observed event without inferring cause. Just the "what", not the "why".
- Example: *"The flower closed up."*

**L2 · Predict what will happen next.**
The child projects a future outcome from the current state. Prediction is the bridge between observation and explanation.
- Example: *"If I bring it into the sun, it will open again."*

**L3 · Explain the mechanism.**
The child gives a causal story for the observed behavior. Names a reason, not just a sequence.
- Example: *"The petals need sunlight to stay open — they close to save energy at night."*

**Detection cues.**
- Phrases: *"that's because…"*, *"it happened when…"*, *"if I do X, then Y"*.
- Verbs: *happened, caused, because, made it, turned into, reacts to*.
- Question patterns: *"What did you see happen?"* · *"What do you think will happen if…?"* · *"Why do you think that happened?"*

**Entity affinity.**
Entities with visible state changes or clear input→output behavior: goldfish (feeding → swimming response), sunflower (sunlight → opening), banana (time → ripening), water (heat → steam). Weak fit for static entities — those lean Form or Function.

**Example dialogue.**

- **T0 · Causation-L1** (goldfish)
  > **AI**: "Look! Fish moved fast! What did the fish do?"
  > **Child**: "It swam!"
  > **AI**: "It swam! You saw it happen!"

- **T1 · Causation-L2** (sunflower)
  > **AI**: "The flower is closed up right now. What do you think will happen if we put it by the window?"
  > **Child**: "It'll open up again."
  > **AI**: "Let's try it and find out. You predicted — now let's check."

- **T2 · Causation-L3** (sunflower)
  > **AI**: "You said the petals close at night. What do you think they're *doing* when they close?"
  > **Child**: "Saving energy. Like, they don't need to catch sun when there's no sun, so they fold up to rest."
  > **AI**: "That's exactly the mechanism — conserving energy when the input stops."

---

### Change

> **Definition.** From ordering two moments in time to telling a full transformation journey with connecting causes.
> **IB Key Concept.** Change — *how is it changing?*
> **Personality word**: *storyteller* / *journey-tracker*.

**L1 · Order two moments.**
The child places two states in correct temporal order. Before and after, nothing in between.
- Example: *"First the green banana. Then the yellow banana."*

**L2 · Fill in before & after.**
The child adds a missing third moment to complete a sequence — adds a middle, or extends past the end.
- Example: *"Before: green. Now: yellow. After: brown and soft."*

**L3 · Tell a transformation journey.**
The child narrates the whole arc with connecting causes between stages. Not just what, but why each step led to the next.
- Example: *"The seed drank rain, grew a stem, made leaves, opened a flower, then dropped new seeds."*

**Detection cues.**
- Phrases: *"first… then…"*, *"it used to be… now it's…"*, *"next it will…"*.
- Verbs: *grew, became, turned into, changed, used to be, going to be*.
- Question patterns: *"What was it like before?"* · *"What will it be like next?"* · *"Can you tell the whole story from start to end?"*

**Entity affinity.**
Entities with obvious life cycles or state trajectories: banana (green → yellow → brown), butterfly (egg → caterpillar → chrysalis → butterfly), sunflower (seed → sprout → flower → seed), leaves (green → red/yellow → fallen). Weak fit for entities that don't visibly transform (a rock at human timescale).

**Example dialogue.**

- **T0 · Change-L1** (banana)
  > **AI**: "Two bananas! Point — which is first?"
  > **Child**: *(points to green)* "This one first!"
  > **AI**: "Green first. Yellow next. You got the order!"

- **T1 · Change-L2** (banana)
  > **AI**: "You put the green one first and the yellow one second. What about after the yellow banana — what comes next?"
  > **Child**: "It turns brown and squishy!"
  > **AI**: "Three moments in order — green, yellow, brown. You filled in the 'after'."

- **T2 · Change-L3** (sunflower)
  > **AI**: "Tell me the whole story of a sunflower — from the first thing to the last thing."
  > **Child**: "A seed falls in the ground, it drinks water, it pushes up a stem, the leaves come out to catch sun, the flower opens, the middle makes new seeds, and then they fall and start again."
  > **AI**: "A full cycle — you even connected why each stage leads to the next. That's a transformation story."

---

### Connection

> **Definition.** From matching one shared property between two items to articulating the rule that connects a whole set.
> **IB Key Concept.** Connection — *how is it connected?*
> **Personality word**: *pattern-finder* / *sorter*.

**L1 · Match one shared property.**
The child finds a second item that shares a single visible property with the first. A pair is enough.
- Example: *"This leaf is also green, like the apple!"*

**L2 · Find 3+ examples of a property.**
The child extends the match to a small collection and groups them together. The set becomes evidence.
- Example: *"Three spotted things: the ladybug, the ball, the cow."*

**L3 · Identify the rule that connects the set.**
The child articulates the property or purpose the whole group shares — and why the grouping is meaningful.
- Example: *"They all have spots. Spots help them hide from predators."*

**Detection cues.**
- Phrases: *"this is like that"*, *"these all have…"*, *"they all…"*, *"they match because…"*.
- Verbs: *match, like, similar, sort, group, both, all*.
- Question patterns: *"What else is like this?"* · *"Can you find three things that share this?"* · *"What do they all have in common, and why might that matter?"*

**Entity affinity.**
Collection-friendly entities whose property we can hunt elsewhere for: leaves (edges, colors), rocks (textures, sizes), flowers (petal counts), small outdoor finds (shells, seeds, sticks). Also any entity used in a quest_collector or mystery_trail style. Connection is the most-covered axis in the current gold-standard inventory (3 Tier-A anchors — see [Axis coverage](#axis-coverage)).

**Example dialogue.**

- **T0 · Connection-L1** (leaves)
  > **AI**: "Green leaf! Can you find one more green thing?"
  > **Child**: *(points to grass)* "That!"
  > **AI**: "Two green things. You matched!"

- **T1 · Connection-L2** (ladybug)
  > **AI**: "You found three spotted things — tell me what they are."
  > **Child**: "The ladybug, my ball, and the picture of a cow."
  > **AI**: "Three spotted things in your collection. What do you want to add next?"

- **T2 · Connection-L3** (playground find set)
  > **AI**: "Your whole collection has spots. What do you think spots *do* for the things that have them?"
  > **Child**: "Spots help them hide. Or warn. It depends on where they live."
  > **AI**: "So the rule isn't just 'spotted' — it's 'spots mean a message'. Hide or warn, depending on the creature."

---

### Perspective

> **Definition.** From attributing a simple feeling to an entity to generating dialogue between two entities — empathy as a ladder.
> **IB Key Concept.** Perspective — *whose point of view?*
> **Personality word**: *storyteller* / *voice-giver*.

**L1 · Attribute a feeling.**
The child assigns a simple emotion to the entity. One feeling, one subject.
- Example: *"The teddy is sleepy."*

**L2 · Imagine the entity's view of you.**
The child reverses viewpoint and imagines what the entity sees or feels about the child.
- Example: *"Teddy thinks I'm big and warm."*

**L3 · Generate dialogue to a third party.**
The child voices the entity speaking about something other than itself. Perspective is now social, not just dyadic.
- Example: *"Teddy tells Bunny: 'My child is gentle and tucks me in.'"*

**Detection cues.**
- Phrases: *"it feels…"*, *"it thinks…"*, *"if I were the [entity]…"*, *"it would say…"*.
- Verbs: *feels, thinks, wants, wishes, would say, sees, believes*.
- Question patterns: *"How do you think it's feeling?"* · *"What does it think of you?"* · *"What would it say to its friend?"*

**Entity affinity.**
Entities with personality hooks: toys (teddy, doll, stuffed animal), voice-friendly animals (lion, bird, cat), imagined humans (queen, pirate). Works with inanimate entities too when framed via voice_stage or ensemble_show — the rubber duck *can* have a day.

**Example dialogue.**

- **T0 · Perspective-L1** (teddy bear)
  > **AI**: "How is teddy feeling today?"
  > **Child**: "Sleepy."
  > **AI**: "Sleepy teddy! You noticed his feeling."

- **T1 · Perspective-L2** (teddy bear)
  > **AI**: "If teddy could see you right now, what would he think about you?"
  > **Child**: "He'd think I'm big. And my hands are warm."
  > **AI**: "You imagined yourself from teddy's side. That's a whole different view."

- **T2 · Perspective-L3** (teddy bear + bunny)
  > **AI**: "Teddy is going to tell bunny about you. What would he say?"
  > **Child**: "Teddy says: 'My kid is gentle — she tucks me in every night and she tells me stories.'"
  > **AI**: "Teddy speaks about you *to* bunny — you gave him his own voice."

---

### Responsibility

> **Definition.** From noticing a need to reasoning about long-term impact of care or neglect.
> **IB Key Concept.** Responsibility — *what should we do?*
> **Personality word**: *carer* / *helper*.

**L1 · Notice a need.**
The child observes that the entity has a need — dirty, dry, lonely, broken, hungry. Noticing, not acting yet.
- Example: *"The flower is droopy."*

**L2 · Propose a care action.**
The child names a concrete action that would help. The gap between need and action closes.
- Example: *"I'll give it water and move it near the window."*

**L3 · Reason about long-term impact.**
The child explains what happens over time with care, and what happens without it. Care becomes a system, not a one-shot.
- Example: *"If I water it every day, it grows. If I forget, the leaves dry and fall off."*

**Detection cues.**
- Phrases: *"it needs…"*, *"I'll help it by…"*, *"if nobody…"*, *"over time it will…"*.
- Verbs: *need, help, care, fix, feed, water, clean, rescue, keep safe*.
- Question patterns: *"What does it need right now?"* · *"What can you do to help?"* · *"What if we kept doing that every day?"*

**Entity affinity.**
Natural home for the Nurture pillar. Entities the child can imagine caring for: flowers (water, light), pets (food, company), teddy bears (warmth, bedtime), plants (soil, sun). Also works for shared-space entities (playground → don't litter; tree → don't snap branches).

**Example dialogue.**

- **T0 · Responsibility-L1** (flower)
  > **AI**: "Look at the flower. Something's not right — what do you see?"
  > **Child**: "It's floppy."
  > **AI**: "You noticed. The flower is floppy. It needs something."

- **T1 · Responsibility-L2** (flower)
  > **AI**: "The flower is droopy. What can we do to help it?"
  > **Child**: "Water it. And put it by the window so it gets sun."
  > **AI**: "Two care actions — water *and* light. That's how the flower knows you noticed."

- **T2 · Responsibility-L3** (flower)
  > **AI**: "You watered the flower today. What happens if you keep doing that every day? What if you stopped?"
  > **Child**: "If I water it every day, it gets big and makes flowers. If I stop, the leaves go brown and the flower dies. So I have to remember, not just one time."
  > **AI**: "Care over time, not a one-time rescue. You're thinking like a keeper."

---

## Axis interaction

### Single-axis is the default

Every activity declares **one** primary `topic_axis`. The round-by-round escalation inside the activity rides that one axis — Beat 3 in the Template 0 spine escalates `{escalation_axis}` which must equal `progression.topic_axis` (see `templates.md` and `docs/template_0_preview.html` §03).

One axis per activity keeps the parent dashboard legible: Mia touched Form three times this week, Connection twice, Perspective once. Not: Mia touched 1.5 axes in a single game.

### Activities that genuinely straddle two axes

Some designs legitimately work on two axes simultaneously — a mix_lab activity on rocks that asks the child to name attributes (Form) *and* group rocks by shared attributes (Connection), for example. Rules of thumb for picking the primary:

1. **Which axis drives the Beat 3 escalation?** If every round climbs the Form ladder (name one attribute → name three → explain why), Form is primary. Connection is secondary, even if the rocks are being grouped.
2. **Which axis owns the Beat 4 magic moment?** The pillar-specific climax almost always reveals one axis's payoff, not both. That's the primary.
3. **Which axis does `next_step_hint` point at?** The hint is a trajectory claim — same-axis rung+1 is the standard next step. The axis the hint is *on* is the primary.

The secondary axis lives in `key_concepts` (not in `progression.topic_axis`). Example tag block for a mix_lab-rocks design:

```yaml
key_concepts: [Form, Connection]    # two lenses the activity looks through
progression:
  topic_axis: form                  # the one axis being climbed
  difficulty_level: 2
  next_step_hint: "Move to Form L3 — ask why each attribute exists. Or sibling-jump to Connection L1."
```

### How to record multi-axis activities in the tag block

The tag block has room for exactly one `progression.topic_axis`. Do not invent a compound value. If the activity genuinely needs to signal both axes to downstream consumers:

- Put both concepts in `key_concepts` (1–2 slots).
- Put the **climbing** axis in `progression.topic_axis`.
- Use `progression.next_step_hint` to name the sibling axis as a follow-up path.

The parent dashboard's progress module reads `topic_axis` for the L×T ladder row; the curiosity radial reads `key_concepts`. Both get their data; neither gets confused.

### Anti-patterns — when an activity claims an axis it's not really working on

1. **Form-washing.** Every activity has *some* observable entity; that doesn't make every activity a Form activity. If the child is asked to name the color once in Beat 1 and nothing else, that's an emotional hook, not Form progression. Look at Beat 3 — if it escalates something else, declare that something else.
2. **Connection-washing.** Finding one similarity in passing is not Connection. Connection requires at least L1 behavior — an intentional second-item match invited by the game. A mystery_lens activity where the child is told "a ladybug is like a stop sign" is not working on Connection; the AI handed the analogy to the child.
3. **Responsibility-theater.** Saying "the flower is pretty" is not Responsibility. The child has to notice a *need*, not a state. If Beat 3 never asks the child to help, the axis is probably Form (observing the flower) or Change (watching it over time).
4. **Axis-swapping mid-activity.** The escalation axis cannot change between rounds. If Beat 3 round 1 climbs Form and round 2 climbs Connection, the design is broken — pick one axis, use the dignity rule (see `docs/template_0_preview.html` §07) to hold or demote within it.

---

## Tag block contract

### Field names

The three progression fields are **fixed strings**. Authors do not rename them. Downstream consumers match on exact field names.

```yaml
progression:
  topic_axis:       <enum>     # required
  difficulty_level: <integer>  # required
  next_step_hint:   <string>   # required
  reward_hook:      <string>   # optional — child-facing badge key
```

### Valid values

**`progression.topic_axis`** — exactly one of:

| Value | Axis |
| --- | --- |
| `form` | Form |
| `function` | Function |
| `causation` | Causation |
| `change` | Change |
| `connection` | Connection |
| `perspective` | Perspective |
| `responsibility` | Responsibility |

Lowercase. No `pattern_recognition`, `color_naming`, or other free-form axis strings — those were the pre-v0.2 Template 0 vocabulary and have been retired. See [Legacy values](#legacy-values) below.

**`progression.difficulty_level`** — one of `1`, `2`, `3` (bare integer, not `L1`/`L2`/`L3`). The human-readable rung names (`L1 Notice`, `L2 Extend`, `L3 Reason`) are used in UI copy and in this doc; the wire-format value is the integer.

**`progression.next_step_hint`** — free-text string, 6–20 words. Names the suggested next activity on the same axis or a sibling axis. Examples:

- *"Move to Form L3 — ask why the red warns predators."*
- *"Sibling jump: Connection L1 — find another round spotted thing."*
- *"Hold at Causation L2; vary the entity (try ice melting)."*

### How child recap §04 consumes this

`docs/child_recap_preview.html` §04 explicitly **does not read** `progression.*` — the child sees what they *did*, not how the IB framework classifies it. Those fields are parent-facing.

The one exception: `docs/child_recap_preview.html` §05 (`highlight_moment` generation) takes `progression.topic_axis` as an *input to the generator*, alongside `attributes`, `pillar`, and the transcript. The axis shapes the one-sentence summary the child sees ("You figured out why the ladybug is red" — Causation-flavored; "You sorted the leaves by their edges" — Connection-flavored). The axis itself is never rendered in child UI.

### How parent dashboard §07 consumes this

`docs/parent_growth_path_preview.html` §07 declares the full read contract. The progression fields feed three modules:

| Module | Fields read |
| --- | --- |
| Progress (L×T ladder) | `progression.topic_axis`, `progression.difficulty_level`, `progression.next_step_hint`, `tier` |
| Curiosity profile | `key_concepts`, `progression.difficulty_level` (aggregate) |
| Try at home | `progression.topic_axis`, `progression.next_step_hint`, recent `entity` |

Three surfaces, same three fields, different aggregation. That's the whole reason the axis enum has to be fixed and small.

### Cross-reference

For the canonical YAML shape of the whole tag block (not just `progression`), see `docs/template_0_preview.html` §04. For the generation rules (which field is required, which is optional, which is runtime-generated), see `program.md` Tag Block section (added in Phase 1b).

### Legacy values

Pre-v0.2 Template 0 drafts (see `docs/plans/2026-04-16-template-0-implementation.md`) used free-form axis strings such as `pattern_recognition`, `color_naming`, and `cause_effect`. The `docs/template_0_preview.html` §04 example YAML previously carried one legacy string (`topic_axis: pattern_recognition`); it was migrated to `topic_axis: connection` in the same PR that shipped this doc (v0.1), so the preview is now aligned with the canonical enum.

Going forward, any `topic_axis` value outside the seven canonical strings is invalid and should be treated as a design error.

### Axis coverage

Current Tier-A gold-standard activities distribute across the 7 axes as follows (from `docs/template_0_preview.html` §07 coverage check):

| Axis | Gold-standard count | Representative activity |
| --- | --- | --- |
| Form | 1 | mix_lab · rock · Creation · L2 |
| Function | 2 | mystery_lens · toy_robot · Mystery · L2 |
| Causation | 1 | prediction_lab · goldfish · Discovery · L2 |
| Change | 1 | time_traveler · banana · Adventure · L2 |
| Connection | 3 | mystery_trail, field_experiment, quest_collector |
| Perspective | 2 | voice_stage · lion, ensemble_show · bird |
| Responsibility | 2 | care_station · teddy, rescue_team · flower |

**Form, Causation, and Change** have only one anchor each — worth asking whether those axes need more Tier-A seeds before Tier-B constellation content expands against them.

---

## Versioning

<!-- When adding a new revision, prepend to this list and bump the version tag at the top of the file. -->

- **v0.1** · Inaugural draft · 2026-04-20 · Extracted the 7-axis enum, L1/L2/L3 ladder, detection cues, and tag-block contract from `docs/template_0_preview.html` §07 and `docs/parent_growth_path_preview.html` §03/§07. This doc is now the source of truth for the axis enum; the preview docs defer to it.
