# Template 0 Implementation Plan

> **Pre-requisite**: Internal team has signed off on the Template 0 preview  
> (`docs/template_0_preview.html` / `docs/template_0_preview_cn.html`).  
> **Goal**: Turn the approved design into working infrastructure the agent can use.  
> **Estimated scope**: 5 files modified, 1 file created, ~2 hours.

---

## Context for the implementing session

Template 0 is a category-agnostic activity skeleton. Currently `templates.md` has two independent templates (Template A for Cat1, Template B for Cat5) that duplicate the same emotional arc, tag logic, and tier guidance. Template 0 lifts the shared structure into a single root that A and B extend.

Three new concepts are introduced:
1. **Tag block** — a required YAML header on every activity (entity, category, attributes, key_concepts, related_concepts, atl_skills, progression, caregiver_role)
2. **Progression axis** — 7 axes derived from the 7 IB Key Concepts (Form / Function / Causation / Change / Connection / Perspective / Responsibility), each with 3 rungs (L1 notice → L2 extend → L3 reason)
3. **Tier adaptation model** — 5 dials (AI role, language, task depth, concept focus, caregiver role) with defaults per tier (T0/T1/T2); activities flex to a neighbor tier, never across two

The full design is in the preview HTML. Reference sections below by their `§` numbers from that doc.

---

## Task 1 — Create `docs/progression_axes.md`

**New file.** This is the canonical reference for the 7 progression axes.

### Content to include

```yaml
# For each of the 7 axes:
axis_id:        form           # matches IB Key Concept name (lowercase)
key_concept:    Form           # the IB Key Concept it derives from
question:       "What is it like?"
levels:
  L1:
    label:      Notice
    description: "Observe, name, or identify one instance of the concept"
    example:    "The ladybug is red."
  L2:
    label:      Extend
    description: "Add more examples, more parts, more steps, or a related viewpoint"
    example:    "Red body, black spots, tiny black legs."
  L3:
    label:      Reason
    description: "Explain why, predict what-if, or state the connecting rule"
    example:    "Red warns birds not to eat it."
```

Include all 7 axes. Copy the level descriptions and examples from the preview HTML §07 ladders — they are already written and reviewed.

### Also include

- A short intro explaining what L1/L2/L3 mean universally (notice → extend → reason) and that they are orthogonal to T0/T1/T2
- The gold-standard coverage table from §07 (which existing designs map to which axes)
- A "how to pick an axis" decision aid: given entity + pillar, which axis is the natural default?

### Files to read first
- `docs/template_0_preview.html` §07 (the ladder content + level legend + coverage grid)
- `program.md` §1.4 (the 7 Key Concepts definitions)

---

## Task 2 — Add Template 0 to `templates.md`

**Modify existing file.** Insert a new `## Template 0` section at the top, above the existing Template A and Template B.

### What Template 0 contains

Copy the skeleton from preview HTML §03 (the collapsible code panel). It has 5 blocks:

1. **§0 Activity Header** — the full required tag block schema
2. **§1 Structural Spine** — the 5-beat emotional arc (transition bridge → frame & role → core loop → magic moment → celebration)
3. **§2 Universal Creative Variables** — metaphor, role_title, escalation_axis, reflective_question
4. **§3 Tier Adaptation Defaults** — the 5 dials × 3 tiers table
5. **§4 Overlay Hooks** — the 8 fields each category overlay must fill (beat_medium, round_count, camera_use, setting, step_count, core_mechanic, anchor_priority, checklist_extras)

### Refactor Template A and Template B

After inserting Template 0, rewrite Template A and Template B as overlays:

**Template A (Cat1) becomes:**
```markdown
## Template A: Category 1 — Sustained Verbal Interaction (In-Device)

> extends: Template 0

| Override field | Value |
|---|---|
| beat_medium | verbal_dialogue |
| round_count | 3–5 |
| camera_use | initial_only |
| setting | indoor_quiet |
| step_count | 5 |
| core_mechanic | scenario → verbal response → pillar validation |
| anchor_priority | engagement-first (emotions, imagination, narrative, reasoning) |
| checklist_extras | (Cat1-specific items from current checklist) |
```

Then keep only the Cat1-specific content that isn't in Template 0:
- The Cat1 pillar overlay details (pillar-specific missions, per-round interactions, synthesis)
- The Cat1 dimension anchoring rules (engagement-first priority)
- The Cat1 entity adaptation checklist (only the items NOT already in Template 0's universal checklist)

**Same pattern for Template B (Cat5).**

### What to delete from Template A/B

Remove from both:
- The duplicated "How Templates Work" prose (now lives in Template 0)
- The duplicated universal creative variables table (now in Template 0 §2)
- The duplicated dimension anchoring intro (now in Template 0)
- The duplicated entity adaptation checklist items that are universal

### Files to read first
- `templates.md` (full file — understand current structure before modifying)
- `docs/template_0_preview.html` §03 (the skeleton) and §08 (the overlay cards)

---

## Task 3 — Promote tag block in `program.md`

**Modify existing file.** The activity output header (around line 214) currently lists Basic Info fields as a flat bullet list. Restructure it to match the Template 0 tag block schema.

### Changes

1. Replace the current `### A. Basic Info` bullet list with the tag block YAML schema from Template 0 §0. The fields are mostly the same but reorganized:
   - Group `tags:` as a nested block (attributes, key_concepts, related_concepts, atl_skills, transdisciplinary_theme)
   - Add `progression:` as a new required block (topic_axis, difficulty_level, next_step_hint, reward_hook)
   - Add `tier_variants:` as an optional field
   - Add `caregiver_role:` with tier-dependent default

2. Add a note near the tier section (~line 41) pointing to `templates.md` Template 0 §3 for the 5-dial tier adaptation defaults.

3. Add a note near the Key Concepts section (~line 58) pointing to `docs/progression_axes.md` for the axis-level mapping.

### What NOT to change
- The KUD model, ATL skills list, 6 Transdisciplinary Themes, V1 constraints, game styles — all stay as-is
- The self-evaluation rubric dimensions (D1-D10) — stay as-is
- The design loop and agent workflow — stay as-is (the agent just reads the new Template 0 instead of Template A/B directly)

### Files to read first
- `program.md` (full file)
- `docs/template_0_preview.html` §04 (tag block with annotations)

---

## Task 4 — Update `entity_guidance.md`

**Modify existing file.** Two small additions:

1. In §5 (Tier Guidance Usage), add a pointer to Template 0 §3 for the 5-dial tier adaptation model. Currently §5 only talks about vocabulary selection from tier_guidance; it should also mention that the tier determines AI role, task depth, concept focus, and caregiver role defaults.

2. Add a new §7 (or append to §6) about **progression axis selection**:
   - When reading an entity mapping, the agent should identify which Key Concept the activity's anchor dimensions most naturally serve
   - That Key Concept becomes the `progression.topic_axis`
   - The `difficulty_level` (1-3) is chosen based on how deep the anchor dimensions go (surface attributes → L1, functional relationships → L2, causal/abstract reasoning → L3)
   - Point to `docs/progression_axes.md` for the full axis definitions

### Files to read first
- `entity_guidance.md` (full file)
- `docs/progression_axes.md` (created in Task 1)

---

## Task 5 — Update `docs/game_design_playbook.md`

**Modify existing file.** The playbook is the human-readable overview. Updates:

1. **Section 4 (How to Design an Entity Gold Standard)**: Update step 1 to mention the tag block header as the first thing to fill. Update step 3 to reference Template 0 instead of "base template + pillar overlay" — the agent now reads Template 0, then the category overlay, then the pillar overlay.

2. **Section 8 (Automated Game Design Pipeline)**: Update the design loop to show that the agent reads Template 0 as the base, then applies the category overlay. The `Step 2: Load base template` instruction should reference Template 0 explicitly.

3. **Add a new subsection** (Section 4.5 or similar) titled "Choosing the Progression Axis" that briefly explains how to pick a topic_axis and difficulty_level for a new design. Point to `docs/progression_axes.md`.

### Files to read first
- `docs/game_design_playbook.md` (full file)
- `docs/template_0_preview.html` §05 (upstream/downstream bridges)

---

## Task 6 — Update `assignments.md` format

**Modify existing file.** Add `axis=` and `level=` as optional fields in the assignment format spec, so future assignments can declare which progression axis and difficulty level to target.

### New format
```markdown
- [ ] entity + category N, tier=TX, style=game_style, axis=form, level=2, scene=...
```

No need to backfill existing completed assignments — they're already marked `[x]`.

---

## Verification checklist

After all tasks are done, verify:

- [ ] `templates.md` has Template 0 at the top, Template A and B are overlays referencing it
- [ ] `program.md` §A.Basic Info matches the tag block schema (includes progression block, tier_variants, caregiver_role)
- [ ] `docs/progression_axes.md` exists with all 7 axes, 3 levels each, gold-standard coverage table
- [ ] `entity_guidance.md` has a pointer to tier adaptation defaults and progression axis selection
- [ ] `docs/game_design_playbook.md` references Template 0 in sections 4 and 8
- [ ] `assignments.md` format spec includes axis= and level= fields
- [ ] Run one test assignment through the updated pipeline to confirm the agent can read Template 0, apply an overlay, fill the tag block, and produce a valid design

---

## Post-implementation follow-ups (not in this session)

- L × T interactive walkthrough for author onboarding (3×3 matrix: one axis × 3 levels × 3 tiers with example dialogue)
- Author training guide with fully worked examples
- Backfill existing 22 designs with the new tag block header (can be automated)
- Design the child recap and parent growth path screens against the tag block contract
