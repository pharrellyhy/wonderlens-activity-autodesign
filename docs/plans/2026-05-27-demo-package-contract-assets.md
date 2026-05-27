# Demo Package Contract And Assets Implementation Plan

Date: 2026-05-27

Status: Completed

## Goal

Define the autodesign-side package contract that lets generated activity
packages be consumed by the fullstack demo without guessing missing runtime or
visual information.

This plan owns the producer side only:

- demo support metadata;
- separate runtime asset manifests;
- device-compatible image style, size, and safe-area rules;
- unsupported and degraded mechanic classification;
- validation that sample packages can be handed to a consumer repo.

The consumer implementation is tracked separately in:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/docs/plans/2026-05-27-autodesign-package-demo-import.md
```

## Current Context

Autodesign canonical packages currently require five files:

```text
activities/<activity_id>/
  spec.md
  prod.md
  tag_block.yaml
  recap.template.yaml
  dashboard.template.yaml
```

`activities/README.md` states that current package generation does not create
image files. `spec.md` can include an Asset Brief and Asset Usage Timeline, and
`prod.md` may reference stable asset IDs and fallbacks, but there is no
package-local runtime asset manifest that a web demo can consume directly.

Earlier asset work generated prebuilt contact sheets for review. Those are not
runtime-ready assets because a contact sheet bakes multiple images into one
file, lacks per-item safe zones, and does not define screen target variants.

The fullstack demo currently needs a concrete, machine-readable handoff:

- whether the package is playable in the existing Cat1/Cat5 demo UI;
- which entity binding should be used for the demo instance;
- which visual assets are required, optional, or fallback-only;
- what prompts and generated files belong to each asset;
- whether each asset is safe for a small round device screen and for the
  current horizontal debug screen.

## Settled Decisions

- Keep the five canonical package files as the required authoring contract.
- Add demo and asset data as optional package-local extension files, not as raw
  prose embedded in `prod.md`.
- Do not make a contact sheet the runtime asset. Contact sheets may remain
  review references only.
- Generate or request separate assets per runtime role: entity hero, Cat5
  correct item, Cat5 distractor, badge, story scene, and optional activity
  thumbnail.
- Assets that represent real-world facts or references, such as constellations,
  artworks, maps, scientific diagrams, cultural artifacts, species, historical
  objects, or named places, must be reference-bound. They need verified source
  material or provenance and must not be arbitrary generated approximations.
- Use the prototype device as the style anchor: porcelain/off-white shell,
  dark round screen, mint controls, soft 3D toy-like educational assets, and
  child-safe simple subjects.
- Treat unsupported mechanics honestly. Do not force drawing, sorting,
  building, tournament, certificate, or complex Cat3 mechanics into the Cat1 or
  Cat5 demo UI.
- The fullstack demo should execute after this contract lands, or against a
  pinned fixture from the final autodesign commit.

## Package Extension Files

Add two optional files for packages intended for demo consumption:

```text
activities/<activity_id>/
  demo_support.yaml
  asset_manifest.yaml
```

Run-local packages may use the same shape under:

```text
runs/<run_id>/activity_packages/<activity_id>/
  demo_support.yaml
  asset_manifest.yaml
```

These files should be required only when a package claims demo readiness. A
package without them remains a valid five-file activity package, but it is not
ready for direct fullstack demo import.

### `demo_support.yaml`

Purpose: tell consumers whether a package can be played in the current demo and
which UI template it needs.

Recommended shape:

```yaml
activity_id: fluffy_expedition_dandelion
version: 1
demo_support:
  status: supported
  ui_template: cat5_collection
  support_level: full
  entity_bindings:
    - entity_id: dandelion
      display_label: Dandelion
      source_entity_exemplar: dandelion
      default: true
  requires:
    generated_assets: true
    real_camera: false
    runtime_judgment: false
    device_round_screen: true
  unsupported_reasons: []
  degraded_reasons: []
  consumer_notes:
    fullstack_demo: Use collection_catalog as demo candidates, not as truth for
      production camera validation.
```

Allowed status values:

- `supported`: playable with existing Cat1/Cat5 demo primitives and generated
  assets.
- `degraded`: playable with explicit limitations, such as catalog/fake vision
  or text explanation for a runtime judgment case.
- `unsupported`: do not show as playable. The package needs UI or runtime
  support not in the current demo.

Allowed MVP UI templates:

- `cat1_dialogue`
- `cat5_collection`
- `cat5_judgment`
- `none`

Future templates, such as `cat3_minimal`, should be introduced only with
matching consumer support and tests.

### `asset_manifest.yaml`

Purpose: describe separate generated assets, style rules, screen targets, and
file paths or generation prompts.

Recommended shape:

```yaml
activity_id: fluffy_expedition_dandelion
entity_id: dandelion
version: 1
style_id: wonderlens_device_mint_soft_3d
palette:
  shell: "warm porcelain off-white"
  screen: "green-tinted near black"
  primary_accent: "soft mint green"
  secondary_accent: "pale sage"
  shadow: "cool gray green"
screen_targets:
  round_device_screen:
    aspect_ratio: "1:1"
    crop_shape: circle
    master_size: 1024
    safe_area: "central 72 percent circle"
  horizontal_debug_screen:
    aspect_ratio: "16:9"
    master_size: "1280x720"
assets:
  - id: entity_hero
    role: entity
    label: Dandelion
    requiredness: required
    accuracy_mode: illustrative
    prompt_en: "Soft 3D educational toy illustration..."
    variants:
      - id: round_512
        target: round_device_screen
        size: "512x512"
        path: null
      - id: landscape_1280x720
        target: horizontal_debug_screen
        size: "1280x720"
        path: null
    fallback_behavior: Show the entity label and neutral badge shape.
  - id: fuzzy_moss
    role: collection_correct
    label: Fuzzy moss
    collection_catalog_id: fuzzy_moss
    requiredness: required
    accuracy_mode: illustrative
    prompt_en: "Soft 3D educational toy illustration..."
    variants:
      - id: icon_256
        target: catalog_grid
        size: "256x256"
        path: null
      - id: round_512
        target: round_device_screen
        size: "512x512"
        path: null
```

Asset role vocabulary for MVP:

- `entity`
- `activity_preview`
- `collection_correct`
- `collection_distractor`
- `badge`
- `story_scene`
- `ui_overlay`

Asset accuracy modes:

- `illustrative`: the asset may be generated from the activity prompt as long
  as it satisfies the style, safety, and recognizability constraints.
- `reference_bound`: the asset depicts a real-world reference where correctness
  matters. Examples include constellations, artworks, maps, scientific
  diagrams, cultural artifacts, species, historical objects, named places, and
  famous structures. These assets must include source material or provenance,
  and generated variants must be checked against the reference.

Reference-bound asset entries should include:

```yaml
accuracy_mode: reference_bound
source_strategy: redraw_from_verified_data
transformation_policy: simplified_redraw
reference_policy:
  source_required: true
  allowed_sources:
    - licensed_asset
    - public_domain_reference
    - approved_internal_reference
    - verified_source_url
  verification_required: true
  verification_notes: "Must preserve the real star arrangement for Orion."
sources:
  - label: "IAU Orion constellation reference"
    uri: "https://example.invalid/reference"
    license: "public_domain_or_approved"
```

If a reference-bound asset lacks approved source material, the package should
not claim the asset is ready. It should either block demo readiness, mark the
asset as missing with fallback behavior, or request a verified source before
generation.

Future asset builds should use run-level `asset_build` modes:

- `none`: skip image generation/curation.
- `manifest_only`: default; emit manifests with nullable paths only.
- `generate_illustrative`: generate only illustrative assets.
- `curate_reference`: use agent-proposed candidates only as search leads, then
  accept verified public-domain, official, licensed/internal, or scientific
  sources.
- `generate_and_curate`: run both illustrative generation and reference
  curation/build.

## Device Visual Style Contract

All generated demo assets should use one shared style profile unless a specific
activity has an approved override.

Style ID:

```text
wonderlens_device_mint_soft_3d
```

Style prompt base:

```text
Soft 3D educational toy illustration, mint green and warm porcelain palette,
rounded friendly shapes, subtle plastic material, clean centered subject,
gentle studio lighting, no text, no watermark, designed for a small round
screen.
```

Visual constraints:

- No embedded text, letters, labels, watermarks, UI chrome, or speech bubbles.
- The subject must be recognizable at 144 px display size.
- The round-screen variant must keep all important detail inside the central
  70 to 75 percent circle.
- Use soft mint and warm porcelain accents that match the prototype device.
- Keep backgrounds simple enough to crop to a circular screen.
- Do not use the old warm storybook or photo-realistic Cat5 prompts as the
  default for device assets. Those can remain references only.
- Reference-bound assets must preserve the real-world structure or identity
  before applying device style. For example, a constellation must keep the
  correct star layout, and a named artwork must use an approved source image or
  public-domain reference rather than a random generated composition.

Recommended masters and variants:

| Asset role | Master | Required variants |
|---|---:|---|
| Entity hero | `1024x1024` | `round_512`, optional `landscape_1280x720` |
| Catalog item | `512x512` or `1024x1024` | `icon_256`, `round_512` |
| Badge | `1024x1024` transparent-safe | `badge_512`, `round_512` |
| Story scene | `1280x720` plus optional `1024x1024` | horizontal and round |
| Activity preview | `1024x1024` | `preview_512` |

## Mechanic Support Gate

Support classification should be deterministic from `tag_block.yaml`,
`prod.md`, asset requirements, and any generated runtime metadata.

MVP support policy:

| Activity shape | Status | Template |
|---|---|---|
| Cat1 dialogue, riddle, voice acting, prediction, imagination | `supported` | `cat1_dialogue` |
| Cat5 simple visual collection, such as fluffy, dots, color, shape | `supported` | `cat5_collection` |
| Cat5 requiring runtime judgment, such as beginning sound or semantic category | `degraded` | `cat5_judgment` |
| Drawing, coloring, building, sorting, tournament, certificate, complex Cat3 | `unsupported` | `none` |

Do not implement minimal runtimes for unsupported mechanics in this producer
goal. Mark them unsupported and explain the reason.

## Implementation Areas

### Contract Documentation

Likely files:

- `activities/README.md`
- `program.md`
- `templates.md`
- `docs/activity_vocabulary.md` only if a closed vocabulary is added

Expected outcome:

- The five required package files remain required.
- `demo_support.yaml` and `asset_manifest.yaml` are documented as optional
  demo extension files.
- `spec.md` and `prod.md` rules explain that image prompts belong in the asset
  manifest or Asset Brief, while runtime text references stable asset IDs.

### Schemas And Validation

Likely files:

- `activities/_schema/demo_support.schema.json`
- `activities/_schema/asset_manifest.schema.json`
- a focused validation script under `scripts/`
- tests or validation fixtures if this repo has a suitable test harness

Expected outcome:

- Demo support status and UI template values are schema-validated.
- Asset manifests validate required roles, sizes, safe-area metadata, prompts,
  fallback behavior, and catalog ID references.
- Reference-bound assets validate source/provenance fields and cannot pass as
  generated random approximations.
- Packages cannot claim `supported` if required assets are absent and no prompt
  or fallback exists.

### Generation Instructions

Likely files:

- `program.md`
- `templates.md`
- `run.md`
- any current run or transformation guidance used to produce packages

Expected outcome:

- Future generation emits separate runtime asset intents instead of one
  contact sheet when fullstack demo export is requested.
- Asset requirements include style ID, screen targets, safe area, role,
  prompt, fallback, and file-path slots.
- Unsupported mechanic handling emits `demo_support.status: unsupported`
  instead of hiding the mismatch.

### Sample Package Coverage

Use at least:

- one Cat1 package;
- one simple Cat5 package, preferably `fluffy_expedition_dandelion` or
  `polka_dot_patrol`;
- one degraded Cat5 judgment example if available;
- one unsupported package or fixture.

Sample outputs may live under a run-local fixture directory if canonical
package changes are not desired.

## Validation Strategy

Minimum checks after implementation:

```bash
git diff --check
```

Validate existing tag blocks still pass:

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

If a demo manifest validator is added, run it against the selected samples,
for example:

```bash
python3 scripts/validate_demo_package_contract.py activities
```

If binary assets are generated, validate that every manifest path exists and
that missing assets have explicit fallback behavior.

## Non-Goals

- Do not change fullstack demo code in this goal.
- Do not implement Cat3, drawing, sorting, building, tournament, or certificate
  runtimes.
- Do not require all existing canonical packages to become demo-ready.
- Do not make contact sheets the runtime asset format.
- Do not add raw image prompts to `prod.md`.
- Do not change recap or dashboard placeholder semantics unless required by a
  validated schema change.
- Do not edit secrets, local credentials, or production data.

## Completion Gate

This plan is complete when:

- demo extension files and schemas are documented;
- package generation guidance can produce `demo_support.yaml` and
  `asset_manifest.yaml`;
- separate asset roles, style, sizes, and round-screen safe zones are defined;
- supported, degraded, and unsupported mechanics are classified honestly;
- selected sample packages or fixtures validate;
- existing tag-block validation is not regressed;
- `docs/plans/README.md` and `goals/README.md` are updated;
- intended changes are committed in this repo.
