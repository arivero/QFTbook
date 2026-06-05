#!/usr/bin/env python3
"""Run the local release-candidate verification gate.

This command is intentionally local.  It aggregates the repository audits,
calculation checks, monograph build, PDF integrity check, and selected optional
expensive passes into one revision-stamped JSON and Markdown manifest.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
import platform
import shlex
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = ROOT / "monograph" / "tex" / "build" / "release_verification"
PDF_PATH = ROOT / "monograph" / "tex" / "main.pdf"
AUX_PATH = ROOT / "monograph" / "tex" / "main.aux"


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def display_path(path: Path) -> str:
    return str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_capture(command: list[str]) -> dict[str, Any]:
    try:
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    except FileNotFoundError as exc:
        return {
            "command": command,
            "available": False,
            "exit_code": None,
            "output": "",
            "error": str(exc),
        }
    output = "\n".join(
        line for line in (proc.stdout + proc.stderr).strip().splitlines() if line
    )
    return {
        "command": command,
        "available": proc.returncode == 0,
        "exit_code": proc.returncode,
        "output": output,
    }


def first_line(data: dict[str, Any]) -> str | None:
    output = data.get("output")
    if not isinstance(output, str) or not output:
        return None
    return output.splitlines()[0]


def tool_versions() -> dict[str, Any]:
    commands = {
        "git": ["git", "--version"],
        "bash": ["bash", "--version"],
        "python3": ["python3", "--version"],
        "rg": ["rg", "--version"],
        "latexmk": ["latexmk", "-v"],
        "xelatex": ["xelatex", "--version"],
        "qpdf": ["qpdf", "--version"],
        "pdftoppm": ["pdftoppm", "-v"],
    }
    return {name: run_capture(command) for name, command in commands.items()}


def selected_verification_python() -> dict[str, Any]:
    probe = run_capture(
        [
            "bash",
            "-lc",
            'source tools/qft_python_env.sh; qft_resolve_python "$PWD"',
        ]
    )
    executable = (
        probe.get("output", "").splitlines()[0] if probe.get("available") else ""
    )
    data: dict[str, Any] = {
        "resolver": probe,
        "executable": executable or None,
        "version": None,
    }
    if executable:
        version = run_capture([executable, "--version"])
        data["version"] = first_line(version)
    return data


def git_text(*args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def git_metadata() -> dict[str, Any]:
    status = git_text("status", "--porcelain=v1")
    return {
        "revision": git_text("rev-parse", "HEAD") or None,
        "short_revision": git_text("rev-parse", "--short", "HEAD") or "nogit",
        "branch": git_text("rev-parse", "--abbrev-ref", "HEAD") or None,
        "dirty": bool(status),
        "status_porcelain": status.splitlines() if status else [],
        "staged_paths": git_text("diff", "--cached", "--name-only").splitlines(),
        "unstaged_paths": git_text("diff", "--name-only").splitlines(),
    }


def synthetic_step(
    name: str,
    status: str,
    *,
    mandatory: bool,
    reason: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    now = utc_now()
    return {
        "name": name,
        "status": status,
        "mandatory": mandatory,
        "command": None,
        "started_at": now,
        "finished_at": now,
        "duration_seconds": 0.0,
        "exit_code": None,
        "log": None,
        "reason": reason,
        "details": details or {},
    }


def run_command_step(
    name: str,
    command: list[str],
    out_dir: Path,
    *,
    mandatory: bool,
    env: dict[str, str] | None = None,
) -> dict[str, Any]:
    log_dir = out_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{name}.log"
    started_at = utc_now()
    start = time.monotonic()
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"$ {shlex.join(command)}\n\n")
        try:
            proc = subprocess.run(
                command,
                cwd=ROOT,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                env=env,
            )
            exit_code = proc.returncode
        except FileNotFoundError as exc:
            log.write(f"\nFAILED: {exc}\n")
            exit_code = 127
    finished_at = utc_now()
    return {
        "name": name,
        "status": "passed" if exit_code == 0 else "failed",
        "mandatory": mandatory,
        "command": command,
        "started_at": started_at,
        "finished_at": finished_at,
        "duration_seconds": round(time.monotonic() - start, 3),
        "exit_code": exit_code,
        "log": display_path(log_path),
        "reason": None,
        "details": {},
    }


def pdf_metadata() -> dict[str, Any]:
    data: dict[str, Any] = {
        "path": display_path(PDF_PATH),
        "exists": PDF_PATH.exists(),
        "size_bytes": None,
        "sha256": None,
        "page_count": None,
        "page_count_error": None,
    }
    if not PDF_PATH.exists():
        return data
    data["size_bytes"] = PDF_PATH.stat().st_size
    data["sha256"] = sha256_file(PDF_PATH)
    page_count = run_capture(["qpdf", "--show-npages", str(PDF_PATH)])
    if page_count.get("available"):
        try:
            data["page_count"] = int(str(page_count["output"]).splitlines()[0])
        except (ValueError, IndexError):
            data["page_count_error"] = page_count
    else:
        data["page_count_error"] = page_count
    return data


def figure_metadata() -> dict[str, Any]:
    data: dict[str, Any] = {
        "aux_path": display_path(AUX_PATH),
        "aux_exists": AUX_PATH.exists(),
        "count": None,
        "unique_anchors": None,
        "error": None,
    }
    if not AUX_PATH.exists():
        return data
    spec = importlib.util.spec_from_file_location(
        "render_figure_pages", ROOT / "tools" / "render_figure_pages.py"
    )
    if spec is None or spec.loader is None:
        data["error"] = "cannot load tools/render_figure_pages.py"
        return data
    module = importlib.util.module_from_spec(spec)
    try:
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        figures = module.parse_aux_figures(AUX_PATH)
    except SystemExit as exc:  # pragma: no cover - defensive manifest path
        data["error"] = str(exc)
        return data
    except Exception as exc:  # pragma: no cover - defensive manifest path
        data["error"] = str(exc)
        return data
    data["count"] = len(figures)
    data["unique_anchors"] = len({figure.anchor for figure in figures})
    return data


def release_steps(args: argparse.Namespace) -> list[tuple[str, list[str], bool]]:
    steps: list[tuple[str, list[str], bool]] = [
        ("git_diff_check", ["git", "diff", "--check"], True),
        ("git_cached_diff_check", ["git", "diff", "--cached", "--check"], True),
        ("chapter_dossier_audit", ["tools/audit_chapter_dossiers.sh"], True),
        ("strict_figure_structure_audit", ["tools/audit_figures.py", "--strict"], True),
        (
            "calculation_evidence_contract_audit",
            ["python3", "tools/audit_calculation_evidence_contracts.py"],
            True,
        ),
        (
            "calculation_check_inventory_audit",
            ["python3", "tools/audit_calculation_check_inventory.py"],
            True,
        ),
        ("calculation_checks", ["tools/run_calculation_checks.sh"], True),
        ("monograph_build", ["tools/build_monograph.sh"], True),
        ("pdf_integrity", ["qpdf", "--check", str(PDF_PATH)], True),
    ]
    if args.rendered_figures:
        steps.extend(
            [
                (
                    "rendered_figure_pages",
                    [
                        "tools/render_figure_pages.py",
                        "--force",
                        "--dpi",
                        str(args.rendered_figure_dpi),
                    ],
                    False,
                ),
                (
                    "rendered_figure_page_audit",
                    ["tools/audit_rendered_figure_pages.py"],
                    False,
                ),
            ]
        )
    if args.qft_scripts_smoke:
        steps.append(("qft_scripts_smoke", ["tools/run_qft_scripts_smoke.sh"], False))
    return steps


def compute_status(steps: list[dict[str, Any]]) -> str:
    unexplained_skip = [
        step for step in steps if step["status"] == "skipped" and not step.get("reason")
    ]
    mandatory_bad = [
        step
        for step in steps
        if step["mandatory"] and step["status"] not in {"passed", "warning"}
    ]
    selected_optional_bad = [
        step
        for step in steps
        if not step["mandatory"] and step["status"] == "failed"
    ]
    if unexplained_skip or mandatory_bad or selected_optional_bad:
        return "failed"
    if any(step["status"] == "warning" for step in steps):
        return "passed_with_warnings"
    return "passed"


def write_markdown_manifest(manifest: dict[str, Any], path: Path) -> None:
    git = manifest["git"]
    pdf = manifest["pdf"]
    figures = manifest["figures"]
    lines = [
        "# Release Verification Manifest",
        "",
        f"- Status: `{manifest['status']}`",
        f"- Run ID: `{manifest['run_id']}`",
        f"- Started: `{manifest['started_at']}`",
        f"- Finished: `{manifest['finished_at']}`",
        f"- Revision: `{git.get('revision')}`",
        f"- Branch: `{git.get('branch')}`",
        f"- Dirty: `{git.get('dirty')}`",
        f"- PDF: `{pdf.get('path')}`",
        f"- PDF pages: `{pdf.get('page_count')}`",
        f"- PDF sha256: `{pdf.get('sha256')}`",
        f"- Figure count: `{figures.get('count')}`",
        "",
        "## Steps",
        "",
        "| Status | Mandatory | Step | Seconds | Log |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for step in manifest["steps"]:
        log = step.get("log") or ""
        lines.append(
            f"| `{step['status']}` | `{step['mandatory']}` | "
            f"`{step['name']}` | {step['duration_seconds']} | `{log}` |"
        )
        if step.get("reason"):
            lines.append(f"| | | reason: {step['reason']} | | |")
    lines.extend(
        [
            "",
            "## Tool Versions",
            "",
        ]
    )
    for name, data in manifest["tool_versions"].items():
        version = first_line(data) or data.get("error") or "unavailable"
        lines.append(f"- `{name}`: {version}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifests(manifest: dict[str, Any], out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    base = out_dir / f"release_verification_{manifest['run_id']}"
    json_path = base.with_suffix(".json")
    md_path = base.with_suffix(".md")
    json_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    write_markdown_manifest(manifest, md_path)
    return json_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="record but do not fail a dirty working tree; not for release-candidate signoff",
    )
    parser.add_argument(
        "--rendered-figures",
        action="store_true",
        help="run the expensive rendered figure-page audit with --force",
    )
    parser.add_argument(
        "--rendered-figure-dpi",
        type=int,
        default=120,
        help="DPI passed to tools/render_figure_pages.py when --rendered-figures is set",
    )
    parser.add_argument(
        "--qft-scripts-smoke",
        action="store_true",
        help="run the public qft_scripts smoke suite",
    )
    args = parser.parse_args()

    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    started_at = utc_now()
    git = git_metadata()
    run_id = f"{started_at.replace(':', '').replace('-', '')}_{git['short_revision']}"
    steps: list[dict[str, Any]] = []

    if git["dirty"] and not args.allow_dirty:
        steps.append(
            synthetic_step(
                "working_tree_clean",
                "failed",
                mandatory=True,
                reason="working tree has uncommitted or untracked changes",
                details={"status_porcelain": git["status_porcelain"]},
            )
        )
    elif git["dirty"]:
        steps.append(
            synthetic_step(
                "working_tree_clean",
                "warning",
                mandatory=True,
                reason="dirty working tree allowed by --allow-dirty",
                details={"status_porcelain": git["status_porcelain"]},
            )
        )
    else:
        steps.append(
            synthetic_step(
                "working_tree_clean",
                "passed",
                mandatory=True,
                reason="working tree clean",
            )
        )

    run_commands = not (git["dirty"] and not args.allow_dirty)
    for name, command, mandatory in release_steps(args):
        if run_commands:
            steps.append(run_command_step(name, command, out_dir, mandatory=mandatory))
        else:
            steps.append(
                synthetic_step(
                    name,
                    "skipped",
                    mandatory=mandatory,
                    reason="working tree dirty; clean tree required before release commands",
                    details={"command": command},
                )
            )

    if not args.rendered_figures:
        steps.append(
            synthetic_step(
                "rendered_figure_pages",
                "skipped",
                mandatory=False,
                reason="optional expensive pass not requested; pass --rendered-figures",
            )
        )
    if not args.qft_scripts_smoke:
        steps.append(
            synthetic_step(
                "qft_scripts_smoke",
                "skipped",
                mandatory=False,
                reason="optional numerical smoke pass not requested; pass --qft-scripts-smoke",
            )
        )

    finished_at = utc_now()
    manifest: dict[str, Any] = {
        "schema": 1,
        "run_id": run_id,
        "status": compute_status(steps),
        "started_at": started_at,
        "finished_at": finished_at,
        "repository_root": str(ROOT),
        "local_only": True,
        "allow_dirty": args.allow_dirty,
        "optional_passes": {
            "rendered_figures": args.rendered_figures,
            "rendered_figure_dpi": args.rendered_figure_dpi,
            "qft_scripts_smoke": args.qft_scripts_smoke,
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "environment": {
            "runner_python": sys.executable,
            "runner_python_version": sys.version,
            "QFT_PYTHON": os.environ.get("QFT_PYTHON"),
            "QFT_SKIP_WOLFRAM": os.environ.get("QFT_SKIP_WOLFRAM"),
            "WOLFRAMKERNEL": os.environ.get("WOLFRAMKERNEL"),
            "WOLFRAMSCRIPT": os.environ.get("WOLFRAMSCRIPT"),
        },
        "verification_python": selected_verification_python(),
        "tool_versions": tool_versions(),
        "git": git,
        "pdf": pdf_metadata(),
        "figures": figure_metadata(),
        "steps": steps,
    }
    json_path, md_path = write_manifests(manifest, out_dir)

    print("Release verification manifest written")
    print(f"  status: {manifest['status']}")
    print(f"  json: {display_path(json_path)}")
    print(f"  markdown: {display_path(md_path)}")
    print(f"  revision: {git.get('revision')}")
    print(f"  dirty: {git.get('dirty')}")
    print(f"  PDF pages: {manifest['pdf'].get('page_count')}")
    print(f"  figures: {manifest['figures'].get('count')}")
    return 0 if manifest["status"] in {"passed", "passed_with_warnings"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
