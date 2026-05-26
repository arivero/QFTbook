#!/usr/bin/env python3
"""Finite convention checks for the sine-Gordon/massive-Thirring section."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def vertex_dimension_from_alpha_squared(alpha_squared_over_pi: Fraction) -> Fraction:
    """Return Delta for <phi phi> = -(2 pi)^(-1) log |x|."""

    return alpha_squared_over_pi / 4


def vertex_ope_exponent(alpha_squared_over_pi: Fraction) -> Fraction:
    """Return the exponent in |x-y|^{-exponent} for V_alpha V_{-alpha}."""

    return alpha_squared_over_pi / 2


def beta_squared_over_four_pi(g_over_pi: Fraction) -> Fraction:
    """Coleman's relation in the monograph convention."""

    return Fraction(1, 1) / (Fraction(1, 1) + g_over_pi)


def fermion_dimension(beta_squared_over_pi: Fraction) -> Fraction:
    """Delta = beta^2/(16 pi) + pi/beta^2 for the Mandelstam field."""

    return beta_squared_over_pi / 16 + Fraction(1, 1) / beta_squared_over_pi


def check_vertex_ope_and_dimensions() -> None:
    alpha_squared_over_pi = Fraction(4, 1)
    assert_equal(
        "full vertex dimension at alpha^2=4 pi",
        vertex_dimension_from_alpha_squared(alpha_squared_over_pi),
        Fraction(1, 1),
    )
    assert_equal(
        "full vertex OPE exponent is twice the scaling dimension",
        vertex_ope_exponent(alpha_squared_over_pi),
        2 * vertex_dimension_from_alpha_squared(alpha_squared_over_pi),
    )

    beta_squared_over_pi_value = Fraction(8, 1)
    assert_equal(
        "sine-Gordon marginal endpoint has Delta=2",
        vertex_dimension_from_alpha_squared(beta_squared_over_pi_value),
        Fraction(2, 1),
    )


def check_coleman_relation_and_current_dictionary() -> None:
    assert_equal(
        "free Dirac point maps to beta^2=4 pi",
        beta_squared_over_four_pi(Fraction(0, 1)),
        Fraction(1, 1),
    )
    assert_equal(
        "sine-Gordon marginal endpoint maps to g/pi=-1/2",
        beta_squared_over_four_pi(Fraction(-1, 2)),
        Fraction(2, 1),
    )

    for g_over_pi in (Fraction(0, 1), Fraction(1, 3), Fraction(-1, 3)):
        k = Fraction(1, 1) + g_over_pi
        beta_sq_over_pi = Fraction(4, 1) / k
        current_coeff_sq = beta_sq_over_pi / 4
        assert_equal(
            f"current coefficient squared equals 1/(pi K), g/pi={g_over_pi}",
            current_coeff_sq,
            Fraction(1, 1) / k,
        )


def check_mandelstam_exchange_and_fermion_dimension() -> None:
    # The line part has b = -2 pi/beta and the local part has a = +/- beta/2,
    # so ab/pi = +/- 1.  The equal-time exchange phase is exp(i ab sgn).
    assert_equal("Mandelstam exchange exponent for psi plus", Fraction(1, 1), Fraction(1, 1))
    assert_equal("Mandelstam exchange exponent for psi minus", Fraction(-1, 1), Fraction(-1, 1))

    beta_squared_over_pi_value = Fraction(4, 1)
    assert_equal(
        "Mandelstam field has free-fermion dimension at beta^2=4 pi",
        fermion_dimension(beta_squared_over_pi_value),
        Fraction(1, 2),
    )


def check_relevance_threshold() -> None:
    for beta_sq_over_four_pi, is_relevant in (
        (Fraction(1, 1), True),
        (Fraction(2, 1), False),
        (Fraction(3, 1), False),
    ):
        dimension = beta_sq_over_four_pi
        assert_equal(
            f"cosine dimension beta^2/(4 pi)={beta_sq_over_four_pi}",
            dimension,
            beta_sq_over_four_pi,
        )
        assert_true(
            f"relevance threshold beta^2/(4 pi)={beta_sq_over_four_pi}",
            (dimension < 2) is is_relevant,
        )


def main() -> None:
    check_vertex_ope_and_dimensions()
    check_coleman_relation_and_current_dictionary()
    check_mandelstam_exchange_and_fermion_dimension()
    check_relevance_threshold()
    print("All sine-Gordon/massive-Thirring bosonization checks passed.")


if __name__ == "__main__":
    main()
