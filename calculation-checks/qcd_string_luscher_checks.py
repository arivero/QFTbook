#!/usr/bin/env python3
"""Exact coefficient checks for the QCD-string effective-spectrum section."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def assert_less(name: str, left: Fraction, right: Fraction) -> None:
    if not left < right:
        raise AssertionError(f"{name} failed: expected {left} < {right}")


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


def colored_partition_degeneracies(colors: int, max_level: int) -> list[int]:
    coeffs = [0] * (max_level + 1)
    coeffs[0] = 1
    for mode in range(1, max_level + 1):
        for _ in range(colors):
            for level in range(mode, max_level + 1):
                coeffs[level] += coeffs[level - mode]
    return coeffs


def check_open_oscillator_degeneracies() -> None:
    # For D=4 there are two transverse colors.  The generating function is
    # product_{n >= 1} (1 - q^n)^(-2), whose first coefficients are displayed
    # in the monograph.
    assert colored_partition_degeneracies(colors=2, max_level=3) == [1, 2, 5, 10]


def check_excited_level_expansion_coefficients() -> None:
    c_perp = Fraction(2, 1)

    # Open NG:
    # E = sigma L + pi A/L - pi^2 A^2/(2 sigma L^3) + ...
    open_level = Fraction(3, 1)
    open_a = open_level - c_perp / 24
    assert_equal("open excited 1/L coefficient", open_a, Fraction(35, 12))
    assert_equal("open excited 1/L^3 coefficient without pi^2/sigma", -open_a * open_a / 2, Fraction(-1225, 288))

    # Closed NG:
    # E = sigma L + 2 pi A/L + 2 pi^2(q^2 - A^2)/(sigma L^3) + ...
    n_left = Fraction(3, 1)
    n_right = Fraction(1, 1)
    q_momentum = Fraction(2, 1)
    closed_a = n_left + n_right - c_perp / 12
    assert_equal("closed level matching", n_left - n_right, q_momentum)
    assert_equal("closed excited 1/L coefficient without pi", 2 * closed_a, Fraction(23, 3))
    assert_equal(
        "closed excited 1/L^3 coefficient without pi^2/sigma",
        2 * (q_momentum * q_momentum - closed_a * closed_a),
        Fraction(-385, 18),
    )


def steiner_length_squared_from_sides(
    sum_squares: Fraction,
    four_sqrt_three_area: Fraction,
) -> Fraction:
    """Return L_Y^2 = (a^2+b^2+c^2+4 sqrt(3) Delta)/2."""

    return (sum_squares + four_sqrt_three_area) / 2


def check_baryonic_y_string_geometry() -> None:
    # Equilateral side length a=1:
    # Delta = sqrt(3)/4, so 4 sqrt(3) Delta = 3.
    equilateral_sum_squares = Fraction(3, 1)
    equilateral_four_sqrt_three_area = Fraction(3, 1)
    equilateral_y_squared = steiner_length_squared_from_sides(
        equilateral_sum_squares,
        equilateral_four_sqrt_three_area,
    )
    assert_equal(
        "equilateral Y-string length squared",
        equilateral_y_squared,
        Fraction(3, 1),
    )

    # The pairwise Delta comparison length is (a+b+c)/2 = 3/2 for a=1.
    delta_squared = Fraction(9, 4)
    assert_less(
        "equilateral Delta comparison shorter than Y length",
        delta_squared,
        equilateral_y_squared,
    )

    # At the 120-degree boundary with adjacent sides 1,1 and opposite side
    # sqrt(3), the Steiner formula gives L_Y^2 = 4, matching the collapsed
    # two-side network of length 2.
    threshold_sum_squares = Fraction(1, 1) + Fraction(1, 1) + Fraction(3, 1)
    threshold_four_sqrt_three_area = Fraction(3, 1)
    threshold_y_squared = steiner_length_squared_from_sides(
        threshold_sum_squares,
        threshold_four_sqrt_three_area,
    )
    assert_equal(
        "120-degree collapsed Y-string length squared",
        threshold_y_squared,
        Fraction(4, 1),
    )


def check_hagedorn_coefficient() -> None:
    # The saddle gives beta_H^2 sigma = pi c/3.  For open strings one uses
    # log rho ~ 2 pi sqrt(c N/6) and E^2 ~ 2 pi sigma N.  For closed strings
    # one uses twice the entropy, log rho ~ 4 pi sqrt(c N/6), and
    # E^2 ~ 8 pi sigma N.  The rational coefficient multiplying pi c/sigma is
    # the same in both cases.
    open_coefficient = Fraction(4, 1) * Fraction(1, 6) / Fraction(2, 1)
    closed_coefficient = Fraction(16, 1) * Fraction(1, 6) / Fraction(8, 1)
    assert_equal("open Hagedorn beta coefficient", open_coefficient, Fraction(1, 3))
    assert_equal("closed Hagedorn beta coefficient", closed_coefficient, Fraction(1, 3))


def main() -> None:
    check_open_and_closed_casimir_coefficients()
    check_nambu_goto_reference_expansion()
    check_open_oscillator_degeneracies()
    check_excited_level_expansion_coefficients()
    check_baryonic_y_string_geometry()
    check_hagedorn_coefficient()
    print("All QCD-string effective-spectrum checks passed.")


if __name__ == "__main__":
    main()
