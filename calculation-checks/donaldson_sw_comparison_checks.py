#!/usr/bin/env python3
"""Finite checks for Donaldson-Witten and Seiberg-Witten comparison formulas."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def chi(b1: int, b2_plus: int, b2_minus: int) -> int:
    return 2 - 2 * b1 + b2_plus + b2_minus


def signature(b2_plus: int, b2_minus: int) -> int:
    return b2_plus - b2_minus


def asd_virtual_dimension(k: int, b1: int, b2_plus: int) -> int:
    return 8 * k - 3 * (1 - b1 + b2_plus)


def asd_index_from_pontryagin(
    p1_ad: int, chi_value: int, sigma_value: int
) -> Fraction:
    """Index of d_A^* plus d_A^+ for an SU(2) bundle."""

    return -2 * p1_ad - Fraction(3, 2) * (chi_value + sigma_value)


def sw_expected_dimension(c1_square: int, chi_value: int, sigma_value: int) -> Fraction:
    return Fraction(c1_square - (2 * chi_value + 3 * sigma_value), 4)


def sw_index_from_dirac_and_gauge(
    c1_square: int, b1: int, b2_plus: int, sigma_value: int
) -> Fraction:
    real_dirac_index = Fraction(c1_square - sigma_value, 4)
    abelian_gauge_index = -(1 - b1 + b2_plus)
    return real_dirac_index + abelian_gauge_index


def donaldson_descent_degree(cycle_dimension: int) -> int:
    return 4 - cycle_dimension


def check_asd_index_formula() -> None:
    examples = [
        # k, b1, b2_plus, b2_minus
        (1, 0, 1, 0),   # CP^2 topology
        (2, 0, 3, 19),  # K3 topology
        (3, 1, 2, 5),
    ]
    for k, b1, b2_plus, b2_minus in examples:
        chi_value = chi(b1, b2_plus, b2_minus)
        sigma_value = signature(b2_plus, b2_minus)
        p1_ad = -4 * k
        index_value = asd_index_from_pontryagin(p1_ad, chi_value, sigma_value)
        closed_form = asd_virtual_dimension(k, b1, b2_plus)
        assert_equal(index_value, closed_form, "ASD index closed form")


def check_sw_index_formula() -> None:
    examples = [
        # b1, b2_plus, b2_minus, c1_square, expected
        (0, 1, 0, 9, Fraction(0)),     # CP^2, c1 = 3H
        (0, 1, 0, 1, Fraction(-2)),    # CP^2, c1 = H
        (0, 3, 19, 0, Fraction(0)),    # K3, c1 = 0
        (1, 2, 5, -3, None),
    ]
    for b1, b2_plus, b2_minus, c1_square, expected in examples:
        chi_value = chi(b1, b2_plus, b2_minus)
        sigma_value = signature(b2_plus, b2_minus)
        formula = sw_expected_dimension(c1_square, chi_value, sigma_value)
        index_sum = sw_index_from_dirac_and_gauge(
            c1_square, b1, b2_plus, sigma_value
        )
        assert_equal(formula, index_sum, "SW index decomposition")
        if expected is not None:
            assert_equal(formula, expected, "SW example dimension")


def check_topological_identity_in_sw_dimension() -> None:
    for b1 in range(4):
        for b2_plus in range(5):
            for b2_minus in range(5):
                chi_value = chi(b1, b2_plus, b2_minus)
                sigma_value = signature(b2_plus, b2_minus)
                lhs = 2 * chi_value + 3 * sigma_value
                rhs = 4 * (1 - b1 + b2_plus) + sigma_value
                assert_equal(lhs, rhs, "2 chi plus 3 sigma identity")


def check_donaldson_degree_bookkeeping() -> None:
    assert_equal(donaldson_descent_degree(0), 4, "point insertion degree")
    assert_equal(donaldson_descent_degree(1), 3, "loop insertion degree")
    assert_equal(donaldson_descent_degree(2), 2, "surface insertion degree")
    assert_equal(donaldson_descent_degree(3), 1, "three-cycle insertion degree")
    assert_equal(donaldson_descent_degree(4), 0, "fundamental-cycle degree")

    # CP^2 topology, k = 1: virtual dimension is 2, so one surface insertion
    # has the matching Donaldson degree.
    dimension = asd_virtual_dimension(k=1, b1=0, b2_plus=1)
    assert_equal(dimension, 2, "CP^2 k=1 ASD virtual dimension")
    assert_equal(donaldson_descent_degree(2), dimension, "surface degree match")


def check_trace_delta_action_normalization() -> None:
    # The BPST normalization used elsewhere in the repository gives
    # integral tr_delta(F wedge *F) = 8 pi^2 for k = 1.  With the monograph
    # action (2 g_YM^2)^(-1) integral tr(F wedge *F), this is 4 pi^2/g_YM^2.
    form_norm_units = 8
    action_units = Fraction(form_norm_units, 2)
    assert_equal(action_units, 4, "trace-delta instanton action coefficient")


def main() -> None:
    check_asd_index_formula()
    check_sw_index_formula()
    check_topological_identity_in_sw_dimension()
    check_donaldson_degree_bookkeeping()
    check_trace_delta_action_normalization()
    print("Donaldson-Witten and Seiberg-Witten comparison checks passed.")


if __name__ == "__main__":
    main()
