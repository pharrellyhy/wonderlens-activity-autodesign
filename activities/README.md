# Activities

Canonical/promoted per-game directory layout. Each subdirectory describes one activity in five required files, with optional package-local demo/export extension files when a package claims direct demo readiness.

## Layout

```
activities/
├── _schema/
│   ├── tag_block.schema.json        # JSON Schema for tag_block.yaml
│   ├── demo_support.schema.json     # JSON Schema for optional demo_support.yaml
│   └── asset_manifest.schema.json   # JSON Schema for optional asset_manifest.yaml
├── README.md                         # this file
└── <activity_id>/
    ├── spec.md                       # authoring intent: premise, target, rationale, selection trigger, optional asset brief
    ├── prod.md                       # runtime dialogue + step instructions
    ├── tag_block.yaml                # structured metadata (validated against _schema/tag_block.schema.json)
    ├── recap.template.yaml           # child recap payload shape (runtime-rendered)
    ├── dashboard.template.yaml       # parent dashboard fragment shape (runtime-rendered)
    ├── demo_support.yaml             # optional: demo support gate and entity binding
    └── asset_manifest.yaml           # optional: runtime asset roles, prompts, variants, paths
```

The directory name MUST equal the `activity_id` inside that dir's `tag_block.yaml`.

Fresh `/goal` generation writes run-local packages under `runs/<run_id>/activity_packages/<base_activity_id>/` with clean `activity_id` values. Do not add fresh rerun packages directly under `activities/` unless explicitly promoting the package to the canonical set. Existing checked-package enrichment may update a package here in place when the checked row points to an existing canonical package.

## File roles

| File | Audience | Format | Runtime role |
|---|---|---|---|
| `spec.md` | authors, reviewers | Markdown prose | design reference; not loaded by runtime; owns the self-evaluation scorecard and optional `## Asset Brief` |
| `prod.md` | authors, LLM prompt composer | Markdown prose | quoted into prompts; beat-level guidance; all runtime rounds fully expanded; references asset IDs only |
| `tag_block.yaml` | matcher, selector | YAML | machine-readable metadata; schema-validated |
| `recap.template.yaml` | recap renderer | YAML with `{placeholders}` | per-session payload emitted at activity end |
| `dashboard.template.yaml` | parent dashboard roller | YAML with `{placeholders}` | per-session fragment merged into device rollup |
| `demo_support.yaml` | demo importer, reviewers | YAML | optional extension declaring `supported`, `degraded`, or `unsupported` demo readiness, UI template, explicit entity binding, and limitations |
| `asset_manifest.yaml` | asset generator, demo importer | YAML | optional extension declaring separate runtime assets, style, screen targets, variants, file slots, fallback behavior, and reference provenance |

## Runtime completeness invariants

- `prod.md` must not contain `## Self-Evaluation Scorecard`.
- `spec.md` must contain exactly one `## Self-Evaluation Scorecard`.
- If an activity references AI-generated images, prebuilt card sets, line art, icons, overlays, or displayed reference images, `spec.md` must include `## Asset Brief` before the scorecard.
- If an activity references AI-generated images, prebuilt card sets, line art, icons, overlays, or displayed reference images, `spec.md` must also include `## Asset Usage Timeline` before the scorecard so reviewers can track where and when each asset is generated, loaded, displayed, used, persisted or hidden, and replaced by fallback.
- `prod.md` may reference stable `asset_id` values, display locations, and fallback behavior, but must not include raw image-generation prompts.
- Every Step 3 round in `prod.md` must be fully executable: AI dialogue, child response branches, AI follow-up branches, and screen state.
- Steps 1, 2, 4, and 5 must also be executable enough for the runtime prompt composer: concrete AI dialogue, branch-specific follow-ups where applicable, and specific screen states.
- Do not use condensed placeholders such as "same structure," "AI gives a riddle," "later rounds follow," or one-line summaries in migrated `prod.md` files.
- Do not treat compact migrated files as a lower-detail target. `spec.md` must preserve decision-useful design rationale, and `prod.md` must preserve concrete game feel, progress, payoff, and source-promise behavior.
- During `/goal` runs, generated packages are accepted only after independent reviewer-agent PASS evidence; reviewer FAILs must be repaired and re-reviewed before logging or assignment checkoff.
- During fresh `/goal` generation, a new run-local package directory is required even when the assignment supplies an `activity_id` that already exists. This keeps rerun outputs distinguishable by run path while preserving clean base IDs.
- Blocked activity concepts may have run-local constrained previews under `runs/<run_id>/blocked_designs/`, but those previews are not activity packages and must not be copied here until blockers are resolved and the standard five-file gates pass.
- Product-contract override runs may convert formerly blocked minimum-to-unblock items into valid run-local packages only when the package records resolved blocker notes in `spec.md`, affected `prod.md` beats, and the run manifest.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` must exactly equal `tag_block.yaml` `activity_signature.focal_attribute`.
- `demo_support.yaml` and `asset_manifest.yaml` are optional extension files. A package without them remains a valid five-file activity package, but it is not direct-demo-import ready.
- If `demo_support.yaml` declares `status: supported` or `status: degraded`, the package must include `asset_manifest.yaml`, at least one explicit entity binding, and a playable `ui_template`.
- If `demo_support.yaml` declares `status: unsupported`, consumers must not expose the package as playable; the file must state `ui_template: none` and explain the missing mechanic, UI, asset, or runtime capability.

## Asset brief invariant

`## Asset Brief` is an authoring dependency record. It remains useful for reviewer context, but demo-ready runtime asset contracts should also be represented in package-local `asset_manifest.yaml` instead of only as prose in `spec.md`. Each Asset Brief row should define:

| Field | Purpose |
|---|---|
| `asset_id` | Stable ID used by `prod.md` screen descriptions. |
| `asset_type` | `reference_image`, `character_image`, `scene_background`, `line_art`, `card_set`, `icon`, or `ui_overlay`. |
| `requiredness` | `required`, `optional`, or `fallback`. |
| `generation_timing` | `pre_generated`, `runtime_generated`, `display_existing`, or `none`. |
| `use_step` | Exact step/round where the asset appears. |
| `display_location` | Screen region or UI slot where the asset appears. |
| `prompt_en` | Direct English generation prompt for generated assets. |
| `source` | Existing asset library, approved reference set, or source description when no generation prompt is needed. |
| `display_behavior` | How the runtime should present it. |
| `fallback_behavior` | What runtime does if it is missing. |
| `safety_constraints` | Visual safety and content constraints. |

Current package generation does not create image files by default. Demo-targeted packages request separate runtime assets through `asset_manifest.yaml`; contact sheets are review artifacts only and must not be treated as runtime assets. A later asset build phase may consume these manifests and write generated files plus `generated_assets/asset_outputs.yaml`, but the source package contract remains the manifest.

`## Asset Usage Timeline` should restate the operational view in a compact table: `asset_id`, `generation_timing`, load/generate moment, first display step, visible step/round range, display location, interaction/use, persistence/hide behavior, and fallback. This section is optimized for `review.html`, not for asset generation.

## Demo extension contract

`demo_support.yaml` tells consumer repos whether a package can be shown in a current demo UI. Required fields:

| Field | Purpose |
|---|---|
| `activity_id` | Must match the package activity ID. |
| `version` | Positive integer schema version. |
| `demo_support.status` | `supported`, `degraded`, or `unsupported`. |
| `demo_support.ui_template` | `cat1_dialogue`, `cat5_collection`, `cat5_judgment`, or `none`. |
| `demo_support.entity_bindings` | Explicit activity-to-entity binding; exactly one binding should have `default: true`. |
| `demo_support.requires` | Booleans for `generated_assets`, `real_camera`, `runtime_judgment`, and `device_round_screen`. |
| `demo_support.unsupported_reasons` | Required when `status: unsupported`. |
| `demo_support.degraded_reasons` | Required when `status: degraded`. |
| `demo_support.consumer_notes` | Consumer-specific guidance, such as fullstack demo limitations. |

`asset_manifest.yaml` describes each runtime asset separately. Do not collapse several cards into one contact sheet. Required fields:

| Field | Purpose |
|---|---|
| `activity_id`, `entity_id`, `version` | Identity for the package and bound demo entity. |
| `style_id` | Must be `wonderlens_device_mint_soft_3d` unless a future schema adds another approved style. |
| `palette` | Prototype-aligned colors: warm porcelain shell, green-tinted near-black screen, soft mint primary accent, optional pale sage/shadow accents. |
| `screen_targets` | At minimum `round_device_screen` with `aspect_ratio: "1:1"`, `crop_shape: circle`, master size, and a central percent-circle safe area. |
| `assets[].role` | `entity`, `activity_preview`, `collection_correct`, `collection_distractor`, `badge`, `story_scene`, or `ui_overlay`. |
| `assets[].accuracy_mode` | `illustrative` or `reference_bound`. |
| `assets[].source_strategy` | `generated_illustrative`, `curated_original`, `redraw_from_verified_data`, `licensed_reference`, or `approved_internal_reference`. |
| `assets[].transformation_policy` | `generate_new`, `crop_resize_only`, `simplified_redraw`, `style_preserving_redraw`, or `no_derivative_generation`. |
| `assets[].prompt_en` | Required for generated illustrative assets; must be English and directly usable by an asset pipeline. |
| `assets[].variants` | Per-target variants such as `round_512`, `icon_256`, `badge_512`, `landscape_1280x720`, with nullable `path` slots before files exist. |
| `assets[].fallback_behavior` | What the runtime does when the asset is unavailable. |

Use style `wonderlens_device_mint_soft_3d` for demo assets:

```text
Soft 3D educational toy illustration, mint green and warm porcelain palette,
rounded friendly shapes, subtle plastic material, clean centered subject,
gentle studio lighting, no text, no watermark, designed for a small round
screen.
```

Round-screen variants must keep important detail inside the central 70 to 75 percent circle and remain recognizable at 144 px. The horizontal debug-screen variant may exist for web demos, but the round device screen is the primary design target.

Reference-bound assets represent real-world facts or identities, such as constellations, artworks, maps, scientific diagrams, cultural artifacts, species, historical objects, named places, and famous structures. They must include `source_strategy`, `transformation_policy`, `reference_policy`, and at least one source/provenance entry. Prompts must preserve the approved reference first, then apply device style. Random or arbitrary generated approximations do not validate.

For reference-bound assets, agents may propose candidate references, but accepted manifests must record only verified sources. Do not scrape or use arbitrary web-image results. Use approved source types only: public-domain museum/archive sources, official or verified source URLs, licensed/internal asset libraries, verified educational/scientific sources, or structured data that can be redrawn accurately. Famous public-domain artwork should normally use `source_strategy: curated_original` with `transformation_policy: crop_resize_only` or `no_derivative_generation`; constellations and diagrams should normally use `source_strategy: redraw_from_verified_data` with `transformation_policy: simplified_redraw`.

## Asset build modes

`demo_export` controls whether packages emit `demo_support.yaml` and `asset_manifest.yaml`. `asset_build` controls whether a run attempts to create image files from those manifests.

| `asset_build` | Behavior |
|---|---|
| `none` | Do not run asset generation or curation; packages may still be valid but are not asset-complete. |
| `manifest_only` | Default. Emit and validate manifests with nullable asset paths; do not create binary image files. |
| `generate_illustrative` | Generate only `accuracy_mode: illustrative` assets; leave reference-bound assets missing unless approved sources already exist. |
| `curate_reference` | Search/curate approved sources for `reference_bound` assets and record provenance; do not generate arbitrary substitutes. |
| `generate_and_curate` | Generate illustrative assets and curate/reference-build approved reference-bound assets in one post-package phase. |

When image files are built, write them under `runs/<run_id>/generated_assets/<activity_id>/` and record actual outputs in `runs/<run_id>/generated_assets/asset_outputs.yaml`. Do not overwrite `asset_manifest.yaml` paths unless an explicit promotion/integration step chooses to bind built files back into the package.

## Canonical vocabulary

The three closed enums in `tag_block.yaml activity_signature` — `observation_angle` (12), `mechanic` (12), `entity_role` (4) — are defined in [`docs/activity_vocabulary.md`](../docs/activity_vocabulary.md). `template_type` is also schema-controlled and currently supports `cat1`, `cat3`, and `cat5`. The schema's enum lists must stay in sync with that doc; drift is CI-blocked.

For field ownership and authoring guidance, use [`docs/activity_tag_block_usage.md`](../docs/activity_tag_block_usage.md). It separates matcher-facing, runtime-presentation, child-recap, and parent-dashboard fields.

For a full tag-block plus progression-algorithm reference, use [`docs/activity_tag_block_progression_guide.md`](../docs/activity_tag_block_progression_guide.md) or the Chinese companion [`docs/activity_tag_block_progression_guide_cn.md`](../docs/activity_tag_block_progression_guide_cn.md). For workflow diagrams, use [`docs/activity_matcher_progression_workflows.md`](../docs/activity_matcher_progression_workflows.md) or the Chinese companion [`docs/activity_matcher_progression_workflows_cn.md`](../docs/activity_matcher_progression_workflows_cn.md).

## Validation

Validate all `tag_block.yaml` files against the schema:

```bash
python3 -c "
import json, yaml, pathlib, sys
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
ok = True
for p in sorted(pathlib.Path('activities').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK  ' if not errs else 'FAIL'), p)
    for e in errs:
        ok = False
        print(f'  {list(e.absolute_path)}: {e.message}')
sys.exit(0 if ok else 1)
"
```

Requires `pip install jsonschema pyyaml`.

Validate optional demo extension files with the focused validator:

```bash
python3 scripts/validate_demo_package_contract.py activities
```

For fixtures:

```bash
python3 scripts/validate_demo_package_contract.py tests/fixtures/demo_package_contract/valid
```

## Current V1 coverage

This repository currently contains 32 canonical/promoted five-file activity package directories under `activities/`. Fresh run-local packages live under `runs/<run_id>/activity_packages/`. Legacy single-file outputs remain under `designs/` for historical reference and migration work.

## Cross-repo notes

Consumer repos (`wonderlens-ai`, `wonderlens-activity-fullstack-demo`) mirror tag-block enums in code. Additions to `docs/activity_vocabulary.md` require matching changes in both consumer repos; see the `## Versioning` section of that doc. The optional demo schemas are producer-side contracts for those consumers, but they do not change tag-block enums.
