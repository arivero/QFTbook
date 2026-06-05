#!/usr/bin/env python3
"""Finite checks for the Weinberg--Witten helicity obstruction.

The monograph section states the four-dimensional helicity form of the
Weinberg--Witten theorem and separates it from gauge-theory and gravity
evasions.  This script checks the finite representation-theory bookkeeping
that supports the load-bearing matrix-element argument:

* a Lorentz vector has transverse SO(2) weights -1, 0, +1;
* a rank-two Lorentz tensor has transverse weights -2, -1, 0, +1, +2;
* the forward matrix-element mechanism requires a helicity-two-phase
  component, so current charges are possible only for |h| <= 1/2 and
  stress-tensor momentum matrix elements only for |h| <= 1;
* the leading soft-graviton Ward identity can be gauge invariant even though
  a helicity-two graviton is outside the Weinberg--Witten stress-tensor
  threshold.

Evidence contract.
Target claims: the Weinberg--Witten theorem-boundary section in Volume I
Chapter 17, especially the displayed helicity-weight selection rule and the
soft-graviton cross-reference.
Independent construction: finite SO(2) weight sets for vector and tensor
representations, rational-momentum Ward checks for the leading soft-graviton
factor, and a hypothesis-ledger model for standard evasion routes.
Imported assumptions: the analytic forward-limit step in the original
Weinberg--Witten theorem, existence of standard one-particle helicity states,
and Lorentz covariance/conservation of the local operator whose matrix
element is being tested.
Negative controls: the script rejects a spin-one current charge, rejects a
spin-two stress-tensor momentum matrix element, and rejects a nonuniversal
spin-two soft coupling under a generic hard momentum-conserving reaction.
Scope boundary: a pass checks the finite helicity and Ward bookkeeping; it
does not prove the analytic theorem, higher-dimensional generalizations, or
any microscopic condensed-matter/holographic model.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def assert_equal(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name}: condition failed")


def assert_false(name: str, condition: bool) -> None:
    if condition:
        raise AssertionError(f"{name}: unexpectedly true")


def vector_weights() -> set[int]:
    # In the complex transverse basis e_+, e_-, e_0/e_parallel, a Lorentz
    # vector restricted to the little transverse rotation has weights
    # +1, -1, and 0.  The two longitudinal/time directions both carry weight 0.
    return {-1, 0, 1}


def tensor_weights(rank: int) -> set[int]:
    weights = {sum(choice) for choice in product(vector_weights(), repeat=rank)}
    return weights


def allowed_helicity_for_rank(rank: int, twice_h: int) -> bool:
    # The Weinberg--Witten forward matrix-element argument asks for an SO(2)
    # component with phase exp(2 i h theta).  With twice_h=2h, this component
    # can exist only if 2h is a weight of the tested Lorentz tensor.
    return twice_h in tensor_weights(rank)


def check_weight_sets_and_thresholds() -> None:
    assert_equal("vector weights", vector_weights(), {-1, 0, 1})
    assert_equal("rank-two tensor weights", tensor_weights(2), {-2, -1, 0, 1, 2})

    # Current version: a vector current can support |h| <= 1/2 only.
    assert_true("scalar current charge can pass", allowed_helicity_for_rank(1, 0))
    assert_true("spin-one-half current charge can pass", allowed_helicity_for_rank(1, 1))
    assert_false("spin-one current charge is forbidden", allowed_helicity_for_rank(1, 2))

    # Stress-tensor version: a rank-two tensor can support |h| <= 1 only.
    assert_true("photon stress-tensor momentum can pass", allowed_helicity_for_rank(2, 2))
    assert_false("graviton stress-tensor momentum is forbidden", allowed_helicity_for_rank(2, 4))


def four_dot(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> Fraction:
    return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def scalar_mul(c: Fraction, v: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(c * x for x in v)


def vec_add(*vectors: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum(v[i] for v in vectors) for i in range(4))


def check_soft_graviton_ward_identity_separate_from_ww() -> None:
    # A hard process with two incoming and two outgoing massive momenta.
    p1 = (Fraction(5), Fraction(3), Fraction(0), Fraction(0))
    p2 = (Fraction(13, 2), Fraction(-1), Fraction(2), Fraction(0))
    p3 = (Fraction(11, 2), Fraction(0), Fraction(-1), Fraction(2))
    # Momentum conservation with eta=(-,-,+,+): p4 = p1 + p2 - p3.
    p4 = vec_add(p1, p2, scalar_mul(Fraction(-1), p3))
    etas = (Fraction(-1), Fraction(-1), Fraction(1), Fraction(1))
    momenta = (p1, p2, p3, p4)
    weighted_sum = vec_add(*[scalar_mul(eta, p) for eta, p in zip(etas, momenta)])
    assert_equal("hard momentum conservation", weighted_sum, (Fraction(0),) * 4)

    xi = (Fraction(0), Fraction(2), Fraction(-3), Fraction(5))
    universal_variation = sum(eta * four_dot(xi, p) for eta, p in zip(etas, momenta))
    assert_equal("universal spin-two soft gauge variation", universal_variation, Fraction(0))

    kappas = (Fraction(1), Fraction(2), Fraction(1), Fraction(2))
    nonuniversal_variation = sum(
        eta * kappa * four_dot(xi, p)
        for eta, kappa, p in zip(etas, kappas, momenta)
    )
    assert_true("nonuniversal spin-two coupling fails generically", nonuniversal_variation != 0)

    # The soft Ward identity is therefore compatible with, but does not erase,
    # the Weinberg--Witten helicity-two stress-tensor obstruction.
    assert_false("soft theorem does not supply WW stress tensor", allowed_helicity_for_rank(2, 4))


def check_evasion_hypothesis_ledger() -> None:
    required = {
        "exact_poincare",
        "local_lorentz_covariant_operator",
        "gauge_invariant_physical_operator",
        "standard_massless_particle_pole",
        "nonzero_forward_matrix_element",
    }
    cases = {
        "ordinary photon stress tensor": required,
        "nonabelian color current for gluon": required - {"gauge_invariant_physical_operator"},
        "dynamical gravity pseudotensor": required - {
            "local_lorentz_covariant_operator",
            "gauge_invariant_physical_operator",
        },
        "condensed-matter emergent gauge field": required - {"exact_poincare"},
        "topological line-charge sector": required - {"standard_massless_particle_pole"},
        "holographic bulk graviton": required - {"local_lorentz_covariant_operator"},
    }
    assert_equal("ordinary photon keeps WW stress hypotheses", cases["ordinary photon stress tensor"], required)
    for name, hypotheses in cases.items():
        if name != "ordinary photon stress tensor":
            assert_true(f"{name} drops at least one hypothesis", hypotheses != required)


def main() -> None:
    check_weight_sets_and_thresholds()
    check_soft_graviton_ward_identity_separate_from_ww()
    check_evasion_hypothesis_ledger()
    print("All Weinberg-Witten helicity checks passed.")


if __name__ == "__main__":
    main()
