# Source Intent Audit - concept_scavenger_hunt_collect

Status: PASS after package authoring and local package review.

## Source Evidence

- TSV baseline: `inputs/original_activity_concepts_2026-05-29.tsv`, source row 1.
- Normalized helper: `inputs/source_activity_concepts.md#source_scavenger_hunt`.
- Asset helper: `none`.

## Locked Source Promise

- Original play frame: Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.
- Child role: the child performs the source activity action, not a generic quiz substitute.
- Device role/action: the device prompts, displays approved package assets when declared, tracks app-owned state separately, and does not bake controls into PNGs.
- Required child actions: First Matching Find, Second Matching Find, Third Matching Find.
- Non-negotiable elements: Three real-world finds become evidence for one shared rule and one child-generated extra connection.

## Package Evidence

- `spec.md` records source baseline, V1 adaptation, asset brief, and support gating.
- `prod.md` includes `Runtime AI instruction` lines for every live beat with source guardrails.
- `demo_support.yaml` records supported/degraded behavior without content improvement.
- `asset_manifest.yaml` uses separate 512x512 runtime assets and package-local references.

## Verdict

PASS. The package preserves source intent. Any V1 limitation is explicit in package metadata and does not rewrite the source promise.
