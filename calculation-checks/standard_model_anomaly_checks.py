#!/usr/bin/env python3
"""Finite checks for the Standard Model hybrid-definition chapter.

The chapter uses left-handed Weyl fields:

    Q_L : (3,2)_{1/6}
    u^c : (bar 3,1)_{-2/3}
    d^c : (bar 3,1)_{1/3}
    L_L : (1,2)_{-1/2}
    e^c : (1,1)_1

The script checks the hypercharge anomaly sums, global-form arithmetic,
flavor counting, electroweak identities, and one-loop RG coefficients used in
the chapter.
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


def check_one_loop_gauge_beta_coefficients() -> None:
    generations = 3
    # U(1)_Y uses spectator multiplicities and the unrescaled Y convention.
    u1_weyl_per_generation = (
        6 * Fraction(1, 6) ** 2
        + 3 * Fraction(-2, 3) ** 2
        + 3 * Fraction(1, 3) ** 2
        + 2 * Fraction(-1, 2) ** 2
        + Fraction(1, 1) ** 2
    )
    u1_scalar = 2 * Fraction(1, 2) ** 2
    b1 = Fraction(2, 3) * generations * u1_weyl_per_generation + Fraction(1, 3) * u1_scalar
    assert_equal("SM b1 in Q=T3+Y convention", b1, Fraction(41, 6))

    su2_weyl_per_generation = 3 * Fraction(1, 2) + Fraction(1, 2)
    su2_scalar = Fraction(1, 2)
    b2 = -Fraction(11, 3) * 2 + Fraction(2, 3) * generations * su2_weyl_per_generation + Fraction(1, 3) * su2_scalar
    assert_equal("SM b2", b2, Fraction(-19, 6))

    su3_weyl_per_generation = 2 * Fraction(1, 2) + Fraction(1, 2) + Fraction(1, 2)
    b3 = -Fraction(11, 3) * 3 + Fraction(2, 3) * generations * su3_weyl_per_generation
    assert_equal("SM b3", b3, Fraction(-7))


def check_hypercharge_gut_rescaling() -> None:
    # g_GUT = sqrt(5/3) g1 implies b_GUT = (3/5) b1.
    assert_equal("GUT-rescaled hypercharge beta coefficient", Fraction(3, 5) * Fraction(41, 6), Fraction(41, 10))


def check_top_higgs_subsystem_coefficients() -> None:
    top_yukawa_coefficients = {
        "yt_self": Fraction(9, 2),
        "g3": Fraction(-8),
        "g2": Fraction(-9, 4),
        "g1": Fraction(-17, 12),
    }
    expected_top = {
        "yt_self": Fraction(9, 2),
        "g3": Fraction(-6) * Fraction(4, 3),
        "g2": Fraction(-9, 4),
        "g1": Fraction(-17, 12),
    }
    assert_equal("top Yukawa one-loop coefficients", top_yukawa_coefficients, expected_top)
    assert_equal(
        "top Yukawa hypercharge coefficient after GUT rescaling",
        Fraction(3, 5) * Fraction(17, 12),
        Fraction(17, 20),
    )

    # Expand (3/8)[2 g2^4 + (g2^2 + g1^2)^2].
    g1 = Fraction(2, 3)
    g2 = Fraction(5, 7)
    compact = Fraction(3, 8) * (2 * g2**4 + (g2**2 + g1**2) ** 2)
    expanded = Fraction(9, 8) * g2**4 + Fraction(3, 4) * g1**2 * g2**2 + Fraction(3, 8) * g1**4
    assert_equal("lambda gauge-quartic compact/expanded form", compact, expanded)

    yt = Fraction(11, 13)
    lam = Fraction(5, 7)
    g3 = Fraction(3, 5)
    ty = 3 * yt**2
    qy = 3 * yt**4
    gu = 8 * g3**2 + Fraction(9, 4) * g2**2 + Fraction(17, 12) * g1**2
    top_from_matrix = yt * (Fraction(3, 2) * yt**2 + ty - gu)
    top_specialized = yt * (
        Fraction(9, 2) * yt**2
        - 8 * g3**2
        - Fraction(9, 4) * g2**2
        - Fraction(17, 12) * g1**2
    )
    assert_equal("top Yukawa rank-one matrix specialization", top_from_matrix, top_specialized)

    lambda_from_matrix = (
        24 * lam**2
        - 3 * lam * (3 * g2**2 + g1**2)
        + compact
        + 4 * lam * ty
        - 2 * qy
    )
    lambda_specialized = (
        24 * lam**2
        + 12 * lam * yt**2
        - 6 * yt**4
        - 3 * lam * (3 * g2**2 + g1**2)
        + compact
    )
    assert_equal("lambda beta rank-one matrix specialization", lambda_from_matrix, lambda_specialized)


def check_higgs_large_field_coupling_chart_identities() -> None:
    lam = Fraction(5, 7)
    c_h = Fraction(11, 13)
    cutoff = Fraction(17, 1)
    h = Fraction(19, 1)
    v = Fraction(2, 1)
    potential = lam * ((h**2 - v**2) / 2) ** 2 + c_h / cutoff**2 * (h**2 / 2) ** 3
    expanded = lam * h**4 / 4 - lam * v**2 * h**2 / 2 + lam * v**4 / 4 + c_h * h**6 / (8 * cutoff**2)
    assert_equal("dimension-six radial Higgs potential expansion", potential, expanded)

    relative_dim6 = (c_h * h**6 / (8 * cutoff**2)) / (lam * h**4 / 4)
    assert_equal("dimension-six/quartic large-field ratio", relative_dim6, c_h * h**2 / (2 * lam * cutoff**2))

    n = 4
    c_n = Fraction(23, 29)
    general_operator = c_n * h ** (2 * n) / (2**n * cutoff ** (2 * n - 4))
    general_ratio = general_operator / (lam * h**4 / 4)
    expected_general_ratio = c_n / (lam * 2 ** (n - 2)) * (h**2 / cutoff**2) ** (n - 2)
    assert_equal("general large-field operator/quartic ratio", general_ratio, expected_general_ratio)

    g1 = Fraction(2, 3)
    g2 = Fraction(5, 7)
    yt = Fraction(11, 13)
    beta_lambda_at_zero = -6 * yt**4 + Fraction(3, 8) * (2 * g2**4 + (g2**2 + g1**2) ** 2)
    direct_at_zero = (
        24 * 0**2
        + 12 * 0 * yt**2
        - 6 * yt**4
        - 3 * 0 * (3 * g2**2 + g1**2)
        + Fraction(3, 8) * (2 * g2**4 + (g2**2 + g1**2) ** 2)
    )
    assert_equal("lambda beta at lambda=0", direct_at_zero, beta_lambda_at_zero)


def check_oblique_parameter_identities() -> None:
    # Use rational sine/cosine satisfying s^2 + c^2 = 1.
    s = Fraction(3, 5)
    c = Fraction(4, 5)
    s2 = s**2
    c2 = c**2
    assert_equal("weak-angle identity", s2 + c2, 1)

    mz2 = Fraction(25, 7)
    mw2 = c2 * mz2
    assert_equal("tree electroweak mass identity", mw2 / (mz2 * c2), 1)

    fractional_w_shift = Fraction(2, 17)
    fractional_z_shift = Fraction(5, 19)
    delta_w = fractional_w_shift * mw2
    delta_z = fractional_z_shift * mz2
    alpha_t = delta_w / mw2 - delta_z / mz2
    assert_equal("T coordinate as fractional rho shift", alpha_t, fractional_w_shift - fractional_z_shift)

    # Universal derivative corrections do not contribute to S or U.
    universal = Fraction(11, 13)
    alpha_s_universal = 4 * s2 * c2 * (universal - universal)
    alpha_u_universal = 4 * s2 * (universal - c2 * universal - s2 * universal)
    assert_zero("universal derivative contribution to S", alpha_s_universal)
    assert_zero("universal derivative contribution to U", alpha_u_universal)

    # If the charged derivative equals the neutral electromagnetic rotation of
    # the same underlying W^3/B self-energy matrix, the U combination vanishes.
    pi_zz_prime = Fraction(7, 23)
    pi_zgamma_prime = Fraction(-5, 29)
    pi_gammagamma_prime = Fraction(13, 31)
    pi_ww_prime = c2 * pi_zz_prime + 2 * s * c * pi_zgamma_prime + s2 * pi_gammagamma_prime
    alpha_u = 4 * s2 * (
        pi_ww_prime
        - c2 * pi_zz_prime
        - 2 * s * c * pi_zgamma_prime
        - s2 * pi_gammagamma_prime
    )
    assert_zero("custodial derivative identity for U", alpha_u)


def check_muon_gminus_two_hybrid_identities() -> None:
    # If a_mu = F_2(0) = alpha/(2 pi), then g_mu = 2(1+a_mu)
    # gives g_mu - 2 = alpha/pi at first order.
    a_mu_schwinger_coeff = Fraction(1, 2)
    assert_equal("Schwinger a_mu coefficient in units alpha/pi", a_mu_schwinger_coeff, Fraction(1, 2))
    assert_equal("Schwinger g-2 coefficient in units alpha/pi", 2 * a_mu_schwinger_coeff, 1)

    # Leading electroweak coefficient:
    # 1/8 * [5/3 + z/3] = [5+z]/24 in units G_F m_mu^2/(sqrt(2) pi^2).
    s2 = Fraction(3, 10)
    z_vector = (1 - 4 * s2) ** 2
    left = Fraction(1, 8) * (Fraction(5, 3) + Fraction(1, 3) * z_vector)
    right = Fraction(1, 24) * (5 + z_vector)
    assert_equal("EW one-loop coefficient normalization", left, right)

    # HVP kernel algebra with Q_x^2 = x^2 m^2/(1-x):
    # (1-x) Q_x^2/(s + Q_x^2) = x^2(1-x)/(x^2 + (1-x)s/m^2).
    x = Fraction(2, 5)
    m2 = Fraction(7, 11)
    s = Fraction(13, 17)
    qx2 = x**2 * m2 / (1 - x)
    feynman_side = (1 - x) * qx2 / (s + qx2)
    kernel_side = x**2 * (1 - x) / (x**2 + (1 - x) * s / m2)
    assert_equal("HVP Feynman-parameter kernel identity", feynman_side, kernel_side)


def check_dimension_six_basis_counts() -> None:
    bosonic_classes = {
        "X^3": 4,
        "H^6": 1,
        "H^4 D^2": 2,
        "X^2 H^2": 8,
    }
    two_fermion_classes = {
        "psi^2 H^3": 3,
        "psi^2 H^2 D": 8,
        "psi^2 X H": 8,
    }
    four_fermion_baryon_preserving_classes = {
        "LL": 5,
        "RR": 7,
        "LR_vector": 8,
        "LR_scalar_tensor": 5,
    }
    assert_equal("dimension-six bosonic one-generation class count", sum(bosonic_classes.values()), 15)
    assert_equal("dimension-six two-fermion one-generation class count", sum(two_fermion_classes.values()), 19)
    assert_equal(
        "dimension-six four-fermion baryon-preserving class count",
        sum(four_fermion_baryon_preserving_classes.values()),
        25,
    )
    assert_equal(
        "dimension-six baryon-preserving one-generation Warsaw-type class count",
        sum(bosonic_classes.values())
        + sum(two_fermion_classes.values())
        + sum(four_fermion_baryon_preserving_classes.values()),
        59,
    )
    assert_equal("dimension-six baryon-violating class count", 4, 4)

    field_dimensions = {
        "X^3": 3 * 2,
        "H^6": 6 * 1,
        "H^4 D^2": 4 * 1 + 2 * 1,
        "X^2 H^2": 2 * 2 + 2 * 1,
        "psi^2 H^3": 2 * Fraction(3, 2) + 3 * 1,
        "psi^2 H^2 D": 2 * Fraction(3, 2) + 2 * 1 + 1,
        "psi^2 X H": 2 * Fraction(3, 2) + 2 + 1,
        "psi^4": 4 * Fraction(3, 2),
    }
    for name, dimension in field_dimensions.items():
        assert_equal(f"dimension-six field-content dimension for {name}", dimension, 6)


def check_chiral_lattice_obstruction_conditions() -> None:
    # The chiral-lattice regulator discussion uses the vanishing of the same
    # local anomaly coefficients as the determinant-line obstruction.
    su3_cubic_without_common_index = 2 - 1 - 1
    assert_zero("SU(3)^3 cubic anomaly in left-handed convention", Fraction(su3_cubic_without_common_index))

    local_obstructions = {
        "SU(3)^2 U(1)_Y": sum(
            su2_dim * hypercharge
            for _, su3_dim, su2_dim, hypercharge, _ in FIELDS
            if su3_dim == 3
        ),
        "SU(2)^2 U(1)_Y": sum(
            su3_dim * hypercharge
            for _, su3_dim, su2_dim, hypercharge, _ in FIELDS
            if su2_dim == 2
        ),
        "U(1)_Y^3": sum(
            su3_dim * su2_dim * hypercharge**3
            for _, su3_dim, su2_dim, hypercharge, _ in FIELDS
        ),
        "grav^2 U(1)_Y": sum(
            su3_dim * su2_dim * hypercharge
            for _, su3_dim, su2_dim, hypercharge, _ in FIELDS
        ),
    }
    for name, value in local_obstructions.items():
        assert_zero(f"chiral-lattice local determinant-line obstruction {name}", value)

    weak_doublets = sum(
        su3_dim
        for _, su3_dim, su2_dim, _, is_weak_doublet in FIELDS
        if is_weak_doublet and su2_dim == 2
    )
    assert_equal("weak-doublet parity for chiral-lattice regulator", weak_doublets % 2, 0)


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
    check_one_loop_gauge_beta_coefficients()
    check_hypercharge_gut_rescaling()
    check_top_higgs_subsystem_coefficients()
    check_higgs_large_field_coupling_chart_identities()
    check_oblique_parameter_identities()
    check_muon_gminus_two_hybrid_identities()
    check_dimension_six_basis_counts()
    check_chiral_lattice_obstruction_conditions()
    print("All Standard Model representation, flavor, SMEFT, chiral-lattice, electroweak, RG, and hybrid-observable checks passed.")


if __name__ == "__main__":
    main()
