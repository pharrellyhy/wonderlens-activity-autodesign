# Full Pass Agentic Pipeline Implementation Plan

Date: 2026-06-01

Status: Completed

## Goal

Implement the full-pass activity generation workflow as a master-orchestrated,
delegated-agent pipeline in autodesign. The pipeline must let autodesign
generate activity packages and all required image assets, then let
fullstack-demo and WonderLens AI load and execute those packages directly
without content improvement or manual repair.

This plan is for hardening the generation workflow and validation contract. It
does not execute a larger/full activity generation pass by itself. A future
full pass should run only after these orchestration, validation, and repair
rules are encoded in the repo workflow documents and checks.

## Current Evidence

The current source-intent pilot workflow already proved several pieces are
available:

- autodesign can produce migrated activity packages with `spec.md`, `prod.md`,
  `tag_block.yaml`, recap/dashboard templates, demo support metadata, and
  `asset_manifest.yaml`;
- `asset_build=generate_and_curate` can produce package-local runtime PNGs and
  validation reports;
- fullstack-demo can import autodesign packages and convert runtime beats into
  `step_instructions`;
- WonderLens AI can generate/load runtime artifacts from autodesign packages,
  but its runtime dialogue quality still needs the same live or simulated
  behavior review as fullstack-demo before full-pass acceptance;
- live fullstack testing can expose runtime issues that static package checks
  miss.

A recent manual audit of the fullstack `feat/activity-text-game` branch found:

- asset prompts in fullstack-demo and autodesign share the same flat Nordic
  WonderLens style target, but fullstack prompts are stricter because they
  repeat the full reference-style contract, scene/sprite distinctions, and
  per-file output rules;
- autodesign pilot assets are visually compatible, but fullstack assets are a
  stronger production reference because they cover beat scenes, icons, item
  sprites, distractors, and full 12-activity screen use;
- Phoneme Treasure Hunt preserved the B-word intent during live API play;
- Career Decision Role Play preserved the child-in-profession role and bounded
  expert decisions during live API play;
- Guided Drawing had good static `step_instructions`, but live API output still
  made unsupported visual-inspection claims such as saying the child's drawing
  "looks" perfect;
- the current fullstack Constellation Star Count package still uses direct
  visible-star counting, not the original repaired workbook intent where the
  child chooses a number, the device reveals a real matching constellation, and
  the AI gives background information;
- fullstack static source-fidelity tests passed while those two runtime/intent
  issues remained, so static checks are necessary but insufficient.

Those findings imply the full pass needs independent source-intent review,
consumer/import validation, live dialogue testing, image QA, and explicit repair
loops before accepting generated packages.

## Architecture Boundary

Autodesign owns the activity truth:

- source row and source snapshot;
- adaptation brief;
- package files;
- runtime AI instructions;
- asset manifest;
- generated or curated PNG assets;
- source-intent, runtime, image, and downstream validation reports.

Fullstack-demo owns execution fidelity:

- loading the package as provided;
- converting package runtime beats into `step_instructions`;
- serving declared assets;
- enforcing generic runtime safety/product constraints;
- running live API sessions against the loaded package.

WonderLens AI owns runtime-generation and WonderLens-side execution fidelity:

- generating/loading runtime artifacts from the package as provided;
- preserving package runtime AI instructions in WonderLens-side runtime steps;
- exercising WonderLens AI dialogue behavior against the same source-intent and
  unsupported-claim constraints;
- reporting package-owned versus runtime-owned failures.

Fullstack-demo and WonderLens AI must not improve, rewrite, or reinterpret
activity content to make a package look better. If either consumer runtime
violates a package constraint, record whether the cause is package quality,
generic runtime guardrails, importer/loader behavior, or product capability.
Repair package problems in autodesign. Repair generic consumer-runtime problems
in separate downstream goals unless the user explicitly asks to include that
work.

## Master Orchestrator

The main agent remains responsible for orchestration and final decisions. It
does not delegate secrets, final acceptance, server lifecycle, commits, or user
reporting.

Responsibilities:

- establish the run branch/worktree and record repo state;
- select source rows and capture stable source snapshots;
- assign disjoint delegated-agent tasks;
- enforce blocking gates and repair ordering;
- decide whether a finding is package-owned, runtime-owned, or product-owned;
- keep unsupported/degraded mechanics honest;
- run final checks;
- commit intended autodesign changes;
- report residual risk.

## Delegated Agent Roles

The full pass should use at least the six delegated roles requested by the
user, plus source/consumer gates and WonderLens AI dialogue roles that prevent
known drift classes.

| Role | Ownership | Inputs | Required output |
|---|---|---|---|
| Source-intent auditor | Text/package review only | original workbook row, normalized helper, adaptation brief, generated package | Verdict per activity: `aligned`, `minor_adaptation`, `intent_drift`, or `needs_product_decision`, with file/section evidence. |
| Activity package writer | Text only | source snapshot, adaptation brief, current generation contract | Package files and runtime AI instructions; no image generation. |
| Scene/object/item asset generator | Image only | `asset_manifest.yaml`, style contract, approved reference sources | Separate PNG source assets and package-local runtime variants; no package prose rewrites. |
| Consumer/import contract validator | Loader/conversion only | generated packages, fullstack importer, current fullstack target branch | Import result, asset path result, converted `step_instructions` quality notes, no-content-mutation evidence. |
| Dialogue quality validator | Live API/runtime only | imported fullstack packages, user-input strategy matrix | Sanitized transcripts and verdicts for source intent, unsupported claims, no-response handling, wrong-answer handling, and step richness. |
| WonderLens AI dialogue quality validator | WonderLens AI runtime only | generated WonderLens AI runtime artifacts, user-input strategy matrix | Sanitized WonderLens AI dialogue/runtime report with verdicts for source intent, unsupported claims, branch recovery, and step richness. |
| Image quality validator | Visual QA only | generated PNGs, style reference, activity package and dialogue beats | Style consistency, object readability, crop safety, scene/dialogue alignment, reference fidelity, and no-text/no-label verdicts. |
| Dialogue quality improver | Text repair only | failed dialogue validator reports | Package/runtime-instruction repairs or fullstack-runtime issue recommendations; no image edits. |
| WonderLens AI dialogue quality improver | WonderLens AI runtime repair triage only | failed WonderLens AI dialogue validator reports | Package/runtime-instruction repairs or WonderLens AI follow-up recommendations; no image edits and no downstream code edits unless explicitly scoped. |
| Image quality improver | Image repair only | failed image QA reports | Regenerated/curated/rebuilt assets and updated asset reports; no activity-flow rewrites. |
| Final independent reviewer | Cross-artifact review | final packages, validation reports, transcripts, asset sheets | Final pass/fail report with unresolved risks. |

Delegated agents must write concise evidence. They should not edit shared files
unless explicitly assigned a disjoint ownership area. They must not print,
copy, edit, or commit secrets.

## Source-Intent Gate

Source intent must be checked before and after package writing.

The auditor compares:

- original workbook row;
- normalized helper;
- adaptation brief;
- `spec.md`;
- `prod.md`;
- `tag_block.yaml`;
- `demo_support.yaml`;
- `asset_manifest.yaml`;
- downstream converted files when available;
- live runtime transcript when available.

Checklist fields:

- original play frame;
- child role;
- device role/action;
- interaction sequence;
- required child actions;
- reference or real-asset requirement;
- background/context promise;
- allowed V1 adaptation;
- unsupported/degraded capability reason;
- generated-package evidence;
- downstream evidence;
- repair status.

`intent_drift` blocks activity acceptance, final report completion, and any
larger pass scale-up until repaired or recorded as a product decision.

## Package Writing Contract

The activity package writer works text-only. It should not generate or select
images. It must write packages against the source snapshot and adaptation brief,
then declare image needs in `asset_manifest.yaml`.

Runtime AI instructions must be strong enough to convert directly into
fullstack `step_instructions`. Each runtime beat should include:

- beat goal/action;
- response-length or tier constraint;
- emotion/tone;
- role/story frame;
- exact child action;
- accepted progress evidence;
- expected, unexpected, and no-response behavior;
- source-intent guardrails;
- product/safety constraints;
- screen/state expectation;
- example AI line;
- must-not-skip details when background information, reference assets, or
  child action sequence are part of the source promise.

Use the current fullstack
`backend/games/fluffy_expedition_dandelion.md` as the practical quality floor
for converted `step_instructions`.

## Asset Generation Contract

The full pass should use:

```text
asset_build=generate_and_curate
```

The asset generator reads only the package `asset_manifest.yaml`, the current
WonderLens activity style contract, and approved source/reference material. It
must not reinterpret the activity.

Illustrative assets:

- one image per declared asset;
- separate scene, character, object, item, icon, badge, and distractor files;
- flat Nordic WonderLens style matching the current fullstack reference;
- clean white item/object/character sprites when applicable;
- full-bleed beat/background scenes when applicable;
- no text, letters, numbers, logos, watermarks, contact sheets, borders,
  circular masks, device chrome, or labels.

Reference-bound assets:

- do not use image generation to invent factual diagrams, constellations, maps,
  artworks, species, named places, or cultural/historical objects;
- use accepted internal references, licensed sources, official sources, or
  deterministic verified redraws;
- store accepted originals and metadata under package-local `assets/sources/`;
- build runtime variants by approved transformation only.

Assets support the activity package. If the asset and package disagree, fix the
asset or manifest; do not rewrite the activity to fit the generated image.

## Fullstack Consumer Contract

Fullstack-demo must be treated as the direct consumer, not a second authoring
environment.

Required validation:

- import the generated package without content improvement;
- verify all declared assets resolve from package/fullstack public paths;
- verify converted `step_instructions` preserve runtime AI instruction quality;
- verify unsupported/degraded packages remain honest;
- verify no package content was rewritten to fit fullstack constraints unless
  the importer has an explicit, audited conversion rule;
- compare high-risk converted activities against the original source intent,
  not only against normalized helper wording.

Fullstack generic guardrails that may need a downstream follow-up:

- do not claim visual inspection unless a real image/photo was provided;
- do not claim screen content that is not in the current frame/assets;
- do not turn a source mechanic into a nearby playable mechanic;
- do not add or remove background/context promises;
- do not make unsupported mechanics playable by changing the child action.

## WonderLens AI Consumer Contract

WonderLens AI must be treated as a second direct runtime consumer, not only a
schema/load check.

Required validation:

- generate WonderLens AI runtime artifacts from the autodesign packages without
  content improvement;
- verify runtime steps preserve the package's runtime AI instruction quality;
- exercise WonderLens AI dialogue behavior for representative activities with
  the same input strategy matrix used for fullstack where the runtime supports
  it;
- verify unsupported/degraded packages remain honest and do not become playable
  through runtime adaptation;
- verify WonderLens AI does not add unsupported sensing, hidden-state claims,
  false screen claims, or mechanic changes;
- record whether failures are package-owned, WonderLens-runtime-owned, or
  product-capability decisions.

WonderLens AI dialogue failures should feed the same repair decision tree as
fullstack failures: fix package-owned instruction gaps in autodesign, and record
WonderLens-runtime-owned guardrail issues as downstream follow-up unless the
user explicitly expands scope.

## Live Dialogue QA

Static tests are not enough. The dialogue validator must start the target
fullstack backend/frontend and WonderLens AI runtime harnesses as needed,
source authorized provider credentials without printing them, and run live or
runtime-equivalent sessions against imported/generated packages.

Use multiple child-input strategies per activity:

- ideal answer;
- minimal answer;
- wrong answer;
- off-topic answer;
- confusion/help request;
- premature done;
- silence/no response;
- unsupported request.

The sanitized transcript report should check:

- source intent preserved across all runtime beats;
- child role and device role are stable;
- no unsupported sensing or hidden-state claims;
- no false screen/asset claims;
- no generic drift in synthesis/celebration/closing;
- no excessive verbosity for tier;
- branches recover back to the intended activity;
- final recap names the correct concept and child action.

Live runs should use a temp database path when possible so tracked demo state is
not dirtied.

## Image QA

The image quality validator checks visual quality independently from the asset
generator.

Checks:

- matches current WonderLens activity style;
- one asset per file;
- scene/object/item role matches manifest role;
- image aligns with package dialogue and screen beat;
- object is readable at runtime size;
- central crop/lens safe area is respected when relevant;
- no text, letters, numbers, logos, watermarks, labels, contact sheets, masks,
  borders, or UI chrome;
- no reference-bound invention;
- no misleading scene that changes the activity mechanic.

Findings should include concrete asset paths and a pass/fail/repair verdict.

## Repair Loops

Dialogue repair loop:

1. Start from live transcript failure or static conversion failure.
2. Decide whether the owner is autodesign package text, fullstack generic
   runtime behavior, or product support.
3. If package-owned, repair runtime AI instructions or source guardrails in the
   package/generation contract.
4. If runtime-owned, record a fullstack follow-up instead of masking the issue
   or WonderLens AI follow-up instead of masking the issue in package prose
   unless the user asks to fix the downstream runtime now.
5. Re-import and re-run the failing transcript strategy.

Image repair loop:

1. Start from image QA failure.
2. Repair prompt specificity, regenerate illustrative asset, replace accepted
   reference source, or apply deterministic crop/resize repair.
3. Rebuild package-local variants.
4. Re-run image QA and asset output validation.
5. Re-run live dialogue QA when changed visuals affect screen/dialogue claims.

## Implementation Areas

The execution goal should inspect current files before editing. Expected
autodesign ownership areas:

- `GOAL.md`;
- `run.md`;
- `program.md`;
- `docs/activity_asset_generation_workflow.md`;
- `docs/plans/`;
- `goals/`;
- validation/review templates or scripts if the current docs cannot enforce
  the required gates.

Do not edit fullstack-demo or WonderLens AI in this autodesign goal unless the
user explicitly expands scope. Consumer-runtime issues discovered during
implementation should be recorded as downstream findings or separate follow-up
goals.

## Required Checks

For doc/contract-only changes:

```bash
git diff --check
rg -n "source-intent auditor|Source-intent auditor|dialogue quality|WonderLens AI dialogue|image quality|asset_build=generate_and_curate|fullstack|WonderLens AI" GOAL.md run.md program.md docs goals
```

If scripts or schemas are changed, add focused tests and run the nearest
relevant checks. Examples:

```bash
python3 scripts/validate_demo_package_contract.py tests/fixtures/demo_package_contract/valid
python3 scripts/validate_asset_build_outputs.py <small-run-dir>
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_generate_run_review.py -q
```

If fullstack or WonderLens AI live/dialogue QA tooling is added or changed, run
it against the smallest representative imported/generated activity set before
accepting the contract.

## Success Criteria

- `GOAL.md`, `run.md`, and `program.md` clearly define the master/subagent full
  pass pipeline.
- The workflow explicitly requires source-intent auditing before and after
  package writing.
- The workflow explicitly requires package/import validation before live API
  testing.
- The workflow explicitly requires WonderLens AI runtime dialogue validation
  before full-pass acceptance, not only WonderLens AI conversion/load checks.
- The workflow requires `asset_build=generate_and_curate` for full pass asset
  generation and treats assets as package-owned outputs.
- The workflow separates package writing, image generation, live dialogue QA,
  WonderLens AI dialogue QA, image QA, dialogue repair, WonderLens AI dialogue
  repair, and image repair responsibilities.
- Delegated/subagent rules are explicit and limited to disjoint ownership.
- Fullstack-demo is documented as a loader/executor, not a content improver.
- WonderLens AI is documented as a runtime consumer whose dialogue quality must
  be validated and repaired or escalated like fullstack dialogue quality.
- Live dialogue QA includes multiple child-input strategies and checks for
  unsupported claims.
- Image QA checks style consistency, scene/dialogue alignment, reference
  fidelity, and no-text/no-label constraints.
- The completion gate requires evidence from source-intent, import, live
  dialogue, image QA, and final independent review before any future full pass
  is accepted.

## Non-Goals

- Do not execute the full activity generation pass in this goal.
- Do not regenerate all activity assets in this goal.
- Do not implement broad fullstack or WonderLens AI runtime repairs in this
  autodesign goal.
- Do not relax source fidelity to make activities easier to run.
- Do not replace live dialogue QA with static term checks.
