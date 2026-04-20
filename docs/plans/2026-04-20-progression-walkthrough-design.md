# Progression Walkthrough — Design Spec

**Date:** 2026-04-20
**Status:** Draft, pending review
**Template 0 authority:** `docs/template_0_preview.html` §07 (v0.3 · 2026-04-20)
**Companion walkthrough:** `docs/template_0_lt_walkthrough.html` (L × T orthogonality)

---

## 1 · Context

Template 0 §07 adds an L1↔L2↔L3 transition subsection that specifies WHEN the runtime promotes, holds, or demotes a child's rung on each progression axis. The rules are quantified (2 consecutive in-activity demotes → next activity −1, etc.) and complemented by three footer rules (**dignity rule**, **sibling-axis jump**, **personalization hook**).

The spec is internally sound, but it's **temporal** — the insight is how a child's state evolves across sessions — which prose can describe but can't make vivid. Specifically, three subtleties get under-communicated:

1. **Dignity rule** — "a demote is never surfaced as failure; language reframes as 'let me show you what I notice first'." In prose it's one bullet; in practice it's the single behavior that separates this system from "you failed, try easier." Reviewers who skim prose miss the full significance.

2. **Per-axis state tracking** — the runtime keeps rung state PER AXIS, not one global rung. So a child can be on Form L3 while still at Causation L1. Prose states this, but a timeline side-by-side makes it visceral.

3. **Sibling-axis jump** — when the child hits L3 on an axis, next activity can pivot to L1 on a related axis instead of forcing L3 elsewhere. Again, prose names it; visualization shows what the move looks like.

The existing L × T walkthrough (`template_0_lt_walkthrough.html`) established a pattern for static-concept visualization: a 3×3 matrix showing orthogonality at a glance. This doc specifies a parallel walkthrough for **temporal** progression — how a child moves through rungs over time.

### 1.1 Why now

Template 0 v0.3 is shipped. Downstream surfaces exist. Matchability tags exist. The question authors + PMs + engineers now face is *"given a specific child over 6-12 sessions, what does the ladder actually do?"* — and prose answers that poorly. A walkthrough closes the gap.

### 1.2 Running entities

The walkthrough uses **Mia** (the running child across all downstream docs) and the **ladybug** running entity where appropriate, plus one or two fresh entities to demonstrate axis-independence. Consistency with the rest of the doc set makes the walkthrough feel like part of one story, not a standalone exercise.

---

## 2 · Scope

### In scope

- **One new HTML preview doc** + CN mirror: `docs/template_0_progression_walkthrough.html` + `_cn.html`
- **4 canonical scenarios** (initial batch; can grow to 6 later):
  1. Steady progression (baseline — no surprises)
  2. Hit-a-wall recovery (dignity rule + sibling-axis jump in action)
  3. Across-axis independence (per-axis state, not one global ladder)
  4. Reluctance vs inability (the can't/won't distinction)
- **Per-scenario horizontal timeline** showing 5–8 activity cards in sequence, with state transitions visible between cards
- **State panel** (per scenario) showing current rung-per-axis after each activity
- **Dialogue snippets** on demote moments so the dignity rule is visible, not just described
- **Cross-link** from Template 0 §07 to the walkthrough
- Same aesthetic tokens and bilingual parity as the surfaces-split + matchability PRs

### Out of scope

- **Live simulator** — not building a state-machine engine. Scenarios are hand-authored sequences.
- **Scenarios 5–6 (personalization hypothetical, long-arc)** — deferred to a v0.2 iteration if the walkthrough lands and gets used. Noted in §6.
- **Runtime-telemetry tie-in** — how the runtime actually records trigger events. That's an implementation detail for `docs/upstream_matcher.md` / runtime spec.
- **Per-child pace model** — explicitly out of scope; the walkthrough describes V1 (quantified threshold) behavior only, with a brief note that a pace model replaces thresholds later.
- **Interactivity beyond hover / click-to-expand** — scenarios are read-through narratives; no drag-to-reorder, no parameter tweaking.
- **Template 0 §07 edits** — the spec in §07 is authoritative; the walkthrough illustrates it, doesn't modify it. Only change to Template 0 is adding a cross-link subhead block pointing to the walkthrough.

### Explicitly deferred / future iterations

- Scenario 5 — **Personalization hypothetical**: split view "v1 threshold rules vs per-child pace model" applied to the same underlying situation
- Scenario 6 — **Long arc**: 12+ sessions compressed into a single view showing rung-per-axis drift divergence over a month; ties into the parent dashboard curiosity radial
- "Pick your own path" interactivity (future consideration — not this round)

---

## 3 · The four scenarios

Each scenario is a horizontal sequence of **activity cards**. Each card is one activity the child plays. Between cards, a compact **transition indicator** shows which trigger matched and what state changed.

### 3.1 Scenario 1 — Steady progression

**Purpose**: baseline. Show the unremarkable, happy-path journey so the other scenarios have something to contrast against.

**Entity**: ladybug (across first three), then butterfly, then sunflower (for variety)
**Axis focus**: Form
**Child**: Mia (T1, 4-6 years)

**Sequence (5 activities)**:

| # | Activity | Entering rung | Outcome | Exit rung | Transition trigger |
|---|---|---|---|---|---|
| 1 | Ladybug · Form | L1 (notice) | Named 4 attributes in 2 rounds without prompt-repeat | L1 | within-activity hold — solid L1 but not yet L+1 spontaneous |
| 2 | Ladybug · Form (new exemplar) | L1 | Named 3 attributes, then spontaneously said "the spots are why birds don't eat it" → L2-ish | L1 | within-activity promote (next-activity) — spontaneous L+1 response |
| 3 | Butterfly · Form | L2 (extend) | Listed 4 attributes + pointed at one | L2 | within-activity hold — completing L2 successfully |
| 4 | Butterfly · Form (second try) | L2 | Listed 5 attributes, located each | L2 | within-activity hold — 2nd L2 success on same axis |
| 5 | Sunflower · Form | L2 | Listed 6 attributes, located each, compared to butterfly | **L3** | **across-activity promote** — 3 consecutive L2 successes on Form → next on Form defaults to L3 |

**State panel shows**: `Form: L1 → L1 → L2 → L2 → L2 → (L3 next)` — rest of axes unchanged.

**Key demonstration**: the normal rhythm — most activities hold, promotions happen at natural breakpoints, nothing dramatic.

### 3.2 Scenario 2 — Hit-a-wall recovery

**Purpose**: show the dignity rule and sibling-axis jump in action. This is the most important scenario because these two rules are the subtle design choices most likely to be misread.

**Entity**: ladybug throughout
**Axis focus**: Causation primary, Connection as sibling
**Child**: Mia (T1, 4-6 years)

**Sequence (6 activities)**:

| # | Activity | Entering rung | Outcome | Exit rung | Transition trigger |
|---|---|---|---|---|---|
| 1 | Ladybug · Causation | L2 (extend) | Explained "red because sun helps" but couldn't connect to predators | L2 | within-activity hold — mixed but on-topic |
| 2 | Ladybug · Causation (second session) | L2 | Went quiet after "why red?" for 8s, then repeated prompt back | **L1** | within-activity demote — drop to L1, same axis, complete the activity at L1 |
| 3 | Ladybug · Causation (third session) | L1 | Again silent, off-topic wander to "what color are my shoes" | L1 | within-activity demote on L1 attempt — hit floor. **Runtime invokes sibling-axis jump.** |
| 4 | Ladybug · Connection ← sibling jump | L1 (new axis) | Named 3 things lines connect to ladybug (grass, bird, leaf) | L1 | within-activity promote — steady L1 on new axis |
| 5 | Ladybug · Connection | L1 | Connected 4 things + explained one ("grass for food") | **L2** | within-activity promote (spontaneous L+1) |
| 6 | Ladybug · Causation (return) | L1 | This time: "red warns birds because birds don't eat red" — clean L2 response | **L2** | within-activity promote — Causation comes back online, bootstrapped by Connection confidence |

**State panel shows** rung-per-axis changing over time:
- Start: `{Form: L2, Causation: L2, Connection: L1, ...}`
- After #3: `{Form: L2, Causation: L1, Connection: L1, ...}` (Causation demote stuck)
- After #5: `{Form: L2, Causation: L1, Connection: L2, ...}` (Connection promoted)
- After #6: `{Form: L2, Causation: L2, Connection: L2, ...}` (Causation recovered)

**Dialogue snippet panels** (critical for dignity rule):

On activity #2 demote event — show two callouts side by side:
- **What the runtime records**: `{"axis": "causation", "rung_change": "L2→L1", "trigger": "2_attempts_no_complete"}`
- **What Mia hears**: "Hmm — let me show you what I notice about the ladybug's red. Then you can tell me what you notice." [not "let's try something easier"]

On activity #3 → #4 sibling jump — show two callouts:
- **What the runtime records**: `{"axis_switch": "causation→connection", "rung": "L1", "trigger": "sibling_jump_on_axis_floor"}`
- **What Mia hears**: "Look at all the things the ladybug touches — the grass, the leaf. Let's see how they all go together." [not "you couldn't answer so we're changing subjects"]

**Key demonstration**: the child's experience is continuous; the runtime's bookkeeping is elaborate. Both are true simultaneously.

### 3.3 Scenario 3 — Across-axis independence

**Purpose**: kill the "one global rung" intuition. Show that at the same moment in time, a child can be at L3 on one axis and L1 on another, with no tension between those states.

**Entity**: bee
**Axes**: Form (strong) + Causation (weaker) + Responsibility (barely touched)
**Child**: Mia (T1)

**Sequence (5 activities, compressed timeline)**:

| # | Activity | Axis | Entering | Exit | State after |
|---|---|---|---|---|---|
| 1 | Bee · Form | Form | L3 | L3 | Form: L3 |
| 2 | Bee · Form (new framing: "match 5 parts to functions") | Form | L3 | L3 | Form: L3 (held) |
| 3 | Bee · Causation | Causation | L1 | L1 | Causation: L1 (held; mixed answers) |
| 4 | Bee · Responsibility | Responsibility | L1 | L1 | Responsibility: L1 (child stayed on-topic but minimal engagement) |
| 5 | Bee · Form (final session) | Form | L3 | L3 | Form: L3 (3rd L3 on Form — personalization hook would kick in here at ≥200 total sessions) |

**State panel visualization** (the point of this scenario): show all 7 axes as a mini-radial or bar chart. Four are untouched (L0 / not started), one is L3 (Form), one is L1 (Causation), one is L1 (Responsibility). That's the full snapshot — NOT one number.

**Key demonstration**: "Mia is at L3 on Form AND L1 on Causation AND uninitialized on Change" is the correct mental model. There's no single "Mia's current level" because rungs live per axis.

Pair this with a small caption contrasting it to traditional game-ladder systems where there's one XP bar: **"There is no XP bar. There are 7 bars, and they drift independently."**

### 3.4 Scenario 4 — Reluctance, not inability

**Purpose**: show that the runtime distinguishes emotional state from cognitive state. A child who goes quiet mid-activity isn't necessarily at the wrong rung — they might be tired, shy, distracted, or processing.

**Entity**: mushroom (new; not covered elsewhere in the doc set — intentional to show the walkthrough isn't ladybug-only)
**Axis focus**: Form
**Child**: Mia (T1)

**Sequence (3 activities)**:

| # | Activity | Entering | What happens | Runtime decision | Exit |
|---|---|---|---|---|---|
| 1 | Mushroom · Form | L2 | Mia gives 2 correct attributes, then stops. Doesn't answer prompts, doesn't repeat them back. Silence for 8s. | **Runtime reads as emotional pause, not cognitive gap.** Shifts to a lower-pressure BEAT within the same activity (still L2) — shows a second mushroom image and says "oh look, this one is different. I wonder what you see." | L2 (held; no rung change) |
| 2 | Mushroom · Form (same session, 2 min later) | L2 | Mia re-engages after the lower-pressure prompt; names 4 attributes in next 2 rounds | within-activity promote (next-activity on Form → L3) | L3 |
| 3 | Mushroom · Form | L3 | Mia completes the L3 task — comparing mushroom to a familiar fruit's form | within-activity hold | L3 |

**Key design callout** in a dedicated side panel:

> **The silence trigger isn't a demote trigger.** A demote requires 2 *attempts* — silence + off-topic wander + repeat-prompt-back. A single silence after a correct response is often just the child thinking, resting, or needing a gentler re-entry. The runtime has a separate **soft-reframe** move for this — it's a beat-level adjustment within the activity, NOT a rung change.

This distinguishes:
- **Demote** — child's cognitive state genuinely mismatches the rung; drop
- **Soft-reframe** — child's emotional/attention state needs a breath; same rung, softer prompt

**Key demonstration**: the runtime isn't rung-greedy. It has intermediate moves that preserve rung without pushing.

---

## 4 · Page structure

The HTML file follows the **same shape** as `template_0_lt_walkthrough.html`. Reuse its aesthetic, tokens, and structural conventions. Concrete sections:

### 4.1 Masthead
- Breadcrumb back to Template 0: `← Template 0 · §07 Progression`
- Page title: `Progression walkthrough · L1 ↔ L2 ↔ L3 in action`
- Version tag: `v0.1 · 2026-04-20 · Internal review`
- Same masthead nav style as L × T walkthrough

### 4.2 Intro block
- 2–3 sentence framing: this doc shows the §07 transition rules applied to specific child journeys. Not a simulator — hand-authored scenarios to make the temporal dynamics concrete.
- Quick legend:
  - ↑ promote = next rung up
  - · hold = same rung, next activity varies exemplar
  - ↓ demote = drop one rung, same axis (dignity rule applies)
  - ⇢ sibling jump = switch to related axis at L1
  - ~ soft-reframe = same rung, different beat

### 4.3 The four scenarios

Each gets its own section:
- Scenario title + one-sentence TL;DR
- Context block (child, axis focus, entity, tier)
- **Horizontal timeline** with 5–8 activity cards (scroll-snap if it overflows)
- **Transition indicators** between cards (↑ ↓ · ⇢ ~ glyph + brief label)
- **State panel** (always visible during scroll) showing rung-per-axis
- **Dialogue snippets** as expandable callouts on key events (especially demotes and sibling jumps)
- Bottom: "Why this scenario matters" — one-paragraph takeaway

### 4.4 The three rules, visualized once

After the scenarios, a compact summary block pulling out the three footer rules from §07 with an icon / visual mnemonic each:

- **Dignity rule** (never shown as failure)
- **Sibling jump** (L3 → L1 on related axis)
- **Personalization hook** (v1 thresholds replaceable by per-child model)

Each gets a 1-sentence restatement + a callout showing the single scenario example where it applied.

### 4.5 Footer
- Revnote block (identical pattern to other preview docs): v0.1 · 2026-04-20 · Inaugural
- Version block
- Companion-link back to Template 0 §07

---

## 5 · Activity card shape

Core unit. Rendered as small stacked cards, ~240px wide, flowing left-to-right.

```html
<article class="ac" data-axis="form" data-entry-rung="L2" data-exit-rung="L2" data-trigger="hold">
  <header class="ac-head">
    <span class="ac-num">Activity 3</span>
    <span class="ac-axis">Form</span>
  </header>

  <div class="ac-entity">
    <svg class="ac-entity-icon" aria-hidden="true">...</svg>
    <span class="ac-entity-name">Butterfly</span>
  </div>

  <div class="ac-rungs">
    <span class="ac-rung ac-rung-entry">L2</span>
    <span class="ac-rung-arrow">→</span>
    <span class="ac-rung ac-rung-exit">L2</span>
  </div>

  <div class="ac-outcome">Listed 4 attributes + pointed at one</div>

  <div class="ac-trigger">
    <span class="ac-trigger-glyph">·</span>
    <span class="ac-trigger-label">hold · completing L2 successfully</span>
  </div>

  <details class="ac-detail">
    <summary>What Mia heard</summary>
    <div class="ac-dialogue">...</div>
  </details>
</article>
```

CSS uses existing tokens (`--accent`, `--tier-0/1/2`, `--mono`, `--serif`, `--bg-card`, `--line`). Entry rung pill uses `--tier-N-bg` where N matches the rung-level mapping (or a custom `--rung-1/2/3` pair if needed — see §8).

### 5.1 Between-card transition indicators

Not part of the card; sit between cards as their own element:

```html
<div class="transition" data-type="promote">
  <span class="t-glyph">↑</span>
  <span class="t-label">promote · spontaneous L+1</span>
</div>
```

Four types: `promote` `hold` `demote` `sibling-jump` `soft-reframe`. Each has a distinct glyph + color (promote = accent; demote = tier-0 warm; sibling-jump = --accent-2 or muted; soft-reframe = muted).

### 5.2 State panel (per scenario)

Sticks to the side or top of each scenario. Shows rung-per-axis as a small horizontal bar chart (7 axes × 3 possible rungs + "not started"). Updates visually as you scroll through the scenario's timeline.

**Low-tech version for v0.1**: static final-state snapshot at the end of each scenario. Live update during scroll is nice-to-have; skip if it becomes complex.

---

## 6 · Deferred scenarios (future iterations)

Not built in v0.1 but named here so they're preserved as design intent:

### Scenario 5 — Personalization hypothetical

Split view. Same child, same history, two columns:
- Left: "V1 threshold rules — what ships today"
- Right: "Per-child pace model — what replaces V1 after ~200 sessions"

Shows the same 6 activities under each rule set; highlights where the pace model would deviate (typically: recognizing that Mia consistently spontaneously jumps ahead on Form, so promoting her faster there, while keeping strict pacing on Causation).

**Why valuable**: makes the upgrade path concrete. Readers see V1 isn't permanent — it's scaffolding.

### Scenario 6 — Long arc

12+ session timeline compressed into one view. Shows how rung-per-axis drifts over a month. Directly feeds the parent-dashboard curiosity radial: the drift IS what the radial shows.

**Why valuable**: ties the walkthrough to the parent dashboard; shows progression as a longitudinal signal.

Both scenarios depend on more mature design of the parent dashboard's month-view cadence + the personalization pace model, which aren't built yet. Revisit in v0.2.

---

## 7 · Cross-references

- Template 0 §07 ↔ this walkthrough (new bidirectional link — §07 gains a "see walkthrough" subhead; walkthrough breadcrumbs back to §07)
- Template 0 §06 (tier comparison) — referenced from scenario intros where T1 matters
- Parent dashboard §03 (curiosity radial) — referenced from Scenario 3 state panel (the radial IS this snapshot, at a longer time window)
- Nothing from the walkthrough feeds INTO Template 0 — one-way illustrative relationship

---

## 8 · Aesthetic + tooling constraints

Mirror the L × T walkthrough and the surfaces-split PRs:

- Same `:root` tokens (no new CSS variables needed)
- Fraunces + IBM Plex font stack
- EN + CN parity strict — YAML-style tokens (`L1`, `L2`, `L3`, axis names) stay English in both locales
- No new JS
- No emojis
- `<html lang="zh-Hans">` on CN
- `:focus-visible` on all interactive elements (details/summary, card expansions, any scroll arrows)
- Semantic HTML (`<article>` for cards, `<section>` for scenarios, `<th scope="col">` for any tables, `<details>/<summary>` for expansions)

### 8.1 Potential new tokens

Current `:root` has `--tier-0`, `--tier-1`, `--tier-2` for age tier colors. The walkthrough needs RUNG colors (L1/L2/L3) that don't collide with tier colors.

**Options:**
- **(a)** Reuse `--accent` + two derived shades via `color-mix` (cheapest)
- **(b)** Introduce `--rung-1`, `--rung-2`, `--rung-3` tokens in `:root` (most correct but adds to the shared palette)

Recommend **(a)** for v0.1 — use `color-mix(in srgb, var(--accent) N%, transparent)` with three N values (e.g. 25% / 55% / 85%). Minimum new tokens. If it feels muddy in review, upgrade to (b) in a follow-up.

### 8.2 Scroll behavior

Scenarios are horizontal timelines. Options:
- Pure CSS `scroll-snap-type: x mandatory` on the timeline container; each card is a snap target
- Fallback vertical stack on mobile (<700px) — prose-style list instead of horizontal scroll

No JS for scroll; the browser's native snap is enough. If design review wants nav arrows or pagination, add in a follow-up — not v0.1.

### 8.3 Mobile

At 375×812:
- Timeline collapses to vertical stack (one card per row)
- State panel moves from side to top
- Transition indicators become top-of-card badges instead of between-card markers
- Everything else stays same

Same breakpoint as the surfaces-split docs — 700px or 960px; reuse whatever is established.

---

## 9 · Verification checklist

Once implemented, all must hold:

### 9.1 Structure (EN + CN both)

- [ ] Masthead breadcrumb back to `template_0_preview.html#axes`
- [ ] 4 scenarios, each with:
  - [ ] Title + TL;DR
  - [ ] Context block (child, axis, entity, tier)
  - [ ] Horizontal timeline with the expected card count (5 / 6 / 5 / 3)
  - [ ] Transition indicators between all cards
  - [ ] State panel showing rung-per-axis
  - [ ] "Why this scenario matters" closer
- [ ] Three-rules summary block
- [ ] Revnote + version footer

### 9.2 Dialogue snippets

- [ ] Scenario 2 activity #2 demote event: two callouts — "what runtime records" + "what Mia heard"
- [ ] Scenario 2 activity #3→#4 sibling jump: same two-callout pattern
- [ ] Scenario 4: soft-reframe distinction clearly boxed off from "demote"

### 9.3 Per-axis state visible

- [ ] Scenario 3 has a 7-axis radial or bar snapshot making axis-independence visceral
- [ ] Other scenarios show rung changes for at most 2–3 axes (don't clutter)

### 9.4 EN/CN parity

- [ ] `<html lang="zh-Hans">` on CN
- [ ] Same structural count of cards, transitions, state panels, dialogue callouts
- [ ] YAML-like tokens (L1/L2/L3, Form, Causation, Connection) stay English
- [ ] Dialogue snippets translated naturally (child speech is the key translation quality gate)

### 9.5 Cross-references

- [ ] Template 0 §07 gains a cross-link subhead pointing to `template_0_progression_walkthrough.html` (both EN and CN)
- [ ] Walkthrough breadcrumb links to `#axes` anchor in Template 0
- [ ] No broken internal links

### 9.6 Visual + a11y

- [ ] Desktop 1280×1000 — scenarios flow left-to-right cleanly
- [ ] Mobile 375×812 — scenarios collapse to vertical stack, no horizontal overflow
- [ ] Console clean
- [ ] `:focus-visible` on all interactive elements
- [ ] Color contrast meets WCAG AA on rung pills, transition glyphs, dialogue callouts

### 9.7 Content accuracy against §07

- [ ] Within-activity promote trigger matches §07: "2+ correct rounds without prompt-repetition, OR spontaneous L+1 response"
- [ ] Within-activity demote trigger matches §07: "2 attempts without completion (silence >6s, off-topic, repeats prompt)"
- [ ] Across-activity promote: "3 consecutive same-axis successes → next +1"
- [ ] Across-activity demote: "2 consecutive same-axis in-activity demotes → next −1 (floor L1)"
- [ ] Dignity rule language: "let me show you what I notice first" — verbatim
- [ ] Sibling jump: L3 → L1 on related axis (NOT L2 on related)
- [ ] Personalization hook: `progression_policy` in tag block upstream config; ≥~200 sessions trigger for pace model swap

---

## 10 · Implementation plan handoff

Once this spec is approved, writer-of-implementation-plan should produce:

`docs/plans/YYYY-MM-DD-progression-walkthrough-implementation.md`

Expected task shape (~8–10 tasks):

1. Worktree + preview server setup
2. Base HTML scaffold — masthead, intro, revnote + footer (EN)
3. Scenario 1 (steady progression) — cards + transitions + state panel (EN)
4. Scenario 2 (hit-a-wall recovery) — cards + dialogue callouts (EN)
5. Scenario 3 (across-axis independence) — cards + per-axis visual (EN)
6. Scenario 4 (reluctance vs inability) — cards + soft-reframe callout (EN)
7. Three-rules summary block (EN)
8. Template 0 §07 cross-link subhead (EN + CN)
9. CN mirror — all 4 scenarios translated, structural parity verified
10. Verification pass + cross-link check
11. Push + PR
12. Final cross-branch review

Estimated scope: **comparable to the matchability-tags PR** — one net-new preview doc (like a miniature version of child recap or parent dashboard in structure) + small surgical Template 0 edit.

Each task gets:
- Implementer subagent (general-purpose)
- Spec-compliance review
- `pr-review-toolkit:code-reviewer` for quality
- `pr-review-toolkit:code-simplifier` for redundancy
- Fixup loops for any Important items
- Final cross-branch review at the end

---

## Revnote

- **v0.1** (2026-04-20) — Inaugural draft. Establishes scope (4 scenarios, no live simulator, v1-threshold-only) and defines the core activity-card + transition-indicator shape. Deferred scenarios 5 (personalization) and 6 (long arc) captured for v0.2.
