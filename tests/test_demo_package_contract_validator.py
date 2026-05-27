import importlib.util
import pathlib
import tempfile
import unittest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "demo_package_contract"


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

    def test_root_with_no_demo_extensions_passes(self):
        validator = load_validator()

        with tempfile.TemporaryDirectory() as tmp:
            issues = validator.validate_roots([pathlib.Path(tmp)])

        self.assertEqual([], issues)


if __name__ == "__main__":
    unittest.main()
