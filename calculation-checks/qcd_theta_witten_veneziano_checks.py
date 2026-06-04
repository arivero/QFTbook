#!/usr/bin/env python3
"""Exact checks for theta, susceptibility, and Witten-Veneziano normalizations.

The finite theta-data checks distinguish exact finite-volume cumulant
identities from the continuum and branch-selection assumptions needed for QCD
theta physics.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{name}: got {simplified!r}, expected 0")


def check_finite_volume_cumulant_identity() -> None:
    theta = sp.symbols("theta")
    charges = [-2, -1, 0, 1, 3]
    weights = [
        sp.Rational(2, 7),
        sp.Rational(3, 5),
        sp.Rational(11, 13),
        sp.Rational(5, 17),
        sp.Rational(7, 19),
    ]
    volume = sp.Rational(23, 3)

    partition = sum(
        weight * sp.exp(sp.I * theta * charge)
        for charge, weight in zip(charges, weights)
    )
    energy = -sp.log(partition) / volume
    susceptibility_from_derivatives = sp.diff(energy, theta, 2).subs(theta, 0)

    normalization = sum(weights)
    mean = sum(weight * charge for charge, weight in zip(charges, weights)) / normalization
    second = sum(weight * charge * charge for charge, weight in zip(charges, weights)) / normalization
    susceptibility_from_cumulant = (second - mean * mean) / volume

    assert_zero(
        "finite-volume susceptibility cumulant",
        susceptibility_from_derivatives - susceptibility_from_cumulant,
    )


def check_finite_volume_theta_cumulant_hierarchy() -> None:
    theta, t = sp.symbols("theta t")
    charges = [-3, -2, -1, 0, 1, 2, 3]
    weights = [
        sp.Rational(2, 7),
        sp.Rational(3, 11),
        sp.Rational(5, 13),
        sp.Rational(17, 19),
        sp.Rational(5, 13),
        sp.Rational(3, 11),
        sp.Rational(2, 7),
    ]
    volume = sp.Rational(31, 5)
    normalization = sum(weights)

    partition = sum(
        weight * sp.exp(sp.I * theta * charge)
        for charge, weight in zip(charges, weights)
    )
    energy = -sp.log(partition) / volume
    cumulant_generator = sp.log(
        sum(
            weight * sp.exp(t * charge)
            for charge, weight in zip(charges, weights)
        )
        / normalization
    )
    cumulants = {
        order: sp.diff(cumulant_generator, t, order).subs(t, 0)
        for order in range(1, 7)
    }

    for order in range(1, 7):
        energy_derivative = sp.diff(energy, theta, order).subs(theta, 0)
        expected = -(sp.I ** order) * cumulants[order] / volume
        assert_zero(
            f"finite theta cumulant derivative order {order}",
            energy_derivative - expected,
        )

    assert_zero("CP-symmetric third charge cumulant", cumulants[3])
    assert_zero("CP-symmetric fifth charge cumulant", cumulants[5])

    chi = cumulants[2] / volume
    b2_from_derivatives = sp.diff(energy, theta, 4).subs(theta, 0) / (12 * chi)
    b4_from_derivatives = sp.diff(energy, theta, 6).subs(theta, 0) / (360 * chi)
    assert_zero(
        "finite theta b2 cumulant sign",
        b2_from_derivatives + cumulants[4] / (12 * cumulants[2]),
    )
    assert_zero(
        "finite theta b4 cumulant sign",
        b4_from_derivatives - cumulants[6] / (360 * cumulants[2]),
    )

    counterterm = (
        sp.Rational(7, 23) * theta**2 / 2
        + sp.Rational(11, 29) * theta**4 / 24
        + sp.Rational(13, 31) * theta**6 / 720
    )
    shifted_energy = energy + counterterm
    for order, shift in {
        2: sp.Rational(7, 23),
        4: sp.Rational(11, 29),
        6: sp.Rational(13, 31),
    }.items():
        assert_zero(
            f"theta local counterterm shifts derivative order {order}",
            sp.diff(shifted_energy, theta, order).subs(theta, 0)
            - sp.diff(energy, theta, order).subs(theta, 0)
            - shift,
        )


def check_local_density_susceptibility_cumulant() -> None:
    density_samples = [
        (Fraction(1), Fraction(0), Fraction(-1), Fraction(2)),
        (Fraction(0), Fraction(1), Fraction(1), Fraction(-1)),
        (Fraction(-2), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(-1), Fraction(2), Fraction(0)),
    ]
    weights = [
        Fraction(2, 7),
        Fraction(3, 5),
        Fraction(5, 11),
        Fraction(7, 13),
    ]
    total_weight = sum(weights, Fraction(0))
    site_count = len(density_samples[0])
    volume = Fraction(site_count)

    def average(values: list[Fraction]) -> Fraction:
        return sum(weight * value for weight, value in zip(weights, values)) / total_weight

    charges = [sum(sample, Fraction(0)) for sample in density_samples]
    charge_mean = average(charges)
    charge_variance = average([charge * charge for charge in charges]) - charge_mean * charge_mean

    site_means = [
        average([sample[site] for sample in density_samples])
        for site in range(site_count)
    ]
    density_double_cumulant = sum(
        average([sample[left] * sample[right] for sample in density_samples])
        - site_means[left] * site_means[right]
        for left in range(site_count)
        for right in range(site_count)
    )
    assert_equal(
        "density double cumulant equals charge variance",
        density_double_cumulant,
        charge_variance,
    )
    assert_equal(
        "density susceptibility equals charge susceptibility",
        density_double_cumulant / volume,
        charge_variance / volume,
    )

    contact_shift = Fraction(7, 11)
    integrated_contact_shift = sum(
        contact_shift if left == right else Fraction(0)
        for left in range(site_count)
        for right in range(site_count)
    ) / volume
    assert_equal(
        "integrated contact term shifts susceptibility",
        integrated_contact_shift,
        contact_shift,
    )
    assert_equal(
        "theta counterterm matches contact convention",
        density_double_cumulant / volume + integrated_contact_shift,
        charge_variance / volume + contact_shift,
    )

    periodic_connected = [
        Fraction(5, 6),
        Fraction(-1, 7),
        Fraction(2, 9),
        Fraction(-1, 7),
    ]
    periodic_double_sum = sum(
        periodic_connected[(left - right) % site_count]
        for left in range(site_count)
        for right in range(site_count)
    ) / volume
    assert_equal(
        "periodic double sum reduces to one-origin integral",
        periodic_double_sum,
        sum(periodic_connected),
    )


def check_cp_symmetric_first_moment() -> None:
    sector_weights = {
        -3: Fraction(5, 11),
        -2: Fraction(7, 13),
        -1: Fraction(2, 5),
        0: Fraction(17, 19),
        1: Fraction(2, 5),
        2: Fraction(7, 13),
        3: Fraction(5, 11),
    }
    total = sum(sector_weights.values(), Fraction(0))
    mean = sum(Fraction(charge) * weight for charge, weight in sector_weights.items()) / total
    require(mean == 0, "CP-symmetric theta weights should have zero first moment")


def check_anomaly_invariant_singlet_coordinate_and_mass_alignment() -> None:
    theta, i_log_det_u, alpha, arg_det_m = sp.symbols(
        "theta i_log_det_u alpha arg_det_m"
    )
    nf = sp.symbols("nf", positive=True, integer=True)

    theta_shifted = theta - 2 * nf * alpha
    i_log_det_u_shifted = i_log_det_u - 2 * nf * alpha

    invariant = theta - i_log_det_u
    shifted_invariant = theta_shifted - i_log_det_u_shifted
    assert_zero(
        "theta minus i log det U is axial invariant",
        shifted_invariant - invariant,
    )

    wrong_coordinate = theta + i_log_det_u
    shifted_wrong_coordinate = theta_shifted + i_log_det_u_shifted
    assert_zero(
        "theta plus i log det U shifts by minus four N_f alpha",
        shifted_wrong_coordinate - wrong_coordinate + 4 * nf * alpha,
    )
    require(
        sp.simplify(shifted_wrong_coordinate - wrong_coordinate) != 0,
        "wrong singlet coordinate accidentally became invariant",
    )

    # If the leading mass spurion aligns U with the phase of M, then
    # log det U = i arg det M and i log det U = - arg det M.
    i_log_det_u_at_mass_alignment = -arg_det_m
    assert_zero(
        "singlet coordinate matches microscopic strong-CP phase",
        invariant.subs(i_log_det_u, i_log_det_u_at_mass_alignment)
        - (theta + arg_det_m),
    )


def check_witten_veneziano_mass_coefficient() -> None:
    eta, theta, chi, f = sp.symbols("eta theta chi f", positive=True)
    nf = sp.symbols("nf", positive=True, integer=True)

    determinant_phase = sp.sqrt(2 * nf) * eta / f
    potential = sp.Rational(1, 2) * chi * (theta + determinant_phase) ** 2
    mass_squared = sp.diff(potential.subs(theta, 0), eta, 2)
    assert_zero("Witten-Veneziano coefficient", mass_squared - 2 * nf * chi / f**2)


def check_theta_eta_curvature_matrix() -> None:
    eta, theta, chi, f = sp.symbols("eta theta chi f", positive=True)
    nf = sp.symbols("nf", positive=True, integer=True)

    a = sp.sqrt(2 * nf) / f
    potential = sp.Rational(1, 2) * chi * (theta + a * eta) ** 2
    hessian = sp.Matrix(
        [
            [sp.diff(potential, theta, theta), sp.diff(potential, theta, eta)],
            [sp.diff(potential, eta, theta), sp.diff(potential, eta, eta)],
        ]
    )
    expected = chi * sp.Matrix([[1, a], [a, a**2]])
    for row in range(2):
        for col in range(2):
            assert_zero(
                f"theta-eta Hessian entry {row}{col}",
                hessian[row, col] - expected[row, col],
            )

    assert_zero("theta-eta Hessian determinant", hessian.det())
    null_vector = sp.Matrix([-a, 1])
    for row, entry in enumerate(hessian * null_vector):
        assert_zero(f"theta-eta screening null vector row {row}", entry)

    fixed_theta_mass = hessian[1, 1]
    assert_zero("fixed-theta singlet mass coefficient", fixed_theta_mass - 2 * nf * chi / f**2)
    schur_curvature = hessian[0, 0] - hessian[0, 1] * hessian[1, 0] / hessian[1, 1]
    assert_zero("screened theta Schur complement", schur_curvature)

    wrong_sign_potential = sp.Rational(1, 2) * chi * (theta - a * eta) ** 2
    wrong_mixed = sp.diff(wrong_sign_potential, theta, eta)
    assert_zero(
        "wrong-sign mixed derivative differs by minus 2 a chi",
        wrong_mixed - hessian[0, 1] + 2 * a * chi,
    )


def check_massless_quark_theta_screening() -> None:
    eta, theta, chi, f = sp.symbols("eta theta chi f", positive=True)
    nf_value = sp.Integer(3)
    determinant_phase = sp.sqrt(2 * nf_value) * eta / f
    potential = sp.Rational(1, 2) * chi * (theta + determinant_phase) ** 2
    eta_at_minimum = -theta * f / sp.sqrt(2 * nf_value)
    minimized = sp.simplify(potential.subs(eta, eta_at_minimum))
    assert_zero("massless theta screening", minimized)


def check_dilute_instanton_chiral_spurion_potential() -> None:
    eta, theta, zeta, f = sp.symbols("eta theta zeta f", positive=True)
    nf = sp.symbols("nf", positive=True, integer=True)

    a = sp.sqrt(2 * nf) / f
    minus_i_log_det_u = a * eta
    i_log_det_u = -minus_i_log_det_u
    theta_eff = theta - i_log_det_u
    assert_zero("dilute instanton determinant-log convention", theta_eff - (theta + a * eta))
    potential = 2 * zeta * (1 - sp.cos(theta_eff))

    det_phase = sp.symbols("det_phase", real=True)
    determinant_vertex = sp.exp(sp.I * theta) * sp.exp(sp.I * det_phase) + sp.exp(
        -sp.I * theta
    ) * sp.exp(-sp.I * det_phase)
    cosine_vertex = 2 * sp.cos(theta + det_phase).rewrite(sp.exp)
    assert_zero(
        "dilute instanton determinant vertex conjugation",
        sp.simplify(determinant_vertex - cosine_vertex),
    )

    susceptibility = sp.diff(potential.subs(eta, 0), theta, 2).subs(theta, 0)
    assert_zero("dilute instanton chiral susceptibility", susceptibility - 2 * zeta)

    hessian = sp.Matrix(
        [
            [sp.diff(potential, theta, theta), sp.diff(potential, theta, eta)],
            [sp.diff(potential, eta, theta), sp.diff(potential, eta, eta)],
        ]
    ).subs({theta: 0, eta: 0})
    expected = 2 * zeta * sp.Matrix([[1, a], [a, a**2]])
    for row in range(2):
        for col in range(2):
            assert_zero(
                f"dilute instanton chiral Hessian entry {row}{col}",
                hessian[row, col] - expected[row, col],
            )

    for row, entry in enumerate(hessian * sp.Matrix([-a, 1])):
        assert_zero(f"dilute instanton screening null vector row {row}", entry)

    mass_contribution = hessian[1, 1]
    assert_zero(
        "dilute instanton singlet mass contribution",
        mass_contribution - 4 * nf * zeta / f**2,
    )

    quartic = sp.diff(potential.subs(eta, 0), theta, 4).subs(theta, 0)
    assert_zero("dilute instanton cosine fourth derivative", quartic + 2 * zeta)


def check_eta_eta_prime_mass_matrix_ledger() -> None:
    m, ms, b0, m0_sq = sp.symbols("m ms B0 m0_sq", positive=True)
    m_pi_sq = 2 * b0 * m
    m_k_sq = b0 * (m + ms)

    mass = sp.diag(m, m, ms)
    t3 = sp.diag(1, -1, 0) / 2
    t8 = sp.diag(1, 1, -2) / (2 * sp.sqrt(3))
    t0 = sp.eye(3) / sp.sqrt(6)
    generators = [t3, t8, t0]
    mass_matrix = sp.Matrix(
        [
            [
                4
                * b0
                * sp.trace(
                    mass
                    * (generators[row] * generators[col] + generators[col] * generators[row])
                    / 2
                )
                for col in range(3)
            ]
            for row in range(3)
        ]
    )
    mass_matrix[2, 2] += m0_sq

    expected_neutral = sp.Matrix(
        [
            [m_pi_sq, 0, 0],
            [
                0,
                (4 * m_k_sq - m_pi_sq) / 3,
                -2 * sp.sqrt(2) * (m_k_sq - m_pi_sq) / 3,
            ],
            [
                0,
                -2 * sp.sqrt(2) * (m_k_sq - m_pi_sq) / 3,
                (2 * m_k_sq + m_pi_sq) / 3 + m0_sq,
            ],
        ]
    )
    for row in range(3):
        for col in range(3):
            assert_zero(
                f"eta neutral mass matrix entry {row}{col}",
                mass_matrix[row, col] - expected_neutral[row, col],
            )

    eta_block = mass_matrix[1:3, 1:3]
    trace_relation = sp.trace(eta_block) - 2 * m_k_sq
    assert_zero("eta eta-prime trace Witten-Veneziano relation", trace_relation - m0_sq)

    determinant_relation = eta_block.det() - (
        m_pi_sq * (2 * m_k_sq - m_pi_sq)
        + m0_sq * (4 * m_k_sq - m_pi_sq) / 3
    )
    assert_zero("eta eta-prime determinant ledger", determinant_relation)


def check_periodic_branch_relabeling() -> None:
    theta, chi = sp.symbols("theta chi")
    k = sp.symbols("k", integer=True)
    branch_energy = sp.Rational(1, 2) * chi * (theta + 2 * sp.pi * k) ** 2
    shifted = branch_energy.subs({theta: theta + 2 * sp.pi, k: k - 1})
    assert_zero("theta periodicity by branch relabeling", shifted - branch_energy)


def check_branch_mixture_cluster_covariance() -> None:
    weights = [sp.Rational(1, 5), sp.Rational(3, 10), sp.Rational(1, 2)]
    o_values = [sp.Rational(2, 3), sp.Rational(-1, 7), sp.Rational(5, 11)]
    p_values = [sp.Rational(13, 17), sp.Rational(3, 19), sp.Rational(-2, 23)]

    separated_limit = sum(weight * o * p for weight, o, p in zip(weights, o_values, p_values))
    one_point_product = (
        sum(weight * o for weight, o in zip(weights, o_values))
        * sum(weight * p for weight, p in zip(weights, p_values))
    )
    covariance = separated_limit - one_point_product

    mean_o = sum(weight * o for weight, o in zip(weights, o_values))
    mean_p = sum(weight * p for weight, p in zip(weights, p_values))
    covariance_direct = sum(
        weight * (o - mean_o) * (p - mean_p)
        for weight, o, p in zip(weights, o_values, p_values)
    )
    assert_zero("branch mixture cluster covariance", covariance - covariance_direct)

    pure_weights = [sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    pure_covariance = (
        sum(weight * o * p for weight, o, p in zip(pure_weights, o_values, p_values))
        - sum(weight * o for weight, o in zip(pure_weights, o_values))
        * sum(weight * p for weight, p in zip(pure_weights, p_values))
    )
    assert_zero("pure branch clusters", pure_covariance)


def check_unique_branch_thermodynamic_selection() -> None:
    volume, gap1, gap2, correction = sp.symbols("volume gap1 gap2 correction", positive=True)
    z_min = sp.exp(-volume * correction / volume)
    z_1 = sp.exp(-volume * gap1)
    z_2 = sp.exp(-volume * gap2)
    nonminimal_ratio = sp.simplify((z_1 + z_2) / z_min)
    require(
        nonminimal_ratio.subs({volume: 10, gap1: 2, gap2: 3, correction: sp.Rational(1, 7)}) < sp.Rational(1, 1000000),
        "nonminimal branch ratios should be exponentially suppressed",
    )


def main() -> None:
    check_finite_volume_cumulant_identity()
    check_finite_volume_theta_cumulant_hierarchy()
    check_local_density_susceptibility_cumulant()
    check_cp_symmetric_first_moment()
    check_anomaly_invariant_singlet_coordinate_and_mass_alignment()
    check_witten_veneziano_mass_coefficient()
    check_theta_eta_curvature_matrix()
    check_massless_quark_theta_screening()
    check_dilute_instanton_chiral_spurion_potential()
    check_eta_eta_prime_mass_matrix_ledger()
    check_periodic_branch_relabeling()
    check_branch_mixture_cluster_covariance()
    check_unique_branch_thermodynamic_selection()
    print("All QCD theta and Witten-Veneziano normalization checks passed.")


if __name__ == "__main__":
    main()
