import importlib.util
import copy
import pathlib
import tempfile
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "demo_package_contract"
MATRIX_PATH = REPO_ROOT / "docs" / "activity_parameterization_matrix.yaml"
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
    path = REPO_ROOT / "scripts" / "validate_demo_package_contract.py"
    spec = importlib.util.spec_from_file_location("validate_demo_package_contract", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DemoPackageContractValidatorTest(unittest.TestCase):
    def test_valid_fixture_set_passes(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "valid"])

        self.assertEqual([], issues)

    def test_reference_bound_asset_requires_source(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "reference_bound_missing_source"])

        self.assertIn("reference_bound asset must declare at least one source", "\n".join(issues))

    def test_reference_bound_asset_rejects_generate_new_policy(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "reference_bound_generate_new"])

        self.assertIn("reference_bound asset must use an approved reference source_strategy", "\n".join(issues))
        self.assertIn("reference_bound asset must not use generate_new transformation_policy", "\n".join(issues))

    def test_supported_package_requires_entity_binding(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "supported_missing_binding"])

        self.assertIn("supported package must declare an entity binding", "\n".join(issues))

    def test_supported_package_rejects_judgment_template(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "supported_judgment_template"])

        self.assertIn("supported package must not use cat5_judgment ui_template", "\n".join(issues))

    def test_asset_manifest_requires_entity_id(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "missing_asset_entity_id"])

        self.assertIn("missing required field entity_id", "\n".join(issues))

    def test_required_asset_rejects_thumbnail_only_variants(self):
        validator = load_validator()
        manifest = validator.load_yaml(FIXTURE_ROOT / "valid" / "supported_cat5" / "asset_manifest.yaml")
        asset = copy.deepcopy(manifest["assets"][1])
        asset["variants"] = [
            {
                "id": "round_128",
                "target": "round_device_screen",
                "size": "128x128",
                "path": None,
            }
        ]

        issues = validator.validate_asset(pathlib.Path("package"), asset, manifest["screen_targets"], 0)

        self.assertIn("required asset must include at least one high-resolution runtime variant", "\n".join(issues))

    def test_root_with_no_demo_extensions_passes(self):
        validator = load_validator()

        with tempfile.TemporaryDirectory() as tmp:
            issues = validator.validate_roots([pathlib.Path(tmp)])

        self.assertEqual([], issues)

    def test_supported_package_requires_parameterization(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "supported_missing_parameterization"])

        self.assertIn("supported package must declare parameterization", "\n".join(issues))

    def test_dynamic_mode_requires_handoff_and_derived_fields(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "entity_target_missing_runtime_fields"])

        joined = "\n".join(issues)
        self.assertIn("dynamic parameterization mode entity_target must declare validity.requires", joined)
        self.assertIn("dynamic parameterization mode entity_target must declare source_fields", joined)
        self.assertIn("dynamic parameterization mode entity_target must declare derived_runtime_fields", joined)

    def test_initial_sound_mode_rejects_static_target_sound(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "phoneme_static_target_sound"])

        self.assertIn("initial_sound_from_entity must not hard-code authored_constants.target_sound", "\n".join(issues))

    def test_fixed_mode_requires_authored_constants(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "invalid" / "fixed_missing_authored_constants"])

        self.assertIn("fixed parameterization mode must declare authored_constants", "\n".join(issues))

    def test_valid_initial_sound_parameterization_passes(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "valid" / "initial_sound_from_entity"])

        self.assertEqual([], issues)

    def test_valid_entity_theme_parameterization_passes(self):
        validator = load_validator()

        issues = validator.validate_roots([FIXTURE_ROOT / "valid" / "entity_theme"])

        self.assertEqual([], issues)

    def test_current_twelve_parameterization_matrix_covers_goal_ids(self):
        validator = load_validator()

        matrix = validator.load_yaml(MATRIX_PATH)
        rows = matrix.get("activities", [])
        activity_ids = {row.get("activity_id") for row in rows if isinstance(row, dict)}

        self.assertTrue(MATRIX_PATH.exists())
        self.assertEqual(CURRENT_TWELVE_IDS, activity_ids)
        for row in rows:
            mode = row.get("mode")
            self.assertIn(mode, validator.PARAMETERIZATION_MODES)
            self.assertTrue(row.get("evidence"))
            self.assertTrue(row.get("metadata_action"))
            self.assertTrue(row.get("fallback_behavior"))
            self.assertTrue(row.get("reviewer_action"))
            self.assertIn("validity", row)
            self.assertIn("source_fields", row)
            self.assertIn("derived_runtime_fields", row)
            self.assertIn("authored_constants", row)
            if mode in validator.DYNAMIC_PARAMETERIZATION_MODES:
                self.assertTrue(row["validity"].get("requires"))
                self.assertTrue(row["source_fields"])
                self.assertTrue(row["derived_runtime_fields"])
            if mode in validator.FIXED_PARAMETERIZATION_MODES:
                self.assertTrue(row["authored_constants"])


if __name__ == "__main__":
    unittest.main()
