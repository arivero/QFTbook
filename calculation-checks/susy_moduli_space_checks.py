#!/usr/bin/env python3
"""Finite algebra checks for supersymmetric moduli-space quotient conventions."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_rank_one_abelian_invariant_ring():
    """Check C[x,y]^{C*} = C[xy] for charges (+1,-1) up to finite degree."""

    for total_degree in range(0, 10):
        invariant_monomials = []
        for a in range(total_degree + 1):
            b = total_degree - a
            charge = a - b
            if charge == 0:
                invariant_monomials.append((a, b))

        if total_degree % 2 == 0:
            power = total_degree // 2
            assert_equal(
                invariant_monomials,
                [(power, power)],
                f"degree {total_degree} invariant monomial is (xy)^{power}",
            )
        else:
            assert_equal(
                invariant_monomials,
                [],
                f"degree {total_degree} has no invariant monomial",
            )


def check_rank_one_abelian_dimension_count():
    """Compare real symplectic and complex affine quotient dimensions."""

    complex_variables = 2
    complex_reductive_quotient = 1
    affine_complex_dimension = complex_variables - complex_reductive_quotient

    real_variables = 4
    real_moment_map_equations = 1
    compact_gauge_orbit_dimension = 1
    symplectic_real_dimension = (
        real_variables - real_moment_map_equations - compact_gauge_orbit_dimension
    )

    assert_equal(affine_complex_dimension, 1, "affine quotient complex dimension")
    assert_equal(symplectic_real_dimension, 2, "symplectic quotient real dimension")
    assert_equal(
        2 * affine_complex_dimension,
        symplectic_real_dimension,
        "Kempf-Ness dimension comparison",
    )


def check_f_term_ideal_equivariance():
    """Invariant W implies dW transforms in the dual representation."""

    q_x = 1
    q_y = -1

    # W=(xy)^2 is invariant.  The derivative F_x=2*x*y^2 has charge -1,
    # and F_y=2*x^2*y has charge +1, i.e. q(F_i)=-q(field_i).
    charge_fx = q_x + 2 * q_y
    charge_fy = 2 * q_x + q_y

    assert_equal(charge_fx, -q_x, "F_x dual charge")
    assert_equal(charge_fy, -q_y, "F_y dual charge")
    assert_equal(charge_fx + q_x, 0, "F_x d x invariant pairing")
    assert_equal(charge_fy + q_y, 0, "F_y d y invariant pairing")


def check_rank_one_hyperkahler_quotient_dimensions():
    """Check the dimension ledger for T^* P^{N-1} as a hyperkahler quotient."""

    for n in range(2, 20):
        ambient_complex_dimension = 2 * n
        complex_moment_equations = 1
        complex_gauge_dimension = 1
        quotient_complex_dimension = (
            ambient_complex_dimension
            - complex_moment_equations
            - complex_gauge_dimension
        )

        ambient_real_dimension = 4 * n
        real_moment_equations = 3
        compact_gauge_dimension = 1
        quotient_real_dimension = (
            ambient_real_dimension
            - real_moment_equations
            - compact_gauge_dimension
        )

        assert_equal(
            quotient_complex_dimension,
            2 * (n - 1),
            "rank-one hyperkahler quotient complex dimension",
        )
        assert_equal(
            quotient_real_dimension,
            4 * (n - 1),
            "rank-one hyperkahler quotient real dimension",
        )
        assert_equal(
            2 * quotient_complex_dimension,
            quotient_real_dimension,
            "rank-one hyperkahler quotient real/complex dimension match",
        )


def check_rank_one_hyperkahler_one_form_descent():
    """Check that sum tilde(q)_i dq_i descends to sum p_i dz_i on a patch."""

    for n in range(2, 10):
        q_a = Fraction(5, 3)
        z = {index: Fraction(index + 2, index + 5) for index in range(1, n)}
        p = {index: Fraction(2 * index + 3, index + 7) for index in range(1, n)}

        tilde = {index: p[index] / q_a for index in range(1, n)}
        tilde_a = -sum(z[index] * p[index] for index in range(1, n)) / q_a

        dq_a_coefficient = tilde_a + sum(
            z[index] * tilde[index]
            for index in range(1, n)
        )
        assert_equal(
            dq_a_coefficient,
            0,
            "rank-one hyperkahler quotient vertical one-form coefficient",
        )

        for index in range(1, n):
            dz_coefficient = q_a * tilde[index]
            assert_equal(
                dz_coefficient,
                p[index],
                "rank-one hyperkahler quotient cotangent coordinate",
            )


def check_rank_one_hyperkahler_cotangent_transition():
    """Check a patch transition preserves the canonical cotangent one-form."""

    for n in range(2, 10):
        z = {index: Fraction(index + 2, index + 4) for index in range(1, n)}
        p = {index: Fraction(3 * index + 1, 2 * index + 5) for index in range(1, n)}
        z_1 = z[1]

        # Move from the q_0 != 0 patch to the q_1 != 0 patch.  New coordinates
        # are w_0=1/z_1 and w_j=z_j/z_1 for j>=2.  The new momenta are
        # r_0=-z_1 sum_j z_j p_j and r_j=z_1 p_j.
        r_0 = -z_1 * sum(z[index] * p[index] for index in range(1, n))
        r = {index: z_1 * p[index] for index in range(2, n)}

        rhs_coefficients = {index: Fraction(0) for index in range(1, n)}
        rhs_coefficients[1] += r_0 * (-1 / (z_1 * z_1))
        for index in range(2, n):
            rhs_coefficients[index] += r[index] * (1 / z_1)
            rhs_coefficients[1] += r[index] * (-z[index] / (z_1 * z_1))

        for index in range(1, n):
            assert_equal(
                rhs_coefficients[index],
                p[index],
                "rank-one hyperkahler cotangent transition preserves one-form",
            )


def su2_nf2_minors(row_1, row_2):
    """Return V^{IJ}=row_1^I row_2^J-row_1^J row_2^I for I<J."""

    minors = {}
    for i in range(4):
        for j in range(i + 1, 4):
            minors[(i, j)] = row_1[i] * row_2[j] - row_1[j] * row_2[i]
    return minors


def su2_nf2_pfaffian(v):
    """Pf(V)=V12 V34 - V13 V24 + V14 V23 in zero-based indices."""

    return (
        v[(0, 1)] * v[(2, 3)]
        - v[(0, 2)] * v[(1, 3)]
        + v[(0, 3)] * v[(1, 2)]
    )


def check_su2_nf2_plucker_identity():
    """Check decomposable SU(2) invariants obey the Pfaffian relation."""

    test_rows = [
        (
            [Fraction(1), Fraction(2), Fraction(3), Fraction(5)],
            [Fraction(7), Fraction(11), Fraction(13), Fraction(17)],
        ),
        (
            [Fraction(-2), Fraction(3, 5), Fraction(0), Fraction(9, 4)],
            [Fraction(1, 7), Fraction(-4), Fraction(6), Fraction(5, 3)],
        ),
    ]

    for row_1, row_2 in test_rows:
        minors = su2_nf2_minors(row_1, row_2)
        assert_equal(
            su2_nf2_pfaffian(minors),
            0,
            "SU(2) N_f=2 decomposable two-form has zero Pfaffian",
        )


def check_su2_nf2_plucker_converse_chart():
    """Check the explicit V12 != 0 reconstruction used in the text."""

    chart_data = [
        (
            Fraction(3),
            Fraction(5),
            Fraction(-7),
            Fraction(11),
            Fraction(13),
        ),
        (
            Fraction(-5, 2),
            Fraction(7, 3),
            Fraction(4),
            Fraction(-9, 5),
            Fraction(6),
        ),
    ]

    for v_01, v_02, v_03, v_12, v_13 in chart_data:
        v_23 = (v_02 * v_13 - v_03 * v_12) / v_01
        v = {
            (0, 1): v_01,
            (0, 2): v_02,
            (0, 3): v_03,
            (1, 2): v_12,
            (1, 3): v_13,
            (2, 3): v_23,
        }
        assert_equal(
            su2_nf2_pfaffian(v),
            0,
            "SU(2) N_f=2 converse chart data lies on Pfaffian hypersurface",
        )

        row_1 = [Fraction(1), Fraction(0), -v_12 / v_01, -v_13 / v_01]
        row_2 = [Fraction(0), v_01, v_02, v_03]
        reconstructed = su2_nf2_minors(row_1, row_2)
        assert_equal(
            reconstructed,
            v,
            "SU(2) N_f=2 Pfaffian-zero point reconstructs from doublets",
        )


def check_su2_nf2_dimension_ledger():
    """Compare the Plucker hypersurface and stable quotient dimensions."""

    antisymmetric_coordinates = 6
    pfaffian_equations = 1
    hypersurface_dimension = antisymmetric_coordinates - pfaffian_equations

    doublet_coordinates = 2 * 4
    complex_gauge_dimension = 3
    stable_quotient_dimension = doublet_coordinates - complex_gauge_dimension

    assert_equal(hypersurface_dimension, 5, "SU(2) N_f=2 hypersurface dimension")
    assert_equal(stable_quotient_dimension, 5, "SU(2) N_f=2 quotient dimension")
    assert_equal(
        hypersurface_dimension,
        stable_quotient_dimension,
        "SU(2) N_f=2 dimension ledger match",
    )


def main():
    check_rank_one_abelian_invariant_ring()
    check_rank_one_abelian_dimension_count()
    check_f_term_ideal_equivariance()
    check_rank_one_hyperkahler_quotient_dimensions()
    check_rank_one_hyperkahler_one_form_descent()
    check_rank_one_hyperkahler_cotangent_transition()
    check_su2_nf2_plucker_identity()
    check_su2_nf2_plucker_converse_chart()
    check_su2_nf2_dimension_ledger()
    print("All supersymmetric moduli-space quotient checks passed.")


if __name__ == "__main__":
    main()
