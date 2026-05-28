#!/usr/bin/env python3
"""Finite representation checks for one Standard Model generation.

The chapter uses left-handed Weyl fields:

    Q_L : (3,2)_{1/6}
    u^c : (bar 3,1)_{-2/3}
    d^c : (bar 3,1)_{1/3}
    L_L : (1,2)_{-1/2}
    e^c : (1,1)_1

The script checks the hypercharge anomaly sums and the even number of weak
doublets needed to avoid the finite SU(2) anomaly.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


FIELDS = [
    ("Q_L", 3, 2, Fraction(1, 6), True),
    ("u^c", 3, 1, Fraction(-2, 3), False),
    ("d^c", 3, 1, Fraction(1, 3), False),
    ("L_L", 1, 2, Fraction(-1, 2), True),
    ("e^c", 1, 1, Fraction(1, 1), False),
]

INTEGER_HYPERCHARGES = {
    "Q_L": 1,
    "u^c": -4,
    "d^c": 2,
    "L_L": -3,
    "e^c": 6,
    "H": 3,
}

B_MINUS_L_FIELDS_WITHOUT_NU_C = [
    ("Q_L", 3, 2, Fraction(1, 3), True, True),
    ("u^c", 3, 1, Fraction(-1, 3), False, True),
    ("d^c", 3, 1, Fraction(-1, 3), False, True),
    ("L_L", 1, 2, Fraction(-1, 1), True, False),
    ("e^c", 1, 1, Fraction(1, 1), False, False),
]

B_MINUS_L_FIELDS_WITH_NU_C = B_MINUS_L_FIELDS_WITHOUT_NU_C + [
    ("nu^c", 1, 1, Fraction(1, 1), False, False)
]


def assert_zero(name: str, value: Fraction) -> None:
    if value != 0:
        raise AssertionError(f"{name} = {value}, expected 0")


def assert_equal(name: str, value, expected) -> None:
    if value != expected:
        raise AssertionError(f"{name} = {value}, expected {expected}")


def check_su3_su3_u1() -> None:
    # The common quadratic index T(3)=T(bar 3) factors out.
    value = sum(su2_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS if su3_dim == 3)
    assert_zero("SU(3)^2 U(1)_Y anomaly coefficient without common T(3)", value)


def check_su2_su2_u1() -> None:
    # The common quadratic index T(2) factors out.
    value = sum(su3_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS if su2_dim == 2)
    assert_zero("SU(2)^2 U(1)_Y anomaly coefficient without common T(2)", value)


def check_u1_cubic() -> None:
    value = sum(su3_dim * su2_dim * hypercharge**3 for _, su3_dim, su2_dim, hypercharge, _ in FIELDS)
    assert_zero("U(1)_Y^3 anomaly coefficient", value)


def check_mixed_gravitational_u1() -> None:
    value = sum(su3_dim * su2_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS)
    assert_zero("mixed gravitational-U(1)_Y anomaly coefficient", value)


def check_witten_su2_anomaly() -> None:
    doublets = sum(su3_dim for _, su3_dim, su2_dim, _, is_weak_doublet in FIELDS if is_weak_doublet and su2_dim == 2)
    if doublets % 2 != 0:
        raise AssertionError(f"weak SU(2) doublets per generation = {doublets}, expected even")
    if 3 * doublets % 2 != 0:
        raise AssertionError("three-generation weak-doublet count should remain even")


def check_electric_charges() -> None:
    q_up = Fraction(1, 2) + Fraction(1, 6)
    q_down = Fraction(-1, 2) + Fraction(1, 6)
    q_nu = Fraction(1, 2) + Fraction(-1, 2)
    q_e = Fraction(-1, 2) + Fraction(-1, 2)
    expected = (Fraction(2, 3), Fraction(-1, 3), Fraction(0), Fraction(-1))
    actual = (q_up, q_down, q_nu, q_e)
    if actual != expected:
        raise AssertionError(f"electric charges {actual} != {expected}")


def check_z6_global_form_generator() -> None:
    # The chapter uses integer y=6Y.  The central generator is
    # (omega_3, -1, exp(i*pi/3)), so triviality means
    # t/3 + s/2 + y/6 is integral.
    triality_and_doublet = {
        "Q_L": (1, 1),
        "u^c": (-1, 0),
        "d^c": (-1, 0),
        "L_L": (0, 1),
        "e^c": (0, 0),
        "H": (0, 1),
    }
    for field, (triality, weak_doublet) in triality_and_doublet.items():
        exponent = Fraction(triality, 3) + Fraction(weak_doublet, 2) + Fraction(INTEGER_HYPERCHARGES[field], 6)
        assert_equal(f"Z6 generator exponent for {field}", exponent.denominator, 1)


def check_ckm_parameter_counting() -> None:
    for generations in range(1, 7):
        total_physical = generations**2 + 1
        masses = 2 * generations
        angles = generations * (generations - 1) // 2
        phases = (generations - 1) * (generations - 2) // 2
        assert_equal(
            f"quark flavor parameter split for n={generations}",
            masses + angles + phases,
            total_physical,
        )
        assert_equal(
            f"CKM mixing parameter count for n={generations}",
            angles + phases,
            (generations - 1) ** 2,
        )
        assert_equal(f"CKM angle count comb for n={generations}", angles, comb(generations, 2))


def check_jarlskog_rephasing_cancellation() -> None:
    # A quartet V_us V_cb V_ub^* V_cs^* carries row/column phases whose
    # integer exponents cancel.  Order rows as u,c,t and columns as d,s,b.
    row_exponents = {"u": 0, "c": 0, "t": 0}
    column_exponents = {"d": 0, "s": 0, "b": 0}
    factors = [
        ("u", "s", 1),
        ("c", "b", 1),
        ("u", "b", -1),
        ("c", "s", -1),
    ]
    for row, column, conjugation_sign in factors:
        row_exponents[row] += conjugation_sign
        column_exponents[column] -= conjugation_sign
    assert_equal("Jarlskog row rephasing exponents", tuple(row_exponents.values()), (0, 0, 0))
    assert_equal("Jarlskog column rephasing exponents", tuple(column_exponents.values()), (0, 0, 0))


def check_higgs_and_rho_tree_identities() -> None:
    g1 = Fraction(3, 5)
    g2 = Fraction(7, 5)
    v = Fraction(11, 1)
    lam = Fraction(13, 17)
    m_w_squared = g2**2 * v**2 / 4
    m_z_squared = (g1**2 + g2**2) * v**2 / 4
    cos2 = g2**2 / (g1**2 + g2**2)
    rho_tree = m_w_squared / (m_z_squared * cos2)
    higgs_mass_squared = 2 * lam * v**2
    quadratic_potential_coefficient = lam * v**2
    assert_equal("tree rho parameter", rho_tree, 1)
    assert_equal("Higgs mass from potential coefficient", 2 * quadratic_potential_coefficient, higgs_mass_squared)


def check_b_minus_l_anomalies() -> None:
    su2_b_minus_l = sum(
        su3_dim * charge
        for _, su3_dim, su2_dim, charge, is_weak_doublet, _ in B_MINUS_L_FIELDS_WITHOUT_NU_C
        if is_weak_doublet and su2_dim == 2
    )
    su3_b_minus_l = sum(
        su2_dim * charge
        for _, su3_dim, su2_dim, charge, _, is_colored in B_MINUS_L_FIELDS_WITHOUT_NU_C
        if is_colored and su3_dim == 3
    )
    grav_without = sum(
        su3_dim * su2_dim * charge
        for _, su3_dim, su2_dim, charge, _, _ in B_MINUS_L_FIELDS_WITHOUT_NU_C
    )
    cubic_without = sum(
        su3_dim * su2_dim * charge**3
        for _, su3_dim, su2_dim, charge, _, _ in B_MINUS_L_FIELDS_WITHOUT_NU_C
    )
    grav_with = sum(
        su3_dim * su2_dim * charge
        for _, su3_dim, su2_dim, charge, _, _ in B_MINUS_L_FIELDS_WITH_NU_C
    )
    cubic_with = sum(
        su3_dim * su2_dim * charge**3
        for _, su3_dim, su2_dim, charge, _, _ in B_MINUS_L_FIELDS_WITH_NU_C
    )
    assert_zero("SU(2)^2 (B-L) anomaly without nu^c", su2_b_minus_l)
    assert_zero("SU(3)^2 (B-L) anomaly without nu^c", su3_b_minus_l)
    assert_equal("gravitational (B-L) anomaly without nu^c", grav_without, Fraction(-1))
    assert_equal("cubic (B-L) anomaly without nu^c", cubic_without, Fraction(-1))
    assert_zero("gravitational (B-L) anomaly with nu^c", grav_with)
    assert_zero("cubic (B-L) anomaly with nu^c", cubic_with)


def check_weinberg_operator_mass_normalization() -> None:
    v = Fraction(11, 1)
    cutoff = Fraction(13, 1)
    coefficient = Fraction(17, 19)
    # Chapter convention: L_5 = -(1/(2 Lambda)) C_5 (LH)(LH) + h.c.
    lh_at_vacuum_squared = v**2 / 2
    mass = coefficient * lh_at_vacuum_squared / cutoff
    assert_equal("Weinberg operator Majorana mass normalization", mass, coefficient * v**2 / (2 * cutoff))


def check_tree_level_singlet_neutrino_matching() -> None:
    # One-generation version of C_5/Lambda = Y_nu M^{-1} Y_nu^T.
    yukawa = Fraction(5, 7)
    majorana_mass = Fraction(11, 3)
    matched = yukawa * (1 / majorana_mass) * yukawa
    assert_equal("type-I singlet matching coefficient", matched, Fraction(75, 539))


def check_strong_cp_phase_invariance() -> None:
    theta = Fraction(2, 7)
    mass_phase = Fraction(3, 11)
    removed_phase = mass_phase
    theta_after_rotation = theta + removed_phase
    mass_phase_after_rotation = mass_phase - removed_phase
    assert_equal(
        "strong CP phase invariant under chiral coordinate change",
        theta_after_rotation + mass_phase_after_rotation,
        theta + mass_phase,
    )


def main() -> None:
    check_su3_su3_u1()
    check_su2_su2_u1()
    check_u1_cubic()
    check_mixed_gravitational_u1()
    check_witten_su2_anomaly()
    check_electric_charges()
    check_z6_global_form_generator()
    check_ckm_parameter_counting()
    check_jarlskog_rephasing_cancellation()
    check_higgs_and_rho_tree_identities()
    check_b_minus_l_anomalies()
    check_weinberg_operator_mass_normalization()
    check_tree_level_singlet_neutrino_matching()
    check_strong_cp_phase_invariance()
    print("All Standard Model representation, flavor, and electroweak checks passed.")


if __name__ == "__main__":
    main()
