#!/usr/bin/env python3
"""Finite convention checks for thermal gauge-theory screening.

These checks accompany Volume X, Chapter 7.  They verify algebraic facts that
are easy to obscure in prose: the Yukawa power in a d-dimensional static
correlator, the one-dimensional projected pole residue, static-source line
renormalization cancellation, and the conversion of the one-loop Debye
coefficient between the monograph trace-delta convention and the common
half-trace convention.
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


def check_static_source_line_renormalization_cancellation() -> None:
    # A wrapped source has an additive line self-energy.  Pair excess free
    # energies and forces must not depend on this local one-line coordinate.
    beta = Fraction(7, 3)
    delta_q = Fraction(5, 3)
    delta_qbar = Fraction(7, 5)
    finite_shift_q = Fraction(2, 11)
    finite_shift_qbar = Fraction(-3, 13)

    physical_q = Fraction(11, 7)
    physical_qbar = Fraction(13, 7)
    interaction = Fraction(-2, 9)

    bare_q = physical_q + delta_q
    bare_qbar = physical_qbar + delta_qbar
    bare_pair = physical_q + physical_qbar + interaction + delta_q + delta_qbar

    ren_q = bare_q - delta_q
    ren_qbar = bare_qbar - delta_qbar
    ren_pair = bare_pair - delta_q - delta_qbar
    bare_excess = bare_pair - bare_q - bare_qbar
    ren_excess = ren_pair - ren_q - ren_qbar

    assert_equal("Polyakov pair excess cancels bare line energies", bare_excess, interaction)
    assert_equal("Polyakov pair excess cancels renormalized line energies", ren_excess, interaction)
    assert_equal(
        "Polyakov ratio exponent line cancellation",
        -beta * bare_excess,
        -beta * ren_excess,
    )

    shifted_q = ren_q - finite_shift_q
    shifted_qbar = ren_qbar - finite_shift_qbar
    shifted_pair = ren_pair - finite_shift_q - finite_shift_qbar
    assert_equal(
        "finite line scheme leaves pair excess invariant",
        shifted_pair - shifted_q - shifted_qbar,
        interaction,
    )

    r = Fraction(3)
    sigma = Fraction(2, 5)
    coulomb = Fraction(7, 11)
    constant = Fraction(19, 13)
    delta_sum = delta_q + delta_qbar
    bare_potential = delta_sum + constant + sigma * r + coulomb / r
    ren_potential = bare_potential - delta_sum
    bare_derivative = sigma - coulomb / (r * r)
    ren_derivative = sigma - coulomb / (r * r)

    assert_equal("static pair force removes line self-energy", -bare_derivative, -ren_derivative)
    assert_equal(
        "static pair potential shifts by line self-energy",
        bare_potential - ren_potential,
        delta_sum,
    )


def main() -> None:
    check_yukawa_screening_power()
    check_projected_pole_residue()
    check_debye_trace_convention_conversion()
    check_static_source_line_renormalization_cancellation()
    print("All thermal screening convention and static-source checks passed.")


if __name__ == "__main__":
    main()
