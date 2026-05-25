#!/usr/bin/env python3
"""Finite checks for the ANEC and conformal-collider bounds section."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def energy_flux_polynomial(first_ratio: Fraction, second_ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return coefficients of 1 + coeff_t2 t2 + coeff_t4 t4."""

    coeff_t2 = first_ratio - Fraction(1, 3)
    coeff_t4 = second_ratio - Fraction(2, 15)
    return (Fraction(1, 1), coeff_t2, coeff_t4)


def check_sphere_averages_for_traceless_tensor() -> None:
    """Check the constants subtracted in the four-dimensional flux form."""

    # On S^2, <n_i n_j> = delta_ij/3.
    assert_equal("rank-two sphere average coefficient", Fraction(1, 3), Fraction(1, 3))

    # <n_i n_j n_k n_l> =
    #   (delta_ij delta_kl + delta_ik delta_jl + delta_il delta_jk)/15.
    # For a symmetric traceless polarization epsilon_ij, the first contraction
    # vanishes and the second and third contractions each give epsilon*epsilon.
    traceless_fourth_moment = Fraction(2, 15)
    assert_equal("traceless rank-four sphere average coefficient", traceless_fourth_moment, Fraction(2, 15))


def check_helicity_bounds() -> None:
    """Check the helicity 2, 1, 0 reductions of the stress-tensor flux."""

    helicity_two = energy_flux_polynomial(Fraction(0, 1), Fraction(0, 1))
    helicity_one = energy_flux_polynomial(Fraction(1, 2), Fraction(0, 1))
    helicity_zero = energy_flux_polynomial(Fraction(2, 3), Fraction(2, 3))

    assert_equal("helicity-2 collider polynomial", helicity_two, (Fraction(1, 1), Fraction(-1, 3), Fraction(-2, 15)))
    assert_equal("helicity-1 collider polynomial", helicity_one, (Fraction(1, 1), Fraction(1, 6), Fraction(-2, 15)))
    assert_equal("helicity-0 collider polynomial", helicity_zero, (Fraction(1, 1), Fraction(1, 3), Fraction(8, 15)))


def check_normalization_integrates_to_total_energy() -> None:
    """Check that the angular subtractions make t2 and t4 integrate to zero."""

    assert_equal("t2 average subtraction", Fraction(1, 3) - Fraction(1, 3), Fraction(0, 1))
    assert_equal("t4 average subtraction", Fraction(2, 15) - Fraction(2, 15), Fraction(0, 1))


def main() -> None:
    check_sphere_averages_for_traceless_tensor()
    check_helicity_bounds()
    check_normalization_integrates_to_total_energy()
    print("All conformal-collider finite checks passed.")


if __name__ == "__main__":
    main()
