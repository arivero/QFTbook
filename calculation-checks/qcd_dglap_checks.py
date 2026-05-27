#!/usr/bin/env python3
"""Exact checks for the DIS/DGLAP convention block in Volume II.

The manuscript uses trace-delta color generators,
tr_fund(t^a t^b)=delta^{ab}, and writes the leading DGLAP equation as
P=(g^2/(8*pi^2)) P^(0)+O(g^4).  These finite rational checks verify the
plus-distribution convention, one-loop number and momentum sum rules, and the
trace-normalization conversion of the cusp coefficient.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def d0_moment(power: int) -> Fraction:
    """Integral of x^power (1/(1-x))_+ on [0,1]."""
    if power < 0:
        raise ValueError("D0 moment is only used here for nonnegative powers")
    return -harmonic(power)


def pqq_moment(n: int, cf: Fraction = Fraction(1)) -> Fraction:
    """Moment int_0^1 dx x^(n-1) P_qq^(0)(x)/delta_ij."""
    return cf * (
        2 * d0_moment(n - 1)
        - Fraction(1, n)
        - Fraction(1, n + 1)
        + Fraction(3, 2)
    )


def pqg_moment(n: int, tr: Fraction = Fraction(1)) -> Fraction:
    """Moment of P_{qg}^{(0)} for one quark or antiquark species."""
    return tr * (
        Fraction(1, n + 2)
        + Fraction(1, n)
        - Fraction(2, n + 1)
        + Fraction(1, n + 2)
    )


def pgq_moment(n: int, cf: Fraction = Fraction(1)) -> Fraction:
    """Moment of P_{gq}^{(0)}."""
    return cf * (
        2 * Fraction(1, n - 1)
        - 2 * Fraction(1, n)
        + Fraction(1, n + 1)
    )


def pgg_moment(
    n: int,
    ca: Fraction = Fraction(1),
    tr: Fraction = Fraction(1),
    nf: Fraction = Fraction(1),
) -> Fraction:
    """Moment of P_{gg}^{(0)} with D0=(1/(1-x))_+."""
    regular = (
        d0_moment(n)
        + Fraction(1, n - 1)
        - Fraction(1, n)
        + Fraction(1, n + 1)
        - Fraction(1, n + 2)
    )
    delta = (11 * ca - 4 * tr * nf) / 6
    return 2 * ca * regular + delta


def check_plus_distribution_monomials() -> None:
    expected = {
        0: Fraction(0),
        1: Fraction(-1),
        2: Fraction(-3, 2),
        3: Fraction(-11, 6),
        4: Fraction(-25, 12),
    }
    for power, value in expected.items():
        assert_equal(f"D0 moment power {power}", d0_moment(power), value)


def check_number_and_momentum_sum_rules() -> None:
    cf = Fraction(7, 3)
    ca = Fraction(10, 1)
    tr = Fraction(2, 1)
    nf = Fraction(5, 1)

    assert_equal("quark number", pqq_moment(1, cf), Fraction(0))
    assert_equal("quark-parent momentum", pqq_moment(2, cf) + pgq_moment(2, cf), Fraction(0))
    assert_equal(
        "gluon-parent momentum",
        2 * nf * pqg_moment(2, tr) + pgg_moment(2, ca, tr, nf),
        Fraction(0),
    )


def check_large_spin_and_trace_conversion() -> None:
    # Exact nonsinglet formula used in the text.
    for n in (1, 2, 5, 11):
        rhs = -2 * harmonic(n - 1) - Fraction(1, n) - Fraction(1, n + 1) + Fraction(3, 2)
        assert_equal(f"nonsinglet moment {n}", pqq_moment(n), rhs)

    # Trace-delta and half-trace conventions give the same one-loop cusp product.
    g_delta_sq = Fraction(3, 7)
    cf_delta = Fraction(16, 5)
    g_half_sq = 2 * g_delta_sq
    cf_half = cf_delta / 2
    assert_equal("cusp product convention", g_delta_sq * cf_delta, g_half_sq * cf_half)


def main() -> None:
    check_plus_distribution_monomials()
    check_number_and_momentum_sum_rules()
    check_large_spin_and_trace_conversion()
    print("All QCD DGLAP plus-distribution, sum-rule, and cusp-normalization checks passed.")


if __name__ == "__main__":
    main()
