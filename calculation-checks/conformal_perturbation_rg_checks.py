#!/usr/bin/env python3
"""Finite checks for two-dimensional conformal-perturbation RG conventions."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def local_shell_cutoff_power(
    output_dimension: Fraction,
    left_dimension: Fraction,
    right_dimension: Fraction,
) -> Fraction:
    coupling_power = (left_dimension - 2) + (right_dimension - 2)
    radial_power = 2 + output_dimension - left_dimension - right_dimension
    return coupling_power + radial_power


def shell_pi_units() -> Fraction:
    second_order_factor = Fraction(1, 2)
    angular_factor_in_pi_units = Fraction(2)
    return second_order_factor * angular_factor_in_pi_units


def length_beta_quadratic_pi_units(ope_coefficient: Fraction) -> Fraction:
    return -shell_pi_units() * ope_coefficient


def energy_beta_quadratic_pi_units(ope_coefficient: Fraction) -> Fraction:
    return -length_beta_quadratic_pi_units(ope_coefficient)


def quadratic_scheme_shift(
    output_y: Fraction,
    left_y: Fraction,
    right_y: Fraction,
    redefinition_coefficient: Fraction,
) -> Fraction:
    return (left_y + right_y - output_y) * redefinition_coefficient


def main() -> None:
    sample_dimensions = [
        (Fraction(2), Fraction(2), Fraction(2)),
        (Fraction(3, 2), Fraction(7, 5), Fraction(11, 6)),
        (Fraction(5, 3), Fraction(4, 3), Fraction(6, 5)),
    ]
    for output_dimension, left_dimension, right_dimension in sample_dimensions:
        assert_equal(
            "annular OPE cutoff power matches output coupling dimension",
            local_shell_cutoff_power(output_dimension, left_dimension, right_dimension),
            output_dimension - 2,
        )

    assert_equal("second-order annulus coefficient in pi units", shell_pi_units(), 1)
    assert_equal(
        "length beta has the Wilsonian OPE sign",
        length_beta_quadratic_pi_units(Fraction(5, 7)),
        Fraction(-5, 7),
    )
    assert_equal(
        "energy beta has the opposite OPE sign",
        energy_beta_quadratic_pi_units(Fraction(5, 7)),
        Fraction(5, 7),
    )

    assert_equal(
        "marginal quadratic channel is scheme invariant",
        quadratic_scheme_shift(Fraction(0), Fraction(0), Fraction(0), Fraction(3, 5)),
        0,
    )
    assert_equal(
        "resonant relevant channel is scheme invariant",
        quadratic_scheme_shift(Fraction(3, 2), Fraction(1), Fraction(1, 2), Fraction(4, 9)),
        0,
    )
    assert_equal(
        "nonresonant quadratic channel shift",
        quadratic_scheme_shift(Fraction(1, 3), Fraction(1), Fraction(2, 5), Fraction(6, 7)),
        Fraction(32, 35),
    )

    bare_quadratic = Fraction(-8, 15)
    denominator = Fraction(1) + Fraction(2, 5) - Fraction(1, 3)
    counterterm = -bare_quadratic / denominator
    assert_equal(
        "nonresonant finite counterterm cancels quadratic coefficient",
        bare_quadratic
        + quadratic_scheme_shift(Fraction(1, 3), Fraction(1), Fraction(2, 5), counterterm),
        0,
    )

    print("All conformal-perturbation RG checks passed.")


if __name__ == "__main__":
    main()
