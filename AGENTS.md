# AGENTS.md

Project-specific instructions for agents working in `wonderlens-activity-autodesign`.
These rules override global guidance when they are more specific.

## 1) Scope and Priority

- Scope: this file applies to the repository root and all subdirectories unless a deeper `AGENTS.md` exists.
- Priority: system/developer/user direct instructions first, then this file, then global defaults.
- Goal: make small, verifiable changes with minimal risk to WonderLens activity quality, metadata contracts, and downstream consumer compatibility.

## 2) Project Snapshot

- Project: WonderLens Activity Auto-Designer, a prompt/content repository for generating, transforming, and maintaining child-facing activity designs.
- Primary source of truth for activity generation: `program.md`.
- Category and pillar scaffolding: `templates.md` and `docs/game_styles.md`.
- Mapping-informed design rules: `entity_guidance.md` and `conversation_bridge.md`.
- Batch execution workflow: `run.md`.
- Engineering-spec to production-format workflow: `transform.md`, `transform_run.md`, and `transform_assignments.md`.
- Legacy activity outputs live under `designs/`.
- Migrated runtime activity packages live under `activities/<activity_id>/` with `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.

Key files and locations:

- `README.md` - stable repo overview and current workflow description.
- `program.md` - generation constraints, output structure, rubric, and seed exemplars.
- `templates.md` - reusable activity templates and pillar overlays.
- `assignments.md` - work queue for generated designs.
- `results.tsv` - generation/evaluation log.
- `activities/_schema/tag_block.schema.json` - JSON Schema for migrated activity metadata.
- `docs/activity_vocabulary.md` - canonical closed vocabularies mirrored by consumer repos.
- `docs/plans/` - design notes, implementation plans, and evaluation notes.
- `HANDOFF.md` - current session/status notes when project state changes meaningfully.

## 3) Non-Negotiable Constraints

- Do not mention Claude or any model as a code generator/co-author in commits, comments, or docs.
- Do not edit secrets, local credentials, production data, or machine-specific config unless explicitly asked.
- Do not perform opportunistic refactors, broad formatting sweeps, or dependency upgrades.
- Preserve the generation contract in `program.md`: exact activity structure, tag block requirements, V1 technical constraints, and 10-dimension self-evaluation rubric.
- Preserve the template/pillar model in `templates.md` and `docs/game_styles.md`; do not invent new pillars, game styles, or category semantics without explicit instruction.
- Preserve mapping-grounded behavior for mapping-informed designs: use tier-specific mapping attributes, key concept selection rules, dimension anchors, and warm/cold bridge convergence.
- Keep `results.tsv` column order intact when appending or updating results.
- Keep `activities/*/tag_block.yaml` enums aligned with `docs/activity_vocabulary.md` and `activities/_schema/tag_block.schema.json`.
- Treat consumer compatibility seriously: vocabulary/schema changes may require matching updates in downstream repos such as `wonderlens-ai` and `wonderlens-activity-fullstack-demo`.
- Never revert user changes you did not make.

## 4) Content and Markdown Style

- Prefer plain Markdown with stable headings and tables already used in the repo.
- Keep child-facing dialogue concrete, age-appropriate, and executable; avoid vague placeholders.
- Keep production files concise only where `transform.md` allows condensation.
- For engineering specs, preserve full dialogue branches, screen descriptions, warm/cold starts when required, and self-evaluation scorecards.
- For production files, follow `transform.md`: 7-row Basic Info table, English-only output, cold-start Step 1 only, condensed later rounds, compressed screen descriptions, no scorecard.
- Use ASCII in new files unless editing content that already intentionally uses non-ASCII symbols or child-facing copy needs them.
- Avoid changing generated design prose outside the requested scope; many files are reviewed artifacts.

## 5) How to Work

1. Read the relevant workflow documents before editing:
   - New design generation: `program.md`, `templates.md`, `docs/game_styles.md`, `entity_guidance.md`, `conversation_bridge.md`, `run.md`.
   - Production transformation: `transform.md`, `transform_run.md`, source `designs/*_spec.md`, and target `designs/*_prod.md`.
   - Migrated activity packages: `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`.
2. State assumptions when a source document and existing output disagree.
3. Make the smallest change that satisfies the request.
4. Validate immediately with the narrowest useful check.
5. Stop on failing checks, summarize the root cause, then fix incrementally.
6. Use a git worktree for code changes by default, and switch into that worktree before editing files or running implementation commands. The exception is doc-only or config-only edits, which may be made in the current checkout when appropriate.
7. When creating a git worktree, place it under `.worktrees/` at the project root using the convention `.worktrees/{feat,docs,fix,refactor,style,test,chore}/<worktree-name>`.
8. When working in plan mode or discussing design / implementation plans, write the plan to `docs/plans/` before making code changes. Use the project plan naming convention and make the plan detailed enough for a fresh session to execute.

## 6) Commit and Pull Request Messages

Use conventional commit format: `type(scope): description`.

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

```text
feat(agents): add director agent
fix(frontend): resolve silence timer race condition
refactor(assembler): simplify recipe validation
```

Keep the first line under 50 characters. Use present tense.

Use the same conventional format for pull request titles. Do not prefix PR
titles with agent markers such as `[codex]`; the title should describe the
full branch diff, for example `feat(graph): rewrite knowledge graph viz with focus+context`.

PR descriptions should be detailed enough to stand alone for reviewers. Use
real Markdown sections and include, as applicable:

- `## Summary` with concise bullets covering what changed, why it changed, and
  operator/developer impact.
- `## What's in the branch` when the branch has multiple commits, phases, or
  implementation arcs.
- `## Files` summarizing important new, modified, and removed paths.
- `## Test plan` with exact commands and manual checks, using checkboxes when
  the checks are reviewer-facing.
- `## Out of scope / deferred` for known non-goals, tradeoffs, or follow-ups.

## 7) Canonical Commands

Run from repo root unless noted.

```bash
# Inspect files
rg --files

# Check worktree state
git status --short

# Review changed markdown without running broad tooling
git diff --check
git diff -- AGENTS.md
```

Validate migrated activity metadata:

```bash
python3 -c "
import json, yaml, pathlib, sys
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
ok = True
for p in sorted(pathlib.Path('activities').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK  ' if not errs else 'FAIL'), p)
    for e in errs:
        ok = False
        print(f'  {list(e.absolute_path)}: {e.message}')
sys.exit(0 if ok else 1)
"
```

Notes:
- This repo currently has no `package.json`, `pyproject.toml`, `Makefile`, or compose manifest at the root.
- The activity metadata validation snippet requires `jsonschema` and `pyyaml` in the active Python environment.
- Do not start long-running services; this repository is primarily markdown, YAML, schema, and prompt assets.

## 8) Validation Policy

- `AGENTS.md` or docs-only edits: run `git diff --check` and review the targeted diff.
- Generated design edits: manually verify against `program.md` Phase 2 format and Phase 3 rubric; run targeted `rg` checks for known forbidden/stale patterns when applicable.
- Production transform edits: verify against `transform.md` and `transform_run.md` self-checks, including no Chinese text, no scorecard, no blockquotes, 7-row Basic Info table, and correct step structure.
- `activities/*/tag_block.yaml` edits: run the schema validation snippet above.
- `docs/activity_vocabulary.md` or schema enum edits: verify vocabulary/schema sync and call out required downstream repo updates.
- `results.tsv` edits: verify tab-separated column order and one row per completed assignment.
- If no automated check applies, state the manual validation performed and the source document used as the reference.

## 9) Change-Specific Guardrails

- New activity generation:
  - Follow `run.md` setup and loop.
  - Read the full required context before writing.
  - Complete one assignment before moving to the next.
  - Save both spec and prod files when the workflow requires both.
  - Append `results.tsv` only after the design passes the required self-evaluation.
- Mapping-informed designs:
  - Load the mapping index and entity block before choosing anchors.
  - Use primary key concepts first and source at least two related concepts from mapping data.
  - Record selected dimensions and ensure the design actually uses them.
  - For `start=warm+cold`, write both bridges and verify convergence into the shared Step 2.
- Transform workflow:
  - Treat `transform_assignments.md` as a progress tracker only.
  - Do not have multiple agents append to `docs/WonderLens_Game_Designs_prod.md`; regenerate it once in order after individual prod files are ready.
  - Keep `Game Style` in the production Basic Info table when present.
- Migrated `activities/` packages:
  - Directory name must equal `activity_id` in `tag_block.yaml`.
  - Keep `spec.md` as author/reviewer reference and `prod.md` as runtime prompt guidance.
  - Keep recap and dashboard templates placeholder-compatible with the runtime payload.

## 10) Documentation and Session State

Update living docs when behavior, operator workflow, or implementation status changes:

- `README.md`: stable overview, current workflow, project structure, and run instructions.
- `docs/plans/`: intended work, design decisions, risks, alternatives, and implementation notes.
- `HANDOFF.md`: current execution status, recent changes, verification, residual risk, and next immediate actions.

Keep documentation factual and tied to repository state. Do not add aspirational architecture or workflow claims that are not reflected in the files.

## 11) External Docs and Uncertainty

- Use Context7 for library/framework API uncertainty before coding or changing tooling.
- Prefer repo source documents over memory for WonderLens domain rules.
- If required docs or manifests referenced by an older file are missing or stale, say so explicitly and use the closest current source of truth.
- When local validation depends on missing Python packages, ask before installing dependencies unless the user has already authorized environment changes.

## 12) Completion Checklist

Before declaring completion:

1. Confirm only intended files changed.
2. Run the smallest relevant verification available for the touched files.
3. Confirm the change matches the relevant source document, such as `program.md`, `transform.md`, or `activities/README.md`.
4. Summarize files changed, checks run, and any remaining risk.
