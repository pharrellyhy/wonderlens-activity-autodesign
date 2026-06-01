# Codex Goal: Autonomous Activity Generation

Use this file as the `/goal` target for running the WonderLens autonomous activity generation loop.

## Goal

Generate or triage WonderLens activity assignments from `assignments.md` using the current authoring workflow in `program.md`, `templates.md`, `run.md`, and the migrated five-required-file activity package contract.

For source-derived batches, preserve the original source design's play frame. A generated package may keep the mechanic/category labels and still fail if it changes the child role, interaction sequence, story frame, or required child action without product approval.

For the current workbook-derived concept batch, use `inputs/original_activity_concepts_2026-05-29.tsv` as the committed source-intent baseline. Treat `inputs/source_activity_concepts.md` as a normalized helper for English naming, mechanics, asset hints, and capability metadata only. If the TSV row and normalized helper disagree, the TSV row controls unless product approval for the adaptation is recorded.

Each run must also create a provenance directory under `runs/<run_id>/` so generated packages, blocked briefs, and constrained blocked design previews can be traced back to the exact `/goal` session.

For fresh assignment generation, the assignment `activity_id=` value is a clean base slug. Strip any trailing `_rYYYYMMDD_HHMMSS` suffix from copied rows, keep the clean base slug as the package `activity_id`, and write the actual package under `runs/<run_id>/activity_packages/<base_activity_id>/`. Enrichment-only maintenance may update existing checked canonical packages under `activities/<activity_id>/` in place. Do not write fresh rerun packages directly under `activities/` unless a later explicit promotion step asks for that.

Direct demo export is enabled by default for this full generation goal. Every generated package must include optional package-local demo extensions unless the user explicitly disables demo export for the run or the package is only a blocked preview:

```text
demo_support.yaml
asset_manifest.yaml
```

These files do not replace the five required package files. They make the generated package direct-demo-import ready by declaring demo support status, explicit entity binding, separate runtime assets, reference-bound provenance, and unsupported/degraded mechanic gates.

The default image-asset behavior for ordinary scoped generation is `asset_build=manifest_only`: generate and validate asset requirements with nullable output paths, but do not create binary image files. For a larger/full production pass, set `asset_build=generate_and_curate` at run start so autodesign creates package-local PNG assets before consumer validation. If the user explicitly requests `asset_build=generate_illustrative`, `asset_build=curate_reference`, or `asset_build=generate_and_curate`, run the post-package asset build phase with `scripts/build_activity_assets.py` after package validation and verify it with `scripts/validate_asset_build_outputs.py`. Reference-bound assets may use agent-proposed candidates only before source acceptance; final outputs must use approved originals, licensed/internal sources, official or verified source URLs, or verified data/redraws, never random generated approximations. The builder must consume preaccepted package-local source originals and source metadata; it must not create its own accepted provenance record. Use `docs/activity_asset_generation_workflow.md` for the runtime PNG workflow and current style contract.

Generated illustrative image assets must follow the current WonderLens activity asset style: flat Nordic children's illustration for the quiet white prototype, broad flat fills, sparse arc-eye/texture linework, restrained boho pastels, clean negative space, and no generic chibi/toy vocabulary or dimensional modeling. Generate square source art. Background scene assets should be full-bleed 512x512 images that can be clipped by the round lens; item, object, and character assets should be separate centered PNGs with generous clean white padding. Final runtime PNGs should be `512x512` unless the manifest explicitly requests a different or additional larger variant. Do not bake in device chrome: no circular/oval mask, lens border, rim, vignette, black corners, transparent margin, colored border, readable text, letters, numbers, logos, watermark, contact sheet, or UI labels. Store outputs only in the current package-local asset locations declared by `asset_manifest.yaml`.

If the user supplies a scope such as "only Batch 5" or "last batch", process only that scoped assignment subset in the run-start snapshot. If the user says the product contract now allows minimum-to-unblock decisions, treat prior capability probes as generation-ready under `product_contract_override=minimum_unblock_allowed`: generate normal packages with the five required files plus any enabled demo extensions, record formerly blocking dependencies as resolved blocker annotations, and keep those callouts visible in `review.html`.

## Full-Pass Agentic Pipeline Contract

For a larger/full activity generation pass, the main agent is the master
orchestrator. It owns run scope, source snapshots, blocking decisions,
credentials, server lifecycle, final acceptance, commits, and user reporting.
It should delegate bounded work to separate agents with disjoint ownership:

- source-intent auditor, before and after package writing;
- activity package writer, text only;
- scene/object/item asset generator, image only;
- package/import contract validator;
- fullstack-demo dialogue quality validator;
- WonderLens AI dialogue quality validator;
- image quality validator;
- dialogue quality improver;
- WonderLens AI dialogue quality improver;
- image quality improver;
- final independent reviewer.

Fullstack-demo and WonderLens AI are direct consumers, not content-improvement
steps. They must load or generate runtime artifacts from the package as
provided, preserve package runtime AI instructions in `step_instructions` or
equivalent runtime prompts, and report failures with ownership: package-owned,
fullstack-owned, WonderLens-owned, or product-capability decision. Do not hide a
package problem by rewriting the source play frame, child role, required child
action, background/context promise, or asset contract inside either consumer.

Source-intent auditing must happen before package writing to lock the original
play frame, child role, device role, sequence, required child action,
real/reference asset requirement, background/context promise, allowed
adaptation, and blocked/degraded capability reason. It must happen again after
package writing and downstream conversion/live runtime evidence. Unresolved
`intent_drift` blocks acceptance, `results.tsv` logging, assignment checkoff,
and full-pass scale-up.

## Recommended `/goal` Command

```text
/goal Execute GOAL.md end to end using run.md. Initialize run provenance, honor any user-specified assignment scope or product-contract override, audit/enrich checked activity packages that have an explicit package_path or canonical activities/<activity_id>/ directory against the current migrated package depth floor with separate reviewer-agent evidence, then process the run-start unchecked assignment snapshot exactly once in order. Direct demo export is enabled by default unless the user explicitly disables it. Default asset_build=manifest_only unless the user explicitly requests asset generation or reference curation; for generate_illustrative, curate_reference, or generate_and_curate, run scripts/build_activity_assets.py after package validation, apply the current WonderLens activity asset workflow and style from docs/activity_asset_generation_workflow.md, and validate scripts/validate_asset_build_outputs.py before review.html. For each generation-ready row, preserve source-promise alignment from the original source design, including original play frame, child role, interaction sequence, required child actions, non-negotiable elements, allowed V1 adaptations, and product dependencies. For workbook-derived rows, derive source-promise fields from the original workbook row first; for the current workbook batch, use inputs/original_activity_concepts_2026-05-29.tsv as the committed workbook export and treat inputs/source_activity_concepts.md as a normalized helper only. If the normalized row weakens sequence, role, real-asset requirements, or background/context requirements, repair the source row or record product-approved adaptation before generation. Use the assignment activity_id as a clean base slug, strip any copied _rYYYYMMDD_HHMMSS suffix, and generate a passing package under runs/<run_id>/activity_packages/<base_activity_id>/ with the five required files plus demo_support.yaml and asset_manifest.yaml, and with tag_block.yaml activity_id matching the clean base slug; for blocked rows, record a blocked brief plus constrained blocked design preview and continue. If product_contract_override=minimum_unblock_allowed is active, generate formerly blocked rows as normal packages, replace invalid blockers with resolved blocker annotations, and still show those resolved dependencies in review.html. Include extensibility notes for every package so reviewers can see whether the activity can be reused with other entities, properties, or asset sets. Do not append results.tsv or mark a generated assignment complete until reviewer issues are repaired and re-reviewed. After final validation, generate and validate runs/<run_id>/review.html according to review_dashboard.md. For workbook-based source comparison, every source_intent_audit.yaml entry must include workbook_evidence and the matrix validation must use --strict-workbook-intent. Stop only on a hard workflow failure that makes later rows unsafe. Use GOAL.md success criteria as the completion contract and report generated, enriched, blocked, resolved blockers, demo support coverage, asset build mode/output status, source-intent drift, extensibility coverage, reviewer-agent coverage, review dashboard path, checks, and residual risks.
```

For a larger/full production pass, add `asset_build=generate_and_curate` to the
invocation and treat the Full-Pass Agentic Pipeline Contract above as mandatory
rather than optional. Full-pass acceptance requires source-intent, package/import,
fullstack dialogue, WonderLens AI dialogue, image QA, repair-loop, and final
independent-review evidence before logging/checkoff.

## Success Criteria

The goal is complete only when all of the applicable criteria below are met.

1. Setup context is loaded:
   - `GOAL.md`
   - `program.md`
   - `templates.md`
   - `run.md`
   - `review_dashboard.md`
   - `docs/activity_asset_generation_workflow.md`
   - `runs/README.md`
   - `activities/README.md`
   - `activities/_schema/tag_block.schema.json`
   - `activities/_schema/demo_support.schema.json`
   - `activities/_schema/asset_manifest.schema.json`
   - `docs/activity_vocabulary.md`
   - `docs/game_styles.md`
   - `assignments.md`
   - `inputs/original_activity_concepts_2026-05-29.tsv` when processing workbook-derived source rows from the current workbook batch
   - Any `concept_source=file#id` or `asset_requirements=file#id` companion files referenced by pending assignment rows
   - `entity_guidance.md` and `conversation_bridge.md` when mapping or warm/cold bridge handling is required

2. Run provenance is initialized before assignment processing:
   - A `run_id` is created in `YYYYMMDD_HHMMSS_<short_label>` format.
   - `runs/<run_id>/run_manifest.yaml` exists with `status: in_progress`, source files, mapping root, output lists, and summary counters.
   - `runs/<run_id>/assignment_snapshot.md` preserves unchecked assignment rows pending at run start.
   - `runs/<run_id>/generated_activity_ids.txt`, `activity_packages/`, `adaptation_briefs/`, `blocked_briefs/`, `blocked_designs/`, `source_snapshots/`, `source_intent_audits/`, and `review_notes.md` are initialized.
   - Any user-specified batch/scope filter, product-contract override, `asset_build` mode, and `full_pass_pipeline` flag are recorded in `run_manifest.yaml` `source` or `notes`.

3. Assignment rows are processed in order:
   - Only unchecked `- [ ]` rows are processed.
   - The run-start `assignment_snapshot.md` is the queue; each snapshot row is visited at most once per run, even if a blocked row remains unchecked for a future product decision.
   - `assignment_type` is parsed or inferred.
   - `activity_concept=` is used for concept-led rows; legacy concept aliases are normalized before Phase 0.
   - Source-promise cues are extracted when the source is richer than a simple entity/category row: original play frame, child role, interaction sequence, required child actions, and non-negotiable source elements.
   - If a normalized assignment paraphrase conflicts with the original source design, the original source design controls unless product approval is recorded.
   - For workbook-derived rows, the source-promise cues are derived from the workbook row before using any normalized source snapshot. For the current workbook batch, `inputs/original_activity_concepts_2026-05-29.tsv` is the committed workbook export to cite in briefs and reviews. Any lossy normalized source row must be repaired, blocked, or explicitly recorded as a product-approved adaptation.
   - Source concepts may be Chinese, but generated adaptation briefs and package files are English-only.

4. Phase 0 adaptation is completed when required:
   - `activity_concept`, `match_pattern`, and `capability_probe` rows always receive an `adaptation_brief`.
   - `entity_activity` rows receive an `adaptation_brief` when mapping, category, mechanic, trigger, or scaffold fit needs resolution.
   - Referenced `concept_source` and `asset_requirements` rows are loaded before the brief is written.
   - The brief records `input_mode`, source-promise alignment, `canonical_mechanic`, readiness, trigger condition, mapping use, asset dependency, product capability flags, scaffold choice, and assumptions.
   - For workbook-derived rows, the brief records workbook-backed evidence for source-promise alignment instead of only repeating the normalized source description.
   - If `asset_policy` or companion asset rows are present, the brief copies them into `asset_dependency` instead of inferring image needs from prose.
   - For full GOAL.md runs, `demo_export` defaults to `true` unless explicitly disabled. The brief records demo support classification and asset manifest requirements for every generation-ready package.
   - `asset_build` defaults to `manifest_only` unless explicitly overridden. The brief records enough `source_strategy`, `transformation_policy`, variants, fallbacks, and provenance requirements for a later asset build to run without changing the activity design.
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
   - If `product_contract_override=minimum_unblock_allowed` is active, do not leave the row blocked solely for a minimum-to-unblock decision. Generate the normal package with the five required files plus any enabled demo extensions, record the former blocker in `spec.md` `## Resolved Product Contract Notes`, record affected runtime beats in run provenance, and record `resolved_blockers` / `resolved_blocker_types` in `run_manifest.yaml`. Raw `RESOLVED BLOCKER` comments may appear in runtime-facing `prod.md` only when the target consumer ignores them safely; WonderLens AI runtime generation must not receive leakage markers unless the downstream converter strips or accepts them.
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
   - Runtime beats may use existing `AI says` exact dialogue or the newer `Runtime AI instruction` plus `Example AI line` contract. A behavior instruction must preserve source frame, required content, branch policy, safety/product constraints, and screen/state expectation, and it must be rich enough to convert into downstream `step_instructions`: goal/action, tier or length constraint, emotion/tone, child progress evidence, branch behavior, and activity/source frame guardrail.
   - Direct-consumer and full-pass packages include a machine-convertible `**Runtime AI instruction:** Goal: ... Constraint: ... Tone: ... Progress evidence: ... Branch behavior: ... Frame/source guardrail: ...` line for every live beat, including Step 1, Step 2, each Step 3 round, Cat5 synthesis when present, celebration, closing, and early-exit behavior where applicable. `AI says` and `Example AI line` may remain as examples, but are not sufficient by themselves for portable downstream loading.
   - Step 3 round headings use parseable ASCII `**Round N -- Short Scenario:**` form. Cat5 packages distinguish collection rounds from synthesis and celebration, and synthesis instructions name collection criterion, accepted evidence, item-combination behavior, and final story/summary format.
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
   - The loop does not generate or store image files during package authoring; image files are created only by an explicit post-package asset build mode.
   - When demo export is enabled, `asset_manifest.yaml` contains separate runtime asset entries, not a contact sheet as the runtime asset.
   - `asset_manifest.yaml` uses `style_id: wonderlens_device_mint_soft_3d`, round-device safe-area rules, target variants, nullable path slots, and fallback behavior.
   - Illustrative assets use the current WonderLens activity asset style from `docs/activity_asset_generation_workflow.md`: flat Nordic children's illustration, quiet white prototype fit, broad flat fills, sparse linework, restrained boho pastels, clean negative space, and no generic chibi/toy vocabulary or dimensional modeling.
   - Illustrative assets are square 512x512 PNGs unless the manifest requests another size. Scene assets are full-bleed square images that can be clipped by the round lens; item, object, and character assets are separate centered PNGs with generous clean white padding. They do not include circular/oval masks, lens borders, rims, vignettes, black corners, transparent margins, colored borders, readable text, letters, numbers, logos, watermarks, contact sheets, or UI labels.
   - Required assets include at least one final runtime PNG at `512x512` or larger, with `512x512` preferred unless the manifest explicitly requests an additional larger variant. Smaller `64px`/`128px` variants are thumbnails only and cannot be the only built output.
   - Reference-bound assets such as constellations, artworks, maps, scientific diagrams, cultural artifacts, species, historical objects, named places, or famous structures include approved `source_strategy`, `transformation_policy`, source/provenance, and verification requirements. Random generated approximations fail the run.
   - If `asset_build=manifest_only`, nullable asset paths are acceptable. If a stronger asset build mode is requested, `scripts/build_activity_assets.py runs/<run_id> --mode <mode>` writes final runtime PNGs under package-local `assets/`, updates package-relative variant paths in `asset_manifest.yaml`, writes `generated_assets/asset_outputs.yaml`, `reference_sources.yaml`, and `qa_notes.yaml`, and `scripts/validate_asset_build_outputs.py runs/<run_id>` passes before the dashboard is finalized. Reference-bound outputs require accepted `assets/sources/<asset_id>__source_metadata.yaml` with source type, license, storage permission, sha256, verification timestamp, and reviewer agent.
   - `demo_support.yaml` marks simple Cat1/Cat5 activities as `supported`, Cat5 runtime-judgment cases as `degraded`, and UI-heavy or unsupported mechanics as `unsupported` instead of claiming they are playable.

11. Mapping checks pass when mapping is required:
   - `mapping=` resolves through `MAPPING_ROOT/_index.yaml`.
   - Entity-specific facts, IB concepts, related concepts, bridge prerequisites, and tier language are grounded in the mapped YAML.
   - Parameterized rows use placeholders instead of inventing entity-specific claims.

12. Review and logging are complete for generated packages:
   - The package passes the 10-dimension rubric in `program.md`.
   - A separate reviewer agent checks every generated package against the same 10 dimensions, the migrated package depth floor, mechanic fidelity, asset-brief coherence, and package-file consistency.
   - A separate source-intent auditor agent checks every source-derived, concept-led, workbook-derived, and pilot-validation package or blocked/degraded artifact against the original source row or run-local source snapshot.
   - `runs/<run_id>/source_intent_audits/` contains one audit file per audited row, recording original play frame, child role, device role/action, interaction sequence, required child actions, real/reference asset requirement, required background/context information, generated-package evidence, downstream conversion evidence when available, verdict, repair requirement, and re-review outcome.
   - No accepted package has unresolved source-intent `intent_drift`. Drift is either repaired and re-reviewed or explicitly left as a product-review finding that prevents generated package acceptance/checkoff for that row.
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
   - Every audit entry includes `workbook_evidence`, a short English note naming the workbook detail used to judge the source play frame.
   - `scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --strict-workbook-intent --validate` passes.
   - `product_review_matrix.html` shows intent alignment separately from category/mechanic/capability status.
   - High-severity `intent_drift` rows are either repaired in the specific affected package or explicitly left as product-review findings.

15. Final report is clear:
   - State how many packages were generated.
   - State how many existing packages were enriched or audited as already compliant.
   - List any blocked assignments and the exact reason.
   - List any resolved blockers that were allowed by product-contract override.
   - Summarize source-intent drift and product-decision counts when a source comparison audit exists.
   - Summarize demo support coverage: generated packages with `supported`, `degraded`, or `unsupported` demo status, and any package where demo export was explicitly disabled.
   - Summarize `asset_build` mode, asset output status, and any reference-bound assets still waiting for approved sources.
   - Summarize extensibility coverage for reusable or parameterized activities.
   - Include the `run_id` and `runs/<run_id>/run_manifest.yaml` path.
   - Include the `runs/<run_id>/review.html` path.
   - Report reviewer-agent coverage: which packages were reviewed, which were edited by reviewers or repaired after review, and whether all generated packages received independent PASS evidence.
   - List verification commands run and their results.
   - State any residual risk or follow-up product decision.

16. Full-pass agentic validation gates pass when the run is a larger/full
    production pass:
   - `run_manifest.yaml` records `source.full_pass_pipeline: true` and
     `source.asset_build: generate_and_curate`.
   - The master orchestrator records delegated-agent ownership and evidence for
     source-intent audit, text-only package writing, image-only asset
     generation, package/import validation, fullstack dialogue QA, WonderLens
     AI dialogue QA, image QA, dialogue repair, WonderLens AI dialogue repair,
     image repair, and final independent review.
   - A pre-package source-intent audit locks the original play frame, child
     role, device role/action, interaction sequence, required child action,
     reference/real asset requirement, background/context promise, and allowed
     adaptation before `prod.md` is written.
   - The post-package source-intent audit rechecks `spec.md`, `prod.md`,
     `tag_block.yaml`, `demo_support.yaml`, `asset_manifest.yaml`, fullstack
     converted `step_instructions`, WonderLens AI runtime artifacts, live or
     runtime-equivalent dialogue transcripts, and image QA findings.
   - Package/import validation runs before live dialogue QA. It verifies that
     fullstack-demo imports the package without content improvement, asset paths
     resolve, unsupported/degraded gates remain honest, and converted
     `step_instructions` preserve runtime AI instruction quality instead of
     falling back to generic defaults. Cat5 imports must preserve any synthesis
     instruction separately from collection rounds and celebration.
   - WonderLens AI runtime validation runs before full-pass acceptance. It
     verifies that generated/loaded runtime artifacts preserve package
     `step_instructions` quality, unsupported/degraded packages remain honest,
     runtime-facing conversion input avoids leakage markers such as raw
     `RESOLVED BLOCKER` comments unless the converter strips or accepts them,
     and runtime behavior does not add unsupported sensing, hidden-state claims,
     false screen claims, or mechanic changes.
   - Before comparing or accepting dialogue quality across fullstack-demo and
     WonderLens AI, prove runtime-facing package input is marker-free. This
     precondition must pass with no matches:
     `! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md`.
   - Fullstack and WonderLens AI dialogue validators exercise multiple child
     input strategies, including ideal, minimal, wrong, off-topic,
     help/confusion, premature done, silence/no response, and unsupported
     request where the runtime supports them.
   - Image QA independently checks style consistency, asset role, crop safety,
     scene/dialogue alignment, reference fidelity, object readability, and
     no-text/no-label/no-device-chrome constraints.
   - Dialogue and image repair loops classify each failure as package-owned,
     fullstack-owned, WonderLens-owned, image-owned, or product-owned. Package
     and image-owned issues are repaired in autodesign and revalidated;
     downstream-owned issues are recorded as follow-up unless the user
     explicitly expands scope.
   - The final independent reviewer reads final packages, source-intent audits,
     package/import reports, fullstack and WonderLens AI transcripts, image QA
     reports, repair notes, and dashboard output before issuing the final
     pass/fail verdict.

## Assignment Type Names

Use these names in new `assignments.md` rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked |

Legacy concept aliases should be treated as `assignment_type=activity_concept` with `activity_concept=<value>`.
