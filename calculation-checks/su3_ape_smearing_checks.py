#!/usr/bin/env python3
"""Checks for qft_scripts/su3_ape_smearing_hdf5.py."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SAMPLER = ROOT / "qft_scripts" / "su3_gauge_4d_metropolis_hdf5.py"
SMEARING = ROOT / "qft_scripts" / "su3_ape_smearing_hdf5.py"


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


def check_cold_configuration_fixed_point(smearing) -> None:
    result = smearing.run(smearing.SmearingConfig(L=2, alpha=0.5, steps=3, seed=1, start="cold"))
    assert_close("cold initial plaquette", result.initial_plaquette, 1.0, tol=1.0e-12)
    assert_close("cold final plaquette", result.final_plaquette, 1.0, tol=1.0e-12)
    require(result.max_unitarity_error < 1.0e-12, "cold smeared links are not unitary")
    require(result.max_det_error < 1.0e-12, "cold smeared links do not have determinant one")


def check_spatial_mode_leaves_temporal_links(su3, smearing) -> None:
    rng = np.random.default_rng(20260527)
    links = su3.hot_links(2, rng)
    smeared = smearing.ape_smear_once(links, alpha=0.4, mode="spatial")
    require(np.linalg.norm(smeared[:, :, :, :, 0] - links[:, :, :, :, 0]) < 1.0e-12, "spatial smearing changed temporal links")
    require(np.linalg.norm(smeared[:, :, :, :, 1:] - links[:, :, :, :, 1:]) > 1.0e-6, "spatial links were not changed")


def check_gauge_covariance(su3, smearing) -> None:
    rng = np.random.default_rng(314159)
    links = su3.hot_links(2, rng)
    gauges = np.empty((2, 2, 2, 2, 3, 3), dtype=np.complex128)
    for site in np.ndindex((2, 2, 2, 2)):
        gauges[site] = su3.random_su3(rng)
    transformed = su3.gauge_transform(links, gauges)
    smeared_then_transformed = su3.gauge_transform(
        smearing.ape_smear_once(links, alpha=0.35, mode="all"),
        gauges,
    )
    transformed_then_smeared = smearing.ape_smear_once(transformed, alpha=0.35, mode="all")
    require(
        np.linalg.norm(smeared_then_transformed - transformed_then_smeared) < 1.0e-10,
        "APE smearing failed gauge covariance check",
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
    raise AssertionError("SU(3) APE-smearing HDF5 check requires h5py; set QFT_HDF5_PYTHON")


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
smearing = root / "qft_scripts" / "su3_ape_smearing_hdf5.py"
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    sampler_h5 = tmp_path / "su3_sampler.h5"
    smear_h5 = tmp_path / "su3_smeared.h5"
    resmear_h5 = tmp_path / "su3_resmeared.h5"
    subprocess.run([
        sys.executable, str(sampler),
        "--L", "2",
        "--beta", "5.4",
        "--proposal-width", "0.35",
        "--sweeps", "4",
        "--therm", "1",
        "--measure-every", "1",
        "--seed", "24680",
        "--max-r", "1",
        "--max-t", "1",
        "--start", "cold",
        "--output-hdf5", str(sampler_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    subprocess.run([
        sys.executable, str(smearing),
        "--L", "2",
        "--alpha", "0.45",
        "--steps", "2",
        "--mode", "spatial",
        "--input-hdf5", str(sampler_h5),
        "--output-hdf5", str(smear_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(smear_h5, "r") as handle:
        assert handle.attrs["input_dataset"] == "checkpoint/links"
        assert handle.attrs["mode"] == "spatial"
        assert tuple(handle["checkpoint/smeared_links"].shape) == (2, 2, 2, 2, 4, 3, 3)
        assert tuple(handle["smearing/plaquette_trajectory"].shape) == (3,)
    subprocess.run([
        sys.executable, str(smearing),
        "--L", "2",
        "--alpha", "0.2",
        "--steps", "1",
        "--input-hdf5", str(smear_h5),
        "--output-hdf5", str(resmear_h5),
    ], check=True, stdout=subprocess.PIPE, text=True)
    with h5py.File(resmear_h5, "r") as handle:
        assert handle.attrs["input_dataset"] == "checkpoint/smeared_links"
"""
    subprocess.run([str(python), "-c", code], check=True)


def main() -> None:
    su3 = load_module("su3_gauge_4d_metropolis_hdf5", SAMPLER)
    smearing = load_module("su3_ape_smearing_hdf5", SMEARING)
    check_cold_configuration_fixed_point(smearing)
    check_spatial_mode_leaves_temporal_links(su3, smearing)
    check_gauge_covariance(su3, smearing)
    check_hdf5_pipeline()
    print("All SU(3) APE-smearing HDF5 checks passed.")


if __name__ == "__main__":
    main()
