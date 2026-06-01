#!/usr/bin/env python3
"""Finite sine-Gordon zero-mode truncation benchmark.

This script implements the finite matrix

    H_N = P_N (-kappa d_theta^2 + g cos(theta)) P_N

on the Fourier basis |n> = exp(i n theta), -N <= n <= N.  It is the
oscillator-vacuum zero-mode slice of a compact-boson TCSA convention check,
not the full finite-volume sine-Gordon spectrum.  The full QFT problem needs
oscillator descendants, winding/topological sectors, normal-ordering
conventions, counterterms, and a cutoff-removal analysis.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RunConfig:
    nmax: int = 8
    kappa: float = 0.7
    coupling: float = 0.2


def basis_labels(nmax: int) -> list[int]:
    if nmax < 0:
        raise ValueError("nmax must be nonnegative")
    return list(range(-nmax, nmax + 1))


def cosine_matrix(nmax: int) -> np.ndarray:
    labels = basis_labels(nmax)
    matrix = np.zeros((len(labels), len(labels)), dtype=float)
    for i, n in enumerate(labels):
        for j, m in enumerate(labels):
            if abs(n - m) == 1:
                matrix[i, j] = 0.5
    return matrix


def hamiltonian_matrix(cfg: RunConfig) -> tuple[list[int], np.ndarray, np.ndarray]:
    if cfg.kappa <= 0.0:
        raise ValueError("kappa must be positive")
    labels = basis_labels(cfg.nmax)
    free = np.diag([float(cfg.kappa) * float(n * n) for n in labels])
    interaction = float(cfg.coupling) * cosine_matrix(cfg.nmax)
    return labels, free, free + interaction


def second_order_ground_shift(kappa: float, coupling: float) -> float:
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    return -(coupling * coupling) / (2.0 * kappa)


def run(cfg: RunConfig) -> dict[str, object]:
    labels, free, hamiltonian = hamiltonian_matrix(cfg)
    eigenvalues = np.linalg.eigvalsh(hamiltonian)
    free_eigenvalues = np.linalg.eigvalsh(free)
    hermiticity_error = float(np.max(np.abs(hamiltonian - hamiltonian.T)))
    reflection_error = 0.0
    label_to_index = {n: i for i, n in enumerate(labels)}
    for n in labels:
        for m in labels:
            reflected_error = abs(
                hamiltonian[label_to_index[n], label_to_index[m]]
                - hamiltonian[label_to_index[-n], label_to_index[-m]]
            )
            reflection_error = max(reflection_error, float(reflected_error))
    return {
        "nmax": cfg.nmax,
        "kappa": cfg.kappa,
        "coupling": cfg.coupling,
        "dimension": len(labels),
        "hermiticity_error": hermiticity_error,
        "reflection_error": reflection_error,
        "free_lowest": [float(x) for x in free_eigenvalues[: min(6, len(labels))]],
        "lowest_eigenvalues": [float(x) for x in eigenvalues[: min(6, len(labels))]],
        "second_order_ground_shift": second_order_ground_shift(cfg.kappa, cfg.coupling),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nmax", type=int, default=8)
    parser.add_argument("--kappa", type=float, default=0.7)
    parser.add_argument("--coupling", type=float, default=0.2)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.nmax = 5
        args.kappa = 0.75
        args.coupling = 0.15
    result = run(RunConfig(args.nmax, args.kappa, args.coupling))
    if args.smoke:
        if result["hermiticity_error"] > 1.0e-12:
            raise AssertionError("finite sine-Gordon zero-mode matrix is not Hermitian")
        if result["reflection_error"] > 1.0e-12:
            raise AssertionError("finite sine-Gordon zero-mode reflection symmetry failed")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
