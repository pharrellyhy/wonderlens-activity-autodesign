# Codex Goal: Autonomous Activity Generation

Use this file as the `/goal` target for running the WonderLens autonomous activity generation loop.

## Goal

Generate or triage WonderLens activity assignments from `assignments.md` using the current authoring workflow in `program.md`, `templates.md`, `run.md`, and the migrated five-required-file activity package contract.

For source-derived batches, preserve the original source design's play frame. A generated package may keep the mechanic/category labels and still fail if it changes the child role, interaction sequence, story frame, or required child action without product approval.

Each run must also create a provenance directory under `runs/<run_id>/` so generated packages, blocked briefs, and constrained blocked design previews can be traced back to the exact `/goal` session.

For fresh assignment generation, the assignment `activity_id=` value is a clean base slug. Strip any trailing `_rYYYYMMDD_HHMMSS` suffix from copied rows, keep the clean base slug as the package `activity_id`, and write the actual package under `runs/<run_id>/activity_packages/<base_activity_id>/`. Enrichment-only maintenance may update existing checked canonical packages under `activities/<activity_id>/` in place. Do not write fresh rerun packages directly under `activities/` unless a later explicit promotion step asks for that.

Direct demo export is enabled by default for this full generation goal. Every generated package must include optional package-local demo extensions unless the user explicitly disables demo export for the run or the package is only a blocked preview:

```text
demo_support.yaml
asset_manifest.yaml
```

These files do not replace the five required package files. They make the generated package direct-demo-import ready by declaring demo support status, explicit entity binding, separate runtime assets, reference-bound provenance, and unsupported/degraded mechanic gates.

If the user supplies a scope such as "only Batch 5" or "last batch", process only that scoped assignment subset in the run-start snapshot. If the user says the product contract now allows minimum-to-unblock decisions, treat prior capability probes as generation-ready under `product_contract_override=minimum_unblock_allowed`: generate normal packages with the five required files plus any enabled demo extensions, record formerly blocking dependencies as resolved blocker annotations, and keep those callouts visible in `review.html`.

## Recommended `/goal` Command

```text
/goal Execute GOAL.md end to end using run.md. Initialize run provenance, honor any user-specified assignment scope or product-contract override, audit/enrich checked activity packages that have an explicit package_path or canonical activities/<activity_id>/ directory against the current migrated package depth floor with separate reviewer-agent evidence, then process the run-start unchecked assignment snapshot exactly once in order. Direct demo export is enabled by default unless the user explicitly disables it. For each generation-ready row, preserve source-promise alignment from the original source design, including original play frame, child role, interaction sequence, required child actions, non-negotiable elements, allowed V1 adaptations, and product dependencies. Use the assignment activity_id as a clean base slug, strip any copied _rYYYYMMDD_HHMMSS suffix, and generate a passing package under runs/<run_id>/activity_packages/<base_activity_id>/ with the five required files plus demo_support.yaml and asset_manifest.yaml, and with tag_block.yaml activity_id matching the clean base slug; for blocked rows, record a blocked brief plus constrained blocked design preview and continue. If product_contract_override=minimum_unblock_allowed is active, generate formerly blocked rows as normal packages, replace invalid blockers with resolved blocker annotations, and still show those resolved dependencies in review.html. Include extensibility notes for every package so reviewers can see whether the activity can be reused with other entities, properties, or asset sets. Do not append results.tsv or mark a generated assignment complete until reviewer issues are repaired and re-reviewed. After final validation, generate and validate runs/<run_id>/review.html according to review_dashboard.md. Stop only on a hard workflow failure that makes later rows unsafe. Use GOAL.md success criteria as the completion contract and report generated, enriched, blocked, resolved blockers, demo support coverage, source-intent drift, extensibility coverage, reviewer-agent coverage, review dashboard path, checks, and residual risks.
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
   - `activities/_schema/demo_support.schema.json`
   - `activities/_schema/asset_manifest.schema.json`
   - `docs/activity_vocabulary.md`
   - `docs/game_styles.md`
   - `assignments.md`
   - Any `concept_source=file#id` or `asset_requirements=file#id` companion files referenced by pending assignment rows
   - `entity_guidance.md` and `conversation_bridge.md` when mapping or warm/cold bridge handling is required

2. Run provenance is initialized before assignment processing:
   - A `run_id` is created in `YYYYMMDD_HHMMSS_<short_label>` format.
   - `runs/<run_id>/run_manifest.yaml` exists with `status: in_progress`, source files, mapping root, output lists, and summary counters.
   - `runs/<run_id>/assignment_snapshot.md` preserves unchecked assignment rows pending at run start.
   - `runs/<run_id>/generated_activity_ids.txt`, `activity_packages/`, `adaptation_briefs/`, `blocked_briefs/`, `blocked_designs/`, and `review_notes.md` are initialized.
   - Any user-specified batch/scope filter and product-contract override are recorded in `run_manifest.yaml` `source` or `notes`.

3. Assignment rows are processed in order:
   - Only unchecked `- [ ]` rows are processed.
   - The run-start `assignment_snapshot.md` is the queue; each snapshot row is visited at most once per run, even if a blocked row remains unchecked for a future product decision.
   - `assignment_type` is parsed or inferred.
   - `activity_concept=` is used for concept-led rows; legacy concept aliases are normalized before Phase 0.
   - Source-promise cues are extracted when the source is richer than a simple entity/category row: original play frame, child role, interaction sequence, required child actions, and non-negotiable source elements.
   - If a normalized assignment paraphrase conflicts with the original source design, the original source design controls unless product approval is recorded.
   - Source concepts may be Chinese, but generated adaptation briefs and package files are English-only.

4. Phase 0 adaptation is completed when required:
   - `activity_concept`, `match_pattern`, and `capability_probe` rows always receive an `adaptation_brief`.
   - `entity_activity` rows receive an `adaptation_brief` when mapping, category, mechanic, trigger, or scaffold fit needs resolution.
   - Referenced `concept_source` and `asset_requirements` rows are loaded before the brief is written.
   - The brief records `input_mode`, source-promise alignment, `canonical_mechanic`, readiness, trigger condition, mapping use, asset dependency, product capability flags, scaffold choice, and assumptions.
   - If `asset_policy` or companion asset rows are present, the brief copies them into `asset_dependency` instead of inferring image needs from prose.
   - For full GOAL.md runs, `demo_export` defaults to `true` unless explicitly disabled. The brief records demo support classification and asset manifest requirements for every generation-ready package.
   - The normalized brief is written to `runs/<run_id>/adaptation_briefs/` when generation may proceed, or to `runs/<run_id>/blocked_briefs/` when blocked.

5. Blocked assignments are triaged safely without halting the batch:
   - If `readiness=blocked_until_product_decision`, output the adaptation brief and a constrained blocked design preview for that assignment, then continue to the next unchecked row.
   - Write the brief to `runs/<run_id>/blocked_briefs/` and the preview to `runs/<run_id>/blocked_designs/`.
   - The preview still designs detailed runtime steps so reviewers can inspect the proposed child experience.
   - Add short inline comments at each unsupported dependency using `BLOCKED ELEMENT: <reason> -- <decision needed>`.
   - Treat inline blocked comments as runtime occurrences. They may outnumber missing product/design decisions when one unresolved blocker affects several beats.
   - Do not create valid runtime package files under `runs/<run_id>/activity_packages/` or `activities/`.
   - Do not append `results.tsv`.
   - Do not mark the assignment complete; it remains visible for the future product/design decision.
   - Update `runs/<run_id>/run_manifest.yaml` with a `blocked_assignments` entry, including `brief_path` and `design_preview`, and increment `blocked_count`.
   - Report the missing product decision, capability, schema, category, template extension, or asset pipeline decision.
   - If the constraint is later resolved, rerun or promote the constrained preview into a normal package with the five required files plus any enabled demo extensions, remove or resolve the blocked comments, then apply the standard self-evaluation, reviewer, validation, `results.tsv`, and checkoff gates.
   - If `product_contract_override=minimum_unblock_allowed` is active, do not leave the row blocked solely for a minimum-to-unblock decision. Generate the normal package with the five required files plus any enabled demo extensions, record the former blocker in `spec.md` `## Resolved Product Contract Notes` and near the affected runtime beat in `prod.md` as `RESOLVED BLOCKER`, and record `resolved_blockers` / `resolved_blocker_types` in `run_manifest.yaml`.
   - Use `status: completed_with_blockers` when the run finishes all processable rows but one or more rows blocked. Use `status: failed` only for hard workflow failures that prevent safe processing of later rows.

6. Generation-ready assignments produce a complete package:
   - Resolve `base_activity_id` from the assignment `activity_id=` when present, or from a stable generated slug when absent.
   - Strip any trailing `_rYYYYMMDD_HHMMSS` suffix from `base_activity_id` before writing the fresh run package.
   - For unchecked generation-ready rows, the actual `activity_id` remains the clean `<base_activity_id>`, and the run-specific identity comes from the package path `runs/<run_id>/activity_packages/<base_activity_id>/`.
   - Do not reuse an existing `activities/<base_activity_id>/` directory for fresh generation. Existing canonical packages may be audited/enriched in place only when the assignment row was already checked or the user explicitly requests package promotion/maintenance.
   - The five required files exist under `runs/<run_id>/activity_packages/<activity_id>/`:
     - `spec.md`
     - `prod.md`
     - `tag_block.yaml`
     - `recap.template.yaml`
     - `dashboard.template.yaml`
   - Unless demo export is explicitly disabled, these package-local extension files also exist and validate:
     - `demo_support.yaml`
     - `asset_manifest.yaml`
   - Directory name matches `tag_block.yaml` `activity_id`.
   - `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.

7. Existing package enrichment is handled before the unchecked assignment loop starts:
   - Checked `assignments.md` rows that include `package_path=<repo-relative package dir>` are audited at that explicit package path; checked rows without `package_path` may audit an existing canonical `activities/<activity_id>/` package.
   - Checked rows are not treated as frozen when generation standards changed after they were created.
   - Separate reviewer agents are spawned for scoped package-quality review when the run audits or enriches packages; assign reviewers disjoint package directories when multiple packages are reviewed in parallel.
   - Structurally valid but thin packages are enriched in place, preserving `activity_id`, tag-block enums, recap/dashboard placeholders, asset IDs, and the five-required-file package contract.
   - Enrichment focuses on decision-useful `spec.md` detail and runnable `prod.md` detail: concrete design intent, scaffold fit, game-feel rationale, executable dialogue, branch-specific follow-ups, screen states, distinct Step 3 rounds, and earned magic moments.
   - Reviewer-agent findings, direct repairs, re-review outcomes, no-op decisions, and residual concerns are recorded in `runs/<run_id>/review_notes.md`; changed packages are recorded under `outputs.enriched_activities`, and already-compliant packages are recorded under `outputs.audited_activities`.
   - Enrichment/audit does not append `results.tsv`, rewrite completed assignment checkboxes, or create a second generated activity entry. It is recorded as package maintenance in `runs/<run_id>/run_manifest.yaml` and `runs/<run_id>/review_notes.md`.
   - Packages that already meet the current floor are recorded as no-op audits with `status: PASS / no changes` so `review.html` displays them as passed activity cards.
   - Package checks are rerun after any enrichment.

8. Runtime package quality checks pass:
   - `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` are written in English, even when the source concept was Chinese.
   - `spec.md` is decision-useful, not just a scorecard wrapper: it records concrete design intent, assumptions, constraints, scaffold fit, asset/product dependencies, game-feel rationale, and residual risk when relevant.
   - `prod.md` satisfies the migrated package depth floor from `program.md`: every step is runnable, concrete, and specific enough for the prompt composer without relying on old design files.
   - Runtime beats may use existing `AI says` exact dialogue or the newer `Runtime AI instruction` plus `Example AI line` contract. A behavior instruction must preserve source frame, required content, branch policy, safety/product constraints, and screen/state expectation.
   - Unexpected and no-response branch policies are specific to the current beat and Step 3 round. They may share safety principles, but must not reuse generic boilerplate across activities or repeat identical rows across rounds; each redirect or scaffold returns to the current source action, role, challenge, asset/fallback, screen state, prior consequence, or completion target.
   - `prod.md` contains no `## Self-Evaluation Scorecard`.
   - `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
   - Every runtime Step 3 round in `prod.md` is fully expanded.
   - Steps 1, 2, 4, and 5 include executable dialogue/screen detail; Step 3 rounds are distinct in objective, child action, branch-specific follow-up, and screen-state change.
   - Magic moments are earned by the child's repeated action and visible in dialogue plus screen behavior, not only awarded as a generic badge.
   - `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
   - `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`, `spec.md`, and `prod.md` agree on mechanic, pillar, game style, focal attribute, badge/reward, and next-step direction.
   - `spec.md` includes `## Extensibility Notes` for concept-led or parameterized packages, describing reusable slots and how the activity can be retargeted to other entities, properties, or approved asset sets without changing the mechanic.
   - When demo export is enabled, `demo_support.yaml` and `asset_manifest.yaml` are present, pass `python3 scripts/validate_demo_package_contract.py <package_dir>`, and agree with the package's activity ID and bound/default entity.

9. Mechanic-first checks pass:
   - `tag_block.yaml` `activity_signature.mechanic` matches the canonical mechanic from the assignment or adaptation brief.
   - The repeated child action in `prod.md` Step 3 matches that mechanic.
   - The runtime flow preserves the source play frame, child role, interaction sequence, and required child actions unless a product-approved adaptation is recorded.
   - Weak scaffold fit or generation assumptions are disclosed in `spec.md` `## Adaptation Rationale`.
   - Pillar and `game_style` support the mechanic; they do not override it.

10. Asset dependency checks pass when assets are present:
   - `spec.md` includes `## Asset Brief` when `asset_dependency.policy` is not `no_assets`.
   - `spec.md` includes `## Asset Usage Timeline` for any prebuilt, displayed, or runtime-generated image dependency.
   - Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
   - Required assets declare `asset_type`, requiredness, generation timing, use step, display location, purpose, display behavior, and fallback behavior.
   - The usage timeline makes the image flow skimmable: prebuilt versus runtime-generated, load/generate moment, first display step, visible step/round range, screen location, interaction/use, prompt/source summary, persistence or hide behavior, and fallback.
   - Review outputs distinguish asset dependencies from display occurrences: one `asset_id` or card set can be displayed in multiple runtime beats, so `review.html` must show `Asset dependencies`, `Display beats`, and `Image items` separately.
   - Generated assets include a directly usable English `prompt_en`; existing/displayed assets include a `source` or approved source description.
   - `prod.md` references asset IDs, display location, and fallback behavior, not raw generation prompts.
   - The loop does not generate or store image files unless a future asset pipeline explicitly changes this contract.
   - When demo export is enabled, `asset_manifest.yaml` contains separate runtime asset entries, not a contact sheet as the runtime asset.
   - `asset_manifest.yaml` uses `style_id: wonderlens_device_mint_soft_3d`, round-device safe-area rules, target variants, nullable path slots, and fallback behavior.
   - Reference-bound assets such as constellations, artworks, maps, scientific diagrams, cultural artifacts, species, historical objects, named places, or famous structures include approved source/provenance and verification requirements. Random generated approximations fail the run.
   - `demo_support.yaml` marks simple Cat1/Cat5 activities as `supported`, Cat5 runtime-judgment cases as `degraded`, and UI-heavy or unsupported mechanics as `unsupported` instead of claiming they are playable.

11. Mapping checks pass when mapping is required:
   - `mapping=` resolves through `MAPPING_ROOT/_index.yaml`.
   - Entity-specific facts, IB concepts, related concepts, bridge prerequisites, and tier language are grounded in the mapped YAML.
   - Parameterized rows use placeholders instead of inventing entity-specific claims.

12. Review and logging are complete for generated packages:
   - The package passes the 10-dimension rubric in `program.md`.
   - A separate reviewer agent checks every generated package against the same 10 dimensions, the migrated package depth floor, mechanic fidelity, asset-brief coherence, and package-file consistency.
   - Reviewers explicitly fail structurally valid but thin/generic packages that do not meet the migrated package depth floor.
   - Any reviewer FAIL or credible uncertainty is repaired before logging; the repaired package is re-reviewed by a fresh separate reviewer agent or by the original reviewer after reading the changed files.
   - Reviewers fail packages whose unexpected/no-response branch policies are generic clones, keyword-substitution rows, or repeated Step 3 round rows rather than beat-specific runtime behavior.
   - `runs/<run_id>/review_notes.md` records reviewer-agent name/id when available, package scope, PASS/FAIL/N/A evidence, repairs made, and final reviewer outcome.
   - `results.tsv` receives one row for each generated package.
   - `runs/<run_id>/generated_activity_ids.txt` includes each generated clean `activity_id`.
   - `runs/<run_id>/run_manifest.yaml` links each generated assignment row to `runs/<run_id>/activity_packages/<activity_id>/`, its `base_activity_id`, its adaptation brief when present, and `results.tsv`.
   - `results.tsv` `filename` points at the run-local package directory, not a reused canonical package.
   - The processed assignment row is changed from `- [ ]` to `- [x]`, keeps or records the clean `activity_id=<base_activity_id>`, and records `package_path=runs/<run_id>/activity_packages/<activity_id>` so checked assignments point to the package produced by that run.

13. Human review dashboard is generated:
   - `runs/<run_id>/review.html` exists before the final report.
   - The dashboard is generated with `python3 scripts/generate_run_review.py runs/<run_id>` and validated with `python3 scripts/generate_run_review.py --validate runs/<run_id>`.
   - The dashboard satisfies `review_dashboard.md`: self-contained light-theme HTML, a `Review Dashboard Workflow` section with generation and validation commands, concise clickable cards for generated/enriched/audited packages, full detail dialog/page content, visual runtime beat maps with extracted source rows, grouped tag colors, search/filter/sort controls, asset usage timelines for image/display dependencies, distinct `Asset dependencies`, `Display beats`, and `Image items` labels, blocked-preview handling, clear missing-decision versus inline-marker counts, per-blocked-card `Minimum To Unblock` sections below capability flags, colored inline blocked marker chips, blocked-preview scorecards, reason guide, reviewer coverage, 10-dimension review criteria, per-package scorecard results with why notes, checks, residual risks, and resolving local links.
   - If resolved blockers exist, the dashboard includes a blocking reason guide, a resolved contract items section, and per-card resolved blocker tags; these callouts do not count as blocked cards or failed package status.
   - The dashboard includes an extensibility overview and per-card extensibility details for reusable slots such as `{runtime_entity}`, `{shared_feature}`, `{matched_color}`, or approved asset-set replacements.
   - The dashboard preserves the editorial design language defined in `review_dashboard.md` §"Design language": warm-paper palette, single indigo accent, serif display title and dialog headings, hairline-divided panels (no card-within-card), tabular numerals on numeric columns, indigo/amber accent rails on activity/blocked cards, and a status-dot run indicator.
   - The dashboard provides in-file preview for every linked `.md`/`.yaml`/`.txt` per `review_dashboard.md` §"In-file preview": raw content embedded as `<template>` elements, a dedicated preview `<dialog>` renders Markdown inline and YAML/text in a code block, plain click previews while modifier-click and the "Open in new tab" link still navigate.
   - `runs/<run_id>/run_manifest.yaml` records the dashboard path, and the final report includes it.

14. Existing-run source-intent audits are patched without full rerun when requested:
   - `runs/<run_id>/source_comparison/source_intent_audit.yaml` exists with one entry per source row.
   - `scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate` passes.
   - `product_review_matrix.html` shows intent alignment separately from category/mechanic/capability status.
   - High-severity `intent_drift` rows are either repaired in the specific affected package or explicitly left as product-review findings.

15. Final report is clear:
   - State how many packages were generated.
   - State how many existing packages were enriched or audited as already compliant.
   - List any blocked assignments and the exact reason.
   - List any resolved blockers that were allowed by product-contract override.
   - Summarize source-intent drift and product-decision counts when a source comparison audit exists.
   - Summarize demo support coverage: generated packages with `supported`, `degraded`, or `unsupported` demo status, and any package where demo export was explicitly disabled.
   - Summarize extensibility coverage for reusable or parameterized activities.
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
