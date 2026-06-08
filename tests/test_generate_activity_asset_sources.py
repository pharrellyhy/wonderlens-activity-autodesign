import importlib.util
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest
from io import BytesIO
from unittest import mock

import yaml
from PIL import Image


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def load_script():
    path = REPO_ROOT / "scripts" / "generate_activity_asset_sources.py"
    spec = importlib.util.spec_from_file_location("generate_activity_asset_sources", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def png_bytes(size=(768, 768), color=(117, 207, 151, 255)):
    image = Image.new("RGBA", size, color)
    output = BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()


def write_yaml(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def read_yaml(path):
    return yaml.safe_load(path.read_text()) or {}


def make_run(run_dir, *, unsafe_asset_id=False):
    package_dir = run_dir / "activity_packages" / "source_smoke"
    package_dir.mkdir(parents=True)
    write_yaml(
        package_dir / "asset_manifest.yaml",
        {
            "activity_id": "source_smoke",
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
                }
            },
            "assets": [
                {
                    "id": "../escape" if unsafe_asset_id else "moss_icon",
                    "role": "collection_correct",
                    "label": "Fuzzy moss",
                    "requiredness": "required",
                    "accuracy_mode": "illustrative",
                    "source_strategy": "generated_illustrative",
                    "transformation_policy": "generate_new",
                    "prompt_en": "Flat Nordic child-safe moss patch, no text.",
                    "variants": [{"id": "round_1024", "target": "round_device_screen", "size": "1024x1024", "path": None}],
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
                    "prompt_en": "Preserve approved Orion star positions exactly.",
                    "variants": [{"id": "round_1024", "target": "round_device_screen", "size": "1024x1024", "path": None}],
                    "fallback_behavior": "Do not claim Orion without source evidence.",
                },
            ],
        },
    )
    return package_dir


class FakeProvider:
    auth_mode = "fake"

    def __init__(self):
        self.calls = 0

    def generate_png(self, prompt):
        self.calls += 1
        self.last_prompt = prompt
        return png_bytes()


class FailingProvider:
    auth_mode = "fake"

    def __init__(self, secret):
        self.secret = secret

    def generate_png(self, prompt):
        raise RuntimeError(f"provider rejected token {self.secret} from /Users/example/secret.json")


class GenerateActivityAssetSourcesTest(unittest.TestCase):
    def test_fake_provider_writes_512_inbox_png_and_sanitized_audit(self):
        script = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "source_test"
            make_run(run_dir)
            provider = FakeProvider()

            result = script.generate_sources(
                run_dir,
                provider=provider,
                activity_id="source_smoke",
                provider_name="gemini",
                model="gemini-2.5-flash-image",
            )

            output = run_dir / "generated_assets" / "inbox" / "source_smoke" / "moss_icon.png"
            audit = read_yaml(run_dir / result["audit_path"])
            self.assertEqual(1, provider.calls)
            self.assertTrue(output.exists())
            with Image.open(output) as image:
                self.assertEqual((512, 512), image.size)
                self.assertEqual("PNG", image.format)
            self.assertEqual("generated", audit["entries"][0]["status"])
            self.assertEqual("generated_assets/inbox/source_smoke/moss_icon.png", audit["entries"][0]["output_path"])
            self.assertEqual(1, audit["skipped_count"])
            self.assertNotIn("/Users/", (run_dir / result["audit_path"]).read_text())

    def test_existing_output_is_not_overwritten_without_force(self):
        script = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "source_test"
            make_run(run_dir)
            output = run_dir / "generated_assets" / "inbox" / "source_smoke" / "moss_icon.png"
            output.parent.mkdir(parents=True)
            output.write_bytes(png_bytes(color=(1, 2, 3, 255)))
            provider = FakeProvider()

            result = script.generate_sources(run_dir, provider=provider, activity_id="source_smoke")

            self.assertEqual(0, provider.calls)
            self.assertEqual(0, result["generated"])
            self.assertEqual(1, result["existing"])

    def test_missing_credentials_fails_with_setup_guidance(self):
        script = load_script()
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "Gemini credentials are missing"):
                script.configure_credentials(env_file=None, google_credentials=None, location=None)

    def test_env_file_and_google_credentials_select_vertex(self):
        script = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            env_file = root / ".env"
            credentials = root / ".elaborate-baton-test.json"
            env_file.write_text('GOOGLE_CLOUD_PROJECT="project-for-test"\nGEMINI_API_KEY="unused"\n')
            credentials.write_text("{}\n")
            with mock.patch.dict(os.environ, {}, clear=True):
                auth = script.configure_credentials(
                    env_file=env_file,
                    google_credentials=credentials,
                    location=None,
                )

            self.assertEqual("vertex", auth.auth_mode)
            self.assertEqual("global", auth.location)

    def test_unsafe_asset_id_is_rejected_before_writing(self):
        script = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "source_test"
            make_run(run_dir, unsafe_asset_id=True)

            with self.assertRaisesRegex(ValueError, "unsafe asset id"):
                script.generate_sources(run_dir, provider=FakeProvider(), activity_id="source_smoke")

            self.assertFalse((run_dir / "generated_assets" / "inbox" / "source_smoke").exists())

    def test_unsafe_provider_name_cannot_escape_audit_path(self):
        script = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "source_test"
            make_run(run_dir)

            with self.assertRaisesRegex(ValueError, "unsafe provider"):
                script.generate_sources(
                    run_dir,
                    provider=FakeProvider(),
                    activity_id="source_smoke",
                    provider_name="x/../../../../escape",
                )

            self.assertFalse((pathlib.Path(tmp) / "escape_source_generation.yaml").exists())

    def test_provider_failure_audit_redacts_secret_and_local_path(self):
        script = load_script()
        secret = "AIza" + "A" * 32
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = pathlib.Path(tmp) / "runs" / "source_test"
            make_run(run_dir)
            with mock.patch.dict(os.environ, {"GEMINI_API_KEY": secret}, clear=True):
                with self.assertRaisesRegex(RuntimeError, "failed to generate"):
                    script.generate_sources(
                        run_dir,
                        provider=FailingProvider(secret),
                        activity_id="source_smoke",
                    )

            audit_files = list((run_dir / "generated_assets" / "provider_runs").glob("*_source_generation.yaml"))
            self.assertEqual(1, len(audit_files))
            audit_text = audit_files[0].read_text()
            self.assertNotIn(secret, audit_text)
            self.assertNotIn("/Users/", audit_text)
            self.assertIn("[REDACTED]", audit_text)

    def test_help_runs_without_provider_credentials(self):
        result = subprocess.run(
            [PYTHON, str(REPO_ROOT / "scripts" / "generate_activity_asset_sources.py"), "--help"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode)
        self.assertIn("--provider", result.stdout)


if __name__ == "__main__":
    unittest.main()
