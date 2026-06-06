#!/usr/bin/env python3
r"""Exact checks for theta, susceptibility, and Witten-Veneziano normalizations.

The finite theta-data checks distinguish exact finite-volume cumulant
identities from the continuum and branch-selection assumptions needed for QCD
theta physics.

Evidence contract.

Target claims:
- Volume II's theta and singlet-axial section uses the finite-volume
  susceptibility cumulant identity with the correct signs and contact-term
  convention.
- The Witten-Veneziano matching coordinate is theta - i log det U, and its
  local Hessian has the screening null vector required by a massless quark.
- The residual Witten-Veneziano budget is Ward-compatible in exactly massless
  QCD: it may shift the anomaly-invariant curvature, but it may not produce a
  nonzero full-QCD theta Schur complement unless finite masses or an explicit
  symmetry-breaking source are declared.
- The physical singlet mass at the same order is a generalized eigenvalue:
  the singlet kinetic normalization, or equivalently F_0^2/f_pi^2, is an
  independent residual from the theta-potential curvature.
- A dynamical pseudoscalar coupled only through the same renormalized theta
  source has curvature n_a^2 chi/(Z_a f_a^2) on a selected branch; fixed
  topology, screened massless-QCD theta curvature, and uncontrolled
  dilute-instanton activity are not substitute inputs.
- A dilute-instanton determinant curvature may be compared with the
  Witten-Veneziano pure-Yang-Mills curvature only after a same-scheme
  curvature-distance estimate and the pole-mass normalization/mixing residuals
  have been supplied; the full massless-QCD theta Schur complement remains
  zero for either rank-one local branch.

Independent construction:
- Builds finite theta partition functions directly from weighted topological
  sectors, differentiates log Z, and compares to cumulants.
- Derives fixed-topology sector weights and local-observable biases from the
  Gaussian Fourier saddle rather than estimating susceptibility inside a
  single fixed sector.
- Differentiates a dynamical-theta source potential, including the kinetic
  generalized-eigenvalue normalization and theta-cumulant self-couplings.
- Differentiates the singlet local potential and all Hessians symbolically,
  then computes Schur complements and null-vector conditions from the matrices.
- Computes the one-field and neutral two-field generalized eigenvalue
  conditions from K^{-1}H data instead of identifying a Hessian entry with a
  physical pole mass.
- Derives the eta/eta-prime mass matrix from flavor generators rather than
  importing the displayed matrix entries.
- Compares the dilute-instanton branch curvature with the pure-Yang-Mills
  Witten-Veneziano curvature symbolically, then checks a finite rational
  residual budget and the massless screening Schur complement.

Imported assumptions:
- The continuum branch and pure-Yang-Mills susceptibility are external inputs
  when the Witten-Veneziano matching window is invoked.
- The dilute-instanton spurion check assumes a finite-activity one-instanton
  determinant coefficient in the declared chiral matching scheme.

Negative controls:
- The wrong singlet coordinate fails axial invariance and flips the mixed
  derivative convention.
- An unconstrained residual Hessian is explicitly rejected as a massless-QCD
  residual when its Schur complement is nonzero and its screening vector is
  broken.
- A nontrivial singlet kinetic residual rejects the shortcut which reads the
  physical eta_0 mass directly from the potential Hessian.
- A nontrivial axion-source kinetic residual rejects the shortcut which reads a
  physical curvature mass directly from the source potential Hessian; fixed
  topology and screened massless-QCD theta curvature give zero in finite
  negative controls.
- Substituting the full massless-QCD susceptibility into the
  Witten-Veneziano mass relation, or replacing the pure-Yang-Mills curvature by
  the dilute-instanton activity without a sufficient curvature budget, is
  rejected by finite examples.
- A branch mixture gives a nonzero cluster covariance, while a pure selected
  branch has zero covariance.
- A fixed-topology sector has zero charge variance and therefore cannot by
  itself estimate the theta susceptibility; omitting the \(Q^2/(\chi V)\)
  bias term gives the wrong fixed-sector local observable for \(Q\ne0\).

Scope boundary:
- These checks verify algebraic identities and local matching bookkeeping.
  They do not prove the Yang-Mills continuum limit, the large-N expansion, the
  absence of branch crossings, or the semiclassical instanton measure.
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


def check_dynamical_theta_source_curvature() -> None:
    theta, a = sp.symbols("theta a")
    chi, b2, n_a, f_a, z_a = sp.symbols("chi b2 n_a f_a z_a", positive=True)

    theta_source = theta + n_a * a / f_a
    branch_energy = (
        sp.Rational(1, 2)
        * chi
        * theta_source**2
        * (1 + b2 * theta_source**2)
    )
    axion_hessian = sp.diff(branch_energy, a, 2).subs({theta: 0, a: 0})
    assert_zero(
        "dynamical theta source Hessian",
        axion_hessian - n_a**2 * chi / f_a**2,
    )
    physical_mass = sp.simplify(axion_hessian / z_a)
    assert_zero(
        "dynamical theta source generalized mass",
        physical_mass - n_a**2 * chi / (z_a * f_a**2),
    )
    mixed_source_curvature = sp.diff(branch_energy, theta, a).subs({theta: 0, a: 0})
    assert_zero(
        "dynamical theta mixed source curvature",
        mixed_source_curvature - n_a * chi / f_a,
    )
    axion_quartic = sp.diff(branch_energy, a, 4).subs({theta: 0, a: 0})
    assert_zero(
        "dynamical theta quartic cumulant",
        axion_quartic - 12 * chi * b2 * n_a**4 / f_a**4,
    )

    zeta = sp.symbols("zeta", positive=True)
    dilute_energy = 2 * zeta * (1 - sp.cos(theta_source))
    dilute_chi = sp.diff(dilute_energy.subs(a, 0), theta, 2).subs(theta, 0)
    assert_zero("dilute theta source susceptibility", dilute_chi - 2 * zeta)
    dilute_axion_hessian = sp.diff(dilute_energy, a, 2).subs({theta: 0, a: 0})
    assert_zero(
        "dilute theta source axion curvature",
        dilute_axion_hessian - 2 * zeta * n_a**2 / f_a**2,
    )
    dilute_b2 = (
        sp.diff(dilute_energy.subs(a, 0), theta, 4).subs(theta, 0)
        / (12 * dilute_chi)
    )
    assert_zero("dilute theta source b2", dilute_b2 + sp.Rational(1, 12))

    values = {
        chi: sp.Rational(7, 19),
        b2: -sp.Rational(2, 23),
        n_a: sp.Rational(3),
        f_a: sp.Rational(5),
        z_a: sp.Rational(11, 13),
    }
    require(
        sp.simplify(axion_hessian.subs(values) - physical_mass.subs(values)) != 0,
        "nontrivial Z_a should reject reading the Hessian as the physical mass",
    )

    screened_massless_qcd_mass = sp.Integer(0) * n_a**2 / (z_a * f_a**2)
    assert_zero("screened full-QCD massless theta source curvature", screened_massless_qcd_mass)
    require(
        sp.simplify(screened_massless_qcd_mass.subs(values) - physical_mass.subs(values)) != 0,
        "screened massless-QCD theta curvature should not replace branch curvature",
    )

    fixed_topology_variance = sp.Integer(0)
    fixed_topology_mass = n_a**2 * fixed_topology_variance / (z_a * f_a**2)
    require(
        sp.simplify(fixed_topology_mass.subs(values) - physical_mass.subs(values)) != 0,
        "fixed-topology sector variance should not supply axion curvature",
    )

    chi_target, zeta_trial, eps_chi = sp.symbols("chi_target zeta_trial eps_chi", positive=True)
    target_mass = n_a**2 * chi_target / (z_a * f_a**2)
    dilute_mass = n_a**2 * (2 * zeta_trial) / (z_a * f_a**2)
    comparison_values = {
        chi_target: sp.Rational(17, 19),
        zeta_trial: sp.Rational(8, 19),
        eps_chi: sp.Rational(1, 19),
        n_a: sp.Rational(3),
        f_a: sp.Rational(7),
        z_a: sp.Rational(5, 4),
    }
    mass_gap = abs(sp.simplify((target_mass - dilute_mass).subs(comparison_values)))
    curvature_budget = (
        n_a**2
        * eps_chi
        / (z_a * f_a**2)
    ).subs(comparison_values)
    require(
        mass_gap <= curvature_budget,
        "same-scheme theta-curvature budget should bound dilute-source mass error",
    )
    require(
        mass_gap > curvature_budget / 2,
        "under-budgeted dilute theta activity should be rejected",
    )


def check_fixed_topology_saddle_extraction() -> None:
    charge, sigma = sp.symbols("charge sigma", positive=True)
    leading_sector_weight = sp.exp(-charge**2 / (2 * sigma))

    gaussian_second_moment = -sp.diff(leading_sector_weight, charge, 2) / leading_sector_weight
    assert_zero(
        "fixed-topology Gaussian second theta moment",
        gaussian_second_moment - (1 / sigma - charge**2 / sigma**2),
    )

    gaussian_fourth_moment = sp.diff(leading_sector_weight, charge, 4) / leading_sector_weight
    expected_fourth = (
        3 / sigma**2
        - 6 * charge**2 / sigma**3
        + charge**4 / sigma**4
    )
    assert_zero(
        "fixed-topology Gaussian fourth theta moment",
        gaussian_fourth_moment - expected_fourth,
    )

    volume, chi, b2 = sp.symbols("volume chi b2", positive=True)
    sigma_substitution = {sigma: chi * volume}
    quartic_prefactor = chi * volume * b2 / 2
    quartic_log_correction = -quartic_prefactor * expected_fourth.subs(sigma_substitution)
    expected_correction = -b2 / 2 * (
        3 / (chi * volume)
        - 6 * charge**2 / (chi * volume) ** 2
        + charge**4 / (chi * volume) ** 3
    )
    assert_zero(
        "fixed-topology quartic sector correction",
        quartic_log_correction - expected_correction,
    )

    slope_in_charge_squared = -1 / (2 * chi * volume)
    extracted_chi = -1 / (2 * volume * slope_in_charge_squared)
    assert_zero("fixed-topology sector slope extracts chi", extracted_chi - chi)

    observable_curvature = sp.symbols("observable_curvature")
    fixed_q_observable_shift = (
        observable_curvature
        / 2
        * gaussian_second_moment.subs(sigma_substitution)
    )
    expected_shift = observable_curvature / (2 * chi * volume) * (
        1 - charge**2 / (chi * volume)
    )
    assert_zero(
        "fixed-topology local observable bias",
        fixed_q_observable_shift - expected_shift,
    )

    values = {
        chi: sp.Rational(5, 7),
        volume: sp.Rational(11, 1),
        charge: sp.Rational(2, 1),
        observable_curvature: sp.Rational(3, 13),
    }
    missing_charge_bias = values[observable_curvature] / (
        2 * values[chi] * values[volume]
    )
    require(
        sp.simplify(fixed_q_observable_shift.subs(values) - missing_charge_bias) != 0,
        "fixed-topology observable bias must retain the Q^2/(chi V) term",
    )

    fixed_sector_charge_variance = sp.Integer(0)
    theta_susceptibility_variance = chi * volume
    require(
        sp.simplify(fixed_sector_charge_variance - theta_susceptibility_variance) != 0,
        "fixed-topology charge variance should not estimate theta susceptibility",
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


def check_witten_veneziano_ward_compatible_residual_budget() -> None:
    chi, a = sp.symbols("chi a", positive=True)
    dchi = sp.symbols("dchi")
    btt, bte, bee, bchi = sp.symbols("btt bte bee bchi")

    rank_one = sp.Matrix([[1, a], [a, a**2]])
    null_vector = sp.Matrix([-a, 1])
    ward_hessian = (chi + dchi) * rank_one

    for row, entry in enumerate(ward_hessian * null_vector):
        assert_zero(f"WV Ward-compatible residual null vector row {row}", entry)

    ward_schur = (
        ward_hessian[0, 0]
        - ward_hessian[0, 1] * ward_hessian[1, 0] / ward_hessian[1, 1]
    )
    assert_zero("WV Ward-compatible massless Schur complement", ward_schur)
    assert_zero(
        "WV Ward-compatible singlet mass shift",
        ward_hessian[1, 1] - a**2 * chi - a**2 * dchi,
    )

    compatible_extra = sp.Matrix([[bchi, a * bchi], [a * bchi, a**2 * bchi]])
    for row, entry in enumerate(compatible_extra * null_vector):
        assert_zero(f"WV rank-one extra residual null vector row {row}", entry)
    compatible_schur = (
        (ward_hessian + compatible_extra)[0, 0]
        - (ward_hessian + compatible_extra)[0, 1]
        * (ward_hessian + compatible_extra)[1, 0]
        / (ward_hessian + compatible_extra)[1, 1]
    )
    assert_zero("WV rank-one extra residual remains screened", compatible_schur)

    breaking = sp.Matrix([[btt, bte], [bte, bee]])
    breaking_hessian = ward_hessian + breaking
    breaking_schur = (
        breaking_hessian[0, 0]
        - breaking_hessian[0, 1] * breaking_hessian[1, 0] / breaking_hessian[1, 1]
    )
    chi_eff = chi + dchi
    breaking_numerator = (
        chi_eff * bee
        + a**2 * chi_eff * btt
        + btt * bee
        - 2 * a * chi_eff * bte
        - bte**2
    )
    assert_zero(
        "WV Ward-breaking Schur diagnostic numerator",
        breaking_schur - breaking_numerator / breaking_hessian[1, 1],
    )

    bad_values = {
        chi: sp.Rational(5, 3),
        dchi: sp.Rational(1, 7),
        a: sp.Rational(3, 2),
        btt: sp.Rational(1, 17),
        bte: -sp.Rational(1, 19),
        bee: sp.Rational(1, 23),
    }
    bad_schur = sp.simplify(breaking_schur.subs(bad_values))
    require(
        bad_schur != 0,
        "unconstrained residual Hessian must not be accepted as massless screening",
    )
    bad_null = [sp.simplify(entry.subs(bad_values)) for entry in breaking_hessian * null_vector]
    require(
        any(entry != 0 for entry in bad_null),
        "unconstrained residual Hessian should break the massless screening vector",
    )

    constrained_values = {
        btt: bchi,
        bte: a * bchi,
        bee: a**2 * bchi,
    }
    assert_zero(
        "WV constrained residual Schur cancellation",
        breaking_schur.subs(constrained_values),
    )


def check_witten_veneziano_kinetic_normalization_residual() -> None:
    chi, dchi, f_pi, z0, nf = sp.symbols(
        "chi dchi f_pi z0 nf",
        positive=True,
    )
    r_chi, r_z = sp.symbols("r_chi r_z", positive=True)

    a = sp.sqrt(2 * nf) / f_pi
    h_eta_eta = a**2 * (chi + dchi)
    physical_mass = sp.simplify(h_eta_eta / z0)
    expected_mass = 2 * nf * (chi + dchi) / (z0 * f_pi**2)
    assert_zero(
        "WV physical mass uses generalized one-field eigenvalue",
        physical_mass - expected_mass,
    )

    leading_mass = 2 * nf * chi / f_pi**2
    exact_shift = sp.simplify(physical_mass - leading_mass)
    expected_shift = sp.simplify(
        2 * nf / f_pi**2 * ((chi + dchi) / z0 - chi)
    )
    assert_zero("WV kinetic-normalization mass shift", exact_shift - expected_shift)

    values = {
        chi: sp.Rational(5, 1),
        dchi: sp.Rational(-1, 7),
        nf: sp.Rational(3, 1),
        f_pi: sp.Rational(11, 1),
        z0: sp.Rational(12, 11),
    }
    wrong_hessian_mass = h_eta_eta.subs(values)
    right_generalized_mass = physical_mass.subs(values)
    require(
        sp.simplify(wrong_hessian_mass - right_generalized_mass) != 0,
        "nontrivial Z0 should reject Hessian-entry mass shortcut",
    )

    bound_values = {
        chi: sp.Rational(5, 1),
        dchi: -sp.Rational(1, 7),
        nf: sp.Rational(3, 1),
        f_pi: sp.Rational(11, 1),
        z0: sp.Rational(12, 11),
        r_chi: sp.Rational(1, 7),
        r_z: sp.Rational(1, 11),
    }
    bounded_shift = abs(sp.simplify(exact_shift.subs(bound_values)))
    bound = (
        2
        * bound_values[nf]
        / bound_values[f_pi] ** 2
        * (bound_values[r_chi] + bound_values[chi] * bound_values[r_z])
        / (1 - bound_values[r_z])
    )
    require(
        bounded_shift <= bound,
        "WV combined curvature and kinetic residual bound should dominate shift",
    )

    theta_hessian = (chi + dchi) * sp.Matrix([[1, a], [a, a**2]])
    schur = (
        theta_hessian[0, 0]
        - theta_hessian[0, 1] * theta_hessian[1, 0] / theta_hessian[1, 1]
    )
    assert_zero(
        "WV kinetic normalization does not alter massless theta Schur complement",
        schur,
    )

    h88, h80, h00, k88, k80, k00, mass_sq = sp.symbols(
        "h88 h80 h00 k88 k80 k00 mass_sq"
    )
    h_neutral = sp.Matrix([[h88, h80], [h80, h00]])
    k_neutral = sp.Matrix([[k88, k80], [k80, k00]])
    characteristic = sp.factor((h_neutral - mass_sq * k_neutral).det())
    expected_characteristic = sp.factor(
        (h88 - mass_sq * k88) * (h00 - mass_sq * k00)
        - (h80 - mass_sq * k80) ** 2
    )
    assert_zero(
        "WV neutral generalized eigenvalue characteristic",
        characteristic - expected_characteristic,
    )

    single_field_root = sp.simplify(
        (h00 / k00).subs({h00: sp.Rational(7), k00: sp.Rational(5)})
    )
    mixed_values = {
        h88: sp.Rational(2),
        h80: sp.Rational(1, 3),
        h00: sp.Rational(7),
        k88: sp.Rational(1),
        k80: sp.Rational(1, 5),
        k00: sp.Rational(5),
        mass_sq: single_field_root,
    }
    require(
        sp.simplify(characteristic.subs(mixed_values)) != 0,
        "finite eta0-octet mixing should reject the unmixed singlet mass root",
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


def check_instanton_witten_veneziano_comparison_window() -> None:
    chi_ym, zeta, eps_chi, f_pi, z0, nf = sp.symbols(
        "chi_ym zeta eps_chi f_pi z0 nf",
        positive=True,
    )
    r_branch, r_mix, r_chiral, r_kin = sp.symbols(
        "r_branch r_mix r_chiral r_kin",
        nonnegative=True,
    )
    theta, eta = sp.symbols("theta eta")

    chi_inst = 2 * zeta
    a = sp.sqrt(2 * nf) / f_pi
    h_inst = chi_inst * sp.Matrix([[1, a], [a, a**2]])
    schur_inst = sp.simplify(
        h_inst[0, 0] - h_inst[0, 1] * h_inst[1, 0] / h_inst[1, 1]
    )
    assert_zero("instanton branch massless theta Schur complement", schur_inst)

    m_wv = 2 * nf * chi_ym / (z0 * f_pi**2)
    m_inst = 2 * nf * chi_inst / (z0 * f_pi**2)
    assert_zero(
        "instanton-WV mass difference tracks curvature difference",
        (m_wv - m_inst)
        - 2 * nf * (chi_ym - chi_inst) / (z0 * f_pi**2),
    )

    comparison_values = {
        nf: sp.Rational(3),
        f_pi: sp.Rational(11),
        z0: sp.Rational(5, 4),
        chi_ym: sp.Rational(17, 19),
        zeta: sp.Rational(8, 19),
        eps_chi: sp.Rational(1, 19),
        r_branch: sp.Rational(0),
        r_mix: sp.Rational(0),
    }
    mass_gap = abs(sp.simplify((m_wv - m_inst).subs(comparison_values)))
    mass_budget = 2 * nf * eps_chi / (z0 * f_pi**2) + r_branch + r_mix
    residual_budget = sp.simplify(mass_budget.subs(comparison_values))
    curvature_only_budget = (
        2
        * comparison_values[nf]
        * comparison_values[eps_chi]
        / (comparison_values[z0] * comparison_values[f_pi] ** 2)
    )
    require(
        mass_gap <= residual_budget,
        "same-scheme curvature distance should bound instanton-WV mass gap",
    )

    too_small_budget = curvature_only_budget / 2
    require(
        mass_gap > too_small_budget,
        "insufficient instanton-WV curvature budget should be rejected",
    )

    wrong_full_qcd_mass = m_wv.subs({chi_ym: 0})
    require(
        sp.simplify(
            m_wv.subs(comparison_values)
            - wrong_full_qcd_mass.subs(comparison_values)
        )
        != 0,
        "full massless-QCD susceptibility must not replace pure-YM WV curvature",
    )

    trace_wv = 2 * nf * chi_ym / f_pi**2
    trace_inst = 2 * nf * chi_inst / f_pi**2
    trace_residual_budget = 2 * nf * eps_chi / f_pi**2 + r_chiral + r_kin + r_mix
    trace_values = {
        nf: sp.Rational(3),
        f_pi: sp.Rational(13),
        chi_ym: sp.Rational(23, 29),
        zeta: sp.Rational(11, 29),
        eps_chi: sp.Rational(1, 29),
        r_chiral: sp.Rational(1, 101),
        r_kin: sp.Rational(1, 103),
        r_mix: sp.Rational(1, 107),
    }
    trace_gap = abs(sp.simplify((trace_wv - trace_inst).subs(trace_values)))
    require(
        trace_gap <= trace_residual_budget.subs(trace_values),
        "eta trace instanton approximant should be controlled by curvature residual budget",
    )

    potential = sp.Rational(1, 2) * chi_inst * (theta + a * eta) ** 2
    fixed_singlet_curvature = sp.diff(potential.subs(eta, 0), theta, 2)
    minimized = sp.simplify(potential.subs(eta, -theta / a))
    assert_zero("instanton branch minimized theta energy", minimized)
    require(
        sp.simplify(fixed_singlet_curvature.subs(comparison_values)) != 0,
        "fixed-branch instanton theta curvature should differ from minimized full-QCD curvature",
    )


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
    check_dynamical_theta_source_curvature()
    check_fixed_topology_saddle_extraction()
    check_cp_symmetric_first_moment()
    check_anomaly_invariant_singlet_coordinate_and_mass_alignment()
    check_witten_veneziano_mass_coefficient()
    check_theta_eta_curvature_matrix()
    check_witten_veneziano_ward_compatible_residual_budget()
    check_witten_veneziano_kinetic_normalization_residual()
    check_massless_quark_theta_screening()
    check_dilute_instanton_chiral_spurion_potential()
    check_instanton_witten_veneziano_comparison_window()
    check_eta_eta_prime_mass_matrix_ledger()
    check_periodic_branch_relabeling()
    check_branch_mixture_cluster_covariance()
    check_unique_branch_thermodynamic_selection()
    print("All QCD theta and Witten-Veneziano normalization checks passed.")


if __name__ == "__main__":
    main()
