#!/usr/bin/env python3
"""Exact checks for massless little-group and helicity conventions.

The corresponding chapter proves the representation-theoretic statements in
text.  This script checks the finite algebra that is easy to get wrong:
null-translation matrices, polarization shifts, auxiliary-vector projectors,
spinor-helicity determinants, and the BCFW on-shell deformation.
"""

import sympy as sp


def assert_matrix_equal(actual, expected, label):
    diff = sp.simplify(actual - expected)
    if diff != sp.zeros(*actual.shape):
        raise AssertionError(f"{label}: got\n{actual}\nexpected\n{expected}")


def assert_equal(actual, expected, label):
    if sp.simplify(actual - expected) != 0:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


eta = sp.diag(-1, 1, 1, 1)


def lower(v):
    return eta * v


def dot(u, v):
    return (u.T * eta * v)[0]


def T(alpha, beta):
    zeta = (alpha**2 + beta**2) / 2
    return sp.Matrix(
        [
            [1 + zeta, alpha, beta, -zeta],
            [alpha, 1, 0, -alpha],
            [beta, 0, 1, -beta],
            [zeta, alpha, beta, 1 - zeta],
        ]
    )


def check_null_translation_matrix():
    alpha = sp.Rational(2, 5)
    beta = sp.Rational(-3, 7)
    gamma = sp.Rational(5, 11)
    delta = sp.Rational(7, 13)
    kappa = sp.Rational(17, 3)
    q = sp.Matrix([kappa, 0, 0, kappa])

    mat = T(alpha, beta)
    assert_matrix_equal(mat.T * eta * mat, eta, "T preserves eta")
    assert_matrix_equal(mat * q, q, "T fixes q")
    assert_matrix_equal(
        T(alpha, beta) * T(gamma, delta),
        T(alpha + gamma, beta + delta),
        "T product adds parameters",
    )


def check_polarization_shift():
    alpha = sp.Rational(3, 5)
    beta = sp.Rational(2, 7)
    kappa = sp.Rational(11, 3)
    q_lower = sp.Matrix([-kappa, 0, 0, kappa])
    eps_plus = sp.Matrix([0, 1, -sp.I, 0]) / sp.sqrt(2)
    eps_minus = sp.Matrix([0, 1, sp.I, 0]) / sp.sqrt(2)

    shifted_plus = T(alpha, beta).T * eps_plus
    expected_plus = eps_plus - (alpha - sp.I * beta) * q_lower / (sp.sqrt(2) * kappa)
    assert_matrix_equal(shifted_plus, expected_plus, "plus polarization shift")

    shifted_minus = T(alpha, beta).T * eps_minus
    expected_minus = eps_minus - (alpha + sp.I * beta) * q_lower / (sp.sqrt(2) * kappa)
    assert_matrix_equal(shifted_minus, expected_minus, "minus polarization shift")


def check_auxiliary_projector():
    k_up = sp.Matrix([5, 3, 4, 0])
    n_up = sp.Matrix([2, 1, 0, 0])
    k_low = lower(k_up)
    n_low = lower(n_up)
    k_dot_n = dot(k_up, n_up)
    assert_equal(dot(k_up, k_up), 0, "sample k is null")
    assert k_dot_n != 0

    projector = eta - (k_low * n_low.T + n_low * k_low.T) / k_dot_n
    projector += dot(n_up, n_up) * (k_low * k_low.T) / (k_dot_n**2)

    assert_matrix_equal(k_up.T * projector, sp.zeros(1, 4), "k transversality")
    assert_matrix_equal(n_up.T * projector, sp.zeros(1, 4), "n transversality")

    m_up = sp.Matrix([0, 4, -3, 0])
    assert_equal(dot(m_up, k_up), 0, "sample conserved vector")
    shift = k_low * sp.Rational(9, 5)
    shifted_projector = projector + k_low * shift.T + shift * k_low.T
    before = (m_up.T * projector * sp.conjugate(m_up))[0]
    after = (m_up.T * shifted_projector * sp.conjugate(m_up))[0]
    assert_equal(after, before, "conserved contraction ignores k shifts")


def angle(lam_i, lam_j):
    return lam_i[0] * lam_j[1] - lam_i[1] * lam_j[0]


def square(tilde_i, tilde_j):
    return tilde_i[0] * tilde_j[1] - tilde_i[1] * tilde_j[0]


def outer(lam, tilde):
    return sp.Matrix([[lam[0] * tilde[0], lam[0] * tilde[1]],
                      [lam[1] * tilde[0], lam[1] * tilde[1]]])


def check_spinor_helicity_identity():
    lam_i = sp.Matrix([2, 3])
    tilde_i = sp.Matrix([5, 7])
    lam_j = sp.Matrix([11, 13])
    tilde_j = sp.Matrix([17, 19])
    p_i = outer(lam_i, tilde_i)
    p_j = outer(lam_j, tilde_j)

    assert_equal(p_i.det(), 0, "rank-one p_i")
    assert_equal(p_j.det(), 0, "rank-one p_j")
    lhs = angle(lam_i, lam_j) * square(tilde_j, tilde_i)
    rhs = -(p_i + p_j).det()
    assert_equal(lhs, rhs, "mostly-plus determinant gives <ij>[ji]")


def check_bcfw_shift():
    z = sp.Rational(5, 7)
    lam_i = sp.Matrix([2, 3])
    tilde_i = sp.Matrix([5, 7])
    lam_j = sp.Matrix([11, 13])
    tilde_j = sp.Matrix([17, 19])

    p_i = outer(lam_i, tilde_i)
    p_j = outer(lam_j, tilde_j)
    shifted_i = outer(lam_i, tilde_i + z * tilde_j)
    shifted_j = outer(lam_j - z * lam_i, tilde_j)

    assert_equal(shifted_i.det(), 0, "shifted i remains null")
    assert_equal(shifted_j.det(), 0, "shifted j remains null")
    assert_matrix_equal(shifted_i + shifted_j, p_i + p_j, "BCFW preserves sum")


def main():
    check_null_translation_matrix()
    check_polarization_shift()
    check_auxiliary_projector()
    check_spinor_helicity_identity()
    check_bcfw_shift()
    print("All massless-helicity convention checks passed.")


if __name__ == "__main__":
    main()
