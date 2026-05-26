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


def sl2_central_charge(level):
    return Fraction(3 * level, level - 2)


def su2_primary_weight(level, highest_weight_l):
    # With long root squared length 2, lambda=l omega and
    # (lambda, lambda+2 rho)=l(l+2)/2.
    return Fraction(highest_weight_l * (highest_weight_l + 2), 4 * (level + 2))


def su2_u1_parafermion_central_charge(level):
    return su2_central_charge(level) - 1


def parafermion_weight(level, ell, charge_m):
    return Fraction(ell * (ell + 2), 4 * (level + 2)) - Fraction(
        charge_m * charge_m,
        4 * level,
    )


def same_mod_integer(left, right):
    return (left - right).denominator == 1


def cigar_central_charge(level):
    return sl2_central_charge(level) - 1


def cigar_weight(level, spin_j, charge_m):
    return -spin_j * (spin_j - 1) / (level - 2) + charge_m * charge_m / level


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
    require(
        su2_u1_parafermion_central_charge(level)
        == Fraction(2 * (level - 1), level + 2),
        f"parafermion central charge mismatch at k={level}",
    )
    for l in range(level + 1):
        require(
            su2_primary_weight(level, l) == Fraction(l * (l + 2), 4 * (level + 2)),
            f"SU(2) primary weight mismatch at k={level}, l={l}",
        )
        for m in range(-2 * level, 2 * level + 1):
            if (l + m) % 2 == 0:
                require(
                    same_mod_integer(
                        parafermion_weight(level, level - l, m + level),
                        parafermion_weight(level, l, m),
                    ),
                    f"parafermion field identification weight mismatch at k={level}, l={l}, m={m}",
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

# The rank-one compact cosets reproduce familiar rational models.
require(
    su2_u1_parafermion_central_charge(2) == Fraction(1, 2),
    "SU(2)_2/U(1) should have c=1/2",
)
require(
    parafermion_weight(2, 1, 1) == Fraction(1, 16),
    "SU(2)_2/U(1) spin weight mismatch",
)
require(
    parafermion_weight(2, 2, 0) == Fraction(1, 2),
    "SU(2)_2/U(1) energy weight mismatch",
)
require(
    same_mod_integer(parafermion_weight(2, 0, 2), Fraction(1, 2)),
    "SU(2)_2/U(1) parafermion current weight mismatch",
)
require(
    su2_u1_parafermion_central_charge(3) == Fraction(4, 5),
    "SU(2)_3/U(1) should have c=4/5",
)
require(
    parafermion_weight(3, 1, 1) == Fraction(1, 15),
    "SU(2)_3/U(1) Potts spin weight mismatch",
)
require(
    parafermion_weight(3, 2, 0) == Fraction(2, 5),
    "SU(2)_3/U(1) Potts energy weight mismatch",
)
require(
    same_mod_integer(parafermion_weight(3, 0, 2), Fraction(2, 3)),
    "SU(2)_3/U(1) parafermion current weight mismatch",
)

for level in range(3, 21):
    require(
        cigar_central_charge(level) == Fraction(2, 1) + Fraction(6, level - 2),
        f"SL(2,R)/U(1) cigar central charge mismatch at k={level}",
    )
    require(
        cigar_weight(level, Fraction(1, 2), Fraction(0, 1)) == Fraction(1, 4 * (level - 2)),
        f"SL(2,R)/U(1) j=1/2 threshold weight mismatch at k={level}",
    )
    for n in range(-3, 4):
        for winding in range(-3, 4):
            m = Fraction(n + level * winding, 2)
            m_bar = Fraction(-n + level * winding, 2)
            require(
                cigar_weight(level, Fraction(1, 2), m)
                - cigar_weight(level, Fraction(1, 2), m_bar)
                == n * winding,
                f"SL(2,R)/U(1) integer-spin mismatch at k={level}, n={n}, w={winding}",
            )

print("All WZW Sugawara and rank-one coset arithmetic checks passed.")
