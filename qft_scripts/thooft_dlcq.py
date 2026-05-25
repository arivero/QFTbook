#!/usr/bin/env python3
"""DLCQ-style finite matrix for the large-N two-dimensional QCD meson equation.

The continuum 't Hooft equation contains the principal-value operator

    PV int_0^1 dy (phi(x)-phi(y))/(x-y)^2.

At harmonic resolution K this script uses grid points x_n=n/K, n=1,...,K-1,
and the positive symmetric matrix

    H_nm = delta_nm [m1^2/x_n + m2^2/(1-x_n)
             + gamma K sum_{j != n} 1/(n-j)^2]
           - (1-delta_nm) gamma K/(n-m)^2.

The matrix is a finite regulator.  Its eigenvalues are not continuum QFT data
until the K -> infinity extrapolation, zero-mode treatment, and normalization
conventions have been analyzed.
"""

from __future__ import annotations

import argparse
import json

import numpy as np


def thooft_matrix(K: int, m1: float, m2: float, gamma: float) -> np.ndarray:
    if K < 3:
        raise ValueError("K must be at least 3")
    size = K - 1
    matrix = np.zeros((size, size), dtype=float)
    xs = np.arange(1, K, dtype=float) / float(K)
    for i in range(size):
        x = xs[i]
        matrix[i, i] += m1 * m1 / x + m2 * m2 / (1.0 - x)
        for j in range(size):
            if i == j:
                continue
            weight = gamma * K / float((i - j) * (i - j))
            matrix[i, i] += weight
            matrix[i, j] -= weight
    return matrix


def quadratic_form_check(matrix: np.ndarray, trials: int, seed: int) -> float:
    rng = np.random.default_rng(seed)
    minimum = float("inf")
    for _ in range(trials):
        v = rng.normal(size=matrix.shape[0])
        value = float(v @ matrix @ v)
        norm = float(v @ v)
        minimum = min(minimum, value / norm)
    return minimum


def run(K: int, m1: float, m2: float, gamma: float, seed: int) -> dict[str, float | int | list[float]]:
    matrix = thooft_matrix(K, m1, m2, gamma)
    eigs = np.linalg.eigvalsh(matrix)
    random_lower_bound = quadratic_form_check(matrix, trials=64, seed=seed)
    return {
        "K": K,
        "m1": m1,
        "m2": m2,
        "gamma": gamma,
        "lowest_M2": [float(x) for x in eigs[: min(6, eigs.size)]],
        "random_quadratic_form_min": random_lower_bound,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--K", type=int, default=24)
    parser.add_argument("--m1", type=float, default=0.2)
    parser.add_argument("--m2", type=float, default=0.2)
    parser.add_argument("--gamma", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=20260525)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.K = 12
        args.m1 = 0.15
        args.m2 = 0.15
        args.gamma = 0.5
        args.seed = 271828
    result = run(args.K, args.m1, args.m2, args.gamma, args.seed)
    if args.smoke:
        if result["lowest_M2"][0] <= 0.0:
            raise AssertionError("finite matrix should be positive for positive quark masses")
        if result["random_quadratic_form_min"] <= 0.0:
            raise AssertionError("random quadratic-form check found a negative value")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
