#!/usr/bin/env python3
"""Finite checks for the SCET factorization datum in the jets chapter.

These checks do not prove a factorization theorem.  They verify the exact
algebraic facts used in the exposition: convolution of jet and soft
distributions preserves normalization and first moments; finite zero-bin
subtraction is inclusion--exclusion; a finite Wilson-line change of variables
removes the leading soft covariant derivative when the Wilson line solves its
defining differential equation; and scalar RG transport is independent of the
common scale when the hard, jet, and soft anomalous dimensions satisfy the
factorization consistency equation.  It also checks the finite phase-space
area behind the massive-vector Sudakov chart used for electroweak jet
boundaries and the finite unitarity diagnostic for Glauber cancellation versus
measurement obstruction.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Mapping

import sympy as sp

Distribution = Mapping[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def normalize(dist: Distribution) -> Fraction:
    return sum(dist.values(), Fraction(0))


def moment(dist: Distribution) -> Fraction:
    return sum(x * weight for x, weight in dist.items())


def endpoint_convolution(
    jet_n: Distribution,
    jet_barn: Distribution,
    soft: Distribution,
    q_hard: Fraction,
) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = defaultdict(Fraction)
    for s1, w1 in jet_n.items():
        for s2, w2 in jet_barn.items():
            for k, ws in soft.items():
                e = (s1 + s2) / (q_hard * q_hard) + k / q_hard
                out[e] += w1 * w2 * ws
    return dict(out)


def generating_transform(dist: Distribution, scale: Fraction) -> dict[Fraction, Fraction]:
    return {scale * x: weight for x, weight in dist.items()}


def multiply_transforms(*transforms: Mapping[Fraction, Fraction]) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    for transform in transforms:
        new_out: dict[Fraction, Fraction] = defaultdict(Fraction)
        for e1, w1 in out.items():
            for e2, w2 in transform.items():
                new_out[e1 + e2] += w1 * w2
        out = dict(new_out)
    return out


def check_event_shape_convolution() -> None:
    jet_n = {Fraction(1): Fraction(1, 3), Fraction(4): Fraction(2, 3)}
    jet_barn = {Fraction(2): Fraction(3, 5), Fraction(5): Fraction(2, 5)}
    soft = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(3, 4)}
    q_hard = Fraction(6)

    direct = endpoint_convolution(jet_n, jet_barn, soft, q_hard)
    transformed = multiply_transforms(
        generating_transform(jet_n, Fraction(1, q_hard * q_hard)),
        generating_transform(jet_barn, Fraction(1, q_hard * q_hard)),
        generating_transform(soft, Fraction(1, q_hard)),
    )
    assert_equal("endpoint convolution transform", direct, transformed)
    assert_equal("convolution normalization", normalize(direct), Fraction(1))

    expected_first_moment = (
        moment(jet_n) / (q_hard * q_hard)
        + moment(jet_barn) / (q_hard * q_hard)
        + moment(soft) / q_hard
    )
    assert_equal("endpoint first moment", moment(direct), expected_first_moment)


def finite_zero_bin_sum(
    collinear: Mapping[str, Fraction],
    soft: Mapping[str, Fraction],
    overlap: Mapping[str, Fraction],
    test: Mapping[str, Fraction],
) -> Fraction:
    return (
        sum(weight * test[cell] for cell, weight in collinear.items())
        + sum(weight * test[cell] for cell, weight in soft.items())
        - sum(weight * test[cell] for cell, weight in overlap.items())
    )


def check_zero_bin_inclusion_exclusion() -> None:
    collinear = {"c": Fraction(5), "o1": Fraction(7), "o2": Fraction(11)}
    soft = {"s": Fraction(13), "o1": Fraction(7), "o2": Fraction(11)}
    overlap = {"o1": Fraction(7), "o2": Fraction(11)}
    test = {
        "c": Fraction(2, 3),
        "s": Fraction(3, 5),
        "o1": Fraction(5, 7),
        "o2": Fraction(7, 11),
    }
    matched = finite_zero_bin_sum(collinear, soft, overlap, test)
    unique_union = (
        collinear["c"] * test["c"]
        + soft["s"] * test["s"]
        + overlap["o1"] * test["o1"]
        + overlap["o2"] * test["o2"]
    )
    naive_double_count = sum(weight * test[cell] for cell, weight in collinear.items()) + sum(
        weight * test[cell] for cell, weight in soft.items()
    )
    assert_equal("finite zero-bin inclusion-exclusion", matched, unique_union)
    assert_equal(
        "naive overlap double count",
        naive_double_count - matched,
        sum(weight * test[cell] for cell, weight in overlap.items()),
    )


def check_zero_bin_scheme_reshuffling() -> None:
    collinear = {"c": Fraction(2), "o": Fraction(5)}
    soft = {"s": Fraction(7), "o": Fraction(5)}
    overlap = {"o": Fraction(5)}
    test = {"c": Fraction(3), "s": Fraction(4), "o": Fraction(11)}
    base = finite_zero_bin_sum(collinear, soft, overlap, test)

    delta = Fraction(13)
    collinear_shifted = {"c": collinear["c"], "o": collinear["o"]}
    soft_shifted = {"s": soft["s"], "o": soft["o"] + delta}
    overlap_shifted = {"o": overlap["o"] + delta}
    shifted = finite_zero_bin_sum(collinear_shifted, soft_shifted, overlap_shifted, test)
    assert_equal("paired zero-bin scheme reshuffling", shifted, base)


def integrate_piecewise(values: Mapping[tuple[Fraction, Fraction], Fraction], start: Fraction, end: Fraction) -> Fraction:
    if start == end:
        return Fraction(0)
    if start > end:
        return -integrate_piecewise(values, end, start)

    total = Fraction(0)
    for (left, right), value in values.items():
        overlap_left = max(start, left)
        overlap_right = min(end, right)
        if overlap_left < overlap_right:
            total += value * (overlap_right - overlap_left)
    return total


def check_rg_transport_common_scale_independence() -> None:
    intervals = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(3)))
    gamma_h = {intervals[0]: Fraction(3), intervals[1]: Fraction(-1), intervals[2]: Fraction(2)}
    gamma_j = {intervals[0]: Fraction(-2), intervals[1]: Fraction(4), intervals[2]: Fraction(1)}
    gamma_s = {interval: -gamma_h[interval] - 2 * gamma_j[interval] for interval in intervals}

    for interval in intervals:
        assert_equal(
            "pointwise SCET anomalous-dimension consistency",
            gamma_h[interval] + 2 * gamma_j[interval] + gamma_s[interval],
            Fraction(0),
        )

    natural_h = Fraction(0)
    natural_j = Fraction(1)
    natural_s = Fraction(2)

    def total_transport_exponent(common_scale: Fraction) -> Fraction:
        return (
            integrate_piecewise(gamma_h, natural_h, common_scale)
            + 2 * integrate_piecewise(gamma_j, natural_j, common_scale)
            + integrate_piecewise(gamma_s, natural_s, common_scale)
        )

    reference = total_transport_exponent(Fraction(2))
    assert_equal("RG transport to first common scale", reference, total_transport_exponent(Fraction(2)))
    assert_equal("RG transport independent of later common scale", reference, total_transport_exponent(Fraction(3)))

    shifted_gamma_h = {interval: gamma_h[interval] + Fraction(5) for interval in intervals}
    shifted_gamma_s = {interval: gamma_s[interval] - Fraction(5) for interval in intervals}
    shifted = (
        integrate_piecewise(shifted_gamma_h, natural_h, Fraction(3))
        + 2 * integrate_piecewise(gamma_j, natural_j, Fraction(3))
        + integrate_piecewise(shifted_gamma_s, natural_s, Fraction(3))
    )
    unshifted = total_transport_exponent(Fraction(3))
    assert_equal("paired hard-soft anomalous-dimension scheme shift", shifted, unshifted + Fraction(5) * (natural_s - natural_h))


def check_soft_wilson_line_decoupling_identity() -> None:
    s = sp.symbols("s")
    a = sp.Rational(3, 2)
    connection = sp.Matrix([[0, a], [0, 0]])
    identity = sp.eye(2)
    # Nilpotency makes this exact polynomial Wilson line solve dY/ds = A Y.
    wilson = identity + s * connection
    field0 = sp.Matrix([1 + 2 * s + s**2, sp.Rational(1, 3) - s])

    lhs = sp.diff(wilson * field0, s) - connection * wilson * field0
    rhs = wilson * sp.diff(field0, s)
    assert_equal("finite BPS decoupling identity", sp.simplify(lhs - rhs), sp.zeros(2, 1))


def trace(matrix: sp.Matrix) -> sp.Rational:
    return sp.trace(matrix)


def check_glauber_unitarity_diagnostic() -> None:
    unitary = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [sp.Rational(-4, 5), sp.Rational(3, 5)]])
    identity = sp.eye(2)
    assert_equal("finite Glauber unitary", unitary.T * unitary, identity)

    rho = sp.Matrix([[sp.Rational(2, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(3, 5)]])
    evolved = unitary * rho * unitary.T
    assert_equal("inclusive Glauber trace", trace(evolved), trace(rho))

    commuting_measurement = sp.Rational(7, 3) * identity
    assert_equal(
        "commuting Glauber measurement",
        trace(commuting_measurement * evolved),
        trace(commuting_measurement * rho),
    )

    noncommuting_measurement = sp.Matrix([[1, 0], [0, 0]])
    without_glauber = trace(noncommuting_measurement * rho)
    with_glauber = trace(noncommuting_measurement * evolved)
    if with_glauber == without_glauber:
        raise AssertionError("noncommuting measurement should detect the finite Glauber rotation")


def massive_vector_sudakov_area(log_q2_over_m2: Fraction) -> Fraction:
    return log_q2_over_m2 * log_q2_over_m2 / 4


def check_massive_vector_sudakov_area() -> None:
    big_log = Fraction(6)
    # The chart is 0 < y < L and 0 < x < y/2.
    triangle_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in [(Fraction(0), big_log)]
    )
    assert_equal(
        "massive-vector Sudakov triangular area",
        triangle_area,
        massive_vector_sudakov_area(big_log),
    )

    alpha_times_c_over_pi = Fraction(5, 7)
    exponent = -alpha_times_c_over_pi * massive_vector_sudakov_area(big_log)
    assert_equal("massive-vector Sudakov exponent coefficient", exponent, Fraction(-45, 7))

    # Splitting the y interval checks additivity of the finite phase-space
    # integral before taking a continuum limit.
    pieces = [
        (Fraction(0), Fraction(2)),
        (Fraction(2), Fraction(5)),
        (Fraction(5), big_log),
    ]
    piecewise_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in pieces
    )
    assert_equal("piecewise massive-vector area", piecewise_area, massive_vector_sudakov_area(big_log))


def main() -> None:
    check_event_shape_convolution()
    check_zero_bin_inclusion_exclusion()
    check_zero_bin_scheme_reshuffling()
    check_rg_transport_common_scale_independence()
    check_soft_wilson_line_decoupling_identity()
    check_glauber_unitarity_diagnostic()
    check_massive_vector_sudakov_area()
    print(
        "All SCET convolution, zero-bin, RG-transport, soft-Wilson-line, "
        "Glauber-unitarity, and massive-vector Sudakov checks passed."
    )


if __name__ == "__main__":
    main()
