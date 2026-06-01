# WonderLens AI Validation

Run: `20260601_155917_full_pass_agentic_tsv`
WonderLens AI repo: `/Users/pharrelly/codebase/gitlab/wonderlens-ai`
Branch: `main`
Artifact destination: `.artifacts/full-pass-agentic/activities`

## Verdict

Current verdict: **runtime generation/load pass**

WonderLens AI rejected the initial runtime generation because 29 `prod.md` files
contained generic leakage phrases blocked by its runtime generator. The scoped
repair in commit `859b434` removed those runtime-facing generic phrases while
preserving package intent. After the repair, runtime generation succeeded for
all 40 packages with zero warnings.

## Checks Run

```bash
rm -rf .artifacts/full-pass-agentic
mkdir -p .artifacts/full-pass-agentic
uv run python scripts/generate_activity_runtime.py \
  --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/full-pass-agentic-run/runs/20260601_155917_full_pass_agentic_tsv/activity_packages \
  --dest .artifacts/full-pass-agentic/activities \
  --write \
  --force \
  --report-json .artifacts/full-pass-agentic/runtime-report.json
```

Result: all 40 packages reported `OK ... warnings=0`.

```bash
uv run pytest \
  tests/unit/activity/test_activity_package_models.py \
  tests/unit/activity/test_activity_package_loader.py \
  tests/unit/activity/test_activity_package_adapter.py \
  tests/unit/activity/test_runtime_generator.py \
  tests/unit/scripts/test_generate_activity_runtime.py -q
```

Result: `51 passed in 0.39s`

```bash
WONDERLENS_ACTIVITY_PACKAGE_DIR="$PWD/.artifacts/full-pass-agentic/activities" \
  uv run python - <<'PY'
from app.modules.activity.packages.loader import load_activity_packages
packages = load_activity_packages()
print('loaded_packages', len(packages))
print('first', packages[0].activity_id)
print('last', packages[-1].activity_id)
unsupported=sum(1 for p in packages if p.demo_support and p.demo_support.demo_support.status == 'unsupported')
degraded=sum(1 for p in packages if p.demo_support and p.demo_support.demo_support.status == 'degraded')
supported=sum(1 for p in packages if p.demo_support and p.demo_support.demo_support.status == 'supported')
print('support_counts', {'supported': supported, 'degraded': degraded, 'unsupported': unsupported})
missing=[p.activity_id for p in packages if p.package_readiness.required_missing_asset_ids]
print('missing_required_assets', missing)
PY
```

Result:

```text
loaded_packages 40
first concept_animal_sound_motion_voice
last concept_would_you_rather_compare
support_counts {'supported': 16, 'degraded': 9, 'unsupported': 15}
missing_required_assets []
```

## Dialogue Quality Status

The runtime-generation blocker is fixed and the package loader accepts the
generated runtime artifacts. A live multi-strategy WonderLens AI dialogue run is
still pending for the full completion gate.

## Local Artifact Policy

All WonderLens AI generated runtime artifacts stayed under `.artifacts/` in the
WonderLens AI repo. That repo remained clean after validation.

