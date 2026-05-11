# Codex Goal: Autonomous Activity Generation

Use this file as the `/goal` target for running the WonderLens autonomous activity generation loop.

## Goal

Generate or triage WonderLens activity assignments from `assignments.md` using the current authoring workflow in `program.md`, `templates.md`, `run.md`, and the migrated `activities/<activity_id>/` package contract.

Each run must also create a provenance directory under `runs/<run_id>/` so generated packages, blocked briefs, and constrained blocked design previews can be traced back to the exact `/goal` session.

For fresh assignment generation, the assignment `activity_id=` value is a base slug, not permission to reuse an existing package directory. The actual generated package directory must be unique to the run: strip any trailing `_rYYYYMMDD_HHMMSS` suffix from the base slug, then create `activities/<base_activity_id>_r<YYYYMMDD_HHMMSS>/` using the current run timestamp. Enrichment-only maintenance may update existing checked packages in place, but unchecked generation-ready rows must produce distinct package directories so reruns can be compared side by side.

## Recommended `/goal` Command

```text
/goal Execute GOAL.md end to end using run.md. Initialize run provenance, audit/enrich checked activity packages against the current migrated package depth floor with separate reviewer-agent evidence, then process the run-start unchecked assignment snapshot exactly once in order. For each generation-ready row, derive a run-specific activity_id by appending _rYYYYMMDD_HHMMSS to the base slug and generate a passing five-file package in a new activities/<run-specific_activity_id>/ directory; for blocked rows, record a blocked brief plus constrained blocked design preview and continue. In blocked previews, still design detailed runtime steps, annotate unsupported dependencies inline with BLOCKED ELEMENT comments, and keep the activity invalid until the blocker is resolved. Do not append results.tsv or mark a generated assignment complete until reviewer issues are repaired and re-reviewed. After final validation, generate and validate runs/<run_id>/review.html according to review_dashboard.md. Stop only on a hard workflow failure that makes later rows unsafe. Use GOAL.md success criteria as the completion contract and report generated, enriched, blocked, reviewer-agent coverage, review dashboard path, checks, and residual risks.
```

## Success Criteria

The goal is complete only when all of the applicable criteria below are met.

1. Setup context is loaded:
   - `GOAL.md`
   - `program.md`
   - `templates.md`
   - `run.md`
   - `review_dashboard.md`
   - `runs/README.md`
   - `activities/README.md`
   - `activities/_schema/tag_block.schema.json`
   - `docs/activity_vocabulary.md`
   - `docs/game_styles.md`
   - `assignments.md`
   - Any `concept_source=file#id` or `asset_requirements=file#id` companion files referenced by pending assignment rows
   - `entity_guidance.md` and `conversation_bridge.md` when mapping or warm/cold bridge handling is required

2. Run provenance is initialized before assignment processing:
   - A `run_id` is created in `YYYYMMDD_HHMMSS_<short_label>` format.
   - `runs/<run_id>/run_manifest.yaml` exists with `status: in_progress`, source files, mapping root, output lists, and summary counters.
   - `runs/<run_id>/assignment_snapshot.md` preserves unchecked assignment rows pending at run start.
   - `runs/<run_id>/generated_activity_ids.txt`, `adaptation_briefs/`, `blocked_briefs/`, `blocked_designs/`, and `review_notes.md` are initialized.

3. Assignment rows are processed in order:
   - Only unchecked `- [ ]` rows are processed.
   - The run-start `assignment_snapshot.md` is the queue; each snapshot row is visited at most once per run, even if a blocked row remains unchecked for a future product decision.
   - `assignment_type` is parsed or inferred.
   - `activity_concept=` is used for concept-led rows; legacy concept aliases are normalized before Phase 0.
   - Source concepts may be Chinese, but generated adaptation briefs and package files are English-only.

4. Phase 0 adaptation is completed when required:
   - `activity_concept`, `match_pattern`, and `capability_probe` rows always receive an `adaptation_brief`.
   - `entity_activity` rows receive an `adaptation_brief` when mapping, category, mechanic, trigger, or scaffold fit needs resolution.
   - Referenced `concept_source` and `asset_requirements` rows are loaded before the brief is written.
   - The brief records `input_mode`, `canonical_mechanic`, readiness, trigger condition, mapping use, asset dependency, product capability flags, scaffold choice, and assumptions.
   - If `asset_policy` or companion asset rows are present, the brief copies them into `asset_dependency` instead of inferring image needs from prose.
   - The normalized brief is written to `runs/<run_id>/adaptation_briefs/` when generation may proceed, or to `runs/<run_id>/blocked_briefs/` when blocked.

5. Blocked assignments are triaged safely without halting the batch:
   - If `readiness=blocked_until_product_decision`, output the adaptation brief and a constrained blocked design preview for that assignment, then continue to the next unchecked row.
   - Write the brief to `runs/<run_id>/blocked_briefs/` and the preview to `runs/<run_id>/blocked_designs/`.
   - The preview still designs detailed runtime steps so reviewers can inspect the proposed child experience.
   - Add short inline comments at each unsupported dependency using `BLOCKED ELEMENT: <reason> -- <decision needed>`.
   - Treat inline blocked comments as runtime occurrences. They may outnumber missing product/design decisions when one unresolved blocker affects several beats.
   - Do not create valid runtime package files under `activities/`.
   - Do not append `results.tsv`.
   - Do not mark the assignment complete; it remains visible for the future product/design decision.
   - Update `runs/<run_id>/run_manifest.yaml` with a `blocked_assignments` entry, including `brief_path` and `design_preview`, and increment `blocked_count`.
   - Report the missing product decision, capability, schema, category, template extension, or asset pipeline decision.
   - If the constraint is later resolved, rerun or promote the constrained preview into a normal five-file package, remove or resolve the blocked comments, then apply the standard self-evaluation, reviewer, validation, `results.tsv`, and checkoff gates.
   - Use `status: completed_with_blockers` when the run finishes all processable rows but one or more rows blocked. Use `status: failed` only for hard workflow failures that prevent safe processing of later rows.

6. Generation-ready assignments produce a complete package:
   - Resolve `base_activity_id` from the assignment `activity_id=` when present, or from a stable generated slug when absent.
   - Strip any trailing `_rYYYYMMDD_HHMMSS` suffix from `base_activity_id` before deriving a fresh run package ID.
   - For unchecked generation-ready rows, the actual `activity_id` is `<base_activity_id>_r<YYYYMMDD_HHMMSS>`, where the timestamp comes from the current `run_id`.
   - Do not reuse an existing `activities/<base_activity_id>/` or previous `activities/<base_activity_id>_r.../` directory for fresh generation. Reuse is allowed only for enrichment/audit of already checked packages.
   - Exactly five files exist under `activities/<activity_id>/`:
     - `spec.md`
     - `prod.md`
     - `tag_block.yaml`
     - `recap.template.yaml`
     - `dashboard.template.yaml`
   - Directory name matches `tag_block.yaml` `activity_id`.
   - `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.

7. Existing package enrichment is handled before the unchecked assignment loop starts:
   - Checked `assignments.md` rows that include `activity_id=<id>` and have an existing `activities/<id>/` package are audited against the current migrated package depth floor.
   - Checked rows are not treated as frozen when generation standards changed after they were created.
   - Separate reviewer agents are spawned for scoped package-quality review when the run audits or enriches packages; assign reviewers disjoint package directories when multiple packages are reviewed in parallel.
   - Structurally valid but thin packages are enriched in place, preserving `activity_id`, tag-block enums, recap/dashboard placeholders, asset IDs, and the five-file package contract.
   - Enrichment focuses on decision-useful `spec.md` detail and runnable `prod.md` detail: concrete design intent, scaffold fit, game-feel rationale, executable dialogue, branch-specific follow-ups, screen states, distinct Step 3 rounds, and earned magic moments.
   - Reviewer-agent findings, direct repairs, re-review outcomes, no-op decisions, and residual concerns are recorded in `runs/<run_id>/review_notes.md`; changed packages are recorded under `outputs.enriched_activities`, and already-compliant packages are recorded under `outputs.audited_activities`.
   - Enrichment/audit does not append `results.tsv`, rewrite completed assignment checkboxes, or create a second generated activity entry. It is recorded as package maintenance in `runs/<run_id>/run_manifest.yaml` and `runs/<run_id>/review_notes.md`.
   - Packages that already meet the current floor are recorded as no-op audits with `status: PASS / no changes` so `review.html` displays them as passed activity cards.
   - Package checks are rerun after any enrichment.

8. Runtime package quality checks pass:
   - `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` are written in English, even when the source concept was Chinese.
   - `spec.md` is decision-useful, not just a scorecard wrapper: it records concrete design intent, assumptions, constraints, scaffold fit, asset/product dependencies, game-feel rationale, and residual risk when relevant.
   - `prod.md` satisfies the migrated package depth floor from `program.md`: every step is runnable, concrete, and specific enough for the prompt composer without relying on old design files.
   - `prod.md` contains no `## Self-Evaluation Scorecard`.
   - `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
   - Every runtime Step 3 round in `prod.md` is fully expanded.
   - Steps 1, 2, 4, and 5 include executable dialogue/screen detail; Step 3 rounds are distinct in objective, child action, branch-specific follow-up, and screen-state change.
   - Magic moments are earned by the child's repeated action and visible in dialogue plus screen behavior, not only awarded as a generic badge.
   - `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
   - `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`, `spec.md`, and `prod.md` agree on mechanic, pillar, game style, focal attribute, badge/reward, and next-step direction.

9. Mechanic-first checks pass:
   - `tag_block.yaml` `activity_signature.mechanic` matches the canonical mechanic from the assignment or adaptation brief.
   - The repeated child action in `prod.md` Step 3 matches that mechanic.
   - Weak scaffold fit or generation assumptions are disclosed in `spec.md` `## Adaptation Rationale`.
   - Pillar and `game_style` support the mechanic; they do not override it.

10. Asset dependency checks pass when assets are present:
   - `spec.md` includes `## Asset Brief` when `asset_dependency.policy` is not `no_assets`.
   - Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
   - Required assets declare `asset_type`, requiredness, generation timing, use step, purpose, display behavior, and fallback behavior.
   - Generated assets include a directly usable English `prompt_en`; existing/displayed assets include a `source` or approved source description.
   - `prod.md` references asset IDs and fallback behavior, not raw generation prompts.
   - The loop does not generate or store image files unless a future asset pipeline explicitly changes this contract.

11. Mapping checks pass when mapping is required:
   - `mapping=` resolves through `MAPPING_ROOT/_index.yaml`.
   - Entity-specific facts, IB concepts, related concepts, bridge prerequisites, and tier language are grounded in the mapped YAML.
   - Parameterized rows use placeholders instead of inventing entity-specific claims.

12. Review and logging are complete for generated packages:
   - The package passes the 10-dimension rubric in `program.md`.
   - A separate reviewer agent checks every generated package against the same 10 dimensions, the migrated package depth floor, mechanic fidelity, asset-brief coherence, and package-file consistency.
   - Reviewers explicitly fail structurally valid but thin/generic packages that do not meet the migrated package depth floor.
   - Any reviewer FAIL or credible uncertainty is repaired before logging; the repaired package is re-reviewed by a fresh separate reviewer agent or by the original reviewer after reading the changed files.
   - `runs/<run_id>/review_notes.md` records reviewer-agent name/id when available, package scope, PASS/FAIL/N/A evidence, repairs made, and final reviewer outcome.
   - `results.tsv` receives one row for each generated package.
   - `runs/<run_id>/generated_activity_ids.txt` includes each generated `activity_id`.
   - `runs/<run_id>/run_manifest.yaml` links each generated assignment row to `activities/<activity_id>/`, its `base_activity_id`, its adaptation brief when present, and `results.tsv`.
   - `results.tsv` `filename` points at the run-specific `activities/<activity_id>` directory, not a reused base package.
   - The processed assignment row is changed from `- [ ]` to `- [x]`, and its `activity_id=` value is rewritten to the actual run-specific `activity_id` so checked assignments point to the package produced by that run.

13. Human review dashboard is generated:
   - `runs/<run_id>/review.html` exists before the final report.
   - The dashboard is generated with `python3 scripts/generate_run_review.py runs/<run_id>` and validated with `python3 scripts/generate_run_review.py --validate runs/<run_id>`.
   - The dashboard satisfies `review_dashboard.md`: self-contained light-theme HTML, concise clickable cards for generated/enriched/audited packages, full detail dialog/page content, grouped tag colors, search/filter/sort controls, blocked-preview handling, clear missing-decision versus inline-marker counts, per-blocked-card `Minimum To Unblock` sections below capability flags, colored inline blocked marker chips, blocked-preview scorecards, reason guide, reviewer coverage, 10-dimension review criteria, per-package scorecard results with why notes, checks, residual risks, and resolving local links.
   - The dashboard preserves the editorial design language defined in `review_dashboard.md` §"Design language": warm-paper palette, single indigo accent, serif display title and dialog headings, hairline-divided panels (no card-within-card), tabular numerals on numeric columns, indigo/amber accent rails on activity/blocked cards, and a status-dot run indicator.
   - The dashboard provides in-file preview for every linked `.md`/`.yaml`/`.txt` per `review_dashboard.md` §"In-file preview": raw content embedded as `<template>` elements, a dedicated preview `<dialog>` renders Markdown inline and YAML/text in a code block, plain click previews while modifier-click and the "Open in new tab" link still navigate.
   - `runs/<run_id>/run_manifest.yaml` records the dashboard path, and the final report includes it.

14. Final report is clear:
   - State how many packages were generated.
   - State how many existing packages were enriched or audited as already compliant.
   - List any blocked assignments and the exact reason.
   - Include the `run_id` and `runs/<run_id>/run_manifest.yaml` path.
   - Include the `runs/<run_id>/review.html` path.
   - Report reviewer-agent coverage: which packages were reviewed, which were edited by reviewers or repaired after review, and whether all generated packages received independent PASS evidence.
   - List verification commands run and their results.
   - State any residual risk or follow-up product decision.

## Assignment Type Names

Use these names in new `assignments.md` rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked |

Legacy concept aliases should be treated as `assignment_type=activity_concept` with `activity_concept=<value>`.
