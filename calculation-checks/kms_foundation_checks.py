#!/usr/bin/env python3
"""Finite checks for the KMS-state and thermal-correlator foundation chapter."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def alpha(matrix: list[list[complex]], energies: list[float], z: complex) -> list[list[complex]]:
    size = len(energies)
    return [
        [matrix[m][n] * cmath.exp(1j * (energies[m] - energies[n]) * z) for n in range(size)]
        for m in range(size)
    ]


def gibbs_expectation(matrix: list[list[complex]], energies: list[float], beta: float) -> complex:
    weights = [math.exp(-beta * e) for e in energies]
    zpart = sum(weights)
    return sum(weights[i] * matrix[i][i] for i in range(len(energies))) / zpart


def check_finite_trace_kms_boundary() -> None:
    beta = 0.8
    energies = [0.0, 1.25, 2.0]
    a = [
        [1.0, 0.3 + 0.2j, -0.4],
        [0.1 - 0.5j, -0.7, 0.6j],
        [0.2, -0.3j, 0.4],
    ]
    b = [
        [0.2, -0.1j, 0.5],
        [0.7 + 0.2j, -0.1, 0.3],
        [-0.6j, 0.4 - 0.2j, 0.9],
    ]
    zpart = sum(math.exp(-beta * e) for e in energies)

    for t in (-1.3, 0.0, 0.9):
        lower = gibbs_expectation(matmul(a, alpha(b, energies, t)), energies, beta)
        explicit_lower = sum(
            math.exp(-beta * energies[m])
            * a[m][n]
            * b[n][m]
            * cmath.exp(1j * (energies[n] - energies[m]) * t)
            for m in range(3)
            for n in range(3)
        ) / zpart
        assert_close("finite KMS lower boundary", lower, explicit_lower)

        upper = sum(
            math.exp(-beta * energies[m])
            * a[m][n]
            * b[n][m]
            * cmath.exp(1j * (energies[n] - energies[m]) * (t + 1j * beta))
            for m in range(3)
            for n in range(3)
        ) / zpart
        target = gibbs_expectation(matmul(alpha(b, energies, t), a), energies, beta)
        assert_close("finite KMS upper boundary", upper, target)


def transition_weights(operator_a: list[list[complex]], energies: list[float], beta: float) -> dict[float, float]:
    zpart = sum(math.exp(-beta * e) for e in energies)
    weights: dict[float, float] = {}
    for m, em in enumerate(energies):
        for n, en in enumerate(energies):
            omega = round(en - em, 12)
            contribution = math.exp(-beta * em) * abs(operator_a[m][n]) ** 2 / zpart
            weights[omega] = weights.get(omega, 0.0) + contribution
    return weights


def check_detailed_balance_and_spectral_reconstruction() -> None:
    beta = 1.1
    energies = [0.0, 0.7, 2.1]
    a = [
        [0.0, 1.0, 0.5],
        [1.0, 0.0, -0.25],
        [0.5, -0.25, 0.0],
    ]
    greater = transition_weights(a, energies, beta)
    for omega, greater_weight in greater.items():
        lesser_weight = greater.get(round(-omega, 12), 0.0)
        if abs(omega) < 1.0e-12:
            assert_close("zero-frequency detailed balance", lesser_weight, greater_weight)
            continue
        assert_close(
            f"detailed balance omega={omega}",
            lesser_weight,
            math.exp(-beta * omega) * greater_weight,
        )

        rho = greater_weight - lesser_weight
        reconstructed = rho / (1.0 - math.exp(-beta * omega))
        assert_close(f"spectral reconstruction omega={omega}", reconstructed, greater_weight)


def check_bosonic_fluctuation_dissipation() -> None:
    beta = 0.9
    for omega, greater_weight in ((0.4, 1.3), (1.7, 0.2), (-0.6, 0.5)):
        lesser_weight = math.exp(-beta * omega) * greater_weight
        rho = greater_weight - lesser_weight
        sym = 0.5 * (greater_weight + lesser_weight)
        coth = math.cosh(0.5 * beta * omega) / math.sinh(0.5 * beta * omega)
        assert_close(f"bosonic FDT omega={omega}", sym, 0.5 * coth * rho)


def check_retarded_sign_and_shear_slope() -> None:
    eta = 0.73
    tau = 1.4

    def retarded(omega: float) -> complex:
        return (-1j * eta * omega) / (1.0 - 1j * tau * omega)

    for omega in (1.0e-5, 2.0e-5, 5.0e-5):
        gr = retarded(omega)
        rho = -2.0 * gr.imag
        assert rho > 0.0
        assert_close("rho=-2 Im GR", rho, -2.0 * gr.imag)
        assert_close("shear slope", rho / (2.0 * omega), eta, tol=2.0e-5)
        assert_close("minus imaginary slope", -gr.imag / omega, eta, tol=2.0e-5)


def main() -> None:
    check_finite_trace_kms_boundary()
    check_detailed_balance_and_spectral_reconstruction()
    check_bosonic_fluctuation_dissipation()
    check_retarded_sign_and_shear_slope()
    print("All KMS foundation checks passed.")


if __name__ == "__main__":
    main()
