# Run Instructions - Autonomous Activity Package Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.
> When launched from Codex `/goal`, use `GOAL.md` as the objective and success criteria, and use this file as the execution procedure.

## Setup (one-time, do this first)

Entity mapping root: `MAPPING_ROOT=data/mappings_dev20_0318` (repo-relative). Use `MAPPING_ROOT/_index.yaml` as the entity registry whenever mapping data is required.

1. Read `GOAL.md` - goal, assignment type names, and success criteria.
2. Read `program.md` fully - constraints, migrated package format, rubric, and seed exemplars.
3. Read `templates.md` fully - Template 0 reference, mechanic adapters, Cat1/Cat5 category modifiers, and pillar/style scaffolds.
4. Read `docs/game_styles.md` - game style taxonomy reference.
5. Read `docs/activity_asset_generation_workflow.md` - runtime PNG workflow, reference curation rules, and current illustrative style contract.
6. Read `activities/README.md` - five required package files and optional demo-extension contract.
7. Read `activities/_schema/tag_block.schema.json`, `activities/_schema/demo_support.schema.json`, `activities/_schema/asset_manifest.schema.json`, and `docs/activity_vocabulary.md` - tag-block schema, demo-extension schemas, and current enum vocabulary.
8. Read `docs/activity_tag_block_usage.md` and `docs/activity_tag_block_progression_guide.md` - field ownership, recap/dashboard usage, and progression guidance.
9. Read `entity_guidance.md` and `conversation_bridge.md` when an assignment is mapping-informed or requests warm/cold bridge handling.
10. Read `assignments.md` - work queue.
11. Verify `activities/` exists with `_schema/tag_block.schema.json`.
12. Verify `results.tsv` exists and has the current header. If it is missing, create it with this header:

```
assignment	entity	category	tier	pillar	style	status	d1_tech	d2_hook_transition	d3_edge	d4_ib	d5_tier	d6_dialogue	d7_screen	d8_mapping	d9_game_feel	d10_pillar_fidelity	filename	timestamp
```

13. Create a run provenance directory before processing the first assignment:

```
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── activity_packages/
├── adaptation_briefs/
├── blocked_briefs/
├── blocked_designs/
├── source_snapshots/
├── source_intent_audits/
├── review_notes.md
└── review.html                  # generated at end of run
```

Use `run_id=YYYYMMDD_HHMMSS_<short_label>`, for example `20260509_113000_activity_concepts`. If the user supplies a run label, slugify it for `<short_label>`; otherwise infer a short label from the assignment batch, such as `activity_concepts`, `mapping_batch`, or `mixed_assignments`.

14. Write `assignment_snapshot.md` with the unchecked `- [ ]` rows that are pending at run start, preserving their original order and section headings where practical. If the user explicitly scoped the run to a batch or named assignment subset, include only that scoped subset in the snapshot and record the scope in `run_manifest.yaml`.

15. Initialize `run_manifest.yaml`:

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
  assignment_scope: "<all unchecked rows or explicit user scope>"
  product_contract_override: "<none|minimum_unblock_allowed>"
  asset_build: "<none|manifest_only|generate_illustrative|curate_reference|generate_and_curate>"
  full_pass_pipeline: <true|false>
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
  source_intent_audits: []
  review_dashboard:
checks: []
notes:
  - "Fresh assignment generation writes run-local packages under runs/<run_id>/activity_packages/<base_activity_id>/ with clean activity_id values."
  - "Existing checked-package enrichment may update canonical activities/<activity_id>/ packages in place, but unchecked generation-ready rows must not reuse old canonical package directories."
  - "If product_contract_override=minimum_unblock_allowed is active, formerly blocking dependencies generate as resolved blocker annotations instead of blocked rows."
  - "Full GOAL.md runs default demo_export=true unless explicitly disabled; generated packages add demo_support.yaml and asset_manifest.yaml as optional extension files while the five canonical files remain required."
  - "Default asset_build=manifest_only; binary image assets are created only by an explicit post-package asset build phase."
  - "Larger/full production passes set full_pass_pipeline=true and asset_build=generate_and_curate, then require source-intent, package/import, fullstack dialogue, WonderLens AI dialogue, image QA, repair-loop, and final independent-review evidence before acceptance."
```

16. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Run id: <run_id>. Starting activity package loop."

## Full-Pass Master/Subagent Pipeline

Ordinary scoped `/goal` runs may use the default `asset_build=manifest_only`.
When the user asks for a larger/full production pass, set
`source.full_pass_pipeline: true` and `source.asset_build:
generate_and_curate` in `run_manifest.yaml` before assignment processing.

The main agent is the master orchestrator. It owns run scope, source snapshots,
blocking decisions, credentials, server lifecycle, final acceptance, commits,
and user reporting. Delegate bounded tasks only when ownership is disjoint and
the delegate can return concise evidence.

Required delegated roles for a full pass:

- Source-intent auditor: text/package review only; checks original source
  promise before and after package writing.
- Activity package writer: text only; writes the five required files plus demo
  extensions and runtime AI instructions; never generates or selects image
  files.
- Scene/object/item asset generator: image only; creates or curates PNG assets
  from `asset_manifest.yaml`, approved sources, and the style contract; never
  rewrites package prose or activity flow.
- Package/import contract validator: loader/conversion only; validates
  fullstack import, asset path resolution, converted `step_instructions`, and
  no content improvement.
- Fullstack dialogue quality validator: live or runtime-equivalent dialogue
  only; runs multiple child-input strategies against imported packages.
- WonderLens AI dialogue quality validator: WonderLens AI runtime only; checks
  generated/loaded runtime artifacts and dialogue behavior.
- Image quality validator: visual QA only; checks style, crop safety,
  scene/dialogue alignment, reference fidelity, and no text/labels/chrome.
- Dialogue quality improver: text repair only; fixes package-owned runtime AI
  instruction gaps or records fullstack-owned follow-up.
- WonderLens AI dialogue quality improver: text/runtime repair triage only;
  fixes package-owned gaps or records WonderLens-owned follow-up.
- Image quality improver: image repair only; regenerates/curates/rebuilds
  assets and updates asset QA records; no activity-flow rewrites.
- Final independent reviewer: cross-artifact review; reads final packages,
  audits, import reports, transcripts, image QA, repairs, and dashboard output.

Fullstack-demo and WonderLens AI are direct consumers, not authoring fallbacks.
They must load generated packages as provided. If either runtime improves,
weakens, rewrites, or reinterprets activity content to make it pass, the run
must classify that as a consumer/runtime finding or a package repair need; do
not hide the issue in downstream output.

## Existing Package Enrichment Pass (do before unchecked assignment processing)

Before processing any unchecked assignment, audit existing migrated packages that may have been generated under older or looser standards. A checked assignment means "already generated"; it does not mean the package is exempt from current quality rules.

Scope for this pass:

- Checked `assignments.md` rows that include `package_path=<repo-relative package dir>`.
- Checked rows without `package_path` that include `activity_id=<id>` and have an existing canonical `activities/<id>/` package.
- Existing `activities/concept_*` packages produced by prior concept-led runs, especially when `program.md`, `templates.md`, `run.md`, or `GOAL.md` recently tightened the migrated package depth floor.
- Packages the user explicitly names for quality repair or enrichment.

For each scoped package:

1. Read `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml`.
2. Audit against the current package checks in this runbook, not only against the standard that existed when the package was first generated.
3. Spawn separate reviewer agents for package-quality review. When more than one package is in scope, partition packages into disjoint directory sets so reviewers can work in parallel without touching the same files.
4. Reviewer agents may make direct, minimal quality repairs inside their assigned package directories when the scope is explicit. They must not edit `assignments.md`, `results.tsv`, run manifests, or unrelated docs.
5. If the package is structurally valid but thin, enrich it in place. Preserve `activity_id`, directory name, tag-block enum values, recap/dashboard placeholders, stable asset IDs, and the five-required-file package contract.
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

Extract: assignment_type (if provided), activity_concept (if provided), legacy concept alias (if provided), concept_source (if provided), description/notes (if provided), source-promise cues (original play frame, child role, interaction sequence, required child actions, non-negotiable source elements), entity, category, tier, mechanic (if provided), pillar (if provided), style (if provided), scene (if provided), trigger_condition (if provided), mapping (if provided), asset_policy (if provided), asset_requirements / companion asset rows (if provided), product_capabilities (if provided), demo_export / demo_support hints (if provided), asset_build override (if provided), full-pass flag (if provided), start type (if provided), and output activity_id (if provided). Normalize any legacy concept alias to `activity_concept=` and infer `assignment_type=activity_concept` unless a more specific type is declared. For full GOAL.md runs, default `demo_export` to `true` unless the user or assignment explicitly sets it to `false`; default `asset_build` to `manifest_only` unless the user or assignment explicitly sets another supported value. For a larger/full production pass, override the ordinary default with `asset_build=generate_and_curate` and set `source.full_pass_pipeline: true`.

For unchecked generation-ready rows, treat `activity_id=` as `base_activity_id`. If the base value already ends in `_rYYYYMMDD_HHMMSS` because a prior run row was copied, strip that suffix first. The final package `activity_id` stays the clean `<base_activity_id>`, and the run-specific identity comes from the package path `runs/<run_id>/activity_packages/<base_activity_id>/`. This prevents fresh reruns from silently linking back to old canonical `activities/` package directories while keeping package IDs clean. The only exception is enrichment/audit of already checked rows, which intentionally uses the existing canonical package ID in place.

If `concept_source=` points to `file#concept_id`, read that repo-relative file and load the matching concept section before Phase 0. If `asset_requirements=` points to `file#asset_id`, read the same or referenced file and load the matching asset requirement section. Use the assignment row as the execution source of truth, and use the companion file as richer source / asset context. When a workbook row, source concept, and normalized assignment paraphrase disagree, preserve the original source design's play frame unless product explicitly approves the adaptation.

For the current workbook-derived concept batch, use `inputs/original_activity_concepts_2026-05-29.tsv` as the committed workbook source-intent baseline. Use `inputs/source_activity_concepts.md` only as a normalized helper for English naming, mechanic labels, capability notes, and asset hints. If the normalized helper or assignment paraphrase weakens the TSV row's child role, interaction sequence, required child action, real/reference asset requirement, or background/context requirement, repair the helper/assignment interpretation first or record an explicit product-approved adaptation before generation.

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
2. Identify `source_promise_alignment`: original play frame, child role, interaction sequence, required child actions, non-negotiable elements, allowed V1 adaptations, product dependencies, and alignment status. This is a required review field for concept-led rows and should be included whenever a source concept is richer than a simple entity/category assignment. For current workbook-derived rows, cite `inputs/original_activity_concepts_2026-05-29.tsv` evidence before normalized helper evidence.
3. Identify `canonical_mechanic` and `mechanic_confidence`. If `mechanic=` is specified, it wins unless it is outside the current enum. The mechanic cannot override the original source play frame; it only labels the repeated child action.
4. Decide `category_decision`, `readiness`, `trigger_condition`, `entity_role`, `observation_angle`, `focal_attribute`, mapping usefulness, asset dependency, product capability flags, and scaffold fit.
5. If `asset_policy` is provided, copy it into `adaptation_brief.asset_dependency.policy` instead of inferring asset need from prose. If companion asset rows are provided, normalize them into `adaptation_brief.asset_dependency.assets`.
   - When `demo_export=true`, each normalized asset row should include `asset_role`, `style_id`, `accuracy_mode`, `source_strategy`, `transformation_policy`, `screen_targets`, `target_variants`, fallback behavior, and nullable path slots for the future asset pipeline.
   - Use `style_id: wonderlens_device_mint_soft_3d` unless the source explicitly provides an approved override.
   - Mark real-world factual/reference assets as `accuracy_mode: reference_bound` and require source/provenance plus verification behavior. Do not accept arbitrary generated approximations for constellations, artworks, maps, scientific diagrams, cultural artifacts, species, historical objects, named places, or famous structures.
   - For reference-bound assets, candidate proposal may use an agent/LLM, but final accepted sources must come from approved public-domain, official, licensed/internal, or verified educational/scientific sources. Record `source_strategy` and `transformation_policy`; never use `source_strategy: generated_illustrative` or `transformation_policy: generate_new` for reference-bound assets. The asset builder requires preaccepted package-local source metadata and must not create its own accepted provenance record.
6. Write the normalized adaptation brief to `runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml` if generation may proceed, or to `runs/<run_id>/blocked_briefs/<ordinal>_<assignment_slug>.yaml` if blocked.
7. If `readiness=blocked_until_product_decision`, first check whether the run has `product_contract_override=minimum_unblock_allowed`.
   - Without the override, block only this assignment but still create a constrained design preview at `runs/<run_id>/blocked_designs/<ordinal>_<assignment_slug>.md`. The preview should follow the activity's likely `prod.md` step shape closely enough for human review, including detailed Step 1-5 and Step 3 rounds when applicable. Add short inline comments exactly where unsupported behavior appears, using this format: `> BLOCKED ELEMENT: <reason> -- <what product/design decision is needed>`. Use the same blocker reason consistently when one missing product decision affects multiple beats; each inline marker is an occurrence, not a separate missing decision. Update `run_manifest.yaml` with a `blocked_assignments` entry, including both `brief_path` and `design_preview`, and increment `summary.blocked_count`; do not create valid package files under `runs/<run_id>/activity_packages/` or `activities/`, append `results.tsv`, mark the assignment complete, or commit mid-row. Continue to the next unchecked assignment unless this revealed a hard workflow failure that prevents safe processing of later rows.
   - With the override, treat the row as generation-ready. Save the brief under `adaptation_briefs/`, set `readiness=generate_with_assumptions`, and copy every former missing decision into `resolved_blockers`. In `spec.md`, add `## Resolved Product Contract Notes`; in run provenance, record the former blocker and affected runtime beats. `prod.md` may include review-only resolved-blocker comments only when the target consumer ignores them safely. When targeting WonderLens AI conversion, do not feed raw `RESOLVED BLOCKER` markers into runtime generation unless the downstream converter explicitly strips or accepts them. Do not create a blocked brief, do not add `blocked_assignments`, and do not count the row as blocked.
8. If `readiness=generate_with_assumptions`, carry assumptions into `spec.md` under `## Adaptation Rationale`.
9. If assets are optional or required but generation proceeds, carry the normalized asset rows into `spec.md` `## Asset Brief`. `prod.md` may reference asset IDs and fallback behavior, but should not include raw image prompts.
10. For any prebuilt, displayed, or runtime-generated image dependency, also create `spec.md` `## Asset Usage Timeline` rows that make the image flow reviewable: `asset_id`, prebuilt/runtime timing, load or generation moment, first display step, visible step/round range, screen location, interaction/use, prompt/source summary, persistence or hide behavior, and fallback.
11. If generation proceeds, carry `canonical_mechanic` into `tag_block.yaml` `activity_signature.mechanic`.
12. If `demo_export=true`, classify demo readiness:
   - `supported` / `cat1_dialogue` for Cat1 dialogue, riddle, voice acting, prediction, imagination, or simple enumeration playable in the current demo.
   - `degraded` / `cat1_dialogue` for simple guided drawing or material build-step flows that can be represented honestly as text-guided child/caregiver self-report with declared step-card assets/fallbacks, no visual assessment, and no photo-verification claim.
   - `supported` / `cat5_collection` for simple Cat5 visible-property collection playable with catalog candidates.
   - `degraded` / `cat5_judgment` for Cat5 activities that need runtime judgment, such as beginning sound or semantic category, and must disclose catalog/text-simulated judgment.
   - `unsupported` / `none` for drawing, coloring, physical building, sorting/grouping UI, tournament, certificate, complex Cat3, visual verification, final-photo validation, before/after comparison, or any unimplemented UI/runtime dependency that cannot be represented by honest self-report.

### Step 1.2: Pre-package source-intent audit

For source-derived, concept-led, workbook-derived, pilot-validation, and full
pass rows, spawn a separate source-intent auditor before package writing. This
is a gate on the adaptation brief and writer instructions, not a review of the
finished package.

Write or initialize one row-level audit file:

```text
runs/<run_id>/source_intent_audits/<ordinal>_<activity_id>.md
```

The pre-package audit must compare the original source row or run-local source
snapshot against the normalized helper and adaptation brief. It records:

- original play frame;
- child role;
- device role/action;
- interaction sequence;
- required child actions;
- real/reference asset requirement versus illustrative asset allowance;
- required background/context information;
- non-negotiable source elements;
- allowed V1 adaptations;
- unsupported/degraded capability reason;
- package-writer constraints that must appear in `spec.md`, `prod.md`,
  `demo_support.yaml`, and `asset_manifest.yaml`;
- pre-package verdict: `aligned`, `minor_adaptation`, `intent_drift`, or
  `needs_product_decision`.

If the pre-package verdict is `intent_drift`, repair the adaptation brief or
source interpretation before writing package files. If the verdict is
`needs_product_decision`, block the row or record explicit product approval
before package writing. Do not let the activity package writer infer a
different role, sequence, required child action, real/reference asset, or
background/context promise from a normalized helper when the original source
row is more specific.

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
3. Cat1, Cat3, or Cat5 category modifier.
4. Pillar/style scaffold selected by the adaptation brief.

Use the composed scaffold as the activity's beat structure. Do not use the retired "Template A / Template B" split. If mapping-informed, ground creative variables in the selected dimensions and mapping attributes. If parameterized, use stable placeholders. If concept-only, avoid entity-specific claims. Cat3 hands-on/material workflows may generate when the product contract explicitly allows caregiver setup, material pacing, and honest completion evidence; otherwise they remain blocked or constrained previews.

The child's actual repeated action must match `canonical_mechanic`. Keep the selected `game_style` coherent with the mechanic, but do not let style override the requested action. If scaffold fit is weak, disclose it in `spec.md` or block this assignment before generation.

### Step 3: Generate the migrated activity package

Resolve the final package ID before writing files:

1. `base_activity_id`: assignment `activity_id=` if present, otherwise a stable lowercase snake_case slug derived from the concept/entity/mechanic.
2. Remove a trailing `_rYYYYMMDD_HHMMSS` suffix from `base_activity_id` when present.
3. `activity_id`: the clean `<base_activity_id>`.
4. `package_dir`: `runs/<run_id>/activity_packages/<activity_id>/`.
5. If `package_dir` already exists in the current run, stop and choose a non-conflicting clean slug before writing. Do not merge into or overwrite an existing package directory.
6. Record `base_activity_id`, `activity_id`, `activity_path`, `package_scope: run_local`, and `generation_policy: fresh_run_local_package` in `run_manifest.yaml`.

Create a complete `runs/<run_id>/activity_packages/<activity_id>/` package with the five required files:

```
runs/<run_id>/activity_packages/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

The activity package writer role is text-only. It may write package markdown,
YAML contracts, runtime AI instructions, branch policy, source guardrails,
asset requirements, and nullable `asset_manifest.yaml` paths. It must not
generate images, select final reference sources, copy PNGs, or rewrite the
activity to fit an image candidate. If source or asset constraints are unclear,
return to the adaptation/source-intent gate instead of inventing a convenient
visual or changing the child action.

Rules:

- `spec.md`: author/reviewer reference with premise, target, rationale, selection trigger, pillar/game style, optional `## Adaptation Rationale`, optional `## Asset Brief`, optional `## Asset Usage Timeline`, and `## Self-Evaluation Scorecard`.
- `prod.md`: runtime prompt guidance with Basic Info, Activity Overview, and full Interaction Flow. It must not contain a scorecard.
- `tag_block.yaml`: structured metadata matching `activities/_schema/tag_block.schema.json`.
- `recap.template.yaml`: child recap payload using the same focal attribute, role/badge, and next-step direction.
- `dashboard.template.yaml`: parent dashboard fragment using the same focal attribute and progression axis.
- `demo_support.yaml`: default extension for full GOAL.md runs unless demo export is explicitly disabled; declares status, UI template, support level, explicit entity binding, requirements, unsupported/degraded reasons, and consumer notes.
- `asset_manifest.yaml`: default extension for full GOAL.md runs unless demo export is explicitly disabled; declares separate runtime assets, `wonderlens_device_mint_soft_3d` style, screen targets, round safe area, roles, prompts/sources, variants, nullable file paths, and fallback behavior.

Runtime completeness rule:

- Every generated concept-led package should include `spec.md` `## Extensibility Notes` when the loop can be reused with other entities, properties, or asset sets. Name concrete reusable slots such as `{runtime_entity}`, `{shared_feature}`, `{matched_color}`, `{matched_shape}`, or a replaceable approved asset-set ID. If the package is intentionally not reusable, state why.
- Every concept-led package should include `spec.md` source-promise alignment notes. The notes must name the original play frame, child role, required child actions, allowed adaptations, and any product-approved source changes.
- For product-contract override runs, every former blocker must be visible as resolved review evidence: `spec.md` `## Resolved Product Contract Notes`, affected runtime beats recorded in run provenance, and `run_manifest.yaml` `resolved_blockers` / `resolved_blocker_types` for the generated activity. Use `prod.md` inline `RESOLVED BLOCKER` comments only when all target consumers ignore them safely; otherwise keep those markers out of runtime-facing conversion input and expose them in review artifacts.
- Every Step 3 round in `prod.md` must be fully expanded with either `AI says` exact dialogue or `Runtime AI instruction` plus `Example AI line`, child response branches, AI follow-up policy/branches, and screen state.
- Never write "same structure," "later rounds follow," "AI gives a riddle," or one-line summaries in generated `prod.md`.
- The migrated package may be shorter than legacy `designs/*_spec.md`, but it must not be thin. `spec.md` must explain the activity's concrete design intent, assumptions, constraints, asset/product dependencies, scaffold fit, and game-feel rationale. `prod.md` must be runnable without the operator inventing missing beats.
- Steps 1, 2, 4, and 5 also need concrete dialogue or runtime behavior contracts, branches, follow-ups, and screen states. Do not concentrate all detail in Step 3 while leaving the bridge, rules, magic moment, or closing generic.
- Runtime behavior contracts must be constrained enough for a live LLM and structured enough to convert into downstream `step_instructions`: include beat goal/action, tier or length constraint, emotion/tone, required story/setup or role-play frame, exact child challenge/action, child progress evidence, branch behavior, safety/product constraints, screen/state expectation, and what must not be skipped. A single example line is only a sample, not the whole runtime response.
- Direct-consumer and full-pass packages must provide a machine-convertible runtime instruction for every live beat, not only exact sample dialogue. Use the exact single-line label `**Runtime AI instruction:** Goal: ... Constraint: ... Tone: ... Progress evidence: ... Branch behavior: ... Frame/source guardrail: ...` for Step 1, Step 2, each Step 3 round, Cat5 synthesis when present, celebration, closing, and early-exit behavior where applicable. `AI says` and `Example AI line` may remain for human tone examples, but they are insufficient by themselves for portable downstream loading.
- Celebration/magic moment beats must not contain new required child gameplay. They may recap, reveal, synthesize, award, or ask an optional reflective closing-style wonder, but they must not ask a new binary choice, tool/action decision, photo, drawing step, or collection/challenge action. Move any source-required extra action into an explicit Step 3 round before celebration.
- Step 3 headings must be parseable ASCII headings in the form `**Round N -- Short Scenario:**`. For Cat5 packages, distinguish collection rounds from synthesis and celebration; synthesis instructions must name the collection criterion, accepted evidence, how collected items combine, and the required final story or summary format.
- Branch behavior must be beat- and round-specific. Unexpected and no-response child branches may share safety principles, but their text must name likely off-track or quiet behavior for this exact beat, and the AI follow-up must return to the current role, source action, challenge, asset/fallback, or screen state. Do not copy boilerplate such as "Child gives an unrelated answer, unsafe action, or asks to change the task", "Validate the idea, restate the safe rule", or "Model a tiny answer" across packages. Do not produce keyword-substitution rows that only swap in the activity title, mechanic, or round title.
- Step 3 branch rows must not repeat across rounds in the same package. If the same unexpected/no-response child behavior or AI follow-up appears in multiple rounds, rewrite each row around the current clue, choice, challenge, prior consequence, asset state, or completion target.
- Each Step 3 round must be distinct: named objective, different clue/challenge/action, child responses that exercise the canonical mechanic, branch-specific follow-ups, and a screen-state change.
- Generic warmth is insufficient. Fail and repair lines like "Great job," "try again," or "screen updates" when they are not tied to specific evidence, consequence, progress, or payoff.
- If `start=warm+cold`, document the bridge logic in `spec.md`; the runtime `prod.md` should still have a single converged Step 1 unless the assignment explicitly asks for both starts at runtime.
- Do not generate image files as part of this loop. When an activity uses AI-generated or displayed images, author the dependency in `spec.md` `## Asset Brief`, add a skimmable `## Asset Usage Timeline`, and reference the stable `asset_id` plus display location from the relevant screen description in `prod.md`.
- Do not make contact sheets the runtime asset contract. For demo export, write separate asset entries in `asset_manifest.yaml`; contact sheets may remain review-only artifacts under pilot asset workflows.
- For reference-bound assets, include approved source/provenance and verification notes in `asset_manifest.yaml`. If source/provenance is missing, mark demo support `degraded` with a limitation, `unsupported`, or leave demo export incomplete rather than pretending a random generated image is correct.
- For illustrative assets, use the current WonderLens activity asset style from `docs/activity_asset_generation_workflow.md`: flat Nordic children's illustration, broad flat fills, sparse arc-eye/texture linework, restrained boho pastels, generous negative space, direct 512x512 square source PNGs for subset and full-pass attempts, full-bleed scenes, and separate centered item/object/character/icon/badge/distractor PNGs with clean white padding.
- Do not bake device chrome or review layout into generated assets: no circular/oval mask, lens border, rim, vignette, black corners, transparent margin, colored border, readable text, letters, numbers, logos, watermark, contact sheet, multi-card sheet, or UI labels.
- Do not bake app-owned progress/control UI into generated assets: no progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or similar runtime interface markers. The app overlays progress and controls separately.
- For required assets, include at least one final runtime PNG at `512x512`, with larger variants allowed only when the manifest explicitly requests them. Tiny `64px`/`128px` variants are allowed only as secondary thumbnails, never as the only playable runtime output.

### Step 4: Self-evaluate and repair

Run through all 10 rubric dimensions from `program.md` Phase 3 against the actual package files. If any dimension FAILS:

1. Identify the specific issue.
2. Fix the relevant package file(s).
3. Re-evaluate.
4. Repeat until all dimensions PASS.

Dimension 1 may pass with formerly blocking capabilities only when `product_contract_override=minimum_unblock_allowed` is recorded and the package exposes those dependencies as resolved blockers. Dimension 8 only applies to mapping-informed designs. Score as N/A if no mapping. Dimensions 9 and 10 always apply. Dimension 10 checks mechanic fidelity + scaffold honesty, even though the legacy log column name remains `d10_pillar_fidelity`.

### Step 4.5: Independent scorecard review

Spawn a separate reviewer agent to independently check the same 10 dimensions against the completed package files before finalizing `spec.md`. This is mandatory for every generated package in an autonomous `/goal` run. If reviewer-agent tooling is unavailable, treat that as a hard workflow failure for package finalization because generated rows cannot be safely logged or checked off without independent review evidence.

For batch efficiency, reviewer agents may review disjoint package sets in parallel after each package is drafted, but each generated package still needs independent PASS evidence before `results.tsv` logging and assignment checkoff. Reviewer agents may propose repairs or directly edit their assigned package directories when explicitly scoped; any edited package must be rechecked and recorded in `review_notes.md`.

Reviewer instructions:

- Read `program.md` Phase 0 and Phase 3, the adaptation brief / `spec.md` `## Adaptation Rationale` when present, and the generated package at `runs/<run_id>/activity_packages/<activity_id>/`.
- Read `templates.md`, `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`.
- If the assignment has `mapping=`, also read the relevant mapping source, `entity_guidance.md`, and `conversation_bridge.md`.
- Evaluate the package files directly, not the authoring agent's claimed scorecard.
- Return PASS/FAIL/N/A for each dimension with brief evidence and concrete file/section references for any issue. For Dimension 10, explicitly confirm that Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic` and the adaptation brief's `canonical_mechanic` when present. When assets are referenced, also confirm the package contains a coherent `## Asset Brief`, that every referenced `asset_id` is defined, and that required assets have prompts/source, use steps, display behavior, and fallback behavior. When demo extension files are present, also confirm `demo_support.yaml` honestly gates supported/degraded/unsupported mechanics and `asset_manifest.yaml` uses separate runtime assets with round-screen safe areas, fallbacks, and reference-bound provenance where needed.
- Fail structurally valid but thin packages. The reviewer should explicitly check whether `spec.md` is decision-useful and whether `prod.md` contains enough concrete dialogue, branch reactions, screen state, game-feel payoff, and source-promise detail to run the activity without filling gaps.
- Fail packages whose unexpected/no-response branch policies are generic clones. The reviewer should confirm those branches are tied to the current mechanic and source frame, not repeated run-level filler.

If the reviewer flags any FAIL or credible uncertainty, fix the package, rerun the author self-evaluation, and spawn a fresh independent review. Only finalize the `## Self-Evaluation Scorecard`, append `results.tsv`, and mark the assignment complete after both the author check and independent reviewer check pass.

### Step 4.6: Post-package source-intent audit

For source-derived, concept-led, workbook-derived, pilot-validation, and
full-pass rows, return to the separate source-intent auditor agent before
accepting the package, blocked preview, or degraded artifact. This post-package
audit updates the row-level audit initialized in Step 1.2 and is separate from
the general 10-dimension scorecard review.

Write one audit file per row under:

```text
runs/<run_id>/source_intent_audits/<ordinal>_<activity_id>.md
```

The source-intent auditor must compare the original source row or run-local
source snapshot against the normalized helper, adaptation brief, pre-package
writer constraints, `spec.md`, `prod.md`, `tag_block.yaml`,
`demo_support.yaml`, `asset_manifest.yaml`, and downstream conversion/runtime
artifacts when available.

Each audit must record:

- original play frame;
- child role;
- device role/action;
- interaction sequence;
- required child actions;
- real/reference asset requirement versus illustrative asset allowance;
- required background/context information;
- non-negotiable source elements;
- allowed V1 adaptations;
- generated-package evidence with file/section references;
- downstream conversion evidence when available;
- live fullstack and WonderLens AI dialogue evidence when available;
- image QA evidence when assets affect source fidelity;
- verdict: `aligned`, `minor_adaptation`, `intent_drift`, or
  `needs_product_decision`;
- repair required and re-review outcome.

`intent_drift` blocks `results.tsv` logging, assignment checkoff, downstream
acceptance, and final completion until repaired or explicitly recorded as a
product-review finding. For blocked previews, the audit should verify that the
preview preserves the source promise up to the unsupported dependency and that
the unsupported behavior is called out rather than silently adapted away.

Record the audit path, verdict, reviewer agent name/id when available, repairs,
and re-review status in `runs/<run_id>/review_notes.md` and
`run_manifest.yaml` `outputs.source_intent_audits`.

### Step 5: Package checks

Before logging or committing, verify:

- `runs/<run_id>/activity_packages/<activity_id>/` contains exactly the five required files.
- Directory name equals `tag_block.yaml` `activity_id`.
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
- `spec.md` and `prod.md` satisfy the migrated package depth floor from `program.md`: concrete rationale, executable runtime detail, branch-specific follow-ups, non-generic screen states, and a magic moment earned by the child's action.
- Every `prod.md` Step 3 round is fully expanded; no condensed-round placeholders remain. Each round uses either `AI says` or `Runtime AI instruction` plus `Example AI line`.
- Every `prod.md` unexpected and no-response branch is specific to the beat. No copied run-level boilerplate remains for child behavior or AI follow-up policy.
- `spec.md` source-promise alignment notes and `prod.md` runtime flow preserve the original play frame, child role, interaction sequence, and required child actions unless a product-approved adaptation is recorded.
- `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
- Concept-led packages with `generate_with_assumptions` include `spec.md` `## Adaptation Rationale`.
- Packages whose adaptation brief has `asset_dependency.policy` other than `no_assets` include `spec.md` `## Asset Brief`.
- Packages with image/display dependencies include `spec.md` `## Asset Usage Timeline`.
- Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
- Every image usage point in the timeline has a step/round, timing, display location, use, prompt/source summary, and fallback.
- Required or optional asset rows include `asset_type`, requiredness, generation timing, use step, display location, display behavior, and fallback behavior; generated assets also include a directly usable `prompt_en`, while existing/displayed assets include a `source` or approved source description.
- `prod.md` Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic`.
- `prod.md` contains zero `## Self-Evaluation Scorecard` sections.
- `runs/<run_id>/review_notes.md` contains independent reviewer-agent evidence for the package, including final PASS status or the unresolved issue that prevents logging.
- `runs/<run_id>/source_intent_audits/` contains independent source-intent auditor evidence for the package or blocked/degraded artifact, and the final verdict is not unresolved `intent_drift`.
- Concept-led and parameterized packages include `spec.md` `## Extensibility Notes`, and `run_manifest.yaml` records `extensibility_summary` / `extensibility_notes` for dashboard review.
- Product-contract override packages include resolved blocker notes in `spec.md`, affected runtime beats in run provenance, and `run_manifest.yaml`.
- If targeting WonderLens AI runtime generation, runtime-facing `prod.md` input does not include leakage markers or unresolved review annotations such as raw `RESOLVED BLOCKER` comments unless the downstream converter is known to strip or accept them.
- Before comparing or accepting fullstack-demo and WonderLens AI dialogue quality, the runtime-facing package input is marker-free. Run `! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md` and treat any match as a package-owned blocker unless the downstream converter is explicitly proven to strip or accept that marker.
- If `demo_support.yaml` and `asset_manifest.yaml` are present, `python3 scripts/validate_demo_package_contract.py <package_dir>` passes.
- In full GOAL.md runs, `demo_support.yaml` and `asset_manifest.yaml` are required for every generated package unless demo export was explicitly disabled for the run or assignment.
- If `demo_support.status` is `supported`, the UI template is not `none`, entity binding is explicit, and unsupported/degraded reasons are not hiding a missing runtime.
- If `demo_support.status` is `degraded`, degraded reasons explain exactly what is simulated or limited.
- If `demo_support.status` is `unsupported`, the package is not logged as demo-playable and unsupported reasons name the missing UI/runtime/mechanic support.
- `asset_manifest.yaml` contains separate runtime asset entries, not a contact sheet as the runtime asset.
- `reference_bound` assets include sources/provenance and verification requirements.
- `reference_bound` assets declare an approved `source_strategy` and `transformation_policy`, and never rely on random generated approximations.
- Accepted reference-bound sources include `assets/sources/<asset_id>__source_original.<ext>` plus `assets/sources/<asset_id>__source_metadata.yaml` with accepted `source_type`, verified `license`, `storage_allowed: true`, `verification_status: accepted`, matching `sha256`, `verified_at`, and `reviewer_agent`.
- If `asset_build` is `manifest_only` or `none`, no binary image paths are required. If `asset_build` requests generated/curated files, run the implemented asset builder after package validation and never fabricate paths for assets whose inputs are missing.

### Step 5.5: Optional asset build phase

Run this phase only after every generated package has passed package validation and only when `source.asset_build` is not `none` or `manifest_only`.

- `generate_illustrative`: build only `accuracy_mode: illustrative` assets from `asset_manifest.yaml`; the agent-generated source PNGs must follow `docs/activity_asset_generation_workflow.md`, should be 512x512 for subset and full-pass attempts, and must represent one scene/object/item/character/icon/badge/distractor per asset ID rather than a composite card sheet. The builder consumes them from `runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png`, writes final variants under each package's `assets/`, updates package-relative variant paths, and summarizes them in `runs/<run_id>/generated_assets/asset_outputs.yaml`.
- `curate_reference`: for `reference_bound` assets, let an agent propose candidate sources, then verify provenance through approved public-domain, official, licensed/internal, or verified educational/scientific sources before accepting. Store accepted source originals and reviewer-approved metadata under package-local `assets/sources/`; do not use random web-image results as sources. The deterministic builder validates this metadata and leaves paths null if accepted provenance is missing or weak.
- `generate_and_curate`: run both behaviors.

For larger/full production passes this phase is mandatory because
`source.asset_build` must be `generate_and_curate`. Assign image generation and
reference curation to the scene/object/item asset generator role. That role
owns images and source files only; it must not change `spec.md`, `prod.md`,
mechanic labels, runtime AI instructions, or source-intent audit verdicts to
make an image easier to accept.

Asset-only rerun command:

```bash
python3 scripts/repair_full_pass_asset_bundle.py runs/<run_id>
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/validate_asset_granularity.py runs/<run_id>
python3 scripts/validate_full_pass_asset_bundle.py runs/<run_id>
```

The builder prepares `generated_assets/work_items/*.md` for delegated agents, preserves existing package-local runtime assets unless `--force` is supplied, leaves missing variants as null, and records failures in `asset_outputs.yaml` / `qa_notes.yaml` rather than pretending unavailable files exist.

For larger/full production passes, `asset_manifest.yaml` must request a
fullstack-style asset bundle, not only the concept-specific cards or objects.
Every package, including unsupported/gated review packages, needs package-local
512x512 PNG variants for `activity_icon`, `intro_scene`, `rules_scene`,
`round_1_scene`, `round_2_scene`, `round_3_scene`, `celebrate_scene`, and
`closing_scene`; Cat5 or synthesis flows also need `synthesis_scene`. Add
separate item/object/entity/target/distractor assets on
top of that bundle when the runtime displays specific cards or objects.
Scene assets must not embed app-owned progress dots, round markers, response
slots, rule strips, buttons, chips, picker slots, badges, or similar runtime
interface markers. Scene bundles must also be visually distinct by activity;
unrelated activities cannot pass image QA with the same cozy-room, blank-board,
child-response, or child-on-rug template. For guided drawing and other
step-by-step build flows, the round scene itself must show what the child
should draw or build in that step.

### Step 5.6: Independent image quality QA

When any generated or curated PNG asset exists, spawn an image quality validator
after the builder and before consumer dialogue QA. The validator reads
`asset_manifest.yaml`, package runtime beats, generated PNGs, source metadata,
and `docs/activity_asset_generation_workflow.md`.

Record image QA under `runs/<run_id>/generated_assets/qa_notes.yaml` or
`runs/<run_id>/review_notes.md` with concrete asset paths and a PASS/FAIL/REPAIR
verdict for:

- current WonderLens flat Nordic activity style;
- one scene/object/item/character asset per file;
- role match against `asset_manifest.yaml`;
- scene/dialogue and screen-beat alignment;
- no baked app progress/control UI such as progress dots, round markers,
  response slots, rule strips, buttons, chips, picker slots, or badges;
- cross-activity distinctness, so unrelated activities do not reuse the same
  generic scene template;
- guided drawing/build-step fidelity when applicable, so each round scene shows
  the exact child action for that step;
- no duplicate selectable item/object in a scene background when the runtime
  uses separate picker sprites, target/distractor cards, or collection items
  to advance the activity;
- progressive evidence and partial-reveal sequencing, so early beat images do
  not expose the final answer, full target, or solution before the dialogue
  reveal step;
- object readability at runtime size;
- central round-lens crop safety where relevant;
- no readable text, letters, numbers, logos, watermark, UI labels, contact
  sheets, masks, borders, or baked device chrome;
- approved provenance and factual fidelity for reference-bound assets;
- no misleading image that changes the source play frame or child action.

Duplicate picker objects in scene backgrounds and premature answer reveal are
hard REPAIR verdicts. Accept the asset only after the image matches the source
intent step by step, including when the answer is supposed to appear.

If QA fails, assign the image quality improver to repair prompt specificity,
regenerate an illustrative asset, replace/verify a reference source, or apply a
deterministic crop/resize repair. Re-run the builder, asset validator, and image
QA. If changed visuals affect dialogue or screen claims, re-run the affected
consumer dialogue strategies.

### Step 5.7: Package/import consumer validation

Run package/import validation before live dialogue QA. Fullstack-demo and
WonderLens AI are consumers, not content improvers.

Fullstack validation should import the package with the current package importer
or equivalent test harness and record:

- package imported without manual content edits;
- unsupported packages were skipped rather than made playable;
- degraded packages exposed their limitation honestly;
- declared assets copied or resolved to consumer-visible paths;
- converted `step_instructions` preserve runtime AI instruction quality:
  goal/action, tier or length constraint, emotion/tone, child progress evidence,
  branch behavior, source/activity frame guardrail, safety/product constraints,
  screen/state expectation, and source-required must-not-skip details;
- converted `step_instructions` did not fall back to generic/default hook,
  transition, round, celebration, closing, or early-exit guidance;
- Cat5 imports preserve synthesis as its own instruction when the package has a
  synthesis beat, rather than blending it into collection rounds or generic
  celebration;
- importer conversion rules did not remove source-required child role,
  sequence, required asset, background/context promise, or required child
  action.

WonderLens AI validation should generate or load runtime artifacts from the
same package without content improvement and record:

- `runtime.yaml` or equivalent runtime artifact exists and loads;
- `step_instructions` or equivalent runtime prompts preserve the package
  runtime AI instruction quality;
- package-local assets and unsupported/degraded gates are honored;
- runtime generation does not add unsupported sensing, hidden-state claims,
  false screen claims, or mechanic changes;
- runtime generation does not reject or leak review-only markers such as
  unresolved notes or raw `RESOLVED BLOCKER` annotations into executable
  dialogue;
- the marker-free precondition passes before dialogue comparison:
  `! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md`;
- failures are classified as package-owned, WonderLens-owned, or product-owned.

If either consumer requires downstream code changes, record the evidence as a
follow-up unless the user explicitly expands scope. Do not repair a consumer
runtime issue by weakening the autodesign activity.

### Step 5.8: Live dialogue QA and repair loops

After package/import validation passes for a playable or degraded package, run
live or runtime-equivalent dialogue QA against fullstack-demo and WonderLens AI
where the runtime supports it. Use sanitized transcripts only; never print
provider secrets.

Use multiple child-input strategies per representative activity:

- ideal answer;
- minimal answer;
- wrong answer;
- off-topic answer;
- confusion/help request;
- premature done;
- silence/no response;
- unsupported request.

Validators must check source intent, child role, device role, unsupported
sensing claims, hidden-state claims, false screen/asset claims, branch recovery,
tier verbosity, synthesis/celebration/closing drift, and final recap fidelity.

Route each failure by owner:

- Package-owned dialogue gap: assign the dialogue quality improver to repair
  `prod.md` runtime AI instructions, branch policies, source guardrails, or
  screen-state expectations in autodesign; then re-import and re-run the failing
  strategies.
- Fullstack-owned generic runtime issue: record a downstream fullstack follow-up
  with transcript evidence. Do not hide it by changing the activity intent.
- WonderLens-owned generic runtime issue: record a downstream WonderLens AI
  follow-up with transcript evidence. Do not hide it by changing the activity
  intent.
- Product-owned capability gap: mark the package degraded/unsupported or record
  a product decision requirement.
- Image-owned mismatch: return to Step 5.6 and re-run affected dialogue after
  image repair.

Full-pass acceptance requires all package-owned and image-owned failures to be
repaired and revalidated. Downstream-owned failures may remain only as explicit
follow-up risks in `review_notes.md`, `run_manifest.yaml`, and the final report.

### Step 6: Log the result

Append a row to `results.tsv`:

```
[assignment]\t[entity]\t[category]\t[tier]\t[pillar]\t[style]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F/N]\t[P/F]\t[P/F]\t[package_path]\t[ISO timestamp]
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
  activity_path: runs/<run_id>/activity_packages/<activity_id>
  package_scope: run_local
  adaptation_brief: runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml # omit when no Phase 0 brief was produced
  results_tsv_row: true
  generation_policy: fresh_run_local_package
  resolved_blockers: [] # omit or leave empty unless product_contract_override allowed former blockers
  resolved_blocker_types: []
  asset_usage:
    - asset_id: "<image/card/line-art/ui asset id>"
      generation_timing: "<pre_generated|runtime_generated|display_existing>"
      use_step: "<prod step/round range>"
      display_location: "<screen region or UI slot>"
      prompt_or_source: "<short prompt/source summary for reviewer traceability>"
      display_behavior: "<how/when the asset appears and persists>"
      fallback_behavior: "<what runtime does if unavailable>"
  demo_support:
    status: "<supported|degraded|unsupported>"
    ui_template: "<cat1_dialogue|cat5_collection|cat5_judgment|none>"
    support_level: "<full|catalog_simulated_judgment|unsupported|...>"
    extension_files:
      - runs/<run_id>/activity_packages/<activity_id>/demo_support.yaml
      - runs/<run_id>/activity_packages/<activity_id>/asset_manifest.yaml
  validation_reports:
    source_intent_audit: runs/<run_id>/source_intent_audits/<ordinal>_<activity_id>.md
    fullstack_import: "<path to import/conversion report when run>"
    fullstack_dialogue: "<path to sanitized transcript report when run>"
    wonderlens_ai_runtime: "<path to runtime generation/load report when run>"
    wonderlens_ai_dialogue: "<path to sanitized transcript report when run>"
    image_quality: "<path to image QA report when assets are built>"
    final_independent_review: "<path to final cross-artifact review when full_pass_pipeline=true>"
  extensibility_summary: "<how this activity can be retargeted, or why not>"
  extensibility_notes:
    - "<reusable entity/property/asset-set slot or limitation>"
  status: PASS
```

3. Add reviewer evidence, repair notes, and residual risks to `runs/<run_id>/review_notes.md` for every generated, enriched, or audited package.
4. Verify `runs/<run_id>/run_manifest.yaml` has an entry for the generated activity and `runs/<run_id>/generated_activity_ids.txt` includes the generated `activity_id`.

For enrichment-only package maintenance, keep changed packages under `enriched_activities` and do not append `results.tsv`. Keep audited packages that passed without edits under `audited_activities` so `review.html` shows all reviewer-covered packages, not only packages that changed.

For blocked assignments, keep the entry under `blocked_assignments`, include `brief_path` and `design_preview`, do not append `results.tsv`, leave the assignment row unchecked, and continue to the next unchecked row. If the constraints are later resolved, rerun or promote the design preview into a normal package with the five required files plus any enabled demo extensions, remove or resolve the blocked-element comments, then send it through the standard self-evaluation, reviewer-agent, validation, `results.tsv`, and checkoff gates.

For product-contract override assignments, do not create a `blocked_assignments` entry for dependencies covered by `minimum_unblock_allowed`. Keep the row under `generated_activities`, add `resolved_blockers` and `resolved_blocker_types`, and ensure the dashboard reports the former blockers as resolved contract items.

### Step 6.7: Generate human review dashboard

This is a final-run step, not a per-assignment step. After every row from `assignment_snapshot.md` has generated, blocked, or failed, and after all package checks, reviewer evidence, manifest entries, blocked-brief entries, and blocked design previews are current, generate a single static review dashboard at:

```text
runs/<run_id>/review.html
```

This file is for human review only. It is a derived artifact, not a source of truth. Follow `review_dashboard.md` for the dashboard contract, including source inputs, concise clickable cards for generated/enriched/audited packages, popup/detail behavior, visual runtime beat maps with extracted source rows, grouped tag colors, asset usage timelines for image/display dependencies, distinct `Asset dependencies` / `Display beats` / `Image items` metrics, 10-dimension criteria and package scorecard results, resolved contract item handling, extensibility overview, blocked-preview handling, per-blocked-card `Minimum To Unblock` sections below capability flags, blocked-preview scorecards, link rules, validation requirements, the editorial design language in `review_dashboard.md` §"Design language" (warm-paper palette, indigo accent, serif display title and dialog headings, hairline-divided panels, tabular numerals, accent rails on cards, status-dot run indicator), and the in-file preview behavior in `review_dashboard.md` §"In-file preview" (embedded `<template>` content, dedicated preview `<dialog>`, dependency-free Markdown rendering, modifier-click bypass, "Open in new tab" escape hatch).

Generation command:

```bash
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

The generator reads `run_manifest.yaml`, `review_notes.md`, `results.tsv`, package files, blocked briefs, and blocked design previews, then writes `runs/<run_id>/review.html`. The generated HTML must include a `Review Dashboard Workflow` section with these generation and validation commands so reviewers can see how the artifact was produced.

After writing `review.html`:

1. Update `runs/<run_id>/run_manifest.yaml` `outputs.review_dashboard` to `runs/<run_id>/review.html`.
2. Add check entries for `python3 scripts/generate_run_review.py runs/<run_id>` and `python3 scripts/generate_run_review.py --validate runs/<run_id>`.
3. Verify the file exists, is non-empty, has `<html`, `<style`, `<script>`, the run id, the `Review Dashboard Workflow` section, cards for generated/enriched/audited packages, blocked entries when present, the 10-dimension review criteria, per-package scorecard results with why notes, asset usage timelines when image/display dependencies exist, distinct `Asset dependencies`, `Display beats`, and `Image items` labels, resolved contract items when resolved blockers exist, extensibility overview when extensibility notes exist, blocked-preview scorecards when blocked entries exist, clickable detail behavior, modal/detail content, per-blocked-card `Minimum To Unblock` sections below capability flags, grouped tag colors, inline blocked/resolved marker chips, clear missing-decision versus inline-marker counts, and resolving local links.

### Step 6.8: Patch existing runs with source-intent audit

Use this step when the generated packages already exist and the user asks for audit/review coverage rather than a full generation rerun. Do not regenerate activities, assets, or exported reviewer packets unless the audit identifies a package that must be repaired.

1. Create or update `runs/<run_id>/source_comparison/source_intent_audit.yaml` with one entry per source workbook row. Each entry records `source_row`, `activity_id`, `workbook_evidence`, `original_play_frame`, `generated_play_frame`, `preserved`, `drift`, `status`, `severity`, `recommendation`, and `product_review_question`.
2. Derive `original_play_frame` from the original workbook row, not from `inputs/source_activity_concepts.md` or an adaptation brief. For the current workbook batch, use `inputs/original_activity_concepts_2026-05-29.tsv` as the committed workbook export for source-intent evidence. Use the normalized source snapshot only as a cross-check. If the normalized row has weakened the workbook's child role, sequence, required asset, or background-information requirement, repair the normalized row first or record the generated package as drift.
3. Classify `status` as `aligned`, `minor_adaptation`, `intent_drift`, or `needs_product_decision`. Use `intent_drift` when the category/mechanic token is preserved but child role, interaction sequence, story frame, required child action, real-vs-fictional asset requirement, or required background/context content materially changes.
4. Regenerate the source review matrix from existing run artifacts:

```bash
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --strict-workbook-intent
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --strict-workbook-intent --validate
```

The source-comparison script currently reads XLSX workbooks for `--workbook`; keep using the original XLSX there when generating the matrix, while citing the committed TSV export in audit evidence and generation briefs. Do not replace the `--workbook` argument with the TSV unless the script is extended to support TSV input first.

5. Record `outputs.source_intent_audit`, `outputs.source_comparison_review`, audit counts, commands, and residual high-severity findings in `run_manifest.yaml` and `review_notes.md` or `HANDOFF.md`.
6. If an entry is high-severity `intent_drift`, either repair only that activity package and regenerate the affected review artifacts, or leave it explicitly flagged as a product-review finding. Do not perform a full rerun merely to create the audit.

### Step 7: Mark generated assignment complete

In `assignments.md`, change `- [ ]` to `- [x]` only for assignments that generated a passing package. Keep or add the clean `activity_id=<base_activity_id>` value, and add or update `package_path=runs/<run_id>/activity_packages/<activity_id>` so the checked row points at the generated directory. Do not rewrite blocked rows.

### Step 8: Commit

```bash
git add runs/<run_id>/activity_packages/<activity_id>/ runs/<run_id>/ results.tsv assignments.md
git commit -m "Design: <activity_id> - ALL PASS"
```

### Step 9: Next assignment

Move to the next `- [ ]` assignment from the run-start queue, including rows after a blocked assignment. When every row from `assignment_snapshot.md` has either generated, blocked, or failed:

If `run_manifest.yaml` records `source.full_pass_pipeline: true`, spawn a final
independent reviewer before setting final run status. The reviewer must read the
final generated/enriched package list, source-intent audits, package/import
reports, fullstack dialogue transcripts, WonderLens AI runtime/dialogue
reports, image QA reports, repair notes, run manifest, and generated dashboard.
It returns PASS/FAIL with unresolved risks. A FAIL blocks full-pass acceptance
until package-owned or image-owned issues are repaired and re-reviewed.
Downstream-owned fullstack or WonderLens AI issues may remain only when they
are explicitly recorded as follow-up scope.

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
- Do not reuse an old `activities/<activity_id>/` directory for unchecked generation-ready rows. Fresh reruns must create a new run-local directory named `runs/<run_id>/activity_packages/<base_activity_id>/`, and `tag_block.yaml` `activity_id` must match the clean base directory name.
- Do not let one product/design blocker halt the whole batch. Record the blocked brief and constrained design preview, leave that row unchecked, and continue to later unchecked rows unless a hard workflow failure makes later processing unsafe.
- When a user scopes a fresh rerun to a named batch or assignment subset, do not process outside that scope.
- When the user declares minimum-to-unblock decisions allowed by product contract, generate those rows as normal packages and preserve the former blockers as resolved annotations rather than invalid blockers.
- Always include extensibility notes for reusable concept-led packages so review.html can show how the activity adapts to other entities, properties, or asset sets.
- For larger/full production passes, always set `asset_build=generate_and_curate`, keep package writing text-only, run image generation as a separate image-only phase, and require source-intent, package/import, fullstack dialogue, WonderLens AI dialogue, image QA, repair-loop, and final independent-review evidence before acceptance.
- Never treat fullstack-demo or WonderLens AI as content-improvement steps. They load/execute package content and report conversion/runtime failures; package-owned failures return to autodesign for repair.
- Commit after every completed package unless the user explicitly asks to batch commits.
- Quality over speed. Take as many self-evaluation rounds as needed.
