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


def spinc_tensor_c1(c1_value: int, line_c1: int) -> int:
    return c1_value + 2 * line_c1


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


def check_spinc_characteristic_lift_bookkeeping() -> None:
    # CP^2: characteristic classes are odd multiples of the hyperplane class.
    base_c1 = 3
    for line_c1 in range(-3, 4):
        shifted = spinc_tensor_c1(base_c1, line_c1)
        assert_equal(shifted % 2, 1, "CP2 Spin^c characteristic parity")

    # K3 is spin; even line twists keep c1 even and the untwisted structure has
    # c1 = 0.
    for line_c1 in range(-3, 4):
        shifted = spinc_tensor_c1(0, line_c1)
        assert_equal(shifted % 2, 0, "K3 Spin^c characteristic parity")


def check_sw_simple_type_examples() -> None:
    # K3.
    chi_k3 = 24
    sigma_k3 = -16
    assert_equal(2 * chi_k3 + 3 * sigma_k3, 0, "K3 simple-type target")
    assert_equal(
        sw_expected_dimension(0, chi_k3, sigma_k3),
        Fraction(0),
        "K3 zero basic class dimension",
    )

    # E(n): chi = 12 n, sigma = -8 n, fiber square zero.  The classes
    # (n - 2 - 2 j) F therefore all have zero square and dimension zero.
    for n in range(2, 8):
        chi_en = 12 * n
        sigma_en = -8 * n
        assert_equal(2 * chi_en + 3 * sigma_en, 0, "E(n) simple-type target")
        for j in range(n - 1):
            fiber_multiple = n - 2 - 2 * j
            c1_square = 0  # (fiber_multiple * F)^2 because F^2 = 0.
            assert_equal(
                sw_expected_dimension(c1_square, chi_en, sigma_en),
                Fraction(0),
                "E(n) fiber basic-class dimension",
            )


def check_blowup_simple_type_square_shift() -> None:
    examples = [
        (24, -16),  # K3
        (48, -32),  # E(4), fiber basic classes square zero
        (7, -3),
    ]
    for chi_value, sigma_value in examples:
        k_square = 2 * chi_value + 3 * sigma_value
        new_chi = chi_value + 1
        new_sigma = sigma_value - 1
        assert_equal(
            k_square - 1,
            2 * new_chi + 3 * new_sigma,
            "blow-up simple-type square shift",
        )


def check_elliptic_surface_binomial_coefficients() -> None:
    # (e^F - e^{-F})^(n-2) gives classes (n-2-2j)F with coefficients
    # (-1)^j binomial(n-2, j).  Check the exponent pattern and coefficient sum.
    for n in range(2, 8):
        degree = n - 2
        exponents = [degree - 2 * j for j in range(degree + 1)]
        expected = list(range(degree, -degree - 1, -2))
        assert_equal(exponents, expected, "E(n) exponent ladder")
        coeff_sum = sum(((-1) ** j) * binomial(degree, j) for j in range(degree + 1))
        target = 1 if degree == 0 else 0
        assert_equal(coeff_sum, target, "E(n) binomial alternating sum")


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for j in range(1, k + 1):
        numerator *= n + 1 - j
        denominator *= j
    return numerator // denominator


def check_furuta_examples() -> None:
    # K3 saturates Furuta's 10/8+2 inequality.
    b2_k3 = 22
    sigma_k3 = -16
    rhs_units = Fraction(10, 8) * abs(sigma_k3) + 2
    assert_equal(Fraction(b2_k3), rhs_units, "K3 Furuta saturation")

    # Spin elliptic surfaces E(2m) obey the inequality; this is only an
    # arithmetic check of the topological numbers used in the chapter.
    for m in range(1, 5):
        n = 2 * m
        b2 = 12 * n - 2
        sigma_value = -8 * n
        if Fraction(b2) < Fraction(10, 8) * abs(sigma_value) + 2:
            raise AssertionError("E(2m) violates Furuta arithmetic check")


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
    check_spinc_characteristic_lift_bookkeeping()
    check_sw_simple_type_examples()
    check_blowup_simple_type_square_shift()
    check_elliptic_surface_binomial_coefficients()
    check_furuta_examples()
    check_trace_delta_action_normalization()
    print("Donaldson-Witten and Seiberg-Witten comparison checks passed.")


if __name__ == "__main__":
    main()
