#!/usr/bin/env python3
"""Symbolic checks for the QCD Borel/Laplace current-sum-rule block.

These checks verify the algebra used in Volume II, Chapter 19:

1. The Borel transform of the subtracted dispersion kernel is
   exp(-s/M2)/M2.
2. Subtraction polynomials are annihilated once the derivative order is
   larger than the degree.
3. Inverse powers (Q2)^(-m) map to 1/((m-1)! (M2)^m).
4. The logarithmic Borel mass estimator is the spectral weighted average of
   the retained squared masses.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{name}: got {simplified!r}, expected 0")


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def check_borel_dispersion_kernel() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    s, m2 = sp.symbols("s m2", positive=True)
    q2 = n * m2
    nth_kernel = n * q2**n / (s + q2) ** (n + 1)
    limit = sp.limit(nth_kernel, n, sp.oo)
    assert_zero("Borel dispersion kernel", limit - sp.exp(-s / m2) / m2)


def check_polynomial_subtractions_are_killed() -> None:
    q2 = sp.symbols("q2")
    polynomial = 7 * q2**4 - 3 * q2**2 + 11
    killed = sp.diff(polynomial, q2, 5)
    assert_zero("subtraction polynomial killed", killed)


def check_inverse_power_borel_transform() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    m2 = sp.symbols("m2", positive=True)
    for power in range(1, 7):
        expression = (
            sp.gamma(power + n)
            / (sp.gamma(power) * sp.gamma(n))
            * (n * m2) ** (-power)
        )
        limit = sp.limit(expression, n, sp.oo)
        expected = 1 / (sp.factorial(power - 1) * m2**power)
        assert_zero(f"inverse power {power}", limit - expected)


def check_borel_mass_weighted_average() -> None:
    tau = sp.symbols("tau", positive=True)
    weights = [sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(11, 13)]
    masses_squared = [sp.Rational(3, 2), sp.Rational(5, 2), sp.Rational(7, 2)]
    spectral_sum = sum(
        weight * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    )
    estimator = -sp.diff(sp.log(spectral_sum), tau)
    weighted_average = sum(
        weight * mass_sq * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    ) / spectral_sum
    assert_zero("Borel mass weighted average", estimator - weighted_average)

    single_atom = weights[0] * sp.exp(-tau * masses_squared[0])
    assert_equal(
        "single atom mass estimator",
        sp.simplify(-sp.diff(sp.log(single_atom), tau)),
        masses_squared[0],
    )


def main() -> None:
    check_borel_dispersion_kernel()
    check_polynomial_subtractions_are_killed()
    check_inverse_power_borel_transform()
    check_borel_mass_weighted_average()
    print("All QCD Borel/Laplace sum-rule checks passed.")


if __name__ == "__main__":
    main()
