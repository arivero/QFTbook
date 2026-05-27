#!/usr/bin/env python3
"""Checks for qft_scripts/su3_wilson_flow_hdf5.py."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SAMPLER = ROOT / "qft_scripts" / "su3_gauge_4d_metropolis_hdf5.py"
FLOW = ROOT / "qft_scripts" / "su3_wilson_flow_hdf5.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def random_su3_algebra_element(flow, rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    algebra = flow.antihermitian_traceless(matrix)
    norm = float(np.linalg.norm(algebra))
    require(norm > 0.0, "random algebra element vanished")
    return algebra / norm


def left_multiply_direction(su3, flow, links: np.ndarray, site: tuple[int, int, int, int], mu: int, direction: np.ndarray, eps: float) -> np.ndarray:
    varied = links.copy()
    varied[site + (mu,)] = flow.antihermitian_exponential(direction, eps) @ links[site + (mu,)]
    return varied


def check_score_gradient_directional_derivative(su3, flow) -> None:
    rng = np.random.default_rng(20260527)
    links = su3.hot_links(2, rng)
    eps = 1.0e-6
    for _ in range(8):
        site = (
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
        )
        mu = int(rng.integers(su3.DIRECTIONS))
        direction = random_su3_algebra_element(flow, rng)
        plus = su3.total_plaquette_score(left_multiply_direction(su3, flow, links, site, mu, direction, eps))
        minus = su3.total_plaquette_score(left_multiply_direction(su3, flow, links, site, mu, direction, -eps))
        finite_difference = (plus - minus) / (2.0 * eps)
        gradient = flow.score_gradient_generator(links, site, mu)
        inner_product = -float(np.real(np.trace(gradient @ direction)))
        assert_close("SU(3) Wilson-flow score gradient", finite_difference, inner_product, tol=2.0e-8)


def check_flow_step_gauge_covariance(su3, flow) -> None:
    rng = np.random.default_rng(314159)
    links = su3.hot_links(2, rng)
    gauges = np.empty((2, 2, 2, 2, 3, 3), dtype=np.complex128)
    for site in np.ndindex((2, 2, 2, 2)):
        gauges[site] = su3.random_su3(rng)
    transformed = su3.gauge_transform(links, gauges)
    flowed_then_transformed = su3.gauge_transform(flow.flow_step(links, 0.01), gauges)
    transformed_then_flowed = flow.flow_step(transformed, 0.01)
    error = float(np.linalg.norm(flowed_then_transformed - transformed_then_flowed))
    require(error < 5.0e-10, f"flow step is not gauge covariant: {error}")


def check_flow_monotonicity_and_group_preservation(su3, flow) -> None:
    cfg = flow.FlowConfig(L=2, steps=5, step_size=0.015, measure_every=1, seed=271828, start="hot")
    result = flow.run(cfg)
    require(result.monotone_violations == 0, "score should be nondecreasing for small flow step")
    require(result.final_plaquette >= result.initial_plaquette - 1.0e-10, "plaquette did not increase")
    require(result.final_action_density <= result.initial_action_density + 1.0e-10, "action density did not decrease")
    require(result.max_unitarity_error < 1.0e-10, "flow did not preserve unitarity")
    require(result.max_det_error < 1.0e-10, "flow did not preserve determinant one")


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
    raise AssertionError("SU(3) Wilson-flow HDF5 check requires h5py; set QFT_HDF5_PYTHON")


def check_hdf5_pipeline() -> None:
    python = find_hdf5_python()
    code = f"""
import h5py
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path({str(ROOT)!r})
sampler = root / "qft_scripts" / "su3_gauge_4d_metropolis_hdf5.py"
flow = root / "qft_scripts" / "su3_wilson_flow_hdf5.py"
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    input_h5 = tmp_path / "su3_sampler.h5"
    output_h5 = tmp_path / "su3_flow.h5"
    subprocess.run([
        sys.executable, str(sampler),
        "--L", "2",
        "--beta", "5.4",
        "--proposal-width", "0.35",
        "--sweeps", "4",
        "--therm", "1",
        "--measure-every", "1",
        "--seed", "8675309",
        "--max-r", "1",
        "--max-t", "1",
        "--start", "cold",
        "--output-hdf5", str(input_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    subprocess.run([
        sys.executable, str(flow),
        "--L", "2",
        "--steps", "4",
        "--step-size", "0.0125",
        "--measure-every", "1",
        "--input-hdf5", str(input_h5),
        "--output-hdf5", str(output_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(output_h5, "r") as handle:
        assert handle["flow/tau"].shape == (5,)
        assert handle["flow/plaquette"].shape == (5,)
        assert handle["flow/action_density"].shape == (5,)
        assert handle["checkpoint/flowed_links"].shape == (2, 2, 2, 2, 4, 3, 3)
        assert handle.attrs["input_hdf5"] == str(input_h5)
        assert handle.attrs["monotone_violations"] == 0
        plaquettes = handle["flow/plaquette"][:]
        assert (plaquettes[1:] + 1.0e-10 >= plaquettes[:-1]).all()
"""
    subprocess.run([str(python), "-c", code], check=True)


def main() -> None:
    su3 = load_module("su3_gauge_4d_metropolis_hdf5", SAMPLER)
    flow = load_module("su3_wilson_flow_hdf5", FLOW)
    check_score_gradient_directional_derivative(su3, flow)
    check_flow_step_gauge_covariance(su3, flow)
    check_flow_monotonicity_and_group_preservation(su3, flow)
    check_hdf5_pipeline()
    print("All SU(3) Wilson-flow HDF5 checks passed.")


if __name__ == "__main__":
    main()
