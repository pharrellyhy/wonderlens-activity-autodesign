from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import validate_full_pass_asset_bundle as bundle


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def asset(asset_id: str, role: str = "story_scene") -> dict:
    return {
        "id": asset_id,
        "role": role,
        "label": asset_id.replace("_", " "),
        "requiredness": "required",
        "accuracy_mode": "illustrative",
        "source_strategy": "generated_illustrative",
        "transformation_policy": "generate_new",
        "prompt_en": f"Generate {asset_id}.",
        "variants": [
            {
                "id": "round_512",
                "target": "round_device_screen",
                "size": "512x512",
                "path": f"assets/{asset_id}__round_512.png",
            }
        ],
        "fallback_behavior": "Show the no-asset fallback instead.",
    }


def write_package(run_dir: Path, activity_id: str, assets: list[dict], template_type: str = "cat1") -> Path:
    package_dir = run_dir / "activity_packages" / activity_id
    package_dir.mkdir(parents=True)
    write_yaml(
        package_dir / "tag_block.yaml",
        {"activity_id": activity_id, "template_type": template_type},
    )
    write_yaml(
        package_dir / "demo_support.yaml",
        {
            "activity_id": activity_id,
            "version": 1,
            "support": {
                "status": "supported",
                "ui_template": "cat1_three_rounds",
            },
        },
    )
    write_yaml(
        package_dir / "asset_manifest.yaml",
        {
            "activity_id": activity_id,
            "entity_id": "fixture",
            "version": 1,
            "style_id": "wonderlens_device_mint_soft_3d",
            "palette": {
                "shell": "warm porcelain off-white",
                "screen": "barely tinted white",
                "primary_accent": "muted sage green",
            },
            "screen_targets": {
                "round_device_screen": {
                    "aspect_ratio": "1:1",
                    "crop_shape": "circle",
                    "master_size": 512,
                    "safe_area": "central 72 percent circle",
                }
            },
            "assets": assets,
        },
    )
    for entry in assets:
        for variant in entry["variants"]:
            path = package_dir / variant["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"png")
    return package_dir


class FullPassAssetBundleValidationTest(unittest.TestCase):
    def test_item_only_package_fails_missing_standard_beat_scenes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            write_package(
                run_dir,
                "item_only",
                [asset("target_card", role="collection_correct")],
            )

            issues = bundle.validate_run(run_dir)

        missing = {issue["missing_asset_id"] for issue in issues if issue["kind"] == "missing_required_asset"}
        self.assertIn("intro_scene", missing)
        self.assertIn("rules_scene", missing)
        self.assertIn("round_1_scene", missing)
        self.assertIn("celebrate_scene", missing)
        self.assertIn("closing_scene", missing)

    def test_standard_cat1_bundle_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            required = [asset(asset_id, role=role) for asset_id, role in bundle.STANDARD_REQUIRED_ASSETS]
            write_package(run_dir, "complete_cat1", required)

            issues = bundle.validate_run(run_dir)

        self.assertEqual([], issues)

    def test_cat5_collection_bundle_requires_synthesis_scene(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            required = [asset(asset_id, role=role) for asset_id, role in bundle.STANDARD_REQUIRED_ASSETS]
            write_package(run_dir, "complete_cat5_without_synthesis", required, template_type="cat5")

            issues = bundle.validate_run(run_dir)

        missing = {issue["missing_asset_id"] for issue in issues if issue["kind"] == "missing_required_asset"}
        self.assertEqual({"synthesis_scene"}, missing)


if __name__ == "__main__":
    unittest.main()
