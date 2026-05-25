#!/usr/bin/env python3
"""Finite checks for the sine-Gordon exact scattering datum in Volume VI."""

from __future__ import annotations

import cmath
import math


ComplexMatrix = list[list[complex]]


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(a: ComplexMatrix, b: ComplexMatrix) -> ComplexMatrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def matrix_part(theta: complex, xi: float) -> ComplexMatrix:
    lam = 1.0 / xi
    denom = cmath.sinh(lam * (1j * math.pi - theta))
    b = cmath.sinh(lam * theta) / denom
    c = 1j * math.sin(math.pi * lam) / denom
    return [
        [1.0 + 0j, 0j, 0j, 0j],
        [0j, b, c, 0j],
        [0j, c, b, 0j],
        [0j, 0j, 0j, 1.0 + 0j],
    ]


def breather_amplitude_b1b1(theta: complex, xi: float) -> complex:
    s = math.sin(math.pi * xi)
    return (cmath.sinh(theta) + 1j * s) / (cmath.sinh(theta) - 1j * s)


def check_matrix_unitarity() -> None:
    for xi in (0.37, 0.72, 1.35):
        for theta in (0.21, 0.93, -0.47):
            product = matmul(matrix_part(theta, xi), matrix_part(-theta, xi))
            for i in range(4):
                for j in range(4):
                    expected = 1.0 if i == j else 0.0
                    assert_close(f"matrix unitarity xi={xi} theta={theta} ({i},{j})", product[i][j], expected)


def check_free_fermion_point() -> None:
    xi = 1.0
    for theta in (0.31, 1.4):
        mat = matrix_part(theta, xi)
        assert_close("free-fermion transmission", mat[1][1], 1.0)
        assert_close("free-fermion reflection", mat[1][2], 0.0)


def check_breather_pole_locations_and_masses() -> None:
    xi = 0.23
    soliton_mass = 2.7
    for n in (1, 2, 3, 4):
        u = math.pi * (1.0 - n * xi)
        theta_pole = 1j * u
        denom = cmath.sinh((1.0 / xi) * (1j * math.pi - theta_pole))
        assert_close(f"breather pole denominator n={n}", denom, 0.0, tol=1.0e-9)

        mass_from_pole = 2.0 * soliton_mass * math.cos(u / 2.0)
        mass_formula = 2.0 * soliton_mass * math.sin(math.pi * n * xi / 2.0)
        assert_close(f"breather mass n={n}", mass_from_pole, mass_formula)


def check_lightest_breather_amplitude() -> None:
    for xi in (0.2, 0.41, 0.73):
        for theta in (0.19, 0.88, -1.2):
            amp = breather_amplitude_b1b1(theta, xi)
            assert_close(f"B1B1 unitarity xi={xi} theta={theta}", amp * breather_amplitude_b1b1(-theta, xi), 1.0)
            assert_close(
                f"B1B1 crossing xi={xi} theta={theta}",
                amp,
                breather_amplitude_b1b1(1j * math.pi - theta, xi),
            )

        pole = 1j * math.pi * xi
        denominator = cmath.sinh(pole) - 1j * math.sin(math.pi * xi)
        assert_close(f"B1B1 pole denominator xi={xi}", denominator, 0.0)


def main() -> None:
    check_matrix_unitarity()
    check_free_fermion_point()
    check_breather_pole_locations_and_masses()
    check_lightest_breather_amplitude()
    print("All sine-Gordon S-matrix checks passed.")


if __name__ == "__main__":
    main()
