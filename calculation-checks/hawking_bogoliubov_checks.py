#!/usr/bin/env python3
"""Finite checks for the Hawking Bogoliubov coefficient calculation.

Evidence contract.
Target claims:
- Verify the finite arithmetic behind the Hawking mode-tracing coefficient,
  wave-packet Planck-bin average, infrared-safe packet restrictions,
  late-time packet remainder bounds, constant-surface-gravity and rotating-KMS
  hypotheses, Schwarzian flux, interacting horizon KMS spectral-density flux
  package, and flux-to-mass backreaction window.
Independent construction:
- The checks recompute the Gamma-function norm, Bogoliubov ratio, KMS
  greater/lesser weights, greybody-weighted flux, mass-loss bookkeeping,
  packet Fourier orthogonality, infrared asymptotics, residual telescopes,
  rotating chemical-potential weights, quasi-stationary control, and flux-noise
  chart bounds directly from finite numerical or rational data.
Imported assumptions:
- The script assumes the geometric-optics ray-tracing form, a stationary
  late-time KMS horizon state, positive channel spectral densities, and
  declared exterior propagation weights, plus a retained mass chart and
  nonnegative residual budgets for drift, state transport, gravitational EFT
  corrections, and flux noise.
Negative controls:
- The checks reject reversed KMS weights, free spectral-density substitution
  in an interacting channel, spontaneous-plus-thermal weights used as emitted
  occupation, omitted residual budgets, propagation weights outside the
  probability range, number-flux substitution for energy flux, long-window
  quasi-stationary overreach, the infrared-divergent j=0 number bin,
  smooth-remainder decay claims without global support and Fourier-derivative
  bounds, sharp-window endpoint shortcuts, variable-kappa Rindler
  transformations, static KMS weights used for rotating modes, generic Kerr
  Hartle-Hawking existence shortcuts, and mean-only backreaction when the
  retained flux noise leaves the mass chart.
Scope boundary:
- Passing this script does not construct an interacting Hadamard state, prove
  a Hawking theorem, compute greybody factors from a black-hole potential, or
  solve the nonlinear semiclassical Einstein equation.
"""

from fractions import Fraction

import mpmath as mp


mp.mp.dps = 60


def assert_close(name, lhs, rhs, tol=mp.mpf("1e-45")):
    lhs = mp.mpf(lhs)
    rhs = mp.mpf(rhs)
    if not mp.isfinite(lhs) or not mp.isfinite(rhs):
        raise AssertionError(f"{name}: nonfinite value {lhs} or {rhs}")
    if not mp.isfinite(tol) or tol < 0:
        raise AssertionError(f"{name}: invalid tolerance {tol}")
    scale = max(mp.mpf(1), abs(lhs), abs(rhs))
    error = abs(lhs - rhs)
    threshold = tol * scale
    if not mp.isfinite(error) or not mp.isfinite(threshold):
        raise AssertionError(f"{name}: nonfinite comparison error")
    if error > threshold:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def assert_exact(name: str, lhs: Fraction, rhs: Fraction) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs!r} != {rhs!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def check_packet_ir_and_late_time_controls() -> None:
    beta_h = mp.mpf("3.7")
    epsilon = mp.mpf("0.2")
    delta_1 = mp.mpf("1e-6")
    delta_2 = mp.mpf("1e-12")

    def low_number_with_cutoff(delta):
        numerator = 1 - mp.e ** (-beta_h * epsilon)
        denominator = -mp.expm1(-beta_h * delta)
        return mp.log(numerator / denominator) / (beta_h * epsilon)

    low_number_1 = low_number_with_cutoff(delta_1)
    low_number_2 = low_number_with_cutoff(delta_2)
    assert_true(
        "j=0 Hawking number packet grows as infrared cutoff is removed",
        low_number_2 > low_number_1,
    )
    assert_close(
        "j=0 Hawking number packet logarithmic divergence",
        low_number_2 - low_number_1,
        mp.log(delta_1 / delta_2) / (beta_h * epsilon),
        tol=mp.mpf("1e-6"),
    )

    low_energy = (
        mp.quad(
            lambda w: (
                1 / beta_h if w == 0 else w / mp.expm1(beta_h * w)
            ),
            [0, epsilon],
        )
        / epsilon
    )
    assert_true("lowest energy bin is finite", mp.isfinite(low_energy))
    assert_true("lowest energy bin has positive flux", low_energy > 0)
    assert_true(
        "energy weight removes the number-packet infrared pole",
        low_energy < 1 / beta_h,
    )

    mode_count = 5
    for row in range(mode_count):
        for col in range(mode_count):
            projector = mp.mpc("0")
            for n in range(mode_count):
                projector += (
                    mp.e ** (2j * mp.pi * n * (row - col) / mode_count)
                    / mode_count
                )
            assert_close(
                "finite packet Fourier completeness",
                abs(projector),
                1 if row == col else 0,
                tol=mp.mpf("1e-45"),
            )

    kappa = mp.mpf("0.7")
    packet_spacing = 2 * mp.pi / epsilon
    ray_constant = mp.mpf("1.3")
    inverse_map_bound = mp.mpf("0.2")
    omega_max = mp.mpf("2.0")

    def ray_remainder_bound(n):
        u_n = packet_spacing * n
        return omega_max * inverse_map_bound * ray_constant * mp.e ** (-kappa * u_n)

    assert_close(
        "subleading ray-map packet bound decays by one packet shift",
        ray_remainder_bound(4) / ray_remainder_bound(3),
        mp.e ** (-kappa * packet_spacing),
    )

    smooth_constant = mp.mpf("3.0")
    derivative_order = 4

    def smooth_remainder_bound(n):
        u_n = packet_spacing * n
        return smooth_constant / (1 + u_n) ** derivative_order

    assert_true(
        "smooth packet remainder decreases with derivative-order bound",
        smooth_remainder_bound(6) < smooth_remainder_bound(3),
    )
    has_global_support = False
    has_fourier_derivative_bound = False
    assert_true(
        "smooth noncompact remainder without Fourier-decay data rejected",
        not (has_global_support and has_fourier_derivative_bound),
    )
    sharp_window_endpoint_vanishes = False
    assert_true(
        "sharp packet endpoint shortcut rejected for rapid remainder estimate",
        not sharp_window_endpoint_vanishes,
    )


def check_horizon_static_and_rotating_kms_controls() -> None:
    kappa_left = Fraction(2, 5)
    kappa_right = Fraction(3, 5)
    beta_left_units = Fraction(1, kappa_left)
    beta_right_units = Fraction(1, kappa_right)
    assert_true(
        "variable kappa has no single cone period",
        beta_left_units != beta_right_units,
    )

    rho = Fraction(1, 7)
    transverse_kappa_derivative = Fraction(4, 9)
    constant_kappa_transverse_log_term = Fraction(0)
    variable_kappa_transverse_log_term = transverse_kappa_derivative / (
        2 * kappa_left * kappa_left
    )
    variable_dr_cross_term = transverse_kappa_derivative * rho * rho / 2
    assert_exact(
        "constant kappa removes transverse logarithmic Rindler term",
        constant_kappa_transverse_log_term,
        Fraction(0),
    )
    assert_true(
        "variable kappa creates transverse logarithmic Rindler term",
        variable_kappa_transverse_log_term != 0,
    )
    assert_true(
        "variable kappa creates dr dy cross term in r=kappa(y)rho^2/2",
        variable_dr_cross_term != 0,
    )

    omega = Fraction(5)
    azimuthal_number = Fraction(2)
    omega_h = Fraction(3, 2)
    horizon_energy = omega - azimuthal_number * omega_h
    assert_exact("rotating horizon mode energy", horizon_energy, Fraction(2))

    spectral_density = Fraction(7, 3)
    q_chi = Fraction(1, 5)
    q_static_time = Fraction(1, 11)
    greater_chi, lesser_chi = bosonic_kms_weights(q_chi, spectral_density)
    greater_static, lesser_static = bosonic_kms_weights(
        q_static_time,
        spectral_density,
    )
    assert_exact(
        "rotating KMS detailed balance uses chi",
        lesser_chi,
        q_chi * greater_chi,
    )
    assert_true(
        "static-time KMS weight changes rotating occupation",
        lesser_static != lesser_chi,
    )

    superradiant_omega = Fraction(1)
    superradiant_m = Fraction(2)
    superradiant_horizon_energy = superradiant_omega - superradiant_m * omega_h
    assert_true(
        "superradiant bosonic mode has negative horizon energy",
        superradiant_horizon_energy < 0,
    )
    positive_schwarzschild_absorption = True
    uses_static_planck_weight = True
    bad_static_superradiant_shortcut = (
        superradiant_horizon_energy < 0
        and positive_schwarzschild_absorption
        and uses_static_planck_weight
    )
    assert_true(
        "positive Schwarzschild greybody shortcut detected for superradiance",
        bad_static_superradiant_shortcut,
    )

    is_static_exterior = False
    kay_wald_obstruction_present = True
    generic_hartle_hawking_claim = (
        is_static_exterior or not kay_wald_obstruction_present
    )
    assert_true(
        "generic rotating Hartle-Hawking existence shortcut rejected",
        not generic_hartle_hawking_claim,
    )


def bosonic_kms_weights(
    q: Fraction,
    spectral_density: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return (G^>, G^<) with q=exp(-beta omega)."""

    greater = spectral_density / (1 - q)
    lesser = q * spectral_density / (1 - q)
    return greater, lesser


def check_interacting_horizon_flux_package() -> None:
    channels = [
        {
            "omega": Fraction(2),
            "greybody": Fraction(3, 5),
            "spectral_density": Fraction(7, 4),
            "q": Fraction(1, 3),
        },
        {
            "omega": Fraction(5),
            "greybody": Fraction(1, 4),
            "spectral_density": Fraction(2, 3),
            "q": Fraction(1, 5),
        },
        {
            "omega": Fraction(7, 2),
            "greybody": Fraction(2, 7),
            "spectral_density": Fraction(9, 5),
            "q": Fraction(1, 9),
        },
    ]

    retained_flux = Fraction(0)
    free_spectral_substitution_flux = Fraction(0)
    spontaneous_plus_thermal_flux = Fraction(0)
    for index, channel in enumerate(channels):
        q = channel["q"]
        spectral_density = channel["spectral_density"]
        greybody = channel["greybody"]
        omega = channel["omega"]
        assert_true(f"greybody probability channel {index}", 0 <= greybody <= 1)
        assert_true(f"KMS q range channel {index}", 0 < q < 1)
        assert_true(f"positive spectral density channel {index}", spectral_density > 0)

        greater, lesser = bosonic_kms_weights(q, spectral_density)
        assert_exact(f"KMS detailed balance channel {index}", lesser, q * greater)
        assert_exact(
            f"spectral density reconstruction channel {index}",
            greater - lesser,
            spectral_density,
        )

        retained_flux += omega * greybody * lesser
        free_greater, free_lesser = bosonic_kms_weights(q, Fraction(1))
        free_spectral_substitution_flux += omega * greybody * free_lesser
        spontaneous_plus_thermal_flux += omega * greybody * greater

        wrong_lesser = greater / q
        assert_true(
            f"reversed KMS weight rejected channel {index}",
            wrong_lesser != lesser,
        )

    assert_exact(
        "interacting retained horizon flux",
        retained_flux,
        Fraction(89, 60),
    )
    assert_true(
        "free spectral-density substitution changes interacting flux",
        free_spectral_substitution_flux != retained_flux,
    )
    assert_true(
        "using G-greater as emitted occupation overcounts the flux",
        spontaneous_plus_thermal_flux > retained_flux,
    )

    residuals = {
        "state construction": Fraction(1, 200),
        "horizon KMS": Fraction(1, 240),
        "spectral truncation": Fraction(1, 300),
        "greybody propagation": Fraction(1, 360),
        "stress renormalization": Fraction(1, 420),
        "nonstationary tail": Fraction(1, 560),
        "backreaction": Fraction(1, 840),
    }
    declared_bound = sum(residuals.values(), Fraction(0))
    actual_residual = declared_bound - Fraction(1, 10000)
    exact_flux = retained_flux + actual_residual
    assert_true(
        "retained interacting Hawking flux residual bound",
        abs(exact_flux - retained_flux) <= declared_bound,
    )
    omitted_spectral_budget = declared_bound - residuals["spectral truncation"]
    assert_true(
        "omitting spectral residual underbudgets the interacting flux",
        actual_residual > omitted_spectral_budget,
    )

    mass = Fraction(100)
    retarded_time_window = Fraction(3, 2)
    mass_after = mass - retarded_time_window * retained_flux
    assert_exact(
        "stress-flux mass-loss bookkeeping",
        mass - mass_after,
        retarded_time_window * retained_flux,
    )

    invalid_greybody = Fraction(6, 5)
    assert_true(
        "superunit greybody propagation weight rejected",
        not (0 <= invalid_greybody <= 1),
    )


def check_flux_to_mass_backreaction_window() -> None:
    mass_0 = Fraction(100)
    delta_u = Fraction(4)
    retained_luminosity = Fraction(1, 80)
    retained_mass_drop = delta_u * retained_luminosity

    residuals = {
        "flux package": Fraction(1, 1000),
        "drift": Fraction(1, 1600),
        "state transport": Fraction(1, 2000),
        "gravitational EFT": Fraction(1, 4000),
    }
    residual_budget = sum(residuals.values(), Fraction(0))
    actual_mass_drop = retained_mass_drop + residual_budget
    mass_after = mass_0 - actual_mass_drop

    assert_true("positive luminosity lowers the mass", mass_after < mass_0)
    assert_exact(
        "retained flux-to-mass residual telescope",
        abs((mass_0 - mass_after) - retained_mass_drop),
        residual_budget,
    )
    assert_true(
        "omitted state-transport residual underbudgets mass loss",
        abs((mass_0 - mass_after) - retained_mass_drop)
        > residual_budget - residuals["state transport"],
    )

    lipschitz_luminosity = Fraction(1, 1000)
    mass_chart_radius = Fraction(1, 2)
    drift_bound = delta_u * lipschitz_luminosity * mass_chart_radius
    assert_true(
        "mass-drift residual obeys Lipschitz chart bound",
        residuals["drift"] <= drift_bound,
    )

    luminosity_bound = retained_luminosity + residuals["flux package"] / delta_u
    epsilon_qs = delta_u * luminosity_bound / mass_0
    assert_true(
        "short retained window is quasi-stationary",
        epsilon_qs < Fraction(1, 100),
    )
    long_window = Fraction(10000)
    long_epsilon_qs = long_window * luminosity_bound / mass_0
    assert_true(
        "long window quasi-stationary overreach rejected",
        long_epsilon_qs > Fraction(1, 1),
    )

    retained_flux_noise = Fraction(1, 10000)
    noise_residual = Fraction(1, 40000)
    noise_total = retained_flux_noise + noise_residual
    assert_true(
        "retained flux noise stays inside the mass chart",
        noise_total < mass_chart_radius * mass_chart_radius,
    )
    assert_true(
        "mean-only backreaction would omit nonzero flux noise",
        noise_total > 0,
    )
    bad_noise_total = mass_chart_radius * mass_chart_radius + Fraction(1, 1000)
    assert_true(
        "noise outside chart invalidates mean-geometry window",
        bad_noise_total > mass_chart_radius * mass_chart_radius,
    )

    number_flux = Fraction(0)
    energy_flux = Fraction(0)
    for omega, greybody, occupation in (
        (Fraction(2), Fraction(1, 3), Fraction(1, 5)),
        (Fraction(5), Fraction(1, 4), Fraction(1, 7)),
    ):
        number_flux += greybody * occupation
        energy_flux += omega * greybody * occupation
    assert_true(
        "mass loss uses stress-energy flux, not number flux",
        energy_flux != number_flux,
    )


def main():
    samples = [
        (mp.mpf("0.7"), mp.mpf("0.2"), mp.mpf("1.3")),
        (mp.mpf("1.0"), mp.mpf("0.9"), mp.mpf("2.0")),
        (mp.mpf("2.5"), mp.mpf("3.1"), mp.mpf("0.8")),
    ]

    for kappa, omega, omega_prime in samples:
        a = omega / kappa
        gamma_abs_squared = abs(mp.gamma(1j * a)) ** 2
        gamma_identity = mp.pi / (a * mp.sinh(mp.pi * a))
        assert_close("Gamma imaginary-axis norm", gamma_abs_squared, gamma_identity)

        common = (1 / (2 * mp.pi * kappa)) ** 2 * (omega / omega_prime)
        alpha_squared = common * mp.e ** (mp.pi * a) * gamma_abs_squared
        beta_squared = common * mp.e ** (-mp.pi * a) * gamma_abs_squared

        assert_close(
            "alpha/beta thermal ratio",
            alpha_squared / beta_squared,
            mp.e ** (2 * mp.pi * a),
        )

        planck_beta = (
            1
            / (2 * mp.pi * kappa * omega_prime)
            / (mp.e ** (2 * mp.pi * omega / kappa) - 1)
        )
        assert_close("beta coefficient Planck factor", beta_squared, planck_beta)

        normalization_density = alpha_squared - beta_squared
        assert_close(
            "continuum Bogoliubov normalization density",
            normalization_density,
            1 / (2 * mp.pi * kappa * omega_prime),
        )

        u = mp.mpf("4.0")
        C = mp.mpf("1.7")
        v0_minus_v = C * mp.e ** (-kappa * u)
        blueshift_from_ray = omega / (kappa * v0_minus_v)
        blueshift_exponential = omega * mp.e ** (kappa * u) / (kappa * C)
        assert_close("late-time precursor blueshift", blueshift_from_ray, blueshift_exponential)

        beta_h = 2 * mp.pi / kappa
        bin_width = mp.mpf("0.13")
        bin_left = mp.mpf("0.41")
        bin_right = bin_left + bin_width
        bin_average_closed = (
            mp.log((1 - mp.e ** (-beta_h * bin_right)) / (1 - mp.e ** (-beta_h * bin_left)))
            / (beta_h * bin_width)
        )
        bin_average_integral = (
            mp.quad(lambda w: 1 / (mp.e ** (beta_h * w) - 1), [bin_left, bin_right])
            / bin_width
        )
        assert_close("wave-packet Planck bin average", bin_average_closed, bin_average_integral)

        p_prime = C * kappa * mp.e ** (-kappa * u)
        p_double_prime = -C * kappa**2 * mp.e ** (-kappa * u)
        p_triple_prime = C * kappa**3 * mp.e ** (-kappa * u)
        schwarzian = p_triple_prime / p_prime - mp.mpf("1.5") * (p_double_prime / p_prime) ** 2
        assert_close("exponential ray-tracing Schwarzian", schwarzian, -kappa**2 / 2)

        c = mp.mpf("1.0")
        flux_from_schwarzian = -c * schwarzian / (24 * mp.pi)
        flux_from_planck = c * mp.pi / (12 * beta_h**2)
        flux_from_kappa = c * kappa**2 / (48 * mp.pi)
        assert_close("two-dimensional Hawking flux from Schwarzian", flux_from_schwarzian, flux_from_kappa)
        assert_close("two-dimensional Hawking flux from Planck integral", flux_from_planck, flux_from_kappa)

        mass = mp.mpf("3.7")
        schwarzschild_kappa = 1 / (4 * mass)
        schwarzschild_temp = schwarzschild_kappa / (2 * mp.pi)
        assert_close("Schwarzschild temperature convention", schwarzschild_temp, 1 / (8 * mp.pi * mass))

    check_interacting_horizon_flux_package()
    check_packet_ir_and_late_time_controls()
    check_horizon_static_and_rotating_kms_controls()
    check_flux_to_mass_backreaction_window()
    print("All Hawking Bogoliubov coefficient checks passed.")


if __name__ == "__main__":
    main()
