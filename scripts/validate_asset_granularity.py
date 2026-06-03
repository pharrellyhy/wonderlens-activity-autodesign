#!/usr/bin/env python3
"""Validate that runtime assets are split into usable visual units."""

from __future__ import annotations

import argparse
import re
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


COMPOSITE_ID_PATTERNS = (
    re.compile(r"(^|_)cards(_|$)"),
    re.compile(r"(^|_)card_set(_|$)"),
    re.compile(r"(^|_)set(_|$)"),
    re.compile(r"(^|_)library(_|$)"),
    re.compile(r"(^|_)board(_|$)"),
    re.compile(r"(^|_)ui(_|$)"),
)
COMPOSITE_TEXT_PATTERNS = (
    re.compile(r"\bcards\b", re.IGNORECASE),
    re.compile(r"\bcard set\b", re.IGNORECASE),
    re.compile(r"\bset of\b", re.IGNORECASE),
    re.compile(r"\bcollection of\b", re.IGNORECASE),
    re.compile(r"\blibrary\b", re.IGNORECASE),
    re.compile(r"\bmultiple\b", re.IGNORECASE),
    re.compile(r"\bseveral\b", re.IGNORECASE),
)
STANDARD_BEAT_ASSET_IDS = {
    "activity_icon",
    "intro_scene",
    "rules_scene",
    "round_1_scene",
    "round_2_scene",
    "round_3_scene",
    "synthesis_scene",
    "celebrate_scene",
    "closing_scene",
}
ITEM_ASSET_ROLES = {"collection_correct", "collection_distractor"}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def discover_package_dirs(run_dir: Path) -> list[Path]:
    package_root = run_dir / "activity_packages"
    if not package_root.exists():
        return []
    return sorted(path.parent for path in package_root.rglob("asset_manifest.yaml"))


def display_reference_count(prod_text: str, asset_id: str) -> int:
    return len(re.findall(rf"Use `{re.escape(asset_id)}`", prod_text))


def composite_reasons(asset: dict[str, Any]) -> list[str]:
    asset_id = norm(asset.get("id"))
    label = norm(asset.get("label"))
    prompt = norm(asset.get("prompt_en"))
    haystack = " ".join([label, prompt])
    reasons: list[str] = []
    for pattern in COMPOSITE_ID_PATTERNS:
        if pattern.search(asset_id):
            reasons.append(f"asset id looks composite: {asset_id}")
            break
    if asset_id not in STANDARD_BEAT_ASSET_IDS:
        for pattern in COMPOSITE_TEXT_PATTERNS:
            if pattern.search(haystack):
                reasons.append(f"asset label/prompt uses composite wording: {pattern.pattern}")
                break
    return reasons


def item_path_reasons(asset: dict[str, Any]) -> list[str]:
    if norm(asset.get("role")) not in ITEM_ASSET_ROLES:
        return []
    reasons: list[str] = []
    for variant in asset.get("variants", []):
        if not isinstance(variant, dict):
            continue
        path = norm(variant.get("path"))
        if path and not path.startswith("assets/items/"):
            reasons.append(f"collection item variant path is not under assets/items/: {path}")
    return reasons


def validate_package(package_dir: Path) -> list[dict[str, Any]]:
    manifest = load_yaml(package_dir / "asset_manifest.yaml")
    activity_id = norm(manifest.get("activity_id")) or package_dir.name
    prod_path = package_dir / "prod.md"
    prod_text = prod_path.read_text() if prod_path.exists() else ""
    issues: list[dict[str, Any]] = []
    for asset in manifest.get("assets", []):
        if not isinstance(asset, dict):
            continue
        asset_id = norm(asset.get("id"))
        if not asset_id:
            continue
        reasons = composite_reasons(asset) + item_path_reasons(asset)
        display_count = display_reference_count(prod_text, asset_id)
        if reasons and display_count >= 3 and len(manifest.get("assets", [])) == 1:
            reasons.append(
                "single asset is reused across three or more runtime display references"
            )
        if reasons:
            issues.append(
                {
                    "activity_id": activity_id,
                    "asset_id": asset_id,
                    "role": norm(asset.get("role")),
                    "requiredness": norm(asset.get("requiredness")),
                    "display_reference_count": display_count,
                    "reasons": reasons,
                    "repair": (
                        "split into one 512x512 runtime asset per scene, object, item, "
                        "character, icon, badge, or distractor used by the activity beat"
                    ),
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
        print(f"FAIL asset granularity: {len(issues)} issue(s)")
        for issue in issues:
            reasons = "; ".join(issue["reasons"])
            print(f"FAIL {issue['activity_id']}/{issue['asset_id']}: {reasons}")
        return 1
    print(f"OK asset granularity: {args.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
