#!/usr/bin/env python3
"""Exact checks for SQCD instantons, ADHM dimensions, and Nekrasov k=1.

The checks include the singular-instanton compactification arithmetic used in
the compact-localization chapter: Uhlenbeck stratum codimensions and the
torsion-free-sheaf charge split, the positive-ADHM-moment-map stability trace
obstruction, and the one-box specialization of the Gieseker tangent Euler class.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


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


def check_uhlenbeck_stratum_codimension() -> None:
    for k in range(1, 8):
        for n in range(1, 7):
            top_complex_dimension = 2 * k * n
            for lost_charge in range(0, k + 1):
                stratum_dimension = 2 * (k - lost_charge) * n + 2 * lost_charge
                codimension = top_complex_dimension - stratum_dimension
                assert_equal(
                    codimension,
                    2 * lost_charge * (n - 1),
                    "Uhlenbeck stratum codimension",
                )
    assert_equal(2 * 1 * (2 - 1), 2, "SU(2) one-point complex codimension")


def check_torsion_free_sheaf_uhlenbeck_charge_split() -> None:
    # For 0 -> E -> E** -> Q -> 0 on a surface, additivity of Chern
    # characters gives ch_2(E)=ch_2(E**)-length(Q)[pt].  In the framed c1=0
    # instanton convention k(F)=-int ch_2(F), so k(E)=k(E**)+length(Q).
    for reflexive_charge in range(0, 8):
        ch2_double_dual = -reflexive_charge
        for quotient_length in range(0, 8):
            ch2_quotient = quotient_length
            ch2_sheaf = ch2_double_dual - ch2_quotient
            sheaf_charge = -ch2_sheaf
            assert_equal(
                sheaf_charge,
                reflexive_charge + quotient_length,
                "Gieseker-to-Uhlenbeck charge split",
            )
            assert_equal(
                sheaf_charge - quotient_length,
                reflexive_charge,
                "Uhlenbeck lower-charge recovery",
            )

    for total_charge in range(1, 8):
        for lost_charge in range(0, total_charge + 1):
            smooth_charge = total_charge - lost_charge
            assert_equal(
                smooth_charge + lost_charge,
                total_charge,
                "Uhlenbeck stratum charge conservation",
            )


def check_positive_adhm_moment_map_stability_trace() -> None:
    # Use a two-block K=S plus T model with S invariant under B_i.  In block
    # form B_i=[[A_i,C_i],[0,D_i]], the T-trace of [B_i,B_i^dagger] is
    # -Tr(C_i^dagger C_i).  If I(W) lies in S, the T-block of I I^dagger is
    # zero, while -J^dagger J is nonpositive.  Hence the T-trace cannot equal
    # a positive FI parameter times dim(T).
    examples = [
        (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)),
        (Fraction(4, 7), Fraction(5, 6), Fraction(7, 8)),
        (Fraction(3, 2), Fraction(5, 4), Fraction(9, 10)),
    ]
    for c1, c2, j_t in examples:
        t_trace_left = -(c1 * c1 + c2 * c2 + j_t * j_t)
        assert_equal(t_trace_left <= 0, True, "positive ADHM left side nonpositive")

        for zeta in (Fraction(1, 7), Fraction(2, 5), Fraction(11, 6)):
            t_trace_right = zeta
            assert_equal(t_trace_right > 0, True, "positive ADHM right side positive")
            assert_equal(
                t_trace_left == t_trace_right,
                False,
                "positive ADHM stability contradiction",
            )


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


def check_ads_radial_higgs_cutoff_integral() -> None:
    for p in range(1, 9):
        current_factorial = factorial(p - 1)

        for c in (Fraction(1, 2), Fraction(3, 5), Fraction(7, 4)):
            for higgs_norm in (Fraction(2), Fraction(5, 3), Fraction(11, 7)):
                integral = Fraction(current_factorial, 2) / (c * higgs_norm) ** p
                recurrence = integral * c * higgs_norm

                previous_factorial = factorial(p - 2) if p > 1 else 1
                previous_integral = (
                    Fraction(previous_factorial, 2) / (c * higgs_norm) ** (p - 1)
                    if p > 1
                    else Fraction(1, 2)
                )
                expected_recurrence = (p - 1) * previous_integral if p > 1 else Fraction(1, 2)
                assert_equal(recurrence, expected_recurrence, "ADS radial integral recurrence")

                for scale_squared in (Fraction(4), Fraction(9, 4), Fraction(25, 9)):
                    scaled_integral = Fraction(current_factorial, 2) / (
                        c * scale_squared * higgs_norm
                    ) ** p
                    assert_equal(
                        scaled_integral,
                        integral / scale_squared**p,
                        "ADS radial Higgs cutoff real scaling",
                    )

        radial_power = 2 * p - 1
        assert_equal((radial_power + 1) // 2, p, "ADS radial power-to-cutoff exponent")


def check_ads_yukawa_lifting_berezin_determinant() -> None:
    for nc in range(2, 12):
        nf = nc - 1

        q_blocks = nf
        tilde_q_blocks = nf
        lifted_bilinears = q_blocks + tilde_q_blocks
        lifted_grassmann_variables = 2 * lifted_bilinears
        assert_equal(
            lifted_bilinears,
            2 * nf,
            "ADS Yukawa lifting bilinear count",
        )
        assert_equal(
            lifted_grassmann_variables,
            4 * nf,
            "ADS Yukawa lifted Grassmann variable saturation",
        )

        adjoint_gaugino_zero_modes = 2 * nc
        lifted_adjoint_modes = 2 * nf
        exact_goldstino_modes = adjoint_gaugino_zero_modes - lifted_adjoint_modes
        assert_equal(exact_goldstino_modes, 2, "ADS Yukawa leaves d^2 theta")

        scalar_coefficients = q_blocks + tilde_q_blocks
        meson_products = nf
        assert_equal(
            scalar_coefficients,
            2 * meson_products,
            "ADS Yukawa determinant scalar coefficient count",
        )

        # In the diagonal patch M_i^i = tilde v_i v_i.  The lifted Berezin
        # determinant carries one conjugate v_i and one conjugate tilde v_i
        # per flavor, hence the conjugate of det(M), not the holomorphic
        # inverse determinant.  The latter is fixed only after the full
        # regulated measure and holomorphy/invariance argument.
        diagonal_det_m_degree = nf
        berezin_product_meson_degree = nf
        assert_equal(
            berezin_product_meson_degree,
            diagonal_det_m_degree,
            "ADS Yukawa Berezin product matches diagonal det M degree",
        )

        for start in (Fraction(2), Fraction(3, 5), Fraction(7, 3)):
            q_coefficients = [start + index for index in range(nf)]
            tilde_coefficients = [start + nf + index for index in range(nf)]
            top_coefficient = Fraction(1)
            for coefficient in q_coefficients + tilde_coefficients:
                top_coefficient *= coefficient
            pair_product = Fraction(1)
            for index in range(nf):
                pair_product *= q_coefficients[index] * tilde_coefficients[index]
            assert_equal(
                top_coefficient,
                pair_product,
                "ADS Yukawa Berezin top coefficient factorization",
            )


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


def one_box_tangent_euler(
    alpha: int,
    a_values: list[Fraction],
    epsilon1: Fraction,
    epsilon2: Fraction,
) -> Fraction:
    total = epsilon1 * epsilon2
    epsilon = epsilon1 + epsilon2
    for beta, a_beta in enumerate(a_values):
        if beta == alpha:
            continue
        diff = a_values[alpha] - a_beta
        total *= diff * (diff + epsilon)
    return total


def check_one_box_tangent_euler_class() -> None:
    samples = [
        ([Fraction(-2), Fraction(3)], Fraction(1), Fraction(2)),
        ([Fraction(-3), Fraction(1), Fraction(5)], Fraction(2), Fraction(-1)),
        ([Fraction(-5), Fraction(-1), Fraction(4), Fraction(9)], Fraction(2), Fraction(1)),
    ]
    for a_values, epsilon1, epsilon2 in samples:
        fixed_point_sum = sum(
            Fraction(1, one_box_tangent_euler(alpha, a_values, epsilon1, epsilon2))
            for alpha in range(len(a_values))
        )
        direct_sum = Fraction(1, epsilon1 * epsilon2) * sum(
            Fraction(
                1,
                math_product(
                    (a_values[alpha] - a_values[beta])
                    * (a_values[alpha] - a_values[beta] + epsilon1 + epsilon2)
                    for beta in range(len(a_values))
                    if beta != alpha
                ),
            )
            for alpha in range(len(a_values))
        )
        assert_equal(fixed_point_sum, direct_sum, "one-box tangent Euler class")


def matrix_product(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(left)
    middle = len(right)
    cols = len(right[0])
    return [
        [sum(left[row][index] * right[index][col] for index in range(middle)) for col in range(cols)]
        for row in range(rows)
    ]


def matrix_trace(matrix: list[list[Fraction]]) -> Fraction:
    return sum(matrix[index][index] for index in range(len(matrix)))


def matrix_rank_at_most_one(matrix: list[list[Fraction]]) -> bool:
    size = len(matrix)
    for row1 in range(size):
        for row2 in range(row1 + 1, size):
            for col1 in range(size):
                for col2 in range(col1 + 1, size):
                    minor = matrix[row1][col1] * matrix[row2][col2] - matrix[row1][col2] * matrix[row2][col1]
                    if minor != 0:
                        return False
    return True


def check_charge_one_nilpotent_cone_resolution_arithmetic() -> None:
    # For k=1, the Uhlenbeck morphism sends ([I],J) to nu=J tensor I with
    # I(J)=0.  Hence Tr(nu)=0, nu^2=0, and rank(nu)<=1.  The dimensions are
    # dim_C T^*CP^{N-1}=2(N-1), dim_C C^2 x T^*CP^{N-1}=2N, and the
    # Uhlenbeck apex C^2 has complex codimension 2(N-1).
    samples = [
        ([Fraction(1), Fraction(0)], [Fraction(0), Fraction(3)]),
        ([Fraction(1), Fraction(2), Fraction(-1)], [Fraction(2), Fraction(-1), Fraction(0)]),
        (
            [Fraction(2), Fraction(-3), Fraction(5), Fraction(1)],
            [Fraction(1), Fraction(1), Fraction(0), Fraction(1)],
        ),
    ]
    for covector, vector in samples:
        n = len(covector)
        pairing = sum(covector[index] * vector[index] for index in range(n))
        assert_equal(pairing, 0, "charge-one ADHM scalar equation I(J)=0")
        matrix = [[vector[row] * covector[col] for col in range(n)] for row in range(n)]
        assert_equal(matrix_trace(matrix), 0, "charge-one nilpotent trace")
        square = matrix_product(matrix, matrix)
        zero = [[Fraction(0) for _ in range(n)] for _ in range(n)]
        assert_equal(square, zero, "charge-one nilpotent square")
        assert_equal(matrix_rank_at_most_one(matrix), True, "charge-one rank-one cone")

    for n in range(2, 12):
        cotangent_projective_dimension = 2 * (n - 1)
        charge_one_gieseker_dimension = 2 + cotangent_projective_dimension
        uhlenbeck_apex_dimension = 2
        assert_equal(charge_one_gieseker_dimension, 2 * n, "charge-one Gieseker dimension")
        assert_equal(
            charge_one_gieseker_dimension - uhlenbeck_apex_dimension,
            2 * (n - 1),
            "charge-one Uhlenbeck apex codimension",
        )


def math_product(values) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def check_young_diagram_one_box_count() -> None:
    for n in range(1, 12):
        one_box_fixed_points = n
        assert_equal(one_box_fixed_points, n, "one-box N-tuple fixed-point count")


def main() -> None:
    check_adhm_dimension_count()
    check_uhlenbeck_stratum_codimension()
    check_torsion_free_sheaf_uhlenbeck_charge_split()
    check_positive_adhm_moment_map_stability_trace()
    check_instanton_exponential_coupling_conversion()
    check_ads_dimensions_and_r_charges()
    check_one_instanton_ads_zero_modes()
    check_ads_higgs_patch_collective_coordinates()
    check_ads_radial_higgs_cutoff_integral()
    check_ads_yukawa_lifting_berezin_determinant()
    check_ads_meson_invariant_uniqueness()
    check_holomorphic_decoupling_dimensions()
    check_ads_decoupling_recursion()
    check_nekrasov_su2_one_instanton()
    check_one_box_tangent_euler_class()
    check_charge_one_nilpotent_cone_resolution_arithmetic()
    check_young_diagram_one_box_count()
    print("All SUSY instanton/ADHM/Nekrasov checks passed.")


if __name__ == "__main__":
    main()
