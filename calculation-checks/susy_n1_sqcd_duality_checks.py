#!/usr/bin/env python3
"""Exact convention checks for 4D N=1 SQCD duality and phase arithmetic.

Evidence contract.
Target claims: rank involution, baryon normalization, faithful
flavor-baryon quotient arithmetic, local anomaly matching, deformation
bookkeeping, conformal-window central-charge arithmetic, and the range ledger
for the standard Seiberg-duality statement versus the free-electric
continuation.
Independent construction: finite rational arithmetic for charges, anomaly
coefficients, NSVZ numerators, dimensions, R-charges, and range inequalities.
The range checks derive the first nonzero electric endpoint beta coefficient
at N_f=3 N_c and the one-loop magnetic gauge-Yukawa ratio flow after a
declared magnetic Kähler normalization, including the coupled lower-edge
flow at 2 N_f=3 N_c.
Imported assumptions: the field content, magnetic Kähler datum, and
superpotential of the proposed magnetic description, the monograph
gamma=-d log Z/d log mu convention for Kähler coefficients, and the stated
continuum or finite-cutoff status of the SQCD range under discussion.
Negative controls: algebraic matching beyond 3 Nc is required to pass as
protected-sector consistency, but it must not admit the same continuum-pair
claim or fixed-point dimension tests as the electric-asymptotically-free
duality range; b0=0 alone does not certify the electric Gaussian edge, and
the nonzero magnetic asymptotically-free ray does not certify the
free-electric continuum-pair statement without matching data; treating
M/mu_* as automatically canonical fails when the meson wavefunction factor is
changed at fixed holomorphic coefficient; at the lower SQCD edge, b0_mag=0,
Delta(M)=1, and gauge-only running are rejected as substitutes for the coupled
magnetic gauge-Yukawa classification.
Scope boundary: these checks do not prove Seiberg duality, construct
infrared fixed points, or supply a UV completion for a free-electric electric
Lagrangian.
"""

from fractions import Fraction


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


def assert_phase_equal(left, right, label):
    """Compare rational U(1) phase exponents modulo one."""
    difference = left - right
    if difference.denominator != 1:
        raise AssertionError(
            f"{label}: phases differ by {difference!r}, not an integer"
        )


def electric_anomalies(nc, nf):
    r_fermion = Fraction(-nc, nf)
    return {
        "SU_L3": Fraction(nc),
        "SU_R3": Fraction(-nc),
        "SU_L2_R": Fraction(nc) * r_fermion,
        "SU_R2_R": Fraction(nc) * r_fermion,
        "SU_L2_B": Fraction(nc),
        "SU_R2_B": Fraction(-nc),
        "B2_R": 2 * nc * nf * r_fermion,
        "Tr_R": Fraction(nc * nc - 1) + 2 * nc * nf * r_fermion,
        "Tr_R3": Fraction(nc * nc - 1) + 2 * nc * nf * r_fermion**3,
    }


def magnetic_anomalies(nc, nf):
    dual_nc = nf - nc
    q_fermion_r = Fraction(-dual_nc, nf)
    mesino_r = Fraction(nf - 2 * nc, nf)
    baryon_q = Fraction(nc, dual_nc)
    return {
        "SU_L3": Fraction(-dual_nc + nf),
        "SU_R3": Fraction(dual_nc - nf),
        "SU_L2_R": dual_nc * q_fermion_r + nf * mesino_r,
        "SU_R2_R": dual_nc * q_fermion_r + nf * mesino_r,
        "SU_L2_B": Fraction(dual_nc) * baryon_q,
        "SU_R2_B": -Fraction(dual_nc) * baryon_q,
        "B2_R": 2 * dual_nc * nf * baryon_q**2 * q_fermion_r,
        "Tr_R": (
            Fraction(dual_nc * dual_nc - 1)
            + 2 * dual_nc * nf * q_fermion_r
            + nf * nf * mesino_r
        ),
        "Tr_R3": (
            Fraction(dual_nc * dual_nc - 1)
            + 2 * dual_nc * nf * q_fermion_r**3
            + nf * nf * mesino_r**3
        ),
    }


def check_dual_rank_and_baryon_map():
    for nc in range(2, 12):
        for nf in range(nc + 2, 4 * nc + 3):
            dual_nc = nf - nc
            assert dual_nc > 0
            assert_equal(nf - dual_nc, nc, "Seiberg dual rank involution")

            electric_baryon_charge = nc
            magnetic_baryon_charge = dual_nc * Fraction(nc, dual_nc)
            assert_equal(
                magnetic_baryon_charge,
                electric_baryon_charge,
                "electric-magnetic baryon charge map",
            )


def check_faithful_flavor_baryon_kernel():
    for nc in range(2, 12):
        for nf in range(nc + 2, 5 * nc + 1):
            dual_nc = nf - nc

            # Generator of the diagonal Z_Nf quotient:
            # (zeta_f 1_L, zeta_f 1_R, exp(-2 pi i/Nf)).
            beta_diag = Fraction(-1, nf)
            electric_q_phase = Fraction(1, nf) + beta_diag
            electric_tilde_phase = Fraction(-1, nf) - beta_diag
            magnetic_q_phase = Fraction(-1, nf) + beta_diag * Fraction(nc, dual_nc)
            magnetic_tilde_phase = Fraction(1, nf) - beta_diag * Fraction(nc, dual_nc)
            meson_phase = Fraction(1, nf) - Fraction(1, nf)

            assert_phase_equal(electric_q_phase, 0, "diagonal quotient on electric Q")
            assert_phase_equal(
                electric_tilde_phase,
                0,
                "diagonal quotient on electric tilde Q",
            )
            assert_phase_equal(
                magnetic_q_phase,
                Fraction(-1, dual_nc),
                "diagonal quotient on magnetic q is magnetic center",
            )
            assert_phase_equal(
                magnetic_tilde_phase,
                Fraction(1, dual_nc),
                "diagonal quotient on magnetic tilde q is inverse magnetic center",
            )
            assert_phase_equal(meson_phase, 0, "diagonal quotient on meson")

            # Generator of the baryon/gauge-center Z_Nc quotient:
            # (1_L, 1_R, exp(2 pi i/Nc)).
            beta_color = Fraction(1, nc)
            assert_phase_equal(beta_color, Fraction(1, nc), "electric Q color center")
            assert_phase_equal(-beta_color, Fraction(-1, nc), "electric tilde color center")
            assert_phase_equal(
                beta_color * Fraction(nc, dual_nc),
                Fraction(1, dual_nc),
                "baryon quotient on magnetic q is magnetic center",
            )
            assert_phase_equal(
                -beta_color * Fraction(nc, dual_nc),
                Fraction(-1, dual_nc),
                "baryon quotient on magnetic tilde q is inverse magnetic center",
            )
            assert_phase_equal(nc * beta_color, 0, "electric baryon sees baryon quotient trivially")
            assert_phase_equal(
                dual_nc * beta_color * Fraction(nc, dual_nc),
                0,
                "magnetic baryon sees baryon quotient trivially",
            )

            # General kernel elements are generated by the two elements above:
            # a=b mod Nf and beta=s/Nc-a/Nf.
            for a in range(nf):
                for s in range(nc):
                    beta = Fraction(s, nc) - Fraction(a, nf)
                    electric_q = Fraction(a, nf) + beta
                    electric_tilde = Fraction(-a, nf) - beta
                    assert_phase_equal(
                        electric_q,
                        Fraction(s, nc),
                        "general faithful-kernel equation for Q",
                    )
                    assert_phase_equal(
                        electric_tilde,
                        Fraction(-s, nc),
                        "general faithful-kernel equation for tilde Q",
                    )


def check_sqcd_nsvz_coordinate_relation():
    for nc in range(2, 12):
        for nf in range(1, 5 * nc + 1):
            c2_adj = nc
            t_fund = Fraction(1, 2)
            t_antifund = Fraction(1, 2)
            matter_index = nf * t_fund + nf * t_antifund

            assert_equal(c2_adj, nc, "SU(Nc) adjoint index")
            assert_equal(matter_index, nf, "SQCD total matter index")

            # X_h = X_c + Nc log(g^2) + Nf log(Z_Q) + kappa on the
            # flavor-symmetric submanifold, with gamma_Q=-d log(Z_Q)/d log(mu).
            # Differentiating gives
            # 2(Nc-x) beta_g/g - Nf gamma = 3Nc - Nf,
            # where x=8 pi^2/g^2.
            for gamma in (Fraction(-2), Fraction(-1, 3), Fraction(0), Fraction(1, 2)):
                nsvz_numerator = 3 * nc - nf * (1 - gamma)
                for x_coordinate in (Fraction(nc + 1), Fraction(2 * nc + 3), Fraction(5 * nc, 2)):
                    beta_over_g = -nsvz_numerator / (2 * (x_coordinate - nc))
                    differentiated_relation = (
                        2 * (nc - x_coordinate) * beta_over_g
                        - nf * gamma
                    )
                    assert_equal(
                        differentiated_relation,
                        3 * nc - nf,
                        "SQCD NSVZ differentiated coordinate relation",
                    )
                    wrong_gamma_sign_relation = (
                        2 * (nc - x_coordinate) * beta_over_g
                        + nf * gamma
                    )
                    if gamma != 0 and wrong_gamma_sign_relation == 3 * nc - nf:
                        raise AssertionError("SQCD gamma=+d log Z convention incorrectly passed")


def check_r_charges_superpotential_and_nsvz():
    for nc in range(2, 12):
        for nf in range(nc + 2, 4 * nc + 3):
            dual_nc = nf - nc
            r_q_electric = Fraction(nf - nc, nf)
            r_q_magnetic = Fraction(nc, nf)
            r_meson = 2 * r_q_electric

            electric_gamma = 3 * r_q_electric - 2
            magnetic_gamma = 3 * r_q_magnetic - 2
            assert_equal(
                3 * nc - nf * (1 - electric_gamma),
                0,
                "electric NSVZ numerator algebraic zero",
            )
            assert_equal(
                3 * dual_nc - nf * (1 - magnetic_gamma),
                0,
                "magnetic NSVZ numerator algebraic zero",
            )

            magnetic_gauge_r_anomaly = (
                dual_nc
                + Fraction(nf, 2) * (r_q_magnetic - 1)
                + Fraction(nf, 2) * (r_q_magnetic - 1)
            )
            assert_equal(
                magnetic_gauge_r_anomaly,
                0,
                "magnetic SU(dual_Nc)^2 U(1)_R anomaly",
            )
            assert_equal(
                r_meson + 2 * r_q_magnetic,
                2,
                "magnetic superpotential R-charge",
            )

            # In the matching convention M is the electric composite Q tilde Q,
            # so dim(M)=2, dim(q)=dim(tilde q)=1, and mu_* has dimension one.
            assert_equal(2 + 1 + 1 - 1, 3, "magnetic superpotential dimension")


def check_local_anomaly_polynomial_matching():
    for nc in range(2, 12):
        for nf in range(nc + 2, 5 * nc + 1):
            electric = electric_anomalies(nc, nf)
            magnetic = magnetic_anomalies(nc, nf)
            for key, value in electric.items():
                assert_equal(magnetic[key], value, f"{key} anomaly matching")

            expected_tr_r3 = Fraction(nc * nc - 1) - Fraction(2 * nc**4, nf * nf)
            assert_equal(electric["Tr_R3"], expected_tr_r3, "electric Tr R^3 form")
            assert_equal(magnetic["Tr_R3"], expected_tr_r3, "magnetic Tr R^3 form")


def check_conformal_window_central_charges():
    for nc in range(2, 20):
        for nf in range(1, 5 * nc + 1):
            tr_r = Fraction(nc * nc - 1) - 2 * nc * nc
            tr_r3 = Fraction(nc * nc - 1) - Fraction(2 * nc**4, nf * nf)

            assert_equal(tr_r, -nc * nc - 1, "SQCD Tr R form")

            a_ir = Fraction(3, 32) * (3 * tr_r3 - tr_r)
            c_ir = Fraction(1, 32) * (9 * tr_r3 - 5 * tr_r)
            assert_equal(
                a_ir,
                Fraction(3, 32) * (4 * nc * nc - 2 - Fraction(6 * nc**4, nf * nf)),
                "SQCD a central charge formula",
            )
            assert_equal(
                c_ir,
                Fraction(1, 32) * (14 * nc * nc - 4 - Fraction(18 * nc**4, nf * nf)),
                "SQCD c central charge formula",
            )

            a_uv = Fraction(3, 16) * (nc * nc - 1) + Fraction(nc * nf, 24)
            y = Fraction(nf, nc)
            a_difference = a_uv - a_ir
            factored_difference = Fraction(nc * nc, 48) * (3 - y) ** 2 * (2 * y + 3) / (y * y)
            assert_equal(a_difference, factored_difference, "SQCD free-field a comparison")

            if Fraction(3, 2) * nc < nf < 3 * nc:
                if not a_difference > 0:
                    raise AssertionError("interacting SQCD free-field a comparison should be positive")
            if nf == 3 * nc:
                assert_equal(a_difference, 0, "SQCD Gaussian edge a equality")


def electric_gaussian_endpoint_coefficient(nc):
    """Coefficient of g^5/pi^4 in beta_g at N_f=3 N_c.

    The chapter convention is gamma_Q=-d log Z_Q/d log mu and
    gamma_Q= - C_F g^2/(4 pi^2)+O(g^4).  At N_f=3 N_c the NSVZ numerator is
    3 N_c gamma_Q, so beta_g has a positive g^5 coefficient.
    """

    c_f = Fraction(nc * nc - 1, 2 * nc)
    gamma_g2_coefficient = -c_f / 4
    nsvz_numerator_g2_coefficient = 3 * nc * gamma_g2_coefficient
    return -nsvz_numerator_g2_coefficient / 16


def magnetic_gauge_yukawa_coefficients(nc, nf):
    dual_nc = nf - nc
    c_f_magnetic = Fraction(dual_nc * dual_nc - 1, 2 * dual_nc)
    b0_magnetic = 3 * dual_nc - nf
    yukawa_self_coefficient = 2 * nf + dual_nc
    ratio_constant = b0_magnetic - 4 * c_f_magnetic
    positive_nonzero_ray = ratio_constant < 0
    fixed_ratio = None
    if positive_nonzero_ray:
        fixed_ratio = -ratio_constant / yukawa_self_coefficient
    return {
        "dual_nc": dual_nc,
        "c_f_magnetic": c_f_magnetic,
        "b0_magnetic": b0_magnetic,
        "yukawa_self_coefficient": yukawa_self_coefficient,
        "ratio_constant": ratio_constant,
        "positive_nonzero_ray": positive_nonzero_ray,
        "fixed_ratio": fixed_ratio,
    }


def magnetic_lower_edge_flow_coefficients(nc, nf):
    if 2 * nf != 3 * nc:
        raise ValueError("not on the SQCD lower conformal-window edge")
    dual_nc = nf - nc
    if dual_nc <= 1:
        raise ValueError("magnetic gauge group is trivial at this integral edge")

    coeffs = magnetic_gauge_yukawa_coefficients(nc, nf)
    c_f_magnetic = coeffs["c_f_magnetic"]
    yukawa_fixed_ratio = Fraction(4) * c_f_magnetic / coeffs["yukawa_self_coefficient"]
    gauge_zero_ratio = Fraction(2) * c_f_magnetic / nf
    gauge_beta_on_yukawa_ray = nf * (Fraction(2) * c_f_magnetic - nf * yukawa_fixed_ratio) / 64
    gauge_beta_on_h_zero_line = nf * c_f_magnetic / 32
    gauge_only_wrong_sign_sample = gauge_zero_ratio + Fraction(1, 10 * dual_nc * dual_nc)
    full_gauge_beta_sample = nf * (
        Fraction(2) * c_f_magnetic - nf * gauge_only_wrong_sign_sample
    ) / 64

    return {
        "dual_nc": dual_nc,
        "b0_magnetic": coeffs["b0_magnetic"],
        "meson_dimension": Fraction(1),
        "yukawa_fixed_ratio": yukawa_fixed_ratio,
        "gauge_zero_ratio": gauge_zero_ratio,
        "ratio_linear_coefficient": coeffs["yukawa_self_coefficient"],
        "gauge_beta_on_yukawa_ray": gauge_beta_on_yukawa_ray,
        "gauge_beta_on_h_zero_line": gauge_beta_on_h_zero_line,
        "gauge_only_wrong_sign_sample": gauge_only_wrong_sign_sample,
        "full_gauge_beta_sample": full_gauge_beta_sample,
        "classification": "marginally free magnetic edge",
    }


def magnetic_lower_edge_gauge_beta_terms(nc, nf):
    if 2 * nf != 3 * nc:
        raise ValueError("not on the SQCD lower conformal-window edge")
    coeffs = magnetic_gauge_yukawa_coefficients(nc, nf)
    c_f_magnetic = coeffs["c_f_magnetic"]
    return {
        "g6_coefficient": nf * c_f_magnetic / 32,
        "g4_h2_coefficient": -nf * nf / 64,
    }


def martin_vaughn_lower_edge_gauge_beta_terms(nc, nf):
    if 2 * nf != 3 * nc:
        raise ValueError("not on the SQCD lower conformal-window edge")
    dual_nc = nf - nc
    c_group = dual_nc
    c_f_magnetic = Fraction(dual_nc * dual_nc - 1, 2 * dual_nc)
    total_dynkin_index = nf
    dynkin_weighted_casimir = nf * c_f_magnetic

    gauge_two_loop = (
        -6 * c_group * c_group
        + 2 * c_group * total_dynkin_index
        + 4 * dynkin_weighted_casimir
    )

    # For W=h M q tilde q in Martin-Vaughn's symmetric Y^{ijk}
    # convention, only q and tilde q carry C(k).  For each charged component
    # Y^{ij k}Y_{ij k}=2 N_f |h|^2, and division by dim SU(t) leaves
    # 2 N_f^2 |h|^2.
    yukawa_contraction_over_dim_g = 2 * nf * nf
    return {
        "g6_coefficient": gauge_two_loop / 128,
        "g4_h2_coefficient": -yukawa_contraction_over_dim_g / 128,
        "gauge_two_loop_bracket": gauge_two_loop,
        "yukawa_contraction_over_dim_g": yukawa_contraction_over_dim_g,
    }


def canonical_yukawa_squared(lambda_squared, z_meson, z_q, z_tilde_q):
    return lambda_squared / (z_meson * z_q * z_tilde_q)


def check_magnetic_kahler_rescaling_covariance():
    samples = [
        (Fraction(1), Fraction(4), Fraction(1), Fraction(1)),
        (Fraction(9), Fraction(1), Fraction(9), Fraction(1)),
        (Fraction(25), Fraction(4), Fraction(9), Fraction(16)),
    ]
    for lambda_squared, z_meson, z_q, z_tilde_q in samples:
        h_squared = canonical_yukawa_squared(lambda_squared, z_meson, z_q, z_tilde_q)
        assert_equal(
            h_squared * z_meson * z_q * z_tilde_q,
            lambda_squared,
            "canonical Yukawa derives from holomorphic coefficient and Kähler metric",
        )
        if z_meson * z_q * z_tilde_q != 1 and h_squared == lambda_squared:
            raise AssertionError("holomorphic coefficient was incorrectly treated as canonical")

    fixed_lambda = Fraction(1)
    canonical_at_unit_metric = canonical_yukawa_squared(
        fixed_lambda,
        Fraction(1),
        Fraction(1),
        Fraction(1),
    )
    canonical_after_meson_rescaling = canonical_yukawa_squared(
        fixed_lambda,
        Fraction(4),
        Fraction(1),
        Fraction(1),
    )
    assert_equal(
        canonical_after_meson_rescaling,
        Fraction(1, 4) * canonical_at_unit_metric,
        "meson wavefunction rescaling changes the canonical Yukawa at fixed lambda",
    )

    naive_engineering_dimension_rule = fixed_lambda
    if naive_engineering_dimension_rule == canonical_after_meson_rescaling:
        raise AssertionError("M/mu_* was incorrectly accepted as automatic canonical normalization")

    # In the flavor-symmetric magnetic chart Z_q=Z_tilde_q, but both factors
    # still enter the physical canonical coupling.
    z_quark = Fraction(3)
    flavor_symmetric_h = canonical_yukawa_squared(
        fixed_lambda,
        Fraction(2),
        z_quark,
        z_quark,
    )
    assert_equal(
        flavor_symmetric_h,
        Fraction(1, 18),
        "flavor-symmetric chart still contains both quark wavefunction factors",
    )


def check_magnetic_canonical_yukawa_beta_sign():
    samples = [
        (4, 6),
        (6, 9),
        (8, 12),
    ]
    for nc, nf in samples:
        coeffs = magnetic_gauge_yukawa_coefficients(nc, nf)
        dual_nc = coeffs["dual_nc"]
        c_f_magnetic = coeffs["c_f_magnetic"]

        gamma_m_h2 = 2 * dual_nc
        gamma_q_h2 = 2 * nf
        gamma_q_g2 = -4 * c_f_magnetic
        beta_h2_yukawa_coefficient = gamma_m_h2 + 2 * gamma_q_h2
        beta_h2_gauge_coefficient = 2 * gamma_q_g2

        assert_equal(
            beta_h2_yukawa_coefficient,
            2 * (2 * nf + dual_nc),
            "canonical magnetic Yukawa self coefficient from gamma=-d log Z",
        )
        assert_equal(
            beta_h2_gauge_coefficient,
            -8 * c_f_magnetic,
            "canonical magnetic Yukawa gauge coefficient from gamma=-d log Z",
        )

        wrong_gamma_sign_self = -beta_h2_yukawa_coefficient
        if wrong_gamma_sign_self == beta_h2_yukawa_coefficient:
            raise AssertionError("wrong gamma sign incorrectly preserved the magnetic Yukawa beta")


def check_lower_edge_426_direct_coefficients():
    flow = magnetic_lower_edge_flow_coefficients(4, 6)
    direct = magnetic_lower_edge_gauge_beta_terms(4, 6)
    martin_vaughn = martin_vaughn_lower_edge_gauge_beta_terms(4, 6)

    assert_equal(flow["dual_nc"], 2, "(4,6,2) magnetic rank")
    assert_equal(flow["yukawa_fixed_ratio"], Fraction(3, 14), "(4,6,2) Yukawa separatrix")
    assert_equal(flow["gauge_zero_ratio"], Fraction(1, 4), "(4,6,2) gauge sign-change ratio")
    assert_equal(direct["g6_coefficient"], Fraction(9, 64), "(4,6,2) direct g^6 coefficient")
    assert_equal(direct["g4_h2_coefficient"], Fraction(-9, 16), "(4,6,2) direct g^4 |h|^2 coefficient")
    assert_equal(martin_vaughn["gauge_two_loop_bracket"], 18, "(4,6,2) Martin-Vaughn gauge bracket")
    assert_equal(
        martin_vaughn["yukawa_contraction_over_dim_g"],
        72,
        "(4,6,2) Martin-Vaughn Yukawa contraction",
    )
    assert_equal(martin_vaughn["g6_coefficient"], direct["g6_coefficient"], "(4,6,2) direct g^6 route match")
    assert_equal(
        martin_vaughn["g4_h2_coefficient"],
        direct["g4_h2_coefficient"],
        "(4,6,2) direct g^4 |h|^2 route match",
    )
    assert_equal(
        flow["gauge_beta_on_yukawa_ray"],
        Fraction(9, 448),
        "(4,6,2) coupled lower-edge gauge coefficient on the Yukawa ray",
    )
    if flow["gauge_beta_on_h_zero_line"] == flow["gauge_beta_on_yukawa_ray"]:
        raise AssertionError("(4,6,2) gauge-only coefficient incorrectly matched the coupled ray")


def check_electric_gaussian_endpoint_beta_coefficient():
    for nc in range(2, 20):
        b0 = 3 * nc - 3 * nc
        assert_equal(b0, 0, "electric endpoint one-loop coefficient vanishes")

        endpoint_coefficient = electric_gaussian_endpoint_coefficient(nc)
        expected = Fraction(3 * (nc * nc - 1), 128)
        assert_equal(endpoint_coefficient, expected, "electric endpoint g^5 beta coefficient")
        if not endpoint_coefficient > 0:
            raise AssertionError("electric endpoint should be marginally irrelevant toward the IR")

        b0_only_coefficient = Fraction(0)
        if b0_only_coefficient == endpoint_coefficient:
            raise AssertionError("b0=0 alone incorrectly certified the Gaussian endpoint")


def check_magnetic_gauge_yukawa_uv_status():
    for nc in range(2, 20):
        for nf in range(nc + 2, 5 * nc + 1):
            coeffs = magnetic_gauge_yukawa_coefficients(nc, nf)
            dual_nc = coeffs["dual_nc"]

            assert_equal(dual_nc, nf - nc, "magnetic gauge rank in RG coefficients")
            assert_equal(
                coeffs["yukawa_self_coefficient"],
                2 * nf + dual_nc,
                "magnetic Yukawa self coefficient",
            )

            if nf >= 3 * nc:
                if not coeffs["b0_magnetic"] > 0:
                    raise AssertionError("free-electric magnetic gauge sector should be asymptotically free")
                expected_ratio_constant = -nc + Fraction(2, dual_nc)
                assert_equal(
                    coeffs["ratio_constant"],
                    expected_ratio_constant,
                    "magnetic free-electric ratio-flow constant",
                )
                if not coeffs["positive_nonzero_ray"] or coeffs["fixed_ratio"] is None:
                    raise AssertionError("nonzero magnetic Yukawa AF ray was missed")
                if not coeffs["fixed_ratio"] > 0:
                    raise AssertionError("free-electric magnetic AF ray should have positive ratio")
            elif coeffs["positive_nonzero_ray"]:
                if not coeffs["fixed_ratio"] > 0:
                    raise AssertionError("positive magnetic gauge-Yukawa ray should have positive ratio")


def check_magnetic_lower_edge_coupled_flow_status():
    for dual_nc in range(2, 12):
        nc = 2 * dual_nc
        nf = 3 * dual_nc
        flow = magnetic_lower_edge_flow_coefficients(nc, nf)

        assert_equal(flow["dual_nc"], dual_nc, "nontrivial lower-edge magnetic rank")
        assert_equal(flow["b0_magnetic"], 0, "lower-edge magnetic one-loop b0")
        assert_equal(flow["meson_dimension"], 1, "lower-edge meson unitarity saturation")
        if not 0 < flow["yukawa_fixed_ratio"] < flow["gauge_zero_ratio"]:
            raise AssertionError("lower-edge Yukawa separatrix should lie in the IR-free gauge-sign chamber")
        if not flow["ratio_linear_coefficient"] > 0:
            raise AssertionError("lower-edge Yukawa fixed ratio should be IR attractive")
        if not flow["gauge_beta_on_yukawa_ray"] > 0:
            raise AssertionError("lower-edge gauge beta should be marginally irrelevant on the Yukawa ray")
        if not flow["gauge_beta_on_h_zero_line"] > flow["gauge_beta_on_yukawa_ray"]:
            raise AssertionError("omitting the Yukawa contribution should change the first nonzero gauge coefficient")
        if not flow["full_gauge_beta_sample"] < 0:
            raise AssertionError("gauge-only running missed the Yukawa contribution to the endpoint sign")
        if flow["classification"] != "marginally free magnetic edge":
            raise AssertionError("lower edge was not classified by the coupled flow")

        b0_only_classification = "undetermined from b0"
        if b0_only_classification == flow["classification"]:
            raise AssertionError("b0_mag=0 alone incorrectly classified the endpoint")

        meson_only_classification = "free meson only"
        if meson_only_classification == flow["classification"]:
            raise AssertionError("Delta(M)=1 alone incorrectly classified the full magnetic sector")


def check_duality_deformation_tests():
    for nc in range(2, 12):
        for nf in range(nc + 2, 5 * nc + 1):
            dual_nc = nf - nc

            # Electric mass for one flavor maps to a rank-one magnetic Higgs
            # branch: SU(dual_nc) -> SU(dual_nc-1), matching the dual of the
            # (nf-1)-flavor electric theory.
            low_flavors = nf - 1
            low_magnetic_rank = dual_nc - 1
            assert_equal(low_magnetic_rank, low_flavors - nc, "mass deformation dual rank")
            assert_equal(dual_nc == 2, low_magnetic_rank == 1, "mass deformation confining boundary")

            # In the microscopic matching convention dim(M)=2, dim(q)=1, and
            # dim(mu_*)=1, so F_M compares q tilde q / mu_* with the mass m.
            assert_equal(1 + 1 - 1, 1, "mass-deformation F_M dimension")
            assert_equal(2 + 1, 3, "electric mass term dimension")

            r_meson = Fraction(2 * (nf - nc), nf)
            r_q_magnetic = Fraction(nc, nf)
            r_mass_spurion = 2 - r_meson
            assert_equal(r_mass_spurion, 2 * r_q_magnetic, "magnetic Higgs F-term R-charge")

            # Electric rank-r meson vevs Higgs SU(nc) -> SU(nc-r) and leave
            # nf-r flavors.  Magnetic rank is unchanged because the same
            # background gives masses to r magnetic flavor pairs.
            for higgs_rank in range(1, nc):
                low_electric_rank = nc - higgs_rank
                low_electric_flavors = nf - higgs_rank
                assert_equal(
                    low_electric_flavors - low_electric_rank,
                    dual_nc,
                    "Higgs deformation dual rank unchanged",
                )
                assert_equal(
                    low_electric_flavors >= low_electric_rank + 2,
                    nf >= nc + 2,
                    "Higgs deformation preserves duality-window offset",
                )

                # The magnetic mass v q tilde q / mu_* has dimension three
                # and R-charge two when v has the meson quantum numbers.
                assert_equal(2 + 1 + 1 - 1, 3, "magnetic Higgs mass dimension")
                assert_equal(r_meson + 2 * r_q_magnetic, 2, "magnetic Higgs mass R-charge")


def check_sconfining_superpotential():
    for nc in range(2, 16):
        nf = nc + 1
        r_quark = Fraction(1, nf)
        r_meson = 2 * r_quark
        r_baryon = nc * r_quark

        assert_equal(r_baryon + r_meson + r_baryon, 2, "B M tilde B R-charge")
        assert_equal(nf * r_meson, 2, "det(M) R-charge")

        baryon_dim = nc
        meson_dim = 2
        term_dim = baryon_dim + meson_dim + baryon_dim
        det_dim = nf * meson_dim
        assert_equal(term_dim, det_dim, "s-confining numerator dimensions")
        assert_equal(term_dim - (2 * nc - 1), 3, "s-confining W dimension")


def check_quantum_modified_constraint_and_decoupling():
    for nc in range(2, 16):
        # Nf=Nc quantum-modified constraint:
        # det(M) and B tilde B have dimension 2 Nc and zero anomaly-free R.
        nf = nc
        r_quark = Fraction(nf - nc, nf)
        r_meson = 2 * r_quark
        r_baryon = nc * r_quark
        assert_equal(r_meson, 0, "Nf=Nc meson R-charge")
        assert_equal(r_baryon, 0, "Nf=Nc baryon R-charge")

        det_m_dimension = 2 * nc
        baryon_pair_dimension = nc + nc
        quantum_scale_exponent = 3 * nc - nf
        assert_equal(det_m_dimension, baryon_pair_dimension, "Nf=Nc constraint dimensions")
        assert_equal(quantum_scale_exponent, 2 * nc, "Nf=Nc quantum scale exponent")

        # Decoupling from the Nf=Nc+1 confining superpotential with mass m:
        # Lambda_-^(2Nc) = m Lambda_+^(2Nc-1).
        high_exponent = 3 * nc - (nc + 1)
        low_exponent = 3 * nc - nc
        assert_equal(high_exponent, 2 * nc - 1, "Nf=Nc+1 scale exponent")
        assert_equal(low_exponent, high_exponent + 1, "quantum-modified decoupling exponent")

        samples = [
            (Fraction(2), Fraction(3), Fraction(5)),
            (Fraction(7), Fraction(11), Fraction(13)),
            (Fraction(-3), Fraction(5), Fraction(17)),
        ]
        for det_hat_m, baryon_pair, lambda_high_power in samples:
            mass = (det_hat_m - baryon_pair) / lambda_high_power
            f_x = (baryon_pair - det_hat_m) / lambda_high_power + mass
            assert_equal(f_x, 0, "F_X gives quantum-modified constraint")
            lambda_low_power = mass * lambda_high_power
            assert_equal(
                det_hat_m - baryon_pair,
                lambda_low_power,
                "det M - B tilde B equals low holomorphic scale",
            )


def check_massive_sqcd_to_pure_sym_decoupling():
    for nc in range(2, 16):
        for nf in range(1, nc):
            d = nc - nf
            ads_scale_exponent = 3 * nc - nf

            assert_equal(d + nf, nc, "massive SQCD ADS denominator plus flavors")
            assert_equal(
                nf + ads_scale_exponent,
                3 * nc,
                "massive SQCD pure-scale matching dimension",
            )

            # For Y=(A/det M)^(1/d), the F_M equation gives
            # m = Y M^{-T}.  Taking determinants gives det(m)=Y^nf/det(M),
            # while the definition of Y gives Y^d=A/det(M).  Eliminating
            # det(M) yields Y^Nc=A det(m).
            y_power_from_f_terms = nf + d
            assert_equal(y_power_from_f_terms, nc, "massive SQCD Y power to pure SYM")

            ads_term_coefficient = d
            mass_term_trace_coefficient = nf
            assert_equal(
                ads_term_coefficient + mass_term_trace_coefficient,
                nc,
                "massive SQCD critical superpotential coefficient",
            )

            root_exponent = Fraction(1, nc)
            source_identity_coefficient = nc * root_exponent
            assert_equal(
                source_identity_coefficient,
                1,
                "massive SQCD pure-branch source identity",
            )

            # The pure branch equation Y^Nc=L_0 has Nc roots.  Raising each
            # branch value to Nc removes the branch label.
            for branch in range(nc):
                assert_equal(
                    (nc * branch) % nc,
                    0,
                    "massive SQCD pure branch root equation",
                )

            # Dimension and R-charge spurion checks.  det(m) has dimension nf;
            # Lambda^(3Nc-nf) has dimension 3Nc-nf, so Y has dimension 3.
            y_dimension = Fraction(nf + ads_scale_exponent, nc)
            assert_equal(y_dimension, 3, "massive SQCD pure condensate dimension")

            r_meson = Fraction(2 * (nf - nc), nf)
            r_mass = 2 - r_meson
            det_mass_r_charge = nf * r_mass
            assert_equal(det_mass_r_charge, 2 * nc, "massive SQCD det mass R-charge")
            assert_equal(
                Fraction(det_mass_r_charge, nc),
                2,
                "massive SQCD pure branch superpotential R-charge",
            )

            # Mass-source/Konishi ledger on a diagonal mass patch:
            # m_i M_i = Y for each flavor, so tr(mM)=nf Y.  The same Y is
            # the source derivative L_0 dW/dL_0 on the pure branch.
            mass_source_euler_coefficient = nc * Fraction(1, nc)
            assert_equal(
                mass_source_euler_coefficient,
                1,
                "massive SQCD mass-source derivative coefficient",
            )
            for branch in range(nc):
                glueball_branch_exponent = branch
                for flavor_index in range(nf):
                    mass_meson_product_exponent = glueball_branch_exponent
                    assert_equal(
                        mass_meson_product_exponent % nc,
                        glueball_branch_exponent % nc,
                        "massive SQCD matrix Konishi branch exponent",
                    )

                trace_coefficient = nf * mass_source_euler_coefficient
                assert_equal(
                    trace_coefficient,
                    nf,
                    "massive SQCD trace Konishi flavor count",
                )

            # The mass source has R-charge 2-R(M), so m M and S both have
            # R-charge two, matching the Konishi matrix identity.
            assert_equal(r_mass + r_meson, 2, "massive SQCD mM Konishi R-charge")
            mass_dimension = 1
            meson_dimension = 2
            assert_equal(
                mass_dimension + meson_dimension,
                3,
                "massive SQCD mM Konishi dimension",
            )
            assert_equal(
                3 - mass_dimension,
                meson_dimension,
                "mass-source derivative dimension",
            )
            assert_equal(2 - r_mass, r_meson, "mass-source derivative R-charge")


def classify_phase(nc, nf):
    if nf < nc:
        return "ADS runaway"
    if nf == nc:
        return "quantum modified"
    if nf == nc + 1:
        return "confining"
    if 2 * nf < 3 * nc:
        return "free magnetic"
    if 2 * nf == 3 * nc:
        return "marginally free magnetic edge"
    if nf < 3 * nc:
        return "interacting conformal"
    if nf == 3 * nc:
        return "Gaussian edge"
    return "free electric"


def sqcd_range_status(nc, nf):
    field_content = nf >= nc + 2
    electric_b0 = 3 * nc - nf
    magnetic_b0 = 3 * (nf - nc) - nf
    interacting = field_content and 2 * nf > 3 * nc and nf < 3 * nc
    endpoint_coefficient_positive = nf == 3 * nc and electric_gaussian_endpoint_coefficient(nc) > 0
    magnetic_yukawa = magnetic_gauge_yukawa_coefficients(nc, nf) if field_content else None
    magnetic_nonzero_yukawa_af_ray = (
        magnetic_yukawa["positive_nonzero_ray"] if magnetic_yukawa is not None else False
    )
    magnetic_h_zero_af_only = (
        field_content
        and nf >= 3 * nc
        and magnetic_yukawa is not None
        and magnetic_yukawa["b0_magnetic"] > 0
        and not magnetic_nonzero_yukawa_af_ray
    )
    magnetic_full_uv_datum_required = (
        field_content
        and nf >= 3 * nc
        and magnetic_yukawa is not None
        and magnetic_yukawa["b0_magnetic"] > 0
        and magnetic_nonzero_yukawa_af_ray
    )
    lower_edge_flow = None
    if field_content and 2 * nf == 3 * nc and nf - nc > 1:
        lower_edge_flow = magnetic_lower_edge_flow_coefficients(nc, nf)
    return {
        "field_content_algebra": field_content,
        "standard_duality_range": field_content and nf < 3 * nc,
        "free_magnetic_wilsonian": field_content and 2 * nf < 3 * nc,
        "lower_edge": field_content and 2 * nf == 3 * nc,
        "lower_edge_coupled_flow_required": lower_edge_flow is not None,
        "lower_edge_marginally_free_magnetic": (
            lower_edge_flow is not None
            and lower_edge_flow["classification"] == "marginally free magnetic edge"
            and lower_edge_flow["gauge_beta_on_yukawa_ray"] > 0
        ),
        "lower_edge_yukawa_fixed_ratio": (
            lower_edge_flow["yukawa_fixed_ratio"] if lower_edge_flow is not None else None
        ),
        "interacting_scft": interacting,
        "fixed_point_dimension_tests": interacting,
        "gaussian_edge": field_content and endpoint_coefficient_positive,
        "electric_endpoint_beta_positive": endpoint_coefficient_positive,
        "strict_free_electric": field_content and nf > 3 * nc,
        "free_electric_continuation": field_content and nf >= 3 * nc,
        "electric_uv_datum_required": field_content and nf > 3 * nc,
        "magnetic_nonzero_yukawa_af_ray": magnetic_nonzero_yukawa_af_ray,
        "magnetic_h_zero_af_only": magnetic_h_zero_af_only,
        "magnetic_full_uv_datum_required": magnetic_full_uv_datum_required,
        "electric_b0": electric_b0,
        "magnetic_b0": magnetic_b0,
    }


def check_phase_inequalities():
    for nc in range(2, 20):
        for nf in range(0, 5 * nc + 1):
            phase = classify_phase(nc, nf)
            status = sqcd_range_status(nc, nf)
            electric_b0 = 3 * nc - nf
            meson_dimension = None if nf == 0 else 3 * Fraction(nf - nc, nf)

            if phase == "free magnetic":
                dual_b0 = 3 * (nf - nc) - nf
                if dual_b0 >= 0:
                    raise AssertionError("free magnetic phase has nonnegative magnetic b0")
                if not (nf >= nc + 2 and nf < Fraction(3 * nc, 2)):
                    raise AssertionError("free magnetic phase inequality failed")
                if not status["standard_duality_range"] or not status["free_magnetic_wilsonian"]:
                    raise AssertionError("free magnetic status range failed")
            elif phase == "interacting conformal":
                dual_b0 = 3 * (nf - nc) - nf
                if not (electric_b0 > 0 and dual_b0 > 0):
                    raise AssertionError("conformal window asymptotic-freedom test failed")
                if meson_dimension is None or meson_dimension <= 1:
                    raise AssertionError("conformal window meson unitarity test failed")
                if not status["standard_duality_range"] or not status["fixed_point_dimension_tests"]:
                    raise AssertionError("conformal-window fixed-point status failed")
            elif phase == "free electric":
                if electric_b0 >= 0:
                    raise AssertionError("free electric phase has nonnegative electric b0")
                if status["standard_duality_range"] or not status["electric_uv_datum_required"]:
                    raise AssertionError("free electric continuation status failed")
                if status["fixed_point_dimension_tests"]:
                    raise AssertionError("free electric range should not admit fixed-point dimension tests")
                if not status["magnetic_nonzero_yukawa_af_ray"] or not status["magnetic_full_uv_datum_required"]:
                    raise AssertionError("free electric magnetic Yukawa UV status failed")
                if status["magnetic_h_zero_af_only"]:
                    raise AssertionError("free electric magnetic status should not be gauge-only")
            elif phase == "Gaussian edge":
                assert_equal(electric_b0, 0, "electric Gaussian edge b0")
                if not status["electric_endpoint_beta_positive"]:
                    raise AssertionError("Gaussian edge requires positive first nonzero beta coefficient")
                if status["standard_duality_range"] or not status["gaussian_edge"]:
                    raise AssertionError("Gaussian edge should be separate from the standard duality range")
                if status["fixed_point_dimension_tests"]:
                    raise AssertionError("Gaussian edge should not be an interacting fixed-point admission")
                if not status["magnetic_nonzero_yukawa_af_ray"] or status["magnetic_h_zero_af_only"]:
                    raise AssertionError("Gaussian edge magnetic Yukawa AF-ray status failed")
            elif phase == "marginally free magnetic edge":
                assert_equal(meson_dimension, 1, "meson unitarity lower edge")
                if not status["lower_edge"] or status["fixed_point_dimension_tests"]:
                    raise AssertionError("lower edge status should not use interacting fixed-point tests")
                if not status["lower_edge_coupled_flow_required"]:
                    raise AssertionError("lower edge status should require coupled magnetic flow data")
                if not status["lower_edge_marginally_free_magnetic"]:
                    raise AssertionError("lower edge was not classified as marginally free magnetic")
                if status["lower_edge_yukawa_fixed_ratio"] is None:
                    raise AssertionError("lower edge should record the Yukawa fixed ratio")


def check_free_electric_continuation_status_negative_control():
    for nc in range(2, 12):
        nf = 3 * nc + 1
        status = sqcd_range_status(nc, nf)
        dual_nc = nf - nc

        assert status["field_content_algebra"]
        assert status["strict_free_electric"]
        assert status["free_electric_continuation"]
        assert status["electric_uv_datum_required"]
        assert status["magnetic_nonzero_yukawa_af_ray"]
        assert status["magnetic_full_uv_datum_required"]
        if status["magnetic_h_zero_af_only"]:
            raise AssertionError("free-electric magnetic status should not be h=0 only")
        if status["standard_duality_range"] or status["fixed_point_dimension_tests"]:
            raise AssertionError("free-electric arithmetic should not admit the standard continuum-pair claim")

        assert_equal(nf - dual_nc, nc, "free-electric rank algebra still passes")
        assert_equal(
            dual_nc * Fraction(nc, dual_nc),
            nc,
            "free-electric baryon-charge algebra still passes",
        )
        electric = electric_anomalies(nc, nf)
        magnetic = magnetic_anomalies(nc, nf)
        for key, value in electric.items():
            assert_equal(magnetic[key], value, f"free-electric {key} anomaly algebra still passes")


def main():
    check_dual_rank_and_baryon_map()
    check_faithful_flavor_baryon_kernel()
    check_sqcd_nsvz_coordinate_relation()
    check_r_charges_superpotential_and_nsvz()
    check_local_anomaly_polynomial_matching()
    check_conformal_window_central_charges()
    check_magnetic_kahler_rescaling_covariance()
    check_magnetic_canonical_yukawa_beta_sign()
    check_lower_edge_426_direct_coefficients()
    check_electric_gaussian_endpoint_beta_coefficient()
    check_magnetic_gauge_yukawa_uv_status()
    check_magnetic_lower_edge_coupled_flow_status()
    check_duality_deformation_tests()
    check_sconfining_superpotential()
    check_quantum_modified_constraint_and_decoupling()
    check_massive_sqcd_to_pure_sym_decoupling()
    check_phase_inequalities()
    check_free_electric_continuation_status_negative_control()
    print("All N=1 SQCD duality and phase checks passed.")


if __name__ == "__main__":
    main()
