# Template 0 Post-v0.2 Roadmap — Macro Implementation Plan

**Source roadmap:** `docs/plans/2026-04-20-template-0-roadmap.md`
**Template 0 authority:** `docs/template_0_preview.html` (v0.2, 2026-04-17)
**Planning date:** 2026-04-20

---

## Context

Template 0 v0.2 is the new category-agnostic activity skeleton. The roadmap in `docs/plans/2026-04-20-template-0-roadmap.md` lists 6 items to close out the v0.2 cycle; item 5 (L×T walkthrough) is already shipped. The remaining five items (1 sign-off, 2 progression_axes.md, 3 templates.md refactor, 4 program.md tag-block, 6 author training) still need executable plans and code.

This macro plan consolidates all five into a single phased sequence with per-item sub-plans, so a separate session can pick up any phase without re-reading the full roadmap. The intended outcome: Template 0 becomes the operational default — `templates.md`, `program.md`, and a training guide all align with the preview spec, and the downstream surfaces (`child_recap_preview.html`, `parent_growth_path_preview.html`) get a stable upstream contract.

### User decisions locking this plan

- **Scope:** all 5 outstanding items bundled into one macro plan.
- **Item 1 (sign-off):** assumed granted — items 3 and 4 proceed without a gate.
- **Item 3 target shape:** Option B (single-file `templates.md` with Template 0 reference + 6 pillar overlay sections + category appendix).
- **Item 6 format:** Markdown v0.1 (`docs/author_training_guide.md`).

### Findings from state check that reshape the roadmap

1. **Item 4 is "introduce" not "promote".** `program.md` (v1.0, 563 lines) currently has no tag-block concept — only scattered concept/discipline tag metadata. The work is adding a new top-level section, not moving an existing one.
2. **Item 3 is synthesis, not extraction.** `templates.md` (376 lines) embeds pillar-specific content inline within each template's Step descriptions, not as nested overlay subsections. Extracting 6 overlays requires synthesizing from ~12 scattered inline references (2 templates × 6 pillars). Plan on content authoring, not pure restructuring.
3. **Item 2 has a downstream constraint.** `docs/child_recap_preview.html` §04 and `docs/parent_growth_path_preview.html` §03/§07 already consume `progression.topic_axis` and axis-keyed content. The 7-axis enum in `progression_axes.md` must match those docs, not the other way around. Treat the downstream preview docs as implicit spec sources during drafting.
4. **All Template 0 work is currently uncommitted** (W16 has 3 commits + ~6 untracked doc/plan files). Each phase below opens its own worktree off `origin/main`; the new plans under `docs/plans/` will be committed as part of phase 0.

---

## Phased sequence

```
Phase 0 — Commit the roadmap + this macro plan              [prep,  ~30 min]
Phase 1 — Items 2 + 4 in parallel (independent)             [2 PRs, ~2 sessions each]
Phase 2 — Item 3: templates.md refactor (Option B)          [1 brainstorm + 2–4 PRs]
Phase 3 — Item 6: author_training_guide.md                  [1 PR, depends on 2+3+4]
```

Phases run strictly in order. Inside phase 1, items 2 and 4 are true parallel (different files, no shared state); a single author can still do them sequentially if bandwidth doesn't permit two worktrees.

---

## Phase 0 — Commit the roadmap + this macro plan

**Type:** prep.  **Files touched:** `docs/plans/2026-04-20-template-0-roadmap.md`, `docs/plans/2026-04-20-template-0-macro-implementation.md` (copy of this plan placed into repo).

**Actions:**
1. In a new worktree (`.worktrees/docs/template-0-macro-plan/`): copy this file into `docs/plans/2026-04-20-template-0-macro-implementation.md`.
2. Commit both plan files with `docs(plans): add template 0 roadmap + macro implementation plan`.
3. Open PR → merge.

**Acceptance:** both plan docs live on `main`; future phases can reference them by path.

---

## Phase 1 — Items 2 and 4 (parallel)

Two independent worktrees. Each gets its own brainstorm → write-plan → subagent-driven-development cycle.

### Phase 1a — Item 2: `docs/progression_axes.md`

- **Worktree:** `.worktrees/feat/progression-axes/` on branch `feat/progression-axes`.
- **Files to read first:**
  - `docs/template_0_preview.html` §07 (axes grid + coverage table)
  - `docs/parent_growth_path_preview.html` §03 curiosity radial (personality-word descriptions for the 7 axes) and §07 (axis contract)
  - `docs/child_recap_preview.html` §04 (tag-block read)
  - `docs/plans/2026-04-17-downstream-surfaces-split-design.md`
  - `entity_guidance.md` (tier-specific language)
  - `program.md` §1.4 (7 Key Concepts definitions)
- **Output shape:** ~500 lines of markdown, sections per roadmap §3: intro / 7 axis sections (definition + L1/L2/L3 signals + detection cues + entity affinity + T0/T1/T2 dialogue examples) / axis interaction / tag-block contract / versioning.
- **Constraint:** axis enum and L1/L2/L3 labels must match what `child_recap_preview.html` and `parent_growth_path_preview.html` already consume. If anything differs, this doc is the new source of truth and the preview docs get a coordinated patch in the same PR.
- **PR:** `docs: add progression axes spec — 7 topic axes × 3 rungs`.
- **Acceptance:** roadmap §3 acceptance criteria met + v0.1 revnote block.

### Phase 1b — Item 4: introduce tag block in `program.md`

**Reframe vs roadmap:** `program.md` currently has no tag-block section at all — this introduces one, not promotes an existing one. The downstream contract is already defined by `child_recap_preview.html` §04 and `parent_growth_path_preview.html` §07; this phase teaches `program.md` to emit it.

- **Worktree:** `.worktrees/refactor/program-tag-block/` on branch `refactor/program-tag-block`.
- **Files to read first:**
  - `program.md` (full, 563 lines — locate insertion point after Phase 1 context, before the generation loop)
  - `docs/template_0_preview.html` §04 (canonical tag block spec)
  - `docs/child_recap_preview.html` §04 and `docs/parent_growth_path_preview.html` §07 (consumer contracts)
  - `docs/progression_axes.md` (from phase 1a — needed for axis enum cross-reference; if 1a hasn't landed yet, reference Template 0 §07 and leave a TODO for 1a's landing)
- **Work:**
  1. Extract existing `program.md` concept-tag / discipline-tag mentions (lines 137, 197, 222, 225) — these may or may not collapse into the new tag block.
  2. Draft new "Tag block — the central contract" section: field-by-field spec (entity, category, tier, pillar, role_title, highlight_moment, key_concepts, atl_skills, subject_tags, transdisciplinary_theme, progression.{topic_axis,difficulty_level,next_step_hint}, caregiver_role, related_concepts, pillar_payoff) with required/optional flags and valid values.
  3. Insert after `program.md` Phase 1 context, before the generation loop.
  4. Add a pre-output self-check prompt to the generation loop: "Have all required tag-block fields been filled with non-placeholder values?"
  5. Cross-references: Template 0 §04, `docs/progression_axes.md`, `docs/child_recap_preview.html`, `docs/parent_growth_path_preview.html`.
- **Dependency note:** if phase 1a hasn't landed when this lands, phase 1b commits a TODO comment pointing at the progression_axes.md enum. Coordinated follow-up PR updates the link after 1a merges. Do not block 1b on 1a.
- **PR:** `refactor(program): introduce tag block as central contract`.
- **Acceptance:** roadmap §5 acceptance + integration check: one sample activity run whose emitted tag block parses against the child recap §04 reader and parent dashboard §07 reader.

---

## Phase 2 — Item 3: `templates.md` refactor (Option B)

**Size:** biggest of the five items. Plan on a full brainstorm → spec → plan cycle before code.

- **Worktree:** `.worktrees/refactor/templates-overlays/` on branch `refactor/templates-overlays`.
- **Brainstorm first** (`superpowers:brainstorming`): confirm Option B shape, decide whether creative variables hoist to Template 0 reference or stay per-overlay, choose v1.0 vs v2.0 version bump.
- **Write-plan** output: `docs/plans/YYYY-MM-DD-templates-overlays-design.md` + `docs/plans/YYYY-MM-DD-templates-overlays-implementation.md`.
- **Target `templates.md` structure (Option B, from approved preview above):**
  ```
  Intro — "Template 0 + 6 pillar overlays"
  Template 0 reference (→ docs/template_0_preview.html §03)
  Overlay: Mystery / Creation / Performance / Discovery / Adventure / Nurture
    (each: game mechanic, payoff pattern, pillar creative variables, step 3/4 overrides)
  Category appendix — Cat1 vs Cat5 structural modifiers
  ```
- **Content synthesis work (the non-obvious cost):** for each of the 6 pillars, gather pillar-specific text currently embedded inline in `templates.md` Template A Step 2–5 **and** Template B Step 2–5. Cross-compare the two, keep what's genuinely pillar-invariant in the overlay, move what's category-specific to the category appendix.
- **Coordinated update to `program.md`** (mandatory same-batch):
  - `program.md` currently references "Template A / Template B" reading flow. After refactor it must read Template 0 (from preview §03) + one pillar overlay (from new templates.md). Include this update as the LAST task in the implementation plan so merge-time `templates.md` and `program.md` stay consistent.
  - `grep -n 'Template [AB]' program.md` before starting to enumerate touch points.
- **Do not touch** `entity_guidance.md` (tier guidance is orthogonal — roadmap §4 explicit).
- **PR strategy:** 2–4 PRs per implementation plan — roughly one per-pillar-overlay batch + one program.md sync PR, or one structural skeleton PR + one content-synthesis PR + one program.md PR. Decide during write-plan.
- **Integration test:** agent generates one activity end-to-end against the new `templates.md` + updated `program.md`. Output must be structurally equivalent (same tag block, same beat order) to a legacy Template A + pillar overlay generation of the same entity × pillar × tier. Keep a pre-refactor golden output in the plan doc for diffing.
- **Acceptance:** roadmap §4 acceptance criteria, plus no `grep` hit for dead "Template A" / "Template B" references in `program.md` after the final PR.

---

## Phase 3 — Item 6: `docs/author_training_guide.md`

**Depends on:** phases 1a, 1b, 2 all merged.

- **Worktree:** `.worktrees/docs/author-training/` on branch `docs/author-training`.
- **Brainstorm first** to pick 3 worked examples spanning tiers / pillars / axes / categories. Candidates from roadmap §6:
  1. Ladybug × Cat1 × Mystery × T1 (reuse running example — continuity with Template 0 and L×T walkthrough)
  2. Sunflower × Cat5 × Discovery × T0 (already a quote context in parent_growth_path_preview §04)
  3. Construction paper × Cat1 × Creation × T2 (fresh — shows generalization)
- **Per worked example:** input triple → Template 0 + pillar overlay read → slot fill → full tag block emission → 10-dimension rubric self-check (from `program.md`) → final design → sample downstream rendering notes (what child recap shows, what parent dashboard shows).
- **Format:** markdown v0.1. No HTML mirror in this pass.
- **Cross-references must be live:** `docs/template_0_preview.html`, `templates.md`, `program.md`, `docs/progression_axes.md`.
- **Acceptance:** roadmap §6 — a new author reading only this guide can generate a 4th activity correctly without help. Validate by running the agent against a novel entity and checking output tag block is fully populated.

---

## Critical files to be modified or created

| Phase | File | Action |
|---|---|---|
| 0 | `docs/plans/2026-04-20-template-0-roadmap.md` | commit (currently untracked) |
| 0 | `docs/plans/2026-04-20-template-0-macro-implementation.md` | create (this plan) |
| 1a | `docs/progression_axes.md` | create |
| 1a | `docs/child_recap_preview.html`, `docs/parent_growth_path_preview.html` | patch iff axis enum drifts |
| 1b | `program.md` | introduce tag-block section + self-check prompt |
| 2 | `templates.md` | refactor to Template 0 reference + 6 overlays + category appendix |
| 2 | `program.md` | sync reading flow to new templates.md (same batch as templates.md PR) |
| 3 | `docs/author_training_guide.md` | create with 3 worked examples |

---

## Existing patterns to reuse

- **Worktree layout:** `.worktrees/{feat,fix,refactor,docs}/<topic>/` off `origin/main` (per repo convention in `~/.claude/projects/.../memory/feedback_worktree_convention.md`).
- **Plan file naming:** `docs/plans/YYYY-MM-DD-<topic>-<kind>.md` where `<kind>` ∈ {design, implementation} (per `feedback_plan_datetime.md`).
- **Per-feature review:** run `code-reviewer` + `code-simplifier` agents on each PR's diff before marking ready (per `feedback_review_simplify.md`).
- **EN/CN parity:** any HTML preview docs touched must keep `_cn.html` mirror structurally identical (YAML/field names stay English in both).
- **Skill workflow:** each phase uses `superpowers:brainstorming` → `superpowers:writing-plans` → `superpowers:subagent-driven-development` per roadmap §7.
- **Version conventions:** each doc's tail revnote block matches the `child_recap_preview.html` / `parent_growth_path_preview.html` style (v0.1 Inaugural draft · YYYY-MM-DD · one-line rationale).
- **Template 0 §§ cross-reference:** every new doc links back to specific `docs/template_0_preview.html` section anchors rather than re-stating spec content, to keep the preview as the single source of truth.

---

## Verification (end-to-end, after phase 3)

Run these against `main` once all 5 items have merged:

1. **Spec integrity**
   - `grep -n 'Template [AB]' program.md templates.md` → no matches outside historical/revnote comments
   - `grep -n 'topic_axis' program.md docs/progression_axes.md docs/child_recap_preview.html docs/parent_growth_path_preview.html` → enum matches across all four
2. **Agent generation smoke test** (per phase 2 integration test, repeated post-phase 3)
   - Pick one of the training guide's 3 worked examples. Feed input triple to the agent. Compare emitted tag block to the guide's expected tag block — structural match (keys present, values well-formed, no placeholders).
3. **Downstream render smoke test**
   - Feed emitted tag block from step 2 through `child_recap_preview.html` §04 reader and `parent_growth_path_preview.html` §07 reader. Both render without missing-field errors.
4. **Training-guide self-validation**
   - Pick a novel entity not in the 3 worked examples. Using only `docs/author_training_guide.md`, generate a 4th activity. Acceptance: the reader (or a fresh session) produces a valid, fully-populated tag block without needing to read `templates.md` or `program.md` directly.

---

## Out of scope for this macro plan

- Entity Bridging implementation (`prompts/constellation_bridge.md`, `constellation_map.yaml`) — tracked separately in W16 handoff, not part of Template 0 v0.2 closeout.
- HTML version of `docs/author_training_guide.md` — deferred until post-v0.1 traffic data says it's worth the cost.
- `HANDOFF.md` resync — out of scope here; noted in W16 weekly report as a separate follow-up.
- `entity_guidance.md` changes — tier guidance is orthogonal to Template 0 structure.
