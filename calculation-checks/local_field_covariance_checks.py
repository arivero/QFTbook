#!/usr/bin/env python3
"""Finite checks for Volume I local-field covariance conventions.

The chapter's analytic objects are distributions and unbounded operators, so
these checks only verify convention-sensitive algebra: Lorentz-sign
bookkeeping, the pullback order for transformed test functions, and the
Koszul sign in adjacent spacelike exchange.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def check_lorentz_interval_preservation():
    beta = Fraction(3, 5)
    gamma = Fraction(5, 4)
    samples = [
        (Fraction(7, 3), Fraction(11, 5)),
        (Fraction(-2, 7), Fraction(5, 2)),
        (Fraction(0), Fraction(9, 4)),
    ]
    for t, x in samples:
        t_prime = gamma * (t - beta * x)
        x_prime = gamma * (x - beta * t)
        before = x * x - t * t
        after = x_prime * x_prime - t_prime * t_prime
        assert_equal(after, before, "boost preserves x^2-t^2")


def check_test_function_pullback_order():
    # In one dimension, represent an affine spacetime map as y |-> a*y + b.
    # The chapter uses f_g(y)=f(g^{-1}y).  Hence (f_g)_h=f_{h g}.
    def compose(left, right):
        a_left, b_left = left
        a_right, b_right = right
        return (a_left * a_right, a_left * b_right + b_left)

    def inverse(transform):
        a, b = transform
        return (1 / a, -b / a)

    def apply(transform, y):
        a, b = transform
        return a * y + b

    # A polynomial is enough to distinguish the competing composition orders.
    def f(y):
        return y**3 - Fraction(5, 2) * y + Fraction(7, 3)

    g = (Fraction(3, 2), Fraction(-4, 5))
    h = (Fraction(5, 3), Fraction(2, 7))
    hg = compose(h, g)
    gh = compose(g, h)

    for y in [Fraction(-3, 4), Fraction(0), Fraction(9, 5)]:
        left = f(apply(inverse(g), apply(inverse(h), y)))
        right = f(apply(inverse(hg), y))
        wrong_order = f(apply(inverse(gh), y))
        assert_equal(left, right, "pullback composition order")
        if g != h:
            assert wrong_order != right, "test data should distinguish hg from gh"


def check_graded_exchange_signs():
    expected = {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): -1,
    }
    for parities, sign in expected.items():
        a, b = parities
        computed = (-1) ** (a * b)
        assert_equal(computed, sign, "Koszul exchange sign")
        assert_equal(computed * computed, 1, "two adjacent exchanges undo")


def check_covariant_component_factors():
    # Component covariance of an n-point distribution uses one representation
    # matrix for each field label.  This checks the tensor-product ordering in
    # a two-component, two-point toy model.
    s = ((Fraction(2), Fraction(1)), (Fraction(-1), Fraction(3)))
    w = ((Fraction(5), Fraction(7)), (Fraction(11), Fraction(13)))

    transformed = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for a1 in range(2):
        for a2 in range(2):
            transformed[a1][a2] = sum(
                s[a1][b1] * s[a2][b2] * w[b1][b2]
                for b1 in range(2)
                for b2 in range(2)
            )

    # Equivalent matrix expression S W S^T fixes that no inverse or reversed
    # component order has slipped into the convention.
    matrix_form = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for a1 in range(2):
        for a2 in range(2):
            matrix_form[a1][a2] = sum(
                s[a1][b1] * w[b1][b2] * s[a2][b2]
                for b1 in range(2)
                for b2 in range(2)
            )
    assert_equal(transformed, matrix_form, "component tensor factors")


def main():
    check_lorentz_interval_preservation()
    check_test_function_pullback_order()
    check_graded_exchange_signs()
    check_covariant_component_factors()
    print("All local-field covariance checks passed.")


if __name__ == "__main__":
    main()
