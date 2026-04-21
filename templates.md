# Templates

> **Version**: 1.1 | **Date**: 2026-04-20
> **Owns**: the pillar-overlay contents (Mystery, Creation, Performance, Discovery, Adventure, Nurture) and the Cat1 / Cat5 category modifier appendix.
> **Does NOT own**: the 5-beat spine, the tag block schema, or the tier defaults — those live in `docs/template_0_preview.html` §03 / §04 / §06 and are the single source of truth for the category-agnostic skeleton.
> **Consumed by**: `program.md` Phase 5 (template-reading flow), `docs/progression_axes.md` (cross-ref from axis → pillar affinity), `designs/cat{1,5}/*.md` (gold-standard outputs).

---

## How templates work

An activity design is built by composing three layers:

1. **Template 0** — the category-agnostic skeleton. It defines the 5-beat spine (Transition Bridge → Frame & Role → Core Loop → Magic Moment → Celebration), the tag-block contract, the universal creative variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`), and the three tier dials (T0 / T1 / T2). Full skeleton lives in `docs/template_0_preview.html` §03; tag block in §04; tier defaults in §06.
2. **Pillar overlay** — one of the six overlays below (Mystery / Creation / Performance / Discovery / Adventure / Nurture). It specializes beats 2, 3, and 4: the framing metaphor, the per-round interaction mechanic, the magic-moment shape. It also declares a small set of pillar-specific creative variables (e.g. `{hidden_details}` for Mystery, `{modifications}` for Creation) that stack on top of the universal four.
3. **Category modifier** — Cat1 (in-device, sustained verbal) or Cat5 (out-of-device, collection/tracking), drawn from the appendix at the bottom of this file. Category modifiers are small — 8 fields (beat medium, round count, camera use, setting, step count, core mechanic, anchor priority, checklist extras). They do not reshape the pillar; they only set the physical frame the pillar plays inside.

The three layers compose like this: `Template 0 + pillar overlay + category modifier → a design's structural scaffold`. The agent then fills the `{slots}` and expands each beat to full program.md format.

**Why Option B (one file).** Each pillar's creative variables (like `{hidden_details}`, `{modifications}`, `{quest_criterion}`) are pillar-specific and worth keeping next to the pillar's interaction mechanic. A split-file layout forced a reader to jump between a creative-variables index and a beat-level overlay. This file keeps each overlay self-contained: game mechanic, payoff, variables, beats, axis affinity, and example references all in one place.

---

## Template 0 reference

Template 0 is the invariant 5-beat spine that every activity shares. The canonical YAML skeleton is in `docs/template_0_preview.html` §03 — do not re-derive or copy it into designs. Instead, assume every design inherits the spine and read the preview once to internalize the shape.

Compressed spine for quick reference (authoritative version lives in the preview):

```
beat_1_transition_bridge  — emotional hook; photo → imaginative reaction; NEVER knowledge-test
beat_2_frame_and_role     — assign {role_title} + {metaphor}; state the mission    ← pillar overlay drives
beat_3_core_loop          — N rounds of pillar-specific mechanic; escalates on {escalation_axis} ← pillar overlay drives
beat_4_magic_moment       — pillar-specific synthesis; the emotional climax        ← pillar overlay drives
beat_5_celebration        — name earned Key Concepts + Related Concepts as praise
```

The overlay hooks the pillar overlays specialize are exactly **beats 2, 3, and 4**. Beats 1 and 5 are universal — same shape for every pillar.

**Universal creative variables** (all pillars inherit these from §02 of the Template 0 skeleton):

| Variable | Description |
| --- | --- |
| `{metaphor}` | The imaginative frame that turns the activity into play. Pillar-flavored but pillar-agnostic in name. |
| `{role_title}` | The badge the child earns. Verb-forward, specific to what they DO. |
| `{escalation_axis}` | How rounds get progressively richer. Rides `progression.topic_axis` from the tag block. |
| `{reflective_question}` | The closing "why" that invites genuine wondering — no single correct answer. |

Every pillar overlay layers 2–3 pillar-specific variables on top of these four (see each overlay below).

**Tag block.** Every design emits the §04 tag block (activity_id, entity, category, pillar, style, tier, tier_variants, tags, kud, progression, caregiver_role). The authoritative shape + field semantics live in `docs/template_0_preview.html` §04 and are re-stated in `program.md` §1.9. This file does not duplicate the tag-block schema.

**Attribute coverage.** Every activity must populate `entity_attributes_covered` in its tag block — a flat list of dotted-path IDs (`tier_{0,1,2}.{dimension}.{attribute}`) that the activity exercises from its entity's `tier_guidance`. The matcher uses this list to route photographed entities to activities, so every ID must resolve to a real `attribute:` entry under `data/mappings_dev20_0318/.../{yaml}`. See `program.md` §1.9 for the full contract and the entity YAML's `tier_guidance` section for the source of valid IDs.

**Tier dials.** T0 / T1 / T2 set language register, task depth, concept focus, AI role, and cumulative caregiver role. Authoritative table in `docs/template_0_preview.html` §06. Tier-guidance detail lives in `entity_guidance.md`.

---

## Overlay: Mystery

**Game mechanic.** The AI hides something — a feature of the photographed entity, or a pattern that will connect several outdoor finds — and feeds the child **progressive clues** (visual, textural, functional, imaginative). The child guesses, narrows, and ultimately uncovers the hidden thing. Suspense builds turn by turn; the climax is a reveal.

**Payoff pattern.** The magic moment the child feels as the "win" is *"I figured it out!"* — the moment the hidden detail or hidden pattern snaps into place. The AI stages a deliberate reveal (dramatic pause, zoom-in, sparkle, a riddle line finally spoken in full) so the child experiences the shift from "I don't know yet" to "I see it now" as a concrete event rather than a verbal confirmation.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{hidden_details}` | What is hidden behind the clues — 3–5 specific features of the entity (in-device) or 3–4 items to collect on an outdoor trail (out-of-device). Must be genuinely discoverable from the entity's real appearance. |
| `{clue_types}` | The rotation of clue modes per round: visual (color, shape), textural (rough, fuzzy), functional (what it does), imaginative (what it reminds you of). Mixing modes keeps the loop fresh. |
| `{reveal_drama}` | How each reveal is dramatized on screen: dramatic pause → zoom-in, glow-on-the-spot, sparkle pulse, or a progressive unveiling of the hidden pattern as new items join the collection. |

**Beat 2 framing.** The AI sets up Mystery as a detective puzzle. In-device: *"I'm going to think of something hidden in your photo. I'll give you clues — you tell me when you figure it out."* Out-of-device: *"You're a {role_title}! I'll give you riddle-clues, and each one points to something out there. Find them all and a hidden pattern will appear."* The role title is specific (Detective, Scout, Codebreaker), never generic.

**Beat 3 interaction.** The per-round loop is **clue → guess → confirm/redirect**. The AI gives one clue, the child proposes a match (in-device: verbally; out-of-device: by photographing a candidate). The AI responds with "warmer / colder" language in-device, or confirms/redirects the photo match out-of-device. Each round's clue targets a different detail, so the child learns that even a familiar entity or a familiar yard is full of discoverable specifics.

**Beat 4 closing.** The magic moment is the **reveal**. In-device: the AI announces the full hidden detail with a visual flourish and celebrates *"You figured it out!"*. Out-of-device: the AI reveals the **hidden pattern** that connects all finds — the theme the riddle-clues were pointing at all along — and the child sees their collection re-framed as a coherent discovery.

**Axis affinity.** Mystery naturally anchors on **Form** (noticing specific features, decoding what's visible) and **Connection** (for out-of-device trails, seeing the hidden pattern that links finds). See `docs/progression_axes.md` — Form §"What is it like?" for the primary affinity.

**Gold-standard examples.**
- `designs/cat1/detail_detective_property_gold_prod.md` — mystery_lens, Form + Function, in-device.
- `designs/cat5/butterfly_cat5_gold_prod.md` — mystery_trail, riddle-clues uncover a habitat pattern.
- `designs/cat5/pattern_trail_property_gold_prod.md` — property-gold version parameterized by any findable pattern.

---

## Overlay: Creation

**Game mechanic.** The AI proposes **what-if modifications** or identifies **properties as superpowers**, and the child invents combinations. Each round adds a new modification/ingredient; the creation grows progressively wilder. The climax is the **unveiling of the combined creation** — "Super {entity}" — with every modification visibly stacked.

**Payoff pattern.** The magic moment is *"I made this!"* — the child sees their invention revealed as a coherent thing (even if absurd). The AI's role is to elaborate and say yes-and, never to correct. The reveal uses a "ta-da!" animation that shows all modifications combined at once, so the child feels the scale of what they built.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{modifications}` *(in-device)* / `{superpowers_per_item}` *(out-of-device)* | The what-if changes proposed each round (in-device), or the "superpower" the AI assigns each collected item (out-of-device: sticky, bouncy, smooth, stretchy, etc.). Must connect to the item's real property. |
| `{combination_name}` *(in-device)* / `{invention_name}` *(out-of-device)* | The name of the final combined creation — "Super {entity}" or "The {adjective} {noun}". Child-delightful and specific, not generic. |
| `{absurdity_escalation}` *(in-device)* / `{combination_prompt}` *(out-of-device)* | How the modifications get wilder (Round 1 plausible → Round 3 impossible-but-delightful), or the prompt that invites the child to combine superpowers into one invention. |

**Beat 2 framing.** In-device: *"We're going to imagine wild changes to your {entity}. What if it had…? Let's invent!"* Out-of-device: *"You're a {role_title}! Your mission — collect ingredients. Each one has a superpower."* The frame makes clear the child is the inventor; the AI is the enthusiastic assistant.

**Beat 3 interaction.** In-device: **AI proposes what-if → child invents → AI elaborates and yes-ands, adding the modification to a visible running creation.** Out-of-device: **child finds an item → AI identifies its superpower (sticky, bouncy, smooth) → child names it.** Each round escalates: round 1 is plausible, round 3 is delightfully absurd. The AI never says "that's not how it works" — Creation is sandbox mode.

**Beat 4 closing.** The magic moment is the **ta-da! reveal**. In-device: the AI narrates the assembly of all modifications into one "Super {entity}" and shows it visually. Out-of-device: the child combines the collected superpowers into an invention — "Let's put sticky + bouncy + shiny together. What is it? What does it do?" — and the AI narrates the invention into being.

**Axis affinity.** Creation naturally anchors on **Change** (transformations, what-if modifications) and **Function** (for out-of-device, composing properties into new capabilities). See `docs/progression_axes.md` — Change §"How is it changing?".

**Gold-standard examples.**
- `designs/cat1/what_if_workshop_property_gold_prod.md` — inventor_workshop, property-gold.
- `designs/cat1/rubber_duck_cat1_gold_prod.md` — inventor_workshop on a toy.
- `designs/cat5/texture_mix_property_gold_prod.md` — mix_lab, texture as superpower.
- `designs/cat5/rock_cat5_gold_prod.md` — mix_lab on natural finds.

---

## Overlay: Performance

**Game mechanic.** The {entity} is going **on stage**. The child takes the performer's role — voicing, animating, directing — and the AI plays the **audience** (judges, fans, animals, siblings in character). In-device: the child performs a sequence of escalating challenges. Out-of-device: the child assembles an ensemble of found items and gives each a voice or role.

**Payoff pattern.** The magic moment is the **standing ovation** — the audience erupts, encore requested, or the ensemble concert plays out with all voices together. The child feels celebrated for expressive risk-taking. The AI's reactions are specific (gasps, laughter, cheers) rather than generic praise.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{challenges}` *(in-device)* / `{sound_per_item}` *(out-of-device)* | The performance prompts per round (in-device: sad lion, happy lion, brave lion), or the voice/sound the child assigns each collected item (out-of-device). |
| `{audience_character}` *(in-device)* / `{ensemble_narrative}` *(out-of-device)* | Who reacts and how — three judges, a stadium, a jungle audience (in-device); or the concert script (solos then ensemble) out-of-device. |
| `{twist_challenge}` *(in-device)* / `{conductor_moments}` *(out-of-device)* | The surprise that changes the rules mid-performance (in-device: "now do it like a whisper!"), or the directing moments out-of-device ("all together now!"). |

**Beat 2 framing.** In-device: *"Your {entity} is going on stage! I'll be the audience. Here's challenge one…"* Out-of-device: *"You're the {role_title}! Your mission — assemble a cast for the big show, one sound or voice per find."* The frame foregrounds expression, not correctness.

**Beat 3 interaction.** In-device: **AI sets a challenge → child performs (voice, sound, gesture described) → AI reacts AS audience.** The reaction is in-character — gasps, cheers, laughter, a judge's comment — not metacommentary. Out-of-device: **child finds item → AI asks "what sound would it make?" → child assigns a voice → AI narrates the item joining the cast.** Escalation: round 1 is warm-up, round 2 introduces contrast, round 3 adds the twist.

**Beat 4 closing.** The magic moment is the **performance finale**. In-device: the audience goes wild, encore requested, a trophy or standing ovation animation plays. Out-of-device: the AI narrates the ensemble concert — each item performs its voice in turn, then all together — and the child conducts.

**Axis affinity.** Performance naturally anchors on **Perspective** (taking on a role, imagining how another character feels/sounds) and **Form** (observing features that motivate the voice/sound assigned). See `docs/progression_axes.md` — Perspective §"Whose point of view?".

**Gold-standard examples.**
- `designs/cat1/lion_cat1_gold_prod.md` — voice_stage, escalating roar challenges with a twist round.
- `designs/cat1/property_performer_property_gold_prod.md` — voice_stage, property-gold.
- `designs/cat5/bird_cat5_gold_prod.md` — ensemble_show, outdoor bird-voice cast.
- `designs/cat5/sound_stage_property_gold_prod.md` — ensemble_show, property-gold.

---

## Overlay: Discovery

**Game mechanic.** The child **commits to a prediction before exploring**, then the AI runs the trial — either by presenting cause-effect scenarios in-device, or by assessing photographed finds against the hypothesis out-of-device. Each round adds data; the climax is the **tally reveal**: "Was I right?!"

**Payoff pattern.** The magic moment is the **tally result** — a final count that confirms or surprises. Discovery differs from Mystery in that Discovery's stakes are **prediction vs outcome**, not hidden-vs-revealed. The child's own guess is on the line. The AI's job is to preserve the surprise — out-of-device, the AI (not the child) assesses each find, so the running tally isn't self-reported.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{scenarios}` *(in-device)* / `{hypothesis}` *(out-of-device)* | Cause-effect scenarios per round (in-device: "what will the lion do if…?"), or the single testable question the child commits to (out-of-device: "most playground things are metal?"). |
| `{scoring_system}` *(in-device)* / `{data_property}` *(out-of-device)* | How points are tracked and awarded (in-device), or the specific property the AI assesses per find (out-of-device). |
| `{reveal_drama}` *(in-device)* / `{tally_result}` *(out-of-device)* | How the final reveal is dramatized — a score tally with a surprise bonus round, or the final count chart flipping from hidden to visible. |

**Out-of-device hypothesis constraint** (load-bearing — keep in sync with designs):
- **Allowed hypothesis properties**: color, shape, material type (metal/wood/plastic/rubber), size (bigger/smaller than a hand), count, alive / not-alive, category membership (natural / man-made), position (above / below, near / far).
- **Banned hypothesis properties**: texture (rough/smooth), weight, temperature, sound, smell, taste, flexibility — none are visually verifiable from a photo.
- **AI-as-assessor rule**: after each photo, the AI identifies the property and announces the result. The child reacts but does NOT self-report. This preserves the tally surprise.

**Beat 2 framing.** In-device: *"I'll describe something that might happen. You predict what {entity} does — and we'll see if you're right!"* Out-of-device: *"You're a {role_title}! Here's your hypothesis: {hypothesis}. Let's go gather evidence!"* The frame makes the child's prediction the center of gravity.

**Beat 3 interaction.** In-device: **AI describes a scenario → child COMMITS a prediction → AI reveals the outcome with drama and tallies the score.** Out-of-device: **child photographs a candidate → AI assesses the hypothesis-relevant property from the photo → announces result → updates the tally.** The child is always committed before the reveal; the reveal always comes from the AI.

**Beat 4 closing.** The magic moment is the **tally reveal**. In-device: "You got N out of M! + surprise bonus round." Out-of-device: the AI tallies the data against the hypothesis and delivers the verdict — "Metal: 2, Not metal: 3 — your prediction was SURPRISING!" A chart flips from hidden to visible; the child sees the full evidence set resolved at once.

**Axis affinity.** Discovery naturally anchors on **Causation** (predicting effects from causes) and **Function** (testing how things work). See `docs/progression_axes.md` — Causation §"Why is it like this?".

**Gold-standard examples.**
- `designs/cat1/goldfish_cat1_gold_prod.md` — prediction_lab, scenario-prediction loop.
- `designs/cat1/property_predictor_property_gold_prod.md` — property_predictor, property-gold.
- `designs/cat5/material_lab_property_gold_prod.md` — field_experiment, material hypothesis.
- `designs/cat5/old_vs_new_property_gold_prod.md` — field_experiment, property-gold.
- `designs/cat5/playground_cat5_gold_prod.md` — field_experiment on a playground.

---

## Overlay: Adventure

**Game mechanic.** The {entity} is the **traveler**, and the activity is a **journey** — through time (past/present/future) in-device, or across a quest criterion in an outdoor environment out-of-device. Each round is a stop on the journey. The AI offers **choice points** that branch the story; the child decides the path.

**Payoff pattern.** The magic moment is the **assembled journey map** — a visible sequence of all stops, all finds, all decisions, rendered together as a narrative the child co-authored. The child feels *"look how far we traveled."* The agency is in the choices along the way.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{time_periods}` *(in-device)* / `{quest_criterion}` *(out-of-device)* | Journey stops (past, present, future, or other narrative arc) in-device, or the specific criterion the child hunts for out-of-device ("things that used to be alive", "things that change with the wind"). |
| `{choice_points}` *(in-device)* / `{detail_harvesting}` *(out-of-device)* | Where the story branches based on the child's choice, or the per-find question that harvests a narrative detail ("what does it remind you of?"). |
| `{timeline_visualization}` *(in-device)* / `{quest_narrative}` *(out-of-device)* | How the journey is displayed at the end — a timeline, a map, a scroll of scenes; or the woven quest story that stitches every find into a coherent narrative. |

**Beat 2 framing.** In-device: *"We're going to travel through time with your {entity}. Ready to jump?"* Out-of-device: *"You're a {role_title}! Your quest — find things that {quest_criterion}."* The frame foregrounds movement and choice, not identification.

**Beat 3 interaction.** In-device: **AI describes the time period → child imagines → AI offers CHOICE POINT → child decides path → AI narrates consequences.** Out-of-device: **child finds item → AI evaluates against quest criterion → harvests a naming detail → weaves item into the running story.** Escalation: round 1 is a short hop, round 3 is far away or decisive.

**Beat 4 closing.** The magic moment is the **journey reveal**. In-device: a timeline assembles showing all stops the child chose — "look how far we traveled!" Out-of-device: the child co-creates the quest story with the AI, each find now a character or landmark — *"the rough bark was the old wizard, the smooth pebble was the river, the fuzzy feather was the wind"* — and the AI narrates the complete adventure back.

**Axis affinity.** Adventure naturally anchors on **Change** (time journeys, transformations) and **Connection** (weaving items into a single quest narrative). See `docs/progression_axes.md` — Change and Connection sections.

**Gold-standard examples.**
- `designs/cat1/banana_cat1_gold_prod.md` — time_traveler, through-time in-device.
- `designs/cat1/time_shifter_property_gold_prod.md` — time_shifter, property-gold.
- `designs/cat5/dandelion_cat5_gold_prod.md` — quest_collector, wind quest with characterization.
- `designs/cat5/movers_quest_property_gold_prod.md` — quest_collector, property-gold.
- `designs/cat5/color_scout_property_gold_prod.md` — quest_collector, color criterion.

---

## Overlay: Nurture

**Game mechanic.** The {entity} (or the collection of finds) **needs help**. The AI names a need — physical at first (dry, broken), then emotional (lonely, scared) — and the child proposes **care solutions**. The AI narrates **visible transformation** as the entity recovers. Out-of-device, rescued items help **each other** in a mutual-aid finale.

**Payoff pattern.** The magic moment is the **transformed entity expressing gratitude** — by round 3, the entity calls the child by name (in-device), or the rescued items form a little community of mutual support (out-of-device). The child feels *"I helped, and it worked."* Relationship deepens turn by turn.

**Creative variables (pillar-specific).**

| Variable | Description |
| --- | --- |
| `{needs_escalation}` *(in-device)* / `{needs_per_item}` *(out-of-device)* | Need progression — physical → emotional → complex — per round in-device, or the need the AI identifies per collected item out-of-device (dry, broken, lonely, cold). |
| `{transformation_arc}` *(in-device)* / `{care_solutions}` *(out-of-device)* | How the entity visibly improves per solution (in-device: colors return, shape straightens, voice brightens), or the care actions the child proposes per find. |
| `{relationship_deepening}` *(in-device)* / `{mutual_aid_synthesis}` *(out-of-device)* | How gratitude grows — by round 3 the entity calls the child by name in-device; out-of-device, how rescued items help one another at synthesis. |

**Beat 2 framing.** In-device: *"Your {entity} needs help! I'll tell you what's wrong, you figure out how to help."* Out-of-device: *"You're a {role_title}! Your mission — find things that need your help."* The frame makes clear the child is the helper; the AI is the narrator of need and transformation.

**Beat 3 interaction.** In-device: **AI describes a need → child proposes a solution → AI narrates VISIBLE TRANSFORMATION as the entity recovers.** Out-of-device: **child finds item → AI identifies its need → child proposes care → AI shows the item responding.** Escalation: round 1 physical need, round 2 emotional, round 3 complex or relational. By round 3 the relationship has depth: the entity remembers earlier solutions, or the rescued items acknowledge each other.

**Beat 4 closing.** The magic moment is **full recovery + gratitude**. In-device: the entity is visibly whole, calls the child by name, expresses deep thanks. Out-of-device: the rescued items help each other — the wet thing shelters under the dry thing, the lonely thing finds the warm thing — and the AI narrates their mutual care as the synthesis.

**Axis affinity.** Nurture naturally anchors on **Responsibility** (what should we do, how do we care) and **Perspective** (imagining how the entity feels). See `docs/progression_axes.md` — Responsibility §"What should we do?".

**Gold-standard examples.**
- `designs/cat1/teddy_bear_cat1_gold_prod.md` — care_station on a stuffed animal.
- `designs/cat1/fix_it_station_property_gold_prod.md` — care_station, property-gold.
- `designs/cat5/flower_cat5_gold_prod.md` — rescue_team on outdoor finds.
- `designs/cat5/living_rescue_property_gold_prod.md` — rescue_team, property-gold.

---

## Appendix: Category modifiers

Category modifiers are small overrides on top of Template 0. Each modifier fills exactly 8 fields and inherits everything else. Only **Cat1** and **Cat5** are live today; Cat2–Cat6 will follow the same shape.

| Dimension | Cat1 — In-Device (sustained verbal) | Cat5 — Out-of-Device (collection / tracking) |
| --- | --- | --- |
| `beat_medium` | `verbal_dialogue` — AI ↔ child voice/text exchange, no additional camera use | `photo_collection + physical` — child moves through a space and photographs finds |
| `round_count` | 3–5 rounds in the core loop (beat 3) | 3–4 photo-taking rounds in the exploration step |
| `camera_use` | Initial photo only — no additional photos after launch | Initial photo + 2–3 additional photos during collection |
| `setting` | Indoor, quiet — sofa, table, floor; minimal distraction | Outdoor — park, yard, playground, nature trail, or a large indoor space with findable variety |
| `step_count` | 5 steps (Bridge → Setup & Demo → Core Loop → Payoff → Celebration) | 5–6 steps (Bridge → Mission Briefing → Exploration → Synthesis → Discovery Celebration → Closing) |
| `core_mechanic` | `scenario → verbal → validate` — AI presents pillar scenario, child responds verbally, AI validates with pillar-specific game element | `mission → find → synthesize` — AI frames collection mission, child explores and photographs, AI reacts per find, child synthesizes the set |
| `anchor_priority` | **Engagement-first** — primary anchor = emotions / imagination / narrative / reasoning; secondary = relationship; physical ground = appearance / senses / function | **Physical-first** — primary anchor = appearance (drives the visual feature children hunt for); secondary = structure / senses; engagement ground = relationship / reasoning (drives synthesis) |
| `checklist_extras` | Verify: (a) magic moment is present in Step 4, (b) blind reader can identify the pillar, (c) role title is specific to what the child DOES, (d) metaphor isn't generic | Verify: (a) visual feature is 4–6 year old observable, (b) collection criterion is broad enough for 3+ finds but specific enough to feel like a mission, (c) stuck hint names REAL, SPECIFIC places to look, (d) reflective question has no single correct answer |

**How the three layers compose.** A concrete example: `lion + Cat1 + Performance + T0`.

1. **Template 0 supplies** the 5-beat spine, the 4 universal creative variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`), the tag-block shape, and the T0 tier dial (onomatopoeia, 3–5 word sentences, `caregiver_role: [scaffold]`).
2. **Performance overlay supplies** the stage framing for beat 2, the challenge-perform-react loop for beat 3, the standing-ovation magic moment for beat 4, and the three pillar-specific variables (`{challenges}`, `{audience_character}`, `{twist_challenge}`).
3. **Cat1 modifier supplies** `verbal_dialogue` medium, 3–5 rounds, initial-photo-only, indoor quiet setting, 5 steps, `scenario → verbal → validate` mechanic, engagement-first anchoring, and the Cat1 checklist extras.

The agent then fills `{role_title}` (e.g. "Roar Reporter"), `{metaphor}` (e.g. "jungle talent show"), the three Performance-specific slots, expands each beat to full program.md dialogue, and emits the tag block.

---

## How the agent uses these templates

1. **Pick the pillar** from the entity + mood signal (see Quick Entity Brainstorm Guide below, `entity_guidance.md`, and the mapping). Pillar is usually given by the assignment.
2. **Read the Template 0 reference** (above + `docs/template_0_preview.html` §03) to internalize the 5-beat spine, universal creative variables, and tag-block shape.
3. **Apply the pillar overlay** — the relevant `## Overlay: {Pillar}` section above. It defines beats 2, 3, and 4, plus the pillar-specific creative variables.
4. **Apply the category modifier** from the appendix — pull the 8 fields that specialize for Cat1 or Cat5 (beat medium, round count, camera use, setting, step count, core mechanic, anchor priority, checklist extras).
5. **Fill all `{slots}`** with entity-specific content. Universal variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`) first, then pillar-specific (`{hidden_details}`, `{modifications}`, `{quest_criterion}`, etc.).
6. **Expand each beat to full dialogue** — complete AI lines, 3 child response branches (ideal / unexpected / silence), screen descriptions — per `program.md` format.
7. **Emit the tag block** per `program.md` §1.9 — run the self-check before output.
8. **Run the 10-dimension rubric** (D1–D10) as normal, and the pillar-specific and category-specific adaptation checks from the appendix's `checklist_extras`.

---

## Quick entity brainstorm guide

The same entity can be designed under different pillars — the pillar determines the emotional shape, not the entity. Use this table for inspiration, then invent something FRESH.

### How the same entity works across pillars

| Entity | Pillar | Style | Metaphor Direction | Role Title Direction |
| --- | --- | --- | --- | --- |
| Teddy bear | Nurture | `care_station` | "Teddy needs bedtime help" | "Bedtime Helper" |
| Teddy bear | Mystery | `mystery_lens` | "What's teddy hiding?" | "Teddy Detective" |
| Teddy bear | Creation | `inventor_workshop` | "Super Teddy modifications" | "Teddy Engineer" |
| Lion | Performance | `voice_stage` | "Jungle talent show" | "Roar Reporter" |
| Lion | Discovery | `prediction_lab` | "What will the lion do?" | "Lion Scientist" |
| Dandelion | Adventure | `quest_collector` | "Find things that transform" | "Wish Puff Scout" |
| Dandelion | Discovery | `field_experiment` | "Are most seeds fluffy?" | "Seed Scientist" |
| Playground | Discovery | `field_experiment` | "Test playground hypothesis" | "Playground Researcher" |
| Playground | Creation | `mix_lab` | "Combine equipment powers" | "Playground Inventor" |

### Entity type brainstorm by pillar

| Entity Type | Natural Pillars | Why It Fits |
| --- | --- | --- |
| Stuffed animals / toys | Nurture, Performance, Mystery | Rich emotional affordances — easy to care for, perform as, or investigate |
| Food items | Adventure, Discovery, Creation | Natural life journeys, cause-effect transformations, combinable properties |
| Vehicles (toy) | Adventure, Discovery | Destinations and time jumps; predict what happens on the route |
| Household objects | Mystery, Creation, Nurture | Hidden lives to investigate, mashup potential, "help it" scenarios |
| Animals (real or toy) | Performance, Discovery, Nurture | Expressive characters, observable behaviors to predict, care relationships |
| Nature items (outdoor) | All pillars (Cat5) | Visually rich, findable, varied — work for any collection mission |

---

## Revnote

- **v1.1 · 2026-04-20** · Note the new required tag-block field `entity_attributes_covered` in the Template 0 reference section. Authors must populate it in every activity; valid IDs are sourced from the entity YAML's `tier_guidance`. Full contract lives in `program.md` §1.9 and `docs/template_0_preview.html` §04.
- **v1.0 · 2026-04-20** · Refactor to Template 0 reference + 6 pillar overlays + Cat1/Cat5 category-modifier appendix (Option B, single file). Replaces the v0.x Template A / Template B dual-template structure. Template 0 skeleton authority now lives in `docs/template_0_preview.html` §03 / §04 / §06; this file owns the pillar overlays and the category modifiers. Creative variables stay per-overlay because they are genuinely pillar-specific (`{hidden_details}` is Mystery-only, `{modifications}` is Creation-only, etc.).
