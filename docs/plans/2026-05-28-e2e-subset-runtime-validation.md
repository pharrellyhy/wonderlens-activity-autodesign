# E2E Subset Runtime Validation Plan

Date: 2026-05-28

Status: Planned

## Goal

Run a small real end-to-end validation subset across the three repos:

- `wonderlens-activity-autodesign`
- `wonderlens-activity-fullstack-demo`
- `wonderlens-ai`

The validation should prove that fresh autodesign activity packages can be
generated with demo metadata and image assets, converted or imported by the two
consumer repos, and then either played or gated according to their support
contract.

This is a validation goal, not a broad implementation goal. If the subset
reveals a substantial consumer bug, record the owning repo and evidence, then
create a follow-up implementation goal instead of burying a large fix in this
run.

## Current Evidence

Autodesign `main` includes PR #32 at `a0c0281`, which added:

- `demo_support.yaml` and `asset_manifest.yaml` package extension workflow;
- `asset_build=generate_and_curate`;
- package-local bitmap assets under `activity_packages/<activity_id>/assets/`;
- high-resolution runtime asset requirements for required assets;
- `scripts/build_activity_assets.py`;
- `scripts/validate_asset_build_outputs.py`;
- review dashboard asset visibility;
- a real smoke package at
  `runs/20260528_094915_asset_pipeline_smoke/activity_packages/smoke_asset_pipeline_collect`.

The existing historical run directories mostly predate this contract and do not
have package-local `demo_support.yaml` and `asset_manifest.yaml`. Therefore this
validation should generate a fresh scoped subset rather than reuse the old
`runs/20260521_163621_workbook_review_packet_full` packages directly.

Use the repo-local WonderLens activity asset style now embedded in `GOAL.md`,
`program.md`, and `run.md` when generating subset image assets. Generated assets
must stay in the current autodesign package-local locations and be referenced
through `asset_manifest.yaml`.

Downstream current heads inspected before this plan:

- fullstack demo: `32650f8`
- WonderLens AI: `cd6cbe6`

Both downstream repos have completed importer/ingestion goals, but those were
validated against pinned fixtures. This plan validates fresh packages produced
after the high-resolution asset contract landed.

## Validation Subset

Pick 3 to 5 packages, preferably 5 so each behavior is independently visible.
The subset should cover:

| Slice | Expected outcome |
|---|---|
| Cat1 simple | Supported and playable in fullstack-demo and WonderLens AI. |
| Cat5 simple collection | Supported and playable with on-device selectable item/card assets plus real camera/photo capture semantics. |
| Cat5 with runtime judgment | Degraded or supported only if runtime judgment is truly available; reasons must be visible. |
| Unsupported UI-heavy mechanic | Not imported as playable; selection/start must gate it. |
| Reference-bound asset case | Requires verified source metadata and high-resolution runtime assets; random generated approximations fail. |

One package may satisfy more than one slice only if the final report explains
the overlap. For example, a Cat5 judgment package may also be reference-bound,
but a separate reference-bound package is preferred because it isolates asset
fidelity from runtime judgment behavior.

Suggested activity concepts if fresh assignments are needed:

- Cat1 simple: short in-device storytelling or prediction with one generated
  entity hero asset.
- Cat5 simple collection: one-criterion real-world collection with generated
  selectable item/card assets on the device screen.
- Cat5 runtime judgment: collection where the runtime must judge a visual or
  spoken property beyond a fixed catalog match.
- Unsupported UI-heavy: sorting, drawing, coloring, tournament, or certificate
  workflow that current Cat1/Cat5 UI cannot honestly play.
- Reference-bound: constellation, public-domain artwork, map, scientific
  diagram, species, cultural artifact, historical object, named place, or
  famous structure with accepted source/provenance.

## Autodesign Contract

For every generated package:

- the five canonical files exist;
- `demo_support.yaml` exists unless the package is an explicitly blocked
  preview;
- `asset_manifest.yaml` exists for every demo-export package;
- required assets include at least one final runtime PNG at `512x512` or larger,
  with `512x512` preferred for this validation unless the current asset
  manifest requires an additional larger variant;
- generated image assets follow the WonderLens activity style: soft 3D toy
  illustration, warm whites, mint green accents, soft sky blue, gentle coral,
  pale yellow, rounded clay/plastic forms, and gentle studio lighting;
- generated image assets are square source art with the primary subject inside
  a central circular safe area, simple full-bleed background continued to the
  square edges, and no baked-in circular mask, lens border, rim, vignette,
  black corners, transparent margin, white margin, readable text, letters,
  numbers, logos, watermarks, contact sheets, or UI labels;
- Cat5 collection packages declare the selectable on-device item/card assets in
  `asset_manifest.yaml`, using roles such as `collection_correct`,
  `collection_distractor`, `card_set`, or `icon` as appropriate;
- Cat5 selectable cards/items follow the same WonderLens activity asset style
  and are referenced from `prod.md` Step 2 or Step 3 screen states by stable
  `asset_id`;
- Cat5 selectable cards/items guide the child before or around capture, but do
  not replace real camera capture or the downstream `photo_id` handoff;
- reference-bound assets include accepted package-local source metadata before
  they are considered ready;
- `prod.md` references stable `asset_id` values and fallback behavior, not raw
  local file paths;
- any `Runtime AI instruction` beat is rich enough to convert into
  fullstack-demo-style `step_instructions`: goal/action, tier or length
  constraint, emotion/tone, child progress evidence, branch behavior,
  source/activity frame guardrail, concrete example line, and specific
  screen/state behavior;
- support state is honest: `supported`, `degraded`, or `unsupported`;
- the run manifest records `asset_build=generate_and_curate`;
- `review.html` links to package-local assets and shows support/readiness
  status.

Autodesign does not directly produce WonderLens AI `runtime.yaml` as its
primary artifact. The validation should treat `runtime.yaml` as a downstream
conversion artifact produced by WonderLens AI from the autodesign package.

## Fullstack Demo Verification

Fullstack demo owns browser demo import and gating. Use its current importer:

```bash
uv run python scripts/import_autodesign_package.py <package_dirs...> --source-commit <autodesign_commit>
```

The importer should:

- convert supported Cat1 and simple Cat5 packages into parseable game
  frontmatter;
- copy package-local assets into browser-safe activity asset paths;
- copy and render Cat5 selectable item/card assets before or around photo
  capture;
- preserve explicit entity binding;
- expose support/degraded/unsupported state in entity selection metadata;
- gate unsupported packages from playable start;
- fail or block required missing assets instead of creating broken games.

Browser or API smoke should verify at least:

- imported Cat1 starts;
- imported Cat5 starts, shows selectable item/card assets, reaches the
  collection loop, sends or simulates `photo_id`, and continues into the
  detail/text response phase;
- degraded Cat5 is visible with reasons and behaves according to its configured
  support state;
- unsupported UI-heavy package is not selectable or does not start as playable;
- reference-bound asset URLs resolve and display without falling back to a
  generated approximation.

## WonderLens AI Verification

WonderLens AI owns runtime conversion, package loading, API/WS execution, and
package asset serving. Use the current runtime generator:

```bash
uv run python scripts/generate_activity_runtime.py \
  --source <autodesign_run>/activity_packages \
  --dest .artifacts/e2e-subset-runtime/activities \
  --write \
  --force \
  --report-json .artifacts/e2e-subset-runtime/report.json
```

Then verify:

- every expected executable package has `runtime.yaml`;
- `demo_support.yaml` and `asset_manifest.yaml` are ingested;
- explicit entity binding is preserved in runtime/report metadata;
- unsupported packages are not executable;
- degraded packages carry reasons and are executable only when the runtime can
  honestly support the limitation;
- package-local assets resolve through safe server URLs;
- Cat5 runtime state preserves the selectable card/item context while still
  treating `photo_id` as the real captured input;
- Activity API or Activity WS behavior follows the generated runtime beats
  closely enough to match the autodesign `prod.md` guidance.

For live runtime behavior, prefer the debug activity pipeline or exact-package
handoff path when available, because it avoids reselecting a different activity
from the photo.

## Delegated Validation Strategy

Delegated agents are useful here because the validation surface is split by
repo and by responsibility. Use them only where ownership is disjoint.

Good delegated-agent slices:

- autodesign package reviewer: verify the generated subset package files,
  support states, asset manifests, source metadata, and review dashboard;
- visual/reference reviewer: inspect generated bitmap assets, round-screen crop
  safety, and reference-bound source fidelity;
- fullstack demo reviewer: import the subset and verify playability/gating
  without modifying autodesign;
- WonderLens AI reviewer: generate/check `runtime.yaml`, load packages, and
  compare runtime behavior against `prod.md`;
- independent final reviewer: read the result report and verify that failures
  are assigned to the right repo.

The main agent owns orchestration, source-of-truth decisions, credentials,
server lifecycle, final report, final checks, and commits.

## Credential And Server Safety

Live provider checks may require `.env` files or Google credentials in the
consumer repos. Do not edit, print, copy, or commit secrets.

Source credentials only in the shell that starts the relevant server. Record
which repo's environment was used, but never record secret values. If
credentials are missing or invalid, stop live-provider verification and record
the exact missing prerequisite as a blocker.

Do not leave long-running server sessions open after the goal completes or
blocks.

## Required Evidence

The final validation report should include:

- autodesign commit and run path;
- selected activity IDs and which validation slice each covers;
- support state and expected consumer behavior for each package;
- asset output summary, including dimensions and reference-bound source
  metadata status;
- WonderLens AI `runtime.yaml` generation report path;
- fullstack demo import output and generated game IDs;
- API/browser/WS smoke evidence for playable and gated cases;
- dialogue/runtime quality notes comparing downstream behavior to `prod.md`;
- defects or blockers, grouped by owning repo;
- exact commands run and pass/fail status.

Prefer storing the report under the autodesign run directory, for example:

```text
runs/<run_id>/e2e_subset_validation.md
```

Use downstream `.artifacts/` directories for transient consumer reports.

## Non-Goals

- Do not regenerate all 40 workbook activities.
- Do not redesign fullstack-demo UI/device shell.
- Do not implement Cat3, sorting, drawing, coloring, tournament, or certificate
  runtimes as part of this validation.
- Do not make Java/device clients parse package YAML directly.
- Do not silently accept reference-bound generated approximations.
- Do not mark the validation complete with only fixture tests; the subset must
  use a fresh autodesign run.

## Open Risks

- The fresh subset may reveal that a downstream importer supports fixtures but
  not the latest package shape. That is useful evidence, but large fixes should
  become separate repo-specific goals.
- Live provider behavior may differ from deterministic tests because of
  credential availability, model behavior, latency, or server configuration.
- Runtime dialogue quality comparison is partly judgment-based. Use delegated
  review and cite concrete `prod.md` beats, `runtime.yaml` fields, and observed
  turns rather than broad impressions.
