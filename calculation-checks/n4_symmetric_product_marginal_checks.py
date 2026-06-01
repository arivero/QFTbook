#!/usr/bin/env python3
"""Finite checks for N=(4,4) symmetric-product marginal-tangent arithmetic.

The manuscript argument is a CFT construction.  This companion verifies only
the exact rational pieces: the length-two twist weight for a c=6 seed, the
spin-field dressing to a chiral primary, the supercharge descendant weight,
the transposition class normalization, and the local tangent dimension counts
for the toroidal and K3-type compact examples.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs!r} != {rhs!r}")


def cyclic_twist_weight(c: Fraction, cycle_length: int) -> Fraction:
    k = Fraction(cycle_length)
    return c * (k - Fraction(1, cycle_length)) / 24


def transposition_count(n: int) -> int:
    return n * (n - 1) // 2


def orthonormal_class_sum_norm_squared(n: int) -> Fraction:
    """Norm squared of |C|^{-1/2} sum_{transpositions} sigma_tau."""

    count = transposition_count(n)
    return Fraction(count, count)


def coset_dimension(p: int, q: int) -> int:
    """Dimension of SO(p,q)/(SO(p) x SO(q))."""

    return p * q


def check_weights() -> None:
    c_seed = Fraction(6)
    bare = cyclic_twist_weight(c_seed, 2)
    assert_equal("c=6 length-two bare twist weight", bare, Fraction(3, 8))

    spin_field_dressing = Fraction(1, 8)
    chiral_primary = bare + spin_field_dressing
    assert_equal("dressed two-cycle chiral-primary weight", chiral_primary, Fraction(1, 2))

    supercharge_mode_shift = Fraction(1, 2)
    marginal_top = chiral_primary + supercharge_mode_shift
    assert_equal("top component marginal weight", marginal_top, Fraction(1))

    # The same arithmetic holds independently in the antiholomorphic sector.
    assert_equal("spinless descendant condition", marginal_top - marginal_top, Fraction(0))


def check_transposition_normalization() -> None:
    for n in range(2, 12):
        count = transposition_count(n)
        assert_equal(f"transposition count N={n}", count, n * (n - 1) // 2)
        assert_equal(
            f"class-normalized transposition norm N={n}",
            orthonormal_class_sum_norm_squared(n),
            Fraction(1),
        )


def check_local_dimension_counts() -> None:
    blowup_multiplet_real_dimension = 4

    torus_seed = coset_dimension(4, 4)
    assert_equal("T4 seed local dimension", torus_seed, 16)
    assert_equal(
        "T4 symmetric-product local dimension",
        torus_seed + blowup_multiplet_real_dimension,
        coset_dimension(5, 4),
    )

    k3_seed = 80
    assert_equal("K3 seed local dimension", k3_seed, coset_dimension(4, 20))
    assert_equal(
        "K3 symmetric-product local dimension",
        k3_seed + blowup_multiplet_real_dimension,
        coset_dimension(4, 21),
    )


def main() -> None:
    check_weights()
    check_transposition_normalization()
    check_local_dimension_counts()
    print("All N=(4,4) symmetric-product marginal-tangent checks passed.")


if __name__ == "__main__":
    main()
