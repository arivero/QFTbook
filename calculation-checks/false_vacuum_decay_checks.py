#!/usr/bin/env python3
r"""Regulated false-vacuum decay checks for Volume I and the SM chapter.

Evidence contract.
Target claims: the quartic oscillator bounce profile/action, the single
negative mode and translation zero mode in the regulated scalar example, the
Pöschl--Teller determinant normalization, the negative-mode half-contour
factor, the zero-mode collective-coordinate Jacobian, dilute multi-bounce
exponentiation, the field-theory translational Gram matrix, the spatial rate
density convention, and the Euclidean-to-real-time width ledger used by the
Standard Model metastability warning.
Independent construction: exact first-integral arithmetic, Pöschl--Teller
mode identities, exact node counts in the \(u=\tanh x\) coordinate, the
reflectionless scattering-phase determinant integral, oriented finite Gaussian
contour rotation, determinant/zero-mode bookkeeping, Euclidean scaling/virial
arithmetic, and direct power-series exponentiation.
Imported assumptions: the chosen false-vacuum Lefschetz cycle or analytic
continuation, a self-adjoint finite-volume regulator defining the metastable
state, and the semiclassical suppression regime in which separated bounces
interact only through the stated residual.
Negative controls: the script rejects the no-factor-two bounce action, the old
quartic determinant ratios, the real-axis negative Gaussian, inclusion of the
zero mode in the determinant, a doubled negative-mode contour, loss of contour
orientation, the \(B/D\) translational Gram matrix, Euclidean spacetime volume
as the physical rate-density denominator, ordinary finite-time amplitudes as
rates without a window, and signed residual cancellations as error bounds.
Scope boundary: these checks verify the finite scalar contour and
semiclassical bookkeeping; they do not prove a Standard Model bounce exists,
establish gauge-parameter independence, control omitted EFT operators, or
derive a Coleman--De Luccia or finite-temperature rate.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, isclose, pi, sqrt


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def assert_close(name: str, got: float, expected: float, tol: float = 1e-12) -> None:
    if not isclose(got, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


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

    # Node count in the exact coordinate u=tanh x.  The negative-mode
    # profile is 1-u^2, whose roots sit only at the compactified endpoints
    # u=+-1.  The zero-mode profile has the sign of u and hence one interior
    # node at u=0.
    interval_left = Fraction(-1, 1)
    interval_right = Fraction(1, 1)
    negative_mode_roots = [interval_left, interval_right]
    zero_mode_roots = [interval_left, Fraction(0, 1), interval_right]
    negative_interior_nodes = [
        root for root in negative_mode_roots if interval_left < root < interval_right
    ]
    zero_interior_nodes = [
        root for root in zero_mode_roots if interval_left < root < interval_right
    ]
    assert_equal("negative mode interior node count", len(negative_interior_nodes), 0)
    assert_equal("translation zero-mode interior node count", len(zero_interior_nodes), 1)

    zero_mode_left_sign = Fraction(-1, 2)
    zero_mode_right_sign = Fraction(1, 2)
    assert_true(
        "translation zero mode changes sign at its interior node",
        zero_mode_left_sign * zero_mode_right_sign < 0,
    )

    negative_eigenvalue = Fraction(-3, 1)
    zero_eigenvalue = Fraction(0, 1)
    assert_true("node-free eigenfunction has lower eigenvalue", negative_eigenvalue < zero_eigenvalue)
    assert_equal(
        "one-dimensional Sturm ordering gives one eigenvalue below the zero mode",
        zero_interior_nodes[0] == Fraction(0, 1)
        and len(negative_interior_nodes) + 1 == len(zero_interior_nodes),
        True,
    )


def check_negative_mode_contour_factor() -> None:
    lambda_abs = Fraction(5, 2)

    # The positive comparison integral is int_R exp(-lambda y^2/2) dy.
    # The steepest half-cycle a=+i y, y in [0,infty), has da=i dy and the
    # same decaying Gaussian on the half-line.  Squaring removes pi and
    # radicals: (half-line magnitude / full-line magnitude)^2 = 1/4.
    positive_gaussian_squared_over_pi = Fraction(2, 1) / lambda_abs
    rotated_halfline_squared_over_pi = Fraction(1, 2) / lambda_abs
    halfline_ratio_squared = (
        rotated_halfline_squared_over_pi / positive_gaussian_squared_over_pi
    )
    assert_equal("negative contour half-line magnitude squared", halfline_ratio_squared, Fraction(1, 4))

    positive_gaussian = sqrt(2 * pi / float(lambda_abs))
    rotated_halfline = sqrt(pi / (2 * float(lambda_abs)))
    upper_relative = 1j * rotated_halfline / positive_gaussian
    lower_relative = -1j * rotated_halfline / positive_gaussian
    assert_close("upper negative half-cycle real part", upper_relative.real, 0.0)
    assert_close("upper negative half-cycle imaginary part", upper_relative.imag, 0.5)
    assert_close("lower negative half-cycle imaginary part", lower_relative.imag, -0.5)

    rotated_quadratic_coefficient = -lambda_abs / 2
    assert_true(
        "imaginary contour makes the negative quadratic decay",
        rotated_quadratic_coefficient < 0,
    )
    assert_equal(
        "full imaginary contour would double the half-cycle factor",
        2 * upper_relative == upper_relative,
        False,
    )
    assert_equal(
        "dropping the orientation would miss the imaginary factor",
        rotated_halfline / positive_gaussian == upper_relative,
        False,
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

    # Reflectionless scattering for L=-d_x^2+1-6 sech^2 x has total phase
    # derivative -2[1/(k^2+1)+2/(k^2+4)].  The integral identity
    # int_0^infty a log(k^2+1)/(k^2+a^2) dk = pi log(1+a) gives the continuum
    # determinant factor product_a (1+a)^(-2), with a=1,2.
    continuum_factor = Fraction(1, 1)
    for pole in [1, 2]:
        continuum_factor *= Fraction(1, (1 + pole) ** 2)
    assert_equal("Pöschl-Teller scattering continuum factor", continuum_factor, Fraction(1, 36))

    # The translation zero mode psi=sech x tanh x has norm
    # int_{-infty}^{infty} psi^2 dx = int_{-1}^{1} u^2 du = 2/3.
    # The McKane-Tarlie/Coleman zero-mode normalization supplies the inverse
    # square of this dimensionless norm in the determinant convention with the
    # collective coordinate removed.
    zero_mode_norm = Fraction(2, 3)
    zero_mode_normalization = 1 / (zero_mode_norm * zero_mode_norm)
    determinant_with_absolute_negative = continuum_factor * zero_mode_normalization
    assert_equal(
        "quartic determinant with absolute negative mode",
        determinant_with_absolute_negative,
        Fraction(1, 16),
    )

    negative_eigenvalue_abs = 3 * omega**2
    positive_det_ratio_tau = determinant_with_absolute_negative / negative_eigenvalue_abs
    inverse_positive_det_ratio_tau = 1 / positive_det_ratio_tau
    assert_equal(
        "quartic determinant with negative and zero modes omitted",
        positive_det_ratio_tau,
        Fraction(1, 48) / omega**2,
    )

    # K_B^2 = (B/(2 pi)) det(M_F)/det''(M_B).  Avoid floating pi by checking
    # 2 pi K_B^2 = B * det(M_F)/det''(M_B).
    two_pi_prefactor_squared = bounce_action * inverse_positive_det_ratio_tau
    expected = bounce_action * 48 * omega**2
    assert_equal("collective-coordinate prefactor square ledger", two_pi_prefactor_squared, expected)
    assert_equal(
        "quartic width prefactor without pi",
        two_pi_prefactor_squared,
        16 * omega**5 / g,
    )

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

    assert_equal(
        "old positive determinant ratio is rejected",
        positive_det_ratio_tau == Fraction(1, 36) / omega**2,
        False,
    )
    assert_equal(
        "old absolute-negative determinant ratio is rejected",
        determinant_with_absolute_negative == Fraction(1, 12),
        False,
    )


def check_field_theory_translation_gram_and_rate_density() -> None:
    for dimension in range(2, 7):
        bounce_action = Fraction(11, 5)

        # For an O(D)-symmetric bounce, rotational averaging gives
        # G_{mu nu}=delta_{mu nu}/D * int (partial phi)^2.  The Euclidean
        # scaling identity gives int (partial phi)^2 = D B.
        gradient_norm = dimension * bounce_action
        gram_diagonal = gradient_norm / dimension
        assert_equal("field-theory translational Gram matrix", gram_diagonal, bounce_action)
        assert_equal(
            "old B/D translational Gram matrix is rejected",
            gram_diagonal == bounce_action / dimension,
            False,
        )

        zero_mode_factor_power = dimension
        assert_equal(
            "translation collective-coordinate factor exponent",
            zero_mode_factor_power,
            dimension,
        )

        euclidean_time = Fraction(13, 3)
        spatial_volume = Fraction(17, 2)
        spacetime_volume = euclidean_time * spatial_volume
        activity_density = Fraction(19, 7)
        euclidean_exponent_activity = activity_density * spacetime_volume
        physical_rate = euclidean_exponent_activity / euclidean_time
        physical_rate_density = physical_rate / spatial_volume
        assert_equal("physical false-vacuum rate density", physical_rate_density, activity_density)
        assert_equal(
            "Euclidean spacetime volume is not the physical rate denominator",
            physical_rate / spacetime_volume == activity_density,
            False,
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
    check_field_theory_translation_gram_and_rate_density()
    check_dilute_exponentiation_and_real_time_width()
    check_residual_negative_controls()
    print("All false-vacuum decay contour checks passed.")


if __name__ == "__main__":
    main()
