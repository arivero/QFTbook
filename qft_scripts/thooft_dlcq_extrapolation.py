#!/usr/bin/env python3
"""Large-K diagnostic fits for the finite 't Hooft DLCQ matrices.

This script takes the finite harmonic-resolution matrices built in
``thooft_dlcq.py`` and fits fixed eigenvalue labels to a chosen polynomial in
K^{-omega}.  The output is a finite-regulator diagnostic.  It is not a proof
of the continuum large-N two-dimensional QCD spectrum: such a proof would
need endpoint estimates, zero-mode control, and a remainder bound for the
chosen cutoff expansion.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

import numpy as np

import thooft_dlcq


def parse_Ks(text: str) -> list[int]:
    pieces = text.replace(",", " ").split()
    if not pieces:
        raise ValueError("at least one harmonic resolution must be supplied")
    values = [int(piece) for piece in pieces]
    if any(K < 3 for K in values):
        raise ValueError("every harmonic resolution K must be at least 3")
    if sorted(set(values)) != values:
        raise ValueError("harmonic resolutions must be distinct and increasing")
    return values


def design_matrix(Ks: Sequence[int], fit_order: int, base_exponent: float) -> np.ndarray:
    if fit_order < 0:
        raise ValueError("fit_order must be nonnegative")
    if base_exponent <= 0.0:
        raise ValueError("base_exponent must be positive")
    if len(Ks) < fit_order + 1:
        raise ValueError("need at least fit_order + 1 cutoff values")
    q = np.array([float(K) ** (-base_exponent) for K in Ks], dtype=float)
    powers = np.arange(fit_order + 1, dtype=float)
    matrix = q[:, np.newaxis] ** powers[np.newaxis, :]
    rank = int(np.linalg.matrix_rank(matrix))
    if rank != fit_order + 1:
        raise ValueError("cutoff design matrix is rank deficient")
    return matrix


def finite_spectrum(
    K: int,
    m1: float,
    m2: float,
    gamma: float,
    levels: int,
) -> list[float]:
    if levels < 1:
        raise ValueError("levels must be positive")
    if levels > K - 1:
        raise ValueError("cannot ask for more levels than the finite matrix size")
    matrix = thooft_dlcq.thooft_matrix(K, m1, m2, gamma)
    eigs = np.linalg.eigvalsh(matrix)
    return [float(x) for x in eigs[:levels]]


def fit_cutoff_sequence(
    Ks: Sequence[int],
    values: Sequence[float],
    fit_order: int,
    base_exponent: float,
) -> dict[str, float | list[float]]:
    if len(Ks) != len(values):
        raise ValueError("Ks and values must have the same length")
    design = design_matrix(Ks, fit_order, base_exponent)
    y = np.array(values, dtype=float)
    coeffs, _, _, singular_values = np.linalg.lstsq(design, y, rcond=None)
    fitted = design @ coeffs
    residuals = y - fitted
    influence = np.linalg.pinv(design)[0, :]
    return {
        "A_infinity": float(coeffs[0]),
        "coefficients": [float(x) for x in coeffs],
        "residual_rms": float(np.sqrt(np.mean(residuals * residuals))),
        "max_residual": float(np.max(np.abs(residuals))),
        "last_cutoff_shift": float(y[-1] - coeffs[0]),
        "intercept_remainder_amplification_l1": float(np.sum(np.abs(influence))),
        "condition_number": float(singular_values[0] / singular_values[-1]),
    }


def run(
    Ks: Sequence[int],
    levels: int,
    m1: float,
    m2: float,
    gamma: float,
    fit_order: int,
    base_exponent: float,
) -> dict[str, object]:
    if levels > min(Ks) - 1:
        raise ValueError("levels must not exceed the smallest finite matrix size")
    finite_data = [
        {
            "K": int(K),
            "levels": finite_spectrum(K, m1, m2, gamma, levels),
        }
        for K in Ks
    ]
    level_fits = []
    for level in range(levels):
        values = [entry["levels"][level] for entry in finite_data]
        fit = fit_cutoff_sequence(Ks, values, fit_order, base_exponent)
        fit["level"] = level
        fit["finite_values"] = [float(x) for x in values]
        level_fits.append(fit)
    positive = all(
        all(float(value) > 0.0 for value in entry["levels"])
        for entry in finite_data
    )
    return {
        "Ks": [int(K) for K in Ks],
        "levels": int(levels),
        "m1": float(m1),
        "m2": float(m2),
        "gamma": float(gamma),
        "fit_order": int(fit_order),
        "base_exponent": float(base_exponent),
        "finite_lowest_M2": finite_data,
        "extrapolated_levels": level_fits,
        "positive_finite_spectra": bool(positive),
        "interpretation": (
            "finite diagnostic only; a continuum claim requires an analytic "
            "large-K remainder estimate"
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ks", default="12,16,20,24,28")
    parser.add_argument("--levels", type=int, default=3)
    parser.add_argument("--m1", type=float, default=0.2)
    parser.add_argument("--m2", type=float, default=0.2)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--fit-order", type=int, default=2)
    parser.add_argument("--base-exponent", type=float, default=1.0)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.Ks = "8,10,12,14"
        args.levels = 2
        args.fit_order = 1
        args.base_exponent = 1.0
        args.m1 = 0.15
        args.m2 = 0.15
        args.gamma = 0.5
    Ks = parse_Ks(args.Ks)
    result = run(
        Ks=Ks,
        levels=args.levels,
        m1=args.m1,
        m2=args.m2,
        gamma=args.gamma,
        fit_order=args.fit_order,
        base_exponent=args.base_exponent,
    )
    if args.smoke:
        if not result["positive_finite_spectra"]:
            raise AssertionError("finite DLCQ spectra should be positive in the smoke run")
        for fit in result["extrapolated_levels"]:
            if not np.isfinite(float(fit["A_infinity"])):
                raise AssertionError("fit produced a non-finite intercept")
            if float(fit["condition_number"]) <= 1.0:
                raise AssertionError("unexpected condition-number diagnostic")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
