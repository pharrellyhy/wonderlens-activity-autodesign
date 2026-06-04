# Full-Pass Agentic Pipeline Presentation Transcript

Source presentation: `docs/full_pass_agentic_pipeline_presentation.html`

Suggested use: presenter script for a product and engineering audience. It is not a word-for-word reading of every label on the page. It is the spoken narrative that explains how to use the pipeline, who produces each artifact, and why each gate exists.

## Opening

Today I will walk through the WonderLens full-pass agentic pipeline.

The goal of this pipeline is to take a source activity idea and turn it into a validated WonderLens activity package. A successful output is not just a package directory. It includes runtime text, image assets, downstream consumer checks, live or runtime-equivalent dialogue QA, repair evidence, and final review.

The most important framing is ownership. Autodesign owns source intent, package quality, runtime instructions, assets, and package-owned repairs. Fullstack-demo and WonderLens AI are direct consumers. They should load and validate the package as provided, not quietly improve weak package content downstream.

## Why The Full Pass Exists

A package can pass static structure checks and still fail the product promise.

The common failure is not that a file is missing. The common failure is drift. A workbook activity might promise one child action, one source object, and one kind of reveal, but the generated package can turn that into a simpler or more generic activity. That can still look valid to a schema.

The full pass adds checks where drift usually happens: source intent, runtime behavior, visual assets, consumer conversion, repair routing, and final review.

The five principles are:

Intent: preserve the source play frame.

Runtime: make `prod.md` executable, not just pleasant to read.

Assets: match the actual beat, not just the general mood.

Consumers: validate both Fullstack-demo and WonderLens AI.

Repair: route every failure to the correct owner.

## Source Rules

The updated contract starts from the original workbook promise.

For workbook-derived activities, `inputs/original_activity_concepts_2026-05-29.tsv` is the controlling source. `inputs/source_activity_concepts.md` is helpful, but it is only a normalized helper. It can clarify names, mechanics, asset hints, and capability notes. It cannot weaken the original source promise.

Before any package writing starts, `run_manifest.yaml` must record `source.full_pass_pipeline: true` and `source.asset_build: generate_and_curate`.

The runtime contract is also locked here. Step 1, Step 2, every Step 3 round, Cat5 synthesis, celebration, closing, and early exits all need machine-convertible instruction. The instruction needs goal, constraint, tone, progress evidence, branch behavior, and frame guardrail.

For Cat5, collection, synthesis, and celebration stay distinct. If a Cat5 activity has synthesis behavior, the importers must preserve it separately instead of collapsing it into a generic final step.

## Pipeline Map

This map is the operating view of the full pass.

There are three lanes:

Autodesign owns source, text package, audits, package repair, and final reporting.

Image phase owns manifest completion, image generation, reference curation, asset build, Image QA, and image repair.

Consumers owns Fullstack-demo import, Fullstack QA, WonderLens AI runtime checks, AI dialogue QA, issue classification, and final review.

Use the clickable steps during the presentation to explain ownership. The right-side detail panel tells us who owns the step, what it takes as input, what it produces, what validates it, and where repairs go.

The key rule is that these steps are not all the same kind of work. Some are deterministic checks. Some are agent judgment. Some depend on downstream runtime systems. The pipeline is valuable because it does not hide those differences.

## Workflow Animation

The animation shows the run packet moving through the pipeline.

Start with Source lock: the master orchestrator and source-intent auditor freeze what must survive.

Then Text package: the writer creates the package files, demo support, runtime beats, and text-only asset contract.

Then Post audit: an independent package auditor checks whether the package still matches the source contract.

Then Bundle repair: the manifest is made asset-ready. This step ensures every required visual role exists before image generation starts.

Then Generate / curate: image agents create PNGs or accept real source material.

Then Build assets: the builder writes final package-local runtime assets and manifest paths.

Then Image QA: the validator checks manifest coverage, runtime size, style, crop safety, beat fit, reference fidelity, duplicate items, and answer leakage.

Then Consumer QA: Fullstack-demo and WonderLens AI load the package and exercise runtime behavior.

Finally, Final review: an independent reviewer checks the evidence chain before acceptance.

Use Pause when discussing a failure route. Use Restart when you want to explain the sequence from the beginning. Use Loop when presenting the overall flow without stopping.

## Text Package Detail

Package writing is text-only, but it is still the runtime contract.

The package is expected to contain `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`, `demo_support.yaml`, and `asset_manifest.yaml`.

`spec.md` is the reviewer reference. It carries source promise, adaptation rationale, asset brief, usage timeline, residual risk, and one self-evaluation scorecard.

`prod.md` is the runtime guide. It must describe Step 1 through Step 5, fully expanded Step 3 rounds, screen states, child branches, follow-up policy, and asset IDs with display and fallback behavior.

`tag_block.yaml` is the machine contract. It carries category, mechanic, pillar, game style, focal attribute, progression, tags, and entity coverage vocabulary.

`demo_support.yaml` is the honest demo gate. It says whether the activity is supported, degraded, or unsupported, and it records UI template, entity binding, runtime requirements, and limitations.

`asset_manifest.yaml` is the text-only asset contract. It names separate runtime assets, variants, fallback behavior, paths, and reference provenance requirements.

The main takeaway is that example lines are not enough. `prod.md` must include a `Runtime AI instruction` for every live beat. That instruction is what lets fullstack-demo produce useful `step_instructions` and lets WonderLens AI preserve the same behavior.

## Agent Roles

The master agent orchestrates, but independent agents own separate review surfaces.

On the authoring side, the master orchestrator controls scope, snapshots, blockers, credentials, servers, commits, and the final report. The source-intent auditor locks the play frame before and after writing. The text-only package writer writes runtime prose and package metadata.

On the asset side, the image-only generator or curator produces the PNGs and reference-backed assets. The image quality validator checks style, crop safety, beat fit, and reference fidelity. The image improver repairs visual artifacts without changing dialogue.

On the consumer side, the package/import validator checks schema, paths, converted instruction shape, and gates. Fullstack and WonderLens AI validators run runtime-equivalent dialogue checks. Dialogue improvers repair package-owned guidance gaps. The final reviewer audits the evidence and residual-risk ownership.

The important rule is that a writer should not be the only reviewer of its own artifact.

## QA Criteria

This section is the pass/fail contract for the three riskiest validation surfaces.

Image QA validates the asset bundle. It checks manifest coverage, package-local 512x512 PNGs, asset IDs and paths, flat Nordic style, round-screen crop safety, beat alignment, reference provenance, reference fidelity, duplicate selectable items, readable text, logos, watermarks, and premature answer reveal.

Image QA evidence should include an asset inventory, built file paths, thumbnails or review notes, source metadata for reference-bound assets, and per-asset QA notes for every failure.

Image QA passes only when every required asset loads, matches its runtime beat and style, source-bound assets are real and faithful, and every remaining issue is repaired, blocked, or explicitly accepted as degraded.

Fullstack QA validates the web demo as a direct consumer. It checks that the package is imported as authored, entity binding is honored, supported/degraded/unsupported gates are respected, assets resolve, `step_instructions` preserve goal, constraint, tone, progress evidence, branch behavior, and frame guardrail, Cat5 synthesis stays separate, and the expected UI state appears.

Fullstack QA must exercise ideal, minimal, wrong, off-topic, help, done, silence, photo, and item flows. Evidence should include the import report, converted runtime YAML or demo MD, asset path report, screenshots or UI notes, representative transcripts, and classified failures.

Fullstack QA passes only when the web demo loads without unsafe fallbacks, honors demo gates, shows declared assets, preserves package runtime beats, and classifies every mismatch as package-owned or fullstack-owned.

AI dialogue QA validates WonderLens AI runtime behavior against the generated YAML and `prod.md`. It checks real camera or `photo_id` assumptions, Cat5 response types, collection catalog use, source guardrails, branch behavior, synthesis, celebration, and unsupported visual claims.

AI dialogue QA evidence should include the runtime artifact report, prompt or context trace, transcripts across the same strategies used by fullstack QA, comparison notes, and owner classification for mismatches.

AI dialogue QA passes only when responses follow the package goal, constraint, tone, progress evidence, branch policy, and source guardrails across ideal and recovery paths, with every discrepancy either repaired or assigned to the correct owner.

## Artifact Flow

The artifact flow explains who generates what and how to use each group.

Source and run artifacts are generated by the master orchestrator and source-intent auditor. Use them to freeze scope, source promise, run flags, blockers, and evidence paths. They produce the source snapshot, assignment snapshot, pre-package audit, and run manifest.

Autodesign package artifacts are generated by the text-only package writer plus the image-only asset generator and builder. Use them as the direct import contract for fullstack-demo and WonderLens AI. They produce the required package files, demo support, asset manifest, PNG assets, selectable items, and reference sources.

Consumer evidence is generated by import validators, runtime validators, Image QA, and the final reviewer. Use it to decide whether the activity should be accepted, repaired in the package, routed to a downstream follow-up, or blocked by product capability.

This is also where ownership becomes clear. Weak package evidence returns to Autodesign. Good package evidence that is ignored by a runtime becomes a downstream issue.

## Asset Phase

The current asset style is flat Nordic nursery illustration: quiet white backgrounds, restrained boho pastels, sparse linework, generous negative space, one file per beat or item, and no baked device chrome.

Every package needs the standard scene bundle: `activity_icon`, `intro_scene`, `rules_scene`, three round scenes, `celebrate_scene`, and `closing_scene`. Cat5 or synthesis flows also need `synthesis_scene`.

Selectable items, targets, distractors, reference sources, and badges are additional assets. They do not replace the scene bundle.

Reference-bound assets are different from purely illustrative assets. If the activity promises a real artwork, constellation, landmark, animal, plant, or other reference-bound object, the asset must be source-backed. A random generated approximation is not enough.

The Vegetable Sort example shows the target shape: scene and icon assets for every major beat, plus separate item PNGs for each selectable vegetable card.

## Repair Routing

The pipeline is useful because it refuses to hide ownership.

If there is source intent drift, repair the text package and rerun source-intent audit.

If runtime instruction is thin, repair the package and rerun import and dialogue validation.

If an image is wrong, repair the image-owned artifact and rerun Image QA.

If fullstack-demo ignores good package instructions, record a fullstack follow-up.

If a product capability is unsupported, do not pretend it is playable. Mark it blocked, degraded, or accepted only with approved minimum behavior.

If credentials or provider access are missing, record the exact missing prerequisite and the retry evidence.

## Acceptance Gates

A full pass is accepted only when every gate has evidence, or every blocker is explicit, owned, and reproducible.

The key gates are run flags, source intent, package quality, runtime instruction quality, assets, fullstack import, WonderLens AI runtime, dialogue QA, marker-free runtime input, and final review.

This means the final acceptance standard is not "the package exists." The standard is that both direct consumers can load and exercise the package without weakening the activity promise.

## Team Views

Product should use the run output to judge whether the generated activity preserves the original promise, whether a required capability is unsupported, whether degraded behavior is acceptable, whether image assets fit the child-facing experience, and whether dialogue transcripts feel like the intended activity.

Engineering should use the run output to verify schema, vocabulary, `prod.md` conversion, fullstack-demo behavior, WonderLens AI behavior, asset path resolution, and issue ownership.

The same run output supports both views, but they answer different questions.

## Invocation

For a full production pass, run:

`/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.`

The scoped goal owns the full-pass flags, delegated-agent rules, credential boundaries, live validation order, and final acceptance criteria.

The asset phase uses the builder sequence:

`repair_full_pass_asset_bundle.py`, then `build_activity_assets.py`, then the asset validation scripts.

The completion standard is not that a package exists. The completion standard is that the package, assets, and direct consumers all preserve the activity promise, or that every remaining limitation has a clear owner and evidence.

## Closing

The practical recommendation is to treat this as a release-quality validation path, not as the cheapest path for every exploratory package.

The full pipeline is intentionally rigorous. It is also long and failure-prone because it crosses text generation, asset generation, consumer import, runtime behavior, and live dialogue. That is why the artifacts, owners, and repair routes need to be explicit.

When the pipeline passes, we can say more than "the package was generated." We can say the source promise survived through package text, image assets, consumer runtime conversion, dialogue behavior, and final review.
