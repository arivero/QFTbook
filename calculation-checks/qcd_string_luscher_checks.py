#!/usr/bin/env python3
"""Exact coefficient checks for the QCD-string Luscher-term section."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def check_open_and_closed_casimir_coefficients() -> None:
    zeta_minus_one = Fraction(-1, 12)

    # One open Dirichlet scalar has E = (pi/(2 L)) zeta_R(-1).
    open_per_scalar = Fraction(1, 2) * zeta_minus_one
    assert_equal("open Luscher coefficient per transverse scalar", open_per_scalar, Fraction(-1, 24))

    # One periodic closed scalar has two oscillators for each n >= 1, so
    # E = (2 pi/L) zeta_R(-1).
    closed_per_scalar = Fraction(2, 1) * zeta_minus_one
    assert_equal("closed Luscher coefficient per transverse scalar", closed_per_scalar, Fraction(-1, 6))


def check_nambu_goto_reference_expansion() -> None:
    # The expansion sqrt(1 - x) = 1 - x/2 - x^2/8 + O(x^3) is applied to
    # x_open = pi c/(12 sigma L^2) and x_closed = pi c/(3 sigma L^2).
    open_luscher_denominator = Fraction(2, 1) * 12
    open_l3_denominator = Fraction(8, 1) * 12 * 12
    assert_equal("open NG 1/L coefficient denominator", Fraction(-1, open_luscher_denominator), Fraction(-1, 24))
    assert_equal("open NG 1/L^3 coefficient denominator", Fraction(-1, open_l3_denominator), Fraction(-1, 1152))

    closed_luscher_denominator = Fraction(2, 1) * 3
    closed_l3_denominator = Fraction(8, 1) * 3 * 3
    assert_equal("closed NG 1/L coefficient denominator", Fraction(-1, closed_luscher_denominator), Fraction(-1, 6))
    assert_equal("closed NG 1/L^3 coefficient denominator", Fraction(-1, closed_l3_denominator), Fraction(-1, 72))


def main() -> None:
    check_open_and_closed_casimir_coefficients()
    check_nambu_goto_reference_expansion()
    print("All QCD-string Luscher-term checks passed.")


if __name__ == "__main__":
    main()
