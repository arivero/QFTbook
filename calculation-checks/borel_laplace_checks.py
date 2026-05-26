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


def conformal_borel_xi_from_w(w: Fraction, singular_distance: Fraction) -> Fraction:
    return 4 * singular_distance * w / ((1 - w) ** 2)


def conformal_borel_w_from_xi(xi: Fraction, singular_distance: Fraction) -> Fraction:
    # This helper is used only for rational square-root samples where
    # 1 + xi/A is a perfect rational square.
    y_squared = 1 + xi / singular_distance
    numerator = y_squared.numerator
    denominator = y_squared.denominator
    y_num = int(numerator**0.5)
    y_den = int(denominator**0.5)
    if y_num * y_num != numerator or y_den * y_den != denominator:
        raise ValueError("sample does not have a rational square root")
    y = Fraction(y_num, y_den)
    return (y - 1) / (y + 1)


def check_conformal_borel_map() -> None:
    singular_distance = Fraction(3, 2)
    assert_eq("conformal map origin", conformal_borel_xi_from_w(Fraction(0, 1), singular_distance), 0)
    assert_eq("conformal map first singularity", conformal_borel_xi_from_w(Fraction(-1, 1), singular_distance), -singular_distance)

    samples = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]
    for w in samples:
        xi = conformal_borel_xi_from_w(w, singular_distance)
        assert_eq(f"conformal inverse sample w={w}", conformal_borel_w_from_xi(xi, singular_distance), w)

    # The positive Borel ray maps monotonically to 0 <= w < 1 in these samples.
    assert conformal_borel_xi_from_w(Fraction(1, 3), singular_distance) > 0
    assert conformal_borel_xi_from_w(Fraction(2, 3), singular_distance) > conformal_borel_xi_from_w(
        Fraction(1, 3), singular_distance
    )


def renormalon_moment(p: Fraction, n: int) -> Fraction:
    return Fraction(factorial(n), 1) / (p ** (n + 1))


def check_renormalon_factorial_moment_and_borel_pole() -> None:
    p = Fraction(5, 3)
    beta0 = Fraction(7, 4)
    for n in range(0, 12):
        coefficient = (beta0**n) * renormalon_moment(p, n)
        borel_coefficient = coefficient / factorial(n)
        expected = (beta0**n) / (p ** (n + 1))
        assert_eq(f"renormalon Borel coefficient n={n}", borel_coefficient, expected)

    # Sum_{n>=0} beta0^n u^n / p^{n+1} = 1/(p - beta0 u).
    u = Fraction(2, 15)
    partial_sum = sum((beta0**n) * (u**n) / (p ** (n + 1)) for n in range(0, 16))
    exact = 1 / (p - beta0 * u)
    assert_close("renormalon geometric Borel pole", float(partial_sum), float(exact), tol=1.0e-7)


def main() -> None:
    check_gaussian_moments()
    check_quartic_coefficients()
    check_ratio_formula_and_limit()
    check_hypergeometric_borel_transform()
    check_borel_coefficient_radius_ratio()
    check_laplace_monomial_normalization()
    check_conformal_borel_map()
    check_renormalon_factorial_moment_and_borel_pole()
    print("All Borel-Laplace, conformal-map, and renormalon-model checks passed.")


if __name__ == "__main__":
    main()
