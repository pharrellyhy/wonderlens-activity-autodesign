import importlib.util
import hashlib
import pathlib
import subprocess
import sys
import tempfile
import unittest

import yaml
from PIL import Image


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def load_script(name):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    assert path.exists(), f"missing script: {path}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_png(path, size=(512, 512), color=(117, 207, 151, 255)):
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGBA", size, color)
    image.save(path, format="PNG")


def read_yaml(path):
    return yaml.safe_load(path.read_text()) or {}


def write_yaml(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_reference_metadata(
    package_dir,
    *,
    asset_id="orion_card",
    source_type="approved_internal_reference",
    storage_allowed=True,
    source_uri="internal://reference/astronomy/orion",
    license_name="approved_internal_reference",
    verification_status="accepted",
    reviewer_agent="fixture-reviewer",
):
    original_path = package_dir / "assets" / "sources" / f"{asset_id}__source_original.png"
    write_yaml(
        package_dir / "assets" / "sources" / f"{asset_id}__source_metadata.yaml",
        {
            "activity_id": "asset_smoke",
            "asset_id": asset_id,
            "source_label": "Approved internal Orion chart",
            "source_uri": source_uri,
            "source_type": source_type,
            "license": license_name,
            "storage_allowed": storage_allowed,
            "verification_status": verification_status,
            "verification_notes": "Must preserve the approved Orion star arrangement.",
            "source_original_path": f"assets/sources/{asset_id}__source_original.png",
            "sha256": sha256_file(original_path),
            "verified_at": "2026-05-28T00:00:00+08:00",
            "reviewer_agent": reviewer_agent,
        },
    )


def base_run(run_dir):
    package_dir = run_dir / "activity_packages" / "asset_smoke"
    package_dir.mkdir(parents=True)
    (run_dir / "run_manifest.yaml").write_text(
        "run_id: test_run\n"
        "source:\n"
        "  asset_build: generate_and_curate\n"
        "outputs:\n"
        "  generated_activities:\n"
        "    - activity_id: asset_smoke\n"
        "      activity_path: runs/test_run/activity_packages/asset_smoke\n"
    )
    (run_dir / "review_notes.md").write_text("# Review Notes\n")
    (package_dir / "spec.md").write_text(
        "## Asset Brief\n\n"
        "| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior |\n"
        "|---|---|---|---|---|---|---|---|---|---|\n"
        "| moss_icon | icon | required | pre_generated | prod.step_2 | center | Show moss. | Prompt. | Show the moss. | Voice fallback. |\n"
        "| orion_card | card | required | pre_generated | prod.step_3 | center | Show Orion. | Approved source. | Show the card. | Use source facts only. |\n"
        "\n## Self-Evaluation Scorecard\n\n"
        "| # | Dimension | Score | Notes |\n"
        "|---|---|---|---|\n"
        + "".join(f"| {i} | D{i} | PASS | ok |\n" for i in range(1, 11))
    )
    (package_dir / "prod.md").write_text(
        "## Asset Smoke\n\n"
        "#### Step 1: Hello\n\n"
        "**Runtime AI instruction:** Greet the child.\n\n"
        "**Child responses:**\n\n"
        "1. (Ideal) Child answers.\n"
        "2. (Unexpected) Child talks about something else.\n"
        "3. (No response) Child is quiet.\n\n"
        "**AI follow-up policy:**\n\n"
        "1. (Ideal) Continue.\n"
        "2. (Unexpected) Redirect gently.\n"
        "3. (No response) Offer a model.\n\n"
        "**Screen/state:** Show the activity start.\n\n"
        "#### Step 2: Moss Icon\n\n"
        "**Runtime AI instruction:** Ask about `moss_icon`.\n\n"
        "**Screen/state:** Show `moss_icon`.\n\n"
        "#### Step 3: Orion Card\n\n"
        "**Runtime AI instruction:** Ask about `orion_card`.\n\n"
        "**Screen/state:** Show `orion_card`.\n"
    )
    (package_dir / "tag_block.yaml").write_text(
        "activity_name: Asset Smoke\n"
        "template_type: cat5\n"
        "activity_signature:\n"
        "  mechanic: collect\n"
    )
    (package_dir / "recap.template.yaml").write_text("{}\n")
    (package_dir / "dashboard.template.yaml").write_text("{}\n")
    write_yaml(
        package_dir / "demo_support.yaml",
        {
            "activity_id": "asset_smoke",
            "version": 1,
            "entity_compatibility": "source_bound",
            "parameterization": {
                "mode": "entity_theme",
                "decision_source": "fixture_author",
                "integrity_status": "validator_fixture",
                "confidence": "high",
                "evidence": [
                    "Moss themes the asset-smoke fixture, but the asset set and collection/reference checks are authored."
                ],
                "validity": {
                    "production_supported": True,
                    "requires": [],
                    "allowed_entity_classes": [],
                    "invalid_when": [],
                },
                "source_fields": {},
                "derived_runtime_fields": {},
                "authored_constants": {
                    "collection_asset": "moss_icon",
                    "reference_asset": "orion_card",
                },
                "fallback_behavior": "Keep the authored asset-smoke flow if no handoff entity is present.",
                "consumer_notes": {
                    "wonderlens_ai": "Do not retarget asset-smoke success criteria from the handoff entity."
                },
                "reviewer_action": "accept_as_thematic_fixture",
            },
            "demo_support": {
                "status": "supported",
                "ui_template": "cat5_collection",
                "support_level": "full",
                "entity_bindings": [
                    {
                        "entity_id": "moss",
                        "display_label": "Moss",
                        "source_entity_exemplar": "moss",
                        "default": True,
                    }
                ],
                "requires": {
                    "generated_assets": True,
                    "real_camera": True,
                    "runtime_judgment": False,
                    "device_round_screen": True,
                },
            },
        },
    )
    write_yaml(
        package_dir / "asset_manifest.yaml",
        {
            "activity_id": "asset_smoke",
            "entity_id": "moss",
            "version": 1,
            "style_id": "wonderlens_device_mint_soft_3d",
            "palette": {
                "shell": "warm porcelain off-white",
                "screen": "green-tinted near black",
                "primary_accent": "soft mint green",
            },
            "screen_targets": {
                "round_device_screen": {
                    "aspect_ratio": "1:1",
                    "crop_shape": "circle",
                    "master_size": 1024,
                    "safe_area": "central 72 percent circle",
                },
                "catalog_grid": {
                    "aspect_ratio": "1:1",
                    "master_size": 512,
                },
            },
            "assets": [
                {
                    "id": "moss_icon",
                    "role": "collection_correct",
                    "label": "Fuzzy moss",
                    "collection_catalog_id": "moss",
                    "requiredness": "required",
                    "accuracy_mode": "illustrative",
                    "source_strategy": "generated_illustrative",
                    "transformation_policy": "generate_new",
                    "prompt_en": "Soft 3D educational toy illustration of a fuzzy moss patch, no text.",
                    "variants": [
                        {
                            "id": "round_1024",
                            "target": "round_device_screen",
                            "size": "1024x1024",
                            "path": None,
                        },
                        {
                            "id": "catalog_512",
                            "target": "catalog_grid",
                            "size": "512x512",
                            "path": None,
                        }
                    ],
                    "fallback_behavior": "Use a spoken moss clue.",
                },
                {
                    "id": "orion_card",
                    "role": "story_scene",
                    "label": "Orion card",
                    "requiredness": "required",
                    "accuracy_mode": "reference_bound",
                    "source_strategy": "curated_original",
                    "transformation_policy": "crop_resize_only",
                    "prompt_en": "Preserve the approved Orion star layout exactly; add no extra stars.",
                    "reference_policy": {
                        "source_required": True,
                        "allowed_sources": ["approved_internal_reference"],
                        "verification_required": True,
                        "verification_notes": "Must preserve the approved Orion star arrangement.",
                    },
                    "sources": [
                        {
                            "label": "Approved internal Orion chart",
                            "uri": "internal://reference/astronomy/orion",
                            "license": "approved_internal_reference",
                        }
                    ],
                    "variants": [
                        {
                            "id": "round_1024",
                            "target": "round_device_screen",
                            "size": "1024x1024",
                            "path": None,
                        }
                    ],
                    "fallback_behavior": "Do not claim Orion if the approved source is unavailable.",
                },
            ],
        },
    )
    return package_dir


class GenerateAndCurateAssetPipelineTest(unittest.TestCase):
    def test_build_updates_package_manifest_and_audit_outputs(self):
        builder = load_script("build_activity_assets")
        validator = load_script("validate_asset_build_outputs")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(package_dir)

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            issues = validator.validate_run(run_dir)
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            asset_outputs = read_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")

            self.assertEqual(0, result["required_failures"])
            self.assertEqual([], issues)
            self.assertEqual(
                "assets/items/moss_icon__round_1024.png",
                manifest["assets"][0]["variants"][0]["path"],
            )
            self.assertEqual(
                "assets/orion_card__round_1024.png",
                manifest["assets"][1]["variants"][0]["path"],
            )
            with Image.open(package_dir / "assets" / "items" / "moss_icon__round_1024.png") as image:
                self.assertEqual((1024, 1024), image.size)
            with Image.open(package_dir / "assets" / "items" / "moss_icon__catalog_512.png") as image:
                self.assertEqual((512, 512), image.size)
            self.assertTrue((package_dir / "assets" / "sources" / "orion_card__source_metadata.yaml").exists())
            statuses = {(entry["asset_id"], entry["status"]) for entry in asset_outputs["entries"]}
            self.assertIn(("moss_icon", "generated"), statuses)
            self.assertIn(("orion_card", "curated"), statuses)
            self.assertTrue((run_dir / "generated_assets" / "work_items" / "asset_smoke__moss_icon.md").exists())

    def test_collection_assets_build_under_items_directory_and_work_item_names_style_sources(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(package_dir)

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            work_item = run_dir / "generated_assets" / "work_items" / "asset_smoke__moss_icon.md"
            item_variant_exists = (
                package_dir / "assets" / "items" / "moss_icon__round_1024.png"
            ).exists()
            work_item_text = work_item.read_text()

        self.assertEqual(0, result["required_failures"])
        self.assertEqual(
            "assets/items/moss_icon__round_1024.png",
            manifest["assets"][0]["variants"][0]["path"],
        )
        self.assertTrue(item_variant_exists)
        self.assertIn("docs/asset_style_reference/wonderlens-activity-style.md", work_item_text)
        self.assertIn("docs/asset_style_reference/style-reference-flat-nordic.png", work_item_text)
        self.assertIn("Codex built-in imagegen", work_item_text)

    def test_missing_required_inputs_leave_paths_null_and_record_failures(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            asset_outputs = read_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")

        self.assertEqual(2, result["required_failures"])
        self.assertIsNone(manifest["assets"][0]["variants"][0]["path"])
        self.assertIsNone(manifest["assets"][1]["variants"][0]["path"])
        statuses = {(entry["asset_id"], entry["status"]) for entry in asset_outputs["entries"]}
        self.assertIn(("moss_icon", "missing_source"), statuses)
        self.assertIn(("orion_card", "missing_source"), statuses)

    def test_missing_rejected_source_clears_stale_removed_variant_path(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            manifest_path = package_dir / "asset_manifest.yaml"
            manifest = read_yaml(manifest_path)
            manifest["assets"][0]["variants"][0]["path"] = "assets/items/moss_icon__round_1024.png"
            write_yaml(manifest_path, manifest)

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            manifest = read_yaml(manifest_path)

        self.assertEqual(2, result["required_failures"])
        self.assertIsNone(manifest["assets"][0]["variants"][0]["path"])

    def test_build_is_idempotent_without_force(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(package_dir)

            first = builder.build_assets(run_dir, mode="generate_and_curate")
            output = package_dir / "assets" / "items" / "moss_icon__round_1024.png"
            metadata_path = package_dir / "assets" / "sources" / "orion_card__source_metadata.yaml"
            first_metadata = metadata_path.read_text()
            output.write_bytes(b"reviewed-output")
            second = builder.build_assets(run_dir, mode="generate_and_curate")

            self.assertEqual(0, first["required_failures"])
            self.assertEqual(0, second["required_failures"])
            self.assertEqual(b"reviewed-output", output.read_bytes())
            self.assertEqual(first_metadata, metadata_path.read_text())

    def test_reference_bound_source_requires_preaccepted_metadata(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            asset_outputs = read_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")

        self.assertEqual(1, result["required_failures"])
        self.assertIsNone(manifest["assets"][1]["variants"][0]["path"])
        self.assertFalse((package_dir / "assets" / "sources" / "orion_card__source_metadata.yaml").exists())
        statuses = {(entry["asset_id"], entry["status"]) for entry in asset_outputs["entries"]}
        self.assertIn(("orion_card", "missing_source"), statuses)

    def test_reference_bound_source_rejects_unknown_license_metadata(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(
                package_dir,
                source_type="unverified_thumbnail",
                source_uri="https://example.com/random-thumbnail.png",
                license_name="unknown",
            )

            result = builder.build_assets(run_dir, mode="generate_and_curate")
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            asset_outputs = read_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")

        self.assertEqual(1, result["required_failures"])
        self.assertIsNone(manifest["assets"][1]["variants"][0]["path"])
        statuses = {(entry["asset_id"], entry["status"]) for entry in asset_outputs["entries"]}
        self.assertIn(("orion_card", "missing_source"), statuses)

    def test_builder_rejects_unsafe_ids_before_writing_outputs(self):
        builder = load_script("build_activity_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            manifest_path = package_dir / "asset_manifest.yaml"
            manifest = read_yaml(manifest_path)
            manifest["assets"][0]["id"] = "../escape"
            write_yaml(manifest_path, manifest)

            with self.assertRaisesRegex(ValueError, "unsafe asset id"):
                builder.build_assets(run_dir, mode="generate_and_curate")

            self.assertFalse((package_dir.parent / "escape__icon_64.png").exists())

    def test_validator_rejects_unsafe_variant_paths(self):
        validator = load_script("validate_asset_build_outputs")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            manifest["assets"][0]["variants"][0]["path"] = "../escape.png"
            write_yaml(package_dir / "asset_manifest.yaml", manifest)

            issues = validator.validate_run(run_dir)

        self.assertIn("unsafe variant path", "\n".join(issues))

    def test_validator_rejects_required_built_thumbnail_only_asset(self):
        validator = load_script("validate_asset_build_outputs")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            manifest = read_yaml(package_dir / "asset_manifest.yaml")
            manifest["assets"] = [manifest["assets"][0]]
            manifest["assets"][0]["variants"] = [
                {
                    "id": "icon_64",
                    "target": "catalog_grid",
                    "size": "64x64",
                    "path": "assets/items/moss_icon__icon_64.png",
                }
            ]
            write_yaml(package_dir / "asset_manifest.yaml", manifest)
            write_png(package_dir / "assets" / "items" / "moss_icon__icon_64.png", size=(64, 64))
            work_item = run_dir / "generated_assets" / "work_items" / "asset_smoke__moss_icon.md"
            work_item.parent.mkdir(parents=True, exist_ok=True)
            work_item.write_text("# moss work item\n")
            write_yaml(
                run_dir / "generated_assets" / "asset_outputs.yaml",
                {
                    "entries": [
                        {
                            "activity_id": "asset_smoke",
                            "asset_id": "moss_icon",
                            "status": "generated",
                            "work_item_path": "generated_assets/work_items/asset_smoke__moss_icon.md",
                            "output_variants": [
                                {
                                    "variant_id": "icon_64",
                                    "path": "assets/items/moss_icon__icon_64.png",
                                    "size": "64x64",
                                }
                            ],
                        }
                    ]
                },
            )
            write_yaml(run_dir / "generated_assets" / "reference_sources.yaml", {"entries": []})
            write_yaml(run_dir / "generated_assets" / "qa_notes.yaml", {"entries": []})

            issues = validator.validate_run(run_dir)

        self.assertIn("required asset has no high-resolution runtime variant", "\n".join(issues))

    def test_dashboard_shows_runtime_asset_outputs(self):
        builder = load_script("build_activity_assets")
        report = load_script("generate_run_review")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(package_dir)
            builder.build_assets(run_dir, mode="generate_and_curate")

            html = report.build_html(run_dir.parents[1], run_dir)

        self.assertIn("Generated Runtime Assets", html)
        self.assertIn("generate_and_curate", html)
        self.assertIn("assets/items/moss_icon__round_1024.png", html)
        self.assertIn("Approved internal Orion chart", html)
        self.assertIn("asset_smoke__orion_card.md", html)

    def test_dashboard_shows_requested_asset_build_when_outputs_are_missing(self):
        report = load_script("generate_run_review")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            base_run(run_dir)

            html = report.build_html(run_dir.parents[1], run_dir)

        self.assertIn("Generated Runtime Assets", html)
        self.assertIn("generate_and_curate", html)
        self.assertIn("Missing asset_outputs.yaml", html)

    def test_committed_valid_fixture_passes_asset_output_validator(self):
        script = REPO_ROOT / "scripts" / "validate_asset_build_outputs.py"
        fixture = REPO_ROOT / "tests" / "fixtures" / "asset_build_runs" / "valid_generate_and_curate"
        self.assertTrue(fixture.exists(), f"missing fixture: {fixture}")

        result = subprocess.run(
            [PYTHON, str(script), str(fixture)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("OK asset build outputs", result.stdout)

    def test_asset_only_rerun_cli_fills_existing_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            package_dir = base_run(run_dir)
            write_png(run_dir / "generated_assets" / "inbox" / "asset_smoke" / "moss_icon.png")
            write_png(package_dir / "assets" / "sources" / "orion_card__source_original.png")
            write_reference_metadata(package_dir)

            result = subprocess.run(
                [
                    PYTHON,
                    str(REPO_ROOT / "scripts" / "build_activity_assets.py"),
                    str(run_dir),
                    "--mode",
                    "generate_and_curate",
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual("", result.stderr)
            self.assertEqual(0, result.returncode, result.stdout)
            self.assertIn("built=2", result.stdout)
            self.assertTrue((package_dir / "assets" / "orion_card__round_1024.png").exists())
            self.assertTrue((package_dir / "assets" / "items" / "moss_icon__round_1024.png").exists())


if __name__ == "__main__":
    unittest.main()
