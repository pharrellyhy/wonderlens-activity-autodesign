# Run Instructions - Autonomous Activity Package Loop

Read this after `GOAL.md`. Scoped files in `goals/` may override this runbook
for a specific subset, full pass, or validation run. `program.md` remains the
detailed authoring, output, and rubric contract.

## Source Documents

Read only the documents needed for the current row and run mode:

- `GOAL.md`: default objective, package invariants, and completion criteria.
- `program.md`: adaptation brief, migrated package contract, and 10-dimension
  rubric.
- `templates.md`: mechanic adapters, pillar overlays, and Cat1/Cat3/Cat5
  modifiers.
- `docs/game_styles.md`: game-style taxonomy.
- `docs/activity_asset_generation_workflow.md`: runtime PNG workflow and style
  contract when assets are declared or built.
- `docs/activity_display_contract.md`: frame-level app layout, control,
  verification, and effect contract when demo/runtime display is declared.
- `activities/README.md`, `activities/_schema/*.schema.json`, and
  `docs/activity_vocabulary.md`: package and enum contracts.
- `entity_guidance.md` and `conversation_bridge.md`: only for mapping-informed
  rows or warm/cold bridge handling.
- Any `concept_source=file#id` or `asset_requirements=file#id` referenced by an
  active assignment row.

## Setup

1. Confirm `assignments.md` is the active queue and `results.tsv` exists.
2. Create a run id in `YYYYMMDD_HHMMSS_<short_label>` format.
3. Create the run directory:

```text
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
├── generated_assets/        # only when an asset build runs
├── manual_audits/
├── review_status/           # per-activity review YAML files
├── review_notes.md
└── review.html              # generated at end of run
```

4. Write `assignment_snapshot.md` with the unchecked rows pending at run start.
   If the user scoped the run, snapshot only that scope.
5. Initialize `run_manifest.yaml` with the run flags, source files, summary
   counters, output arrays, check list, and notes. At minimum record:

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
  demo_export: <true|false>
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
notes: []
```


   Create an empty `runs/<run_id>/review_status/` directory. Each generated
   package will get a per-activity status file here (see step 7).
6. Say: `Setup complete. <N> assignments pending. Run id: <run_id>.`

## Optional Existing-Package Maintenance

Run this only when the user or scoped goal explicitly asks to audit/enrich
checked packages or named `activities/<activity_id>/` packages. Checked rows in
the archive are not active queue items.

- Audit the five required files plus demo extensions when present.
- Preserve `activity_id`, package directory, tag-block enums, recap/dashboard
  placeholders, and stable asset IDs.
- Repair only package-owned thinness or contract drift.
- Record changed packages under `outputs.enriched_activities`; record no-op
  reviewer passes under `outputs.audited_activities`.
- Do not append `results.tsv` or change assignment checkboxes for maintenance.

## Assignment Loop

Process each row from `assignment_snapshot.md` once, in order.

### 1. Parse The Row

Extract or infer:

- `assignment_type`, `activity_concept`, `entity`, `category`, `tier`,
  `mechanic`, `pillar`, `style`, `scene`, `trigger_condition`, `mapping`,
  `start`, and `activity_id`;
- `concept_source`, source-promise cues, and workbook/source evidence;
- `asset_policy`, `asset_requirements`, `demo_export`, `demo_support`,
  `asset_build`, and `product_capabilities`;
- `full_pass_pipeline` and `product_contract_override` overrides.

For fresh generation, treat `activity_id=` as a clean base slug. Strip any
trailing `_rYYYYMMDD_HHMMSS` suffix before writing the run-local package.

### 2. Load Source Context

Load referenced `concept_source` and `asset_requirements` rows before Phase 0.
For workbook-derived rows in the current batch, cite
`inputs/original_activity_concepts_2026-05-29.tsv` first and use
`inputs/source_activity_concepts.md` only as a normalized helper.

Normalize generated briefs and package copy to English even when source names
or notes are Chinese.

### 3. Write The Adaptation Brief

Run `program.md` Phase 0 for concept-led, match-pattern, capability-probe,
legacy alias, underspecified, mapping-informed, or asset-dependent rows.

The brief must decide:

- source-promise alignment;
- input mode;
- canonical mechanic and confidence;
- category, tier, trigger, and scaffold fit;
- mapping use;
- asset dependency and demo support;
- readiness: generate, generate with assumptions, degrade, or block.

Write the brief under `runs/<run_id>/adaptation_briefs/` when generation may
proceed, or `runs/<run_id>/blocked_briefs/` when it cannot.

If blocked, also write a constrained design preview under
`runs/<run_id>/blocked_designs/`, annotate unsupported runtime elements with
`BLOCKED ELEMENT`, record the blocker in the manifest, leave the assignment row
unchecked, and continue to the next snapshot row.

If `product_contract_override=minimum_unblock_allowed` applies, generate the
package with resolved contract notes instead of treating the row as blocked.

### 4. Run Pre-Package Source-Intent Audit

For source-derived, concept-led, workbook-derived, pilot-validation, and
full-pass rows, obtain independent source-intent evidence before package
writing. The audit locks:

- original play frame;
- child role;
- device role/action;
- interaction sequence;
- required child actions;
- real/reference asset requirement;
- background/context promise;
- allowed adaptation and product dependency.

Unresolved `intent_drift` blocks package writing until repaired or explicitly
approved as a product decision.

### 5. Load Mapping When Needed

If `mapping=` is supplied or the brief is mapping-informed, resolve the entity
through `data/mappings_dev20_0318/_index.yaml`, load the mapped YAML, and use
`entity_guidance.md` for dimensions, Key Concepts, Related Concepts, and tier
language. Do not invent mapping-derived facts for `concept_only` or
`parameterized` rows.

### 6. Compose The Scaffold

Read `templates.md` in layered order:

1. Template 0 spine.
2. Mechanic adapter matching `canonical_mechanic`.
3. Cat1, Cat3, or Cat5 category modifier.
4. Pillar/style overlay selected by the brief.

The repeated child action in Step 3 must match the canonical mechanic. Pillar
and style flavor the action; they do not replace it.

### 7. Write The Package

Create:

```text
runs/<run_id>/activity_packages/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

When `demo_export=true`, also write:

```text
demo_support.yaml
asset_manifest.yaml
activity_display_contract_v1.yaml
```

For every generated package, also create the per-activity review status file:

```bash
cp runs/_templates/review_status.yaml runs/<run_id>/review_status/<activity_id>.yaml
```

Edit `activity_id`, `run_id`, and `owners.run_captain` before committing.
Leave `text_review`, `asset_review`, and downstream gate statuses
as `pending`. These per-activity files are the parallel-workflow status
source of truth defined in
`docs/full_pass_agentic_parallel_workflow.html` and
`docs/role_agent_prompting_guide.md`.

Package-writing rules:

- keep package writing text-only;
- preserve source play frame, child role, sequence, and required actions;
- put source-promise and assumption notes in `spec.md`;
- put runnable Step 1-5 runtime guidance in `prod.md`;
- use machine-convertible `Runtime AI instruction` lines for live beats;
- fully expand every Step 3 round;
- make unexpected/no-response branches beat-specific;
- separate Cat5 collection, synthesis, celebration, and closing beats;
- define all asset IDs in `spec.md` and `asset_manifest.yaml`;
- author `activity_display_contract_v1.yaml` after `prod.md` and asset metadata
  are stable; bind each verifiable policy to the displayed asset or displayed
  option, declare wheel/press/voice `input_affordance`, and use only the five
  approved `layout_id` values;
- keep raw image prompts out of `prod.md`;
- include `## Extensibility Notes` for reusable or parameterized activities.

## Review And Validation Gates

Before logging or checkoff, complete these gates for each generated package:

1. Author self-evaluation against `program.md` Phase 3.
2. Independent package review. A reviewer FAIL or credible uncertainty requires
   repair and re-review.
3. Post-package source-intent audit. Unresolved `intent_drift` blocks
   acceptance.
4. Package checks:
   - required files exist;
   - directory name matches `tag_block.yaml` `activity_id`;
   - `tag_block.yaml` validates against the schema;
   - `prod.md` has no scorecard;
   - `spec.md` has exactly one scorecard;
   - `dashboard.template.yaml` focal attribute matches `tag_block.yaml`;
   - runtime instructions, branch behavior, screen states, asset IDs, demo
     status, and package metadata agree.
5. Demo extension validation when `demo_support.yaml` and `asset_manifest.yaml`
   are present:

```bash
python3 scripts/validate_demo_package_contract.py <package_dir>
```

6. Display contract validation when `activity_display_contract_v1.yaml` is
   present:

```bash
python3 scripts/validate_activity_display_contract.py <package_dir>
```

Record review evidence, commands, repairs, and residual risks in
`runs/<run_id>/review_notes.md` and `run_manifest.yaml`.

## Asset Build Phase

Run this phase only after package validation and only when `asset_build` is not
`none` or `manifest_only`.

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode <generate_illustrative|curate_reference|generate_and_curate>
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
```

For larger/full production passes, also run:

```bash
python3 scripts/repair_full_pass_asset_bundle.py runs/<run_id>
python3 scripts/validate_asset_granularity.py runs/<run_id>
python3 scripts/validate_full_pass_asset_bundle.py runs/<run_id>
```

Asset rules:

- illustrative source PNGs come from Codex built-in imagegen;
- reference-bound assets require approved source originals and metadata;
- final runtime PNGs are package-local and generally 512x512;
- picker/item/object assets are separate files under package-local
  `assets/items/`;
- every scene asset must visually explain the activity beat's child action,
  learning evidence, or source-specific screen state; generic baskets, blank
  cards, blank boards, glows, empty rooms, and decorative placeholders fail
  image QA unless the beat itself is explicitly about that object;
- story-scene assets must feel like coherent real-world scenes with plausible
  spaces, stable camera/framing, consistent subject treatment, and concrete
  beat-to-beat changes; isolated floating symbols are for icons, badges, and
  item sprites, not scene backgrounds;
- sound/phoneme/word-hunt scenes must foreground listening, speaking, sound
  waves, search motion, or runtime evidence areas rather than defaulting to a
  treasure/basket metaphor;
- picker/catalog activities must provide a consumer-parity item set, normally
  four correct items and eight distractors, unless the goal records an approved
  smaller catalog;
- no baked text, labels, UI controls, masks, borders, contact sheets, device
  chrome, duplicate picker objects in backgrounds, or premature answer reveals.

Run independent image QA whenever PNG assets exist. The reviewer must inspect
the actual PNGs, not only the prompts, manifest, or build logs. Repair
image-owned failures with a recorded prompt-root-cause note and an exact
regeneration prompt that removes the failed placeholder subject, rebuild, and
revalidate.

For subset/full-pass runs, write a run-local manual prompt trace for each
generated package under:

```text
runs/<run_id>/manual_audits/<activity_id>_prompt_trace.md
```

The trace must list, per runtime step, package instruction vs recorded
downstream LLM prompt material and image description vs exact recorded imagegen
prompt. If a provider or tool does not expose the raw request payload, state
that limitation explicitly and point to the closest recorded prompt material
such as `step_instructions`, `asset_manifest.yaml`, and generated asset work
items. Do not include secrets or credential material.

## Consumer And Full-Pass Gates

When `full_pass_pipeline=true`, use the scoped goal file as the detailed
ordering contract. At minimum:

- keep the main agent as orchestrator for scope, credentials, server lifecycle,
  repair routing, final acceptance, commits, and user reporting;
- use delegated agents for disjoint ownership when available;
- run at most three delegated/sub-agents in parallel;
- collect evidence and terminate or kill a finished delegated agent before
  spawning another;
- validate fullstack-demo import/conversion before live dialogue QA;
- validate WonderLens AI runtime generation/load and dialogue behavior;
- reject generic downstream picker placeholders such as `Matching placeholder`,
  `/icons/green_apple.png`, or `/icons/straight_stick.png` when package item
  assets exist;
- classify failures as package-owned, fullstack-owned, WonderLens-owned,
  image-owned, or product-owned;
- repair package-owned and image-owned issues in autodesign, then revalidate;
- obtain final independent review before full-pass acceptance.

Do not let fullstack-demo or WonderLens AI improve, weaken, rewrite, or
reinterpret package content to make the run pass.

For every `full_pass_pipeline=true` run with generated packages, record
consumer dialogue QA before final dashboard validation. Missing dialogue QA is
a run blocker, even when conversion/load checks pass. Write:

```text
runs/<run_id>/downstream_reports/fullstack_demo/dialogue_qa_report.json
runs/<run_id>/downstream_reports/wonderlens_ai/dialogue_qa_report.json
```

Each report must be a sanitized JSON object with:

```json
{
  "status": "pass",
  "mode": "live|runtime_equivalent",
  "activity_ids": ["<activity_id>"],
  "strategies": [
    {"strategy": "expected_answer", "status": "pass"},
    {"strategy": "wrong_unproductive_answer", "status": "pass"},
    {"strategy": "help_confusion", "status": "pass"},
    {"strategy": "silence_no_response", "status": "pass"},
    {"strategy": "premature_done", "status": "pass"}
  ]
}
```

Use `status: downstream_owned_failure` only when the report includes a
`failure_summary` or `downstream_follow_up` and the issue is explicitly not
package-owned. Do not mark a run complete when a report is missing, has fewer
than the five strategies above, or uses conversion/load evidence as a substitute
for dialogue QA.

Before comparing or accepting live dialogue, prove runtime-facing package input
does not contain raw blocker markers:

```bash
if rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md; then exit 1; fi
```

Retry transient provider throttles such as `429`, `RESOURCE_EXHAUSTED`,
`rate_limit`, quota exceeded, or equivalent errors with backoff before
classifying the phase as blocked.

## Logging And Dashboard

For each accepted generated package:

1. Append one `results.tsv` row.
2. Append the clean `activity_id` to `generated_activity_ids.txt`.
3. Add a `generated_activities` entry in `run_manifest.yaml` with package path,
   brief path, audit paths, checks, demo status, asset status, extensibility,
   and final status.
4. Mark the corresponding active assignment row complete and add
   `package_path=runs/<run_id>/activity_packages/<activity_id>`.

For blocked rows, update `blocked_assignments`, leave the active assignment row
unchecked, and do not append `results.tsv`.

At the end of the run:

```bash
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

Record `outputs.review_dashboard: runs/<run_id>/review.html`, fill
`completed_at`, set final status, and include the dashboard path in the final
report.

## Commit Rule

After a coherent passing unit:

```bash
git add <intended run/package/results/assignment files>
git commit -m "Design: <activity_id> - ALL PASS"
```

Use the project's conventional commit rules when editing docs, scripts, schemas,
or workflow files. Do not push unless the user explicitly asks.

## Important Rules

- Do not process rows outside the run-start snapshot or explicit user scope.
- Do not reuse canonical `activities/<activity_id>/` directories for fresh
  generation.
- Do not skip independent review, source-intent audit, or applicable validators.
- Do not abbreviate runtime rounds with "same structure" language.
- Do not hide unsupported product behavior inside valid runtime dialogue.
- Do not generate binary images during text package writing.
- Do not treat archived assignment rows as active work unless a goal explicitly
  copies or references a scoped subset back into `assignments.md`.
- Do not leave servers running after live validation.
- Stop on hard workflow failures that make later rows unsafe; otherwise record
  row-level blockers and continue.

## Legacy Transform Workflow

`transform.md` and `transform_run.md` are retained only for the old
`designs/*_spec.md` to `designs/*_prod.md` workflow. Do not use them for
migrated `activities/*/prod.md` files.
