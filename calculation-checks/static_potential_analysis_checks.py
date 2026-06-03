#!/usr/bin/env python3
"""Checks for the static-potential Wilson-loop analysis script."""

from __future__ import annotations

import importlib.util
import csv
import math
import os
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "static_potential_from_wilson_loops.py"


def load_module():
    spec = importlib.util.spec_from_file_location("static_potential_from_wilson_loops", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load static-potential analysis script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


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
    raise AssertionError("static-potential HDF5 check requires h5py; set QFT_HDF5_PYTHON")


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def mat_mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def transpose(a: Matrix2) -> Matrix2:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def inv2(a: Matrix2) -> Matrix2:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if det == 0:
        raise AssertionError("singular matrix in static-source GEVP check")
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def diag(d1: Fraction, d2: Fraction) -> Matrix2:
    return ((d1, Fraction(0)), (Fraction(0), d2))


def corr_matrix(z: Matrix2, r1: Fraction, r2: Fraction, t: int) -> Matrix2:
    return mat_mul(mat_mul(z, diag(r1**t, r2**t)), transpose(z))


def check_static_source_gevp_matrix_mode(module) -> None:
    z: Matrix2 = ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(5)))
    r1 = Fraction(1, 3)
    r2 = Fraction(1, 8)
    t0 = 1
    t = 4
    gevp_matrix = mat_mul(inv2(corr_matrix(z, r1, r2, t0)), corr_matrix(z, r1, r2, t))
    trace = gevp_matrix[0][0] + gevp_matrix[1][1]
    determinant = gevp_matrix[0][0] * gevp_matrix[1][1] - gevp_matrix[0][1] * gevp_matrix[1][0]
    require(trace == r1 ** (t - t0) + r2 ** (t - t0), "static GEVP trace invariant failed")
    require(determinant == (r1 * r2) ** (t - t0), "static GEVP determinant invariant failed")

    matrices = {
        3: {
            time: np.array(
                [[float(entry) for entry in row] for row in corr_matrix(z, r1, r2, time)],
                dtype=np.complex128,
            )
            for time in [1, 2, 4]
        }
    }
    results = module.static_gevp_from_matrices(matrices, selected_r=3, t0=1, times=[2, 4], lattice_spacing=1.0)
    expected = [-math.log(float(r1)), -math.log(float(r2))]
    for level, energy in enumerate(expected):
        got = [datum.value for datum in results if datum.level == level]
        require(len(got) == 2, "static GEVP matrix mode should return both analysis times")
        for value in got:
            require(abs(value - energy) < 1.0e-12, "static GEVP matrix-mode energy failed")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        matrix_path = tmp_path / "static_matrix.csv"
        out_path = tmp_path / "static_gevp.csv"
        with matrix_path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["R", "T", "i", "j", "C"])
            writer.writeheader()
            for time, matrix in matrices[3].items():
                for i in range(2):
                    for j in range(2):
                        writer.writerow({"R": 3, "T": time, "i": i + 1, "j": j + 1, "C": f"{matrix[i, j].real:.17g}"})
        subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--matrix-input",
                str(matrix_path),
                "--matrix-r",
                "3",
                "--t0",
                "1",
                "--times",
                "2,4",
                "--one-based",
                "--output",
                str(out_path),
            ],
            check=True,
        )
        with out_path.open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        require(len(rows) == 4, "static GEVP CSV mode should write two levels at two times")
        require({row["observable"] for row in rows} == {"static_gevp_energy"}, "static GEVP CSV observable label failed")
        require(any(row["level"] == "0" and abs(float(row["value"]) - expected[0]) < 1.0e-12 for row in rows), "static GEVP CSV ground energy failed")


def check_hdf5_static_potential_bridge() -> None:
    python = find_hdf5_python()
    code = f"""
import csv
import h5py
import importlib.util
import math
import numpy as np
import subprocess
import sys
import tempfile
from pathlib import Path

script = Path({str(SCRIPT)!r})
spec = importlib.util.spec_from_file_location("static_potential_from_wilson_loops", script)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    h5_path = tmp_path / "wilson_loop_samples.h5"
    out_path = tmp_path / "static_observables.csv"
    sigmas = [0.21, 0.25, 0.28, 0.34]
    mu = 0.17
    constant = 0.04
    grid = np.empty((len(sigmas), 3, 4), dtype=float)
    for sample, sigma in enumerate(sigmas):
        for r in range(1, 4):
            for t in range(1, 5):
                grid[sample, r - 1, t - 1] = math.exp(-(sigma * r * t + mu * (r + t) + constant))
    with h5py.File(h5_path, "w") as handle:
        measurements = handle.create_group("measurements")
        measurements.create_dataset("wilson_loops", data=grid)
        measurements["wilson_loops"].attrs["index_convention"] = "wilson_loops[sample, R-1, T-1]"

    data = module.read_wilson_loop_sample_hdf5(h5_path)
    assert len(data) == len(sigmas) * 3 * 4
    indexed = module.index_sample_data(data)
    central = module.observables_from_sample_ids(indexed, sorted(indexed), 1.0, True, True)
    key = ("effective_mass", 2, 1)
    expected = (sum(sigmas) / len(sigmas)) * 2 + mu
    assert abs(central[key] - expected) < 0.02

    subprocess.run([
        sys.executable,
        str(script),
        "--samples-hdf5",
        str(h5_path),
        "--output",
        str(out_path),
        "--block-size",
        "1",
        "--bootstrap-samples",
        "8",
        "--seed",
        "31",
    ], check=True)
    with out_path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert any(row["observable"] == "effective_mass" for row in rows)
    assert any(row["observable"] == "creutz_ratio" for row in rows)
    assert any(float(row["jackknife_error"]) > 0.0 for row in rows if row["jackknife_error"])
"""
    subprocess.run([str(python), "-c", code], check=True)


def main() -> None:
    module = load_module()
    sigma = 0.41
    mu = 0.23
    constant = 0.07
    data = module.synthetic_area_perimeter_data(sigma, mu, constant, max_r=5, max_t=6)
    eff = module.effective_masses(data, lattice_spacing=1.0)
    creutz = module.creutz_ratios(data)
    require(len(eff) > 0, "effective-mass output should be nonempty")
    require(len(creutz) > 0, "Creutz-ratio output should be nonempty")
    for datum in eff:
        require(abs(datum.value - (sigma * datum.r + mu)) < 1e-12, "effective mass should recover sigma R + mu")
    for datum in creutz:
        require(abs(datum.value - sigma) < 1e-12, "Creutz ratio should recover sigma")

    noisy_error_data = [
        module.WilsonLoopDatum(1, 1, math.exp(-0.3), 0.01),
        module.WilsonLoopDatum(1, 2, math.exp(-0.6), 0.02),
    ]
    one_eff = module.effective_masses(noisy_error_data, lattice_spacing=2.0)[0]
    expected_error = 0.5 * math.sqrt((0.02 / math.exp(-0.6)) ** 2 + (0.01 / math.exp(-0.3)) ** 2)
    require(abs(one_eff.error - expected_error) < 1e-14, "effective-mass error propagation failed")

    sigmas = [0.25, 0.34, 0.39, 0.52]
    sample_data = module.synthetic_area_perimeter_sample_data(sigmas, mu=0.17, constant=0.03, max_r=3, max_t=4)
    resampled = module.resampled_static_observables(
        sample_data,
        lattice_spacing=1.0,
        block_size=1,
        bootstrap_samples=12,
        seed=19,
    )
    resampled_map = {
        (datum.observable, datum.r, datum.t): datum
        for datum in resampled
    }
    key = ("effective_mass", 2, 1)
    datum = resampled_map[key]

    indexed = module.index_sample_data(sample_data)
    all_samples = sorted(indexed)
    central = module.observables_from_sample_ids(indexed, all_samples, 1.0, True, True)
    require(abs(datum.value - central[key]) < 1e-14, "central resampled observable failed")

    delete_values = []
    for removed in all_samples:
        kept = [sample for sample in all_samples if sample != removed]
        delete_values.append(module.observables_from_sample_ids(indexed, kept, 1.0, True, True)[key])
    theta_bar = sum(delete_values) / len(delete_values)
    expected_jackknife = math.sqrt(
        (len(delete_values) - 1) / len(delete_values)
        * sum((theta - theta_bar) ** 2 for theta in delete_values)
    )
    require(abs(datum.jackknife_error - expected_jackknife) < 1e-14, "correlated jackknife error failed")
    require(datum.bootstrap_error > 0.0, "block bootstrap error should be positive on varying samples")

    check_static_source_gevp_matrix_mode(module)
    check_hdf5_static_potential_bridge()

    print("All static-potential analysis checks passed.")


if __name__ == "__main__":
    main()
