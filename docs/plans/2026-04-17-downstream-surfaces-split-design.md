# Downstream Surfaces Split — Design Spec

> **Date**: 2026-04-17
> **Status**: Draft for user review
> **Depends on**: Template 0 v0.2 (`docs/template_0_preview.html`)
> **Feeds**: Implementation plan (next step, separate file)

---

## 1 · Context

Template 0's preview doc currently conflates three things:

1. **The template itself** — §03 skeleton, §04 tag block, §06 tier adaptation, §07 progression
2. **A reference to the existing upstream pipeline** — §05 Tier A/B/P selection (already specced in `game_design_playbook.md` §7)
3. **Illustrative mockups for two downstream surfaces that haven't been designed yet** — §05 child recap, §05 parent growth path

PM feedback in the v0.2 review round was largely about (3) — the child-vs-parent split of the tag system. Since those surfaces are now scheduled for real design work in the next 1–2 sprints, they warrant their own design docs rather than living as half-specced sidebars in Template 0.

**Goal of this spec**: cleanly extract the two downstream surfaces into their own design docs, leaving Template 0 as a focused contract document. Add the design depth the PM's feedback pushed for — anti-addiction principles for the child recap, and four new parent-facing modules beyond the L×T ladder.

---

## 2 · Scope

### In scope

- Layout tweak to `template_0_preview.html` (+ `_cn.html`): tag-block legend moves below the YAML
- Rewrite of Template 0's §05 downstream block as a compact "reference strip" with links out
- New doc: `docs/child_recap_preview.html` (+ `_cn.html`)
- New doc: `docs/parent_growth_path_preview.html` (+ `_cn.html`)
- Cross-link navigation between all three docs
- Bump Template 0 revnote with a new v0.2 bullet noting the extraction

### Out of scope (this design round)

- Back-end or tag-block schema changes (the contract in Template 0 v0.2 is sufficient)
- Final product copy, illustrations, animation timing (real product design, downstream)
- Cross-child / cross-family features
- Export, sharing, school-report flows
- Cross-session activity-transcript view (privacy concerns, needs its own design round)
- Developmental-milestones comparison ribbon (risks parental anxiety, deferred)
- Prediction / trajectory forecasting (over-promises, deferred)

---

## 3 · Changes to `template_0_preview.html` (+ `_cn.html`)

### 3.1 Layout tweak · tag-block legend below YAML

Current desktop layout puts the "Why these slots — split by the surface they feed" legend to the right of the YAML in a 3fr/2fr grid. The new two-column child/parent split needs horizontal room that the right column can't provide.

**Change**: in the `.tagblock` rule, drop the two-column grid and stack vertically on all viewports.

```css
.tagblock {
  display: grid;
  grid-template-columns: 1fr;  /* was: 3fr 2fr */
  gap: 32px;
  align-items: start;
}
/* The @media(max-width: 900px) override on .tagblock can be removed */
```

Mirror identically in `_cn.html`.

### 3.2 §05 downstream rewrite

**Remove from §05**:

- The two current mockup blocks (child recap + parent growth path)
- The closing "What's intentionally not designed yet" note

**Keep in §05**:

- The flow diagram (photo → recognition → tag block → selection → runtime)
- The upstream bridge (Tier A/B/P cards)
- The "Why this matters for Template 0" note directly under the upstream bridge

**Add in §05** (replacing the removed blocks): a thin *reference strip* — two compact cards, side-by-side on desktop, stacked on mobile.

Each card contains:

- Small label: "Downstream surface · N of 2"
- Serif title: "Child recap" / "Parent growth path"
- One-sentence purpose (see §4 and §5 below for copy)
- Monospace chip list of tag-block fields it reads
- Link arrow: "Full design →" linking to the corresponding new doc

Close the section with a single sentence (replacing the removed note):

> The full specs for these surfaces live in their own docs. The contract they depend on is what Template 0 provides.

### 3.3 Revnote update

Extend the v0.2 revnote with one more bullet:

> **Downstream surfaces extracted into their own docs** (§05). `child_recap_preview.html` and `parent_growth_path_preview.html` now carry the full designs; §05 keeps only the upstream pipeline + a compact reference strip to both.

Mirror in CN revnote.

---

## 4 · New doc · `docs/child_recap_preview.html` (+ `_cn.html`)

### 4.1 Purpose

The post-activity screen the child sees at the end of beat 5. Its job is to celebrate the specific cognitive act the child just performed and leave them with a warm, bounded ending — explicitly not to hook them into another session.

### 4.2 Aesthetic

Identical to Template 0: Fraunces variable serif for display, IBM Plex Sans/Mono for body/mono, cream (`#F4EFE6`) / ink (`#141311`) / vermilion (`#C5411C`) palette, same fixed masthead pattern with doc-specific title, same `§ NN / Section` numbering, same subhead treatment with `data-dir="..."` prefix. All CSS custom properties are the same `:root` block — copy verbatim from Template 0.

### 4.3 Section list

**§ 01 · Purpose & stance**

What the screen does and what it explicitly doesn't do. Frame the "explicitly doesn't" list early — this is the lens for every downstream decision.

**§ 02 · Anti-addiction principles & mechanisms**

The defining section of the doc. Two sub-blocks:

(a) **Principles table** — "Typical addictive pattern / Why it hurts / Our stance" for 8 patterns:

| Pattern | Why it hurts | Our stance |
|---|---|---|
| Streaks ("don't break your chain") | Creates guilt on skip days; pushes daily use regardless of need | No streaks. Ever. |
| Variable rewards (random drops) | Slot-machine dopamine loop | Deterministic — earned by a specific cognitive act |
| Unbounded collection | Grinding incentive; never "done" | Bounded set, visible from day 1 |
| Rare vs. common badges | Gambling / hoarding instinct | All badges equal. No rarity tiers |
| Leaderboards / peer comparison | Social anxiety, competition | Never show another child |
| External push notifications | Manufactured FOMO | App never pings the child |
| Infinite-scroll recap | Eyes-on-screen loop | One screen, one ending, dismissible |
| Time-based XP | Rewards duration over learning | Rewards tied to cognitive moves |

(b) **Mechanisms block** — 8 concrete rules (numbered list, each with 1–3 sentences):

1. **Bounded badge universe**: 7 axes × 3 rungs = 21 slots. Fixed from day 1; no mystery / locked slots.
2. **Mastery display, not tally display**: depth per axis (filling bar L1→L2→L3), not a pile of medals.
3. **`highlight_moment` is hero, badges are ambient**: the runtime-generated one-liner is large and serif; badges are secondary with no sparkles / pops / animation.
4. **Soft session cap**: after N activities in one sitting (T0: 2, T1: 3, T2: 4), the recap ends with "Good thinking today. See you tomorrow." App doesn't lock.
5. **Replay is welcomed, not re-earned**: second playthrough of same entity celebrates the new noticing, doesn't mint a new badge.
6. **No streaks UI, anywhere**: not hidden, not built.
7. **Exit with warmth, not a hook**: end on an invitation to look at the real world; never "tap to continue" or "N more until Level M."
8. **Opt-in history**: earned badges live on a separate collection screen. Never pushed.

**§ 03 · Layout walkthrough**

Annotated mockup — the existing Template 0 §05 child mockup enlarged, with callouts numbered 1–6 pointing to:

1. Badge circle (role_title)
2. Title + pillar subtitle (badge_title / pillar)
3. "The moment" row — `highlight_moment` one-liner rendered in serif (this is the hero)
4. "You earned" chips — `related_concepts` (ambient, small)
5. "You practiced" chips — `atl_skills` (ambient, small)
6. "See you tomorrow" exit copy (if soft cap reached) OR "Next time you're outside, see if…" real-world invitation

**§ 04 · Tag-block contract**

Which fields this screen reads from Template 0's tag block, and how each one renders:

| Field | Renders as | Notes |
|---|---|---|
| `role_title` | Badge title (serif) | Main identity beat of the screen |
| `pillar` | Subtitle under title ("Mystery · solved") | Emotional mode, sets tone |
| `highlight_moment` | Large serif pull-quote | Generated at runtime; see §05 |
| `related_concepts` | Small chip row under "You earned" | Child-friendly concept words |
| `atl_skills` | Small chip row under "You practiced" | Worded child-friendly, not IB jargon |
| `attributes` | Surfaced in `highlight_moment` generation | Not shown as chips; feeds the one-liner |

Explicitly **not read**: `key_concepts`, `transdisciplinary_theme`, `subject_tags`, `progression.*` (those are parent-facing).

**§ 05 · `highlight_moment` generation rule**

The one-liner is generated at activity-end from the child's responses during the activity. Spec the rule:

- Input: activity transcript (child turns) + `attributes` + `pillar` + `progression.topic_axis`
- Output: a **sanitized summary** (not a raw quote) — a single sentence in second person, past tense, evocative and specific: *"You spotted the warning sign on the ladybug's back"*. The transcript is input to the generator only; it never surfaces verbatim in the recap.
- Rules:
  - Always second-person ("You ___"), not "Mia ___"
  - Past tense
  - Grounded in something the child actually said or did (from transcript), not generic
  - 6–12 words
  - No IB terminology, no tier names, no level numbers
  - If no usable material, default to pillar-generic fallback (e.g. Mystery → "You solved a small mystery today.")
- Tier-specific copy examples — T0 ("You said 'red' when you saw the ladybug"), T1 ("You figured out why the ladybug is red"), T2 ("You predicted what birds do with red bugs, and you were right")

**§ 06 · Cross-session badge persistence**

How the 21-slot universe fills over time:

- First time a child earns a badge slot: the slot lights up in the collection view
- Subsequent earnings: a small count badge appears next to the slot ("×4"), but the visual state doesn't change
- Depth: the axis bar (L1 / L2 / L3) fills based on progression level reached; depth fills forward only (never retracts on in-session demotes)
- Collection view is reached by an opt-in "see your collection" link, not a post-recap auto-transition

**§ 07 · Copy tone by tier**

Voice samples for each row of the recap at T0 / T1 / T2:

- **Role title** — T0: "Ladybug Watcher" / T1: "Ladybug Detective" / T2: "Ladybug Field Researcher"
- **Highlight moment** — see §05 examples above
- **You earned** — same chip words across tiers; chip color / typography unchanged
- **You practiced** — T0: "Looking carefully" / T1: "Observing" / T2: "Observing · Describing"
- **Exit copy** — T0: "See you next time!" / T1: "Good thinking today." / T2: "Nice work. Come back when you want to keep going."

**§ 08 · Edge cases**

- In-activity demote happened: recap language softens, no "You figured out" — use "You noticed" (safer L1 frame)
- Child rage-quits mid-activity: no recap; next session opens with neutral welcome, no guilt
- Repeat entity within a week: `highlight_moment` acknowledges the replay ("You saw the ladybug again, and this time you noticed its round shape")
- Soft cap triggered: exit copy explicitly says "see you tomorrow" instead of a forward hook
- ASR failed to capture a usable quote: fall back to pillar-generic highlight_moment

**§ 09 · Open questions (deliberate)**

- Can parents opt the collection view off entirely? (Default: yes)
- How long until earned badges "fade" in visual state, if ever? (Default: never; parent can archive a semester)
- Should there be end-of-week / end-of-month synthesis screens for the child? (Deferred — would mirror addictive recap patterns)

**§ 10 · Out of scope**

- Monthly roll-ups for the child (see §09 above)
- Share-with-parent flow (parent sees it via the parent dashboard, not pushed to them)
- Offline / "while disconnected" badge state

---

## 5 · New doc · `docs/parent_growth_path_preview.html` (+ `_cn.html`)

### 5.1 Purpose

The parent dashboard. Weekly default view, with monthly and term toggles. Its job is to make the child's growth legible and actionable to the parent — without turning into a grade report or an addictive engagement loop.

### 5.2 Aesthetic

Same as Template 0 and child recap. Identical `:root`, same masthead, same section numbering.

### 5.3 Section list

**§ 01 · Purpose & stance**

What parents want, what the dashboard does, what it explicitly doesn't do. Include the anti-pattern table:

| Typical dashboard feature | Why we don't | Our stance |
|---|---|---|
| Peer comparison ("vs. other kids") | Anxiety, competition, parental guilt | Never. Only this child's journey |
| Letter grades / scores | Anti-IB philosophy; reduces nuance | No scores, no grades |
| Predictive trajectories | Over-promises; sets up disappointment | No forecast lines |
| Activity transcripts | Surveillance vibe | Out of scope this round |

**§ 02 · Layout walkthrough**

One annotated mockup showing the full weekly view. Six numbered regions:

1. Header — child name, week label, tier chip
2. **Progress** block — the L×T axis ladder (existing Template 0 §05 parent mockup content)
3. **Curiosity profile** — new; see §03 below
4. **This week in their words** — new; see §04
5. **Try this at home** — new; see §05
6. **Gauges strip** — new; footer with co-play share + time-this-week

**§ 03 · Module · Curiosity profile** _(NEW)_

A compact 7-lobed radial visualization — one lobe per IB Key Concept (Form, Function, Causation, Change, Connection, Perspective, Responsibility). For each lobe:

- Filled area proportional to frequency (how often the child has worked on that concept)
- Outline reach proportional to depth achieved (max rung L1 / L2 / L3)
- Color-coded by the same `--tier-*` palette if tier-filtered view is used

Auto-generated caption below the radial (1–2 sentences):

> *Mia is a pattern-finder and a storyteller. She explores Form and Perspective most deeply; Responsibility is next to try.*

Caption generation rules:

- Name the child's 1–2 dominant concepts using personality words (pattern-finder, storyteller, investigator, carer, …) — not raw concept names
- Mention the axis with lowest frequency as a gentle "next to try", not "weakness"
- Never imply the child should "catch up" on anything

**Reads from**: aggregate `key_concepts` + `progression.difficulty_level` across the session window

**§ 04 · Module · This week in their words** _(NEW)_

Two to three pull-quotes per week. Each quote-card has:

- The `highlight_moment` string OR a notable child utterance captured during activities (subject to privacy rules — see §09)
- Day + activity context ("Tuesday · playing with a sunflower")
- Optional: link to replay the activity

Rendered in serif, large, warm — deliberately feels like a journal entry, not a metric.

> *Mia said: "The flower closes to save energy at night."*
> *Tuesday · playing with a sunflower*

**Reads from**: weekly aggregate of `highlight_moment` + opt-in child-utterance highlights

**Privacy constraint**: child utterances shown only if parent opted in during onboarding; default is `highlight_moment`-only (since those are runtime-generated summaries, not raw transcripts).

**§ 05 · Module · Try this at home** _(NEW)_

Two to three concrete, offline, parent-participation suggestions per week. Each suggestion-card has:

- Single imperative sentence: *"On your walk, look for three spotted things together."*
- Small tag showing which axis it extends: *"Extends: Connection · matches pattern-finding"*
- Optional: an example photo or illustration (deferred — copy-only in v1 of the doc)

Bounded to 2–3 per week deliberately. More than that turns into a chore list.

**Key stance**: this module's purpose is to **send the parent-child pair away from the app**. It's the anti-engagement feature. Copy reinforces that.

**Reads from**: current `progression.topic_axis` + `progression.next_step_hint` + entity hints from the week's activities

**§ 06 · Module · Gauges strip** _(NEW)_

Footer row with two small, ambient gauges:

(a) **Co-play share** — stacked horizontal bar showing proportions of `scaffold / co-explorer / observer` across the week's activities. No judgment copy; just a visible tally. Caption: *"This week you were mostly a co-explorer."*

(b) **Time this week** — minutes as a filled bar with a "healthy range" band. Band values default:

- T0: 20–60 min/week
- T1: 45–90 min/week
- T2: 60–120 min/week

In-band = neutral cream fill. Over band = subtle amber tint. Never red, never alarming. Caption example: *"Gentle amount this week." / "A little more than usual."*

**Reads from**: `caregiver_role` (list, per activity) aggregated over the window + session-duration telemetry

**§ 07 · Tag-block contract (full)**

Which fields the dashboard reads, grouped by module:

| Module | Fields |
|---|---|
| Progress (L×T ladder) | `progression.topic_axis`, `progression.difficulty_level`, `progression.next_step_hint`, `tier` |
| IB framework chips | `key_concepts`, `atl_skills`, `transdisciplinary_theme`, `subject_tags` |
| Curiosity profile | `key_concepts`, `progression.difficulty_level` (aggregate) |
| In their words | `highlight_moment`, opt-in child-utterance highlights |
| Try this at home | `progression.topic_axis`, `progression.next_step_hint`, recent `entity` |
| Gauges | `caregiver_role`, session-duration telemetry |

Explicitly **not read** on the parent dashboard: the child recap's `role_title` (that's child-facing identity, not parent-facing data).

**§ 08 · View cadence**

- Default view: weekly (rolling 7 days, Sun–Sat)
- Toggle to monthly (calendar month)
- Toggle to term (12 weeks)
- Empty states: if < 3 activities in the current window, show an onboarding-style "still getting to know Mia" copy instead of half-empty modules

**§ 09 · Privacy & data scope**

- Default data shown: `highlight_moment`, aggregate tag counts, session duration
- Opt-in (via onboarding setting): specific child utterance highlights in the "In their words" module
- Never shown: raw activity transcripts, other children's data, predictive scores
- Retention: rolling 12 months on the dashboard; archived beyond that

**§ 10 · Edge cases**

- New child (< 3 activities this week): collapse to "getting to know Mia" onboarding state
- Single-axis over-indexing: curiosity profile copy nudges toward a neighbor axis, "next to try"
- Demote streaks: do not surface as a negative; absorbed into the ladder state silently
- Multiple children on one account: each child has a separate dashboard; never cross-compared

**§ 11 · Out of scope**

- Cross-child comparisons (same account or other families)
- School-report export
- Notification cadence (push frequency, email digests) — separate product decision
- Activity-transcript drill-down view — needs its own design round
- Developmental-milestones ribbon — deferred (risk of parental anxiety)

---

## 6 · Cross-references & navigation

- Template 0 §05 reference strip links to `child_recap_preview.html` and `parent_growth_path_preview.html`
- Both new docs have a breadcrumb in the masthead: *"← Template 0 · reads tag block"*
- Both new docs have a "companion surface" link in the footer (child ↔ parent)
- Chinese versions link to Chinese versions, English to English

---

## 7 · Aesthetic & tooling constraints

- Both new docs are self-contained single HTML files (all CSS + JS inline) — matches Template 0's deployment model. Open any one directly in a browser without a build step.
- Copy Template 0's `:root` CSS custom properties verbatim so palette, type scale, and tier colors stay identical.
- Reuse Template 0's masthead pattern, `.hero` section structure, `§ NN / Section` heading treatment, `.subhead[data-dir]` subhead pattern, `.note-block` callout styling, `.revnote` revision-note pattern for the inaugural v0.1 note.
- Chinese versions follow existing CN doc conventions: natural Chinese prose (not word-by-word translation); technical terms (tag-block field names, tier IDs, IB terminology) kept in English; same fonts; same palette.
- Files served from `docs/` via the existing `launch.json` walkthrough preview server; no additional tooling needed.

---

## 8 · Verification checklist

Completion criteria for the implementation phase:

- [ ] `template_0_preview.html`: `.tagblock` stacks vertically on all viewports
- [ ] `template_0_preview.html`: §05 downstream mockups replaced with 2-card reference strip
- [ ] `template_0_preview.html`: revnote v0.2 has the "downstream surfaces extracted" bullet
- [ ] `template_0_preview_cn.html`: all three items above mirrored
- [ ] `docs/child_recap_preview.html` exists and matches the 10-section spec in §4
- [ ] `docs/child_recap_preview_cn.html` exists and mirrors the English version
- [ ] `docs/parent_growth_path_preview.html` exists and matches the 11-section spec in §5
- [ ] `docs/parent_growth_path_preview_cn.html` exists and mirrors the English version
- [ ] Reference strip in Template 0 §05 correctly links to both new docs
- [ ] Both new docs have masthead breadcrumb back to Template 0
- [ ] Both new docs have footer companion-link to each other
- [ ] All four new files share the same `:root` CSS custom properties as Template 0
- [ ] Preview server renders all four new files with no console errors
- [ ] Mobile layout (375×812) tested for all four new files

---

## 9 · Implementation plan

A detailed implementation plan (task order, file-by-file changes, agent-review gates) will be written separately via the writing-plans workflow once this spec is user-approved.
