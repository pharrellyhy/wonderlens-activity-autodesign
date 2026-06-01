# WonderLens AI Dialogue Repair Evidence

Run: `20260601_155917_full_pass_agentic_tsv`

Date: 2026-06-01

## Scope

- Repaired runtime-facing dialogue in 29 `activity_packages/*/prod.md` files.
- Left `spec.md`, manifests, assets, source audits, downstream repos, and `visual_reference_reviews/image_quality_reaudit*` untouched.
- Added this evidence file and `wonderlens_ai_dialogue_repair.yaml`.

## Leakage Counts

| Phrase | Before | After |
|---|---:|---:|
| `Open from the source trigger` | 29 | 0 |
| `I found a small mission` | 29 | 0 |
| `Rule: I prompt` | 29 | 0 |
| `source-intent cue` | 89 | 0 |
| `current prompt` | 32 | 0 |
| `What is your first try` | 23 | 0 |
| `What did we make` | 23 | 0 |
| `Your turns made the board light up` | 29 | 0 |
| `RESOLVED BLOCKER` | 0 | 0 |
| `RESOLVE BLOCKER` | 0 | 0 |

Total rejected phrase hits: 283 before, 0 after.

## Repair Pattern

- Replaced generic opening lines with each activity name, child role, and first source-specific turn.
- Replaced generic rule examples with activity-specific cue wording and preserved token-saving behavior.
- Replaced generic screen cue labels with activity-specific cues while preserving asset and fallback guardrails.
- Replaced generic first-try, recap, and finish examples with activity-specific action language.

## Validation Commands

```bash
if rg -n "Open from the source trigger|I found a small mission|Rule: I prompt|source-intent cue|current prompt|What is your first try|What did we make|Your turns made the board light up|RESOLVED BLOCKER|RESOLVE BLOCKER" runs/20260601_155917_full_pass_agentic_tsv/activity_packages/*/prod.md; then exit 1; else echo no_runtime_leakage; fi
```

Output:

```text
no_runtime_leakage
```

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_demo_package_contract.py runs/20260601_155917_full_pass_agentic_tsv/activity_packages
```

Output:

```text
OK demo package contract: 40 package(s)
```

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai && rm -rf .artifacts/full-pass-agentic && mkdir -p .artifacts/full-pass-agentic && uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/full-pass-agentic-run/runs/20260601_155917_full_pass_agentic_tsv/activity_packages --dest .artifacts/full-pass-agentic/activities --write --force --report-json .artifacts/full-pass-agentic/runtime-report.json
```

Output summary:

```text
40 package(s) generated; each package reported warnings=0.
```

`git diff --check` is recorded in the YAML evidence and final validation output.

## Residual Risk

- This repair only removes the listed leakage phrases and restores source-specific runtime wording; it does not perform a new full dialogue quality audit.
- The WonderLens AI validation command wrote only the requested `.artifacts/full-pass-agentic` validation output in the downstream repo.
