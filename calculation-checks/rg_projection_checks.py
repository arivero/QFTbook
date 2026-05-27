#!/usr/bin/env python3
"""Exact finite checks for projected RG fixed-point warnings.

The Volume XI rigorous-RG chapter uses these two-dimensional examples to
separate projected fixed points from theorem-level fixed points of the full
Banach-space RG map.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def project(vector):
    return (vector[0], Fraction(0))


def complement(vector):
    return (Fraction(0), vector[1])


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def sub(left, right):
    return (left[0] - right[0], left[1] - right[1])


def norm_l1(vector):
    return abs(vector[0]) + abs(vector[1])


def check_spurious_projected_zero():
    def residual(point):
        _x, _y = point
        return (Fraction(0), Fraction(1))

    for x_value in [Fraction(-2), Fraction(0), Fraction(5, 3)]:
        point = (x_value, Fraction(0))
        assert_equal(
            "projected residual vanishes",
            project(residual(point)),
            (Fraction(0), Fraction(0)),
        )
        assert_true(
            "full residual remains nonzero",
            residual(point) != (Fraction(0), Fraction(0)),
        )


def check_projected_zero_lift_condition():
    epsilon = Fraction(1, 10)

    def residual(point):
        x_value, y_value = point
        return (x_value, y_value - epsilon)

    projected_zero = (Fraction(0), Fraction(0))
    assert_equal(
        "projected equation",
        project(residual(projected_zero)),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "complement residual",
        norm_l1(complement(residual(projected_zero))),
        epsilon,
    )

    # For this linear example A is the identity, rho=L=0, and the true zero
    # lies exactly at distance epsilon from the projected zero.
    radius = epsilon
    rho = Fraction(0)
    lipschitz = Fraction(0)
    assert_true(
        "Newton-Kantorovich projected lift inequality",
        epsilon + rho * radius + lipschitz * radius * radius / 2 <= radius,
    )
    true_zero = (Fraction(0), epsilon)
    assert_equal(
        "full residual at lifted zero",
        residual(true_zero),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "distance from projected zero",
        norm_l1(sub(true_zero, projected_zero)),
        radius,
    )

    # The projected-zero residual decomposes into P and Q parts exactly.
    full_residual = residual(projected_zero)
    assert_equal(
        "P plus Q decomposition",
        add(project(full_residual), complement(full_residual)),
        full_residual,
    )


def check_irrelevant_tail_residual():
    # Model B = R^1 + K with a finite irrelevant tail K = R^3.
    # The projected local equation vanishes at g=0, but the tail residual is
    # nonzero unless the kernel coordinate is solved as part of the full fixed
    # point equation.
    local_residual = Fraction(0)
    tail_residual = (Fraction(1, 2), Fraction(-1, 3), Fraction(1, 5))
    assert_equal("projected local residual", local_residual, 0)
    assert_true("irrelevant tail residual is nonzero", norm_l1(tail_residual[:2]) + abs(tail_residual[2]) > 0)

    # If the irrelevant equation is linear K' = lambda K + c with |lambda|<1,
    # the exact graph solution is K*=c/(1-lambda).  This is the finite algebra
    # behind solving the irrelevant tail by contraction rather than dropping it.
    lambdas = (Fraction(1, 2), Fraction(1, 3), Fraction(-1, 4))
    graph_solution = tuple(c / (1 - lam) for c, lam in zip(tail_residual, lambdas))
    residual_after_graph = tuple(lam * k + c - k for k, c, lam in zip(graph_solution, tail_residual, lambdas))
    assert_equal(
        "irrelevant graph residual",
        residual_after_graph,
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def main():
    check_spurious_projected_zero()
    check_projected_zero_lift_condition()
    check_irrelevant_tail_residual()
    print("All RG projection checks passed.")


if __name__ == "__main__":
    main()
