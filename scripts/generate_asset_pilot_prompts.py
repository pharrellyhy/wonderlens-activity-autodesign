#!/usr/bin/env python3
"""Prepare pilot prompts for run-local prebuilt activity assets."""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


PILOT_SELECTION = [
    {"mechanic": "collect", "activity_id": "concept_phoneme_hunt_collect", "asset_id": "phoneme_letter_card_01"},
    {"mechanic": "deduce", "activity_id": "concept_partial_reveal_deduce", "asset_id": "partial_reveal_cards_01"},
    {"mechanic": "motion_voice", "activity_id": "concept_animal_sound_motion_voice", "asset_id": "animal_sound_cards_01"},
    {"mechanic": "remember", "activity_id": "concept_word_echo_remember", "asset_id": "word_echo_cards_01"},
    {"mechanic": "care", "activity_id": "concept_emotion_reader_care", "asset_id": "emotion_expression_cards_01"},
    {"mechanic": "enumerate", "activity_id": "concept_constellation_star_count_enumerate", "asset_id": "constellation_count_cards_01"},
    {"mechanic": "decide", "activity_id": "concept_career_decision_decide", "asset_id": "career_portrait_cards_01"},
    {"mechanic": "sort", "activity_id": "concept_vegetable_sort_sort", "asset_id": "vegetable_sort_cards_01"},
    {"mechanic": "predict", "activity_id": "concept_travel_planner_predict", "asset_id": "travel_planning_cards_01"},
    {"mechanic": "build", "activity_id": "concept_guided_drawing_probe", "asset_id": "guided_drawing_step_cards_01"},
    {"mechanic": "imagine", "activity_id": "concept_story_unlock_probe", "asset_id": "story_unlock_cards_01"},
    {"mechanic": "compare", "activity_id": "concept_recognition_pop_probe", "asset_id": "recognition_challenge_cards_01"},
]

STYLE_OVERRIDES = {
    "collect": "sunny phonics desk, rounded letter-card design, cheerful yellow and sky-blue accents",
    "deduce": "soft mystery clue table, cropped animal detail cards, lavender and teal accents",
    "motion_voice": "tiny pretend stage, friendly animal cards, coral and mint accents",
    "remember": "cozy vocabulary shelf, centered object cards, warm green and cream accents",
    "care": "calm feeling-helper station, expressive character cards, peach and soft blue accents",
    "enumerate": "night-sky counting board, high-contrast star cards, deep blue and warm gold accents",
    "decide": "inclusive helper-role desk, portrait cards with simple tools, fresh blue and orange accents",
    "sort": "market sorting mat, vegetable cards, garden green and tomato red accents",
    "predict": "pretend trip planning table, travel item cards, aqua and sunflower accents",
    "build": "simple sketch workshop, drawing-step cards, black line art with pastel tabs",
    "imagine": "storybook unlock table, magical door and token cards, warm violet and amber accents",
    "compare": "recognition challenge board, target and distractor object cards, crisp teal and red accents",
}


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text())
    return data if isinstance(data, dict) else {}


def safe_slug(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in value).strip("_")


def find_activity(manifest: dict[str, Any], activity_id: str) -> dict[str, Any]:
    outputs = manifest.get("outputs", {})
    for entry in outputs.get("generated_activities", []):
        if entry.get("activity_id") == activity_id:
            return entry
    raise KeyError(f"Activity not found in manifest: {activity_id}")


def find_asset(entry: dict[str, Any], asset_id: str) -> dict[str, Any]:
    for asset in entry.get("asset_usage", []) or []:
        if asset.get("asset_id") == asset_id:
            return asset
    raise KeyError(f"Asset not found for {entry.get('activity_id')}: {asset_id}")


def activity_title(entry: dict[str, Any]) -> str:
    path = Path(entry.get("activity_path", ""))
    tag = load_yaml(path / "tag_block.yaml")
    return tag.get("activity_name") or entry.get("activity_id", "")


def build_prompt(entry: dict[str, Any], asset: dict[str, Any], mechanic: str) -> str:
    title = activity_title(entry)
    style = STYLE_OVERRIDES.get(mechanic, "polished child-friendly activity cards")
    base_prompt = asset.get("prompt_en") or asset.get("prompt_or_source") or asset.get("purpose") or ""
    return f"""Create one reviewable contact-sheet image for a WonderLens prebuilt activity asset.
Activity: {title} ({entry.get("activity_id")})
Mechanic: {mechanic}
Asset: {asset.get("asset_id")} ({asset.get("asset_type")}); requiredness={asset.get("requiredness")}; timing={asset.get("generation_timing")}
Runtime use: {asset.get("use_step")}
Display location: {asset.get("display_location")}
Purpose: {asset.get("purpose")}

Source asset prompt:
{base_prompt}

Contact-sheet requirements:
- Make one square contact sheet with 6 to 9 individual card thumbnails arranged in a clean grid.
- Keep all cards within this one activity visually consistent: same card frame, illustration style, lighting, scale, and background treatment.
- Make this activity visually distinct from other mechanics by using this scene/style direction: {style}.
- Child-friendly and preschool/early-elementary appropriate: warm, clear, non-scary, non-punitive, no real child photos.
- Use plain backgrounds inside cards unless the source prompt explicitly needs a scene.
- Keep each card's subject large, centered, inspectable, and easy to understand at small size.
- Avoid brands, copyrighted characters, watermarks, dense UI, clutter, weapons, hazards, stereotypes, and photoreal faces.
- No text unless the source asset explicitly requires letters or simple word labels; if text is required, keep it large, minimal, and high contrast.
- This is a review contact sheet, not final sliced runtime output; do not add explanatory captions outside the cards."""


def write_prompt(path: Path, entry: dict[str, Any], asset: dict[str, Any], prompt: str) -> None:
    text = f"""# Generated Asset Pilot Prompt - {asset.get("asset_id")}

This is a pilot review artifact for prebuilt child-facing assets.
It does not change `spec.md`, `prod.md`, or runtime asset contracts.

## Prompt

```text
{prompt}
```

## Runtime Placement

- Activity: `{entry.get("activity_id")}`
- Asset: `{asset.get("asset_id")}`
- Requiredness: `{asset.get("requiredness")}`
- Timing: `{asset.get("generation_timing")}`
- Use step: `{asset.get("use_step")}`
- Display location: `{asset.get("display_location")}`
- Fallback: {asset.get("fallback_behavior")}
"""
    path.write_text(text)


def refresh(run_dir: Path) -> list[dict[str, Any]]:
    manifest = load_yaml(run_dir / "run_manifest.yaml")
    root = run_dir / "generated_assets_pilot"
    root.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, Any]] = []
    for item in PILOT_SELECTION:
        entry = find_activity(manifest, item["activity_id"])
        asset = find_asset(entry, item["asset_id"])
        activity_id = entry["activity_id"]
        asset_id = asset["asset_id"]
        asset_dir = root / activity_id / safe_slug(asset_id)
        asset_dir.mkdir(parents=True, exist_ok=True)
        prompt = build_prompt(entry, asset, item["mechanic"])
        prompt_path = asset_dir / "contact_sheet.prompt.md"
        meta_path = asset_dir / "asset.meta.yaml"
        image_path = asset_dir / "contact_sheet.png"
        old_meta = load_yaml(meta_path)
        image_exists = image_path.exists()
        generated_at = old_meta.get("generated_at") if image_exists else ""
        if image_exists and not generated_at:
            generated_at = datetime.fromtimestamp(image_path.stat().st_mtime).isoformat(timespec="seconds")
        source_image = old_meta.get("source_image", "") if image_exists else ""
        write_prompt(prompt_path, entry, asset, prompt)
        meta = {
            "run_id": run_dir.name,
            "activity_id": activity_id,
            "activity_name": activity_title(entry),
            "mechanic": item["mechanic"],
            "asset_id": asset_id,
            "asset_type": asset.get("asset_type"),
            "requiredness": asset.get("requiredness"),
            "generation_timing": asset.get("generation_timing"),
            "status": "generated" if image_exists else "prompt_ready",
            "artifact_kind": "prebuilt_asset_contact_sheet_pilot",
            "tool": "Codex built-in image generation",
            "target_model": "gpt-image-2",
            "actual_model": old_meta.get("actual_model", "codex-configured image model") if image_exists else "codex-configured image model",
            "generated_at": generated_at or "",
            "source_image": source_image,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "prompt_path": str(prompt_path.relative_to(run_dir)),
            "image_path": str(image_path.relative_to(run_dir)),
            "meta_path": str(meta_path.relative_to(run_dir)),
            "package_path": entry.get("activity_path"),
            "use_step": asset.get("use_step"),
            "display_location": asset.get("display_location"),
            "purpose": asset.get("purpose"),
            "display_behavior": asset.get("display_behavior"),
            "fallback_behavior": asset.get("fallback_behavior"),
            "safety_constraints": asset.get("safety_constraints"),
        }
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=False))
        entries.append(
            {
                "activity_id": activity_id,
                "activity_name": meta["activity_name"],
                "mechanic": item["mechanic"],
                "asset_id": asset_id,
                "asset_type": asset.get("asset_type"),
                "requiredness": asset.get("requiredness"),
                "generation_timing": asset.get("generation_timing"),
                "status": meta["status"],
                "prompt_path": str(prompt_path.relative_to(run_dir)),
                "image_path": str(image_path.relative_to(run_dir)),
                "meta_path": str(meta_path.relative_to(run_dir)),
            }
        )
    manifest_data = {
        "run_id": run_dir.name,
        "artifact_kind": "prebuilt_asset_contact_sheet_pilot",
        "selection_rule": "one declared prebuilt or display-existing asset per mechanic",
        "asset_count": len(entries),
        "generated_count": sum(1 for entry in entries if entry["status"] == "generated"),
        "prompt_ready_count": sum(1 for entry in entries if entry["status"] != "generated"),
        "entries": entries,
    }
    (root / "asset_manifest.yaml").write_text(yaml.safe_dump(manifest_data, sort_keys=False, allow_unicode=False))
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    args = parser.parse_args()
    run_dir = args.run_dir if args.run_dir.is_absolute() else Path.cwd() / args.run_dir
    entries = refresh(run_dir)
    generated = sum(1 for entry in entries if entry["status"] == "generated")
    print(f"Wrote pilot asset prompts for {len(entries)} assets ({generated} images present).")


if __name__ == "__main__":
    main()
