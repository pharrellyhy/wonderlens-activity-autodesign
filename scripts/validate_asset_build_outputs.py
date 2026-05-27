#!/usr/bin/env python3
"""Validate package-local runtime assets built from asset_manifest.yaml."""

from __future__ import annotations

import argparse
import hashlib
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

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "Pillow is required for runtime asset validation. Install Pillow or "
        "use the repo validation environment."
    ) from exc


BUILT_STATUSES = {"generated", "curated"}
FAILURE_STATUSES = {"missing_source", "qa_failed", "blocked", "skipped_fallback"}
ALLOWED_STATUSES = BUILT_STATUSES | FAILURE_STATUSES
ACCEPTED_REFERENCE_SOURCE_TYPES = {
    "approved_internal_reference",
    "licensed_asset",
    "public_domain_reference",
    "verified_source_url",
}
REJECTED_LICENSE_VALUES = {"", "unknown", "unverified", "none", "n/a", "random", "thumbnail"}
REFERENCE_METADATA_REQUIRED_FIELDS = (
    "source_label",
    "source_uri",
    "source_type",
    "license",
    "storage_allowed",
    "verification_status",
    "verification_notes",
    "source_original_path",
    "sha256",
    "verified_at",
    "reviewer_agent",
)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def discover_package_dirs(run_dir: Path) -> list[Path]:
    package_root = run_dir / "activity_packages"
    if not package_root.exists():
        return []
    return sorted(path.parent for path in package_root.rglob("asset_manifest.yaml"))


def safe_relative_path(value: Any, *, prefix: str = "") -> tuple[str, str]:
    text = norm(value)
    if not text:
        return "", "empty path"
    path = Path(text)
    if path.is_absolute():
        return text, "absolute path"
    if ".." in path.parts:
        return text, "path traversal"
    if prefix and (not path.parts or path.parts[0] != prefix.rstrip("/")):
        return text, f"path must be under {prefix}"
    return text, ""


def parse_size(value: Any) -> tuple[int, int] | None:
    text = norm(value)
    if "x" not in text:
        return None
    left, right = text.lower().split("x", 1)
    try:
        return int(left), int(right)
    except ValueError:
        return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_package_path(package_dir: Path, value: Any, *, prefix: str) -> tuple[Path | None, str, str]:
    text = norm(value)
    if not text:
        return None, text, "empty path"
    path = Path(text)
    if path.is_absolute():
        return None, text, "absolute path"
    if ".." in path.parts:
        return None, text, "path traversal"
    expected = tuple(part for part in Path(prefix).parts if part)
    if expected and path.parts[: len(expected)] != expected:
        return None, text, f"path must be under {prefix}"
    target = (package_dir / path).resolve()
    try:
        target.relative_to(package_dir.resolve())
    except ValueError:
        return None, text, "path escapes package"
    return target, text, ""


def allowed_reference_source_types(asset: dict[str, Any]) -> set[str]:
    policy = asset.get("reference_policy")
    if not isinstance(policy, dict):
        return set()
    allowed = policy.get("allowed_sources")
    if not isinstance(allowed, list):
        return set()
    return {norm(source) for source in allowed if norm(source)}


def validate_png(path: Path, expected_size: tuple[int, int] | None) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return [f"file does not exist at {path}"]
    try:
        with Image.open(path) as image:
            if image.format != "PNG":
                issues.append(f"{path}: expected PNG, found {image.format}")
            if expected_size and image.size != expected_size:
                issues.append(f"{path}: expected size {expected_size[0]}x{expected_size[1]}, found {image.size[0]}x{image.size[1]}")
    except Exception as exc:
        issues.append(f"{path}: could not inspect image: {exc}")
    return issues


def audit_entries_by_asset(run_dir: Path) -> dict[tuple[str, str], dict[str, Any]]:
    data = load_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")
    entries: dict[tuple[str, str], dict[str, Any]] = {}
    for entry in as_list(data.get("entries")):
        if not isinstance(entry, dict):
            continue
        key = (norm(entry.get("activity_id")), norm(entry.get("asset_id")))
        if key[0] and key[1]:
            entries[key] = entry
    return entries


def reference_entries_by_asset(run_dir: Path) -> dict[tuple[str, str], dict[str, Any]]:
    data = load_yaml(run_dir / "generated_assets" / "reference_sources.yaml")
    entries: dict[tuple[str, str], dict[str, Any]] = {}
    for entry in as_list(data.get("entries")):
        if not isinstance(entry, dict):
            continue
        key = (norm(entry.get("activity_id")), norm(entry.get("asset_id")))
        if key[0] and key[1]:
            entries[key] = entry
    return entries


def validate_reference_source(
    package_dir: Path,
    activity_id: str,
    asset: dict[str, Any],
    references: dict[tuple[str, str], dict[str, Any]],
) -> list[str]:
    asset_id = norm(asset.get("id"))
    label = f"{activity_id}/{asset_id}"
    issues: list[str] = []
    metadata_path = package_dir / "assets" / "sources" / f"{asset_id}__source_metadata.yaml"
    if not metadata_path.exists():
        issues.append(f"{label}: reference_bound built asset missing source metadata")
    else:
        metadata = load_yaml(metadata_path)
        for field in REFERENCE_METADATA_REQUIRED_FIELDS:
            value = metadata.get(field)
            if field == "storage_allowed":
                if value is not True:
                    issues.append(f"{label}: source metadata storage_allowed must be true")
            elif not norm(value):
                issues.append(f"{label}: source metadata missing {field}")
        source_type = norm(metadata.get("source_type"))
        if source_type not in ACCEPTED_REFERENCE_SOURCE_TYPES:
            issues.append(f"{label}: source metadata source_type {source_type!r} is not accepted")
        allowed_sources = allowed_reference_source_types(asset)
        if allowed_sources and source_type not in allowed_sources:
            issues.append(f"{label}: source metadata source_type {source_type!r} is not allowed by reference_policy")
        if norm(metadata.get("license")).lower() in REJECTED_LICENSE_VALUES:
            issues.append(f"{label}: source metadata license must be a verified license or approved internal reference")
        if norm(metadata.get("verification_status")) != "accepted":
            issues.append(f"{label}: source metadata verification_status must be accepted")
        if norm(metadata.get("activity_id")) and norm(metadata.get("activity_id")) != activity_id:
            issues.append(f"{label}: source metadata activity_id does not match manifest")
        if norm(metadata.get("asset_id")) and norm(metadata.get("asset_id")) != asset_id:
            issues.append(f"{label}: source metadata asset_id does not match asset")
        source_path, source_text, source_error = safe_package_path(
            package_dir,
            metadata.get("source_original_path"),
            prefix="assets/sources",
        )
        if source_error:
            issues.append(f"{label}: unsafe source_original_path {source_text!r}: {source_error}")
        elif source_path is None or not source_path.exists():
            issues.append(f"{label}: source_original_path does not exist at {source_text}")
        else:
            expected_sha = norm(metadata.get("sha256"))
            actual_sha = sha256_file(source_path)
            if expected_sha and expected_sha != actual_sha:
                issues.append(f"{label}: source metadata sha256 does not match source original")
    reference_entry = references.get((activity_id, asset_id))
    if not reference_entry:
        issues.append(f"{label}: missing reference_sources.yaml entry")
    elif reference_entry.get("status") != "accepted":
        issues.append(f"{label}: reference_sources status must be accepted")
    else:
        for field in ("source_type", "storage_allowed", "source_metadata_path", "source_original_path", "sha256"):
            if field == "storage_allowed":
                if reference_entry.get(field) is not True:
                    issues.append(f"{label}: reference_sources storage_allowed must be true")
            elif not norm(reference_entry.get(field)):
                issues.append(f"{label}: reference_sources missing {field}")
    return issues


def validate_asset(
    run_dir: Path,
    package_dir: Path,
    manifest: dict[str, Any],
    asset: dict[str, Any],
    audits: dict[tuple[str, str], dict[str, Any]],
    references: dict[tuple[str, str], dict[str, Any]],
) -> list[str]:
    activity_id = norm(manifest.get("activity_id")) or package_dir.name
    asset_id = norm(asset.get("id"))
    label = f"{activity_id}/{asset_id}"
    requiredness = norm(asset.get("requiredness"))
    accuracy_mode = norm(asset.get("accuracy_mode"))
    issues: list[str] = []
    built_paths: list[str] = []
    for variant in as_list(asset.get("variants")):
        if not isinstance(variant, dict):
            continue
        path_text = variant.get("path")
        if path_text in (None, ""):
            continue
        rel_path, path_error = safe_relative_path(path_text, prefix="assets")
        if path_error:
            issues.append(f"{label}: unsafe variant path {rel_path!r}: {path_error}")
            continue
        expected_size = parse_size(variant.get("size"))
        issues.extend(validate_png(package_dir / rel_path, expected_size))
        built_paths.append(rel_path)

    audit = audits.get((activity_id, asset_id))
    if not audit:
        issues.append(f"{label}: missing asset_outputs.yaml entry")
    else:
        status = norm(audit.get("status"))
        if status not in ALLOWED_STATUSES:
            issues.append(f"{label}: asset_outputs status {status!r} is not allowed")
        for output in as_list(audit.get("output_variants")):
            if not isinstance(output, dict):
                continue
            rel_path, path_error = safe_relative_path(output.get("path"), prefix="assets")
            if path_error:
                issues.append(f"{label}: unsafe audit output path {rel_path!r}: {path_error}")
            elif not (package_dir / rel_path).exists():
                issues.append(f"{label}: audit output path does not exist at {rel_path}")
        work_item, work_error = safe_relative_path(audit.get("work_item_path"), prefix="generated_assets")
        if work_error:
            issues.append(f"{label}: unsafe work_item_path {work_item!r}: {work_error}")
        elif not (run_dir / work_item).exists():
            issues.append(f"{label}: work item does not exist at {work_item}")

    if requiredness == "required" and not built_paths:
        issues.append(f"{label}: required asset has no built variant path")
    if built_paths and accuracy_mode == "reference_bound":
        issues.extend(validate_reference_source(package_dir, activity_id, asset, references))
    return issues


def validate_no_absolute_contract_paths(run_dir: Path) -> list[str]:
    issues: list[str] = []
    for path in [
        run_dir / "generated_assets" / "asset_outputs.yaml",
        run_dir / "generated_assets" / "reference_sources.yaml",
        run_dir / "generated_assets" / "qa_notes.yaml",
    ] + [p for d in discover_package_dirs(run_dir) for p in [d / "asset_manifest.yaml"]]:
        if not path.exists():
            continue
        text = path.read_text()
        if "/Users/" in text or "file://" in text:
            issues.append(f"{path}: contains unsafe absolute local path")
    return issues


def validate_run(run_dir: Path) -> list[str]:
    run_dir = run_dir.resolve()
    issues: list[str] = []
    package_dirs = discover_package_dirs(run_dir)
    if not package_dirs:
        issues.append(f"{run_dir}: no activity package asset manifests found")
        return issues
    asset_outputs_path = run_dir / "generated_assets" / "asset_outputs.yaml"
    reference_sources_path = run_dir / "generated_assets" / "reference_sources.yaml"
    qa_notes_path = run_dir / "generated_assets" / "qa_notes.yaml"
    for path in (asset_outputs_path, reference_sources_path, qa_notes_path):
        if not path.exists():
            issues.append(f"{run_dir}: missing {path.relative_to(run_dir)}")
    audits = audit_entries_by_asset(run_dir)
    references = reference_entries_by_asset(run_dir)
    for package_dir in package_dirs:
        manifest = load_yaml(package_dir / "asset_manifest.yaml")
        for asset in as_list(manifest.get("assets")):
            if isinstance(asset, dict):
                issues.extend(validate_asset(run_dir, package_dir, manifest, asset, audits, references))
    issues.extend(validate_no_absolute_contract_paths(run_dir))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    args = parser.parse_args(argv)
    issues = validate_run(args.run_dir)
    if issues:
        for issue in issues:
            print(f"FAIL {issue}")
        return 1
    print(f"OK asset build outputs: {args.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
