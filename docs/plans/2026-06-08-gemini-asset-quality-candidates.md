# Gemini Asset Quality Candidates Plan

Date: 2026-06-08

Status: Planned

## Goal

Upgrade the merged Gemini illustrative asset provider from an API-plumbing path
into a reviewable production-quality candidate workflow. The next branch should
let collaborators generate multiple Gemini candidates per illustrative asset,
use the repo-local flat Nordic style reference image in provider calls, curate
one accepted candidate into the builder inbox, and leave enough sanitized
evidence for image QA and review-status handoff.

This is the quality layer after:

```text
docs/plans/2026-06-08-team-readiness-and-gemini-assets.md
goals/2026-06-08-team-readiness-and-gemini-assets-goal.md
```

## Current Evidence

The readiness branch merged as PR #40 and added:

- `scripts/generate_activity_asset_sources.py`;
- `tests/test_generate_activity_asset_sources.py`;
- `docs/image_generation_provider_setup.md`;
- `docs/team_onboarding.md`;
- `runs/_templates/review_status.yaml`;
- `requirements-imagegen.txt`.

The live smoke proved the Gemini API can generate one source PNG, place it in
`generated_assets/inbox/<activity_id>/<asset_id>.png`, run
`scripts/build_activity_assets.py`, and pass
`scripts/validate_asset_build_outputs.py`.

The smoke did not prove production visual quality. A later manual trial using a
real `concept_phoneme_hunt_collect` `round_1_scene` prompt showed:

- one-shot output quality is variable;
- initial candidates can bake a circular crop or mask into the PNG;
- real prompts need stronger role-specific repair rules;
- passing the style reference image to Gemini improved style alignment;
- a repaired full-bleed candidate was materially closer to production quality,
  but still needs human/agent visual QA before acceptance.

## Problem Statement

The current provider has the right artifact boundary but too little quality
control:

- it generates one PNG per asset directly into the builder inbox;
- it does not produce a reviewable candidate set;
- it does not require a curator decision before acceptance;
- it does not pass `docs/asset_style_reference/style-reference-flat-nordic.png`
  as an image reference;
- it does not record enough prompt/candidate evidence for image QA to explain
  why an image passed or failed;
- bad Gemini outputs can still satisfy file-size and path validators.

The deterministic builder is intentionally not an image-quality validator. The
quality gate must happen before accepted source PNGs enter the inbox.

## Settled Decisions

- Keep `asset_manifest.yaml` as the source request for asset IDs, roles,
  prompts, accuracy mode, and variants.
- Keep `scripts/build_activity_assets.py` as the only component that writes
  package-local runtime variants and updates manifest variant paths.
- Add a candidate layer before the existing builder inbox.
- Gemini candidate generation should write reviewable candidates under
  run-local `generated_assets/candidates/`, not directly into package-local
  `assets/`.
- Accepted candidates should be copied into
  `generated_assets/inbox/<activity_id>/<asset_id>.png` only after a curator
  decision.
- Gemini calls should use both the text style contract and the flat Nordic
  reference image when available.
- Generated prompt material and provider audits must be sanitized and must not
  include secrets or machine-local absolute paths.
- Reference-bound factual assets remain outside this workflow unless a later
  branch implements curated redraw from accepted source originals and metadata.
- The workflow should remain usable by non-Codex collaborators through CLI
  commands and review-status files.

## Proposed Contract

The exact CLI can be adjusted during implementation, but it should support these
operations:

```bash
# Generate review candidates for one illustrative asset.
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --run runs/<run_id> \
  --activity <activity_id> \
  --asset <asset_id> \
  --candidates 3 \
  --review-only

# Accept one candidate into the builder inbox.
python3 scripts/generate_activity_asset_sources.py \
  --run runs/<run_id> \
  --activity <activity_id> \
  --asset <asset_id> \
  --accept-candidate <candidate-id-or-path>
```

Candidate outputs should be run-local and reviewable, for example:

```text
runs/<run_id>/generated_assets/candidates/<activity_id>/<asset_id>/<candidate_set_id>/
├── candidate_01.png
├── candidate_02.png
├── candidate_03.png
├── prompt.txt
└── candidates.yaml
```

Accepted source output remains the existing builder contract:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

Provider audit output remains sanitized under:

```text
runs/<run_id>/generated_assets/provider_runs/
```

## Prompt And Style Requirements

The prompt compiler should combine:

- `asset_manifest.yaml` `prompt_en`;
- `asset.id`, `asset.role`, `asset.label`, `accuracy_mode`, and
  `source_strategy`;
- top-level palette and round-screen target details;
- `docs/activity_asset_generation_workflow.md` current style contract;
- `docs/asset_style_reference/wonderlens-activity-style.md`;
- the image reference
  `docs/asset_style_reference/style-reference-flat-nordic.png`.

The generated prompt should add hard quality constraints that address observed
Gemini failure modes:

- full-bleed square canvas, no circular crop, lens, border, frame, vignette,
  mask, badge, or white margin;
- no text, letters, numbers, logos, watermarks, contact sheets, or UI chrome;
- no progress dots, buttons, picker slots, camera slots, cards, badges, or
  other app-owned controls;
- important content inside the central round-screen safe area;
- scene assets must show the child action and runtime beat, not a generic cozy
  room, empty container, blank card, magic glow, or decorative metaphor;
- item/object/character assets must be one centered reusable subject with clean
  padding;
- picker/selectable target objects should not be duplicated inside background
  scenes unless the package explicitly needs that visual.

Implementation may add role-specific prompt helpers where they remove real
ambiguity. Avoid rewriting activity mechanics or package prose to make image
generation easier.

## Curation And Acceptance

The workflow should make candidate acceptance explicit:

- candidate generation records the exact candidate set, prompt source, provider,
  model, dimensions, hashes, and output paths;
- candidate acceptance records selected candidate ID/path, reviewer or agent
  name when available, acceptance timestamp, and short acceptance notes;
- rejected candidates can record concise failure reasons such as
  `circular_mask`, `baked_ui`, `target_spoiler`, `wrong_style`,
  `generic_scene`, `text_artifact`, or `unsafe_reference`;
- only accepted candidates are copied into the existing inbox path;
- acceptance should be idempotent and should not overwrite an existing inbox PNG
  unless an explicit `--force` or replacement flow is used.

The first implementation does not need a browser dashboard. YAML/Markdown
evidence is enough if a fresh reviewer can inspect the candidates and decision.

## Test Scenarios

Focused tests should cover:

- `--candidates N` writes separate candidate PNGs and metadata without touching
  the builder inbox in review-only mode;
- candidate output paths reject unsafe activity IDs, asset IDs, provider IDs,
  and candidate IDs;
- acceptance copies one candidate to the existing inbox path and records
  sanitized evidence;
- acceptance rejects paths outside the run candidate root;
- existing inbox PNGs are not overwritten without explicit force;
- provider audit and candidate metadata redact API-key-like strings,
  credential paths, `/Users/...`, `file://`, and private-key-looking material;
- missing style reference image fails with setup guidance or has a documented
  fallback;
- non-illustrative/reference-bound assets stay skipped or gated;
- CLI `--help` works without provider credentials.

The existing tests should continue to pass:

```bash
python3 -m unittest tests.test_generate_activity_asset_sources
python3 -m unittest tests.test_generate_and_curate_asset_pipeline
```

## Live Smoke Requirements

After static checks pass, run a small non-production Gemini smoke using the
same credential pattern as the merged readiness workflow. The smoke should:

1. create or reuse a non-production run fixture with one real illustrative
   activity asset, preferably a full-pass scene asset such as
   `concept_phoneme_hunt_collect/round_1_scene`;
2. generate at least two Gemini candidates using the style reference image;
3. visually inspect or record a human/agent QA note for candidate acceptance;
4. accept one candidate into `generated_assets/inbox/`;
5. run the deterministic builder;
6. run `scripts/validate_asset_build_outputs.py`;
7. scan generated audit/output files for secrets and unsafe local paths.

The smoke should not commit generated production assets unless the executor
creates a deliberately tiny test fixture. Real trial outputs should remain in
ignored `tmp/` or another documented non-production location.

## File Ownership

Likely implementation files:

```text
scripts/generate_activity_asset_sources.py
tests/test_generate_activity_asset_sources.py
docs/image_generation_provider_setup.md
docs/activity_asset_generation_workflow.md
docs/team_onboarding.md
runs/_templates/review_status.yaml
README.md
HANDOFF.md
```

Only touch `scripts/build_activity_assets.py` if the existing work-item text or
audit handoff needs to refer to the candidate workflow. Do not change package
contract schemas unless a real schema-enforced field is needed.

## Non-Goals

- Do not run the full workbook or all 40 activities.
- Do not claim fully automated image-quality judgment.
- Do not modify WonderLens AI or fullstack-demo code.
- Do not generate random replacements for reference-bound factual assets.
- Do not make the builder responsible for visual quality or provider calls.
- Do not commit `.env`, service-account JSON files, candidate request payloads
  containing secrets, or machine-local generated images from exploratory smoke
  runs.

## Risks And Mitigations

| Risk | Mitigation |
|---|---|
| Gemini still produces poor images | Generate multiple candidates, require explicit acceptance, and record rejection reasons for repair. |
| Candidates accidentally become runtime assets | Keep candidates under `generated_assets/candidates/`; only accepted candidates enter `generated_assets/inbox/`. |
| Style reference image path is unavailable for collaborators | Document setup and fail with a clear message; do not silently fall back to weak one-shot prompts. |
| Secrets leak through prompt traces or provider exceptions | Reuse and extend sanitizer tests; scan smoke outputs before completion. |
| Candidate workflow creates merge churn | Keep candidate outputs run-local and avoid committing live generated images by default. |
| CLI becomes too complex | Keep generation and acceptance commands explicit, with `--help` examples and docs. |

## Completion Definition

The feature is complete when a collaborator can generate multiple Gemini
candidates for one real illustrative asset, inspect reviewable candidate
metadata, accept one candidate into the builder inbox, build package-local
runtime variants, pass asset output validation, and update review-status
evidence without needing Codex built-in `imagegen` or committing secrets.
