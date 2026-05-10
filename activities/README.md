# Activities

Per-game directory layout. Each subdirectory describes one activity in 5 files.

## Layout

```
activities/
├── _schema/
│   └── tag_block.schema.json        # JSON Schema for tag_block.yaml
├── README.md                         # this file
└── <activity_id>/
    ├── spec.md                       # authoring intent: premise, target, rationale, selection trigger, optional asset brief
    ├── prod.md                       # runtime dialogue + step instructions
    ├── tag_block.yaml                # structured metadata (validated against _schema/tag_block.schema.json)
    ├── recap.template.yaml           # child recap payload shape (runtime-rendered)
    └── dashboard.template.yaml       # parent dashboard fragment shape (runtime-rendered)
```

The directory name MUST equal the `activity_id` inside that dir's `tag_block.yaml`.

## File roles

| File | Audience | Format | Runtime role |
|---|---|---|---|
| `spec.md` | authors, reviewers | Markdown prose | design reference; not loaded by runtime; owns the self-evaluation scorecard and optional `## Asset Brief` |
| `prod.md` | authors, LLM prompt composer | Markdown prose | quoted into prompts; beat-level guidance; all runtime rounds fully expanded; references asset IDs only |
| `tag_block.yaml` | matcher, selector | YAML | machine-readable metadata; schema-validated |
| `recap.template.yaml` | recap renderer | YAML with `{placeholders}` | per-session payload emitted at activity end |
| `dashboard.template.yaml` | parent dashboard roller | YAML with `{placeholders}` | per-session fragment merged into device rollup |

## Runtime completeness invariants

- `prod.md` must not contain `## Self-Evaluation Scorecard`.
- `spec.md` must contain exactly one `## Self-Evaluation Scorecard`.
- If an activity references AI-generated images, prebuilt card sets, line art, icons, overlays, or displayed reference images, `spec.md` must include `## Asset Brief` before the scorecard.
- `prod.md` may reference stable `asset_id` values and fallback behavior, but must not include raw image-generation prompts.
- Every Step 3 round in `prod.md` must be fully executable: AI dialogue, child response branches, AI follow-up branches, and screen state.
- Steps 1, 2, 4, and 5 must also be executable enough for the runtime prompt composer: concrete AI dialogue, branch-specific follow-ups where applicable, and specific screen states.
- Do not use condensed placeholders such as "same structure," "AI gives a riddle," "later rounds follow," or one-line summaries in migrated `prod.md` files.
- Do not treat compact migrated files as a lower-detail target. `spec.md` must preserve decision-useful design rationale, and `prod.md` must preserve concrete game feel, progress, payoff, and source-promise behavior.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` must exactly equal `tag_block.yaml` `activity_signature.focal_attribute`.

## Asset brief invariant

`## Asset Brief` is an authoring dependency record, not a sixth package file. Each asset row should define:

| Field | Purpose |
|---|---|
| `asset_id` | Stable ID used by `prod.md` screen descriptions. |
| `asset_type` | `reference_image`, `character_image`, `scene_background`, `line_art`, `card_set`, `icon`, or `ui_overlay`. |
| `requiredness` | `required`, `optional`, or `fallback`. |
| `generation_timing` | `pre_generated`, `runtime_generated`, `display_existing`, or `none`. |
| `use_step` | Exact step/round where the asset appears. |
| `prompt_en` | Direct English generation prompt for generated assets. |
| `source` | Existing asset library, approved reference set, or source description when no generation prompt is needed. |
| `display_behavior` | How the runtime should present it. |
| `fallback_behavior` | What runtime does if it is missing. |
| `safety_constraints` | Visual safety and content constraints. |

Current package generation does not create image files. A separate asset pipeline may later consume the prompts or source descriptions.

## Canonical vocabulary

The three closed enums in `tag_block.yaml activity_signature` — `observation_angle` (12), `mechanic` (12), `entity_role` (4) — are defined in [`docs/activity_vocabulary.md`](../docs/activity_vocabulary.md). The schema's enum lists must stay in sync with that doc; drift is CI-blocked.

For field ownership and authoring guidance, use [`docs/activity_tag_block_usage.md`](../docs/activity_tag_block_usage.md). It separates matcher-facing, runtime-presentation, child-recap, and parent-dashboard fields.

For a full tag-block plus progression-algorithm reference, use [`docs/activity_tag_block_progression_guide.md`](../docs/activity_tag_block_progression_guide.md) or the Chinese companion [`docs/activity_tag_block_progression_guide_cn.md`](../docs/activity_tag_block_progression_guide_cn.md). For workflow diagrams, use [`docs/activity_matcher_progression_workflows.md`](../docs/activity_matcher_progression_workflows.md) or the Chinese companion [`docs/activity_matcher_progression_workflows_cn.md`](../docs/activity_matcher_progression_workflows_cn.md).

## Validation

Validate all `tag_block.yaml` files against the schema:

```bash
python3 -c "
import json, yaml, pathlib, sys
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
ok = True
for p in sorted(pathlib.Path('activities').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK  ' if not errs else 'FAIL'), p)
    for e in errs:
        ok = False
        print(f'  {list(e.absolute_path)}: {e.message}')
sys.exit(0 if ok else 1)
"
```

Requires `pip install jsonschema pyyaml`.

## Current V1 coverage

5 games migrated to this layout; 19 games remain on the legacy single-`.md` layout under `designs/`. The backend loader supports both during migration. Follow-up PRs migrate the rest.

## Cross-repo notes

Consumer repos (`wonderlens-ai`, `wonderlens-activity-fullstack-demo`) mirror this schema's enums in code. Additions to `docs/activity_vocabulary.md` require matching changes in both consumer repos; see the `## Versioning` section of that doc.
