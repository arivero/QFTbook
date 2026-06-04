#!/usr/bin/env python3
"""Focused tests for tools/audit_rendered_figure_pages.py."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "audit_rendered_figure_pages.py"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_fixture(root: Path) -> tuple[Path, Path]:
    from PIL import Image, ImageDraw

    out_dir = root / "figure_audit"
    page_dir = out_dir / "pages"
    contact_dir = out_dir / "contact"
    page_dir.mkdir(parents=True)
    contact_dir.mkdir()

    pdf_path = root / "main.pdf"
    pdf_path.write_bytes(b"%PDF synthetic fixture\n")
    page_path = page_dir / "page-0001.png"
    image = Image.new("RGB", (200, 260), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([40, 50, 160, 180], outline="black", width=3)
    draw.line([50, 170, 150, 60], fill=(10, 10, 10), width=4)
    image.save(page_path)
    Image.new("RGB", (80, 80), "white").save(contact_dir / "sheet-01.png")

    manifest = [
        {
            "label": "fig:test",
            "number": "1.1",
            "printed_page": "1",
            "physical_page": 1,
            "anchor": "figure.test",
            "caption": "test figure",
            "pdf_sha256": sha256_file(pdf_path),
            "render_dpi": 120,
            "renderer": {"version": "pdftoppm fixture"},
            "render_options": {"dpi": 120},
            "page_image_sha256": sha256_file(page_path),
        }
    ]
    provenance = {
        "schema": 1,
        "pdf": {"path": str(pdf_path), "sha256": sha256_file(pdf_path)},
        "renderer": {"program": "pdftoppm", "version": "pdftoppm fixture"},
        "options": {"dpi": 120},
        "pages": {
            "1": {
                "file": "pages/page-0001.png",
                "sha256": sha256_file(page_path),
            }
        },
    }
    (out_dir / "figure_pages_manifest.json").write_text(
        json.dumps(manifest) + "\n",
        encoding="utf-8",
    )
    (out_dir / "render_provenance.json").write_text(
        json.dumps(provenance) + "\n",
        encoding="utf-8",
    )
    return out_dir, pdf_path


def run_audit(out_dir: Path, pdf_path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--out-dir",
            str(out_dir),
            "--pdf",
            str(pdf_path),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def test_fixture_passes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out_dir, pdf_path = write_fixture(Path(tmp))
        proc = run_audit(out_dir, pdf_path)
        if proc.returncode != 0:
            raise AssertionError(proc.stdout + proc.stderr)
        report = json.loads(
            (out_dir / "rendered_figure_page_audit.json").read_text()
        )
        if report["summary"]["status"] != "passed":
            raise AssertionError("fixture did not produce a passing report")


def test_digest_mismatch_fails() -> None:
    from PIL import Image

    with tempfile.TemporaryDirectory() as tmp:
        out_dir, pdf_path = write_fixture(Path(tmp))
        Image.new("RGB", (200, 260), "white").save(
            out_dir / "pages" / "page-0001.png"
        )
        proc = run_audit(out_dir, pdf_path)
        if proc.returncode == 0:
            raise AssertionError("digest mismatch unexpectedly passed")
        if "digest mismatch" not in proc.stdout:
            raise AssertionError(proc.stdout + proc.stderr)


def main() -> int:
    test_fixture_passes()
    test_digest_mismatch_fails()
    print("audit_rendered_figure_pages tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
