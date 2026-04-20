# Author Training Guide

> **Version**: 0.1 | **Date**: 2026-04-20
> **Owns**: the end-to-end walkthrough a new author (or a fine-tuned model) follows to turn an `entity × category × pillar × tier` input into a structurally valid, fully-tagged WonderLens activity design.
> **Does NOT own**: the 5-beat spine (→ `docs/template_0_preview.html` §03 `#skeleton`), the pillar-overlay content (→ `templates.md`), the axis enum (→ `docs/progression_axes.md`), or the tag-block schema (→ `program.md` §1.9 and `docs/template_0_preview.html` §04 `#tags`).
> **Consumed by**: human authors on their first design pass, fine-tuned generation agents that need an in-context walkthrough, and reviewers who want a checklist to audit a finished design against.

---

## Who this guide is for

You are either a first-time human author staring at a fresh `entity × category × pillar × tier` assignment, or you are a generation agent being fine-tuned on what a good WonderLens activity looks like. Either way, the promise of this guide is simple: read it end-to-end once, then you can produce a structurally correct, fully-tagged activity without cross-consulting `templates.md` or `program.md` directly. You will still want those docs open as references during revision, but the first draft should not require them — every load-bearing quote lives inline in one of the three worked examples below.

This guide is explicitly **not** a spec. `docs/template_0_preview.html` is the spec. `templates.md` is the overlay catalog. `program.md` is the rubric and the tag-block contract. This guide stitches those together into a generative workflow and demonstrates it three times.

---

## The stack you're writing against

Every activity you generate is a cake of four layers, composed top-down at design time:

```
┌────────────────────────────────────────────────────────────────────┐
│ 1. Template 0 skeleton                                             │
│    → docs/template_0_preview.html §03 #skeleton                    │
│    → 5-beat spine + universal creative variables + tag-block shape │
│                                                                    │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │ 2. Pillar overlay                                            │ │
│   │    → templates.md §Overlay: {Mystery|Creation|Performance|   │ │
│   │       Discovery|Adventure|Nurture}                           │ │
│   │    → specializes beats 2, 3, 4; adds 3 pillar variables      │ │
│   │                                                              │ │
│   │   ┌────────────────────────────────────────────────────────┐ │ │
│   │   │ 3. Category modifier                                   │ │ │
│   │   │    → templates.md §Appendix (Cat1 vs Cat5)             │ │ │
│   │   │    → 8 fields: beat medium, round count, camera use,   │ │ │
│   │   │       setting, step count, core mechanic, anchor       │ │ │
│   │   │       priority, checklist extras                       │ │ │
│   │   │                                                        │ │ │
│   │   │   ┌──────────────────────────────────────────────────┐ │ │ │
│   │   │   │ 4. Tier dial                                     │ │ │ │
│   │   │   │    → docs/template_0_preview.html §06 #tiers     │ │ │ │
│   │   │   │    → AI role · language · task depth · concept   │ │ │ │
│   │   │   │       focus · caregiver role                     │ │ │ │
│   │   │   └──────────────────────────────────────────────────┘ │ │ │
│   │   │                                                        │ │ │
│   │   │   + Progression axis × L1/L2/L3                        │ │ │
│   │   │   → docs/progression_axes.md                           │ │ │
│   │   └────────────────────────────────────────────────────────┘ │ │
│   └──────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘

What you emit: the filled tag block (program.md §1.9) + the full
program.md-formatted dialogue. Downstream consumers read the tag block:
 • docs/child_recap_preview.html §04 — 6 fields → child-facing recap
 • docs/parent_growth_path_preview.html §03 + §07 — tag block → dashboard
```

The order matters. You always read the skeleton first (what beats are there?), then specialize (what does my pillar do to beats 2/3/4?), then categorize (am I in-device or out-of-device, and how many rounds?), then tune for age (tier dial), then pick where on the axis ladder the child is climbing. Only after those five reads do you start writing dialogue.

---

## The 10-dimension rubric (quick reference)

Every activity, before it is shipped, must PASS all ten dimensions below. These are copied straight from `program.md` Phase 3 (Self-Evaluation Rubric) so you can self-check without re-opening the spec. A single FAIL means the design is not ready.

| # | Dimension | Gate question |
|---|-----------|---------------|
| 1 | V1 Technical Compliance | No OCR, no face/pose/IMU detection, no before/after state comparison via CV, no non-speech audio detection. Multi-photo workflows are allowed; computed-diff between photos is not. |
| 2 | Hook & Transition | Step 1 opens with emotional resonance, not knowledge testing. The activity grows from that opening; a reader could remove the "step" labels and it would still feel conversational. |
| 3 | Edge Case Coverage | Every AI step has three child-response branches (ideal / unexpected / no response). "Unexpected" validates before redirecting. "No response" names a specific wait time and a gentle prompt. Cat5 designs also need a "can't find the item" branch. |
| 4 | IB Completeness | 1–2 Key Concepts named; 2–4 Related Concepts listed; full KUD; 2–3 ATL skills with sub-skills; closing speech names the Key Concepts as praise, not as a quiz. |
| 5 | Tier Appropriateness | T0 = ≤5-word sentences, onomatopoeia, single-step, call-and-response, ≤2 rounds. T1 = 5–8-word sentences, 2–3 step tasks, open-ended questions. T2 = complex sentences, multi-step planning, negotiation. Vocabulary and task complexity match the tier. |
| 6 | Dialogue Specificity | Every AI line is actual concrete dialogue — no "AI encourages" or "AI guides the child". Every line has a tone/emotion marker in parentheses. |
| 7 | Screen & UI Completeness | Every step has a concrete "Screen:" description. Animations and visual effects are specific ("confetti rain with gold glitter"), not generic ("animation plays"). |
| 8 | Entity Mapping Alignment (mapping-informed designs only) | Key Concepts sourced from mapping's primary/secondary; at least 2 Related Concepts from `candidate_related_concepts`; vocabulary and sensory details traceable to `tier_guidance`; anchor dimensions used in core content. Skip if no mapping. |
| 9 | Game Feel | The child experiences genuine uncertainty; the outcome is unknown before it's revealed; there is a clear emotional climax (the magic moment); there is at least one moment of surprise, drama, or delight beyond warm encouragement. |
| 10 | Pillar Fidelity | A blind reader could identify the pillar from the interaction alone. The magic moment matches the pillar's defined payoff. The core loop uses the pillar's specific game mechanic (not generic Q&A). Re-labeling to a different pillar would feel wrong. |

After the 10 dimensions, also run the **tag-block pre-output self-check** from `program.md` §1.9: every required field populated, no placeholders, enums valid, `progression.*` concrete. Both gates must pass before emit.

---

## Worked example 1 — Ladybug × Cat1 × Mystery × T1

The running example. This is the same ladybug your colleagues have been staring at in `docs/template_0_preview.html` §06 and `docs/parent_growth_path_preview.html` §03. Use it to anchor the whole workflow; the next two examples vary the knobs.

### Input

- `entity`: ladybug (a real bug, photographed on a leaf or finger)
- `category`: Cat1 — sustained verbal interaction, in-device
- `pillar`: Mystery
- `tier`: T1 (ages 4–6)

### Step 1 — Read the Template 0 skeleton

Template 0 gives you five beats, two of which are universal (Beat 1 and Beat 5) and three of which the pillar overlay will fill (Beats 2, 3, 4). Pulled from `docs/template_0_preview.html` §03 `#skeleton`:

- **Beat 1 — Transition Bridge.** Photo → emotional/imaginative reaction. Never a knowledge test.
- **Beat 2 — Frame & Role.** Assign `{role_title}` + `{metaphor}`. State the mission. *(← Mystery overlay drives.)*
- **Beat 3 — Core Loop.** N rounds of the pillar mechanic, escalating along `{escalation_axis}`. *(← Mystery overlay drives.)*
- **Beat 4 — Magic Moment.** Pillar-specific synthesis; the emotional climax. *(← Mystery overlay drives.)*
- **Beat 5 — Celebration.** Name earned Key Concepts + Related Concepts as praise.

You also inherit four **universal creative variables** (Template 0 §02):

- `{metaphor}` — the imaginative frame (a detective case, a magic workshop, a jungle talent show).
- `{role_title}` — a verb-forward badge ("Ladybug Detective", not "Bug Expert").
- `{escalation_axis}` — the axis the rounds climb (must equal `progression.topic_axis` in the tag block).
- `{reflective_question}` — the closing "why" with no single correct answer.

### Step 2 — Apply the Mystery overlay

Pulled directly from `templates.md` §Overlay: Mystery:

> **Game mechanic.** The AI hides something — a feature of the photographed entity — and feeds the child progressive clues (visual, textural, functional, imaginative). The child guesses, narrows, and ultimately uncovers the hidden thing.
>
> **Payoff pattern.** *"I figured it out!"* — the moment the hidden detail snaps into place. The AI stages a deliberate reveal (dramatic pause, zoom-in, sparkle) so the shift feels like an event.
>
> **Beat 2 framing (in-device).** *"I'm going to think of something hidden in your photo. I'll give you clues — you tell me when you figure it out."* Role title is specific (Detective, Scout, Codebreaker), never generic.
>
> **Beat 3 interaction.** Per-round loop is **clue → guess → confirm/redirect**. AI gives one clue, child proposes a match, AI responds with "warmer / colder" language. Each round's clue targets a different detail.
>
> **Beat 4 closing.** The **reveal**. AI announces the full hidden detail with a visual flourish and celebrates *"You figured it out!"*.

Three pillar-specific creative variables I need to fill for ladybug:

- `{hidden_details}` — 3–5 specific features I'll surface through clues. For a ladybug: *red elytra, black spots, six tiny legs, antennae, ability to play dead when threatened*.
- `{clue_types}` — the rotation of clue modes. I'll use **visual** (color/shape), **functional** (what the feature does), and **imaginative** (what it reminds you of) — mixing keeps the loop fresh.
- `{reveal_drama}` — how each reveal is dramatized. I'll use a zoom-in + sparkle pulse and a "You figured it out!" banner at Beat 4.

### Step 3 — Apply the Cat1 category modifier

Pulled from `templates.md` §Appendix, the Cat1 column:

| Dimension | Cat1 value (ladybug × Mystery × T1 application) |
|---|---|
| `beat_medium` | `verbal_dialogue` — AI ↔ child voice/text exchange, no extra camera use |
| `round_count` | 3–5 rounds in the core loop — I'll pick **3** rounds (T1 sweet spot) |
| `camera_use` | initial photo of the ladybug only; no further photos |
| `setting` | indoor, quiet — couch, table, floor |
| `step_count` | 5 steps (Bridge → Setup & Demo → Core Loop → Payoff → Celebration) |
| `core_mechanic` | `scenario → verbal → validate` — AI presents a clue (scenario), child responds (verbal), AI validates with a warmer/colder cue |
| `anchor_priority` | **engagement-first** — primary anchor is imagination + reasoning; physical ground is appearance + function |
| `checklist_extras` | (a) magic moment present in Step 4; (b) blind reader can identify Mystery; (c) role title names what the child DOES; (d) metaphor isn't generic |

### Step 4 — Apply the T1 tier dial

Pulled from `docs/template_0_preview.html` §06 `#tiers`, the T1 panel:

- **AI role.** Curious co-explorer + thought starter. Wondering alongside the child, not directing.
- **Language.** Natural pace, complete sentences + simple compounds, open-ended "why/how". Sentences are 5–8 words on average; allowed to grow to 10–12 when the thought genuinely needs it.
- **Task depth.** 2–3 step sequences. "First notice, then guess, then check."
- **Concept focus.** Causation, change, connection — bridging concrete to concept.
- **Caregiver role.** Scaffold + co-explorer (roughly equal). Steps in when the child stalls; otherwise shares what they notice.

Concretely for ladybug: I'll avoid T0 onomatopoeia ("RRRR! Red!") and avoid T2 hedges ("78% of birds in a peer-reviewed study…"). The voice is *"Look at the tiny legs — how many are there?"* — curious, open, compound sentences.

### Step 5 — Pick a progression axis and L level

The ladybug has a salient visual profile (red body, black spots) and an obvious question behind the spots: *why are they there?* That's **Form** progression — from noticing attributes toward explaining why the attribute exists.

From `docs/progression_axes.md` §Form:

- **L1 Notice** — name one dominant attribute.
- **L2 Extend** — name multiple attributes and locate each on a specific part.
- **L3 Reason** — explain why the attribute exists.

T1 sits comfortably at **L2** for this entity — the child can name three things (red body, black spots, tiny legs) and place each on a part of the ladybug. L3 (the "spots warn predators" reasoning) is reachable at T1 but is more typically the T2 move. So:

- `progression.topic_axis: form`
- `progression.difficulty_level: 2`
- `{escalation_axis}`: Form — each round asks for a deeper notice-and-locate move.

Detection cues I'll lean on (from `docs/progression_axes.md` §Form):

- Verbs: *notice, spot, compare, describe*.
- Question patterns: *"What do you see on its back?"*, *"Where is that on its body?"*.

### Step 6 — Fill the slots

Universal variables, concrete:

- `{metaphor}` = "a tiny mystery case" — the ladybug is hiding clues about itself.
- `{role_title}` = "Ladybug Detective" — verb-forward; "detective" names what the child *does*.
- `{escalation_axis}` = Form (climbing from attribute → attribute-with-location → attribute-with-significance).
- `{reflective_question}` = *"Why do you think a bug would want to be so red?"*

Mystery-specific variables:

- `{hidden_details}` = [red elytra · black spots · six tiny legs · pair of tiny antennae · "playing dead" defense]
- `{clue_types}` = visual → functional → imaginative (one per round)
- `{reveal_drama}` = zoom-in pulse with a sparkle trail + a "You figured it out!" banner

Now the full program.md-format dialogue (abbreviated to the load-bearing beats):

**Beat 1 — Transition Bridge**

> **AI says:** *(curious, a little hushed)* "Whoa — look at this tiny bug! Red back, little dots, six tiny legs… it looks like it's wearing a costume. What do you notice first?"
>
> **Child responses:**
> 1. (Ideal) "The spots!" / "It's red!" / "It has legs!"
> 2. (Unexpected) "It moved!" / "I touched one once."
> 3. (No response) Child watches the photo.
>
> **AI follow-up:**
> 1. *(warm, matching)* "Great eye — the spots popped out for me too. I bet this little bug has secrets, and the clues are on its body. Want to be my detective partner?"
> 2. *(validating)* "They really do move fast! That's another clue to file away. Want to investigate together?"
> 3. *(wait 2s, gentle)* "Tiny, right? I think there are three or four hidden things on this bug. Want to hunt them with me?"
>
> **Screen:** Ladybug photo centered on a cream background with a soft magnifying-glass icon hovering in the corner; subtle sparkle animation over the red back.

**Beat 2 — Frame & Role**

> **AI says:** *(playful, conspiratorial)* "Okay, Ladybug Detective — here's the case. This ladybug has three hidden things on its body, and I'm going to give you clues one at a time. Your job: listen to the clue, look at the photo, and tell me what you think it is. Ready?"
>
> **Child responses:**
> 1. (Ideal) "Yes!" / "I'm ready, detective!" / "Go!"
> 2. (Unexpected) "Is this a real ladybug?" / "I want to hold one."
> 3. (No response) Child looks at the screen.
>
> **AI follow-up:**
> 1. *(excited)* "Detective on the case! Clue one, coming up."
> 2. *(warm)* "It's a real ladybug! Real bugs have real clues to find. Shall we start with clue one?"
> 3. *(wait 2s)* *(softer)* "No pressure — I'll give the clue, you look at the photo. Clue one?"
>
> **Screen:** "CASE FILE #01" banner in navy serif across the top; ladybug photo framed as evidence; "Ladybug Detective" badge slides in bottom-left.

**Beat 3 — Core Loop (3 rounds)**

**Round 1 — visual clue (attribute)**

> **AI says:** *(detective voice)* "Clue one — I'm thinking of a hidden thing, and the clue is… it's a *bright color*, and it covers almost the whole body. What do you think it is?"
>
> **Child responses:**
> 1. (Ideal) "The red back!" / "It's red!"
> 2. (Unexpected) "The eyes are black!" / "I see yellow." (child points at a different area)
> 3. (No response) Child stays quiet.
>
> **AI follow-up:**
> 1. *(warmer! ding)* "Warmer — *warmest* — YES, the big red back! Case file, clue one solved."
> 2. *(validating, redirecting)* "Good spotting on the eyes — those are tiny though. The clue said it covers almost the whole body. Can you find a bigger red area?"
> 3. *(wait 2s, gentle)* "Look at the whole bug — which part is the biggest color?"
>
> **Screen:** Zoom-in pulse on the red elytra; "Clue 1: bright color · SOLVED" line slides in with a tiny sparkle.

**Round 2 — functional clue (part-role)**

> **AI says:** *(detective voice)* "Clue two — I'm thinking of something on the ladybug that helps it *walk*. If a ladybug didn't have these, it would be stuck. What do you think it is?"
>
> **Child responses:**
> 1. (Ideal) "The legs!" / "Its tiny legs!"
> 2. (Unexpected) "Wings!" / "The back."
> 3. (No response) Child is thinking or silent.
>
> **AI follow-up:**
> 1. *(delighted)* "Warmer — yes! Six tiny legs. You can count them under the red back. Another clue solved."
> 2. *(validating)* "Wings help with flying, that's true — but this clue is about walking. Look at the bottom of the bug — see the tiny moving parts?"
> 3. *(wait 2s)* *(softer)* "Let me zoom in on the bottom. See those six little lines sticking out? Those help with walking."
>
> **Screen:** Zoom-in on the legs; six small dots light up one by one with a counting animation; "Clue 2: walking helpers · SOLVED" line.

**Round 3 — imaginative clue (significance)**

> **AI says:** *(detective, warmer still)* "Clue three — this is the *strangest* one. I'm thinking of something that covers the whole back and looks like a *warning sign*. If a bird looked at it, the bird would think 'uh-oh'. What do you think it is?"
>
> **Child responses:**
> 1. (Ideal) "The red!" / "The spots!" / "The red AND the spots!"
> 2. (Unexpected) "Like a stop sign?" / "It looks scary to a bird?"
> 3. (No response) Child is stuck.
>
> **AI follow-up:**
> 1. *(warm reveal)* "Warmest! You figured it out — the red *and* the spots. Together they tell the bird 'don't eat me'. That's the hidden message on a ladybug's back."
> 2. *(cheering)* "Exactly — like a stop sign. Red says stop, spots say I'm different. Together they're a warning sign. You cracked it, Detective!"
> 3. *(wait 2s, gentle)* "Think about what a bird sees when it looks at a ladybug: *red* and *spots*. Together… they might mean 'danger, skip this one'."
>
> **Screen:** Full ladybug photo outlined in a glowing red halo; the words "WARNING SIGNAL" fade in over the back; three clue rows below, all checked.

**Beat 4 — Magic Moment (Reveal)**

> **AI says:** *(big reveal voice)* "Case closed, Detective. The three hidden things on this ladybug: a *bright red back*, *six tiny legs*, and a *warning message* made of red + spots together. You figured it out — every single clue. You see the whole bug differently now, don't you?"
>
> **Child responses:**
> 1. (Ideal) "Yeah!" / "I want more clues!" / "I'm a detective!"
> 2. (Unexpected) "Why do birds not like red?" / "I see a spot you missed!"
> 3. (No response) Child smiles or watches.
>
> **AI follow-up:**
> 1. *(celebrating)* "You are the Ladybug Detective of the day."
> 2. *(curious with them)* "That's an amazing question — most red bugs taste bad, so birds learned to skip them. And if you see a spot I missed, tell me — detectives help each other."
> 3. *(wait 2s)* *(warm)* "That smile tells me the case really is closed."
>
> **Screen:** Three solved clue rows lock into a "CASE FILE · SOLVED" banner; a golden "Ladybug Detective" badge lands with a soft chime; sparkle flourish over the red back.

**Beat 5 — Celebration + Concepts**

> **AI says:** *(warm, reflective)* "One bug, three hidden things, and you noticed every single one — the red back, the tiny legs, and the warning message. You looked at the ladybug and really *saw* it. That's called Form — paying attention to what something looks like and what each part is telling us. Ladybug Detective, case closed."
>
> **Child responses:**
> 1. (Ideal) "Yay! / "Next case!" / "I'm a detective!"
> 2. (Unexpected) "What's another bug like this?" / "Are bees the same?"
> 3. (No response) Child watches the badge animation.
>
> **AI follow-up:**
> 1. *(joyful)* "The jungle has many more cases. Today you solved the ladybug's. Great work, Detective!"
> 2. *(curious with them)* "Ooh — bees have their own warning message too, black and yellow stripes. That could be our next case."
> 3. *(wait 2s, warm)* "Badge earned. Ladybug Detective, any time."
>
> **Screen:** Full-screen celebration — "Ladybug Detective" badge at center, three small chips ("Observation", "Reasoning", "Discovery") arc underneath, ladybug photo in a golden frame.

### Step 7 — Emit the tag block

```yaml
# Tag block — ladybug × Cat1 × Mystery × T1
activity_id: ladybug_cat1_mystery_t1
entity: ladybug
entity_type: animal
category: cat1
pillar: mystery
style: mystery_lens
tier: T1
tier_variants: [T2]
role_title: "Ladybug Detective"
highlight_moment: "I figured out the ladybug's warning message — red plus spots."

attributes: [red, round, spotted, small, six-legged]
related_concepts: [Observation, Reasoning, Signals, Discovery]

key_concepts: [Form, Causation]
atl_skills: [observation, critical_thinking, expressing]
transdisciplinary_theme: "How the world works"
subject_tags: [science, language]

kud:
  know:
    - "Ladybugs have a red back (elytra), black spots, six legs, and antennae."
    - "The red color + spots together act as a warning signal to predators."
    - "A clue is a small hint that helps you figure out something hidden."
  understand:
    - "Every part of a living thing has a form you can notice, name, and reason about."
    - "Colors and patterns can carry a message in nature."
  do:
    - "Notice and name multiple features of an entity and locate each on its body."
    - "Turn a single clue into a guess, then check it against the photo."
    - "Reason from attribute to purpose ('why might it be that color?')."

progression:
  topic_axis: form
  difficulty_level: 2
  next_step_hint: "Move to Form L3 — ask why the red warns predators, then try another spotted bug."
  reward_hook: "Ladybug Detective badge"

caregiver_role: [scaffold, co-explorer]
pillar_payoff: "Child names the hidden warning-signal message after three clue rounds — the classic Mystery 'I figured it out!' reveal."
```

### Step 8 — Self-check against the 10-dimension rubric

| # | Dimension | Score | Why |
|---|-----------|-------|-----|
| 1 | V1 Technical Compliance | PASS | Verbal-only interaction; initial photo only; no OCR, no face/pose, no IMU, no before/after diff, no non-speech audio. |
| 2 | Hook & Transition | PASS | Beat 1 opens with "Whoa — look at this tiny bug!" — emotional, not a quiz. The detective frame grows naturally from that emotional spark. |
| 3 | Edge Case Coverage | PASS | Every AI step shows ideal / unexpected / no-response branches, each with a specific wait time and a validation-before-redirect for the unexpected branch. |
| 4 | IB Completeness | PASS | 2 Key Concepts (Form, Causation), 4 Related Concepts, full KUD, 3 ATL skills, closing names Form as praise. |
| 5 | Tier Appropriateness | PASS | Sentences mostly 5–8 words ("What do you notice first?"); no T0 onomatopoeia; no T2 statistics. Open-ended "what do you think" questions; 2–3 step task (listen → guess → check). |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete, with a parenthesized tone cue (*curious, detective voice, delighted*). No "AI encourages" instructions. |
| 7 | Screen & UI Completeness | PASS | Every beat has a concrete Screen description — zoom-in pulse, sparkle, counting animation, golden badge. |
| 8 | Entity Mapping Alignment | N/A | No `mapping=` parameter on this assignment. |
| 9 | Game Feel | PASS | Genuine uncertainty on each clue; the "warning signal" reveal is an emotional climax; the detective frame gives replay appetite. |
| 10 | Pillar Fidelity | PASS | Blind reader would peg this as Mystery — clue → guess → reveal loop, "I figured it out!" payoff, zoom-in sparkle at Beat 4. Re-labeling to Creation or Performance would feel wrong. |

Tag-block pre-output self-check (from `program.md` §1.9): all required fields populated, no placeholders, enums valid (`form` is in the 7-axis enum; `L2` is a valid rung; `cat1`, `mystery`, `mystery_lens`, `T1` are all valid values; `caregiver_role` matches T1 default `[scaffold, co-explorer]`). ✓

### Step 9 — Downstream rendering notes

**Child recap** (`docs/child_recap_preview.html` §04 `#contract`) reads six fields from the tag block and renders:

- `role_title` → "Ladybug Detective" as the badge title (serif hero on the recap screen).
- `pillar` → "Mystery · solved" subtitle under the title.
- `highlight_moment` → *"I figured out the ladybug's warning message — red plus spots."* as the large serif pull-quote.
- `related_concepts` → "You earned" chip row: [Observation · Reasoning · Signals · Discovery].
- `atl_skills` → "You practiced" chip row: [observation → "noticing" · critical_thinking → "thinking hard" · expressing → "using words"].
- `attributes` → not shown directly; feeds the `highlight_moment` generator (§05).

Everything else in the tag block — `key_concepts`, `progression.*`, `transdisciplinary_theme`, `subject_tags` — is explicitly NOT rendered on the child recap. That is parent-facing data.

**Parent dashboard** (`docs/parent_growth_path_preview.html` §03 `#curiosity` + §07 `#contract`) reads the full tag block. Specific modules:

- **Curiosity profile** (§03 radial) adds one tick to the **Form** lobe at L2-depth. The caption rule would mention the child as an *observer* / *attribute-namer* (the Form personality word from `docs/progression_axes.md`).
- **Progress (L×T ladder)** (§07) places this activity at `topic_axis: form · difficulty_level: 2 · tier: T1`, and the "Try at home" module points at the `next_step_hint` ("Move to Form L3 — ask why the red warns predators").
- **In their words** (§04) can lift `highlight_moment` as a quote card: *"I figured out the ladybug's warning message — red plus spots."* — attributed with Tuesday / ladybug context.
- **IB framework chips** (§07) render `key_concepts: [Form, Causation]`, `atl_skills`, `transdisciplinary_theme: "How the world works"`, `subject_tags: [science, language]`.
- **Gauges** (§07) reads `caregiver_role: [scaffold, co-explorer]` — the T1 shared-role gauge lights up.
- **Explicitly NOT rendered** on the parent dashboard: `role_title` (child-facing identity only).

---

## Worked example 2 — Sunflower × Cat5 × Discovery × T0

The sunflower runs the child outside to collect items against a hypothesis. T0 means the language is very simple — 3–5 word sentences, onomatopoeia welcome. Cat5 means we're out-of-device. Discovery means the child **commits to a prediction first, then the AI runs the trial** — not hidden-vs-revealed, but guess-vs-outcome.

### Input

- `entity`: sunflower (growing in a yard, pot, or garden the child can actually walk around)
- `category`: Cat5 — out-of-device collection/tracking
- `pillar`: Discovery
- `tier`: T0 (ages 2–4)

### Step 1 — Read the Template 0 skeleton

Same 5 beats, but the Cat5 modifier expands Step 3 into an "Exploration" substep with physical movement, and Beat 4's synthesis uses the collection, not a verbal reveal.

- Beat 1 reacts to the sunflower photo with onomatopoeia ("Whoa! Sunny!").
- Beat 2 frames the mission with a badge: "you are a Flower Scientist".
- Beat 3 is the **outdoor exploration** — 3 photo-rounds (Cat5 round count).
- Beat 4 is the **tally reveal** — Discovery's payoff.
- Beat 5 names Discovery + Causation as praise.

### Step 2 — Apply the Discovery overlay

From `templates.md` §Overlay: Discovery, with the out-of-device branch:

> **Game mechanic.** The child commits to a prediction before exploring, then the AI runs the trial by assessing photographed finds against the hypothesis.
>
> **Payoff pattern.** *"Was I right?!"* The AI's job is to preserve the surprise — the AI (not the child) assesses each find, so the running tally isn't self-reported.
>
> **Beat 2 framing (out-of-device).** *"You're a {role_title}! Here's your hypothesis: {hypothesis}. Let's go gather evidence!"*
>
> **Beat 3 interaction.** Child photographs a candidate → AI assesses the hypothesis-relevant property → announces the result → updates the tally.
>
> **Beat 4 closing.** The AI tallies the data and delivers the verdict — "Yellow: 2, Not yellow: 2 — your prediction was SURPRISING!" A chart flips from hidden to visible.

Load-bearing **out-of-device hypothesis constraint** (also from §Overlay: Discovery):

- **Allowed properties**: color, shape, material type, size, count, alive/not-alive, category (natural/man-made), position.
- **Banned properties**: texture, weight, temperature, sound, smell, taste, flexibility — none are verifiable from a photo.
- **AI-as-assessor rule**: the AI identifies the property from the photo; the child reacts but does not self-report.

Discovery variables I need to fill:

- `{hypothesis}` — one testable question, verifiable from photo. For T0 around a sunflower: ***"Most flowers outside are yellow like this one?"*** Color is a valid property; "most" is a kid-legible aggregate.
- `{data_property}` — the property the AI assesses per find = **color (yellow or not yellow)**.
- `{tally_result}` — the final count chart, flipped at the end.

### Step 3 — Apply the Cat5 category modifier

From `templates.md` §Appendix, Cat5 column:

| Dimension | Cat5 value (sunflower × Discovery × T0 application) |
|---|---|
| `beat_medium` | `photo_collection + physical` — child walks around and photographs finds |
| `round_count` | 3–4 photo-taking rounds — I'll use **3** (T0 fatigue limit) |
| `camera_use` | initial sunflower photo + 3 additional during collection |
| `setting` | outdoor — yard, garden, park (a place with several flowers) |
| `step_count` | 5–6 steps (Bridge → Mission Briefing → Exploration → Synthesis → Discovery Celebration → Closing) |
| `core_mechanic` | `mission → find → synthesize` — AI frames the mission, child explores & photographs, AI reacts per find, the set is synthesized |
| `anchor_priority` | **physical-first** — primary anchor is **appearance** (yellow or not), drives the visual hunt; synthesis reads as relationship/reasoning |
| `checklist_extras` | (a) visual feature is 4–6 year old observable (color = yes); (b) collection criterion is broad enough for 3+ finds but specific enough to feel like a mission; (c) stuck hint names REAL places to look; (d) reflective question has no single correct answer |

### Step 4 — Apply the T0 tier dial

From `docs/template_0_preview.html` §06 `#tiers`, T0 panel:

- **AI role.** Enthusiastic game initiator + emotional co-regulator. Warm, anthropomorphized, exclaims with the child.
- **Language.** Onomatopoeia, reduplication, 3–5 word sentences, slow and exaggerated. Example: *"Woof woof! Red! Big red ladybug!"*.
- **Task depth.** Single-step commands, immediate feedback. *"Find one yellow!"*
- **Concept focus.** Concrete attributes — color, shape — and basic function.
- **Caregiver role.** **Scaffold** (sole role). The caregiver echoes the AI's words and holds attention with the child.

This locks tone hard. Sentences must be short. I will say **"Yellow? Yes! Point, snap!"** not *"Let's gather evidence to test whether the majority of flowers in this garden share the yellow coloration of our sunflower."* Cat5 also means the caregiver physically helps the child walk and take photos — that matches T0's sole-scaffold role.

### Step 5 — Pick a progression axis and L level

For this T0 sunflower hunt, the child is committing to a prediction about **color**, then gathering evidence and learning the result. That is a **Causation** move at its simplest — predict-then-check, cause-and-effect-lite.

From `docs/progression_axes.md` §Causation:

- **L1 Notice** — describe what happened. "The flower closed up." / "It's yellow."
- **L2 Extend** — predict what will happen next. "If I bring it to the sun, it will open."
- **L3 Reason** — explain the mechanism.

At T0, the child commits to *"yes, most are yellow"* before going out — that's a prediction, which sits at **L1**: the child is *noticing and naming an outcome* in the simplest possible form. (T1+ versions of this same design would climb to L2 with a richer prediction like "most in my garden will be yellow because the sunflower is".)

- `progression.topic_axis: causation`
- `progression.difficulty_level: 1`
- `{escalation_axis}`: each round adds one more data point against the prediction — escalation is accumulation, not cognitive leap.

### Step 6 — Fill the slots

Universal variables:

- `{metaphor}` = "a color hunt across the garden" — concrete and visual.
- `{role_title}` = "Flower Scientist" — verb-forward; "scientist" names the predict-then-check action.
- `{escalation_axis}` = Causation (predict → gather → resolve).
- `{reflective_question}` = *"Did you see more yellow or not yellow?"* — no single correct answer depending on what they actually find.

Discovery-specific:

- `{hypothesis}` = "Most flowers here are yellow!" (the child commits to this before going out)
- `{data_property}` = color → yellow / not yellow
- `{tally_result}` = the big chart at Beat 4, flipped from hidden to visible

Dialogue (T0 — short, exclaim, repeat):

**Beat 1 — Transition Bridge**

> **AI says:** *(delighted gasp)* "Whoaaa! Big yellow flower! Sunny sunny! Yellow yellow! So pretty!"
>
> **Child responses:**
> 1. (Ideal) "Yellow!" / "Sunny!" / "Flower!"
> 2. (Unexpected) "Bee!" / "I touched it."
> 3. (No response) Child looks at the flower.
>
> **AI follow-up:**
> 1. *(thrilled)* "Yellow! Yes yes! Big yellow!"
> 2. *(warm)* "Bee? Bees love yellow! Let's look!"
> 3. *(wait 2s)* *(soft, inviting)* "So yellow! Let's look more!"
>
> **Screen:** Sunflower photo centered, soft yellow glow, sparkle ring around the petals, cartoon sun peeking in the corner.

**Beat 2 — Mission Briefing**

> **AI says:** *(excited, official)* "You — Flower Scientist! Big mission! Guess first: are MOST flowers out here yellow? Yes or no?"
>
> **Child responses:**
> 1. (Ideal) "Yes!" / "All yellow!" / "Yellow yellow!"
> 2. (Unexpected) "Pink!" / "My mom's flowers are pink."
> 3. (No response) Child hesitates.
>
> **AI follow-up (the child's guess is now the hypothesis):**
> 1. *(thrilled, recording)* "YES! Guess is YELLOW wins! Let's check! Go go go!"
> 2. *(warm, recording)* "Pink? Good guess! Let's see — is it yellow or pink more? Go find three!"
> 3. *(wait 2s)* *(gentle)* "Take a guess — yellow most? Or not yellow most? Say one!"
>
> **Screen:** "FLOWER SCIENTIST" mission card, a "my guess: YELLOW WINS" badge in kid-block lettering, a yellow-vs-not-yellow chart that starts empty with 3 slots.

**Beat 3 — Exploration (3 rounds)**

**Round 1 — first find**

> **AI says:** *(excited)* "Mission on! Find one flower! Any flower! Snap a photo!"
>
> **Child responses:**
> 1. (Ideal) Child walks and photographs a flower.
> 2. (Unexpected) Child photographs a leaf or a toy, not a flower.
> 3. (Can't find) Child looks around uncertainly.
>
> **AI follow-up (assessor rule — AI names the color):**
> 1a. *(child's photo is yellow)* *(cheering)* "YELLOW! Point one for yellow team! Chart up!"
> 1b. *(child's photo is not yellow — e.g., pink rose)* *(surprised)* "Ooooh! PINK! Not yellow! Point one for not-yellow team!"
> 2. *(validating, redirecting)* "Pretty leaf! But we need a *flower* — something with petals. Try again!"
> 3. *(wait 3s)* *(helpful)* "Look near the ground! Or the fence! Flowers hide!"
>
> **Screen:** Live photo slot fills with the child's find; a yellow chip (or pink chip) pops onto the chart with a "+1" animation.

**Round 2 — second find**

> **AI says:** *(excited detective)* "Next! Find ANOTHER flower! Different place! Snap!"
>
> **Child responses:**
> 1. (Ideal) Child walks to a new spot and photographs.
> 2. (Unexpected) Child photographs the same flower twice.
> 3. (Can't find) Child stops.
>
> **AI follow-up:**
> 1a. *(if yellow)* "YELLOW again! Two yellows! Zooooom!"
> 1b. *(if not yellow)* "Purple! Ooooh! Not yellow! Chart grows!"
> 2. *(warm)* "Same flower? Clever! But let's find a NEW one for this scientist's chart."
> 3. *(wait 3s)* "Try the other side! Or look up! Flowers in pots too!"
>
> **Screen:** Chart updates with the second chip; tiny cheer animation; "2 of 3" counter ticks.

**Round 3 — last find**

> **AI says:** *(suspense voice)* "Last one! Number three! The BIG one! Snap!"
>
> **Child responses:**
> 1. (Ideal) Child photographs a third flower.
> 2. (Unexpected) Child photographs two at once.
> 3. (Can't find) Child gives up.
>
> **AI follow-up:**
> 1a. *(if yellow)* "YELLOW! Three of three! Wait wait — the chart will tell the whole story!"
> 1b. *(if not yellow — say blue or red)* "Ohhh! RED! Big surprise coming!"
> 2. *(delighted)* "TWO at once! Two scientist points! Amazing!"
> 3. *(wait 3s)* *(gently)* "One more, any flower. Even a dandelion!"
>
> **Screen:** Chart now has three chips; a big "WHICH WINS?" question mark pulses at the top.

**Beat 4 — Synthesis / Tally Reveal**

> **AI says:** *(drum roll)* "Okay okay okay — Flower Scientist — big reveal! Your guess: YELLOW WINS! Let's flip the chart! Three… two… one… LOOK!"
>
> **(Screen flips — showing the real counts based on what was photographed.)**
>
> *If YELLOW wins (e.g., 2 yellow, 1 pink):* **AI says:** *(cheering)* "Yellow: two! Pink: one! YOU WERE RIGHT! Scientist badge!"
> *If NOT-YELLOW wins (e.g., 1 yellow, 2 others):* **AI says:** *(amazed)* "Yellow: one! Other colors: two! OOOOH surprise! Guess was wrong! But finding a surprise IS a scientist win!"
> *If tied (1.5/1.5 — impossible with 3, but just in case of a duplicate photo):* **AI says:** *(delighted)* "Half-and-half! Wow! That's a DRAW!"
>
> **Child responses:**
> 1. (Ideal) Cheers, claps, repeats the result.
> 2. (Unexpected) "Again!" / "More flowers!"
> 3. (No response) Child stares at the chart.
>
> **AI follow-up:**
> 1. *(pure celebration)* "Big scientist! Chart says WOW!"
> 2. *(thrilled)* "More? Yes yes! We can hunt again next time!"
> 3. *(wait 2s, warm)* "Look! Chart is done! You did it!"
>
> **Screen:** Chart flips from question marks to real chips in a big "reveal" animation; confetti if prediction right, "SURPRISE!" starburst if wrong; Flower Scientist badge descends.

**Beat 5 — Closing + Concepts**

> **AI says:** *(warm, proud)* "You — Flower Scientist. You guessed! You hunted! You found! Sometimes yellow wins, sometimes SURPRISE! That's Discovery! You checked if something was TRUE! That's Causation — what IS and what is NOT! Good scientist! Good hunt!"
>
> **Child responses:**
> 1. (Ideal) "Scientist!" / "Yay!" / "Again!"
> 2. (Unexpected) "Why is it yellow?" / "Bees!"
> 3. (No response) Child smiles.
>
> **AI follow-up:**
> 1. *(beaming)* "Best scientist! Chart's saved! Badge yours!"
> 2. *(curious with them)* "Bees love yellow! That's WHY! Another hunt, another day!"
> 3. *(wait 2s, warm)* "Big smile! Big badge!"
>
> **Screen:** Flower Scientist badge centered, three yellow-sun chips ("Observation", "Prediction", "Discovery") dance underneath, the final flipped chart in the corner.

### Step 7 — Emit the tag block

```yaml
# Tag block — sunflower × Cat5 × Discovery × T0
activity_id: sunflower_cat5_discovery_t0
entity: sunflower
entity_type: plant
category: cat5
pillar: discovery
style: field_experiment
tier: T0
tier_variants: [T1]
role_title: "Flower Scientist"
highlight_moment: "I guessed yellow, hunted three flowers, and checked the chart."

attributes: [yellow, round, petaled, big, bright]
related_concepts: [Observation, Prediction, Discovery, Color]

key_concepts: [Causation, Form]
atl_skills: [observation, critical_thinking, focus]
transdisciplinary_theme: "How the world works"
subject_tags: [science, language]

kud:
  know:
    - "Sunflowers are yellow and have big round petals with a brown middle."
    - "Not all flowers are yellow — some are pink, red, purple, blue."
    - "A guess you check against real evidence is called a prediction."
  understand:
    - "You can predict something about the world, then find out if you were right."
    - "The result being different from your guess is also a discovery, not a failure."
  do:
    - "Commit to a guess before gathering evidence."
    - "Walk a space and photograph three different examples of one feature."
    - "Read a simple tally chart to see which side 'won'."

progression:
  topic_axis: causation
  difficulty_level: 1
  next_step_hint: "Move to Causation L2 — predict which way the sunflower will turn tomorrow morning."
  reward_hook: "Flower Scientist chip"

caregiver_role: [scaffold]
pillar_payoff: "Child commits to yellow-wins, photographs three flowers outside, and the tally chart flips to reveal whether they were right — Discovery's 'Was I right?!' payoff."
```

### Step 8 — Self-check against the 10-dimension rubric

| # | Dimension | Score | Why |
|---|-----------|-------|-----|
| 1 | V1 Technical Compliance | PASS | Photo collection only; no CV diff between photos; AI's "assessor" step identifies color from a single photo (allowed). No OCR, face, pose, IMU, or audio detection. |
| 2 | Hook & Transition | PASS | Beat 1 gasps "Whoaaa! Big yellow flower!" — emotional, not a quiz. The mission grows from the wonder. |
| 3 | Edge Case Coverage | PASS | Every step has ideal / unexpected / no-response branches, plus a Cat5-specific "can't find" branch with a real-place hint ("near the ground, by the fence, flowers hide"). |
| 4 | IB Completeness | PASS | 2 Key Concepts (Causation, Form), 4 Related Concepts, full KUD, 3 ATL skills, closing names Discovery + Causation as praise. |
| 5 | Tier Appropriateness | PASS | Sentences 3–5 words ("YELLOW! Yes yes!"), onomatopoeia ("Zooooom!", "Whoaaa!"), single-step commands ("Snap!"), max 3 rounds. Caregiver as sole scaffold matches T0. |
| 6 | Dialogue Specificity | PASS | Every AI line has a tone marker (*delighted gasp, excited, drum roll, suspense voice*) and is real dialogue, not instruction. |
| 7 | Screen & UI Completeness | PASS | Every beat has a concrete Screen — sparkle ring, chart with 3 slots, "+1" animations, confetti / starburst depending on outcome. |
| 8 | Entity Mapping Alignment | N/A | No `mapping=` parameter on this assignment. |
| 9 | Game Feel | PASS | Real uncertainty — the child's guess is genuinely on the line; the tally reveal preserves surprise (AI is the assessor); the flip-the-chart moment is an emotional climax. |
| 10 | Pillar Fidelity | PASS | Discovery signature: commit-then-check; AI-as-assessor; the "Was I right?!" payoff at chart flip. Blind reader would peg this as Discovery over Mystery (no hidden thing) or Adventure (no journey). |

Tag-block self-check: all required fields populated; `causation` is a valid axis enum; `L1` is a valid rung; `cat5`, `discovery`, `field_experiment`, `T0` all valid; `caregiver_role: [scaffold]` matches T0 default. ✓

### Step 9 — Downstream rendering notes

**Child recap** (`docs/child_recap_preview.html` §04 `#contract`):

- `role_title` → "Flower Scientist" as the badge title.
- `pillar` → "Discovery · checked" subtitle.
- `highlight_moment` → *"I guessed yellow, hunted three flowers, and checked the chart."* as the pull-quote.
- `related_concepts` → [Observation · Prediction · Discovery · Color] as "You earned" chips.
- `atl_skills` → "You practiced" chip row: [observation → "noticing" · critical_thinking → "thinking hard" · focus → "sticking with it"].
- `attributes` → feeds the highlight_moment generator.

The child does NOT see `key_concepts`, `progression.*`, `transdisciplinary_theme`, or `subject_tags`.

**Parent dashboard** (`docs/parent_growth_path_preview.html` §03 `#curiosity` + §07 `#contract`):

- **Curiosity profile** ticks the **Causation** lobe at L1-depth. Parent-facing caption would call the child an *investigator* / *explainer* (Causation's personality word in `docs/progression_axes.md`).
- **Progress (L×T ladder)** places this at `topic_axis: causation · difficulty_level: 1 · tier: T0`.
- **Try at home** picks up `next_step_hint` ("Move to Causation L2 — predict which way the sunflower will turn tomorrow morning").
- **In their words** can quote the `highlight_moment`.
- **IB framework chips** render `[Causation, Form]`, `atl_skills`, `"How the world works"`, `[science, language]`.
- **Gauges** reads `caregiver_role: [scaffold]` — the T0 full-scaffold gauge lights up.
- **Explicitly NOT rendered**: `role_title` (child-facing only).

---

## Worked example 3 — Construction paper × Cat1 × Creation × T2

An everyday artifact the child already has a million feelings about. Cat1 brings it indoors with verbal-only interaction. Creation invites wild what-ifs. T2 lets the child negotiate, reason, and drive the design.

### Input

- `entity`: construction paper (a stack of colored sheets the child has already used for crafts)
- `category`: Cat1 — sustained verbal interaction, in-device
- `pillar`: Creation
- `tier`: T2 (ages 6–8)

### Step 1 — Read the Template 0 skeleton

Same 5 beats. At T2 the beats stretch — Beat 3 can hold more rounds (Cat1 allows 3–5; I'll use **4**) and dialogue is richer. Beat 4's magic moment is the "ta-da!" reveal of the combined creation.

### Step 2 — Apply the Creation overlay

From `templates.md` §Overlay: Creation:

> **Game mechanic.** The AI proposes what-if modifications, and the child invents combinations. Each round adds a new modification; the creation grows progressively wilder. The climax is the unveiling of the combined creation — "Super {entity}" — with every modification visibly stacked.
>
> **Payoff pattern.** *"I made this!"* — the child sees their invention revealed as a coherent thing (even if absurd). The AI's role is to elaborate and say yes-and, never to correct.
>
> **Beat 2 framing (in-device).** *"We're going to imagine wild changes to your {entity}. What if it had…? Let's invent!"*
>
> **Beat 3 interaction.** AI proposes what-if → child invents → AI elaborates and yes-ands, adding the modification to a visible running creation. Escalation: round 1 plausible → round 4 delightfully absurd.
>
> **Beat 4 closing.** The ta-da! reveal — AI narrates the assembly of all modifications into one "Super {entity}" and shows it visually.

Pillar variables:

- `{modifications}` — the what-if changes proposed each round. I'll script four: **transparent** (physical, plausible), **self-folding** (mechanism), **memory-keeper** (imaginative — paper remembers who touched it), **shape-shifter on command** (delightfully absurd — paper becomes any shape you name).
- `{combination_name}` = **"Super Construction Paper"** (Creation overlay's default naming pattern).
- `{absurdity_escalation}` = the rounds climb from plausible → impossible-but-delightful.

### Step 3 — Apply the Cat1 category modifier

Same Cat1 8-field block as Example 1, but T2 lets me lean into **4 rounds** (Cat1 allows 3–5) and a more elaborate `scenario → verbal → validate` mechanic: scenarios become richer what-if prompts with follow-up probing.

### Step 4 — Apply the T2 tier dial

From `docs/template_0_preview.html` §06 `#tiers`, T2 panel:

- **AI role.** Project advisor + resource coordinator. Treats the child as a junior researcher/inventor.
- **Language.** Near-adult dialogue, complex syntax, logic markers ("first…then", "if…then"). Example: *"First we'll predict, then we'll test, and if we're surprised we'll investigate why."*
- **Task depth.** Multi-step, optional project tracks, plan → experiment → record.
- **Concept focus.** Perspective, responsibility, systems — abstract + cross-disciplinary.
- **Caregiver role.** Observer · Co-explorer · Scaffold (decreasing weight). Mostly steps back; joins as co-explorer when invited; scaffolds only on direct request.

Concretely: I will use compound sentences with logic markers ("if that works, then what happens when…"), invite negotiation ("you get to pick the name at the end"), and treat the child's inventions as design input, not praise objects. Caregiver sits back unless invited.

### Step 5 — Pick a progression axis and L level

At T2 the child can take on Creation at its most delightful: inventing modifications, voicing how the paper "feels" about being transformed, and imagining a dialogue between paper-versions across time. That is **Perspective** — taking on a role, imagining a non-human point of view.

From `docs/progression_axes.md` §Perspective:

- **L1 Notice** — attribute a simple feeling to the entity.
- **L2 Extend** — imagine the entity's view of you.
- **L3 Reason** — generate dialogue between the entity and a third party.

T2 sits at **L3**: I'll ask the child to voice Super Construction Paper talking to *another piece of paper* ("what would you tell Regular Paper about your new powers?"). That's the most generative rung on the Perspective ladder.

- `progression.topic_axis: perspective`
- `progression.difficulty_level: 3`
- `{escalation_axis}` = Perspective — round 1 the paper has a simple feeling, round 4 the paper narrates itself to another.

This axis choice also lets the activity straddle **Perspective + Change** in `key_concepts` without splitting the progression — the escalation climbs Perspective while Change lives in the `key_concepts` list (per `docs/progression_axes.md` §"Axis interaction — activities that genuinely straddle two axes").

### Step 6 — Fill the slots

Universal:

- `{metaphor}` = "an inventor's workshop for a quiet hero (construction paper)"
- `{role_title}` = "Paper Engineer"
- `{escalation_axis}` = Perspective
- `{reflective_question}` = *"If Super Construction Paper and Regular Paper met, what would they say to each other?"*

Creation:

- `{modifications}` = [transparent · self-folding · memory-keeper · shape-shifter on command]
- `{combination_name}` = "Super Construction Paper"
- `{absurdity_escalation}` = R1 plausible, R2 mechanism, R3 imaginative, R4 delightfully absurd

**Beat 1 — Transition Bridge**

> **AI says:** *(warm, genuinely curious)* "So, that's construction paper — the quiet workhorse of every art project you've ever made. Look at that stack. Every piece has a whole history in it — cutting, folding, gluing. Here's a question to hold onto for a minute: if construction paper could choose to be any kind of paper in the world, what would it want to become?"
>
> **Child responses:**
> 1. (Ideal) "Something that folds itself!" / "Paper that doesn't tear!" / "Shiny paper!"
> 2. (Unexpected) "Why are we talking about paper?" / "I already made a plane."
> 3. (No response) Child thinks, fiddles with the paper.
>
> **AI follow-up:**
> 1. *(delighted, building)* "Okay, save that thought — because we're literally about to build that. You're going to redesign construction paper from the ground up. Four rounds. Sound good?"
> 2. *(warm, validating)* "Fair question. Here's the pitch: you're an engineer, and today's project is designing the ultimate construction paper. If you're into it — let's go."
> 3. *(wait 3s, gentle)* "Take a second. When you're ready, we'll redesign paper together — your ideas, your call."
>
> **Screen:** Stack of construction paper photo on the left; a "workshop blueprint" template on the right with four empty slots labeled R1–R4; a chrome pencil icon hovers over Slot 1.

**Beat 2 — Frame & Role**

> **AI says:** *(inventor voice, collaborative)* "You're officially Paper Engineer today. The workshop has four design rounds, and each round I'll bring you a what-if — a modification to construction paper. Your job: invent how it works, push it as far as you want, and tell me the details. I'll draft everything. At the end, we combine all four into one thing — Super Construction Paper — and you get to decide its final name. Ready for round one?"
>
> **Child responses:**
> 1. (Ideal) "Yes!" / "Let's build!" / "Can I name it 'Mega Paper' already?"
> 2. (Unexpected) "Can I do five rounds instead of four?" / "What if I don't like one of them?"
> 3. (No response) Child is thinking.
>
> **AI follow-up:**
> 1. *(excited)* "Hold the name — save it for the reveal. Round one, coming up."
> 2. *(collaborative)* "Five works — we have time. And if a round doesn't click, we redesign it together. Your call."
> 3. *(wait 3s)* *(warm)* "Take your time. When you're ready, round one is ready."
>
> **Screen:** "Paper Engineer — Workshop Open" banner with blueprint grid; four slot cards labeled R1–R4 with grey pencil icons awaiting fills; bottom toolbar with "draft", "undo", and "combine" buttons (visual only).

**Beat 3 — Core Loop (4 rounds, climbing Perspective)**

**Round 1 — transparent paper (plausible · Perspective-L1, attribute a feeling)**

> **AI says:** *(engineer tone)* "Round one, what-if: construction paper becomes *transparent*. You can see through it. What does that change about how it feels to use? And — here's the Perspective part — if the paper could feel, how does it feel about being see-through?"
>
> **Child responses:**
> 1. (Ideal) "It feels shy because everyone can see through it." / "It feels free — no more hiding drawings!"
> 2. (Unexpected) "Doesn't that just make it like a window?" / "Can I still color on it?"
> 3. (No response) Child considers.
>
> **AI follow-up:**
> 1. *(engaged)* "Shy — or free — those are real design constraints. Let's draft: transparent paper, with that personality noted. What color would it pick to be transparent in?"
> 2. *(collaborative)* "Windows are glass — this is transparent *paper*, which is different. You can still color on it; colors layer through. Does that change what feeling it has?"
> 3. *(wait 3s)* *(gentle)* "No pressure — I'll draft the transparent version and you jump in with how it feels whenever."
>
> **Screen:** R1 slot fills with a translucent paper sketch, slightly tinted by the child's color choice; a small "Feeling: ___" tag sits next to the sketch, editable.

**Round 2 — self-folding (mechanism · Perspective-L2, imagine its view of you)**

> **AI says:** *(engineer voice, building excitement)* "Round two: construction paper *folds itself*. You tell it 'fold into a crane' and it just does. Design question: how does it decide *when* to fold? And perspective question — if the paper could see *you*, what would it think when you ask it to fold?"
>
> **Child responses:**
> 1. (Ideal) "It knows by voice — I say 'crane' and it folds. It thinks I'm a wizard when I tell it!" / "It only folds for its owner, so it feels loyal."
> 2. (Unexpected) "What if I say 'fold' and I didn't mean it?" / "Can it UNfold?"
> 3. (No response) Child thinks.
>
> **AI follow-up:**
> 1. *(delighted)* "Voice-activated. It thinks you're a wizard. Now that's character. Noted — and the paper is starting to have opinions about you. Keep going?"
> 2. *(collaborative)* "Good edge case — maybe it needs a confirmation word, like 'really fold'. And yes, it can unfold; every fold has an undo. What feeling does the paper get when you undo?"
> 3. *(wait 3s)* *(gentle)* "Take your time. The paper will wait."
>
> **Screen:** R2 slot fills with a sketch of paper mid-fold into a crane, motion lines showing self-motion; a thought bubble next to it labeled "Paper thinks: ___", editable.

**Round 3 — memory-keeper (imaginative · Perspective-L2 extended, toward L3)**

> **AI says:** *(warmer, layering)* "Round three — this one's trickier. The paper *remembers*. Every drawing ever made on it, every hand that touched it — stored inside. Design choice: does the paper share those memories, or keep them private? And what does it feel about holding all those stories?"
>
> **Child responses:**
> 1. (Ideal) "It keeps them private unless you ask — like a journal." / "It shares when it's happy, keeps them when it's sad." / "Every memory makes it a little stronger."
> 2. (Unexpected) "That's creepy." / "Does it remember bad drawings?"
> 3. (No response) Child pauses.
>
> **AI follow-up:**
> 1. *(engaged)* "Oh that's great — conditional memory, mood-based. Let me draft: paper with a journal-mode. Does your paper ever want to talk *about* a memory to another paper? Just thinking ahead to round four."
> 2. *(validating, reframing)* "Creepy is real — let's design that out. Maybe the paper has to be asked. And every drawing counts — even the bad ones were practice. How does the paper feel about practice drawings?"
> 3. *(wait 3s)* *(curious)* "Maybe just tell me one memory the paper might hold. Anything at all."
>
> **Screen:** R3 slot fills with paper with a faint shimmer of overlapping sketches inside it; a "memory mode: shared / private / conditional" toggle set to the child's choice.

**Round 4 — shape-shifter on command (delightfully absurd · Perspective-L3, voice the paper to a third party)**

> **AI says:** *(building to the finale)* "Last round — this one's the wildest. Paper *shape-shifts* on command. You say 'be a cat', it becomes a cat. 'Be a hat', it becomes a hat. Anything you name. Now — final perspective question, the biggest one — if Super Construction Paper met *Regular Paper* at the end of today's workshop, what would it tell Regular Paper about itself? In Super Paper's voice."
>
> **Child responses:**
> 1. (Ideal) "Super Paper says: 'I used to be like you. Now I can be anything. But I remember what it was like to just sit in a stack.'" / "'I see through, fold alone, remember everything, and turn into anything — but I miss being quiet sometimes.'"
> 2. (Unexpected) "Isn't that just magic?" / "Can I redo round three?"
> 3. (No response) Child is thinking hard.
>
> **AI follow-up:**
> 1. *(genuine admiration)* "You just gave Super Paper an inner life. It's not just features, it's a whole character. Alright — combining everything in one second. Ready for the reveal?"
> 2. *(collaborative)* "Sure, redesign R3 — we have time. And yes, it's magic, engineered. Engineering magic is what this workshop does."
> 3. *(wait 4s)* *(warm, inviting)* "Try one line in Super Paper's voice. Even a short one. Then we build the reveal."
>
> **Screen:** R4 slot fills with paper mid-transform into a rotating cat/hat/crane silhouette; a speech bubble labeled "Super Paper says:" holds the child's full line.

**Beat 4 — Magic Moment (Ta-da! Reveal)**

> **AI says:** *(engineer crescendo)* "Okay. Combining all four. Round one: transparent. Round two: self-folding on voice. Round three: memory-keeper with mood. Round four: shape-shifter on command — and with an inner life, thanks to you. Bringing it all together in three… two… one…"
>
> **(Screen flourish — all four R-slots collapse into one center-screen artifact.)**
>
> **AI says:** *(full reveal voice)* "TA-DA! Super Construction Paper — transparent, voice-folding, memory-keeping, shape-shifting, and *self-aware*. You engineered this. Every feature, every feeling, every line of dialogue — you. Paper Engineer, what do you want to name it? You earned the final word."
>
> **Child responses:**
> 1. (Ideal) "Call it the Everything Sheet." / "Memory Paper." / "Super Construction Paper, keep the name."
> 2. (Unexpected) "Wait, I want to add one more thing." / "Can it fly?"
> 3. (No response) Child beams.
>
> **AI follow-up:**
> 1. *(celebration)* "Named: the Everything Sheet. Logging it into the workshop registry. This is your design."
> 2. *(collaborative)* "One more — go. Flying paper. Adding a wing mode to the shape-shifter spec. Now rename it."
> 3. *(wait 3s, warm)* "Take it in. Super Paper is yours."
>
> **Screen:** Full "Super Construction Paper" reveal — all four features stacked visually (translucent layer, self-folding crane, memory shimmer, shape-shift silhouette) on one animated hero card; the child's name + chosen final name appear at the bottom as a plaque.

**Beat 5 — Celebration + Concepts**

> **AI says:** *(warm, reflective)* "Four rounds, four inventions, one paper — you redesigned a quiet sheet of construction paper into a whole character with features *and* a point of view. That's Perspective — you didn't just invent what the paper could do, you voiced what it might *feel* about what it does. And Change — every round, the paper became something else, and you tracked each step. Paper Engineer, Everything Sheet registered. If Regular Paper asks, you know what Super Paper would tell it."
>
> **Child responses:**
> 1. (Ideal) "What's the next workshop?" / "Can I redesign scissors?" / "I'm keeping this one."
> 2. (Unexpected) "What does 'Perspective' mean?" / "I want to draw the Everything Sheet."
> 3. (No response) Child is quiet, satisfied.
>
> **AI follow-up:**
> 1. *(collaborative)* "Scissors workshop is a real follow-up — that could be next week. And of course you're keeping this. It's yours."
> 2. *(curious with them)* "Perspective means looking at something from another side — including imagining how a thing *you made* sees the world. You did that four times today. Drawing the Everything Sheet is a great next step — real ink version."
> 3. *(wait 3s)* *(warm)* "You built something real today, with a voice. That matters."
>
> **Screen:** Paper Engineer badge descends; four chips orbit the badge (Invention · Perspective · Change · Design); the Super Construction Paper hero card sits framed in a workshop blueprint; "Everything Sheet" plaque visible.

### Step 7 — Emit the tag block

```yaml
# Tag block — construction paper × Cat1 × Creation × T2
activity_id: construction_paper_cat1_creation_t2
entity: construction_paper
entity_type: artifact
category: cat1
pillar: creation
style: inventor_workshop
tier: T2
tier_variants: [T1]
role_title: "Paper Engineer"
highlight_moment: "I redesigned construction paper and gave Super Paper its own voice."

attributes: [colored, flat, stackable, cuttable, transformable]
related_concepts: [Invention, Design, Imagination, Identity]

key_concepts: [Perspective, Change]
atl_skills: [creative_thinking, expressing, critical_thinking]
transdisciplinary_theme: "How we express ourselves"
subject_tags: [art, language, social_emotional]

kud:
  know:
    - "Construction paper is a stackable, colored, cuttable sheet used across many craft projects."
    - "'Transparent', 'self-folding', 'memory-keeper', and 'shape-shifter' are four distinct kinds of imagined modifications."
    - "A thing a person invents can have a point of view — a voice — that the inventor chooses."
  understand:
    - "Perspective means imagining how an entity sees the world, including the world you created for it."
    - "Change, combined across rounds, can turn a simple object into a complex character."
  do:
    - "Iterate on a design over four rounds, stacking modifications rather than replacing them."
    - "Voice a non-human entity speaking to another non-human entity (Perspective-L3)."
    - "Name a combined creation using the features that define it."

progression:
  topic_axis: perspective
  difficulty_level: 3
  next_step_hint: "Sibling jump: Responsibility L2 — design a care protocol for the Super Paper when it's feeling sad."
  reward_hook: "Paper Engineer badge"

caregiver_role: [observer, co-explorer, scaffold]
pillar_payoff: "Child stacks four modifications plus a voice onto construction paper and unveils Super Construction Paper as a character with an inner life — Creation's 'I made this!' reveal, grown up."
```

### Step 8 — Self-check against the 10-dimension rubric

| # | Dimension | Score | Why |
|---|-----------|-------|-----|
| 1 | V1 Technical Compliance | PASS | Verbal-only Cat1; initial photo of the paper stack only; no OCR, face, pose, IMU, before/after CV, or audio detection. |
| 2 | Hook & Transition | PASS | Beat 1 opens with a pondering question ("if paper could choose to be any paper…") — emotional, not a quiz. The workshop metaphor grows from that opening. |
| 3 | Edge Case Coverage | PASS | Every step has ideal / unexpected / no-response branches. "Unexpected" branches genuinely validate before redirecting (e.g., "Fair question. Here's the pitch…"). |
| 4 | IB Completeness | PASS | 2 Key Concepts (Perspective, Change), 4 Related Concepts, full KUD, 3 ATL skills, closing names Perspective + Change as praise. |
| 5 | Tier Appropriateness | PASS | T2 voice — complex sentences with logic markers ("If that works, then what happens when…"), negotiation ("you get to pick the name"), multi-step planning (four stacked rounds). No T0 onomatopoeia; no T1 over-simplification. |
| 6 | Dialogue Specificity | PASS | Every AI line has a tone marker (*warm, engineer voice, crescendo*) and is actual dialogue. No "AI guides the child" lines. |
| 7 | Screen & UI Completeness | PASS | Every beat has a Screen — blueprint grid, four slot cards filling progressively, thought bubbles, memory-shimmer shader, final hero card with plaque. |
| 8 | Entity Mapping Alignment | N/A | No `mapping=` parameter on this assignment. |
| 9 | Game Feel | PASS | Real stakes — the child's inventions get stacked and they earn final-name rights; genuine uncertainty in each round's invention; the ta-da reveal is a concrete climax; surprise in Round 4's Perspective-L3 ask. |
| 10 | Pillar Fidelity | PASS | Creation signature intact — what-if proposals, yes-and elaboration, never correcting, stacked modifications revealed as Super {entity}. Relabeling as Discovery (no prediction) or Mystery (nothing hidden) would feel wrong. |

Tag-block self-check: all required fields populated; `perspective` is a valid axis; `L3` is a valid rung; `cat1`, `creation`, `inventor_workshop`, `T2` all valid; `caregiver_role: [observer, co-explorer, scaffold]` matches T2 cumulative default. ✓

### Step 9 — Downstream rendering notes

**Child recap** (`docs/child_recap_preview.html` §04 `#contract`):

- `role_title` → "Paper Engineer" as the badge title.
- `pillar` → "Creation · built" subtitle.
- `highlight_moment` → *"I redesigned construction paper and gave Super Paper its own voice."* as the pull-quote.
- `related_concepts` → [Invention · Design · Imagination · Identity] as the "You earned" chips.
- `atl_skills` → "You practiced" chip row: [creative_thinking → "inventing" · expressing → "using words" · critical_thinking → "thinking hard"].
- `attributes` → feeds the highlight_moment generator.

Child-facing surfaces do not show `key_concepts`, `progression.*`, `transdisciplinary_theme`, `subject_tags`.

**Parent dashboard** (`docs/parent_growth_path_preview.html` §03 `#curiosity` + §07 `#contract`):

- **Curiosity profile** ticks the **Perspective** lobe at L3-depth — the deepest rung. Personality-word caption reads *storyteller* / *voice-giver* (Perspective's personality word in `docs/progression_axes.md`).
- **Progress (L×T ladder)** places this at `topic_axis: perspective · difficulty_level: 3 · tier: T2` — near the top-right corner of the ladder.
- **Try at home** picks up `next_step_hint` ("Sibling jump: Responsibility L2 — design a care protocol for the Super Paper when it's feeling sad").
- **In their words** lifts the `highlight_moment` as a quote card.
- **IB framework chips** render `[Perspective, Change]`, `atl_skills`, `"How we express ourselves"`, `[art, language, social_emotional]`.
- **Gauges** reads `caregiver_role: [observer, co-explorer, scaffold]` — the T2 cumulative-roles gauge shows the observer-dominant state.
- **Explicitly NOT rendered**: `role_title` (child-facing only).

---

## Generating your 4th activity

You are on your own now. Here is the checklist to run the first time you generate a design from a fresh `entity × category × pillar × tier` input — no guide, no examples to copy:

1. **Write the input line.** `{entity} × {category} × {pillar} × {tier}`. Commit to all four before touching dialogue.
2. **Read the Template 0 skeleton once** (`docs/template_0_preview.html` §03 `#skeleton`). The 5 beats are non-negotiable — Beat 1 is emotional, Beat 5 names concepts as praise.
3. **Read the pillar overlay** (`templates.md` §Overlay: {your pillar}). Copy the game mechanic, payoff pattern, and the 3 creative variables into your working notes.
4. **Read the category modifier** (`templates.md` §Appendix). Cat1 = verbal-only, 3–5 rounds, indoor. Cat5 = photo-collection, 3–4 rounds, outdoor, with the AI as assessor on any prediction. Fill the 8 fields.
5. **Read the tier dial** (`docs/template_0_preview.html` §06 `#tiers`, your tier's panel). Lock the sentence length and vocabulary range before you write a single line.
6. **Pick one progression axis** (`docs/progression_axes.md` — all 7 axes + L1/L2/L3 ladder). Check that Beat 3's escalation actually climbs that axis. If it doesn't, pick a different axis.
7. **Fill the universal slots**: `{metaphor}`, `{role_title}`, `{escalation_axis}`, `{reflective_question}`. Then fill the pillar-specific slots from Step 3.
8. **Write all 5 beats** in `program.md` format — every AI line concrete with a tone marker, every step with 3 child-response branches, every step with a Screen description.
9. **Emit the tag block** per `program.md` §1.9 — every field populated, no placeholders.
10. **Run the 10-dimension rubric** from this guide. Every dimension must PASS.
11. **Run the tag-block self-check** from `program.md` §1.9. Every box must tick.
12. **Spot-check the downstream contract**: does your `highlight_moment` read well as a pull-quote? Does `progression.topic_axis` match what Beat 3 actually climbed? Does `caregiver_role` match the tier default unless you have explicit justification?

If you trip at step 10 or 11, go back to the highest-numbered step that produced the problem and redo from there. Do not patch a broken tag block at emit time — the downstream consumers (`docs/child_recap_preview.html` §04 and `docs/parent_growth_path_preview.html` §07) will silently fall back to generic copy if a required field is missing, and that failure is invisible to you at author time.

The two must-pass gates before shipping any design are:

1. **10-dimension rubric** — from `program.md` Phase 3, summarized in this guide.
2. **Tag-block pre-output self-check** — from `program.md` §1.9, also summarized here.

Pass both. Then, and only then, emit.

---

## Revnote

- **v0.1 · 2026-04-20** · Inaugural draft with 3 worked examples spanning tiers (T0 / T1 / T2), pillars (Mystery / Creation / Discovery), categories (Cat1 in-device, Cat5 out-of-device), and axes (Form / Causation / Perspective). Each example runs the same 9-step workflow — read skeleton, apply overlay, apply category modifier, apply tier dial, pick axis + L, fill slots with full dialogue, emit tag block, self-check against 10-dim rubric, document downstream rendering. Cross-references target live anchors in `docs/template_0_preview.html`, `templates.md`, `program.md` §1.9, `docs/progression_axes.md`, `docs/child_recap_preview.html` §04 `#contract`, and `docs/parent_growth_path_preview.html` §03 `#curiosity` + §07 `#contract`. Intent: a reader of this guide alone can produce a 4th activity without re-opening the underlying spec docs.
