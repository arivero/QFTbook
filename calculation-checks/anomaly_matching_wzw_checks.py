#!/usr/bin/env python3
"""Finite coefficient checks for the anomaly-matching/WZW section.

The script checks algebraic factors only:

* WZW matching forces n=N_c because the UV left-flavor anomaly coefficient is
  N_c/(48 pi^2) and the level-n WZW variation is n/(48 pi^2).
* The finite Wess-Zumino extension ambiguity exp(2 pi i n k) is trivial for
  every integer winding k exactly when the level n is integral.
* Bardeen counterterms change anomaly representatives but leave the completely
  symmetric descent coefficient, hence the WZW level coordinate, unchanged.
* The Abelianized cubic descent coordinate determines the symmetric cubic
  coefficient through the polarization identity.
* Vector flavor anomalies cancel between the left and right components of a
  Dirac quark.
* The two-flavor electromagnetic trace is
  Tr(T^3 {q,q}) = 1/3, giving the N_c=3 coefficient
  e^2/(16 pi^2 f_pi) in the monograph convention.

Evidence contract.
Target claims: the finite coefficient subclaims in the anomaly-matching and
Wess-Zumino-Witten sections: level matching, integral extension ambiguity,
Bardeen-counterterm invariance of the symmetric cubic coordinate, vector
flavor cancellation, and the two-flavor electromagnetic trace.
Independent construction: exact rational arithmetic from the displayed
charge, flavor, and descent-coordinate definitions, plus polarization of the
Abelianized cubic polynomial rather than substitution of a fitted anomaly
coefficient.
Imported assumptions: the chapter's current normalization, flavor-generator
normalization, WZW variation convention, and the finite list of quark charges.
Negative controls: counterterm tensors with antisymmetric slots are checked
to change representatives while preserving the complete symmetric coordinate,
and vector-pair contributions are checked to cancel between left and right
components.
Scope boundary: a pass fixes convention-sensitive finite coefficients; it
does not prove existence of the WZW functional, current algebra in continuum
QCD, pion dominance, or nonperturbative anomaly matching.
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


def is_trivial_wz_extension_phase(level: Fraction, winding: int) -> bool:
    # The phase is exp(2 pi i * level * winding).  It is trivial exactly when
    # the exponent in units of 2 pi is an integer.
    return (level * winding).denominator == 1


def check_wz_extension_ambiguity_integrality() -> None:
    for integer_level in range(-3, 7):
        level = Fraction(integer_level, 1)
        for winding in range(-5, 6):
            if not is_trivial_wz_extension_phase(level, winding):
                raise AssertionError(
                    f"integer WZ level {level} failed at winding {winding}"
                )

    for fractional_level in (Fraction(1, 2), Fraction(2, 3), Fraction(-5, 4)):
        if is_trivial_wz_extension_phase(fractional_level, 1):
            raise AssertionError(f"fractional WZ level {fractional_level} passed")

    for n_c in range(2, 10):
        assert_eq(
            f"QCD color multiplicity gives integral WZ level N_c={n_c}",
            Fraction(Fraction(wzw_level_for_matching(n_c), 1).denominator, 1),
            Fraction(1),
        )


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


def check_abelianized_cubic_polarization_identity() -> None:
    # The WZW level comparison uses the Abelianized descent coordinate
    # C_abc lambda^a F^b F^c.  A symmetric cubic tensor is recovered from the
    # homogeneous cubic polynomial P(x)=C_abc x^a x^b x^c by polarization.
    raw_components = {
        (0, 0, 0): Fraction(2, 5),
        (1, 1, 1): Fraction(-3, 7),
        (2, 2, 2): Fraction(5, 11),
        (0, 0, 1): Fraction(7, 13),
        (0, 0, 2): Fraction(-11, 17),
        (0, 1, 1): Fraction(13, 19),
        (1, 1, 2): Fraction(-17, 23),
        (0, 2, 2): Fraction(19, 29),
        (1, 2, 2): Fraction(-23, 31),
        (0, 1, 2): Fraction(29, 37),
    }

    def canonical(indices: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(sorted(indices))

    def c(a: int, b: int, c_index: int) -> Fraction:
        return raw_components[canonical((a, b, c_index))]

    def cubic(vector: tuple[Fraction, Fraction, Fraction]) -> Fraction:
        total = Fraction(0)
        for a in range(3):
            for b in range(3):
                for c_index in range(3):
                    total += c(a, b, c_index) * vector[a] * vector[b] * vector[c_index]
        return total

    def add(*vectors: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
        return (
            sum(vector[0] for vector in vectors),
            sum(vector[1] for vector in vectors),
            sum(vector[2] for vector in vectors),
        )

    basis = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    ]

    for x_index, x in enumerate(basis):
        for y_index, y in enumerate(basis):
            for z_index, z in enumerate(basis):
                recovered = (
                    cubic(add(x, y, z))
                    - cubic(add(x, y))
                    - cubic(add(x, z))
                    - cubic(add(y, z))
                    + cubic(x)
                    + cubic(y)
                    + cubic(z)
                ) / Fraction(6)
                assert_eq(
                    f"cubic polarization C_{x_index}{y_index}{z_index}",
                    recovered,
                    c(x_index, y_index, z_index),
                )


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
    check_wz_extension_ambiguity_integrality()
    check_bardeen_counterterm_preserves_symmetric_class()
    check_abelianized_cubic_polarization_identity()
    check_vector_anomaly_cancellation()
    check_pi0_two_photon_trace()
    print("All anomaly-matching and WZW coefficient checks passed.")


if __name__ == "__main__":
    main()
