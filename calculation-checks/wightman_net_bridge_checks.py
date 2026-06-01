#!/usr/bin/env python3
"""Finite checks for the Wightman-to-local-net comparison discussion.

The script verifies only the bounded finite-dimensional algebra used as a
diagnostic in Volume IV, Chapter 3.  It does not assert any general
Wightman-to-AQFT theorem.
"""

from __future__ import annotations

from fractions import Fraction

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def add(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def sub(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] - b[0][0], a[0][1] - b[0][1]),
        (a[1][0] - b[1][0], a[1][1] - b[1][1]),
    )


def scale(c: Fraction, a: Matrix) -> Matrix:
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def assert_eq(got: Matrix, expected: Matrix, msg: str) -> None:
    if got != expected:
        raise AssertionError(f"{msg}: got {got}, expected {expected}")


zero: Matrix = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
one: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
parity: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
odd_field: Matrix = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))

half = Fraction(1, 2)
proj_plus = scale(half, add(one, odd_field))
proj_minus = scale(half, sub(one, odd_field))
even_plus = scale(half, add(one, parity))
even_minus = scale(half, sub(one, parity))


def average_over_z2(a: Matrix) -> Matrix:
    """Conditional expectation onto the fixed-point algebra."""
    return scale(half, add(a, matmul(matmul(parity, a), parity)))


def span_coefficients(a: Matrix) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return coefficients in the basis 1, P, X, PX."""
    px = matmul(parity, odd_field)
    # For [[a,b],[c,d]], coefficients are
    # alpha+beta=a, alpha-beta=d, gamma+delta=b, gamma-delta=-c.
    alpha = half * (a[0][0] + a[1][1])
    beta = half * (a[0][0] - a[1][1])
    gamma = half * (a[0][1] + a[1][0])
    delta = half * (a[0][1] - a[1][0])
    reconstructed = add(add(scale(alpha, one), scale(beta, parity)),
                        add(scale(gamma, odd_field), scale(delta, px)))
    assert_eq(reconstructed, a, "basis reconstruction")
    return alpha, beta, gamma, delta


def main() -> None:
    assert_eq(matmul(parity, parity), one, "parity squares to one")
    assert_eq(matmul(odd_field, odd_field), one, "odd field squares to one")
    assert_eq(matmul(matmul(parity, odd_field), parity),
              scale(Fraction(-1), odd_field),
              "odd field changes sign under parity")

    assert_eq(matmul(proj_plus, proj_plus), proj_plus, "P_+^X idempotent")
    assert_eq(matmul(proj_minus, proj_minus), proj_minus, "P_-^X idempotent")
    assert_eq(add(proj_plus, proj_minus), one, "odd spectral projections sum to one")

    assert_eq(matmul(matmul(parity, proj_plus), parity), proj_minus,
              "parity exchanges odd-field spectral projections")
    assert_eq(average_over_z2(odd_field), zero, "conditional expectation kills odd field")
    assert_eq(average_over_z2(parity), parity, "conditional expectation preserves even field")
    assert_eq(average_over_z2(proj_plus), scale(half, one),
              "odd spectral projection is not an observable projection")

    # The fixed-point algebra consists of the diagonal span of 1 and parity.
    for observable in (one, parity, even_plus, even_minus):
        coeffs = span_coefficients(observable)
        if coeffs[2] != 0 or coeffs[3] != 0:
            raise AssertionError("fixed-point observable has odd component")

    # Adding the odd-field spectral projections recovers the odd generator and
    # hence the full two-by-two field algebra once the even parity operator is
    # also present.
    recovered_x = sub(proj_plus, proj_minus)
    assert_eq(recovered_x, odd_field, "odd field recovered from spectral projections")
    px = matmul(parity, odd_field)
    basis = (one, parity, odd_field, px)
    for b in basis:
        span_coefficients(b)

    # Strong locality is a spectral-projection statement.  Commuting
    # self-adjoint generators have commuting projections; the odd and parity
    # generators do not.
    assert_eq(comm(even_plus, even_minus), zero, "even spectral projections commute")
    if comm(proj_plus, even_plus) == zero:
        raise AssertionError("noncommuting field/observable projections incorrectly commute")

    print("All Wightman-to-net bridge finite-algebra checks passed.")


if __name__ == "__main__":
    main()
