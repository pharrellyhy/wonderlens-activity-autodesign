import importlib.util
import pathlib
import tempfile
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_script(name):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_valid_fixture(run_dir):
    package_dir = run_dir / "activity_packages" / "activity_one"
    asset_dir = run_dir / "generated_assets_pilot" / "activity_one" / "asset_one"
    package_dir.mkdir(parents=True)
    asset_dir.mkdir(parents=True)

    (package_dir / "spec.md").write_text(
        "## Asset Brief\n\n"
        "| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| asset_one | card_set | required | pre_generated | prod.step_3.round_1 | center_card_area | Purpose. | Prompt. | Show the card. | Use voice only. | Safe. |\n"
        "\n## Asset Usage Timeline\n\n"
        "| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |\n"
        "|---|---|---|---|---|---|---|---|---|---|\n"
        "| asset_one | card_set | required | pre_generated | prod.step_3.round_1 | center_card_area | Purpose. | generated | Show the card. | Use voice only. |\n"
    )
    (package_dir / "prod.md").write_text(
        "## Activity One\n\n"
        "#### Step 3: Multi-Round Play\n\n"
        "**Round 1 -- Card:**\n\n"
        "**Screen:** Show `asset_one` in the center card area.\n"
    )
    (package_dir / "tag_block.yaml").write_text("activity_name: Activity One\n")
    (package_dir / "recap.template.yaml").write_text("{}\n")
    (package_dir / "dashboard.template.yaml").write_text("{}\n")
    (asset_dir / "contact_sheet.png").write_bytes(b"png")
    (asset_dir / "asset.meta.yaml").write_text(
        "activity_id: activity_one\n"
        "asset_id: asset_one\n"
        "asset_type: card_set\n"
        "requiredness: required\n"
        "generation_timing: pre_generated\n"
        "use_step: prod.step_3.round_1\n"
        "display_location: center_card_area\n"
    )
    (asset_dir / "contact_sheet.prompt.md").write_text("# Prompt\n")

    (run_dir / "run_manifest.yaml").write_text(
        "outputs:\n"
        "  generated_activities:\n"
        "    - activity_id: activity_one\n"
        "      activity_path: runs/test_run/activity_packages/activity_one\n"
        "      asset_usage:\n"
        "        - asset_id: asset_one\n"
        "          asset_type: card_set\n"
        "          requiredness: required\n"
        "          generation_timing: pre_generated\n"
        "          use_step: prod.step_3.round_1\n"
        "          display_location: center_card_area\n"
        "          display_behavior: Show the card.\n"
        "          fallback_behavior: Use voice only.\n"
    )
    (run_dir / "generated_assets_pilot" / "asset_manifest.yaml").write_text(
        "entries:\n"
        "  - activity_id: activity_one\n"
        "    activity_name: Activity One\n"
        "    mechanic: deduce\n"
        "    asset_id: asset_one\n"
        "    asset_type: card_set\n"
        "    requiredness: required\n"
        "    generation_timing: pre_generated\n"
        "    status: generated\n"
        "    prompt_path: generated_assets_pilot/activity_one/asset_one/contact_sheet.prompt.md\n"
        "    image_path: generated_assets_pilot/activity_one/asset_one/contact_sheet.png\n"
        "    meta_path: generated_assets_pilot/activity_one/asset_one/asset.meta.yaml\n"
    )


class IntegratedAssetWorkflowTest(unittest.TestCase):
    def test_integration_manifest_binds_one_asset(self):
        integrate = load_script("integrate_generated_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)

            manifest = integrate.build_manifest(run_dir)
            issues = integrate.validate_manifest(run_dir, manifest, {("activity_one", "asset_one")})

        self.assertEqual([], issues)
        self.assertEqual(1, manifest["asset_count"])
        self.assertEqual("integrated", manifest["entries"][0]["integration_status"])
        self.assertTrue(manifest["entries"][0]["validation"]["prod_mentions_asset_id"])
        self.assertTrue(manifest["entries"][0]["validation"]["spec_use_step_matches"])

    def test_integration_validation_rejects_wrong_pair_set(self):
        integrate = load_script("integrate_generated_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)
            manifest = integrate.build_manifest(run_dir)
            issues = integrate.validate_manifest(run_dir, manifest, {("other_activity", "other_asset")})

        self.assertIn("binding entries do not match required activity/asset pairs", "\n".join(issues))

    def test_integration_validation_rejects_duplicate_pair(self):
        integrate = load_script("integrate_generated_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)
            manifest = integrate.build_manifest(run_dir)
            manifest["entries"].append(dict(manifest["entries"][0]))
            manifest["asset_count"] = len(manifest["entries"])
            issues = integrate.validate_manifest(run_dir, manifest, {("activity_one", "asset_one")})

        self.assertIn("duplicate activity/asset pair", "\n".join(issues))

    def test_integration_validation_rejects_metadata_identity_mismatch(self):
        integrate = load_script("integrate_generated_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)
            meta_path = run_dir / "generated_assets_pilot" / "activity_one" / "asset_one" / "asset.meta.yaml"
            meta_path.write_text(meta_path.read_text().replace("asset_id: asset_one", "asset_id: wrong_asset"))
            manifest = integrate.build_manifest(run_dir)
            issues = integrate.validate_manifest(run_dir, manifest, {("activity_one", "asset_one")})

        self.assertIn("validation.meta_asset_id_matches is not true", "\n".join(issues))

    def test_integration_validation_rejects_spec_field_disagreement(self):
        integrate = load_script("integrate_generated_assets")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)
            spec_path = run_dir / "activity_packages" / "activity_one" / "spec.md"
            spec_path.write_text(spec_path.read_text().replace("center_card_area", "wrong_location"))
            manifest = integrate.build_manifest(run_dir)
            issues = integrate.validate_manifest(run_dir, manifest, {("activity_one", "asset_one")})

        self.assertIn("validation.spec_display_location_matches is not true", "\n".join(issues))

    def test_exporter_embeds_bound_asset_image(self):
        exporter = load_script("export_activity_html")
        html = exporter.render_static_image("asset_one", b"png")

        self.assertIn("data:image/png;base64,cG5n", html)
        self.assertIn("asset_one", html)

    def test_export_validation_rejects_wrong_embedded_image(self):
        integrate = load_script("integrate_generated_assets")
        exporter = load_script("export_activity_html")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            write_valid_fixture(run_dir)
            binding_manifest = integrate.build_manifest(run_dir)
            (run_dir / "integrated_assets").mkdir()
            integrate.write_yaml(run_dir / "integrated_assets" / "asset_bindings.yaml", binding_manifest)
            export_dir = run_dir / "activity_exports"
            export_dir.mkdir()
            (export_dir / "activity_one.html").write_text(
                "<!doctype html><html lang=\"en\"><body>activity_one asset_one "
                "data:image/png;base64,d3Jvbmc= Static Activity Export Integrated Prebuilt Asset "
                "Fallback Runtime Flow Scorecard Source Files</body></html>"
            )
            exporter.write_yaml(
                export_dir / "export_manifest.yaml",
                {
                    "export_count": 1,
                    "entries": [
                        {
                            "activity_id": "activity_one",
                            "asset_id": "asset_one",
                            "html_path": "activity_exports/activity_one.html",
                            "image_path": "generated_assets_pilot/activity_one/asset_one/contact_sheet.png",
                        }
                    ],
                },
            )
            issues = exporter.validate_exports(run_dir, expected_count=1)

        self.assertIn("embedded image does not match", "\n".join(issues))

    def test_export_validation_rejects_duplicate_activity(self):
        exporter = load_script("export_activity_html")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            (run_dir / "integrated_assets").mkdir(parents=True)
            (run_dir / "activity_exports").mkdir()
            exporter.write_yaml(
                run_dir / "integrated_assets" / "asset_bindings.yaml",
                {
                    "entries": [
                        {
                            "activity_id": "activity_one",
                            "asset_id": "asset_one",
                            "image_path": "generated_assets_pilot/activity_one/asset_one/contact_sheet.png",
                        },
                        {
                            "activity_id": "activity_two",
                            "asset_id": "asset_two",
                            "image_path": "generated_assets_pilot/activity_two/asset_two/contact_sheet.png",
                        },
                    ]
                },
            )
            exporter.write_yaml(
                run_dir / "activity_exports" / "export_manifest.yaml",
                {
                    "export_count": 2,
                    "entries": [
                        {
                            "activity_id": "activity_one",
                            "asset_id": "asset_one",
                            "html_path": "activity_exports/activity_one.html",
                            "image_path": "generated_assets_pilot/activity_one/asset_one/contact_sheet.png",
                        },
                        {
                            "activity_id": "activity_one",
                            "asset_id": "asset_one",
                            "html_path": "activity_exports/activity_one_copy.html",
                            "image_path": "generated_assets_pilot/activity_one/asset_one/contact_sheet.png",
                        },
                    ],
                },
            )
            issues = exporter.validate_exports(run_dir, expected_count=2)

        self.assertIn("export entries do not match binding activity/asset pairs", "\n".join(issues))

    def test_export_validation_handles_multiple_assets_for_one_activity(self):
        exporter = load_script("export_activity_html")
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "test_run"
            (run_dir / "integrated_assets").mkdir(parents=True)
            asset_root = run_dir / "generated_assets_pilot" / "activity_one"
            export_dir = run_dir / "activity_exports"
            export_dir.mkdir()
            entries = []
            for asset_id, image_bytes in [("asset_one", b"one"), ("asset_two", b"two")]:
                asset_dir = asset_root / asset_id
                asset_dir.mkdir(parents=True)
                image_path = asset_dir / "contact_sheet.png"
                image_path.write_bytes(image_bytes)
                html_name = f"activity_one_{asset_id}.html"
                (export_dir / html_name).write_text(
                    "<!doctype html><html lang=\"en\"><body>activity_one "
                    f"{asset_id} {exporter.data_uri(image_path)} Static Activity Export "
                    "Integrated Prebuilt Asset Fallback Runtime Flow Scorecard Source Files</body></html>"
                )
                entries.append(
                    {
                        "activity_id": "activity_one",
                        "asset_id": asset_id,
                        "html_path": f"activity_exports/{html_name}",
                        "image_path": f"generated_assets_pilot/activity_one/{asset_id}/contact_sheet.png",
                    }
                )
            exporter.write_yaml(run_dir / "integrated_assets" / "asset_bindings.yaml", {"entries": entries})
            exporter.write_yaml(
                export_dir / "export_manifest.yaml",
                {"export_count": 2, "entries": entries},
            )
            issues = exporter.validate_exports(run_dir, expected_count=2)

        self.assertEqual([], issues)


if __name__ == "__main__":
    unittest.main()
