# Workbook To Review Packet Goal

## Goal File Role

This file is the concise Codex goal-mode execution contract for generating reviewer-ready WonderLens activity packets from the original design workbook.

Detailed implementation lives in:

- Source dry-run plan: `docs/plans/2026-05-21-workbook-to-review-packet-dry-run.md`
- Repo-local workflow skill: `skills/wonderlens-workbook-to-review-packet/SKILL.md`
- Supporting references: `skills/wonderlens-workbook-to-review-packet/references/`
- Stable generation contracts: `program.md`, `run.md`, `GOAL.md`, `templates.md`, `review_dashboard.md`, `runs/README.md`

Use the dry-run plan for workbook inspection, source scope, and row mapping. Use the repo docs for package format, generation rules, review dashboard behavior, and validation. If this goal conflicts with the repo docs, the repo docs control behavior unless this goal states a narrower run-specific constraint.

Source plan version: `2026-05-21`.

Workbook:

```text
/Users/pharrelly/Downloads/活动库内部初版.xlsx
```

Python environment: script commands require PyYAML. In this local checkout, use:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3
```

## Objective

Execute a fresh workbook-to-review-packet run from the original activity design workbook.

The finished system must:

- ingest and verify all 40 `Sheet1` workbook activity rows;
- generate or explicitly resolve all scoped activity packages under a new `runs/<run_id>/activity_packages/` directory;
- preserve the workbook source intent for every row, including original play frame, child role, interaction sequence, required child actions, story/role-play framing, product dependencies, and allowed V1 adaptations;
- complete a full 40-row source-intent audit after generation;
- produce the product-facing source comparison matrix and the run-level `review.html`;
- integrate available prebuilt assets and mechanism storyboards into standalone reviewer packets when their images exist;
- record any missing images, unresolved product decisions, or high-severity intent drift as explicit review findings.

## Recommended `/goal` Command

```text
/goal Execute goals/2026-05-21-workbook-to-review-packet-goal.md end to end. Use docs/plans/2026-05-21-workbook-to-review-packet-dry-run.md for workbook scope and row mapping, use inputs/source_activity_concepts.md as the normalized source snapshot after verifying it against the workbook, create a fresh run labeled workbook_review_packet, preserve source intent for all 40 rows, run full source-intent audit, generate review.html and source comparison review, integrate/export available reviewer assets, run focused validations, commit intended changes only, and report artifacts/checks/residual risks.
```

## Required Execution Mode

- Create an implementation worktree from current `main` before generation or artifact changes unless already in an active feature worktree.
- Treat this as a full fresh run, not a patch of `runs/20260512_172135_batch5_unblocked`, unless the user explicitly redirects to existing-run patch mode.
- Use `product_contract_override=minimum_unblock_allowed` by default so capability-probe rows can generate reviewable packages with resolved blocker annotations. If the user rejects this override before execution, switch to blocker-preserving mode and do not force unsupported rows into valid packages.
- Use sub-agent-driven review when work can be split safely:
  - workbook/source snapshot verification;
  - package generation review;
  - source-intent audit;
  - review/export validation.
- Keep sub-agent write ownership disjoint.
- Use runtime behavior contracts where LLM wording should be generated at runtime: `Runtime AI instruction` plus `Example AI line`.
- Use exact `AI says` only when exact wording is intentionally required.
- After major feature groups pass focused checks, run `code-simplifier` on changed implementation scripts when applicable and request an independent review pass.
- Before marking complete, run final review until no accepted/actionable findings remain. If `codex-review` is unavailable, document the blocker and alternate review evidence.
- Use conventional commits and do not push unless explicitly requested.

## Hard Constraints

- Do not hand-edit generated HTML as source of truth. Fix source package, manifest, audit, asset, storyboard, or generator inputs and regenerate.
- Do not change activity IDs, tag-block enum values, pillar names, game style names, or vocabulary/schema contracts unless a separate downstream compatibility plan authorizes it.
- Do not let category or mechanic labels override the workbook's original play frame.
- Do not preserve a category token while changing child role, story frame, interaction sequence, or required child action without explicit product approval.
- Do not commit raw Chinese source prose into generated package content; normalize package-facing and audit-facing text to English while retaining row references.
- Do not claim asset exports are complete when required contact-sheet or storyboard images are missing. Record prompt-ready or missing-image status instead.
- Do not treat source-intent audit output as product signoff. It is structured review input.
- Do not touch `.env`, secrets, credentials, production data, or machine-specific config.
- Preserve existing user changes and avoid broad formatting/refactor sweeps.

## Required Scope

Implement the full workflow for:

- workbook path: `/Users/pharrelly/Downloads/活动库内部初版.xlsx`;
- sheet: `Sheet1`;
- activity rows: Excel rows 2-41;
- normalized source snapshot: `inputs/source_activity_concepts.md`;
- source concept count: 40;
- run label: `workbook_review_packet`;
- assignment scope: all 40 workbook activity rows;
- product contract override: `minimum_unblock_allowed`.

Major work areas:

- verify workbook headers, row count, and source concept mapping against `docs/plans/2026-05-21-workbook-to-review-packet-dry-run.md`;
- initialize a new `runs/<run_id>/` directory per `run.md`;
- create run-start assignment snapshot from the 40 source concepts;
- generate five-file run-local packages for scoped rows, or record explicit blocked/product-decision outputs if the override is disabled;
- run self-evaluation, reviewer evidence, and focused package checks before logging results;
- run full source-intent audit with one entry per workbook row;
- render and validate `source_comparison/product_review_matrix.html`;
- generate or refresh review-only storyboard prompt artifacts;
- generate or refresh prebuilt asset prompt artifacts for selected activity/asset pairs;
- integrate available generated contact sheets when images exist;
- export standalone activity HTML reviewer packets for integrated activities when bindings validate;
- generate and validate `runs/<run_id>/review.html`;
- update `run_manifest.yaml`, `review_notes.md`, `generated_activity_ids.txt`, `results.tsv`, `assignments.md` only where the run workflow requires it;
- update `HANDOFF.md` with the run outputs, checks, residual risks, and product-review findings.

## Known Source-Intent Risks

Pay special attention to these workbook rows:

- `source_career_decision`: the child must first assume a profession, then make decisions inside a work scenario. Do not turn it into "pick the matching profession for this scenario."
- `source_story_challenge_unlock`: the AI must tell a story, pause for a small challenge, and unlock the next story beat. Do not turn it into disconnected challenges without story narration.
- `source_toy_tidy_challenge`: preserve the tidy-up process and before/after or confirmation risk; do not reduce it to verbal sorting only unless product approves the adaptation.
- `source_coloring_game`: do not claim live fillable coloring UI unless product support exists or the dependency is recorded as a resolved blocker under the override.

For these rows, read and preserve the `source_intent_lock_en`, `minimum_unblock_status`, and `resolved_assumptions_en` fields in `inputs/source_activity_concepts.md`.

## Preconditions

Before execution:

```bash
test -f /Users/pharrelly/Downloads/活动库内部初版.xlsx
test -f docs/plans/2026-05-21-workbook-to-review-packet-dry-run.md
test -f inputs/source_activity_concepts.md
test -f program.md
test -f run.md
test -f review_dashboard.md
test -f scripts/generate_run_review.py
test -f scripts/generate_source_comparison_review.py
test -f scripts/generate_storyboard_prompts.py
test -f scripts/generate_asset_pilot_prompts.py
test -f scripts/integrate_generated_assets.py
test -f scripts/export_activity_html.py
git status --short
```

Confirm source concept coverage:

```bash
rg -c "^### source_" inputs/source_activity_concepts.md
```

Expected output: `40`.

## Success Criteria

### Workbook Ingest

- Workbook inspection confirms `Sheet1` has 40 activity rows.
- Each workbook row maps to exactly one normalized source concept.
- The run records source row IDs so later audit rows can trace back to the workbook.
- Intent-sensitive source concepts carry explicit source-intent locks into adaptation briefs and generated package rationale.
- Any mismatch between workbook text and `inputs/source_activity_concepts.md` is repaired before generation.

### Package Generation

- Every generated package has exactly five files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`.
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- Package runtime beats preserve workbook source intent and use runtime LLM behavior contracts when appropriate.
- Resolved product blockers are visible in package files and review outputs when `minimum_unblock_allowed` is active.

### Source-Intent Audit

- `runs/<run_id>/source_comparison/source_intent_audit.yaml` exists with exactly 40 entries.
- Every entry records `source_row`, `activity_id`, `original_play_frame`, `generated_play_frame`, `preserved`, `drift`, `status`, `severity`, `recommendation`, and `product_review_question`.
- Status values are limited to `aligned`, `minor_adaptation`, `intent_drift`, and `needs_product_decision`.
- High-severity drift is either repaired or explicitly reported as a product-review finding.

### Review And Export

- `runs/<run_id>/source_comparison/product_review_matrix.html` exists and validates.
- `runs/<run_id>/review.html` exists and validates.
- Storyboard and asset prompt manifests are current.
- Integrated asset bindings validate for every available generated contact sheet.
- Standalone activity HTML reviewer packets validate for every integrated activity.
- Missing image files are recorded as prompt-ready or residual risk, not silently treated as completed exports.

## Required Checks

Run the narrowest relevant checks during execution. Minimum final checks:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m py_compile scripts/generate_run_review.py scripts/generate_source_comparison_review.py scripts/generate_storyboard_prompts.py scripts/generate_asset_pilot_prompts.py scripts/integrate_generated_assets.py scripts/export_activity_html.py
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/<run_id>
git diff --check
git status --short
```

When generated contact-sheet images exist and integration/export is in scope, also run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/<run_id>
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/<run_id>
```

For metadata/package changes, also run the activity tag-block schema validation command from `AGENTS.md`.

## Final Completion Gate

Do not mark achieved until:

- all 40 workbook rows are covered by generated or explicitly blocked/resolved outputs;
- source-intent audit covers all 40 rows;
- source comparison and review dashboard validations pass;
- available integrated asset exports validate, or missing image artifacts are documented as residual risk;
- focused checks pass;
- independent review has no accepted/actionable findings remaining;
- `HANDOFF.md`, run manifest, and review notes record outputs, checks, and residual risks;
- intended changes are committed with conventional commits;
- no secrets or unrelated files are included.

Final response must include:

- run ID;
- generated/blocked/resolved counts;
- source-intent audit counts by status;
- review dashboard path;
- source comparison path;
- standalone HTML export count;
- checks run and results;
- residual risks or product-review findings;
- commit hashes.
