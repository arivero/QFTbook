#!/usr/bin/env python3
"""Finite checks for the monopole/dyon quantum-sector chapter.

Evidence contract.

Target claims:
- `prop:monopole-chapter-dsz-pairing`: the physical Witten-shifted electric
  charges give a theta-independent integer DSZ pairing.
- `eq:monopole-chapter-field-angular-momentum`: the long-range fields carry
  half the DSZ pairing as angular momentum.
- `prop:monopole-chapter-monopole-harmonics`: the two-body angular sector uses
  monopole harmonics with `j=|N|/2+ell` and barrier
  `j(j+1)-N^2/4`.
- `ca:monopole-chapter-aligned-bps-no-force`: same-ray BPS charge vectors
  cancel the leading vector-plus-scalar static tail.

Independent construction:
- The checks build the Witten-shifted charges from integer labels, compute
  the antisymmetric two-sector pairing, enumerate finite monopole-harmonic
  angular momenta, and test the BPS tail using exact rational Pythagorean
  charge vectors.

Imported assumptions:
- The primitive charge convention is `e*g_m=2*pi`; the long-range two-body
  Hilbert-space statement uses the standard charge-monopole rotation algebra;
  the BPS no-force check is an Abelian tail benchmark with scalar charge equal
  to the norm of the electromagnetic charge vector.

Negative controls:
- The script rejects a theta-dependent one-body `Q_E Q_M` shortcut, omitting
  the factor `1/2` in field angular momentum, ordinary spherical harmonics for
  nonzero DSZ pairing, vector-Coulomb-only no-force, and anti-aligned BPS
  charge vectors.

Scope boundary:
- Passing these checks proves finite charge-lattice algebra and exact
  two-body kinematic bookkeeping.  It does not construct the full monopole
  moduli-space metric, prove a supersymmetric BPS spectrum, or compute
  nonzero-mode/radiative corrections.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def assert_not_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs == rhs:
        raise AssertionError(f"{name}: wrong shortcut unexpectedly matched {lhs!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def dsz_integer(gamma_1: tuple[int, int], gamma_2: tuple[int, int]) -> int:
    ne_1, nm_1 = gamma_1
    ne_2, nm_2 = gamma_2
    return ne_1 * nm_2 - nm_1 * ne_2


def check_witten_effect_dsz_pairing() -> None:
    ne_1, nm_1, ne_2, nm_2 = sp.symbols("ne_1 nm_1 ne_2 nm_2", integer=True)
    theta, e = sp.symbols("theta e", nonzero=True)
    g_m = 2 * sp.pi / e

    qe_1 = e * (ne_1 + theta * nm_1 / (2 * sp.pi))
    qe_2 = e * (ne_2 + theta * nm_2 / (2 * sp.pi))
    qm_1 = g_m * nm_1
    qm_2 = g_m * nm_2

    pairing = sp.simplify((qe_1 * qm_2 - qm_1 * qe_2) / (2 * sp.pi))
    expected = ne_1 * nm_2 - nm_1 * ne_2
    assert_zero("theta-independent DSZ pairing", pairing - expected)

    one_body_shortcut = sp.simplify(qe_1 * qm_1 / (2 * sp.pi))
    assert_not_equal("one-body electric-magnetic product is theta-dependent", one_body_shortcut, ne_1 * nm_1)
    assert_equal("sample DSZ integer", dsz_integer((2, 1), (-1, 3)), 7)


def check_field_angular_momentum_half_integer() -> None:
    samples = [((1, 0), (0, 1)), ((2, 1), (-1, 3)), ((1, 2), (3, -1))]
    for gamma_1, gamma_2 in samples:
        n = dsz_integer(gamma_1, gamma_2)
        field_spin = Fraction(n, 2)
        assert_equal("twice field angular momentum is DSZ", 2 * field_spin, n)
        assert_not_equal("missing half in field angular momentum", field_spin, n)

    odd_pairing_spin = Fraction(dsz_integer((1, 0), (0, 1)), 2)
    if odd_pairing_spin.denominator != 2:
        raise AssertionError("odd DSZ pairing should give half-integer field spin")


def check_monopole_harmonic_partial_waves() -> None:
    for n in range(-5, 6):
        nu = Fraction(abs(n), 2)
        for ell in range(0, 6):
            j = nu + ell
            degeneracy = 2 * j + 1
            if degeneracy.denominator != 1:
                raise AssertionError("monopole-harmonic degeneracy should be integral")

            barrier = j * (j + 1) - Fraction(n * n, 4)
            expected = Fraction(ell * (ell + abs(n) + 1), 1) + nu
            assert_equal("monopole-harmonic barrier", barrier, expected)
            if barrier < 0:
                raise AssertionError("monopole-harmonic barrier should be nonnegative")

        if n != 0:
            ordinary_lowest_j = Fraction(0, 1)
            if ordinary_lowest_j >= nu:
                raise AssertionError("ordinary spherical harmonic shortcut should fail for nonzero DSZ")

    n = 0
    for ell in range(0, 6):
        j = Fraction(ell, 1)
        assert_equal("N=0 spherical-harmonic limit", j * (j + 1), ell * (ell + 1))


def dot(v: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] * w[0] + v[1] * w[1]


def norm_pythagorean(v: tuple[Fraction, Fraction]) -> Fraction:
    squares = v[0] * v[0] + v[1] * v[1]
    root = int(sp.sqrt(squares.numerator * squares.denominator))
    if root * root != squares.numerator * squares.denominator:
        raise AssertionError(f"not a rational Pythagorean norm: {v}")
    return Fraction(root, squares.denominator)


def bps_tail_numerator(v: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> Fraction:
    return dot(v, w) - norm_pythagorean(v) * norm_pythagorean(w)


def check_bps_aligned_no_force_tail() -> None:
    charge = (Fraction(3), Fraction(4))
    aligned = (Fraction(6), Fraction(8))
    assert_equal("same-ray BPS no-force tail", bps_tail_numerator(charge, aligned), 0)

    vector_only = dot(charge, aligned)
    assert_not_equal("vector Coulomb term alone does not cancel", vector_only, 0)

    nonparallel = (Fraction(4), Fraction(3))
    assert_not_equal("nonparallel BPS tail", bps_tail_numerator(charge, nonparallel), 0)

    anti_aligned = (Fraction(-3), Fraction(-4))
    assert_equal("anti-aligned BPS tail is attractive", bps_tail_numerator(charge, anti_aligned), -50)


def main() -> None:
    check_witten_effect_dsz_pairing()
    check_field_angular_momentum_half_integer()
    check_monopole_harmonic_partial_waves()
    check_bps_aligned_no_force_tail()
    print("All monopole/dyon quantum-sector checks passed.")


if __name__ == "__main__":
    main()
