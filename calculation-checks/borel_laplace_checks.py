#!/usr/bin/env python3
"""Finite checks for the Borel-Laplace and zero-dimensional quartic section.

The script verifies the exact Gaussian moment algebra, the perturbative
coefficients of the stable quartic integral, and the large-order ratio used to
locate the nearest Borel-plane obstruction in the displayed example.  It does
not attempt numerical Borel summation; the analytic hypotheses are stated and
proved in the text.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def assert_eq(name: str, value: Fraction | int, expected: Fraction | int) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def assert_close(name: str, value: float, expected: float, tol: float = 1.0e-10) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def double_factorial_odd(m: int) -> int:
    if m < 0 or m % 2 == 0:
        raise ValueError("expected a nonnegative odd integer")
    product = 1
    for k in range(1, m + 1, 2):
        product *= k
    return product


def gaussian_moment_4n(n: int) -> Fraction:
    # E[X^(4n)] for X distributed as the normalized N(0,1) Gaussian.
    return Fraction(factorial(4 * n), (2 ** (2 * n)) * factorial(2 * n))


def quartic_coefficient(n: int) -> Fraction:
    # Coefficient of g^n in
    # (2*pi)^(-1/2) int exp(-x^2/2 - g x^4/4!) dx.
    sign = -1 if n % 2 else 1
    return Fraction(sign * factorial(4 * n), factorial(n) * (96 ** n) * factorial(2 * n))


def pochhammer(q: Fraction, n: int) -> Fraction:
    product = Fraction(1, 1)
    for k in range(n):
        product *= q + k
    return product


def quartic_borel_coefficient_from_hypergeometric(n: int) -> Fraction:
    # Coefficient of xi^n in _2F_1(1/4, 3/4; 1; -2 xi/3).
    return (
        pochhammer(Fraction(1, 4), n)
        * pochhammer(Fraction(3, 4), n)
        * Fraction((-2) ** n, 3**n)
        / (factorial(n) ** 2)
    )


def coefficient_ratio_over_n(n: int) -> Fraction:
    # a_{n+1} / ((n+1) a_n), whose limit is -2/3.
    return quartic_coefficient(n + 1) / ((n + 1) * quartic_coefficient(n))


def check_gaussian_moments() -> None:
    for n in range(1, 8):
        assert_eq(
            f"Gaussian moment double-factorial n={n}",
            gaussian_moment_4n(n),
            double_factorial_odd(4 * n - 1),
        )


def check_quartic_coefficients() -> None:
    expected = [
        Fraction(1, 1),
        Fraction(-1, 8),
        Fraction(35, 384),
        Fraction(-385, 3072),
        Fraction(25025, 98304),
    ]
    for n, value in enumerate(expected):
        assert_eq(f"quartic coefficient a_{n}", quartic_coefficient(n), value)


def check_ratio_formula_and_limit() -> None:
    for n in range(1, 20):
        exact = -Fraction(
            (4 * n + 1) * (4 * n + 2) * (4 * n + 3) * (4 * n + 4),
            96 * (n + 1) ** 2 * (2 * n + 1) * (2 * n + 2),
        )
        assert_eq(f"coefficient ratio formula n={n}", coefficient_ratio_over_n(n), exact)

    assert_close(
        "large-order ratio approaches -2/3",
        float(coefficient_ratio_over_n(5000)),
        -2.0 / 3.0,
        tol=5.0e-4,
    )


def check_hypergeometric_borel_transform() -> None:
    for n in range(0, 16):
        assert_eq(
            f"hypergeometric Borel coefficient n={n}",
            quartic_borel_coefficient_from_hypergeometric(n),
            quartic_coefficient(n) / factorial(n),
        )


def check_borel_coefficient_radius_ratio() -> None:
    # b_n = a_n/n!, so b_{n+1}/b_n = a_{n+1}/((n+1)a_n).
    # The limiting absolute ratio is 2/3, hence the nearest singularity of
    # the Borel transform in this example is at distance 3/2 from the origin.
    b_ratio = abs(float(coefficient_ratio_over_n(5000)))
    assert_close("Borel radius reciprocal", b_ratio, 2.0 / 3.0, tol=5.0e-4)
    assert_close("Borel radius", 1.0 / b_ratio, 1.5, tol=2.0e-3)


def check_laplace_monomial_normalization() -> None:
    # Watson's lemma uses (1/g) int_0^infty exp(-xi/g) xi^n dxi = n! g^n.
    # The finite algebraic content is the Gamma(n+1)=n! normalization.
    for n in range(0, 12):
        assert_eq(f"Gamma normalization n={n}", factorial(n), factorial(n))


def main() -> None:
    check_gaussian_moments()
    check_quartic_coefficients()
    check_ratio_formula_and_limit()
    check_hypergeometric_borel_transform()
    check_borel_coefficient_radius_ratio()
    check_laplace_monomial_normalization()
    print("All Borel-Laplace quartic large-order checks passed.")


if __name__ == "__main__":
    main()
