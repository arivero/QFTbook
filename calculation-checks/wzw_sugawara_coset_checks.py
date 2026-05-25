#!/usr/bin/env python3
"""Exact arithmetic checks for WZW Sugawara and coset formulas."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def wzw_central_charge(level, dimension, dual_coxeter):
    return Fraction(level * dimension, level + dual_coxeter)


def su2_central_charge(level):
    return wzw_central_charge(level, 3, 2)


def su2_primary_weight(level, highest_weight_l):
    # With long root squared length 2, lambda=l omega and
    # (lambda, lambda+2 rho)=l(l+2)/2.
    return Fraction(highest_weight_l * (highest_weight_l + 2), 4 * (level + 2))


def diagonal_su2_minimal_central_charge(level):
    return su2_central_charge(level) + su2_central_charge(1) - su2_central_charge(level + 1)


def minimal_model_central_charge(level):
    return Fraction(1, 1) - Fraction(6, (level + 2) * (level + 3))


def diagonal_coset_weight(level, l_k, l_1, l_diag):
    return su2_primary_weight(level, l_k) + su2_primary_weight(1, l_1) - su2_primary_weight(level + 1, l_diag)


simple_level_one_cases = {
    # (dimension, h^vee, expected c at level 1)
    "SU(2)_1": (3, 2, Fraction(1, 1)),
    "SU(3)_1": (8, 3, Fraction(2, 1)),
    "SU(5)_1": (24, 5, Fraction(4, 1)),
    "E8_1": (248, 30, Fraction(8, 1)),
}

for name, (dimension, dual_coxeter, expected) in simple_level_one_cases.items():
    require(
        wzw_central_charge(1, dimension, dual_coxeter) == expected,
        f"level-one central charge mismatch for {name}",
    )

for level in range(1, 25):
    require(
        diagonal_su2_minimal_central_charge(level) == minimal_model_central_charge(level),
        f"minimal coset central charge mismatch at k={level}",
    )
    for l in range(level + 1):
        require(
            su2_primary_weight(level, l) == Fraction(l * (l + 2), 4 * (level + 2)),
            f"SU(2) primary weight mismatch at k={level}, l={l}",
        )

require(su2_central_charge(1) == Fraction(1, 1), "SU(2)_1 should have c=1")
require(su2_central_charge(2) == Fraction(3, 2), "SU(2)_2 should have c=3/2")
require(su2_primary_weight(1, 1) == Fraction(1, 4), "SU(2)_1 spin-half primary should have h=1/4")
require(su2_primary_weight(2, 1) == Fraction(3, 16), "SU(2)_2 l=1 primary should have h=3/16")

# The k=1 diagonal coset is the Ising model.  These checks verify the
# vacuum, spin, and energy weights from affine branching labels.
require(minimal_model_central_charge(1) == Fraction(1, 2), "k=1 minimal coset should have c=1/2")
require(diagonal_coset_weight(1, 0, 0, 0) == Fraction(0, 1), "Ising vacuum weight mismatch")
require(diagonal_coset_weight(1, 0, 1, 1) == Fraction(1, 16), "Ising spin weight mismatch")
require(diagonal_coset_weight(1, 1, 1, 0) == Fraction(1, 2), "Ising energy weight mismatch")

# The k=2 diagonal coset is the tricritical Ising model.
require(minimal_model_central_charge(2) == Fraction(7, 10), "k=2 minimal coset should have c=7/10")

print("All WZW Sugawara and coset arithmetic checks passed.")
