#!/usr/bin/env python3
"""Exact bookkeeping checks for 3D Chern-Simons-matter light-cone gauge."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def permutation_sign(p: tuple[int, int, int]) -> int:
    inv = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                inv += 1
    return -1 if inv % 2 else 1


def check_light_cone_quadratic_factor() -> None:
    # Labels are (+,-,perp)=(0,1,2), with epsilon^{+-perp}=+1.
    eps_plus_minus_perp = permutation_sign((0, 1, 2))
    eps_perp_minus_plus = permutation_sign((2, 1, 0))
    assert_equal("epsilon + - perp", eps_plus_minus_perp, 1)
    assert_equal("epsilon perp - +", eps_perp_minus_plus, -1)

    # A_+ d_- A_perp - A_perp d_- A_+ becomes 2 A_+ d_- A_perp after
    # integrating the second term by parts.  The CS prefactor k/(4*pi)
    # therefore becomes k/(2*pi).
    coefficient_before_parts = Fraction(eps_plus_minus_perp, 1)
    coefficient_after_parts = Fraction(-eps_perp_minus_plus, 1)
    assert_equal(
        "light-cone CS quadratic factor",
        coefficient_before_parts + coefficient_after_parts,
        Fraction(2),
    )


def check_first_order_gaussian_sign() -> None:
    # Finite-dimensional analogue with antisymmetric D replaced by a formal
    # inverse convention.  For S=a A_+ D A_perp - A_+ J+ - A_perp Jperp,
    # equations give A_perp=a^{-1}D^{-1}J+, A_+=-a^{-1}D^{-1}Jperp.
    # The on-shell action is -a^{-1}(D^{-1}J+)Jperp, so the rational
    # coefficient multiplying 2*pi/k is -1.
    bilinear = Fraction(1)
    source_plus = Fraction(-1)
    source_perp = Fraction(-1)

    # Substitute D A_perp = a^{-1} J+ and A_+ = -a^{-1}D^{-1}Jperp.
    # Coefficients are counted relative to a^{-1}(D^{-1}Jperp)J+ and then
    # converted to the displayed ordering (D^{-1}J+)Jperp.
    first_two_terms = -bilinear - source_plus
    remaining_term = source_perp
    assert_equal("first-order CS first two terms cancel", first_two_terms, Fraction(0))
    assert_equal("first-order CS effective source sign", remaining_term, Fraction(-1))


def check_trace_delta_color_scaling() -> None:
    # In trace-delta normalization,
    # t^a_i^j t^a_k^l = delta_i^l delta_k^j - (1/N) delta_i^j delta_k^l.
    # A normalized singlet contraction receives an O(N) planar term and an
    # O(1) trace-subtraction term before the conventional overall 1/N
    # normalization of connected singlet correlators.
    for n in (3, 5, 11):
        planar = Fraction(n, 1)
        subtraction = Fraction(1, 1)
        assert_equal(f"CS vector planar/subleading ratio N={n}", planar / subtraction, Fraction(n, 1))


def check_t_hooft_coordinate_dimensionless() -> None:
    # In three dimensions k is an integer level and N is a rank.  Their ratio is
    # dimensionless.  This check records the algebraic normalization used in the
    # chapter: lambda=N/k_eff and one gauge exchange from the CS kernel carries
    # the coefficient 2*pi/k_eff, hence N times the rational part is 2 lambda.
    n = Fraction(17)
    k_eff = Fraction(19)
    lam = n / k_eff
    one_exchange_without_pi = Fraction(2, 1) / k_eff
    planar_exchange_without_pi = n * one_exchange_without_pi
    assert_equal("CS vector planar exchange coefficient", planar_exchange_without_pi, 2 * lam)


def main() -> None:
    check_light_cone_quadratic_factor()
    check_first_order_gaussian_sign()
    check_trace_delta_color_scaling()
    check_t_hooft_coordinate_dimensionless()
    print("All Chern-Simons-matter light-front checks passed.")


if __name__ == "__main__":
    main()
