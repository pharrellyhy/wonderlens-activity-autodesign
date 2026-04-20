# Matchability Tags Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to execute this plan task-by-task. After each task, run **code-reviewer** (pr-review-toolkit:code-reviewer) and **code-simplifier** (pr-review-toolkit:code-simplifier) agents. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three matchability tags (`entity_binding`, `entity_class`, `tier_range`) to Template 0's tag block and make the upstream matcher visible as a pipeline stage in §05. Ship a new `docs/entity_ontology.md` as the class-hierarchy reference. Version bump Template 0 v0.2 → v0.3.

**Architecture:** Pure docs PR on top of v0.2. Edits 6 HTML files (Template 0, child recap, parent dashboard — EN + CN each), plus 1 net-new markdown file (`docs/entity_ontology.md`). No code changes, no JS. Same aesthetic discipline as the surfaces-split PR.

**Tech Stack:** Plain HTML/CSS in the existing design-system tokens; markdown for the ontology. Git worktree under `.worktrees/feat/matchability-tags/`. Preview server via MCP Claude_Preview on port 8765.

**Design authority:** `docs/plans/2026-04-20-matchability-tags-design.md`

---

## Task 1 · Worktree setup

**Files:** (git operations)

- [ ] **Step 1**: From main repo root, confirm branch state.

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git fetch origin
git status
```

Expected: clean working tree on `main` (or whatever branch was active after merging the surfaces-split PR — if PR #2 hasn't merged yet, base off `origin/main` anyway since this branch is independent).

- [ ] **Step 2**: Create the worktree.

```bash
git worktree add -b feat/matchability-tags .worktrees/feat/matchability-tags origin/main
cd .worktrees/feat/matchability-tags
```

- [ ] **Step 3**: Update `.claude/launch.json` to point the preview server at this worktree's docs.

Read the current launch.json in the main repo (`/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.claude/launch.json`). If `-d` points at a different worktree (e.g. downstream-surfaces-split), update it to:

```json
"runtimeArgs": ["-m", "http.server", "8765", "-d", "/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/matchability-tags/docs"]
```

This is a one-line edit. Don't commit it — it's a local config.

- [ ] **Step 4**: Stop any running preview server and restart it pointing at the new path.

Via MCP Claude_Preview: `preview_stop` on the existing serverId (if any), then `preview_start` with `name: "walkthrough"`. Confirm it serves `parent_growth_path_preview.html` OR `template_0_preview.html` from the worktree's docs at http://localhost:8765.

- [ ] **Step 5**: Commit nothing (worktree setup is environmental).

---

## Task 2 · Create `docs/entity_ontology.md`

**Spec reference**: design §5

**Files:**
- Create: `docs/entity_ontology.md`

- [ ] **Step 1**: Draft the file. Structure per design §5.2:

```markdown
# Entity Ontology

> Canonical class hierarchy for the `entity_class` tag in Template 0's tag block. Every entity appearing in an activity design must have a chain that resolves against this file.

**Version**: v0.1 · 2026-04-20 · Inaugural
**Upstream**: `docs/template_0_preview.html` §04

---

## Purpose

`entity_class` is an ordered list from specific to general (e.g. `[ladybug, beetle, insect, small_creature, living_thing, observable_thing]`). The upstream matcher uses this chain to roll up when exact-entity matches miss — "we have no ladybug activities but we have an `insect` activity tagged `parameterized`, so serve that one."

This file defines which class names are valid and how entities roll up.

---

## Top-level class

- `observable_thing` — the root. Used alone only by `entity_binding: agnostic` activities.

---

## Taxonomic hierarchy

```
observable_thing
├── natural_thing
│   ├── living_thing
│   │   ├── animal
│   │   │   ├── insect
│   │   │   │   ├── beetle
│   │   │   │   │   ├── ladybug
│   │   │   │   │   └── weevil
│   │   │   │   ├── bee
│   │   │   │   ├── ant
│   │   │   │   ├── caterpillar
│   │   │   │   └── butterfly
│   │   │   ├── arachnid
│   │   │   │   └── spider
│   │   │   ├── mollusk
│   │   │   │   ├── snail
│   │   │   │   └── slug
│   │   │   ├── bird
│   │   │   ├── mammal
│   │   │   └── fish
│   │   ├── plant
│   │   │   ├── flower
│   │   │   │   ├── sunflower
│   │   │   │   ├── daisy
│   │   │   │   └── rose
│   │   │   ├── tree
│   │   │   ├── fruit
│   │   │   │   ├── apple
│   │   │   │   └── banana
│   │   │   ├── vegetable
│   │   │   └── leaf
│   │   └── fungus
│   │       └── mushroom
│   └── non_living_natural_thing
│       ├── rock
│       ├── water
│       │   ├── puddle
│       │   └── stream
│       ├── weather_phenomenon
│       │   ├── cloud
│       │   └── rainbow
│       └── celestial
│           ├── sun
│           └── moon
└── human_made_thing
    ├── vehicle
    │   ├── car
    │   ├── bicycle
    │   ├── truck
    │   └── airplane
    ├── tool
    │   ├── scissors
    │   └── paintbrush
    ├── toy
    │   ├── doll
    │   ├── ball
    │   └── block
    ├── food
    │   ├── bread
    │   └── fruit_prepared
    ├── container
    │   ├── cup
    │   └── box
    ├── clothing
    └── instrument
```

---

## Abstract / cross-cutting classes

These aren't strict taxonomy — they tag *capability*. An entity can belong to multiple abstract classes in addition to its taxonomic chain.

| Abstract class | Member examples | Used for activities about |
|---|---|---|
| `small_creature` | ladybug, bee, ant, caterpillar, snail, slug, spider, small bird | Gentle observation, holding, attribute naming |
| `warning_colored_small_creature` | ladybug, bee, wasp, monarch caterpillar, poison-dart frog | Causation (why warning colors?), biology |
| `patterned_thing` | ladybug, zebra, giraffe, butterfly, polka-dot cup, striped fabric | Form, pattern recognition |
| `moving_thing` | any animal, vehicle, leaves in wind, flowing water | Change, motion, causation |
| `handheld_thing` | pencil, apple, cup, toy, small rock | Fine motor, close observation |
| `edible_thing` | fruit, vegetable, bread, prepared food | Sensory, food origin |

---

## Usage rules for activity authors

1. **Every activity with a specific nominal entity** declares an `entity_class` chain starting at the entity and rolling up to `observable_thing`.
2. **Abstract class memberships are additive** — an activity can target `entity_class: [ladybug, beetle, insect, small_creature, warning_colored_small_creature, living_thing, observable_thing]` to enable rollup on either axis.
3. **`entity_binding: agnostic` activities** use the minimal chain: `entity_class: [observable_thing]`.
4. **Adding a new entity**: if your activity uses an entity not in this file, add it to the ontology in the same PR as the activity. New entities never break existing chains.
5. **Never shrink the ontology** — renaming or removing a class is a breaking change requiring repo-wide migration and a version bump to v1.0.

---

## Example chains

| Nominal entity | Typical chain |
|---|---|
| ladybug | `[ladybug, beetle, insect, small_creature, warning_colored_small_creature, patterned_thing, living_thing, natural_thing, observable_thing]` |
| sunflower | `[sunflower, flower, plant, living_thing, natural_thing, observable_thing]` |
| apple | `[apple, fruit, plant, edible_thing, living_thing, natural_thing, observable_thing]` |
| car (toy) | `[car, vehicle, moving_thing, human_made_thing, observable_thing]` |
| cloud | `[cloud, weather_phenomenon, non_living_natural_thing, natural_thing, observable_thing]` |

---

## Versioning

- **v0.1** (2026-04-20) — Inaugural file. Covers the 7 running examples across Template 0 + surfaces docs (ladybug, sunflower, apple, ladybug variations) plus enough breadth to seed matcher development.

Append-only growth. Breaking changes bump to v1.0 and require coordinated migration of all tag blocks.
```

- [ ] **Step 2**: Verify the file exists and has the expected structure.

```bash
wc -l docs/entity_ontology.md  # expect 100-150 lines
grep -c "^## " docs/entity_ontology.md  # expect 6-7 H2 sections
grep "ladybug" docs/entity_ontology.md  # should appear in both the hierarchy and the example chains table
```

- [ ] **Step 3**: Commit.

```bash
git add docs/entity_ontology.md
git commit -m "feat(docs): add entity_ontology.md — canonical class hierarchy for entity_class tag"
```

---

## Task 3 · Template 0 §04 additions — EN

**Spec reference**: design §4.1, §4.2

**Files:**
- Modify: `docs/template_0_preview.html`

- [ ] **Step 1**: Locate the tag-block YAML in §04. Grep for the existing `entity:` line.

```bash
grep -n "entity:" docs/template_0_preview.html | head -5
```

- [ ] **Step 2**: Add three new fields to the YAML block. Place them immediately AFTER the existing `entity:` line and BEFORE the tier field. Use the same `<span class="key">` / `<span class="str">` / `<span class="cmt">` span structure the existing YAML uses (grep to see the pattern).

New YAML content to insert:

```yaml
entity_class:  [ladybug, beetle, insect, small_creature, warning_colored_small_creature, living_thing, observable_thing]   # ordered specific → general
entity_binding: parameterized   # bound | parameterized | agnostic

tier_range:
  primary:    T1
  span:       [T0, T1, T2]
  elasticity: neighbor          # strict | neighbor | broad
```

Render these with the same span-wrapped syntax-highlighting approach used by neighboring fields. Use `<span class="cmt"># comment</span>` for the trailing comments.

- [ ] **Step 3**: Replace the existing single-value `tier: T1` line with a note or mark it as legacy-shorthand since it's now subsumed by `tier_range.primary`. Options:
  - Option A (recommended): Remove the standalone `tier:` line entirely — `tier_range.primary` is now the source of truth
  - Option B: Keep `tier: T1` with a `# deprecated: use tier_range.primary` comment

Pick Option A for cleanliness.

- [ ] **Step 4**: Locate the legend block below the YAML. Add a new sub-section titled **"Matchability — three tags that keep a small catalog portable"**.

Content for the new sub-section (paste as a `.legend-row` or equivalent block matching the existing legend structure):

```html
<div class="legend-row">
  <div class="legend-key"><code>entity_class</code></div>
  <div class="legend-val">Ordered list from specific to general. The matcher rolls up when exact-entity matches miss. See <a href="entity_ontology.md"><code>docs/entity_ontology.md</code></a> for the canonical class hierarchy.</div>
</div>
<div class="legend-row">
  <div class="legend-key"><code>entity_binding</code></div>
  <div class="legend-val"><code>bound</code> = activity needs this specific entity. <code>parameterized</code> = entity is a slot; works for any member of the class. <code>agnostic</code> = cognitive drill, works on anything.</div>
</div>
<div class="legend-row">
  <div class="legend-key"><code>tier_range</code></div>
  <div class="legend-val"><code>primary</code> = preferred tier. <code>span</code> = accepted tiers. <code>elasticity</code>: <code>strict</code> = primary only; <code>neighbor</code> = ±1 tier; <code>broad</code> = all three.</div>
</div>
```

- [ ] **Step 5**: Add a static-vs-dynamic annotation. Right after the new matchability legend rows, add a two-column table:

```html
<div class="tag-lifecycle">
  <div class="tl-head">Tag lifecycle — catalog-time vs instance-time</div>
  <div class="tl-grid">
    <div class="tl-col">
      <div class="tl-lbl">Catalog-time · author declares</div>
      <div class="tl-body">
        <code>entity_class</code>, <code>entity_binding</code>, <code>tier_range</code>, <code>pillar</code>, <code>key_concepts</code>, <code>atl_skills</code>, <code>subject_tags</code>, <code>transdisciplinary_theme</code>, <code>category</code>, <code>progression.topic_axis</code>
      </div>
    </div>
    <div class="tl-col">
      <div class="tl-lbl">Instance-time · runtime populates</div>
      <div class="tl-body">
        <code>entity</code> (what was seen), <code>tier</code> (child's actual tier), <code>highlight_moment</code> (runtime one-liner), <code>caregiver_role</code> (observed), <code>progression.difficulty_level</code> (rung reached), <code>progression.next_step_hint</code>
      </div>
    </div>
  </div>
  <div class="tl-foot">Rule of thumb: if the value would differ between two children playing the "same" activity, it's instance-time.</div>
</div>
```

Add corresponding CSS to the `<style>` block. Use existing tokens:

```css
.tag-lifecycle {
  margin-top: 24px;
  padding: 20px 24px;
  background: color-mix(in srgb, var(--accent) 5%, var(--bg));
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.tl-head {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}
.tl-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
@media (max-width: 960px) {
  .tl-grid { grid-template-columns: 1fr; }
}
.tl-lbl {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
}
.tl-body {
  font-size: 13px;
  line-height: 1.6;
  color: var(--ink-soft);
}
.tl-body code {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--accent);
  padding: 1px 4px;
  background: color-mix(in srgb, var(--accent) 6%, transparent);
  border-radius: 2px;
  margin-right: 2px;
}
.tl-foot {
  margin-top: 14px;
  font-family: var(--serif);
  font-style: italic;
  font-size: 13px;
  color: var(--ink-soft);
}
```

- [ ] **Step 6**: Verify EN.

```js
({
  yamlHasEntityClass: !!document.body.innerText.match(/entity_class/),
  yamlHasEntityBinding: !!document.body.innerText.match(/entity_binding/),
  yamlHasTierRange: !!document.body.innerText.match(/tier_range/),
  lifecycleExists: !!document.querySelector('.tag-lifecycle'),
  lifecycleCols: document.querySelectorAll('.tag-lifecycle .tl-col').length,
})
```

Expected: all YAML fields present, lifecycle exists, 2 columns.

- [ ] **Step 7**: Commit.

```bash
git add docs/template_0_preview.html
git commit -m "feat(template-0-en): add matchability tags to §04 YAML + legend + static-vs-dynamic annotation"
```

---

## Task 4 · Template 0 §04 additions — CN mirror

**Files:**
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1**: Apply the same YAML additions as Task 3 Step 2 to the CN file. YAML field names stay English; the `# comment` trailing text stays English too (matches the existing CN convention for YAML comments).

- [ ] **Step 2**: Same cleanup as Task 3 Step 3 (remove standalone `tier:` line in favor of `tier_range.primary`).

- [ ] **Step 3**: Add the CN matchability legend rows. Translate prose; keep YAML token names (`entity_class`, `entity_binding`, `tier_range`, `bound`, `parameterized`, `agnostic`, `primary`, `span`, `elasticity`, `strict`, `neighbor`, `broad`) in English.

Suggested CN translations:

| EN | CN |
|---|---|
| "Ordered list from specific to general. The matcher rolls up when exact-entity matches miss." | "由具体到宽泛的有序列表。精确匹配未命中时，matcher 会沿链条上滚。" |
| "bound = activity needs this specific entity." | "`bound` = 活动依赖这个具体 entity。" |
| "parameterized = entity is a slot; works for any member of the class." | "`parameterized` = entity 是个槽位；对该类中的任意成员都适用。" |
| "agnostic = cognitive drill, works on anything." | "`agnostic` = 认知训练，对任何东西都适用。" |
| "primary = preferred tier." | "`primary` = 首选 tier。" |
| "span = accepted tiers." | "`span` = 可接受的 tier 列表。" |
| "elasticity: strict = primary only; neighbor = ±1 tier; broad = all three." | "`elasticity`: `strict` = 只支持 primary；`neighbor` = ±1 tier；`broad` = 全部三档。" |

For the ontology link: `<a href="entity_ontology.md"><code>docs/entity_ontology.md</code></a>` — keep English filename (no CN translation of file paths).

- [ ] **Step 4**: Add the CN static-vs-dynamic annotation. Translate labels:

| EN | CN |
|---|---|
| "Tag lifecycle — catalog-time vs instance-time" | "标签生命周期 · 目录时 vs 运行时" |
| "Catalog-time · author declares" | "目录时 · 作者声明" |
| "Instance-time · runtime populates" | "运行时 · 填充" |
| "Rule of thumb: if the value would differ between two children playing the 'same' activity, it's instance-time." | "规律: 两个孩子玩'同一个'活动时这个值会不同的，就是运行时字段。" |

YAML field names stay English in the body text.

- [ ] **Step 5**: Add the same CSS rules added in Task 3 Step 5. CSS is identical in both files.

- [ ] **Step 6**: Verify CN.

Same JS eval as Task 3 Step 6.

- [ ] **Step 7**: Commit.

```bash
git add docs/template_0_preview_cn.html
git commit -m "feat(template-0-cn): mirror §04 matchability additions"
```

---

## Task 5 · Template 0 §05 — rename + flow diagram + reference strip — EN

**Spec reference**: design §4.3

**Files:**
- Modify: `docs/template_0_preview.html`

- [ ] **Step 1**: Rename the §05 section title.

Find the `.sec-num` or equivalent heading for §05 (grep for `§ 05` in the file). Change:

- From: `§ 05 / Downstream`
- To: `§ 05 / Data pipeline · upstream &amp; downstream`

Also update the `<nav>` / masthead TOC link text accordingly (grep for `#bridges` to find the nav link).

- [ ] **Step 2**: Add two new upstream boxes to the flow diagram.

Locate the existing `.pipeline` / `.flow-box` structure (grep for `pipeline` or `flow-box`). Insert two new boxes BEFORE the existing Tier A / B / P upstream bridge:

```html
<div class="flow-box flow-moment">
  <div class="fb-label">Moment</div>
  <div class="fb-body">
    <div class="fb-line">entity seen <span class="fb-tag">(camera)</span></div>
    <div class="fb-line">tier <span class="fb-tag">(onboarding)</span></div>
    <div class="fb-line">setting <span class="fb-tag">(time + place)</span></div>
    <div class="fb-line">caregiver present <span class="fb-tag">(runtime)</span></div>
  </div>
</div>

<div class="flow-arrow">↓</div>

<div class="flow-box flow-matcher">
  <div class="fb-label">Matcher</div>
  <div class="fb-body">
    <div class="fb-desc">Reads catalog tag blocks · ranks by <code>entity_class</code> rollup + <code>tier_range</code> fit · picks best-matching activity shell.</div>
  </div>
</div>

<div class="flow-arrow">↓</div>
```

These boxes should go ABOVE the existing "Tier A / B / P" cards. The existing cards stay but get re-framed: they describe *what* the matcher is choosing from.

CSS for the new boxes (add to `<style>`):

```css
.flow-box.flow-moment,
.flow-box.flow-matcher {
  padding: 16px 20px;
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
  margin: 12px 0;
}
.flow-box .fb-label {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 8px;
}
.flow-box .fb-line {
  font-size: 13px;
  color: var(--ink-soft);
  margin: 2px 0;
}
.flow-box .fb-tag {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--muted);
  margin-left: 6px;
}
.flow-box .fb-desc {
  font-size: 13px;
  line-height: 1.55;
  color: var(--ink-soft);
}
.flow-box .fb-desc code {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--accent);
}
.flow-arrow {
  text-align: center;
  font-family: var(--mono);
  font-size: 20px;
  color: var(--muted);
  margin: 4px 0;
}
```

If `.flow-box` already exists in the doc with different styling, scope the new rules to `.flow-box.flow-moment` and `.flow-box.flow-matcher` to avoid conflict.

- [ ] **Step 3**: Add the "Upstream reads" prefix row BEFORE the existing `<div class="surface-strip">`.

```html
<div class="upstream-reads">
  <div class="ur-head">Upstream reads <span class="ur-sub">· catalog-time</span></div>
  <div class="ur-body">
    <code>entity_class</code> · <code>entity_binding</code> · <code>tier_range</code> · <code>pillar</code> · <code>category</code> · <code>progression.topic_axis</code> · <code>key_concepts</code> · <code>atl_skills</code> · <code>subject_tags</code> · <code>transdisciplinary_theme</code>
  </div>
  <div class="ur-note">Matcher logic: see <code>docs/upstream_matcher.md</code> <em>(to be written separately)</em>.</div>
</div>

<div class="downstream-reads-head">Downstream reads <span class="ur-sub">· instance-time</span></div>

<!-- existing surface-strip follows unchanged -->
```

CSS:

```css
.upstream-reads {
  margin: 32px 0 20px;
  padding: 18px 22px;
  background: color-mix(in srgb, var(--accent) 4%, var(--bg));
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.ur-head {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}
.ur-sub {
  color: var(--muted);
  font-weight: normal;
  letter-spacing: 0.08em;
}
.ur-body {
  font-size: 13px;
  line-height: 1.9;
  color: var(--ink-soft);
}
.ur-body code {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--accent);
  padding: 2px 6px;
  background: color-mix(in srgb, var(--accent) 8%, transparent);
  border-radius: 2px;
}
.ur-note {
  margin-top: 12px;
  font-family: var(--serif);
  font-style: italic;
  font-size: 12px;
  color: var(--muted);
}
.downstream-reads-head {
  margin-top: 20px;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}
```

- [ ] **Step 4**: Verify EN.

```js
({
  sec05Title: document.querySelector('#bridges .sec-num, #bridges h2')?.innerText,
  momentBox: !!document.querySelector('.flow-moment'),
  matcherBox: !!document.querySelector('.flow-matcher'),
  upstreamReads: !!document.querySelector('.upstream-reads'),
  surfaceCardsStillPresent: document.querySelectorAll('.surface-card').length,
})
```

Expected: title contains "Data pipeline", both new boxes exist, upstream-reads exists, surface cards still = 2.

- [ ] **Step 5**: Commit.

```bash
git add docs/template_0_preview.html
git commit -m "feat(template-0-en): §05 pipeline — rename + matcher upstream stage + catalog-time reads prefix"
```

---

## Task 6 · Template 0 §05 — CN mirror

**Files:**
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1**: Apply the same Task 5 changes to the CN file.

- Section title CN: `§ 05 / 数据管线 · 上游 · 下游`
- Nav link text CN: `数据管线` (or whatever existing CN nav term was used — check consistency)

- [ ] **Step 2**: Translate flow-box content:

| EN | CN |
|---|---|
| Moment | 场景 |
| entity seen (camera) | 看到的 entity（相机） |
| tier (onboarding) | tier（入门设置） |
| setting (time + place) | 环境（时间 + 地点） |
| caregiver present (runtime) | 照护者在场（运行时） |
| Matcher | 匹配器 |
| "Reads catalog tag blocks · ranks by entity_class rollup + tier_range fit · picks best-matching activity shell." | "读取目录标签块 · 按 `entity_class` 上滚 + `tier_range` 适配排序 · 选出最佳匹配的活动骨架。" |

YAML field names (`entity_class`, `tier_range`) stay English inside `<code>` tags.

- [ ] **Step 3**: Translate upstream-reads strip:

| EN | CN |
|---|---|
| "Upstream reads · catalog-time" | "上游读取 · 目录时" |
| "Downstream reads · instance-time" | "下游读取 · 运行时" |
| "Matcher logic: see docs/upstream_matcher.md (to be written separately)." | "匹配器逻辑: 见 `docs/upstream_matcher.md`（单独成文）。" |

YAML token names stay English.

- [ ] **Step 4**: Same CSS as Task 5 Step 2 and Step 3. Identical in both files.

- [ ] **Step 5**: Verify CN.

Same JS eval as Task 5 Step 4.

- [ ] **Step 6**: Commit.

```bash
git add docs/template_0_preview_cn.html
git commit -m "feat(template-0-cn): mirror §05 pipeline upstream stage"
```

---

## Task 7 · Template 0 version bump + revnote — EN + CN

**Spec reference**: design §4.4, §4.5

**Files:**
- Modify: `docs/template_0_preview.html`
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1**: Find the version indicator in EN. Grep for `v0.2` or `Version 0.2` in the masthead/meta and the footer version block.

Update:
- Masthead `.meta` or equivalent: `Draft v0.2` → `Draft v0.3`
- Footer `.version` block: `Version 0.2` → `Version 0.3`
- Any page-level `<title>` or header referencing "v0.2" — update to "v0.3"

- [ ] **Step 2**: Append the new revnote bullet to the EN revnote `<ol>`. Place it as the LAST bullet (newest on top is NOT the pattern; this doc appends).

```html
<li><b>Matchability tags added</b> (§04) + <b>upstream pipeline made explicit</b> (§05) — three new static fields (<code>entity_binding</code>, <code>entity_class</code>, <code>tier_range</code>) let one activity match many moments. §05's flow diagram now shows the matcher as a distinct upstream stage reading catalog-time tags; downstream surfaces unchanged. See <code>docs/plans/2026-04-20-matchability-tags-design.md</code>.</li>
```

Confirm revnote `<ol>` bullet count is now 6 (was 5 after surfaces-split).

- [ ] **Step 3**: CN file — same version bump (`v0.2` → `v0.3`) everywhere EN was changed.

- [ ] **Step 4**: Append the CN revnote bullet:

```html
<li><b>新增 matchability 标签</b>（§04）+ <b>明确上游管线</b>（§05）——三个新增的静态字段（<code>entity_binding</code>、<code>entity_class</code>、<code>tier_range</code>）让一个活动能匹配更多场景。§05 流程图现在把 matcher 作为独立的上游阶段，读取目录时标签；下游面不变。见 <code>docs/plans/2026-04-20-matchability-tags-design.md</code>。</li>
```

- [ ] **Step 5**: Verify both files.

```js
// Run in each file
({
  metaVersion: document.querySelector('.meta')?.innerText,
  footerVersion: document.querySelector('.version')?.innerText,
  revnoteBullets: document.querySelectorAll('.revnote ol li').length,
})
```

Expected: metaVersion contains "v0.3", footerVersion contains "0.3", revnoteBullets === 6 in both files.

- [ ] **Step 6**: Commit.

```bash
git add docs/template_0_preview.html docs/template_0_preview_cn.html
git commit -m "feat(template-0): bump v0.2 → v0.3 + revnote for matchability tags"
```

---

## Task 8 · Downstream doc contract annotations

**Spec reference**: design §6

**Files:**
- Modify: `docs/child_recap_preview.html`
- Modify: `docs/child_recap_preview_cn.html`
- Modify: `docs/parent_growth_path_preview.html`
- Modify: `docs/parent_growth_path_preview_cn.html`

- [ ] **Step 1**: In `docs/child_recap_preview.html` §04 (Tag-block contract), locate the "Explicitly not read" note block (grep for "Explicitly not read" or "explicitly not").

Append one more line / bullet to that list:

```html
<div class="contract-not-read-row">
  <code>entity_binding</code>, <code>entity_class</code>, <code>tier_range</code> — matcher-only tags; child recap reads the resolved instance values (<code>entity</code>, <code>tier</code>), not the declaration shape.
</div>
```

Match the existing class/structure of sibling "not read" rows — grep to see the pattern.

- [ ] **Step 2**: Mirror in `docs/child_recap_preview_cn.html`:

```html
<div class="contract-not-read-row">
  <code>entity_binding</code>、<code>entity_class</code>、<code>tier_range</code> — matcher 专用标签；儿童端回顾读取解析后的运行时值（<code>entity</code>、<code>tier</code>），不读声明形态。
</div>
```

- [ ] **Step 3**: In `docs/parent_growth_path_preview.html` §07 (Tag-block contract full), append to its "Explicitly not read" section:

```html
<div class="contract-not-read-row">
  <code>entity_binding</code>, <code>entity_class</code>, <code>tier_range</code> — matcher-only tags; the parent dashboard reads resolved instance values, not the declaration shape.
</div>
```

- [ ] **Step 4**: Mirror in `docs/parent_growth_path_preview_cn.html`:

```html
<div class="contract-not-read-row">
  <code>entity_binding</code>、<code>entity_class</code>、<code>tier_range</code> — matcher 专用标签；家长端面板读取运行时值，不读声明形态。
</div>
```

- [ ] **Step 5**: Verify all 4 files.

```js
// In each of the 4 docs
document.body.innerText.includes('matcher-only tags') || document.body.innerText.includes('matcher 专用标签')
```

Expected: true in all 4.

- [ ] **Step 6**: Commit.

```bash
git add docs/child_recap_preview.html docs/child_recap_preview_cn.html docs/parent_growth_path_preview.html docs/parent_growth_path_preview_cn.html
git commit -m "docs: annotate matcher-only tags in child recap + parent dashboard contract tables"
```

---

## Task 9 · 6-file verification pass

**Files:** (no edits)

Same protocol as the surfaces-split Task 13, scoped to validate the matchability additions.

- [ ] **Step 1**: Desktop 1280×1000 — navigate to each of the 6 files:

```
http://localhost:8765/template_0_preview.html
http://localhost:8765/template_0_preview_cn.html
http://localhost:8765/child_recap_preview.html
http://localhost:8765/child_recap_preview_cn.html
http://localhost:8765/parent_growth_path_preview.html
http://localhost:8765/parent_growth_path_preview_cn.html
```

Per-file eval:

```js
({
  title: document.title,
  sectionCount: document.querySelectorAll('section[id]').length,
  hasBreadcrumb: !!document.querySelector('.breadcrumb'),
  hasCompanion: !!document.querySelector('.companion-link'),
  hasRevnote: !!document.querySelector('.revnote'),
  revnoteBullets: document.querySelectorAll('.revnote ol li').length,
})
```

Expected:
- Template 0 (EN + CN): revnote bullets = 6 (was 5)
- Child recap (EN + CN): revnote bullets unchanged (3)
- Parent dashboard (EN + CN): revnote bullets unchanged (3)
- All section counts unchanged (9 / 10 / 11 per doc)

- [ ] **Step 2**: Matchability-specific eval — Template 0 only (EN + CN):

```js
({
  yamlHasNewFields: ['entity_class', 'entity_binding', 'tier_range'].every(t => document.body.innerText.includes(t)),
  lifecycleExists: !!document.querySelector('.tag-lifecycle'),
  momentBox: !!document.querySelector('.flow-moment'),
  matcherBox: !!document.querySelector('.flow-matcher'),
  upstreamReadsBox: !!document.querySelector('.upstream-reads'),
  sec05TitleUpdated: !!document.body.innerText.match(/Data pipeline|数据管线/),
})
```

Expected: all true.

- [ ] **Step 3**: Console clean on all 6 files. Use `mcp__Claude_Preview__preview_console_logs` with `level: 'error'` — should return empty.

- [ ] **Step 4**: Mobile 375×812 — for each file:

```js
({
  scrollWidth: document.documentElement.scrollWidth,
  innerWidth: window.innerWidth,
  overflow: document.documentElement.scrollWidth > window.innerWidth,
})
```

Expected: `overflow: false` on all 6 (Template 0 mobile auto-zoom pre-existing issue is tracked separately, not a blocker).

- [ ] **Step 5**: EN/CN drift check — 3 pairs:

```js
JSON.stringify(Array.from(document.querySelectorAll('section[id]')).map(s => s.id))
```

EN vs CN arrays must be identical per pair.

- [ ] **Step 6**: Ontology file sanity:

```bash
ls -la docs/entity_ontology.md
grep -c "^## " docs/entity_ontology.md   # expect 6-7 H2 sections
grep "ladybug" docs/entity_ontology.md    # must appear
```

- [ ] **Step 7**: No commit (verification-only task).

---

## Task 10 · Push + PR

**Files:** (git operations)

- [ ] **Step 1**: Working tree clean check.

```bash
git status
```

Expected: clean.

- [ ] **Step 2**: Push.

```bash
git push -u origin feat/matchability-tags
```

- [ ] **Step 3**: Open PR.

```bash
gh pr create --base main --title "Matchability tags — keep the small catalog portable" --body "$(cat <<'EOF'
## Summary

Adds three matchability tags to Template 0's §04 tag block so one activity can match many upstream moments — addresses the recall-first ask raised after the downstream-surfaces-split PR.

- `entity_binding` — bound / parameterized / agnostic — declares entity swap-ability
- `entity_class` — ordered class chain, specific → general, for matcher rollup
- `tier_range` — primary + span + elasticity — accepts tier stretch

Also:
- §05 renamed from "Downstream" to "Data pipeline · upstream & downstream"
- §05 flow diagram gains Moment + Matcher boxes showing the upstream pipeline
- §05 reference strip prefixed with an "Upstream reads" row naming catalog-time fields
- New `docs/entity_ontology.md` — canonical class hierarchy for `entity_class`
- Child recap §04 + parent dashboard §07 contract tables annotated with "matcher-only" rows
- Template 0 bumped v0.2 → v0.3

## Design spec

`docs/plans/2026-04-20-matchability-tags-design.md`

## Test plan

- [x] Desktop + mobile preview on all 6 HTML files
- [x] Console clean
- [x] EN/CN section-ID drift: zero
- [x] Template 0 revnote bullets 5 → 6
- [x] Ontology markdown file valid, ladybug chain resolves
- [x] Matcher-only annotation present in child recap §04 + parent dashboard §07

## Out of scope (future rounds)

- Tier 2 matchability tags (`skill_focus`, `activity_shape`, `fallback_match`, `pillar_compatible`, `setting_flex`)
- Matcher logic implementation (`docs/upstream_matcher.md` — separate spec)
- Runtime telemetry for match quality

## Depends on

Template 0 v0.2 as shipped in PR #2 (downstream surfaces split).
EOF
)"
```

- [ ] **Step 4**: Note PR URL in report.

---

## Task 11 · Final cross-branch review

After all task-level commits land, dispatch a final reviewer for holistic cross-file inspection. Same protocol as the surfaces-split final review:

- Check design-token consistency across all 6 HTML files
- Verify EN/CN parity on the new elements
- Confirm navigation graph unchanged (no broken links)
- Spot-check accessibility: new boxes have proper heading hierarchy, tables have scope, code tags used consistently
- Verify no over-building (no tags added beyond the 3 specified, no §05 content beyond what the spec listed)
- Verify no under-building (all checklist items from design §9 pass)

Reviewer should approve with nits or request changes. Handle fixups via one cleanup subagent as needed.

---

## Execution notes for subagent-driven development

**Per-task cadence:**
1. Dispatch implementer subagent with full task text + pointers to design spec + reference files
2. Spec-compliance review (checks the commit matches the spec's letter)
3. Code-quality review (pr-review-toolkit:code-reviewer) — catches a11y, token discipline, EN/CN drift, consistency with siblings
4. Code-simplifier review (pr-review-toolkit:code-simplifier) — finds over-engineering, bloat, redundant CSS
5. Fixup loops for any Important items

**EN/CN parity** is the most common drift point — the simplifier should specifically watch for: English left in CN text, missing translations, YAML tokens accidentally translated, `<html lang="zh-Hans">` accidentally changed.

**Don't combine tasks across EN/CN** — keep them separate for clean per-file review. The design spec hands off 10-task granularity; follow it.
