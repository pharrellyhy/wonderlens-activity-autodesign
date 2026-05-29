# Source Intent Pilot Validation Plan

Date: 2026-05-29

Status: Planned

## Goal

Run a focused 3 to 5 activity pilot selected from the original source-design
inputs before scaling to a larger or full pass. The pilot must prove that the
generation workflow preserves the original activity intent, produces runtime AI
instructions that can become strong downstream `step_instructions`, generates
runtime PNG assets when requested, and loads cleanly in both consumer repos.

This is a validation and contract-hardening plan. If the pilot reveals a large
consumer bug, record the owning repo and evidence, then create a separate
follow-up goal instead of hiding broad implementation work inside this run.

## Current Evidence

The current `GOAL.md`, `run.md`, and `program.md` already require
`source_promise_alignment`, independent reviewer-agent coverage, migrated
package depth, runtime instruction quality, demo support metadata, and asset
manifests. They do not yet require a named standalone source-intent auditor
checklist for every pilot package.

Recent downstream validation showed that:

- fullstack-demo can import autodesign packages and convert runtime beats into
  `step_instructions`;
- WonderLens AI can generate/load runtime artifacts from autodesign packages;
- pydantic contract mismatches and runtime-beat conversion gaps are small enough
  to fix when they appear;
- the strongest current fullstack runtime-instruction quality reference is
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/games/fluffy_expedition_dandelion.md`.

The pilot should intentionally include examples where drift is easy to miss,
such as factual/reference assets, required background information, multi-step
child action, and asset-dependent screens.

The current original source-design input is:

```text
inputs/source_activity_concepts.md
```

Assignment rows in `assignments.md` Batch 4 already point into this file with
`concept_source=inputs/source_activity_concepts.md#source_*`. Historical
source-intent audit evidence also exists under run-local
`source_comparison/source_intent_audit.yaml` files and can help prioritize
high-risk rows.

## Source Designs

Select 3 to 5 activity designs from the original source-design inputs. If the
user names specific designs, use those first. Otherwise, choose representative
high-risk rows from `inputs/source_activity_concepts.md` and record the
selection rationale before generation.

If the user provides additional designs in chat or another non-versioned form,
capture a stable source snapshot before generation under the run directory or
another explicit input file so reviewers can compare the generated package
against the original wording.

Preferred coverage:

| Slice | Why it matters |
|---|---|
| Factual/reference asset | Prevents arbitrary generated approximations, especially constellations, maps, diagrams, artworks, named places, or species. |
| Required background information | Catches cases where a generated activity keeps the mechanic but drops the teaching/context promise. |
| Multi-step child action | Catches sequence drift and child-role drift. |
| Asset-dependent scene/character/object | Verifies `asset_manifest.yaml`, generated PNGs, screen references, and fallback behavior. |
| Simple control activity | Confirms the stricter audit does not overfit only hard cases. |

One design may cover more than one slice, but the final report must explain the
overlap. Do not use only old fixtures or previously accepted packages.

Default candidate set if the user does not override:

| Concept source | Activity | Why this belongs in the pilot |
|---|---|---|
| `inputs/source_activity_concepts.md#source_constellation_star_count` | Constellation Star Count | Known high-risk source-intent case: child chooses a number, device reveals a real matching constellation, and AI gives background information. Requires reference-bound assets and must not become arbitrary star counting. |
| `inputs/source_activity_concepts.md#source_plant_parts_explorer` | Plant Parts Explorer | Tests whether generated beats preserve photo-based plant-part exploration and required part-function/background notes instead of generic naming/counting. |
| `inputs/source_activity_concepts.md#source_career_decision` | Career Decision | Tests child-role and sequence fidelity: the child must be placed into a profession role and make expert decisions, not merely match professions to scenarios. |
| `inputs/source_activity_concepts.md#source_partial_reveal_guess` | Partial Reveal Guess | Tests required visual-asset flow: the screen shows a distinctive part, the child guesses the whole, and the AI follows visible evidence rather than voice-only generic clues unless fallback is explicit. |
| `inputs/source_activity_concepts.md#source_would_you_rather` | Would You Rather | Simple control activity with no asset dependency, useful for proving the stricter audit does not overfit only hard/reference cases. |

## Contract Hardening

Before accepting pilot output, strengthen the run contract in the relevant
source documents if it is not already present:

- `run.md`: add the primary source-intent audit gate near the independent
  reviewer step, because this file controls execution flow.
- `GOAL.md`: add the top-level completion-contract wording so `/goal` runs
  report source-intent auditor coverage and block on unresolved drift.
- `program.md`: add the reusable generation/review rule so new designs outside
  the exact pilot still inherit the quality bar.

The source-intent auditor must compare the original source design against the
adaptation brief, `spec.md`, `prod.md`, `tag_block.yaml`, `asset_manifest.yaml`,
and downstream conversion artifacts when available.

Required checklist fields:

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
- verdict: `aligned`, `minor_adaptation`, `intent_drift`, or
  `needs_product_decision`;
- repair required and re-review outcome.

`intent_drift` blocks `results.tsv` logging, assignment checkoff, downstream
acceptance, and final completion until repaired or explicitly recorded as a
product-review finding.

## Asset Build Contract

Set the pilot run to:

```text
asset_build=generate_and_curate
```

This is required so the pilot produces actual runtime PNGs, not only nullable
manifest paths.

Expected asset behavior:

- `asset_manifest.yaml` declares separate runtime assets by role, such as
  `entity`, `story_scene`, `activity_preview`, `collection_correct`,
  `collection_distractor`, `badge`, or `ui_overlay`;
- illustrative assets use `accuracy_mode: illustrative`,
  `source_strategy: generated_illustrative`, and `transformation_policy:
  generate_new`;
- reference-bound assets use `accuracy_mode: reference_bound` and verified
  source/provenance, never arbitrary generated approximations;
- the executing agent or delegated visual agent creates illustrative source PNGs
  under `runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png`;
- accepted reference originals and metadata live under package-local
  `assets/sources/`;
- `scripts/build_activity_assets.py` creates package-local runtime variants
  under `runs/<run_id>/activity_packages/<activity_id>/assets/`;
- `scripts/validate_asset_build_outputs.py` passes before final review;
- missing required sources are recorded as failures instead of fake paths.

Generated illustrative PNGs must follow the built-in WonderLens activity asset
style from `GOAL.md` and `program.md`: soft 3D educational toy illustration,
warm white and mint prototype-device palette, soft sky blue, gentle coral, pale
yellow, rounded clay/plastic forms, gentle studio lighting, square full-bleed
art, central round-screen safe area, no text, no logo, no watermark, and no
baked-in device chrome.

## Runtime Instruction Quality

Runtime AI instructions must be judged against downstream conversion needs, not
only against authoring readability.

Every runtime beat that uses `Runtime AI instruction` must include enough
structure to become quality `step_instructions` in fullstack-demo and
WonderLens AI:

- beat goal/action;
- tier or response-length constraint;
- emotion/tone;
- required story/setup or role-play frame;
- exact child challenge/action;
- child progress evidence;
- branch behavior for expected, unexpected, and quiet/no-response cases;
- source-intent guardrails;
- safety/product constraints;
- screen/state expectation;
- example AI line that demonstrates, but does not replace, the instruction;
- explicit "must not skip" details when background information, reference
  assets, or child action sequencing are part of the source promise.

Use the current fullstack example
`backend/games/fluffy_expedition_dandelion.md` as a practical quality floor for
converted `step_instructions`.

## Downstream Validation

Fullstack demo path:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
```

Validate that the importer converts the pilot packages into quality
`step_instructions`, preserves support/degraded/unsupported state, copies or
serves package-local assets, and gates unsupported activities honestly.

WonderLens AI path:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai
```

Validate that the runtime generator converts/loads the pilot packages cleanly,
preserves demo support and asset metadata, serves package-local assets safely,
and produces runtime behavior that matches `prod.md`.

## Delegated Review Strategy

Use delegated agents where ownership is disjoint:

- source-intent auditor: compare original source designs against generated
  packages and downstream conversion outputs;
- runtime-instruction reviewer: compare `prod.md` runtime beats and downstream
  `step_instructions` quality;
- visual/reference reviewer: inspect generated PNGs, safe-area framing, and
  reference-bound provenance;
- fullstack reviewer: import and smoke the pilot in fullstack-demo;
- WonderLens AI reviewer: generate/load runtimes and compare behavior to
  `prod.md`;
- final reviewer: check that the final report assigns failures to the right
  repo and does not hide unresolved drift.

The main agent owns orchestration, input normalization, source-of-truth
decisions, credentials, server lifecycle, final report, and commits.

## Required Evidence

The final pilot report should live under the autodesign run directory, for
example:

```text
runs/<run_id>/source_intent_pilot_validation.md
```

It must include:

- source design snapshot path and selected activity IDs;
- autodesign commit and run path;
- `asset_build=generate_and_curate` evidence;
- generated asset summary with PNG paths, dimensions, and reference metadata;
- source-intent auditor checklist and verdict for each package;
- runtime-instruction quality review for each package;
- fullstack import output and generated game IDs;
- fullstack `step_instructions` quality comparison, including the
  `fluffy_expedition_dandelion.md` quality floor;
- WonderLens AI runtime generation report path;
- WonderLens AI load/conversion/runtime-beat comparison evidence;
- blockers or defects grouped by owning repo;
- exact commands run and pass/fail status;
- recommendation on whether to proceed to a larger/full pass.

## Non-Goals

- Do not run a full assignment pass until the pilot passes or the remaining
  failures are explicitly accepted as product follow-ups.
- Do not change the original source designs to make generation easier unless
  the user approves the source edit.
- Do not make unsupported mechanics playable just to pass downstream checks.
- Do not accept generated approximations for reference-bound assets.
- Do not implement broad downstream rewrites inside this pilot.
- Do not commit secrets, local credentials, or long-lived server artifacts.

## Open Risks

- The user-supplied designs may require product/runtime capabilities that are
  not yet represented by the package contract; those should become blocked
  previews or product-decision findings instead of drifted runnable packages.
- Reference-bound assets may need real source curation and reviewer acceptance
  before PNG variants can validate.
- Runtime instruction quality is partly judgment-based; use delegated review
  and concrete file/section evidence rather than broad impressions.
- Consumer repos may expose conversion gaps. Small contract mismatches can be
  fixed in the owning repo; larger feature gaps should become separate goals.
