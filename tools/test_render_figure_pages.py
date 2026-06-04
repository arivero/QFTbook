#!/usr/bin/env python3
"""Focused tests for tools/render_figure_pages.py."""

from __future__ import annotations

import importlib.util
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


def main() -> int:
    test_dependency_gate_requires_pillow_by_default()
    test_dependency_gate_reports_missing_render_tools()
    test_remove_unexpected_managed_outputs()
    test_write_contact_sheets_removes_stale_sheets()
    print("render_figure_pages tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
