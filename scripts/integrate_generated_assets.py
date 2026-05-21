#!/usr/bin/env python3
"""Bind generated prebuilt asset files to run-local activity packages."""

from __future__ import annotations

import argparse
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


PACKAGE_FILES = (
    "spec.md",
    "prod.md",
    "tag_block.yaml",
    "recap.template.yaml",
    "dashboard.template.yaml",
)

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


def run_relative(run_dir: Path, value: Any) -> str:
    text = norm(value)
    if not text:
        return ""
    path = Path(text)
    if path.is_absolute():
        try:
            return path.resolve().relative_to(run_dir.resolve()).as_posix()
        except ValueError:
            return path.as_posix()
    run_prefix = f"runs/{run_dir.name}/"
    if text.startswith(run_prefix):
        return text[len(run_prefix) :]
    return text


def generated_activities(run_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    outputs = run_manifest.get("outputs", {})
    entries = outputs.get("generated_activities", []) if isinstance(outputs, dict) else []
    activities: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if isinstance(entry, dict) and entry.get("activity_id"):
            activities[norm(entry["activity_id"])] = entry
    return activities


def asset_entries(asset_manifest: dict[str, Any]) -> list[dict[str, Any]]:
    entries = asset_manifest.get("entries", [])
    return [entry for entry in entries if isinstance(entry, dict)]


def asset_pairs_from_manifest(asset_manifest: dict[str, Any]) -> list[tuple[str, str]]:
    return [
        (norm(entry.get("activity_id")), norm(entry.get("asset_id")))
        for entry in asset_entries(asset_manifest)
        if norm(entry.get("activity_id")) and norm(entry.get("asset_id"))
    ]


def expected_asset_pairs(run_dir: Path) -> list[tuple[str, str]]:
    return asset_pairs_from_manifest(load_yaml(run_dir / "generated_assets_pilot" / "asset_manifest.yaml"))


def find_manifest_asset_usage(activity_entry: dict[str, Any], asset_id: str) -> dict[str, Any]:
    for asset in activity_entry.get("asset_usage", []) or []:
        if isinstance(asset, dict) and norm(asset.get("asset_id")) == asset_id:
            return asset
    return {}


def activity_title(run_dir: Path, package_path: str, fallback: str) -> str:
    tag = load_yaml(run_dir / package_path / "tag_block.yaml")
    if tag.get("activity_name"):
        return norm(tag["activity_name"])
    prod_path = run_dir / package_path / "prod.md"
    if prod_path.exists():
        for line in prod_path.read_text().splitlines():
            if line.startswith("## "):
                return norm(line.strip("# "))
    return norm(fallback)


def value_from(*sources: Any) -> str:
    for source in sources:
        text = norm(source)
        if text:
            return text
    return ""


def table_columns(line: str) -> list[str]:
    return [norm(cell) for cell in line.strip().strip("|").split("|")]


def is_separator(columns: list[str]) -> bool:
    return bool(columns) and all(set(column.replace(" ", "")) <= {"-", ":"} for column in columns)


def markdown_asset_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    header: list[str] = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        columns = table_columns(line)
        if not columns:
            continue
        if "asset_id" in columns:
            header = columns
            continue
        if not header or is_separator(columns):
            continue
        values = columns + [""] * max(0, len(header) - len(columns))
        rows.append(dict(zip(header, values[: len(header)])))
    return rows


def spec_asset_row(spec_text: str, asset_id: str) -> dict[str, str]:
    for row in markdown_asset_rows(spec_text):
        if norm(row.get("asset_id")) == asset_id:
            return row
    return {}


def step_tokens(use_step: str) -> list[str]:
    tokens: list[str] = []
    for raw_part in use_step.split(";"):
        part = raw_part.strip()
        step_match = re_match(r"prod\.step_(\d+)", part)
        if step_match:
            token = f"Step {step_match}"
            if token not in tokens:
                tokens.append(token)
        round_match = re_match(r"round_(\d+)(?:-(\d+))?", part)
        if round_match:
            start = int(round_match)
            end_match = re_match(r"round_\d+-(\d+)", part)
            end = int(end_match) if end_match else start
            for number in range(start, end + 1):
                token = f"Round {number}"
                if token not in tokens:
                    tokens.append(token)
    return tokens


def re_match(pattern: str, text: str) -> str:
    match = re.search(pattern, text)
    return match.group(1) if match else ""


def prod_covers_use_steps(prod_text: str, use_step: str) -> bool:
    tokens = step_tokens(use_step)
    return bool(tokens) and all(token in prod_text for token in tokens)


def compare_field(binding: dict[str, Any], meta: dict[str, Any], asset_usage: dict[str, Any], field: str) -> bool:
    expected = norm(asset_usage.get(field))
    if not expected:
        return False
    return norm(binding.get(field)) == expected and (
        not norm(meta.get(field)) or norm(meta.get(field)) == expected
    )


def build_binding(run_dir: Path, activity_entry: dict[str, Any], asset_entry: dict[str, Any]) -> dict[str, Any]:
    activity_id = norm(asset_entry.get("activity_id"))
    asset_id = norm(asset_entry.get("asset_id"))
    asset_usage = find_manifest_asset_usage(activity_entry, asset_id)
    meta_path = run_relative(run_dir, asset_entry.get("meta_path"))
    meta = load_yaml(run_dir / meta_path) if meta_path else {}
    package_path = run_relative(run_dir, activity_entry.get("activity_path") or meta.get("package_path"))
    image_path = run_relative(run_dir, value_from(asset_entry.get("image_path"), meta.get("image_path")))
    prompt_path = run_relative(run_dir, value_from(asset_entry.get("prompt_path"), meta.get("prompt_path")))
    meta_path = run_relative(run_dir, value_from(meta_path, meta.get("meta_path")))
    spec_path = f"{package_path}/spec.md" if package_path else ""
    prod_path = f"{package_path}/prod.md" if package_path else ""
    spec_text = (run_dir / spec_path).read_text() if spec_path and (run_dir / spec_path).exists() else ""
    prod_text = (run_dir / prod_path).read_text() if prod_path and (run_dir / prod_path).exists() else ""
    spec_asset = spec_asset_row(spec_text, asset_id)
    binding: dict[str, Any] = {
        "activity_id": activity_id,
        "activity_name": activity_title(run_dir, package_path, activity_id) if package_path else activity_id,
        "asset_id": asset_id,
        "asset_type": value_from(asset_usage.get("asset_type"), meta.get("asset_type"), asset_entry.get("asset_type")),
        "requiredness": value_from(asset_usage.get("requiredness"), meta.get("requiredness"), asset_entry.get("requiredness")),
        "generation_timing": value_from(
            asset_usage.get("generation_timing"),
            meta.get("generation_timing"),
            asset_entry.get("generation_timing"),
        ),
        "integration_status": "pending",
        "package_path": package_path,
        "spec_path": spec_path,
        "prod_path": prod_path,
        "image_path": image_path,
        "meta_path": meta_path,
        "prompt_path": prompt_path,
        "use_step": value_from(asset_usage.get("use_step"), meta.get("use_step")),
        "display_location": value_from(asset_usage.get("display_location"), meta.get("display_location")),
        "display_behavior": value_from(asset_usage.get("display_behavior"), meta.get("display_behavior")),
        "fallback_behavior": value_from(asset_usage.get("fallback_behavior"), meta.get("fallback_behavior")),
        "safety_constraints": value_from(asset_usage.get("safety_constraints"), meta.get("safety_constraints")),
    }
    validation = {
        "package_exists": bool(package_path and all((run_dir / package_path / name).exists() for name in PACKAGE_FILES)),
        "image_exists": bool(image_path and (run_dir / image_path).exists()),
        "metadata_exists": bool(meta_path and (run_dir / meta_path).exists()),
        "prompt_exists": bool(prompt_path and (run_dir / prompt_path).exists()),
        "run_manifest_asset_usage_matches": bool(asset_usage),
        "meta_activity_id_matches": norm(meta.get("activity_id")) == activity_id,
        "meta_asset_id_matches": norm(meta.get("asset_id")) == asset_id,
        "spec_mentions_asset_id": asset_id in spec_text,
        "prod_mentions_asset_id": asset_id in prod_text,
        "requiredness_matches": compare_field(binding, meta, asset_usage, "requiredness"),
        "use_step_matches": compare_field(binding, meta, asset_usage, "use_step"),
        "display_location_matches": compare_field(binding, meta, asset_usage, "display_location"),
        "spec_requiredness_matches": norm(spec_asset.get("requiredness")) == binding["requiredness"],
        "spec_use_step_matches": norm(spec_asset.get("use_step")) == binding["use_step"],
        "spec_display_location_matches": norm(spec_asset.get("display_location")) == binding["display_location"],
        "prod_covers_use_steps": prod_covers_use_steps(prod_text, binding["use_step"]),
    }
    binding["validation"] = validation
    binding["integration_status"] = "integrated" if all(validation.values()) else "invalid"
    return binding


def validate_binding(run_dir: Path, binding: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    label = f"{binding.get('activity_id', 'unknown')}/{binding.get('asset_id', 'unknown')}"
    for key, value in (binding.get("validation") or {}).items():
        if value is not True:
            issues.append(f"{label}: validation.{key} is not true")
    if binding.get("integration_status") != "integrated":
        issues.append(f"{label}: integration_status is {binding.get('integration_status')!r}")
    for field in ("package_path", "spec_path", "prod_path", "image_path", "meta_path", "prompt_path"):
        value = norm(binding.get(field))
        if not value:
            issues.append(f"{label}: missing {field}")
            continue
        if field.endswith("_path") and field != "package_path" and not (run_dir / value).exists():
            issues.append(f"{label}: {field} does not exist at {value}")
    return issues


def build_manifest(run_dir: Path) -> dict[str, Any]:
    run_manifest = load_yaml(run_dir / "run_manifest.yaml")
    asset_manifest = load_yaml(run_dir / "generated_assets_pilot" / "asset_manifest.yaml")
    activities = generated_activities(run_manifest)
    bindings: list[dict[str, Any]] = []
    missing: list[str] = []
    for asset_entry in asset_entries(asset_manifest):
        activity_id = norm(asset_entry.get("activity_id"))
        activity_entry = activities.get(activity_id)
        if not activity_entry:
            missing.append(activity_id or "unknown")
            continue
        bindings.append(build_binding(run_dir, activity_entry, asset_entry))
    return {
        "run_id": run_dir.name,
        "artifact_kind": "integrated_prebuilt_asset_bindings",
        "source_asset_manifest": "generated_assets_pilot/asset_manifest.yaml",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "activity_count": len({entry["activity_id"] for entry in bindings}),
        "asset_count": len(bindings),
        "missing_activity_entries": missing,
        "entries": bindings,
    }


def validate_manifest(
    run_dir: Path,
    manifest: dict[str, Any],
    expected_pairs: set[tuple[str, str]] | list[tuple[str, str]] | None = None,
) -> list[str]:
    issues: list[str] = []
    entries = manifest.get("entries", [])
    if not isinstance(entries, list):
        return ["entries is not a list"]
    if manifest.get("missing_activity_entries"):
        issues.append(f"missing activity entries: {manifest['missing_activity_entries']}")
    if manifest.get("asset_count") != len(entries):
        issues.append("asset_count does not match entries length")
    activity_ids = [norm(entry.get("activity_id")) for entry in entries if isinstance(entry, dict)]
    if manifest.get("activity_count") != len(set(activity_ids)):
        issues.append("activity_count does not match distinct activity IDs")
    actual_pair_list = [
        (norm(entry.get("activity_id")), norm(entry.get("asset_id")))
        for entry in entries
        if isinstance(entry, dict)
    ]
    duplicate_pairs = sorted({pair for pair in actual_pair_list if actual_pair_list.count(pair) > 1})
    if duplicate_pairs:
        issues.append(f"duplicate activity/asset pair entries: {duplicate_pairs}")
    if expected_pairs is None:
        expected_pair_list = expected_asset_pairs(run_dir)
    else:
        expected_pair_list = list(expected_pairs)
    if expected_pair_list:
        expected_pair_set = set(expected_pair_list)
        actual_pairs = set(actual_pair_list)
        if len(expected_pair_set) != len(expected_pair_list):
            issues.append("source asset manifest contains duplicate activity/asset pairs")
        if actual_pairs != expected_pair_set:
            missing = sorted(expected_pair_set - actual_pairs)
            extra = sorted(actual_pairs - expected_pair_set)
            issues.append(
                "binding entries do not match required activity/asset pairs"
                f"; missing={missing}; extra={extra}"
            )
        if len(entries) != len(expected_pair_list):
            issues.append(f"expected exactly {len(expected_pair_list)} binding entries, found {len(entries)}")
    for entry in entries:
        if isinstance(entry, dict):
            issues.extend(validate_binding(run_dir, entry))
    return issues


def load_existing_manifest(run_dir: Path) -> dict[str, Any]:
    return load_yaml(run_dir / "integrated_assets" / "asset_bindings.yaml")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="Validate existing bindings instead of regenerating them.")
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    args = parser.parse_args()
    run_dir = args.run_dir if args.run_dir.is_absolute() else Path.cwd() / args.run_dir
    output_path = run_dir / "integrated_assets" / "asset_bindings.yaml"
    if args.validate:
        manifest = load_existing_manifest(run_dir)
        if not manifest:
            print(f"FAIL integrated asset bindings: missing {output_path}", file=sys.stderr)
            raise SystemExit(1)
        issues = validate_manifest(run_dir, manifest)
        if issues:
            print("FAIL integrated asset bindings:", file=sys.stderr)
            for issue in issues:
                print(f"- {issue}", file=sys.stderr)
            raise SystemExit(1)
        print(f"PASS integrated asset bindings: {manifest['asset_count']} assets, {manifest['activity_count']} activities.")
        return
    manifest = build_manifest(run_dir)
    write_yaml(output_path, manifest)
    issues = validate_manifest(run_dir, manifest)
    if issues:
        print("FAIL integrated generated assets:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Integrated {manifest['asset_count']} generated assets for {manifest['activity_count']} activities.")
    print(f"Wrote {output_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
