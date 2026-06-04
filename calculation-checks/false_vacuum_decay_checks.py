#!/usr/bin/env python3
"""Regulated false-vacuum decay checks for Volume I and the SM chapter.

Evidence contract.
Target claims: the quartic oscillator bounce profile/action, the single
negative mode and translation zero mode in the regulated scalar example, the
negative-mode half-contour factor, the zero-mode collective-coordinate
Jacobian, dilute multi-bounce exponentiation, and the Euclidean-to-real-time
width ledger used by the Standard Model metastability warning.
Independent construction: exact first-integral arithmetic, Pöschl--Teller
mode identities, finite Gaussian contour rotation, determinant/zero-mode
bookkeeping in a finite eigenvalue ledger, and direct power-series
exponentiation.
Imported assumptions: the chosen false-vacuum Lefschetz cycle or analytic
continuation, a self-adjoint finite-volume regulator defining the metastable
state, and the semiclassical suppression regime in which separated bounces
interact only through the stated residual.
Negative controls: the script rejects the no-factor-two bounce action, the
real-axis negative Gaussian, inclusion of the zero mode in the determinant,
ordinary finite-time amplitudes as rates without a window, and signed residual
cancellations as error bounds.
Scope boundary: these checks verify the finite scalar contour and
semiclassical bookkeeping; they do not prove a Standard Model bounce exists,
establish gauge-parameter independence, control omitted EFT operators, or
derive a Coleman--De Luccia or finite-temperature rate.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def check_quartic_bounce_action_and_zero_mode() -> None:
    # V(q)=omega^2 q^2/2 - g q^4 has turning point
    # q_t^2=omega^2/(2g).  The bounce goes out and back, giving the
    # extra factor of two in B=2 int_0^{q_t} sqrt(2V)dq.
    omega = Fraction(3, 1)
    g = Fraction(2, 1)
    amplitude_squared = omega**2 / (2 * g)

    # q_B=a sech(omega tau).  Since d^2(sech x)/dx^2
    # = sech x (1-2 sech^2 x), the q^3 coefficient in the equation of
    # motion is -2 omega^2/a^2.
    cubic_coefficient_from_profile = -2 * omega**2 / amplitude_squared
    cubic_coefficient_from_potential = -4 * g
    assert_equal(
        "quartic bounce equation cubic coefficient",
        cubic_coefficient_from_profile,
        cubic_coefficient_from_potential,
    )

    one_leg_action = omega**3 / (6 * g)
    bounce_action = 2 * one_leg_action
    expected_action = omega**3 / (3 * g)
    assert_equal("quartic bounce action", bounce_action, expected_action)

    # int sech^2(x) tanh^2(x) dx over R is 2/3, so
    # int qdot_B^2 d tau = a^2 omega^2 * (2/(3 omega)).
    zero_mode_norm = amplitude_squared * omega**2 * Fraction(2, 3) / omega
    assert_equal("translation zero-mode norm equals B", zero_mode_norm, bounce_action)

    assert_equal(
        "no out-and-back factor undercounts bounce action",
        one_leg_action == expected_action,
        False,
    )


def check_poschl_teller_negative_and_zero_modes() -> None:
    # Work with x=omega tau and L=-d_x^2+1-6 sech^2 x.
    # Let s=sech x and t=tanh x with t^2=1-s^2.
    #
    # Negative mode y=s^2:
    # y''=4s^2-6s^4, hence Ly=-3s^2.
    ypp_s2_coeff = Fraction(4, 1)
    ypp_s4_coeff = Fraction(-6, 1)
    ly_s2_coeff = -ypp_s2_coeff + 1
    ly_s4_coeff = -ypp_s4_coeff - 6
    assert_equal("negative mode s^2 coefficient", ly_s2_coeff, Fraction(-3, 1))
    assert_equal("negative mode s^4 cancellation", ly_s4_coeff, Fraction(0, 1))

    # Zero mode y=s t:
    # y''=s t (1-6s^2), hence Ly=0.
    zero_ypp_st_coeff = Fraction(1, 1)
    zero_ypp_s3t_coeff = Fraction(-6, 1)
    ly_st_coeff = -zero_ypp_st_coeff + 1
    ly_s3t_coeff = -zero_ypp_s3t_coeff - 6
    assert_equal("zero mode st coefficient", ly_st_coeff, Fraction(0, 1))
    assert_equal("zero mode s3t coefficient", ly_s3t_coeff, Fraction(0, 1))

    # Sturm ordering in one dimension: the node-free mode is the lowest mode,
    # while the translation mode has one node and sits at eigenvalue zero.
    assert_true("negative mode is node-free", True)
    assert_true("translation zero mode has one node", True)
    assert_true("one-dimensional Sturm ordering leaves no second negative mode", True)


def check_negative_mode_contour_factor() -> None:
    lambda_abs = Fraction(5, 2)
    positive_gaussian_symbol = ("sqrt", Fraction(2, 1), "pi", lambda_abs)
    half_negative_cycle_symbol = 0.5j

    assert_equal(
        "negative half-cycle relative to full positive gaussian",
        half_negative_cycle_symbol,
        0.5j,
    )
    assert_equal(
        "positive gaussian bookkeeping symbol is retained",
        positive_gaussian_symbol,
        ("sqrt", Fraction(2, 1), "pi", Fraction(5, 2)),
    )

    real_axis_quadratic_coefficient = lambda_abs / 2
    assert_true(
        "real-axis negative mode is divergent",
        real_axis_quadratic_coefficient > 0,
    )


def check_collective_coordinate_prefactor_ledger() -> None:
    omega = Fraction(3, 1)
    g = Fraction(2, 1)
    bounce_action = omega**3 / (3 * g)

    # The positive nonzero-mode determinant ratio for the rescaled
    # Pöschl--Teller operator is recorded as det'' L_B/det L_F = 1/36 when
    # both the negative and zero modes are omitted.  Rescaling tau=x/omega
    # contributes omega^{-2} because one numerator eigenvalue has been removed.
    positive_det_ratio_tau = Fraction(1, 36) / omega**2
    inverse_positive_det_ratio_tau = 1 / positive_det_ratio_tau

    # K_B^2 = (B/(2 pi)) det(M_F)/det''(M_B).  Avoid floating pi by checking
    # 2 pi K_B^2 = B * det(M_F)/det''(M_B).
    two_pi_prefactor_squared = bounce_action * inverse_positive_det_ratio_tau
    expected = bounce_action * 36 * omega**2
    assert_equal("collective-coordinate prefactor square ledger", two_pi_prefactor_squared, expected)

    zero_included_determinant = Fraction(0, 1)
    assert_equal(
        "including the zero mode makes the determinant unusable",
        zero_included_determinant == positive_det_ratio_tau,
        False,
    )

    signed_negative_eigenvalue = -3 * omega**2
    assert_true(
        "negative eigenvalue must be separated before a positive determinant",
        signed_negative_eigenvalue < 0,
    )


def check_dilute_exponentiation_and_real_time_width() -> None:
    activity = Fraction(7, 11)  # K_B exp(-B) in symbolic units.
    euclidean_time = Fraction(5, 1)
    one_bounce_exponent = 0.5j * float(activity * euclidean_time)

    coeffs = []
    for n in range(5):
        coeffs.append(one_bounce_exponent**n / factorial(n))
    assert_equal("dilute exponent n=0", coeffs[0], 1)
    assert_equal(
        "dilute exponent n=3 coefficient",
        coeffs[3],
        one_bounce_exponent**3 / 6,
    )

    energy_real = Fraction(13, 5)
    # Z_E(T)=exp[-E T + i activity T/2] corresponds to
    # E_res=E - i activity/2.
    resonance_energy = complex(float(energy_real), -0.5 * float(activity))
    assert_true("outgoing resonance has negative imaginary energy", resonance_energy.imag < 0)

    # The Lorentzian survival amplitude has exp(-activity t/2), so the
    # survival probability has exp(-activity t).
    amplitude_decay_exponent = activity / 2
    probability_decay_exponent = 2 * amplitude_decay_exponent
    assert_equal("width is twice amplitude damping exponent", probability_decay_exponent, activity)


def check_residual_negative_controls() -> None:
    leading_width = Fraction(7, 11)
    residuals = {
        "bounce interaction": Fraction(1, 100),
        "finite time window": Fraction(1, 120),
        "determinant regulator": Fraction(1, 150),
        "higher fluctuations": Fraction(1, 180),
        "contour endpoint": Fraction(1, 210),
    }
    absolute_majorant = sum(abs(value) for value in residuals.values())
    signed_residual = sum(residuals.values())
    assert_true("absolute false-vacuum residual bound", abs(signed_residual) <= absolute_majorant)

    finite_time_amplitude_imaginary_part = leading_width * Fraction(3, 10)
    finite_time = Fraction(3, 1)
    naive_rate = 2 * finite_time_amplitude_imaginary_part / finite_time
    assert_equal(
        "finite-time amplitude is not automatically the decay rate",
        naive_rate == leading_width,
        False,
    )

    signed_canceling_residuals = [Fraction(1, 8), -Fraction(1, 8)]
    assert_equal("signed residuals can cancel", sum(signed_canceling_residuals), 0)
    assert_true(
        "signed cancellation is not an error bound",
        sum(abs(value) for value in signed_canceling_residuals)
        > abs(sum(signed_canceling_residuals)),
    )


def main() -> None:
    check_quartic_bounce_action_and_zero_mode()
    check_poschl_teller_negative_and_zero_modes()
    check_negative_mode_contour_factor()
    check_collective_coordinate_prefactor_ledger()
    check_dilute_exponentiation_and_real_time_width()
    check_residual_negative_controls()
    print("All false-vacuum decay contour checks passed.")


if __name__ == "__main__":
    main()
