#!/usr/bin/env python3
"""Validate full-pass activity packages have fullstack-style asset bundles."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyYAML is required. Install pyyaml or run from the repo environment "
        "used for activity metadata validation."
    ) from exc


STANDARD_REQUIRED_ASSETS = [
    ("activity_icon", "activity_preview"),
    ("intro_scene", "story_scene"),
    ("rules_scene", "story_scene"),
    ("round_1_scene", "story_scene"),
    ("round_2_scene", "story_scene"),
    ("round_3_scene", "story_scene"),
    ("celebrate_scene", "story_scene"),
    ("closing_scene", "story_scene"),
]
SYNTHESIS_REQUIRED_ASSET = ("synthesis_scene", "story_scene")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def discover_package_dirs(run_dir: Path) -> list[Path]:
    package_root = run_dir / "activity_packages"
    if not package_root.exists():
        return []
    return sorted(path.parent for path in package_root.rglob("asset_manifest.yaml"))


def package_relative(package_dir: Path, path: Path) -> str:
    return path.resolve().relative_to(package_dir.resolve()).as_posix()


def asset_by_id(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    assets = manifest.get("assets", [])
    if not isinstance(assets, list):
        return {}
    return {
        norm(asset.get("id")): asset
        for asset in assets
        if isinstance(asset, dict) and norm(asset.get("id"))
    }


def variant_paths(asset: dict[str, Any]) -> list[str]:
    variants = asset.get("variants", [])
    if not isinstance(variants, list):
        return []
    return [
        norm(variant.get("path"))
        for variant in variants
        if isinstance(variant, dict) and norm(variant.get("path"))
    ]


def needs_synthesis_scene(package_dir: Path) -> bool:
    tag_block = load_yaml(package_dir / "tag_block.yaml")
    template_type = norm(tag_block.get("template_type")).lower()
    if template_type == "cat5":
        return True
    prod_text = (package_dir / "prod.md").read_text() if (package_dir / "prod.md").exists() else ""
    return "synthesis" in prod_text.lower()


def required_assets_for_package(package_dir: Path) -> list[tuple[str, str]]:
    required = list(STANDARD_REQUIRED_ASSETS)
    if needs_synthesis_scene(package_dir):
        required.insert(-2, SYNTHESIS_REQUIRED_ASSET)
    return required


def validate_package(package_dir: Path) -> list[dict[str, Any]]:
    manifest_path = package_dir / "asset_manifest.yaml"
    manifest = load_yaml(manifest_path)
    activity_id = norm(manifest.get("activity_id")) or package_dir.name
    assets = asset_by_id(manifest)
    issues: list[dict[str, Any]] = []

    for asset_id, expected_role in required_assets_for_package(package_dir):
        asset = assets.get(asset_id)
        if not asset:
            issues.append(
                {
                    "activity_id": activity_id,
                    "package_path": package_dir.as_posix(),
                    "kind": "missing_required_asset",
                    "missing_asset_id": asset_id,
                    "expected_role": expected_role,
                    "repair": "Declare and build a separate 512x512 package-local PNG for this fullstack-style beat asset.",
                }
            )
            continue
        role = norm(asset.get("role"))
        if role != expected_role:
            issues.append(
                {
                    "activity_id": activity_id,
                    "package_path": package_dir.as_posix(),
                    "kind": "wrong_required_asset_role",
                    "asset_id": asset_id,
                    "actual_role": role,
                    "expected_role": expected_role,
                    "repair": "Use the standard role so consumers can map the asset into icon, beat scene, item, or badge surfaces.",
                }
            )
        paths = variant_paths(asset)
        if not paths:
            issues.append(
                {
                    "activity_id": activity_id,
                    "package_path": package_dir.as_posix(),
                    "kind": "missing_required_asset_path",
                    "asset_id": asset_id,
                    "expected_role": expected_role,
                    "repair": "Run the asset build so the required variant path points at a package-local PNG.",
                }
            )
            continue
        missing_paths = [
            path
            for path in paths
            if not (package_dir / path).exists()
        ]
        for path in missing_paths:
            issues.append(
                {
                    "activity_id": activity_id,
                    "package_path": package_dir.as_posix(),
                    "kind": "required_asset_file_missing",
                    "asset_id": asset_id,
                    "path": path,
                    "expected_role": expected_role,
                    "repair": "Generate or copy the 512x512 PNG, then rebuild the package-local asset variants.",
                }
            )

    return issues


def validate_run(run_dir: Path) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    for package_dir in discover_package_dirs(run_dir):
        issues.extend(validate_package(package_dir))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    parser.add_argument("--report-yaml", type=Path, default=None)
    args = parser.parse_args(argv)

    issues = validate_run(args.run_dir)
    if args.report_yaml is not None:
        args.report_yaml.parent.mkdir(parents=True, exist_ok=True)
        args.report_yaml.write_text(
            yaml.safe_dump(
                {
                    "run_id": args.run_dir.name,
                    "issue_count": len(issues),
                    "issues": issues,
                },
                sort_keys=False,
                allow_unicode=False,
            )
        )

    if issues:
        print(f"FAIL full-pass asset bundle: {len(issues)} issue(s)")
        for issue in issues[:50]:
            activity_id = issue["activity_id"]
            kind = issue["kind"]
            asset_id = issue.get("missing_asset_id") or issue.get("asset_id")
            print(f"FAIL {activity_id}/{asset_id}: {kind}")
        if len(issues) > 50:
            print(f"... {len(issues) - 50} more issue(s)")
        return 1

    print(f"OK full-pass asset bundle: {args.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
