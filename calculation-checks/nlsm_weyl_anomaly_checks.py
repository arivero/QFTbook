#!/usr/bin/env python3
"""Coefficient checks for one-loop NLSM Weyl-anomaly bookkeeping."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def check_h_squared_variation_coefficients() -> None:
    h_squared_lagrangian = Fraction(-1, 12)

    # H_{abc} H^{abc} contains three inverse metrics.
    metric_variation_factor = 3
    metric_equation_coefficient = h_squared_lagrangian * metric_variation_factor
    assert_equal(
        "metric variation coefficient of -H^2/12",
        metric_equation_coefficient,
        Fraction(-1, 4),
    )

    # delta(H^2)=2 H delta H and delta H=d delta B has three antisymmetric
    # placements.  Thus -H^2/12 varies as -1/2 H^{ijk} nabla_i delta B_jk.
    h_variation_factor = 2 * 3
    before_parts = h_squared_lagrangian * h_variation_factor
    assert_equal("B variation before integration by parts", before_parts, Fraction(-1, 2))

    after_parts = -before_parts
    beta_divergence_coefficient = -after_parts
    dilaton_gradient_coefficient = beta_divergence_coefficient * Fraction(-2)
    assert_equal("B beta divergence coefficient", beta_divergence_coefficient, Fraction(-1, 2))
    assert_equal("B beta dilaton-gradient coefficient", dilaton_gradient_coefficient, 1)


def check_linear_dilaton_constant() -> None:
    for dimension in range(2, 27):
        alpha_prime_v_squared = Fraction(26 - dimension, 6)
        scalar_beta_constant = Fraction(dimension - 26, 6) + alpha_prime_v_squared
        matter_central_charge = dimension + 6 * alpha_prime_v_squared
        assert_equal(f"linear dilaton beta constant in D={dimension}", scalar_beta_constant, 0)
        assert_equal(f"linear dilaton matter central charge in D={dimension}", matter_central_charge, 26)


def check_heterotic_bianchi_coefficients() -> None:
    green_schwarz_coefficient = Fraction(1, 4)

    tr_r_wedge_r = Fraction(7, 3)
    tr_f_wedge_f = tr_r_wedge_r
    standard_embedding_rhs = green_schwarz_coefficient * (tr_r_wedge_r - tr_f_wedge_f)
    assert_equal("standard embedding cancels dH source", standard_embedding_rhs, 0)

    tr_f_wedge_f = Fraction(-5, 2)
    rhs = green_schwarz_coefficient * (tr_r_wedge_r - tr_f_wedge_f)
    expected = Fraction(1, 4) * (Fraction(7, 3) + Fraction(5, 2))
    assert_equal("Green-Schwarz one-quarter normalization", rhs, expected)


def check_heterotic_gauge_dilaton_redundant_direction() -> None:
    # The hatted gauge equation is -1/2(D.F + H.F/2 - 2 grad Phi . F).
    overall = Fraction(-1, 2)
    assert_equal("heterotic D.F coefficient", overall, Fraction(-1, 2))
    assert_equal("heterotic H.F coefficient", overall * Fraction(1, 2), Fraction(-1, 4))
    assert_equal("heterotic dilaton-gradient coefficient", overall * Fraction(-2), 1)


def main() -> None:
    check_h_squared_variation_coefficients()
    check_linear_dilaton_constant()
    check_heterotic_bianchi_coefficients()
    check_heterotic_gauge_dilaton_redundant_direction()
    print("All NLSM Weyl-anomaly coefficient checks passed.")


if __name__ == "__main__":
    main()
