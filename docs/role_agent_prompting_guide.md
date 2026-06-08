# Role Agent Prompting Guide

Use this guide with `docs/full_pass_agentic_parallel_workflow.html` when several
people run coding agents against the same full-pass run branch.

Root `GOAL.md`, `run.md`, and `program.md` remain the canonical generation
contract. This file is only for role-scoped contributor prompts: what to ask the
agent, what files it may touch, what evidence it must produce, and when it must
stop.

## Core Rule

Every agent prompt should include one role, one branch, one package slice, and
an explicit forbidden scope.

```text
You are the <role> for run <run_id>.
Work only on <paths>.
Goal: <specific outcome>.
Allowed files: <files>.
Forbidden files: <files>.
Update runs/<run_id>/review_status/<activity_id>.yaml.
Run <validators>.
Commit only intended files.
Stop if <blocker>.
```

Avoid prompts such as "fix whatever fails" or "make the activity pass." Those
prompts erase ownership boundaries and make review evidence hard to trust.

## Branch Rules

- Branch from the latest run integration branch, such as
  `run/202606xx-agentic-pass`.
- Use one contributor branch per role slice, such as
  `alice/text-activities-01-05` or `bob/assets-activity-vegetable-sort`.
- Do not let two agents edit the same package or manifest at the same time.
- Sync before PR with `git fetch origin`, rebase onto the run branch, then run
  `git diff --check`.
- The integration owner routes failures by owner. They should not silently fix
  package text, assets, and downstream code in the same PR.

## Run Captain Prompt

Use this when creating or refreshing the baseline run output.

```text
You are the run captain for run <run_id>.
Work from the wonderlens-activity-autodesign repo root.
Execute the scoped full-pass goal:
/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.

Scope:
- Generate the baseline activity packages for the selected assignment set.
- Write run_manifest.yaml, generated_activity_ids.txt, review.html, and review_status files when supported.
- Keep asset_build and demo_export flags recorded in run_manifest.yaml.

Allowed files:
- runs/<run_id>/**
- results.tsv only if the goal explicitly requires logging after reviewer PASS evidence.

Forbidden files:
- Downstream app repos.
- Unrelated canonical docs.
- Unassigned activity packages from older runs.

Validation:
- Run the validators required by the goal file.
- Run git diff --check.

Commit only the intended baseline run output.
Stop if assignment scope, credentials, source files, or goal constraints are ambiguous.
```

## Text Reviewer Prompt

Use this for package text, runtime beats, and YAML alignment.

```text
You are the text reviewer for run <run_id>.
Review only runs/<run_id>/activity_packages/<activity_id>.

Goal:
- Verify spec.md, prod.md, tag_block.yaml, demo_support.yaml, recap.template.yaml, and dashboard.template.yaml describe the same activity.
- Improve runtime beat quality, step instructions, parameterization, entity binding, and demo support metadata if needed.
- Preserve child-facing tone and age-appropriate interaction.

Allowed files:
- runs/<run_id>/activity_packages/<activity_id>/spec.md
- runs/<run_id>/activity_packages/<activity_id>/prod.md
- runs/<run_id>/activity_packages/<activity_id>/tag_block.yaml
- runs/<run_id>/activity_packages/<activity_id>/demo_support.yaml
- runs/<run_id>/activity_packages/<activity_id>/recap.template.yaml
- runs/<run_id>/activity_packages/<activity_id>/dashboard.template.yaml
- runs/<run_id>/review_status/<activity_id>.yaml

Forbidden files:
- assets/**
- generated_assets/**
- downstream app repos
- unrelated activity packages

Validation:
- python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages/<activity_id>
- git diff --check

Update review_status with evidence, owner, next_owner, and remaining risks.
Stop if the activity needs new visual assets, unsupported UI capability, or product decisions.
```

## Asset Curator Prompt

Use this for illustrative PNG generation, reference curation, package-local
asset outputs, and asset QA evidence.

```text
You are the asset curator for run <run_id>.
Work only on assets for runs/<run_id>/activity_packages/<activity_id>.

Goal:
- Use asset_manifest.yaml as the source of truth.
- Generate or curate source images for every required runtime asset.
- Preserve the WonderLens flat Nordic style, round-screen fit, and package-local output paths.
- Reject fake reference-bound assets.

Allowed files:
- runs/<run_id>/activity_packages/<activity_id>/asset_manifest.yaml
- runs/<run_id>/activity_packages/<activity_id>/assets/**
- runs/<run_id>/generated_assets/**
- runs/<run_id>/review_status/<activity_id>.yaml

Forbidden files:
- prod.md mechanics or dialogue
- spec.md activity design, except clearly scoped asset brief path corrections
- downstream app repos
- unrelated activity packages

Validation:
- python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
- python3 scripts/validate_asset_build_outputs.py runs/<run_id>
- git diff --check

For reference-bound assets, store approved source originals and metadata under
package-local assets/sources. For illustrative assets, use Codex imagegen when
available or the configured Gemini provider described in
docs/image_generation_provider_setup.md.

Update review_status with generated paths, rejected candidates, source evidence,
and final QA status. Stop if credentials, license, reference fidelity, or image
quality is uncertain.
```

## Integration Owner Prompt

Use this only after package and asset gates pass.

```text
You are the integration owner for run <run_id>.
Test downstream behavior for runs/<run_id>/activity_packages/<activity_id>.

Goal:
- Import or load the package in wonderlens-activity-fullstack-demo when available.
- Load or convert the package in wonderlens-ai when available.
- Compare runtime behavior against prod.md, demo_support.yaml, and asset_manifest.yaml.
- Route failures to package, image, fullstack-demo, WonderLens AI, or product capability.

Allowed files:
- Runs evidence files and review_status for <activity_id>.
- Downstream test logs or fixtures only when the corresponding repo is part of the task.

Forbidden files:
- Silent package repair in the same PR as downstream runtime repair.
- New product behavior not declared by the package.
- Broad downstream refactors.

Validation:
- Run the narrowest available fullstack-demo import/runtime check.
- Run the narrowest available WonderLens AI load/runtime check.
- Capture transcript or screenshot evidence when UI or dialogue quality is being judged.
- git diff --check in every touched repo.

Update review_status with pass/fail evidence and next owner.
Stop if downstream access, credentials, or required local servers are unavailable.
```

## Status Rules

Each activity should have:

```text
runs/<run_id>/review_status/<activity_id>.yaml
```

Use `runs/_templates/review_status.yaml` when creating a new status file. Keep
statuses limited to `pending`, `pass`, `needs_fix`, `blocked`, or
`not_applicable`.

Every status update should record:

- Current owner.
- Next owner, if blocked or failed.
- Commands or manual checks run.
- Evidence paths, transcript paths, source paths, or screenshot paths.
- Residual risk in one or two concrete sentences.

## Stop Conditions

Ask the human owner before continuing when:

- A prompt would touch secrets, credentials, or machine-specific configuration.
- A reference-bound asset lacks an approved source.
- An activity needs an unsupported mechanic or UI capability.
- Multiple contributors need to edit the same file.
- A validator fails for a reason outside the role scope.
- Downstream consumer behavior contradicts the package contract.
- The requested fix would change root generation rules instead of only the
  assigned package or run evidence.
