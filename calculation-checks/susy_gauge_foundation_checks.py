#!/usr/bin/env python3
"""Finite checks for foundational supersymmetric gauge-theory conventions."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def coeff(real=0, imag=0):
    return (Fraction(real), Fraction(imag))


def add_coeff(left, right):
    return (left[0] + right[0], left[1] + right[1])


def mul_coeff(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def scale_expr(expr, factor):
    scaled = {}
    for word, value in expr.items():
        product = mul_coeff(factor, value)
        if product != coeff():
            scaled[word] = product
    return scaled


def add_expr(*exprs):
    total = {}
    for expr in exprs:
        for word, value in expr.items():
            new_value = add_coeff(total.get(word, coeff()), value)
            if new_value == coeff():
                total.pop(word, None)
            else:
                total[word] = new_value
    return total


def singleton(word, value=coeff(1)):
    return {word: value}


def commutator(left, right):
    return add_expr(
        singleton((left, right)),
        singleton((right, left), coeff(-1)),
    )


def matmul2(left, right):
    return [
        [
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ],
        [
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ],
    ]


def matvec2(matrix, vector):
    return [
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    ]


def rowmat2(row, matrix):
    return [
        row[0] * matrix[0][0] + row[1] * matrix[1][0],
        row[0] * matrix[0][1] + row[1] * matrix[1][1],
    ]


def rowvec2(row, vector):
    return row[0] * vector[0] + row[1] * vector[1]


def check_d_term_square_completion():
    """Check the auxiliary D-field equation and on-shell potential sign."""

    g_squared = Fraction(5, 3)
    mu = Fraction(7, 4)
    zeta = Fraction(1, 6)
    eta = mu - zeta

    d_on_shell = -g_squared * eta
    lagrangian_on_shell = d_on_shell * d_on_shell / (2 * g_squared) + eta * d_on_shell
    expected_lagrangian = -g_squared * eta * eta / 2
    potential = -lagrangian_on_shell

    assert_equal(d_on_shell, -g_squared * eta, "D-field algebraic equation")
    assert_equal(lagrangian_on_shell, expected_lagrangian, "D-term on-shell Lagrangian")
    assert_equal(potential, g_squared * eta * eta / 2, "positive D-term potential")


def check_fi_parameter_centrality_for_su2():
    """A linear FI functional on a semisimple algebra must vanish."""

    # In an su(2) basis [e1,e2]=e3, [e2,e3]=e1, [e3,e1]=e2.
    # Gauge invariance of zeta requires zeta([x,y])=0 for each bracket, so the
    # linear system for (zeta(e1), zeta(e2), zeta(e3)) has these rows.
    constraint_rows = [
        (0, 0, 1),  # zeta([e1,e2]) = zeta(e3)
        (1, 0, 0),  # zeta([e2,e3]) = zeta(e1)
        (0, 1, 0),  # zeta([e3,e1]) = zeta(e2)
    ]
    determinant = (
        constraint_rows[0][0] * constraint_rows[1][1] * constraint_rows[2][2]
        + constraint_rows[0][1] * constraint_rows[1][2] * constraint_rows[2][0]
        + constraint_rows[0][2] * constraint_rows[1][0] * constraint_rows[2][1]
        - constraint_rows[0][2] * constraint_rows[1][1] * constraint_rows[2][0]
        - constraint_rows[0][1] * constraint_rows[1][0] * constraint_rows[2][2]
        - constraint_rows[0][0] * constraint_rows[1][2] * constraint_rows[2][1]
    )
    assert_equal(abs(determinant), 1, "SU(2) FI centrality matrix has full rank")


def cubic_u1_anomaly(charges):
    return sum(q**3 for q in charges)


def mixed_gravity_u1_anomaly(charges):
    return sum(charges)


def check_vectorlike_u1_anomaly_cancellation():
    for q in (Fraction(1), Fraction(2), Fraction(-3, 2), Fraction(5, 3)):
        charges = [q, -q]
        assert_equal(cubic_u1_anomaly(charges), 0, f"U(1)^3 vectorlike anomaly q={q}")
        assert_equal(
            mixed_gravity_u1_anomaly(charges),
            0,
            f"mixed gravitational-U(1) vectorlike anomaly q={q}",
        )


def check_conjugate_nonabelian_anomaly_sign():
    """Model the sign A_{R^vee}=-A_R for a single anomaly coefficient."""

    anomaly_r = Fraction(11, 7)
    anomaly_dual = -anomaly_r
    assert_equal(anomaly_r + anomaly_dual, 0, "conjugate representation anomaly sign")


def check_wz_closure_translation_decomposition():
    """Check the Hermitian-sign identity used in Wess-Zumino-gauge closure."""

    minus_i = coeff(0, -1)
    plus_i = coeff(0, 1)

    f_rho_mu = add_expr(
        singleton(("partial_rho_A_mu",)),
        singleton(("partial_mu_A_rho",), coeff(-1)),
        scale_expr(commutator("A_rho", "A_mu"), minus_i),
    )
    covariant_derivative_a_rho = add_expr(
        singleton(("partial_mu_A_rho",)),
        scale_expr(commutator("A_mu", "A_rho"), minus_i),
    )
    ordinary_translation_a_mu = singleton(("partial_rho_A_mu",))
    assert_equal(
        add_expr(f_rho_mu, covariant_derivative_a_rho),
        ordinary_translation_a_mu,
        "connection closure: a^rho F_{rho mu}+D_mu(a^rho A_rho)",
    )

    adjoint_left = add_expr(
        singleton(("partial_rho_X",)),
        scale_expr(commutator("Omega", "X"), plus_i),
    )
    adjoint_right = add_expr(
        singleton(("partial_rho_X",)),
        scale_expr(commutator("A_rho", "X"), minus_i),
        scale_expr(commutator("Omega", "X"), plus_i),
        scale_expr(commutator("A_rho", "X"), plus_i),
    )
    assert_equal(
        adjoint_right,
        adjoint_left,
        "adjoint closure: ordinary plus gauge equals covariant plus shifted gauge",
    )


def check_n2_qcd_superpotential_contraction_and_fterms():
    """Check the N=2 QCD cubic contraction and F-term coefficient."""

    phi = [
        [Fraction(2), Fraction(3)],
        [Fraction(5), Fraction(7)],
    ]
    q = [Fraction(11), Fraction(13)]
    q_tilde = [Fraction(17), Fraction(19)]
    u = [
        [Fraction(1), Fraction(1)],
        [Fraction(0), Fraction(1)],
    ]
    u_inv = [
        [Fraction(1), Fraction(-1)],
        [Fraction(0), Fraction(1)],
    ]

    original = rowvec2(rowmat2(q_tilde, phi), q)
    transformed_q = matvec2(u, q)
    transformed_q_tilde = rowmat2(q_tilde, u_inv)
    transformed_phi = matmul2(matmul2(u, phi), u_inv)
    transformed = rowvec2(rowmat2(transformed_q_tilde, transformed_phi), transformed_q)
    assert_equal(transformed, original, "N=2 QCD cubic gauge contraction")

    g_squared = Fraction(5, 7)
    coefficient_squared = 2 * g_squared
    assert_equal(
        coefficient_squared,
        Fraction(10, 7),
        "N=2 QCD F-term coefficient from (sqrt(2) g)^2",
    )


def main():
    check_d_term_square_completion()
    check_fi_parameter_centrality_for_su2()
    check_vectorlike_u1_anomaly_cancellation()
    check_conjugate_nonabelian_anomaly_sign()
    check_wz_closure_translation_decomposition()
    check_n2_qcd_superpotential_contraction_and_fterms()
    print("All supersymmetric gauge-foundation checks passed.")


if __name__ == "__main__":
    main()
