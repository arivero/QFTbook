#!/usr/bin/env python3
"""Finite checks for the K-S positive-energy semigroup discussion."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import cmath
import math


TOL = 1e-10


def assert_close(label: str, lhs: complex, rhs: complex, tol: float = TOL) -> None:
    _assert_close(label, lhs, rhs, tol=tol)


def coth(z: complex) -> complex:
    return cmath.cosh(z) / cmath.sinh(z)


def csch(z: complex) -> complex:
    return 1 / cmath.sinh(z)


def mehler_coefficients(omega: float, tau: complex) -> tuple[complex, complex, complex]:
    """Return N_tau, A_tau, B_tau for exp[-1/2(A x^2 + 2B xy + A y^2)]."""

    wt = omega * tau
    normalization = cmath.sqrt(omega / (2 * math.pi * cmath.sinh(wt)))
    diagonal = omega * coth(wt)
    off_diagonal = -omega * csch(wt)
    return normalization, diagonal, off_diagonal


def compose_coefficients(
    first: tuple[complex, complex, complex],
    second: tuple[complex, complex, complex],
) -> tuple[complex, complex, complex]:
    n1, a1, b1 = first
    n2, a2, b2 = second
    c = a1 + a2
    normalization = n1 * n2 * cmath.sqrt(2 * math.pi / c)
    diagonal_left = a1 - b1 * b1 / c
    diagonal_right = a2 - b2 * b2 / c
    off_diagonal = -b1 * b2 / c
    assert_close("left and right diagonal agree", diagonal_left, diagonal_right)
    return normalization, diagonal_left, off_diagonal


def check_mehler_composition() -> None:
    examples = [
        (0.7, 0.3, 0.4),
        (1.0, 0.2 + 0.1j, 0.5 - 0.05j),
        (2.3, 0.6 - 0.2j, 0.25 + 0.1j),
    ]
    for omega, tau, sigma in examples:
        lhs = compose_coefficients(
            mehler_coefficients(omega, tau),
            mehler_coefficients(omega, sigma),
        )
        rhs = mehler_coefficients(omega, tau + sigma)
        assert_close(f"Mehler normalization omega={omega}", lhs[0], rhs[0])
        assert_close(f"Mehler diagonal omega={omega}", lhs[1], rhs[1])
        assert_close(f"Mehler off-diagonal omega={omega}", lhs[2], rhs[2])


def check_positive_energy_boundary_values() -> None:
    eigenvalues = [0.0, 0.4, 1.7, 5.2]
    for epsilon in [0.5, 0.1, 0.01]:
        for time in [-2.0, -0.3, 0.0, 1.2]:
            for lam in eigenvalues:
                semigroup_value = cmath.exp(-(epsilon + 1j * time) * lam)
                boundary_value = cmath.exp(-1j * time * lam)
                assert abs(semigroup_value) <= 1 + TOL
                if epsilon == 0.01:
                    assert_close(
                        f"boundary approach lambda={lam}, t={time}",
                        semigroup_value,
                        boundary_value,
                        tol=6e-2,
                    )


def main() -> None:
    check_mehler_composition()
    check_positive_energy_boundary_values()
    print("All K-S semigroup checks passed.")


if __name__ == "__main__":
    main()
