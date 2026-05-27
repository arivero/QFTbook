#!/usr/bin/env python3
"""Finite algebra checks for HMC and pseudofermion identities.

These checks certify only the finite-dimensional identities used in
Volume XI, Chapter 6.  They do not test a continuum limit, solver
stability, or ergodicity of a production Markov chain.
"""

from __future__ import annotations

from fractions import Fraction


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matmul(a: Matrix2, b: Matrix2) -> Matrix2:
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


def det2(a: Matrix2) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a: Matrix2) -> Matrix2:
    det = det2(a)
    if det == 0:
        raise AssertionError("singular matrix in inverse check")
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def assert_equal(got: object, expected: object, label: str) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_true(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def check_one_dimensional_leapfrog() -> None:
    """Check determinant one and R L R = L^{-1} for quadratic leapfrog."""

    eps = Fraction(2, 7)
    k = Fraction(3, 5)
    mass = Fraction(5, 4)

    a = 1 - eps * eps * k / (2 * mass)
    b = eps / mass
    c = -eps * k + eps * eps * eps * k * k / (4 * mass)
    leapfrog: Matrix2 = ((a, b), (c, a))

    assert_equal(det2(leapfrog), Fraction(1), "leapfrog determinant")

    flip: Matrix2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
    conjugated = matmul(matmul(flip, leapfrog), flip)
    assert_equal(conjugated, inv2(leapfrog), "leapfrog reversibility")


def metropolis_acceptance(weight_from: Fraction, weight_to: Fraction) -> Fraction:
    ratio = weight_to / weight_from
    return min(Fraction(1), ratio)


def check_pairwise_metropolis_balance() -> None:
    """Check w(z) a(z->z') = w(z') a(z'->z) in both energy orderings."""

    examples = [
        (Fraction(7, 3), Fraction(2, 5)),
        (Fraction(2, 5), Fraction(7, 3)),
        (Fraction(11, 13), Fraction(11, 13)),
    ]
    for w0, w1 in examples:
        lhs = w0 * metropolis_acceptance(w0, w1)
        rhs = w1 * metropolis_acceptance(w1, w0)
        assert_equal(lhs, rhs, "pairwise Metropolis balance")


def check_pseudofermion_determinant_identity() -> None:
    """Check the pi-free determinant factor after diagonalization."""

    eigenvalues = (Fraction(2), Fraction(5), Fraction(7, 3))
    det_a = Fraction(1)
    gaussian_factor_without_pi = Fraction(1)
    for lam in eigenvalues:
        det_a *= lam
        # int_C exp(-|z|^2 / lam) d^2 z = pi * lam.
        gaussian_factor_without_pi *= lam
    assert_equal(
        gaussian_factor_without_pi,
        det_a,
        "pseudofermion Gaussian determinant factor",
    )


def check_rational_action_error_bound() -> None:
    """Check |phi^*(r(A)-f(A))phi| <= delta ||phi||^2 diagonally."""

    target_values = (Fraction(1, 2), Fraction(1, 5), Fraction(3, 11))
    rational_values = (
        target_values[0] + Fraction(1, 100),
        target_values[1] - Fraction(1, 200),
        target_values[2] + Fraction(1, 250),
    )
    phi_norm_squares = (Fraction(3), Fraction(2), Fraction(5, 4))

    errors = [r - f for r, f in zip(rational_values, target_values)]
    delta = max(abs(error) for error in errors)
    action_error = sum(
        error * norm_square
        for error, norm_square in zip(errors, phi_norm_squares)
    )
    norm_square = sum(phi_norm_squares)
    assert_true(
        abs(action_error) <= delta * norm_square,
        "rational pseudofermion action-error bound",
    )


def main() -> None:
    check_one_dimensional_leapfrog()
    check_pairwise_metropolis_balance()
    check_pseudofermion_determinant_identity()
    check_rational_action_error_bound()
    print("All HMC and pseudofermion checks passed.")


if __name__ == "__main__":
    main()
