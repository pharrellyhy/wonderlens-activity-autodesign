#!/usr/bin/env python3
"""Validate optional demo support and runtime asset manifest files."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

try:  # Prefer the repo's usual YAML dependency when available.
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - exercised in dependency-light envs.
    yaml = None


DEMO_STATUSES = {"supported", "degraded", "unsupported"}
UI_TEMPLATES = {"cat1_dialogue", "cat5_collection", "cat5_judgment", "none"}
PARAMETERIZATION_MODES = {
    "fixed",
    "entity_theme",
    "entity_target",
    "property_target",
    "initial_sound_from_entity",
    "word_from_entity",
    "asset_catalog_target",
    "unsupported_until_parameterized",
}
ENTITY_COMPATIBILITY_VALUES = {"source_bound", "agnostic", "unsupported"}
DYNAMIC_PARAMETERIZATION_MODES = {
    "entity_target",
    "property_target",
    "initial_sound_from_entity",
    "word_from_entity",
    "asset_catalog_target",
}
HANDOFF_SAFE_PARAMETERIZATION_MODES = {
    "entity_theme",
    *DYNAMIC_PARAMETERIZATION_MODES,
}
FIXED_PARAMETERIZATION_MODES = {"fixed", "entity_theme"}
ASSET_ROLES = {
    "entity",
    "activity_preview",
    "collection_correct",
    "collection_distractor",
    "badge",
    "story_scene",
    "ui_overlay",
}
REQUIREDNESS = {"required", "optional", "fallback"}
ACCURACY_MODES = {"illustrative", "reference_bound"}
STYLE_IDS = {"wonderlens_device_mint_soft_3d"}
SOURCE_STRATEGIES = {
    "generated_illustrative",
    "curated_original",
    "redraw_from_verified_data",
    "licensed_reference",
    "approved_internal_reference",
}
REFERENCE_SOURCE_STRATEGIES = {
    "curated_original",
    "redraw_from_verified_data",
    "licensed_reference",
    "approved_internal_reference",
}
TRANSFORMATION_POLICIES = {
    "generate_new",
    "crop_resize_only",
    "simplified_redraw",
    "style_preserving_redraw",
    "no_derivative_generation",
}
REFERENCE_TRANSFORMATION_POLICIES = {
    "crop_resize_only",
    "simplified_redraw",
    "style_preserving_redraw",
    "no_derivative_generation",
}
REFERENCE_SOURCE_TYPES = {
    "licensed_asset",
    "public_domain_reference",
    "approved_internal_reference",
    "verified_source_url",
}
RANDOM_REFERENCE_WORDS = ("random", "arbitrary", "made-up", "made up", "hallucinated")
MIN_REQUIRED_RUNTIME_EDGE = 512


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


def parse_size(value: Any) -> tuple[int, int] | None:
    text = norm(value)
    if "x" not in text:
        return None
    left, right = text.lower().split("x", 1)
    try:
        return int(left), int(right)
    except ValueError:
        return None


def add_required(issue_list: list[str], label: str, data: dict[str, Any], fields: tuple[str, ...]) -> None:
    for field in fields:
        if not norm(data.get(field)):
            issue_list.append(f"{label}: missing required field {field}")


def discover_package_dirs(roots: list[Path]) -> list[Path]:
    dirs: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        root = root.resolve()
        candidates: list[Path]
        if root.is_file():
            candidates = [root.parent]
        elif (root / "demo_support.yaml").exists() or (root / "asset_manifest.yaml").exists():
            candidates = [root]
        else:
            candidates = sorted(
                {
                    path.parent
                    for pattern in ("demo_support.yaml", "asset_manifest.yaml")
                    for path in root.rglob(pattern)
                    if "generated_assets_pilot" not in path.parts
                }
            )
        for candidate in candidates:
            if candidate not in seen:
                seen.add(candidate)
                dirs.append(candidate)
    return dirs


def validate_demo_support(package_dir: Path, data: dict[str, Any]) -> list[str]:
    label = str(package_dir)
    issues: list[str] = []
    add_required(issues, label, data, ("activity_id", "version", "demo_support"))
    support = as_dict(data.get("demo_support"))
    add_required(issues, f"{label}/demo_support", support, ("status", "ui_template", "support_level"))

    status = norm(support.get("status"))
    template = norm(support.get("ui_template"))
    if status and status not in DEMO_STATUSES:
        issues.append(f"{label}: demo_support.status {status!r} is not allowed")
    if template and template not in UI_TEMPLATES:
        issues.append(f"{label}: demo_support.ui_template {template!r} is not allowed")
    if status == "supported" and template == "cat5_judgment":
        issues.append(f"{label}: supported package must not use cat5_judgment ui_template")
    if template == "cat5_judgment" and status != "degraded":
        issues.append(f"{label}: cat5_judgment ui_template must be degraded")

    bindings = as_list(support.get("entity_bindings"))
    if status == "supported" and not bindings:
        issues.append(f"{label}: supported package must declare an entity binding")
    if status in {"supported", "degraded"} and template == "none":
        issues.append(f"{label}: {status} package must use a playable ui_template")
    if status == "unsupported" and template != "none":
        issues.append(f"{label}: unsupported package must use ui_template none")
    if status == "unsupported" and not as_list(support.get("unsupported_reasons")):
        issues.append(f"{label}: unsupported package must declare unsupported_reasons")
    if status == "degraded" and not as_list(support.get("degraded_reasons")):
        issues.append(f"{label}: degraded package must declare degraded_reasons")
    if status == "supported" and as_list(support.get("unsupported_reasons")):
        issues.append(f"{label}: supported package must not declare unsupported_reasons")

    default_count = 0
    for index, binding in enumerate(bindings):
        binding_data = as_dict(binding)
        binding_label = f"{label}: entity_bindings[{index}]"
        add_required(issues, binding_label, binding_data, ("entity_id", "display_label", "source_entity_exemplar"))
        if binding_data.get("default") is True:
            default_count += 1
    if bindings and default_count != 1:
        issues.append(f"{label}: entity_bindings must contain exactly one default binding")

    requires = as_dict(support.get("requires"))
    for field in ("generated_assets", "real_camera", "runtime_judgment", "device_round_screen"):
        if field not in requires:
            issues.append(f"{label}: demo_support.requires missing {field}")
        elif not isinstance(requires.get(field), bool):
            issues.append(f"{label}: demo_support.requires.{field} must be boolean")
    if status == "supported" and requires.get("runtime_judgment") is True:
        issues.append(f"{label}: supported package must not require runtime_judgment")

    return issues


def catalog_target_asset_count(asset_data: dict[str, Any]) -> int:
    return sum(
        1
        for asset in as_list(asset_data.get("assets"))
        if norm(as_dict(asset).get("role")) in {"collection_correct", "collection_distractor", "story_scene", "entity"}
    )


def validate_parameterization(package_dir: Path, demo_data: dict[str, Any], asset_data: dict[str, Any]) -> list[str]:
    label = str(package_dir)
    issues: list[str] = []
    support = as_dict(demo_data.get("demo_support"))
    status = norm(support.get("status"))
    compatibility = norm(demo_data.get("entity_compatibility"))
    raw_parameterization = demo_data.get("parameterization")
    parameterization = as_dict(raw_parameterization)

    if not compatibility:
        issues.append(f"{label}: entity_compatibility is required")
    elif compatibility not in ENTITY_COMPATIBILITY_VALUES:
        issues.append(f"{label}: entity_compatibility {compatibility!r} is not allowed")

    if status in {"supported", "degraded"} and not parameterization:
        issues.append(f"{label}: {status} package must declare parameterization")
        if compatibility == "agnostic":
            issues.append(f"{label}: entity_compatibility agnostic requires parameterization.mode")
        return issues
    if raw_parameterization is not None and not isinstance(raw_parameterization, dict):
        issues.append(f"{label}: parameterization must be a mapping")
        return issues
    if not parameterization:
        return issues

    mode = norm(parameterization.get("mode"))
    if not mode:
        issues.append(f"{label}: parameterization.mode is required")
    elif mode not in PARAMETERIZATION_MODES:
        issues.append(f"{label}: parameterization.mode {mode!r} is not allowed")

    if mode == "unsupported_until_parameterized" and status in {"supported", "degraded"}:
        issues.append(f"{label}: {status} package must not use unsupported_until_parameterized mode")
    if status == "unsupported" and mode in DYNAMIC_PARAMETERIZATION_MODES:
        issues.append(f"{label}: unsupported package must not claim dynamic parameterization mode {mode}")
    if compatibility == "agnostic":
        if not mode:
            issues.append(f"{label}: entity_compatibility agnostic requires parameterization.mode")
        elif mode not in HANDOFF_SAFE_PARAMETERIZATION_MODES:
            issues.append(f"{label}: entity_compatibility agnostic requires a non-fixed parameterization.mode")
    if compatibility == "unsupported" and mode and mode != "unsupported_until_parameterized":
        issues.append(f"{label}: entity_compatibility unsupported must use unsupported_until_parameterized mode")

    if not norm(parameterization.get("decision_source")):
        issues.append(f"{label}: parameterization.decision_source is required")
    if not norm(parameterization.get("integrity_status")):
        issues.append(f"{label}: parameterization.integrity_status is required")
    if not norm(parameterization.get("confidence")):
        issues.append(f"{label}: parameterization.confidence is required")
    if not as_list(parameterization.get("evidence")):
        issues.append(f"{label}: parameterization.evidence must include at least one item")
    if not norm(parameterization.get("reviewer_action")):
        issues.append(f"{label}: parameterization.reviewer_action is required")
    if not norm(parameterization.get("fallback_behavior")):
        issues.append(f"{label}: parameterization.fallback_behavior is required")

    validity = as_dict(parameterization.get("validity"))
    source_fields = as_dict(parameterization.get("source_fields"))
    derived_runtime_fields = as_dict(parameterization.get("derived_runtime_fields"))
    authored_constants = as_dict(parameterization.get("authored_constants"))

    if mode in DYNAMIC_PARAMETERIZATION_MODES:
        if not as_list(validity.get("requires")):
            issues.append(f"{label}: dynamic parameterization mode {mode} must declare validity.requires")
        if not source_fields:
            issues.append(f"{label}: dynamic parameterization mode {mode} must declare source_fields")
        if not derived_runtime_fields:
            issues.append(f"{label}: dynamic parameterization mode {mode} must declare derived_runtime_fields")
    if mode in FIXED_PARAMETERIZATION_MODES and not authored_constants:
        issues.append(f"{label}: {mode} parameterization mode must declare authored_constants")
    if mode == "initial_sound_from_entity":
        target_sound = norm(authored_constants.get("target_sound")).lower()
        if target_sound and target_sound != "dynamic":
            issues.append(f"{label}: initial_sound_from_entity must not hard-code authored_constants.target_sound")
    if mode == "asset_catalog_target" and catalog_target_asset_count(asset_data) == 0:
        issues.append(f"{label}: asset_catalog_target must declare target/catalog assets in asset_manifest.yaml")

    return issues


def validate_screen_targets(package_dir: Path, manifest: dict[str, Any]) -> list[str]:
    label = str(package_dir)
    issues: list[str] = []
    targets = as_dict(manifest.get("screen_targets"))
    round_target = as_dict(targets.get("round_device_screen"))
    if not round_target:
        issues.append(f"{label}: screen_targets.round_device_screen is required")
        return issues
    if norm(round_target.get("aspect_ratio")) != "1:1":
        issues.append(f"{label}: round_device_screen aspect_ratio must be 1:1")
    if norm(round_target.get("crop_shape")) != "circle":
        issues.append(f"{label}: round_device_screen crop_shape must be circle")
    safe_area = norm(round_target.get("safe_area")).lower()
    if "circle" not in safe_area or "percent" not in safe_area:
        issues.append(f"{label}: round_device_screen safe_area must describe a percent circle")
    if not norm(round_target.get("master_size")):
        issues.append(f"{label}: round_device_screen master_size is required")
    return issues


def validate_asset(package_dir: Path, asset: dict[str, Any], targets: dict[str, Any], index: int) -> list[str]:
    label = f"{package_dir}: assets[{index}]"
    issues: list[str] = []
    add_required(
        issues,
        label,
        asset,
        (
            "id",
            "role",
            "label",
            "requiredness",
            "accuracy_mode",
            "source_strategy",
            "transformation_policy",
            "fallback_behavior",
        ),
    )

    role = norm(asset.get("role"))
    requiredness = norm(asset.get("requiredness"))
    accuracy_mode = norm(asset.get("accuracy_mode"))
    source_strategy = norm(asset.get("source_strategy"))
    transformation_policy = norm(asset.get("transformation_policy"))
    if role and role not in ASSET_ROLES:
        issues.append(f"{label}: role {role!r} is not allowed")
    if requiredness and requiredness not in REQUIREDNESS:
        issues.append(f"{label}: requiredness {requiredness!r} is not allowed")
    if accuracy_mode and accuracy_mode not in ACCURACY_MODES:
        issues.append(f"{label}: accuracy_mode {accuracy_mode!r} is not allowed")
    if source_strategy and source_strategy not in SOURCE_STRATEGIES:
        issues.append(f"{label}: source_strategy {source_strategy!r} is not allowed")
    if transformation_policy and transformation_policy not in TRANSFORMATION_POLICIES:
        issues.append(f"{label}: transformation_policy {transformation_policy!r} is not allowed")
    if role in {"collection_correct", "collection_distractor"} and not norm(asset.get("collection_catalog_id")):
        issues.append(f"{label}: collection asset must declare collection_catalog_id")

    if accuracy_mode == "illustrative" and requiredness in {"required", "optional"}:
        if not norm(asset.get("prompt_en")):
            issues.append(f"{label}: illustrative required/optional asset must declare prompt_en")
        if source_strategy != "generated_illustrative":
            issues.append(f"{label}: illustrative required/optional asset must use source_strategy generated_illustrative")
        if transformation_policy != "generate_new":
            issues.append(f"{label}: illustrative required/optional asset must use transformation_policy generate_new")

    variants = as_list(asset.get("variants"))
    if requiredness in {"required", "optional"} and not variants:
        issues.append(f"{label}: required/optional asset must declare variants")
    has_high_resolution_variant = False
    for variant_index, variant in enumerate(variants):
        variant_data = as_dict(variant)
        variant_label = f"{label}.variants[{variant_index}]"
        add_required(issues, variant_label, variant_data, ("id", "target", "size"))
        target = norm(variant_data.get("target"))
        if target and target not in targets:
            issues.append(f"{variant_label}: target {target!r} is not declared in screen_targets")
        size = parse_size(variant_data.get("size"))
        if norm(variant_data.get("size")) and size is None:
            issues.append(f"{variant_label}: size must use WIDTHxHEIGHT pixels")
        elif size and min(size) >= MIN_REQUIRED_RUNTIME_EDGE:
            has_high_resolution_variant = True

    if requiredness == "required" and variants and not has_high_resolution_variant:
        issues.append(
            f"{label}: required asset must include at least one high-resolution runtime variant "
            f"with minimum edge >= {MIN_REQUIRED_RUNTIME_EDGE}px; thumbnails may only be secondary variants"
        )

    if accuracy_mode == "reference_bound":
        if source_strategy not in REFERENCE_SOURCE_STRATEGIES:
            issues.append(f"{label}: reference_bound asset must use an approved reference source_strategy")
        if transformation_policy not in REFERENCE_TRANSFORMATION_POLICIES:
            issues.append(f"{label}: reference_bound asset must not use generate_new transformation_policy")
        reference_policy = as_dict(asset.get("reference_policy"))
        sources = as_list(asset.get("sources"))
        if reference_policy.get("source_required") is not True:
            issues.append(f"{label}: reference_bound asset must set reference_policy.source_required true")
        if reference_policy.get("verification_required") is not True:
            issues.append(f"{label}: reference_bound asset must set reference_policy.verification_required true")
        allowed_sources = set(norm(source) for source in as_list(reference_policy.get("allowed_sources")))
        if not allowed_sources:
            issues.append(f"{label}: reference_bound asset must declare allowed_sources")
        elif not allowed_sources <= REFERENCE_SOURCE_TYPES:
            issues.append(f"{label}: reference_bound asset has unsupported allowed_sources")
        if not sources:
            issues.append(f"{label}: reference_bound asset must declare at least one source")
        for source_index, source in enumerate(sources):
            source_data = as_dict(source)
            add_required(issues, f"{label}.sources[{source_index}]", source_data, ("label", "uri", "license"))
        prompt = norm(asset.get("prompt_en")).lower()
        if any(word in prompt for word in RANDOM_REFERENCE_WORDS):
            issues.append(f"{label}: reference_bound asset prompt must not request random or arbitrary generation")

    return issues


def validate_asset_manifest(package_dir: Path, data: dict[str, Any]) -> list[str]:
    label = str(package_dir)
    issues: list[str] = []
    add_required(issues, label, data, ("activity_id", "entity_id", "version", "style_id", "palette", "screen_targets", "assets"))
    style_id = norm(data.get("style_id"))
    if style_id and style_id not in STYLE_IDS:
        issues.append(f"{label}: style_id {style_id!r} is not allowed")

    palette = as_dict(data.get("palette"))
    for field in ("shell", "screen", "primary_accent"):
        if not norm(palette.get(field)):
            issues.append(f"{label}: palette missing {field}")

    issues.extend(validate_screen_targets(package_dir, data))
    targets = as_dict(data.get("screen_targets"))
    for index, asset in enumerate(as_list(data.get("assets"))):
        issues.extend(validate_asset(package_dir, as_dict(asset), targets, index))
    return issues


def validate_package(package_dir: Path) -> list[str]:
    issues: list[str] = []
    demo_path = package_dir / "demo_support.yaml"
    asset_path = package_dir / "asset_manifest.yaml"
    demo_data = as_dict(load_yaml(demo_path)) if demo_path.exists() else {}
    asset_data = as_dict(load_yaml(asset_path)) if asset_path.exists() else {}

    if demo_path.exists():
        issues.extend(validate_demo_support(package_dir, demo_data))
        issues.extend(validate_parameterization(package_dir, demo_data, asset_data))
    if asset_path.exists():
        issues.extend(validate_asset_manifest(package_dir, asset_data))
    if demo_path.exists() != asset_path.exists():
        issues.append(f"{package_dir}: demo_support.yaml and asset_manifest.yaml should be paired")

    if demo_data and asset_data:
        demo_activity_id = norm(demo_data.get("activity_id"))
        asset_activity_id = norm(asset_data.get("activity_id"))
        if demo_activity_id and asset_activity_id and demo_activity_id != asset_activity_id:
            issues.append(f"{package_dir}: activity_id differs between demo_support.yaml and asset_manifest.yaml")

        support = as_dict(demo_data.get("demo_support"))
        status = norm(support.get("status"))
        requires = as_dict(support.get("requires"))
        if status in {"supported", "degraded"} and requires.get("generated_assets") is True:
            if not as_list(asset_data.get("assets")):
                issues.append(f"{package_dir}: {status} package requires generated assets but asset_manifest has none")
        if status == "unsupported" and as_list(support.get("degraded_reasons")):
            issues.append(f"{package_dir}: unsupported package should not use degraded_reasons")

    return issues


def validate_roots(roots: list[Path]) -> list[str]:
    package_dirs = discover_package_dirs(roots)
    issues: list[str] = []
    for package_dir in package_dirs:
        issues.extend(validate_package(package_dir))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path, help="Package dirs or roots containing demo extension files")
    args = parser.parse_args(argv)

    package_dirs = discover_package_dirs(args.roots)
    issues = validate_roots(args.roots)
    if issues:
        for issue in issues:
            print(f"FAIL {issue}")
        return 1
    print(f"OK demo package contract: {len(package_dirs)} package(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
