#!/usr/bin/env python3
"""Prepare review-only mechanism storyboard prompts for a completed run."""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_run_review as review  # noqa: E402


PANEL_TITLES = [
    "Setup",
    "Prompt",
    "Child Action",
    "Feedback Loop",
    "Variation",
    "Completion",
]


def clip(value: Any, limit: int = 170) -> str:
    return review.clip_text(value, limit)


def beat_line(beat: dict[str, str], fallback: str) -> str:
    if not beat:
        return fallback
    parts = [
        beat.get("title", ""),
        beat.get("ai", ""),
        beat.get("child", ""),
        beat.get("followup", ""),
        beat.get("screen", ""),
    ]
    text = " | ".join(clip(part, 110) for part in parts if review.normalize_text(part))
    return text or fallback


def select_panel_sources(package: dict[str, Any]) -> list[dict[str, str]]:
    beats = package.get("runtime_beats", [])
    rounds = [beat for beat in beats if "round" in review.normalize_text(beat.get("title")).lower()]
    first_round = rounds[0] if rounds else (beats[2] if len(beats) > 2 else {})
    second_round = rounds[1] if len(rounds) > 1 else (beats[3] if len(beats) > 3 else first_round)
    final_beat = beats[-1] if beats else {}
    setup_beat = beats[0] if beats else {}
    prompt_beat = beats[1] if len(beats) > 1 else setup_beat
    mechanic = package.get("mechanic") or "activity"
    return [
        {
            "number": "1",
            "title": "Setup",
            "caption": clip(
                package.get("typical_scenario")
                or package.get("brief_description")
                or package.get("premise")
                or beat_line(setup_beat, "The child starts with a concrete scene or object."),
                190,
            ),
            "source": setup_beat.get("title", "package premise"),
        },
        {
            "number": "2",
            "title": "Prompt",
            "caption": clip(beat_line(prompt_beat, "The AI introduces the activity prompt."), 190),
            "source": prompt_beat.get("title", "prod prompt beat"),
        },
        {
            "number": "3",
            "title": "Child Action",
            "caption": clip(
                f"The repeated mechanic is {mechanic}: {beat_line(first_round, 'the child responds through the core action.')}",
                210,
            ),
            "source": first_round.get("title", "core round"),
        },
        {
            "number": "4",
            "title": "Feedback Loop",
            "caption": clip(first_round.get("followup") or beat_line(first_round, "The AI reacts and redirects based on the child response."), 190),
            "source": first_round.get("title", "core round follow-up"),
        },
        {
            "number": "5",
            "title": "Variation",
            "caption": clip(
                beat_line(second_round, "A second round changes the entity, clue, property, or challenge while keeping the same mechanic."),
                190,
            ),
            "source": second_round.get("title", "variation beat"),
        },
        {
            "number": "6",
            "title": "Completion",
            "caption": clip(beat_line(final_beat, "The activity closes with a small recap or earned magic moment."), 190),
            "source": final_beat.get("title", "closing beat"),
        },
    ]


def panel_prompt_lines(panel_captions: list[dict[str, str]]) -> str:
    lines = []
    for item in panel_captions:
        lines.append(f'{item["number"]}. {item["title"]}: {clip(item["caption"], 115)}')
    return "\n".join(lines)


def build_prompt(package: dict[str, Any], panel_captions: list[dict[str, str]]) -> str:
    title = package.get("activity_name") or package.get("activity_id")
    return f"""Create one square 3x2 mechanism storyboard grid for WonderLens reviewers.
Activity: "{title}" ({package.get("activity_id")}); category={package.get("category")}; tier={package.get("tier")}; mechanic={package.get("mechanic")}; pillar={package.get("pillar")}; style={package.get("game_style")}; focal={package.get("focal_attribute")}.
Style: polished light-theme children's educational illustration, warm paper background, indigo accent, muted teal/amber support colors, soft geometric shapes, tablet-like activity screen, no photoreal child faces.
Panels:
{panel_prompt_lines(panel_captions)}
Composition: exactly six equal panels in 3 columns by 2 rows with clean gutters and consistent camera language.
Constraints: no readable words or UI copy, no logos, no copyrighted characters, no watermark, no unsupported runtime feature claims, no dark theme, no clutter. Captions will be outside the image."""


def write_prompt_file(path: Path, package: dict[str, Any], prompt: str, panel_captions: list[dict[str, str]]) -> None:
    caption_lines = "\n".join(
        f'- **{item["number"]}. {item["title"]}** - {item["caption"]} _(source: {item["source"]})_'
        for item in panel_captions
    )
    text = f"""# Mechanism Storyboard Prompt - {package.get("activity_id")}

This is a review-only visual aid for the run dashboard.
It does not change `spec.md`, `prod.md`, or runtime asset requirements.

## Prompt

```text
{prompt}
```

## Panel Captions

{caption_lines}
"""
    path.write_text(text)


def refresh_storyboards(repo_root: Path, run_dir: Path) -> list[dict[str, Any]]:
    manifest = review.load_yaml(run_dir / "run_manifest.yaml")
    outputs = manifest.get("outputs", {}) if isinstance(manifest.get("outputs"), dict) else {}
    package_entries = outputs.get("generated_activities", []) + outputs.get("enriched_activities", []) + outputs.get("audited_activities", [])
    storyboard_root = run_dir / "visual_storyboards"
    storyboard_root.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, Any]] = []
    for entry in package_entries:
        package = review.collect_package(repo_root, run_dir, entry, "Generated")
        activity_id = review.normalize_text(package.get("activity_id"))
        if not activity_id:
            continue
        storyboard_dir = storyboard_root / activity_id
        storyboard_dir.mkdir(parents=True, exist_ok=True)
        panel_captions = select_panel_sources(package)
        prompt = build_prompt(package, panel_captions)
        prompt_path = storyboard_dir / "mechanism_grid.prompt.md"
        meta_path = storyboard_dir / "mechanism_grid.meta.yaml"
        image_path = storyboard_dir / "mechanism_grid.png"
        existing_meta = review.load_yaml(meta_path)
        write_prompt_file(prompt_path, package, prompt, panel_captions)
        image_exists = image_path.exists()
        generated_at = existing_meta.get("generated_at") if isinstance(existing_meta, dict) else ""
        if image_exists and not generated_at:
            generated_at = datetime.fromtimestamp(image_path.stat().st_mtime).isoformat(timespec="seconds")
        meta = {
            "activity_id": activity_id,
            "activity_name": package.get("activity_name"),
            "status": "generated" if image_exists else "prompt_ready",
            "tool": "Codex built-in image generation",
            "target_model": "gpt-image-2",
            "actual_model": existing_meta.get("actual_model", "codex-configured image model") if isinstance(existing_meta, dict) else "codex-configured image model",
            "generated_at": generated_at or "",
            "source_image": existing_meta.get("source_image", "") if isinstance(existing_meta, dict) else "",
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "prompt_path": str(prompt_path.relative_to(run_dir)),
            "image_path": str(image_path.relative_to(run_dir)),
            "package_path": package.get("activity_path"),
            "panel_captions": panel_captions,
        }
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=False))
        entries.append(
            {
                "activity_id": activity_id,
                "status": meta["status"],
                "prompt_path": str(prompt_path.relative_to(run_dir)),
                "meta_path": str(meta_path.relative_to(run_dir)),
                "image_path": str(image_path.relative_to(run_dir)),
            }
        )
    manifest_data = {
        "run_id": run_dir.name,
        "storyboard_count": len(entries),
        "generated_count": sum(1 for item in entries if item["status"] == "generated"),
        "prompt_ready_count": sum(1 for item in entries if item["status"] != "generated"),
        "entries": entries,
    }
    (storyboard_root / "storyboard_manifest.yaml").write_text(
        yaml.safe_dump(manifest_data, sort_keys=False, allow_unicode=False)
    )
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    args = parser.parse_args()
    repo_root = Path.cwd()
    run_dir = args.run_dir if args.run_dir.is_absolute() else repo_root / args.run_dir
    entries = refresh_storyboards(repo_root, run_dir)
    generated = sum(1 for item in entries if item["status"] == "generated")
    print(f"Wrote storyboard prompts for {len(entries)} activities ({generated} images present).")


if __name__ == "__main__":
    main()
