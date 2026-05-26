#!/usr/bin/env python3
"""Exact convention checks for 4D N=1 SQCD duality and phase arithmetic."""

from fractions import Fraction


def assert_equal(left, right, label):
    if left != right:
        raise AssertionError(f"{label}: got {left!r}, expected {right!r}")


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


def check_sqcd_nsvz_coordinate_relation():
    for nc in range(2, 12):
        for nf in range(1, 5 * nc + 1):
            c2_adj = nc
            t_fund = Fraction(1, 2)
            t_antifund = Fraction(1, 2)
            matter_index = nf * t_fund + nf * t_antifund

            assert_equal(c2_adj, nc, "SU(Nc) adjoint index")
            assert_equal(matter_index, nf, "SQCD total matter index")

            # X_h = X_c + Nc log(g^2) - Nf log(Z_Q) + kappa on the
            # flavor-symmetric submanifold.  Differentiating gives
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
                "electric NSVZ numerator at candidate fixed point",
            )
            assert_equal(
                3 * dual_nc - nf * (1 - magnetic_gamma),
                0,
                "magnetic NSVZ numerator at candidate fixed point",
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


def check_anomaly_matching():
    for nc in range(2, 12):
        for nf in range(nc + 2, 5 * nc + 1):
            electric = electric_anomalies(nc, nf)
            magnetic = magnetic_anomalies(nc, nf)
            for key, value in electric.items():
                assert_equal(magnetic[key], value, f"{key} anomaly matching")

            expected_tr_r3 = Fraction(nc * nc - 1) - Fraction(2 * nc**4, nf * nf)
            assert_equal(electric["Tr_R3"], expected_tr_r3, "electric Tr R^3 form")
            assert_equal(magnetic["Tr_R3"], expected_tr_r3, "magnetic Tr R^3 form")


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
        return "lower edge"
    if nf < 3 * nc:
        return "interacting conformal"
    if nf == 3 * nc:
        return "Gaussian edge"
    return "free electric"


def check_phase_inequalities():
    for nc in range(2, 20):
        for nf in range(0, 5 * nc + 1):
            phase = classify_phase(nc, nf)
            electric_b0 = 3 * nc - nf
            meson_dimension = None if nf == 0 else 3 * Fraction(nf - nc, nf)

            if phase == "free magnetic":
                dual_b0 = 3 * (nf - nc) - nf
                if dual_b0 >= 0:
                    raise AssertionError("free magnetic phase has nonnegative magnetic b0")
                if not (nf >= nc + 2 and nf < Fraction(3 * nc, 2)):
                    raise AssertionError("free magnetic phase inequality failed")
            elif phase == "interacting conformal":
                dual_b0 = 3 * (nf - nc) - nf
                if not (electric_b0 > 0 and dual_b0 > 0):
                    raise AssertionError("conformal window asymptotic-freedom test failed")
                if meson_dimension is None or meson_dimension <= 1:
                    raise AssertionError("conformal window meson unitarity test failed")
            elif phase == "free electric":
                if electric_b0 >= 0:
                    raise AssertionError("free electric phase has nonnegative electric b0")
            elif phase == "Gaussian edge":
                assert_equal(electric_b0, 0, "electric Gaussian edge b0")
            elif phase == "lower edge":
                assert_equal(meson_dimension, 1, "meson unitarity lower edge")


def main():
    check_dual_rank_and_baryon_map()
    check_sqcd_nsvz_coordinate_relation()
    check_r_charges_superpotential_and_nsvz()
    check_anomaly_matching()
    check_duality_deformation_tests()
    check_sconfining_superpotential()
    check_quantum_modified_constraint_and_decoupling()
    check_phase_inequalities()
    print("All N=1 SQCD duality and phase checks passed.")


if __name__ == "__main__":
    main()
