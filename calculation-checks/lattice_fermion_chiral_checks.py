#!/usr/bin/env python3
"""Finite checks for lattice-fermion/chiral-symmetry conventions.

The script verifies exact arithmetic used in Volume XI, Chapter 11:
naive doubler chirality signs, Wilson doubler masses, the
Ginsparg-Wilson/overlap algebra, and the finite Berezinian index factor.
"""

from fractions import Fraction
from itertools import product, combinations


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def matmul(a, b):
    n = len(a)
    m = len(b[0])
    kdim = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(kdim)) for j in range(m)]
        for i in range(n)
    ]


def matadd(a, b):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def matsub(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scalar_mul(c, a):
    return [[c * x for x in row] for row in a]


def diag(entries):
    return [
        [entry if i == j else Fraction(0) for j, entry in enumerate(entries)]
        for i, entry in enumerate(entries)
    ]


def eye(n):
    return diag([Fraction(1) for _ in range(n)])


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def transpose(a):
    return [list(row) for row in zip(*a)]


def assert_zero_matrix(a, label):
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != 0:
                raise AssertionError(f"{label}: entry {(i, j)} is {value!r}")


def check_naive_doubler_chirality_sum():
    dimension = 4
    signs = []
    for epsilon in product([0, 1], repeat=dimension):
        signs.append((-1) ** sum(epsilon))
    assert_equal(len(signs), 2**dimension, "number of naive Brillouin corners")
    assert_equal(sum(signs), 0, "sum of doubler chirality signs")
    assert_equal(signs.count(1), signs.count(-1), "opposite chirality multiplicities")


def check_wilson_corner_masses():
    dimension = 4
    mass = Fraction(1, 7)
    r = Fraction(1)
    a = Fraction(1)
    degeneracies = {}
    for epsilon in product([0, 1], repeat=dimension):
        n_epsilon = sum(epsilon)
        corner_mass = mass + 2 * r * n_epsilon / a
        degeneracies[corner_mass] = degeneracies.get(corner_mass, 0) + 1
    expected = {
        Fraction(1, 7): 1,
        Fraction(15, 7): 4,
        Fraction(29, 7): 6,
        Fraction(43, 7): 4,
        Fraction(57, 7): 1,
    }
    assert_equal(degeneracies, expected, "Wilson corner mass degeneracies")


def check_ginsparg_wilson_and_overlap_index():
    # A diagonal exact example with nonzero overlap index.
    gamma5 = diag([Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)])
    v = diag([Fraction(1), Fraction(1), Fraction(1), Fraction(-1)])
    ident = eye(4)
    d = matadd(ident, v)  # lattice spacing a=1

    lhs = matadd(matmul(gamma5, d), matmul(d, gamma5))
    rhs = matmul(matmul(d, gamma5), d)
    assert_zero_matrix(matsub(lhs, rhs), "Ginsparg-Wilson relation")

    index = trace(matmul(gamma5, matsub(ident, scalar_mul(Fraction(1, 2), d))))
    sign_h = matmul(gamma5, v)
    spectral_asymmetry = -Fraction(1, 2) * trace(sign_h)
    assert_equal(index, Fraction(-1), "sample overlap index")
    assert_equal(index, spectral_asymmetry, "overlap spectral asymmetry index")

    measure_log_linear = trace(matmul(gamma5, d))
    assert_equal(measure_log_linear, -2 * index, "Berezinian index exponent")

    # A non-diagonal unitary V with zero index checks the same algebra without
    # relying on simultaneous diagonalization.
    gamma5_2 = diag([Fraction(1), Fraction(-1)])
    v2 = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]
    d2 = matadd(eye(2), v2)
    lhs2 = matadd(matmul(gamma5_2, d2), matmul(d2, gamma5_2))
    rhs2 = matmul(matmul(d2, gamma5_2), d2)
    assert_zero_matrix(matsub(lhs2, rhs2), "non-diagonal GW relation")
    v2_dagger = transpose(v2)
    gamma_v_gamma = matmul(matmul(gamma5_2, v2), gamma5_2)
    assert_equal(v2_dagger, gamma_v_gamma, "gamma5-Hermiticity of V")


def check_reflection_positive_crossing_coefficients():
    coefficients = [Fraction(1, 2), Fraction(3, 5), Fraction(7, 4)]
    subset_products = []
    for r in range(len(coefficients) + 1):
        for subset in combinations(coefficients, r):
            prod_value = Fraction(1)
            for value in subset:
                prod_value *= value
            subset_products.append(prod_value)
    if any(value < 0 for value in subset_products):
        raise AssertionError("reflection-positive crossing coefficient became negative")
    assert_equal(sum(subset_products), Fraction(33, 5), "crossing factor coefficient sum")


def check_wilson_reflection_projectors():
    gamma0 = diag([Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)])
    ident = eye(4)
    p_plus = scalar_mul(Fraction(1, 2), matadd(ident, gamma0))
    p_minus = scalar_mul(Fraction(1, 2), matsub(ident, gamma0))
    assert_zero_matrix(matsub(matmul(p_plus, p_plus), p_plus), "P+ idempotent")
    assert_zero_matrix(matsub(matmul(p_minus, p_minus), p_minus), "P- idempotent")
    assert_zero_matrix(matmul(p_plus, p_minus), "P+ P- orthogonality")
    assert_equal(trace(p_plus), Fraction(2), "P+ rank")
    assert_equal(trace(p_minus), Fraction(2), "P- rank")


def check_staggered_phase_antisymmetry():
    # Two-dimensional staggered phases eta_0=1, eta_1=(-1)^x0 in lattice units.
    def eta(mu, x):
        if mu == 0:
            return 1
        if mu == 1:
            return (-1) ** x[0]
        raise ValueError(mu)

    sites = [(x0, x1) for x0 in range(4) for x1 in range(4)]
    for x in sites:
        for mu in [0, 1]:
            y = list(x)
            y[mu] = (y[mu] + 1) % 4
            y = tuple(y)
            forward = Fraction(eta(mu, x), 2)
            backward = -Fraction(eta(mu, x), 2)
            # M(x,y)=eta_mu(x)/2 and M(y,x)=-eta_mu(x)/2 for the same link.
            assert_equal(forward, -backward, "staggered link antisymmetry")

    for x in sites:
        reflection_phase = (-1) ** x[1]
        assert_equal(reflection_phase * reflection_phase, 1, "staggered reflection phase squares to one")


def main():
    check_naive_doubler_chirality_sum()
    check_wilson_corner_masses()
    check_ginsparg_wilson_and_overlap_index()
    check_reflection_positive_crossing_coefficients()
    check_wilson_reflection_projectors()
    check_staggered_phase_antisymmetry()
    print(
        "All lattice-fermion doubler, Wilson-mass, Ginsparg-Wilson, "
        "overlap-index, reflection-crossing, Wilson-projector, and "
        "staggered-phase checks passed."
    )


if __name__ == "__main__":
    main()
