# Integrated Assets HTML Export Goal

## Goal File Role

This file is the concise Codex goal-mode execution contract for integrating the 12 generated prebuilt asset sets and exporting the corresponding 12 activity HTML files.

Detailed implementation lives in:

- Source of truth: `docs/plans/2026-05-20-integrated-assets-html-export.md`
- Supporting contracts: `review_dashboard.md`, `runs/README.md`, `HANDOFF.md`

Use the source plan for implementation details, output paths, validation behavior, and task order. If this goal and the source plan conflict, the source plan controls implementation details, but this goal controls scope, hard constraints, and completion gates.

Source plan version: `2026-05-20`.

Python environment: all script commands require PyYAML. In this local worktree, use the PyYAML-capable pyenv interpreter prefix:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3
```

## Objective

Implement the asset integration and static HTML export workflow for the 12 generated Batch 5 pilot asset sets.

The finished system must:

- create a run-local binding manifest that maps each generated pilot asset to its corresponding activity package;
- export exactly 12 self-contained static HTML activity pages with embedded contact-sheet images;
- update run provenance and workflow docs without changing the canonical five-file activity package contract.

## Recommended `/goal` Command

```text
/goal Execute goals/2026-05-20-integrated-assets-html-export-goal.md end to end. Use docs/plans/2026-05-20-integrated-assets-html-export.md as the controlling implementation plan. Integrate the 12 generated pilot assets, export the 12 self-contained activity HTML files, update run provenance/docs, run all focused validations, commit intended changes only, and report outputs/checks/residual risks.
```

## Required Execution Mode

- This is doc/script/artifact implementation work, not new activity generation.
- Create an implementation worktree from current `main` before code changes unless already in an active feature worktree. Docs-only goal-file edits may remain in the current checkout.
- Use TDD or test-first validation for each behavior change:
  - add validation expectations before or alongside each script implementation;
  - run the validation command and confirm the failing or missing-artifact state before relying on the implementation.
- Use sub-agent-driven implementation when work can be split safely:
  - asset integration script;
  - HTML exporter;
  - docs/provenance wiring and final review.
- Keep sub-agent write ownership disjoint.
- After each major feature group passes focused checks, run `code-simplifier` on changed implementation files when applicable.
- After each major feature group, request code review using `superpowers:requesting-code-review` or an equivalent fresh review pass.
- Before marking complete, run a final review pass until no accepted/actionable findings remain. If `codex-review` is unavailable in the environment, document that blocker and the alternate review performed.
- Use conventional commits and do not push unless explicitly requested.

## Hard Constraints

- Do not modify canonical package IDs, tag-block enums, activity mechanics, pillars, game styles, or vocabulary/schema contracts.
- Do not add asset paths directly into canonical `tag_block.yaml`.
- Do not replace, redesign, or regenerate the 12 existing activity packages.
- Do not generate the remaining assets in this goal.
- Do not slice contact sheets into individual runtime card files in this goal.
- Do not build a live WonderLens runtime simulator.
- Do not hand-edit generated HTML as source of truth; fix scripts or source manifests and regenerate.
- Do not touch `.env`, secrets, credentials, production data, or machine-specific config.
- Keep generated HTML self-contained: no external CSS, JavaScript, fonts, images, or CDN references.
- Preserve existing user changes and avoid broad formatting/refactor sweeps.

## Required Scope

Implement the source plan and include these major work areas:

- asset integration script: `scripts/integrate_generated_assets.py`;
- run-local binding output: `runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml`;
- per-activity HTML exporter: `scripts/export_activity_html.py`;
- 12 self-contained HTML files and `export_manifest.yaml` under `runs/20260512_172135_batch5_unblocked/activity_exports/`;
- run manifest provenance updates in `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`;
- workflow documentation updates in `review_dashboard.md`, `runs/README.md`, and `HANDOFF.md`;
- regenerated and validated run review dashboard when provenance changes require it.

## Inputs

The implementation must use these existing inputs:

- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/asset_manifest.yaml`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/contact_sheet.png`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/asset.meta.yaml`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/contact_sheet.prompt.md`
- `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/spec.md`
- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/prod.md`
- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/tag_block.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/recap.template.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/dashboard.template.yaml`

## Required Activity Set

Exactly these 12 activity/asset pairs are in scope:

| activity_id | asset_id |
|---|---|
| `concept_phoneme_hunt_collect` | `phoneme_letter_card_01` |
| `concept_partial_reveal_deduce` | `partial_reveal_cards_01` |
| `concept_animal_sound_motion_voice` | `animal_sound_cards_01` |
| `concept_word_echo_remember` | `word_echo_cards_01` |
| `concept_emotion_reader_care` | `emotion_expression_cards_01` |
| `concept_constellation_star_count_enumerate` | `constellation_count_cards_01` |
| `concept_career_decision_decide` | `career_portrait_cards_01` |
| `concept_vegetable_sort_sort` | `vegetable_sort_cards_01` |
| `concept_travel_planner_predict` | `travel_planning_cards_01` |
| `concept_guided_drawing_probe` | `guided_drawing_step_cards_01` |
| `concept_story_unlock_probe` | `story_unlock_cards_01` |
| `concept_recognition_pop_probe` | `recognition_challenge_cards_01` |

## Preconditions

Before implementation:

- Confirm the source plan exists:

```bash
test -f docs/plans/2026-05-20-integrated-assets-html-export.md
```

- Confirm the run and asset manifest exist:

```bash
test -f runs/20260512_172135_batch5_unblocked/run_manifest.yaml
test -f runs/20260512_172135_batch5_unblocked/generated_assets_pilot/asset_manifest.yaml
```

- Confirm the pilot has 12 generated images:

```bash
find runs/20260512_172135_batch5_unblocked/generated_assets_pilot -path '*/contact_sheet.png' -type f | wc -l
```

Expected output: `12`.

- Confirm worktree state and avoid including unrelated changes:

```bash
git status --short
```

## Success Criteria

### Asset Integration

- `scripts/integrate_generated_assets.py` exists and supports:
  - `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py runs/20260512_172135_batch5_unblocked`
  - `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/20260512_172135_batch5_unblocked`
- `runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml` exists.
- The binding manifest has exactly 12 entries and 12 distinct `activity_id` values.
- Every binding entry has a real package path, image path, metadata path, and prompt path.
- Every binding entry validates that `spec.md`, `prod.md`, and `run_manifest.yaml` agree on `asset_id`, requiredness, use step, and display location.
- Validation fails on missing files, mismatched asset IDs, or false validation flags.

### HTML Export

- `scripts/export_activity_html.py` exists and supports:
  - `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py runs/20260512_172135_batch5_unblocked`
  - `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/20260512_172135_batch5_unblocked`
- `runs/20260512_172135_batch5_unblocked/activity_exports/export_manifest.yaml` exists.
- Exactly 12 `.html` files exist under `runs/20260512_172135_batch5_unblocked/activity_exports/`.
- Every HTML file embeds its corresponding `contact_sheet.png` as `data:image/png;base64,`.
- Every HTML file includes activity metadata, the integrated asset contract, fallback behavior, runtime flow, scorecard rows, and source snapshots.
- No HTML file references external `http://`, `https://`, CDN, remote font, or remote image resources.
- No HTML file claims to be a live runtime simulator.

### Provenance And Docs

- `runs/20260512_172135_batch5_unblocked/run_manifest.yaml` records:
  - `integrated_asset_bindings`;
  - `activity_html_exports`;
  - `activity_html_export_manifest`;
  - `integrated_asset_count: 12`;
  - `activity_html_export_count: 12`;
  - PASS check entries for integration/export generation and validation.
- `review_dashboard.md` documents the integration/export commands and generated-artifact rule.
- `runs/README.md` documents `integrated_assets/` and `activity_exports/`.
- `HANDOFF.md` records current status, generated outputs, checks, and residual risk.
- If `review.html` is regenerated, it validates with the existing dashboard validator.

## Required Checks

Minimum final checks:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m py_compile scripts/integrate_generated_assets.py scripts/export_activity_html.py scripts/generate_run_review.py
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
git diff --check
git status --short
```

Also run the generation commands before validation:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py runs/20260512_172135_batch5_unblocked
```

## Commit Expectations

Use small conventional commits after focused checks pass:

- `feat(assets): bind pilot assets`
- `feat(exports): add activity HTMLs`
- `chore(run): record asset exports`
- `docs(exports): document activity HTMLs`

If a different grouping is more practical during execution, keep commits small and ensure unrelated files are not staged.

## Final Completion Gate

Do not mark achieved until:

- source plan requirements are implemented or explicitly deferred with rationale;
- all 12 bindings validate;
- all 12 HTML exports validate;
- dashboard validation still passes;
- focused checks pass;
- code simplification and review passes have been performed or documented as not applicable;
- `HANDOFF.md` reflects the new status and residual risk;
- only intended files are changed and committed;
- no secrets or machine-specific paths are introduced into committed source files, except existing run-local generated asset provenance that was already present.

Final response must include:

- files and directories changed;
- exact output paths for binding manifest and 12 HTML exports;
- checks run and results;
- review status;
- residual risks, especially that contact sheets are preview/review assets, not sliced final runtime cards;
- commit hashes created during execution.
