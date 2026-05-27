#!/usr/bin/env python3
"""Exact checks for Volume VI bridges from integrable to nonintegrable 2D QFT."""

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


def main() -> None:
    check_broken_charge_ledger()
    check_ffpt_mass_shift()
    check_semilocal_residue_and_confinement_tension()
    check_tcsa_coupling_and_counterterm_powers()
    check_airy_scaling_dimension()
    print("All nonintegrable-bridge checks passed.")


if __name__ == "__main__":
    main()
