# Template 0 — Post-v0.2 Roadmap

> Written for a fresh session with zero prior context.
> Covers the "Next actions" + "Post-approval" items originally listed in Template 0's v0.2 footer.

**Date:** 2026-04-20
**Last updated:** 2026-04-20 — items 2/3/4/6 landed; Item 7 shipped (PR #10); **Item 8 added** (progression walkthrough, shipped as PR #11)
**Template 0 authority:** `docs/template_0_preview.html` (v0.3, 2026-04-20)
**Ancillary specs:** `docs/plans/2026-04-17-downstream-surfaces-split-design.md` · `docs/plans/2026-04-20-matchability-tags-design.md` · `docs/plans/2026-04-20-progression-walkthrough-design.md`

---

## The 8 items and their state

| # | Item | State |
|---|---|---|
| 1 | Internal team sign-off on Template 0 shape | Process (not code) — owner-driven |
| 2 | Draft `docs/progression_axes.md` | ✅ **shipped** (PR #5) |
| 3 | Refactor `templates.md` (Template A/B → pillar overlays on Template 0) | ✅ **shipped** (PR #7, v1.0) |
| 4 | Promote tag block in `program.md` | ✅ **shipped** (PR #6) |
| 5 | L × T interactive walkthrough for author onboarding | ✅ already shipped (`docs/template_0_lt_walkthrough.html` + `_cn.html`) |
| 6 | Author training guide with worked examples | ✅ **shipped** (PR #8, v0.1) |
| 7 | Matchability tags — `entity_binding` + `entity_class` + `tier_range` + §05 pipeline update + `docs/entity_ontology.md` | ✅ **shipped** (PR #10, Template 0 v0.3) |
| 8 | **[NEW]** Progression walkthrough — 4 scenarios visualizing §07 L1↔L2↔L3 transitions in action | ✅ **shipped** (PR #11, v0.1) |

**Status summary:** All 6 original roadmap items complete. Two post-initial additions (Items 7 + 8) shipped — both address gaps that became visible only AFTER the v0.2 foundation landed. Item 7 addresses recall-first upstream matching; Item 8 makes the temporal dynamics of §07's transition rules vivid rather than just prose-described.

Item 1 (internal sign-off) remains a process step — owner-driven, not code.

---

## Table of contents

1. [Context — what Template 0 is](#1-context)
2. [Item 1 — Internal team sign-off](#2-item-1--sign-off)
3. [Item 2 — Draft `docs/progression_axes.md`](#3-item-2--progression-axes)
4. [Item 3 — Refactor `templates.md` to overlays](#4-item-3--templates-overlays)
5. [Item 4 — Promote tag block in `program.md`](#5-item-4--tag-block-promotion)
6. [Item 6 — Author training guide](#6-item-6--author-training)
7. [Execution conventions](#7-conventions)

---

<a id="1-context"></a>
## 1. Context — what Template 0 is

**Template 0** is the category-agnostic activity skeleton for WonderLens. It was built to replace the former Template A (Cat 1) + Template B (Cat 5) dual-template structure with **one skeleton + pillar overlays**, on the thesis that activity structure is mostly shared across categories/pillars and the differences are better captured as lightweight overlays.

**Key artifacts you will reference across all items below:**

| File | What it holds |
|---|---|
| `docs/template_0_preview.html` (+ `_cn.html`) | The v0.2 design spec for Template 0. This is what the team signs off on. Sections: §01 Concerns, §02 Spine (5 beats), §03 Skeleton, §04 Tag block, §05 Downstream pipeline (reference strip), §06 Tier comparison, §07 Axes, §08 Pillar overlays, §09 Decisions. |
| `docs/child_recap_preview.html` (+ `_cn.html`) | Downstream surface 1 (child-facing) — reads from the tag block |
| `docs/parent_growth_path_preview.html` (+ `_cn.html`) | Downstream surface 2 (parent-facing) — reads from the tag block |
| `docs/template_0_lt_walkthrough.html` (+ `_cn.html`) | L × T author onboarding animation (item 5, already shipped) |
| `templates.md` | The CURRENT legacy template spec (Template A + Template B as full standalones, with pillar overlays nested inside each). Item 3 refactors this. |
| `program.md` | The agent instruction file that tells the AI how to read templates.md and generate activities. Item 4 promotes the tag block inside it. |
| `entity_guidance.md` | Tier-specific guidance — not touched by any item below but relevant to item 6 (training examples) |

**Repo conventions** (see `~/.claude/projects/.../memory/MEMORY.md`):
- Always create a worktree under `.worktrees/{feat,fix,refactor,docs,...}/<topic>/` — never work on main directly.
- Plan files under `docs/plans/` with prefix `YYYY-MM-DD-<topic>.md`.
- After each feature, run code-reviewer + code-simplifier agents.
- Use `/brainstorm` → `/writing-plans` → `/subagent-driven-development` for non-trivial changes.

---

<a id="2-item-1--sign-off"></a>
## 2. Item 1 — Internal team sign-off on Template 0 shape

**Type:** process, not code.
**Owner:** product + design leads.
**Depends on:** nothing. Can happen in parallel with items 2–6.

### What it means

Team walks the Template 0 v0.2 preview doc (`docs/template_0_preview.html`), plus the two downstream surface docs, plus the L × T walkthrough, and confirms:

- The **tag block** is the right contract between upstream (activity) and downstream (child recap + parent dashboard)
- **5-beat spine** is the right activity structure
- **Pillar overlay** concept (vs full Template A/B) is the direction we're committing to
- **L × T orthogonality** (cognitive depth independent of age tier) is correctly represented

### Concrete deliverable

One of:
- A written sign-off in an issue / comment / PR ("Template 0 v0.2 shape approved — proceed with templates.md refactor and progression_axes.md draft")
- An explicit list of blockers that must change before sign-off

### How to drive it

```bash
# Serve all 6 preview docs locally so reviewers can click through
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
python3 -m http.server 8765 -d docs

# Review URLs
# http://localhost:8765/template_0_preview.html
# http://localhost:8765/child_recap_preview.html
# http://localhost:8765/parent_growth_path_preview.html
# http://localhost:8765/template_0_lt_walkthrough.html
```

Share the URLs asynchronously, collect comments in a single thread, capture the decision in a `docs/decisions/` ADR-style file if that convention exists (grep for `docs/decisions`); otherwise add a line to Template 0's revnote when approval lands.

### Acceptance

- Written approval recorded somewhere durable (PR comment, issue, ADR)
- A new revnote bullet on Template 0 updating v0.2 → v0.3 or v1.0 with the sign-off date

### Unblocks

Items 3 and 4 (refactor templates.md + promote tag block) — both are semi-structural changes that should wait for sign-off before burning implementation cycles.

Items 2 and 6 can proceed in parallel without sign-off (axes are descriptive; training guide is instructional).

---

<a id="3-item-2--progression-axes"></a>
## 3. Item 2 — Draft `docs/progression_axes.md`

**Type:** content / spec doc.
**File:** `docs/progression_axes.md` (to be created).
**Depends on:** nothing (Template 0 §07 already describes the axes at a high level; this formalizes them).
**Scope estimate:** 1 worktree, 1 PR, ~400–600 lines of markdown.

### Context — what "progression axes" means

Template 0 §07 (read `docs/template_0_preview.html` #axes) introduces the concept that cognitive progression isn't a single 1-D ladder — it runs along multiple **topic axes**. Each activity sits on one or more axes, and the progression ladder (L1 → L2 → L3) advances along each axis independently.

The downstream docs already reference axes like:

- `Form` — attribute description (colors, parts, shapes)
- `Function` — what it does, what it's for
- `Causation` — why / how it works
- `Change` — how it changes over time
- `Connection` — how it relates to other things
- `Perspective` — seeing it through different lenses
- `Responsibility` — relational / ethical stance

These seven map to the IB PYP Key Concepts. `docs/plans/2026-04-17-downstream-surfaces-split-design.md` and the parent dashboard §03 curiosity-radial already bake these seven axes in.

But there's no single authoritative doc defining:
- What each axis means (definition, scope)
- What L1 / L2 / L3 looks like **per axis** (concrete progression signals)
- Which entities / categories tend to anchor on which axes
- How to **detect** which axis an activity is working on (so the tag block's `progression.topic_axis` field can be filled programmatically or by the agent)

### What `docs/progression_axes.md` needs to contain

```markdown
# Progression Axes

## Introduction
- What a "topic axis" is
- Why axes instead of a single ladder
- Relationship to IB PYP Key Concepts
- Relationship to the `progression.topic_axis` tag-block field

## The 7 axes — one section per axis
For EACH of Form / Function / Causation / Change / Connection / Perspective / Responsibility:

### <Axis name>
- One-sentence definition
- IB Key Concept this maps to
- L1 / L2 / L3 progression signals (what the child says/does at each rung)
- Detection cues (phrases, verbs, question patterns the AI listens for)
- Entity affinity (which kinds of entities naturally anchor on this axis)
- Example dialogue snippets across T0/T1/T2 (reuse the L×T walkthrough's ladybug or pick a fresh entity)

## Axis interaction
- Activities that genuinely straddle two axes (primary + secondary)
- How to record multi-axis activities in the tag block
- Anti-patterns: when an activity claims an axis it's not really working on

## Tag block contract
- Exact field names (`progression.topic_axis`, `progression.difficulty_level`, `progression.next_step_hint`)
- Valid values (enum of the 7 axis names; the L1/L2/L3 enum)
- How the tag-block consumer (child recap + parent dashboard curiosity radial) reads this

## Versioning
- v0.1 Inaugural draft · 2026-04-20
- Revnote block
```

### Execution recipe for a fresh session

```bash
# 1. Worktree
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git fetch origin
git worktree add -b feat/progression-axes .worktrees/feat/progression-axes origin/main
cd .worktrees/feat/progression-axes

# 2. Read the existing references
# - docs/template_0_preview.html §07 (grep for id="axes")
# - docs/parent_growth_path_preview.html §03 (curiosity radial — the 7 axes are already listed here with personality-word descriptions)
# - docs/plans/2026-04-17-downstream-surfaces-split-design.md
# - entity_guidance.md (for tier-specific language)

# 3. Draft the markdown
# Use the /brainstorm skill if the scope feels unclear; otherwise draft directly.

# 4. Commit + PR
git add docs/progression_axes.md
git commit -m "docs: add progression axes spec — 7 topic axes × 3 rungs with detection cues"
git push -u origin feat/progression-axes
gh pr create --base main --title "Draft docs/progression_axes.md" --body "..."
```

### Acceptance

- All 7 axes have sections with definition + L1/L2/L3 signals + detection cues + example dialogue
- The tag-block contract section matches what's already in `docs/parent_growth_path_preview.html` §07 and `docs/child_recap_preview.html` §04
- No drift between this doc and what's in the preview docs — if anything differs, THIS doc becomes the source of truth and the preview docs get a patch
- v0.1 revnote + version block at the end, matching the style used by child recap and parent dashboard

### Why this item is important

Without a single source of truth for the axes:
- `program.md` can't tell the agent how to correctly fill `progression.topic_axis`
- Author training (item 6) has nothing concrete to teach against
- The parent dashboard curiosity radial's axis labels are visually authoritative but semantically under-specified

---

<a id="4-item-3--templates-overlays"></a>
## 4. Item 3 — Refactor `templates.md` (Template A/B → pillar overlays on Template 0)

**Type:** structural refactor of a canonical spec file.
**Files:** `templates.md` (rewrite), potentially new `docs/pillar_overlays/*.md` files.
**Depends on:** item 1 (sign-off) strongly recommended before starting.
**Scope estimate:** this is the **biggest** of the four items. Plan on a brainstorm → spec → plan → execute cycle. 2–4 PRs.

### Context — what templates.md currently is

```
templates.md (376 lines, repo root)
├── Introduction: "2 base templates (Cat1 + Cat5) × 6 Experience Pillar overlays = 12 game styles"
├── Template A: Category 1 — Sustained Verbal Interaction
│   ├── Structural Constants (table)
│   ├── Step sequence (5 steps with slots)
│   ├── Universal creative variables
│   └── 6 pillar overlays nested inside (Mystery, Creation, Performance, Discovery, Adventure, Nurture)
└── Template B: Category 5 — Out-of-Device Collection
    └── Same shape as Template A, nested pillar overlays
```

The legacy model is: **Template = base + pillar overlay**. `program.md` tells the agent: "read Template A or Template B + its pillar overlay, then fill slots." Template 0 makes this model obsolete — the agent should read Template 0's skeleton + a pillar overlay, full stop.

### Target structure after refactor

Option A (recommended — flat):

```
templates.md (slim — becomes a pointer doc)
├── Introduction: "Template 0 is the skeleton. Pillar overlays specialize it."
├── Links to:
│   └── docs/pillar_overlays/
│       ├── mystery.md
│       ├── creation.md
│       ├── performance.md
│       ├── discovery.md
│       ├── adventure.md
│       └── nurture.md
└── Category handling (Cat 1 vs Cat 5 vs future) as a small appendix — structural differences (device relation, step count) tied to the entity/category pair
```

Option B (compact — single file):

```
templates.md
├── Introduction: "Template 0 + 6 pillar overlays"
├── Template 0 reference (short — points to template_0_preview.html)
├── 6 pillar overlay sections, each with:
│   ├── Game mechanic summary
│   ├── Payoff pattern
│   ├── Pillar-specific creative variables
│   └── Spec overrides for Steps 2–4 of Template 0's 5-beat spine
└── Category modifier appendix (device relation, round count)
```

Recommend Option A if the 6 overlays are substantial (>200 lines each); Option B if they're compact (<80 lines each). Decide during brainstorming.

### Execution recipe

```bash
# 1. Worktree + brainstorm skill
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git fetch origin
git worktree add -b refactor/templates-overlays .worktrees/refactor/templates-overlays origin/main
cd .worktrees/refactor/templates-overlays

# 2. Brainstorm — this is a structural decision, not a mechanical refactor.
#    Use the superpowers:brainstorming skill.
#    Key questions to resolve during brainstorm:
#    - Option A (split) or Option B (single file)?
#    - Does Template 0 + one overlay fully subsume Template A/B, or do we still need
#      category modifiers (Cat 1 in-device vs Cat 5 out-of-device)?
#    - What happens to the "creative variables" section — hoist to Template 0,
#      keep per-overlay, or both?
#    - Versioning: v1.0 (breaking change — program.md must update to match) or
#      v2.0?

# 3. Write spec + implementation plan
#    - docs/plans/YYYY-MM-DD-templates-overlays-design.md
#    - docs/plans/YYYY-MM-DD-templates-overlays-implementation.md

# 4. Execute with subagent-driven-development
#    Each task small, reviewed inline, EN-only (templates.md has no CN mirror).

# 5. IMPORTANT — program.md references templates.md heavily (grep `templates.md`
#    in program.md to see instances). After the refactor, program.md needs a
#    coordinated update. Include that as the LAST task in the plan — avoid
#    leaving program.md pointing at dead file paths or removed sections.
```

### Acceptance

- `templates.md` no longer presents Template A / Template B as top-level templates
- Template 0 is the sole skeleton; pillar overlays are the specialization
- All 6 pillars have complete overlay specs (mechanic, payoff, creative variables, step overrides)
- `program.md` updated to match the new structure (no dead references)
- `entity_guidance.md` unchanged (tier guidance is orthogonal)
- A sample activity generation (agent running against the new templates) produces output structurally equivalent to the legacy Template A + pillar result — this is the integration test

### Why this is the biggest item

- Breaking change to the agent's reading model
- `program.md` has to be touched in lockstep
- The 6 pillar overlays may need actual content rewrites (they were nested inside Template A, now they're first-class)
- This unblocks item 6 (training guide) — author examples need a stable templates.md to teach against

---

<a id="5-item-4--tag-block-promotion"></a>
## 5. Item 4 — Promote tag block in `program.md`

**Type:** content rewrite of the agent instruction file.
**File:** `program.md` (repo root).
**Depends on:** items 2 + 3 ideally landed first (so the tag-block contract is concrete). Can be started in draft form earlier.
**Scope estimate:** 1 worktree, 1 PR, a moderate rewrite to one section of program.md plus cross-references.

### Context — what the tag block is

The tag block is the structured YAML-ish object that every activity design emits. It's what the downstream surfaces (child recap + parent dashboard) consume. Template 0 §04 is the authoritative spec. Example shape:

```yaml
entity: ladybug
category: sustained_verbal_interaction
tier: T1
pillar: mystery
role_title: "Young naturalist"
highlight_moment: "Mia noticed the ladybug's spots hide it from birds."
key_concepts: [form, causation]
atl_skills: [observation, hypothesis]
subject_tags: [biology, animal_defense]
transdisciplinary_theme: "Sharing the planet"
progression:
  topic_axis: causation
  difficulty_level: L2
  next_step_hint: "Try asking about what else uses warning colors."
caregiver_role: [co-explorer, observer]
related_concepts: [camouflage, predator]
pillar_payoff: "Mystery solved."
```

### Where `program.md` stands today

`program.md` §§ 1–2 (Context + Age Tiers) are solid. But the tag block currently appears late in the file, described as "output artifact" rather than as the central contract. The file emphasizes the step-by-step activity generation loop and treats tags as output-time cleanup.

Template 0's thesis is the opposite: **the tag block is the contract**. Everything upstream (the activity design) exists to populate it. Everything downstream reads from it.

### What "promoting" means concretely

1. **Move the tag block earlier in `program.md`** — right after Phase 1 context, before the generation loop. So the agent sees it before anything else.
2. **Rewrite framing** — from "output format" to "central contract, filled during design, read by both child recap and parent dashboard."
3. **Field-by-field spec** — exact field names, valid values (cross-linked to `docs/progression_axes.md` for axis enum), required vs optional.
4. **Self-check prompt** — add a pre-output check: "Have all required tag-block fields been filled with non-placeholder values? If any are TODO/missing, the design is incomplete."
5. **Cross-reference** — link to Template 0 §04 as the authoritative spec, and to child recap / parent dashboard docs as the consumers.

### Execution recipe

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git worktree add -b refactor/program-tag-block .worktrees/refactor/program-tag-block origin/main
cd .worktrees/refactor/program-tag-block

# Read current program.md carefully — it's ~563 lines. Locate the tag-block
# mention (grep -n "tag" program.md) and design the reorganization.

# Draft a small implementation plan (5–8 steps):
# 1. Extract current tag-block content
# 2. Draft new "Tag block — the central contract" section
# 3. Insert after Phase 1 context
# 4. Remove/redirect legacy tag mentions elsewhere
# 5. Add self-check prompt to the generation loop
# 6. Verify by running the agent on a sample entity and checking all tag fields
#    are filled
# 7. Commit with a reviewer-friendly diff

git add program.md
git commit -m "refactor(program): promote tag block to central contract, front-loaded"
git push -u origin refactor/program-tag-block
gh pr create --base main --title "Promote tag block in program.md"
```

### Acceptance

- Tag block has its own top-level section in `program.md`, appearing before the generation loop
- Every field is enumerated with required/optional + valid values
- Cross-references to Template 0 §04, `docs/progression_axes.md`, and the two downstream docs
- Self-check prompt prevents emitting designs with TODO / empty tag fields
- Integration test: agent generates one activity end-to-end; the resulting tag block is parseable by both child recap's §04 contract and parent dashboard's §07 contract

---

<a id="6-item-6--author-training"></a>
## 6. Item 6 — Author training guide with worked examples

**Type:** documentation / teaching artifact.
**File:** `docs/author_training_guide.md` or `docs/author_training_guide.html` (choose during brainstorm).
**Depends on:** items 2 + 3 + 4 landed. This is the teaching layer on top of the stable spec.
**Scope estimate:** 1 worktree, 1 PR, 600–1200 lines depending on format.

### What it is

A walk-through for a human author (or a new AI agent being fine-tuned) showing **3 complete end-to-end activity designs** for concrete entity × category × pillar combinations. Each worked example runs through:

1. Input: `entity = X, category = Cat N, pillar = P`
2. Reading Template 0 + the pillar overlay (post-refactor templates.md)
3. Filling every slot with entity-specific content
4. Emitting the tag block (fully populated, no placeholders)
5. Pre-flight self-check against the 10-dimension rubric from `program.md`
6. Final design + tag block + a sample downstream rendering (what the child recap would show, what the parent dashboard would show)

### Recommended examples to cover

Pick three contrasting combinations that span:

- **Different tiers** — one T0, one T1, one T2
- **Different pillars** — pick three of {Mystery, Creation, Performance, Discovery, Adventure, Nurture}
- **Different axes** — at least one each from {Form, Causation, Perspective} (the most common anchors)
- **Different categories** — mix Cat 1 (in-device) + Cat 5 (out-of-device) if the refactor preserves them

Candidate examples:
- Ladybug × Cat 1 × Mystery × T1 (already used across Template 0 docs as the running example — good for continuity)
- Sunflower × Cat 5 × Discovery × T0 (already appears in parent-dashboard §04 as a quote context)
- Construction paper × Cat 1 × Creation × T2 (fresh example — shows the model generalizes)

### Format choice

Two reasonable formats:

- **Markdown**: easy to edit, grep-able, renders fine in GitHub. Use fenced code blocks for dialogue + YAML for tag blocks.
- **HTML preview doc**: matches the aesthetic of the Template 0 / child recap / parent dashboard preview docs. More work to build, but more viscerally useful for a human author (they can see what the activity "looks like" running).

Recommend markdown for v0.1 (ship faster, easier to iterate), then an HTML version later if the doc gets heavy traffic.

### Execution recipe

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git worktree add -b docs/author-training .worktrees/docs/author-training origin/main
cd .worktrees/docs/author-training

# Use the /brainstorm skill to pick the 3 examples and confirm format.
# Then /writing-plans to break the training guide into tasks (one task per
# worked example + opening framing + rubric reminder + closing notes).
# Then /subagent-driven-development to execute.

# Verify:
# - Each worked example is runnable end-to-end (paste the input into the agent,
#   generate, compare output to the training guide's output — should match
#   structurally)
# - Tag blocks are fully populated in each example
# - References to templates.md, program.md, progression_axes.md all point at
#   their current (post-refactor) shape
```

### Acceptance

- 3 worked examples present, spanning tiers / pillars / axes / categories
- Each example shows the full design artifact + tag block + a note on what downstream surfaces would render
- Cross-references to the stable spec docs (Template 0 preview, templates.md, program.md, progression_axes.md) are all live
- A new author reading only this guide can generate their 4th example correctly without needing to ask for help

---

<a id="item-7-matchability"></a>
## 6b. Item 7 — **[NEW 2026-04-20]** Matchability tags + upstream pipeline

> **Added to the roadmap after items 1–6 were defined.** Surfaced during post-surfaces-split review when the question shifted from "deep-link to the best-fit activity" to "map a small catalog onto as many moments as possible." Shipped as PR #10.

**Type:** docs-only change, 3 new tag fields + §05 pipeline depiction update.
**Files:** 6 HTML (Template 0, child recap, parent dashboard — EN + CN) + 1 net-new markdown (`docs/entity_ontology.md`).
**Depends on:** items 2–6 all landed (this sits on top of the v0.2 foundation).
**Status:** ✅ **shipped** as PR #10 · Template 0 bumped **v0.2 → v0.3**.

### What it ships

**Three new catalog-time fields in Template 0 §04:**
- `entity_binding` — `bound` / `parameterized` / `agnostic` — declares how tightly coupled the activity is to its nominal entity
- `entity_class` — ordered list (specific → general) that lets the matcher roll up when exact-entity matches miss
- `tier_range` — `primary` + `span` + `elasticity` — accepts tier stretch

**§05 pipeline update (renamed "Data pipeline · upstream & downstream"):**
- New Moment + Matcher boxes showing the upstream stage the matcher occupies
- "Upstream reads · catalog-time" prefix listing the 10 tags the matcher consumes
- Downstream reference strip unchanged (still links to child recap + parent dashboard)

**New supporting doc:**
- `docs/entity_ontology.md` — canonical class hierarchy: `observable_thing` root, natural vs human-made subtrees, 6 abstract/cross-cutting classes, 5 worked example chains

**Downstream doc annotations:**
- Child recap §04 contract + parent dashboard §07 contract now note that the 3 new tags are matcher-only (not read by the surfaces)

### Why it was added after the initial roadmap

The original 6 items closed out v0.2's PM-feedback loop (tag-block split by surface, caregiver cumulative roles, L1↔L2↔L3 transitions, etc.). Matchability became visible as a gap only AFTER v0.2 shipped and the question changed from "what does an activity describe" to "how does the catalog get mapped to moments." The recall-first framing (small catalog → maximize coverage per activity) doesn't fit cleanly into any of items 1–6.

### Design + implementation specs

- `docs/plans/2026-04-20-matchability-tags-design.md`
- `docs/plans/2026-04-20-matchability-tags-implementation.md`

Both ship with PR #10.

### Deferred to future rounds (out of scope)

- **Tier 2 matchability tags**: `skill_focus`, `activity_shape`, `fallback_match`, `pillar_compatible`, `setting_flex`, `time_of_day_flex`, `energy_flex`
- **Matcher logic doc** (`docs/upstream_matcher.md`) — referenced by §05 as a forward link; not yet written. Belongs in a separate spec cycle once runtime architecture settles.
- **Runtime telemetry** for match quality

---

<a id="7-conventions"></a>
## 7. Execution conventions (apply to every item)

Inherited from the user's global and repo-specific preferences — do not deviate unless told to.

### Worktree + branch

```bash
# All feature work in a worktree under .worktrees/<kind>/<topic>
# Naming: feat/<topic>, fix/<topic>, refactor/<topic>, docs/<topic>
git worktree add -b <kind>/<topic> .worktrees/<kind>/<topic> origin/main
```

**Never** start implementation on `main`.

### Planning

For any item larger than a 1-line change:

1. `/brainstorm` to confirm scope (creates `docs/superpowers/specs/...` or `docs/plans/...-design.md`)
2. `/writing-plans` to convert to a task-by-task implementation plan
3. `/subagent-driven-development` to execute with per-task spec + code reviews

Plan filenames: `docs/plans/YYYY-MM-DD-<topic>-<kind>.md` where `<kind>` is `design` or `implementation`.

### Per-task review cadence

- Spec-compliance review after each implementation
- Code-quality review after spec passes
- Fix-up loop for every reviewer-flagged Important item
- Never "batch" reviews — one task at a time

### Commit hygiene

- `feat(scope): ...` for new work
- `fix(scope): ...` for bug fixes
- `refactor(scope): ...` for structural changes without behavior change
- `docs(scope): ...` for doc-only changes
- Never `--no-verify`, never force-push
- Keep per-task commits (don't squash away the review loop story)

### EN/CN parity

If the file has a `_cn.html` mirror (preview docs), EN + CN must stay structurally identical. YAML field names stay English in both locales. Aria-labels are translated. `<html lang="zh-Hans">` on CN files.

### Accessibility baseline

- `:focus-visible` styles on every interactive element
- SVG data visualizations: `<title>` + `<desc>` + `aria-labelledby`
- Tables: `<thead>` / `<tbody>` / `<th scope="col">`
- Semantic elements over div-soup

### After each feature

Run code-reviewer + code-simplifier subagents on the diff before opening the PR.

---

<a id="item-8-progression-walkthrough"></a>
## 6c. Item 8 — **[NEW 2026-04-20]** Progression walkthrough

> **Added to the roadmap after items 1–7 were shipped.** Surfaced in the same post-v0.3 review session where Item 7 landed — once Template 0 §07's transition rules were firm and matchability tags locked the catalog-time story, the next gap was making §07's temporal dynamics vivid. Shipped as PR #11.

**Type:** new companion preview doc (HTML/CSS only), no code changes.
**Files:** 2 new HTML files (EN + CN) + small cross-link addition to Template 0 §07 in both locales.
**Depends on:** Template 0 v0.3 (§07 transition rules are the spec the walkthrough visualizes).
**Status:** ✅ **shipped** as PR #11 · walkthrough v0.1.

### What it ships

**One new preview doc in two locales:** `docs/template_0_progression_walkthrough.html` + `_cn.html`. Four scenarios, each a horizontal timeline of 3–6 activity cards showing how the runtime's promote / hold / demote / sibling-jump / soft-reframe triggers apply to a specific child journey:

- **Scenario 1 — Steady progression** (baseline). 5 activities on Form axis. Shows the unremarkable happy path: most activities hold, promotions happen at natural breakpoints.
- **Scenario 2 — Hit-a-wall recovery.** 6 activities. Causation demote → sibling-axis jump to Connection → Causation bounces back. Two dialogue-callout expansions show what the runtime recorded vs what Mia heard (the dignity rule in action).
- **Scenario 3 — Across-axis independence.** 5 activities + a 7-axis snapshot visual. Kills the "one global rung" intuition — Mia is at L3 on Form, L1 on Causation, L1 on Responsibility, uninitialized on Connection, all simultaneously.
- **Scenario 4 — Reluctance vs inability.** 3 activities + a dedicated comparison box distinguishing demote (cognitive-state mismatch) from soft-reframe (emotional breath).

Plus a **three-rules summary §05** restating §07's dignity rule / sibling jump / personalization hook with pointers to where each showed up in the scenarios.

**Cross-link** from Template 0 §07 to the walkthrough in both locales — a cream-tinted block sitting under the three-rules footer.

### Why it was added after the initial roadmap

Items 1–7 closed out Template 0's v0.2–v0.3 spec work. But the §07 transition rules describe WHEN promotions/demotions happen in abstract terms; readers kept missing the **dignity rule** (demote is never surfaced as failure), the **per-axis state** (it's not one global ladder), and the **sibling-axis jump** (stuck at floor → pivot, not force). Prose made them invisible; a visual walkthrough makes them vivid.

### Design + implementation specs

- `docs/plans/2026-04-20-progression-walkthrough-design.md` (~460 lines)
- `docs/plans/2026-04-20-progression-walkthrough-implementation.md` (~1290 lines, 11 tasks)

Both ship with PR #11.

### Deferred to future rounds (explicitly out of scope)

- **Scenario 5** — personalization hypothetical (split view: "v1 threshold rules" vs "per-child pace model" applied to the same history)
- **Scenario 6** — long-arc compressed timeline (12+ sessions in one view, ties to parent dashboard curiosity radial)
- **Live simulator** — deliberate: hand-authored scenarios avoid codifying transitional v1 thresholds as permanent
- **Parameter tweaking / interactive rung state** — future v0.2

---

## Suggested ordering (historical — for reference)

The original plan ordered items as:

1. **Item 1** (sign-off) — unblocks structural items 3 and 4
2. **Item 2** (progression_axes.md) — can run in parallel with 1, sharpens the spec items 3, 4, 6 build on
3. **Item 4** (program.md tag-block promotion) — medium lift, unblocks item 6
4. **Item 3** (templates.md refactor) — biggest, highest risk, should go after sign-off
5. **Item 6** (author training guide) — depends on 2, 3, 4 landing

**What actually happened**: items 2→4→3→6 shipped in PRs #5, #6, #7, #8 in that order. Items 7 (matchability) and 8 (progression walkthrough) were added in a post-v0.3 review session and shipped as PRs #10 and #11. Item 1 (sign-off) is still owner-driven.

---

## Summary table

| # | Item | Scope | Depends on | State | Delivered via |
|---|---|---|---|---|---|
| 1 | Internal sign-off | Process | — | Pending | owner-driven |
| 2 | `docs/progression_axes.md` | 1 worktree, ~500 lines | — | ✅ shipped | PR #5 |
| 3 | Refactor `templates.md` | 1 brainstorm + plan + 2–4 PRs | item 1 | ✅ shipped | PR #7 (v1.0) |
| 4 | Promote tag block in `program.md` | 1 worktree, 1 PR | items 2+3 (loose) | ✅ shipped | PR #6 |
| 5 | L × T walkthrough | — | — | ✅ shipped | pre-existing |
| 6 | Author training guide | 1 worktree, 1 PR | items 2+3+4 | ✅ shipped | PR #8 (v0.1) |
| 7 | Matchability tags + §05 pipeline + entity ontology | 1 worktree, 1 PR, 13 commits | items 2–6 | ✅ shipped | PR #10 (Template 0 v0.3) |
| 8 | **[NEW]** Progression walkthrough — 4 scenarios, dialogue callouts, 7-axis snapshot, distinction-box | 1 worktree, 1 PR, 16 commits | Template 0 v0.3 + §07 transition rules | ✅ shipped | PR #11 (walkthrough v0.1) |

Only Item 1 (process-level team sign-off) remains. All code/doc work from this roadmap + the two post-roadmap additions (Items 7 + 8) is merged.

---

## Change log for this roadmap doc

- **2026-04-20 initial** — items 1–6 defined based on Template 0 v0.2's "Next actions" + "Post-approval" footer
- **2026-04-20 revised (first pass)** — items 2/3/4/6 marked shipped; **Item 7 (matchability tags) added** as a post-initial addition. Prompted by the question "given a limited catalog, how can the upstream app map to as many activities as possible?" which revealed a gap not covered by items 1–6. Full design + implementation plan + PR shipped same day.
- **2026-04-20 revised (second pass)** — **Item 8 (progression walkthrough) added** as a second post-initial addition. Prompted by the observation that Template 0 §07's transition rules describe WHEN promotions/demotions happen but can't make the temporal dynamics vivid in prose — readers kept missing the dignity rule, per-axis state, and sibling-axis jump. Full design + implementation plan + PR shipped same day.

### Sections newly added in THIS revision (second pass)

For reviewers comparing against the first-pass version:

- **Header block** — "Last updated" line extended; mention of `progression-walkthrough-design.md` added to Ancillary specs
- **The 8 items and their state** (was "7 items") — new row 8; status summary reworded to reference both post-roadmap additions
- **§6c Item 8 — Progression walkthrough** — entirely new section inserted between §6b (Item 7 Matchability tags) and §7 Execution conventions
- **Suggested ordering** — "What actually happened" line extended to mention Item 8 as PR #11
- **Summary table** — new row 8
- **Change log** — this bullet + next subsection

### Sections newly added in the FIRST revision (pass 1)

For reviewers comparing against the very-original version:

- **Header block** — "Last updated" line + new mention of `matchability-tags-design.md`; "Template 0 authority" bumped to v0.3
- **The 7 items and their state** (was "6 items") — new row 7 + all other rows marked shipped with PR refs
- **§6b Item 7 — Matchability tags** — entirely new section inserted between Item 6 and §7 Execution conventions
- **Suggested ordering** — reworded from imperative ("If you can only do one at a time") to retrospective ("What actually happened")
- **Summary table** — new "Delivered via" column; all states updated; new row 7
- **Change log** (this section) — entirely new
