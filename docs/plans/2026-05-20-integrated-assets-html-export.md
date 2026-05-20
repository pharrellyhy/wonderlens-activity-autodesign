# Integrated Assets HTML Export Implementation Plan

> **For implementer:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Integrate the 12 generated prebuilt asset contact sheets into their corresponding Batch 5 activity packages and export those 12 asset-backed activities as 12 separate static HTML files.

**Architecture:** Keep the five-file activity package contract stable. Add a run-local asset binding manifest that joins package asset IDs to generated image files, then generate self-contained per-activity HTML exports from the binding manifest, package files, and asset metadata. The exports are review/runtime-preview artifacts, not a replacement for `spec.md`, `prod.md`, or the live WonderLens runtime.

**Python environment:** Script commands require PyYAML. In this local worktree, run them through the PyYAML-capable pyenv interpreter:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3
```

**Tech Stack:** Python 3 standard library, PyYAML, existing run-local Markdown/YAML package files, static HTML/CSS with embedded base64 PNG images, no external CSS/JS/fonts/CDNs.

---

## Context

The current pilot assets live under:

- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/asset_manifest.yaml`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/contact_sheet.png`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/asset.meta.yaml`
- `runs/20260512_172135_batch5_unblocked/generated_assets_pilot/<activity_id>/<asset_id>/contact_sheet.prompt.md`

The corresponding activities already exist under:

- `runs/20260512_172135_batch5_unblocked/activity_packages/<activity_id>/`

The 12 pilot activities are:

| activity_id | asset_id |
|---|---|
| `concept_phoneme_hunt_collect` | `phoneme_letter_card_01` |
| `concept_partial_reveal_deduce` | `partial_reveal_cards_01` |
| `concept_animal_sound_motion_voice` | `animal_sound_cards_01` |
| `concept_word_echo_remember` | `word_echo_cards_01` |
| `concept_emotion_reader_care` | `emotion_expression_cards_01` |
| `concept_constellation_star_count_enumerate` | `constellation_count_cards_01` |
| `concept_career_decision_decide` | `career_portrait_cards_01` |
| `concept_vegetable_sort_sort` | `vegetable_sort_cards_01` |
| `concept_travel_planner_predict` | `travel_planning_cards_01` |
| `concept_guided_drawing_probe` | `guided_drawing_step_cards_01` |
| `concept_story_unlock_probe` | `story_unlock_cards_01` |
| `concept_recognition_pop_probe` | `recognition_challenge_cards_01` |

## Design Choice

Use a run-local binding layer.

Approaches considered:

- Modify each `prod.md` and `spec.md` to include concrete PNG paths. This makes the package files easier to inspect but pollutes the canonical prompt package with run-specific artifact paths.
- Create a run-local `integrated_assets/asset_bindings.yaml` and generate HTML exports from it. This is recommended because it preserves package stability, gives downstream consumers one machine-readable bridge, and can be regenerated safely.
- Build a runtime app integration first. This is premature because the pilot only has contact-sheet images, not sliced final runtime cards or a consumer-side asset API.

The binding manifest is the contract between asset generation and per-activity HTML export.

## Output Shape

Create:

- `runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_exports/export_manifest.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_phoneme_hunt_collect.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_partial_reveal_deduce.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_animal_sound_motion_voice.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_word_echo_remember.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_emotion_reader_care.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_constellation_star_count_enumerate.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_career_decision_decide.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_vegetable_sort_sort.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_travel_planner_predict.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_guided_drawing_probe.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_story_unlock_probe.html`
- `runs/20260512_172135_batch5_unblocked/activity_exports/concept_recognition_pop_probe.html`

Each HTML file is self-contained and embeds its `contact_sheet.png` as a base64 data URI. This makes the 12 exports portable and avoids broken relative image paths when a reviewer opens one file directly.

## Binding Manifest Schema

Write `integrated_assets/asset_bindings.yaml` with this shape:

```yaml
run_id: 20260512_172135_batch5_unblocked
artifact_kind: integrated_prebuilt_asset_bindings
source_asset_manifest: generated_assets_pilot/asset_manifest.yaml
created_at: "2026-05-20T00:00:00+08:00"
activity_count: 12
asset_count: 12
entries:
  - activity_id: concept_partial_reveal_deduce
    activity_name: Partial Reveal Guess
    asset_id: partial_reveal_cards_01
    asset_type: card_set
    requiredness: required
    generation_timing: pre_generated
    integration_status: integrated
    package_path: activity_packages/concept_partial_reveal_deduce
    spec_path: activity_packages/concept_partial_reveal_deduce/spec.md
    prod_path: activity_packages/concept_partial_reveal_deduce/prod.md
    image_path: generated_assets_pilot/concept_partial_reveal_deduce/partial_reveal_cards_01/contact_sheet.png
    meta_path: generated_assets_pilot/concept_partial_reveal_deduce/partial_reveal_cards_01/asset.meta.yaml
    prompt_path: generated_assets_pilot/concept_partial_reveal_deduce/partial_reveal_cards_01/contact_sheet.prompt.md
    use_step: prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4
    display_location: center_card_area
    display_behavior: Show one partial-reveal card full screen each round.
    fallback_behavior: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.
    validation:
      package_exists: true
      image_exists: true
      metadata_exists: true
      prompt_exists: true
      run_manifest_asset_usage_matches: true
      spec_mentions_asset_id: true
      prod_mentions_asset_id: true
      requiredness_matches: true
      use_step_matches: true
      display_location_matches: true
```

Validation must fail if any `validation` value is false.

## HTML Export Content

Each per-activity HTML page must include:

- Activity title and `activity_id`.
- Mechanic, category, tier, pillar, game style, asset policy, and reviewer status.
- Embedded contact sheet image.
- Asset ID, asset type, requiredness, generation timing, use steps, display location, display behavior, fallback behavior, and safety constraints.
- Brief description, design highlight, typical scenario, and runtime flow from `prod.md`.
- Asset brief/timeline summary from `spec.md` or `run_manifest.yaml` asset usage.
- Scorecard summary and all 10 scorecard rows from `spec.md`.
- File provenance links as plain relative paths for the package, asset metadata, prompt, and source contact sheet image.
- A source snapshot section with collapsible `spec.md`, `prod.md`, `asset.meta.yaml`, and `contact_sheet.prompt.md` text.

The page must not claim to be a live runtime simulator. Use labels such as `Static Activity Export`, `Integrated Prebuilt Asset`, and `Fallback Contract`.

## Task 1: Add Asset Integration Script

**Files:**

- Create: `scripts/integrate_generated_assets.py`
- Modify: none initially
- Generated by command: `runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml`

**Step 1: Confirm the script does not exist**

Run:

```bash
test ! -f scripts/integrate_generated_assets.py
```

Expected: exit code 0.

**Step 2: Create `scripts/integrate_generated_assets.py`**

Implement a CLI:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py runs/<run_id>
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/<run_id>
```

Core structure:

```python
#!/usr/bin/env python3
"""Bind generated prebuilt asset files to run-local activity packages."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


PACKAGE_FILES = ("spec.md", "prod.md", "tag_block.yaml", "recap.template.yaml", "dashboard.template.yaml")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def rel_to_run(run_dir: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else run_dir / path
```

Required functions:

- `generated_activities(run_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]`
- `asset_entries(asset_manifest: dict[str, Any]) -> list[dict[str, Any]]`
- `find_manifest_asset_usage(activity_entry: dict[str, Any], asset_id: str) -> dict[str, Any]`
- `activity_title(run_dir: Path, package_path: str, fallback: str) -> str`
- `build_binding(run_dir: Path, activity_entry: dict[str, Any], asset_entry: dict[str, Any]) -> dict[str, Any]`
- `validate_binding(run_dir: Path, binding: dict[str, Any]) -> list[str]`
- `build_manifest(run_dir: Path) -> dict[str, Any]`
- `validate_manifest(run_dir: Path, manifest: dict[str, Any]) -> list[str]`
- `main() -> None`

`build_binding()` must join data in this priority:

1. `run_manifest.yaml` `outputs.generated_activities[*].asset_usage[*]`
2. `generated_assets_pilot/<activity_id>/<asset_id>/asset.meta.yaml`
3. `generated_assets_pilot/asset_manifest.yaml`

Do not infer an asset if the `asset_id` is absent from the activity's `asset_usage`.

**Step 3: Generate the binding manifest**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py runs/20260512_172135_batch5_unblocked
```

Expected output:

```text
Integrated 12 generated assets for 12 activities.
Wrote runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml
```

**Step 4: Validate the binding manifest**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/20260512_172135_batch5_unblocked
```

Expected output:

```text
PASS integrated asset bindings: 12 assets, 12 activities.
```

**Step 5: Commit**

```bash
git add scripts/integrate_generated_assets.py runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml
git commit -m "feat(assets): bind pilot assets"
```

## Task 2: Add Per-Activity HTML Exporter

**Files:**

- Create: `scripts/export_activity_html.py`
- Generated by command: `runs/20260512_172135_batch5_unblocked/activity_exports/*.html`
- Generated by command: `runs/20260512_172135_batch5_unblocked/activity_exports/export_manifest.yaml`

**Step 1: Confirm the script does not exist**

Run:

```bash
test ! -f scripts/export_activity_html.py
```

Expected: exit code 0.

**Step 2: Create `scripts/export_activity_html.py`**

Implement a CLI:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py runs/<run_id>
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/<run_id>
```

The exporter may import parsing helpers from `scripts/generate_run_review.py`:

```python
from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_run_review as review  # noqa: E402
```

Required functions:

- `load_yaml(path: Path) -> dict[str, Any]`
- `read_text(path: Path) -> str`
- `data_uri(path: Path) -> str`
- `html_escape(value: Any) -> str`
- `activity_slug(value: str) -> str`
- `run_manifest_entry_by_activity(run_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]`
- `collect_activity_package(repo_root: Path, run_dir: Path, activity_entry: dict[str, Any]) -> dict[str, Any]`
- `render_runtime_flow(package: dict[str, Any]) -> str`
- `render_scorecard(package: dict[str, Any]) -> str`
- `render_source_snapshot(title: str, text: str) -> str`
- `render_activity_html(run_dir: Path, binding: dict[str, Any], package: dict[str, Any]) -> str`
- `write_exports(run_dir: Path) -> dict[str, Any]`
- `validate_exports(run_dir: Path) -> list[str]`
- `main() -> None`

Use `review.collect_package(repo_root, run_dir, activity_entry, "generated")` to avoid duplicating package parsing. Use `review.runtime_map(package)`, `review.runtime_sections(package)`, or direct `package["runtime_beats"]` rendering if the existing functions are too dashboard-specific.

**Step 3: Use this HTML skeleton**

```python
def render_activity_html(run_dir: Path, binding: dict[str, Any], package: dict[str, Any]) -> str:
    image_uri = data_uri(run_dir / binding["image_path"])
    spec_text = read_text(run_dir / binding["spec_path"])
    prod_text = read_text(run_dir / binding["prod_path"])
    meta_text = read_text(run_dir / binding["meta_path"])
    prompt_text = read_text(run_dir / binding["prompt_path"])
    title = html_escape(package["activity_name"])
    activity_id = html_escape(binding["activity_id"])
    asset_id = html_escape(binding["asset_id"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} - Static Activity Export</title>
  <style>{BASE_CSS}</style>
</head>
<body>
  <main class="page">
    <header class="hero">
      <p class="eyebrow">WonderLens Static Activity Export</p>
      <h1>{title}</h1>
      <p class="subline">{activity_id} - integrated asset {asset_id}</p>
    </header>
    <section class="layout">
      <figure class="asset-panel">
        <img src="{image_uri}" alt="Contact sheet for {asset_id}">
        <figcaption>{asset_id} - {html_escape(binding.get("asset_type"))}</figcaption>
      </figure>
      <article class="summary-panel">
        {render_metadata(package, binding)}
        {render_asset_contract(binding)}
      </article>
    </section>
    {render_overview(package)}
    {render_runtime_flow(package)}
    {render_scorecard(package)}
    <section class="source-panel">
      <h2>Source Files</h2>
      {render_source_snapshot("spec.md", spec_text)}
      {render_source_snapshot("prod.md", prod_text)}
      {render_source_snapshot("asset.meta.yaml", meta_text)}
      {render_source_snapshot("contact_sheet.prompt.md", prompt_text)}
    </section>
  </main>
</body>
</html>
"""
```

Keep CSS inline. Use a compact light product-dashboard style consistent with `review_dashboard.md`: warm paper background, slate text, restrained indigo accent, asset chips, and no external dependencies.

**Step 4: Generate the 12 HTML exports**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py runs/20260512_172135_batch5_unblocked
```

Expected output:

```text
Exported 12 activity HTML files.
Wrote runs/20260512_172135_batch5_unblocked/activity_exports/export_manifest.yaml
```

**Step 5: Validate the 12 HTML exports**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/20260512_172135_batch5_unblocked
```

Expected output:

```text
PASS activity HTML exports: 12 files.
```

Validation must check:

- `export_manifest.yaml` exists and lists 12 exports.
- Every `html_path` exists.
- Every HTML contains `<!doctype html>`, `<html lang="en">`, the `activity_id`, the `asset_id`, and `data:image/png;base64,`.
- No HTML contains external `http://`, `https://`, CDN references, or unresolved placeholders such as `{{`.
- Every export references the same `asset_id` and `image_path` as `integrated_assets/asset_bindings.yaml`.

**Step 6: Commit**

```bash
git add scripts/export_activity_html.py runs/20260512_172135_batch5_unblocked/activity_exports
git commit -m "feat(exports): add activity HTMLs"
```

## Task 3: Wire Provenance Into Run Manifest

**Files:**

- Modify: `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`

**Step 1: Add output references**

Add under `outputs`:

```yaml
  integrated_asset_bindings: runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml
  activity_html_exports: runs/20260512_172135_batch5_unblocked/activity_exports
  activity_html_export_manifest: runs/20260512_172135_batch5_unblocked/activity_exports/export_manifest.yaml
```

Add under `summary`:

```yaml
  integrated_asset_count: 12
  activity_html_export_count: 12
```

If the manifest already has a `checks` list, append the four commands from Tasks 1 and 2 with result `PASS`. If it does not have one, add a `checks` list near the end.

**Step 2: Validate run dashboard still builds**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py runs/20260512_172135_batch5_unblocked
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
```

Expected: both commands pass. The regenerated `review.html` should continue to show the generated asset pilot section.

**Step 3: Commit**

```bash
git add runs/20260512_172135_batch5_unblocked/run_manifest.yaml runs/20260512_172135_batch5_unblocked/review.html
git commit -m "chore(run): record asset exports"
```

## Task 4: Update Workflow Docs

**Files:**

- Modify: `review_dashboard.md`
- Modify: `runs/README.md`
- Modify: `HANDOFF.md`

**Step 1: Update `review_dashboard.md`**

Add the integration/export commands after the generated prebuilt contact-sheet step:

```markdown
- Integrate generated prebuilt assets:
  `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py runs/<run_id>`
- Validate integrated prebuilt assets:
  `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/<run_id>`
- Export per-activity static HTML files:
  `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py runs/<run_id>`
- Validate per-activity static HTML files:
  `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/<run_id>`
```

Clarify that per-activity HTML exports are derived artifacts and should not be hand-edited.

**Step 2: Update `runs/README.md`**

Document the new optional run-local directories:

```markdown
- `integrated_assets/` - run-local bindings between package asset IDs and generated asset files.
- `activity_exports/` - one self-contained static HTML export per integrated activity, plus `export_manifest.yaml`.
```

**Step 3: Update `HANDOFF.md`**

Record:

- 12 pilot assets integrated.
- 12 self-contained activity HTML exports generated.
- Validation commands and results.
- Remaining risk: contact sheets are review/runtime-preview assets, not sliced final runtime cards.

**Step 4: Commit**

```bash
git add review_dashboard.md runs/README.md HANDOFF.md
git commit -m "docs(exports): document activity HTMLs"
```

## Task 5: Final Verification

**Files:**

- Verify all files changed by Tasks 1-4.

**Step 1: Run Python syntax checks**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 -m py_compile scripts/integrate_generated_assets.py scripts/export_activity_html.py scripts/generate_run_review.py
```

Expected: exit code 0.

**Step 2: Run integration validation**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/integrate_generated_assets.py --validate runs/20260512_172135_batch5_unblocked
```

Expected: `PASS integrated asset bindings: 12 assets, 12 activities.`

**Step 3: Run HTML export validation**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/export_activity_html.py --validate runs/20260512_172135_batch5_unblocked
```

Expected: `PASS activity HTML exports: 12 files.`

**Step 4: Run dashboard validation**

Run:

```bash
env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 scripts/generate_run_review.py --validate runs/20260512_172135_batch5_unblocked
```

Expected: existing dashboard validation passes.

**Step 5: Run docs/whitespace check**

Run:

```bash
git diff --check
```

Expected: no output.

**Step 6: Inspect intended file scope**

Run:

```bash
git status --short
```

Expected changed paths are limited to:

- `scripts/integrate_generated_assets.py`
- `scripts/export_activity_html.py`
- `review_dashboard.md`
- `runs/README.md`
- `HANDOFF.md`
- `runs/20260512_172135_batch5_unblocked/run_manifest.yaml`
- `runs/20260512_172135_batch5_unblocked/review.html`
- `runs/20260512_172135_batch5_unblocked/integrated_assets/asset_bindings.yaml`
- `runs/20260512_172135_batch5_unblocked/activity_exports/`

## Acceptance Criteria

- Exactly 12 pilot asset rows are integrated.
- Exactly 12 self-contained HTML files are exported.
- Every HTML file embeds its corresponding generated `contact_sheet.png`.
- Every HTML file includes the corresponding activity runtime flow and fallback contract.
- Validation fails if an image, package, metadata file, prompt, or asset ID link is missing.
- The five-file activity package contract remains intact.
- The run manifest records integration and export output paths.
- The main `review.html` still validates after the new outputs are recorded.

## Out Of Scope

- Generating the remaining prebuilt assets.
- Slicing contact sheets into individual runtime cards.
- Building a live WonderLens runtime simulator.
- Changing `activities/_schema/tag_block.schema.json`.
- Adding asset paths directly into canonical `tag_block.yaml`.
- Replacing the existing run review dashboard.

## Follow-Up After This Plan

After these 12 exports validate, use the binding/export scripts as the acceptance gate for the remaining assets. Generate the next batch only after the consuming team agrees that the binding manifest and HTML page content are the right integration shape.
