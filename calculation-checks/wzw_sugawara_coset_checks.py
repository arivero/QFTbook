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


def reduce_parafermion_charge(level, charge_m):
    return charge_m % (2 * level)


def is_parafermion_label(level, ell, charge_m):
    return 0 <= ell <= level and (ell + reduce_parafermion_charge(level, charge_m)) % 2 == 0


def parafermion_identified_label(level, ell, charge_m):
    return (level - ell, reduce_parafermion_charge(level, charge_m + level))


def parafermion_canonical_label(level, ell, charge_m):
    charge_m = reduce_parafermion_charge(level, charge_m)
    require(
        is_parafermion_label(level, ell, charge_m),
        f"invalid parafermion label k={level}, ell={ell}, m={charge_m}",
    )
    return min((ell, charge_m), parafermion_identified_label(level, ell, charge_m))


def su2_fusion_targets(level, ell_left, ell_right):
    lower = abs(ell_left - ell_right)
    upper = min(ell_left + ell_right, 2 * level - ell_left - ell_right)
    return list(range(lower, upper + 1, 2))


def parafermion_fusion_targets(level, left, right):
    ell_left, charge_left = left
    ell_right, charge_right = right
    targets = set()
    for ell_target in su2_fusion_targets(level, ell_left, ell_right):
        targets.add(
            parafermion_canonical_label(
                level,
                ell_target,
                charge_left + charge_right,
            )
        )
    return targets


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

    selected_labels = [
        (l, m)
        for l in range(level + 1)
        for m in range(2 * level)
        if is_parafermion_label(level, l, m)
    ]
    primary_orbits = {parafermion_canonical_label(level, l, m) for l, m in selected_labels}
    require(
        len(selected_labels) == level * (level + 1),
        f"parafermion selected-label count mismatch at k={level}",
    )
    require(
        len(primary_orbits) == level * (level + 1) // 2,
        f"parafermion primary-orbit count mismatch at k={level}",
    )
    for l, m in selected_labels:
        require(
            parafermion_canonical_label(level, l, m)
            == parafermion_canonical_label(level, *parafermion_identified_label(level, l, m)),
            f"parafermion canonicalization mismatch at k={level}, l={l}, m={m}",
        )

    simple_current = parafermion_canonical_label(level, 0, 2)
    vacuum = parafermion_canonical_label(level, 0, 0)
    current_power = vacuum
    for power in range(1, level + 1):
        current_power = next(
            iter(parafermion_fusion_targets(level, current_power, simple_current))
        )
        expected = (
            vacuum
            if power == level
            else parafermion_canonical_label(level, 0, 2 * power)
        )
        require(
            current_power == expected,
            f"parafermion simple-current power mismatch at k={level}, power={power}",
        )
    for label in primary_orbits:
        require(
            parafermion_fusion_targets(level, simple_current, label)
            == {parafermion_canonical_label(level, label[0], label[1] + 2)},
            f"parafermion simple-current charge shift mismatch at k={level}, label={label}",
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

ising_vacuum = parafermion_canonical_label(2, 0, 0)
ising_spin = parafermion_canonical_label(2, 1, 1)
ising_energy = parafermion_canonical_label(2, 2, 0)
require(
    parafermion_fusion_targets(2, ising_spin, ising_spin)
    == {ising_vacuum, ising_energy},
    "SU(2)_2/U(1) Ising spin fusion mismatch",
)
require(
    parafermion_fusion_targets(2, ising_energy, ising_energy) == {ising_vacuum},
    "SU(2)_2/U(1) Ising energy fusion mismatch",
)
require(
    parafermion_fusion_targets(2, ising_energy, ising_spin) == {ising_spin},
    "SU(2)_2/U(1) Ising energy-spin fusion mismatch",
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
    for spin_j in [
        Fraction(-1, 2),
        Fraction(0, 1),
        Fraction(1, 3),
        Fraction(3, 2),
        Fraction(5, 2),
    ]:
        require(
            cigar_weight(level, spin_j, Fraction(1, 1))
            == cigar_weight(level, 1 - spin_j, Fraction(1, 1)),
            f"SL(2,R)/U(1) reflection weight mismatch at k={level}, j={spin_j}",
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

print("All WZW Sugawara and rank-one coset arithmetic/fusion checks passed.")
