#!/usr/bin/env python3
"""Build package-local runtime assets from asset_manifest.yaml files.

This script is the deterministic half of the agent-assisted asset workflow. It
prepares work items, consumes already generated/curated source PNGs, writes
package-local runtime variants, and records run-level audit files. Agents remain
responsible for the judgment-heavy work: image generation, source research, and
visual QA.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
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
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "Pillow is required for runtime asset variant resizing. Install Pillow "
        "or use the repo validation environment."
    ) from exc


SUPPORTED_MODES = {"generate_illustrative", "curate_reference", "generate_and_curate"}
SAFE_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]*$")
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
REFERENCE_TRANSFORM_REQUIRES_CURATED_VARIANT = {"simplified_redraw", "style_preserving_redraw"}
DERIVABLE_REFERENCE_TRANSFORMS = {"crop_resize_only", "no_derivative_generation"}
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".webp")


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


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_relative(run_dir: Path, path: Path) -> str:
    return path.resolve().relative_to(run_dir.resolve()).as_posix()


def package_relative(package_dir: Path, path: Path) -> str:
    return path.resolve().relative_to(package_dir.resolve()).as_posix()


def parse_size(value: Any) -> tuple[int, int]:
    text = norm(value)
    if "x" not in text:
        raise ValueError(f"invalid variant size {text!r}")
    width, height = text.lower().split("x", 1)
    return int(width), int(height)


def validate_safe_id(value: Any, label: str) -> str:
    text = norm(value)
    if not SAFE_ID_PATTERN.fullmatch(text):
        raise ValueError(f"unsafe {label}: {text!r}")
    return text


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


def discover_package_dirs(run_dir: Path) -> list[Path]:
    package_root = run_dir / "activity_packages"
    if not package_root.exists():
        return []
    return sorted(path.parent for path in package_root.rglob("asset_manifest.yaml"))


def safe_output_path(package_dir: Path, asset_id: str, variant_id: str) -> Path:
    asset_id = validate_safe_id(asset_id, "asset id")
    variant_id = validate_safe_id(variant_id, "variant id")
    return package_dir / "assets" / f"{asset_id}__{variant_id}.png"


def asset_source_dir(package_dir: Path) -> Path:
    return package_dir / "assets" / "sources"


def find_image(candidates: list[Path]) -> Path | None:
    for candidate in candidates:
        if candidate.is_file():
            return candidate
        for suffix in IMAGE_SUFFIXES:
            suffixed = candidate.with_suffix(suffix)
            if suffixed.is_file():
                return suffixed
    return None


def illustrative_input_path(run_dir: Path, activity_id: str, asset_id: str) -> Path | None:
    activity_id = validate_safe_id(activity_id, "activity id")
    asset_id = validate_safe_id(asset_id, "asset id")
    inbox = run_dir / "generated_assets" / "inbox" / activity_id
    return find_image(
        [
            inbox / asset_id,
            inbox / f"{asset_id}__master",
            inbox / f"{asset_id}__source",
        ]
    )


def reference_original_path(package_dir: Path, asset_id: str) -> Path | None:
    asset_id = validate_safe_id(asset_id, "asset id")
    source_dir = asset_source_dir(package_dir)
    return find_image(
        [
            source_dir / f"{asset_id}__source_original",
            source_dir / f"{asset_id}__source",
        ]
    )


def curated_reference_variant_input(run_dir: Path, activity_id: str, asset_id: str) -> Path | None:
    activity_id = validate_safe_id(activity_id, "activity id")
    asset_id = validate_safe_id(asset_id, "asset id")
    inbox = run_dir / "generated_assets" / "inbox" / activity_id
    return find_image(
        [
            inbox / f"{asset_id}__curated",
            inbox / f"{asset_id}__redraw",
            inbox / asset_id,
        ]
    )


def resize_png(source: Path, target: Path, size: tuple[int, int], *, force: bool = False) -> bool:
    if target.exists() and not force:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = image.convert("RGBA")
        image = image.resize(size, Image.Resampling.LANCZOS)
        image.save(target, format="PNG")
    return True


def write_work_item(
    run_dir: Path,
    package_dir: Path,
    manifest: dict[str, Any],
    asset: dict[str, Any],
    mode: str,
) -> str:
    activity_id = validate_safe_id(norm(manifest.get("activity_id")) or package_dir.name, "activity id")
    asset_id = validate_safe_id(asset.get("id"), "asset id")
    work_path = run_dir / "generated_assets" / "work_items" / f"{activity_id}__{asset_id}.md"
    variants = "\n".join(
        f"- `{norm(variant.get('id'))}`: {norm(variant.get('target'))}, {norm(variant.get('size'))}"
        for variant in asset.get("variants", [])
        if isinstance(variant, dict)
    )
    sources = "\n".join(
        f"- {norm(source.get('label'))}: {norm(source.get('uri'))} ({norm(source.get('license'))})"
        for source in asset.get("sources", [])
        if isinstance(source, dict)
    )
    if not sources:
        sources = "- None declared"
    guidance = (
        "Generate one source PNG into "
        f"`generated_assets/inbox/{activity_id}/{asset_id}.png` using the prompt and device style."
        if norm(asset.get("accuracy_mode")) == "illustrative"
        else "Verify the source, store the accepted original in package-local "
        f"`assets/sources/{asset_id}__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one."
    )
    body = f"""# Asset Work Item: {activity_id}/{asset_id}

Mode: `{mode}`
Package: `{run_relative(run_dir, package_dir)}`
Role: `{norm(asset.get('role'))}`
Requiredness: `{norm(asset.get('requiredness'))}`
Accuracy mode: `{norm(asset.get('accuracy_mode'))}`
Source strategy: `{norm(asset.get('source_strategy'))}`
Transformation policy: `{norm(asset.get('transformation_policy'))}`

## Prompt Or Source Requirement

{norm(asset.get('prompt_en')) or 'No prompt recorded.'}

## Declared Sources

{sources}

## Variants

{variants or '- No variants declared'}

## Agent Instructions

{guidance}

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
"""
    work_path.parent.mkdir(parents=True, exist_ok=True)
    work_path.write_text(body)
    return run_relative(run_dir, work_path)


def variant_entry(asset: dict[str, Any], variant: dict[str, Any], output_path: Path, package_dir: Path) -> dict[str, Any]:
    return {
        "variant_id": norm(variant.get("id")),
        "path": package_relative(package_dir, output_path),
        "size": norm(variant.get("size")),
        "sha256": sha256_file(output_path) if output_path.exists() else "",
        "byte_count": output_path.stat().st_size if output_path.exists() else 0,
        "mime_type": "image/png" if output_path.exists() else "",
        "source_asset_id": norm(asset.get("id")),
    }


def update_variant_path(variant: dict[str, Any], package_dir: Path, output_path: Path) -> None:
    variant["path"] = package_relative(package_dir, output_path)


def first_source(asset: dict[str, Any]) -> dict[str, Any]:
    sources = asset.get("sources", [])
    if isinstance(sources, list):
        for source in sources:
            if isinstance(source, dict):
                return source
    return {}


def allowed_reference_source_types(asset: dict[str, Any]) -> set[str]:
    policy = asset.get("reference_policy")
    if not isinstance(policy, dict):
        return set()
    allowed = policy.get("allowed_sources")
    if not isinstance(allowed, list):
        return set()
    return {norm(source) for source in allowed if norm(source)}


def accepted_reference_source(
    run_dir: Path,
    package_dir: Path,
    manifest: dict[str, Any],
    asset: dict[str, Any],
) -> tuple[Path | None, str, dict[str, Any] | None, list[str]]:
    activity_id = validate_safe_id(norm(manifest.get("activity_id")) or package_dir.name, "activity id")
    asset_id = validate_safe_id(asset.get("id"), "asset id")
    metadata_path = asset_source_dir(package_dir) / f"{asset_id}__source_metadata.yaml"
    if not metadata_path.exists():
        return None, "", None, [f"Missing accepted source metadata at {package_relative(package_dir, metadata_path)}."]

    metadata = load_yaml(metadata_path)
    issues: list[str] = []
    for field in REFERENCE_METADATA_REQUIRED_FIELDS:
        value = metadata.get(field)
        if field == "storage_allowed":
            if value is not True:
                issues.append("source metadata storage_allowed must be true")
        elif not norm(value):
            issues.append(f"source metadata missing {field}")

    source_type = norm(metadata.get("source_type"))
    if source_type not in ACCEPTED_REFERENCE_SOURCE_TYPES:
        issues.append(f"source metadata source_type {source_type!r} is not accepted")
    allowed_sources = allowed_reference_source_types(asset)
    if allowed_sources and source_type not in allowed_sources:
        issues.append(f"source metadata source_type {source_type!r} is not allowed by reference_policy")
    license_name = norm(metadata.get("license"))
    if license_name.lower() in REJECTED_LICENSE_VALUES:
        issues.append("source metadata license must be a verified license or approved internal reference")
    if norm(metadata.get("verification_status")) != "accepted":
        issues.append("source metadata verification_status must be accepted")
    if norm(metadata.get("activity_id")) and norm(metadata.get("activity_id")) != activity_id:
        issues.append("source metadata activity_id does not match manifest")
    if norm(metadata.get("asset_id")) and norm(metadata.get("asset_id")) != asset_id:
        issues.append("source metadata asset_id does not match asset")

    source_original, source_original_path, source_path_error = safe_package_path(
        package_dir,
        metadata.get("source_original_path"),
        prefix="assets/sources",
    )
    if source_path_error:
        issues.append(f"unsafe source_original_path {source_original_path!r}: {source_path_error}")
    elif source_original is None or not source_original.exists():
        issues.append(f"source_original_path does not exist at {source_original_path}")
    else:
        expected_sha = norm(metadata.get("sha256"))
        actual_sha = sha256_file(source_original)
        if expected_sha and expected_sha != actual_sha:
            issues.append("source metadata sha256 does not match source original")

    if issues:
        return None, "", None, issues

    assert source_original is not None
    source_reference = {
        "activity_id": activity_id,
        "asset_id": asset_id,
        "status": "accepted",
        "source_label": norm(metadata.get("source_label")),
        "source_uri": norm(metadata.get("source_uri")),
        "source_type": source_type,
        "license": license_name,
        "storage_allowed": bool(metadata.get("storage_allowed")),
        "source_original_path": source_original_path,
        "source_metadata_path": package_relative(package_dir, metadata_path),
        "sha256": norm(metadata.get("sha256")),
        "verified_at": norm(metadata.get("verified_at")),
        "reviewer_agent": norm(metadata.get("reviewer_agent")),
        "verification_notes": norm(metadata.get("verification_notes")),
    }
    return source_original, run_relative(run_dir, metadata_path), source_reference, []


def mode_allows(asset: dict[str, Any], mode: str) -> bool:
    accuracy = norm(asset.get("accuracy_mode"))
    if mode == "generate_and_curate":
        return accuracy in {"illustrative", "reference_bound"}
    if mode == "generate_illustrative":
        return accuracy == "illustrative"
    if mode == "curate_reference":
        return accuracy == "reference_bound"
    return False


def build_asset(
    run_dir: Path,
    package_dir: Path,
    manifest: dict[str, Any],
    asset: dict[str, Any],
    mode: str,
    *,
    force: bool,
) -> tuple[dict[str, Any], dict[str, Any] | None, bool]:
    activity_id = validate_safe_id(norm(manifest.get("activity_id")) or package_dir.name, "activity id")
    asset_id = validate_safe_id(asset.get("id"), "asset id")
    requiredness = norm(asset.get("requiredness"))
    accuracy = norm(asset.get("accuracy_mode"))
    transformation_policy = norm(asset.get("transformation_policy"))
    work_item_path = write_work_item(run_dir, package_dir, manifest, asset, mode)
    output_variants: list[dict[str, Any]] = []
    qa_notes: list[str] = []
    source_reference: dict[str, Any] | None = None

    status = "skipped_fallback"
    source_image: Path | None = None
    source_metadata_path = ""
    if not mode_allows(asset, mode):
        qa_notes.append(f"Skipped because mode {mode} does not build {accuracy} assets.")
    elif accuracy == "illustrative":
        source_image = illustrative_input_path(run_dir, activity_id, asset_id)
        if source_image is None:
            status = "missing_source"
            qa_notes.append(
                f"Missing generated illustrative source in generated_assets/inbox/{activity_id}/{asset_id}.png."
            )
        else:
            status = "generated"
    elif accuracy == "reference_bound":
        source_original, source_metadata_path, source_reference, source_issues = accepted_reference_source(
            run_dir,
            package_dir,
            manifest,
            asset,
        )
        if source_original is None:
            status = "missing_source"
            qa_notes.extend(source_issues or [f"Missing accepted source original under assets/sources for {asset_id}."])
        else:
            if transformation_policy in DERIVABLE_REFERENCE_TRANSFORMS:
                source_image = source_original
                status = "curated"
            elif transformation_policy in REFERENCE_TRANSFORM_REQUIRES_CURATED_VARIANT:
                source_image = curated_reference_variant_input(run_dir, activity_id, asset_id)
                if source_image is None:
                    status = "blocked"
                    qa_notes.append(
                        f"{transformation_policy} requires an agent-curated variant in generated_assets/inbox/{activity_id}/{asset_id}__curated.png."
                    )
                else:
                    status = "curated"
            else:
                status = "blocked"
                qa_notes.append(f"Unsupported reference transformation policy: {transformation_policy}.")
    else:
        status = "blocked"
        qa_notes.append(f"Unsupported accuracy_mode: {accuracy}.")

    if source_image is not None and status in {"generated", "curated"}:
        for variant in asset.get("variants", []):
            if not isinstance(variant, dict):
                continue
            variant_id = norm(variant.get("id"))
            output_path = safe_output_path(package_dir, asset_id, variant_id)
            try:
                wrote = resize_png(source_image, output_path, parse_size(variant.get("size")), force=force)
            except Exception as exc:  # pragma: no cover - defensive guard
                status = "qa_failed"
                qa_notes.append(f"Could not create {variant_id}: {exc}")
                continue
            update_variant_path(variant, package_dir, output_path)
            output_variants.append(variant_entry(asset, variant, output_path, package_dir))
        if not output_variants:
            status = "qa_failed"
            qa_notes.append("No runtime variants were produced.")

    failed_required = requiredness == "required" and status not in {"generated", "curated"}
    output_entry = {
        "activity_id": activity_id,
        "asset_id": asset_id,
        "role": norm(asset.get("role")),
        "accuracy_mode": accuracy,
        "requiredness": requiredness,
        "source_strategy": norm(asset.get("source_strategy")),
        "transformation_policy": transformation_policy,
        "status": status,
        "package_path": run_relative(run_dir, package_dir),
        "work_item_path": work_item_path,
        "output_variants": output_variants,
        "source_metadata_path": source_metadata_path,
        "qa_notes": qa_notes or ["Built package-local runtime asset variants."],
    }
    return output_entry, source_reference, failed_required


def validate_packages_before_build(package_dirs: list[Path]) -> list[str]:
    try:
        import validate_demo_package_contract as contract
    except ImportError:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import validate_demo_package_contract as contract  # type: ignore

    issues: list[str] = []
    for package_dir in package_dirs:
        issues.extend(contract.validate_package(package_dir))
    return issues


def validate_manifest_safety(package_dirs: list[Path]) -> None:
    for package_dir in package_dirs:
        manifest = load_yaml(package_dir / "asset_manifest.yaml")
        validate_safe_id(norm(manifest.get("activity_id")) or package_dir.name, "activity id")
        assets = manifest.get("assets", [])
        if not isinstance(assets, list):
            continue
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            validate_safe_id(asset.get("id"), "asset id")
            variants = asset.get("variants", [])
            if not isinstance(variants, list):
                continue
            for variant in variants:
                if isinstance(variant, dict):
                    validate_safe_id(variant.get("id"), "variant id")


def build_assets(run_dir: Path, mode: str = "generate_and_curate", *, force: bool = False) -> dict[str, Any]:
    if mode not in SUPPORTED_MODES:
        raise ValueError(f"unsupported asset build mode: {mode}")
    run_dir = run_dir.resolve()
    package_dirs = discover_package_dirs(run_dir)
    contract_issues = validate_packages_before_build(package_dirs)
    if contract_issues:
        raise ValueError("demo package contract validation failed:\n" + "\n".join(contract_issues))
    validate_manifest_safety(package_dirs)

    entries: list[dict[str, Any]] = []
    source_entries: list[dict[str, Any]] = []
    qa_entries: list[dict[str, Any]] = []
    required_failures = 0
    built_count = 0
    for package_dir in package_dirs:
        manifest_path = package_dir / "asset_manifest.yaml"
        manifest = load_yaml(manifest_path)
        changed = False
        for asset in manifest.get("assets", []):
            if not isinstance(asset, dict):
                continue
            entry, source_entry, failed_required = build_asset(
                run_dir,
                package_dir,
                manifest,
                asset,
                mode,
                force=force,
            )
            entries.append(entry)
            qa_entries.append(
                {
                    "activity_id": entry["activity_id"],
                    "asset_id": entry["asset_id"],
                    "status": entry["status"],
                    "qa_notes": entry["qa_notes"],
                }
            )
            if source_entry is not None:
                source_entries.append(source_entry)
            if entry["status"] in {"generated", "curated"}:
                built_count += 1
                changed = True
            if failed_required:
                required_failures += 1
        if changed:
            write_yaml(manifest_path, manifest)

    output_root = run_dir / "generated_assets"
    output_root.mkdir(parents=True, exist_ok=True)
    asset_outputs = {
        "run_id": run_dir.name,
        "asset_build_mode": mode,
        "generated_at": now_iso(),
        "package_count": len(package_dirs),
        "asset_count": len(entries),
        "built_count": built_count,
        "required_failures": required_failures,
        "entries": entries,
    }
    reference_sources = {
        "run_id": run_dir.name,
        "asset_build_mode": mode,
        "generated_at": now_iso(),
        "entries": source_entries,
    }
    qa_notes = {
        "run_id": run_dir.name,
        "asset_build_mode": mode,
        "generated_at": now_iso(),
        "entries": qa_entries,
    }
    write_yaml(output_root / "asset_outputs.yaml", asset_outputs)
    write_yaml(output_root / "reference_sources.yaml", reference_sources)
    write_yaml(output_root / "qa_notes.yaml", qa_notes)

    result = {
        "run_id": run_dir.name,
        "mode": mode,
        "package_count": len(package_dirs),
        "asset_count": len(entries),
        "built": built_count,
        "required_failures": required_failures,
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    parser.add_argument(
        "--mode",
        choices=sorted(SUPPORTED_MODES),
        default="generate_and_curate",
        help="Asset build mode to execute.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing package-local runtime assets.")
    args = parser.parse_args(argv)

    try:
        result = build_assets(args.run_dir, mode=args.mode, force=args.force)
    except Exception as exc:
        print(f"FAIL asset build: {exc}", file=sys.stderr)
        return 1
    print(
        "OK asset build: "
        f"mode={result['mode']} packages={result['package_count']} "
        f"assets={result['asset_count']} built={result['built']} "
        f"required_failures={result['required_failures']}"
    )
    return 1 if result["required_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
