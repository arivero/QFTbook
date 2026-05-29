#!/usr/bin/env python3
"""Finite-regulator glueball GEVP analysis from correlator matrices.

The theorem anchor is Volume XI, Chapter 5, "Glueball Correlator Matrices and
the GEVP".  The script solves the finite generalized eigenvalue problem

    C(t) v = lambda(t,t0) C(t0) v

after Hermitian whitening by C(t0).  It is a finite matrix-analysis utility:
continuum, infinite-volume, operator-renormalization, and excited-state
systematics are inputs to the surrounding QFT analysis, not consequences of
this script.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class GevpResult:
    t: int
    t0: int
    lambdas: list[float]
    energies: list[float]


def hermitian_part(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.conjugate().T)


def positive_whitener(c0: np.ndarray, *, floor: float = 1.0e-12) -> np.ndarray:
    c0_h = hermitian_part(c0)
    evals, evecs = np.linalg.eigh(c0_h)
    min_eval = float(np.min(evals))
    if min_eval <= floor:
        raise ValueError(
            f"C(t0) is not positive definite at the requested tolerance: "
            f"min eigenvalue {min_eval:.6e}"
        )
    inv_sqrt = np.diag(evals ** -0.5)
    return evecs @ inv_sqrt @ evecs.conjugate().T


def solve_gevp(c_t: np.ndarray, c_t0: np.ndarray) -> np.ndarray:
    """Return generalized eigenvalues sorted from largest to smallest."""
    w = positive_whitener(c_t0)
    b = hermitian_part(w @ c_t @ w)
    evals = np.linalg.eigvalsh(b)
    return np.array(sorted((float(x) for x in evals), reverse=True), dtype=float)


def effective_energies(lambdas: Iterable[float], t: int, t0: int, spacing: float) -> list[float]:
    dt = spacing * (t - t0)
    if dt <= 0:
        raise ValueError("GEVP times must obey t > t0")
    out: list[float] = []
    for lam in lambdas:
        if lam <= 0.0:
            out.append(float("nan"))
        else:
            out.append(float(-math.log(lam) / dt))
    return out


def analyze_correlators(
    correlators: dict[int, np.ndarray],
    *,
    t0: int,
    times: Iterable[int] | None,
    spacing: float,
) -> list[GevpResult]:
    if t0 not in correlators:
        raise ValueError(f"t0={t0} is not present in the correlator data")
    selected = sorted(t for t in (times if times is not None else correlators) if t > t0)
    if not selected:
        raise ValueError("no analysis times with t > t0 were supplied")
    c0 = correlators[t0]
    results: list[GevpResult] = []
    for t in selected:
        if t not in correlators:
            raise ValueError(f"t={t} is not present in the correlator data")
        lambdas = solve_gevp(correlators[t], c0)
        energies = effective_energies(lambdas, t, t0, spacing)
        results.append(
            GevpResult(
                t=t,
                t0=t0,
                lambdas=[float(x) for x in lambdas],
                energies=energies,
            )
        )
    return results


def parse_complex(row: dict[str, str]) -> complex:
    if "C" in row and row["C"] != "":
        return complex(float(row["C"]), 0.0)
    if "real" in row and row["real"] != "":
        real = float(row["real"])
        imag = float(row.get("imag", "0") or "0")
        return complex(real, imag)
    raise ValueError("CSV rows must contain either C or real[,imag] columns")


def read_correlator_csv(path: Path, *, one_based: bool) -> dict[int, np.ndarray]:
    rows: list[tuple[int, int, int, complex]] = []
    max_index = -1
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("empty CSV input")
        for row in reader:
            t = int(row.get("t", ""))
            i_key = "i" if "i" in row else "op_i"
            j_key = "j" if "j" in row else "op_j"
            i = int(row[i_key])
            j = int(row[j_key])
            if one_based:
                i -= 1
                j -= 1
            if i < 0 or j < 0:
                raise ValueError("operator indices must be nonnegative after indexing convention")
            value = parse_complex(row)
            rows.append((t, i, j, value))
            max_index = max(max_index, i, j)
    n_ops = max_index + 1
    by_time: dict[int, np.ndarray] = {}
    present: dict[int, set[tuple[int, int]]] = {}
    for t, i, j, value in rows:
        by_time.setdefault(t, np.zeros((n_ops, n_ops), dtype=np.complex128))
        present.setdefault(t, set())
        by_time[t][i, j] = value
        present[t].add((i, j))
    for t, matrix in by_time.items():
        for i in range(n_ops):
            for j in range(n_ops):
                if (i, j) not in present[t] and (j, i) in present[t]:
                    matrix[i, j] = matrix[j, i].conjugate()
        by_time[t] = hermitian_part(matrix)
    return by_time


def exact_smoke_correlators() -> tuple[dict[int, np.ndarray], np.ndarray]:
    energies = np.array([0.55, 1.35], dtype=float)
    z = np.array([[1.0, 0.30], [0.45, 1.20]], dtype=float)
    correlators: dict[int, np.ndarray] = {}
    for t in range(0, 7):
        d = np.diag(np.exp(-energies * t))
        correlators[t] = z @ d @ z.T
    return correlators, energies


def run_smoke() -> dict[str, object]:
    correlators, exact_energies = exact_smoke_correlators()
    results = analyze_correlators(correlators, t0=1, times=[2, 3, 5], spacing=1.0)
    for result in results:
        got = np.array(result.energies)
        if not np.allclose(got, exact_energies, rtol=2.0e-12, atol=2.0e-12):
            raise AssertionError(f"smoke energies {got} do not match {exact_energies}")
    return {
        "status": "ok",
        "exact_energies": [float(x) for x in exact_energies],
        "results": [result.__dict__ for result in results],
    }


def parse_times(value: str | None) -> list[int] | None:
    if value is None or value.strip() == "":
        return None
    return [int(piece) for piece in value.split(",") if piece.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="CSV with columns t,i,j,C or t,i,j,real,imag")
    parser.add_argument("--t0", type=int, default=1, help="reference Euclidean time")
    parser.add_argument("--times", help="comma-separated analysis times; default: all t>t0")
    parser.add_argument("--spacing", type=float, default=1.0, help="Euclidean time lattice spacing")
    parser.add_argument("--one-based", action="store_true", help="interpret operator indices as one-based")
    parser.add_argument("--smoke", action="store_true", help="run the exact two-state smoke test")
    args = parser.parse_args(argv)

    if args.smoke:
        print(json.dumps(run_smoke(), indent=2, sort_keys=True))
        return 0
    if args.input is None:
        parser.error("--input is required unless --smoke is used")
    correlators = read_correlator_csv(args.input, one_based=args.one_based)
    results = analyze_correlators(
        correlators,
        t0=args.t0,
        times=parse_times(args.times),
        spacing=args.spacing,
    )
    print(json.dumps({"results": [result.__dict__ for result in results]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
