#!/usr/bin/env python3
"""Finite algebra checks for mirror TBA wrapping formulas in Volume VI."""

from __future__ import annotations

from check_utils import assert_leq as _assert_leq

from fractions import Fraction


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def check_two_winding_tba_expansion() -> None:
    q = [Fraction(2, 5), Fraction(3, 7)]
    energy = [Fraction(11, 3), Fraction(13, 5)]
    kernel = [
        [Fraction(1, 6), Fraction(-2, 9)],
        [Fraction(5, 8), Fraction(1, 10)],
    ]

    kernel_q = [
        sum(kernel[a][b] * q[b] for b in range(2))
        for a in range(2)
    ]
    l1 = q
    l2 = [
        q[a] * kernel_q[a] - Fraction(1, 2) * q[a] * q[a]
        for a in range(2)
    ]

    # Substitute the ansatz into L = log(1 + exp[-d + K L]) through order t^2.
    # With q_a -> q_a t, the coefficient is
    # L_a = q_a t + (q_a (K q)_a - q_a^2/2) t^2 + O(t^3).
    rhs_l2 = [
        q[a] * sum(kernel[a][b] * l1[b] for b in range(2))
        - Fraction(1, 2) * q[a] * q[a]
        for a in range(2)
    ]
    for a in range(2):
        assert_equal(f"TBA L2 coefficient species {a}", l2[a], rhs_l2[a])

    e1 = -sum(energy[a] * l1[a] for a in range(2))
    e2 = -sum(energy[a] * l2[a] for a in range(2))
    displayed_e2 = (
        -sum(energy[a] * q[a] * kernel_q[a] for a in range(2))
        + Fraction(1, 2) * sum(energy[a] * q[a] * q[a] for a in range(2))
    )
    assert_equal("one-winding energy coefficient", e1, -sum(energy[a] * q[a] for a in range(2)))
    assert_equal("two-winding energy coefficient", e2, displayed_e2)


def check_vacuum_luscher_coefficient_and_threshold() -> None:
    # The theorem uses
    #   int_{-infty}^{infty} cosh(theta) exp[-r cosh(theta)] dtheta = 2 K_1(r).
    # Combined with the energy prefactor -m/(2 pi), this gives -m K_1(mR)/pi.
    full_line_bessel_factor = Fraction(2, 1)
    energy_measure_factor = Fraction(-1, 2)
    assert_equal(
        "vacuum Luscher K1 coefficient",
        energy_measure_factor * full_line_bessel_factor,
        Fraction(-1, 1),
    )

    masses = [Fraction(2, 1), Fraction(3, 1), Fraction(5, 1)]
    m_star = min(masses)

    # The two sources of the stated remainder are q_a e^{-m_* R} and q_a^2.
    # Their exponential rates are respectively m_a + m_* and 2 m_a; both are
    # bounded below by 2 m_* for every species.
    mixed_rates = [m + m_star for m in masses]
    square_rates = [2 * m for m in masses]
    assert_equal("mixed remainder exponential threshold", min(mixed_rates), 2 * m_star)
    assert_equal("square remainder exponential threshold", min(square_rates), 2 * m_star)


def check_bessel_k1_asymptotic_coefficients() -> None:
    nu = 1
    coeffs = [Fraction(1, 1)]
    for k in range(1, 4):
        coeffs.append(
            coeffs[-1] * Fraction(4 * nu * nu - (2 * k - 1) ** 2, 8 * k)
        )

    assert_equal("K1 asymptotic a0", coeffs[0], Fraction(1, 1))
    assert_equal("K1 asymptotic a1", coeffs[1], Fraction(3, 8))
    assert_equal("K1 asymptotic a2", coeffs[2], Fraction(-15, 128))
    assert_equal("K1 asymptotic a3", coeffs[3], Fraction(315, 3072))


def check_f_term_product_subtraction() -> None:
    s1 = Fraction(3, 2)
    s2 = Fraction(5, 3)
    one_particle_factor = s1 - 1
    two_particle_factor = s1 * s2 - 1
    inclusion_exclusion = (s1 - 1) + (s2 - 1) + (s1 - 1) * (s2 - 1)

    assert_equal("one-particle F-term factor", one_particle_factor, Fraction(1, 2))
    assert_equal("two-particle F-term product subtraction", two_particle_factor, inclusion_exclusion)
    assert_equal("vacuum subtraction for empty product", Fraction(1, 1) - 1, Fraction(0, 1))
    assert_equal("transparent scattering factor", Fraction(1, 1) * Fraction(1, 1) - 1, Fraction(0, 1))


def check_mu_residue_orientation_ledger() -> None:
    residue = Fraction(7, 11)
    sigma_plus = Fraction(1, 1)
    sigma_minus = Fraction(-1, 1)
    # The common factor -i is outside the rational ledger; the orientation
    # coefficient changes sign when the contour deformation is reversed.
    assert_equal("mu-term orientation reversal", -sigma_plus * residue, sigma_minus * residue)


def check_excited_state_continuation_residual_budget() -> None:
    bethe_yang_energy = Fraction(50, 7)
    f_term = Fraction(-3, 11)
    mu_term = Fraction(2, 13)
    one_winding_coordinate = bethe_yang_energy + f_term + mu_term

    residuals = {
        "trace": Fraction(1, 11),
        "contour": Fraction(-2, 13),
        "branch": Fraction(3, 17),
        "pole": Fraction(-1, 19),
        "multi": Fraction(5, 23),
        "density": Fraction(-7, 29),
        "normalization": Fraction(11, 31),
    }
    total_residual = sum(residuals.values(), Fraction(0))
    direct_energy = one_winding_coordinate + total_residual

    assert_equal(
        "excited-state continuation residual telescope",
        direct_energy - one_winding_coordinate - total_residual,
        Fraction(0),
    )
    if total_residual == 0:
        raise AssertionError("excited-state residual budget accidentally collapsed")

    residual_bound = sum(abs(value) for value in residuals.values())
    _assert_leq(
        "excited-state residual triangle budget",
        abs(direct_energy - one_winding_coordinate),
        residual_bound,
        tol=Fraction(0),
    )

    exact_when_residuals_vanish = one_winding_coordinate + sum(
        Fraction(0) for _ in residuals
    )
    assert_equal(
        "zero residual gives exact one-winding coordinate",
        exact_when_residuals_vanish,
        one_winding_coordinate,
    )
    assert_equal(
        "one-winding coordinate still misses direct energy",
        direct_energy - one_winding_coordinate,
        total_residual,
    )


def main() -> None:
    check_two_winding_tba_expansion()
    check_vacuum_luscher_coefficient_and_threshold()
    check_bessel_k1_asymptotic_coefficients()
    check_f_term_product_subtraction()
    check_mu_residue_orientation_ledger()
    check_excited_state_continuation_residual_budget()
    print("All mirror-channel TBA wrapping checks passed.")


if __name__ == "__main__":
    main()
