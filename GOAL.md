# Codex Goal: Autonomous Activity Generation

Use this file as the default `/goal` target for ordinary WonderLens activity
generation. It defines the objective and completion contract. `run.md` defines
the execution loop. `program.md` remains the detailed authoring contract.

For scoped, high-risk, or full production runs, execute the matching file under
`goals/` instead of expanding this root goal inline.

## Goal

Process the active assignment queue in `assignments.md`, create run-local
activity packages under `runs/<run_id>/activity_packages/<activity_id>/`, and
record enough provenance for review, rerun, downstream import, and package
promotion decisions.

Fresh generation must preserve the source activity's play frame: child role,
device role, interaction sequence, required child action, real/reference asset
need, and background/context promise. If a normalized helper row conflicts with
the original source, the original source controls unless a product-approved
adaptation is recorded.

## Default Run Settings

| Setting | Default | Notes |
|---|---|---|
| `demo_export` | `true` | Generated packages include `demo_support.yaml`, `asset_manifest.yaml`, and `activity_display_contract_v1.yaml` unless disabled. |
| `asset_build` | `manifest_only` | Write asset requirements and nullable paths, but do not create binary image files. |
| `full_pass_pipeline` | `false` | Full source, asset, consumer, dialogue, image, repair, and final-review gates are opt-in. |
| `product_contract_override` | `none` | Use `minimum_unblock_allowed` only when explicitly requested. |
| `package_scope` | `run_local` | Fresh packages go under `runs/<run_id>/activity_packages/`, not `activities/`. |
| `mapping_root` | `data/mappings_dev20_0318` | Use when `mapping=` is supplied or the brief is mapping-informed. |

Workbook-derived rows in the current source batch use
`inputs/original_activity_concepts_2026-05-29.tsv` as the committed source
baseline. `inputs/source_activity_concepts.md` is a normalized helper for
English naming, mechanics, asset hints, and capability metadata only.

## Package Contract

Every generated package must contain the five required files:

```text
spec.md
prod.md
tag_block.yaml
recap.template.yaml
dashboard.template.yaml
```

When `demo_export=true`, each generation-ready package also contains:

```text
demo_support.yaml
asset_manifest.yaml
activity_display_contract_v1.yaml
```

The package must satisfy these invariants:

- directory name equals `tag_block.yaml` `activity_id`;
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`;
- demo extension files validate with `scripts/validate_demo_package_contract.py`;
- display contracts validate with `scripts/validate_activity_display_contract.py`;
- every display-contract frame uses one of the five approved `layout_id` values:
  `single_image`, `two_image_options`, `two_direction_options`,
  `two_number_options`, or `multi_option_carousel`;
- app layout, control mode, displayed option, verification policy, sound,
  lighting, and haptic metadata live in `activity_display_contract_v1.yaml`,
  not `tag_block.yaml`;
- `spec.md` has exactly one `## Self-Evaluation Scorecard`;
- `prod.md` has no scorecard and contains runnable Step 1-5 guidance;
- every live beat has machine-convertible runtime AI instructions or equivalent
  behavior guidance rich enough for downstream `step_instructions`;
- Step 3 rounds are fully expanded and use parseable
  `**Round N -- Short Scenario:**` headings;
- unexpected and no-response branches are beat-specific, not copied boilerplate;
- Cat5 synthesis, when present, is separate from collection rounds and
  celebration;
- concept-led or reusable packages include `## Extensibility Notes`;
- asset dependencies appear in `spec.md` `## Asset Brief`,
  `## Asset Usage Timeline`, and `asset_manifest.yaml`;
- reference-bound assets require approved provenance and must not use random
  generated approximations;
- supported, degraded, and unsupported demo behavior is declared honestly.

## Source And Review Gates

For source-derived, concept-led, workbook-derived, pilot-validation, and
full-pass rows:

- create an adaptation brief before package writing;

- a `review_status/<activity_id>.yaml` file is copied from
  `runs/_templates/review_status.yaml` for each generated package, recording
  per-activity gate status for the parallel workflow in
  `docs/full_pass_agentic_parallel_workflow.html`.
- run a pre-package source-intent audit when the source promise is richer than a
  simple entity/category row;
- repair or block unresolved `intent_drift` before package writing;
- run the 10-dimension self-evaluation from `program.md`;
- obtain independent package-review evidence before logging/checkoff;
- run a post-package source-intent audit before accepting the row;
- record evidence and repairs in `runs/<run_id>/review_notes.md` and
  `run_manifest.yaml`.

Blocked rows do not produce valid runtime packages, do not append `results.tsv`,
and remain unchecked in `assignments.md`. Write a blocked brief plus a
constrained blocked design preview, then continue to later snapshot rows unless
the blocker makes later processing unsafe.

When `product_contract_override=minimum_unblock_allowed` is active, formerly
blocking minimum-to-unblock items generate as normal packages with resolved
contract notes and dashboard-visible resolved blockers.

## Asset Behavior

Package authoring is text-only. Binary image files are created only in an
explicit post-package asset phase:

- `manifest_only`: default; no image files required.
- `generate_illustrative`: use Codex built-in imagegen for illustrative PNG
  sources.
- `curate_reference`: accept only approved internal, licensed, public-domain,
  official, or verified educational/scientific reference sources.
- `generate_and_curate`: run both behaviors.

Illustrative runtime assets must follow
`docs/activity_asset_generation_workflow.md` and
`docs/asset_style_reference/`: flat Nordic children's illustration, 512x512
runtime PNGs, scene assets as full-bleed square images, item/object assets as
separate centered images with clean padding, and no baked text, UI, masks,
device chrome, contact sheets, or multi-card sheets.

For larger/full production passes, use the scoped full-pass goal file and set
`asset_build=generate_and_curate`.

## Consumer Boundary

Fullstack-demo and WonderLens AI are consumers, not authoring fallbacks. They
must load or generate runtime artifacts from the package as provided, preserve
package runtime instructions, and report failures as package-owned,
fullstack-owned, WonderLens-owned, image-owned, or product-owned. Do not hide a
weak package by rewriting content downstream.

Before live dialogue comparison or acceptance, runtime-facing package input
must be free of raw review/leakage markers such as `RESOLVED BLOCKER` unless a
converter is explicitly proven to strip or accept them.

Retry transient provider errors such as `429`, `RESOURCE_EXHAUSTED`,
`rate_limit`, quota exceeded, or equivalent throttles during imagegen, hosted
LLM calls, runtime conversion, or live API validation with a few-minute backoff.
Declare a blocker only after at least three retry attempts or a non-retryable
error.

## Recommended Commands

Default active-queue generation:

```text
/goal Execute GOAL.md end to end using run.md.
```

Default generation without demo extensions:

```text
/goal Execute GOAL.md end to end using run.md with demo_export=false.
```

Full production pass:

```text
/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.
```

Subset validation pass:

```text
/goal Execute goals/2026-06-03-subset-agentic-validation-goal.md end to end.
```

## Completion Criteria

The goal is complete only when:

- setup context, assignment snapshot, and run manifest are initialized;
- every run-start snapshot row is generated, blocked, or failed exactly once;
- generated packages pass package, schema, source-intent, reviewer, demo, and
  asset-manifest checks applicable to the run mode;
- asset-build checks pass when `asset_build` creates or curates PNG files;
- full-pass consumer/dialogue/image/final-review gates pass when
  `full_pass_pipeline=true`;
- `results.tsv`, `generated_activity_ids.txt`, `assignments.md`, and
  `run_manifest.yaml` are updated only for accepted generated packages;
- `runs/<run_id>/review_status/<activity_id>.yaml` exists for every
  generated package, copied from `runs/_templates/review_status.yaml`
  with per-activity gate status tracked by the assigned role owners;
- `runs/<run_id>/review.html` exists and validates;
- the final report lists generated, enriched/audited, blocked, failed,
  supported/degraded/unsupported demo coverage, asset status, checks, residual
  risks, and the review dashboard path.

## Assignment Type Names

Use these names in active `assignments.md` rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked or degraded |

Legacy concept aliases should be treated as
`assignment_type=activity_concept` with `activity_concept=<value>`.
