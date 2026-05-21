---
name: wonderlens-workbook-to-review-packet
description: Use when a WonderLens original activity design workbook is the source input for creating or patching generated activities, Codex goal files, source-intent audits, review.html dashboards, standalone activity HTML reviewer packets, or PR-ready run artifacts.
---

# WonderLens Workbook To Review Packet

## Overview

Use this repo-local skill to turn an original WonderLens design workbook into reviewer-ready run artifacts. Keep repo docs and scripts as the source of truth; this skill only chooses the workflow, loads the right references, and preserves the workbook's original design intent.

Operate from the `wonderlens-activity-autodesign` repo root. If the current directory is different, locate the repo before editing or running commands.

## Decision Flow

Choose the smallest workflow that matches the request:

| Request shape | Load |
|---|---|
| User provides only an original workbook and wants end-to-end output | `references/workbook-ingest.md`, then `references/goal-planning.md`, `references/generation-run.md`, `references/source-intent-audit.md`, and `references/review-export.md` |
| User wants a fresh full rerun from a workbook | `references/goal-planning.md`, `references/generation-run.md`, `references/source-intent-audit.md`, `references/review-export.md` |
| User wants to patch an existing run without full rerun | `references/existing-run-patch.md`, then `references/source-intent-audit.md` and `references/review-export.md` if needed |
| User wants only review/export artifacts regenerated | `references/review-export.md` |
| User wants only source-intent comparison | `references/source-intent-audit.md` |

Ask for clarification only when the workbook path, target run, or full-rerun-vs-patch choice cannot be inferred safely.

## Required Repo Context

Before changing generated activities or run artifacts, read the relevant current repo files:

- Always: `README.md`, `program.md`, `run.md`, `templates.md`, `review_dashboard.md`, `GOAL.md`, `activities/README.md`.
- Metadata/schema work: `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`.
- Mapping-informed generation: `entity_guidance.md`, `conversation_bridge.md`, `docs/game_styles.md`.
- Existing run patch/export: `runs/<run_id>/run_manifest.yaml`, `runs/<run_id>/review_notes.md`, existing package files, and any existing `source_comparison/` or `activity_exports/` artifacts.

Do not duplicate long rules from these files into new docs. If a repo doc conflicts with this skill, the repo doc wins unless the user's latest instruction explicitly changes the contract.

## Source-Intent Rules

For every workbook row, preserve the original source promise:

- original play frame;
- child role;
- interaction sequence;
- required child action;
- story or role-play framing;
- non-negotiable source elements;
- allowed V1 adaptations;
- product or asset dependencies.

Treat category and mechanic labels as metadata, not replacements for the actual play frame. A generated activity can keep a category token and still drift if the child role or loop changes materially.

## Minimum Accepted Contract

Capability-probe rows are not automatically blocked. If the user or run manifest states `product_contract_override=minimum_unblock_allowed`, treat the minimum acceptable version as approved for generation:

- generate normal five-file packages for all scoped workbook rows when the minimum version can preserve source intent;
- record formerly blocking dependencies as resolved blocker annotations, not unresolved product decisions;
- keep assumptions visible in `spec.md`, `prod.md`, `run_manifest.yaml`, `review.html`, and source comparison artifacts;
- do not claim unsupported runtime capabilities. Use honest reduced-scope behavior such as voice-only fallback, prebuilt assets, child/parent confirmation, no quality judgment, no motion detection, no live recoloring, or no hidden UI state unless the product actually supports it;
- still run the source-intent audit. A minimum version can pass only if it preserves the original play frame, child role, sequence, and required action.

Use `needs_product_decision` only when no minimum acceptable version has been approved, or when the approved minimum version still cannot express the source idea honestly.

Known drift patterns to catch:

- A profession-first role-play source becomes "pick the matching profession" instead of "you are this worker facing a scene."
- A story-unlock source becomes disconnected challenges without story narration and challenge-gated story progress.
- A runtime AI line is fixed when the design needs a runtime behavior contract plus an example line.

## Goal Mode

For full workbook-to-review-packet work, create a visible goal file before execution. Prefer `goals/YYYY-MM-DD-<slug>-goal.md` for run-specific goals and keep root `GOAL.md` as the stable generic contract unless the user asks to edit it.

Use the `goal-file-creator` skill when creating or revising a goal file. If a goal command/tool is available and the user wants end-to-end execution, run from that goal file. If goal mode is unavailable, execute the goal file manually and record that limitation.

## Validation

Use the narrowest checks for the touched files. Common checks:

```bash
git diff --check
python3 scripts/generate_run_review.py --validate runs/<run_id>
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate
python3 scripts/export_activity_html.py --validate runs/<run_id>
python3 scripts/integrate_generated_assets.py --validate runs/<run_id>
```

If the local default `python3` lacks required packages, use the repo/operator Python environment already documented in `HANDOFF.md` and `review_dashboard.md` before installing anything.

## Completion Contract

Before reporting completion:

- confirm only intended files changed;
- verify generated artifacts are derived from source run/package files, not hand-edited HTML;
- run focused validation;
- update `run_manifest.yaml`, `review_notes.md`, and `HANDOFF.md` when run behavior or handoff status changes;
- commit repo changes with a conventional commit unless validation failed or the user asked not to commit.
