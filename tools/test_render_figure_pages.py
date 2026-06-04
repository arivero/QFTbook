#!/usr/bin/env python3
"""Focused tests for tools/render_figure_pages.py."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "render_figure_pages.py"


def load_module():
    spec = importlib.util.spec_from_file_location("render_figure_pages", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def assert_system_exit_contains(callable_obj, needle: str) -> None:
    try:
        callable_obj()
    except SystemExit as exc:
        if needle not in str(exc):
            raise AssertionError(f"expected {needle!r} in SystemExit message, got {exc!r}")
        return
    raise AssertionError("expected SystemExit")


def test_dependency_gate_requires_pillow_by_default() -> None:
    module = load_module()
    original_which = module.shutil.which
    original_find_spec = module.importlib.util.find_spec
    try:
        module.shutil.which = lambda name: f"/usr/bin/{name}"
        module.importlib.util.find_spec = (
            lambda name: None if name == "PIL" else original_find_spec(name)
        )
        assert_system_exit_contains(
            lambda: module.check_dependencies(render_page_images=True, contact_sheets=True),
            "--no-contact-sheets",
        )
        module.check_dependencies(render_page_images=True, contact_sheets=False)
    finally:
        module.shutil.which = original_which
        module.importlib.util.find_spec = original_find_spec


def test_dependency_gate_reports_missing_render_tools() -> None:
    module = load_module()
    original_which = module.shutil.which
    original_find_spec = module.importlib.util.find_spec
    try:
        module.shutil.which = lambda _name: None
        module.importlib.util.find_spec = lambda name: object() if name == "PIL" else object()
        assert_system_exit_contains(
            lambda: module.check_dependencies(render_page_images=True, contact_sheets=True),
            "qpdf",
        )
        assert_system_exit_contains(
            lambda: module.check_dependencies(render_page_images=True, contact_sheets=True),
            "pdftoppm",
        )
    finally:
        module.shutil.which = original_which
        module.importlib.util.find_spec = original_find_spec


def test_remove_unexpected_managed_outputs() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        page_dir = Path(tmp) / "pages"
        page_dir.mkdir()
        keep = page_dir / "page-0001.png"
        stale = page_dir / "page-9999.png"
        keep.write_bytes(b"current")
        stale.write_bytes(b"stale")

        module.remove_unexpected_files(page_dir, "page-*.png", {"page-0001.png"})

        if not keep.exists():
            raise AssertionError("current page output was removed")
        if stale.exists():
            raise AssertionError("stale page output was not removed")


def test_write_contact_sheets_removes_stale_sheets() -> None:
    module = load_module()
    from PIL import Image

    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        page_dir = out_dir / "pages"
        sheet_dir = out_dir / "contact"
        page_dir.mkdir()
        sheet_dir.mkdir()
        Image.new("RGB", (80, 120), "white").save(page_dir / "page-0001.png")
        (sheet_dir / "sheet-99.png").write_bytes(b"stale")
        row = module.FigureManifestRow(
            label="fig:test",
            number="1.1",
            printed_page="1",
            physical_page=1,
            anchor="figure.test",
            caption="test figure",
        )

        module.write_contact_sheets([row], out_dir, columns=1, thumb_width=40)

        if not (sheet_dir / "sheet-01.png").exists():
            raise AssertionError("current contact sheet was not written")
        if (sheet_dir / "sheet-99.png").exists():
            raise AssertionError("stale contact sheet was not removed")


def test_write_manifest_includes_render_provenance() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        row = module.FigureManifestRow(
            label="fig:test",
            number="1.1",
            printed_page="1",
            physical_page=7,
            anchor="figure.test",
            caption="test figure",
        )
        provenance = {
            "schema": module.PROVENANCE_SCHEMA,
            "pdf": {"path": "main.pdf", "sha256": "pdf-digest"},
            "renderer": {
                "program": "pdftoppm",
                "executable": "pdftoppm",
                "version": "pdftoppm test",
            },
            "options": {"dpi": 72, "format": "png"},
        }

        module.write_manifest(
            [row],
            out_dir,
            provenance=provenance,
            page_sha256={7: "page-digest"},
        )

        data = json.loads(
            (out_dir / "figure_pages_manifest.json").read_text(encoding="utf-8")
        )
        if data[0]["pdf_sha256"] != "pdf-digest":
            raise AssertionError("manifest did not record the PDF digest")
        if data[0]["page_image_sha256"] != "page-digest":
            raise AssertionError("manifest did not record the page image digest")
        if data[0]["renderer"]["version"] != "pdftoppm test":
            raise AssertionError("manifest did not record the renderer version")


def test_render_pages_repairs_wrong_same_named_cache() -> None:
    module = load_module()
    from PIL import Image

    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        pdf_path = out_dir / "main.pdf"
        pdf_path.write_bytes(b"%PDF-1.7 fake test file\n")
        colors = {
            1: (30, 60, 90),
            2: (190, 40, 20),
        }
        rendered_pages: list[int] = []
        original_run = module.subprocess.run

        def fake_run(command, **_kwargs):
            executable = Path(command[0]).name
            if executable == "pdftoppm" and command[1:] == ["-v"]:
                return subprocess.CompletedProcess(
                    command,
                    0,
                    stdout="",
                    stderr="pdftoppm version test-1.0\n",
                )
            if executable == "pdftoppm":
                page = int(command[command.index("-f") + 1])
                prefix = Path(command[-1])
                Image.new("RGB", (18, 18), colors[page]).save(
                    prefix.with_suffix(".png")
                )
                rendered_pages.append(page)
                return subprocess.CompletedProcess(command, 0)
            raise AssertionError(f"unexpected command: {command}")

        try:
            module.subprocess.run = fake_run
            first = module.render_pages(pdf_path, [1, 2], out_dir, dpi=72, force=False)
            if rendered_pages != [1, 2]:
                raise AssertionError(f"first render did not render both pages: {rendered_pages}")
            first_page_digest = first.page_sha256[1]
            Image.new("RGB", (18, 18), colors[2]).save(out_dir / "pages" / "page-0001.png")

            rendered_pages.clear()
            second = module.render_pages(pdf_path, [1, 2], out_dir, dpi=72, force=False)
        finally:
            module.subprocess.run = original_run

        if rendered_pages != [1]:
            raise AssertionError(f"wrong same-named cache was not repaired: {rendered_pages}")
        if second.rendered != 1 or second.reused != 1:
            raise AssertionError("rerun did not re-render only the corrupted page")
        if second.page_sha256[1] != first_page_digest:
            raise AssertionError("repaired page digest does not match the original render")
        provenance = json.loads(
            (out_dir / module.PROVENANCE_FILE).read_text(encoding="utf-8")
        )
        if provenance["pages"]["1"]["sha256"] != first_page_digest:
            raise AssertionError("provenance was not refreshed after repairing the page")


def main() -> int:
    test_dependency_gate_requires_pillow_by_default()
    test_dependency_gate_reports_missing_render_tools()
    test_remove_unexpected_managed_outputs()
    test_write_contact_sheets_removes_stale_sheets()
    test_write_manifest_includes_render_provenance()
    test_render_pages_repairs_wrong_same_named_cache()
    print("render_figure_pages tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
