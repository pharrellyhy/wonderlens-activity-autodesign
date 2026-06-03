# WonderLens Activity Asset Generation Workflow

This document records the workflow used to create runtime image assets for
autodesign activity packages.

Repo-local style source for fresh runs:

```text
docs/asset_style_reference/wonderlens-activity-style.md
docs/asset_style_reference/style-reference-flat-nordic.png
```

These files were copied from the fullstack-demo prompt folder on 2026-06-03:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/frontend/public/activity-assets/prompts/
```

The schema value remains `style_id: wonderlens_device_mint_soft_3d` for
consumer compatibility. The current visual target for that style is the flat
Nordic nursery illustration style below, not the older soft-3D toy look.

## When Assets Are Generated

Package authoring does not create binary images. `GOAL.md` runs default to
`asset_build=manifest_only`, which emits `asset_manifest.yaml` with nullable
variant paths.

Larger/full production passes must set `asset_build=generate_and_curate` so
runtime PNGs are generated or curated before fullstack-demo and WonderLens AI
dialogue validation. The asset generator role is image-only: it reads the
accepted package manifest, approved reference material, and this style contract;
it must not rewrite activity mechanics, runtime AI instructions, source-intent
audits, or dialogue to make an image easier to accept.

Generate or curate image files only after packages pass package validation and
the run explicitly requests one of these modes:

- `generate_illustrative`: generate only `accuracy_mode: illustrative` assets.
- `curate_reference`: curate only `accuracy_mode: reference_bound` assets.
- `generate_and_curate`: do both.

## Transient API Error Handling

Treat image generation, hosted LLM, live API, and runtime-conversion errors
such as `429`, `RESOURCE_EXHAUSTED`, quota exceeded, `rate_limit`, and
equivalent provider throttles as retryable. Record a sanitized note with the
phase, activity ID or batch, command/tool name, timestamp, and error class; do
not print secrets or request payloads.

Do not stop immediately on the first throttle. Wait a few minutes before the
first retry, then use a short backoff such as 3/5/8 minutes for repeated
throttles on the same request or batch. Retry at least three times before
declaring the run blocked, and reduce concurrency or batch size when that is
safe.

## Source Of Truth

Use package files in this order:

1. `asset_manifest.yaml` is the machine-readable source request: asset IDs,
   roles, prompts/sources, accuracy mode, variants, nullable paths, and
   fallback behavior.
2. `spec.md` explains reviewer-facing `## Asset Brief` and
   `## Asset Usage Timeline` rationale.
3. `prod.md` references stable `asset_id` values, display locations, and
   fallback behavior. It should not contain raw image-generation prompts.

Do not rewrite activity mechanics or runtime prose to fit generated images.
Assets support the accepted activity design.

## Illustrative Asset Workflow

1. Read each illustrative asset entry in `asset_manifest.yaml`.
2. Combine the asset-specific `prompt_en` subject with the repo-local style
   prompt and reference image in `docs/asset_style_reference/`.
3. Use the Codex built-in imagegen tool to create one 512x512 square source
   image per asset for subset and full-pass attempts. Do not substitute SVG,
   PIL/vector drawings, placeholder art, contact sheets, multi-card sheets, or
   combined runtime assets for imagegen output. Prompts should combine the
   asset-specific subject, scene/object/item role, use beat, and the full style
   contract below so the output aligns with the dialogue and screen state.
   Quality improvements should come from beat-specific prompts, removal of
   app-owned UI language, no duplicated picker sprites in scene backgrounds, and
   image QA repair before acceptance.
4. Select the best output, then copy it from
   `/Users/pharrelly/.codex/generated_images/...` into:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

5. Visually inspect the PNG before running the builder:
   - illustrative source image is square and exactly 512x512; downsample larger
     generated outputs to 512x512 before build;
   - no text, letters, numbers, logos, watermarks, UI labels, borders, masks,
     vignettes, black corners, or baked device chrome;
   - the style matches the flat Nordic nursery target;
   - item/object/character assets have one centered subject with generous clean
     white padding;
   - scene/background assets are full-bleed square images and keep important
     content inside the round lens-safe center.
6. Run the deterministic builder:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_illustrative
```

Use `--mode generate_and_curate` when the same run also has reference-bound
assets.

The builder consumes the inbox PNGs, writes package-local runtime variants
under `runs/<run_id>/activity_packages/<activity_id>/assets/`, updates
package-relative paths in `asset_manifest.yaml`, and writes run audit files
under `runs/<run_id>/generated_assets/`.

For item/object picker assets, the builder writes collection item variants
under package-local `assets/items/`, not beside beat-scene/background PNGs.

For subset/full-pass runs, write or update:

```text
runs/<run_id>/manual_audits/<activity_id>_prompt_trace.md
```

The trace must compare package step instructions with recorded downstream LLM
prompt material, and package image descriptions with the exact final imagegen
prompt recorded by the image agent. If the exact provider payload is not
available, say so and cite the closest recorded artifact. Keep request payloads
sanitized and do not include secrets.

## Reference-Bound Asset Workflow

Reference-bound assets include constellations, artworks, maps, scientific
diagrams, cultural artifacts, species, historical objects, named places, and
famous structures. Do not use random generated approximations for these.

1. Use `asset_manifest.yaml` `reference_policy` and `sources` to identify the
   required source type and transformation policy.
2. Accept only approved internal references, licensed assets, public-domain
   references, official sources, or verified educational/scientific sources.
3. Store the accepted original under the package:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/sources/<asset_id>__source_original.<ext>
```

4. Store reviewer-approved metadata beside it:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/sources/<asset_id>__source_metadata.yaml
```

Required metadata includes `source_type`, verified `license`,
`storage_allowed: true`, `verification_status: accepted`, matching `sha256`,
`verified_at`, and `reviewer_agent`.

5. If `transformation_policy` requires a curated redraw, place the reviewed
   redraw in:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>__curated.png
```

6. Run:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode curate_reference
```

Use `--mode generate_and_curate` when illustrative assets are also present.

## Current Style Contract

Use case: `illustration-story`.

Visual target:

- flat Nordic children's illustration matching the quiet white WonderLens
  prototype;
- asymmetric simple silhouettes, large blocky body shapes, muted salmon and
  dusty blue characters, pale cheeks, arc eyes, sparse decorative strokes,
  thin colored-pencil linework, light paper grain inside subjects, airy nursery
  composition, and generous negative space;
- broad flat color fills with linework only for arc eyes, tiny facial marks,
  and sparse short texture dashes.

Palette:

- clean white or barely tinted white background;
- restrained boho pastels inside subjects: oatmeal beige, muted sage, dusty
  teal-blue, soft terracotta/salmon, warm brown, mustard/ochre, blush pink,
  pale leaf green, and muted sky accents;
- brighter yellow, coral, cyan, or lavender only as tiny accents.

Avoid:

- generic chibi/toy vocabulary, glossy eyes, dimensional modeling, bevels, hard
  shadows, deep perspective, heavy texture, cartoon clutter, thick outlines,
  raised seams, clothing construction lines, internal contour bands, dominant
  mint, dominant blue, dominant purple, black-heavy screens, neon pink, or neon
  cyan.

Composition:

- generate or downsample illustrative source art to square 512x512 PNGs for
  subset and full-pass attempts;
- background scenes are full-bleed square images that can be clipped by the
  device's circular lens;
- item, object, and character assets are separate reusable PNGs with one
  centered subject per file, generous clean white padding, and no baked UI
  frame unless the frame itself is the intended object.
- activities that need a picker or item/object selection must keep selectable
  item/object PNGs separate from beat-scene/background PNGs. Declare each
  picker item as its own asset ID and store built runtime item/object variants
  under package-local `assets/items/` when the package is built; fullstack
  direct exports use `frontend/public/activity-assets/<activity_id>/items/`.

Hard constraints:

- no circular or oval image mask;
- no baked-in lens border, rim, vignette, black corners, transparent margin,
  colored border, readable text, letters, numbers, logos, watermark, UI labels,
  or combined multi-image source asset.
- no baked app progress or control UI: progress dots, round tokens, response
  slots, rule strips, buttons, chips, picker slots, badges, and similar runtime
  markers belong to the app, not the PNG.

Final runtime outputs should include separate 512x512 PNG files for each beat,
item, object, character, icon, badge, or distractor asset unless
`asset_manifest.yaml` explicitly requests another size. A single composite card
set is not an acceptable substitute for separate runtime assets.

For larger/full production passes, the accepted package-local assets must match
the fullstack-demo bundle shape before downstream validation. Every package
needs separate 512x512 variants for `activity_icon`, `intro_scene`,
`rules_scene`, `round_1_scene`, `round_2_scene`, `round_3_scene`,
`celebrate_scene`, and `closing_scene`. Cat5 or other synthesis flows also need
`synthesis_scene`. These beat-scene assets are required in
addition to any object, item, target, distractor, entity, or badge assets used
inside the rounds.

Full-pass scene bundles must not use one generic template across unrelated
activities. Each activity needs a distinct visual motif grounded in the source
promise and runtime mechanic. For example, little poem scenes should use a poem
page and small image tokens, time-sense scenes should use elapsed-time
prediction imagery, and current-topic interview scenes should use interview
visuals. A repeated cozy-room/blank-board/child-response layout is a hard image
QA repair finding.

Every scene asset must answer a plain visual question: what is happening in
this activity beat, and why does this image help the child do that action now?
Generic containers, blank cards, blank boards, empty rooms, glows, sparkles,
camera placeholders, or decorative props are not acceptable scene subjects
unless the beat itself is explicitly about that object. Do not start image
prompts from a loose metaphor such as treasure, basket, magic glow, clue card,
or cozy room. Start from the child action, learning evidence, and runtime screen
state, then add only props that are needed for that beat.

For sound, phoneme, rhyme, or word-hunt activities, generated scene assets must
make the listening/speaking/search action visually legible without baking in
letters, words, or target answers. Acceptable subjects include a child listening,
mouth/sound-wave cue, indoor search path, voice-wave trail, photo evidence area
kept outside the PNG, or abstract sound tokens. Baskets, treasure chests, blank
letter cards, and empty collection containers are not valid default subjects;
they may appear only when the runtime beat genuinely uses that object and the
image still communicates the sound task.

For guided drawing or other step-by-step build activities, the beat images must
show the actual instruction sequence. Round scenes should show the first shape,
the added detail, and the finished simple form. Generic paper/pencil props,
locks, timers, cameras, or placeholder cards are not acceptable substitutes
when the source promise is to guide what the child draws next.

## Independent Image QA

After the builder writes package-local PNG variants, run an independent image
quality validator before consumer dialogue QA. The validator reads
`asset_manifest.yaml`, `prod.md` runtime beats, accepted reference metadata,
and the generated PNGs. It records concrete asset paths, verdicts, and repair
requests in `generated_assets/qa_notes.yaml` or `review_notes.md`.

The validator checks:

- style consistency with the current flat Nordic WonderLens target;
- one asset per file, with scene/object/item/character role matching the
  manifest;
- scene and object content aligns with the dialogue beat and screen state;
- scene semantic coherence: the image must show the beat's child action,
  learning evidence, or source-specific screen state, not a generic metaphor,
  empty container, blank card, blank board, glow, sparkle field, or empty room;
- prompt root cause: if an accepted image contains a nonsensical repeated prop,
  QA must inspect the recorded imagegen prompt and fail the prompt when it asked
  for that prop without a beat-specific reason;
- for activities that advance by choosing an item/object, scene backgrounds do
  not duplicate the same selectable items or objects in a way that competes
  with picker sprites, target/distractor cards, or collection items;
- for activities that show a picker or selectable collection catalog, the
  package must provide a consumer-parity catalog: four correct items and eight
  distractors unless the run goal records a product-approved smaller catalog;
- progressive evidence and partial-reveal images preserve reveal timing: early
  beats must not show the final answer, full target, or solution before the
  source-aligned dialogue reveal step;
- duplicate picker objects in scene backgrounds and premature answer reveal are
  hard repair findings, not optional polish notes;
- object readability at runtime size;
- important content stays inside the round lens-safe center when relevant;
- no readable text, letters, numbers, logos, watermark, UI labels, contact
  sheets, masks, borders, or baked device chrome;
- no baked app progress/control UI such as progress dots, round markers,
  response slots, rule strips, buttons, chips, picker slots, or badges;
- cross-activity distinctness, so unrelated packages cannot pass with the same
  layout, props, and screen-template composition;
- guided drawing/build-step fidelity when applicable: each round scene shows the
  specific child action for that step;
- reference-bound assets use accepted provenance and do not invent factual
  material;
- no image changes the activity mechanic, source play frame, or child action.

If QA fails, the image quality improver repairs only image-owned artifacts:
prompt specificity, regenerated illustrative PNGs, accepted reference source,
curated redraw, crop/resize, or built variants. It must not rewrite package
prose or source-intent evidence. Re-run the builder, asset output validator,
and image QA after repairs. Re-run dialogue QA when changed visuals affect
screen/dialogue claims.

Repair requests must be concrete enough to drive imagegen without repeating the
failed prompt. Record `asset_id`, `failure_type`, `visual_problem`,
`prompt_root_cause`, `remove`, `replace_with`, `exact_regeneration_prompt`, and
`post_check`. For a nonsensical prop failure, the replacement prompt must name
the real child action and explicitly ban the failed placeholder subject.

## Validation

After any asset build, run:

```bash
python3 scripts/repair_full_pass_asset_bundle.py runs/<run_id>
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/validate_asset_granularity.py runs/<run_id>
python3 scripts/validate_full_pass_asset_bundle.py runs/<run_id>
```

These validations check package-local runtime PNG paths, fail illustrative
generated assets whose inbox source PNG is not the accepted 512x512 square
source size, and reject
composite card/set/board/library assets that should be split into separate
runtime visual units. Full-pass runs also fail when the standard beat-scene
bundle is missing or has no package-local PNG paths.

For each package with demo extensions, also run:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages/<activity_id>
```

Then regenerate and validate the review dashboard:

```bash
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

If an input image or verified source is missing, leave the variant path null and
record the failure in `generated_assets/asset_outputs.yaml` or
`generated_assets/qa_notes.yaml`. Do not fabricate paths or mark unavailable
assets as displayed.

## Fullstack Demo Direct-Asset Workflow

When working directly in the fullstack demo repo rather than autodesign run
packages, follow the same style contract, generate one separate PNG per beat or
item, copy selected Codex imagegen outputs into:

```text
frontend/public/activity-assets/<activity_id>/
frontend/public/activity-assets/<activity_id>/items/
```

Then run the fullstack repo's asset screen builder:

```bash
python3 scripts/build_activity_screen_assets.py
```

Autodesign package runs should still use the package-local
`generated_assets/inbox/` plus `scripts/build_activity_assets.py` flow above.
