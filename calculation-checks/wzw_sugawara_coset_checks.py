#!/usr/bin/env python3
"""Arithmetic and finite modular-data checks for WZW/coset formulas."""

import cmath
import math
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


def parafermion_primary_orbits(level):
    selected_labels = [
        (ell, charge_m)
        for ell in range(level + 1)
        for charge_m in range(2 * level)
        if is_parafermion_label(level, ell, charge_m)
    ]
    return sorted(
        {parafermion_canonical_label(level, ell, charge_m) for ell, charge_m in selected_labels}
    )


def parafermion_modular_s(level, left, right):
    ell_left, charge_left = left
    ell_right, charge_right = right
    sine = math.sin(math.pi * (ell_left + 1) * (ell_right + 1) / (level + 2))
    phase = cmath.exp(-1j * math.pi * charge_left * charge_right / level)
    return 2 * sine * phase / math.sqrt(level * (level + 2))


def require_close_complex(value, target, message, tolerance=1.0e-9):
    if abs(value - target) > tolerance:
        raise AssertionError(f"{message}: got {value!r}, expected {target!r}")


def check_parafermion_modular_verlinde(max_level=7):
    for level in range(1, max_level + 1):
        labels = parafermion_primary_orbits(level)
        vacuum = parafermion_canonical_label(level, 0, 0)

        for left in labels:
            for right in labels:
                inner = sum(
                    parafermion_modular_s(level, left, x)
                    * parafermion_modular_s(level, right, x).conjugate()
                    for x in labels
                )
                expected_inner = 1 if left == right else 0
                require_close_complex(
                    inner,
                    expected_inner,
                    f"parafermion S unitarity k={level}, left={left}, right={right}",
                )

        for left in labels:
            for right in labels:
                fusion_targets = parafermion_fusion_targets(level, left, right)
                for target in labels:
                    verlinde = sum(
                        parafermion_modular_s(level, left, x)
                        * parafermion_modular_s(level, right, x)
                        * parafermion_modular_s(level, target, x).conjugate()
                        / parafermion_modular_s(level, vacuum, x)
                        for x in labels
                    )
                    expected = 1 if target in fusion_targets else 0
                    require_close_complex(
                        verlinde,
                        expected,
                        f"parafermion Verlinde k={level}, left={left}, right={right}, target={target}",
                    )


def epsilon2(left, right):
    if (left, right) == (0, 1):
        return Fraction(1)
    if (left, right) == (1, 0):
        return Fraction(-1)
    return Fraction(0)


four_spinor_indices = [
    (a, b, c, d)
    for a in (0, 1)
    for b in (0, 1)
    for c in (0, 1)
    for d in (0, 1)
]


def invariant_s(index):
    a, b, c, d = index
    return epsilon2(a, b) * epsilon2(c, d)


def invariant_t(index):
    a, b, c, d = index
    return epsilon2(a, c) * epsilon2(b, d)


def invariant_u(index):
    a, b, c, d = index
    return epsilon2(a, d) * epsilon2(b, c)


invariant_s_vector = [invariant_s(index) for index in four_spinor_indices]
invariant_t_vector = [invariant_t(index) for index in four_spinor_indices]
invariant_u_vector = [invariant_u(index) for index in four_spinor_indices]


def add_vectors(left, right):
    return [a + b for a, b in zip(left, right)]


def scale_vector(coefficient, vector):
    return [coefficient * entry for entry in vector]


def apply_swap(vector, first, second):
    output = []
    for index in four_spinor_indices:
        swapped = list(index)
        swapped[first], swapped[second] = swapped[second], swapped[first]
        output.append(vector[four_spinor_indices.index(tuple(swapped))])
    return output


def apply_su2_omega(vector, first, second):
    return add_vectors(
        apply_swap(vector, first, second),
        scale_vector(Fraction(-1, 2), vector),
    )


def coordinates_in_st_basis(vector):
    for row_1 in range(len(four_spinor_indices)):
        for row_2 in range(row_1 + 1, len(four_spinor_indices)):
            determinant = (
                invariant_s_vector[row_1] * invariant_t_vector[row_2]
                - invariant_s_vector[row_2] * invariant_t_vector[row_1]
            )
            if determinant == 0:
                continue
            coefficient_s = (
                vector[row_1] * invariant_t_vector[row_2]
                - vector[row_2] * invariant_t_vector[row_1]
            ) / determinant
            coefficient_t = (
                invariant_s_vector[row_1] * vector[row_2]
                - invariant_s_vector[row_2] * vector[row_1]
            ) / determinant
            if all(
                coefficient_s * invariant_s_vector[index]
                + coefficient_t * invariant_t_vector[index]
                == vector[index]
                for index in range(len(four_spinor_indices))
            ):
                return coefficient_s, coefficient_t
    raise AssertionError("tensor is not in the invariant s/t span")


def check_su2_four_fundamental_kz_matrices():
    require(
        all(
            invariant_s_vector[index]
            - invariant_t_vector[index]
            + invariant_u_vector[index]
            == 0
            for index in range(len(four_spinor_indices))
        ),
        "SU(2) four-invariant epsilon relation failed",
    )

    omega_12_s = coordinates_in_st_basis(apply_su2_omega(invariant_s_vector, 0, 1))
    omega_12_t = coordinates_in_st_basis(apply_su2_omega(invariant_t_vector, 0, 1))
    omega_23_s = coordinates_in_st_basis(apply_su2_omega(invariant_s_vector, 1, 2))
    omega_23_t = coordinates_in_st_basis(apply_su2_omega(invariant_t_vector, 1, 2))

    require(omega_12_s == (Fraction(-3, 2), 0), "Omega_12 on I_s mismatch")
    require(omega_12_t == (Fraction(-1), Fraction(1, 2)), "Omega_12 on I_t mismatch")
    require(omega_23_s == (Fraction(-1, 2), Fraction(1)), "Omega_23 on I_s mismatch")
    require(omega_23_t == (Fraction(1), Fraction(-1, 2)), "Omega_23 on I_t mismatch")

    fundamental_casimir = Fraction(3, 2)
    singlet_casimir = Fraction(0)
    triplet_casimir = Fraction(4)
    require(
        (singlet_casimir - 2 * fundamental_casimir) / 2 == Fraction(-3, 2),
        "SU(2) singlet residue eigenvalue mismatch",
    )
    require(
        (triplet_casimir - 2 * fundamental_casimir) / 2 == Fraction(1, 2),
        "SU(2) triplet residue eigenvalue mismatch",
    )


def same_mod_integer(left, right):
    return (left - right).denominator == 1


def cigar_central_charge(level):
    return sl2_central_charge(level) - 1


def cigar_weight(level, spin_j, charge_m):
    return -spin_j * (spin_j - 1) / (level - 2) + charge_m * charge_m / level


def rank_one_rotational_geometry(kind, f_squared):
    """Return metric equation residuals and scalar anomaly constant times K.

    The angular metric equation is divided by f^2, so tests avoid f=0.
    """
    if kind == "cigar":
        f_prime_over_f_times_phi_prime = -(1 - f_squared)
        f_second_over_f = -2 * (1 - f_squared)
        phi_second = -(1 - f_squared)
    elif kind == "bell":
        f_prime_over_f_times_phi_prime = 1 + f_squared
        f_second_over_f = 2 * (1 + f_squared)
        phi_second = 1 + f_squared
    else:
        raise ValueError(f"unknown rank-one geometry kind: {kind}")

    radial_metric_residual = -f_second_over_f + 2 * phi_second
    angular_metric_residual_over_f_squared = (
        -f_second_over_f + 2 * f_prime_over_f_times_phi_prime
    )
    scalar_anomaly_times_scale = f_squared - Fraction(
        phi_second + f_prime_over_f_times_phi_prime,
        2,
    )
    return (
        radial_metric_residual,
        angular_metric_residual_over_f_squared,
        scalar_anomaly_times_scale,
    )


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
    primary_orbits = set(parafermion_primary_orbits(level))
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

check_parafermion_modular_verlinde()
check_su2_four_fundamental_kz_matrices()

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

for sample in [Fraction(1, 9), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
    require(
        rank_one_rotational_geometry("cigar", sample) == (0, 0, 1),
        f"cigar one-loop geometry residual mismatch at tanh^2 rho={sample}",
    )

for sample in [Fraction(1, 9), Fraction(1, 2), Fraction(2, 1), Fraction(5, 1)]:
    require(
        rank_one_rotational_geometry("bell", sample) == (0, 0, -1),
        f"bell one-loop geometry residual mismatch at tan^2 theta={sample}",
    )

for level in range(3, 21):
    require(
        cigar_central_charge(level)
        - (Fraction(2, 1) + Fraction(6, level))
        == Fraction(12, level * (level - 2)),
        f"cigar exact-versus-large-level central charge mismatch at k={level}",
    )

for level in range(1, 21):
    require(
        su2_u1_parafermion_central_charge(level)
        - (Fraction(2, 1) - Fraction(6, level))
        == Fraction(12, level * (level + 2)),
        f"bell exact-versus-large-level central charge mismatch at k={level}",
    )

print("All WZW Sugawara, KZ, and rank-one coset arithmetic/fusion/geometry checks passed.")
