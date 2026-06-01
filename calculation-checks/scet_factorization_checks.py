#!/usr/bin/env python3
"""Finite checks for the SCET factorization datum in the jets chapter.

These checks do not prove a factorization theorem.  They verify the exact
algebraic facts used in the exposition: convolution of jet and soft
distributions preserves normalization and first moments, and a finite
Wilson-line change of variables removes the leading soft covariant derivative
when the Wilson line solves its defining differential equation.
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


def main() -> None:
    check_event_shape_convolution()
    check_zero_bin_inclusion_exclusion()
    check_zero_bin_scheme_reshuffling()
    check_soft_wilson_line_decoupling_identity()
    print("All SCET convolution, zero-bin, and soft-Wilson-line checks passed.")


if __name__ == "__main__":
    main()
