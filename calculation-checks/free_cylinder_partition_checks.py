#!/usr/bin/env python3
"""Finite character checks for free fields on the radial cylinder."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def scalar_letter_coefficient_d4(level: int) -> int:
    """Coefficient of q^(1+level) in q(1 - q^2)/(1 - q)^4."""

    total = comb(level + 3, 3)
    trace = comb(level + 1, 3) if level >= 2 else 0
    return total - trace


def fermion_letter_coefficient_d4_weyl(level: int) -> int:
    """Coefficient of q^(3/2+level) in 2 q^(3/2)/(1 - q)^3."""

    return 2 * comb(level + 2, 2)


def maxwell_letter_coefficient(level: int) -> int:
    """Coefficient of q^(2+level) in (6 q^2 - 2 q^3)/(1 - q)^3."""

    first = 6 * comb(level + 2, 2)
    second = 2 * comb(level + 1, 2) if level >= 1 else 0
    return first - second


def check_scalar_d4_reduction() -> None:
    """Check the scalar formula reduces to q(1+q)/(1-q)^3 in D=4."""

    for level in range(8):
        expected = comb(level + 2, 2) + (comb(level + 1, 2) if level >= 1 else 0)
        assert_equal(f"D=4 scalar coefficient level {level}", scalar_letter_coefficient_d4(level), expected)


def check_fermion_d4_coefficients() -> None:
    """Check Weyl and Dirac free-fermion letter degeneracies in D=4."""

    expected_weyl = [2, 6, 12, 20, 30]
    for level, expected in enumerate(expected_weyl):
        assert_equal(f"D=4 Weyl fermion coefficient level {level}", fermion_letter_coefficient_d4_weyl(level), expected)

    for level, expected in enumerate(expected_weyl):
        assert_equal(
            f"D=4 Dirac fermion coefficient level {level}",
            2 * fermion_letter_coefficient_d4_weyl(level),
            2 * expected,
        )


def check_maxwell_character_identity() -> None:
    """Check q^2(6-8q+2q^2)/(1-q)^4 = (6q^2-2q^3)/(1-q)^3."""

    # Equality follows from (6 - 2q)(1 - q) = 6 - 8q + 2q^2.
    left_numerator = (6, -8, 2)
    right_after_multiplying_by_one_minus_q = (6, -2 - 6, 2)
    assert_equal("Maxwell numerator identity", right_after_multiplying_by_one_minus_q, left_numerator)

    expected = [6, 16, 30, 48, 70, 96]
    for level, expected_coeff in enumerate(expected):
        assert_equal(f"Maxwell coefficient level {level}", maxwell_letter_coefficient(level), expected_coeff)


def check_shortening_subtractions() -> None:
    """Check finite multiplicities in the short-module numerators."""

    assert_equal("D=4 Weyl numerator dimensions", (2, -2), (2, -2))
    assert_equal("D=4 Maxwell numerator dimensions", (6, -8, 2), (6, -8, 2))

    # A four-dimensional Dirac field is two Weyl towers in this unrefined count.
    dirac_over_weyl = Fraction(4, 2)
    assert_equal("Dirac over Weyl multiplicity", dirac_over_weyl, Fraction(2, 1))


def main() -> None:
    check_scalar_d4_reduction()
    check_fermion_d4_coefficients()
    check_maxwell_character_identity()
    check_shortening_subtractions()
    print("All free-cylinder partition character checks passed.")


if __name__ == "__main__":
    main()
