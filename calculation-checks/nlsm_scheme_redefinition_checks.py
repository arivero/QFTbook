#!/usr/bin/env python3
"""Finite checks for beta-vector-field scheme redefinitions."""

from __future__ import annotations

from fractions import Fraction


Monomial = tuple[int, int]
Polynomial = dict[Monomial, Fraction]
VectorField = tuple[Polynomial, Polynomial]


def clean(poly: Polynomial) -> Polynomial:
    return {monomial: coeff for monomial, coeff in poly.items() if coeff != 0}


def add(lhs: Polynomial, rhs: Polynomial, sign: int = 1) -> Polynomial:
    result = dict(lhs)
    for monomial, coeff in rhs.items():
        result[monomial] = result.get(monomial, Fraction(0)) + sign * coeff
    return clean(result)


def mul(lhs: Polynomial, rhs: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (lx, ly), left_coeff in lhs.items():
        for (rx, ry), right_coeff in rhs.items():
            monomial = (lx + rx, ly + ry)
            result[monomial] = result.get(monomial, Fraction(0)) + left_coeff * right_coeff
    return clean(result)


def deriv(poly: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for powers, coeff in poly.items():
        exponent = powers[variable]
        if exponent == 0:
            continue
        new_powers = list(powers)
        new_powers[variable] -= 1
        result[tuple(new_powers)] = coeff * exponent
    return clean(result)


def directional_derivative(vector: VectorField, target: Polynomial) -> Polynomial:
    return add(mul(vector[0], deriv(target, 0)), mul(vector[1], deriv(target, 1)))


def bracket(beta: VectorField, redefinition: VectorField) -> VectorField:
    return (
        add(
            directional_derivative(beta, redefinition[0]),
            directional_derivative(redefinition, beta[0]),
            sign=-1,
        ),
        add(
            directional_derivative(beta, redefinition[1]),
            directional_derivative(redefinition, beta[1]),
            sign=-1,
        ),
    )


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def main() -> None:
    # Couplings are (x,y).  This toy model checks the sign in
    # beta' = beta + [beta,F] to first order in the finite redefinition F.
    beta: VectorField = (
        {(2, 0): Fraction(1)},
        {(1, 1): Fraction(1)},
    )
    finite_redefinition: VectorField = (
        {(0, 2): Fraction(1)},
        {(2, 0): Fraction(1)},
    )
    expected: VectorField = (
        {},
        {(3, 0): Fraction(1), (0, 3): Fraction(-1)},
    )
    assert_equal(
        "finite-redefinition beta-vector bracket",
        bracket(beta, finite_redefinition),
        expected,
    )
    print("All NLSM scheme-redefinition checks passed.")


if __name__ == "__main__":
    main()
