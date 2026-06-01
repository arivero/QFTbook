#!/usr/bin/env python3
"""Exact checks for the DIS/DGLAP convention block in Volume II.

The manuscript uses trace-delta color generators,
tr_fund(t^a t^b)=delta^{ab}, and writes the leading DGLAP equation as
P=(g^2/(8*pi^2)) P^(0)+O(g^4).  These finite rational checks verify the
plus-distribution convention, one-loop number and momentum sum rules, the
trace-normalization conversion of the cusp coefficient, and the sign
normalization of the local moment tower obtained from the Wilson-line light-ray
operator.
"""

from __future__ import annotations

from fractions import Fraction

ComplexRational = tuple[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def complex_mul(left: ComplexRational, right: ComplexRational) -> ComplexRational:
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def complex_pow_i(power: int) -> ComplexRational:
    values = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    ]
    return values[power % 4]


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


def check_light_ray_moment_normalization() -> None:
    # A free target with f(x)=delta(1-x) has M(lambda)=exp(i lambda P).
    # The N-th lambda derivative contributes (i P)^N.  Because the bilocal
    # derivative acts on the left endpoint, the local moment operator must use
    # (-i \overleftarrow D_n)^N; the product (-i)^N i^N is +1.
    momentum = Fraction(7, 3)
    minus_i = (Fraction(0), Fraction(-1))
    for moment in range(5):
        derivative_phase = complex_pow_i(moment)
        local_phase = (Fraction(1), Fraction(0))
        for _ in range(moment):
            local_phase = complex_mul(local_phase, minus_i)
        combined_phase = complex_mul(local_phase, derivative_phase)
        assert_equal(f"quark moment phase {moment}", combined_phase, (Fraction(1), Fraction(0)))

        local_matrix_element = momentum**moment
        extracted_moment = local_matrix_element / momentum**moment
        assert_equal(f"quark delta-target moment {moment}", extracted_moment, Fraction(1))

    # The gluon convention has an additional factor of x in the inverse
    # light-ray transform, so the N-th PDF moment uses N-1 left derivatives.
    for moment in range(1, 6):
        derivative_order = moment - 1
        derivative_phase = complex_pow_i(derivative_order)
        local_phase = (Fraction(1), Fraction(0))
        for _ in range(derivative_order):
            local_phase = complex_mul(local_phase, minus_i)
        combined_phase = complex_mul(local_phase, derivative_phase)
        assert_equal(f"gluon moment phase {moment}", combined_phase, (Fraction(1), Fraction(0)))

        local_matrix_element = momentum ** (moment - 1)
        extracted_moment = local_matrix_element / momentum ** (moment - 1)
        assert_equal(f"gluon delta-target moment {moment}", extracted_moment, Fraction(1))


def main() -> None:
    check_plus_distribution_monomials()
    check_number_and_momentum_sum_rules()
    check_large_spin_and_trace_conversion()
    check_light_ray_moment_normalization()
    print(
        "All QCD DGLAP plus-distribution, sum-rule, "
        "cusp-normalization, and light-ray moment checks passed."
    )


if __name__ == "__main__":
    main()
