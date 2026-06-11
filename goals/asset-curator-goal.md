# Asset Curator Goal

## Mode

Re-runnable. Accepts `RUN_ID` and `ACTIVITY_ID` as parameters.

Use this file as the Codex goal-mode execution contract for generating or
curating runtime image assets for a single activity package. Run it once per
assigned activity, as many times as needed until asset QA passes.

## Objective

Generate or curate source images for every required runtime asset declared in
`runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/asset_manifest.yaml`, build
package-local runtime PNGs, run image QA, and update the per-activity review
status file. Do NOT edit package text, dialogue, mechanics, or downstream
consumer repos.

## Parameters

Replace these before each run:

```text
RUN_ID=<run_id>                # e.g. 20260611_093000_batch3
ACTIVITY_ID=<activity_id>      # e.g. constellation_count
```

## Source Documents

- `docs/activity_asset_generation_workflow.md` — WonderLens flat Nordic style
  contract, round-screen rules, picker item requirements.
- `docs/asset_style_reference/wonderlens-activity-style.md` — style prompt and
  reference image.
- `docs/asset_style_reference/style-reference-flat-nordic.png` — visual target.
- `docs/image_generation_provider_setup.md` — Gemini provider setup for
  non-Codex operators.
- `docs/asset_curator_daily_workflow.md` — detailed session workflow.
- `docs/full_pass_agentic_parallel_workflow.html` — file ownership matrix.

## Allowed Files

- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/asset_manifest.yaml`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/assets/**`
- `runs/<RUN_ID>/generated_assets/**`
- `runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml`
- `runs/<RUN_ID>/manual_audits/<ACTIVITY_ID>_prompt_trace.md`
- Narrow corrections to `spec.md` `## Asset Brief` and `## Asset Usage Timeline`
  (asset IDs and paths only, not activity design)

## Forbidden Files

- `prod.md` mechanics, dialogue, or branch behavior
- `spec.md` activity design rationale (except asset brief path corrections)
- `tag_block.yaml`, `demo_support.yaml`, `recap.template.yaml`,
  `dashboard.template.yaml`
- Downstream app repos
- Unrelated activity packages

## Hard Constraints

- Use `asset_manifest.yaml` as the source of truth for asset requirements.
- Illustrative assets must follow the flat Nordic style contract in
  `docs/activity_asset_generation_workflow.md`.
- Illustrative source PNGs come from Codex built-in `imagegen` or the
  configured Gemini provider in `docs/image_generation_provider_setup.md`.
  Do not accept SVG/vector/placeholder substitutes as generated art.
- Reference-bound assets require approved source originals and metadata under
  `assets/sources/`; random generated approximations fail.
- Scene assets must visually explain the beat's child action, not use generic
  placeholder subjects (baskets, blank cards, empty rooms, glows).
- Story-scene assets must feel like coherent real-world scenes with concrete
  beat-to-beat changes.
- Picker/catalog assets: 4 correct items + 8 distractors unless the run goal
  records an approved smaller catalog. Item/object PNGs are separate files
  under `assets/items/`.
- No baked text, letters, numbers, UI chrome, masks, borders, logos,
  watermarks, contact sheets, or multi-card sheets in generated assets.
- Round-screen variants keep detail inside the central 70-75% circle.
- Scene backgrounds must not contain duplicate selectable objects that compete
  with picker sprites.

## Required Checks

```bash
RUN_ID="<run_id>"
ACTIVITY_ID="<activity_id>"

# Run the deterministic builder
python3 scripts/build_activity_assets.py runs/${RUN_ID} --mode generate_and_curate

# Validate build outputs
python3 scripts/validate_asset_build_outputs.py runs/${RUN_ID}

# For larger production runs, also run:
python3 scripts/repair_full_pass_asset_bundle.py runs/${RUN_ID}
python3 scripts/validate_asset_granularity.py runs/${RUN_ID}
python3 scripts/validate_full_pass_asset_bundle.py runs/${RUN_ID}

# Create manual prompt trace
python3 scripts/validate_demo_package_contract.py \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}

git diff --check
```

## Required Scope

1. Read `asset_manifest.yaml`, `spec.md` `## Asset Brief`, and `prod.md`
   display beats for asset context.
2. Classify each asset as illustrative or reference-bound.
3. **Illustrative assets:**
   - Generate source PNGs, place in
     `runs/<RUN_ID>/generated_assets/inbox/<ACTIVITY_ID>/<asset_id>.png`.
   - Every scene prompt must tie to the beat's child action, learning evidence,
     and runtime screen state.
4. **Reference-bound assets:**
   - Accept only approved sources. Store originals under
     `assets/sources/<asset_id>__source_original.<ext>`.
   - Write `assets/sources/<asset_id>__source_metadata.yaml` with verified
     source type, license, storage_allowed, sha256, and verification status.
5. Run the deterministic builder and asset validators.
6. Run independent image QA — inspect actual PNGs against the style contract.
7. Repair image-owned failures with a prompt root-cause note and exact
   regeneration prompt.
8. Update `review_status/<ACTIVITY_ID>.yaml` `asset_review` block with status,
   reviewer, generated sources, reference sources, findings, and next_owner.
9. Create a manual prompt trace at
   `runs/<RUN_ID>/manual_audits/<ACTIVITY_ID>_prompt_trace.md`.
10. Run required checks.

## Completion Gate

The goal is complete when:

- Every required runtime asset has a source (generated or curated).
- Illustrative assets follow the flat Nordic style contract and pass visual QA.
- Reference-bound assets have approved source originals and metadata.
- The deterministic builder and all validators pass.
- Image QA passes or failures are recorded with root-cause notes.
- `review_status/<ACTIVITY_ID>.yaml` `asset_review.status` is `pass` or
  `needs_fix` with a concrete repair scope.
- Required checks pass.
- Intended asset files and metadata are committed.

## Goal Invocation

```text
/goal Execute goals/asset-curator-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```
