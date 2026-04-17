# Downstream Surfaces Split — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract child recap and parent growth path out of Template 0's §05 into their own full-fidelity preview HTML docs (+ Chinese versions), per design spec `docs/plans/2026-04-17-downstream-surfaces-split-design.md`.

**Architecture:** Six static self-contained HTML files. Two existing files (`template_0_preview.html` + `_cn`) get surgical edits — a CSS layout tweak, a §05 rewrite into a compact reference strip, and a revnote bullet. Four new files (`child_recap_preview.html` + `_cn`, `parent_growth_path_preview.html` + `_cn`) are authored from copy-of-Template-0 scaffolds so they inherit the `:root` custom properties, masthead pattern, section numbering (`§ NN / Section`), and type scale verbatim. All preview verification runs through the existing `launch.json` walkthrough server on port 8765.

**Tech Stack:** Static HTML5, CSS custom properties, CSS Grid, `<details>/<summary>` for collapsibles, minimal vanilla JS (only for module toggles on the parent dashboard). No build step. Fraunces (serif) + IBM Plex Sans/Mono (body/mono) via Google Fonts (same as Template 0).

**Spec reference:** Every task that authors content cites the corresponding spec section. Read the spec first, then the task.

---

## Pre-flight · conventions

- **Worktree**: All work happens in `.worktrees/feat/downstream-surfaces-split/` per repo convention.
- **Commit cadence**: One commit per completed task. Conventional commit prefix: `feat:` for new files, `refactor:` for the Template 0 edits, `docs:` for cross-links.
- **Preview server**: Start once via `mcp__Claude_Preview__preview_start("walkthrough")`, leave running across tasks. Each verification step resizes / navigates instead of restarting.
- **EN + CN parity**: For every authored section, EN first, then mirror in CN. Keep them in the same commit so drift can't accumulate.
- **No new dependencies**: Everything is inline CSS + inline JS. No npm, no build.

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `docs/template_0_preview.html` | Modify | Tag-block layout tweak (§3.1 spec), §05 reference strip (§3.2), revnote bullet (§3.3) |
| `docs/template_0_preview_cn.html` | Modify | Mirror of above in Chinese |
| `docs/child_recap_preview.html` | Create | Full child-recap design doc, 10 sections per spec §4 |
| `docs/child_recap_preview_cn.html` | Create | Chinese mirror |
| `docs/parent_growth_path_preview.html` | Create | Full parent-dashboard design doc, 11 sections per spec §5 |
| `docs/parent_growth_path_preview_cn.html` | Create | Chinese mirror |

Approach to authoring the 4 new files: **clone Template 0's HTML as starter, strip §03-§09 content but keep the `:root`, masthead, fixed-header script, and section scaffolding**. This guarantees aesthetic parity with zero CSS duplication effort. Each new doc is then built section-by-section.

---

## Task 1 · Create worktree + preview server

**Files:** (no file edits)

- [ ] **Step 1**: Create worktree from current branch.

```bash
git worktree add -b feat/downstream-surfaces-split .worktrees/feat/downstream-surfaces-split HEAD
cd .worktrees/feat/downstream-surfaces-split
```

- [ ] **Step 2**: Confirm `.claude/launch.json` exists in the worktree (created earlier) and points to `docs/`.

```bash
cat .claude/launch.json
```

Expected: shows the `walkthrough` config with `docs` as the served directory.

- [ ] **Step 3**: Start preview server.

Use `mcp__Claude_Preview__preview_start` with `name: "walkthrough"`. Confirm server running on port 8765.

- [ ] **Step 4**: Verify Template 0 loads.

Navigate to `http://localhost:8765/template_0_preview.html`. Eval `document.title` — expect `"Template 0 · WonderLens Activity Design — Internal Review"`.

- [ ] **Step 5**: No commit yet — setup-only task.

---

## Task 2 · Template 0 · tag-block layout tweak

**Spec reference**: §3.1

**Files:**
- Modify: `docs/template_0_preview.html` (CSS `.tagblock` rule around line 608; mobile media query override around line 2087)
- Modify: `docs/template_0_preview_cn.html` (same rules in CN file)

- [ ] **Step 1**: Edit EN. Change `.tagblock` from two-column to single-column:

Find the current rule:

```css
.tagblock {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 40px;
  align-items: start;
}
```

Replace with:

```css
.tagblock {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  align-items: start;
}
```

- [ ] **Step 2**: In the same EN file, remove the now-redundant mobile media query override:

```css
@media (max-width: 900px) {
  .tagblock {
    grid-template-columns: 1fr;
  }
  ...
}
```

Delete only the `.tagblock { grid-template-columns: 1fr; }` rule from inside the `@media` block. Keep the other rules in that `@media` block (there are sibling rules like `.dials { grid-template-columns: 1fr; }` — those stay).

- [ ] **Step 3**: Mirror both edits in `docs/template_0_preview_cn.html`. Exact same find/replace.

- [ ] **Step 4**: Verify EN.

Navigate preview to `http://localhost:8765/template_0_preview.html#tags`. Eval:

```js
(() => {
  const el = document.querySelector('.tagblock');
  const s = getComputedStyle(el);
  return { cols: s.gridTemplateColumns, childCount: el.children.length };
})()
```

Expected: single column value (e.g. `"1040px"` — one column the viewport width). Child count should be 2 (code panel + legend).

- [ ] **Step 5**: Verify CN. Navigate to `http://localhost:8765/template_0_preview_cn.html#tags`. Run same eval. Same result expected.

- [ ] **Step 6**: Commit.

```bash
git add docs/template_0_preview.html docs/template_0_preview_cn.html
git commit -m "refactor(template-0): stack tag-block legend below YAML on all viewports"
```

---

## Task 3 · Child recap · scaffold from Template 0

**Spec reference**: §4.2, §4.3 §01

**Files:**
- Create: `docs/child_recap_preview.html`
- Create: `docs/child_recap_preview_cn.html`

- [ ] **Step 1**: Copy Template 0 as the starter.

```bash
cp docs/template_0_preview.html docs/child_recap_preview.html
cp docs/template_0_preview_cn.html docs/child_recap_preview_cn.html
```

- [ ] **Step 2**: In `child_recap_preview.html`, update the following:

- `<title>` → `Child recap · WonderLens Activity Design`
- `.brand` text → `WonderLens · Child recap design`
- Header nav `<a>` items → replace with placeholders for this doc's sections (we'll fill real anchors as sections are added): start with just two items, `<a href="#purpose">Purpose</a>` and `<a href="#anti-addiction">Anti-addiction</a>`.
- `.meta` in masthead → `Draft v0.1 · 2026-04-17 · Internal review`
- Breadcrumb: **add** a new element inside the masthead, right after `.brand`:

```html
<span class="breadcrumb">← <a href="template_0_preview.html">Template 0</a> · reads tag block</span>
```

Add the CSS for `.breadcrumb` (next to the existing `.brand` CSS rules):

```css
.breadcrumb {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  color: var(--muted);
  text-transform: uppercase;
  margin-left: 16px;
}
.breadcrumb a {
  color: var(--accent);
  text-decoration: none;
}
.breadcrumb a:hover { text-decoration: underline; }

@media (max-width: 700px) {
  .breadcrumb { display: none; }
}
```

- [ ] **Step 3**: In `child_recap_preview.html`, strip out the sections that don't belong. Delete the `<section>` elements for the following IDs:
  - `concerns`, `spine`, `skeleton`, `tags`, `bridges`, `tiers`, `axes`, `overlays`, `decisions`

Keep: `<header class="masthead">`, the hero `<section>` (we'll rewrite its content in step 4), the `<footer>`, and the `<script>` block (we'll trim script later).

- [ ] **Step 4**: Rewrite the hero section content.

Replace the hero's `<h1>` and descriptive `<p>` and `.hero-meta` with:

```html
<section class="hero">
  <div class="eyebrow">Surface · 1 of 2 · post-activity</div>
  <h1>What the child<br />sees <em>at the end</em>.</h1>
  <p class="lede">
    This doc specifies the post-activity screen — the one the child sees when beat 5 ends.
    Its job is to <b>celebrate the specific cognitive act</b> the child just performed
    and leave them with a <b>warm, bounded ending</b>. Explicitly not to hook them into
    another session.
  </p>
  <div class="hero-meta">
    <div>
      <span class="label">Reads from</span>
      <span class="value">Template 0 tag block</span>
    </div>
    <div>
      <span class="label">Consumers</span>
      <span class="value">The child · post-activity</span>
    </div>
    <div>
      <span class="label">Stance</span>
      <span class="value">Anti-addiction by design</span>
    </div>
    <div>
      <span class="label">Status</span>
      <span class="value">Draft v0.1 · pending sign-off</span>
    </div>
  </div>
</section>
```

- [ ] **Step 5**: Remove any `<script>` logic that references removed sections (tier tabs, axis tabs, spine overlay toggle, comment system, skeleton collapse). Keep only the fixed-header script logic if it exists; otherwise leave the `<script>` block empty.

Search the `<script>` block for references to `.tier-tab`, `.axis-btn`, `.spine-toggle`, `.axis-btn`, etc., and delete those handler blocks.

- [ ] **Step 6**: Add a **§01 Purpose** section after the hero. Content per spec §4.3 §01.

```html
<section id="purpose">
  <div class="sec-head">
    <div class="sec-num">§ 01 / Purpose &amp; stance</div>
    <h2 class="sec-title">A <em>warm ending</em>,<br />not a hook.</h2>
  </div>
  <p class="sec-desc">The recap screen has exactly one job: reflect back what the child just did, in language the child can feel. It is not a dashboard. It is not a streak tracker. It is not a reason to play again right now.</p>

  <div class="note-block">
    <strong>What this screen does.</strong> Names the specific cognitive move the child just made (the <code>highlight_moment</code>). Shows the concepts they touched (child-friendly words, never IB terminology). Gives a soft sign-off tailored to the tier.
  </div>

  <div class="note-block" style="border-left-color: var(--tier-1); background: color-mix(in srgb, var(--tier-1) 6%, var(--bg));">
    <strong>What this screen explicitly doesn't do.</strong> No streaks, no daily-goal rings, no "N more until the next level", no rarity tiers, no push notifications, no infinite scroll, no peer comparison, no push toward another session.
  </div>
</section>
```

- [ ] **Step 7**: Mirror all of Steps 2-6 in `docs/child_recap_preview_cn.html` with Chinese copy. Natural Chinese prose; technical terms (tag-block field names like `highlight_moment`) kept in English. Example hero translation:

```html
<h1>活动结束时，<br />孩子<em>看到的</em>那一屏。</h1>
<p class="lede">
  这份文档界定活动结束后（beat 5 之后）孩子看到的那一屏。
  它的任务是<b>肯定孩子刚刚做到的那个具体认知动作</b>，
  给孩子一个<b>温暖、有边界的收尾</b>。不是把孩子拽回下一局。
</p>
```

For §01 CN content, follow the pattern established in `template_0_preview_cn.html` §01.

- [ ] **Step 8**: Verify EN.

Navigate preview to `http://localhost:8765/child_recap_preview.html`. Eval:

```js
({
  title: document.title,
  brand: document.querySelector('.brand')?.innerText,
  heroH1: document.querySelector('.hero h1')?.innerText,
  purposeExists: !!document.querySelector('#purpose'),
  noteBlocks: document.querySelectorAll('#purpose .note-block').length,
})
```

Expected: title says "Child recap", brand says "WonderLens · Child recap design", hero H1 contains "warm ending", `#purpose` exists, 2 note blocks.

- [ ] **Step 9**: Verify CN. Same pattern at `/child_recap_preview_cn.html`.

- [ ] **Step 10**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html
git commit -m "feat(child-recap): scaffold doc with masthead, hero, and §01 purpose"
```

---

## Task 4 · Child recap · §02 anti-addiction principles & mechanisms

**Spec reference**: §4.3 §02

This is the defining section of the doc — treat it as the hero of the doc's middle.

**Files:**
- Modify: `docs/child_recap_preview.html`
- Modify: `docs/child_recap_preview_cn.html`

- [ ] **Step 1**: In EN, add a new `<section id="anti-addiction">` immediately after `#purpose`.

Structure:
- `.sec-head` with `§ 02 / Principles` eyebrow and title "Eight patterns,<br />eight <em>refusals</em>."
- `.sec-desc` explaining the lens: "These are anti-patterns standard to ed-tech. We refuse each deliberately."
- A styled table containing the 8 rows (pattern / why it hurts / our stance). Use a new class `.anti-table` with the same editorial aesthetic as `.mapping-table` in Template 0.
- A `.mechanisms-block` containing 8 numbered list items — each with a short title and 1–3 sentence description.

Table content — verbatim from spec §4.3 §02 (a):

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

Mechanisms — 8 items verbatim from spec §4.3 §02 (b):

1. **Bounded badge universe** — 7 axes × 3 rungs = 21 slots. Fixed from day 1; no mystery / locked slots.
2. **Mastery display, not tally display** — depth per axis (filling bar L1→L2→L3), not a pile of medals.
3. **`highlight_moment` is hero, badges are ambient** — the runtime-generated one-liner is large and serif; badges are secondary with no sparkles / pops / animation.
4. **Soft session cap** — after N activities in one sitting (T0: 2, T1: 3, T2: 4), the recap ends with "Good thinking today. See you tomorrow." App doesn't lock.
5. **Replay is welcomed, not re-earned** — second playthrough of same entity celebrates the new noticing, doesn't mint a new badge.
6. **No streaks UI, anywhere** — not hidden, not built.
7. **Exit with warmth, not a hook** — end on an invitation to look at the real world; never "tap to continue" or "N more until Level M."
8. **Opt-in history** — earned badges live on a separate collection screen. Never pushed.

- [ ] **Step 2**: Add CSS for `.anti-table` and `.mechanisms-block`.

```css
.anti-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 24px;
  font-size: 13px;
}

.anti-table th,
.anti-table td {
  padding: 14px 18px;
  text-align: left;
  vertical-align: top;
  border-bottom: 1px dashed var(--line);
  line-height: 1.55;
}

.anti-table th {
  font-family: var(--mono);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent);
  font-weight: 500;
  padding-bottom: 10px;
}

.anti-table tbody tr:hover {
  background: color-mix(in srgb, var(--accent) 4%, transparent);
}

.anti-table .pattern {
  font-family: var(--serif);
  font-size: 15px;
  color: var(--ink);
  font-weight: 500;
  min-width: 180px;
}

.anti-table .stance {
  color: var(--accent);
  font-weight: 500;
}

.mechanisms-block {
  margin-top: 40px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

@media (max-width: 900px) {
  .mechanisms-block { grid-template-columns: 1fr; }
}

.mech {
  padding: 18px 22px;
  background: var(--bg-card);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
}

.mech-num {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.mech-title {
  font-family: var(--serif);
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 6px;
  color: var(--ink);
}

.mech-title code {
  font-family: var(--mono);
  font-size: 13px;
  color: var(--accent);
}

.mech-body {
  font-size: 13px;
  line-height: 1.6;
  color: var(--ink-soft);
}
```

- [ ] **Step 3**: Render the mechanisms block in HTML using the above classes:

```html
<div class="mechanisms-block">
  <div class="mech">
    <div class="mech-num">Mechanism 01</div>
    <div class="mech-title">Bounded badge universe</div>
    <div class="mech-body">7 axes × 3 rungs = 21 slots. Fixed from day 1; no mystery / locked slots. The child sees the full universe the first time they open the collection.</div>
  </div>
  <!-- repeat for mechanisms 02–08 with content from spec -->
</div>
```

- [ ] **Step 4**: Update the masthead nav to include the new anchor. Add `<a href="#anti-addiction">Principles</a>` to the nav list.

- [ ] **Step 5**: Mirror all of the above in `child_recap_preview_cn.html`. CN table headers: `模式 / 为什么有害 / 我们的立场`.

Chinese table rows (natural translation, keep technical terms in English where appropriate):

| 模式 | 为什么有害 | 我们的立场 |
|---|---|---|
| 连胜 streak（"别断了链条"） | 漏一天就有负罪感；不管需不需要都逼着每天用 | 不做 streak。永远不做 |
| 随机奖励（随机掉落） | 老虎机式的多巴胺循环 | 奖励由具体的认知动作决定，非随机 |
| 无上限的徽章收集 | 让孩子一直刷，永远玩不"完" | 上限固定，第一天就全部可见 |
| 稀有 / 普通分级 | 赌博 + 囤积本能 | 所有徽章平等，不分稀有度 |
| 排行榜 / 和别人比 | 社交焦虑、攀比 | 永远不展示其他孩子 |
| 推送通知 | 人造 FOMO | App 永远不主动叫孩子回来 |
| 无限滚动回顾 | 把孩子的眼睛黏在屏幕上 | 就一屏，有尽头，可关闭 |
| 按时长给 XP | 奖励"待得久"而不是"学到了" | 奖励绑定到认知动作 |

Mechanisms CN translations:
1. **有界徽章体系** — 7 条轴 × 3 个级数 = 21 个槽位。第一天就固定；没有隐藏 / 锁死的槽。
2. **展示"深度"，不展示"总数"** — 每条轴的深度（L1→L2→L3 的进度条），不是一堆勋章堆在一起。
3. **`highlight_moment` 才是主角，徽章是背景** — 运行时生成的这一句话用大号 serif；徽章是小号、次级，不加星星 / 弹跳 / 动效。
4. **柔性会话上限** — 一次连续玩了 N 个活动以后（T0: 2，T1: 3，T2: 4），回顾屏以"今天动脑动得不错，明天见"收尾。App 不做硬锁。
5. **重玩被欢迎，不是重新发奖** — 同一个 entity 再玩一次，回顾强调"你这次注意到了 ___"，不发新徽章。
6. **UI 里完全没有 streak** — 不是藏起来，是不做。
7. **温柔收场，不是钩子** — 用"出门的时候可以找找 ___"这样的邀请收尾；从不说"点这里继续"或"再 N 个就升级"。
8. **opt-in 的历史** — 已获得的徽章在单独的收藏页。不会被推到孩子眼前。

- [ ] **Step 6**: Verify EN.

```js
({
  antiTableRows: document.querySelectorAll('#anti-addiction .anti-table tbody tr').length,
  mechCount: document.querySelectorAll('#anti-addiction .mech').length,
  mechTitles: Array.from(document.querySelectorAll('#anti-addiction .mech-title')).map(e=>e.innerText),
})
```

Expected: 8 table rows, 8 mechanisms, mechanism titles include "Bounded badge universe", "Soft session cap", etc.

- [ ] **Step 7**: Verify CN at `/child_recap_preview_cn.html#anti-addiction` with the same eval shape. Expect 8 rows + 8 mechanisms with Chinese titles.

- [ ] **Step 8**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html
git commit -m "feat(child-recap): add §02 anti-addiction principles table + 8 mechanisms"
```

---

## Task 5 · Child recap · §03 Layout + §04 Contract + §05 highlight_moment rule

**Spec reference**: §4.3 §03, §04, §05

**Files:**
- Modify: `docs/child_recap_preview.html`
- Modify: `docs/child_recap_preview_cn.html`

- [ ] **Step 1**: Add §03 Layout walkthrough.

Structure:
- `<section id="layout">` with `.sec-head` "§ 03 / Layout · annotated mockup"
- A mockup frame — **copy the structure from Template 0 §05's child recap mockup** (it already exists in Template 0; just duplicate the HTML and enlarge it). Classes: `.mockup-frame`, `.recap-head`, `.recap-badge`, `.recap-row`, `.chip-*`, `.reads-from`.
- **Annotation overlay**: 6 numbered callouts positioned around the mockup with lines pointing to regions. Per spec §4.3 §03:
  1. Badge circle — `role_title`
  2. Title + pillar subtitle
  3. "The moment" row — `highlight_moment` (the hero)
  4. "You earned" chips — `related_concepts`
  5. "You practiced" chips — `atl_skills`
  6. Exit copy — real-world invitation OR "see you tomorrow"

For annotations, use a simple flex layout: mockup on the left (60% width), numbered callouts list on the right (40%). No SVG arrows needed in v0.1 — just a numbered legend.

Example annotation markup:

```html
<div class="layout-annotated">
  <div class="layout-mockup">
    <!-- full mockup here -->
  </div>
  <ol class="layout-callouts">
    <li><span class="co-num">1</span><span class="co-name">Badge circle</span><span class="co-field"><code>role_title</code></span><span class="co-note">Serif, centered, single letter or glyph. The identity beat.</span></li>
    <li><!-- 2 --></li>
    <!-- through 6 -->
  </ol>
</div>
```

Add CSS for `.layout-annotated` (grid `3fr 2fr` on desktop, stacked on mobile), `.layout-callouts` (numbered list with gray circles), `.co-num` (accent-colored number circle).

- [ ] **Step 2**: Add §04 Tag-block contract.

Structure:
- `<section id="contract">` with `.sec-head` "§ 04 / Tag-block contract"
- `.sec-desc` noting that the contract is declared in Template 0 §04 and this section enumerates which fields this screen reads.
- A table listing each field + render + notes. Use the same `.mapping-table` class from Template 0.

Table (per spec §4.3 §04):

| Field | Renders as | Notes |
|---|---|---|
| `role_title` | Badge title (serif) | Main identity beat |
| `pillar` | Subtitle ("Mystery · solved") | Emotional mode, sets tone |
| `highlight_moment` | Large serif pull-quote | Runtime-generated; see §05 |
| `related_concepts` | "You earned" chip row | Child-friendly concept words |
| `atl_skills` | "You practiced" chip row | Child-friendly wording, not IB jargon |
| `attributes` | Feeds highlight_moment | Not shown as chips |

Add a **"Explicitly not read"** note block below the table: `key_concepts`, `transdisciplinary_theme`, `subject_tags`, `progression.*` — those are parent-facing.

- [ ] **Step 3**: Add §05 `highlight_moment` generation rule.

Structure:
- `<section id="moment-rule">` with `.sec-head` "§ 05 / <code>highlight_moment</code> generation"
- A 3-column breakdown: **Input**, **Output**, **Rules** — as a `.grid-3` card set or structured list. Rules per spec §4.3 §05:
  - Always second person, past tense, 6–12 words
  - Grounded in something the child said/did
  - No IB terminology, no tier names, no level numbers
  - Fallback to pillar-generic if no usable material
- A **tier-specific examples** sub-block with 3 example rows (T0 / T1 / T2).
- A privacy clarifier note: "The transcript is input to the generator only; it never surfaces verbatim in the recap. Output is a sanitized summary."

Add `.moment-rule-grid` CSS (flex / grid of 3 columns on desktop).

- [ ] **Step 4**: Mirror all three sections in CN. Natural Chinese translation.

For §04 contract table header in CN: `字段 / 如何呈现 / 备注`.

Explicitly-not-read fields in CN: "这一屏不读取这些 —— 它们是家长端的内容。"

- [ ] **Step 5**: Update masthead nav in both EN and CN to include `#layout`, `#contract`, `#moment-rule`.

- [ ] **Step 6**: Verify EN.

```js
({
  layoutCallouts: document.querySelectorAll('#layout .layout-callouts li').length,
  contractRows: document.querySelectorAll('#contract .mapping-table tbody tr').length,
  momentRuleExists: !!document.querySelector('#moment-rule'),
  notReadBlock: document.querySelector('#contract .note-block')?.innerText?.includes('key_concepts'),
})
```

Expected: 6 callouts, 6 contract rows, moment-rule exists, not-read block mentions `key_concepts`.

- [ ] **Step 7**: Verify CN with same eval.

- [ ] **Step 8**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html
git commit -m "feat(child-recap): add §03 layout, §04 tag-block contract, §05 highlight_moment rule"
```

---

## Task 6 · Child recap · §06-§10 persistence, copy, edges, scope

**Spec reference**: §4.3 §06–§10

**Files:**
- Modify: `docs/child_recap_preview.html`
- Modify: `docs/child_recap_preview_cn.html`

- [ ] **Step 1**: Add §06 Cross-session badge persistence.

Structure:
- `<section id="persistence">` with `.sec-head` "§ 06 / Persistence"
- 4-point explanation per spec §4.3 §06. Render as a numbered list or a 2×2 card grid.
- Include a **small mockup** of the 21-slot grid (7 rows × 3 cols) showing an example child's state — some lit, some dimmed, one with a "×4" count badge.

Example 21-slot mockup HTML:

```html
<div class="slot-grid">
  <div class="slot-row">
    <div class="slot-axis">Form</div>
    <div class="slot-cell filled">L1</div>
    <div class="slot-cell filled count">L2<span class="slot-count">×4</span></div>
    <div class="slot-cell">L3</div>
  </div>
  <!-- 6 more rows for Function, Causation, Change, Connection, Perspective, Responsibility -->
</div>
```

Add `.slot-grid` CSS — 4-column grid (axis label + 3 rung cells). Filled cells use `var(--accent)` background; count badges are small vermilion pills.

- [ ] **Step 2**: Add §07 Copy tone by tier.

Structure:
- `<section id="copy-tone">` with `.sec-head` "§ 07 / Copy tone · T0 · T1 · T2"
- A 3-column card set (one per tier) showing voice samples for each recap row. Content per spec §4.3 §07.

Example tier card:

```html
<div class="tone-card tone-t0">
  <div class="tone-head"><span class="tone-tier">Tier 0 · 2–4 yrs</span><span class="tone-name">Exploration Companion</span></div>
  <div class="tone-row"><span class="tone-lbl">Role title</span><span class="tone-val">"Ladybug Watcher"</span></div>
  <div class="tone-row"><span class="tone-lbl">Highlight moment</span><span class="tone-val">"You said 'red' when you saw the ladybug"</span></div>
  <div class="tone-row"><span class="tone-lbl">Exit copy</span><span class="tone-val">"See you next time!"</span></div>
  <!-- more rows -->
</div>
```

Reuse `.tier-compare` / `.tcc-col` CSS pattern from Template 0 §06 as inspiration — or use tier colors directly (`var(--tier-0)` etc.).

- [ ] **Step 3**: Add §08 Edge cases.

Structure:
- `<section id="edges">` with `.sec-head` "§ 08 / Edge cases"
- A 5-row table or card set. Content per spec §4.3 §08:
  - In-activity demote → softer language, "You noticed" instead of "You figured out"
  - Child rage-quits → no recap; next session opens with neutral welcome
  - Repeat entity within a week → `highlight_moment` acknowledges replay
  - Soft cap triggered → exit copy = "see you tomorrow"
  - ASR failed to capture usable quote → pillar-generic fallback

- [ ] **Step 4**: Add §09 Open questions + §10 Out of scope.

Structure:
- `<section id="open">` — two note blocks or a two-column layout.
- **§09 Open questions** (deliberately open): 3 items per spec.
- **§10 Out of scope**: 3 items per spec.

- [ ] **Step 5**: Add a `.revnote` at the bottom of the doc (the inaugural v0.1 note). Mirror the pattern from Template 0:

```html
<details class="revnote">
  <summary><span class="revnote-tag">v0.1</span> Inaugural draft · 2026-04-17</summary>
  <ol>
    <li>Extracted from Template 0 §05 per design spec 2026-04-17-downstream-surfaces-split-design.md.</li>
    <li>Anti-addiction principles and 8 concrete mechanisms are the defining content (§02). Read that section first.</li>
    <li>Badge universe is bounded at 21 slots (7 axes × 3 rungs) — this is a product stance, not a UX detail.</li>
  </ol>
</details>
```

- [ ] **Step 6**: Update the `.version` block at the bottom (matches Template 0's pattern):

```html
<div class="version">
  <span>Version 0.1 · Draft for review</span>
  <span>WonderLens x 奇朵 · Child recap design · 2026-04-17</span>
</div>
```

- [ ] **Step 7**: Update masthead nav to include all new anchors: `#persistence`, `#copy-tone`, `#edges`, `#open`.

- [ ] **Step 8**: Mirror Steps 1–7 in CN. Natural Chinese prose. For §09 "Open questions" in CN: `悬而未决`. For §10 "Out of scope": `本轮不做`.

- [ ] **Step 9**: Verify EN.

```js
({
  persistenceSlots: document.querySelectorAll('#persistence .slot-cell').length,
  toneCards: document.querySelectorAll('#copy-tone .tone-card').length,
  edgesExists: !!document.querySelector('#edges'),
  openExists: !!document.querySelector('#open'),
  revnote: !!document.querySelector('.revnote'),
})
```

Expected: 21 slot cells, 3 tone cards, edges exists, open exists, revnote present.

- [ ] **Step 10**: Verify CN with the same eval.

- [ ] **Step 11**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html
git commit -m "feat(child-recap): add §06 persistence + §07 copy tone + §08 edges + §09-10 open/scope + v0.1 revnote"
```

---

## Task 7 · Parent growth · scaffold + §01-§02

**Spec reference**: §5.2, §5.3 §01, §5.3 §02

**Files:**
- Create: `docs/parent_growth_path_preview.html`
- Create: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: Copy Template 0 as the starter (same approach as Task 3).

```bash
cp docs/template_0_preview.html docs/parent_growth_path_preview.html
cp docs/template_0_preview_cn.html docs/parent_growth_path_preview_cn.html
```

- [ ] **Step 2**: In EN, update title, brand, masthead meta, breadcrumb (copy the `.breadcrumb` CSS from child recap Task 3 — both new docs need it). New values:

- `<title>` → `Parent growth path · WonderLens Activity Design`
- `.brand` → `WonderLens · Parent dashboard design`
- `.meta` → `Draft v0.1 · 2026-04-17 · Internal review`
- Breadcrumb → `← <a href="template_0_preview.html">Template 0</a> · reads tag block`

- [ ] **Step 3**: Strip out Template 0 content sections as in Task 3 Step 3 (delete `#concerns`, `#spine`, `#skeleton`, `#tags`, `#bridges`, `#tiers`, `#axes`, `#overlays`, `#decisions` sections). Keep masthead, hero, footer, script block (trim to empty).

- [ ] **Step 4**: Rewrite hero content:

```html
<section class="hero">
  <div class="eyebrow">Surface · 2 of 2 · parent dashboard</div>
  <h1>What parents<br />see <em>over time</em>.</h1>
  <p class="lede">
    This doc specifies the parent-facing dashboard — default weekly view, with monthly
    and term toggles. Its job is to <b>make the child's growth legible and actionable</b>
    to parents, without turning into a grade report or an engagement loop.
  </p>
  <div class="hero-meta">
    <div>
      <span class="label">Reads from</span>
      <span class="value">Template 0 tag block</span>
    </div>
    <div>
      <span class="label">Consumers</span>
      <span class="value">Parents · async</span>
    </div>
    <div>
      <span class="label">Stance</span>
      <span class="value">Legible, not clinical</span>
    </div>
    <div>
      <span class="label">Status</span>
      <span class="value">Draft v0.1 · pending sign-off</span>
    </div>
  </div>
</section>
```

- [ ] **Step 5**: Add §01 Purpose & stance.

Structure:
- `<section id="purpose">` with `.sec-head` "§ 01 / Purpose &amp; stance"
- `.sec-desc`: what parents actually want (progress / personality / connection / action / awareness) + what we explicitly don't do.
- An anti-pattern table (same `.anti-table` class as child recap Task 4). Content per spec §5.3 §01:

| Typical dashboard feature | Why we don't | Our stance |
|---|---|---|
| Peer comparison ("vs. other kids") | Anxiety, competition, parental guilt | Never. Only this child's journey |
| Letter grades / scores | Anti-IB philosophy; reduces nuance | No scores, no grades |
| Predictive trajectories | Over-promises; sets up disappointment | No forecast lines |
| Activity transcripts | Surveillance vibe | Out of scope this round |

- [ ] **Step 6**: Add §02 Layout walkthrough.

Structure:
- `<section id="layout">` with `.sec-head` "§ 02 / Layout · annotated mockup"
- A large mockup frame — **copy from Template 0 §05's parent growth path mockup** and enlarge. Classes: `.mockup-frame`, `.path-head`, `.path-axis`, `.step`, `.path-frame-rows`, `.pfr-lbl`, `.chip-subject`, etc. (These classes exist in Template 0 v0.2 already — copy the CSS verbatim.)
- 6 numbered callouts with lines / numbers pointing to regions (per spec §5.3 §02):
  1. Header — child name, week label, tier chip
  2. Progress block — L×T axis ladder
  3. Curiosity profile — new
  4. "In their words" — new
  5. "Try this at home" — new
  6. Gauges strip — footer

Use the same `.layout-annotated` pattern established in child recap Task 5.

- [ ] **Step 7**: Mirror all of Steps 2–6 in CN. Breadcrumb in CN: `← <a href="template_0_preview_cn.html">Template 0</a> · 读取 tag block`.

- [ ] **Step 8**: Verify EN.

```js
({
  title: document.title,
  brand: document.querySelector('.brand')?.innerText,
  breadcrumb: !!document.querySelector('.breadcrumb'),
  purposeTable: document.querySelectorAll('#purpose .anti-table tbody tr').length,
  layoutCallouts: document.querySelectorAll('#layout .layout-callouts li').length,
})
```

Expected: title mentions "Parent growth path", breadcrumb exists, 4 anti-pattern rows, 6 callouts.

- [ ] **Step 9**: Verify CN with the same eval.

- [ ] **Step 10**: Commit.

```bash
git add docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "feat(parent-dashboard): scaffold doc with masthead, hero, §01 purpose, §02 layout"
```

---

## Task 8 · Parent growth · §03 curiosity profile + §04 in-their-words

**Spec reference**: §5.3 §03, §5.3 §04

**Files:**
- Modify: `docs/parent_growth_path_preview.html`
- Modify: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: Add §03 Curiosity profile module.

Structure:
- `<section id="curiosity">` with `.sec-head` "§ 03 / Curiosity profile"
- `.sec-desc` explaining the module's purpose — 1-glance answer to "what kind of thinker is my kid?"
- A 7-lobed SVG radial visualization (hand-draw the SVG path; don't pull a library). 7 axes placed at 0°, 51°, 103°, 154°, 206°, 257°, 309°. Each lobe filled proportional to frequency; outline radius proportional to depth.
- Auto-generated caption styled as serif pull-quote below the radial: *"Mia is a pattern-finder and a storyteller. She explores Form and Perspective most deeply; Responsibility is next to try."*
- A sub-block listing the caption generation rules per spec §5.3 §03.

SVG radial structure — concrete example-child data for "Mia" baked in. The 7 axes sit at evenly-spaced angles starting at 12 o'clock: Form 0°, Function ~51.4°, Causation ~102.9°, Change ~154.3°, Connection ~205.7°, Perspective ~257.1°, Responsibility ~308.6°.

**Example values (Mia this week)** — per-axis `{frequency, depth}` where frequency is activity count (0–6 scale) and depth is max rung reached (L1=1, L2=2, L3=3):

| Axis | Frequency | Depth | Polygon radius |
|---|---|---|---|
| Form | 3 | 3 | 95 |
| Function | 1 | 1 | 35 |
| Causation | 2 | 2 | 65 |
| Change | 1 | 2 | 55 |
| Connection | 2 | 2 | 65 |
| Perspective | 1 | 3 | 85 |
| Responsibility | 0 | 0 | 20 |

Polygon radius formula: `30 + 10 * frequency + 15 * depth`, clamped to [20, 105]. The plotted points are `(radius * sin(angle), -radius * cos(angle))` for each of the 7 axis angles, resulting in:

- Form: `(0, -95)`
- Function: `(74.2, -59.5)`
- Causation: `(63.4, 14.6)`
- Change: `(23.9, 49.5)`
- Connection: `(-28.3, 58.6)`
- Perspective: `(-82.9, 17.7)`
- Responsibility: `(-15.6, -12.6)`

```html
<svg class="curiosity-radial" viewBox="-130 -130 260 260" aria-label="Curiosity radial">
  <!-- Background rings (3 concentric for L1/L2/L3 reference) -->
  <circle class="ring" r="35" />
  <circle class="ring" r="65" />
  <circle class="ring" r="95" />

  <!-- 7 axis spokes -->
  <g class="spokes">
    <line x1="0" y1="0" x2="0" y2="-105" class="spoke" data-axis="form" />
    <line x1="0" y1="0" x2="82.1" y2="-65.7" class="spoke" data-axis="function" />
    <line x1="0" y1="0" x2="102.3" y2="23.5" class="spoke" data-axis="causation" />
    <line x1="0" y1="0" x2="45.5" y2="94.6" class="spoke" data-axis="change" />
    <line x1="0" y1="0" x2="-45.5" y2="94.6" class="spoke" data-axis="connection" />
    <line x1="0" y1="0" x2="-102.3" y2="23.5" class="spoke" data-axis="perspective" />
    <line x1="0" y1="0" x2="-82.1" y2="-65.7" class="spoke" data-axis="responsibility" />
  </g>

  <!-- Filled polygon based on per-axis frequency + depth -->
  <polygon class="profile-fill"
           points="0,-95 74.2,-59.5 63.4,14.6 23.9,49.5 -28.3,58.6 -82.9,17.7 -15.6,-12.6" />

  <!-- Axis labels just past each spoke -->
  <g class="labels">
    <text x="0" y="-115" text-anchor="middle">Form</text>
    <text x="95" y="-72" text-anchor="start">Function</text>
    <text x="118" y="28" text-anchor="start">Causation</text>
    <text x="52" y="112" text-anchor="middle">Change</text>
    <text x="-52" y="112" text-anchor="middle">Connection</text>
    <text x="-118" y="28" text-anchor="end">Perspective</text>
    <text x="-95" y="-72" text-anchor="end">Responsibility</text>
  </g>
</svg>
```

CSS:

```css
.curiosity-radial {
  width: 100%;
  max-width: 420px;
  display: block;
  margin: 16px auto;
}

.curiosity-radial .ring {
  fill: none;
  stroke: var(--line);
  stroke-dasharray: 3 3;
  stroke-width: 1;
}

.curiosity-radial .spoke {
  stroke: var(--line-soft);
  stroke-width: 1;
}

.curiosity-radial .profile-fill {
  fill: color-mix(in srgb, var(--accent) 22%, transparent);
  stroke: var(--accent);
  stroke-width: 1.5;
  stroke-linejoin: round;
}

.curiosity-radial .labels text {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  fill: var(--muted);
}
```

**Do NOT make it interactive in v0.1** — static SVG with Mia's baked-in values. Interactivity (hover tooltips, tier filter, cadence switch) is v0.2.

- [ ] **Step 2**: Add §04 In their words module.

Structure:
- `<section id="in-their-words">` with `.sec-head` "§ 04 / In their words · this week"
- `.sec-desc` explaining that this module shows 2–3 pull-quotes per week.
- 3 `.quote-card` elements, each with:
  - Serif italic quote text (large, warm)
  - `.quote-context` below: day + activity description
  - Optional: replay link

Example:

```html
<div class="quote-card">
  <div class="quote-text">"The flower closes to save energy at night."</div>
  <div class="quote-attrib">
    <span class="quote-who">Mia said</span>
    <span class="quote-ctx">Tuesday · playing with a sunflower</span>
  </div>
</div>
```

Add `.quote-card` CSS — cream background, vermilion left border, large serif for quote text.

Below the cards, add a **privacy note block** explaining the opt-in rule per spec §5.3 §04.

- [ ] **Step 3**: Update masthead nav to include `#curiosity`, `#in-their-words`.

- [ ] **Step 4**: Mirror both sections in CN. Example CN quote: `"花到晚上合起来是为了省力气。"` with context `周二 · 和向日葵一起玩`.

- [ ] **Step 5**: Verify EN.

```js
({
  radialExists: !!document.querySelector('.curiosity-radial'),
  radialSpokes: document.querySelectorAll('.curiosity-radial .spoke').length,
  radialLabels: document.querySelectorAll('.curiosity-radial .labels text').length,
  quoteCards: document.querySelectorAll('#in-their-words .quote-card').length,
})
```

Expected: radial exists, 7 spokes, 7 labels, 3 quote cards.

- [ ] **Step 6**: Verify CN with the same eval.

- [ ] **Step 7**: Commit.

```bash
git add docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "feat(parent-dashboard): add §03 curiosity radial + §04 in-their-words module"
```

---

## Task 9 · Parent growth · §05 try-at-home + §06 gauges strip

**Spec reference**: §5.3 §05, §5.3 §06

**Files:**
- Modify: `docs/parent_growth_path_preview.html`
- Modify: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: Add §05 Try this at home module.

Structure:
- `<section id="try-at-home">` with `.sec-head` "§ 05 / Try this at home · offline"
- `.sec-desc` — emphasis on "this module sends the parent-child pair away from the app"; 2–3 suggestions per week, bounded deliberately.
- 3 `.suggestion-card` elements, each with:
  - Imperative sentence (serif): *"On your walk, look for three spotted things together."*
  - `.suggestion-tag`: `Extends: Connection · matches pattern-finding`

Example:

```html
<div class="suggestion-card">
  <div class="suggestion-text">On your walk, look for three spotted things together.</div>
  <div class="suggestion-tag">
    <span class="tag-lbl">Extends</span>
    <span class="tag-val">Connection axis · matches pattern-finding</span>
  </div>
</div>
```

Add `.suggestion-card` CSS — cream card, subtle border, serif body, mono tag.

- [ ] **Step 2**: Add §06 Gauges strip module.

Structure:
- `<section id="gauges">` with `.sec-head` "§ 06 / Gauges · co-play &amp; time"
- Two gauge blocks side-by-side:

**(a) Co-play share** — stacked horizontal bar.

```html
<div class="gauge co-play">
  <div class="gauge-title">Co-play share · this week</div>
  <div class="stacked-bar">
    <div class="bar-seg seg-scaffold" style="width: 18%;">scaffold</div>
    <div class="bar-seg seg-coexplorer" style="width: 55%;">co-explorer</div>
    <div class="bar-seg seg-observer" style="width: 27%;">observer</div>
  </div>
  <div class="gauge-caption">This week you were mostly a co-explorer.</div>
</div>
```

**(b) Time this week** — filled bar with "healthy range" band markers.

```html
<div class="gauge time">
  <div class="gauge-title">Time this week · T1 band</div>
  <div class="time-bar">
    <div class="time-band-min" style="left: 45%;"></div>
    <div class="time-band-max" style="left: 90%;"></div>
    <div class="time-fill" style="width: 62%;"></div>
    <div class="time-label">62 min</div>
  </div>
  <div class="gauge-caption">Gentle amount this week.</div>
</div>
```

Tier band defaults per spec §5.3 §06:
- T0: 20–60 min/week
- T1: 45–90 min/week
- T2: 60–120 min/week

Add CSS for both gauge types — `.stacked-bar`, `.bar-seg` (different colors per caregiver role using `--tier-*` palette), `.time-bar`, `.time-band-min/max` (vertical markers), `.time-fill` (vermilion fill that goes amber if past max).

- [ ] **Step 3**: Update masthead nav to include `#try-at-home`, `#gauges`.

- [ ] **Step 4**: Mirror both sections in CN. Example CN suggestion: `散步的时候，一起找三件带斑点的东西。` Example gauge caption: `这周花的时间不多，刚刚好。`

- [ ] **Step 5**: Verify EN.

```js
({
  suggestions: document.querySelectorAll('#try-at-home .suggestion-card').length,
  gauges: document.querySelectorAll('#gauges .gauge').length,
  stackedSegs: document.querySelectorAll('#gauges .stacked-bar .bar-seg').length,
  timeFillExists: !!document.querySelector('#gauges .time-fill'),
})
```

Expected: 3 suggestion cards, 2 gauges, 3 stacked segments, time-fill exists.

- [ ] **Step 6**: Verify CN with the same eval.

- [ ] **Step 7**: Commit.

```bash
git add docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "feat(parent-dashboard): add §05 try-at-home + §06 gauges strip"
```

---

## Task 10 · Parent growth · §07-§11 contract, cadence, privacy, edges, scope

**Spec reference**: §5.3 §07–§11

**Files:**
- Modify: `docs/parent_growth_path_preview.html`
- Modify: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: Add §07 Tag-block contract (full).

Structure:
- `<section id="contract">` with `.sec-head` "§ 07 / Tag-block contract"
- `.sec-desc`: which fields each module reads, grouped.
- A table grouped by module per spec §5.3 §07:

| Module | Fields |
|---|---|
| Progress (L×T ladder) | `progression.topic_axis`, `progression.difficulty_level`, `progression.next_step_hint`, `tier` |
| IB framework chips | `key_concepts`, `atl_skills`, `transdisciplinary_theme`, `subject_tags` |
| Curiosity profile | `key_concepts`, `progression.difficulty_level` (aggregate) |
| In their words | `highlight_moment`, opt-in child utterances |
| Try at home | `progression.topic_axis`, `progression.next_step_hint`, recent `entity` |
| Gauges | `caregiver_role`, session-duration telemetry |

- Below table: note "Explicitly not read: `role_title` — that's child-facing."

- [ ] **Step 2**: Add §08 View cadence.

Structure:
- `<section id="cadence">` with `.sec-head` "§ 08 / View cadence"
- Short prose: default weekly (Sun–Sat), toggle to monthly, toggle to term (12 weeks).
- A note about empty state: `< 3 activities in window` → show "still getting to know Mia" onboarding state instead of half-empty modules.

- [ ] **Step 3**: Add §09 Privacy & data scope.

Structure:
- `<section id="privacy">` with `.sec-head` "§ 09 / Privacy &amp; data scope"
- 4 categories (default shown / opt-in / never shown / retention) as a card set or list. Content per spec §5.3 §09.

- [ ] **Step 4**: Add §10 Edge cases.

Structure:
- `<section id="edges">` with `.sec-head` "§ 10 / Edge cases"
- 4-row table or card set per spec §5.3 §10:
  - New child (< 3 activities)
  - Single-axis over-indexing
  - Demote streaks
  - Multiple children on one account

- [ ] **Step 5**: Add §11 Out of scope.

Structure:
- `<section id="scope">` with `.sec-head` "§ 11 / Out of scope"
- 5-item list per spec §5.3 §11:
  - Cross-child comparisons
  - School-report export
  - Notification cadence
  - Activity-transcript drill-down
  - Developmental-milestones ribbon (deferred, with a 1-sentence note on why)

- [ ] **Step 6**: Add footer revnote + version block (same pattern as child recap Task 6 Step 5-6).

```html
<details class="revnote">
  <summary><span class="revnote-tag">v0.1</span> Inaugural draft · 2026-04-17</summary>
  <ol>
    <li>Extracted from Template 0 §05 per design spec 2026-04-17-downstream-surfaces-split-design.md.</li>
    <li>Four new modules beyond the L×T ladder: curiosity profile, in their words, try at home, gauges.</li>
    <li>No predictive features, no peer comparison, no letter grades — stance choices, not feature gaps.</li>
  </ol>
</details>
```

Version block:

```html
<div class="version">
  <span>Version 0.1 · Draft for review</span>
  <span>WonderLens x 奇朵 · Parent dashboard design · 2026-04-17</span>
</div>
```

- [ ] **Step 7**: Update masthead nav to include `#contract`, `#cadence`, `#privacy`, `#edges`, `#scope`.

- [ ] **Step 8**: Mirror all of Steps 1–7 in CN.

- [ ] **Step 9**: Verify EN.

```js
({
  contractTable: document.querySelectorAll('#contract tbody tr').length,
  cadenceExists: !!document.querySelector('#cadence'),
  privacyExists: !!document.querySelector('#privacy'),
  edgesExists: !!document.querySelector('#edges'),
  scopeExists: !!document.querySelector('#scope'),
  revnote: !!document.querySelector('.revnote'),
})
```

Expected: 6 contract rows, all sections exist, revnote present.

- [ ] **Step 10**: Verify CN with same eval.

- [ ] **Step 11**: Commit.

```bash
git add docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "feat(parent-dashboard): add §07 contract + §08 cadence + §09 privacy + §10 edges + §11 scope + v0.1 revnote"
```

---

## Task 11 · Template 0 · §05 reference strip + revnote update

**Spec reference**: §3.2, §3.3

Now that both new docs exist, replace Template 0's §05 downstream content with the compact reference strip.

**Files:**
- Modify: `docs/template_0_preview.html`
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1**: Locate the existing `.mockups` block inside `<section id="bridges">` (around line 2994 in EN). Delete the two `.mockup` children (child recap mockup + parent growth mockup). Delete the closing `.note-block` that says "What's intentionally not designed yet..." directly after `.mockups`.

Keep everything before the `.mockups` block (flow diagram, upstream bridge, first note-block).

- [ ] **Step 2**: Replace the deleted blocks with a reference strip:

```html
<h3 class="subhead" data-dir="Downstream">Two surfaces consume the tag block</h3>
<p class="subhead-desc">The full specs for these surfaces live in their own docs. The contract they depend on is what Template 0 provides.</p>

<div class="surface-strip">
  <a class="surface-card" href="child_recap_preview.html">
    <div class="sc-label">Surface · 1 of 2</div>
    <div class="sc-title">Child recap</div>
    <div class="sc-purpose">The post-activity screen. Celebrates the specific cognitive act the child just made; soft-sign-off, no hooks, no streaks.</div>
    <div class="sc-reads">
      <span class="sc-reads-lbl">Reads</span>
      <code>role_title</code>
      <code>pillar</code>
      <code>highlight_moment</code>
      <code>related_concepts</code>
      <code>atl_skills</code>
    </div>
    <div class="sc-arrow">Full design →</div>
  </a>
  <a class="surface-card" href="parent_growth_path_preview.html">
    <div class="sc-label">Surface · 2 of 2</div>
    <div class="sc-title">Parent growth path</div>
    <div class="sc-purpose">The parent dashboard. Makes growth legible and actionable over time, without turning into a grade report.</div>
    <div class="sc-reads">
      <span class="sc-reads-lbl">Reads</span>
      <code>progression.*</code>
      <code>key_concepts</code>
      <code>atl_skills</code>
      <code>subject_tags</code>
      <code>tier</code>
      <code>caregiver_role</code>
    </div>
    <div class="sc-arrow">Full design →</div>
  </a>
</div>
```

- [ ] **Step 3**: Add CSS for `.surface-strip` and `.surface-card`.

```css
.surface-strip {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 24px;
}

@media (max-width: 900px) {
  .surface-strip { grid-template-columns: 1fr; }
}

.surface-card {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 24px 26px;
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
  text-decoration: none;
  color: inherit;
  transition: border-left-color 0.15s;
}

.surface-card:hover {
  border-left-color: var(--ink);
}

.sc-label {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.sc-title {
  font-family: var(--serif);
  font-size: 24px;
  font-weight: 500;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.sc-purpose {
  font-size: 13px;
  line-height: 1.55;
  color: var(--ink-soft);
}

.sc-reads {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
  padding-top: 12px;
  border-top: 1px dashed var(--line);
  font-size: 11px;
}

.sc-reads-lbl {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-right: 8px;
}

.sc-reads code {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--accent);
  padding: 2px 6px;
  background: color-mix(in srgb, var(--accent) 8%, transparent);
  border-radius: 2px;
}

.sc-arrow {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-top: 4px;
}
```

- [ ] **Step 4**: Add a new revnote bullet at the bottom of the existing v0.2 revnote block. Find the `<ol>` inside `.revnote` and append:

```html
<li><b>Downstream surfaces extracted into their own docs</b> (§05). <code>child_recap_preview.html</code> and <code>parent_growth_path_preview.html</code> now carry the full designs; §05 keeps only the upstream pipeline + a compact reference strip to both.</li>
```

- [ ] **Step 5**: Mirror Steps 1–4 in `docs/template_0_preview_cn.html`. CN reference strip labels: `下游面 · 2 之 1` / `儿童端活动回顾` / `家长端成长路径`. CN arrow: `查看完整设计 →`.

CN revnote bullet:

```html
<li><b>下游面单独成文</b>（§05）。<code>child_recap_preview.html</code> 和 <code>parent_growth_path_preview.html</code> 承载各自完整设计；§05 只保留上游管线 + 一条指向两份文档的参考条。</li>
```

- [ ] **Step 6**: Verify EN.

```js
({
  surfaceCards: document.querySelectorAll('.surface-strip .surface-card').length,
  firstCardLinks: document.querySelector('.surface-strip .surface-card:nth-child(1)')?.getAttribute('href'),
  secondCardLinks: document.querySelector('.surface-strip .surface-card:nth-child(2)')?.getAttribute('href'),
  oldMockupsGone: !document.querySelector('#bridges .mockups'),
  revnoteBullets: document.querySelectorAll('.revnote ol li').length,
})
```

Expected: 2 surface cards, first links to `child_recap_preview.html`, second links to `parent_growth_path_preview.html`, old mockups gone, revnote has 5 bullets (was 4, +1).

- [ ] **Step 7**: Verify CN with same eval (expect links to `_cn.html` variants).

- [ ] **Step 8**: Click-through test: click the first surface card. Should navigate to `child_recap_preview.html`. Go back, click second card. Should navigate to `parent_growth_path_preview.html`.

- [ ] **Step 9**: Commit.

```bash
git add docs/template_0_preview.html docs/template_0_preview_cn.html
git commit -m "refactor(template-0): replace §05 downstream mockups with reference strip to extracted docs"
```

---

## Task 12 · Cross-link navigation

**Spec reference**: §6

Both new docs already have breadcrumbs back to Template 0 (added in Tasks 3 and 7). Now add footer companion-links between the two new docs.

**Files:**
- Modify: `docs/child_recap_preview.html`
- Modify: `docs/child_recap_preview_cn.html`
- Modify: `docs/parent_growth_path_preview.html`
- Modify: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: In `child_recap_preview.html`, add a companion link inside the `<footer>`, just above the `.version` block:

```html
<div class="companion-link">
  <span class="cl-lbl">Companion surface</span>
  <a href="parent_growth_path_preview.html">Parent growth path →</a>
  <span class="cl-note">Same tag block, different lens.</span>
</div>
```

- [ ] **Step 2**: Add CSS for `.companion-link`:

```css
.companion-link {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 0;
  border-top: 1px dashed var(--line);
  margin-top: 28px;
  font-family: var(--mono);
  font-size: 11px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

.cl-lbl {
  color: var(--accent);
}

.companion-link a {
  font-family: var(--serif);
  font-size: 18px;
  letter-spacing: -0.01em;
  text-transform: none;
  color: var(--ink);
  text-decoration: none;
  border-bottom: 1px solid var(--accent);
}

.cl-note {
  font-family: var(--sans);
  text-transform: none;
  letter-spacing: 0;
  color: var(--ink-soft);
  font-size: 12px;
  margin-left: auto;
}

@media (max-width: 700px) {
  .companion-link { flex-wrap: wrap; gap: 8px; }
  .cl-note { margin-left: 0; }
}
```

- [ ] **Step 3**: In `parent_growth_path_preview.html`, add the mirror companion link pointing back to child recap:

```html
<div class="companion-link">
  <span class="cl-lbl">Companion surface</span>
  <a href="child_recap_preview.html">Child recap →</a>
  <span class="cl-note">Same tag block, different lens.</span>
</div>
```

Copy the same CSS.

- [ ] **Step 4**: Mirror Steps 1–3 in the CN files. CN copy:

```html
<div class="companion-link">
  <span class="cl-lbl">对应面</span>
  <a href="parent_growth_path_preview_cn.html">家长端成长路径 →</a>
  <span class="cl-note">同一份 tag block，换一个视角。</span>
</div>
```

And for the parent CN file: points to `child_recap_preview_cn.html`.

- [ ] **Step 5**: Verify EN in both docs.

```js
// Run in each doc
({
  companionExists: !!document.querySelector('.companion-link'),
  companionTarget: document.querySelector('.companion-link a')?.getAttribute('href'),
})
```

Expected: companion exists in both; child recap's companion → `parent_growth_path_preview.html`; parent dashboard's companion → `child_recap_preview.html`.

- [ ] **Step 6**: Verify CN in both docs — expect `_cn.html` targets.

- [ ] **Step 7**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "docs: add companion-surface cross-links between child recap and parent dashboard docs"
```

---

## Task 13 · Verification pass — all six files

**Files:** (no edits)

- [ ] **Step 1**: Desktop viewport check. Resize preview to 1280×1000. Navigate to each of the 6 files in order:
  1. `template_0_preview.html` — confirm reference strip renders, links work
  2. `template_0_preview_cn.html` — same
  3. `child_recap_preview.html` — scroll through all sections, confirm no empty sections
  4. `child_recap_preview_cn.html` — same
  5. `parent_growth_path_preview.html` — scroll through, confirm curiosity radial + all modules render
  6. `parent_growth_path_preview_cn.html` — same

For each, eval:

```js
({
  title: document.title,
  sectionCount: document.querySelectorAll('section[id]').length,
  hasBreadcrumb: !!document.querySelector('.breadcrumb'),
  hasCompanion: !!document.querySelector('.companion-link'),
  hasRevnote: !!document.querySelector('.revnote'),
})
```

Expected per file:
- Template 0 EN/CN: no breadcrumb, no companion (those are for the surface docs only), has revnote
- Child recap EN/CN: breadcrumb + companion + revnote; sectionCount = 7 (purpose, anti-addiction, layout, contract, moment-rule, persistence, copy-tone, edges, open — approx 9 sections)
- Parent dashboard EN/CN: breadcrumb + companion + revnote; sectionCount = 11 sections

- [ ] **Step 2**: Console error check. For each of the 6 files:

```js
// Run preview_console_logs with level: 'error'
```

Expected: no errors for any file.

- [ ] **Step 3**: Mobile viewport check. Resize to 375×812. Navigate to each file; confirm:
  - Masthead collapses / breadcrumb hides (as designed by media query)
  - Grid layouts collapse to single column
  - No horizontal overflow (eval `document.documentElement.scrollWidth` — should equal 375)
  - All text is readable

Eval per file:

```js
({
  scrollWidth: document.documentElement.scrollWidth,
  viewportWidth: window.innerWidth,
  overflow: document.documentElement.scrollWidth > window.innerWidth,
})
```

Expected: `overflow: false` for all 6 files.

- [ ] **Step 4**: Click-through test. From Template 0:
  - Click first surface card → lands on child recap doc
  - From child recap, click breadcrumb → back to Template 0
  - From child recap, click companion link → lands on parent dashboard
  - From parent dashboard, click companion link → back to child recap
  - All back and forward navigation works

- [ ] **Step 5**: EN/CN drift check. Diff section IDs between EN and CN pairs:

```js
// Run in each EN file
JSON.stringify(Array.from(document.querySelectorAll('section[id]')).map(s => s.id))
```

Then same in matching CN file. Arrays must be identical per file pair.

- [ ] **Step 6**: Revnote content check. Eval in Template 0:

```js
document.querySelectorAll('.revnote ol li').length
```

Expected: 5 bullets (v0.2 original 4 + the new "downstream surfaces extracted" bullet).

- [ ] **Step 7**: If any verification fails, fix inline and re-verify. Do not commit bug fixes as a new task — amend to the latest commit or add a `fix:` commit before continuing.

- [ ] **Step 8**: Commit nothing (verification-only task); move to Task 14.

---

## Task 14 · Rebase, push, PR

**Files:** (git operations)

- [ ] **Step 1**: Update `.claude/launch.json` is correct for the worktree — it should be untouched from the earlier commit.

- [ ] **Step 2**: Check branch state.

```bash
git log --oneline main..HEAD
```

Expected: 10–11 commits visible (Tasks 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).

- [ ] **Step 3**: Rebase on latest main if main has moved.

```bash
git fetch origin
git rebase origin/main
```

Resolve conflicts if any. Most likely conflicts would be in `template_0_preview.html` if someone else edited it.

- [ ] **Step 4**: Run the verification pass from Task 13 one more time to confirm no regressions from rebase.

- [ ] **Step 5**: Push the branch.

```bash
git push -u origin feat/downstream-surfaces-split
```

- [ ] **Step 6**: Open PR.

```bash
gh pr create --title "Downstream surfaces split — child recap + parent dashboard design docs" --body "$(cat <<'EOF'
## Summary

Extracts child recap and parent growth path out of Template 0's §05 into their own full-fidelity preview docs, per design spec `docs/plans/2026-04-17-downstream-surfaces-split-design.md`.

- Template 0 §05 → compact reference strip pointing to both new docs
- `docs/child_recap_preview.html` (+ `_cn.html`) — 10 sections including anti-addiction principles table and 8 concrete mechanisms
- `docs/parent_growth_path_preview.html` (+ `_cn.html`) — 11 sections with 4 new modules beyond the L×T ladder (curiosity radial, in-their-words, try-at-home, gauges strip)
- Tag-block legend in Template 0 §04 now stacks below YAML (layout tweak)

## Test plan

- [ ] Desktop preview at 1280×1000 — all 6 files render
- [ ] Mobile preview at 375×812 — no horizontal overflow
- [ ] Click-through: Template 0 reference strip → both new docs; breadcrumbs back; companion links between new docs
- [ ] Console clean (no errors) on all 6 files
- [ ] EN/CN section IDs match per pair

## Depends on

Design spec: `docs/plans/2026-04-17-downstream-surfaces-split-design.md`
EOF
)"
```

- [ ] **Step 7**: Note PR URL in response to user.

---

## Task 15 · Post-merge cleanup

- [ ] **Step 1**: After PR merge, return to main worktree.

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git checkout main
git pull
```

- [ ] **Step 2**: Remove the feature worktree.

```bash
git worktree remove .worktrees/feat/downstream-surfaces-split
git branch -d feat/downstream-surfaces-split
```

- [ ] **Step 3**: Done.

---

## Completion criteria — spec verification checklist

Mirrors spec §8. Every item must be checkable from a finished implementation:

- [ ] `template_0_preview.html`: `.tagblock` stacks vertically on all viewports (Task 2)
- [ ] `template_0_preview.html`: §05 downstream mockups replaced with 2-card reference strip (Task 11)
- [ ] `template_0_preview.html`: revnote v0.2 has the "downstream surfaces extracted" bullet (Task 11)
- [ ] `template_0_preview_cn.html`: all three items above mirrored (Tasks 2, 11)
- [ ] `docs/child_recap_preview.html` exists and matches the 10-section spec in §4 (Tasks 3–6)
- [ ] `docs/child_recap_preview_cn.html` exists and mirrors the English version (Tasks 3–6)
- [ ] `docs/parent_growth_path_preview.html` exists and matches the 11-section spec in §5 (Tasks 7–10)
- [ ] `docs/parent_growth_path_preview_cn.html` exists and mirrors the English version (Tasks 7–10)
- [ ] Reference strip in Template 0 §05 correctly links to both new docs (Task 11)
- [ ] Both new docs have masthead breadcrumb back to Template 0 (Tasks 3, 7)
- [ ] Both new docs have footer companion-link to each other (Task 12)
- [ ] All four new files share the same `:root` CSS custom properties as Template 0 (Tasks 3, 7 — via copy-clone)
- [ ] Preview server renders all four new files with no console errors (Task 13)
- [ ] Mobile layout (375×812) tested for all four new files (Task 13)
