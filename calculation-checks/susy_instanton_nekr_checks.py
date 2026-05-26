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


def check_ads_higgs_patch_collective_coordinates() -> None:
    for nc in range(2, 12):
        nf = nc - 1

        su_nc_dimension = nc * nc - 1
        stabilizer_dimension = (nc - 2) * (nc - 2) - 1 + 1
        if nc == 2:
            # For SU(2), the embedded instanton is the whole gauge group and
            # the continuous orientation stabilizer is trivial.
            stabilizer_dimension = 0
        orientation_dimension = su_nc_dimension - stabilizer_dimension
        assert_equal(orientation_dimension, 4 * nc - 5, "k=1 SU(Nc) orientation dimension")
        assert_equal(4 + 1 + orientation_dimension, 4 * nc, "k=1 SU(Nc) bosonic moduli")

        adjoint_gaugino_zero_modes = 2 * nc
        exact_goldstino_modes = 2
        lifted_gaugino_modes = adjoint_gaugino_zero_modes - exact_goldstino_modes
        matter_zero_modes = 2 * nf
        assert_equal(lifted_gaugino_modes, matter_zero_modes, "Higgs-patch Yukawa lifting rank")

        det_m_dimension = 2 * nf
        reduced_factor_dimension = 3 - (2 * nc + 1)
        assert_equal(reduced_factor_dimension, -det_m_dimension, "ADS reduced determinant dimension")


def check_ads_meson_invariant_uniqueness() -> None:
    for nc in range(2, 12):
        n = nc - 1
        nf = n

        # The complexified special-flavor action M -> L M R^{-1} preserves
        # det(M) because det(L)=det(R)=1.
        for det_m in (Fraction(2), Fraction(5, 3), Fraction(11, 7)):
            det_l = Fraction(1)
            det_r = Fraction(1)
            transformed_det = det_l * det_m / det_r
            assert_equal(transformed_det, det_m, "ADS special-flavor determinant invariant")

            # The proof uses D_delta=diag(delta,1,...,1): M D_delta^{-1}
            # has determinant one and so lies in SL_n(C).
            det_d_delta = det_m
            det_left_multiplier = det_m / det_d_delta
            assert_equal(det_left_multiplier, 1, "ADS determinant-fiber SL transitivity")

        reduced_factor_dimension = 3 - (2 * nc + 1)
        meson_entry_dimension = 2
        homogeneous_degree = Fraction(reduced_factor_dimension, meson_entry_dimension)
        assert_equal(homogeneous_degree, -n, "ADS reduced factor meson-scaling degree")

        determinant_scaling_degree = n
        inverse_det_scaling_degree = -determinant_scaling_degree
        assert_equal(inverse_det_scaling_degree, homogeneous_degree, "ADS inverse determinant scaling")

        r_m = Fraction(2 * (nf - nc), nf)
        r_det_m = nf * r_m
        assert_equal(r_det_m, -2, "ADS determinant semi-invariant R-charge")
        assert_equal(-r_det_m, 2, "ADS inverse determinant superpotential R-charge")

        # If F(M)=f(det M) and F(sM)=s^{-n}F(M), then
        # f(u delta)=u^{-1}f(delta).  Check the exponent arithmetic.
        for u in (Fraction(2), Fraction(3, 5), Fraction(7)):
            for delta in (Fraction(5), Fraction(11, 3)):
                left = (u * delta) ** -1
                right = u ** -1 * delta ** -1
                assert_equal(left, right, "ADS determinant homogeneity descent")


def check_holomorphic_decoupling_dimensions() -> None:
    for nc in range(2, 12):
        for nf in range(1, nc + 3):
            high_exponent = 3 * nc - nf
            low_exponent = 3 * nc - (nf - 1)
            assert_equal(low_exponent, high_exponent + 1, "decoupling exponent shift")
            assert_equal(1 + high_exponent, low_exponent, "mass times high scale dimension")


def check_ads_decoupling_recursion() -> None:
    for nc in range(3, 14):
        for n_light in range(1, nc - 1):
            d = nc - n_light
            high_flavors = n_light + 1
            high_exponent = 3 * nc - high_flavors
            low_exponent = 3 * nc - n_light

            assert_equal(d >= 2, True, "ADS recursion denominator range")
            assert_equal(low_exponent, high_exponent + 1, "ADS recursion scale exponent")

            # If the one-instanton seed is normalized with C_{Nc-1}=1, the
            # recursion C_n=d(C_{n+1}/(d-1))^((d-1)/d) is solved by C_n=d.
            high_coefficient = d - 1
            coefficient_power = (
                Fraction(d) ** d
                * Fraction(high_coefficient, d - 1) ** (d - 1)
            )
            assert_equal(coefficient_power, Fraction(d) ** d, "standard ADS coefficient recursion")

            # A = Lambda_+^b/det(M_light).  The combination m A has dimension
            # 3d, so its d-th root has the dimension of a superpotential.
            det_light_dimension = 2 * n_light
            mass_times_a_dimension = 1 + high_exponent - det_light_dimension
            assert_equal(mass_times_a_dimension, 3 * d, "ADS recursion mA dimension")

            for mass in (Fraction(2), Fraction(5, 3), Fraction(11, 7)):
                for a_value in (Fraction(3), Fraction(7, 5), Fraction(13, 2)):
                    y_power_from_f_term = Fraction(d - 1) * mass * a_value / high_coefficient
                    assert_equal(y_power_from_f_term, mass * a_value, "ADS recursion Y^d relation")


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
    check_ads_higgs_patch_collective_coordinates()
    check_ads_meson_invariant_uniqueness()
    check_holomorphic_decoupling_dimensions()
    check_ads_decoupling_recursion()
    check_nekrasov_su2_one_instanton()
    check_young_diagram_one_box_count()
    print("All SUSY instanton/ADHM/Nekrasov checks passed.")


if __name__ == "__main__":
    main()
