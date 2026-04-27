# Activity Signature — Cross-Repo Integration Overview

> **This is a coordination/overview doc.** The actual bite-sized implementation plans live in their target repos:
>
> - **Authoring (this repo):** `docs/plans/2026-04-23-activity-signature-authoring.md`
> - **Backend (wonderlens-ai):** `wonderlens-ai/docs/plans/2026-04-23-activity-signature-backend.md`
> - **Demo port (fullstack-demo):** `wonderlens-activity-fullstack-demo/docs/plans/2026-04-23-activity-signature-demo.md`
>
> Design spec (required reading for all three): `docs/plans/2026-04-23-activity-signature-design.md`

---

## 1 · What this feature is

Extend the Template 0 §04 tag block with an `activity_signature` block — 6 new fields that answer *"should this activity follow this conversation?"* Complements matchability tags (which answer *"can this entity run this activity?"*).

The signature gives each game an editorial identity: what attribute it attends to (`observation_angle`), what the child does (`mechanic`), and how the photographed entity participates (`entity_role`). The runtime uses those signals to score candidate activities against a `conversation_signature` derived from the preceding chat — so if the conversation dwelled on color, a color-attending activity wins; if it shifted to shape, a shape-attending activity wins.

Same directory restructure: each game becomes a folder (`activities/<game_id>/`) with `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`. Runtime writes `recap.latest.yaml` + `dashboard.latest.yaml` into that folder on session end as a last-run cache.

## 2 · The 6 new tag-block fields (verbatim from design spec §3)

```yaml
activity_signature:
  observation_angle: color          # enum, 12 values — §3.2 of design spec
  mechanic: collect                 # enum, 10 values — §3.3
  entity_role: exemplar             # enum, 4 values — §3.4
  focal_attribute: red              # string, parameterized attribute
  bridge_prerequisites:
    primary:   [color]              # 1-3 angles — must-have for clean transition
    secondary: [pattern]            # 0-3 angles — nice-to-have
  preview_label:  "Find three red things!"
  preview_prompt: "You noticed the red... Let's go find more red things together."
  role_pivot_note: "..."            # optional; surfaces pivot when entity_role shifts
```

Authoritative vocabularies in `docs/activity_vocabulary.md` (authored in Task 1 of the authoring plan).

## 3 · Repos and where implementation lives

| Repo | Role | Plan file | Task count |
|---|---|---|---|
| `wonderlens-activity-autodesign` (this) | Authoring + vocabulary + 5 game migrations | `docs/plans/2026-04-23-activity-signature-authoring.md` | 4 |
| `wonderlens-ai` (GitLab) | Production backend — loader, models, selector, writer, DB | `docs/plans/2026-04-23-activity-signature-backend.md` | 12 |
| `wonderlens-activity-fullstack-demo` (GitHub) | Prototype — dataclass port of the backend | `docs/plans/2026-04-23-activity-signature-demo.md` | 5 |

**Rule from `memory/project_three_repos.md`:** don't copy code between backend and demo. Each re-implements in its own style (Pydantic vs dataclasses; `DatabaseManager` vs `aiosqlite`). Logic parity is verified by a shared JSON test vector.

## 4 · Shared scenario vector

`activity_signature_scenarios.json` encodes 4 conversation-to-activity scenarios:

1. `pen_color_matches_color_scout` — conversation attended to color → Color Scout wins over Shape Quest (primary bonus +1.5)
2. `ladybug_shape_matches_shape_quest` — conversation shifted to shape → Shape Quest wins
3. `lion_behavior_matches_voice_stage` — Tier A match stacks with behavior bonus → Voice Stage Lion
4. `no_conversation_signature_legacy_behavior` — null signature → base tier scoring, backwards-compatible

**Lifecycle:**
1. Authored in this repo (autodesign) during Task 4 of the authoring plan
2. Copied byte-identical into wonderlens-ai during Task 10 (or earlier, per the backend plan)
3. Copied byte-identical into fullstack-demo during Task 5 of the demo plan
4. Any change to rules → update JSON here first → re-copy into both consumer repos → both test runners must pass

Divergence = automatic block on merging any of the three PRs.

## 5 · Execution order

1. **Authoring PR ships first.** Produces the canonical vocabulary doc, Template 0 §04 update, 5 migrated game dirs, scenario fixture. All three downstream plans consume these artifacts.
2. **Backend + demo can ship in parallel** (independent of each other). Backend is the reference implementation; demo is the mirror. Both copy the fixture + per-game dirs from the autodesign worktree/branch.
3. **Three separate PRs.** Each cross-links to this overview doc and the design spec.

One optimization worth noting: the backend and demo plans can start *before* the authoring PR merges, as long as the authoring *branch* exists with the fixture + per-game dirs committed. Consumer plans read from that branch's worktree via absolute path in their copy steps.

## 6 · Known V1 limitations (common to all three plans)

Document in each PR description.

1. **Outcome classification is shallow.** V1 uses keyword-matching heuristic for `dominant_angle`. False negatives on synonyms not in the table (e.g., *"crimson"* → color). An LLM-based classifier is future work.
2. **5 games migrated; 19 remain on legacy layout.** Dual-layout loader handles both; follow-up PRs migrate the rest in batches. Unmigrated games have `activity_signature = None` and are scored without signature bonus.
3. **Angle-to-axis map is static.** `_ANGLE_TO_AXIS` hardcodes visual/physical angles → Form. If an activity is genuinely at Causation angle=color (*"why is it red?"*), dashboard rollup misattributes. Revisit when a real case surfaces.
4. **`.latest.yaml` files committed to git.** Cautious default; switch to `.gitignore`d if authors find the noise unhelpful.
5. **`bridge_prerequisites.secondary` non-enum strings stored but unscored.** V1 preserves them for authoring flexibility; matching comes later.

## 7 · Related design artifacts

- **Design spec** — `docs/plans/2026-04-23-activity-signature-design.md` (authoritative)
- **Vocabulary doc** — `docs/activity_vocabulary.md` (produced by authoring Task 1)
- **Template 0 §04** — `docs/template_0_preview.html` + `_cn.html` (extended by authoring Task 2)
- **Matchability tags** — `docs/plans/2026-04-20-matchability-tags-*.md` (complementary; already shipped)
- **Progression runtime** — `docs/plans/2026-04-21-progression-runtime-*.md` (selector bonus stacks with progression's rung bonus)
- **Background brief** — `docs/plans/2026-04-23-progression-background-brief.md` (related system context)

## 8 · How to start

**Executing the authoring plan:**
```
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
cat docs/plans/2026-04-23-activity-signature-authoring.md | less
```

**Executing the backend plan:**
```
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
cat docs/plans/2026-04-23-activity-signature-backend.md | less
```

**Executing the demo plan:**
```
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
cat docs/plans/2026-04-23-activity-signature-demo.md | less
```

All three plans expect `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans`.

---

## Revnote

- **v0.3** (2026-04-27) — Updated observation-angle references to 12 values after adding `quantity` and `emotion`.
- **v0.2** (2026-04-23) — Split from monolithic 20-task combined plan into three repo-specific implementation plans (linked in the header). This doc is now a thin coordination layer — scenario contract, limitations, repos, execution order — rather than containing task bodies.
- **v0.1** (2026-04-23) — Inaugural single-doc combined plan covering 20 tasks across all three repos. Superseded by v0.2 split.
