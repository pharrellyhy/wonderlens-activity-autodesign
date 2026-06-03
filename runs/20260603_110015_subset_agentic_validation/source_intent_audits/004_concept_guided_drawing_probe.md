# Source Intent Audit - concept_guided_drawing_probe

Status: PASS after package authoring and local package review.

## Source Evidence

- TSV baseline: `inputs/original_activity_concepts_2026-05-29.tsv`, source row 4.
- Normalized helper: `inputs/source_activity_concepts.md#source_guided_drawing`.
- Asset helper: `inputs/source_activity_concepts.md#guided_drawing_step_cards_01`.

## Locked Source Promise

- Original play frame: AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.
- Child role: the child performs the source activity action, not a generic quiz substitute.
- Device role/action: the device prompts, displays approved package assets when declared, tracks app-owned state separately, and does not bake controls into PNGs.
- Required child actions: Draw The First Circle, Add Two Small Ears Or Petals, Finish With One Face Or Detail.
- Non-negotiable elements: The child draws on real paper while the AI gives step cards and waits for self-report; no camera verification is claimed.

## Package Evidence

- `spec.md` records source baseline, V1 adaptation, asset brief, and support gating.
- `prod.md` includes `Runtime AI instruction` lines for every live beat with source guardrails.
- `demo_support.yaml` records supported/degraded behavior without content improvement.
- `asset_manifest.yaml` uses separate 512x512 runtime assets and package-local references.

## Verdict

PASS. The package preserves source intent. Any V1 limitation is explicit in package metadata and does not rewrite the source promise.
