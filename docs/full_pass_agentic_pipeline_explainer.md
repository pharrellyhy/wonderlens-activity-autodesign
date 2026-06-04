# Full-Pass Agentic Pipeline Explainer

Audience: engineering and product teams

Status: Current workflow explanation

Presentation version:

- `docs/full_pass_agentic_pipeline_presentation.html`

## Executive Summary

The full-pass agentic pipeline is the production workflow for turning a source
activity idea into a complete WonderLens activity package with text runtime
instructions, image assets, downstream import validation, dialogue QA, repair
loops, and final review.

It exists because a package can look structurally valid while still failing the
actual product promise. Static checks can miss problems such as activity intent
drift, thin runtime instructions, unsupported visual claims, missing image
context, or downstream consumers silently falling back to generic dialogue.

The central rule is simple: autodesign owns activity quality, while fullstack-demo
and WonderLens AI are direct consumers. They must load and execute the package as
provided. They should not improve weak package content downstream.

## Why This Pipeline Exists

The source-intent pilot exposed several failure modes that ordinary generation
and static review did not reliably catch:

- Source intent drift: for example, a workbook activity about choosing a number,
  revealing a real matching constellation, and hearing background information can
  drift into a simpler "count stars in a picture" task.
- Runtime instruction drift: generated `prod.md` can contain pleasant example
  lines but not enough machine-convertible guidance for downstream
  `step_instructions`.
- Consumer mismatch: fullstack-demo and WonderLens AI can load the same package
  through different conversion/runtime paths, so both must be validated.
- Image mismatch: generated assets can be stylistically acceptable but misaligned
  with the dialogue beat, source promise, or required real/reference asset.
- Live dialogue gaps: a runtime can pass static import tests but still make an
  unsupported claim, mishandle silence/off-topic input, or weaken the original
  activity frame during live turns.

The full-pass pipeline adds independent checks and repair routing at each point
where those failures appear.

## What The Full Pass Produces

A successful full pass produces a run directory under `runs/<run_id>/` with:

- activity packages under `activity_packages/<activity_id>/`;
- five required package files: `spec.md`, `prod.md`, `tag_block.yaml`,
  `recap.template.yaml`, and `dashboard.template.yaml`;
- demo extension files when enabled: `demo_support.yaml` and
  `asset_manifest.yaml`;
- generated or curated package-local runtime PNG assets when
  `asset_build=generate_and_curate`;
- source-intent audit reports;
- package review notes;
- asset build and image QA evidence;
- fullstack-demo import/dialogue reports;
- WonderLens AI runtime/dialogue reports;
- repair-loop evidence;
- final independent-review evidence;
- `review.html` and `run_manifest.yaml` summarizing generated, blocked,
  repaired, degraded, and accepted outputs.

## Invocation

Use this mode for larger or production-scale passes, not for a small exploratory
package-only run.

Recommended command:

```text
/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.
```

Required run behavior:

- `asset_build=generate_and_curate`
- `full_pass_pipeline=true`
- package writing remains text-only
- image generation and curation run in a separate image-only phase
- fullstack-demo and WonderLens AI are validation targets, not authoring
  fallbacks
- the scoped goal owns delegated-agent rules, credential boundaries, live
  validation ordering, and final acceptance criteria

## System Boundaries

### Autodesign Owns

Autodesign is the source of truth for activity quality:

- source row and source snapshot;
- source-promise interpretation;
- adaptation brief;
- package files;
- runtime AI instructions;
- demo support metadata;
- asset manifest;
- generated or curated assets;
- source-intent audit;
- package-owned repairs.

If an activity package has thin instructions, intent drift, missing branch
behavior, unsupported asset claims, or weak image prompts, the fix belongs in
autodesign.

### Fullstack-Demo Owns

Fullstack-demo owns loader and demo execution fidelity:

- importing package files as provided;
- converting package runtime beats into `step_instructions`;
- serving declared runtime assets;
- running live or runtime-equivalent dialogue sessions;
- reporting whether failures are package-owned or fullstack-runtime-owned.

Fullstack-demo should not rewrite package content to hide weak source
instructions.

### WonderLens AI Owns

WonderLens AI owns WonderLens-side runtime generation and execution fidelity:

- generating or loading runtime artifacts from package files;
- preserving package runtime AI instructions in WonderLens-side runtime prompts;
- exercising the same source-intent and unsupported-claim constraints used for
  fullstack dialogue QA;
- reporting package-owned versus WonderLens-runtime-owned failures.

WonderLens AI should not reinterpret package content to make a weak package
appear stronger.

## Agent Roles

The full pass uses a master agent plus delegated agents with disjoint ownership.

| Role | Owns | Does Not Own |
|---|---|---|
| Master orchestrator | Run setup, ordering, blocking gates, repair routing, final acceptance, commits, user report | Secret sharing, unchecked downstream mutation |
| Source-intent auditor | Source promise, required child action, real/reference asset requirements, background/context requirements | Rewriting package prose |
| Text-only package writer | `spec.md`, `prod.md`, tag block, recap/dashboard templates, demo support metadata, asset manifest text | Binary image generation |
| Image-only asset generator | Scene/object/item PNG generation or curation from approved prompts and manifests | Runtime prose or package contract changes |
| Package/import validator | Schema, package completeness, fullstack import, asset path resolution, converted instruction shape | Content improvement |
| Fullstack dialogue validator | Live or runtime-equivalent dialogue quality in fullstack-demo | Package text edits |
| WonderLens AI dialogue validator | WonderLens-side runtime/dialogue quality | Package text edits |
| Image quality validator | Style consistency, crop safety, scene/dialogue alignment, reference fidelity | Dialogue repair |
| Dialogue improver | Package-owned runtime instruction fixes | Image repair or downstream runtime code |
| Image improver | Package-owned asset prompt/source/image fixes | Dialogue repair |
| Final independent reviewer | End-to-end evidence audit and residual-risk classification | First-pass generation |

The master agent can use more than these roles, but it must not collapse
independent validation into the same writer that produced the artifact.

## End-To-End Flow

### 1. Run Setup

The master agent creates or selects the run branch/worktree, records repo state,
captures the assignment snapshot, and confirms the run flags. For full pass, the
important flags are `asset_build=generate_and_curate` and
`full_pass_pipeline=true`.

### 2. Source Snapshot And Pre-Package Audit

Before writing a package, the source-intent auditor locks the original source
promise:

- original play frame;
- child role;
- device role;
- interaction sequence;
- required child actions;
- real/reference asset requirement;
- required background or context information;
- allowed V1 adaptations;
- product dependencies.

For workbook-derived rows, the committed workbook export is the first source of
truth. Normalized helper files cannot weaken sequence, role, real-asset
requirements, or background/context requirements.

### 3. Text-Only Package Writing

The package writer creates the package files. The writer must keep image work out
of this phase and must make `prod.md` executable.

Every live runtime beat in direct-consumer/full-pass packages needs a
machine-convertible runtime instruction:

```text
**Runtime AI instruction:** Goal: ... Constraint: ... Tone: ... Progress evidence: ... Branch behavior: ... Frame/source guardrail: ...
```

This applies to:

- Step 1 hook;
- Step 2 mission/transition;
- every Step 3 round;
- Cat5 synthesis when present;
- celebration;
- closing;
- early exit where applicable.

`AI says` and `Example AI line` may remain as tone examples, but they are not
enough by themselves for downstream runtime loading.

### 4. Post-Package Source-Intent Audit

After package writing, the auditor compares the generated package against the
source snapshot. This is where intent drift should be caught before downstream
testing.

If the package changes the activity type, child role, required action, real asset
requirement, or promised background/context information without a
product-approved adaptation, the package cannot be accepted.

### 5. Asset Generation And Curation

The image-only phase reads `asset_manifest.yaml`, `spec.md` asset briefs, and the
current WonderLens asset style guidance. It generates or curates runtime PNGs
without editing package prose.

Generated assets should be beat-specific, style-consistent, readable at runtime
size, and free of baked UI chrome, app-owned progress/control markers, readable
text, labels, logos, watermarks, and unsupported claims. Subset and full-pass
generation should use 512x512 source PNGs while final runtime variants remain
manifest-driven.

The full-pass asset floor matches the current fullstack-demo activity packages:
each package needs package-local 512x512 beat assets for `activity_icon`,
`intro_scene`, `rules_scene`, `round_1_scene`, `round_2_scene`,
`round_3_scene`, `celebrate_scene`, and `closing_scene`; Cat5 or synthesis
flows also need `synthesis_scene`. Round objects, choice items,
targets, distractors, characters, and badges are generated as additional
separate PNGs, not as substitutes for the beat-scene bundle.

Scene bundles must also stay activity-specific. A generic cozy-room,
blank-board, child-response, or child-on-rug layout cannot be reused across
unrelated activities. Guided drawing and other build-step activities must show
the exact child action for each round, not generic materials or capability
placeholder imagery.

Reference-bound assets require accepted source/provenance metadata. Random
illustrative approximations are not acceptable for real constellations,
artworks, maps, scientific diagrams, cultural artifacts, species, historical
objects, named places, or famous structures.

### 6. Package And Import Validation

Before dialogue QA, package/import validation checks:

- required files exist;
- schemas validate;
- demo support and asset manifests validate;
- fullstack-demo imports the package without content improvement;
- converted fullstack `step_instructions` preserve runtime instruction quality;
- Cat5 synthesis remains distinct from collection rounds and celebration;
- WonderLens AI can generate/load runtime artifacts from the package;
- asset paths resolve;
- unsupported/degraded gates remain honest.

### 7. Marker-Free Runtime Input Precondition

Before comparing or accepting fullstack-demo and WonderLens AI dialogue quality,
runtime-facing package input must not contain review-only blocker markers.

Required check:

```bash
! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md
```

Any match is treated as a package-owned blocker unless the downstream converter
is explicitly proven to strip or accept that marker. This matters because
WonderLens AI rejects raw leakage markers during runtime generation.

### 8. Fullstack Dialogue QA

The fullstack dialogue validator starts from the imported package and tests live
or runtime-equivalent turns across representative user strategies:

- ideal response;
- minimal response;
- wrong answer;
- off-topic input;
- help or confusion;
- premature done;
- silence or no response;
- unsupported request where the runtime supports testing it.

The validator checks whether the dialogue preserves source intent, uses package
runtime instructions, keeps branch behavior concrete, avoids unsupported sensing
or screen claims, and handles recovery without drifting to generic copy.

### 9. WonderLens AI Dialogue QA

The WonderLens AI dialogue validator runs equivalent checks against WonderLens AI
runtime artifacts. The goal is not just "conversion succeeded"; it is whether
the runtime behavior remains as rich and faithful as the package requires.

Failures are classified as:

- package-owned instruction gap;
- WonderLens-runtime-owned guardrail or converter gap;
- product-capability decision;
- test harness or credential blocker.

Package-owned failures return to autodesign for repair.

### 10. Repair Loops

Repair is routed by owner:

- source-intent drift: text/package repair, then source-intent re-audit;
- thin runtime instructions: package repair, then import/dialogue revalidation;
- asset misalignment: image prompt/source/image repair, then image QA;
- fullstack runtime issue: downstream follow-up unless explicitly in scope;
- WonderLens AI runtime issue: downstream follow-up unless explicitly in scope;
- product capability gap: blocked/degraded/resolved-blocker decision, depending
  on run contract.

The pipeline should not hide a downstream runtime issue by weakening the
autodesign package.

### 11. Final Independent Review

The final reviewer checks the full evidence chain before acceptance:

- source-intent audit passed;
- package depth floor passed;
- runtime instructions are machine-convertible;
- assets passed image QA;
- fullstack import/dialogue evidence exists;
- WonderLens AI runtime/dialogue evidence exists;
- marker-free precondition passed;
- repair loops were revalidated;
- unresolved issues are correctly owned and recorded.

Only after this final review can the run be accepted.

## Product Team View

Product should use the full-pass reports to answer:

- Does each generated activity preserve the original product promise?
- Is any required capability unsupported today?
- Is a degraded behavior acceptable, or should the row stay blocked?
- Are image assets appropriate for the child-facing experience, including no
  duplicated selectable objects in picker backgrounds and no early answer
  reveal in progressive-evidence flows?
- Do live dialogue transcripts feel like the intended activity, not just a
  generic interaction?
- Are downstream issues product-capability decisions or implementation bugs?

Product decisions should be recorded explicitly. If minimum-to-unblock behavior
is approved, the package records former blockers in `spec.md`, run provenance,
`run_manifest.yaml`, and review output. Runtime-facing `prod.md` should remain
safe for direct consumers.

## Engineering Team View

Engineering should use the pipeline to verify contracts:

- package schema and required files;
- tag vocabulary compatibility;
- `prod.md` runtime instruction parseability;
- fullstack import and `step_instructions` conversion;
- WonderLens AI runtime generation/loading;
- asset path resolution;
- marker-free runtime input;
- no unsupported sensing, hidden-state, screen, or image claims;
- issue ownership between autodesign, fullstack-demo, WonderLens AI, image
  generation, and product capability.

Engineering follow-ups should be opened only for downstream-owned failures.
Package-owned failures should be repaired in autodesign first.

## Acceptance Gates

| Gate | Required Evidence | Owner |
|---|---|---|
| Source intent | Pre/post source-intent audit with source evidence | Autodesign |
| Package quality | Five-file package plus executable `prod.md` | Autodesign |
| Runtime instruction quality | Machine-convertible instruction for every live beat | Autodesign |
| Assets | Built PNGs, manifest validation, image QA | Autodesign image phase |
| Fullstack import | Import report and converted `step_instructions` | Fullstack validation |
| WonderLens AI runtime | Generated/loaded runtime artifacts | WonderLens AI validation |
| Dialogue QA | Sanitized transcripts or runtime-equivalent reports | Consumer validators |
| Marker-free input | No `RESOLVED BLOCKER` or `RESOLVE BLOCKER` in runtime-facing `prod.md` | Autodesign |
| Final review | Independent PASS or explicit residual-risk report | Final reviewer |

## Relationship To Other Documents

- `README.md`: entry point and common invocation.
- `goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md`: executable
  full-pass run contract; owns hard constraints, delegated-agent rules,
  credential boundaries, live validation ordering, and final acceptance.
- `GOAL.md`: compact default objective and completion contract for ordinary
  active-queue runs.
- `run.md`: compact default execution loop.
- `program.md`: canonical authoring, package quality, and rubric contract.
- `docs/plans/2026-06-01-full-pass-agentic-pipeline.md`: implementation plan for
  adding the full-pass workflow contract to the repo.
- `goals/2026-06-01-full-pass-agentic-pipeline-goal.md`: Codex goal file for the
  workflow-contract implementation, not the production run invocation.
- `docs/activity_asset_generation_workflow.md`: detailed asset generation and
  curation workflow.

## Common Questions

### Should I Run Root GOAL.md First?

No. For a full production pass, execute the scoped full-pass goal directly. It
pulls in the compact root defaults plus the hard full-pass requirements for
asset generation, package validation, image QA, fullstack dialogue QA,
WonderLens AI dialogue QA, repairs, and final review.

### Does Fullstack-Demo Improve The Activity?

No. Fullstack-demo is a loader and executor. If fullstack output is weak because
the package instructions are weak, autodesign must repair the package. If
fullstack ignores good package instructions, record a downstream fullstack
follow-up.

### Does WonderLens AI Improve The Activity?

No. WonderLens AI is a direct runtime consumer. If WonderLens AI rejects or
weakens valid package content, record a WonderLens-owned follow-up. If the
package content is thin, repair autodesign first.

### Why Require Both Fullstack And WonderLens AI Dialogue QA?

They are separate runtime consumers with different conversion and execution
paths. A package is not production-ready just because one consumer loads it.
Both need to preserve source intent and runtime instruction quality.

### Why Is The Marker-Free Check Necessary?

Resolved-blocker notes are useful for review artifacts, but raw markers in
runtime-facing `prod.md` can break downstream conversion. WonderLens AI currently
rejects raw leakage markers, so the full-pass comparison must start from clean
runtime-facing input.
