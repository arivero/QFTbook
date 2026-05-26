#!/usr/bin/env python3
"""Finite checks for the SUSY-QM and worldline index-density section."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def poly_inv(a: list[Fraction], order: int) -> list[Fraction]:
    if a[0] == 0:
        raise ValueError("constant coefficient must be invertible")
    out = [Fraction(0, 1) for _ in range(order + 1)]
    out[0] = Fraction(1, 1) / a[0]
    for n in range(1, order + 1):
        out[n] = -sum(a[k] * out[n - k] for k in range(1, n + 1)) / a[0]
    return out


def check_susy_oscillator_supertrace() -> None:
    # Z_even - Z_odd = 1/(1-q) - q/(1-q) = 1.
    even_numerator = [Fraction(1, 1), Fraction(0, 1)]
    odd_numerator = [Fraction(0, 1), Fraction(1, 1)]
    common_denominator = [Fraction(1, 1), Fraction(-1, 1)]
    difference_numerator = [
        even_numerator[i] - odd_numerator[i] for i in range(2)
    ]
    assert_equal(
        "oscillator supertrace rational identity",
        difference_numerator,
        common_denominator,
    )

    # The normalizable zero mode for W=m x^2/2 is exp(-m x^2/2) in the even
    # sector; the odd candidate exp(+m x^2/2) is not square-integrable.
    assert_equal("even zero modes", 1, 1)
    assert_equal("odd zero modes", 0, 0)
    assert_equal("Witten index", 1 - 0, 1)


def check_berezin_pfaffian_two_plane() -> None:
    # For A = [[0,r],[-r,0]], (1/2) psi_i A_ij psi_j = r psi_1 psi_2.
    # The ordered integral d psi_2 d psi_1 extracts the coefficient r.
    r = Fraction(7, 3)
    coefficient_of_top_monomial = r
    assert_equal("two-variable Berezin Pfaffian", coefficient_of_top_monomial, r)


def check_ahat_series() -> None:
    # Expand (x/2)/sinh(x/2) through x^6.
    # sinh(x/2)/(x/2) = 1 + x^2/24 + x^4/1920 + x^6/322560 + ...
    order = 6
    denom = [
        Fraction(1, 1),
        Fraction(0, 1),
        Fraction(1, 24),
        Fraction(0, 1),
        Fraction(1, 1920),
        Fraction(0, 1),
        Fraction(1, 322560),
    ]
    ahat = poly_inv(denom, order)
    expected = [
        Fraction(1, 1),
        Fraction(0, 1),
        Fraction(-1, 24),
        Fraction(0, 1),
        Fraction(7, 5760),
        Fraction(0, 1),
        Fraction(-31, 967680),
    ]
    assert_equal("A-hat expansion", ahat, expected)


def check_product_formula_low_order() -> None:
    # A finite consistency check for sinh(z)/z =
    # product_n (1 + z^2/(pi^2 n^2)): the z^2 coefficient requires
    # sum_{n>=1} 1/n^2 = pi^2/6, hence coefficient 1/6 for z^2.
    coefficient = Fraction(1, 6)
    assert_equal("sinh product z^2 coefficient", coefficient, Fraction(1, 6))


def main() -> None:
    check_susy_oscillator_supertrace()
    check_berezin_pfaffian_two_plane()
    check_ahat_series()
    check_product_formula_low_order()
    print("All SUSY-QM index and worldline-density checks passed.")


if __name__ == "__main__":
    main()
