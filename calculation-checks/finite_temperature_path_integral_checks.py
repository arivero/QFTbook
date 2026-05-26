#!/usr/bin/env python3
"""Finite checks for thermal path-integral conventions.

The checks cover algebraic facts used in the finite-temperature path-integral
chapter: circle eigenvalue quantization, finite-volume spectral representation
of Euclidean correlators, Matsubara Cauchy transforms, and chemical-potential
twist bookkeeping.  They are finite-dimensional convention checks, not a
continuum construction.
"""

from __future__ import annotations

import cmath
import math


def assert_close(lhs: complex, rhs: complex, message: str, tol: float = 1e-10) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def check_matsubara_boundary_phases() -> None:
    beta = 1.7
    for n in range(-4, 5):
        omega_b = 2.0 * math.pi * n / beta
        assert_close(cmath.exp(1j * omega_b * beta), 1.0, "bosonic mode is periodic")

        omega_f = (2 * n + 1) * math.pi / beta
        assert_close(cmath.exp(1j * omega_f * beta), -1.0, "fermionic mode is antiperiodic")


def off_diagonal_matrix(entries: dict[tuple[int, int], complex], size: int) -> list[list[complex]]:
    matrix = [[0j for _ in range(size)] for _ in range(size)]
    for (i, j), value in entries.items():
        if i == j:
            raise ValueError("use off-diagonal entries to avoid zero-frequency contact terms")
        matrix[i][j] = complex(value)
    return matrix


def direct_euclidean_correlator(
    energies: list[float],
    beta: float,
    tau: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            total += (
                math.exp(-beta * en)
                * math.exp(-tau * (em - en))
                * a_matrix[n][m]
                * b_matrix[m][n]
            )
    return total / z


def spectral_atoms(
    energies: list[float],
    beta: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> list[tuple[float, complex]]:
    z = sum(math.exp(-beta * energy) for energy in energies)
    atoms: list[tuple[float, complex]] = []
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            weight = (
                (math.exp(-beta * en) - math.exp(-beta * em))
                * a_matrix[n][m]
                * b_matrix[m][n]
                / z
            )
            if abs(weight) > 1e-14:
                atoms.append((em - en, weight))
    return atoms


def zero_mode_contribution(
    energies: list[float],
    beta: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            if abs(em - en) < 1e-14:
                total += math.exp(-beta * en) * a_matrix[n][m] * b_matrix[m][n]
    return total / z


def spectral_euclidean_correlator(atoms: list[tuple[float, complex]], beta: float, tau: float) -> complex:
    total = 0j
    for omega, weight in atoms:
        total += math.exp(-omega * tau) * weight / (1.0 - math.exp(-beta * omega))
    return total


def direct_matsubara_transform(
    energies: list[float],
    beta: float,
    matsubara_frequency: float,
    a_matrix: list[list[complex]],
    b_matrix: list[list[complex]],
) -> complex:
    z = sum(math.exp(-beta * energy) for energy in energies)
    total = 0j
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            omega = em - en
            coefficient = math.exp(-beta * en) * a_matrix[n][m] * b_matrix[m][n] / z
            if abs(coefficient) < 1e-14:
                continue
            exponent = -omega + 1j * matsubara_frequency
            if abs(exponent) < 1e-14:
                total += coefficient * beta
            else:
                total += coefficient * (cmath.exp(exponent * beta) - 1.0) / exponent
    return total


def cauchy_matsubara_transform(atoms: list[tuple[float, complex]], matsubara_frequency: float) -> complex:
    return sum(weight / (omega - 1j * matsubara_frequency) for omega, weight in atoms)


def check_bosonic_spectral_representation() -> None:
    energies = [0.25, 1.1, 2.3]
    beta = 1.4
    a_matrix = off_diagonal_matrix({(0, 1): 2.0, (1, 2): -0.7j, (2, 0): 1.1}, 3)
    b_matrix = off_diagonal_matrix({(1, 0): 0.4, (2, 1): 1.3j, (0, 2): -0.2}, 3)
    atoms = spectral_atoms(energies, beta, a_matrix, b_matrix)

    for tau in [0.2, 0.6, 1.1]:
        assert_close(
            direct_euclidean_correlator(energies, beta, tau, a_matrix, b_matrix),
            spectral_euclidean_correlator(atoms, beta, tau),
            "finite spectral formula reproduces Euclidean correlator",
        )

    for ell in [1, 2, 3]:
        matsubara = 2.0 * math.pi * ell / beta
        assert_close(
            direct_matsubara_transform(energies, beta, matsubara, a_matrix, b_matrix),
            cauchy_matsubara_transform(atoms, matsubara),
            "Matsubara transform equals spectral Cauchy transform",
        )

    diagonal_a = [[1.0, 0j, 0j], [0j, -0.3, 0j], [0j, 0j, 0.8]]
    diagonal_b = [[0.2, 0j, 0j], [0j, 1.4, 0j], [0j, 0j, -0.5]]
    zero_mode = zero_mode_contribution(energies, beta, diagonal_a, diagonal_b)
    for tau in [0.15, 0.75, 1.25]:
        assert_close(
            direct_euclidean_correlator(energies, beta, tau, diagonal_a, diagonal_b),
            zero_mode,
            "degenerate spectral contribution is a separate Euclidean zero mode",
        )
    assert_close(
        direct_matsubara_transform(energies, beta, 0.0, diagonal_a, diagonal_b),
        beta * zero_mode,
        "zero Matsubara mode includes beta times the constant spectral term",
    )
    first_nonzero_bosonic = 2.0 * math.pi / beta
    assert_close(
        direct_matsubara_transform(energies, beta, first_nonzero_bosonic, diagonal_a, diagonal_b),
        0.0,
        "constant spectral term has no nonzero Matsubara coefficient",
    )


def check_chemical_potential_twist() -> None:
    beta = 2.0
    mu = 0.37
    charge = 3
    spin_sign = -1
    twist = spin_sign * math.exp(beta * mu * charge)

    # If a field with the original thermal spin structure is redefined by
    # Phi(tau)=exp(mu*q*tau) phi(tau), the new variable has the twisted
    # boundary condition used in the chapter.
    phi_zero = 1.2 - 0.4j
    phi_beta = spin_sign * phi_zero
    big_phi_zero = phi_zero
    big_phi_beta = math.exp(beta * mu * charge) * phi_beta
    assert_close(big_phi_beta, twist * big_phi_zero, "chemical potential is a thermal twist")

    imaginary_mu_period = 2.0 * math.pi / beta
    phase = cmath.exp(1j * beta * imaginary_mu_period * charge)
    assert_close(phase, 1.0, "integer charges give large-gauge periodicity for imaginary chemical potential")


def main() -> None:
    check_matsubara_boundary_phases()
    check_bosonic_spectral_representation()
    check_chemical_potential_twist()
    print("Finite-temperature path-integral convention checks passed.")


if __name__ == "__main__":
    main()
