#!/usr/bin/env python3
"""Exact checks for rapidity and factorized-scattering algebra.

These checks accompany Volume VI, Chapter 1.  They verify finite algebraic
identities behind the rapidity invariant, Newton separation of rapidity
multisets, chamber braid relations, the rational Yang--Baxter identity, and
scalar Watson-exchange bookkeeping.
"""

from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def zero_matrix(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def identity(n):
    out = zero_matrix(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def pair_operator(pair: tuple[int, int], two_body: Matrix) -> Matrix:
    op = zero_matrix(8)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                incoming = (a, b, c)
                incoming_index = 4 * a + 2 * b + c
                i, j = pair
                pair_index = 2 * incoming[i] + incoming[j]
                for outgoing_pair_index in range(4):
                    coefficient = two_body[outgoing_pair_index][pair_index]
                    if coefficient == 0:
                        continue
                    outgoing = list(incoming)
                    outgoing[i] = outgoing_pair_index // 2
                    outgoing[j] = outgoing_pair_index % 2
                    outgoing_index = 4 * outgoing[0] + 2 * outgoing[1] + outgoing[2]
                    op[outgoing_index][incoming_index] += coefficient
    return op


def flip_two_body() -> Matrix:
    p = zero_matrix(4)
    for a in range(2):
        for b in range(2):
            incoming = 2 * a + b
            outgoing = 2 * b + a
            p[outgoing][incoming] = Fraction(1)
    return p


def rational_r(u: Fraction) -> Matrix:
    # The Yang rational R-matrix R(u)=u I + P satisfies
    # R12(u) R13(u+v) R23(v) = R23(v) R13(u+v) R12(u).
    return add(scale(u, identity(4)), flip_two_body())


def check_rapidity_invariant():
    ma = Fraction(3)
    mb = Fraction(5)
    z1 = Fraction(7, 2)
    z2 = Fraction(4, 3)

    p1 = (ma * (z1 + Fraction(1, 1) / z1) / 2, ma * (z1 - Fraction(1, 1) / z1) / 2)
    p2 = (mb * (z2 + Fraction(1, 1) / z2) / 2, mb * (z2 - Fraction(1, 1) / z2) / 2)
    total = (p1[0] + p2[0], p1[1] + p2[1])
    minus_total_square = total[0] * total[0] - total[1] * total[1]
    formula = ma * ma + mb * mb + ma * mb * (z1 / z2 + z2 / z1)
    assert_equal(minus_total_square, formula, "mostly-plus rapidity invariant")


def check_newton_two_root_separation():
    roots = [Fraction(2), Fraction(5)]
    p1 = sum(roots)
    p2 = sum(r * r for r in roots)
    e1 = p1
    e2 = (p1 * p1 - p2) / 2
    assert_equal((e1, e2), (Fraction(7), Fraction(10)), "Newton identities for two rapidity roots")
    for root in roots:
        assert_equal(root * root - e1 * root + e2, Fraction(0), "recovered monic polynomial")


def check_chamber_groupoid_permutation_relations():
    p12 = pair_operator((0, 1), flip_two_body())
    p23 = pair_operator((1, 2), flip_two_body())
    assert_equal(matmul(p12, p12), identity(8), "adjacent involution P12")
    assert_equal(matmul(p23, p23), identity(8), "adjacent involution P23")
    assert_equal(matmul(matmul(p12, p23), p12), matmul(matmul(p23, p12), p23), "S3 braid relation")


def check_rational_yang_baxter_identity():
    u = Fraction(2)
    v = Fraction(3)
    r12 = pair_operator((0, 1), rational_r(u))
    r13 = pair_operator((0, 2), rational_r(u + v))
    r23 = pair_operator((1, 2), rational_r(v))
    lhs = matmul(matmul(r12, r13), r23)
    rhs = matmul(matmul(r23, r13), r12)
    assert_equal(lhs, rhs, "rational Yang-Baxter identity")


def scalar_s(x: Fraction) -> Fraction:
    return (x - 1) / (x + 1)


def check_scalar_unitarity_and_watson_bookkeeping():
    theta12 = Fraction(5)
    theta13 = Fraction(7)
    theta23 = Fraction(2)
    assert_equal(scalar_s(theta12) * scalar_s(-theta12), Fraction(1), "scalar two-body unitarity")
    lhs = scalar_s(theta12) * scalar_s(theta13) * scalar_s(theta23)
    rhs = scalar_s(theta23) * scalar_s(theta13) * scalar_s(theta12)
    assert_equal(lhs, rhs, "scalar ZF reorder coefficient")

    form_factor_neighbor = Fraction(11, 3)
    form_factor_original = scalar_s(theta12) * form_factor_neighbor
    assert_equal(
        form_factor_original,
        Fraction(4, 6) * form_factor_neighbor,
        "scalar Watson exchange coefficient",
    )


def main():
    check_rapidity_invariant()
    check_newton_two_root_separation()
    check_chamber_groupoid_permutation_relations()
    check_rational_yang_baxter_identity()
    check_scalar_unitarity_and_watson_bookkeeping()
    print("All factorized-scattering algebra checks passed.")


if __name__ == "__main__":
    main()
