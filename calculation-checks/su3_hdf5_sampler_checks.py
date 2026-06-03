#!/usr/bin/env python3
"""Checks for qft_scripts/su3_gauge_4d_metropolis_hdf5.py."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "su3_gauge_4d_metropolis_hdf5.py"


def load_module():
    spec = importlib.util.spec_from_file_location("su3_gauge_4d_metropolis_hdf5", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load su3_gauge_4d_metropolis_hdf5.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def transformed_link(module, links: np.ndarray, site: tuple[int, int, int, int], mu: int, proposal: np.ndarray) -> np.ndarray:
    result = links.copy()
    module.left_multiply_link_in_place(result, site, mu, proposal)
    return result


def check_embedded_su2_proposals(module) -> None:
    rng = np.random.default_rng(20260527)
    identity = np.eye(3, dtype=np.complex128)
    for pair in module.COLOR_PAIRS:
        proposal, chosen_pair = module.random_small_su3_subgroup(rng, 0.4, pair=pair)
        require(chosen_pair == pair, "proposal pair bookkeeping failed")
        assert_close("embedded SU(2) unitarity", float(np.linalg.norm(module.dagger(proposal) @ proposal - identity)), 0.0)
        assert_close("embedded SU(2) determinant", abs(np.linalg.det(proposal) - 1.0), 0.0)


def check_local_score_change(module) -> None:
    rng = np.random.default_rng(314159)
    links = module.hot_links(2, rng)
    for _ in range(12):
        site = (
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
        )
        mu = int(rng.integers(module.DIRECTIONS))
        proposal, _ = module.random_small_su3_subgroup(rng, 0.35)
        direct = module.total_plaquette_score(transformed_link(module, links, site, mu, proposal)) - module.total_plaquette_score(links)
        local = module.local_score_change_for_left_multiply(links, site, mu, proposal)
        assert_close("local SU(3) score change", local, direct, tol=1.0e-9)
        links = transformed_link(module, links, site, mu, proposal)


def check_gauge_invariance(module) -> None:
    rng = np.random.default_rng(161803)
    links = module.hot_links(2, rng)
    gauges = np.empty((2, 2, 2, 2, 3, 3), dtype=np.complex128)
    for site in np.ndindex((2, 2, 2, 2)):
        gauges[site] = module.random_su3(rng)
    transformed = module.gauge_transform(links, gauges)
    assert_close("SU(3) plaquette score gauge invariance", module.total_plaquette_score(links), module.total_plaquette_score(transformed), tol=1.0e-9)
    assert_close(
        "SU(3) Wilson loop gauge invariance",
        module.wilson_loop_rectangle(links, 1, 1),
        module.wilson_loop_rectangle(transformed, 1, 1),
        tol=1.0e-9,
    )


def check_one_plaquette_loop_identity(module) -> None:
    rng = np.random.default_rng(271828)
    links = module.hot_links(2, rng)
    plaquette_mean = module.total_plaquette_score(links) / float(6 * 2**4)
    loop_mean = module.wilson_loop_rectangle(links, 1, 1)
    assert_close("SU(3) 1x1 Wilson loop equals plaquette mean", loop_mean, plaquette_mean, tol=1.0e-10)


def python_has_h5py(python: Path) -> bool:
    result = subprocess.run(
        [str(python), "-c", "import h5py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return result.returncode == 0


def find_hdf5_python() -> Path:
    candidates: list[Path] = []
    if os.environ.get("QFT_HDF5_PYTHON"):
        candidates.append(Path(os.environ["QFT_HDF5_PYTHON"]))
    candidates.append(Path(sys.executable))
    candidates.append(
        Path.home()
        / ".cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
    )
    for candidate in candidates:
        if candidate.exists() and python_has_h5py(candidate):
            return candidate
    raise AssertionError("HDF5 sampler check requires a Python with h5py; set QFT_HDF5_PYTHON")


def check_hdf5_output() -> None:
    python = find_hdf5_python()
    code = f"""
import h5py
import json
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path({str(ROOT)!r})
script = root / "qft_scripts" / "su3_gauge_4d_metropolis_hdf5.py"
with tempfile.TemporaryDirectory() as tmp:
    h5_path = Path(tmp) / "su3.h5"
    csv_path = Path(tmp) / "su3_samples.csv"
    subprocess.run([
        sys.executable, str(script),
        "--L", "2",
        "--beta", "5.4",
        "--proposal-width", "0.35",
        "--sweeps", "5",
        "--therm", "1",
        "--measure-every", "1",
        "--seed", "8675309",
        "--max-r", "1",
        "--max-t", "1",
        "--start", "cold",
        "--output-hdf5", str(h5_path),
        "--samples-csv", str(csv_path),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(h5_path, "r") as handle:
        assert handle["measurements/wilson_loops"].shape == (4, 1, 1)
        assert handle["checkpoint/links"].shape == (2, 2, 2, 2, 4, 3, 3)
        assert handle.attrs["L"] == 2
        assert 0.0 <= handle.attrs["acceptance"] <= 1.0
        assert "rng_state_json" in handle["checkpoint"].attrs
        json.loads(handle["checkpoint"].attrs["rng_state_json"])
    rows = csv_path.read_text().strip().splitlines()
    assert rows[0] == "sample,R,T,W"
    assert len(rows) == 5
    resumed_path = Path(tmp) / "su3_resumed.h5"
    subprocess.run([
        sys.executable, str(script),
        "--L", "2",
        "--beta", "5.4",
        "--proposal-width", "0.35",
        "--sweeps", "3",
        "--therm", "0",
        "--measure-every", "1",
        "--seed", "123",
        "--max-r", "1",
        "--max-t", "1",
        "--resume-from", str(h5_path),
        "--output-hdf5", str(resumed_path),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(resumed_path, "r") as handle:
        assert handle["measurements/wilson_loops"].shape == (3, 1, 1)
        assert handle.attrs["resume_from"] == str(h5_path)
        assert "rng_state_json" in handle["checkpoint"].attrs
"""
    subprocess.run([str(python), "-c", code], check=True)


def main() -> None:
    module = load_module()
    check_embedded_su2_proposals(module)
    check_local_score_change(module)
    check_gauge_invariance(module)
    check_one_plaquette_loop_identity(module)
    check_hdf5_output()
    print("All SU(3) HDF5 sampler checks passed.")


if __name__ == "__main__":
    main()
