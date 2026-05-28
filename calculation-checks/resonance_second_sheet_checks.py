#!/usr/bin/env python3
"""Finite checks for the resonance second-sheet conventions.

The resonance chapter derives the threshold interval, the sign of the
one-loop self-energy discontinuity, the adjacent-sheet continuation, the
Breit--Wigner unitarity identity, and the narrow-pole Newton step.  This
script checks only the finite algebra and sign bookkeeping behind those
derivations.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def assert_true(condition, label):
    if not condition:
        raise AssertionError(label)


def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cabs2(z):
    return z[0] * z[0] + z[1] * z[1]


def check_threshold_interval():
    # Choose m_1^2=4 and s=25, so rho=sqrt(1-16/25)=3/5.
    rho = Fraction(3, 5)
    x_minus = (1 - rho) / 2
    x_plus = (1 + rho) / 2
    assert_equal(x_minus, Fraction(1, 5), "threshold x_minus")
    assert_equal(x_plus, Fraction(4, 5), "threshold x_plus")
    assert_equal(x_plus - x_minus, rho, "threshold interval length")


def check_self_energy_and_sheet_signs():
    rho = Fraction(3, 5)

    # In units of g^2/pi, the imaginary part of Sigma^R on the physical upper
    # edge is (-1/32) * (-1) * rho.
    im_sigma_upper = Fraction(-1, 32) * Fraction(-1, 1) * rho
    assert_equal(im_sigma_upper, Fraction(3, 160), "Im Sigma upper coefficient")

    im_f_upper = -im_sigma_upper
    assert_equal(im_f_upper, Fraction(-3, 160), "Im F upper coefficient")

    # The lower first-sheet boundary is the complex conjugate.  The adjacent
    # lower second-sheet boundary differs by the logarithmic discontinuity
    # -2 pi i over the interval, i.e. by -2 W in the denominator.
    im_f_lower_first = im_sigma_upper
    im_discontinuity_in_f = -2 * im_sigma_upper
    im_f_lower_second = im_f_lower_first + im_discontinuity_in_f
    assert_equal(im_f_lower_second, im_f_upper, "second-sheet lower sign")


def check_first_sheet_no_zero_signs():
    # For Im s > 0 and alpha > 0, 1 - alpha s has negative imaginary part,
    # while -s also has negative imaginary part.
    im_s = Fraction(1, 7)
    alpha = Fraction(1, 16)
    im_log_argument = -alpha * im_s
    im_minus_s = -im_s
    assert_true(im_log_argument < 0, "upper half-plane log argument sign")
    assert_true(im_minus_s < 0, "upper half-plane -s sign")

    im_s = Fraction(-1, 7)
    im_log_argument = -alpha * im_s
    im_minus_s = -im_s
    assert_true(im_log_argument > 0, "lower half-plane log argument sign")
    assert_true(im_minus_s > 0, "lower half-plane -s sign")


def check_breit_wigner_unitarity():
    a = Fraction(3, 1)
    w = Fraction(4, 1)
    numerator = (a, w)
    denominator = (a, -w)
    assert_equal(cabs2(numerator), Fraction(25, 1), "Breit-Wigner numerator modulus")
    assert_equal(cabs2(denominator), Fraction(25, 1), "Breit-Wigner denominator modulus")


def check_energy_square_width_conversion():
    mass = Fraction(5, 1)
    width = Fraction(2, 1)
    energy = (mass, -width / 2)
    s_pole = cmul(energy, energy)
    expected = (mass * mass - width * width / 4, -mass * width)
    assert_equal(s_pole, expected, "s-plane pole from complex energy")


def check_narrow_pole_newton_step():
    # Let W_R = c eps^2 and write R_1=a eps^2, R_0=b eps^4.  To order eps^4,
    # the fixed-point equation delta=-i W_R + delta R_1 + R_0 gives
    # delta=-i c eps^2 + (b - i a c) eps^4.
    a = Fraction(7, 1)
    b = Fraction(11, 1)
    c = Fraction(5, 1)
    delta_eps2 = (Fraction(0), -c)
    correction_eps4 = cadd((b, Fraction(0)), cmul(delta_eps2, (a, Fraction(0))))
    assert_equal(correction_eps4, (b, -a * c), "Newton eps4 correction")

    # The leading term is therefore the pole quoted in the text.
    leading_delta = delta_eps2
    assert_equal(leading_delta, (Fraction(0), -c), "leading adjacent-sheet pole shift")


def check_partial_wave_bound_arithmetic():
    # With |S|<=1 and S_l=1+2 i rho a_l, the triangle inequality gives
    # |a_l| <= 1/rho.  A sample elastic point S=-1 saturates the bound.
    rho = Fraction(2, 3)
    s_minus_one = (Fraction(-2, 1), Fraction(0, 1))
    two_i_rho = (Fraction(0, 1), 2 * rho)
    # Divide by 2 i rho by multiplying by -i/(2 rho).
    a = cmul(s_minus_one, (Fraction(0, 1), -Fraction(1, 1) / (2 * rho)))
    assert_equal(a, (Fraction(0, 1), Fraction(3, 2)), "sample partial-wave amplitude")
    assert_equal(cabs2(a), Fraction(9, 4), "partial-wave bound saturation")
    assert_equal(Fraction(1, 1) / (rho * rho), Fraction(9, 4), "partial-wave bound square")


def main():
    check_threshold_interval()
    check_self_energy_and_sheet_signs()
    check_first_sheet_no_zero_signs()
    check_breit_wigner_unitarity()
    check_energy_square_width_conversion()
    check_narrow_pole_newton_step()
    check_partial_wave_bound_arithmetic()
    print("All resonance second-sheet checks passed.")


if __name__ == "__main__":
    main()
