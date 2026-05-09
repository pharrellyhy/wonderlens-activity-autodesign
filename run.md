# Run Instructions - Autonomous Activity Package Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.
> When launched from Codex `/goal`, use `GOAL.md` as the objective and success criteria, and use this file as the execution procedure.

## Setup (one-time, do this first)

Entity mapping root: `MAPPING_ROOT=data/mappings_dev20_0318` (repo-relative). Use `MAPPING_ROOT/_index.yaml` as the entity registry whenever mapping data is required.

1. Read `GOAL.md` - goal, assignment type names, and success criteria.
2. Read `program.md` fully - constraints, migrated package format, rubric, and seed exemplars.
3. Read `templates.md` fully - Template 0 reference, mechanic adapters, Cat1/Cat5 category modifiers, and pillar/style scaffolds.
4. Read `docs/game_styles.md` - game style taxonomy reference.
5. Read `activities/README.md` - required five-file package layout.
6. Read `activities/_schema/tag_block.schema.json` and `docs/activity_vocabulary.md` - tag-block schema and current enum vocabulary.
7. Read `docs/activity_tag_block_usage.md` and `docs/activity_tag_block_progression_guide.md` - field ownership, recap/dashboard usage, and progression guidance.
8. Read `entity_guidance.md` and `conversation_bridge.md` when an assignment is mapping-informed or requests warm/cold bridge handling.
9. Read `assignments.md` - work queue.
10. Verify `activities/` exists with `_schema/tag_block.schema.json`.
11. Verify `results.tsv` exists and has the current header. If it is missing, create it with this header:

```
assignment	entity	category	tier	pillar	style	status	d1_tech	d2_hook_transition	d3_edge	d4_ib	d5_tier	d6_dialogue	d7_screen	d8_mapping	d9_game_feel	d10_pillar_fidelity	filename	timestamp
```

12. Create a run provenance directory before processing the first assignment:

```
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── adaptation_briefs/
├── blocked_briefs/
└── review_notes.md
```

Use `run_id=YYYYMMDD_HHMMSS_<short_label>`, for example `20260509_113000_activity_concepts`. If the user supplies a run label, slugify it for `<short_label>`; otherwise infer a short label from the assignment batch, such as `activity_concepts`, `mapping_batch`, or `mixed_assignments`.

13. Write `assignment_snapshot.md` with the unchecked `- [ ]` rows that are pending at run start, preserving their original order and section headings where practical.

14. Initialize `run_manifest.yaml`:

```yaml
run_id: <run_id>
status: in_progress
started_at: "<ISO 8601 timestamp>"
completed_at:
source:
  goal_file: GOAL.md
  runbook: run.md
  assignments_file: assignments.md
  assignment_snapshot: runs/<run_id>/assignment_snapshot.md
  mapping_root: data/mappings_dev20_0318
summary:
  pending_at_start: <N>
  generated_count: 0
  blocked_count: 0
  failed_count: 0
outputs:
  generated_activities: []
  blocked_assignments: []
checks: []
notes:
  - "Canonical packages remain under activities/<activity_id>/."
```

15. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Run id: <run_id>. Starting activity package loop."

## The Loop (repeat for every uncompleted assignment)

For each assignment in `assignments.md` that is marked `- [ ]` (not yet completed):

### Step 1: Parse the assignment

Extract: assignment_type (if provided), activity_concept (if provided), legacy concept alias (if provided), concept_source (if provided), description/notes (if provided), entity, category, tier, mechanic (if provided), pillar (if provided), style (if provided), scene (if provided), trigger_condition (if provided), mapping (if provided), asset_policy (if provided), asset_requirements / companion asset rows (if provided), product_capabilities (if provided), start type (if provided), and output activity_id (if provided). Normalize any legacy concept alias to `activity_concept=` and infer `assignment_type=activity_concept` unless a more specific type is declared.

If `concept_source=` points to `file#concept_id`, read that repo-relative file and load the matching concept section before Phase 0. If `asset_requirements=` points to `file#asset_id`, read the same or referenced file and load the matching asset requirement section. Use the assignment row as the execution source of truth, and use the companion file as richer source / asset context.

Source concepts may arrive in Chinese or mixed language. Before writing an adaptation brief or package, normalize the concept name, description, trigger, assumptions, asset rows, and generated copy to English. Do not copy Chinese source prose into generated activity artifacts.

If `assignment_type` is not specified, infer it:

- `entity + category` with no concept field -> `entity_activity`
- `activity_concept=` or a legacy concept alias -> `activity_concept`
- property/category-driven concept with runtime placeholders -> `match_pattern`
- declared product dependency flags or unsupported category risk -> `capability_probe`

If tier is not specified, infer it per `program.md` rules. If scene is not specified, invent one unless the assignment is blocked in the adaptation brief.

### Step 1.1: Create adaptation brief

Run `program.md` Phase 0 before scaffold composition. This is required for `activity_concept`, `match_pattern`, `capability_probe`, legacy concept aliases, and underspecified rows; it is allowed for normal `entity_activity` rows.

1. Classify `input_mode` as `mapping_informed`, `parameterized`, or `concept_only`.
2. Identify `canonical_mechanic` and `mechanic_confidence`. If `mechanic=` is specified, it wins unless it is outside the current enum.
3. Decide `category_decision`, `readiness`, `trigger_condition`, `entity_role`, `observation_angle`, `focal_attribute`, mapping usefulness, asset dependency, product capability flags, and scaffold fit.
4. If `asset_policy` is provided, copy it into `adaptation_brief.asset_dependency.policy` instead of inferring asset need from prose. If companion asset rows are provided, normalize them into `adaptation_brief.asset_dependency.assets`.
5. Write the normalized adaptation brief to `runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml` if generation may proceed, or to `runs/<run_id>/blocked_briefs/<ordinal>_<assignment_slug>.yaml` if blocked.
6. If `readiness=blocked_until_product_decision`, stop. Output the adaptation brief and missing capability/template/asset decision. Update `run_manifest.yaml` with a `blocked_assignments` entry and `status: blocked`; do not create package files, append `results.tsv`, mark the assignment complete, or commit.
7. If `readiness=generate_with_assumptions`, carry assumptions into `spec.md` under `## Adaptation Rationale`.
8. If assets are optional or required but generation proceeds, carry the normalized asset rows into `spec.md` `## Asset Brief`. `prod.md` may reference asset IDs and fallback behavior, but should not include raw image prompts.
9. If generation proceeds, carry `canonical_mechanic` into `tag_block.yaml` `activity_signature.mechanic`.

### Step 1.5: Load entity mapping (when required or available)

Read mapping YAML when `mapping=` is specified, when the adaptation brief has `input_mode=mapping_informed`, or when the package claims entity-specific mapping grounding. Do not require mapping for `concept_only` or `parameterized` briefs that use runtime placeholders.

If mapping is required:

1. Read `MAPPING_ROOT/_index.yaml` and find the entity_id.
2. Read the mapped YAML file and locate the entity block.
3. Extract:
   - target-tier `primary_theme` and `secondary_themes`
   - target-tier `primary_key_concepts` and `secondary_key_concepts`
   - `candidate_related_concepts`
   - `tier_guidance.[target_tier].dimensions`
4. Select 2-3 anchor dimensions per `entity_guidance.md` section 6:
   - Cat1: engagement-first plus one physical anchor.
   - Cat5: physical-first plus one engagement anchor.
5. Select Key Concepts, IB theme, and Related Concepts per `entity_guidance.md`.
6. If no mapping is present and the brief is `parameterized`, keep focal attributes and entity values as runtime placeholders.
7. If no mapping is present and the brief is `concept_only`, do not invent mapping-derived facts or Key Concepts.

### Step 2: Compose the scaffold

Read `templates.md` in layered order:

1. Template 0 reference.
2. Mechanic adapter matching `canonical_mechanic`.
3. Cat1 or Cat5 category modifier.
4. Pillar/style scaffold selected by the adaptation brief.

Use the composed scaffold as the activity's beat structure. Do not use the retired "Template A / Template B" split. If mapping-informed, ground creative variables in the selected dimensions and mapping attributes. If parameterized, use stable placeholders. If concept-only, avoid entity-specific claims.

The child's actual repeated action must match `canonical_mechanic`. Keep the selected `game_style` coherent with the mechanic, but do not let style override the requested action. If scaffold fit is weak, disclose it in `spec.md` or stop before generation.

### Step 3: Generate the migrated activity package

Create a complete `activities/<activity_id>/` package with exactly five files:

```
activities/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

Rules:

- `spec.md`: author/reviewer reference with premise, target, rationale, selection trigger, pillar/game style, optional `## Adaptation Rationale`, optional `## Asset Brief`, and `## Self-Evaluation Scorecard`.
- `prod.md`: runtime prompt guidance with Basic Info, Activity Overview, and full Interaction Flow. It must not contain a scorecard.
- `tag_block.yaml`: structured metadata matching `activities/_schema/tag_block.schema.json`.
- `recap.template.yaml`: child recap payload using the same focal attribute, role/badge, and next-step direction.
- `dashboard.template.yaml`: parent dashboard fragment using the same focal attribute and progression axis.

Runtime completeness rule:

- Every Step 3 round in `prod.md` must be fully expanded with AI dialogue, child response branches, AI follow-up branches, and screen state.
- Never write "same structure," "later rounds follow," "AI gives a riddle," or one-line summaries in `activities/*/prod.md`.
- If `start=warm+cold`, document the bridge logic in `spec.md`; the runtime `prod.md` should still have a single converged Step 1 unless the assignment explicitly asks for both starts at runtime.
- Do not generate image files as part of this loop. When an activity uses AI-generated or displayed images, author the dependency in `spec.md` `## Asset Brief` and reference the stable `asset_id` from the relevant screen description in `prod.md`.

### Step 4: Self-evaluate and repair

Run through all 10 rubric dimensions from `program.md` Phase 3 against the actual package files. If any dimension FAILS:

1. Identify the specific issue.
2. Fix the relevant package file(s).
3. Re-evaluate.
4. Repeat until all dimensions PASS.

Dimension 8 only applies to mapping-informed designs. Score as N/A if no mapping. Dimensions 9 and 10 always apply. Dimension 10 checks mechanic fidelity + scaffold honesty, even though the legacy log column name remains `d10_pillar_fidelity`.

### Step 4.5: Independent scorecard review

Spawn a separate reviewer agent to independently check the same 10 dimensions against the completed package files before finalizing `spec.md`.

Reviewer instructions:

- Read `program.md` Phase 0 and Phase 3, the adaptation brief / `spec.md` `## Adaptation Rationale` when present, and the generated `activities/<activity_id>/` package.
- Read `templates.md`, `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`.
- If the assignment has `mapping=`, also read the relevant mapping source, `entity_guidance.md`, and `conversation_bridge.md`.
- Evaluate the package files directly, not the authoring agent's claimed scorecard.
- Return PASS/FAIL/N/A for each dimension with brief evidence and concrete file/section references for any issue. For Dimension 10, explicitly confirm that Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic` and the adaptation brief's `canonical_mechanic` when present. When assets are referenced, also confirm the package contains a coherent `## Asset Brief`, that every referenced `asset_id` is defined, and that required assets have prompts/source, use steps, display behavior, and fallback behavior.

If the reviewer flags any FAIL or credible uncertainty, fix the package, rerun the author self-evaluation, and spawn a fresh independent review. Only finalize the `## Self-Evaluation Scorecard`, append `results.tsv`, and mark the assignment complete after both the author check and independent reviewer check pass.

### Step 5: Package checks

Before logging or committing, verify:

- `activities/<activity_id>/` contains exactly the five required files.
- Directory name equals `tag_block.yaml` `activity_id`.
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
- Every `prod.md` Step 3 round is fully expanded; no condensed-round placeholders remain.
- `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
- Concept-led packages with `generate_with_assumptions` include `spec.md` `## Adaptation Rationale`.
- Packages whose adaptation brief has `asset_dependency.policy` other than `no_assets` include `spec.md` `## Asset Brief`.
- Every `asset_id` referenced in `prod.md` is defined in `spec.md` `## Asset Brief`.
- Required or optional asset rows include `asset_type`, requiredness, generation timing, use step, display behavior, and fallback behavior; generated assets also include a directly usable `prompt_en`, while existing/displayed assets include a `source` or approved source description.
- `prod.md` Step 3's repeated child action matches `tag_block.yaml` `activity_signature.mechanic`.
- `prod.md` contains zero `## Self-Evaluation Scorecard` sections.

### Step 6: Log the result

Append a row to `results.tsv`:

```
[assignment]\t[entity]\t[category]\t[tier]\t[pillar]\t[style]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F/N]\t[P/F]\t[P/F]\t[activity_id]\t[ISO timestamp]
```

Column order: assignment, entity, category, tier, pillar, style, status, d1_tech, d2_hook_transition, d3_edge, d4_ib, d5_tier, d6_dialogue, d7_screen, d8_mapping, d9_game_feel, d10_pillar_fidelity, filename, timestamp.

For `d8_mapping`: use P, F, or N. `d9_game_feel` and `d10_pillar_fidelity` are always P or F. The `d10_pillar_fidelity` column is retained for log compatibility and now records Dimension 10 Mechanic Fidelity + Scaffold Honesty.

### Step 6.5: Update run provenance

For every generated package:

1. Append the `activity_id` to `runs/<run_id>/generated_activity_ids.txt`.
2. Add or update a `generated_activities` entry in `runs/<run_id>/run_manifest.yaml`:

```yaml
- assignment_index: <ordinal from assignment_snapshot.md>
  assignment: "<original assignment row>"
  activity_id: <activity_id>
  activity_path: activities/<activity_id>
  adaptation_brief: runs/<run_id>/adaptation_briefs/<ordinal>_<assignment_slug>.yaml # omit when no Phase 0 brief was produced
  results_tsv_row: true
  status: PASS
```

3. Add reviewer evidence, repair notes, or residual risks to `runs/<run_id>/review_notes.md` when useful.
4. Verify `runs/<run_id>/run_manifest.yaml` has an entry for the generated activity and `runs/<run_id>/generated_activity_ids.txt` includes the generated `activity_id`.

For blocked assignments, keep the entry under `blocked_assignments` and do not append `results.tsv`.

### Step 7: Mark assignment complete

In `assignments.md`, change `- [ ]` to `- [x]` for this assignment.

### Step 8: Commit

```bash
git add activities/<activity_id>/ runs/<run_id>/ results.tsv assignments.md
git commit -m "Design: <activity_id> - ALL PASS"
```

### Step 9: Next assignment

Move to the next `- [ ]` assignment. If none remain, set `run_manifest.yaml status: completed`, fill `completed_at`, update the summary counts, and say: "All assignments complete. [N] activity packages generated. See results.tsv and runs/<run_id>/run_manifest.yaml for summary."

## Legacy transform workflow

`transform.md` and `transform_run.md` are retained only for the old `designs/*_spec.md` to `designs/*_prod.md` workflow. Do not use them for migrated `activities/*/prod.md` files.

## Important Rules

- Never skip steps. Every activity package must be complete before saving.
- Never abbreviate later rounds because "they follow the same pattern." Each runtime round is fully independent.
- Never put a scorecard in `prod.md`.
- Always put the scorecard in `spec.md`.
- Keep `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` aligned with the runtime flow.
- Commit after every completed package unless the user explicitly asks to batch commits.
- Quality over speed. Take as many self-evaluation rounds as needed.
