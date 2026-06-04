#!/usr/bin/env python3
"""Focused tests for tools/verify_release.py."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "verify_release.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_release", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_sha256_file() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sample.txt"
        path.write_text("release gate\n", encoding="utf-8")
        expected = "a04bf5144d04fc8129e9d3260f44ccc53997e49cf19d469d7f8cd4b8d9cc0201"
        if module.sha256_file(path) != expected:
            raise AssertionError("sha256_file returned an unexpected digest")


def test_compute_status_flags_mandatory_failures_only() -> None:
    module = load_module()
    steps = [
        module.synthetic_step("mandatory", "passed", mandatory=True, reason="ok"),
        module.synthetic_step(
            "optional",
            "skipped",
            mandatory=False,
            reason="not requested",
        ),
    ]
    if module.compute_status(steps) != "passed":
        raise AssertionError("optional explained skip should not fail the gate")

    steps.append(
        module.synthetic_step(
            "bad",
            "skipped",
            mandatory=True,
            reason="dependency failed",
        )
    )
    if module.compute_status(steps) != "failed":
        raise AssertionError("mandatory skip should fail the gate")


def test_write_manifests() -> None:
    module = load_module()
    manifest = {
        "run_id": "20260604T000000Z_test",
        "status": "passed",
        "started_at": "2026-06-04T00:00:00Z",
        "finished_at": "2026-06-04T00:00:01Z",
        "git": {"revision": "abc123", "branch": "main", "dirty": False},
        "pdf": {
            "path": "monograph/tex/main.pdf",
            "page_count": 12,
            "sha256": "pdf",
        },
        "figures": {"count": 3},
        "tool_versions": {
            "git": {"output": "git version test", "available": True},
        },
        "steps": [
            module.synthetic_step(
                "working_tree_clean",
                "passed",
                mandatory=True,
                reason="clean",
            ),
        ],
    }
    with tempfile.TemporaryDirectory() as tmp:
        json_path, md_path = module.write_manifests(manifest, Path(tmp))
        data = json.loads(json_path.read_text(encoding="utf-8"))
        if data["run_id"] != manifest["run_id"]:
            raise AssertionError("JSON manifest did not preserve the run id")
        text = md_path.read_text(encoding="utf-8")
        if (
            "Release Verification Manifest" not in text
            or "working_tree_clean" not in text
        ):
            raise AssertionError("Markdown manifest is missing expected content")


def main() -> int:
    test_sha256_file()
    test_compute_status_flags_mandatory_failures_only()
    test_write_manifests()
    print("verify_release tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
