# Run Instructions - Autonomous Activity Package Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.
> When launched from Codex `/goal`, use `GOAL.md` as the objective and success criteria, and use this file as the execution procedure.

## Setup (one-time, do this first)

Entity mapping root: `MAPPING_ROOT=data/mappings_dev20_0318` (repo-relative). Use `MAPPING_ROOT/_index.yaml` as the entity registry whenever mapping data is required.

1. Read `GOAL.md` - goal, assignment type names, and success criteria.
2. Read `program.md` fully - constraints, migrated package format, rubric, and seed exemplars.
3. Read `templates.md` fully - Template 0 reference, mechanic adapters, Cat1/Cat5 category modifiers, and pillar/style scaffolds.
4. Read `docs/game_styles.md` - game style taxonomy reference.
5. Read `activities/README.md` - required five-file package layout.
6. Read `activities/_schema/tag_block.schema.json` and `docs/activity_vocabulary.md` - tag-block schema and current enum vocabulary.
7. Read `docs/activity_tag_block_usage.md` and `docs/activity_tag_block_progression_guide.md` - field ownership, recap/dashboard usage, and progression guidance.
8. Read `entity_guidance.md` and `conversation_bridge.md` when an assignment is mapping-informed or requests warm/cold bridge handling.
9. Read `assignments.md` - work queue.
10. Verify `activities/` exists with `_schema/tag_block.schema.json`.
11. Verify `results.tsv` exists and has the current header. If it is missing, create it with this header:

```
assignment	entity	category	tier	pillar	style	status	d1_tech	d2_hook_transition	d3_edge	d4_ib	d5_tier	d6_dialogue	d7_screen	d8_mapping	d9_game_feel	d10_pillar_fidelity	filename	timestamp
```

12. Create a run provenance directory before processing the first assignment:

```
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── adaptation_briefs/
├── blocked_briefs/
├── blocked_designs/
├── review_notes.md
└── review.html                  # generated at end of run
```

Use `run_id=YYYYMMDD_HHMMSS_<short_label>`, for example `20260509_113000_activity_concepts`. If the user supplies a run label, slugify it for `<short_label>`; otherwise infer a short label from the assignment batch, such as `activity_concepts`, `mapping_batch`, or `mixed_assignments`.

13. Write `assignment_snapshot.md` with the unchecked `- [ ]` rows that are pending at run start, preserving their original order and section headings where practical.

14. Initialize `run_manifest.yaml`:

```yaml
run_id: <run_id>
status: in_progress
started_at: "<ISO 8601 timestamp>"
completed_at:
source:
  goal_file: GOAL.md
  runbook: run.md
  assignments_file: assignments.md
  assignment_snapshot: runs/<run_id>/assignment_snapshot.md
  mapping_root: data/mappings_dev20_0318
summary:
  pending_at_start: <N>
  enrichment_audited_count: 0
  enrichment_noop_count: 0
  enriched_count: 0
  generated_count: 0
  blocked_count: 0
  failed_count: 0
outputs:
  enriched_activities: []
  audited_activities: []
  generated_activities: []
  blocked_assignments: []
  review_dashboard:
checks: []
notes:
  - "Fresh assignment generation creates distinct package directories under activities/<base_activity_id>_r<YYYYMMDD_HHMMSS>."
  - "Existing checked-package enrichment may update activities/<activity_id>/ in place, but unchecked generation-ready rows must not reuse old package directories."
```

15. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Run id: <run_id>. Starting activity package loop."

## Existing Package Enrichment Pass (do before unchecked assignment processing)

Before processing any unchecked assignment, audit existing migrated packages that may have been generated under older or looser standards. A checked assignment means "already generated"; it does not mean the package is exempt from current quality rules.

Scope for this pass:

- Checked `assignments.md` rows that include `activity_id=<id>` and have an existing `activities/<id>/` package.
- Existing `activities/concept_*` packages produced by prior concept-led runs, especially when `program.md`, `templates.md`, `run.md`, or `GOAL.md` recently tightened the migrated package depth floor.
- Packages the user explicitly names for quality repair or enrichment.

For each scoped package:

1. Read `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.
2. Audit against the current package checks in this runbook, not only against the standard that existed when the package was first generated.
3. Spawn separate reviewer agents for package-quality review. When more than one package is in scope, partition packages into disjoint directory sets so reviewers can work in parallel without touching the same files.
4. Reviewer agents may make direct, minimal quality repairs inside their assigned package directories when the scope is explicit. They must not edit `assignments.md`, `results.tsv`, run manifests, or unrelated docs.
5. If the package is structurally valid but thin, enrich it in place. Preserve `activity_id`, directory name, tag-block enum values, recap/dashboard placeholders, stable asset IDs, and the five-file package contract.
6. For `spec.md`, add or update reviewer-facing detail that explains concrete design intent, scaffold fit, assumptions, constraints, product/asset dependency, game-feel rationale, and residual risk. A `## Runtime Detail Floor Notes` section is an acceptable way to record this when the existing file lacks an equivalent audit trail.
7. For `prod.md`, enrich runnable runtime detail: executable Step 1/2/4/5 dialogue, branch-specific follow-ups, non-generic screen states, distinct Step 3 objectives, child actions that match the mechanic, and a magic moment earned by repeated child action.
8. Do not append `results.tsv`, change completed assignment checkboxes, or create a duplicate `generated_activities` entry for enrichment-only work.
9. Record the author audit, reviewer-agent findings, direct reviewer repairs, re-review outcomes, and residual concerns in `runs/<run_id>/review_notes.md`. Increment `summary.enrichment_audited_count` for every package audited. If files changed, add or update an `outputs.enriched_activities` entry in `run_manifest.yaml` and increment `summary.enriched_count`; otherwise add or update an `outputs.audited_activities` entry and increment `summary.enrichment_noop_count` so the dashboard still shows the passed package.
10. Rerun the narrow package checks after any enrichment before moving to the unchecked assignment loop.

Enriched activity entry:

```yaml
- activity_id: <activity_id>
  activity_path: activities/<activity_id>
  source_assignment: "<checked assignment row or package discovery source>"
  changed_files:
    - activities/<activity_id>/spec.md
    - activities/<activity_id>/prod.md
  reason: "Updated to current migrated package depth floor"
  results_tsv_row: false
  status: enriched
```

Audited no-op activity entry:

```yaml
- activity_id: <activity_id>
  activity_path: activities/<activity_id>
  source_assignment: "<checked assignment row or package discovery source>"
  changed_files: []
  reason: "Reviewer audit passed against the current migrated package depth floor; no package edits required"
  results_tsv_row: false
  status: PASS / no changes
  reviewer: "<reviewer-agent name/id>"
```

## The Loop (repeat for every uncompleted assignment)

For each assignment in the run-start `assignment_snapshot.md` that is marked `- [ ]` (not yet completed), visit the row once in its original order. A blocked row remains unchecked in `assignments.md` for future product/design follow-up, but it is not retried again in the same run.

### Step 1: Parse the assignment

Extract: assignment_type (if provided), activity_concept (if provided), legacy concept alias (if provided), concept_source (if provided), description/notes (if provided), entity, category, tier, mechanic (if provided), pillar (if provided), style (if provided), scene (if provided), trigger_condition (if provided), mapping (if provided), asset_policy (if provided), asset_requirements / companion asset rows (if provided), product_capabilities (if provided), start type (if provided), and output activity_id (if provided). Normalize any legacy concept alias to `activity_concept=` and infer `assignment_type=activity_concept` unless a more specific type is declared.

For unchecked generation-ready rows, treat `activity_id=` as `base_activity_id`, not the final package ID. If the base value already ends in `_rYYYYMMDD_HHMMSS` because a prior run row was copied, strip that suffix first. The final package ID for this run must be `<base_activity_id>_r<YYYYMMDD_HHMMSS>`, using the timestamp prefix from the current `run_id`. This prevents fresh reruns from silently linking back to old `activities/` package directories. The only exception is enrichment/audit of already checked rows, which intentionally uses the existing package ID in place.

If `concept_source=` points to `file#concept_id`, read that repo-relative file and load the matching concept section before Phase 0. If `asset_requirements=` points to `file#asset_id`, read the same or referenced file and load the matching asset requirement section. Use the assignment row as the execution source of truth, and use the companion file as richer source / asset context.

Source concepts may arrive in Chinese or mixed language. Before writing an adaptation brief or package, normalize the concept name, description, trigger, assumptions, asset rows, and generated copy to English. Do not copy Chinese source prose into generated activity artifacts.

If `assignment_type` is not specified, infer it:

- `entity + category` with no concept field -> `entity_activity`
- `activity_concept=` or a legacy concept alias -> `activity_concept`
- property/category-driven concept with runtime placeholders -> `match_pattern`
- declared product dependency flags or unsupported category risk -> `capability_probe`

If tier is not specified, infer it per `program.md` rules. If scene is not specified, invent one unless the assignment is blocked in the adaptation brief.

### Step 1.1: Create adaptation brief

Run `program.md` Phase 0 before scaffold composition. This is required for `activity_concept`, `match_pattern`, `capability_probe`, legacy concept aliases, and underspecified rows; it is allowed for normal `entity_activity` rows.

1. Classify `input_mode` as `mapping_informed`, `parameterized`, or `concept_only`.
2. Identify `canonical_mechanic` and `mechanic_confidence`. If `mechanic=` is specified, it wins unless it is outside the current enum.
3. Decide `category_decision`, `readiness`, `trigger_condition`, `entity_role`, `observation_angle`, `focal_attribute`, mapping usefulness, asset dependency, product capability flags, and scaffold fit.
4. If `asset_policy` is provided, copy it into `adaptation_brief.asset_dependency.policy` instead of inferring asset need from prose. If companion asset rows are provided, normalize them into `adaptation_brief.asset_dependency.assets`.
5. Write the normalized adaptation brief to `runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml` if generation may proceed, or to `runs/<run_id>/blocked_briefs/<ordinal>_<assignment_slug>.yaml` if blocked.
6. If `readiness=blocked_until_product_decision`, block only this assignment but still create a constrained design preview at `runs/<run_id>/blocked_designs/<ordinal>_<assignment_slug>.md`. The preview should follow the activity's likely `prod.md` step shape closely enough for human review, including detailed Step 1-5 and Step 3 rounds when applicable. Add short inline comments exactly where unsupported behavior appears, using this format: `> BLOCKED ELEMENT: <reason> -- <what product/design decision is needed>`. Use the same blocker reason consistently when one missing product decision affects multiple beats; each inline marker is an occurrence, not a separate missing decision. Update `run_manifest.yaml` with a `blocked_assignments` entry, including both `brief_path` and `design_preview`, and increment `summary.blocked_count`; do not create valid package files under `activities/`, append `results.tsv`, mark the assignment complete, or commit mid-row. Continue to the next unchecked assignment unless this revealed a hard workflow failure that prevents safe processing of later rows.
7. If `readiness=generate_with_assumptions`, carry assumptions into `spec.md` under `## Adaptation Rationale`.
8. If assets are optional or required but generation proceeds, carry the normalized asset rows into `spec.md` `## Asset Brief`. `prod.md` may reference asset IDs and fallback behavior, but should not include raw image prompts.
9. If generation proceeds, carry `canonical_mechanic` into `tag_block.yaml` `activity_signature.mechanic`.

### Step 1.5: Load entity mapping (when required or available)

Read mapping YAML when `mapping=` is specified, when the adaptation brief has `input_mode=mapping_informed`, or when the package claims entity-specific mapping grounding. Do not require mapping for `concept_only` or `parameterized` briefs that use runtime placeholders.

If mapping is required:

1. Read `MAPPING_ROOT/_index.yaml` and find the entity_id.
2. Read the mapped YAML file and locate the entity block.
3. Extract:
   - target-tier `primary_theme` and `secondary_themes`
   - target-tier `primary_key_concepts` and `secondary_key_concepts`
   - `candidate_related_concepts`
   - `tier_guidance.[target_tier].dimensions`
4. Select 2-3 anchor dimensions per `entity_guidance.md` section 6:
   - Cat1: engagement-first plus one physical anchor.
   - Cat5: physical-first plus one engagement anchor.
5. Select Key Concepts, IB theme, and Related Concepts per `entity_guidance.md`.
6. If no mapping is present and the brief is `parameterized`, keep focal attributes and entity values as runtime placeholders.
7. If no mapping is present and the brief is `concept_only`, do not invent mapping-derived facts or Key Concepts.

### Step 2: Compose the scaffold

Read `templates.md` in layered order:

1. Template 0 reference.
2. Mechanic adapter matching `canonical_mechanic`.
3. Cat1 or Cat5 category modifier.
4. Pillar/style scaffold selected by the adaptation brief.

Use the composed scaffold as the activity's beat structure. Do not use the retired "Template A / Template B" split. If mapping-informed, ground creative variables in the selected dimensions and mapping attributes. If parameterized, use stable placeholders. If concept-only, avoid entity-specific claims.

The child's actual repeated action must match `canonical_mechanic`. Keep the selected `game_style` coherent with the mechanic, but do not let style override the requested action. If scaffold fit is weak, disclose it in `spec.md` or block this assignment before generation.

### Step 3: Generate the migrated activity package

Resolve the final package ID before writing files:

1. `base_activity_id`: assignment `activity_id=` if present, otherwise a stable lowercase snake_case slug derived from the concept/entity/mechanic.
2. Remove a trailing `_rYYYYMMDD_HHMMSS` suffix from `base_activity_id` when present.
3. `activity_id`: `<base_activity_id>_r<YYYYMMDD_HHMMSS>`, using the current run timestamp.
4. If `activities/<activity_id>/` already exists, stop and choose the next non-conflicting run-specific suffix before writing. Do not merge into or overwrite the existing directory.
5. Record both `base_activity_id` and `activity_id` in `run_manifest.yaml`.

Create a complete `activities/<activity_id>/` package with exactly five files:

```
activities/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

Rules:

- `spec.md`: author/reviewer reference with premise, target, rationale, selection trigger, pillar/game style, optional `## Adaptation Rationale`, optional `## Asset Brief`, and `## Self-Evaluation Scorecard`.
- `prod.md`: runtime prompt guidance with Basic Info, Activity Overview, and full Interaction Flow. It must not contain a scorecard.
- `tag_block.yaml`: structured metadata matching `activities/_schema/tag_block.schema.json`.
- `recap.template.yaml`: child recap payload using the same focal attribute, role/badge, and next-step direction.
- `dashboard.template.yaml`: parent dashboard fragment using the same focal attribute and progression axis.

Runtime completeness rule:

- Every Step 3 round in `prod.md` must be fully expanded with AI dialogue, child response branches, AI follow-up branches, and screen state.
- Never write "same structure," "later rounds follow," "AI gives a riddle," or one-line summaries in `activities/*/prod.md`.
- The migrated package may be shorter than legacy `designs/*_spec.md`, but it must not be thin. `spec.md` must explain the activity's concrete design intent, assumptions, constraints, asset/product dependencies, scaffold fit, and game-feel rationale. `prod.md` must be runnable without the operator inventing missing beats.
- Steps 1, 2, 4, and 5 also need concrete dialogue branches, follow-ups, and screen states. Do not concentrate all detail in Step 3 while leaving the bridge, rules, magic moment, or closing generic.
- Each Step 3 round must be distinct: named objective, different clue/challenge/action, child responses that exercise the canonical mechanic, branch-specific follow-ups, and a screen-state change.
- Generic warmth is insufficient. Fail and repair lines like "Great job," "try again," or "screen updates" when they are not tied to specific evidence, consequence, progress, or payoff.
- If `start=warm+cold`, document the bridge logic in `spec.md`; the runtime `prod.md` should still have a single converged Step 1 unless the assignment explicitly asks for both starts at runtime.
- Do not generate image files as part of this loop. When an activity uses AI-generated or displayed images, author the dependency in `spec.md` `## Asset Brief` and reference the stable `asset_id` from the relevant screen description in `prod.md`.

### Step 4: Self-evaluate and repair

Run through all 10 rubric dimensions from `program.md` Phase 3 against the actual package files. If any dimension FAILS:

1. Identify the specific issue.
2. Fix the relevant package file(s).
3. Re-evaluate.
4. Repeat until all dimensions PASS.

Dimension 8 only applies to mapping-informed designs. Score as N/A if no mapping. Dimensions 9 and 10 always apply. Dimension 10 checks mechanic fidelity + scaffold honesty, even though the legacy log column name remains `d10_pillar_fidelity`.

### Step 4.5: Independent scorecard review

Spawn a separate reviewer agent to independently check the same 10 dimensions against the completed package files before finalizing `spec.md`. This is mandatory for every generated package in an autonomous `/goal` run. If reviewer-agent tooling is unavailable, treat that as a hard workflow failure for package finalization because generated rows cannot be safely logged or checked off without independent review evidence.

For batch efficiency, reviewer agents may review disjoint package sets in parallel after each package is drafted, but each generated package still needs independent PASS evidence before `results.tsv` logging and assignment checkoff. Reviewer agents may propose repairs or directly edit their assigned package directories when explicitly scoped; any edited package must be rechecked and recorded in `review_notes.md`.

Reviewer instructions:

- Read `program.md` Phase 0 and Phase 3, the adaptation brief / `spec.md` `## Adaptation Rationale` when present, and the generated `activities/<activity_id>/` package.
- Read `templates.md`, `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`.
- If the assignment has `mapping=`, also read the relevant mapping source, `entity_guidance.md`, and `conversation_bridge.md`.
- Evaluate the package files directly, not the authoring agent's claimed scorecard.
- Return PASS/FAIL/N/A for each dimension with brief evidence and concrete file/section references for any issue. For Dimension 10, explicitly confirm that Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic` and the adaptation brief's `canonical_mechanic` when present. When assets are referenced, also confirm the package contains a coherent `## Asset Brief`, that every referenced `asset_id` is defined, and that required assets have prompts/source, use steps, display behavior, and fallback behavior.
- Fail structurally valid but thin packages. The reviewer should explicitly check whether `spec.md` is decision-useful and whether `prod.md` contains enough concrete dialogue, branch reactions, screen state, game-feel payoff, and source-promise detail to run the activity without filling gaps.

If the reviewer flags any FAIL or credible uncertainty, fix the package, rerun the author self-evaluation, and spawn a fresh independent review. Only finalize the `## Self-Evaluation Scorecard`, append `results.tsv`, and mark the assignment complete after both the author check and independent reviewer check pass.

### Step 5: Package checks

Before logging or committing, verify:

- `activities/<activity_id>/` contains exactly the five required files.
- Directory name equals `tag_block.yaml` `activity_id`.
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
- `spec.md` and `prod.md` satisfy the migrated package depth floor from `program.md`: concrete rationale, executable runtime detail, branch-specific follow-ups, non-generic screen states, and a magic moment earned by the child's action.
- Every `prod.md` Step 3 round is fully expanded; no condensed-round placeholders remain.
- `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
- Concept-led packages with `generate_with_assumptions` include `spec.md` `## Adaptation Rationale`.
- Packages whose adaptation brief has `asset_dependency.policy` other than `no_assets` include `spec.md` `## Asset Brief`.
- Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
- Required or optional asset rows include `asset_type`, requiredness, generation timing, use step, display behavior, and fallback behavior; generated assets also include a directly usable `prompt_en`, while existing/displayed assets include a `source` or approved source description.
- `prod.md` Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic`.
- `prod.md` contains zero `## Self-Evaluation Scorecard` sections.
- `runs/<run_id>/review_notes.md` contains independent reviewer-agent evidence for the package, including final PASS status or the unresolved issue that prevents logging.

### Step 6: Log the result

Append a row to `results.tsv`:

```
[assignment]\t[entity]\t[category]\t[tier]\t[pillar]\t[style]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F/N]\t[P/F]\t[P/F]\t[activity_id]\t[ISO timestamp]
```

Column order: assignment, entity, category, tier, pillar, style, status, d1_tech, d2_hook_transition, d3_edge, d4_ib, d5_tier, d6_dialogue, d7_screen, d8_mapping, d9_game_feel, d10_pillar_fidelity, filename, timestamp.

For `d8_mapping`: use P, F, or N. `d9_game_feel` and `d10_pillar_fidelity` are always P or F. The `d10_pillar_fidelity` column is retained for log compatibility and now records Dimension 10 Mechanic Fidelity + Scaffold Honesty.

### Step 6.5: Update run provenance

For every generated package:

1. Append the `activity_id` to `runs/<run_id>/generated_activity_ids.txt`.
2. Add or update a `generated_activities` entry in `runs/<run_id>/run_manifest.yaml`:

```yaml
- assignment_index: <ordinal from assignment_snapshot.md>
  assignment: "<original assignment row>"
  base_activity_id: <base_activity_id>
  activity_id: <activity_id>
  activity_path: activities/<activity_id>
  adaptation_brief: runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml # omit when no Phase 0 brief was produced
  results_tsv_row: true
  generation_policy: fresh_rerun_distinct_directory
  status: PASS
```

3. Add reviewer evidence, repair notes, and residual risks to `runs/<run_id>/review_notes.md` for every generated, enriched, or audited package.
4. Verify `runs/<run_id>/run_manifest.yaml` has an entry for the generated activity and `runs/<run_id>/generated_activity_ids.txt` includes the generated `activity_id`.

For enrichment-only package maintenance, keep changed packages under `enriched_activities` and do not append `results.tsv`. Keep audited packages that passed without edits under `audited_activities` so `review.html` shows all reviewer-covered packages, not only packages that changed.

For blocked assignments, keep the entry under `blocked_assignments`, include `brief_path` and `design_preview`, do not append `results.tsv`, leave the assignment row unchecked, and continue to the next unchecked row. If the constraints are later resolved, rerun or promote the design preview into a normal five-file package, remove or resolve the blocked-element comments, then send it through the standard self-evaluation, reviewer-agent, validation, `results.tsv`, and checkoff gates.

### Step 6.7: Generate human review dashboard

This is a final-run step, not a per-assignment step. After every row from `assignment_snapshot.md` has generated, blocked, or failed, and after all package checks, reviewer evidence, manifest entries, blocked-brief entries, and blocked design previews are current, generate a single static review dashboard at:

```text
runs/<run_id>/review.html
```

This file is for human review only. It is a derived artifact, not a source of truth. Follow `review_dashboard.md` for the dashboard contract, including source inputs, concise clickable cards for generated/enriched/audited packages, popup/detail behavior, grouped tag colors, 10-dimension criteria and package scorecard results, blocked-preview handling, per-blocked-card `Minimum To Unblock` sections below capability flags, blocked-preview scorecards, link rules, validation requirements, the editorial design language in `review_dashboard.md` §"Design language" (warm-paper palette, indigo accent, serif display title, hairline-divided panels, tabular numerals, accent rails on cards, status-dot run indicator), and the in-file preview behavior in `review_dashboard.md` §"In-file preview" (embedded `<template>` content, dedicated preview `<dialog>`, dependency-free Markdown rendering, modifier-click bypass, "Open in new tab" escape hatch).

Generation command:

```bash
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

The generator reads `run_manifest.yaml`, `review_notes.md`, `results.tsv`, package files, blocked briefs, and blocked design previews, then writes `runs/<run_id>/review.html`.

After writing `review.html`:

1. Update `runs/<run_id>/run_manifest.yaml` `outputs.review_dashboard` to `runs/<run_id>/review.html`.
2. Add check entries for `python3 scripts/generate_run_review.py runs/<run_id>` and `python3 scripts/generate_run_review.py --validate runs/<run_id>`.
3. Verify the file exists, is non-empty, has `<html`, `<style`, `<script>`, the run id, cards for generated/enriched/audited packages, blocked entries when present, the 10-dimension review criteria, per-package scorecard results with why notes, blocked-preview scorecards when blocked entries exist, clickable detail behavior, modal/detail content, per-blocked-card `Minimum To Unblock` sections below capability flags, grouped tag colors, inline blocked marker chips, clear missing-decision versus inline-marker counts, and resolving local links.

### Step 7: Mark generated assignment complete

In `assignments.md`, change `- [ ]` to `- [x]` only for assignments that generated a passing package. Also rewrite that row's `activity_id=` value to the actual run-specific `activity_id` so the checked row points at the generated directory. If the row did not already have `activity_id=`, add one near the other assignment fields. Do not rewrite blocked rows.

### Step 8: Commit

```bash
git add activities/<activity_id>/ runs/<run_id>/ results.tsv assignments.md
git commit -m "Design: <activity_id> - ALL PASS"
```

### Step 9: Next assignment

Move to the next `- [ ]` assignment from the run-start queue, including rows after a blocked assignment. When every row from `assignment_snapshot.md` has either generated, blocked, or failed:

- If `failed_count > 0`, set `run_manifest.yaml status: failed` and stop with the failure reason.
- Else if `blocked_count > 0`, set `run_manifest.yaml status: completed_with_blockers`.
- Else set `run_manifest.yaml status: completed`.

Fill `completed_at`, update the summary counts, and generate `runs/<run_id>/review.html` after the final manifest/check entries are current. Then say: "Run complete. [N] activity packages generated; [M] existing packages enriched; [B] assignments blocked for product/design decisions. See results.tsv, runs/<run_id>/run_manifest.yaml, and runs/<run_id>/review.html for summary and review."

Before that final message, ensure `runs/<run_id>/review.html` exists and is referenced in `run_manifest.yaml`. Include the dashboard path in the final message so reviewers can open the run in one place.

## Legacy transform workflow

`transform.md` and `transform_run.md` are retained only for the old `designs/*_spec.md` to `designs/*_prod.md` workflow. Do not use them for migrated `activities/*/prod.md` files.

## Important Rules

- Never skip steps. Every activity package must be complete before saving.
- Never abbreviate later rounds because "they follow the same pattern." Each runtime round is fully independent.
- Never put a scorecard in `prod.md`.
- Always put the scorecard in `spec.md`.
- Keep `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` aligned with the runtime flow.
- Do not treat checked assignment rows as immutable when generation standards changed; audit and enrich existing packages before the unchecked loop starts.
- Do not reuse an old `activities/<activity_id>/` directory for unchecked generation-ready rows. Fresh reruns must create a new run-specific directory named `activities/<base_activity_id>_r<YYYYMMDD_HHMMSS>/`, and `tag_block.yaml` `activity_id` must match it.
- Do not let one product/design blocker halt the whole batch. Record the blocked brief and constrained design preview, leave that row unchecked, and continue to later unchecked rows unless a hard workflow failure makes later processing unsafe.
- Commit after every completed package unless the user explicitly asks to batch commits.
- Quality over speed. Take as many self-evaluation rounds as needed.
