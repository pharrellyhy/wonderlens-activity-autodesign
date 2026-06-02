from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import repair_full_pass_asset_bundle as repair


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def write_package(run_dir: Path, activity_id: str, *, template_type: str = "cat1") -> Path:
    package_dir = run_dir / "activity_packages" / activity_id
    package_dir.mkdir(parents=True)
    write_yaml(
        package_dir / "tag_block.yaml",
        {
            "activity_id": activity_id,
            "template_type": template_type,
            "activity_signature": {"preview_label": "Fixture Quest"},
        },
    )
    (package_dir / "prod.md").write_text(
        "## Fixture Quest\n\n"
        "#### Step 1: Welcome\n\n"
        "**Screen:** A cozy trail opening with one empty progress token.\n\n"
        "#### Step 2: Rules\n\n"
        "**Screen:** Three simple mission tokens explain the rule.\n\n"
        "**Round 1 -- First Clue:**\n\n"
        "**Screen:** First clue glows in the middle.\n\n"
        "**Round 2 -- Second Clue:**\n\n"
        "**Screen:** Second clue waits beside the first token.\n\n"
        "**Round 3 -- Third Clue:**\n\n"
        "**Screen:** Third clue completes the trail.\n\n"
        "#### Step 4: Magic Moment\n\n"
        "**Screen:** Badge sparkles over the completed trail.\n\n"
        "#### Step 5: Closing\n\n"
        "**Screen:** Recap badge and goodbye trail are visible.\n"
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
            "assets": [],
        },
    )
    return package_dir


class RepairFullPassAssetBundleTest(unittest.TestCase):
    def test_adds_standard_scene_bundle_with_null_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            package_dir = write_package(run_dir, "fixture_quest")

            result = repair.repair_run(run_dir)

            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

        asset_ids = {asset["id"] for asset in manifest["assets"]}
        self.assertIn("activity_icon", asset_ids)
        self.assertIn("intro_scene", asset_ids)
        self.assertIn("rules_scene", asset_ids)
        self.assertIn("round_1_scene", asset_ids)
        self.assertIn("celebrate_scene", asset_ids)
        self.assertIn("closing_scene", asset_ids)
        self.assertEqual(8, result["added_count"])
        intro = next(asset for asset in manifest["assets"] if asset["id"] == "intro_scene")
        self.assertEqual("story_scene", intro["role"])
        self.assertIsNone(intro["variants"][0]["path"])
        self.assertNotIn("progress token", intro["prompt_en"])
        self.assertIn("full-bleed", intro["prompt_en"])

    def test_guided_drawing_round_prompts_are_step_specific(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            package_dir = write_package(run_dir, "concept_guided_drawing_probe")

            repair.repair_run(run_dir)

            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

        by_id = {asset["id"]: asset for asset in manifest["assets"]}
        self.assertIn("one big circle", by_id["round_1_scene"]["prompt_en"])
        self.assertIn("exactly two small ears or petals", by_id["round_2_scene"]["prompt_en"])
        self.assertIn("one face/detail", by_id["round_3_scene"]["prompt_en"])
        self.assertNotIn("progress markers", by_id["rules_scene"]["prompt_en"])

    def test_rejected_template_activities_get_beat_specific_prompts(self) -> None:
        cases = {
            "concept_little_poem_build": [
                ("round_1_scene", "first contribution step"),
                ("round_2_scene", "second contribution step"),
                ("round_3_scene", "final contribution step"),
                ("round_3_scene", "do not draw readable text"),
            ],
            "concept_time_sense_probe": [
                ("round_1_scene", "first prediction moment"),
                ("round_2_scene", "sand has moved halfway"),
                ("round_3_scene", "before-and-after tray"),
                ("round_3_scene", "no score, answer, or progress dots"),
            ],
            "concept_current_topic_interview_deduce": [
                ("round_1_scene", "first opinion step"),
                ("round_2_scene", "reason step"),
                ("round_3_scene", "polite follow-up step"),
                ("round_3_scene", "completed interview thought set"),
            ],
        }
        for activity_id, expectations in cases.items():
            with self.subTest(activity_id=activity_id):
                with tempfile.TemporaryDirectory() as tmp:
                    run_dir = Path(tmp)
                    package_dir = write_package(run_dir, activity_id)

                    repair.repair_run(run_dir)

                    manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

                by_id = {asset["id"]: asset for asset in manifest["assets"]}
                for asset_id, phrase in expectations:
                    self.assertIn(phrase, by_id[asset_id]["prompt_en"])

    def test_recognition_pop_scene_prompts_do_not_duplicate_picker_animals(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            package_dir = write_package(run_dir, "concept_recognition_pop_probe")

            repair.repair_run(run_dir)

            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

        by_id = {asset["id"]: asset for asset in manifest["assets"]}
        for asset_id in ("round_1_scene", "round_2_scene", "round_3_scene"):
            prompt = by_id[asset_id]["prompt_en"]
            self.assertIn("no animals are drawn in the background", prompt)
            self.assertIn("do not redraw those selectable animals", prompt)
        self.assertIn("do not include dog, fox, wolf", by_id["activity_icon"]["prompt_en"])

    def test_cat5_adds_synthesis_scene(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            package_dir = write_package(run_dir, "fixture_cat5", template_type="cat5")

            repair.repair_run(run_dir)

            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

        asset_ids = {asset["id"] for asset in manifest["assets"]}
        self.assertIn("synthesis_scene", asset_ids)

    def test_existing_asset_is_not_duplicated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            package_dir = write_package(run_dir, "fixture_existing")
            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())
            manifest["assets"].append(repair.bundle_asset("fixture_existing", "intro_scene", "story_scene", "Existing intro."))
            write_yaml(package_dir / "asset_manifest.yaml", manifest)

            repair.repair_run(run_dir)

            manifest = yaml.safe_load((package_dir / "asset_manifest.yaml").read_text())

        self.assertEqual(1, sum(1 for asset in manifest["assets"] if asset["id"] == "intro_scene"))


if __name__ == "__main__":
    unittest.main()
