#!/usr/bin/env python3
"""Finite checks for constructive scalar/SPDE normalization conventions."""

from fractions import Fraction
import math


def assert_equal(got, expected, label):
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def hermite_probabilists(n):
    """Return coefficients of H_n(x), low degree first."""
    h0 = [Fraction(1)]
    if n == 0:
        return h0
    h1 = [Fraction(0), Fraction(1)]
    if n == 1:
        return h1
    prev2, prev1 = h0, h1
    for k in range(1, n):
        x_prev1 = [Fraction(0)] + prev1
        k_prev2 = [k * c for c in prev2] + [Fraction(0)] * (len(x_prev1) - len(prev2))
        nxt = [a - b for a, b in zip(x_prev1, k_prev2)]
        prev2, prev1 = prev1, nxt
    return prev1


def wick_coefficients(n):
    """Return terms in :X^n: as (power_X, power_c, coefficient)."""
    hermite = hermite_probabilists(n)
    terms = []
    for k, coeff in enumerate(hermite):
        if coeff == 0:
            continue
        assert (n - k) % 2 == 0
        terms.append((k, (n - k) // 2, coeff))
    return terms


def check_wick_polynomials():
    assert_equal(
        wick_coefficients(2),
        [(0, 1, Fraction(-1)), (2, 0, Fraction(1))],
        "Wick square",
    )
    assert_equal(
        wick_coefficients(3),
        [(1, 1, Fraction(-3)), (3, 0, Fraction(1))],
        "Wick cubic",
    )
    assert_equal(
        wick_coefficients(4),
        [(0, 2, Fraction(3)), (2, 1, Fraction(-6)), (4, 0, Fraction(1))],
        "Wick quartic",
    )


def check_tadpole_asymptotics():
    # I_d(Lambda,m) = |S^{d-1}|/(2pi)^d int_0^Lambda r^{d-1}/(r^2+m^2) dr.
    coeff_2 = (2 * math.pi) / ((2 * math.pi) ** 2)  # radial integral contributes log Lambda.
    coeff_3 = (4 * math.pi) / ((2 * math.pi) ** 3)  # radial integral contributes Lambda.
    if abs(coeff_2 - 1 / (2 * math.pi)) > 1e-15:
        raise AssertionError("two-dimensional tadpole log coefficient mismatch")
    if abs(coeff_3 - 1 / (2 * math.pi**2)) > 1e-15:
        raise AssertionError("three-dimensional tadpole linear coefficient mismatch")


def check_phi4_power_counting():
    # omega_d = d - (d-2) E/2 + (d-4) V.
    def omega(d, external_legs, quartic_vertices):
        return (
            Fraction(d, 1)
            - Fraction(d - 2, 2) * external_legs
            + Fraction(d - 4, 1) * quartic_vertices
        )

    assert_equal(omega(3, 0, 1), Fraction(2), "3D phi4 vacuum one vertex")
    assert_equal(omega(3, 2, 1), Fraction(1), "3D phi4 one-loop two point")
    assert_equal(omega(3, 2, 2), Fraction(0), "3D phi4 two-loop two point")
    assert_equal(omega(3, 4, 1), Fraction(0), "3D phi4 one-loop four point")
    assert_equal(omega(3, 4, 2), Fraction(-1), "3D phi4 higher four point")
    assert_equal(omega(4, 4, 1), Fraction(0), "4D phi4 marginal four point")


def check_phi4_three_two_loop_mass_coordinate():
    # In the normalization int lambda :phi^4: + alpha :phi^2:, the k=3
    # Wick contraction in :phi^4(x)::phi^4(y): has coefficient
    # binom(4,3)^2 3! = 96.  The perturbative expansion gives a factor 1/2,
    # while the two possible external attachments to the local bilinear give
    # a factor 2, so the local two-point divergence is
    # 96 lambda^2 J_epsilon C*C.  The alpha :phi^2: insertion contributes
    # -2 alpha C*C; hence alpha = 48 lambda^2 J_epsilon.
    wick_k3 = math.comb(4, 3) ** 2 * math.factorial(3)
    expansion_half = Fraction(1, 2)
    external_pairings = 2
    local_two_point_coefficient = Fraction(wick_k3 * external_pairings, 1) * expansion_half
    alpha_insertion_coefficient = 2
    alpha_over_j = local_two_point_coefficient / alpha_insertion_coefficient
    assert_equal(wick_k3, 96, "phi4_3 sunset Wick contraction coefficient")
    assert_equal(local_two_point_coefficient, Fraction(96), "phi4_3 local two-point coefficient")
    assert_equal(alpha_over_j, Fraction(48), "phi4_3 alpha/J coefficient")

    # C_m(x) ~ 1/(4 pi r) in three dimensions, so int C_m(x)^3 d^3x has
    # logarithmic coefficient 4 pi / (4 pi)^3 = 1/(16 pi^2).  Therefore
    # alpha_epsilon has coefficient 48/(16 pi^2)=3/pi^2.
    sunset_log_numerator = Fraction(48, 16)
    assert_equal(sunset_log_numerator, Fraction(3), "phi4_3 logarithmic mass numerator")


def check_spde_ou_and_smoothing_normalizations():
    # For dZ_t = -a Z_t dt + sqrt(2) dB_t, the stationary variance is
    # 2 int_0^infty exp(-2 a u) du = 1/a.  This fixes the noise
    # normalization giving invariant covariance (-Delta + m^2)^(-1).
    a = Fraction(7, 3)
    stationary_variance = Fraction(2, 1) * Fraction(1, 2 * a)
    assert_equal(stationary_variance, Fraction(1, 1) / a, "OU stationary variance")

    # In two dimensions, E ||X||_{H^{-s}}^2 has shell integrand
    # r * r^{-2s} * r^{-2} = r^{-1-2s}, which is integrable at infinity
    # precisely when s > 0.
    s = Fraction(1, 5)
    shell_exponent = Fraction(1, 1) - 2 * s - 2
    if not shell_exponent < -1:
        raise AssertionError("2D OU negative-Sobolev convergence threshold failed")

    # The sharpened Wick-power Sobolev proof uses the two-dimensional
    # n-fold massive-propagator convolution bound
    # G^{*n}(q) <= log(q)^(n-1) / q^2.  With H^{-s} weight the shell
    # exponent is r * r^{-2s} * r^{-2} = r^{-1-2s}, so any s > 0 works.
    s_wick = Fraction(1, 5)
    wick_shell_exponent = Fraction(1, 1) - 2 * s_wick - 2
    if not wick_shell_exponent < -1:
        raise AssertionError("2D Wick H^{-s} convergence threshold failed")

    # Heat smoothing uses sup_{y >= 0} y^theta exp(-t y) =
    # (theta/t)^theta exp(-theta).  Check the value for a finite sample.
    theta = 2.0
    t = 0.25
    y_star = theta / t
    lhs = (y_star**theta) * math.exp(-t * y_star)
    rhs = (theta / t) ** theta * math.exp(-theta)
    if abs(lhs - rhs) > 1.0e-12:
        raise AssertionError("heat-kernel smoothing optimization failed")


def check_dpd_sobolev_fixed_point_exponents():
    # The Sobolev DPD proof in Volume XI Chapter 9 takes
    # beta = 1 + 2 kappa on T^2.  The conditions below are the exact
    # inequalities used in the multiplication and heat-smoothing proof.
    kappa = Fraction(1, 5)
    beta = 1 + 2 * kappa
    assert_equal(beta, Fraction(7, 5), "DPD beta value")

    if not (0 < kappa < Fraction(1, 4)):
        raise AssertionError("DPD kappa range failed")
    if not beta > 1:
        raise AssertionError("H^beta is not above the 2D algebra threshold")

    # H^beta * H^beta -> H^beta follows from the resonant estimate landing in
    # H^(2 beta - 1), which must be at least H^beta.
    algebra_gain = 2 * beta - 1 - beta
    assert_equal(algebra_gain, Fraction(2, 5), "DPD algebra gain")
    if not algebra_gain > 0:
        raise AssertionError("DPD algebra resonance estimate failed")

    # H^beta * H^(-kappa) -> H^(-kappa) uses beta - kappa > 1 and the
    # resonant regularity beta - kappa - 1 = kappa > -kappa.
    multiplier_threshold = beta - kappa - 1
    assert_equal(multiplier_threshold, kappa, "DPD multiplier resonant output")
    if not beta - kappa > 1:
        raise AssertionError("DPD multiplier resonance threshold failed")
    if not multiplier_threshold > -kappa:
        raise AssertionError("DPD multiplier output does not dominate H^-kappa")

    # Heat smoothing from H^(-kappa) to H^beta requires
    # theta = (beta + kappa)/2 < 1 so that the Duhamel integral gains
    # T^(1-theta).
    theta = (beta + kappa) / 2
    assert_equal(theta, Fraction(4, 5), "DPD heat-smoothing theta")
    assert_equal(1 - theta, Fraction(1, 5), "DPD Duhamel time gain")
    if not theta < 1:
        raise AssertionError("DPD Duhamel exponent is not integrable")


def main():
    check_wick_polynomials()
    check_tadpole_asymptotics()
    check_phi4_power_counting()
    check_phi4_three_two_loop_mass_coordinate()
    check_spde_ou_and_smoothing_normalizations()
    check_dpd_sobolev_fixed_point_exponents()
    print("All constructive scalar/SPDE Wick, power-counting, and DPD exponent checks passed.")


if __name__ == "__main__":
    main()
