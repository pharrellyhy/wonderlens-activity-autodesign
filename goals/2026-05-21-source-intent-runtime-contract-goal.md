# Source Intent And Runtime Contract Goal

## Goal File Role

This file is the concise Codex goal-mode execution contract for adding source-intent review and runtime behavior-contract support to the Batch 5 activity generation workflow.

Detailed implementation lives in:

- Source of truth: `docs/plans/2026-05-21-source-intent-runtime-contract.md`
- Supporting contracts: `program.md`, `run.md`, `GOAL.md`, `templates.md`, `review_dashboard.md`, `runs/README.md`
- Existing review artifact: `runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html`

Use the source plan for task order, exact file paths, validation behavior, and implementation detail. If this goal and the source plan conflict, the source plan controls implementation detail, but this goal controls scope, hard constraints, and completion gates.

Source plan version: `2026-05-21`.

Python environment: all script commands require PyYAML. In this local worktree, use the PyYAML-capable pyenv interpreter prefix:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3
```

## Objective

Implement a full source-intent audit layer for Batch 5 and update the generation/review contract so future packages preserve the original play frame while runtime AI beats can use constrained behavior instructions plus example dialogue.

The finished system must:

- audit all 40 Batch 5 workbook rows for source-intent alignment against generated runtime beats;
- show intent alignment in the product review matrix, separate from category/mechanic/capability status;
- update `program.md`, `run.md`, and `GOAL.md` so future generation fails review when the mechanic is preserved but the original play frame is changed without explicit approval;
- update review parsing so runtime beats may use either existing `AI says` dialogue or the new `Runtime AI instruction` plus `Example AI line` shape;
- repair or explicitly flag confirmed high-severity drift in Career Decision and Story Challenge Unlock.

## Recommended `/goal` Command

```text
/goal Execute goals/2026-05-21-source-intent-runtime-contract-goal.md end to end. Use docs/plans/2026-05-21-source-intent-runtime-contract.md as the controlling implementation plan. Add the full Batch 5 source-intent audit, update the product review matrix, update future generation contracts for source-promise alignment and runtime behavior contracts, repair or flag confirmed high-severity drift, run focused validations, commit intended changes only, and report outputs/checks/residual risks.
```

## Required Execution Mode

- Create an implementation worktree from current `main` before code changes unless already in an active feature worktree.
- Use TDD or test-first validation for every behavior change:
  - write failing source-intent audit tests before generator changes;
  - write failing runtime-contract parser tests before dashboard parser changes.
- Use sub-agent-driven development where work can be split safely:
  - source comparison/audit generator changes;
  - full 40-row content audit;
  - generation contract documentation;
  - runtime beat parser/dashboard changes;
  - package repairs for high-severity drift.
- Keep sub-agent write ownership disjoint.
- After each major feature group passes focused checks, run `code-simplifier` on changed implementation scripts when applicable.
- After each major feature group, request a fresh code review using `superpowers:requesting-code-review` or an equivalent independent review pass.
- Before marking complete, run `codex-review` until no accepted/actionable findings remain. If `codex-review` is unavailable, document that blocker and the alternate review performed.
- Use conventional commits and do not push unless explicitly requested.

## Hard Constraints

- Do not generate remaining prebuilt assets.
- Do not rewrite all 40 packages unless the source-intent audit identifies necessary repairs.
- Do not change activity IDs, tag-block enum values, pillar names, game style names, or vocabulary/schema contracts unless a later explicit downstream compatibility plan authorizes it.
- Do not remove existing `AI says` support; existing packages and review dashboards must remain parseable.
- Do not treat a single fixed example line as the only allowed runtime LLM response for new packages.
- Do not let runtime behavior contracts become vague. They must preserve source frame, required content, branch behavior, safety/product constraints, and screen/state expectations.
- Do not commit Chinese source prose into generated package content or audit fields; paraphrase source intent in English for generated artifacts.
- Do not claim the source-intent audit is product signoff. It is structured review input for product/curriculum approval.
- Do not hand-edit generated HTML as source of truth; fix scripts, audit YAML, package files, or source manifests and regenerate.
- Do not touch `.env`, secrets, credentials, production data, or machine-specific config.
- Preserve existing user changes and avoid broad formatting/refactor sweeps.

## Required Scope

Implement the source plan and include these major work areas:

- source-intent audit schema and validation in `scripts/generate_source_comparison_review.py`;
- focused tests in `tests/test_source_comparison_review.py`;
- full audit file at `runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml`;
- regenerated source comparison page at `runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html`;
- source-promise alignment contract updates in `program.md`, `run.md`, `GOAL.md`, `templates.md`, and `runs/README.md`;
- runtime behavior contract parsing in `scripts/generate_run_review.py`;
- focused parser/dashboard tests in `tests/test_generate_run_review.py`;
- review dashboard contract updates in `review_dashboard.md`;
- targeted repairs or explicit unresolved findings for:
  - `runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide/`;
  - `runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe/`;
- run provenance and handoff updates in `runs/20260512_172135_batch5_unblocked/run_manifest.yaml` and `HANDOFF.md`.

## Known Findings To Preserve

The implementation must carry these known review findings into the audit:

- `concept_career_decision_decide`: original source is role-play-first, where the child assumes a profession and then faces a work scenario. The generated package is scenario-first and asks the child to choose which helper/profession fits. This is high-severity intent drift unless repaired or explicitly product-approved.
- `concept_story_unlock_probe`: original source is story-first, where the AI tells a story, pauses, asks for a quick challenge, then unlocks the next story beat. The generated package has story-themed choices but does not actually tell a story before the challenge. This is high-severity intent drift unless repaired or explicitly product-approved.

## Preconditions

Before implementation:

- Confirm the source plan exists:

```bash
test -f docs/plans/2026-05-21-source-intent-runtime-contract.md
```

- Confirm the current review generator and run artifacts exist:

```bash
test -f scripts/generate_source_comparison_review.py
test -f scripts/generate_run_review.py
test -f runs/20260512_172135_batch5_unblocked/run_manifest.yaml
test -f runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html
```

- Confirm worktree state and avoid unrelated changes:

```bash
git status --short
```

## Success Criteria

### Source Intent Audit

- `source_intent_audit.yaml` exists with exactly 40 entries.
- Every entry has `source_row`, `activity_id`, `original_play_frame`, `generated_play_frame`, `preserved`, `drift`, `status`, `severity`, `recommendation`, and `product_review_question`.
- Status is one of `aligned`, `minor_adaptation`, `intent_drift`, or `needs_product_decision`.
- Severity is one of `none`, `low`, `medium`, or `high`.
- Generator validation fails on missing audit coverage, invalid status values, or audit/package activity ID disagreement.
- The product review matrix renders an `Intent alignment` column and intent-drift filters.

### Future Generation Contract

- `program.md`, `run.md`, and `GOAL.md` require source-promise alignment review.
- The contract says the original source design controls over a lossy normalized paraphrase when they conflict.
- Phase 0 or the adaptation brief captures original play frame, child role, interaction sequence, required child actions, non-negotiable elements, allowed V1 adaptations, and product dependencies.
- Reviewer agents must fail packages where category/mechanic are preserved but the source play frame materially changes without explicit product approval.

### Runtime Beat Contract

- Existing `AI says` beats still parse and render.
- New `Runtime AI instruction` and `Example AI line` beats parse and render.
- `AI follow-up policy` is accepted as the new equivalent of existing `AI follow-up`.
- `Screen/state` is accepted as the new equivalent of existing `Screen`.
- Review dashboards show whether a beat is exact dialogue or a runtime behavior contract plus example line.

### High-Severity Drift Handling

- Career Decision and Story Challenge Unlock are either repaired or explicitly remain high-severity product-review findings.
- If repaired, package runtime beats preserve the original source frame:
  - Career Decision is profession role-play first, scenario second;
  - Story Challenge Unlock tells a story beat, pauses, asks for a challenge, and unlocks the next story beat.
- Regenerated `review.html` and `product_review_matrix.html` reflect the repaired or unresolved status.

## Required Checks

Minimum final checks:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m py_compile scripts/generate_source_comparison_review.py scripts/generate_run_review.py
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest discover -s tests -v
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml --validate
git diff --check
git status --short
```

Also run generation commands before validation:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml
```

Run a targeted documentation scan:

```bash
rg -n "source-promise alignment|original play frame|child role|interaction sequence|runtime behavior contract|Example AI line|intent_drift" program.md run.md GOAL.md templates.md runs/README.md review_dashboard.md
```

## Commit Expectations

Use small conventional commits after focused checks pass. Recommended grouping:

- `feat(review): add intent audit support`
- `chore(review): add source intent audit`
- `docs(program): require source intent checks`
- `feat(review): parse runtime contracts`
- `fix(activities): restore source intent`
- `chore(run): record intent audit`

If a different grouping is more practical during execution, keep commits focused and ensure unrelated files are not staged.

## Final Completion Gate

Do not mark achieved until:

- source plan requirements are implemented or explicitly deferred with rationale;
- `source_intent_audit.yaml` covers all 40 workbook rows;
- source comparison validation passes with the audit file;
- run review dashboard validation passes;
- all local unittest tests pass;
- focused docs scans pass;
- `git diff --check` passes;
- code simplification and review passes have been performed or documented as not applicable;
- `codex-review` reports no accepted/actionable findings, or unavailability is documented with alternate review evidence;
- `HANDOFF.md` and run manifest record outputs, checks, residual risk, and remaining product decisions;
- only intended files are changed and committed;
- no secrets or new machine-specific paths are introduced into committed source files.

Final response must include:

- files and directories changed;
- audit summary counts by status;
- whether Career Decision and Story Challenge Unlock were repaired or remain product-review findings;
- checks run and results;
- review status;
- residual risks, especially that intent alignment remains human/product review input;
- commit hashes created during execution.
