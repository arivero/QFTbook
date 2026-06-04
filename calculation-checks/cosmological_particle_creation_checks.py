#!/usr/bin/env python3
"""Exact convention checks for cosmological particle-creation formulas.

Evidence contract:
  independent construction: finite mode sums for Robertson-Walker particle
  diagnostics, stress-tensor source coordinates, pressure work, and Friedmann
  response coefficients;
  imported assumptions: the free scalar mode equation, adiabatic/asymptotic
  particle basis, and renormalized-stress subtraction scheme stated in the
  chapter;
  negative controls: wrong scale-factor powers, missing pressure work,
  treating ongoing production as a conserved fluid, and zero-particle source
  checks;
  scope boundary: these checks verify finite stress-source bookkeeping, not
  interacting cosmological QFT, full adiabatic subtraction, or nonlinear
  semiclassical existence.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


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


def check_produced_stress_continuity_certificate() -> None:
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


def main() -> None:
    check_conformal_cancellation()
    check_de_sitter_nu_values()
    check_de_sitter_frequency_coefficient()
    check_sudden_quench_bogoliubov()
    check_adiabatic_riccati_power_law()
    check_detector_positive_type_finite_model()
    check_out_region_produced_stress_tensor()
    check_produced_stress_continuity_certificate()
    print("Cosmological particle-creation convention checks passed.")


if __name__ == "__main__":
    main()
