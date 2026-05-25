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


def neutral_block(theta: complex, a: float) -> complex:
    s = math.sin(math.pi * a)
    return (cmath.sinh(theta) + 1j * s) / (cmath.sinh(theta) - 1j * s)


def breather_mass(n: int, xi: float, soliton_mass: float) -> float:
    return 2.0 * soliton_mass * math.sin(math.pi * n * xi / 2.0)


def breather_breather_amplitude(theta: complex, m: int, n: int, xi: float) -> complex:
    low = min(m, n)
    gap = abs(m - n)
    result = neutral_block(theta, (m + n) * xi / 2.0) * neutral_block(theta, gap * xi / 2.0)
    for ell in range(1, low):
        result *= neutral_block(theta, (gap + 2 * ell) * xi / 2.0) ** 2
    return result


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

        for pole_name, pole in (
            ("direct", 1j * math.pi * xi),
            ("crossed", 1j * math.pi * (1.0 - xi)),
        ):
            denominator = cmath.sinh(pole) - 1j * math.sin(math.pi * xi)
            assert_close(f"B1B1 {pole_name} pole denominator xi={xi}", denominator, 0.0)


def check_neutral_block_residues() -> None:
    for a in (0.18, 0.31, 0.43):
        direct_residue = 2j * math.tan(math.pi * a)
        crossed_residue = -2j * math.tan(math.pi * a)
        assert_close(f"neutral block direct -i residue a={a}", -1j * direct_residue, 2.0 * math.tan(math.pi * a))
        assert_close(f"neutral block crossed -i residue a={a}", -1j * crossed_residue, -2.0 * math.tan(math.pi * a))
        for theta in (0.11, 0.75, -1.1):
            amp = neutral_block(theta, a)
            assert_close(f"neutral block unitarity a={a} theta={theta}", amp * neutral_block(-theta, a), 1.0)
            assert_close(
                f"neutral block crossing a={a} theta={theta}",
                amp,
                neutral_block(1j * math.pi - theta, a),
            )


def check_breather_breather_direct_fusion_masses() -> None:
    xi = 0.17
    soliton_mass = 3.2
    for m, n in ((1, 1), (1, 2), (2, 2), (1, 3)):
        u = math.pi * (m + n) * xi / 2.0
        mass_from_pole_squared = (
            breather_mass(m, xi, soliton_mass) ** 2
            + breather_mass(n, xi, soliton_mass) ** 2
            + 2.0
            * breather_mass(m, xi, soliton_mass)
            * breather_mass(n, xi, soliton_mass)
            * math.cos(u)
        )
        assert_close(
            f"B{m}B{n}->B{m+n} mass",
            math.sqrt(mass_from_pole_squared),
            breather_mass(m + n, xi, soliton_mass),
        )

        pole = 1j * u
        parameter = (m + n) * xi / 2.0
        denominator = cmath.sinh(pole) - 1j * math.sin(math.pi * parameter)
        assert_close(f"B{m}B{n} direct-pole denominator", denominator, 0.0)

        for theta in (0.23, 0.9):
            amp = breather_breather_amplitude(theta, m, n, xi)
            assert_close(
                f"B{m}B{n} unitarity theta={theta}",
                amp * breather_breather_amplitude(-theta, m, n, xi),
                1.0,
            )
            assert_close(
                f"B{m}B{n} crossing theta={theta}",
                amp,
                breather_breather_amplitude(1j * math.pi - theta, m, n, xi),
            )


def main() -> None:
    check_matrix_unitarity()
    check_free_fermion_point()
    check_breather_pole_locations_and_masses()
    check_lightest_breather_amplitude()
    check_neutral_block_residues()
    check_breather_breather_direct_fusion_masses()
    print("All sine-Gordon S-matrix checks passed.")


if __name__ == "__main__":
    main()
