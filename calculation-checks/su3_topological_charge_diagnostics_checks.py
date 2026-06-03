#!/usr/bin/env python3
"""Checks for qft_scripts/su3_topological_charge_diagnostics_hdf5.py."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

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
TOPOLOGY = ROOT / "qft_scripts" / "su3_topological_charge_diagnostics_hdf5.py"


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
    _assert_close(name, got, expected, tol=tol)


def check_oriented_plaquette_conventions(su3, topology) -> None:
    rng = np.random.default_rng(20260527)
    links = su3.hot_links(2, rng)
    site = (1, 0, 1, 0)
    for mu in range(su3.DIRECTIONS):
        for nu in range(mu + 1, su3.DIRECTIONS):
            direct = su3.plaquette(links, site, mu, nu)
            oriented = topology.oriented_plaquette(links, site, mu, nu)
            assert_close(
                "positive oriented plaquette",
                float(np.linalg.norm(direct - oriented)),
                0.0,
                tol=1.0e-12,
            )
            reverse = topology.oriented_plaquette(links, site, nu, mu)
            assert_close(
                "opposite plaquette orientation",
                float(np.linalg.norm(reverse - su3.dagger(direct))),
                0.0,
                tol=1.0e-12,
            )


def check_cold_configuration_zero(su3, topology) -> None:
    cfg = topology.TopologyConfig(L=2, seed=1, start="cold")
    result = topology.run(cfg)
    assert_close("cold clover charge", result.q_clover, 0.0, tol=1.0e-12)
    assert_close("cold clover action density", result.clover_action_density, 0.0, tol=1.0e-12)
    assert_close("cold plaquette deviation", result.max_plaquette_deviation, 0.0, tol=1.0e-12)
    require(result.max_clover_antihermitian_error < 1.0e-12, "cold clover field is not anti-Hermitian")
    require(result.max_clover_trace_abs < 1.0e-12, "cold clover field is not traceless")


def check_clover_field_quality_and_antisymmetry(su3, topology) -> None:
    rng = np.random.default_rng(314159)
    links = su3.hot_links(2, rng)
    site = (0, 1, 0, 1)
    for mu in range(su3.DIRECTIONS):
        for nu in range(mu + 1, su3.DIRECTIONS):
            field = topology.clover_field_strength(links, site, mu, nu)
            flipped = topology.clover_field_strength(links, site, nu, mu)
            require(np.linalg.norm(su3.dagger(field) + field) < 1.0e-12, "clover field is not anti-Hermitian")
            require(abs(np.trace(field)) < 1.0e-12, "clover field is not traceless")
            assert_close(
                "clover antisymmetry",
                float(np.linalg.norm(field + flipped)),
                0.0,
                tol=1.0e-12,
            )


def check_gauge_invariance(su3, topology) -> None:
    rng = np.random.default_rng(271828)
    links = su3.hot_links(2, rng)
    gauges = np.empty((2, 2, 2, 2, 3, 3), dtype=np.complex128)
    for site in np.ndindex((2, 2, 2, 2)):
        gauges[site] = su3.random_su3(rng)
    transformed = su3.gauge_transform(links, gauges)
    q_density, action_density = topology.diagnostic_arrays(links)
    q_density_g, action_density_g = topology.diagnostic_arrays(transformed)
    assert_close("clover topological charge gauge invariance", float(np.sum(q_density)), float(np.sum(q_density_g)), tol=1.0e-10)
    assert_close("clover action-density gauge invariance", float(np.mean(action_density)), float(np.mean(action_density_g)), tol=1.0e-10)
    assert_close(
        "plaquette admissibility diagnostic gauge invariance",
        topology.max_plaquette_deviation(links),
        topology.max_plaquette_deviation(transformed),
        tol=1.0e-10,
    )


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
    raise AssertionError("SU(3) topology HDF5 check requires h5py; set QFT_HDF5_PYTHON")


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
topology = root / "qft_scripts" / "su3_topological_charge_diagnostics_hdf5.py"
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    sampler_h5 = tmp_path / "su3_sampler.h5"
    flow_h5 = tmp_path / "su3_flow.h5"
    topology_h5 = tmp_path / "su3_topology.h5"
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
        "--output-hdf5", str(sampler_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    subprocess.run([
        sys.executable, str(flow),
        "--L", "2",
        "--steps", "4",
        "--step-size", "0.0125",
        "--measure-every", "1",
        "--input-hdf5", str(sampler_h5),
        "--output-hdf5", str(flow_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    subprocess.run([
        sys.executable, str(topology),
        "--L", "2",
        "--input-hdf5", str(flow_h5),
        "--output-hdf5", str(topology_h5),
        "--write-density",
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(topology_h5, "r") as handle:
        assert handle.attrs["input_dataset"] == "checkpoint/flowed_links"
        assert "q_clover" in handle.attrs
        assert "clover_action_density" in handle.attrs
        assert handle["diagnostics/q_density"].shape == (2, 2, 2, 2)
        assert handle["diagnostics/clover_action_density"].shape == (2, 2, 2, 2)
        assert handle["diagnostics"].attrs["write_density"]
    raw_topology_h5 = tmp_path / "su3_topology_raw.h5"
    subprocess.run([
        sys.executable, str(topology),
        "--L", "2",
        "--input-hdf5", str(sampler_h5),
        "--output-hdf5", str(raw_topology_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(raw_topology_h5, "r") as handle:
        assert handle.attrs["input_dataset"] == "checkpoint/links"
        assert "diagnostics/q_density" not in handle
"""
    subprocess.run([str(python), "-c", code], check=True)


def main() -> None:
    su3 = load_module("su3_gauge_4d_metropolis_hdf5", SAMPLER)
    load_module("su3_wilson_flow_hdf5", FLOW)
    topology = load_module("su3_topological_charge_diagnostics_hdf5", TOPOLOGY)
    check_oriented_plaquette_conventions(su3, topology)
    check_cold_configuration_zero(su3, topology)
    check_clover_field_quality_and_antisymmetry(su3, topology)
    check_gauge_invariance(su3, topology)
    check_hdf5_pipeline()
    print("All SU(3) topological-diagnostic HDF5 checks passed.")


if __name__ == "__main__":
    main()
