# Source Intent Audit - concept_recognition_pop_probe

Status: PASS after package authoring and local package review.

## Source Evidence

- TSV baseline: `inputs/original_activity_concepts_2026-05-29.tsv`, source row 31.
- Normalized helper: `inputs/source_activity_concepts.md#source_whack_a_mole_recognition`.
- Asset helper: `inputs/source_activity_concepts.md#recognition_challenge_cards_01`.

## Locked Source Promise

- Original play frame: After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.
- Child role: the child performs the source activity action, not a generic quiz substitute.
- Device role/action: the device prompts, displays approved package assets when declared, tracks app-owned state separately, and does not bake controls into PNGs.
- Required child actions: Learn The Target Rule, Compare One Distractor, Pop The Target Again.
- Non-negotiable elements: The child compares changing pictures against a target rule; target and distractor sprites are separate from scene backgrounds.

## Package Evidence

- `spec.md` records source baseline, V1 adaptation, asset brief, and support gating.
- `prod.md` includes `Runtime AI instruction` lines for every live beat with source guardrails.
- `demo_support.yaml` records supported/degraded behavior without content improvement.
- `asset_manifest.yaml` uses separate 512x512 runtime assets and package-local references.

## Verdict

PASS. The package preserves source intent. Any V1 limitation is explicit in package metadata and does not rewrite the source promise.
