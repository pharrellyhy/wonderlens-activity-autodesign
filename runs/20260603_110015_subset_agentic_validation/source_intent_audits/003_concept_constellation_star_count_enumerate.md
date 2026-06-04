# Source Intent Audit - concept_constellation_star_count_enumerate

Status: PASS after package authoring and local package review.

## Source Evidence

- TSV baseline: `inputs/original_activity_concepts_2026-05-29.tsv`, source row 20.
- Normalized helper: `inputs/source_activity_concepts.md#source_constellation_star_count`.
- Asset helper: `inputs/source_activity_concepts.md#constellation_count_cards_01`.

## Locked Source Promise

- Original play frame: Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.
- Child role: the child performs the source activity action, not a generic quiz substitute.
- Device role/action: the device prompts, displays approved package assets when declared, tracks app-owned state separately, and does not bake controls into PNGs.
- Required child actions: Choose A Star Number, Reveal The Matching Real Card, Hear One Background Fact.
- Non-negotiable elements: Number choice comes before the reveal; the displayed card is approved and reference-bound; the AI gives one fact instead of asking the child to count a generic image.

## Package Evidence

- `spec.md` records source baseline, V1 adaptation, asset brief, and support gating.
- `prod.md` includes `Runtime AI instruction` lines for every live beat with source guardrails.
- `demo_support.yaml` records supported/degraded behavior without content improvement.
- `asset_manifest.yaml` uses separate 512x512 runtime assets and package-local references.

## Verdict

PASS. The package preserves source intent. Any V1 limitation is explicit in package metadata and does not rewrite the source promise.
