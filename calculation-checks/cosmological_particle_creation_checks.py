#!/usr/bin/env python3
"""Exact convention checks for cosmological particle-creation formulas.

Evidence contract.

Target claims:
- `ch:cosmological-particle-creation`: Robertson-Walker scalar-mode
  conventions, de Sitter index arithmetic, Bogoliubov normalization and
  phase-sensitive annihilator transformations, detector positivity,
  finite adiabatic-order bookkeeping, produced-stress source coordinates,
  pressure work, omitted-stress conservation defects, Friedmann response
  coefficients, compact spacetime stress-noise smearing, retarded metric-noise
  pushforward, and a finite backreaction-window budget.

Independent construction:
- The checks use finite mode sums, exact rational complex two-mode
  Bogoliubov matrices, direct coefficient comparison, retained FLRW
  stress-source samples, adversarial omitted-stress decompositions, and finite
  cell-averaged covariance matrices rather than copying the prose formulae.

Imported assumptions:
- The free scalar mode equation, adiabatic/asymptotic particle basis,
  finite-volume two-mode CCR, and renormalized-stress subtraction scheme
  stated in the chapter.

Negative controls:
- Wrong scale-factor powers, missing pressure work, treating ongoing
  production as a conserved fluid, untransported scheme shifts, omitted
  tail/noise budgets, number-density-only sources, zero-particle source
  shortcuts, using the diagonal identity as an omitted-stress residual,
  curvature-as-zeroth-order WKB bookkeeping, finite-order adiabatic/Hadamard
  conflation, pointlike spatial stress-noise evaluation,
  unnormalized whole-slice smearing, the old conjugated-alpha annihilator rule,
  and real-quench-only Bogoliubov tests are rejected.

Scope boundary:
- Passing this file checks finite stress-source, stress-noise, response, and
  Bogoliubov bookkeeping; it does not prove interacting cosmological QFT, full
  adiabatic subtraction, or nonlinear semiclassical existence.
"""

from __future__ import annotations

from fractions import Fraction


ComplexRat = tuple[Fraction, Fraction]
Matrix2 = tuple[tuple[ComplexRat, ComplexRat], tuple[ComplexRat, ComplexRat]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def c(real: int | Fraction, imag: int | Fraction = 0) -> ComplexRat:
    return (Fraction(real), Fraction(imag))


def cadd(left: ComplexRat, right: ComplexRat) -> ComplexRat:
    return (left[0] + right[0], left[1] + right[1])


def cneg(value: ComplexRat) -> ComplexRat:
    return (-value[0], -value[1])


def cmul(left: ComplexRat, right: ComplexRat) -> ComplexRat:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cconj(value: ComplexRat) -> ComplexRat:
    return (value[0], -value[1])


def cabs2(value: ComplexRat) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            cadd(cmul(left[0][0], right[0][0]), cmul(left[0][1], right[1][0])),
            cadd(cmul(left[0][0], right[0][1]), cmul(left[0][1], right[1][1])),
        ),
        (
            cadd(cmul(left[1][0], right[0][0]), cmul(left[1][1], right[1][0])),
            cadd(cmul(left[1][0], right[0][1]), cmul(left[1][1], right[1][1])),
        ),
    )


def conformal_coupling(d: int) -> Fraction:
    return Fraction(d - 2, 4 * (d - 1))


def check_conformal_cancellation() -> None:
    for d in range(2, 13):
        xi = conformal_coupling(d)
        p = Fraction(d - 2, 2)
        curvature_hprime_coeff = xi * (d - 1) * 2
        curvature_hsquare_coeff = xi * (d - 1) * (d - 2)
        assert_equal(f"H' cancellation d={d}", curvature_hprime_coeff, p)
        assert_equal(f"H^2 cancellation d={d}", curvature_hsquare_coeff, p * p)


def de_sitter_nu_squared(d: int, mass_over_h_squared: Fraction, xi: Fraction) -> Fraction:
    return Fraction((d - 1) ** 2, 4) - mass_over_h_squared - xi * d * (d - 1)


def check_de_sitter_nu_values() -> None:
    for d in range(2, 13):
        assert_equal(
            f"conformal massless de Sitter nu^2 d={d}",
            de_sitter_nu_squared(d, Fraction(0), conformal_coupling(d)),
            Fraction(1, 4),
        )
    assert_equal(
        "four-dimensional minimally coupled massless nu^2",
        de_sitter_nu_squared(4, Fraction(0), Fraction(0)),
        Fraction(9, 4),
    )


def check_de_sitter_frequency_coefficient() -> None:
    samples = [
        (3, Fraction(2, 5), Fraction(1, 8)),
        (4, Fraction(7, 3), Fraction(1, 6)),
        (7, Fraction(5, 2), Fraction(3, 20)),
    ]
    for d, mass_over_h_squared, xi in samples:
        p = Fraction(d - 2, 2)
        coefficient = mass_over_h_squared + xi * d * (d - 1) - p * (p + 1)
        nu2 = de_sitter_nu_squared(d, mass_over_h_squared, xi)
        assert_equal(
            f"de Sitter frequency coefficient d={d}",
            coefficient,
            -(nu2 - Fraction(1, 4)),
        )


def check_sudden_quench_bogoliubov() -> None:
    samples = [(Fraction(1), Fraction(4)), (Fraction(2, 3), Fraction(7, 5)), (Fraction(5), Fraction(2))]
    for omega_i, omega_f in samples:
        alpha_squared = (omega_f + omega_i) ** 2 / (4 * omega_i * omega_f)
        beta_squared = (omega_f - omega_i) ** 2 / (4 * omega_i * omega_f)
        assert_equal(f"Bogoliubov normalization {omega_i}->{omega_f}", alpha_squared - beta_squared, 1)


def check_complex_bogoliubov_annihilator_matrix() -> None:
    alpha = c(Fraction(1), Fraction(4, 3))
    beta = c(Fraction(20, 39), Fraction(16, 13))
    assert_equal("complex Bogoliubov normalization", cabs2(alpha) - cabs2(beta), Fraction(1))

    mode_matrix: Matrix2 = (
        (alpha, beta),
        (cconj(beta), cconj(alpha)),
    )
    inverse_mode_matrix: Matrix2 = (
        (cconj(alpha), cneg(beta)),
        (cneg(cconj(beta)), alpha),
    )
    identity: Matrix2 = ((c(1), c(0)), (c(0), c(1)))
    assert_equal("mode matrix inverse", matmul(mode_matrix, inverse_mode_matrix), identity)
    assert_equal("inverse mode matrix", matmul(inverse_mode_matrix, mode_matrix), identity)

    # The field coefficient row satisfies a_out^T = a_in^T B, so the
    # annihilator column transforms with B^T, not B^dagger or B^{-1}.
    annihilator_matrix: Matrix2 = (
        (alpha, cconj(beta)),
        (beta, cconj(alpha)),
    )
    wrong_adjoint_first_coefficient = cconj(alpha)
    assert_equal(
        "complex alpha exposes old conjugation error",
        annihilator_matrix[0][0] == wrong_adjoint_first_coefficient,
        False,
    )

    particle_number = cabs2(annihilator_matrix[0][1])
    assert_equal("out particle number from complex beta", particle_number, cabs2(beta))
    anomalous_correlator = cmul(alpha, cconj(beta))
    wrong_anomalous_correlator = cmul(cconj(alpha), cconj(beta))
    assert_equal(
        "complex anomalous correlator rejects conjugated alpha",
        anomalous_correlator == wrong_anomalous_correlator,
        False,
    )
    assert_equal(
        "phase-sensitive anomalous correlator",
        anomalous_correlator,
        cmul(annihilator_matrix[0][0], annihilator_matrix[0][1]),
    )

    phase_in = c(Fraction(3, 5), Fraction(4, 5))
    phase_out = c(Fraction(5, 13), -Fraction(12, 13))
    alpha_rephased = cmul(cmul(phase_in, cconj(phase_out)), alpha)
    beta_rephased = cmul(cmul(phase_in, phase_out), beta)
    assert_equal(
        "alpha rephasing keeps annihilator coefficient covariant",
        cmul(alpha_rephased, cconj(phase_in)),
        cmul(cconj(phase_out), alpha),
    )
    assert_equal(
        "beta rephasing keeps creation coefficient covariant",
        cmul(cconj(beta_rephased), phase_in),
        cmul(cconj(phase_out), cconj(beta)),
    )


def check_adiabatic_riccati_power_law() -> None:
    # For W=c/eta, the exact Riccati equation gives
    # Omega^2=(c^2+1/4)/eta^2.
    samples = [(Fraction(3, 2), Fraction(5, 7)), (Fraction(4), Fraction(2, 3))]
    for c, eta in samples:
        w = c / eta
        wp_over_w = -1 / eta
        wpp_over_w = 2 / (eta * eta)
        omega_squared = w * w + Fraction(1, 2) * wpp_over_w - Fraction(3, 4) * wp_over_w * wp_over_w
        assert_equal(
            f"adiabatic Riccati power law c={c} eta={eta}",
            omega_squared,
            (c * c + Fraction(1, 4)) / (eta * eta),
        )


def check_finite_adiabatic_order_bookkeeping() -> None:
    omega0 = Fraction(5)
    omega0_prime = Fraction(2, 3)
    omega0_second = -Fraction(1, 7)
    curvature_potential_second_order = Fraction(3, 11)

    second_order_correction = (
        curvature_potential_second_order / (2 * omega0)
        - omega0_second / (4 * omega0 * omega0)
        + 3 * omega0_prime * omega0_prime / (8 * omega0 * omega0 * omega0)
    )
    riccati_second_order_rhs = (
        curvature_potential_second_order
        - Fraction(1, 2) * omega0_second / omega0
        + Fraction(3, 4) * (omega0_prime / omega0) * (omega0_prime / omega0)
    )
    assert_equal(
        "second adiabatic order Riccati recursion",
        2 * omega0 * second_order_correction,
        riccati_second_order_rhs,
    )

    derivative_only_correction = (
        -omega0_second / (4 * omega0 * omega0)
        + 3 * omega0_prime * omega0_prime / (8 * omega0 * omega0 * omega0)
    )
    assert_equal(
        "curvature potential is not zeroth-order WKB data",
        2 * omega0 * derivative_only_correction == riccati_second_order_rhs,
        False,
    )

    adiabatic_order = Fraction(4)
    stress_subtraction_required_order = Fraction(4)
    sobolev_regular_orders_below = adiabatic_order + Fraction(3, 2)
    full_hadamard_test_order = Fraction(8)
    assert_equal(
        "finite fourth order passes selected stress subtraction gate",
        adiabatic_order >= stress_subtraction_required_order,
        True,
    )
    assert_equal(
        "finite fourth order fails full Hadamard smooth-difference gate",
        full_hadamard_test_order < sobolev_regular_orders_below,
        False,
    )

    truncated_frequency = Fraction(7, 3)
    truncated_frequency_prime = -Fraction(5, 11)
    amplitude_squared = 1 / (2 * truncated_frequency)
    log_derivative_real_part = -truncated_frequency_prime / (
        2 * truncated_frequency
    )
    assert_equal(
        "truncated WKB initial data has unit Wronskian factor",
        2 * truncated_frequency * amplitude_squared,
        Fraction(1),
    )
    assert_equal(
        "truncated WKB initial real logarithmic derivative",
        log_derivative_real_part,
        Fraction(5, 22) / truncated_frequency,
    )
    bad_truncated_frequency = -Fraction(1, 5)
    assert_equal(
        "negative truncated frequency violates positivity boundary",
        bad_truncated_frequency > 0,
        False,
    )


def check_detector_positive_type_finite_model() -> None:
    gram = [
        [Fraction(5), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]
    vectors = [
        (Fraction(1), Fraction(0)),
        (Fraction(3), Fraction(-2)),
        (Fraction(-1), Fraction(4)),
    ]
    for x, y in vectors:
        quadratic = gram[0][0] * x * x + 2 * gram[0][1] * x * y + gram[1][1] * y * y
        if quadratic < 0:
            raise AssertionError(f"positive-type detector Gram form failed: {quadratic}")


def check_out_region_produced_stress_tensor() -> None:
    # In d spacetime dimensions, the out-region produced energy density is
    # a^{-d} sum Omega_k |beta_k|^2 over comoving modes.  The extra a^{-1}
    # converts conformal energy to physical energy.
    d = 4
    scale_factor = Fraction(2)
    modes = [
        # degeneracy, comoving momentum k, conformal frequency Omega, |beta|^2
        (3, Fraction(8), Fraction(10), Fraction(1, 5)),
        (2, Fraction(0), Fraction(6), Fraction(1, 7)),
    ]
    energy_sum = sum(
        Fraction(degeneracy) * omega * beta2
        for degeneracy, _k, omega, beta2 in modes
    )
    pressure_sum = sum(
        Fraction(degeneracy) * k * k * beta2 / ((d - 1) * omega)
        for degeneracy, k, omega, beta2 in modes
    )
    energy_density = energy_sum / (scale_factor ** d)
    pressure = pressure_sum / (scale_factor ** d)
    assert_equal("out produced energy density", energy_density, Fraction(27, 56))
    assert_equal("out produced pressure", pressure, Fraction(2, 25))

    wrong_comoving_volume_only_density = energy_sum / (scale_factor ** (d - 1))
    assert_equal(
        "comoving-volume-only density has wrong scale factor power",
        wrong_comoving_volume_only_density == energy_density,
        False,
    )

    massless_modes = [
        (1, Fraction(3), Fraction(3), Fraction(2, 9)),
        (4, Fraction(5), Fraction(5), Fraction(1, 25)),
    ]
    massless_energy_sum = sum(
        Fraction(degeneracy) * omega * beta2
        for degeneracy, _k, omega, beta2 in massless_modes
    )
    massless_pressure_sum = sum(
        Fraction(degeneracy) * k * k * beta2 / ((d - 1) * omega)
        for degeneracy, k, omega, beta2 in massless_modes
    )
    assert_equal(
        "massless produced equation of state",
        massless_pressure_sum,
        massless_energy_sum / (d - 1),
    )

    no_particles = [
        (1, Fraction(3), Fraction(5), Fraction(0)),
        (2, Fraction(4), Fraction(7), Fraction(0)),
    ]
    assert_equal(
        "zero beta gives zero produced energy",
        sum(Fraction(degeneracy) * omega * beta2 for degeneracy, _k, omega, beta2 in no_particles),
        Fraction(0),
    )

    kappa_d = Fraction(3, 2)
    friedmann_coefficient = 2 * kappa_d / ((d - 1) * (d - 2))
    assert_equal("four-dimensional Friedmann response coefficient", friedmann_coefficient, Fraction(1, 2))
    assert_equal(
        "produced Friedmann Hubble-square response",
        friedmann_coefficient * energy_density,
        Fraction(27, 112),
    )


def check_produced_stress_continuity_check() -> None:
    # In physical Robertson-Walker time,
    # rho=a^(-d) sum Omega n and
    # P=a^(-d) sum k^2 n/((d-1) Omega) obey
    # dot rho +(d-1)H(rho+P)=a^(-d) sum Omega dot n.
    d = 4
    scale_factor = Fraction(2)
    hubble = Fraction(1, 3)
    modes = [
        # degeneracy, comoving momentum k, conformal frequency Omega, n, dot n
        (2, Fraction(3), Fraction(5), Fraction(7, 11), Fraction(1, 13)),
        (1, Fraction(4), Fraction(6), Fraction(5, 17), -Fraction(1, 19)),
    ]

    rho_sum = sum(
        Fraction(degeneracy) * omega * occupation
        for degeneracy, _k, omega, occupation, _occupation_dot in modes
    )
    pressure_sum = sum(
        Fraction(degeneracy) * k * k * occupation / ((d - 1) * omega)
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    )
    production_sum = sum(
        Fraction(degeneracy) * omega * occupation_dot
        for degeneracy, _k, omega, _occupation, occupation_dot in modes
    )
    omega_dot_sum = sum(
        Fraction(degeneracy)
        * hubble
        * (omega - k * k / omega)
        * occupation
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    )

    rho = rho_sum / (scale_factor ** d)
    pressure = pressure_sum / (scale_factor ** d)
    production_source = production_sum / (scale_factor ** d)
    rho_dot = (
        omega_dot_sum + production_sum
    ) / (scale_factor ** d) - d * hubble * rho

    assert_equal(
        "produced stress continuity source",
        rho_dot + (d - 1) * hubble * (rho + pressure),
        production_source,
    )

    constant_occupations = [
        (degeneracy, k, omega, occupation, Fraction(0))
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    ]
    constant_production_sum = sum(
        Fraction(degeneracy) * omega * occupation_dot
        for degeneracy, _k, omega, _occupation, occupation_dot in constant_occupations
    )
    assert_equal("constant occupation has no production source", constant_production_sum, Fraction(0))

    wrong_pressure = sum(
        Fraction(degeneracy) * k * k * occupation / omega
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    ) / (scale_factor ** d)
    assert_equal(
        "wrong pressure normalization breaks continuity",
        rho_dot + (d - 1) * hubble * (rho + wrong_pressure) == production_source,
        False,
    )

    wrong_source_scale = production_sum / (scale_factor ** (d - 1))
    assert_equal(
        "wrong production source scale-factor power",
        wrong_source_scale == production_source,
        False,
    )

    assert_equal(
        "ongoing production is not a conserved fluid",
        rho_dot + (d - 1) * hubble * (rho + pressure) == 0,
        False,
    )


def check_omitted_stress_conservation_defect() -> None:
    d = 4
    scale_factor = Fraction(2)
    hubble = Fraction(1, 3)
    modes = [
        # degeneracy, comoving momentum k, conformal frequency Omega, n, dot n
        (2, Fraction(3), Fraction(5), Fraction(7, 11), Fraction(1, 13)),
        (1, Fraction(4), Fraction(6), Fraction(5, 17), -Fraction(1, 19)),
    ]

    rho_sum = sum(
        Fraction(degeneracy) * omega * occupation
        for degeneracy, _k, omega, occupation, _occupation_dot in modes
    )
    pressure_sum = sum(
        Fraction(degeneracy) * k * k * occupation / ((d - 1) * omega)
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    )
    production_sum = sum(
        Fraction(degeneracy) * omega * occupation_dot
        for degeneracy, _k, omega, _occupation, occupation_dot in modes
    )
    omega_dot_sum = sum(
        Fraction(degeneracy)
        * hubble
        * (omega - k * k / omega)
        * occupation
        for degeneracy, k, omega, occupation, _occupation_dot in modes
    )

    rho = rho_sum / (scale_factor ** d)
    pressure = pressure_sum / (scale_factor ** d)
    production_source = production_sum / (scale_factor ** d)
    rho_dot = (
        omega_dot_sum + production_sum
    ) / (scale_factor ** d) - d * hubble * rho

    old_diagonal_difference = (
        rho_dot + (d - 1) * hubble * (rho + pressure) - production_source
    )
    assert_equal(
        "old diagonal continuity difference is tautologically zero",
        old_diagonal_difference,
        Fraction(0),
    )

    coherence_rho = Fraction(1, 30)
    coherence_pressure = Fraction(1, 45)
    coherence_rho_dot = Fraction(1, 70)
    coherence_divergence = coherence_rho_dot + (d - 1) * hubble * (
        coherence_rho + coherence_pressure
    )

    basis_rho = Fraction(1, 40)
    basis_pressure = Fraction(1, 120)
    # Choose the basis-change channel so the full renormalized stress is
    # conserved, while the omitted stress divergence remains nonzero.
    basis_divergence = -production_source - coherence_divergence
    basis_rho_dot = basis_divergence - (d - 1) * hubble * (
        basis_rho + basis_pressure
    )

    missing_rho = coherence_rho + basis_rho
    missing_pressure = coherence_pressure + basis_pressure
    missing_rho_dot = coherence_rho_dot + basis_rho_dot
    omitted_divergence_defect = missing_rho_dot + (d - 1) * hubble * (
        missing_rho + missing_pressure
    )
    assert_equal(
        "full stress minus diagonal stress is nonzero",
        (missing_rho == 0 and missing_pressure == 0),
        False,
    )
    assert_equal(
        "omitted stress divergence cancels production in conserved full stress",
        production_source + omitted_divergence_defect,
        Fraction(0),
    )
    assert_equal(
        "corrected omitted-stress defect detects discarded channels",
        omitted_divergence_defect == Fraction(0),
        False,
    )

    wrong_no_pressure_residual = rho_dot + (d - 1) * hubble * rho - production_source
    assert_equal(
        "dropping pressure fails the diagonal source equation",
        wrong_no_pressure_residual == Fraction(0),
        False,
    )
    wrong_no_source_residual = rho_dot + (d - 1) * hubble * (rho + pressure)
    assert_equal(
        "dropping production source fails during particle creation",
        wrong_no_source_residual == Fraction(0),
        False,
    )


def check_cosmological_backreaction_window() -> None:
    d = 4
    kappa_d = Fraction(3, 2)
    friedmann_coefficient = 2 * kappa_d / ((d - 1) * (d - 2))
    assert_equal(
        "backreaction-window Friedmann coefficient",
        friedmann_coefficient,
        Fraction(1, 2),
    )

    produced_energy = Fraction(27, 56)
    produced_pressure = Fraction(2, 25)
    retained_delta_hubble_squared = friedmann_coefficient * produced_energy
    assert_equal(
        "retained produced Hubble-square coordinate",
        retained_delta_hubble_squared,
        Fraction(27, 112),
    )

    # A finite stress scheme shift is harmless only when the gravitational
    # coordinate is transported with it.
    finite_scheme_shift = Fraction(1, 300)
    untransported_response = friedmann_coefficient * (
        produced_energy + finite_scheme_shift
    )
    transported_gravity_shift = -friedmann_coefficient * finite_scheme_shift
    transported_response = untransported_response + transported_gravity_shift
    assert_equal(
        "transported scheme coordinate",
        transported_response,
        retained_delta_hubble_squared,
    )
    assert_equal(
        "untransported scheme shift changes response",
        untransported_response == retained_delta_hubble_squared,
        False,
    )

    coherence_remainder = Fraction(1, 150)
    basis_remainder = -Fraction(1, 300)
    vacuum_remainder = Fraction(1, 1000)
    geometric_remainder = -Fraction(1, 1000)
    tail_remainder = Fraction(1, 100)
    missing_stress_density = (
        coherence_remainder
        + basis_remainder
        + vacuum_remainder
        + geometric_remainder
        + tail_remainder
    )
    gravitational_remainder = Fraction(1, 2000)
    full_delta_hubble_squared = (
        friedmann_coefficient * (produced_energy + missing_stress_density)
        + gravitational_remainder
    )
    error = abs(full_delta_hubble_squared - retained_delta_hubble_squared)
    density_budget = (
        abs(coherence_remainder)
        + abs(basis_remainder)
        + abs(vacuum_remainder)
        + abs(geometric_remainder)
        + abs(tail_remainder)
    )
    full_budget = friedmann_coefficient * density_budget + abs(gravitational_remainder)
    missing_coherence_basis_budget = (
        friedmann_coefficient
        * (abs(vacuum_remainder) + abs(geometric_remainder) + abs(tail_remainder))
        + abs(gravitational_remainder)
    )
    assert_equal("backreaction remainder budget controls response", error <= full_budget, True)
    assert_equal(
        "omitting coherence/basis budgets undercontrols response",
        error <= missing_coherence_basis_budget,
        False,
    )

    hubble = Fraction(1, 3)
    production_source = Fraction(7, 80)
    produced_energy_dot = (
        production_source
        - (d - 1) * hubble * (produced_energy + produced_pressure)
    )
    retained_delta_hubble_squared_dot = friedmann_coefficient * produced_energy_dot
    drift_bound = friedmann_coefficient * (
        abs(production_source)
        + (d - 1) * abs(hubble) * (abs(produced_energy) + abs(produced_pressure))
    )
    assert_equal(
        "produced-source drift bound",
        abs(retained_delta_hubble_squared_dot) <= drift_bound,
        True,
    )
    missing_pressure_energy_dot = (
        production_source
        - (d - 1) * hubble * produced_energy
    )
    assert_equal(
        "omitting pressure changes Hubble-square drift",
        missing_pressure_energy_dot == produced_energy_dot,
        False,
    )

    missing_stress_pressure = Fraction(1, 75)
    omitted_divergence = -production_source
    gravitational_response_dot = Fraction(1, 3000)
    full_minus_retained_hubble_drift = (
        friedmann_coefficient
        * (
            omitted_divergence
            - (d - 1) * hubble * (missing_stress_density + missing_stress_pressure)
        )
        + gravitational_response_dot
    )
    drift_error_budget = (
        friedmann_coefficient
        * (
            abs(omitted_divergence)
            + (d - 1)
            * abs(hubble)
            * (density_budget + abs(missing_stress_pressure))
        )
        + abs(gravitational_response_dot)
    )
    no_divergence_budget = (
        friedmann_coefficient
        * (
            (d - 1)
            * abs(hubble)
            * (density_budget + abs(missing_stress_pressure))
        )
        + abs(gravitational_response_dot)
    )
    assert_equal(
        "omitted-stress divergence controls full-minus-retained drift",
        abs(full_minus_retained_hubble_drift) <= drift_error_budget,
        True,
    )
    assert_equal(
        "tautological diagonal residual underbudgets omitted-stress drift",
        abs(full_minus_retained_hubble_drift) <= no_divergence_budget,
        False,
    )

    number_density = Fraction(19, 60)
    number_source = Fraction(1, 30)
    assert_equal(
        "number density alone is not the Hubble-square source",
        friedmann_coefficient * number_density == retained_delta_hubble_squared,
        False,
    )
    assert_equal(
        "number source alone is not the stress-energy source",
        number_source == production_source,
        False,
    )

    assert_equal(
        "retained mean response is not the full backreaction coordinate",
        retained_delta_hubble_squared == full_delta_hubble_squared,
        False,
    )


def check_spacetime_smeared_stress_noise_response() -> None:
    time_width = Fraction(5)
    physical_cell_volume = Fraction(8)
    local_noise_density = Fraction(3)

    normalized_cell_variance = local_noise_density / (
        time_width * physical_cell_volume
    )
    assert_equal(
        "normalized spacetime cell stress-noise variance",
        normalized_cell_variance,
        Fraction(3, 40),
    )

    shorter_time_width = Fraction(5, 2)
    shorter_time_variance = local_noise_density / (
        shorter_time_width * physical_cell_volume
    )
    assert_equal(
        "shorter time smearing increases variance",
        shorter_time_variance,
        2 * normalized_cell_variance,
    )

    larger_cell_volume = Fraction(32)
    larger_cell_variance = local_noise_density / (
        time_width * larger_cell_volume
    )
    assert_equal(
        "larger normalized spatial cell suppresses density variance",
        larger_cell_variance,
        normalized_cell_variance / 4,
    )

    ultraviolet_cell_volume = Fraction(1, 64)
    pointlike_spatial_variance = local_noise_density / (
        time_width * ultraviolet_cell_volume
    )
    assert_equal(
        "pointlike spatial evaluation is not the finite cell diagnostic",
        pointlike_spatial_variance == normalized_cell_variance,
        False,
    )
    assert_equal(
        "pointlike spatial evaluation exceeds finite window",
        pointlike_spatial_variance <= Fraction(1, 20),
        False,
    )

    box_volume = Fraction(200)
    unnormalized_whole_slice_variance = local_noise_density * box_volume / time_width
    normalized_whole_slice_variance = local_noise_density / (time_width * box_volume)
    assert_equal(
        "normalized whole-box average has density variance",
        normalized_whole_slice_variance,
        Fraction(3, 1000),
    )
    assert_equal(
        "unnormalized whole-slice integral carries volume factor",
        unnormalized_whole_slice_variance == normalized_whole_slice_variance,
        False,
    )
    assert_equal(
        "unnormalized whole-slice variance grows with box volume",
        unnormalized_whole_slice_variance > normalized_cell_variance,
        True,
    )

    friedmann_coefficient = Fraction(1, 2)
    response_tail_weight = Fraction(1, 5)
    tail_variance = Fraction(1, 200)
    density_tail_covariance = Fraction(1, 400)
    retarded_metric_variance = (
        friedmann_coefficient * friedmann_coefficient * normalized_cell_variance
        + 2
        * friedmann_coefficient
        * response_tail_weight
        * density_tail_covariance
        + response_tail_weight * response_tail_weight * tail_variance
    )
    omitted_noise_budget = Fraction(1, 10000)
    total_metric_variance = retarded_metric_variance + omitted_noise_budget
    assert_equal(
        "retarded metric-noise pushforward",
        total_metric_variance,
        Fraction(391, 20000),
    )

    scalar_density_only_variance = (
        friedmann_coefficient * friedmann_coefficient * normalized_cell_variance
    )
    assert_equal(
        "density-only scalar noise misses retarded tail covariance",
        scalar_density_only_variance == total_metric_variance,
        False,
    )
    assert_equal(
        "mean-only metric estimate misses stress fluctuations",
        Fraction(0) == total_metric_variance,
        False,
    )

    window_tolerance_squared = Fraction(1, 50)
    deterministic_tolerance_squared = Fraction(1, 100)
    assert_equal(
        "retarded stress-noise budget fits declared metric window",
        total_metric_variance <= window_tolerance_squared,
        True,
    )
    assert_equal(
        "overoptimistic deterministic metric tolerance fails noise check",
        total_metric_variance <= deterministic_tolerance_squared,
        False,
    )


def main() -> None:
    check_conformal_cancellation()
    check_de_sitter_nu_values()
    check_de_sitter_frequency_coefficient()
    check_sudden_quench_bogoliubov()
    check_complex_bogoliubov_annihilator_matrix()
    check_adiabatic_riccati_power_law()
    check_finite_adiabatic_order_bookkeeping()
    check_detector_positive_type_finite_model()
    check_out_region_produced_stress_tensor()
    check_produced_stress_continuity_check()
    check_omitted_stress_conservation_defect()
    check_cosmological_backreaction_window()
    check_spacetime_smeared_stress_noise_response()
    print("Cosmological particle-creation convention checks passed.")


if __name__ == "__main__":
    main()
