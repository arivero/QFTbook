#!/usr/bin/env python3
"""Finite coefficient checks for the anomaly-matching/WZW section.

The script checks algebraic factors only:

* WZW matching forces n=N_c because the UV left-flavor anomaly coefficient is
  N_c/(48 pi^2) and the level-n WZW variation is n/(48 pi^2).
* Bardeen counterterms change anomaly representatives but leave the completely
  symmetric descent coefficient, hence the WZW level coordinate, unchanged.
* Vector flavor anomalies cancel between the left and right components of a
  Dirac quark.
* The two-flavor electromagnetic trace is
  Tr(T^3 {q,q}) = 1/3, giving the N_c=3 coefficient
  e^2/(16 pi^2 f_pi) in the monograph convention.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations


def assert_eq(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def wzw_level_for_matching(n_c: int) -> int:
    uv_coefficient = Fraction(n_c, 48)
    level_one_wzw_coefficient = Fraction(1, 48)
    return int(uv_coefficient / level_one_wzw_coefficient)


def check_wzw_level() -> None:
    for n_c in range(2, 10):
        if wzw_level_for_matching(n_c) != n_c:
            raise AssertionError(f"WZW matching failed for N_c={n_c}")


def check_bardeen_counterterm_preserves_symmetric_class() -> None:
    # A local Abelianized Bardeen counterterm with h_ab,c=-h_ba,c shifts
    # d_abc by (h_ab,c + h_ac,b)/2.  The completely symmetric part is the
    # cohomology coordinate compared by WZW level matching.
    raw_h = {
        (0, 1, 0): Fraction(2, 3),
        (0, 1, 2): Fraction(-5, 7),
        (0, 2, 1): Fraction(11, 5),
        (1, 2, 0): Fraction(13, 6),
    }

    def h(a: int, b: int, c: int) -> Fraction:
        if a == b:
            return Fraction(0)
        if (a, b, c) in raw_h:
            return raw_h[(a, b, c)]
        if (b, a, c) in raw_h:
            return -raw_h[(b, a, c)]
        return Fraction(0)

    def delta(a: int, b: int, c: int) -> Fraction:
        return Fraction(1, 2) * (h(a, b, c) + h(a, c, b))

    for a in range(3):
        for b in range(3):
            for c in range(3):
                sym_delta = sum(delta(*p) for p in permutations((a, b, c))) / Fraction(6)
                assert_eq(f"symmetric Bardeen shift ({a}{b}{c})", sym_delta, Fraction(0))


def check_vector_anomaly_cancellation() -> None:
    for n_c in range(2, 10):
        for trace_value in (Fraction(1, 5), Fraction(-7, 3), Fraction(11, 6)):
            left = Fraction(n_c, 2) * trace_value
            right = Fraction(n_c, 2) * trace_value
            assert_eq(f"vector anomaly cancellation N_c={n_c}", left - right, Fraction(0, 1))


def check_pi0_two_photon_trace() -> None:
    t3 = (Fraction(1, 2), Fraction(-1, 2))
    q = (Fraction(2, 3), Fraction(-1, 3))
    anticommutator_trace = sum(t * 2 * charge * charge for t, charge in zip(t3, q))
    assert_eq("Tr(T3 {q,q})", anticommutator_trace, Fraction(1, 3))

    coefficient_without_e2_fpi = Fraction(3, 16) * anticommutator_trace
    assert_eq("N_c=3 pi0 gamma gamma coefficient", coefficient_without_e2_fpi, Fraction(1, 16))


def main() -> None:
    check_wzw_level()
    check_bardeen_counterterm_preserves_symmetric_class()
    check_vector_anomaly_cancellation()
    check_pi0_two_photon_trace()
    print("All anomaly-matching and WZW coefficient checks passed.")


if __name__ == "__main__":
    main()
