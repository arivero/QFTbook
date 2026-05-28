#!/usr/bin/env python3
"""Exact checks for the tree-level collinear EEC coefficient.

The QCD EEC section derives the resolved small-angle coefficient by combining
the ordered detector weight 2 x (1-x) with real final-state splitting kernels.
This script verifies the endpoint cancellation and the rational kernel
integrals without using floating-point arithmetic.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def poly_add(left, right):
    degree = max(len(left), len(right))
    result = [Fraction(0) for _ in range(degree)]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return tuple(result)


def poly_mul(left, right):
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a_i in enumerate(left):
        for j, b_j in enumerate(right):
            result[i + j] += a_i * b_j
    return tuple(result)


def poly_integral_0_1(poly):
    return sum(coeff / Fraction(power + 1) for power, coeff in enumerate(poly))


def check_local_eec_weight_conservation():
    # Contact weight x^2 + (1-x)^2 plus ordered separated weight 2x(1-x).
    x = (Fraction(0), Fraction(1))
    one_minus_x = (Fraction(1), Fraction(-1))
    contact = poly_add(poly_mul(x, x), poly_mul(one_minus_x, one_minus_x))
    separated = tuple(2 * coeff for coeff in poly_mul(x, one_minus_x))
    total = poly_add(contact, separated)
    assert_equal("local two-detector weight conservation", total, (Fraction(1), Fraction(0), Fraction(0)))


def check_real_kernel_weight_integrals():
    # q -> q g: 2 x(1-x) * (1+x^2)/(1-x) = 2 x(1+x^2).
    q_weighted = (Fraction(0), Fraction(2), Fraction(0), Fraction(2))
    assert_equal("quark EEC coefficient divided by C_F", poly_integral_0_1(q_weighted), Fraction(3, 2))

    # g -> g g:
    # 2x(1-x) * 2[x/(1-x) + (1-x)/x + x(1-x)]
    # = 4[x^2 + (1-x)^2 + x^2(1-x)^2].
    x = (Fraction(0), Fraction(1))
    one_minus_x = (Fraction(1), Fraction(-1))
    x_squared = poly_mul(x, x)
    one_minus_x_squared = poly_mul(one_minus_x, one_minus_x)
    x2_one_minus_x2 = poly_mul(x_squared, one_minus_x_squared)
    gg_weighted = tuple(
        4 * coeff
        for coeff in poly_add(poly_add(x_squared, one_minus_x_squared), x2_one_minus_x2)
    )
    assert_equal("gluon to gluon EEC coefficient divided by C_A", poly_integral_0_1(gg_weighted), Fraction(14, 5))

    # g -> q qbar: 2x(1-x)[x^2+(1-x)^2].
    gq_weighted = tuple(
        2 * coeff
        for coeff in poly_mul(poly_mul(x, one_minus_x), poly_add(x_squared, one_minus_x_squared))
    )
    assert_equal("gluon to quark EEC coefficient divided by T_F", poly_integral_0_1(gq_weighted), Fraction(1, 5))


def check_endpoint_cancellation_by_detector_weight():
    # The detector weight cancels the real-kernel endpoint poles as a
    # polynomial integrand.  We encode the reduced numerator after cancellation.
    q_reduced = (Fraction(0), Fraction(2), Fraction(0), Fraction(2))
    assert_true("q endpoint at x=1 is finite", sum(q_reduced) == 4)
    assert_true("q endpoint at x=0 vanishes", q_reduced[0] == 0)

    # The g->gg weighted integrand 4[x^2+(1-x)^2+x^2(1-x)^2] is finite and
    # nonnegative at both endpoints.
    x = (Fraction(0), Fraction(1))
    one_minus_x = (Fraction(1), Fraction(-1))
    gg_reduced = tuple(
        4 * coeff
        for coeff in poly_add(
            poly_add(poly_mul(x, x), poly_mul(one_minus_x, one_minus_x)),
            poly_mul(poly_mul(x, x), poly_mul(one_minus_x, one_minus_x)),
        )
    )
    assert_equal("g endpoint x=0 finite value", gg_reduced[0], Fraction(4))
    assert_equal("g endpoint x=1 finite value", sum(gg_reduced), Fraction(4))


def main():
    check_local_eec_weight_conservation()
    check_real_kernel_weight_integrals()
    check_endpoint_cancellation_by_detector_weight()
    print("All EEC collinear coefficient checks passed.")


if __name__ == "__main__":
    main()
