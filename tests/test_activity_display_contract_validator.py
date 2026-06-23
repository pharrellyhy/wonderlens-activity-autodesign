import importlib.util
import json
import pathlib
import tempfile
import textwrap
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "activity_display_contract"
RUN_LOCAL_ROOT = (
    REPO_ROOT
    / "runs"
    / "20260604_144222_wonderlens_ai_runtime_ready_12"
    / "activity_packages"
)
CURRENT_TWELVE_IDS = {
    "concept_animal_sound_motion_voice",
    "concept_career_decision_decide",
    "concept_constellation_star_count_enumerate",
    "concept_emotion_reader_care",
    "concept_guided_drawing_probe",
    "concept_partial_reveal_deduce",
    "concept_phoneme_hunt_collect",
    "concept_recognition_pop_probe",
    "concept_story_unlock_probe",
    "concept_travel_planner_predict",
    "concept_vegetable_sort_sort",
    "concept_word_echo_remember",
}


def load_validator():
    path = REPO_ROOT / "scripts" / "validate_activity_display_contract.py"
    spec = importlib.util.spec_from_file_location("validate_activity_display_contract", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ActivityDisplayContractValidatorTest(unittest.TestCase):
    def test_valid_fixture_set_passes(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "valid"])

        self.assertEqual([], issues)

    def test_unknown_layout_id_is_rejected(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "unknown_layout"])

        self.assertIn("layout_id 'two_image_choice' is not allowed", "\n".join(issues))

    def test_verifiable_policy_requires_display_bound_target(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "missing_verification_target"])

        self.assertIn("choice_match policy must declare target.option_id", "\n".join(issues))

    def test_display_asset_policy_must_target_frame_display_asset(self):
        validator = load_validator()

        with tempfile.TemporaryDirectory() as tmp:
            package_dir = pathlib.Path(tmp) / "wrong_display_target"
            package_dir.mkdir()
            (package_dir / "activity_display_contract_v1.yaml").write_text(
                textwrap.dedent(
                    """
                    activity_id: wrong_display_target
                    version: 1
                    contract: activity_display_contract_v1
                    display_assets:
                      - display_asset_id: shown_count
                        kind: number
                        metadata:
                          expected_number: 4
                      - display_asset_id: other_count
                        kind: number
                        metadata:
                          expected_number: 9
                    frames:
                      - frame_id: count_round
                        step_ref: prod.step_3.round_1
                        layout_id: single_image
                        display_asset_id: shown_count
                        control_mode: voice_only
                        verification_policy:
                          type: number_match
                          required: true
                          target:
                            type: display_asset
                            display_asset_id: other_count
                          evidence:
                            - spoken_number
                        effect_profile:
                          id: count_confirm
                          sound_effects:
                            - count_tick
                          lighting_effects:
                            - star_focus
                          haptic_feedback:
                            - count_pulse
                    """
                )
            )

            issues = validator.validate_roots([package_dir])

        self.assertIn("number_match target must match the frame display_asset_id", "\n".join(issues))

    def test_photo_policy_requires_displayed_initial_sound_target(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "photo_policy_unbound"])

        joined = "\n".join(issues)
        self.assertIn("photo_object_initial_sound policy must target a displayed asset", joined)
        self.assertIn("target display asset must declare metadata.target_initial_sound", joined)

    def test_manifest_asset_references_must_exist(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "missing_manifest_asset"])

        self.assertIn("asset_manifest_id 'missing_scene' is not declared in asset_manifest.yaml", "\n".join(issues))

    def test_effect_profile_rejects_chinese_terms(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "chinese_effect_terms"])

        self.assertIn("effect_profile.sound_effects[0] must be English-only", "\n".join(issues))

    def test_empty_contract_is_rejected(self):
        validator = load_validator()

        with tempfile.TemporaryDirectory() as tmp:
            package_dir = pathlib.Path(tmp) / "empty_contract"
            package_dir.mkdir()
            (package_dir / "activity_display_contract_v1.yaml").write_text(
                textwrap.dedent(
                    """
                    activity_id: empty_contract
                    version: 1
                    contract: activity_display_contract_v1
                    display_assets: []
                    frames: []
                    """
                )
            )

            issues = validator.validate_roots([package_dir])

        joined = "\n".join(issues)
        self.assertIn("display_assets must include at least one item", joined)
        self.assertIn("frames must include at least one item", joined)

    def test_schema_requires_verification_target(self):
        schema_path = REPO_ROOT / "activities" / "_schema" / "activity_display_contract_v1.schema.json"
        schema = json.loads(schema_path.read_text())

        required = schema["$defs"]["verification_policy"]["required"]

        self.assertIn("target", required)

    def test_current_twelve_activity_packages_have_valid_contracts(self):
        validator = load_validator()

        missing = [
            activity_id
            for activity_id in sorted(CURRENT_TWELVE_IDS)
            if not (REPO_ROOT / "activities" / activity_id / "activity_display_contract_v1.yaml").exists()
        ]
        issues = validator.validate_roots([REPO_ROOT / "activities" / activity_id for activity_id in CURRENT_TWELVE_IDS])

        self.assertEqual([], missing)
        self.assertEqual([], issues)

    def test_current_run_local_packages_have_valid_contracts(self):
        validator = load_validator()

        missing = [
            activity_id
            for activity_id in sorted(CURRENT_TWELVE_IDS)
            if not (RUN_LOCAL_ROOT / activity_id / "activity_display_contract_v1.yaml").exists()
        ]
        issues = validator.validate_roots([RUN_LOCAL_ROOT / activity_id for activity_id in CURRENT_TWELVE_IDS])

        self.assertEqual([], missing)
        self.assertEqual([], issues)

    def test_phoneme_hunt_uses_photo_verification_against_displayed_sound_target(self):
        validator = load_validator()

        contract_path = REPO_ROOT / "activities" / "concept_phoneme_hunt_collect" / "activity_display_contract_v1.yaml"
        contract = validator.load_yaml(contract_path)
        display_assets = {
            asset["display_asset_id"]: asset
            for asset in contract["display_assets"]
            if isinstance(asset, dict)
        }
        photo_frames = [
            frame
            for frame in contract["frames"]
            if frame.get("verification_policy", {}).get("type") == "photo_object_initial_sound"
        ]

        self.assertTrue(photo_frames)
        for frame in photo_frames:
            policy = frame["verification_policy"]
            target = policy["target"]
            self.assertEqual("display_asset", target["type"])
            self.assertEqual(frame["display_asset_id"], target["display_asset_id"])
            self.assertIn("photo_id", policy["evidence"])
            self.assertEqual(
                "b",
                str(display_assets[target["display_asset_id"]]["metadata"]["target_initial_sound"]).lower(),
            )


if __name__ == "__main__":
    unittest.main()
