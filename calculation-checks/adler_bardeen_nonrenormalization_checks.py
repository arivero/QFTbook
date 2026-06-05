#!/usr/bin/env python3
"""Exact finite checks for Adler--Bardeen nonrenormalization bookkeeping.

The script verifies the algebra used in the Chapter 20
Adler--Bardeen section:

* exact local counterterm/current-improvement directions do not change the
  nontrivial anomaly-class coordinate;
* singlet axial-current and topological-density source redefinitions can move
  terms inside a displayed divergence equation without changing the
  coefficient of the cohomology class;
* a two-loop-looking local term is removable precisely when its projection on
  the topological anomaly coordinate vanishes;
* the Callan--Symanzik class equation recursively kills higher coefficients in
  a finite beta-function model once the nontrivial descent insertion has zero
  anomalous dimension;
* one-loop cancellation of the cubic gauge-anomaly coordinate leaves only
  exact higher-loop Slavnov breakings in the Adler--Bardeen local sector.

Evidence contract.
Target claims: Theorem `thm:adler-bardeen-nonrenormalization`, equation
`eq:adler-bardeen-cs-class-equation`, and the singlet-current/operator-mixing
paragraph in Volume II Chapter 20.
Independent construction: finite vector-space models of local operators
modulo exact/current-improvement directions, exact rational source-coordinate
changes, and a direct power-series coefficient extraction from
beta(g) d c(g)/dg.
Imported assumptions: the chapter's identification of the nontrivial descent
coordinate with a one-dimensional local BRST cohomology projection in the
tested sector, the quantum-action-principle locality reduction, and the
Adler--Bardeen all-order input that the descent insertion has no independent
anomalous dimension in that cohomology coordinate.
Negative controls: the checks deliberately add a nonzero topological-class
piece to a purported removable two-loop term, use uncancelled cubic anomaly
data, and test nonzero higher coefficients in the RG recurrence.
Scope boundary: a pass checks finite algebra and recurrence bookkeeping; it
does not prove the analytic all-order theorem, the full local BRST cohomology
classification, a global anomaly statement, or existence of a nonperturbative
chiral gauge-theory regulator.
"""

from __future__ import annotations

from fractions import Fraction


BASIS = ("A", "E", "M")


def op(a: Fraction = Fraction(0), e: Fraction = Fraction(0), m: Fraction = Fraction(0)) -> dict[str, Fraction]:
    """Vector in anomaly, exact/current-divergence, and mass-breaking directions."""

    return {"A": a, "E": e, "M": m}


def add(*vectors: dict[str, Fraction]) -> dict[str, Fraction]:
    return {key: sum(vector[key] for vector in vectors) for key in BASIS}


def scale(coefficient: Fraction, vector: dict[str, Fraction]) -> dict[str, Fraction]:
    return {key: coefficient * vector[key] for key in BASIS}


def project_anomaly_class(vector: dict[str, Fraction]) -> Fraction:
    return vector["A"]


def assert_equal(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def assert_not_equal(name: str, value: Fraction, forbidden: Fraction) -> None:
    if value == forbidden:
        raise AssertionError(f"{name}: unexpectedly got forbidden value {forbidden}")


def check_exact_shifts_preserve_anomaly_class() -> None:
    one_loop_class = Fraction(5, 3)
    representative = op(a=one_loop_class, e=Fraction(7, 11), m=Fraction(-2, 13))
    counterterm_shift = op(e=Fraction(-19, 17), m=Fraction(23, 29))
    shifted = add(representative, counterterm_shift)

    assert_equal(
        "counterterm/current exact shift preserves anomaly projection",
        project_anomaly_class(shifted),
        one_loop_class,
    )

    fake_higher_loop_class = add(shifted, op(a=Fraction(1, 37)))
    assert_not_equal(
        "nonzero higher-loop class is not an exact shift",
        project_anomaly_class(fake_higher_loop_class),
        one_loop_class,
    )


def check_singlet_operator_mixing_filter() -> None:
    # q' = q + alpha div J_5 + beta mass-breaking has the same cohomology
    # projection as q.  The extra directions change the displayed operator
    # identity but not the topological anomaly coordinate.
    alpha = Fraction(3, 5)
    beta = Fraction(-4, 7)
    q_prime = op(a=Fraction(1), e=alpha, m=beta)

    current_rescaling = scale(Fraction(11, 13), op(e=Fraction(1)))
    mass_source_shift = add(op(m=Fraction(1)), scale(Fraction(-2, 17), op(e=Fraction(1))))

    assert_equal("mixed q source has unit anomaly projection", project_anomaly_class(q_prime), Fraction(1))
    assert_equal("current rescaling is exact in anomaly quotient", project_anomaly_class(current_rescaling), Fraction(0))
    assert_equal("mass-source shift is exact in anomaly quotient", project_anomaly_class(mass_source_shift), Fraction(0))

    apparent_two_loop = add(scale(Fraction(5, 19), current_rescaling), scale(Fraction(-7, 23), mass_source_shift))
    assert_equal(
        "two-loop-looking exact operator term is removable",
        project_anomaly_class(apparent_two_loop),
        Fraction(0),
    )

    true_two_loop_violation = add(apparent_two_loop, scale(Fraction(1, 31), q_prime))
    assert_not_equal(
        "two-loop term with topological projection is a real anomaly correction",
        project_anomaly_class(true_two_loop_violation),
        Fraction(0),
    )


def check_callan_symanzik_recurrence() -> None:
    # beta(g) d c(g)/dg = 0 with
    # beta=b0 g^3+b1 g^5+b2 g^7 and
    # c=c1+c2 g^2+c3 g^4+c4 g^6 gives the three displayed equations.
    beta0 = Fraction(7, 3)
    beta1 = Fraction(-5, 11)
    beta2 = Fraction(13, 17)

    c2 = Fraction(0)
    c3 = Fraction(0)
    c4 = Fraction(0)

    g4 = 2 * beta0 * c2
    g6 = 4 * beta0 * c3 + 2 * beta1 * c2
    g8 = 6 * beta0 * c4 + 4 * beta1 * c3 + 2 * beta2 * c2

    assert_equal("RG class equation g^4 coefficient", g4, Fraction(0))
    assert_equal("RG class equation g^6 coefficient", g6, Fraction(0))
    assert_equal("RG class equation g^8 coefficient", g8, Fraction(0))

    wrong_c2 = Fraction(1, 5)
    wrong_g4 = 2 * beta0 * wrong_c2
    assert_not_equal("nonzero two-loop coefficient violates RG class equation", wrong_g4, Fraction(0))

    wrong_c3 = Fraction(-3, 10)
    wrong_g6_after_c2_zero = 4 * beta0 * wrong_c3
    assert_not_equal(
        "nonzero three-loop coefficient violates next RG class equation",
        wrong_g6_after_c2_zero,
        Fraction(0),
    )


def check_one_loop_gauge_cancellation_to_exact_breakings() -> None:
    # In the tested one-dimensional cubic-anomaly coordinate, vectorlike or
    # otherwise cancelling matter content leaves no nontrivial local class.
    cancelled_cubic_data = [Fraction(1), Fraction(-1), Fraction(2), Fraction(-2)]
    uncancelled_cubic_data = [Fraction(1), Fraction(1), Fraction(-1)]

    cancelled_class = sum(cancelled_cubic_data)
    uncancelled_class = sum(uncancelled_cubic_data)

    assert_equal("one-loop cubic gauge-anomaly coordinate cancels", cancelled_class, Fraction(0))
    assert_not_equal("uncancelled cubic coordinate survives", uncancelled_class, Fraction(0))

    higher_loop_after_ab = op(a=cancelled_class, e=Fraction(5, 8), m=Fraction(-9, 10))
    assert_equal(
        "after Adler-Bardeen cancellation, higher-loop ST breaking is exact",
        project_anomaly_class(higher_loop_after_ab),
        Fraction(0),
    )

    stale_cubic_obstruction = op(a=uncancelled_class, e=Fraction(5, 8), m=Fraction(-9, 10))
    assert_not_equal(
        "uncancelled one-loop class cannot be removed by exact terms",
        project_anomaly_class(stale_cubic_obstruction),
        Fraction(0),
    )


def main() -> None:
    check_exact_shifts_preserve_anomaly_class()
    check_singlet_operator_mixing_filter()
    check_callan_symanzik_recurrence()
    check_one_loop_gauge_cancellation_to_exact_breakings()
    print("All Adler-Bardeen nonrenormalization bookkeeping checks passed.")


if __name__ == "__main__":
    main()
