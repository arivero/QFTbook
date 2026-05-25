#!/usr/bin/env python3
"""Finite Hamiltonian-truncation benchmark for the Ising energy deformation.

The Ising CFT perturbed by its energy operator is the free massive Majorana
theory.  On a circle, each positive Neveu-Schwarz mode r = n + 1/2 gives a
two-dimensional Bogoliubov block

    H_r = [[-p_r, m], [m, p_r]],   p_r = 2 pi r / L.

The eigenvalues are exactly +/-sqrt(p_r^2 + m^2).  This script diagonalizes
the finite truncated block matrix and compares against the closed form.  It is
a deliberately elementary TCSA-style benchmark: it checks the cutoff
Hamiltonian algebra before one moves to nonintegrable perturbations where
matrix elements and counterterms are not diagonal block data.
"""

from __future__ import annotations

import argparse
import json
import math

import numpy as np


def block_matrix(num_modes: int, mass: float, circumference: float) -> np.ndarray:
    matrix = np.zeros((2 * num_modes, 2 * num_modes), dtype=float)
    for n in range(num_modes):
        r = n + 0.5
        p = 2.0 * math.pi * r / circumference
        block = np.array([[-p, mass], [mass, p]], dtype=float)
        matrix[2 * n : 2 * n + 2, 2 * n : 2 * n + 2] = block
    return matrix


def exact_eigenvalues(num_modes: int, mass: float, circumference: float) -> np.ndarray:
    values: list[float] = []
    for n in range(num_modes):
        r = n + 0.5
        p = 2.0 * math.pi * r / circumference
        omega = math.sqrt(p * p + mass * mass)
        values.extend([-omega, omega])
    return np.array(sorted(values), dtype=float)


def run(num_modes: int, mass: float, circumference: float) -> dict[str, float | int | list[float]]:
    matrix = block_matrix(num_modes, mass, circumference)
    numerical = np.linalg.eigvalsh(matrix)
    exact = exact_eigenvalues(num_modes, mass, circumference)
    max_abs_error = float(np.max(np.abs(numerical - exact)))
    return {
        "num_modes": num_modes,
        "mass": mass,
        "circumference": circumference,
        "max_abs_error": max_abs_error,
        "lowest_eigenvalues": [float(x) for x in numerical[: min(6, numerical.size)]],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--num-modes", type=int, default=8)
    parser.add_argument("--mass", type=float, default=0.7)
    parser.add_argument("--circumference", type=float, default=10.0)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.num_modes = 5
        args.mass = 0.6
        args.circumference = 7.0
    result = run(args.num_modes, args.mass, args.circumference)
    if args.smoke and result["max_abs_error"] > 1.0e-12:
        raise AssertionError("Bogoliubov block diagonalization failed")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
