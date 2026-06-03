# Subset Agentic Validation Goal

## Mode

Goal-only.

Use this file as the Codex goal-mode execution contract for a small, high-risk
subset run after the merged subset workflow gates. This goal validates the
pipeline before resuming any larger/full pass.

## Objective

Run a one-activity subset through the current agentic generation, asset,
consumer-conversion, dialogue-QA, image-QA, and repair gates using 512x512 image
assets.

The finished run must prove that:

- source intent does not drift from the original workbook/TSV source;
- package runtime AI instructions are rich enough for downstream conversion;
- fullstack-demo and WonderLens AI load/convert the generated packages without
  content improvement;
- generated/curated image assets are 512x512, role-specific, style-consistent,
  source-aligned, and free of baked app UI;
- the run remains a scoped subset and does not resume the paused full pass.

## Scope

Process only the active `assignments.md` row:

```text
concept_phoneme_hunt_collect
```

Do not process archived rows in `docs/assignments_archive.md` or any other
unchecked rows if additional rows are added later.

## Design Decisions

- This is a subset validation run, not a full-pass generation run.
- Run from a fresh worktree/branch created from current `main`, not from the
  merged `feat/subset-agentic-workflow` branch and not from the paused
  `feat/full-pass-agentic-run` worktree.
- Set `source.asset_build: generate_and_curate`.
- Set `source.full_pass_pipeline: true` so the subset exercises the full
  source-intent, asset, consumer, dialogue, image, repair, and final-review
  gates.
- Set `source.product_contract_override: minimum_unblock_allowed` so known
  capability-probe rows generate honest packages with resolved contract notes
  rather than blocked previews.
- Keep package writing text-only until the explicit post-package asset phase.
- Generate illustrative source PNGs with Codex built-in imagegen, not SVG,
  vector, placeholder, or script-generated substitute art.
- Use the repo-local flat Nordic style prompt and reference image in
  `docs/asset_style_reference/` for every generated illustrative asset.
- Generate or downsample illustrative source PNGs to exactly 512x512 before
  build. Final runtime PNGs must also be 512x512 unless a manifest explicitly
  requests a larger additional variant.
- Preserve the current no-`recap_scene` image-bundle contract. Required
  standard scene assets are `activity_icon`, `intro_scene`, `rules_scene`,
  `round_1_scene`, `round_2_scene`, `round_3_scene`, `celebrate_scene`, and
  `closing_scene`; Cat5/synthesis flows also require `synthesis_scene`.
- For `concept_phoneme_hunt_collect`, preserve the original source intent:
  the AI introduces a target sound, then the child finds one indoor treasure
  whose spoken word starts with that sound.
- Selectable item/object PNGs must be declared
  separately and built under package-local `assets/items/`, not mixed with
  scene/background assets.

## Hard Constraints

- Do not touch, delete, clean, or resume
  `.worktrees/feat/full-pass-agentic-run`.
- Do not delete or overwrite local untracked artifacts at
  `runs/20260601_155917_full_pass_agentic_tsv/`.
- Do not run a full workbook pass.
- Do not edit or expose `.env`, credential JSON files, tokens, or provider
  secrets.
- Do not feed raw `RESOLVED BLOCKER` or `RESOLVE BLOCKER` markers into
  fullstack-demo or WonderLens AI runtime conversion.
- Do not let fullstack-demo or WonderLens AI improve, weaken, rewrite, or
  reinterpret package content to make it pass.
- Do not accept image assets with baked progress dots, round markers, buttons,
  chips, picker slots, badges, readable text, labels, contact sheets, circular
  masks, borders, or device chrome.
- Do not accept progressive-evidence or partial-reveal images that expose the
  answer before the source/dialogue reveal step.

## Execution Rules

- Create a new worktree from current `main` before running the subset, using a
  path such as `.worktrees/feat/subset-agentic-validation`.
- Use `run.md` and `program.md` as the execution contract, with this goal's
  scoped overrides taking precedence.
- Use `inputs/original_activity_concepts_2026-05-29.tsv` as the workbook source
  baseline. Treat `inputs/source_activity_concepts.md` as the normalized helper
  only when it does not weaken the TSV/source promise.
- Use delegated/sub-agents for independent roles when available: source-intent
  audit, package review, image generation, image QA, fullstack validation,
  WonderLens AI validation, dialogue repair, image repair, and final independent
  review. Use at most three delegated/sub-agents in parallel; collect evidence
  and terminate or kill each finished agent before spawning a replacement. Keep
  run orchestration, credentials, scope, and final acceptance local to the main
  agent.
- If an API/provider rate limit occurs during image generation, hosted LLM
  calls, fullstack live API, WonderLens AI live API, or runtime conversion, wait
  a few minutes and retry with backoff at least three times before classifying
  the condition as blocked.
- Use conventional commits after a coherent passing unit of work, per project
  instructions. Do not push unless explicitly asked.

## Live Provider And Consumer Rules

Fullstack-demo validation must start from:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game
```

Use credentials only from the fullstack-demo main backend directory when live
API access is required:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.env
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/.elaborate-baton-480304-r8-a8a39bcb34f1.json
```

WonderLens AI validation must use:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai
```

Do not copy secrets into generated artifacts, logs, reports, commits, PR
descriptions, or final responses.

## Success Criteria

### Autodesign Package Quality

- Exactly the one scoped row is snapshotted and processed:
  `concept_phoneme_hunt_collect`.
- Every generated package has the five required files plus
  `demo_support.yaml` and `asset_manifest.yaml`.
- `prod.md` contains machine-convertible `Runtime AI instruction` lines for
  every live beat, with goal/action, constraint, tone, progress evidence,
  branch behavior, frame/source guardrail, example line, and screen/state
  behavior.
- No generated package has unresolved source-intent drift.
- No runtime-facing `prod.md` contains raw blocker leakage markers.

### Asset Quality

- `asset_manifest.yaml` declares the standard scene bundle plus required
  item/object/entity/target/distractor/reference assets.
- Picker/selectable item/object assets are declared individually and built
  under package-local `assets/items/`.
- Package-local generated/curated PNGs are built and validated at 512x512.
- Generated illustrative source PNGs come from Codex built-in imagegen and
  match `docs/asset_style_reference/`.
- Run-local manual prompt trace exists at
  `runs/<run_id>/manual_audits/concept_phoneme_hunt_collect_prompt_trace.md`
  and lists, per runtime step, package instruction vs recorded downstream LLM
  prompt material plus image description vs exact recorded imagegen prompt or
  an explicit provider-payload logging gap.
- Image QA evidence confirms role match, style consistency, crop safety,
  scene/dialogue alignment, no baked UI, no duplicate picker objects in scene
  backgrounds, no premature answer reveal, and reference fidelity where
  applicable.
- Image QA evidence includes actual PNG review, not only manifest/prompt review.
  Scene assets fail if they do not visually explain the current beat's child
  action, sound/phoneme evidence, or source-specific screen state. Generic
  baskets, blank cards, blank boards, empty rooms, glows, and decorative
  placeholders require regeneration unless the beat itself is explicitly about
  that object.
- Story-scene assets feel like coherent real-world scenes, with plausible
  spaces, stable camera/framing, consistent subject treatment, and concrete
  beat-to-beat changes. Isolated floating symbols are acceptable for icons,
  badges, and item sprites only.
- Sound/phoneme/word-hunt assets foreground listening, speaking, sound waves,
  search motion, or runtime evidence areas; they do not default to a
  treasure/basket metaphor.
- Picker/catalog activities provide a consumer-parity item set, normally four
  correct items and eight distractors under `assets/items/`, unless the run goal
  records an approved smaller catalog.
- Constellation/reference-bound assets use approved provenance or verified
  source data; random generated approximations do not pass.

### Consumer Validation

- Fullstack-demo imports/loads the subset packages from the required worktree.
- Fullstack converted `step_instructions` are at least as rich as current
  high-quality activity instructions such as `fluffy_expedition_dandelion.md`.
- Fullstack export does not use generic placeholder collection entries such as
  `Matching placeholder`, `/icons/green_apple.png`, or `/icons/straight_stick.png`
  for `concept_phoneme_hunt_collect`; picker entries must come from package
  assets or be recorded as a downstream-owned failure.
- Fullstack live or runtime-equivalent dialogue QA exercises multiple child
  input strategies, including expected answer, wrong/unproductive answer,
  help/confusion, silence/no response, and premature done where applicable.
- WonderLens AI converts/loads the subset packages cleanly.
- WonderLens AI emits package `asset_manifest.yaml` and runtime/package asset
  references without an empty asset binding where item assets are required; if
  its runtime model intentionally keeps item candidates outside `runtime.yaml`,
  record that as explicit downstream evidence instead of silently accepting
  `asset_bindings: []`.
- WonderLens AI dialogue/runtime QA meets the same source-intent and runtime
  instruction quality bar as fullstack validation.
- Package-owned consumer failures are repaired in autodesign and revalidated;
  downstream-owned failures are recorded as downstream follow-up and do not get
  hidden by package rewrites.

## Required Checks

Run the narrowest applicable checks from `AGENTS.md`, plus these subset checks
when the run exists:

```bash
git diff --check
python scripts/repair_full_pass_asset_bundle.py runs/<run_id>
python scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python scripts/validate_asset_build_outputs.py runs/<run_id>
python scripts/validate_asset_granularity.py runs/<run_id>
python scripts/validate_full_pass_asset_bundle.py runs/<run_id>
if rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md; then exit 1; fi
test -f runs/<run_id>/manual_audits/concept_phoneme_hunt_collect_prompt_trace.md
test -f runs/<run_id>/downstream_reports/fullstack_demo/dialogue_qa_report.json
test -f runs/<run_id>/downstream_reports/wonderlens_ai/dialogue_qa_report.json
if rg -n "Matching placeholder|/icons/green_apple.png|/icons/straight_stick.png" runs/<run_id>/downstream_reports/fullstack_demo; then exit 1; fi
```

Also run or record evidence for:

- activity package/schema validation for all generated `tag_block.yaml` files;
- source-intent audit validation with workbook evidence;
- fullstack import/conversion/dialogue validation;
- WonderLens AI conversion/load/dialogue validation;
- image QA and re-QA after any image repair;
- final independent review across packages, audits, downstream reports, image
  QA, and `review.html`.

## Final Completion Gate

Do not mark the goal achieved until:

- only `concept_phoneme_hunt_collect` was processed;
- `runs/<run_id>/review.html`, `run_manifest.yaml`, and validation reports
  document the subset result;
- all success criteria above pass or residual downstream-owned risks are
  documented with evidence;
- all package-owned text, asset, source-intent, fullstack, WonderLens AI, and
  image-QA issues are repaired and revalidated;
- focused checks pass;
- no secrets are included in committed or reported artifacts;
- no full-pass generation was resumed.

Final response must include the run id, generated package paths, checks run,
consumer validation result, image QA result, repairs made, commits, and any
remaining risks.
