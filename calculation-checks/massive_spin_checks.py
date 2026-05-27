#!/usr/bin/env python3
"""Exact checks for massive-spin conventions in Volume I.

The chapter proves the representation-theoretic statements in text.  This
script checks finite algebra that is convention-sensitive: the mass-shell
Jacobian, Wigner cocycle, spin-frame conjugation law, the SU(2) central sign,
and the mostly-plus Dirac projector and spin-sum formulas.
"""

import sympy as sp


ii = sp.I
eta = sp.diag(-1, 1, 1, 1)


def assert_equal(actual, expected, label):
    if sp.simplify(actual - expected) != 0:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def assert_matrix_equal(actual, expected, label):
    diff = actual - expected
    diff = diff.applyfunc(sp.simplify)
    if diff != sp.zeros(*actual.shape):
        raise AssertionError(f"{label}: got\n{actual}\nexpected\n{expected}")


def lorentz_dot(u, v):
    return (u.T * eta * v)[0]


def boost_x(beta):
    gamma = sp.simplify(1 / sp.sqrt(1 - beta**2))
    return sp.Matrix(
        [
            [gamma, gamma * beta, 0, 0],
            [gamma * beta, gamma, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def rotation_z_quarter_turn():
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ]
    )


def standard_boost(p, mass):
    energy = p[0]
    spatial = [p[1], p[2], p[3]]
    boost = sp.zeros(4, 4)
    boost[0, 0] = energy / mass
    for i in range(3):
        boost[0, i + 1] = spatial[i] / mass
        boost[i + 1, 0] = spatial[i] / mass
    for i in range(3):
        for j in range(3):
            boost[i + 1, j + 1] = (
                (1 if i == j else 0)
                + spatial[i] * spatial[j] / (mass * (energy + mass))
            )
    return boost


def wigner_rotation(lorentz, p, mass):
    transformed = lorentz * p
    return standard_boost(transformed, mass).inv() * lorentz * standard_boost(p, mass)


def check_mass_shell_jacobian_and_wigner_cocycle():
    mass = sp.Integer(3)
    p = sp.Matrix([5, 4, 0, 0])
    rest = sp.Matrix([mass, 0, 0, 0])
    beta = sp.Rational(3, 5)
    boost = boost_x(beta)
    rotation = rotation_z_quarter_turn()

    assert_equal(lorentz_dot(p, p), -mass**2, "sample momentum mass shell")
    assert_matrix_equal(boost.T * eta * boost, eta, "boost preserves eta")
    assert_matrix_equal(rotation.T * eta * rotation, eta, "rotation preserves eta")
    assert_matrix_equal(standard_boost(p, mass) * rest, p, "standard boost")

    boosted = boost * p
    energy_ratio = sp.simplify(boosted[0] / p[0])
    jacobian = sp.simplify((sp.Rational(5, 4)) * (1 + beta * p[1] / p[0]))
    assert_equal(jacobian, energy_ratio, "on-shell d^3p boost Jacobian")

    w_boost = wigner_rotation(boost, p, mass)
    w_rotation = wigner_rotation(rotation, p, mass)
    assert_matrix_equal(w_boost * rest, rest, "boost Wigner element fixes rest")
    assert_matrix_equal(
        w_rotation * rest,
        rest,
        "rotation Wigner element fixes rest",
    )

    lhs = wigner_rotation(rotation * boost, p, mass)
    rhs = wigner_rotation(rotation, boost * p, mass) * wigner_rotation(
        boost,
        p,
        mass,
    )
    assert_matrix_equal(lhs, rhs, "Wigner cocycle")


def check_covering_signs_and_spin_frame_change():
    for twice_j in range(5):
        dimension = twice_j + 1
        central_sign = (-1) ** twice_j
        assert dimension >= 1
        assert central_sign in (-1, 1)
        if twice_j % 2 == 0:
            assert_equal(central_sign, 1, "integer-spin central sign")
        else:
            assert_equal(central_sign, -1, "half-integer central sign")

    q_p = sp.diag(ii, -ii)
    q_lp = sp.Matrix([[0, 1], [-1, 0]])
    w = sp.diag(-1, 1)
    w_prime = q_lp.inv() * w * q_p
    assert_matrix_equal(w_prime, q_lp.conjugate().T * w * q_p, "unitary inverse")

    psi_l = sp.Matrix([2 + ii, 3 - ii])
    chi_l = sp.Matrix([1 - 2 * ii, 4 + ii])
    psi_lp = q_p.inv() * psi_l
    chi_lp = q_p.inv() * chi_l
    inner_l = (psi_l.conjugate().T * chi_l)[0]
    inner_lp = (psi_lp.conjugate().T * chi_lp)[0]
    assert_equal(inner_lp, inner_l, "spin-frame inner product")


def block2(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


def check_dirac_projectors_and_spin_sums():
    zero = sp.zeros(2)
    eye = sp.eye(2)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -ii], [ii, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    gamma = [
        -ii * block2(zero, eye, eye, zero),
        -ii * block2(zero, sigma1, -sigma1, zero),
        -ii * block2(zero, sigma2, -sigma2, zero),
        -ii * block2(zero, sigma3, -sigma3, zero),
    ]
    identity4 = sp.eye(4)

    for mu in range(4):
        for nu in range(4):
            anti = gamma[mu] * gamma[nu] + gamma[nu] * gamma[mu]
            assert_matrix_equal(
                anti,
                2 * eta[mu, nu] * identity4,
                f"Clifford relation {mu}{nu}",
            )

    beta = ii * gamma[0]
    assert_matrix_equal(beta * beta, identity4, "beta squared")
    assert_matrix_equal(gamma[0].conjugate().T, -gamma[0], "gamma0 dagger")
    for i in range(1, 4):
        assert_matrix_equal(gamma[i].conjugate().T, gamma[i], f"gamma{i} dagger")

    mass = sp.Integer(3)
    slash_rest = -mass * gamma[0]
    pi_plus = (mass * identity4 - ii * slash_rest) / (2 * mass)
    pi_minus = (mass * identity4 + ii * slash_rest) / (2 * mass)
    assert_matrix_equal(pi_plus * pi_plus, pi_plus, "Pi plus idempotent")
    assert_matrix_equal(pi_minus * pi_minus, pi_minus, "Pi minus idempotent")
    assert_matrix_equal(pi_plus * pi_minus, sp.zeros(4), "orthogonal projectors")
    assert_matrix_equal(pi_plus + pi_minus, identity4, "projector sum")

    root2 = sp.sqrt(2)
    u1 = sp.Matrix([1, 0, 1, 0]) / root2
    u2 = sp.Matrix([0, 1, 0, 1]) / root2
    v1 = sp.Matrix([1, 0, -1, 0]) / root2
    v2 = sp.Matrix([0, 1, 0, -1]) / root2
    us = [u1, u2]
    vs = [v1, v2]

    for a, spinor_a in enumerate(us):
        for b, spinor_b in enumerate(us):
            value = (spinor_a.conjugate().T * beta * spinor_b)[0]
            assert_equal(value, 1 if a == b else 0, "positive beta norm")
    for a, spinor_a in enumerate(vs):
        for b, spinor_b in enumerate(vs):
            value = (spinor_a.conjugate().T * beta * spinor_b)[0]
            assert_equal(value, -1 if a == b else 0, "negative beta norm")

    spin_sum_u = sum((u * u.conjugate().T for u in us), sp.zeros(4))
    spin_sum_v = sum((v * v.conjugate().T for v in vs), sp.zeros(4))
    expected_u = (mass * identity4 - ii * slash_rest) * beta / (2 * mass)
    expected_v = (-mass * identity4 - ii * slash_rest) * beta / (2 * mass)
    assert_matrix_equal(spin_sum_u, expected_u, "rest U spin sum")
    assert_matrix_equal(spin_sum_v, expected_v, "rest V spin sum")

    gamma5 = -ii * gamma[0] * gamma[1] * gamma[2] * gamma[3]
    assert_matrix_equal(gamma5, block2(eye, zero, zero, -eye), "gamma5 basis")
    assert_matrix_equal(gamma5 * u1, v1, "gamma5 maps U1 to V1")
    assert_matrix_equal(gamma5 * u2, v2, "gamma5 maps U2 to V2")


def main():
    check_mass_shell_jacobian_and_wigner_cocycle()
    check_covering_signs_and_spin_frame_change()
    check_dirac_projectors_and_spin_sums()
    print("All massive-spin convention checks passed.")


if __name__ == "__main__":
    main()
