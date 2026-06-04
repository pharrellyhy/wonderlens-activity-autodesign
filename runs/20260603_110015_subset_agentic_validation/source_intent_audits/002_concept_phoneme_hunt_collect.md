# Source Intent Audit - concept_phoneme_hunt_collect

Status: PASS after package authoring and local package review.

## Source Evidence

- TSV baseline: `inputs/original_activity_concepts_2026-05-29.tsv`, source row 2.
- Normalized helper: `inputs/source_activity_concepts.md#source_phoneme_hunt`.
- Asset helper: `inputs/source_activity_concepts.md#phoneme_letter_card_01`.

## Locked Source Promise

- Original play frame: AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.
- Child role: the child performs the source activity action, not a generic quiz substitute.
- Device role/action: the device prompts, displays approved package assets when declared, tracks app-owned state separately, and does not bake controls into PNGs.
- Required child actions: Hear The Target Sound, Capture One Treasure, Name Evidence Check.
- Non-negotiable elements: The target sound becomes the collection criterion; visual objects support but do not replace spoken or typed name evidence.

## Package Evidence

- `spec.md` records source baseline, V1 adaptation, asset brief, and support gating.
- `prod.md` includes `Runtime AI instruction` lines for every live beat with source guardrails.
- `demo_support.yaml` records supported/degraded behavior without content improvement.
- `asset_manifest.yaml` uses separate 512x512 runtime assets and package-local references.

## Verdict

PASS. The package preserves source intent. Any V1 limitation is explicit in package metadata and does not rewrite the source promise.
