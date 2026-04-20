# Progression Walkthrough Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development`. After each task, run **pr-review-toolkit:code-reviewer** + **pr-review-toolkit:code-simplifier**. Steps use checkbox (`- [ ]`).

**Goal:** Build `docs/template_0_progression_walkthrough.html` + `_cn.html` — 4 scenarios visualizing L1↔L2↔L3 transitions in action per §07 of Template 0. Cross-link from §07.

**Architecture:** One net-new preview doc (EN + CN), mirroring the aesthetic and token conventions of the existing walkthrough + surface docs. Small surgical edit to Template 0 §07 to add a "see walkthrough" cross-link. Pure HTML/CSS, no JS. Same editorial voice and bilingual parity discipline.

**Tech Stack:** Plain HTML + CSS in Template 0's existing token set. Preview via MCP Claude_Preview on port 8765. Worktree at `.worktrees/feat/progression-walkthrough/` (already created).

**Design authority:** `docs/plans/2026-04-20-progression-walkthrough-design.md`

---

## Task 1 · Base scaffold — masthead, intro, footer (EN)

**Spec reference:** design §4.1, §4.2, §4.5

**Files:**
- Create: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Scaffold the new file. Base it on the structure of `docs/template_0_lt_walkthrough.html` (the sibling walkthrough). Copy/adapt:
  - `<!DOCTYPE html>` + `<html lang="en">`
  - `<head>` with same meta tags, title, fonts, and base `<style>` block inheriting all `:root` tokens from Template 0 (copy the `:root` declaration and other foundational CSS rules from `lt_walkthrough.html` or `template_0_preview.html`)
  - Masthead with breadcrumb `← Template 0 · §07 Progression` linking to `template_0_preview.html#axes`
  - Masthead title: `Progression walkthrough · L1 ↔ L2 ↔ L3 in action`
  - Masthead `.meta` / version tag: `Draft v0.1 · 2026-04-20 · Internal review`

- [ ] **Step 2**: Add the intro section — 2–3 sentences framing this as illustration, not simulator. End with a compact legend:

```html
<section id="intro">
  <div class="sec-num">§ 00 / How to read this</div>
  <h2 class="sec-title">A child's journey through rungs — four scenarios.</h2>
  <p class="sec-desc">Template 0 §07 specifies WHEN the runtime promotes, holds, or demotes a child's rung on each axis. This doc shows WHAT that looks like for specific child journeys. Not a live simulator — hand-authored scenarios chosen to make the temporal dynamics concrete.</p>

  <dl class="legend-compact">
    <div class="lc-row"><dt>↑ promote</dt><dd>next rung up</dd></div>
    <div class="lc-row"><dt>· hold</dt><dd>same rung, next activity varies exemplar</dd></div>
    <div class="lc-row"><dt>↓ demote</dt><dd>drop one rung, same axis (dignity rule applies)</dd></div>
    <div class="lc-row"><dt>⇢ sibling jump</dt><dd>switch to related axis at L1</dd></div>
    <div class="lc-row"><dt>~ soft-reframe</dt><dd>same rung, different beat (not a demote)</dd></div>
  </dl>
</section>
```

Add CSS for `.legend-compact`, `.lc-row` (small grid, mono labels, cream body).

- [ ] **Step 3**: Add the revnote + version footer (same pattern as `child_recap_preview.html` + `parent_growth_path_preview.html`):

```html
<footer>
  <details class="revnote">
    <summary><span class="revnote-tag">v0.1</span> Inaugural draft · 2026-04-20</summary>
    <ol>
      <li>Four scenarios covering steady progression, hit-a-wall recovery (dignity rule + sibling jump), across-axis independence, and reluctance vs inability.</li>
      <li>Hand-authored — not a live simulator. Each scenario is a horizontal timeline of 5–8 activity cards with transition indicators and dialogue snippets on key events.</li>
      <li>Scenarios 5 (personalization hypothetical) and 6 (long arc) deferred to v0.2 — design captured in <code>docs/plans/2026-04-20-progression-walkthrough-design.md</code> §6.</li>
    </ol>
  </details>
  <div class="version">
    <span>Version 0.1 · Draft for review</span>
    <span>WonderLens x 奇朵 · Progression walkthrough · 2026-04-20</span>
  </div>
</footer>
```

Reuse `.revnote` + `.version` CSS from sibling docs.

- [ ] **Step 4**: Add a `<nav>` masthead TOC. Entries: `Intro / Scenario 1 / Scenario 2 / Scenario 3 / Scenario 4 / Rules`.

- [ ] **Step 5**: Verify scaffold renders. Load via preview server at http://localhost:8765/template_0_progression_walkthrough.html. Eval:

```js
({
  title: document.title,
  hasBreadcrumb: !!document.querySelector('.breadcrumb'),
  hasIntro: !!document.querySelector('#intro'),
  hasLegend: document.querySelectorAll('.legend-compact .lc-row').length,
  hasRevnote: !!document.querySelector('.revnote'),
  revnoteBullets: document.querySelectorAll('.revnote ol li').length,
  navLinks: document.querySelectorAll('nav a').length,
})
```

Expected: title set, breadcrumb, intro, 5 legend rows, revnote w/ 3 bullets, 6 nav links.

- [ ] **Step 6**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): scaffold doc with masthead, intro, legend, revnote footer"
```

---

## Task 2 · Scenario 1 — Steady progression (EN)

**Spec reference:** design §3.1, §5

**Files:**
- Modify: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Add the reusable activity-card + transition-indicator CSS to the file's `<style>` block. This CSS will be reused across scenarios 1–4.

```css
/* Activity card — the atomic unit of a scenario timeline */
.ac {
  flex: 0 0 240px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 16px;
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
  scroll-snap-align: start;
}
.ac-head {
  display: flex;
  justify-content: space-between;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}
.ac-num { color: var(--accent); }
.ac-entity {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--serif);
  font-size: 15px;
  color: var(--ink);
}
.ac-rungs {
  display: flex;
  align-items: center;
  gap: 8px;
}
.ac-rung {
  font-family: var(--mono);
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 2px;
  background: color-mix(in srgb, var(--accent) 15%, transparent);
  color: var(--accent);
  letter-spacing: 0.05em;
}
.ac-rung-arrow { color: var(--muted); font-family: var(--mono); }
.ac-outcome {
  font-size: 12px;
  line-height: 1.5;
  color: var(--ink-soft);
  flex-grow: 1;
}
.ac-trigger {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 0.04em;
  display: flex;
  gap: 6px;
  padding-top: 8px;
  border-top: 1px dashed var(--line);
}
.ac-trigger-glyph { color: var(--accent); font-weight: 600; }
.ac-detail { font-size: 11px; }
.ac-detail summary {
  cursor: pointer;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.ac-detail summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.ac-dialogue {
  padding: 8px 10px;
  margin-top: 6px;
  background: color-mix(in srgb, var(--accent) 5%, var(--bg));
  border-left: 2px solid var(--accent);
  font-family: var(--serif);
  font-style: italic;
  color: var(--ink-soft);
  line-height: 1.5;
}

/* Transition indicator between cards */
.transition {
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 0 8px;
  align-self: center;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.06em;
}
.transition .t-glyph { font-size: 18px; line-height: 1; }
.transition .t-label {
  text-transform: uppercase;
  color: var(--muted);
  max-width: 90px;
  text-align: center;
}
.transition[data-type="promote"] .t-glyph { color: var(--accent); }
.transition[data-type="hold"] .t-glyph { color: var(--muted); }
.transition[data-type="demote"] .t-glyph { color: var(--tier-0); }
.transition[data-type="sibling-jump"] .t-glyph { color: var(--accent); }
.transition[data-type="soft-reframe"] .t-glyph { color: var(--muted); }

/* Timeline container */
.timeline {
  display: flex;
  gap: 0;
  padding: 24px 0;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  align-items: stretch;
}

/* State panel */
.state-panel {
  margin-top: 16px;
  padding: 14px 18px;
  background: color-mix(in srgb, var(--accent) 4%, var(--bg));
  border-left: 2px solid var(--line);
  border-radius: 0 4px 4px 0;
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-soft);
}
.state-panel strong {
  font-family: var(--mono);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent);
  display: block;
  margin-bottom: 6px;
}
.state-panel code {
  font-size: 11px;
  color: var(--accent);
  background: color-mix(in srgb, var(--accent) 8%, transparent);
  padding: 1px 5px;
  border-radius: 2px;
}

/* Scenario wrapper */
.scenario {
  margin-top: 48px;
  scroll-margin-top: 80px;
}
.scenario-tldr {
  font-family: var(--serif);
  font-size: 15px;
  font-style: italic;
  color: var(--ink-soft);
  margin: 8px 0 14px;
}
.scenario-context {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 10px 0;
  border-top: 1px dashed var(--line);
  border-bottom: 1px dashed var(--line);
  margin-bottom: 8px;
}
.scenario-context strong {
  color: var(--accent);
  margin-right: 6px;
}
.scenario-close {
  margin-top: 18px;
  font-family: var(--serif);
  font-size: 14px;
  line-height: 1.55;
  color: var(--ink-soft);
  padding: 12px 16px;
  border-left: 2px solid var(--accent);
  background: color-mix(in srgb, var(--accent) 3%, var(--bg));
}
.scenario-close strong {
  font-family: var(--serif);
  color: var(--accent);
  margin-right: 6px;
}

/* Mobile collapse */
@media (max-width: 700px) {
  .timeline {
    flex-direction: column;
    gap: 8px;
  }
  .transition {
    flex-direction: row;
    justify-content: flex-start;
    width: 100%;
    padding: 4px 0;
  }
}
```

- [ ] **Step 2**: Add Scenario 1's HTML after the intro section, before the footer. Use the data from design §3.1:

```html
<section class="scenario" id="scenario-1">
  <div class="sec-num">§ 01 / Steady progression</div>
  <h2 class="sec-title">The baseline journey — most activities hold, promotions happen at natural breakpoints.</h2>
  <p class="scenario-tldr">Mia works the Form axis across 5 activities. She promotes L1 → L2 early, then holds steady through 3 L2 activities, earning the cross-activity promote to L3.</p>

  <div class="scenario-context">
    <span><strong>Child</strong>Mia · T1 · 4–6 yrs</span>
    <span><strong>Axis</strong>Form</span>
    <span><strong>Entity</strong>Ladybug → Butterfly → Sunflower</span>
  </div>

  <div class="timeline">
    <article class="ac" data-axis="form">
      <header class="ac-head">
        <span class="ac-num">Activity 1</span>
        <span class="ac-axis">Form</span>
      </header>
      <div class="ac-entity">🐞 Ladybug</div>
      <div class="ac-rungs">
        <span class="ac-rung">L1</span>
        <span class="ac-rung-arrow">→</span>
        <span class="ac-rung">L1</span>
      </div>
      <div class="ac-outcome">Named 4 attributes in 2 rounds without prompt-repeat.</div>
      <div class="ac-trigger">
        <span class="ac-trigger-glyph">·</span>
        <span>hold · solid L1, no spontaneous L+1 yet</span>
      </div>
    </article>

    <div class="transition" data-type="hold">
      <span class="t-glyph">·</span>
      <span class="t-label">hold</span>
    </div>

    <article class="ac" data-axis="form">
      <header class="ac-head">
        <span class="ac-num">Activity 2</span>
        <span class="ac-axis">Form</span>
      </header>
      <div class="ac-entity">🐞 Ladybug (new exemplar)</div>
      <div class="ac-rungs">
        <span class="ac-rung">L1</span>
        <span class="ac-rung-arrow">→</span>
        <span class="ac-rung">L1</span>
      </div>
      <div class="ac-outcome">Named 3 attributes, then spontaneously said "the spots are why birds don't eat it."</div>
      <div class="ac-trigger">
        <span class="ac-trigger-glyph">↑</span>
        <span>promote (next activity) · spontaneous L+1 response</span>
      </div>
    </article>

    <div class="transition" data-type="promote">
      <span class="t-glyph">↑</span>
      <span class="t-label">promote · next activity L2</span>
    </div>

    <article class="ac" data-axis="form">
      <header class="ac-head">
        <span class="ac-num">Activity 3</span>
        <span class="ac-axis">Form</span>
      </header>
      <div class="ac-entity">🦋 Butterfly</div>
      <div class="ac-rungs">
        <span class="ac-rung">L2</span>
        <span class="ac-rung-arrow">→</span>
        <span class="ac-rung">L2</span>
      </div>
      <div class="ac-outcome">Listed 4 attributes + pointed at one.</div>
      <div class="ac-trigger">
        <span class="ac-trigger-glyph">·</span>
        <span>hold · completing L2 successfully</span>
      </div>
    </article>

    <div class="transition" data-type="hold">
      <span class="t-glyph">·</span>
      <span class="t-label">hold</span>
    </div>

    <article class="ac" data-axis="form">
      <header class="ac-head">
        <span class="ac-num">Activity 4</span>
        <span class="ac-axis">Form</span>
      </header>
      <div class="ac-entity">🦋 Butterfly (second session)</div>
      <div class="ac-rungs">
        <span class="ac-rung">L2</span>
        <span class="ac-rung-arrow">→</span>
        <span class="ac-rung">L2</span>
      </div>
      <div class="ac-outcome">Listed 5 attributes, located each.</div>
      <div class="ac-trigger">
        <span class="ac-trigger-glyph">·</span>
        <span>hold · 2nd L2 success on Form</span>
      </div>
    </article>

    <div class="transition" data-type="hold">
      <span class="t-glyph">·</span>
      <span class="t-label">hold</span>
    </div>

    <article class="ac" data-axis="form">
      <header class="ac-head">
        <span class="ac-num">Activity 5</span>
        <span class="ac-axis">Form</span>
      </header>
      <div class="ac-entity">🌻 Sunflower</div>
      <div class="ac-rungs">
        <span class="ac-rung">L2</span>
        <span class="ac-rung-arrow">→</span>
        <span class="ac-rung">L2</span>
      </div>
      <div class="ac-outcome">Listed 6 attributes, located each, compared to butterfly.</div>
      <div class="ac-trigger">
        <span class="ac-trigger-glyph">↑</span>
        <span>cross-activity promote · 3 consecutive L2 successes</span>
      </div>
    </article>
  </div>

  <div class="state-panel">
    <strong>State after Scenario 1</strong>
    Form: <code>L1 → L1 → L2 → L2 → L2 → (L3 next)</code>
  </div>

  <div class="scenario-close">
    <strong>Why this matters:</strong> most activities in real use will look like this. Promotions happen at natural breakpoints (spontaneous L+1, or 3-session consecutive completion), not on every success. Holding is not stagnation — it's how the system gives exemplars room to vary while the child internalizes the rung.
  </div>
</section>
```

**Note on entity icons**: this plan uses emoji `🐞 🦋 🌻` as shorthand. The design spec forbids emojis. Replace with tiny inline SVGs OR with CSS-drawn pills containing just the entity NAME. During implementation, use text-only entity labels (`Ladybug`, `Butterfly`, `Sunflower`) with no emoji.

- [ ] **Step 3**: Verify. Load the page and eval:

```js
({
  scenarioExists: !!document.querySelector('#scenario-1'),
  activityCards: document.querySelectorAll('#scenario-1 .ac').length,
  transitions: document.querySelectorAll('#scenario-1 .transition').length,
  statePanel: !!document.querySelector('#scenario-1 .state-panel'),
  closeBlock: !!document.querySelector('#scenario-1 .scenario-close'),
})
```

Expected: 5 activity cards, 4 transitions, state panel + close block present.

- [ ] **Step 4**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): add Scenario 1 — steady progression (baseline) + timeline CSS"
```

---

## Task 3 · Scenario 2 — Hit-a-wall recovery (EN)

**Spec reference:** design §3.2

**Files:**
- Modify: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Add scenario 2 section after scenario 1. Use the full 6-activity sequence from design §3.2.

Core structure mirrors scenario 1 but adds TWO `<details class="ac-detail">` expansions with dialogue callouts — one on activity #2 (demote event) and one on activity #4 (sibling jump landing).

Activity #2 `<details>` content (verbatim from design):

```html
<details class="ac-detail">
  <summary>What happened here</summary>
  <div class="ac-dialogue-split">
    <div class="ac-dialogue-col">
      <div class="ac-dialogue-lbl">What the runtime recorded</div>
      <code>{"axis": "causation", "rung_change": "L2→L1", "trigger": "2_attempts_no_complete"}</code>
    </div>
    <div class="ac-dialogue-col">
      <div class="ac-dialogue-lbl">What Mia heard</div>
      <div class="ac-dialogue">"Hmm — let me show you what I notice about the ladybug's red. Then you can tell me what you notice."</div>
    </div>
  </div>
</details>
```

Activity #4 `<details>` content:

```html
<details class="ac-detail">
  <summary>What happened here</summary>
  <div class="ac-dialogue-split">
    <div class="ac-dialogue-col">
      <div class="ac-dialogue-lbl">What the runtime recorded</div>
      <code>{"axis_switch": "causation→connection", "rung": "L1", "trigger": "sibling_jump_on_axis_floor"}</code>
    </div>
    <div class="ac-dialogue-col">
      <div class="ac-dialogue-lbl">What Mia heard</div>
      <div class="ac-dialogue">"Look at all the things the ladybug touches — the grass, the leaf. Let's see how they all go together."</div>
    </div>
  </div>
</details>
```

- [ ] **Step 2**: Add CSS for `.ac-dialogue-split` + `.ac-dialogue-col` + `.ac-dialogue-lbl`:

```css
.ac-dialogue-split {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-top: 8px;
}
.ac-dialogue-col code {
  display: block;
  font-family: var(--mono);
  font-size: 10px;
  padding: 6px 8px;
  background: color-mix(in srgb, var(--accent) 6%, transparent);
  color: var(--accent);
  border-radius: 2px;
  word-break: break-all;
  line-height: 1.5;
}
.ac-dialogue-lbl {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 4px;
}
```

- [ ] **Step 3**: Multi-axis state panel for scenario 2:

```html
<div class="state-panel">
  <strong>Rung-per-axis evolution</strong>
  <div class="state-row">Start <code>{Form: L2, Causation: L2, Connection: L1}</code></div>
  <div class="state-row">After #3 <code>{Form: L2, Causation: L1, Connection: L1}</code> <em>— Causation hit floor</em></div>
  <div class="state-row">After #5 <code>{Form: L2, Causation: L1, Connection: L2}</code> <em>— Connection promoted via sibling jump</em></div>
  <div class="state-row">After #6 <code>{Form: L2, Causation: L2, Connection: L2}</code> <em>— Causation bounced back</em></div>
</div>
```

Add CSS for `.state-row`:

```css
.state-panel .state-row {
  display: flex;
  gap: 8px;
  align-items: center;
  padding: 4px 0;
  flex-wrap: wrap;
}
.state-panel .state-row em {
  font-family: var(--serif);
  font-style: italic;
  font-size: 11px;
  color: var(--muted);
}
```

- [ ] **Step 4**: Verify.

```js
({
  scenarioExists: !!document.querySelector('#scenario-2'),
  activityCards: document.querySelectorAll('#scenario-2 .ac').length,
  transitions: document.querySelectorAll('#scenario-2 .transition').length,
  dialogueSplits: document.querySelectorAll('#scenario-2 .ac-dialogue-split').length,
  statePanelRows: document.querySelectorAll('#scenario-2 .state-row').length,
})
```

Expected: 6 activity cards, 5 transitions, 2 dialogue splits (dignity + sibling jump), 4 state rows.

- [ ] **Step 5**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): add Scenario 2 — hit-a-wall recovery (dignity rule + sibling jump)"
```

---

## Task 4 · Scenario 3 — Across-axis independence (EN)

**Spec reference:** design §3.3

**Files:**
- Modify: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Add scenario 3 with 5 activities per design §3.3.

- [ ] **Step 2**: Add the **7-axis snapshot visual** showing axis-independence. Use a simple horizontal bar chart:

```html
<div class="axes-snapshot">
  <strong class="as-head">Rung across all 7 axes · snapshot after Scenario 3</strong>
  <div class="as-grid">
    <div class="as-row" data-rung="L3">
      <span class="as-name">Form</span>
      <span class="as-bar as-l3"></span>
      <span class="as-val">L3</span>
    </div>
    <div class="as-row" data-rung="L0">
      <span class="as-name">Function</span>
      <span class="as-bar as-l0"></span>
      <span class="as-val">—</span>
    </div>
    <div class="as-row" data-rung="L1">
      <span class="as-name">Causation</span>
      <span class="as-bar as-l1"></span>
      <span class="as-val">L1</span>
    </div>
    <div class="as-row" data-rung="L0">
      <span class="as-name">Change</span>
      <span class="as-bar as-l0"></span>
      <span class="as-val">—</span>
    </div>
    <div class="as-row" data-rung="L0">
      <span class="as-name">Connection</span>
      <span class="as-bar as-l0"></span>
      <span class="as-val">—</span>
    </div>
    <div class="as-row" data-rung="L0">
      <span class="as-name">Perspective</span>
      <span class="as-bar as-l0"></span>
      <span class="as-val">—</span>
    </div>
    <div class="as-row" data-rung="L1">
      <span class="as-name">Responsibility</span>
      <span class="as-bar as-l1"></span>
      <span class="as-val">L1</span>
    </div>
  </div>
  <p class="as-caption">There is no XP bar. There are 7 bars, and they drift independently.</p>
</div>
```

CSS for axes-snapshot:

```css
.axes-snapshot {
  margin-top: 18px;
  padding: 20px 24px;
  background: color-mix(in srgb, var(--accent) 3%, var(--bg));
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.as-head {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  display: block;
  margin-bottom: 14px;
}
.as-grid {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.as-row {
  display: grid;
  grid-template-columns: 130px 1fr 40px;
  align-items: center;
  gap: 10px;
}
.as-name {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--ink-soft);
  letter-spacing: 0.04em;
}
.as-bar {
  height: 6px;
  border-radius: 2px;
  background: var(--line);
  position: relative;
}
.as-l0 { background: var(--line); }
.as-l1 {
  background: linear-gradient(to right, color-mix(in srgb, var(--accent) 30%, transparent) 33%, var(--line) 33%);
}
.as-l2 {
  background: linear-gradient(to right, color-mix(in srgb, var(--accent) 60%, transparent) 66%, var(--line) 66%);
}
.as-l3 {
  background: color-mix(in srgb, var(--accent) 85%, transparent);
}
.as-val {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--accent);
  text-align: right;
}
.as-caption {
  margin-top: 14px;
  font-family: var(--serif);
  font-style: italic;
  font-size: 14px;
  color: var(--ink);
}
```

- [ ] **Step 3**: Verify.

```js
({
  scenarioExists: !!document.querySelector('#scenario-3'),
  activityCards: document.querySelectorAll('#scenario-3 .ac').length,
  axesSnapshot: !!document.querySelector('#scenario-3 .axes-snapshot'),
  axesRows: document.querySelectorAll('#scenario-3 .as-row').length,
  caption: document.querySelector('#scenario-3 .as-caption')?.innerText.includes('no XP bar'),
})
```

Expected: 5 activity cards, axes snapshot exists, 7 axis rows, caption present.

- [ ] **Step 4**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): add Scenario 3 — across-axis independence + 7-axis snapshot"
```

---

## Task 5 · Scenario 4 — Reluctance vs inability (EN)

**Spec reference:** design §3.4

**Files:**
- Modify: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Add scenario 4 with 3 activities per design §3.4.

- [ ] **Step 2**: Add a **dedicated side-box** calling out the soft-reframe vs demote distinction (this is the scenario's load-bearing insight):

```html
<aside class="distinction-box">
  <div class="db-head">Silence ≠ Demote</div>
  <div class="db-body">
    <p><strong>A demote requires 2 attempts</strong> — silence <em>plus</em> off-topic wander <em>plus</em> repeat-prompt-back. A single silence after a correct response is often just the child thinking, resting, or needing a gentler re-entry.</p>
    <p>The runtime has a separate <strong>soft-reframe</strong> move for this — it's a beat-level adjustment within the activity, NOT a rung change.</p>
  </div>
  <div class="db-compare">
    <div class="db-col db-demote">
      <span class="db-col-label">Demote</span>
      <span class="db-col-text">Child's cognitive state genuinely mismatches the rung. Drop.</span>
    </div>
    <div class="db-col db-soft">
      <span class="db-col-label">Soft-reframe</span>
      <span class="db-col-text">Child's emotional / attention state needs a breath. Same rung, softer prompt.</span>
    </div>
  </div>
</aside>
```

CSS:

```css
.distinction-box {
  margin-top: 18px;
  padding: 20px 24px;
  background: color-mix(in srgb, var(--accent) 4%, var(--bg));
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.db-head {
  font-family: var(--serif);
  font-size: 18px;
  color: var(--accent);
  margin-bottom: 10px;
}
.db-body p {
  font-size: 13px;
  line-height: 1.6;
  color: var(--ink-soft);
  margin: 6px 0;
}
.db-compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 14px;
}
.db-col {
  padding: 12px 14px;
  border-radius: 4px;
}
.db-demote {
  background: color-mix(in srgb, var(--tier-0) 10%, transparent);
  border-left: 2px solid var(--tier-0);
}
.db-soft {
  background: color-mix(in srgb, var(--muted) 10%, transparent);
  border-left: 2px solid var(--muted);
}
.db-col-label {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  display: block;
  margin-bottom: 6px;
}
.db-col-text {
  font-size: 13px;
  line-height: 1.5;
  color: var(--ink-soft);
}
@media (max-width: 700px) {
  .db-compare { grid-template-columns: 1fr; }
}
```

- [ ] **Step 3**: Verify.

```js
({
  scenarioExists: !!document.querySelector('#scenario-4'),
  activityCards: document.querySelectorAll('#scenario-4 .ac').length,
  distinctionBox: !!document.querySelector('#scenario-4 .distinction-box'),
  distinctionCols: document.querySelectorAll('#scenario-4 .db-col').length,
})
```

Expected: 3 activity cards, distinction-box exists, 2 comparison columns.

- [ ] **Step 4**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): add Scenario 4 — reluctance vs inability + demote/soft-reframe distinction"
```

---

## Task 6 · Three-rules summary block (EN)

**Spec reference:** design §4.4

**Files:**
- Modify: `docs/template_0_progression_walkthrough.html`

- [ ] **Step 1**: Add a summary block AFTER scenario 4 and BEFORE the footer. Pulls out the three footer rules from §07, each with a one-sentence restatement + callout of the scenario where it showed up.

```html
<section class="scenario" id="rules">
  <div class="sec-num">§ 05 / The three rules · one place</div>
  <h2 class="sec-title">What the scenarios demonstrated, restated.</h2>

  <div class="rules-grid">
    <div class="rule-card">
      <div class="rule-head">Dignity rule</div>
      <p class="rule-body">A demote is never surfaced as failure. Language switches from "let's try again" to "let me show you what I notice first." The child experiences variety, not regression.</p>
      <div class="rule-shown">↑ shown in Scenario 2, Activity 2</div>
    </div>

    <div class="rule-card">
      <div class="rule-head">Sibling jump</div>
      <p class="rule-body">When a child hits L3 on an axis, the next activity can pivot to L1 on a <em>related</em> axis (Form L3 → Connection L1) instead of forcing L3 elsewhere. Keeps novelty without pushing depth faster than the child can absorb. Also applies inversely — when stuck at floor L1 on an axis, jump to a related axis at L1.</p>
      <div class="rule-shown">↑ shown in Scenario 2, Activity 3 → 4</div>
    </div>

    <div class="rule-card">
      <div class="rule-head">Personalization hook</div>
      <p class="rule-body">The thresholds above (2-for-promote, 2-for-demote, 3-for-cross-activity-promote) are a <code>progression_policy</code> object in the upstream catalog config — not hardcoded. V1 uses these defaults. Once ≥ ~200 sessions per child are logged, a per-child pace model can swap in <strong>without any activity design change</strong>.</p>
      <div class="rule-shown">— foundational · applies to every scenario</div>
    </div>
  </div>
</section>
```

CSS:

```css
.rules-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
  margin-top: 18px;
}
.rule-card {
  padding: 20px 22px;
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.rule-head {
  font-family: var(--serif);
  font-size: 18px;
  color: var(--accent);
  margin-bottom: 10px;
}
.rule-body {
  font-size: 13px;
  line-height: 1.6;
  color: var(--ink-soft);
  margin: 0 0 14px;
}
.rule-body code {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--accent);
  padding: 1px 4px;
  background: color-mix(in srgb, var(--accent) 6%, transparent);
  border-radius: 2px;
}
.rule-shown {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  padding-top: 10px;
  border-top: 1px dashed var(--line);
}
@media (max-width: 960px) {
  .rules-grid { grid-template-columns: 1fr; }
}
```

- [ ] **Step 2**: Verify.

```js
({
  rulesSection: !!document.querySelector('#rules'),
  ruleCards: document.querySelectorAll('#rules .rule-card').length,
})
```

Expected: rules section + 3 rule cards.

- [ ] **Step 3**: Commit.

```bash
git add docs/template_0_progression_walkthrough.html
git commit -m "feat(progression-walkthrough): add three-rules summary block (dignity / sibling jump / personalization hook)"
```

---

## Task 7 · CN mirror

**Spec reference:** all design sections

**Files:**
- Create: `docs/template_0_progression_walkthrough_cn.html`

- [ ] **Step 1**: Copy the full EN file to the CN filename, then translate all prose.

Hard constraints:
- `<html lang="zh-Hans">`
- All YAML-like tokens stay English: `L1`, `L2`, `L3`, `Form`, `Causation`, `Connection`, `Change`, `Perspective`, `Responsibility`, `Function`, axis names, `progression_policy`, `axis_switch`, `rung_change`, trigger JSON keys
- Dialogue snippets (what Mia heard) translated naturally to child-voice CN
- Runtime-recorded JSON stays English in both locales (it's code, not prose)

Key translations:

| EN | CN |
|---|---|
| Progression walkthrough · L1 ↔ L2 ↔ L3 in action | 进阶过程演示 · L1 ↔ L2 ↔ L3 在实际中如何运作 |
| How to read this | 如何阅读本文 |
| A child's journey through rungs — four scenarios. | 一个孩子在阶梯上的旅程 — 四个场景。 |
| promote | 晋级 |
| hold | 保持 |
| demote | 回退 |
| sibling jump | 跳到相邻轴 |
| soft-reframe | 温和换场 |
| Steady progression | 平稳推进 |
| Hit-a-wall recovery | 撞墙后的恢复 |
| Across-axis independence | 各轴独立 |
| Reluctance vs inability | 不想 vs 不能 |
| What the runtime recorded | 运行时记录 |
| What Mia heard | 米娅听到的 |
| There is no XP bar. There are 7 bars, and they drift independently. | 没有经验条。有七根条，它们各自独立推移。 |
| Silence ≠ Demote | 沉默 ≠ 回退 |
| Dignity rule | 尊严原则 |
| Sibling jump | 相邻轴跳转 |
| Personalization hook | 个性化接口 |

Mia dialogue — scenario 2 activity #2 demote event:

> EN: "Hmm — let me show you what I notice about the ladybug's red. Then you can tell me what you notice."
> CN: "嗯——我先给你看看我看到瓢虫的红色。然后你告诉我你看到了什么。"

Mia dialogue — scenario 2 activity #3→#4 sibling jump:

> EN: "Look at all the things the ladybug touches — the grass, the leaf. Let's see how they all go together."
> CN: "看看瓢虫碰到的所有东西——草、叶子。我们来看看它们怎么连在一起。"

- [ ] **Step 2**: Parity check via grep:

```bash
grep -c "class=\"ac\"" docs/template_0_progression_walkthrough.html docs/template_0_progression_walkthrough_cn.html
grep -c "class=\"transition\"" docs/template_0_progression_walkthrough.html docs/template_0_progression_walkthrough_cn.html
grep -c "class=\"state-panel\"" docs/template_0_progression_walkthrough.html docs/template_0_progression_walkthrough_cn.html
grep -c "class=\"scenario\"" docs/template_0_progression_walkthrough.html docs/template_0_progression_walkthrough_cn.html
grep -c "class=\"rule-card\"" docs/template_0_progression_walkthrough.html docs/template_0_progression_walkthrough_cn.html
```

Expected: EN and CN counts identical for each class.

- [ ] **Step 3**: Verify CN in the browser.

```js
({
  htmlLang: document.documentElement.lang,
  scenarios: document.querySelectorAll('.scenario').length,
  activityCards: document.querySelectorAll('.ac').length,
  rulesCards: document.querySelectorAll('.rule-card').length,
  hasYAMLTokensEnglish: document.body.innerText.includes('L1') && document.body.innerText.includes('progression_policy'),
})
```

Expected: `htmlLang: "zh-Hans"`, scenarios ≥ 5 (intro/§01–§04/rules), activity cards = 19 (5+6+5+3), rule cards = 3, YAML tokens English.

- [ ] **Step 4**: Commit.

```bash
git add docs/template_0_progression_walkthrough_cn.html
git commit -m "feat(progression-walkthrough-cn): full CN mirror — 4 scenarios + rules summary translated"
```

---

## Task 8 · Template 0 §07 cross-link (EN + CN)

**Files:**
- Modify: `docs/template_0_preview.html`
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1**: Find §07's "Promotion & demotion" subhead in EN (around line 4272). Add a cross-link subhead block immediately AFTER the `trans-foot` block (the three-rules footer at ~line 4313–4328).

```html
<div class="walkthrough-link">
  <span class="wl-eyebrow">For a visual walkthrough</span>
  <a class="wl-link" href="template_0_progression_walkthrough.html">
    4 scenarios showing these rules in action →
  </a>
  <p class="wl-body">Steady progression · hit-a-wall recovery · across-axis independence · reluctance vs inability. Each with dialogue snippets on key events.</p>
</div>
```

CSS (add to Template 0's style block):

```css
.walkthrough-link {
  margin: 24px 0 8px;
  padding: 20px 24px;
  background: color-mix(in srgb, var(--accent) 5%, var(--bg));
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.wl-eyebrow {
  display: block;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
}
.wl-link {
  font-family: var(--serif);
  font-size: 20px;
  color: var(--accent);
  text-decoration: none;
  border-bottom: 1px solid var(--accent);
}
.wl-link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
.wl-body {
  margin-top: 10px;
  font-size: 13px;
  line-height: 1.55;
  color: var(--ink-soft);
}
```

- [ ] **Step 2**: Mirror in CN file with translations:

```html
<div class="walkthrough-link">
  <span class="wl-eyebrow">可视化演示</span>
  <a class="wl-link" href="template_0_progression_walkthrough_cn.html">
    四个场景 · 这些规则在实际中如何运作 →
  </a>
  <p class="wl-body">平稳推进 · 撞墙后的恢复 · 各轴独立 · 不想 vs 不能。每个场景在关键节点附有对话摘录。</p>
</div>
```

- [ ] **Step 3**: Verify both Template 0 files:

```js
({
  walkthroughLink: !!document.querySelector('.walkthrough-link'),
  linkHref: document.querySelector('.wl-link')?.getAttribute('href'),
})
```

EN expects `template_0_progression_walkthrough.html`; CN expects `template_0_progression_walkthrough_cn.html`.

- [ ] **Step 4**: Commit.

```bash
git add docs/template_0_preview.html docs/template_0_preview_cn.html
git commit -m "feat(template-0): cross-link §07 to progression walkthrough doc"
```

---

## Task 9 · Verification pass

**Files:** (no edits)

- [ ] **Step 1**: Desktop 1280×1000. For each of the 4 files affected:
  - `docs/template_0_progression_walkthrough.html`
  - `docs/template_0_progression_walkthrough_cn.html`
  - `docs/template_0_preview.html` (cross-link landed)
  - `docs/template_0_preview_cn.html` (cross-link mirror)

Eval (for walkthrough doc):

```js
({
  title: document.title,
  lang: document.documentElement.lang,
  scenarios: document.querySelectorAll('.scenario').length,
  activityCards: document.querySelectorAll('.ac').length,
  transitions: document.querySelectorAll('.transition').length,
  ruleCards: document.querySelectorAll('.rule-card').length,
  dialogueSplits: document.querySelectorAll('.ac-dialogue-split').length,
  revnoteBullets: document.querySelectorAll('.revnote ol li').length,
})
```

Expected (both EN/CN):
- scenarios: 5 (intro, 4 scenarios, rules)  OR just count `.scenario` class which excludes intro; pick one counting rule and apply consistently
- activityCards: 19 (5 + 6 + 5 + 3)
- transitions: 4 + 5 + 4 + 2 = 15
- ruleCards: 3
- dialogueSplits: 2 (both in Scenario 2)
- revnoteBullets: 3

For Template 0 docs: `walkthroughLink` present; href correctly locale-scoped.

- [ ] **Step 2**: Mobile 375×812 — confirm no horizontal overflow in either walkthrough file. Timelines should collapse to vertical.

- [ ] **Step 3**: Console clean on all 4 files.

- [ ] **Step 4**: EN/CN structural parity. Grep counts must match across locale pairs.

- [ ] **Step 5**: Cross-link smoke test:
  - Load Template 0 EN, scroll to §07, verify the walkthrough-link block visible, click → lands on walkthrough EN
  - From walkthrough EN, click breadcrumb → lands back on Template 0 §07
  - Repeat for CN chain

- [ ] **Step 6**: No commit (verification-only).

---

## Task 10 · Push + PR

**Files:** (git operations)

- [ ] **Step 1**: Confirm clean working tree.

- [ ] **Step 2**: Fetch origin + rebase if needed.

```bash
git fetch origin
git rebase origin/main
```

- [ ] **Step 3**: Push.

```bash
git push -u origin feat/progression-walkthrough
```

- [ ] **Step 4**: Open PR.

```bash
gh pr create --base main --title "Progression walkthrough — L1↔L2↔L3 in action (v0.1)" --body "$(cat <<'EOF'
## Summary

New companion preview doc showing Template 0 §07's promotion/demotion rules applied to specific child journeys. Addresses the gap that the §07 prose describes the rules but can't make the temporal dynamics visceral.

- **Four scenarios**: steady progression, hit-a-wall recovery (dignity rule + sibling jump), across-axis independence, reluctance vs inability
- **Hand-authored, not a live simulator** — keeps scope tight and avoids codifying transitional v1 thresholds as permanent
- **Dialogue snippets** on demote / sibling-jump events make the dignity rule visible, not just described
- **7-axis snapshot** in Scenario 3 kills the "one global rung" intuition

## Files

- `docs/template_0_progression_walkthrough.html` (new)
- `docs/template_0_progression_walkthrough_cn.html` (new)
- `docs/template_0_preview.html` — cross-link added in §07
- `docs/template_0_preview_cn.html` — cross-link mirror
- Design spec + implementation plan ship with the PR

## Design spec

`docs/plans/2026-04-20-progression-walkthrough-design.md`

## Test plan

- [x] Desktop + mobile preview on all 4 files
- [x] Console clean
- [x] EN/CN structural parity
- [x] Cross-link Template 0 §07 ↔ walkthrough works in both locales
- [x] All 4 scenarios render with correct card count (5 / 6 / 5 / 3) + transitions + state panels

## Out of scope (v0.2+)

- Scenario 5 (personalization hypothetical) — split view V1 vs per-child pace model
- Scenario 6 (long arc) — 12+ sessions compressed, ties to parent dashboard curiosity radial
- Live simulator / parameter tweaking

## Depends on

Template 0 v0.3 (§07 transition rules are the spec this visualizes).
EOF
)"
```

- [ ] **Step 5**: Note PR URL.

---

## Task 11 · Final cross-branch review

Dispatch `pr-review-toolkit:code-reviewer` on the whole branch. Focus on:

- Cross-file consistency (tokens, class-naming, aesthetic harmony with sibling walkthroughs)
- EN/CN parity walk (structural counts, translations, token preservation)
- Fidelity to §07 rules (triggers, dignity rule language, sibling jump, personalization hook)
- Accessibility (focus-visible, heading hierarchy, semantic HTML)
- Mobile rendering
- Overall coherence — does it feel like part of the doc family or an outlier?

Address any Important items with one fixup commit. Nits optional.

---

## Execution notes

- **Per-task cadence**: implementer → pr-review-toolkit:code-reviewer → pr-review-toolkit:code-simplifier → fixups. Same pattern as matchability-tags.
- **Don't run reviews in parallel for the first 2 tasks** — Task 2 establishes reusable CSS (activity-card + transition). Review carefully so tasks 3–5 inherit a stable foundation.
- **Tasks 3–5 can share CSS review** — if card shape works in scenario 2, it works in 3 and 4. Simplifier should look for dedupe opportunities at that point.
- **Task 7 (CN mirror)** is the main parity-drift risk — CN translation quality of child dialogue is the key review gate.
- **Commit hygiene**: every task = one `feat:` or `feat(scope):` commit. Fixups = separate `fix:` or `refactor:` commits. Don't squash away the review story.
- **EN/CN split**: keep EN and CN tasks separated (as in tasks 2–6 EN-only, then task 7 CN-all). Cleaner review than trying to build both in lockstep per scenario.

Good candidate for `superpowers:subagent-driven-development`.
