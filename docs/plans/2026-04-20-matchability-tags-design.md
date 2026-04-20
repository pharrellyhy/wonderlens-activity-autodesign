# Matchability Tags — Design Spec

**Date:** 2026-04-20
**Status:** Draft, pending review
**Author-convention version:** Template 0 v0.2 (`docs/template_0_preview.html`)

---

## 1 · Context

Template 0 v0.2 established a tag block that acts as the contract between an activity design and its downstream surfaces (child recap + parent dashboard). That contract is tuned for **downstream summary** — the fields describe what the activity *was*, so the surfaces can render it.

The upstream side is underserved. Today, the agent invents one activity per moment; there's no notion of a **catalog** of pre-designed activities with a **matcher** selecting among them. As the catalog grows, we will need that matcher. And the catalog is small right now — which inverts the usual matching priority:

- Big catalog → optimize for **precision** (narrow down to the single best fit)
- Small catalog → optimize for **recall** (find *any* activity that plausibly fits)

Today's tag block is precision-oriented: `entity: ladybug`, `tier: T1`, `pillar: mystery` all *narrow* the match. With a 40-activity catalog and any given moment, this narrowing yields zero or one candidate. We need tags that let a single activity design fire for *many* moments — tags that describe the activity's **stretch**, not just its identity.

This doc specifies the minimal set of matchability tags to add to Template 0 v0.3, plus the pipeline-depiction changes needed in §05 to make the matcher's role visible.

### 1.1 Running example

A "ladybug mystery" activity today:
- `entity: ladybug` — fires only when a ladybug is seen
- `tier: T1` — fires only for 4–6 year olds
- `pillar: mystery`

With matchability tags, the same activity becomes portable:
- `entity_class: [ladybug, beetle, insect, small_creature, living_thing]` — rolls up to broader classes when exact match misses
- `entity_binding: parameterized` — entity is a slot, not a fixture; the reveal adapts to any `warning-colored_small_creature`
- `tier_range: {primary: T1, span: [T0, T1, T2], elasticity: neighbor}` — stretches one tier in either direction

Same activity, ~10× effective coverage. That's what this design delivers.

---

## 2 · Scope

### In scope

- **Three new tag fields** in Template 0 §04 tag block: `entity_binding`, `entity_class`, `tier_range`
- **Pipeline depiction update** in Template 0 §05: make the matcher visible as an upstream stage; split tag-block visualization into static (catalog) vs dynamic (instance) fields
- **New doc**: `docs/entity_ontology.md` defining the canonical entity class hierarchy (required for `entity_class` to function)
- **Downstream doc updates**: small addendum to child recap §04 contract + parent dashboard §07 contract noting which new fields are matcher-only (not read downstream)
- **Revnote**: Template 0 bumps to v0.3 with a dedicated bullet
- Same EN + CN parity discipline as the surfaces-split PR

### Out of scope (this round)

- **Matcher logic implementation** — how the matcher ranks candidates when multiple match. Belongs in a separate `docs/upstream_matcher.md` spec, drafted after this design lands.
- **Tier 2 matchability tags** — `skill_focus`, `activity_shape`, `fallback_match`, `pillar_compatible`, `setting_flex`. Deferred until the Tier 1 trio proves its value and authoring-cost budget allows more.
- **Catalog data layer** — how activity designs get stored, indexed, and served. Out of scope; depends on runtime architecture decisions not yet made.
- **Runtime telemetry** — how to detect when a match is "tolerated" vs "preferred" post-hoc. Separate measurement design.
- **The existing §04 YAML fields** — unchanged. We add, we don't refactor.
- **Existing §05 downstream reference strip** — unchanged. We add an upstream sibling; we don't touch the two existing cards.

### Deferred to a follow-up round (not this spec)

- `skill_focus` — content-neutral cognitive drill tag (observation / naming / hypothesis etc.)
- `activity_shape` — reusable mechanic id
- `fallback_match` — three-level graceful degradation
- `pillar_compatible` — multi-pillar activities
- `setting_flex`, `time_of_day_flex`, `energy_flex` — environmental stretch
- Mood / cultural / light / noise tags

All of the above are valid future additions but each carries real authoring cost and the catalog doesn't need them yet.

---

## 3 · The three tags

### 3.1 `entity_binding`

Declares how tightly coupled the activity is to its nominal entity.

```yaml
entity_binding: parameterized   # bound | parameterized | agnostic
```

| Value | Meaning | Example |
|---|---|---|
| `bound` | Activity depends on specific entity properties (e.g. a reveal about *this* entity's color + shape). Can't swap the entity without breaking the activity. | "Why is the ladybug red and not green?" — the answer is ladybug-specific folklore |
| `parameterized` | Entity is a slot. The activity's spine, pillar, and mechanic work for any entity satisfying `entity_class` membership constraints. | "Find three attributes that help this creature not get eaten" — works for ladybug, bee, wasp, monarch caterpillar |
| `agnostic` | Entity is decorative; the activity is really about the cognitive move. Works on literally anything the child sees. | "Name three things you notice" |

**Authoring cost**: very low — one of three values, chosen once per activity.
**Default**: `parameterized` (bias toward recall). `bound` and `agnostic` are opt-in declarations.

### 3.2 `entity_class`

An ordered list from specific to general, anchoring the activity in an entity hierarchy so the matcher can roll up when exact entity matches miss.

```yaml
entity_class:                     # ordered specific → general
  - ladybug
  - beetle
  - insect
  - small_creature
  - living_thing
  - observable_thing
```

**Matcher behavior**: try to match at index 0 first. If no catalog activity hits, walk the chain and try each broader level until a match is found or the chain exhausts.

**Shape constraints**:
- Must be an ordered list, not a single value
- Every link in the chain must appear in `docs/entity_ontology.md`
- Last entry MUST be a top-level class in the ontology (currently `observable_thing`)
- 2–8 entries typical; >10 suggests the ontology isn't structured enough

**Authoring cost**: low — look up the entity in the ontology, copy its chain into the activity's tag block. One-time ontology cost plus low per-activity cost.

**Relationship to `entity`**: `entity` stays as-is (the nominal / primary entity). `entity_class[0]` should equal `entity` when the activity is `bound` or `parameterized`; `agnostic` activities might have `entity: any` + a minimal `entity_class: [observable_thing]`.

### 3.3 `tier_range`

Replaces the current single-value `tier` with a three-field range that declares both the preferred tier and the tier stretch this activity accepts.

```yaml
tier_range:
  primary: T1                     # preferred tier
  span: [T0, T1, T2]              # tiers this activity accepts
  elasticity: neighbor            # strict | neighbor | broad
```

| Elasticity | `span` values | When to pick |
|---|---|---|
| `strict` | exactly `[primary]` | Activity uses tier-specific vocabulary or mechanics that break outside (rare — maybe 5% of catalog) |
| `neighbor` | `primary` ± 1 tier | Default — most 5-beat activities stretch one tier via the tier dials in Template 0 §06 |
| `broad` | all three tiers | Cognitive-drill activities (`entity_binding: agnostic`) typically work at every tier |

**Backward compatibility**: Existing activities with `tier: T1` are equivalent to `tier_range: {primary: T1, span: [T1], elasticity: strict}`. Migration can be lazy — the matcher treats a `tier` string as `tier_range: {primary: <value>, span: [<value>], elasticity: strict}` if the new shape isn't present.

**Authoring cost**: low — most activities get `elasticity: neighbor` and the matcher infers `span` from that plus `primary`. Only authors who want `broad` or `strict` need to think about it explicitly.

---

## 4 · Changes to `template_0_preview.html` (+ `_cn.html`)

### 4.1 §04 — tag block additions

Three new fields inserted into the YAML example, in roughly this order (near the other progression/match-facing fields):

```yaml
# ... existing fields ...

entity:        ladybug
entity_class:  [ladybug, beetle, insect, small_creature, living_thing, observable_thing]
entity_binding: parameterized

tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: neighbor

# ... rest of existing tag block ...
```

Legend block below the YAML gets a new sub-section:

**"Matchability — three tags that keep a small catalog portable"**

Brief prose explaining:
- The split between static (catalog-time) and dynamic (instance-time) fields
- Why these three tags matter most given today's small catalog
- How `entity_binding` controls swap-ability
- How `entity_class` enables graceful rollup
- How `tier_range` accepts age stretch

Links to `docs/entity_ontology.md` from the `entity_class` explanation.

### 4.2 §04 — static vs dynamic annotation

The tag block today is implicitly both authoring-time declarations and runtime-populated values mixed together. With matchability tags the split becomes structural — authors declare matchability at catalog time, runtime populates instance values.

Add a two-column annotation near the tag YAML (or a small table below the legend):

| Catalog-time — author declares | Instance-time — runtime populates |
|---|---|
| `entity_class`, `entity_binding`, `tier_range`, `pillar`, `key_concepts`, `atl_skills`, `subject_tags`, `transdisciplinary_theme`, `category`, `progression.topic_axis` | `entity` (what was seen), `tier` (actual child tier used), `highlight_moment` (runtime one-liner), `caregiver_role` (observed), `progression.difficulty_level` (rung reached), `progression.next_step_hint` |

**Rule of thumb**: if the value would differ between two children playing the "same" activity, it's instance-time.

### 4.3 §05 — pipeline depiction update

Section gets renamed:
- **EN**: `§05 / Downstream` → `§05 / Data pipeline · upstream & downstream`
- **CN**: `§05 / 下游` → `§05 / 数据管线 · 上游 · 下游`

Flow diagram gets two new boxes on the upstream side:

```
[Moment]
   entity seen (camera) · tier (onboarding) · setting (time/place) · caregiver present
     ↓
[MATCHER]
   reads catalog tag blocks · ranks by entity_class rollup + tier_range fit
     ↓
[Selected + parameterized activity instance]  ← this is where the existing Tier A / B / P bridge cards sit
     ↓
[Instance tag block]  ← runtime populates dynamic fields
     ↓
[Child recap]  [Parent dashboard]  ← existing reference strip
```

The existing Tier A / B / P upstream-bridge cards (describing the conceptual layers feeding Template 0's skeleton) **stay where they are** but get repositioned: they describe *what* the matcher is choosing from, sitting beneath the matcher rather than at the top of the flow.

Reference strip gets a prefix row:

**"Upstream reads (catalog-time)"**
```
entity_class · entity_binding · tier_range · pillar · category · progression.topic_axis · key_concepts · atl_skills · subject_tags · transdisciplinary_theme
(Matcher logic: see docs/upstream_matcher.md — to be written separately)
```

Followed by the existing two-card strip:

**"Downstream reads (instance-time)"**
```
[card 1: Child recap — entity, role_title, pillar, highlight_moment, related_concepts, atl_skills]
[card 2: Parent dashboard — progression.*, key_concepts, atl_skills, subject_tags, tier, caregiver_role]
```

### 4.4 Revnote bullet

```html
<li><b>Matchability tags added</b> (§04) + <b>upstream pipeline made explicit</b> (§05) — three new static fields (<code>entity_binding</code>, <code>entity_class</code>, <code>tier_range</code>) let one activity match many moments. §05's flow diagram now shows the matcher as a distinct upstream stage reading catalog-time tags; downstream surfaces unchanged.</li>
```

CN revnote bullet:
```html
<li><b>新增 matchability 标签</b>（§04）+ <b>明确上游管线</b>（§05）——三个新增的静态字段（<code>entity_binding</code>、<code>entity_class</code>、<code>tier_range</code>）让一个活动能匹配更多场景。§05 流程图现在把 matcher 作为独立的上游阶段，读取目录时标签；下游面不变。</li>
```

### 4.5 Version bump

Template 0 header + footer version: `v0.2` → `v0.3`.

---

## 5 · New doc · `docs/entity_ontology.md`

Markdown (not HTML — no preview aesthetic needed; this is a reference / data file authors look up).

### 5.1 Purpose

The canonical class hierarchy for `entity_class`. Every entity that can appear in an activity's tag block must have a chain that resolves against this file.

### 5.2 Structure

```markdown
# Entity Ontology

## Top-level class
- observable_thing    # the root; never used alone except by `entity_binding: agnostic` activities

## Hierarchy

- observable_thing
  - natural_thing
    - living_thing
      - animal
        - insect
          - beetle
            - ladybug
            - weevil
          - bee
          - ant
          - caterpillar
          - butterfly
        - arachnid
          - spider
        - mollusk
          - snail
          - slug
        - bird
        - mammal
        - fish
      - plant
        - flower
          - sunflower
          - daisy
          - rose
        - tree
        - fruit
          - apple
          - banana
        - vegetable
        - leaf
      - fungus
        - mushroom
    - non_living_natural_thing
      - rock
      - water
        - puddle
        - stream
      - weather_phenomenon
        - cloud
        - rainbow
      - celestial
        - sun
        - moon
  - human_made_thing
    - vehicle
      - car
      - bicycle
      - truck
      - airplane
    - tool
      - scissors
      - paintbrush
    - toy
      - doll
      - ball
      - block
    - food
      - bread
      - fruit_prepared
    - container
      - cup
      - box
    - clothing
    - instrument    # musical

## Abstract / cross-cutting classes
These aren't strict hierarchy — they tag capability rather than taxonomy. An activity can require entity_class membership in any of:

- small_creature       # anything a child could hold gently (overlaps insect/mollusk/small bird)
- warning_colored_small_creature   # ladybug, bee, wasp, monarch caterpillar, poison-dart frog
- patterned_thing      # ladybug, zebra, giraffe, striped fabric, polka-dot cup
- moving_thing         # any animal, vehicle, leaves in wind
- handheld_thing       # pencil, apple, cup, toy
```

### 5.3 Usage rules

- Each leaf entity (ladybug, apple, car) has ONE taxonomic chain plus zero or more abstract-class memberships
- When an activity's `entity_class` lists both taxonomic and abstract classes, the matcher treats them all as valid match points
- Abstract classes enable the most interesting recall: a `warning_colored_small_creature` activity fires for ANY member of that set

### 5.4 Versioning

File starts at v0.1. New entities get appended; ontology never shrinks in a way that breaks existing tag blocks. Breaking changes (renaming a class, removing one) would require a repo-wide migration and get a v1.0 bump.

### 5.5 Authorial convention

When an author creates a new activity for an entity NOT in the ontology, they add it to the ontology first (same PR). This keeps the class hierarchy comprehensive without a separate maintenance cycle.

---

## 6 · Changes to downstream docs

### 6.1 `child_recap_preview.html` §04 (Tag-block contract)

Add a row to the "Explicitly not read on child recap" note:

> `entity_binding`, `entity_class`, `tier_range` — these are matcher-only tags; child recap reads the resolved instance values (`entity`, `tier`), not the declaration shape.

CN mirror.

### 6.2 `parent_growth_path_preview.html` §07 (Tag-block contract full)

Add a row to the "Explicitly not read" note:

> `entity_binding`, `entity_class`, `tier_range` — matcher-only; parent dashboard reads resolved instance values.

CN mirror.

### 6.3 No visual / layout changes to the downstream docs

The downstream surfaces render instance-time values. Matchability is an upstream concern. The only change to these docs is the contract-table annotation to prevent future-reader confusion ("why is `entity_binding` in the tag block but not in my dashboard contract?").

---

## 7 · Cross-references & navigation

- Template 0 §04 ↔ `docs/entity_ontology.md` (new bidirectional link — §04 references the ontology; ontology's intro links back to Template 0 §04)
- Template 0 §05 ↔ `docs/upstream_matcher.md` (forward reference only — matcher doc not yet written)
- Template 0 §05 ↔ child recap §04 + parent dashboard §07 (existing — unchanged)
- Child recap / parent dashboard ↔ Template 0 (existing breadcrumb — unchanged)

---

## 8 · Aesthetic & tooling constraints

Same as the surfaces-split PR:

- Same `:root` tokens; no new CSS variables needed (the new §05 boxes can reuse existing card/flow styles)
- Fraunces + IBM Plex font stack
- EN/CN parity strict; YAML field names stay English in both locales
- No new JS
- No emojis
- `<html lang="zh-Hans">` on CN
- `:focus-visible` on any new interactive element
- Semantic HTML (`<code>` for YAML tokens, `<th scope="col">` for table headers)

### 8.1 Specific to §05 flow diagram

The existing §05 flow diagram uses `.flow-box` and related classes (grep to locate). The two new upstream boxes (Moment, Matcher) should use the same classes — no new visual vocabulary. If the current diagram needs to grow vertically to accommodate two more stages, adjust the container height but not the box style.

---

## 9 · Verification checklist

Once implemented, all of the following must hold:

### 9.1 Template 0

- [ ] §04 YAML shows the three new fields with realistic example values (ladybug-themed, matching running example)
- [ ] §04 legend explains each new field in 1–2 sentences
- [ ] §04 has a static-vs-dynamic annotation (table, list, or two-column callout)
- [ ] §05 title includes "upstream & downstream" (EN and CN)
- [ ] §05 flow diagram has Moment and Matcher boxes on the upstream side
- [ ] §05 reference strip has an "Upstream reads" prefix row listing the catalog-time field names
- [ ] Existing Tier A / B / P bridge cards are retained and positioned beneath the matcher
- [ ] Version header shows v0.3 (EN) / v0.3 (CN)
- [ ] Footer revnote has the new bullet in both locales

### 9.2 `docs/entity_ontology.md`

- [ ] File exists
- [ ] `ladybug` chain resolves: `ladybug → beetle → insect → animal → living_thing → natural_thing → observable_thing`
- [ ] At least one abstract class is defined (`warning_colored_small_creature` or equivalent)
- [ ] Intro section explains usage rules for activity authors
- [ ] Cross-link back to Template 0 §04

### 9.3 Downstream docs

- [ ] Child recap §04 "not read" list mentions the three matcher-only tags
- [ ] Parent dashboard §07 "not read" list mentions the three matcher-only tags
- [ ] CN mirrors both

### 9.4 Cross-file consistency

- [ ] EN/CN section-ID drift: zero (run the same check from Task 13 of the surfaces-split PR)
- [ ] No broken links
- [ ] Console clean on all 6 HTML files
- [ ] Desktop + mobile viewports both render cleanly (test at 1280×1000 and 375×812)

### 9.5 Semantic correctness

- [ ] A sample activity's tag block contains the new fields, entity_class chain resolves against the ontology, tier_range is internally consistent (`primary` ∈ `span`)
- [ ] The downstream surfaces still render the running-example ladybug activity correctly (no regression)

---

## 10 · Implementation plan handoff notes

This design spec, once approved, is ready to be converted into a task-by-task implementation plan under `docs/plans/YYYY-MM-DD-matchability-tags-implementation.md` using the `superpowers:writing-plans` skill.

Expected task shape (the plan writer will decide the exact split):

1. Worktree setup (`.worktrees/feat/matchability-tags/`)
2. Draft `docs/entity_ontology.md` (new file — no dependencies)
3. Template 0 §04 additions — EN (YAML, legend, static-vs-dynamic annotation)
4. Template 0 §04 — CN mirror
5. Template 0 §05 — rename + flow diagram upstream boxes — EN
6. Template 0 §05 — CN mirror
7. Template 0 §05 — reference strip upstream prefix — EN + CN
8. Template 0 version bump + revnote — EN + CN
9. Child recap §04 contract annotation — EN + CN
10. Parent dashboard §07 contract annotation — EN + CN
11. 6-file verification pass (same protocol as surfaces-split Task 13)
12. Push + PR

Estimated scope: **half the size of the surfaces-split PR**. Two new modules (§04 additions + §05 upstream boxes) on existing docs, one net-new markdown file, and minor annotations on the downstream docs. No brand-new preview doc, no net-new mockups.

Good candidate for subagent-driven development with the same per-task spec + code-quality review cadence.

---

## Revnote

- **v0.1** (2026-04-20) — Inaugural draft. Addresses the recall-first ask raised during post-surfaces-split review: "given a limited catalog, how can the upstream app map to as many activities as possible?" Answer: three stretch tags (`entity_binding`, `entity_class`, `tier_range`) + pipeline-depiction update making the matcher visible. Deferred tags captured in §2 out-of-scope for future rounds.
