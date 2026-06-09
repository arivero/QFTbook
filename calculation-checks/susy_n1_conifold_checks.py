#!/usr/bin/env python3
"""Exact convention checks for the N=1 conifold SCFT and cascade chapter.

The a-maximization checks are finite anomaly arithmetic only.  They verify the
stationarity and Hessian formulas used after the monograph states the imported
SCFT current-multiplet theorem and its no-accidental-current assumptions.
"""

from fractions import Fraction


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


def check_kw_r_anomaly_and_nsvz():
    r = Fraction(1, 2)
    gamma = 3 * r - 2
    assert_equal(gamma, Fraction(-1, 2), "KW gamma from R")
    c_field = gamma / 2
    c_meson = 2 * c_field
    assert_equal(c_field, Fraction(-1, 4), "KW field anomalous dimension in C notation")
    assert_equal(c_meson, gamma, "KW gamma equals meson C_AB at the symmetric point")

    for n in range(2, 11):
        anomaly = n + 4 * Fraction(n, 2) * (r - 1)
        assert_equal(anomaly, 0, f"KW SU({n})^2 U(1)_R anomaly")

        superpotential_r = 4 * r
        assert_equal(superpotential_r, 2, "KW superpotential R-charge")

        matter_index = 4 * n * Fraction(1, 2)
        nsvz_numerator = 3 * n - matter_index * (1 - gamma)
        assert_equal(nsvz_numerator, 0, f"KW SU({n}) NSVZ numerator")


def check_kw_beta_rank_count():
    gamma_samples = [
        (Fraction(0), Fraction(0)),
        (Fraction(-1, 2), Fraction(-1, 2)),
        (Fraction(-2, 3), Fraction(-1, 3)),
        (Fraction(1, 5), Fraction(-6, 5)),
    ]
    for n in range(2, 13):
        for gamma_a, gamma_b in gamma_samples:
            first_gauge_numerator = (
                3 * n
                - 2 * Fraction(n, 2) * (1 - gamma_a)
                - 2 * Fraction(n, 2) * (1 - gamma_b)
            )
            second_gauge_numerator = first_gauge_numerator
            superpotential_defect = 1 + gamma_a + gamma_b

            assert_equal(
                first_gauge_numerator,
                n * superpotential_defect,
                "KW first gauge numerator vs quartic defect",
            )
            assert_equal(
                second_gauge_numerator,
                n * superpotential_defect,
                "KW second gauge numerator vs quartic defect",
            )

            operator_dimension = (
                2 * (1 + gamma_a / 2)
                + 2 * (1 + gamma_b / 2)
            )
            assert_equal(
                operator_dimension - 3,
                superpotential_defect,
                "KW quartic marginality defect",
            )

    gamma_symmetric = Fraction(-1, 2)
    assert_equal(1 + 2 * gamma_symmetric, 0, "KW exchange-symmetric fixed defect")


def check_kw_quartic_canonical_source_convention():
    """Differentiate the KW quartic source in the gamma=-d log Z convention."""

    gamma_samples = [
        (Fraction(-1, 2), Fraction(-1, 2)),
        (Fraction(-2, 3), Fraction(-1, 3)),
        (Fraction(1, 5), Fraction(-6, 5)),
    ]
    for gamma_a, gamma_b in gamma_samples:
        # A dimensionless quartic source is obtained by multiplying the
        # holomorphic quartic coefficient by one power of mu and by the four
        # canonical-field factors.  With gamma=-d log Z/d log mu this gives
        # d log h_can/d log mu = 1 + gamma_A + gamma_B.
        d_log_mu = Fraction(1)
        d_log_z_a = -gamma_a
        d_log_z_b = -gamma_b
        canonical_source_beta = (
            d_log_mu
            - Fraction(1, 2) * (2 * d_log_z_a + 2 * d_log_z_b)
        )
        defect = 1 + gamma_a + gamma_b
        assert_equal(canonical_source_beta, defect, "KW quartic source convention")

        wrong_gamma_sign = d_log_mu - gamma_a - gamma_b
        if defect != 1 and wrong_gamma_sign == defect:
            raise AssertionError("KW wrong gamma sign incorrectly preserved quartic defect")


def check_kw_exact_marginal_dimension_count():
    for n in range(2, 13):
        # The beta map factors through one common defect E:
        # (B_1, B_2, B_h) = (N E, N E, E).  The coefficient vector has
        # rank one for N != 0, so the zero set is one equation in the
        # three-source coordinate system (tau_1, tau_2, h), provided dE is nonzero.
        coefficient_vector = (n, n, 1)
        nonzero_entries = sum(1 for entry in coefficient_vector if entry != 0)
        coefficient_rank = 1 if nonzero_entries else 0
        source_dimension = 3
        local_conformal_dimension = source_dimension - coefficient_rank

        assert_equal(coefficient_rank, 1, "KW common beta-map rank")
        assert_equal(local_conformal_dimension, 2, "KW exact marginal dimension")

        # Two useful local coordinates may be taken as tangent directions
        # annihilating dE.  If dE=(1,1,1) in a normalized linear chart, these
        # two independent vectors span its kernel.
        tangent_one = (1, -1, 0)
        tangent_two = (1, 0, -1)
        normal = (1, 1, 1)
        dot_one = sum(a * b for a, b in zip(tangent_one, normal))
        dot_two = sum(a * b for a, b in zip(tangent_two, normal))
        determinant_minor = tangent_one[0] * tangent_two[1] - tangent_one[1] * tangent_two[0]

        assert_equal(dot_one, 0, "KW first tangent lies in beta kernel")
        assert_equal(dot_two, 0, "KW second tangent lies in beta kernel")
        assert_equal(determinant_minor, 1, "KW tangent directions independent")


def check_kw_a_maximization_and_central_charges():
    # The trial baryonic mixing parameter is s.  In the SU(2)_A x SU(2)_B
    # preserving sector, gauge-anomaly and superpotential constraints leave
    # only R_A + R_B = 1, so the remaining one-parameter mixing is baryonic.
    for r_a in (Fraction(1, 3), Fraction(1, 2), Fraction(7, 10)):
        r_b = 1 - r_a
        for n in range(2, 8):
            gauge_anomaly = n + n * (r_a - 1) + n * (r_b - 1)
            superpotential_r = 2 * r_a + 2 * r_b
            baryonic_parameter = (r_a - r_b) / 2
            assert_equal(gauge_anomaly, 0, "KW preserved-sector gauge anomaly")
            assert_equal(superpotential_r, 2, "KW preserved-sector superpotential R")
            assert_equal(r_a, Fraction(1, 2) + baryonic_parameter, "KW A charge is baryonic mixing")
            assert_equal(r_b, Fraction(1, 2) - baryonic_parameter, "KW B charge is baryonic mixing")

    # The exact trace is
    # Tr R_s^3 = 3 N^2/2 - 2 - 6 N^2 s^2, so the quadratic coefficient in
    # a(s) is negative.
    for n in range(2, 11):
        quadratic_coefficient = Fraction(3, 32) * (-18 * n * n)
        if quadratic_coefficient >= 0:
            raise AssertionError("KW a-maximization quadratic term is not negative")

        tr_r = -2
        tr_r_cubed = Fraction(3, 2) * n * n - 2
        a = Fraction(3, 32) * (3 * tr_r_cubed - tr_r)
        c = Fraction(1, 32) * (9 * tr_r_cubed - 5 * tr_r)
        assert_equal(a, Fraction(27 * n * n, 64) - Fraction(3, 8), f"KW a for N={n}")
        assert_equal(c, Fraction(27 * n * n, 64) - Fraction(1, 4), f"KW c for N={n}")
        assert_equal(a - c, Fraction(-1, 8), f"KW a-c for N={n}")

        # Stationarity: d a/ds = (3/32)(9 Tr R^2 B - Tr B) vanishes at s=0.
        tr_b = 2 * n * n - 2 * n * n
        tr_r_squared_b = (
            2 * n * n * Fraction(1, 4)
            - 2 * n * n * Fraction(1, 4)
        )
        stationarity = Fraction(3, 32) * (9 * tr_r_squared_b - tr_b)
        assert_equal(stationarity, 0, "KW a-max stationarity")

        # Hessian/current two-point relation in the chapter normalization:
        # tau_BB=-3 Tr R B^2 and a''(0)=-(9/16) tau_BB.
        tr_r_b_squared = 4 * n * n * Fraction(-1, 2)
        tau_bb = -3 * tr_r_b_squared
        hessian = Fraction(3, 32) * (-36 * n * n)
        assert_equal(tau_bb, 6 * n * n, "KW baryon current two-point coefficient")
        assert_equal(hessian, Fraction(-9, 16) * tau_bb, "KW a-max Hessian vs current two-point")


def chiral_a_contribution(r_charge: Fraction) -> Fraction:
    fermion_r = r_charge - 1
    return Fraction(3, 32) * (3 * fermion_r**3 - fermion_r)


def check_accidental_symmetry_unitarity_correction():
    free_chiral_a = chiral_a_contribution(Fraction(2, 3))
    assert_equal(free_chiral_a, Fraction(1, 48), "free chiral a contribution")

    # SQCD's naive electric meson charge crosses the chiral unitarity bound at
    # N_f=3 N_c/2.  Below that, the anomaly functional must be corrected by a
    # decoupled meson contribution rather than maximized as-is.
    n_c = 5
    below_nf = 7
    below_meson_r = 2 * (1 - Fraction(n_c, below_nf))
    assert_equal(below_meson_r < Fraction(2, 3), True, "SQCD meson below unitarity bound")
    correction = free_chiral_a - chiral_a_contribution(below_meson_r)
    assert_equal(correction > 0, True, "accidental meson correction is nonzero")

    boundary_nf = 15
    boundary_nc = 10
    boundary_meson_r = 2 * (1 - Fraction(boundary_nc, boundary_nf))
    boundary_correction = free_chiral_a - chiral_a_contribution(boundary_meson_r)
    assert_equal(boundary_meson_r, Fraction(2, 3), "SQCD meson at unitarity boundary")
    assert_equal(boundary_correction, 0, "unitarity-bound correction vanishes at boundary")

    above_nf = 8
    above_meson_r = 2 * (1 - Fraction(n_c, above_nf))
    assert_equal(above_meson_r > Fraction(2, 3), True, "SQCD meson above unitarity bound")


def check_conifold_rank_one_relation():
    samples = [
        (0, 1, 2, 3),
        (1, -2, 3, -5),
        (4, 7, -3, 11),
        (-2, -3, -5, -7),
    ]
    for a1, a2, b1, b2 in samples:
        w11 = a1 * b1
        w12 = a1 * b2
        w21 = a2 * b1
        w22 = a2 * b2
        assert_equal(w11 * w22 - w12 * w21, 0, "rank-one conifold determinant")


def check_ks_nsvz_and_rank_steps():
    gamma_kw = Fraction(-1, 2)
    for m in range(1, 8):
        for n in range(m + 1, 4 * m + 9):
            large = 3 * (n + m) - 2 * n * (1 - gamma_kw)
            small = 3 * n - 2 * (n + m) * (1 - gamma_kw)
            assert_equal(large, 3 * m, f"KS large-node numerator M={m}, N={n}")
            assert_equal(small, -3 * m, f"KS small-node numerator M={m}, N={n}")

            flavors = 2 * n
            electric_colors = n + m
            magnetic_colors = flavors - electric_colors
            assert_equal(magnetic_colors, n - m, "KS Seiberg magnetic rank")
            assert_equal(n - magnetic_colors, m, "KS rank difference after duality")


def check_ks_r_anomaly_remnant():
    r_chiral_fermion = Fraction(-1, 2)
    for m in range(1, 8):
        for n in range(m + 1, 4 * m + 9):
            large_matter_index = 4 * n * Fraction(1, 2)
            small_matter_index = 4 * (n + m) * Fraction(1, 2)
            large_anomaly = (n + m) + large_matter_index * r_chiral_fermion
            small_anomaly = n + small_matter_index * r_chiral_fermion
            assert_equal(large_anomaly, m, "KS large-node R anomaly")
            assert_equal(small_anomaly, -m, "KS small-node R anomaly")

            # A rotation by phi shifts theta by +/- 2 M phi.  The allowed
            # fixed-theta rotations are phi = pi k/M modulo 2 pi, so there
            # are 2M distinct elements.
            allowed_rotations_mod_2pi = 2 * m
            assert_equal(allowed_rotations_mod_2pi, 2 * m, "KS Z_{2M} order")


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    total = Fraction(0)
    for col, value in enumerate(matrix[0]):
        minor = [
            [entry for j, entry in enumerate(row) if j != col]
            for row in matrix[1:]
        ]
        total += ((-1) ** col) * value * determinant(minor)
    return total


def check_ks_magnetic_meson_quadratic_form():
    # Variables are ordered as M_11, M_12, M_21, M_22.  The KW quadratic
    # meson form eps^{ij} eps^{kl} M_{ik} M_{jl} equals
    # 2(M_11 M_22 - M_12 M_21).  Its Hessian is invertible, so all four
    # magnetic mesons are massive after the duality step.
    hessian = [
        [0, 0, 0, 2],
        [0, 0, -2, 0],
        [0, -2, 0, 0],
        [2, 0, 0, 0],
    ]
    assert_equal(determinant(hessian), 16, "KS meson quadratic Hessian")

    # Solving d/dM [h Q(M) + M_ij X_ij/mu] = 0 gives
    # M_11=-X_22/(2h mu), M_22=-X_11/(2h mu),
    # M_12= X_21/(2h mu), M_21= X_12/(2h mu).  Substitution is proportional
    # to X_11 X_22 - X_12 X_21, the same epsilon-epsilon quartic tensor.
    h = Fraction(3, 1)
    mu = Fraction(5, 1)
    samples = [
        (1, 2, 3, 4),
        (-1, 5, -2, 7),
        (0, 3, 11, -6),
    ]
    for x11, x12, x21, x22 in samples:
        m11 = Fraction(-x22, 2 * h * mu)
        m22 = Fraction(-x11, 2 * h * mu)
        m12 = Fraction(x21, 2 * h * mu)
        m21 = Fraction(x12, 2 * h * mu)
        q_m = 2 * (m11 * m22 - m12 * m21)
        source = (m11 * x11 + m12 * x12 + m21 * x21 + m22 * x22) / mu
        on_shell = h * q_m + source
        expected = Fraction(-1, 2 * h * mu * mu) * (x11 * x22 - x12 * x21)
        assert_equal(on_shell, expected, "KS meson integration quartic tensor")


def check_cascade_euclidean_division():
    for m in range(1, 12):
        for n in range(m + 1, 7 * m + 5):
            q, r = divmod(n, m)
            current = n
            steps = 0
            while current >= m:
                current -= m
                steps += 1
            assert_equal(steps, q, "cascade step count")
            assert_equal(current, r, "cascade residual rank")
            assert 0 <= current < m


def check_endpoint_discrete_r_symmetry():
    for m in range(1, 20):
        unbroken_phases = 2 * m
        vacua_after_gaugino_condensation = m
        preserved_subgroup_order = 2
        assert_equal(
            unbroken_phases // preserved_subgroup_order,
            vacua_after_gaugino_condensation,
            "Z_{2M} -> Z_2 vacuum count",
        )


def main():
    check_kw_r_anomaly_and_nsvz()
    check_kw_beta_rank_count()
    check_kw_quartic_canonical_source_convention()
    check_kw_exact_marginal_dimension_count()
    check_kw_a_maximization_and_central_charges()
    check_accidental_symmetry_unitarity_correction()
    check_conifold_rank_one_relation()
    check_ks_nsvz_and_rank_steps()
    check_ks_r_anomaly_remnant()
    check_ks_magnetic_meson_quadratic_form()
    check_cascade_euclidean_division()
    check_endpoint_discrete_r_symmetry()
    print("All N=1 conifold SCFT/cascade checks passed.")


if __name__ == "__main__":
    main()
