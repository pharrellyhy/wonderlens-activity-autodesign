#!/usr/bin/env python3
"""Declare missing full-pass beat assets in package asset manifests."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyYAML is required. Install pyyaml or run from the repo environment "
        "used for activity metadata validation."
    ) from exc

try:
    import validate_full_pass_asset_bundle as bundle
except ImportError:  # pragma: no cover - direct execution fallback
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import validate_full_pass_asset_bundle as bundle  # type: ignore


BEAT_LABELS = {
    "activity_icon": "Activity icon",
    "intro_scene": "Intro scene",
    "rules_scene": "Rules scene",
    "round_1_scene": "Round 1 scene",
    "round_2_scene": "Round 2 scene",
    "round_3_scene": "Round 3 scene",
    "synthesis_scene": "Synthesis scene",
    "celebrate_scene": "Celebration scene",
    "closing_scene": "Closing scene",
}
STYLE_REFERENCE_MD = "docs/asset_style_reference/wonderlens-activity-style.md"
STYLE_REFERENCE_IMAGE = "docs/asset_style_reference/style-reference-flat-nordic.png"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def activity_title(package_dir: Path, manifest: dict[str, Any]) -> str:
    tag_block = load_yaml(package_dir / "tag_block.yaml")
    for value in (
        tag_block.get("activity_name"),
        tag_block.get("activity_signature", {}).get("preview_label")
        if isinstance(tag_block.get("activity_signature"), dict)
        else "",
        manifest.get("activity_id"),
        package_dir.name,
    ):
        if norm(value):
            return norm(value).replace("_", " ").title()
    return package_dir.name.replace("_", " ").title()


def prod_text(package_dir: Path) -> str:
    path = package_dir / "prod.md"
    return path.read_text() if path.exists() else ""


def section_screen(text: str, marker_pattern: str) -> str:
    match = re.search(marker_pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    if not match:
        return ""
    tail = text[match.end() :]
    next_heading = re.search(r"\n(?:#### Step|\*\*Round\s+\d+\s+--)", tail)
    body = tail[: next_heading.start()] if next_heading else tail
    screen_match = re.search(r"\*\*(?:Screen|Screen/state):\*\*\s*(.+)", body, flags=re.IGNORECASE)
    return norm(screen_match.group(1)) if screen_match else ""


def screen_context(package_dir: Path, asset_id: str) -> str:
    if asset_id == "celebrate_scene" and bundle.needs_synthesis_scene(package_dir):
        return (
            "Use `celebrate_scene` only as a short celebration state after the synthesis payoff; "
            "do not repeat `synthesis_scene`, accepted-photo evidence, app badges, progress, or labels."
        )
    text = prod_text(package_dir)
    patterns = {
        "activity_icon": r"^##\s+.+?$",
        "intro_scene": r"#### Step\s+1\b.*?$",
        "rules_scene": r"#### Step\s+2\b.*?$",
        "round_1_scene": r"\*\*Round\s+1\s+--.*?:\*\*",
        "round_2_scene": r"\*\*Round\s+2\s+--.*?:\*\*",
        "round_3_scene": r"\*\*Round\s+3\s+--.*?:\*\*",
        "synthesis_scene": r"(?:#### Step\s+\d+\b.*?Synthesis.*?$|\*\*Synthesis.*?:\*\*)",
        "celebrate_scene": r"#### Step\s+4\b.*?$",
        "closing_scene": r"#### Step\s+5\b.*?$",
    }
    pattern = patterns.get(asset_id, "")
    if not pattern:
        return ""
    return section_screen(text, pattern)


UI_CONTEXT_PATTERNS = (
    r"\b(?:empty|active|current|completed|filled)?\s*(?:progress|round|pop)?\s*tokens?\b",
    r"\b(?:empty|active|current|completed|filled)?\s*(?:progress|round)?\s*markers?\b",
    r"\b(?:child )?response slots?\b",
    r"\brule strips?\b",
    r"\basset/fallback chips?\b",
    r"\btitle\b",
    r"\bbuttons?\b",
    r"\bpicker slots?\b",
    r"\bUI\b",
)


def sanitize_screen_context(context: str) -> str:
    text = norm(context)
    parts = [part.strip() for part in re.split(r"(?<=[.!?])\s+|;\s*", text) if part.strip()]
    kept: list[str] = []
    for part in parts:
        if any(re.search(pattern, part, flags=re.IGNORECASE) for pattern in UI_CONTEXT_PATTERNS):
            continue
        kept.append(part)
    text = " ".join(kept)
    for pattern in UI_CONTEXT_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:shows?|show)\s+(?:the\s+)?(?:and\s+)?", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:and|or)\s+(?=[.;,]|$)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:with|and)\s*$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+(?:and|or|,)\s+(?:and|or|,)\s+", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip(" ;,.")


def visual_direction(activity_id: str, activity_name: str, asset_id: str) -> str:
    key = f"{activity_id} {activity_name}".lower()
    if "guided_drawing" in key or "guided drawing" in key:
        guided_steps = {
            "activity_icon": (
                "show a clean paper-and-pencil guided drawing motif, with a simple circle drawing "
                "as the main subject."
            ),
            "intro_scene": (
                "show a blank sheet of paper and pencil ready for a child to start a guided sketch; "
                "do not show a completed drawing yet."
            ),
            "rules_scene": (
                "show paper and pencil with a few small drawing example marks arranged loosely as art "
                "materials."
            ),
            "round_1_scene": (
                "show only the first drawing instruction: one big circle on paper, with no ears, petals, "
                "face, or finished picture yet."
            ),
            "round_2_scene": (
                "show the second drawing instruction: the circle now has exactly two small ears or petals; "
                "do not add a face or final detail yet."
            ),
            "round_3_scene": (
                "show the final drawing instruction: the circle with two small ears or petals now gains "
                "one face/detail and reads as a finished simple drawing."
            ),
            "celebrate_scene": (
                "show the finished simple drawing on paper being warmly celebrated through color and "
                "composition only, without badges, stickers, or app UI."
            ),
            "closing_scene": (
                "show the finished simple drawing resting beside the pencil as a quiet process recap."
            ),
        }
        step_direction = guided_steps.get(asset_id, guided_steps["activity_icon"])
        return (
            "Activity-specific direction: guided drawing scene assets must be usable as step cards. "
            f"For this asset, {step_direction} Include paper and pencil only as supporting context."
        )
    if "little_poem" in key or "poem" in key:
        poem_steps = {
            "activity_icon": (
                "show one blank poem page with a pencil and three loose picture tokens: a heart, "
                "a leaf, and a soft dot."
            ),
            "intro_scene": (
                "show a blank poem page waiting beside a pencil and one small source-picture token; "
                "do not show a completed poem yet."
            ),
            "rules_scene": (
                "show the poem-building materials only: blank page, pencil, and separate picture tokens "
                "arranged as art supplies, not as progress markers."
            ),
            "round_1_scene": (
                "show the first contribution step: one simple picture token has been placed near the "
                "blank page, with no written poem lines."
            ),
            "round_2_scene": (
                "show the second contribution step: add one feeling or sound token beside the first "
                "picture token, still no readable writing or pseudo-writing."
            ),
            "round_3_scene": (
                "show the final contribution step: three gathered picture/feeling tokens surround the "
                "page as a finished poem idea board, but do not draw readable text."
            ),
            "celebrate_scene": (
                "show the completed poem-making board glowing softly through color and composition "
                "only, with tokens and pencil visible but no badge UI."
            ),
            "closing_scene": (
                "show the poem page and tokens resting calmly as a process recap, still blank of "
                "readable words."
            ),
        }
        step_direction = poem_steps.get(asset_id, poem_steps["activity_icon"])
        return (
            "Activity-specific direction: Little Poem must look like poem-making, not a generic board. "
            f"For this asset, {step_direction} Avoid interview, timer, microphone, child-on-rug, or "
            "generic response-board staging."
        )
    if "time_sense" in key or "time sense" in key:
        time_steps = {
            "activity_icon": (
                "show one simple sand timer or stopwatch-inspired time object with no numerals."
            ),
            "intro_scene": (
                "show an empty before/after time tray with a sand timer ready to start; no result is "
                "shown yet."
            ),
            "rules_scene": (
                "show the prediction setup: sand timer, start cue, and check tray as physical props, "
                "not as UI controls."
            ),
            "round_1_scene": (
                "show the first prediction moment: sand gathered near the top of a timer and a child-safe "
                "waiting tray before the check."
            ),
            "round_2_scene": (
                "show the second timing variation: sand has moved halfway and a small shadow cue has "
                "shifted slightly."
            ),
            "round_3_scene": (
                "show the check/reflect moment: a before-and-after tray with changed sand/shadow state, "
                "but no score, answer, or progress dots."
            ),
            "celebrate_scene": (
                "show the completed time-prediction tray with the sand settled and a warm color lift, "
                "without trophies, badges, or app UI."
            ),
            "closing_scene": (
                "show the sand timer resting beside the before/after tray as a calm recap of estimating "
                "then checking."
            ),
        }
        step_direction = time_steps.get(asset_id, time_steps["activity_icon"])
        return (
            "Activity-specific direction: Time Sense must show elapsed-time prediction and checking. "
            f"For this asset, {step_direction} Avoid poem pages, interview microphones, child-on-rug, "
            "and repeated blank-board layouts."
        )
    if "current_topic" in key or "interview" in key:
        interview_steps = {
            "activity_icon": (
                "show one small microphone with two blank speech bubbles and two idea cards."
            ),
            "intro_scene": (
                "show an interview table with a small microphone and empty idea cards ready for an "
                "opinion-and-reason turn."
            ),
            "rules_scene": (
                "show the interview tools as physical props: microphone, blank speech bubbles, and "
                "idea cards, without progress markers or rule strips."
            ),
            "round_1_scene": (
                "show the first opinion step: one blank speech bubble is active beside the microphone, "
                "with one idea card nearby."
            ),
            "round_2_scene": (
                "show the reason step: a second blank speech bubble links to the first idea card with "
                "a simple visual connector, no text."
            ),
            "round_3_scene": (
                "show the polite follow-up step: three blank idea cards gathered around the microphone "
                "as a completed interview thought set."
            ),
            "celebrate_scene": (
                "show the gathered interview ideas warmly highlighted around the microphone, with no "
                "score badge or app UI."
            ),
            "closing_scene": (
                "show the microphone and idea cards resting calmly as an interview recap."
            ),
        }
        step_direction = interview_steps.get(asset_id, interview_steps["activity_icon"])
        return (
            "Activity-specific direction: Current Topic Interview must look like opinion-and-reason "
            f"interview work. For this asset, {step_direction} Avoid poem tokens, clocks, timers, "
            "child-on-rug, or a generic blank board."
        )
    if "recognition_pop" in key or "recognition pop" in key:
        pop_steps = {
            "activity_icon": (
                "show a neutral pop-stage with one empty reveal slot and a small sound-wave motif; "
                "do not include dog, fox, wolf, or any animal silhouette."
            ),
            "intro_scene": (
                "show an empty pop-stage ready for the source target card overlay; leave the center "
                "clear for the app-placed card."
            ),
            "rules_scene": (
                "show three empty card stands or reveal slots that imply say/quiet practice through "
                "composition only; do not draw the animal cards."
            ),
            "round_1_scene": (
                "show one empty center pop slot with a gentle spotlight where the target card can be "
                "overlaid; no animals are drawn in the background."
            ),
            "round_2_scene": (
                "show one quiet pop slot with a soft muted curtain or pause motif where a distractor "
                "card can be overlaid; no animals are drawn in the background."
            ),
            "round_3_scene": (
                "show two sequential empty pop slots with the first fading and the second ready for "
                "the app-placed card stream; no animals are drawn in the background."
            ),
            "celebrate_scene": (
                "show the neutral pop-stage warmly lit after the target/quiet sequence, without tokens "
                "or animal duplicates."
            ),
            "closing_scene": (
                "show the empty reveal stage resting calmly, with the card area still clear."
            ),
        }
        step_direction = pop_steps.get(asset_id, pop_steps["activity_icon"])
        return (
            "Activity-specific direction: Recognition Pop must use neutral stage art because target and "
            f"distractor cards are separate sprites. For this asset, {step_direction} If the activity "
            "has separate target/distractor item assets, do not redraw those selectable animals inside "
            "story-scene backgrounds; let the app place the picker/card sprites."
        )
    if "phoneme" in key:
        return (
            "Activity-specific direction: use neutral treasure-hunt/search imagery such as a listening "
            "spot, soft treasure path, empty basket, or camera clue slot; do not reveal target objects "
            "before the child supplies evidence."
        )
    if "vegetable_sort" in key or "vegetable sort" in key:
        return (
            "Activity-specific direction: use empty garden trays, baskets, or sorting mats as scene "
            "context. Generate vegetables as separate item sprites instead of baking selectable produce "
            "into backgrounds."
        )
    return (
        "Activity-specific direction: choose a visual motif unique to this activity's source promise "
        "and mechanic; avoid reusing the same blank-board, child-on-rug, response-slot, or cozy-room "
        "template across activities."
    )


def prompt_for(activity_id: str, activity_name: str, asset_id: str, role: str, context: str) -> str:
    label = BEAT_LABELS.get(asset_id, asset_id.replace("_", " "))
    composition = (
        "full-bleed square beat scene, softly painterly nursery composition, no app UI"
        if role == "story_scene"
        else "single centered icon or badge on a clean white background, no app UI"
    )
    clean_context = sanitize_screen_context(context)
    context_clause = f" Source beat context, for subject only: {clean_context}." if clean_context else ""
    direction = visual_direction(activity_id, activity_name, asset_id)
    return (
        "Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. "
        f"Primary request: {label} for {activity_name}. "
        f"Composition: {composition}; generate a 512x512 square source PNG; "
        "if the image tool returns a larger square, downsample it to 512x512 before asset build; "
        "keep important details inside the central round-lens safe area."
        f"{context_clause} "
        f"{direction} "
        "Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; "
        f"use repo-local style reference `{STYLE_REFERENCE_MD}` and visual target `{STYLE_REFERENCE_IMAGE}`; "
        "broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, "
        "restrained boho pastels, airy negative space, organic simple silhouettes. "
        "No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, "
        "device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. "
        "Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, "
        "badges, or other app-owned interface state; the runtime overlays those separately."
    )


def bundle_asset(
    activity_name: str,
    asset_id: str,
    role: str,
    context: str,
    activity_id: str | None = None,
) -> dict[str, Any]:
    prompt_activity_id = activity_id or activity_name
    return {
        "id": asset_id,
        "role": role,
        "label": f"{BEAT_LABELS.get(asset_id, asset_id.replace('_', ' '))} for {activity_name}.",
        "requiredness": "required",
        "accuracy_mode": "illustrative",
        "source_strategy": "generated_illustrative",
        "transformation_policy": "generate_new",
        "prompt_en": prompt_for(prompt_activity_id, activity_name, asset_id, role, context),
        "variants": [
            {
                "id": "round_512",
                "target": "round_device_screen",
                "size": "512x512",
                "path": None,
            }
        ],
        "fallback_behavior": (
            "If this beat asset is unavailable, degrade the demo screen and do not claim "
            "that the missing visual is displayed."
        ),
    }


def repair_package(package_dir: Path) -> dict[str, Any]:
    manifest_path = package_dir / "asset_manifest.yaml"
    manifest = load_yaml(manifest_path)
    manifest.setdefault("assets", [])
    assets = manifest.get("assets")
    if not isinstance(assets, list):
        assets = []
        manifest["assets"] = assets
    by_id = {
        norm(asset.get("id")): asset
        for asset in assets
        if isinstance(asset, dict) and norm(asset.get("id"))
    }
    activity_id = norm(manifest.get("activity_id")) or package_dir.name
    title = activity_title(package_dir, manifest)
    added: list[str] = []
    updated: list[str] = []

    for asset_id, role in bundle.required_assets_for_package(package_dir):
        existing = by_id.get(asset_id)
        context = screen_context(package_dir, asset_id)
        if existing is None:
            assets.append(bundle_asset(title, asset_id, role, context, activity_id))
            by_id[asset_id] = assets[-1]
            added.append(asset_id)
            continue
        if norm(existing.get("role")) != role:
            existing["role"] = role
            updated.append(asset_id)
        refreshed_label = f"{BEAT_LABELS.get(asset_id, asset_id.replace('_', ' '))} for {title}."
        if norm(existing.get("label")) != refreshed_label:
            existing["label"] = refreshed_label
            updated.append(asset_id)
        refreshed_fallback = (
            "If this beat asset is unavailable, degrade the demo screen and do not claim "
            "that the missing visual is displayed."
        )
        if norm(existing.get("fallback_behavior")) != refreshed_fallback:
            existing["fallback_behavior"] = refreshed_fallback
            updated.append(asset_id)
        if (
            norm(existing.get("accuracy_mode")) == "illustrative"
            and norm(existing.get("source_strategy")) == "generated_illustrative"
        ):
            refreshed_prompt = prompt_for(activity_id, title, asset_id, role, context)
            if norm(existing.get("prompt_en")) != refreshed_prompt:
                existing["prompt_en"] = refreshed_prompt
                updated.append(asset_id)
        variants = existing.get("variants")
        if not isinstance(variants, list) or not variants:
            existing["variants"] = [
                {
                    "id": "round_512",
                    "target": "round_device_screen",
                    "size": "512x512",
                    "path": None,
                }
            ]
            updated.append(asset_id)

    if added or updated:
        write_yaml(manifest_path, manifest)

    return {
        "activity_id": activity_id,
        "package_path": package_dir.as_posix(),
        "added_assets": added,
        "updated_assets": sorted(set(updated)),
    }


def repair_run(run_dir: Path) -> dict[str, Any]:
    package_dirs = bundle.discover_package_dirs(run_dir)
    package_results = [repair_package(package_dir) for package_dir in package_dirs]
    added_count = sum(len(result["added_assets"]) for result in package_results)
    updated_count = sum(len(result["updated_assets"]) for result in package_results)
    return {
        "run_id": run_dir.name,
        "generated_at": now_iso(),
        "package_count": len(package_dirs),
        "added_count": added_count,
        "updated_count": updated_count,
        "packages": package_results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    parser.add_argument("--report-yaml", type=Path, default=None)
    args = parser.parse_args(argv)

    result = repair_run(args.run_dir)
    if args.report_yaml is not None:
        args.report_yaml.parent.mkdir(parents=True, exist_ok=True)
        args.report_yaml.write_text(yaml.safe_dump(result, sort_keys=False, allow_unicode=False))
    print(
        "OK full-pass bundle manifest repair: "
        f"packages={result['package_count']} added={result['added_count']} updated={result['updated_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
