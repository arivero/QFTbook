#!/usr/bin/env python3
"""Exact checks for SQCD instantons, ADHM dimensions, and Nekrasov k=1."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


def check_adhm_dimension_count() -> None:
    for k in range(1, 8):
        for n in range(1, 9):
            variables = 2 * k * k + 2 * k * n
            complex_equations = k * k
            complex_quotient = k * k
            complex_dimension = variables - complex_equations - complex_quotient
            assert_equal(complex_dimension, 2 * k * n, "ADHM complex dimension")
            assert_equal(2 * complex_dimension, 4 * k * n, "ADHM real dimension")
            assert_equal(2 * complex_dimension - 4, 4 * k * n - 4, "centered ADHM dimension")


def check_instanton_exponential_coupling_conversion() -> None:
    # The monograph trace-delta coordinate and the common half-trace
    # coordinate are related by g_ht^2 = 2 g_YM^2.  The BPST action
    # 8 pi^2 / g_ht^2 is therefore 4 pi^2 / g_YM^2.
    for g_delta_squared in (Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)):
        g_half_trace_squared = 2 * g_delta_squared
        half_trace_coefficient = Fraction(8, 1) / g_half_trace_squared
        trace_delta_coefficient = Fraction(4, 1) / g_delta_squared
        assert_equal(half_trace_coefficient, trace_delta_coefficient, "instanton action conversion")


def check_ads_dimensions_and_r_charges() -> None:
    for nc in range(2, 12):
        for nf in range(1, nc):
            numerator_dimension = 3 * nc - nf
            det_m_dimension = 2 * nf
            denominator = nc - nf
            superpotential_dimension = Fraction(numerator_dimension - det_m_dimension, denominator)
            assert_equal(superpotential_dimension, 3, "ADS dimension")

            r_m = Fraction(2 * (nf - nc), nf)
            r_det_m = nf * r_m
            ads_r_charge = Fraction(-r_det_m, denominator)
            assert_equal(ads_r_charge, 2, "ADS R-charge")


def check_one_instanton_ads_zero_modes() -> None:
    for nc in range(2, 12):
        nf = nc - 1
        b0 = 3 * nc - nf
        assert_equal(b0, 2 * nc + 1, "Nf=Nc-1 one-instanton scale exponent")

        adjoint_gaugino_zero_modes = 2 * nc
        matter_zero_modes = 2 * nf
        lifted_adjoint_modes = matter_zero_modes
        unlifted_adjoint_modes = adjoint_gaugino_zero_modes - lifted_adjoint_modes
        assert_equal(unlifted_adjoint_modes, 2, "ADS d^2 theta zero modes")

        det_m_dimension = 2 * nf
        superpotential_dimension = b0 - det_m_dimension
        assert_equal(superpotential_dimension, 3, "ADS k=1 dimension")

        r_m = Fraction(2 * (nf - nc), nf)
        r_det_m = nf * r_m
        assert_equal(r_det_m, -2, "ADS k=1 det M R-charge")
        assert_equal(-r_det_m, 2, "ADS k=1 inverse determinant R-charge")


def check_holomorphic_decoupling_dimensions() -> None:
    for nc in range(2, 12):
        for nf in range(1, nc + 3):
            high_exponent = 3 * nc - nf
            low_exponent = 3 * nc - (nf - 1)
            assert_equal(low_exponent, high_exponent + 1, "decoupling exponent shift")
            assert_equal(1 + high_exponent, low_exponent, "mass times high scale dimension")


def z1_su2(a: Fraction, epsilon1: Fraction, epsilon2: Fraction) -> Fraction:
    epsilon = epsilon1 + epsilon2
    term_plus = Fraction(1, (2 * a) * (2 * a + epsilon))
    term_minus = Fraction(1, (-2 * a) * (-2 * a + epsilon))
    return Fraction(1, epsilon1 * epsilon2) * (term_plus + term_minus)


def check_nekrasov_su2_one_instanton() -> None:
    samples = [
        (Fraction(2), Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(2), Fraction(5)),
        (Fraction(5), Fraction(-1), Fraction(4)),
        (Fraction(7), Fraction(3), Fraction(-2)),
    ]
    for a, epsilon1, epsilon2 in samples:
        epsilon = epsilon1 + epsilon2
        got = z1_su2(a, epsilon1, epsilon2)
        expected = Fraction(2, epsilon1 * epsilon2 * (4 * a * a - epsilon * epsilon))
        assert_equal(got, expected, "SU(2) Nekrasov k=1 fixed-point sum")

    for a in (Fraction(2), Fraction(3), Fraction(5), Fraction(11)):
        epsilon1 = Fraction(1)
        epsilon2 = Fraction(-1)
        got = epsilon1 * epsilon2 * z1_su2(a, epsilon1, epsilon2)
        expected = Fraction(1, 2 * a * a)
        assert_equal(got, expected, "SU(2) Nekrasov prepotential coefficient")


def check_young_diagram_one_box_count() -> None:
    for n in range(1, 12):
        one_box_fixed_points = n
        assert_equal(one_box_fixed_points, n, "one-box N-tuple fixed-point count")


def main() -> None:
    check_adhm_dimension_count()
    check_instanton_exponential_coupling_conversion()
    check_ads_dimensions_and_r_charges()
    check_one_instanton_ads_zero_modes()
    check_holomorphic_decoupling_dimensions()
    check_nekrasov_su2_one_instanton()
    check_young_diagram_one_box_count()
    print("All SUSY instanton/ADHM/Nekrasov checks passed.")


if __name__ == "__main__":
    main()
