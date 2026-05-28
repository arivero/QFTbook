#!/usr/bin/env python3
"""Finite spectral-flow diagnostic for the Ising connected TFFSA block.

The connected-block script builds a finite Hermitian matrix

    H(h) = H_0 + h W

for the zero-momentum massive-Ising spin perturbation in a declared
finite-volume convention.  This companion diagonalizes H(h) on a small grid
of magnetic couplings and compares finite-difference slopes with the
finite-dimensional Hellmann-Feynman derivative

    d lambda_a / dh = <u_a, W u_a>

at a selected value of h.  The output is a finite-matrix diagnostic.  It does
not assert the continuum magnetic-Ising spectrum or the E8 mass ratios.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

import numpy as np

import tffsa_ising_spin_connected as tffsa


def parse_h_values(text: str) -> list[float]:
    pieces = text.replace(",", " ").split()
    if not pieces:
        raise ValueError("at least one magnetic coupling must be supplied")
    values = [float(piece) for piece in pieces]
    if sorted(values) != values:
        raise ValueError("magnetic couplings must be nondecreasing")
    return values


def config_with_h(base: tffsa.RunConfig, magnetic_coupling: float) -> tffsa.RunConfig:
    return tffsa.RunConfig(
        num_pairs=base.num_pairs,
        mass=base.mass,
        circumference=base.circumference,
        magnetic_coupling=magnetic_coupling,
        sigma_bar=base.sigma_bar,
    )


def perturbation_matrix(base: tffsa.RunConfig) -> np.ndarray:
    h_zero = tffsa.finite_matrix(config_with_h(base, 0.0))
    h_one = tffsa.finite_matrix(config_with_h(base, 1.0))
    return h_one - h_zero


def eigensystem(base: tffsa.RunConfig, magnetic_coupling: float) -> tuple[np.ndarray, np.ndarray]:
    matrix = tffsa.finite_matrix(config_with_h(base, magnetic_coupling))
    values, vectors = np.linalg.eigh(matrix)
    return values, vectors


def minimum_neighbor_gap(values: Sequence[float]) -> float:
    if len(values) <= 1:
        return float("inf")
    sorted_values = np.sort(np.array(values, dtype=float))
    return float(np.min(np.diff(sorted_values)))


def hellmann_feynman_slopes(
    base: tffsa.RunConfig,
    magnetic_coupling: float,
) -> tuple[np.ndarray, np.ndarray, float]:
    values, vectors = eigensystem(base, magnetic_coupling)
    derivative = perturbation_matrix(base)
    slopes = np.einsum("ia,ij,ja->a", vectors.conjugate(), derivative, vectors)
    slopes = np.real_if_close(slopes, tol=1000).astype(float)
    trace_error = float(abs(np.sum(slopes) - np.trace(derivative).real))
    return values, slopes, trace_error


def centered_difference_slopes(
    base: tffsa.RunConfig,
    magnetic_coupling: float,
    delta: float,
) -> np.ndarray:
    if delta <= 0.0:
        raise ValueError("delta must be positive")
    values_plus, _ = eigensystem(base, magnetic_coupling + delta)
    values_minus, _ = eigensystem(base, magnetic_coupling - delta)
    return (values_plus - values_minus) / (2.0 * delta)


def run(
    base: tffsa.RunConfig,
    h_values: Sequence[float],
    slope_at: float,
    delta: float,
) -> dict[str, object]:
    derivative = perturbation_matrix(base)
    derivative_hermiticity_error = float(np.max(np.abs(derivative - derivative.conjugate().T)))
    flow = []
    minimum_gap = float("inf")
    for h_value in h_values:
        values, _ = eigensystem(base, h_value)
        minimum_gap = min(minimum_gap, minimum_neighbor_gap(values))
        flow.append(
            {
                "h": float(h_value),
                "lowest_eigenvalues": [float(x) for x in values[: min(6, len(values))]],
                "minimum_neighbor_gap": minimum_neighbor_gap(values),
            }
        )

    values_at, hf_slopes, trace_error = hellmann_feynman_slopes(base, slope_at)
    fd_slopes = centered_difference_slopes(base, slope_at, delta)
    slope_errors = fd_slopes - hf_slopes
    return {
        "num_pairs": base.num_pairs,
        "mass": base.mass,
        "circumference": base.circumference,
        "sigma_bar": base.sigma_bar,
        "h_values": [float(x) for x in h_values],
        "spectral_flow": flow,
        "slope_at": float(slope_at),
        "delta": float(delta),
        "eigenvalues_at_slope_point": [float(x) for x in values_at[: min(6, len(values_at))]],
        "hellmann_feynman_slopes": [float(x) for x in hf_slopes[: min(6, len(hf_slopes))]],
        "centered_difference_slopes": [float(x) for x in fd_slopes[: min(6, len(fd_slopes))]],
        "max_abs_slope_error": float(np.max(np.abs(slope_errors))),
        "trace_slope_error": trace_error,
        "derivative_hermiticity_error": derivative_hermiticity_error,
        "minimum_gap_over_grid": minimum_gap,
        "interpretation": (
            "finite connected-block spectral-flow diagnostic only; continuum "
            "magnetic-Ising claims require cutoff and finite-volume estimates"
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--num-pairs", type=int, default=5)
    parser.add_argument("--mass", type=float, default=1.0)
    parser.add_argument("--circumference", type=float, default=8.0)
    parser.add_argument("--sigma-bar", type=float, default=1.0)
    parser.add_argument("--h-values", default="-0.03,-0.015,0.0,0.015,0.03")
    parser.add_argument("--slope-at", type=float, default=0.02)
    parser.add_argument("--delta", type=float, default=1.0e-5)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.num_pairs = 4
        args.mass = 1.0
        args.circumference = 7.0
        args.sigma_bar = 1.0
        args.h_values = "-0.02,-0.01,0.0,0.01,0.02"
        args.slope_at = 0.015
        args.delta = 1.0e-5

    base = tffsa.RunConfig(
        num_pairs=args.num_pairs,
        mass=args.mass,
        circumference=args.circumference,
        magnetic_coupling=0.0,
        sigma_bar=args.sigma_bar,
    )
    result = run(
        base=base,
        h_values=parse_h_values(args.h_values),
        slope_at=args.slope_at,
        delta=args.delta,
    )
    if args.smoke:
        if result["derivative_hermiticity_error"] > 1.0e-12:
            raise AssertionError("TFFSA perturbation matrix is not Hermitian")
        if result["trace_slope_error"] > 1.0e-10:
            raise AssertionError("Hellmann-Feynman slopes fail the trace identity")
        if result["max_abs_slope_error"] > 1.0e-6:
            raise AssertionError("finite-difference slopes do not match Hellmann-Feynman slopes")
        if result["minimum_gap_over_grid"] <= 0.0:
            raise AssertionError("spectral-flow grid contains an unresolved finite-matrix crossing")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
