# Codex Goal: Autonomous Activity Generation

Use this file as the `/goal` target for running the WonderLens autonomous activity generation loop.

## Goal

Generate or triage WonderLens activity assignments from `assignments.md` using the current authoring workflow in `program.md`, `templates.md`, `run.md`, and the migrated `activities/<activity_id>/` package contract.

Each run must also create a provenance directory under `runs/<run_id>/` so generated packages and blocked briefs can be traced back to the exact `/goal` session.

## Recommended `/goal` Command

```text
/goal Execute GOAL.md end to end using run.md. Initialize run provenance, audit/enrich existing checked activity packages against the current migrated package depth floor, using separate reviewer agents for package-quality review and repair evidence. Then process the run-start unchecked assignment snapshot exactly once in order. For each row, generate a five-file package that passes author self-check, independent reviewer-agent review, and package validation, or record a blocked brief and continue. Do not append results.tsv or mark a generated assignment complete until reviewer issues are repaired and re-reviewed. After final validation, generate and validate a self-contained light-theme review dashboard at runs/<run_id>/review.html with direct activity detail cards, sortable Cat1/Cat3/Cat5/status/mechanic controls, and classified blocked-reason badges. Stop only on a hard workflow failure that makes later rows unsafe. Use GOAL.md success criteria as the completion contract and report generated, enriched, blocked, reviewer-agent coverage, review dashboard path, checks, and residual risks.
```

## Success Criteria

The goal is complete only when all of the applicable criteria below are met.

1. Setup context is loaded:
   - `GOAL.md`
   - `program.md`
   - `templates.md`
   - `run.md`
   - `runs/README.md`
   - `activities/README.md`
   - `activities/_schema/tag_block.schema.json`
   - `docs/activity_vocabulary.md`
   - `docs/game_styles.md`
   - `assignments.md`
   - Any `concept_source=file#id` or `asset_requirements=file#id` companion files referenced by pending assignment rows
   - `entity_guidance.md` and `conversation_bridge.md` when mapping or warm/cold bridge handling is required

2. Run provenance is initialized before assignment processing:
   - A `run_id` is created in `YYYYMMDD_HHMMSS_<short_label>` format.
   - `runs/<run_id>/run_manifest.yaml` exists with `status: in_progress`, source files, mapping root, output lists, and summary counters.
   - `runs/<run_id>/assignment_snapshot.md` preserves unchecked assignment rows pending at run start.
   - `runs/<run_id>/generated_activity_ids.txt`, `adaptation_briefs/`, `blocked_briefs/`, and `review_notes.md` are initialized.

3. Assignment rows are processed in order:
   - Only unchecked `- [ ]` rows are processed.
   - The run-start `assignment_snapshot.md` is the queue; each snapshot row is visited at most once per run, even if a blocked row remains unchecked for a future product decision.
   - `assignment_type` is parsed or inferred.
   - `activity_concept=` is used for concept-led rows; legacy concept aliases are normalized before Phase 0.
   - Source concepts may be Chinese, but generated adaptation briefs and package files are English-only.

4. Phase 0 adaptation is completed when required:
   - `activity_concept`, `match_pattern`, and `capability_probe` rows always receive an `adaptation_brief`.
   - `entity_activity` rows receive an `adaptation_brief` when mapping, category, mechanic, trigger, or scaffold fit needs resolution.
   - Referenced `concept_source` and `asset_requirements` rows are loaded before the brief is written.
   - The brief records `input_mode`, `canonical_mechanic`, readiness, trigger condition, mapping use, asset dependency, product capability flags, scaffold choice, and assumptions.
   - If `asset_policy` or companion asset rows are present, the brief copies them into `asset_dependency` instead of inferring image needs from prose.
   - The normalized brief is written to `runs/<run_id>/adaptation_briefs/` when generation may proceed, or to `runs/<run_id>/blocked_briefs/` when blocked.

5. Blocked assignments are triaged safely without halting the batch:
   - If `readiness=blocked_until_product_decision`, output the adaptation brief for that assignment and continue to the next unchecked row.
   - Do not create package files.
   - Do not append `results.tsv`.
   - Do not mark the assignment complete; it remains visible for the future product/design decision.
   - Update `runs/<run_id>/run_manifest.yaml` with a `blocked_assignments` entry and increment `blocked_count`.
   - Report the missing product decision, capability, schema, category, template extension, or asset pipeline decision.
   - Use `status: completed_with_blockers` when the run finishes all processable rows but one or more rows blocked. Use `status: failed` only for hard workflow failures that prevent safe processing of later rows.

6. Generation-ready assignments produce a complete package:
   - Exactly five files exist under `activities/<activity_id>/`:
     - `spec.md`
     - `prod.md`
     - `tag_block.yaml`
     - `recap.template.yaml`
     - `dashboard.template.yaml`
   - Directory name matches `tag_block.yaml` `activity_id`.
   - `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.

7. Existing package enrichment is handled before the unchecked assignment loop starts:
   - Checked `assignments.md` rows that include `activity_id=<id>` and have an existing `activities/<id>/` package are audited against the current migrated package depth floor.
   - Checked rows are not treated as frozen when generation standards changed after they were created.
   - Separate reviewer agents are spawned for scoped package-quality review when the run audits or enriches packages; assign reviewers disjoint package directories when multiple packages are reviewed in parallel.
   - Structurally valid but thin packages are enriched in place, preserving `activity_id`, tag-block enums, recap/dashboard placeholders, asset IDs, and the five-file package contract.
   - Enrichment focuses on decision-useful `spec.md` detail and runnable `prod.md` detail: concrete design intent, scaffold fit, game-feel rationale, executable dialogue, branch-specific follow-ups, screen states, distinct Step 3 rounds, and earned magic moments.
   - Reviewer-agent findings, direct repairs, re-review outcomes, no-op decisions, and residual concerns are recorded in `runs/<run_id>/review_notes.md`; any changed files are also recorded in `runs/<run_id>/run_manifest.yaml`.
   - Enrichment does not append `results.tsv`, rewrite completed assignment checkboxes, or create a second generated activity entry. It is recorded as package maintenance in `runs/<run_id>/run_manifest.yaml` and/or `runs/<run_id>/review_notes.md`.
   - Packages that already meet the current floor are recorded as no-op audits in the run notes when useful.
   - Package checks are rerun after any enrichment.

8. Runtime package quality checks pass:
   - `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` are written in English, even when the source concept was Chinese.
   - `spec.md` is decision-useful, not just a scorecard wrapper: it records concrete design intent, assumptions, constraints, scaffold fit, asset/product dependencies, game-feel rationale, and residual risk when relevant.
   - `prod.md` satisfies the migrated package depth floor from `program.md`: every step is runnable, concrete, and specific enough for the prompt composer without relying on old design files.
   - `prod.md` contains no `## Self-Evaluation Scorecard`.
   - `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
   - Every runtime Step 3 round in `prod.md` is fully expanded.
   - Steps 1, 2, 4, and 5 include executable dialogue/screen detail; Step 3 rounds are distinct in objective, child action, branch-specific follow-up, and screen-state change.
   - Magic moments are earned by the child's repeated action and visible in dialogue plus screen behavior, not only awarded as a generic badge.
   - `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
   - `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`, `spec.md`, and `prod.md` agree on mechanic, pillar, game style, focal attribute, badge/reward, and next-step direction.

9. Mechanic-first checks pass:
   - `tag_block.yaml` `activity_signature.mechanic` matches the canonical mechanic from the assignment or adaptation brief.
   - The repeated child action in `prod.md` Step 3 matches that mechanic.
   - Weak scaffold fit or generation assumptions are disclosed in `spec.md` `## Adaptation Rationale`.
   - Pillar and `game_style` support the mechanic; they do not override it.

10. Asset dependency checks pass when assets are present:
   - `spec.md` includes `## Asset Brief` when `asset_dependency.policy` is not `no_assets`.
   - Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
   - Required assets declare `asset_type`, requiredness, generation timing, use step, purpose, display behavior, and fallback behavior.
   - Generated assets include a directly usable English `prompt_en`; existing/displayed assets include a `source` or approved source description.
   - `prod.md` references asset IDs and fallback behavior, not raw generation prompts.
   - The loop does not generate or store image files unless a future asset pipeline explicitly changes this contract.

11. Mapping checks pass when mapping is required:
   - `mapping=` resolves through `MAPPING_ROOT/_index.yaml`.
   - Entity-specific facts, IB concepts, related concepts, bridge prerequisites, and tier language are grounded in the mapped YAML.
   - Parameterized rows use placeholders instead of inventing entity-specific claims.

12. Review and logging are complete for generated packages:
   - The package passes the 10-dimension rubric in `program.md`.
   - A separate reviewer agent checks every generated package against the same 10 dimensions, the migrated package depth floor, mechanic fidelity, asset-brief coherence, and package-file consistency.
   - Reviewers explicitly fail structurally valid but thin/generic packages that do not meet the migrated package depth floor.
   - Any reviewer FAIL or credible uncertainty is repaired before logging; the repaired package is re-reviewed by a fresh separate reviewer agent or by the original reviewer after reading the changed files.
   - `runs/<run_id>/review_notes.md` records reviewer-agent name/id when available, package scope, PASS/FAIL/N/A evidence, repairs made, and final reviewer outcome.
   - `results.tsv` receives one row for each generated package.
   - `runs/<run_id>/generated_activity_ids.txt` includes each generated `activity_id`.
   - `runs/<run_id>/run_manifest.yaml` links each generated assignment row to `activities/<activity_id>/`, its adaptation brief when present, and `results.tsv`.
   - The processed assignment row is changed from `- [ ]` to `- [x]`.

13. Human review dashboard is generated:
   - `runs/<run_id>/review.html` exists before the final report.
   - The page is a static, self-contained HTML file with embedded CSS/JS only; it does not require a dev server, build step, network access, or external assets.
   - The page is a derived review artifact, not a source of truth. It summarizes data from `run_manifest.yaml`, `review_notes.md`, `results.tsv`, package files, adaptation briefs, and blocked briefs; if a value cannot be derived, it is shown as unknown or omitted rather than invented.
   - Default visual design is a polished light theme. Use restrained color, clear typography, accessible contrast, compact tables, stable spacing, responsive layout, and status badges; do not default to a dark theme or decorative gradient/orb-heavy presentation.
   - The dashboard is generated with `python3 scripts/generate_run_review.py runs/<run_id>` and validated with `python3 scripts/generate_run_review.py --validate runs/<run_id>`.
   - The dashboard includes run summary counts, direct activity detail cards for every generated/enriched package, blocked assignment cards or tables, reviewer-agent coverage, validation/check results, residual risks, and next actions.
   - Activity cards expose enough `spec.md`, `prod.md`, and `tag_block.yaml` detail for a reviewer to inspect the activity in the page without opening or downloading package files, including concrete runtime beat details for AI prompt, child responses, follow-up, and screen state.
   - Generated and enriched package rows link to the package files; blocked rows link to blocked briefs; run-level links point to the manifest, review notes, assignment snapshot, and generated activity ID list.
   - The dashboard includes search/filter/sort controls for status, package type, Cat1/Cat3/Cat5 type, mechanic, tier, reviewer coverage, asset dependency, and blocked reason when those fields are available.
   - Blocked assignments classify missing product/design decisions into skim-friendly reason badges, for example runtime image generation, coloring/recoloring UI, Cat3 material workflow, UI state/progress memory, prebuilt asset display, motion safety, before/after evidence, OCR/text handling, and caregiver setup/pacing.
   - Blocked assignments are labeled as Phase 0 only. They do not have runtime beats or package files until the blocking product/design decision is resolved; the dashboard includes a blocking-reason guide explaining what each reason means and why it prevents safe design.
   - `runs/<run_id>/run_manifest.yaml` records the dashboard path, and the final report includes it.

14. Final report is clear:
   - State how many packages were generated.
   - State how many existing packages were enriched or audited as already compliant.
   - List any blocked assignments and the exact reason.
   - Include the `run_id` and `runs/<run_id>/run_manifest.yaml` path.
   - Include the `runs/<run_id>/review.html` path.
   - Report reviewer-agent coverage: which packages were reviewed, which were edited by reviewers or repaired after review, and whether all generated packages received independent PASS evidence.
   - List verification commands run and their results.
   - State any residual risk or follow-up product decision.

## Assignment Type Names

Use these names in new `assignments.md` rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked |

Legacy concept aliases should be treated as `assignment_type=activity_concept` with `activity_concept=<value>`.
