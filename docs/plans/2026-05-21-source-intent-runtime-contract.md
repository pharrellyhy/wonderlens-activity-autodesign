# Source Intent And Runtime Contract Implementation Plan

> **For implementer:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Add a full source-intent audit layer for Batch 5 and update future generation rules so generated packages preserve the original play frame while runtime AI beats become constrained behavior contracts with example dialogue.

**Architecture:** Keep the existing activity package format stable, but add two review/generation guardrails. First, extend the source comparison workflow with a run-local intent audit file that compares each original workbook design against the generated `prod.md` runtime beats. Second, update the authoring contract so future `prod.md` beats can carry a runtime behavior instruction plus an example AI line, instead of treating a single fixed line as the whole runtime response.

**Python environment:** Script commands require PyYAML. In this local worktree, run them through the PyYAML-capable pyenv interpreter:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3
```

**Tech Stack:** Python 3 standard library, PyYAML, existing Markdown/YAML package files, static self-contained HTML review pages, unittest.

---

## Context

The current Batch 5 source comparison page proves that all 40 workbook rows are covered, but it only classifies category/mechanic/capability drift. It does not reliably catch source-intent drift where the generated package preserves the mechanic token but changes the play frame.

Two confirmed examples:

- `concept_career_decision_decide`: original design starts with role assumption, roughly "assume you are a profession, then encounter a concrete work scenario." The generated package starts with a scenario and asks the child which profession/helper fits. Mechanic `decide` is preserved, but the child role and sequence drift.
- `concept_story_unlock_probe`: original design is story-first: tell a story, pause, ask the child to complete a small challenge, then unlock the next story beat. The generated package has story-themed choices and an unlock shell, but does not actually tell a story before the challenge.

The current `program.md` contract says `AI says` lines must be actual dialogue. That remains useful for reviewer concreteness, but a live LLM runtime should not be forced to reuse a fixed line verbatim. Future packages should include:

- a **runtime behavior contract** describing what the LLM must accomplish and preserve;
- a concrete **example AI line** showing tone and acceptable wording;
- branch policy, screen/state behavior, and source-promise constraints.

This plan should be implemented before generating more source-concept packages or asking product to sign off on Batch 5 source fidelity.

## Design Choice

Use a run-local source-intent audit file plus generator support.

Approaches considered:

- Rely only on the existing comparison page. This is insufficient because category and mechanic can match while the child role, sequence, or story frame changes.
- Try to infer all intent drift automatically from text similarity. This is not reliable enough for product review and risks false confidence.
- Add a structured human-readable audit file and have scripts validate/render it. This is recommended because it keeps the judgment explicit, reviewable, and reusable by the HTML page.

Use this audit file:

```text
runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml
```

The comparison generator should read this file when present and render intent-alignment status in `product_review_matrix.html`.

## Source Intent Audit Schema

Create `source_intent_audit.yaml` with this shape:

```yaml
run_id: 20260512_172135_batch5_unblocked
artifact_kind: source_intent_audit
source_workbook: "活动库内部初版.xlsx"
created_at: "2026-05-21T00:00:00+08:00"
reviewer: codex
status_values:
  - aligned
  - minor_adaptation
  - intent_drift
  - needs_product_decision
summary:
  source_rows: 40
  aligned: 0
  minor_adaptation: 0
  intent_drift: 0
  needs_product_decision: 0
entries:
  - source_row: 26
    activity_id: concept_career_decision_decide
    original_play_frame: "Role-play starts by assuming a profession, then the child faces a concrete work scenario."
    generated_play_frame: "Scenario is presented first, then the child chooses which helper/profession fits."
    preserved:
      - "Decision mechanic"
      - "Career/helper domain"
      - "Simple work-related situation"
    drift:
      - "Child role changes from acting as the professional to selecting the professional."
      - "Source sequence changes from profession-first to scenario-first."
    status: intent_drift
    severity: high
    recommendation: "Revise runtime beats so the child first becomes a named professional, then chooses what to do in that role when the scenario appears."
    product_review_question: "Should Career Decision be role-play-first as in the workbook, or is scenario-to-profession matching acceptable?"
```

Rules:

- Exactly one entry per workbook row.
- `source_row` must match the original workbook row index used by `source_activity_concepts.md`.
- `activity_id` must match the generated package where coverage exists.
- `status` must be one of the declared `status_values`.
- `severity` must be `none`, `low`, `medium`, or `high`.
- `original_play_frame`, `generated_play_frame`, and `recommendation` must be English. Do not commit Chinese source prose into generated artifacts; paraphrase it in English.
- `intent_drift` means the package may preserve category/mechanic but changes the source's role, sequence, story frame, or required child action enough that product should explicitly approve or request repair.

## Runtime Beat Contract Shape

Keep `prod.md` backward-compatible with existing parsers, but allow richer future beats.

Preferred future format:

```markdown
**Runtime AI instruction:** Tell a short story beat first: the character reaches a locked moon gate while carrying a tiny lantern. Pause before the gate opens. Ask the child to complete one small challenge to unlock the next story beat. Do not skip the story setup.

**Example AI line:** [mysterious story tone] "The little fox reaches a silver moon gate. It will only open if we help. Can you say a tiny moon word to unlock the next part?"

**Child responses:**

1. (Ideal) ...
2. (Unexpected) ...
3. (No response) ...

**AI follow-up policy:**

1. ...
2. ...
3. ...

**Screen/state:** ...
```

Backward-compatible rules:

- Existing `**AI says:**` remains valid for older packages.
- New packages may use `**Runtime AI instruction:**` plus `**Example AI line:**`.
- Review dashboards and validators must parse both shapes.
- The example line is not necessarily a fixed runtime response; it is a concrete sample that constrains tone, content, and source frame.
- Safety-critical instructions, fallback warnings, and product contract constraints must remain explicit and should not be left solely to runtime improvisation.

## Task 1: Add Tests For Source Intent Audit Loading

**Files:**

- Modify: `tests/test_source_comparison_review.py`
- Modify: `scripts/generate_source_comparison_review.py`

**Step 1: Write failing tests**

Add tests that build a small fixture with three workbook rows, generated package entries, and a `source_comparison/source_intent_audit.yaml`.

Test requirements:

- `build_report(..., intent_audit_path=...)` loads audit entries by `source_row`.
- Rendered HTML includes `Intent alignment`, `intent_drift`, and the row recommendation.
- Validation fails when the audit has missing row coverage.
- Validation fails when `status` is not in the allowed enum.
- Validation fails when the audit row's `activity_id` disagrees with the generated package for that source row.

**Step 2: Run the new focused test and confirm failure**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest tests/test_source_comparison_review.py -v
```

Expected: FAIL because the generator does not yet support source intent audit loading or rendering.

**Step 3: Implement minimal audit support**

In `scripts/generate_source_comparison_review.py`:

- Add `load_intent_audit(path: Path) -> dict[int, dict[str, Any]]`.
- Add `validate_intent_audit(report: dict[str, Any], audit: dict[int, dict[str, Any]]) -> list[str]`.
- Add optional CLI argument:

```bash
--intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml
```

- Add row fields:
  - `intent_status`
  - `intent_severity`
  - `original_play_frame`
  - `generated_play_frame`
  - `intent_recommendation`
  - `intent_review_question`
- Render a new table column: `Intent alignment`.
- Add a top-level metric for `Intent drift`.
- Add filter buttons for `Intent drift` and `Needs product decision`.

**Step 4: Run focused tests**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest tests/test_source_comparison_review.py -v
```

Expected: PASS.

**Step 5: Commit**

```bash
git add scripts/generate_source_comparison_review.py tests/test_source_comparison_review.py
git commit -m "feat(review): add intent audit support"
```

## Task 2: Create The Full Batch 5 Source Intent Audit

**Files:**

- Create: `runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml`
- Modify: `runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html`
- Modify: `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`
- Modify: `HANDOFF.md`

**Step 1: Generate an audit worksheet draft**

Use the generator or a small helper inside `scripts/generate_source_comparison_review.py` to print row-level audit scaffolding from:

- `/Users/pharrelly/Downloads/活动库内部初版.xlsx`
- `inputs/source_activity_concepts.md`
- `runs/20260512_172135_batch5_unblocked/activity_packages/*/prod.md`
- `runs/20260512_172135_batch5_unblocked/adaptation_briefs/*.yaml`

The scaffold should include source row, activity ID, workbook activity name, original source description, generated title, and generated typical scenario/core loop.

**Step 2: Fill the audit manually**

Inspect all 40 rows. For each row, compare the original workbook intent against the generated runtime beats.

Classify:

- `aligned`: core play frame, child role, sequence, and repeated action are preserved.
- `minor_adaptation`: changes are acceptable V1 adaptations and do not invert the source promise.
- `intent_drift`: category/mechanic may be preserved, but role, sequence, story frame, or child action changes materially.
- `needs_product_decision`: product support determines whether the generated version is acceptable.

At minimum, include these known findings:

- `concept_career_decision_decide`: `intent_drift`, high severity, role-play-first source became scenario-to-profession matching.
- `concept_story_unlock_probe`: `intent_drift`, high severity, story-first challenge unlock became a generic door/path choice loop without a real story beat before the challenge.

**Step 3: Validate the audit**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml --validate
```

Expected: PASS with 40 source rows, 40 covered, and nonzero intent drift count.

**Step 4: Regenerate the product review matrix**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml
```

Expected output:

```text
runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html
```

**Step 5: Static scan the generated page**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 - <<'PY'
from pathlib import Path
import re
p = Path('runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html')
text = p.read_text(errors='replace')
issues = []
if '/Users/' in text:
    issues.append('local path leaked')
if '{{' in text or '}}' in text:
    issues.append('unresolved template marker')
if re.search(r'(?:src|href)=["\\']https?://', text, re.I):
    issues.append('external link or image')
if text.count('<tr data-status=') != 40:
    issues.append('wrong row count')
if 'Intent alignment' not in text:
    issues.append('missing intent alignment column')
if 'concept_career_decision_decide' not in text or 'concept_story_unlock_probe' not in text:
    issues.append('known findings missing')
if issues:
    print('FAIL')
    for issue in issues:
        print('-', issue)
    raise SystemExit(1)
print('PASS source intent review page scan')
PY
```

Expected: PASS.

**Step 6: Update run provenance**

Update `run_manifest.yaml`:

- `outputs.source_intent_audit`
- check entries for audit validation and static scan
- note that the source comparison page now includes source-intent alignment review

Update `HANDOFF.md` with current status, findings summary, checks, and residual risks.

**Step 7: Commit**

```bash
git add runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html runs/20260512_172135_batch5_unblocked/run_manifest.yaml HANDOFF.md
git commit -m "chore(review): add source intent audit"
```

## Task 3: Update Generation Contracts For Source-Promise Alignment

**Files:**

- Modify: `program.md`
- Modify: `run.md`
- Modify: `GOAL.md`
- Modify: `templates.md`
- Modify: `runs/README.md`

**Step 1: Add doc tests or targeted scans**

Add a focused validation command to check required phrases after docs are edited:

```bash
rg -n "source-promise alignment|original play frame|child role|interaction sequence|runtime behavior contract|example AI line|intent drift" program.md run.md GOAL.md templates.md runs/README.md
```

Before edits, expected: missing or incomplete coverage.

**Step 2: Update `program.md`**

Add a new source-promise alignment rule near the Phase 0 / generation contract:

- The original source design controls over a lossy normalized paraphrase when they conflict.
- Phase 0 must extract a `source_promise_contract` with:
  - `original_play_frame`
  - `child_role`
  - `interaction_sequence`
  - `required_child_actions`
  - `non_negotiable_elements`
  - `allowed_v1_adaptations`
  - `known_product_dependencies`
- A generated package fails review if it preserves mechanic/category but materially changes the play frame without explicit product approval.

Update the runtime dialogue section:

- Existing `AI says` remains valid as exact example dialogue.
- Future beats may use `Runtime AI instruction` plus `Example AI line`.
- `Runtime AI instruction` must describe what the LLM should do at runtime, including source frame, required content, branch behavior, and safety/product constraints.
- `Example AI line` must remain concrete, age-appropriate, and aligned with the instruction.

**Step 3: Update `run.md`**

Add steps to the Phase 0 and review workflow:

- During adaptation brief creation, compare the original source row/workbook design against the normalized source concept and capture any nuance lost in normalization.
- Before package generation, write or confirm `source_promise_contract`.
- During self-review and reviewer-agent review, explicitly compare `prod.md` runtime beats to `source_promise_contract`.
- If a generated package changes the play frame, record `intent_drift` and either repair the package or ask for product approval before marking PASS.

**Step 4: Update `GOAL.md`**

Add goal success criteria:

- Every generated package preserves original play frame, child role, interaction sequence, and required child action unless `run_manifest.yaml` records an explicit product-approved adaptation.
- Reviewer agents must fail "mechanic preserved but source frame changed" packages.
- Source comparison review should include an intent-alignment layer when the run is based on workbook/source concept rows.

**Step 5: Update `templates.md`**

Add a short note in the mechanic adapter self-check:

- Mechanic adapter selection does not permit inversion of the source frame.
- Examples:
  - career role-play must not become profession classification unless approved;
  - story challenge unlock must tell a story beat before asking for unlock challenge;
  - photo-hunt source must not become purely voice-only unless the adaptation is explicitly recorded.

**Step 6: Update `runs/README.md`**

Document `source_intent_audit.yaml` under `source_comparison/`.

**Step 7: Run doc checks**

Run:

```bash
rg -n "source-promise alignment|original play frame|child role|interaction sequence|runtime behavior contract|Example AI line|intent_drift" program.md run.md GOAL.md templates.md runs/README.md
git diff --check
```

Expected: required phrases present; diff check clean.

**Step 8: Commit**

```bash
git add program.md run.md GOAL.md templates.md runs/README.md
git commit -m "docs(program): require source intent checks"
```

## Task 4: Update Runtime Beat Parsing For Behavior Contracts

**Files:**

- Modify: `scripts/generate_run_review.py`
- Modify: `tests/test_generate_run_review.py`
- Modify: `review_dashboard.md`

**Step 1: Write failing regression tests**

Add a test fixture or direct parser test showing that a runtime beat using:

```markdown
**Runtime AI instruction:** ...
**Example AI line:** ...
**AI follow-up policy:** ...
**Screen/state:** ...
```

is parsed into the runtime beat map.

Expected assertions:

- HTML contains `Runtime AI instruction`.
- HTML contains `Example AI line`.
- HTML preserves branch chips.
- HTML preserves screen/state text.
- Existing `AI says` packages still parse and render.

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest tests/test_generate_run_review.py -v
```

Expected: FAIL until parser supports the new labels.

**Step 2: Implement parser support**

Update `scripts/generate_run_review.py`:

- Recognize `Runtime AI instruction` as `ai_instruction`.
- Recognize `Example AI line` as `ai_example`.
- Recognize `AI follow-up policy` as equivalent to existing `AI follow-up`.
- Recognize `Screen/state` as equivalent to existing `Screen`.
- Keep existing `AI says` support untouched.

Update runtime map rendering:

- If `ai_instruction` exists, show it as the primary runtime contract.
- If `ai_example` exists, show it as the example line.
- If only `AI says` exists, show the existing AI prompt lane.

**Step 3: Update dashboard contract docs**

Update `review_dashboard.md` so runtime beat maps must show either:

- exact `AI says`; or
- runtime behavior instruction plus example AI line.

**Step 4: Run tests**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest tests/test_generate_run_review.py -v
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest discover -s tests -v
```

Expected: PASS.

**Step 5: Commit**

```bash
git add scripts/generate_run_review.py tests/test_generate_run_review.py review_dashboard.md
git commit -m "feat(review): parse runtime contracts"
```

## Task 5: Repair Confirmed High-Severity Drift Packages

**Files:**

- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide/spec.md`
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide/prod.md`
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide/recap.template.yaml` if wording no longer matches
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide/dashboard.template.yaml` if wording no longer matches
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe/spec.md`
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe/prod.md`
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe/recap.template.yaml` if wording no longer matches
- Modify: `runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe/dashboard.template.yaml` if wording no longer matches
- Modify: `runs/20260512_172135_batch5_unblocked/review.html`
- Modify: `runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml`
- Modify: `runs/20260512_172135_batch5_unblocked/source_comparison/product_review_matrix.html`

**Step 1: Write or update validation expectations**

Add assertions to source-comparison tests or a new focused test that known repaired rows can move from `intent_drift` to `aligned` or `minor_adaptation` only when `source_intent_audit.yaml` is updated with a repair note.

**Step 2: Repair Career Decision**

Revise the package so:

- Step 1 makes the child assume a specific profession or choose a profession before the scenario.
- Step 2 explains the role-play rule: "You are the [profession]. Listen to what happens at work, then choose what you do."
- Step 3 rounds keep `decide`, but decisions are made from inside the role:
  - decide the first responsible action;
  - decide which tool the professional uses;
  - decide what to say/do next in the scenario.
- The package no longer asks the child to classify which profession matches a scenario as the primary loop.

Use runtime behavior contract format plus example lines where appropriate.

**Step 3: Repair Story Challenge Unlock**

Revise the package so:

- Each challenge round starts with an actual short story beat.
- The story pauses before the challenge.
- The child completes a simple challenge to unlock the next story beat.
- Challenge examples can include:
  - say a magic word;
  - find or name an object with a target color;
  - imitate a safe animal sound;
  - repeat a simple word.
- The unlock payoff is a continuation of the story, not a generic progress badge.
- UI state remains documented as product-dependent with fallback language.

Use runtime behavior contract format plus example lines where appropriate.

**Step 4: Regenerate review artifacts**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml --validate
```

**Step 5: Run focused checks**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest discover -s tests -v
git diff --check
```

Expected: PASS.

**Step 6: Commit**

```bash
git add runs/20260512_172135_batch5_unblocked/activity_packages/concept_career_decision_decide runs/20260512_172135_batch5_unblocked/activity_packages/concept_story_unlock_probe runs/20260512_172135_batch5_unblocked/review.html runs/20260512_172135_batch5_unblocked/source_comparison tests
git commit -m "fix(activities): restore source intent"
```

## Task 6: Final Review And Handoff

**Files:**

- Modify: `HANDOFF.md`
- Modify: `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`

**Step 1: Run final checks**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m py_compile scripts/generate_source_comparison_review.py scripts/generate_run_review.py
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m unittest discover -s tests -v
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_source_comparison_review.py runs/20260512_172135_batch5_unblocked --workbook /Users/pharrelly/Downloads/活动库内部初版.xlsx --intent-audit runs/20260512_172135_batch5_unblocked/source_comparison/source_intent_audit.yaml --validate
git diff --check
git status --short
```

Expected: all checks pass; only intended files changed before commit.

**Step 2: Run review gates**

Run `code-simplifier` on changed implementation scripts if available and useful.

Run a fresh code review pass:

- Use `superpowers:requesting-code-review` or an equivalent independent review.
- Run `codex-review` if installed.
- If `codex-review` is unavailable, record the blocker and the alternate review performed in `HANDOFF.md`.

**Step 3: Update handoff**

`HANDOFF.md` should record:

- full 40-row source intent audit completed;
- count of `aligned`, `minor_adaptation`, `intent_drift`, and `needs_product_decision`;
- repaired packages;
- remaining product decisions;
- validation commands and results;
- residual risk that intent audit contains human judgment and should be product-reviewed.

`run_manifest.yaml` should record:

- `outputs.source_intent_audit`;
- final source comparison validation command;
- final run review validation command;
- full test command.

**Step 4: Final commit**

```bash
git add HANDOFF.md runs/20260512_172135_batch5_unblocked/run_manifest.yaml
git commit -m "chore(run): record intent audit"
```

## Final Success Criteria

The implementation is complete when:

- `source_intent_audit.yaml` has exactly 40 entries.
- `product_review_matrix.html` displays source intent alignment for every row.
- Career Decision and Story Challenge Unlock are either repaired or explicitly recorded as unresolved high-severity product-review items.
- `program.md`, `run.md`, and `GOAL.md` require source-promise alignment checks for future generation.
- Runtime beat parsing supports both old `AI says` and new runtime behavior contract / example line shape.
- Review dashboard validation passes.
- Source comparison validation passes.
- All local unittest tests pass.
- `git diff --check` passes.
- Changes are committed with conventional commit messages.

## Explicit Non-Goals

- Do not generate remaining prebuilt assets.
- Do not rewrite all 40 packages unless the audit identifies necessary repairs.
- Do not change tag-block enum values or activity IDs.
- Do not change downstream runtime code in other repos.
- Do not remove existing `AI says` support; existing packages must remain parseable.
- Do not claim intent audit is product signoff. It is a structured review input for product/curriculum approval.
