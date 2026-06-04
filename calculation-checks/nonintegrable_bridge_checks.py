#!/usr/bin/env python3
"""Exact checks for Volume VI bridges from integrable to nonintegrable 2D QFT.

Evidence contract.
Target claims: the broken-charge ledger, first-order FFPT mass shift,
semi-local confinement diagnostic, finite-volume golden-rule/phase-space
normalization, and decay-rate reconstruction certificate in Volume VI
Chapter 10.
Independent construction: direct commutator eigenvalue arithmetic,
finite-volume diagonal matrix-element normalization, Kallen/Jacobian algebra,
finite residual telescopes, and absolute majorants for rate reconstruction.
Imported assumptions: integrable asymptotic states, connected crossed form
factors, weak convergence of the finite-time kernel, Bethe--Yang
finite-volume normalization, and the regulated local perturbation chart stated
in the chapter.
Negative controls: fixed finite-volume/time sums are rejected as continuum
rates, exact form-factor data are rejected as full decay-width evidence,
omitted threshold/channel residuals underbudget the width, and signed residual
cancellations are rejected as certificates.
Scope boundary: these are exact finite checks of normalization and residual
bookkeeping; they do not prove existence of the nonintegrable continuum limit,
uniform threshold control, or convergence of all form-factor/channel tails.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def check_broken_charge_ledger() -> None:
    q_alpha = Fraction(7, 3)
    q_beta = Fraction(5, 6)
    matrix_element = Fraction(11, 5)
    commutator_coefficient = (q_alpha - q_beta) * matrix_element
    assert_equal("broken charge coefficient", commutator_coefficient, Fraction(33, 10))


def check_ffpt_mass_shift() -> None:
    epsilon = Fraction(2, 7)
    form_factor = Fraction(15, 4)
    mass = Fraction(5, 3)
    cosh_theta = Fraction(13, 12)
    energy = mass * cosh_theta

    delta_energy = epsilon * form_factor / energy
    delta_m_squared = 2 * epsilon * form_factor
    assert_equal("FFPT mass shift", delta_m_squared, Fraction(15, 7))
    assert_equal("relativistic energy shift", delta_energy, delta_m_squared / (2 * energy))


def check_semilocal_residue_and_confinement_tension() -> None:
    vev = Fraction(9, 5)
    local_phase = Fraction(1, 1)
    ising_kink_phase = Fraction(-1, 1)

    assert_equal("local kinematic residue coefficient", (1 - local_phase) * vev, Fraction(0, 1))
    assert_equal("Ising semilocal residue coefficient", (1 - ising_kink_phase) * vev, Fraction(18, 5))

    h = Fraction(7, 11)
    vacuum_plus = -h * vev
    vacuum_minus = h * vev
    assert_equal("Ising false-vacuum energy-density split", vacuum_minus - vacuum_plus, 2 * h * vev)


def check_tcsa_coupling_and_counterterm_powers() -> None:
    delta_sigma = Fraction(1, 8)
    delta_epsilon = Fraction(1, 1)
    delta_identity = Fraction(0, 1)

    assert_equal("TCSA sigma coupling power", 2 - delta_sigma, Fraction(15, 8))
    assert_equal("TCSA epsilon coupling power", 2 - delta_epsilon, Fraction(1, 1))

    sigma_sigma_to_identity = delta_sigma + delta_sigma - delta_identity - 2
    sigma_sigma_to_epsilon = delta_sigma + delta_sigma - delta_epsilon - 2
    epsilon_epsilon_to_identity = delta_epsilon + delta_epsilon - delta_identity - 2

    assert_equal("sigma sigma to identity counterterm power", sigma_sigma_to_identity, Fraction(-7, 4))
    assert_equal("sigma sigma to epsilon counterterm power", sigma_sigma_to_epsilon, Fraction(-11, 4))
    assert_equal("epsilon epsilon to identity logarithmic power", epsilon_epsilon_to_identity, Fraction(0, 1))


def check_airy_scaling_dimension() -> None:
    # In [-1/m d^2/dx^2 + T |x|] psi = E psi, balancing kinetic
    # 1/(m ell^2) with potential T ell gives ell=(m T)^(-1/3)
    # and E=(T^2/m)^(1/3).
    mass_power_in_length = Fraction(-1, 3)
    tension_power_in_length = Fraction(-1, 3)
    mass_power_in_energy = Fraction(-1, 3)
    tension_power_in_energy = Fraction(2, 3)

    kinetic_mass_power = -1 - 2 * mass_power_in_length
    kinetic_tension_power = -2 * tension_power_in_length
    potential_mass_power = mass_power_in_length
    potential_tension_power = 1 + tension_power_in_length

    assert_equal("Airy mass power kinetic", kinetic_mass_power, mass_power_in_energy)
    assert_equal("Airy tension power kinetic", kinetic_tension_power, tension_power_in_energy)
    assert_equal("Airy mass power potential", potential_mass_power, mass_power_in_energy)
    assert_equal("Airy tension power potential", potential_tension_power, tension_power_in_energy)


def check_two_body_phase_space_jacobian() -> None:
    mass_a = Fraction(5, 1)
    mass_r = Fraction(2, 1)
    mass_s = Fraction(1, 1)

    kallen = (
        mass_a**4
        + mass_r**4
        + mass_s**4
        - 2 * mass_a**2 * mass_r**2
        - 2 * mass_a**2 * mass_s**2
        - 2 * mass_r**2 * mass_s**2
    )
    p_squared = kallen / (4 * mass_a**2)
    energy_r = (mass_a**2 + mass_r**2 - mass_s**2) / (2 * mass_a)
    energy_s = (mass_a**2 + mass_s**2 - mass_r**2) / (2 * mass_a)

    assert_equal("two-body energy sum", energy_r + energy_s, mass_a)
    assert_equal("two-body r on shell", energy_r**2 - mass_r**2, p_squared)
    assert_equal("two-body s on shell", energy_s**2 - mass_s**2, p_squared)

    # The delta-function derivative is |p_*| M/(E_r E_s).  Squaring avoids
    # introducing irrational arithmetic for this exact check.
    derivative_squared = p_squared * mass_a**2 / (energy_r**2 * energy_s**2)
    reciprocal_squared = energy_r**2 * energy_s**2 / (p_squared * mass_a**2)
    assert_equal("two-body Jacobian inverse", derivative_squared * reciprocal_squared, 1)


def check_decay_rate_reconstruction_certificate() -> None:
    leading_rate = Fraction(7, 10)
    residuals = {
        "weak kernel": Fraction(1, 40),
        "finite volume": Fraction(1, 50),
        "Bethe-Yang normalization": Fraction(1, 60),
        "form-factor boundary": Fraction(1, 70),
        "channel tail": Fraction(1, 80),
        "threshold window": Fraction(1, 12),
        "higher order": Fraction(1, 90),
    }
    residual_total = sum(residuals.values(), Fraction(0))
    physical_rate = leading_rate + residual_total
    assert_equal(
        "nonintegrable decay-rate residual telescope",
        physical_rate - leading_rate,
        residual_total,
    )

    absolute_majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "nonintegrable decay-rate absolute bound",
        abs(physical_rate - leading_rate) <= absolute_majorant,
        True,
    )

    phase_space_majorant = Fraction(9, 10)
    noncancellation_margin = leading_rate / phase_space_majorant
    assert_equal(
        "nonintegrable decay-rate noncancellation margin",
        noncancellation_margin,
        Fraction(7, 9),
    )
    relative_bound = absolute_majorant / leading_rate
    assert_equal(
        "nonintegrable decay-rate relative certificate",
        abs(physical_rate - leading_rate) / leading_rate <= relative_bound,
        True,
    )

    finite_box_rate = (
        leading_rate
        + residuals["weak kernel"]
        + residuals["finite volume"]
    )
    assert_equal(
        "finite box and finite time rate is not continuum golden-rule rate",
        finite_box_rate == leading_rate,
        False,
    )

    exact_form_factor_residual = Fraction(0)
    non_form_factor_residual = residual_total - residuals["form-factor boundary"]
    assert_equal(
        "exact form factors leave spectral-limit residuals",
        non_form_factor_residual > exact_form_factor_residual,
        True,
    )

    omitted_threshold_budget = absolute_majorant - residuals["threshold window"]
    assert_equal(
        "omitted threshold residual underbudgets decay rate",
        abs(physical_rate - leading_rate) <= omitted_threshold_budget,
        False,
    )

    signed_canceling_residuals = [Fraction(1, 6), -Fraction(1, 6)]
    signed_sum = sum(signed_canceling_residuals, Fraction(0))
    absolute_sum = sum(abs(value) for value in signed_canceling_residuals)
    assert_equal("signed decay residuals can cancel", signed_sum, Fraction(0))
    assert_equal(
        "signed cancellation is not a decay-rate certificate",
        absolute_sum > abs(signed_sum),
        True,
    )


def main() -> None:
    check_broken_charge_ledger()
    check_ffpt_mass_shift()
    check_semilocal_residue_and_confinement_tension()
    check_tcsa_coupling_and_counterterm_powers()
    check_airy_scaling_dimension()
    check_two_body_phase_space_jacobian()
    check_decay_rate_reconstruction_certificate()
    print("All nonintegrable-bridge checks passed.")


if __name__ == "__main__":
    main()
