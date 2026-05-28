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
import tffsa_ising_spin_connected as tffsa  # noqa: E402
import thooft_dlcq  # noqa: E402
import thooft_dlcq_extrapolation as thooft_extrapolation  # noqa: E402


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-11) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name: str, actual: float, bound: float, tol: float = 1.0e-12) -> None:
    if actual > bound + tol:
        raise AssertionError(f"{name}: got {actual!r}, bound {bound!r}")


def check_ising_bogoliubov_benchmark() -> None:
    result = tcsa.run(num_modes=7, mass=0.8, circumference=9.0)
    assert_leq("Ising Bogoliubov finite spectrum", result["max_abs_error"], 1.0e-12)


def check_tffsa_connected_spin_block() -> None:
    cfg = tffsa.RunConfig(
        num_pairs=4,
        mass=1.0,
        circumference=7.0,
        magnetic_coupling=0.02,
        sigma_bar=1.3,
    )
    states = tffsa.pair_states(cfg.num_pairs, cfg.mass, cfg.circumference)
    matrix = tffsa.finite_matrix(cfg)
    hermiticity_error = float(np.max(np.abs(matrix - matrix.conjugate().T)))
    assert_leq("TFFSA finite block Hermiticity", hermiticity_error, 1.0e-12)

    theta = states[0].theta
    density = states[0].density
    expected_vacuum_pair = (
        cfg.magnetic_coupling
        * cfg.circumference
        * 1j
        * cfg.sigma_bar
        * np.tanh(theta)
        / np.sqrt(density)
    )
    assert_close("TFFSA vacuum-pair form factor", matrix[0, 1], expected_vacuum_pair)

    theta_1 = states[0].theta
    theta_2 = states[1].theta
    crossed = [complex(theta_1, np.pi), complex(-theta_1, np.pi), theta_2, -theta_2]
    expected_pair_pair = (
        cfg.magnetic_coupling
        * cfg.circumference
        * tffsa.spin_even_form_factor(crossed, cfg.sigma_bar)
        / np.sqrt(states[0].density * states[1].density)
    )
    assert_close("TFFSA pair-pair crossed form factor", matrix[1, 2], expected_pair_pair)

    free_cfg = tffsa.RunConfig(
        num_pairs=cfg.num_pairs,
        mass=cfg.mass,
        circumference=cfg.circumference,
        magnetic_coupling=0.0,
        sigma_bar=cfg.sigma_bar,
    )
    free_eigs = np.linalg.eigvalsh(tffsa.finite_matrix(free_cfg))
    expected_free = np.array([0.0] + [state.energy for state in states])
    if np.max(np.abs(free_eigs - expected_free)) > 1.0e-12:
        raise AssertionError("TFFSA zero-coupling spectrum does not match free energies")


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


def check_thooft_large_K_fit_algebra() -> None:
    Ks = thooft_extrapolation.parse_Ks("8, 10 12,16")
    if Ks != [8, 10, 12, 16]:
        raise AssertionError("DLCQ K parser changed its ordering convention")

    exact_values = [2.5 - 1.25 / K + 0.75 / (K * K) for K in Ks]
    exact_fit = thooft_extrapolation.fit_cutoff_sequence(
        Ks=Ks,
        values=exact_values,
        fit_order=2,
        base_exponent=1.0,
    )
    assert_close("DLCQ exact polynomial intercept", exact_fit["A_infinity"], 2.5)
    assert_leq("DLCQ exact polynomial residual", exact_fit["max_residual"], 1.0e-13)

    constant_fit = thooft_extrapolation.fit_cutoff_sequence(
        Ks=Ks,
        values=[3.0 for _ in Ks],
        fit_order=2,
        base_exponent=1.0,
    )
    assert_close("DLCQ constant intercept", constant_fit["A_infinity"], 3.0)
    assert_leq("DLCQ constant residual", constant_fit["max_residual"], 1.0e-13)

    script_result = thooft_extrapolation.run(
        Ks=[8, 10, 12],
        levels=2,
        m1=0.15,
        m2=0.15,
        gamma=0.5,
        fit_order=1,
        base_exponent=1.0,
    )
    if not script_result["positive_finite_spectra"]:
        raise AssertionError("finite large-K DLCQ diagnostic found a negative spectrum")
    for level_fit in script_result["extrapolated_levels"]:
        if not np.isfinite(level_fit["A_infinity"]):
            raise AssertionError("finite large-K DLCQ diagnostic produced a non-finite fit")


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
    check_tffsa_connected_spin_block()
    check_thooft_quadratic_form_identity()
    check_thooft_large_K_fit_algebra()
    check_residual_certificate()
    check_feshbach_determinant_identity()
    print("All Hamiltonian-truncation and DLCQ checks passed.")


if __name__ == "__main__":
    main()
