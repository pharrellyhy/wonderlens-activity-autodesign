# Progression Runtime — Cross-Repo Integration Overview

> **This is a coordination/overview doc.** The actual bite-sized implementation plans live in the target repos:
>
> - **Backend (wonderlens-ai):** `wonderlens-ai/docs/plans/2026-04-21-progression-runtime-backend.md`
> - **Demo port (fullstack-demo):** `wonderlens-activity-fullstack-demo/docs/plans/2026-04-21-progression-runtime-demo.md`

---

## 1 · What this feature is

Implement the promotion / demotion / sibling-axis-jump progression engine that Template 0 §07 specifies and `template_0_progression_walkthrough.html` illustrates in 4 scenarios.

The runtime tracks a **rung-per-axis** state per device (7 axes × 3 rungs = 21 slots). Each activity session emits per-round signals; the rules engine classifies the trail into one of four outcomes (promote, hold, demote, soft-reframe) and updates per-axis counters that gate future rung assignments.

## 2 · The five quantified triggers (verbatim from §07)

| Trigger | Scope | Condition | Effect |
|---|---|---|---|
| **Within-activity promote** | single activity | child answered current rung correctly in **2+ rounds** without prompt-repetition, OR spontaneously produced an L+1 response | bump target rung for next activity on this axis |
| **Within-activity hold** | single activity | mixed or slow but on-topic | stay at current rung, vary exemplar |
| **Within-activity demote** | single activity | child did not complete current rung after **2 attempts** (silence > 6s, off-topic, or repeats prompt) | drop one rung, **same axis**; floor L1 |
| **Across-activity promote** | session sequence | child finished at current rung in **3 consecutive activities** on the same axis | next activity on that axis defaults to rung + 1 |
| **Across-activity demote** | session sequence | child needed an in-activity demote in **2 consecutive sessions** on the same axis | next activity on that axis defaults to rung − 1 (floor L1) |

Plus three footer rules: dignity reframe, sibling-axis jump, personalization hook. See Template 0 §07 in `docs/template_0_preview.html` for the authoritative text.

## 3 · Repos and where implementation lives

| Repo | Role | Plan file |
|---|---|---|
| `wonderlens-ai` (GitLab) | Production backend, DB-persisted multi-device | `docs/plans/2026-04-21-progression-runtime-backend.md` — 15 tasks |
| `wonderlens-activity-fullstack-demo` (GitHub) | Prototype, single-user, local SQLite | `docs/plans/2026-04-21-progression-runtime-demo.md` — 5 tasks |
| `wonderlens-activity-autodesign` (GitHub, this repo) | Owns the design artifacts (Template 0 §07, walkthrough, this overview) | No runtime code — design-only |

**Rule from `memory/project_three_repos.md`:** don't copy code between the two implementations. Each re-implements in its own style (Pydantic vs dataclasses; `DatabaseManager` vs `aiosqlite`). Logic parity is verified by a **shared JSON test vector**.

## 4 · Shared scenario vector

`progression_scenarios.json` encodes the 4 walkthrough scenarios as sequences of `(axis, entry_rung, round_signals)` → expected `(final_outcome, next_rung, sibling_jump_applied)`:

1. `steady_progression_form` — 3 sessions on Form, ending with across-activity promote to L3
2. `hit_a_wall_recovery` — 3 Causation sessions ending with 2 consecutive demotes → sibling jump pending
3. `across_axis_independence` — Form L3 + Causation L1 + Responsibility L1 coexist
4. `reluctance_not_inability` — soft-reframe after a single long silence is NOT a demote

**Lifecycle:**
1. Authored in the backend repo (`wonderlens-ai`) during Task 14 of the backend plan
2. Copied verbatim into the demo repo (`fullstack-demo`) during Task 2 of the demo plan
3. Any change to rules → update JSON in backend first → re-copy into demo → both test runners must pass

Divergence between the two implementations = automatic block on merging either PR.

## 5 · Execution order

1. **Backend plan ships first.** It's the production target and drives the canonical JSON. Target MR on GitLab.
2. **Demo plan ships second** (any time after backend MR merges — or even before, just copy the fixture from the backend branch directly).

The two plans can be implemented by different sessions / collaborators. Neither needs to wait for the other to start — only the JSON copy step (demo Task 2 Step 8) depends on the backend having authored the vector.

## 6 · Known V1 limitations (common to both repos)

These are intentional scope cuts; each repo-specific plan lists them in §6 for PR descriptions.

1. **Outcome classification from raw dialogue is shallow.** V1 uses placeholder heuristics (silent → silence, non-empty → correct). Proper LLM-based classifier is a separate future design.
2. **`topic_axis` missing from some gold-standard games.** Follow-up task inventories the 12 gold standards and backfills missing `progression.topic_axis` fields.
3. **Tier P property-bridges default to Form axis.** Some should be Function, Change, or Responsibility. Classification pending.
4. **Personalization pace model is interface-only.** V1 ships `v1_default/strict/loose` profiles. Per-child pace model needs ≥200 sessions of data and a separate ML spec.
5. **Parent-dashboard wiring.** The API feeds the 7-axis radial; the dashboard UI integration is a separate plan (tied to `parent_growth_path_preview.html` §03 curiosity radial).
6. **Cross-session continuity beyond last state.** History is stored but not used for smoother promotion curves; V1 is strictly counter-based.

## 7 · Related design artifacts

- **Template 0 §07** — `docs/template_0_preview.html` (authoritative rule text, English)
- **Template 0 §07 CN mirror** — `docs/template_0_preview_cn.html`
- **Walkthrough** — `docs/template_0_progression_walkthrough.html` + `_cn.html` (4 scenarios, dialogue snippets, state panels)
- **L × T walkthrough** — `docs/template_0_lt_walkthrough.html` (orthogonality of depth and tier; referenced from Scenario 3 state panel design)
- **Tag block spec** — `docs/template_0_preview.html` §04 (the `progression.topic_axis` and `progression.difficulty_level` fields the runtime reads)

## 8 · How to start

**If executing the backend plan:**
```
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
cat docs/plans/2026-04-21-progression-runtime-backend.md | less
```

**If executing the demo plan:**
```
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
cat docs/plans/2026-04-21-progression-runtime-demo.md | less
```

Both plans expect to be executed under `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans`.

---

## Revnote

- **v0.2** (2026-04-21) — Split from monolithic integration plan into two repo-specific implementation docs (linked in the header). This doc is now a thin coordination layer — scenario contract, limitations, repos, execution order — rather than containing task bodies.
- **v0.1** (2026-04-21) — Inaugural single-doc integration plan covering 19 tasks across both repos. Superseded by v0.2 split.
