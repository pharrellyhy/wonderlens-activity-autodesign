#!/usr/bin/env python3
"""Validate activity_display_contract_v1.yaml package files."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

try:  # Prefer the repo's usual YAML dependency when available.
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - exercised in dependency-light envs.
    yaml = None


CONTRACT_NAME = "activity_display_contract_v1"
LAYOUT_IDS = {
    "single_image",
    "two_image_options",
    "two_direction_options",
    "two_number_options",
    "multi_option_carousel",
}
CONTROL_MODES = {
    "voice_only",
    "binary_choice",
    "carousel_choice",
    "number_choice",
    "step_confirm",
    "camera_capture",
    "replay_only",
    "reveal_control",
    "sort_pick_place",
    "self_report",
}
POLICY_TYPES = {
    "choice_match",
    "number_match",
    "category_match",
    "alias_match",
    "echo_match",
    "photo_object_initial_sound",
    "semantic_llm_judge",
    "self_report",
    "accept_any_participation",
}
DISPLAY_ASSET_KINDS = {"image", "option", "cue", "number", "category", "word", "scene", "item", "group"}
OPTION_LAYOUTS = {"two_image_options", "two_direction_options", "two_number_options", "multi_option_carousel"}
VERIFIABLE_POLICIES = POLICY_TYPES - {"accept_any_participation"}
CJK_RE = re.compile(r"[\u3400-\u9fff]")


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def load_yaml(path: Path) -> Any:
    if yaml is not None:
        return yaml.safe_load(path.read_text()) or {}

    script = "require 'yaml'; require 'json'; data = YAML.load_file(ARGV[0]); puts JSON.generate(data)"
    result = subprocess.run(
        ["ruby", "-e", script, str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Could not parse YAML via Ruby for {path}: {result.stderr.strip()}")
    return json.loads(result.stdout) if result.stdout.strip() else {}


def as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def add_required(issue_list: list[str], label: str, data: dict[str, Any], fields: tuple[str, ...]) -> None:
    for field in fields:
        value = data.get(field)
        if isinstance(value, (list, dict)):
            missing = not value
        else:
            missing = not norm(value)
        if missing:
            issue_list.append(f"{label}: missing required field {field}")


def has_chinese(value: Any) -> bool:
    return bool(CJK_RE.search(norm(value)))


def discover_package_dirs(roots: list[Path]) -> list[Path]:
    dirs: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        root = root.resolve()
        candidates: list[Path]
        if root.is_file():
            candidates = [root.parent] if root.name == f"{CONTRACT_NAME}.yaml" else []
        elif (root / f"{CONTRACT_NAME}.yaml").exists():
            candidates = [root]
        elif root.exists():
            candidates = sorted(
                {
                    path.parent
                    for path in root.rglob(f"{CONTRACT_NAME}.yaml")
                    if "generated_assets_pilot" not in path.parts
                }
            )
        else:
            candidates = []
        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                dirs.append(candidate)
    return dirs


def validate_display_asset(
    package_dir: Path,
    display_asset: dict[str, Any],
    manifest_asset_ids: set[str],
    index: int,
) -> list[str]:
    label = f"{package_dir}: display_assets[{index}]"
    issues: list[str] = []
    add_required(issues, label, display_asset, ("display_asset_id", "kind"))

    kind = norm(display_asset.get("kind"))
    if kind and kind not in DISPLAY_ASSET_KINDS:
        issues.append(f"{label}: kind {kind!r} is not allowed")

    asset_manifest_id = norm(display_asset.get("asset_manifest_id"))
    if asset_manifest_id and asset_manifest_id not in manifest_asset_ids:
        issues.append(f"{label}: asset_manifest_id {asset_manifest_id!r} is not declared in asset_manifest.yaml")

    return issues


def validate_effect_profile(package_dir: Path, frame_id: str, effect_profile: dict[str, Any]) -> list[str]:
    label = f"{package_dir}: frame {frame_id}: effect_profile"
    issues: list[str] = []
    add_required(issues, label, effect_profile, ("id", "sound_effects", "lighting_effects", "haptic_feedback"))

    stale_fields = {"sound", "lighting", "haptics", "effect_profile"}
    for field in sorted(stale_fields & set(effect_profile)):
        issues.append(f"{label}: stale effect field {field!r}; use sound_effects, lighting_effects, and haptic_feedback")

    for field in ("id", "sound_effects", "lighting_effects", "haptic_feedback"):
        raw_value = effect_profile.get(field)
        values = as_list(raw_value) if field != "id" else [raw_value]
        if field != "id" and raw_value is not None and not isinstance(raw_value, list):
            issues.append(f"{label}.{field} must be a list")
            continue
        for index, value in enumerate(values):
            if not norm(value):
                issues.append(f"{label}.{field}[{index}] must not be empty")
            if has_chinese(value):
                issues.append(f"{label}.{field}[{index}] must be English-only")

    return issues


def validate_frame_options(
    package_dir: Path,
    frame_id: str,
    layout_id: str,
    options: list[Any],
    display_asset_ids: set[str],
) -> tuple[list[str], dict[str, dict[str, Any]]]:
    label = f"{package_dir}: frame {frame_id}"
    issues: list[str] = []
    option_map: dict[str, dict[str, Any]] = {}

    if layout_id in OPTION_LAYOUTS and not options:
        issues.append(f"{label}: {layout_id} frame must declare options")
    if layout_id in {"two_image_options", "two_direction_options", "two_number_options"} and len(options) != 2:
        issues.append(f"{label}: {layout_id} frame must declare exactly two options")
    if layout_id == "multi_option_carousel" and len(options) < 3:
        issues.append(f"{label}: multi_option_carousel frame must declare at least three options")

    for index, option in enumerate(options):
        option_data = as_dict(option)
        option_label = f"{label}: options[{index}]"
        add_required(issues, option_label, option_data, ("option_id", "label"))
        option_id = norm(option_data.get("option_id"))
        if option_id:
            if option_id in option_map:
                issues.append(f"{option_label}: duplicate option_id {option_id!r}")
            option_map[option_id] = option_data
        option_asset_id = norm(option_data.get("display_asset_id"))
        if option_asset_id and option_asset_id not in display_asset_ids:
            issues.append(f"{option_label}: display_asset_id {option_asset_id!r} is not declared in display_assets")
        if layout_id == "two_number_options" and "value" not in option_data:
            issues.append(f"{option_label}: two_number_options option must declare value")

    return issues, option_map


def target_display_asset(
    target: dict[str, Any],
    frame_display_asset_id: str,
    display_assets: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    display_asset_id = norm(target.get("display_asset_id")) or frame_display_asset_id
    return display_assets.get(display_asset_id, {})


def require_display_asset_target(
    issues: list[str],
    package_dir: Path,
    frame_id: str,
    policy_type: str,
    policy: dict[str, Any],
    frame_display_asset_id: str,
    display_assets: dict[str, dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    label = f"{package_dir}: frame {frame_id}"
    target = as_dict(policy.get("target"))
    if norm(target.get("type")) != "display_asset" or not norm(target.get("display_asset_id")):
        issues.append(f"{label}: {policy_type} policy must target a displayed asset")
    display_asset = target_display_asset(target, frame_display_asset_id, display_assets)
    if target and norm(target.get("display_asset_id")) and norm(target.get("display_asset_id")) not in display_assets:
        issues.append(f"{label}: target.display_asset_id {target.get('display_asset_id')!r} is not declared in display_assets")
    if norm(target.get("display_asset_id")) and norm(target.get("display_asset_id")) != frame_display_asset_id:
        issues.append(f"{label}: {policy_type} target must match the frame display_asset_id")
    return target, display_asset


def validate_verification_policy(
    package_dir: Path,
    frame_id: str,
    frame_display_asset_id: str,
    policy: dict[str, Any],
    option_map: dict[str, dict[str, Any]],
    display_assets: dict[str, dict[str, Any]],
) -> list[str]:
    label = f"{package_dir}: frame {frame_id}"
    issues: list[str] = []
    add_required(issues, f"{label}: verification_policy", policy, ("type", "evidence"))

    policy_type = norm(policy.get("type"))
    if policy_type and policy_type not in POLICY_TYPES:
        issues.append(f"{label}: verification_policy.type {policy_type!r} is not allowed")
    if "required" not in policy or not isinstance(policy.get("required"), bool):
        issues.append(f"{label}: verification_policy.required must be boolean")

    evidence = as_list(policy.get("evidence"))
    if not evidence:
        issues.append(f"{label}: verification_policy.evidence must include at least one item")

    if policy_type == "choice_match":
        target = as_dict(policy.get("target"))
        if norm(target.get("type")) != "option" or not norm(target.get("option_id")):
            issues.append(f"{label}: choice_match policy must declare target.option_id")
            return issues
        option_id = norm(target.get("option_id"))
        option = option_map.get(option_id)
        if option is None:
            issues.append(f"{label}: target.option_id {option_id!r} is not declared in frame options")
        elif option.get("is_correct") is not True:
            issues.append(f"{label}: target.option_id {option_id!r} must point to an option with is_correct true")
        return issues

    if policy_type == "number_match":
        _, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if "expected_number" not in as_dict(display_asset.get("metadata")):
            issues.append(f"{label}: target display asset must declare metadata.expected_number")
        return issues

    if policy_type == "category_match":
        _, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if "target_category_id" not in as_dict(display_asset.get("metadata")):
            issues.append(f"{label}: target display asset must declare metadata.target_category_id")
        return issues

    if policy_type == "alias_match":
        _, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if not as_list(as_dict(display_asset.get("metadata")).get("accepted_aliases")):
            issues.append(f"{label}: target display asset must declare metadata.accepted_aliases")
        return issues

    if policy_type == "echo_match":
        _, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        metadata = as_dict(display_asset.get("metadata"))
        if not norm(metadata.get("target_phrase")) and not as_list(metadata.get("accepted_aliases")):
            issues.append(f"{label}: target display asset must declare metadata.target_phrase or metadata.accepted_aliases")
        return issues

    if policy_type == "photo_object_initial_sound":
        target, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if "photo_id" not in evidence:
            issues.append(f"{label}: photo_object_initial_sound policy must include photo_id evidence")
        if not norm(as_dict(display_asset.get("metadata")).get("target_initial_sound")):
            issues.append(f"{label}: target display asset must declare metadata.target_initial_sound")
        return issues

    if policy_type == "semantic_llm_judge":
        _, display_asset = require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if not norm(as_dict(display_asset.get("metadata")).get("semantic_rubric")):
            issues.append(f"{label}: target display asset must declare metadata.semantic_rubric")
        return issues

    if policy_type == "self_report":
        require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        if "self_reported_done" not in evidence:
            issues.append(f"{label}: self_report policy must include self_reported_done evidence")
        return issues

    if policy_type == "accept_any_participation":
        require_display_asset_target(
            issues, package_dir, frame_id, policy_type, policy, frame_display_asset_id, display_assets
        )
        return issues

    if policy_type in VERIFIABLE_POLICIES:
        issues.append(f"{label}: {policy_type} policy has no validator implementation")

    return issues


def validate_frame(
    package_dir: Path,
    frame: dict[str, Any],
    display_assets: dict[str, dict[str, Any]],
    index: int,
) -> list[str]:
    frame_id = norm(frame.get("frame_id")) or f"frames[{index}]"
    label = f"{package_dir}: frame {frame_id}"
    issues: list[str] = []
    add_required(
        issues,
        label,
        frame,
        ("frame_id", "step_ref", "layout_id", "display_asset_id", "control_mode", "verification_policy", "effect_profile"),
    )

    layout_id = norm(frame.get("layout_id"))
    if layout_id and layout_id not in LAYOUT_IDS:
        issues.append(f"{label}: layout_id {layout_id!r} is not allowed")

    control_mode = norm(frame.get("control_mode"))
    if control_mode and control_mode not in CONTROL_MODES:
        issues.append(f"{label}: control_mode {control_mode!r} is not allowed")

    frame_display_asset_id = norm(frame.get("display_asset_id"))
    if frame_display_asset_id and frame_display_asset_id not in display_assets:
        issues.append(f"{label}: display_asset_id {frame_display_asset_id!r} is not declared in display_assets")

    option_issues, option_map = validate_frame_options(
        package_dir, frame_id, layout_id, as_list(frame.get("options")), set(display_assets)
    )
    issues.extend(option_issues)
    issues.extend(
        validate_verification_policy(
            package_dir,
            frame_id,
            frame_display_asset_id,
            as_dict(frame.get("verification_policy")),
            option_map,
            display_assets,
        )
    )
    issues.extend(validate_effect_profile(package_dir, frame_id, as_dict(frame.get("effect_profile"))))
    return issues


def validate_contract(package_dir: Path) -> list[str]:
    contract_path = package_dir / f"{CONTRACT_NAME}.yaml"
    manifest_path = package_dir / "asset_manifest.yaml"
    label = str(package_dir)
    issues: list[str] = []
    contract = as_dict(load_yaml(contract_path))
    manifest = as_dict(load_yaml(manifest_path)) if manifest_path.exists() else {}

    add_required(issues, label, contract, ("activity_id", "version", "contract", "display_assets", "frames"))
    if "display_assets" in contract and not as_list(contract.get("display_assets")):
        issues.append(f"{label}: display_assets must include at least one item")
    if "frames" in contract and not as_list(contract.get("frames")):
        issues.append(f"{label}: frames must include at least one item")
    if contract.get("version") != 1:
        issues.append(f"{label}: version must be 1")
    if norm(contract.get("contract")) != CONTRACT_NAME:
        issues.append(f"{label}: contract must be {CONTRACT_NAME}")
    if manifest and norm(manifest.get("activity_id")) and norm(contract.get("activity_id")) != norm(manifest.get("activity_id")):
        issues.append(f"{label}: activity_id differs between activity_display_contract_v1.yaml and asset_manifest.yaml")

    manifest_asset_ids = {norm(asset.get("id")) for asset in as_list(manifest.get("assets")) if isinstance(asset, dict)}
    display_assets: dict[str, dict[str, Any]] = {}
    for index, display_asset in enumerate(as_list(contract.get("display_assets"))):
        display_asset_data = as_dict(display_asset)
        display_asset_id = norm(display_asset_data.get("display_asset_id"))
        if display_asset_id:
            if display_asset_id in display_assets:
                issues.append(f"{label}: display_assets[{index}]: duplicate display_asset_id {display_asset_id!r}")
            display_assets[display_asset_id] = display_asset_data
        issues.extend(validate_display_asset(package_dir, display_asset_data, manifest_asset_ids, index))

    frame_ids: set[str] = set()
    for index, frame in enumerate(as_list(contract.get("frames"))):
        frame_data = as_dict(frame)
        frame_id = norm(frame_data.get("frame_id"))
        if frame_id:
            if frame_id in frame_ids:
                issues.append(f"{label}: frames[{index}]: duplicate frame_id {frame_id!r}")
            frame_ids.add(frame_id)
        issues.extend(validate_frame(package_dir, frame_data, display_assets, index))

    return issues


def validate_roots(roots: list[Path]) -> list[str]:
    package_dirs = discover_package_dirs(roots)
    issues: list[str] = []
    for package_dir in package_dirs:
        issues.extend(validate_contract(package_dir))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path, help="Package dirs or roots containing display contract files")
    args = parser.parse_args(argv)

    package_dirs = discover_package_dirs(args.roots)
    issues = validate_roots(args.roots)
    if issues:
        for issue in issues:
            print(f"FAIL {issue}")
        return 1
    print(f"OK activity display contract: {len(package_dirs)} package(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
