# Templates

> **Version**: 1.11 | **Date**: 2026-05-27
> **Owns**: the mechanic adapters, pillar-overlay contents (Mystery, Creation, Performance, Discovery, Adventure, Nurture), and the Cat1 / Cat3 / Cat5 category modifier appendix.
> **Does NOT own**: the migrated five-file package layout, the tag block schema, asset requirement rows, or the tier defaults — those live in `activities/README.md`, `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`, and `program.md` Phase 0 / §1.9.
> **Consumed by**: `program.md` Phase 5 (template-reading flow), `run.md` (activity package loop), `docs/progression_axes.md` (cross-ref from axis → pillar affinity), generated `prod.md` runtime outputs, and legacy `designs/cat{1,5}/*.md` references.

> **v1.7 — 2026-05-10**: Clarify enrichment mode. Existing migrated packages may be updated to the current template expansion floor without changing their mechanic, pillar/style, tag-block identity, or runtime package contract.
> **v1.8 — 2026-05-11**: Make independent reviewer-agent quality review part of the package acceptance gate for generated and enriched packages.
> **v1.9 — 2026-05-12**: Add Cat3 material-exploration modifier for product-contract override runs, and require reusable concept-led packages to expose extensibility slots such as `{runtime_entity}`, `{shared_feature}`, or approved asset-set IDs.
> **v1.11 — 2026-05-27**: Reference optional demo export extensions. Templates still own scaffolding only; demo support gates and asset manifests live in `activities/README.md`, `program.md`, and `run.md`.
> **v1.10 — 2026-05-21**: Add source-promise alignment as a layer above templates. Mechanic adapters, category modifiers, and pillar/style scaffolds must preserve the original source play frame unless product approval is recorded.

---

## How templates work

An activity design is built by composing four activity layers, plus source-promise and optional asset dependency layers supplied by Phase 0:

0. **Source-promise alignment** — the original play frame, child role, interaction sequence, required child actions, non-negotiable elements, allowed V1 adaptations, and product dependencies. This layer controls over normalized category/mechanic shorthand when they conflict. Templates can shape the experience, but they cannot invert a profession-first activity into scenario matching, a story-first unlock into a door-choice game, or a photo-collection concept into in-device-only play without product approval.

1. **Template 0** — the category-agnostic skeleton. It defines the 5-beat spine (Transition Bridge → Frame & Role → Core Loop → Magic Moment → Celebration), the universal creative variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`), and the three tier dials (T0 / T1 / T2). The migrated output contract lives in `program.md` §1.9 and `activities/README.md`.
2. **Mechanic adapter** — one of the twelve `activity_signature.mechanic` adapters below. It defines what the child actually does in the repeated loop. This is the primary action label, but it does not replace the source-promise layer. If the mechanic token is right but the child role or sequence changes, the package still needs repair or product approval.
3. **Category modifier** — Cat1 (in-device, sustained verbal), Cat3 (out-of-device material exploration), or Cat5 (out-of-device collection/tracking), drawn from the appendix at the bottom of this file. Category modifiers are small — 8 fields (beat medium, round count, camera use, setting, step count, core mechanic, anchor priority, checklist extras). They set the physical frame for the mechanic.
4. **Pillar/style scaffold** — one of the six overlays below (Mystery / Creation / Performance / Discovery / Adventure / Nurture) and its compatible style. It provides emotional payoff, metaphor flavor, and magic-moment shape. If no pillar/style cleanly fits, choose the least misleading scaffold only when the mechanic remains intact; otherwise block generation per `program.md` Phase 0.

The optional **asset dependency layer** is not a template layer and must not change the mechanic. It declares whether the scaffold may reference prebuilt cards, AI-generated images, line art, icons, overlays, or reference pictures. Asset requirements come from `adaptation_brief.asset_dependency` and are documented in `spec.md` `## Asset Brief`; demo-targeted packages also mirror the runtime asset contract in optional `asset_manifest.yaml`. `prod.md` references asset IDs and fallback behavior only.

The layers compose like this:

```text
Source Promise
+ Template 0 spine
+ Mechanic Adapter
+ Category Modifier
+ Optional Pillar/Style scaffold
+ Optional Asset Dependency references
= activity scaffold
```

The agent then fills the `{slots}` and expands each beat to full `program.md` format. The migrated five-file package may be more compact than older legacy specs, but template expansion must not become thin or generic: every beat needs enough concrete dialogue, branch reaction, screen state, and payoff detail for the runtime prompt composer to run it without inventing missing behavior.

**Why Option B (one file).** Mechanics, pillar creative variables (like `{hidden_details}`, `{modifications}`, `{quest_criterion}`), and category modifiers all influence the executable scaffold. Keeping them together avoids split-file drift while still making the mechanic layer the first-class child-action contract.

---

## Template 0 reference

Template 0 is the invariant 5-beat spine that every activity shares. The canonical YAML skeleton is in `docs/template_0_preview.html` §03 — do not re-derive or copy it into designs. Instead, assume every design inherits the spine and read the preview once to internalize the shape.

Compressed spine for quick reference (authoritative version lives in the preview):

```
beat_1_transition_bridge  — emotional hook; photo → imaginative reaction; NEVER knowledge-test
beat_2_frame_and_role     — assign {role_title} + {metaphor}; state the mission    ← mechanic + scaffold drive
beat_3_core_loop          — N rounds of the canonical mechanic; escalates on {escalation_axis} ← mechanic adapter drives
beat_4_magic_moment       — synthesis / payoff; the emotional climax               ← scaffold/pillar flavors
beat_5_celebration        — name earned Key Concepts + Related Concepts as praise
```

The mechanic adapter owns the repeated child action in **beat 3**. The pillar/style scaffold flavors **beats 2, 3, and 4** only after the mechanic is set. Beats 1 and 5 are universal — same shape for every mechanic and pillar.

**Universal creative variables** (all pillars inherit these from §02 of the Template 0 skeleton):

| Variable | Description |
| --- | --- |
| `{metaphor}` | The imaginative frame that turns the activity into play. Pillar-flavored but pillar-agnostic in name. |
| `{role_title}` | The badge the child earns. Verb-forward, specific to what they DO. |
| `{escalation_axis}` | How rounds get progressively richer. Rides `progression.topic_axis` from the tag block. |
| `{reflective_question}` | The closing "why" that invites genuine wondering — no single correct answer. |

Every pillar overlay layers 2–3 pillar-specific variables on top of these four (see each overlay below).

---

## Mechanic adapters

Mechanic adapters define the child-action loop independent of pillar. Use the adapter matching `activity_signature.mechanic` and Phase 0 `canonical_mechanic`; then apply category and pillar/style scaffolding around it. If an activity concept cannot be expressed by one of these adapters without changing the child action, mark it with `readiness: blocked_until_product_decision`, draft a constrained design preview, or recommend a vocabulary/template extension.

| Mechanic | Core loop | Notes |
| --- | --- | --- |
| `enumerate` | notice/identify/count/measure → AI confirms/extends → next attribute/part | Use for naming visible parts, counting obvious features, measuring relative quantity/size, or listing attributes. Avoid OCR/text-reading and unreliable photo counting. |
| `compare` | inspect A/B → child states same/different/preference/evidence → AI names contrast | The compared angle must still be a concrete `observation_angle` such as color, size, material, quantity, or state. |
| `collect` | criterion → child finds/matches/pairs/photos → AI reacts → set synthesis | Best for Cat5 and parameterized property bridges. Criterion must be broad enough for 3+ finds and V1-visible when AI assesses photos. |
| `sort` | rule or child-made rule → group/rank/sequence items → explain organizing logic | Use when the child's action is categorizing, sequencing, ranking, or arranging. If the rule is child-invented, AI validates and helps name it rather than correcting. |
| `deduce` | clue/evidence → child infers/guesses → child justifies → AI reveals or gives next clue | Use for mystery, Guess-in-10, hidden detail, and evidence-based inference. Always include soft hints when the child is stuck. |
| `build` | material/idea prompt → child creates/assembles/transforms/experiments → AI adds/combines | In Cat1/Cat5 this is imaginative or collection-combination build. Physical material builds use Cat3 only when the product contract covers caregiver setup, material pacing, and honest completion evidence. |
| `predict` | commit guess/hypothesis/plan → reveal/result/action → tally or consequence | Preserve commit-before-reveal. Out-of-device hypotheses must use V1-visible properties. Planning is valid only when the later action/result can be represented honestly. |
| `decide` | options appear → child chooses/corrects → AI applies consequence or explains correction | Use for branching choices, decision points, correction games, or "which one should we use?" loops. If the decision requires a complex UI state, declare the product dependency. |
| `remember` | encode/show/hear → delay or distract → child recalls/repeats/retells → AI confirms and extends | Use for memory, recall, repetition, retell, and "what did we see before?" loops. Keep recall age-appropriate and avoid testing pressure. |
| `imagine` | story/pretend setup → child adds choice/detail/roleplay/retell → AI weaves or summarizes | Use for story chains, journey planning, pretend play, roleplay, retelling, and recap-style co-narration. Pre-authored branching may be required for quality. |
| `care` | need or feeling appears → child proposes help → AI shows gratitude/impact | Use for empathy, responsibility, rescue, and repair metaphors. Avoid before/after state-change verification; impact can be narrated or self-reported. |
| `motion_voice` | motion/sound/role prompt → child moves, imitates, or speaks in role → AI reacts as audience/partner | ASR captures words only and cannot verify motion/audio quality. For motion-heavy prompts, use caregiver-safe, low-risk actions and do not claim sensor verification. |

**Mechanic adapter self-check.** Before writing runtime dialogue, verify: (a) Step 3's repeated child action matches the adapter, (b) `tag_block.yaml activity_signature.mechanic` uses the same mechanic, (c) the selected pillar/style does not replace the adapter loop with a different action, and (d) unsupported source/product needs are never hidden in valid package dialogue. For blocked assignments, continue drafting the run-local constrained design preview, but annotate the unsupported runtime elements inline with `BLOCKED ELEMENT` comments and keep the preview out of valid package directories until the constraint is resolved. For demo export, a package can remain a valid activity while `demo_support.status: unsupported` honestly tells consumers the current Cat1/Cat5 UI cannot play it.

**Tag block.** Every migrated activity package emits `<package_dir>/tag_block.yaml`. Fresh runs use `runs/<run_id>/activity_packages/<activity_id>/`; canonical packages use `activities/<activity_id>/`. The authoritative shape and field semantics live in `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`, and `program.md` §1.9. This file does not duplicate the tag-block schema.

**Package output.** Templates provide the creative scaffold only. The agent must still expand the scaffold into the five required migrated files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`. When a run requests direct demo export, which full `GOAL.md` generation does by default, the package also includes `demo_support.yaml` and `asset_manifest.yaml` per `program.md` and `activities/README.md`; templates do not own those schemas. `prod.md` keeps all runtime rounds fully expanded; `spec.md` carries the self-evaluation scorecard and, when applicable, `## Asset Brief`; the YAML files carry machine-readable metadata and recap/dashboard payloads. A package that is structurally valid but under-detailed still fails the template contract. Generated packages are not accepted until a separate reviewer agent passes the files or all reviewer issues are repaired and re-reviewed. When enriching an existing package, keep its mechanic, pillar/style, `activity_id`, tag block, recap/dashboard payload shape, and asset IDs stable; add the missing scaffold expansion detail rather than redesigning the activity, and record reviewer-agent evidence in the run notes.

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

Category modifiers are small overrides on top of Template 0. Each modifier fills exactly 8 fields and inherits everything else. **Cat1**, **Cat3**, and **Cat5** are live today. Cat2, Cat4, and Cat6 will follow the same shape later.

| Dimension | Cat1 — In-Device (sustained verbal) | Cat3 — Out-of-Device (material exploration) | Cat5 — Out-of-Device (collection / tracking) |
| --- | --- | --- | --- |
| `beat_medium` | `verbal_dialogue` — AI ↔ child voice/text exchange, no additional camera use | `guided_material_action + self_report` — child uses safe materials while AI paces and records self-reported progress | `photo_collection + physical` — child moves through a space and photographs finds |
| `round_count` | 3–5 rounds in the core loop (beat 3) | 3 concrete making/arranging/drawing rounds in the core loop | 3–4 photo-taking rounds in the exploration step |
| `camera_use` | Initial photo only — no additional photos after launch | Initial photo optional; final photo/self-report only when contract allows honest completion evidence | Initial photo + 2–3 additional photos during collection |
| `setting` | Indoor, quiet — sofa, table, floor; minimal distraction | Indoor table/floor with caregiver-approved safe materials and cleanup boundary | Outdoor — park, yard, playground, nature trail, or a large indoor space with findable variety |
| `step_count` | 5 steps (Bridge → Setup & Demo → Core Loop → Payoff → Celebration) | 5 steps (Bridge → Materials & Safety → Make Loop → Share/Inspect → Celebration) | 5–6 steps (Bridge → Mission Briefing → Exploration → Synthesis → Discovery Celebration → Closing) |
| `category_frame` | `scenario → verbal → validate` — AI presents a mechanic-specific scenario, child responds verbally, AI validates through the chosen mechanic | `setup → make → self-report/share` — AI defines safe materials and small actions, child creates, AI reflects without claiming unsupported verification | `mission → find → synthesize` — AI frames a physical mission, child explores and photographs, AI reacts per find, child synthesizes the set |
| `anchor_priority` | **Engagement-first** — primary anchor = emotions / imagination / narrative / reasoning; secondary = relationship; physical ground = appearance / senses / function | **Material-first** — primary anchor = hand action / material property / safety boundary; secondary = child intention; evidence ground = self-report or allowed photo | **Physical-first** — primary anchor = appearance (drives the visual feature children hunt for); secondary = structure / senses; engagement ground = relationship / reasoning (drives synthesis) |
| `checklist_extras` | Verify: (a) magic moment is present in Step 4, (b) blind reader can identify the pillar, (c) role title is specific to what the child DOES, (d) metaphor isn't generic | Verify: (a) material setup is caregiver-safe, (b) every action is small and age-appropriate, (c) completion evidence is self-reported or contract-supported, (d) cleanup/stop branch exists | Verify: (a) visual feature is 4–6 year old observable, (b) collection criterion is broad enough for 3+ finds but specific enough to feel like a mission, (c) stuck hint names REAL, SPECIFIC places to look, (d) reflective question has no single correct answer |

**How the layers compose.** A concrete example: `lion + Cat1 + Performance + T0`.

1. **Template 0 supplies** the 5-beat spine, the 4 universal creative variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`), and the T0 tier dial (onomatopoeia, 3–5 word sentences, `caregiver_role: [scaffold]`).
2. **`motion_voice` mechanic adapter supplies** the repeated child action: role or motion prompt → child speaks, imitates, or moves as the entity → AI reacts as audience/partner.
3. **Cat1 modifier supplies** `verbal_dialogue` medium, 3–5 rounds, initial-photo-only, indoor quiet setting, 5 steps, engagement-first anchoring, and the Cat1 checklist extras.
4. **Performance / `voice_stage` scaffold supplies** the stage framing for beat 2, audience flavor around the `motion_voice` loop, standing-ovation magic moment for beat 4, and the three pillar-specific variables (`{challenges}`, `{audience_character}`, `{twist_challenge}`).

The agent then fills `{role_title}` (e.g. "Roar Reporter"), `{metaphor}` (e.g. "jungle talent show"), the three Performance-specific slots, expands each beat to full `program.md` dialogue, and emits the five-file activity package.

---

## How the agent uses these templates

1. **Run Phase 0** from `program.md` when the assignment is concept-led or lacks a full entity + category request. This produces `canonical_mechanic`, input mode, readiness, and scaffold fit.
2. **Pick the mechanic adapter** from `activity_signature.mechanic` / `canonical_mechanic`. This is the primary child-action layer.
3. **Read the Template 0 reference** (above + `docs/template_0_preview.html` §03) to internalize the 5-beat spine, universal creative variables, and package shape.
4. **Apply the category modifier** from the appendix — pull the 8 fields that specialize for Cat1, Cat3, or Cat5 (beat medium, round count, camera use, setting, step count, category frame, anchor priority, checklist extras).
5. **Pick the pillar/style scaffold** only after the mechanic and category are fixed. Use the overlay that best supports the mechanic's emotional payoff; if scaffold fit is weak, disclose it in `spec.md` or block per Phase 0.
6. **Fill all `{slots}`** with entity- or source-specific content. Universal variables (`{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`) first, then mechanic-specific loop details, then pillar-specific flavor (`{hidden_details}`, `{modifications}`, `{quest_criterion}`, etc.).
7. **Expand each beat to full dialogue** — complete AI lines, 3 child response branches (ideal / unexpected / silence), follow-up branches, and screen descriptions — per `program.md` format. This applies to bridge, framing, magic moment, and closing beats too, not only the core loop.
8. **Do not condense runtime rounds** — every round in generated `prod.md` must be executable on its own, not a summary of a pattern. Rounds should be distinct in objective, child action, follow-up, and screen-state change.
9. **Record extensibility** for concept-led and parameterized packages. `spec.md` should name reusable slots and whether another entity, shared feature, matched property, or approved asset set can replace the current one without changing the mechanic.
10. **Emit the five required files** per `program.md` §1.9 and `activities/README.md`; if direct demo export is requested, which full `GOAL.md` generation does by default, also emit `demo_support.yaml` and `asset_manifest.yaml` and run the focused demo contract validator.
11. **Run the 10-dimension rubric** (D1–D10), especially game feel and mechanic fidelity + scaffold honesty, and the category-specific adaptation checks from the appendix's `checklist_extras`. Repair packages that feel like a sparse template fill even if every required section exists.

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

- **v1.7 · 2026-05-10** · Add enrichment-mode guidance for existing migrated packages: keep identity and machine-readable contracts stable while adding missing scaffold expansion detail.
- **v1.6 · 2026-05-09** · Tighten migrated package expansion standards: compact five-file packages are acceptable, but structurally valid thin packages fail; every beat needs executable detail, and every core-loop round needs distinct action, reaction, and screen progression.
- **v1.3 · 2026-05-08** · Add the mechanic adapter layer between Template 0 and pillar/style scaffolds. Mechanics now define the primary child-action loop; pillar/style provides emotional payoff only after mechanic and category are fixed.
- **v1.3 · 2026-05-12** · Clarify that fresh run packages live under `runs/<run_id>/activity_packages/<activity_id>/` while canonical packages live under `activities/<activity_id>/`.
- **v1.2 · 2026-05-08** · Align template consumption with the migrated five-file package. Templates now explicitly forbid condensed runtime rounds and defer tag-block shape to `activities/_schema/tag_block.schema.json`.
- **v1.1 · 2026-04-20** · Legacy inline-design note for `entity_attributes_covered`; superseded for migrated packages by v1.2 and `activities/_schema/tag_block.schema.json`.
- **v1.0 · 2026-04-20** · Refactor to Template 0 reference + 6 pillar overlays + Cat1/Cat5 category-modifier appendix (Option B, single file). Replaces the v0.x Template A / Template B dual-template structure. Template 0 skeleton authority now lives in `docs/template_0_preview.html` §03 / §04 / §06; this file owns the pillar overlays and the category modifiers. Creative variables stay per-overlay because they are genuinely pillar-specific (`{hidden_details}` is Mystery-only, `{modifications}` is Creation-only, etc.).
