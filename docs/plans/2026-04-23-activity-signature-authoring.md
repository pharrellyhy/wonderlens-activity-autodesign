# Activity Signature — Authoring Plan (wonderlens-activity-autodesign)

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the authoring-side artifacts for the `activity_signature` extension — closed-vocabulary reference doc, Template 0 §04 HTML update, 5-game migration to the per-game directory layout, and the shared JSON scenario fixture that both consumer repos will consume.

**Architecture:** Self-contained content work in `wonderlens-activity-autodesign`. No backend code; this plan produces the design artifacts that the backend + demo implementation plans consume.

**Companion plans:**
- **Backend:** `wonderlens-ai/docs/plans/2026-04-23-activity-signature-backend.md` — consumes the vocabulary + game dirs + scenario fixture from this plan
- **Demo port:** `wonderlens-activity-fullstack-demo/docs/plans/2026-04-23-activity-signature-demo.md` — same dependency
- **Integration overview:** `docs/plans/2026-04-23-activity-signature-integration.md` — cross-repo coordination + limitations + execution order

**Tech Stack:**
- Markdown + HTML (existing `template_0_preview.html` edit pattern)
- YAML (per-game tag blocks, scenario fixture)
- No code compilation; validate via manual preview render

---

## ◆ Recent updates (2026-04-24)

Spec additions landed after the plan was first written. Search this plan for `◆ 2026-04-24` to find every affected spot.

| Change | Affected tasks | What changes |
|---|---|---|
| **New `activity_signature.intro` field** — one-sentence observer-facing description, Layer 2 templated (see design spec §3.5) | Task 3 (all 5 game migrations) | Each `tag_block.yaml` gains an `intro:` field alongside `preview_label` / `preview_prompt`. Authored template with `{placeholders}`; rendered at session start. |
| **Two-layer activity_signature distinction clarified** — Layer 1 (identity, matcher-facing) vs Layer 2 (presentation, templated) | All game migrations (Task 3) | Ordering of fields in each `tag_block.yaml` follows Layer 1 → Layer 2 grouping for readability |
| **observation_angle ↔ topic_axis now explicitly orthogonal** (not sub-dimension) | `docs/activity_vocabulary.md` (Task 1) | Vocabulary doc's `observation_angle` heading rewritten — already applied |

---

## 0 · Context (read this first)

### 0.1 Design spec

**Required reading before starting:** `docs/plans/2026-04-23-activity-signature-design.md`

That doc is authoritative for:
- The required `activity_signature` block (§3)
- 3 closed vocabularies: `observation_angle` (10), `mechanic` (10), `entity_role` (4) (§3.2-3.4)
- Per-game directory layout (§4)
- Matcher scoring (§5.3)
- Payload extensions (§6)
- DB schema changes (§7)
- V1 scope: migrate 5 games, leave 19 on legacy layout via dual-loader (§8)

This plan implements the spec. If the spec is ambiguous, fix the spec first — don't improvise.

### 0.2 Repos and paths

| Repo | Root | Role |
|---|---|---|
| autodesign | `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign` | Source of truth — vocabulary, spec, games |
| wonderlens-ai | `/Users/pharrelly/codebase/gitlab/wonderlens-ai` | Production backend; Pydantic + DatabaseManager |
| fullstack-demo | `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo` | Prototype; dataclasses + aiosqlite |

### 0.3 Git worktree convention

Per `memory/feedback_worktree_convention.md`: branches under `.worktrees/feat/activity-signature/` in each of the three repos. Task 1 creates these.

### 0.4 Complementary systems (read-only context)

- **Progression runtime plans** (`2026-04-21-progression-runtime-*.md`) — already-written. The `ProgressionService.plan_next_activity` signature accepts an axis; this plan's work leaves that alone and stacks its own scoring bonus onto the existing selector.
- **Matchability tags** (`2026-04-20-matchability-tags-*.md`) — already shipped. `entity_binding`/`entity_class`/`tier_range` are already in game tag blocks; this plan's `activity_signature` sits alongside them in the same tag_block.yaml.

---

## 1 · File structure (this repo only)

```
docs/
├── activity_vocabulary.md          # closed enums canonical source (Task 1)
├── template_0_preview.html         # MODIFIED — §04 gains activity_signature block (Task 2)
├── template_0_preview_cn.html      # MODIFIED — CN mirror (Task 2)
└── plans/
    ├── 2026-04-23-activity-signature-design.md        # already written
    ├── 2026-04-23-activity-signature-integration.md   # cross-repo overview
    ├── 2026-04-23-activity-signature-authoring.md     # THIS FILE
    └── fixtures/
        └── activity_signature_scenarios.json          # shared test vector (Task 4)

activities/                         # ◆ NEW directory layout (Task 3)
├── color_scout_property/
│   ├── spec.md
│   ├── prod.md
│   ├── tag_block.yaml
│   ├── recap.template.yaml
│   └── dashboard.template.yaml
├── shape_quest_property/           (same 5 files)
├── voice_stage_lion/               (same 5 files)
├── mystery_trail_butterfly/        (same 5 files)
└── polka_dot_patrol/               (same 5 files)
```

---

## 2 · Task plan (bite-sized)

4 tasks total:
- **Task 1** — Worktree + `activity_vocabulary.md`
- **Task 2** — Template 0 §04 HTML update (EN + CN)
- **Task 3** — Migrate 5 games to per-game directory layout
- **Task 4** — Shared scenario fixture + push + PR

---

### Task 1: Worktree setup + vocabulary doc

**Files:**
- Create: `.worktrees/feat/activity-signature/` in this repo
- Create: `docs/activity_vocabulary.md`

- [ ] **Step 1: Create the worktree**

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git fetch origin
git worktree add .worktrees/feat/activity-signature -b feat/activity-signature origin/main
```

All file paths in subsequent tasks are relative to `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature`.

- [ ] **Step 2: Write `docs/activity_vocabulary.md`**

Path: `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature/docs/activity_vocabulary.md`

```markdown
# Activity Vocabulary

> **Canonical source** for the three closed enums in Template 0 §04's `activity_signature` block. Any addition here MUST be reflected in both consumer repos' enum code; enum-drift tests compare against this doc.

**Version:** 1.2 · 2026-04-27

---

## observation_angle (10 values)

What attribute/dimension the activity centers on. **Orthogonal to `progression.topic_axis`** — all 7 IB Key Concepts can use all 10 angles (see design spec §3.2 for examples).

| Token | Definition | Example games | Example focal_attribute |
|---|---|---|---|
| `color` | Surface color | Color Scout, Color Friends Adventure | red, blue, yellow |
| `shape` | Outline/form geometry | Shape Quest, Circle Spotter Challenge | round, pointy, long |
| `size` | Absolute or relative scale | (none yet — V2 addition) | tiny, huge |
| `texture` | Surface feel | Texture Mix, Fluffy Expedition | fuzzy, smooth, rough |
| `material` | Substance composition | Material Lab, Nature vs Made | wood, metal, fabric |
| `pattern` | Repeating visual design | Pattern Trail, Polka Dot Patrol | spots, stripes, zigzag |
| `function` | What it does / how it works | Detail Detective, What-If Workshop | moves, carries, protects |
| `origin` | Where it came from | Time Shifter, Library Book's Journey | natural, man-made, local |
| `behavior` | How it moves/acts/interacts | Mood Changer, Dream Whisperer | friendly, hides, flies |
| `state` | Condition | Fix-It Station, Old vs New | worn, fresh, alive |

## mechanic (10 values)

What the child actually does during the activity.

| Token | Definition | Example games |
|---|---|---|
| `enumerate` | Name parts or list attributes | Detail Detective, Mix Lab |
| `compare` | Contrast two+ items | Material Detective, comparison-chart games |
| `collect` | Find N things matching a criterion | Color Scout, Shape Quest, most property bridges |
| `sort` | Categorize into groups | Nature vs Made |
| `deduce` | Infer an answer from clues or evidence | Mystery Lens, Mystery Trail |
| `voice` | Give the entity a voice | Voice Stage Lion, Playground Voices |
| `build` | Make/invent something | What-If Workshop, Inventor Workshop |
| `predict` | "What happens next?" | Apple What Happens Next, Prediction Lab |
| `narrate` | Tell a story | Library Book's Journey, storytelling_chain games |
| `care` | Notice a need and propose help | Care Station, Rescue Team |

## entity_role (4 values)

How the photographed entity participates in this activity.

| Token | Definition | Pivot from conversation? |
|---|---|---|
| `subject` | Activity is about this entity specifically | No pivot (continuity) |
| `exemplar` | Entity is one example of a broader category | Yes — surface via `role_pivot_note` |
| `catalyst` | Entity sparked the question; activity is elsewhere | Yes |
| `reference` | Entity is source material for creating something new | Yes |

---

## Versioning

- Adding a value: bump minor (1.0 → 1.1); requires matching change in both consumer repos' enum code
- Removing a value: major bump (1.0 → 2.0); requires migration of all affected games
- Renaming: treat as remove + add

## Consumer mirrors

- `wonderlens-ai/app/modules/activity/activity_signature/vocabulary.py`
- `wonderlens-activity-fullstack-demo/backend/activity_signature/vocabulary.py`

Drift test compares parsed tables above against enum members; failure = CI block.
```

- [ ] **Step 3: Commit vocabulary doc**

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature
git add docs/activity_vocabulary.md
git commit -m "docs: add activity_vocabulary.md (closed enums for activity_signature)"
```

---

### Task 2: Template 0 §04 HTML update (EN + CN)

**Files:**
- Modify: `docs/template_0_preview.html` (§04 tag block section)
- Modify: `docs/template_0_preview_cn.html`

- [ ] **Step 1: Locate §04 tag block YAML render in `template_0_preview.html`**

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature
grep -n "caregiver_role" docs/template_0_preview.html | head -3
```

Expected: finds the line where `caregiver_role` is rendered in the tag block YAML (around line 3436 from the roadmap notes).

- [ ] **Step 2: Add `activity_signature` block after `caregiver_role`**

Find the text (around the existing `caregiver_role:` line) and add a new block below it in the same YAML code block:

```html
  <span class="key">caregiver_role</span>:  <span class="str">[scaffold, co-explorer, observer]</span>   <span class="cmt"># cumulative list; tier-dependent default</span>

  <span class="hl"><span class="key">activity_signature</span>:                       <span class="cmt"># answers "should this activity follow this conversation?"</span>
    <span class="key">observation_angle</span>: <span class="str">{color|shape|size|texture|material|pattern|function|origin|behavior|state}</span>
    <span class="key">mechanic</span>:          <span class="str">{enumerate|compare|collect|sort|deduce|voice|build|predict|narrate|care}</span>
    <span class="key">entity_role</span>:       <span class="str">{subject|exemplar|catalyst|reference}</span>
    <span class="key">focal_attribute</span>:   <span class="str">"..."</span>                <span class="cmt"># the parameterized attribute</span>
    <span class="key">bridge_prerequisites</span>:
      <span class="key">primary</span>:   [<span class="str">...</span>]
      <span class="key">secondary</span>: [<span class="str">...</span>]
    <span class="key">preview_label</span>:    <span class="str">"..."</span>
    <span class="key">preview_prompt</span>:   <span class="str">"..."</span>
    <span class="key">role_pivot_note</span>:  <span class="str">"..."</span>              <span class="cmt"># optional; used when entity_role shifts</span></span>
```

Read the file first, then make the edit. Use Edit tool with exact surrounding context.

- [ ] **Step 3: Add `activity_signature` entries to the §04 "downstream reads" table**

Find the table showing which fields are read by `game_selector`, `child_recap`, `parent_dashboard`. Add rows:
- `activity_signature.observation_angle` — read by: selector (scoring), recap (copy), dashboard (radial split)
- `activity_signature.mechanic` — read by: recap (copy), dashboard (exploration matrix)
- `activity_signature.entity_role` — read by: script agent (pivot phrasing), recap (copy)
- `activity_signature.focal_attribute` — read by: script agent (prompts), recap (rendered copy)

Exact table location and format: read the file around the `reads-from` or lifecycle annotation markup and match style.

- [ ] **Step 4: Verify EN render**

Start a preview server:
```bash
python3 -m http.server 8765 -d docs &
curl -s http://localhost:8765/template_0_preview.html | grep -c "activity_signature"
```
Expected: 2+ (once in the YAML render, once in the downstream-reads table).

Stop the server: `kill %1`

- [ ] **Step 5: Mirror in CN**

Apply the same two changes to `docs/template_0_preview_cn.html`:
- YAML block — identical (YAML tokens stay English per house style)
- Downstream-reads table — Chinese phrasing, same field references

- [ ] **Step 6: Revnote update**

Find the revision note block (usually bottom of the §08 section or footer). Add a bullet under the current version; the Template 0 preview is now at v0.6 after the PM-review clarification pass:

```html
<li><b>activity_signature block added</b> (§04) — signature fields for each activity: observation_angle, mechanic, entity_role, focal_attribute, bridge_prerequisites, preview_label+prompt. See <code>docs/activity_vocabulary.md</code> for enum closure.</li>
```

Mirror in CN.

- [ ] **Step 7: Commit**

```bash
git add docs/template_0_preview.html docs/template_0_preview_cn.html
git commit -m "docs(template-0): add activity_signature block to §04 (EN+CN)"
```

---

### Task 3: Migrate 5 games to per-game dir layout

**Files:**
- Create: `activities/color_scout_property/{spec.md,prod.md,tag_block.yaml,recap.template.yaml,dashboard.template.yaml}`
- Create: `activities/shape_quest_property/{…same 5 files…}`
- Create: `activities/voice_stage_lion/{…same 5 files…}`
- Create: `activities/mystery_trail_butterfly/{…same 5 files…}`
- Create: `activities/polka_dot_patrol/{…same 5 files…}`

Reference the game-split recipe in the design spec §8.3.

- [ ] **Step 1: Create all 5 directories**

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature
mkdir -p activities/color_scout_property \
         activities/shape_quest_property \
         activities/voice_stage_lion \
         activities/mystery_trail_butterfly \
         activities/polka_dot_patrol
```

- [ ] **Step 2: Migrate color_scout_property**

Source: find the existing color_scout definition. Check both `designs/` (autodesign) and the mirror in wonderlens-ai:
```bash
find /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/designs \
     /Users/pharrelly/codebase/gitlab/wonderlens-ai/app/modules/activity/games \
     -name "*color*scout*" -o -name "*color_friends*" 2>/dev/null
```

Read the matched files. Then produce the 5 per-game files under `activities/color_scout_property/`:

**`activities/color_scout_property/spec.md`** — authoring-intent prose. Cover:
- Game premise (what the child does and why)
- Target IB axis + rung + age tier
- Pedagogical rationale (why collect-by-color teaches Form/color)
- When this game is selected (Tier P trigger on any color property)

Write from scratch if absent; otherwise extract from the existing `.md` file's non-YAML prose.

**`activities/color_scout_property/prod.md`** — runtime dialogue and step instructions. Extract from the frontmatter-less body of the source `.md`.

**`activities/color_scout_property/tag_block.yaml`** — structured metadata:

```yaml
# ─── §0 · IDENTITY ────────────────────────────────────
activity_id: color_scout_property
version: 1
source_entity_exemplar: ladybug        # exemplar entity for illustrating the template
template_type: cat5
pillar: Discovery                       # field_experiment → Discovery
game_style: field_experiment

# ─── §1 · IB FRAME ────────────────────────────────────
entity: "{parameterized_by_matched_property}"
entity_class: []                        # filled at runtime from matched entity's class chain
entity_binding: parameterized
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"

category: objects                       # filled at runtime
attributes: []                          # filled at runtime

key_concepts: [Form]
related_concepts: [variety, attention]
atl_skills: [observation, classification]
transdisciplinary_theme: How_We_Express_Ourselves

kud:
  know:       ["the focal color appears on many kinds of things"]
  understand: ["color is a property we can use to group things"]
  do:         ["find 3 things that share the focal color"]

progression:
  topic_axis: form
  difficulty_level: 2                   # L2: extend attributes into category
  next_step_hint: "Next time, notice another attribute alongside color"
  reward_hook: "Earned the Color Scout badge"

caregiver_role: [scaffold, co-explorer]

# ─── §2 · ACTIVITY SIGNATURE ───────────────────────────
activity_signature:
  # ── Layer 1: editorial identity (fixed; matcher reads these) ──
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  bridge_prerequisites:
    primary:   [color]
    secondary: [pattern, visibility]

  # ── Layer 2: presentation (author templates; runtime renders) ──
  focal_attribute: "{matched_color}"    # runtime-parameterized from matched property
  intro: "The child finds three {color} things using the photographed {entity} as a starting example."   # ◆ 2026-04-24 NEW
  preview_label:  "Find three {color} things!"
  preview_prompt: "You noticed the {color} of the {entity}. Let's go find more {color} things together."
  role_pivot_note: |
    The {entity} was our subject during the chat; now it becomes an
    EXAMPLE of {color} — we're going to find more {color} things.

# ─── §3 · MATCHABILITY (from 2026-04-20 spec) ─────────
matchability:
  entity_class_filter: []               # wide — runs against any color-bearing entity
  tier_support: {T0: yes, T1: yes, T2: yes}
```

**`activities/color_scout_property/recap.template.yaml`**:

```yaml
# Child recap payload shape for this game.
# At runtime, {placeholders} are filled with session-specific values.
recap_payload:
  entity: "{runtime_entity}"            # e.g. ladybug
  tier: "{runtime_tier}"                # T0 | T1 | T2
  age_years: "{runtime_age}"

  what_we_noticed: color
  what_we_did:     collected
  entity_role:     exemplar

  focal_attribute:
    token: "{runtime_color}"            # e.g. red
    child_label: "{runtime_color}"
    badge_emoji_none: true

  highlight_moment: "You found THREE {runtime_color} things!"

  finds:
    - {label: "{find_1}", photo: "{photo_1}"}
    - {label: "{find_2}", photo: "{photo_2}"}
    - {label: "{find_3}", photo: "{photo_3}"}

  difficulty_level: 2
  next_step_hint:  "Next time, let's notice shapes too"

  caregiver_observed: co-explorer
  reward_badge:       color_scout

rendered:
  title:  "You were a Color Scout today!"
  line_1: "We noticed a lot of {runtime_color}."
  line_2: "You collected 3 {runtime_color} things."
  line_3: "The {runtime_entity} helped us spot {runtime_color} in our whole world."
  badge:  "Color Scout"
  next:   "Next time, let's notice shapes too."
```

**`activities/color_scout_property/dashboard.template.yaml`**:

```yaml
# Parent dashboard FRAGMENT produced by this game.
# This is what gets merged into the device-scoped rollup at session end.
dashboard_fragment:
  session:
    axis: form
    angle: color
    mechanic: collect
    entity_role: exemplar
    focal_attribute: "{runtime_color}"
    entry_rung: "{runtime_entry_rung}"
    exit_rung:  "{runtime_exit_rung}"
    outcome:    "{runtime_outcome}"         # promote | hold | demote | soft_reframe

  contributes_to:
    curiosity_radial:
      axis: form
      angle: color                           # bumps form.by_angle.color.sessions
    exploration_matrix:
      cell: "collect × color"                # bumps this cell's count
    key_concepts_exposure:
      Form:
        angle: color
    atl_skills_trail:
      - observation
      - classification
```

- [ ] **Step 3: Migrate shape_quest_property**

Same recipe. Differences:
- `tag_block.yaml`: `observation_angle: shape`, `focal_attribute: "{matched_shape}"`, `bridge_prerequisites.primary: [shape]`, `bridge_prerequisites.secondary: [size, pattern]`, `preview_label: "Find three {shape} things!"`
- ◆ 2026-04-24 NEW — `activity_signature.intro: "The child finds three {shape} things using the photographed {entity} as a starting example."`
- `recap.template.yaml`: `what_we_noticed: shape`, copy rewrite
- `dashboard.template.yaml`: `axis: form, angle: shape, cell: "collect × shape"`
- `spec.md` + `prod.md`: source from existing shape_quest definition

- [ ] **Step 4: Migrate voice_stage_lion**

Cat1 gold standard. Differences:
- `template_type: cat1`, `pillar: Performance`, `game_style: voice_stage`
- `activity_signature.observation_angle: behavior`, `mechanic: voice`, `entity_role: subject` (no pivot — the lion IS the subject of the voice)
- `focal_attribute: "lion_voice"` (or similar; the voice-stage game voices the entity itself, not an attribute)
- `bridge_prerequisites.primary: [behavior, function]`
- ◆ 2026-04-24 NEW — `activity_signature.intro: "The child gives the {entity} a voice and personality to match its presence."`
- `preview_label: "Let's voice the lion!"`
- `role_pivot_note`: empty (subject → subject, no pivot needed)
- `kud.do`: "give the lion a voice and personality"
- `recap.template.yaml`: `what_we_noticed: behavior`, `what_we_did: voiced`

- [ ] **Step 5: Migrate mystery_trail_butterfly**

Cat5 gold standard, Connection axis. Differences:
- `template_type: cat5`, `pillar: Mystery`, `game_style: mystery_trail`
- `key_concepts: [Connection]`, `progression.topic_axis: connection`
- `activity_signature.observation_angle: pattern`, `mechanic: collect`, `entity_role: subject`
- `focal_attribute: "butterfly_wing_pattern"`
- `bridge_prerequisites.primary: [pattern]`, `secondary: [color, shape]`
- ◆ 2026-04-24 NEW — `activity_signature.intro: "The child hunts for three more things that share the {entity}'s wing pattern, connecting patterns across the world."`

- [ ] **Step 6: Migrate polka_dot_patrol**

Cat5 gold standard. Differences:
- `activity_signature.observation_angle: pattern`, `mechanic: collect`, `entity_role: exemplar`
- `focal_attribute: "polka_dots"` or `"spots"`
- `bridge_prerequisites.primary: [pattern]`, `secondary: [color]`
- ◆ 2026-04-24 NEW — `activity_signature.intro: "The child patrols the neighborhood looking for three more spotted things, using the {entity} as the first clue."`

- [ ] **Step 7: Remove legacy `.md` files for migrated games**

Since autodesign stores source games in `designs/` and the mirrors are in the consumer repos:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature
# List what exists
ls designs/ | grep -iE "color_friends|shape|lion|butterfly|polka"
# Remove the 5 games that are now in activities/
# (exact filenames depend on what ls found; run remove for each)
```

Check before deleting — the designs/ folder may contain different filenames. The canonical list is what you just migrated; whatever legacy file corresponds to each, delete.

- [ ] **Step 8: Commit the 5-game migration**

```bash
git add activities/ designs/    # or: git rm the old designs/, git add activities/
git commit -m "feat(activities): migrate 5 V1 games to per-game dir layout"
```

---

### Task 4: Shared scenario fixture

**Files:**
- Create: `docs/plans/fixtures/activity_signature_scenarios.json`

This fixture encodes 4 conversation-to-activity scenarios that BOTH wonderlens-ai and fullstack-demo implementations must handle identically (same pattern as the progression-runtime plan's `progression_scenarios.json`).

- [ ] **Step 1: Create the fixture**

```bash
mkdir -p /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/activity-signature/docs/plans/fixtures
```

Content of `activity_signature_scenarios.json`:

```json
{
  "scenarios": [
    {
      "name": "pen_color_matches_color_scout",
      "photo_entity": "red_pen",
      "detected_properties": ["red", "cylindrical", "smooth", "plastic"],
      "conversation_signature": {
        "dominant_angle": "color",
        "secondary_angles": ["shape"],
        "entity_role_implied": "subject"
      },
      "age_tier": 1,
      "candidate_games": ["color_scout_property", "shape_quest_property"],
      "expected_pick": "color_scout_property",
      "expected_role_pivot_fires": true,
      "rationale": "Conversation attended to color; Color Scout's angle=color matches primary → +1.5. Shape Quest's angle=shape matches secondary → +0.75. Color wins."
    },
    {
      "name": "ladybug_shape_matches_shape_quest",
      "photo_entity": "ladybug",
      "detected_properties": ["red", "round", "spotted"],
      "conversation_signature": {
        "dominant_angle": "shape",
        "secondary_angles": ["pattern"],
        "entity_role_implied": "subject"
      },
      "age_tier": 1,
      "candidate_games": ["color_scout_property", "shape_quest_property", "polka_dot_patrol"],
      "expected_pick": "shape_quest_property",
      "expected_role_pivot_fires": true,
      "rationale": "Conversation shifted to shape; Shape Quest primary matches, others don't on primary."
    },
    {
      "name": "lion_behavior_matches_voice_stage",
      "photo_entity": "lion",
      "detected_properties": ["mammal", "big", "golden"],
      "conversation_signature": {
        "dominant_angle": "behavior",
        "secondary_angles": ["function"],
        "entity_role_implied": "subject"
      },
      "age_tier": 1,
      "candidate_games": ["voice_stage_lion", "color_scout_property"],
      "expected_pick": "voice_stage_lion",
      "expected_role_pivot_fires": false,
      "rationale": "Voice Stage Lion is Tier A match; also angle=behavior matches primary. Tier A score (10) + signature bonus (1.5) dominates. entity_role=subject throughout, no pivot."
    },
    {
      "name": "no_conversation_signature_legacy_behavior",
      "photo_entity": "crayons",
      "detected_properties": ["multi-colored", "wax"],
      "conversation_signature": null,
      "age_tier": 0,
      "candidate_games": ["color_friends_adventure_crayons", "color_scout_property"],
      "expected_pick": "color_friends_adventure_crayons",
      "expected_role_pivot_fires": false,
      "rationale": "No conversation_signature → no bonus from this plan. Existing Tier A beats Tier P (10 vs 7). Backwards-compatible."
    }
  ]
}
```

- [ ] **Step 2: Commit**

```bash
git add docs/plans/fixtures/activity_signature_scenarios.json
git commit -m "test(activity-signature): shared scenario fixture for cross-repo parity"
```

- [ ] **Step 3: Push + open PR**

```bash
git push -u origin feat/activity-signature
gh pr create --title "feat(activity-signature): vocabulary + Template 0 §04 + 5 game migrations" \
             --body "$(cat <<'EOF'
## Summary

Authoring-side work for the activity_signature extension (design spec already merged).

- \`docs/activity_vocabulary.md\` — closed enums (10 angles / 10 mechanics / 4 roles)
- Template 0 §04 preview (EN + CN) — new \`activity_signature\` block
- 5 games migrated to per-game dir layout under \`activities/\`
- \`docs/plans/fixtures/activity_signature_scenarios.json\` — shared test vector

Backend + demo implementation ships separately via:
- \`wonderlens-ai/docs/plans/2026-04-23-activity-signature-backend.md\`
- \`wonderlens-activity-fullstack-demo/docs/plans/2026-04-23-activity-signature-demo.md\`

See \`docs/plans/2026-04-23-activity-signature-integration.md\` for cross-repo coordination.

## Test plan

- [ ] Template 0 preview renders cleanly in browser (EN + CN)
- [ ] All 5 game dirs have 5 required files each
- [ ] tag_block.yaml in each game validates against activity_vocabulary.md enum closure
- [ ] Scenario fixture parses as valid JSON
EOF
)"
```

Note the PR URL; the backend + demo PRs should cross-link to it.

---

## 3 · Known V1 limitations

Document in each PR/MR description:

1. **LLM-based dominant_angle is deferred.** V1 uses keyword-matching heuristic. Expect false negatives on synonyms not in the table (e.g., "crimson" → color).
2. **5 games migrated; 19 remain on legacy layout.** Loader supports both; follow-up PRs migrate the rest. Until then, unmigrated games have `activity_signature = None` and are scored without signature bonus.
3. **Angle-to-axis map is static.** `_ANGLE_TO_AXIS` hardcodes that all visual/physical angles map to Form. If an activity is genuinely at Causation angle=color ("why is it red?"), the dashboard rollup will misattribute. Acceptable for V1; revisit when a real case arises.
4. **`.latest.yaml` files committed to git.** Initial cautious default; switch to `.gitignore`d if authors find the noise unhelpful (1-line change).
5. **`bridge_prerequisites.secondary` can contain non-enum strings.** V1 stores them but doesn't score them; full matching is future work.

---

## 4 · Commit/PR discipline

Per `memory/feedback_review_simplify.md`:
- After each task → code-reviewer + code-simplifier, fix Important findings, commit follow-ups
- After each Phase → cross-branch code-reviewer before opening PR/MR

Per `memory/feedback_worktree_convention.md`: branch under `.worktrees/feat/activity-signature/` (Task 1 creates it).

Per `memory/feedback_plan_datetime.md`: this plan is `2026-04-23-activity-signature-authoring.md`.

---

## 5 · Verification summary

- [ ] `docs/activity_vocabulary.md` committed with 10 angles / 10 mechanics / 4 roles
- [ ] Template 0 §04 EN + CN render the new `activity_signature` block
- [ ] Template 0 revnote updated
- [ ] 5 game directories exist under `activities/` with all 5 required files each:
  - color_scout_property, shape_quest_property, voice_stage_lion, mystery_trail_butterfly, polka_dot_patrol
- [ ] Each `tag_block.yaml` validates (required fields present, enums legal per `activity_vocabulary.md`)
- [ ] ◆ 2026-04-24 — Each `tag_block.yaml` has an `activity_signature.intro` field (one sentence, third-person, observer-facing, with `{placeholders}` for parameterized entities)
- [ ] Legacy `.md` files removed for the 5 migrated games
- [ ] `docs/plans/fixtures/activity_signature_scenarios.json` committed with 4 scenarios
- [ ] PR opened with link to `docs/plans/2026-04-23-activity-signature-integration.md`

---

## Revnote

- **v0.3** (2026-04-27) — Aligned version numbering with the PM-review clarification pass: vocabulary v1.2, Template 0 v0.6, 10 mechanics, and WonderLens thinking/learning language for `atl_skills`.
- **v0.2** (2026-04-24) — Added `activity_signature.intro` field requirement for each migrated game's `tag_block.yaml`. Updated Task 3 steps 2–6 with the specific intro template to author per game. Updated verification checklist. See design spec §3.5 for field definition and constraints.
- **v0.1** (2026-04-23) — Inaugural authoring plan. 4 tasks: worktree + vocabulary doc, Template 0 §04 update (EN+CN), 5-game migration to per-game dir layout, shared scenario fixture + PR. Produces the design artifacts the backend + demo plans consume. V1 migrates 5 games; remaining 19 games deferred to follow-up PRs under the same schema.
