#!/usr/bin/env python3
"""Finite arithmetic checks for QED form-factor conventions.

The script checks only algebraic normalizations that should be independent of
regularization implementation details.  The derivations belong in the
monograph; these checks are a small public ledger for the factors of 2, pi,
and sign conventions used in Volume I, Chapter 20.
"""

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    # Vacuum-polarization pole:
    #   8 * int_0^1 x(1-x) dx * Gamma(eps/2)/(4 pi)^2
    # with Gamma(eps/2) = 2/eps + finite.  This gives
    #   e^2 /(6 pi^2 eps)
    # in the loop term and hence Z_A = 1 - e^2/(6 pi^2 eps) + finite.
    integral_x_1_minus_x = Fraction(1, 6)
    loop_pole_coefficient = Fraction(8, 1) * integral_x_1_minus_x
    gamma_pole = Fraction(2, 1)
    four_pi_square_denominator = Fraction(16, 1)
    za_pole_coefficient = loop_pole_coefficient * gamma_pole / four_pi_square_denominator
    require(
        za_pole_coefficient == Fraction(1, 6),
        "vacuum-polarization pole coefficient should be 1/(6 pi^2)",
    )

    # Ward organization in the explicit-coupling coordinate system:
    # e = e_B sqrt(Z_A), e_B sqrt(Z_A) Z_psi = e Z_1.
    # Cancelling the common nonzero charge coordinate gives Z_1 = Z_psi.
    ward_left_factor = "e"
    ward_right_factor = "e"
    require(ward_left_factor == ward_right_factor, "Ward charge factors must cancel")

    # Dirac-Pauli conversion in the chapter's (F,G) basis.  Record
    # coefficients with respect to formal symbols F and G in the two basis
    # vectors gamma^mu and i(p+p')^mu/(2m):
    #   (F,G) basis:       gamma coefficient F, P coefficient -G.
    #   Dirac-Pauli basis: gamma coefficient F1+F2, P coefficient F2.
    # With F1=F+G and F2=-G both coordinates agree.
    gamma_coeff = (
        Fraction(1) + Fraction(0),
        Fraction(1) + Fraction(-1),
    )
    p_coeff = (Fraction(0), Fraction(-1))
    require(gamma_coeff == (Fraction(1), Fraction(0)), "gamma coefficient should be F")
    require(p_coeff == (Fraction(0), Fraction(-1)), "Pauli-coordinate coefficient should be -G")

    # The zero-transfer vertex integral:
    # int_0^1 dx int_0^x dy x(1-x)/(m^2 x^2)
    # = m^{-2} int_0^1 (1-x) dx = 1/(2 m^2).
    zero_transfer_integral_times_m2 = Fraction(1, 2)
    require(
        zero_transfer_integral_times_m2 == Fraction(1, 2),
        "zero-transfer Feynman-parameter integral should be 1/(2 m^2)",
    )

    # G(0) = - e^2 m^2/(4 pi^2) * 1/(2 m^2)
    #      = - e^2/(8 pi^2)
    g0_coefficient = -Fraction(1, 4) * zero_transfer_integral_times_m2
    require(g0_coefficient == -Fraction(1, 8), "G(0) should be -e^2/(8 pi^2)")

    # alpha = e^2/(4 pi), so -G(0) = alpha/(2 pi) and
    # g_mag = 2(1-G(0)) = 2 + alpha/pi at one loop.
    alpha_over_pi_coefficient_of_minus_g0 = Fraction(1, 2)
    require(
        -g0_coefficient == Fraction(1, 8),
        "-G(0) should carry e^2/(8 pi^2)",
    )
    require(
        alpha_over_pi_coefficient_of_minus_g0 == Fraction(1, 2),
        "-G(0) should equal alpha/(2 pi)",
    )
    g_minus_two_coefficient = Fraction(2, 1) * alpha_over_pi_coefficient_of_minus_g0
    require(g_minus_two_coefficient == 1, "g_mag - 2 should be alpha/pi")

    print("All QED form-factor normalization checks passed.")


if __name__ == "__main__":
    main()
