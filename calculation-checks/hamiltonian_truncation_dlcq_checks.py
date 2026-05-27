#!/usr/bin/env python3
"""Finite checks for Hamiltonian truncation and DLCQ benchmark algebra."""

from __future__ import annotations

import pathlib
import sys

import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import tcsa_ising_energy_benchmark as tcsa  # noqa: E402
import thooft_dlcq  # noqa: E402


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-11) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name: str, actual: float, bound: float, tol: float = 1.0e-12) -> None:
    if actual > bound + tol:
        raise AssertionError(f"{name}: got {actual!r}, bound {bound!r}")


def check_ising_bogoliubov_benchmark() -> None:
    result = tcsa.run(num_modes=7, mass=0.8, circumference=9.0)
    assert_leq("Ising Bogoliubov finite spectrum", result["max_abs_error"], 1.0e-12)


def check_thooft_quadratic_form_identity() -> None:
    K = 10
    m1 = 0.3
    m2 = 0.4
    gamma = 0.7
    matrix = thooft_dlcq.thooft_matrix(K, m1, m2, gamma)
    v = np.array([(-1.0) ** n * (n + 1.0) / 7.0 for n in range(K - 1)])
    left = float(v @ matrix @ v)
    xs = np.arange(1, K, dtype=float) / float(K)
    mass_part = float(np.sum((m1 * m1 / xs + m2 * m2 / (1.0 - xs)) * v * v))
    kernel_part = 0.0
    for n in range(K - 1):
        for m in range(n + 1, K - 1):
            kernel_part += gamma * K * (v[n] - v[m]) ** 2 / float((n - m) ** 2)
    assert_close("DLCQ quadratic-form identity", left, mass_part + kernel_part)
    if float(np.linalg.eigvalsh(matrix)[0]) <= 0.0:
        raise AssertionError("finite 't Hooft matrix should be positive definite")


def check_residual_certificate() -> None:
    eigenvalues = np.array([1.0, 3.0, 8.0])
    matrix = np.diag(eigenvalues)
    epsilon = 0.08
    vector = np.array([(1.0 - epsilon * epsilon) ** 0.5, epsilon, 0.0])
    vector /= np.linalg.norm(vector)
    lam = float(vector @ matrix @ vector)
    residual = float(np.linalg.norm((matrix - lam * np.eye(3)) @ vector))
    distance_to_spectrum = float(np.min(np.abs(eigenvalues - lam)))
    assert_leq("residual distance to spectrum", distance_to_spectrum, residual)

    complement_gap = float(np.min(np.abs(eigenvalues[1:] - lam)))
    leakage = float(np.linalg.norm(vector[1:]))
    assert_leq("projector leakage bound", leakage, residual / complement_gap)


def check_feshbach_determinant_identity() -> None:
    matrix = np.array(
        [
            [2.0, 0.3, 0.1],
            [0.3, 4.0, -0.2],
            [0.1, -0.2, 7.0],
        ],
        dtype=float,
    )
    energy = 1.7
    p_block = matrix[:2, :2]
    q_block = matrix[2:, 2:]
    p_to_q = matrix[:2, 2:]
    q_to_p = matrix[2:, :2]
    schur = p_block - p_to_q @ np.linalg.inv(q_block - energy * np.eye(1)) @ q_to_p
    full_det = float(np.linalg.det(matrix - energy * np.eye(3)))
    factored_det = float(
        np.linalg.det(q_block - energy * np.eye(1))
        * np.linalg.det(schur - energy * np.eye(2))
    )
    assert_close("Feshbach determinant identity", full_det, factored_det)


def main() -> None:
    check_ising_bogoliubov_benchmark()
    check_thooft_quadratic_form_identity()
    check_residual_certificate()
    check_feshbach_determinant_identity()
    print("All Hamiltonian-truncation and DLCQ checks passed.")


if __name__ == "__main__":
    main()
