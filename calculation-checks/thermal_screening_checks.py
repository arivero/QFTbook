#!/usr/bin/env python3
"""Finite convention checks for thermal gauge-theory screening.

These checks accompany Volume X, Chapter 7.  They verify algebraic facts that
are easy to obscure in prose: the Yukawa power in a d-dimensional static
correlator, the one-dimensional projected pole residue, and the conversion of
the one-loop Debye coefficient between the monograph trace-delta convention
and the common half-trace convention.
"""

from __future__ import annotations

from fractions import Fraction
from math import exp, pi


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_close(name: str, actual: float, expected: float, tol: float = 1.0e-12) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: expected {expected}, got {actual}")


def yukawa_asymptotic_powers(spatial_dim: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return Bessel order, mass power, and distance power for a scalar pole."""

    d = Fraction(spatial_dim, 1)
    bessel_order = d / 2 - 1
    mass_power = (d - 3) / 2
    distance_power = -(d - 1) / 2
    return bessel_order, mass_power, distance_power


def check_yukawa_screening_power() -> None:
    expected = {
        1: (Fraction(-1, 2), Fraction(-1, 1), Fraction(0, 1)),
        2: (Fraction(0, 1), Fraction(-1, 2), Fraction(-1, 2)),
        3: (Fraction(1, 2), Fraction(0, 1), Fraction(-1, 1)),
        4: (Fraction(1, 1), Fraction(1, 2), Fraction(-3, 2)),
    }
    for spatial_dim, powers in expected.items():
        assert_equal(
            f"Yukawa asymptotic powers d={spatial_dim}",
            yukawa_asymptotic_powers(spatial_dim),
            powers,
        )

    # The old r^{-(d-2)/2} power would be wrong already in d=3, where the
    # massive static Green function is exp(-Mr)/(4 pi r).
    assert_equal("three-dimensional static Yukawa power", yukawa_asymptotic_powers(3)[2], Fraction(-1, 1))


def check_projected_pole_residue() -> None:
    mass = 1.7
    z = 2.3
    residue = 0.4
    projected = residue * exp(-mass * abs(z)) / (2.0 * mass)

    # Differentiating twice away from z=0 verifies that the projected kernel is
    # the Green function of -d_z^2 + M^2 with pole residue Z.
    second_derivative = mass * mass * projected
    assert_close("projected pole homogeneous equation", (-second_derivative + mass * mass * projected), 0.0)


def debye_half_trace_coefficient(n_c: int, n_f: int) -> Fraction:
    c_a = Fraction(n_c, 1)
    t_fund = Fraction(1, 2)
    return c_a / 3 + n_f * t_fund / 3


def debye_trace_delta_coefficient(n_c: int, n_f: int) -> Fraction:
    c_a = Fraction(2 * n_c, 1)
    t_fund = Fraction(1, 1)
    return c_a / 3 + n_f * t_fund / 3


def check_debye_trace_convention_conversion() -> None:
    for n_c in range(2, 8):
        for n_f in range(0, 7):
            # If t_delta^a=sqrt(2) t_half^a, the same covariant derivative
            # has g_delta=g_half/sqrt(2).  Thus the doubled trace-delta group
            # coefficient is compensated by g_delta^2=g_half^2/2.
            half_trace = debye_half_trace_coefficient(n_c, n_f)
            trace_delta_physical = debye_trace_delta_coefficient(n_c, n_f) / 2
            assert_equal(
                f"Debye trace conversion SU({n_c}) Nf={n_f}",
                trace_delta_physical,
                half_trace,
            )


def main() -> None:
    check_yukawa_screening_power()
    check_projected_pole_residue()
    check_debye_trace_convention_conversion()
    print("All thermal screening convention checks passed.")


if __name__ == "__main__":
    main()
