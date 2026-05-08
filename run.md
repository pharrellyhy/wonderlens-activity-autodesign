# Run Instructions - Autonomous Activity Package Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.

## Setup (one-time, do this first)

1. Read `program.md` fully - constraints, migrated package format, rubric, and seed exemplars.
2. Read `templates.md` fully - Template 0 reference, pillar overlays, and Cat1/Cat5 category modifiers.
3. Read `docs/game_styles.md` - game style taxonomy reference.
4. Read `activities/README.md` - required five-file package layout.
5. Read `activities/_schema/tag_block.schema.json` and `docs/activity_vocabulary.md` - tag-block schema and current enum vocabulary.
6. Read `docs/activity_tag_block_usage.md` and `docs/activity_tag_block_progression_guide.md` - field ownership, recap/dashboard usage, and progression guidance.
7. Read `entity_guidance.md` and `conversation_bridge.md` when an assignment is mapping-informed or requests warm/cold bridge handling.
8. Read `assignments.md` - work queue.
9. Verify `activities/` exists with `_schema/tag_block.schema.json`.
10. Verify `results.tsv` exists and has the current header. If it is missing, create it with this header:

```
assignment	entity	category	tier	pillar	style	status	d1_tech	d2_hook_transition	d3_edge	d4_ib	d5_tier	d6_dialogue	d7_screen	d8_mapping	d9_game_feel	d10_pillar_fidelity	filename	timestamp
```

11. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Starting activity package loop."

## The Loop (repeat for every uncompleted assignment)

For each assignment in `assignments.md` that is marked `- [ ]` (not yet completed):

### Step 1: Parse the assignment

Extract: entity, category, tier, mechanic (if provided), pillar (if provided), style (if provided), scene (if provided), mapping (if provided), start type (if provided), output activity_id (if provided). If tier is not specified, infer it per `program.md` rules. If mechanic is specified, treat it as the primary child-action requirement and carry it into `activity_signature.mechanic`. If pillar/style is not specified, infer per `program.md` section 1.6 using mechanic first, then entity affordances, category, and pillar fit. If scene is not specified, invent one.

### Step 1.5: Load entity mapping (if `mapping=` is specified)

1. Read `data/mappings_dev20_0318/_index.yaml` and find the entity_id.
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
6. If no `mapping=` parameter is present, skip this step.

### Step 2: Compose the scaffold

Read `templates.md` in layered order:

1. Template 0 reference.
2. Assigned pillar overlay.
3. Cat1 or Cat5 category modifier.

Use the composed scaffold as the activity's beat structure. Do not use the retired "Template A / Template B" split. If mapping-informed, ground creative variables in the selected dimensions and mapping attributes. If not mapping-informed, brainstorm fresh variables constrained by the pillar overlay.

If the assignment provided `mechanic=`, adapt the scaffold so the child's actual repeated action matches that mechanic. Keep the selected `game_style` coherent with the mechanic, but do not let style override the requested action.

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

- `spec.md`: author/reviewer reference with premise, target, rationale, selection trigger, pillar/game style, and `## Self-Evaluation Scorecard`.
- `prod.md`: runtime prompt guidance with Basic Info, Activity Overview, and full Interaction Flow. It must not contain a scorecard.
- `tag_block.yaml`: structured metadata matching `activities/_schema/tag_block.schema.json`.
- `recap.template.yaml`: child recap payload using the same focal attribute, role/badge, and next-step direction.
- `dashboard.template.yaml`: parent dashboard fragment using the same focal attribute and progression axis.

Runtime completeness rule:

- Every Step 3 round in `prod.md` must be fully expanded with AI dialogue, child response branches, AI follow-up branches, and screen state.
- Never write "same structure," "later rounds follow," "AI gives a riddle," or one-line summaries in `activities/*/prod.md`.
- If `start=warm+cold`, document the bridge logic in `spec.md`; the runtime `prod.md` should still have a single converged Step 1 unless the assignment explicitly asks for both starts at runtime.

### Step 4: Self-evaluate and repair

Run through all 10 rubric dimensions from `program.md` Phase 3 against the actual package files. If any dimension FAILS:

1. Identify the specific issue.
2. Fix the relevant package file(s).
3. Re-evaluate.
4. Repeat until all dimensions PASS.

Dimension 8 only applies to mapping-informed designs. Score as N/A if no mapping. Dimensions 9 and 10 always apply.

### Step 4.5: Independent scorecard review

Spawn a separate reviewer agent to independently check the same 10 dimensions against the completed package files before finalizing `spec.md`.

Reviewer instructions:

- Read `program.md` Phase 3 and the generated `activities/<activity_id>/` package.
- Read `templates.md`, `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`.
- If the assignment has `mapping=`, also read the relevant mapping source, `entity_guidance.md`, and `conversation_bridge.md`.
- Evaluate the package files directly, not the authoring agent's claimed scorecard.
- Return PASS/FAIL/N/A for each dimension with brief evidence and concrete file/section references for any issue.

If the reviewer flags any FAIL or credible uncertainty, fix the package, rerun the author self-evaluation, and spawn a fresh independent review. Only finalize the `## Self-Evaluation Scorecard`, append `results.tsv`, and mark the assignment complete after both the author check and independent reviewer check pass.

### Step 5: Package checks

Before logging or committing, verify:

- `activities/<activity_id>/` contains exactly the five required files.
- Directory name equals `tag_block.yaml` `activity_id`.
- `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
- Every `prod.md` Step 3 round is fully expanded; no condensed-round placeholders remain.
- `spec.md` contains exactly one `## Self-Evaluation Scorecard`.
- `prod.md` contains zero `## Self-Evaluation Scorecard` sections.

### Step 6: Log the result

Append a row to `results.tsv`:

```
[assignment]\t[entity]\t[category]\t[tier]\t[pillar]\t[style]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F/N]\t[P/F]\t[P/F]\t[activity_id]\t[ISO timestamp]
```

Column order: assignment, entity, category, tier, pillar, style, status, d1_tech, d2_hook_transition, d3_edge, d4_ib, d5_tier, d6_dialogue, d7_screen, d8_mapping, d9_game_feel, d10_pillar_fidelity, filename, timestamp.

For `d8_mapping`: use P, F, or N. `d9_game_feel` and `d10_pillar_fidelity` are always P or F.

### Step 7: Mark assignment complete

In `assignments.md`, change `- [ ]` to `- [x]` for this assignment.

### Step 8: Commit

```bash
git add activities/<activity_id>/ results.tsv assignments.md
git commit -m "Design: <activity_id> - ALL PASS"
```

### Step 9: Next assignment

Move to the next `- [ ]` assignment. If none remain, say: "All assignments complete. [N] activity packages generated. See results.tsv for summary."

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
