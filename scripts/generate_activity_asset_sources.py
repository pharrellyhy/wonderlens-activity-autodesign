#!/usr/bin/env python3
"""Generate illustrative source PNGs for activity asset manifests.

This is the provider-backed half of the asset workflow. It reads
`asset_manifest.yaml` files, generates accepted illustrative source PNGs, and
writes them into the deterministic builder inbox:

    runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png

It does not write package-local runtime variants or update manifest paths.
Run `scripts/build_activity_assets.py` after source generation.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Protocol


DEFAULT_PROVIDER = "gemini"
DEFAULT_MODEL = "gemini-2.5-flash-image"
DEFAULT_ASPECT_RATIO = "1:1"
DEFAULT_OUTPUT_SIZE = (512, 512)
STYLE_DOC_PATH = Path("docs/activity_asset_generation_workflow.md")
SAFE_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]*$")
SECRET_PATTERNS = (
    re.compile(r"AIza[0-9A-Za-z_\-]{20,}"),
    re.compile(r"-----BEGIN [^-]+-----.*?-----END [^-]+-----", re.DOTALL),
    re.compile(r"/Users/[^ \n\t'\"`]+"),
)


class Provider(Protocol):
    auth_mode: str

    def generate_png(self, prompt: str) -> bytes:
        """Return provider-generated image bytes."""


@dataclass(frozen=True)
class AuthConfig:
    auth_mode: str
    location: str = "global"


@dataclass(frozen=True)
class AssetRequest:
    run_dir: Path
    package_dir: Path
    manifest_path: Path
    activity_id: str
    asset_id: str
    role: str
    label: str
    prompt_en: str
    palette: dict[str, Any]
    screen_targets: dict[str, Any]


def require_yaml():
    try:
        import yaml  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment guard
        raise RuntimeError("PyYAML is required. Install with `python3 -m pip install -r requirements-imagegen.txt`.") from exc
    return yaml


def require_pillow():
    try:
        from PIL import Image, ImageOps  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment guard
        raise RuntimeError("Pillow is required. Install with `python3 -m pip install -r requirements-imagegen.txt`.") from exc
    return Image, ImageOps


def load_yaml(path: Path) -> dict[str, Any]:
    yaml = require_yaml()
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    yaml = require_yaml()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def safe_id(value: Any, label: str) -> str:
    text = norm(value)
    if not SAFE_ID_PATTERN.fullmatch(text):
        raise ValueError(f"unsafe {label}: {text!r}")
    return text


def run_relative(run_dir: Path, path: Path) -> str:
    return path.resolve().relative_to(run_dir.resolve()).as_posix()


def safe_inbox_output_path(run_dir: Path, activity_id: str, asset_id: str) -> Path:
    activity_id = safe_id(activity_id, "activity id")
    asset_id = safe_id(asset_id, "asset id")
    output = (run_dir / "generated_assets" / "inbox" / activity_id / f"{asset_id}.png").resolve()
    try:
        output.relative_to(run_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"output path escapes run directory for {activity_id}/{asset_id}") from exc
    return output


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        raise FileNotFoundError(f"env file not found: {path}")
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def load_env_file(path: Path, *, override: bool = False) -> None:
    for key, value in parse_env_file(path).items():
        if override or key not in os.environ:
            os.environ[key] = value


def configure_credentials(
    *,
    env_file: Path | None,
    google_credentials: Path | None,
    location: str | None,
) -> AuthConfig:
    if env_file is not None:
        load_env_file(env_file)
    if google_credentials is not None:
        if not google_credentials.exists():
            raise FileNotFoundError("Google credentials file was requested but does not exist.")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(google_credentials.resolve())

    project = norm(os.environ.get("GOOGLE_CLOUD_PROJECT"))
    api_key = norm(os.environ.get("GEMINI_API_KEY"))
    credentials_path = norm(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    provider_location = norm(location) or norm(os.environ.get("WONDERLENS_GEMINI_LOCATION")) or "global"

    if project:
        if not credentials_path:
            raise RuntimeError(
                "GOOGLE_CLOUD_PROJECT is set, but GOOGLE_APPLICATION_CREDENTIALS is missing. "
                "Export a service-account path or pass --google-credentials."
            )
        if not Path(credentials_path).exists():
            raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS points to a missing file.")
        return AuthConfig(auth_mode="vertex", location=provider_location)
    if api_key:
        return AuthConfig(auth_mode="api_key", location=provider_location)
    raise RuntimeError(
        "Gemini credentials are missing. Export GOOGLE_CLOUD_PROJECT plus "
        "GOOGLE_APPLICATION_CREDENTIALS, or export GEMINI_API_KEY."
    )


def sanitize_text(text: Any, *, extra_secrets: list[str] | None = None) -> str:
    result = str(text)
    env_secrets = [
        os.environ.get("GEMINI_API_KEY", ""),
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""),
    ]
    for secret in [*(extra_secrets or []), *env_secrets]:
        if secret and len(secret) >= 4:
            result = result.replace(secret, "[REDACTED]")
    for pattern in SECRET_PATTERNS:
        result = pattern.sub("[REDACTED]", result)
    return result


def sanitized_error(exc: BaseException) -> str:
    return f"{type(exc).__name__}: {sanitize_text(str(exc))[:240]}"


def discover_manifest_paths(run_dir: Path) -> list[Path]:
    root = run_dir / "activity_packages"
    if not root.exists():
        return []
    return sorted(root.rglob("asset_manifest.yaml"))


def is_generated_illustrative_asset(asset: dict[str, Any]) -> bool:
    return (
        norm(asset.get("accuracy_mode")) == "illustrative"
        and norm(asset.get("source_strategy")) == "generated_illustrative"
    )


def select_requests(
    run_dir: Path,
    *,
    activity_id: str | None = None,
    asset_id: str | None = None,
    limit: int | None = None,
) -> tuple[list[AssetRequest], list[dict[str, Any]]]:
    run_dir = run_dir.resolve()
    selected: list[AssetRequest] = []
    skipped: list[dict[str, Any]] = []
    activity_filter = safe_id(activity_id, "activity filter") if activity_id else None
    asset_filter = safe_id(asset_id, "asset filter") if asset_id else None

    for manifest_path in discover_manifest_paths(run_dir):
        package_dir = manifest_path.parent
        manifest = load_yaml(manifest_path)
        manifest_activity_id = safe_id(norm(manifest.get("activity_id")) or package_dir.name, "activity id")
        if activity_filter and manifest_activity_id != activity_filter:
            continue
        assets = manifest.get("assets")
        if not isinstance(assets, list):
            continue
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            current_asset_id = safe_id(asset.get("id"), "asset id")
            if asset_filter and current_asset_id != asset_filter:
                continue
            if not is_generated_illustrative_asset(asset):
                skipped.append(
                    {
                        "activity_id": manifest_activity_id,
                        "asset_id": current_asset_id,
                        "status": "skipped",
                        "reason": "not generated_illustrative",
                        "accuracy_mode": norm(asset.get("accuracy_mode")),
                        "source_strategy": norm(asset.get("source_strategy")),
                    }
                )
                continue
            prompt = norm(asset.get("prompt_en"))
            if not prompt:
                skipped.append(
                    {
                        "activity_id": manifest_activity_id,
                        "asset_id": current_asset_id,
                        "status": "skipped",
                        "reason": "missing prompt_en",
                    }
                )
                continue
            selected.append(
                AssetRequest(
                    run_dir=run_dir,
                    package_dir=package_dir,
                    manifest_path=manifest_path,
                    activity_id=manifest_activity_id,
                    asset_id=current_asset_id,
                    role=norm(asset.get("role")),
                    label=norm(asset.get("label")),
                    prompt_en=prompt,
                    palette=manifest.get("palette") if isinstance(manifest.get("palette"), dict) else {},
                    screen_targets=manifest.get("screen_targets") if isinstance(manifest.get("screen_targets"), dict) else {},
                )
            )
            if limit is not None and len(selected) >= limit:
                return selected, skipped
    return selected, skipped


def extract_style_contract(style_path: Path) -> str:
    if not style_path.exists():
        raise FileNotFoundError(f"style contract not found: {style_path}")
    text = style_path.read_text()
    start = text.find("## Current Style Contract")
    end = text.find("## Independent Image QA", start)
    if start == -1:
        return text[:5000]
    if end == -1:
        end = len(text)
    return text[start:end].strip()[:5000]


def compose_prompt(request: AssetRequest, style_contract: str) -> str:
    palette = ", ".join(f"{key}: {value}" for key, value in request.palette.items())
    targets = ", ".join(f"{key}: {value}" for key, value in request.screen_targets.items())
    return "\n".join(
        [
            "Generate exactly one WonderLens runtime source image.",
            "Output: square 512x512 PNG, no contact sheet, no text, no letters, no numbers, no logos.",
            "Do not include device chrome, progress dots, buttons, picker slots, masks, borders, or UI labels.",
            "Keep important content inside the central round-screen safe area.",
            f"Activity ID: {request.activity_id}",
            f"Asset ID: {request.asset_id}",
            f"Asset role: {request.role}",
            f"Asset label: {request.label}",
            f"Asset prompt: {request.prompt_en}",
            f"Palette: {palette or 'Use the WonderLens flat Nordic palette.'}",
            f"Screen targets: {targets or 'Square source art for later round-screen fitting.'}",
            "",
            "Style contract:",
            style_contract,
        ]
    )


def normalize_png(image_bytes: bytes, *, size: tuple[int, int] = DEFAULT_OUTPUT_SIZE) -> bytes:
    Image, ImageOps = require_pillow()
    with Image.open(io.BytesIO(image_bytes)) as image:
        image = image.convert("RGBA")
        image = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS)
        output = io.BytesIO()
        image.save(output, format="PNG")
        return output.getvalue()


def png_size(image_bytes: bytes) -> tuple[int, int]:
    Image, _ = require_pillow()
    with Image.open(io.BytesIO(image_bytes)) as image:
        return image.size


def extract_image_bytes(response: Any) -> bytes:
    parts = getattr(response, "parts", None)
    candidates = getattr(response, "candidates", None)
    if parts is None and candidates:
        candidate = candidates[0]
        parts = getattr(getattr(candidate, "content", None), "parts", None)
    for part in parts or []:
        inline_data = getattr(part, "inline_data", None)
        if inline_data is not None:
            data = getattr(inline_data, "data", None)
            if data:
                return data
    raise RuntimeError("Gemini returned no inline image data.")


class GeminiProvider:
    def __init__(
        self,
        *,
        model: str,
        auth_config: AuthConfig,
        aspect_ratio: str,
        retries: int,
        retry_delay: float,
    ) -> None:
        self.model = model
        self.auth_config = auth_config
        self.auth_mode = auth_config.auth_mode
        self.aspect_ratio = aspect_ratio
        self.retries = retries
        self.retry_delay = retry_delay

    def _client(self) -> Any:
        try:
            from google import genai  # type: ignore
        except ImportError as exc:  # pragma: no cover - environment guard
            raise RuntimeError(
                "google-genai is required. Install with `python3 -m pip install -r requirements-imagegen.txt`."
            ) from exc
        if self.auth_config.auth_mode == "vertex":
            return genai.Client(
                vertexai=True,
                project=os.environ["GOOGLE_CLOUD_PROJECT"],
                location=self.auth_config.location,
            )
        return genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def generate_png(self, prompt: str) -> bytes:
        try:
            from google.genai import errors as genai_errors  # type: ignore
            from google.genai import types  # type: ignore
        except ImportError as exc:  # pragma: no cover - environment guard
            raise RuntimeError(
                "google-genai is required. Install with `python3 -m pip install -r requirements-imagegen.txt`."
            ) from exc

        client = self._client()
        retryable_types = (genai_errors.ClientError, genai_errors.APIError)
        for attempt in range(max(self.retries, 1)):
            try:
                response = client.models.generate_content(
                    model=self.model,
                    contents=[prompt],
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE"],
                        image_config=types.ImageConfig(aspect_ratio=self.aspect_ratio),
                    ),
                )
                return extract_image_bytes(response)
            except retryable_types as exc:
                is_retryable = "RESOURCE_EXHAUSTED" in str(exc) or "429" in str(exc)
                if not is_retryable or attempt == self.retries - 1:
                    raise
                time.sleep(self.retry_delay)
        raise RuntimeError("Gemini generation exhausted retries.")


def make_provider(
    *,
    provider_name: str,
    model: str,
    env_file: Path | None,
    google_credentials: Path | None,
    location: str | None,
    aspect_ratio: str,
    retries: int,
    retry_delay: float,
) -> Provider:
    if provider_name != "gemini":
        raise ValueError(f"unsupported provider: {provider_name}")
    auth_config = configure_credentials(
        env_file=env_file,
        google_credentials=google_credentials,
        location=location,
    )
    return GeminiProvider(
        model=model,
        auth_config=auth_config,
        aspect_ratio=aspect_ratio,
        retries=retries,
        retry_delay=retry_delay,
    )


def provider_audit_path(run_dir: Path, provider_name: str) -> Path:
    provider_id = safe_id(provider_name, "provider")
    timestamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S")
    path = (run_dir / "generated_assets" / "provider_runs" / f"{timestamp}_{provider_id}_source_generation.yaml").resolve()
    try:
        path.relative_to(run_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"provider audit path escapes run directory for provider {provider_id!r}") from exc
    return path


def generate_sources(
    run_dir: Path,
    *,
    provider_name: str = DEFAULT_PROVIDER,
    model: str = DEFAULT_MODEL,
    activity_id: str | None = None,
    asset_id: str | None = None,
    limit: int | None = None,
    force: bool = False,
    env_file: Path | None = None,
    google_credentials: Path | None = None,
    location: str | None = None,
    aspect_ratio: str = DEFAULT_ASPECT_RATIO,
    retries: int = 3,
    retry_delay: float = 3.0,
    style_path: Path = STYLE_DOC_PATH,
    provider: Provider | None = None,
) -> dict[str, Any]:
    run_dir = run_dir.resolve()
    if not run_dir.exists():
        raise FileNotFoundError(f"run directory not found: {run_dir}")
    selected, skipped = select_requests(run_dir, activity_id=activity_id, asset_id=asset_id, limit=limit)
    if not selected:
        raise RuntimeError("No generated illustrative assets matched the requested filters.")

    style_contract = extract_style_contract(style_path)
    active_provider = provider or make_provider(
        provider_name=provider_name,
        model=model,
        env_file=env_file,
        google_credentials=google_credentials,
        location=location,
        aspect_ratio=aspect_ratio,
        retries=retries,
        retry_delay=retry_delay,
    )

    entries: list[dict[str, Any]] = []
    generated = 0
    failed = 0
    for request in selected:
        output_path = safe_inbox_output_path(run_dir, request.activity_id, request.asset_id)
        output_rel = run_relative(run_dir, output_path)
        if output_path.exists() and not force:
            entries.append(
                {
                    "activity_id": request.activity_id,
                    "asset_id": request.asset_id,
                    "status": "exists",
                    "output_path": output_rel,
                    "sha256": sha256_file(output_path),
                    "byte_count": output_path.stat().st_size,
                }
            )
            continue
        prompt = compose_prompt(request, style_contract)
        try:
            raw_png = active_provider.generate_png(prompt)
            normalized = normalize_png(raw_png)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(normalized)
            width, height = png_size(normalized)
            generated += 1
            entries.append(
                {
                    "activity_id": request.activity_id,
                    "asset_id": request.asset_id,
                    "status": "generated",
                    "output_path": output_rel,
                    "width": width,
                    "height": height,
                    "sha256": sha256_bytes(normalized),
                    "byte_count": len(normalized),
                    "prompt_source": "asset_manifest.yaml:prompt_en + docs/activity_asset_generation_workflow.md",
                }
            )
        except Exception as exc:  # pragma: no cover - exercised through tests with fake provider
            failed += 1
            entries.append(
                {
                    "activity_id": request.activity_id,
                    "asset_id": request.asset_id,
                    "status": "failed",
                    "output_path": output_rel,
                    "error": sanitized_error(exc),
                }
            )

    audit = {
        "run_id": run_dir.name,
        "provider": provider_name,
        "model": model,
        "auth_mode": getattr(active_provider, "auth_mode", "unknown"),
        "generated_at": now_iso(),
        "style_source": STYLE_DOC_PATH.as_posix(),
        "output_root": "generated_assets/inbox",
        "selected_count": len(selected),
        "generated_count": generated,
        "existing_count": sum(1 for entry in entries if entry.get("status") == "exists"),
        "skipped_count": len(skipped),
        "failed_count": failed,
        "entries": entries,
        "skipped": skipped,
    }
    audit_path = provider_audit_path(run_dir, provider_name)
    write_yaml(audit_path, audit)
    result = {
        "run_id": run_dir.name,
        "provider": provider_name,
        "model": model,
        "selected": len(selected),
        "generated": generated,
        "existing": audit["existing_count"],
        "skipped": len(skipped),
        "failed": failed,
        "audit_path": run_relative(run_dir, audit_path),
    }
    if failed:
        raise RuntimeError(
            "One or more source assets failed to generate. "
            f"See {result['audit_path']} for sanitized details."
        )
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", default=DEFAULT_PROVIDER, choices=["gemini"], help="Image provider to use.")
    parser.add_argument("--model", default=os.environ.get("WONDERLENS_IMAGE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--run", required=True, type=Path, help="Path to runs/<run_id>.")
    parser.add_argument("--activity", help="Generate sources for one activity_id.")
    parser.add_argument("--asset", help="Generate one asset_id within the selected activity.")
    parser.add_argument("--limit", type=int, help="Maximum number of illustrative source PNGs to generate.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing inbox PNGs.")
    parser.add_argument("--env-file", type=Path, help="Optional .env file to load without printing values.")
    parser.add_argument("--google-credentials", type=Path, help="Optional service-account JSON path.")
    parser.add_argument("--location", help="Vertex AI location. Defaults to global to match fullstack-demo image generation.")
    parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO, help="Provider aspect ratio request.")
    parser.add_argument("--retries", type=int, default=3, help="Retry count for retryable provider errors.")
    parser.add_argument("--retry-delay", type=float, default=3.0, help="Seconds between retryable provider attempts.")
    args = parser.parse_args(argv)

    try:
        result = generate_sources(
            args.run,
            provider_name=args.provider,
            model=args.model,
            activity_id=args.activity,
            asset_id=args.asset,
            limit=args.limit,
            force=args.force,
            env_file=args.env_file,
            google_credentials=args.google_credentials,
            location=args.location,
            aspect_ratio=args.aspect_ratio,
            retries=args.retries,
            retry_delay=args.retry_delay,
        )
    except Exception as exc:
        print(f"FAIL source generation: {sanitized_error(exc)}", file=sys.stderr)
        return 1

    print(
        "OK source generation: "
        f"provider={result['provider']} model={result['model']} "
        f"selected={result['selected']} generated={result['generated']} "
        f"existing={result['existing']} skipped={result['skipped']} "
        f"audit={result['audit_path']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
