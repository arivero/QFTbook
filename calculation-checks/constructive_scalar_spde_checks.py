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


def poly_multiply(a, b):
    product = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            product[i + j] += ai * bj
    return product


def gaussian_moment(power):
    if power % 2 == 1:
        return Fraction(0)
    result = Fraction(1)
    for odd in range(1, power, 2):
        result *= odd
    return result


def gaussian_polynomial_expectation(coefficients):
    return sum(coeff * gaussian_moment(power) for power, coeff in enumerate(coefficients))


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


def check_wiener_chaos_isometry_and_moments():
    h2 = hermite_probabilists(2)
    h3 = hermite_probabilists(3)
    h2_squared = poly_multiply(h2, h2)
    h3_squared = poly_multiply(h3, h3)
    h2_fourth = poly_multiply(h2_squared, h2_squared)
    assert_equal(gaussian_polynomial_expectation(h2_squared), 2, "second chaos isometry")
    assert_equal(gaussian_polynomial_expectation(h3_squared), 6, "third chaos isometry")
    assert_equal(gaussian_polynomial_expectation(h2_fourth), 60, "second chaos fourth moment")

    # Corollary constant for Q=2, m=2, B_0=1, B_1=2, B_2=3 with
    # C_0=1, C_1=3!!=3, C_2 bounded by the exact fourth moment 60.
    q_plus_one_factor = 3 ** 3
    moment_constant = q_plus_one_factor * (1 + 3 * 2**4 + 60 * 3**4)
    assert_equal(moment_constant, 132543, "finite chaos coordinate-moment constant")


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


def check_phi4_three_finite_cutoff_stability_bound():
    # For p(q)=lambda :q^4: + alpha :q^2: + beta at cutoff variance c,
    # write y=q^2 and p=lambda y^2 + A y + B.  The lower bound is
    # B - (A^-)^2/(4 lambda).
    lam = Fraction(2)
    c = Fraction(5)
    alpha = Fraction(3)
    beta = Fraction(7)
    a_coeff = alpha - 6 * lam * c
    b_coeff = 3 * lam * c * c - alpha * c + beta
    lower_bound = b_coeff - max(-a_coeff, 0) ** 2 / (4 * lam)
    vertex_y = -a_coeff / (2 * lam)
    vertex_value = lam * vertex_y * vertex_y + a_coeff * vertex_y + b_coeff
    assert_equal(lower_bound, Fraction(-2113, 8), "phi4_3 local stability lower bound")
    assert_equal(vertex_value, lower_bound, "phi4_3 local stability vertex value")


def check_phi4_three_multiscale_geometric_bound():
    # The abstract phase-cell theorem uses
    # sum_j C0 |lambda|^(1+delta) L^(-alpha j)
    # = C0 |lambda|^(1+delta)/(1-L^(-alpha)).
    # Use a finite exact sample with L^(-alpha)=1/2.
    scale_ratio = Fraction(1, 2)
    c_lambda = Fraction(1, 100)
    b_r = Fraction(3)
    a_prime = Fraction(1, 10)
    scale_sum = c_lambda / (1 - scale_ratio)
    assert_equal(scale_sum, Fraction(1, 50), "phi4_3 multiscale full sum")
    if not b_r * scale_sum <= a_prime:
        raise AssertionError("phi4_3 multiscale KP smallness failed")

    tail_j5 = c_lambda * scale_ratio**5 / (1 - scale_ratio)
    assert_equal(tail_j5, Fraction(1, 1600), "phi4_3 multiscale ultraviolet tail")


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


def check_dpd_energy_young_exponents():
    # The smooth DPD energy estimate uses Young pairs:
    # |Y|^3 |X_1| with (4/3,4), |Y|^2 |X_2| with (2,2),
    # and |Y| |X_3| with (4,4/3).  The Y-powers must all become |Y|^4.
    pairs = [
        (Fraction(3), Fraction(4, 3), Fraction(1), Fraction(4), "Y^3 X1"),
        (Fraction(2), Fraction(2), Fraction(1), Fraction(2), "Y^2 X2"),
        (Fraction(1), Fraction(4), Fraction(1), Fraction(4, 3), "Y X3"),
    ]
    for y_power, p, x_power, q, label in pairs:
        assert_equal(Fraction(1, 1) / p + Fraction(1, 1) / q, 1, f"{label} Young conjugacy")
        assert_equal(y_power * p, 4, f"{label} Y exponent")
        if label == "Y X3":
            assert_equal(x_power * q, Fraction(4, 3), f"{label} X exponent")
        else:
            assert_equal(x_power * q, 4 if label == "Y^3 X1" else 2, f"{label} X exponent")


def check_invariant_measure_limit_identity():
    # A finite Markov-chain analogue of the cutoff invariance passage:
    # if mu P = mu and P_n=P exactly, then the invariant identity is the
    # row-vector equality sum_i mu_i (P f)_i = sum_i mu_i f_i.
    p = [
        [Fraction(3, 4), Fraction(1, 4)],
        [Fraction(1, 2), Fraction(1, 2)],
    ]
    mu = [Fraction(2, 3), Fraction(1, 3)]
    f = [Fraction(5), Fraction(-1)]
    pf = [sum(p[i][j] * f[j] for j in range(2)) for i in range(2)]
    lhs = sum(mu[i] * pf[i] for i in range(2))
    rhs = sum(mu[i] * f[i] for i in range(2))
    assert_equal(lhs, rhs, "finite invariant-measure identity")


def check_reconstruction_wavelet_scale_powers():
    # The compact reconstruction proof uses two dyadic sums.  For coarse
    # scales l >= delta the factor is delta^r l^(gamma-r), which sums to
    # delta^gamma when r > gamma.  For fine scales l < delta and a
    # homogeneity alpha, the factor is delta^(gamma-alpha-r) l^(alpha+r),
    # which sums to delta^gamma when alpha+r > 0.
    gamma = Fraction(3, 5)
    alpha = Fraction(-2, 5)
    r = Fraction(1, 1)
    parabolic_dimension = Fraction(5, 1)
    if not gamma < parabolic_dimension:
        raise AssertionError("reconstruction scaling-function condition gamma < |s| failed")
    if not r > gamma:
        raise AssertionError("reconstruction coarse wavelet condition r > gamma failed")
    if not alpha + r > 0:
        raise AssertionError("reconstruction fine wavelet condition alpha+r > 0 failed")

    coarse_delta_power = r + (gamma - r)
    fine_delta_power = (gamma - alpha - r) + (alpha + r)
    assert_equal(coarse_delta_power, gamma, "reconstruction coarse delta power")
    assert_equal(fine_delta_power, gamma, "reconstruction fine delta power")


def check_phi4_three_spde_bphz_counterterm_combinatorics():
    # Parabolic dimension for dynamic Phi^4_3 is |s|=5.  With
    # |Xi|=-5/2-kappa and integration degree 2, X=I Xi has homogeneity
    # -1/2-kappa.  The two-loop symbol X^2 I(X^3) must remain negative for
    # the small kappa used in the chapter.
    kappa = Fraction(1, 20)
    xi = Fraction(-5, 2) - kappa
    x = xi + 2
    x2 = 2 * x
    x3 = 3 * x
    ix3 = x3 + 2
    two_loop_tree = x2 + ix3
    xy2 = x + 2 * ix3
    y3 = 3 * ix3
    assert_equal(x, Fraction(-11, 20), "Phi4_3 X homogeneity")
    assert_equal(x3, Fraction(-33, 20), "Phi4_3 X^3 homogeneity")
    assert_equal(ix3, Fraction(7, 20), "Phi4_3 I(X^3) homogeneity")
    assert_equal(two_loop_tree, Fraction(-3, 4), "Phi4_3 two-loop tree homogeneity")
    assert_equal(xy2, Fraction(3, 20), "Phi4_3 X I(X^3)^2 homogeneity")
    assert_equal(y3, Fraction(21, 20), "Phi4_3 I(X^3)^3 homogeneity")
    if not kappa < Fraction(1, 14):
        raise AssertionError("Phi4_3 drift-ledger kappa range failed")
    if not two_loop_tree < 0:
        raise AssertionError("Phi4_3 two-loop tree is not negative")
    if not xy2 > 0:
        raise AssertionError("Phi4_3 X I(X^3)^2 should be positive in the drift ledger")
    if not y3 > 0:
        raise AssertionError("Phi4_3 I(X^3)^3 should be positive in the drift ledger")

    # In the sharp spatial cutoff chart for the one-loop local coordinate,
    # the l-infinity shell |n|_infty=r contains (2r+1)^3-(2r-1)^3 modes.
    r = 5
    shell_count = (2 * r + 1) ** 3 - (2 * r - 1) ** 3
    assert_equal(shell_count, 24 * r * r + 2, "Z^3 l-infinity shell count")
    shell_upper = Fraction(shell_count, r * r)
    if not shell_upper <= 26:
        raise AssertionError("one-loop shell upper bound failed")
    shell_lower = Fraction(shell_count, 4 * r * r)
    if not shell_lower >= 6:
        raise AssertionError("one-loop shell lower bound failed")
    dyadic_shell_count = sum((2 * s + 1) ** 3 - (2 * s - 1) ** 3 for s in range(9, 17))
    dyadic_shell_bound = sum(Fraction((2 * s + 1) ** 3 - (2 * s - 1) ** 3, s * s) for s in range(9, 17))
    assert_equal(dyadic_shell_count, 31024, "dyadic Z^3 shell count")
    if not dyadic_shell_bound <= 26 * 8:
        raise AssertionError("dyadic one-loop shell increment bound failed")

    # The two-loop Fourier coordinate is logarithmic because the dyadic
    # block with p-scale ell and q-scale s is bounded by 2^(-|ell-s|).
    max_scale = 6
    c2_upper_factor = sum(
        Fraction(1, 2) ** abs(ell - scale)
        for ell in range(max_scale + 1)
        for scale in range(max_scale + 1)
    )
    if not c2_upper_factor <= 3 * (max_scale + 1):
        raise AssertionError("two-loop dyadic logarithmic upper sum failed")
    if not c2_upper_factor >= max_scale + 1:
        raise AssertionError("two-loop dyadic diagonal lower sum failed")

    lower_scale = 5
    positive_box_width = 2 ** (lower_scale - 2)
    positive_box_size = positive_box_width ** 3
    positive_pair_count = positive_box_size ** 2
    lower_block_factor = Fraction(positive_pair_count, 2 ** (6 * lower_scale))
    assert_equal(lower_block_factor, Fraction(1, 4096), "two-loop lower block factor")

    shell_center = 6
    c2_shell_factor = sum(
        Fraction(1, 2) ** abs(ell - scale)
        for ell in range(shell_center + 2)
        for scale in range(shell_center + 2)
        if max(ell, scale) >= shell_center - 1
    )
    if not c2_shell_factor <= 9:
        raise AssertionError("two-loop dyadic shell bound failed")

    # For the non-nested dynamic Phi4_3 sunset, the retarded heat edge has
    # order 2 and the two covariance edges have order 4 in parabolic
    # dimension Q=5.  The equal-scale exponent is zero, and the relative
    # gaps have weights 3,1,1.
    q_parabolic = 5
    heat_order = 2
    cov_order = 4
    heat_gap = q_parabolic - heat_order
    cov_gap = q_parabolic - cov_order
    sunset_equal_scale_exponent = 2 * q_parabolic - (heat_order + 2 * cov_order)
    assert_equal(sunset_equal_scale_exponent, 0, "Phi4_3 sunset logarithmic balance")
    assert_equal(heat_gap, 3, "Phi4_3 sunset heat gap")
    assert_equal(cov_gap, 1, "Phi4_3 sunset covariance gap")
    sunset_shell_factor = (
        Fraction(1, 1) / (1 - Fraction(1, 2)) ** 2
        + 2
        * Fraction(1, 1)
        / ((1 - Fraction(1, 8)) * (1 - Fraction(1, 2)))
    )
    assert_equal(sunset_shell_factor, Fraction(60, 7), "Phi4_3 sunset shell factor")

    # The nested tadpole at fixed scales cancels against the inner one-loop
    # forest subtraction: 2*3 pairings from X(z)^2 X(w)^3 and -3*2 from
    # X(z)^2 C1 X(w).
    nested_pairings = 2 * 3
    inner_counterterm_pairings = -3 * 2
    assert_equal(nested_pairings + inner_counterterm_pairings, 0, "Phi4_3 nested forest cancellation")

    # One-loop cubic Wick contraction: choose the contracted pair in three
    # fields.  Two-loop non-nested sunset: choose the corrected outer factor,
    # then the local linear part of X(z)^2 K X(w)^3 gives 3*C2 with the
    # chapter normalization C2=2*I.
    one_loop_pairings = 3
    outer_response_choices = 3
    raw_sunset_pairings = 6
    c2_normalization = 2
    local_sunset_factor = Fraction(raw_sunset_pairings, c2_normalization)
    assert_equal(local_sunset_factor, 3, "Phi4_3 local sunset factor")
    assert_equal(outer_response_choices * local_sunset_factor, 9, "Phi4_3 two-loop coefficient")

    # Divergent local part of the drift is -3 lambda C1 + 9 lambda^2 C2;
    # the counterterm inserted in the equation has the opposite signs.
    assert_equal(-one_loop_pairings, -3, "Phi4_3 one-loop drift sign")
    assert_equal(-(outer_response_choices * local_sunset_factor), -9, "Phi4_3 two-loop counterterm sign")


def check_phi4_three_negative_sector_coordinate_chart():
    kappa = Fraction(1, 20)
    x = -Fraction(1, 2) - kappa
    xi = -Fraction(5, 2) - kappa
    y = 3 * x + 2
    gamma_minus = Fraction(1, 2) - 7 * kappa

    hom = {
        "Xi": xi,
        "X": x,
        "X2": 2 * x,
        "X3": 3 * x,
        "Y": y,
        "XY": x + y,
        "X2Y": 2 * x + y,
        "Y2": 2 * y,
        "XY2": x + 2 * y,
        "Y3": 3 * y,
    }
    assert_equal(y, Fraction(7, 20), "Phi4_3 Y homogeneity")
    assert_equal(gamma_minus, Fraction(3, 20), "Phi4_3 negative-sector cutoff")
    expected_below = {"Xi", "X", "X2", "X3", "XY", "X2Y"}
    actual_below = {name for name, value in hom.items() if value < gamma_minus}
    assert_equal(actual_below, expected_below, "Phi4_3 negative coordinate sector")
    assert_equal(hom["XY2"], gamma_minus, "Phi4_3 excluded boundary monomial")
    if not hom["Y"] > gamma_minus:
        raise AssertionError("Y should lie above the strict negative coordinate sector")
    if not hom["Y2"] > gamma_minus:
        raise AssertionError("Y^2 should lie above the strict negative coordinate sector")
    if not hom["Y3"] > gamma_minus:
        raise AssertionError("Y^3 should lie above the strict negative coordinate sector")

    gamma_gap_xy_to_x = hom["XY"] - hom["X"]
    gamma_gap_x2y_to_x2 = hom["X2Y"] - hom["X2"]
    assert_equal(gamma_gap_xy_to_x, y, "Gamma XY-to-X gap")
    assert_equal(gamma_gap_x2y_to_x2, y, "Gamma X2Y-to-X2 gap")

    nontrivial_pi_coordinates = len(expected_below)
    nontrivial_gamma_coordinates = 2
    assert_equal(nontrivial_pi_coordinates + nontrivial_gamma_coordinates, 8, "negative-sector coordinate count")


def check_modelled_fixed_point_contraction_arithmetic():
    # Exact rational check of the abstract fixed-point inequalities:
    # A T^theta (B |lambda| R^3 + D |M| R) <= R/2 and
    # A T^theta (2 B |lambda| R^2 + D |M|) < 1.
    a = Fraction(2)
    ttheta = Fraction(1, 200)
    b = Fraction(3)
    lam = Fraction(1)
    d = Fraction(1)
    mass = Fraction(1, 2)
    r0 = Fraction(1)
    r = 2 * r0

    ball_increment = a * ttheta * (b * lam * r**3 + d * mass * r)
    contraction = a * ttheta * (2 * b * lam * r**2 + d * mass)
    assert_equal(ball_increment, Fraction(1, 4), "modelled fixed-point ball increment")
    assert_equal(r / 2, 1, "modelled fixed-point half radius")
    if not ball_increment <= r / 2:
        raise AssertionError("modelled fixed-point ball condition failed")
    if not contraction < 1:
        raise AssertionError("modelled fixed-point contraction condition failed")

    # The Picard tail bound is q^n/(1-q) times the first step.
    q = contraction
    n = 3
    first_step = Fraction(5, 7)
    tail = q**n * first_step / (1 - q)
    expected = Fraction(16807, 1208000)
    assert_equal(tail, expected, "modelled fixed-point Picard tail")


def check_random_model_cauchy_criterion_arithmetic():
    # The random-model convergence theorem uses dyadic Cauchy estimates
    # E D_n^p <= C 2^(-p rho n).  With rho=2, rho'=1, p=3, the
    # Borel-Cantelli exponent p(rho-rho') is positive and the dyadic tail is
    # exactly geometric.
    p = 3
    rho = Fraction(2)
    rho_prime = Fraction(1)
    markov_exponent = p * (rho - rho_prime)
    assert_equal(markov_exponent, Fraction(3), "random-model Markov exponent")
    if not markov_exponent > 0:
        raise AssertionError("random-model Markov series is not summable")

    n = 5
    assert_equal(rho_prime, 1, "random-model sample rho prime")
    dyadic_tail = sum(Fraction(1, 2) ** j for j in range(n, 40))
    closed_tail = (Fraction(1, 2) ** n) / (1 - Fraction(1, 2))
    finite_remainder = (Fraction(1, 2) ** 40) / (1 - Fraction(1, 2))
    assert_equal(dyadic_tail + finite_remainder, closed_tail, "random-model geometric tail")
    assert_equal(closed_tail, Fraction(1, 16), "random-model tail at n=5")


def check_dyadic_parabolic_convolution_bound_arithmetic():
    # For kernels of orders a and b in homogeneous dimension Q, the
    # proposition gives output L^infty exponent Q-a-b and L^1 exponent
    # -(a+b).  The geometric factor separates the i=k and j=k branches.
    qdim = Fraction(5)
    a = Fraction(2)
    b = Fraction(1)
    output_linf_exponent = qdim - a - b
    output_l1_exponent = output_linf_exponent - qdim
    assert_equal(output_linf_exponent, Fraction(2), "dyadic convolution L-infinity exponent")
    assert_equal(output_l1_exponent, Fraction(-3), "dyadic convolution L1 exponent")

    k = 3
    branch_j_tail = Fraction(1, 1) / (1 - Fraction(1, 2) ** b)
    branch_i_tail = (Fraction(1, 2) ** a) / (1 - Fraction(1, 2) ** a)
    total_geometric_factor = branch_j_tail + branch_i_tail
    scaled_bound = (Fraction(2) ** (output_linf_exponent * k)) * total_geometric_factor
    assert_equal(branch_j_tail, 2, "dyadic convolution j-tail factor")
    assert_equal(branch_i_tail, Fraction(1, 3), "dyadic convolution i-tail factor")
    assert_equal(total_geometric_factor, Fraction(7, 3), "dyadic convolution total factor")
    assert_equal(scaled_bound, Fraction(448, 3), "dyadic convolution sample bound")


def check_parabolic_taylor_subtraction_gain_arithmetic():
    # The Taylor-subtraction lemma multiplies the kernel L1 scale
    # 2^(-a i) by the remainder scale 2^(-r i).
    a = Fraction(2)
    r = Fraction(3)
    i = 4
    exponent = -(a + r) * i
    assert_equal(exponent, Fraction(-20), "Taylor-subtraction total exponent")
    bound = Fraction(2) ** exponent
    assert_equal(bound, Fraction(1, 1048576), "Taylor-subtraction sample bound")


def check_dyadic_net_supremum_upgrade_arithmetic():
    # The dyadic-net theorem bounds the base net by C0^(1/p) B0 and the
    # edge tower by C1^(1/p) B sum_l 2^(-epsilon l/p).  Choose perfect
    # p-th powers so that the check remains exact in rational arithmetic.
    p = 2
    d = 5
    epsilon = 2
    c0 = 9
    c1 = 4
    b0 = 5
    b = 3

    base = 3 * b0
    if epsilon % p != 0:
        raise AssertionError("dyadic-net sample must use an integral epsilon/p")
    ratio = Fraction(1, 2) ** (epsilon // p)
    tail = 2 * b / (1 - ratio)
    total = base + tail
    assert_equal(ratio, Fraction(1, 2), "dyadic-net geometric ratio")
    assert_equal(base, 15, "dyadic-net base contribution")
    assert_equal(tail, 12, "dyadic-net edge contribution")
    assert_equal(total, 27, "dyadic-net supremum bound")

    # At edge level ell=3 the summed p-th moment is
    # C1 B^p 2^(-epsilon ell)=4*9/64=9/16, whose L^2 root is 3/4.
    ell = 3
    edge_exponent = d * ell - (d + epsilon) * ell
    assert_equal(edge_exponent, -epsilon * ell, "dyadic-net entropy cancellation")
    summed_p_moment = c1 * b**p * Fraction(2) ** edge_exponent
    assert_equal(summed_p_moment, Fraction(9, 16), "dyadic-net edge p-moment sum")
    edge_l2_norm_squared = summed_p_moment
    assert_equal(edge_l2_norm_squared, Fraction(3, 4) ** 2, "dyadic-net edge L2 root")

    # If the base and edge constants both carry a cutoff factor
    # 2^(-rho n), then the entire right side carries the same factor.
    rho = 1
    n = 4
    cutoff_total = total * Fraction(1, 2) ** (rho * n)
    assert_equal(cutoff_total, Fraction(27, 16), "dyadic-net cutoff tail")


def check_scale_summed_coordinate_upgrade_arithmetic():
    # Scale-summed coordinate upgrade: entropy 2^(D m) changes the scale
    # decay from 2^(-sigma m) to 2^(-(sigma-D/p)m) after taking an L^p root.
    p = 2
    d_big = 4
    sigma = 3
    epsilon = 2
    c0_root = 3
    c1_root = 2
    b0 = 5
    b = 3
    slack = Fraction(sigma) - Fraction(d_big, p)
    assert_equal(slack, 1, "scale-summed entropy slack")

    if epsilon % p != 0:
        raise AssertionError("scale-summed sample must use integral epsilon/p")
    ell_ratio = Fraction(1, 2) ** (epsilon // p)
    per_scale_constant = c0_root * b0 + c1_root * b / (1 - ell_ratio)
    scale_ratio = Fraction(1, 2) ** slack
    total = per_scale_constant / (1 - scale_ratio)
    assert_equal(per_scale_constant, 27, "scale-summed per-scale constant")
    assert_equal(scale_ratio, Fraction(1, 2), "scale-summed m-ratio")
    assert_equal(total, 54, "scale-summed total constant")

    m = 5
    summed_base_p_moment = (c0_root**p) * (2 ** (d_big * m)) * (b0**p) * Fraction(1, 2) ** (p * sigma * m)
    assert_equal(summed_base_p_moment, Fraction(225, 1024), "scale-summed base entropy cancellation")

    rho = 2
    n = 3
    cutoff_total = total * Fraction(1, 2) ** (rho * n)
    assert_equal(cutoff_total, Fraction(27, 32), "scale-summed cutoff factor")


def check_coordinate_to_model_convergence_arithmetic():
    # Exact arithmetic for the coordinate-to-model theorem.  With p=2 and
    # epsilon=2, every coordinate has geometric ratio 1/2.  The first
    # uniform coordinate has S_1=3*5+2*3/(1-1/2)=27.  The second has
    # S_2=4*2+3*1/(1-1/2)=14.
    p = 2
    epsilon = 2
    if epsilon % p != 0:
        raise AssertionError("coordinate-to-model sample must use integral epsilon/p")
    ratio = Fraction(1, 2) ** (epsilon // p)
    s1 = 3 * 5 + 2 * 3 / (1 - ratio)
    s2 = 4 * 2 + 3 * 1 / (1 - ratio)
    a_ctrl = 2
    uniform_lp_bound = a_ctrl * (1 + s1 + s2)
    assert_equal(s1, 27, "coordinate-to-model S1")
    assert_equal(s2, 14, "coordinate-to-model S2")
    assert_equal(uniform_lp_bound, 84, "coordinate-to-model uniform Lp bound")
    assert_equal(uniform_lp_bound**p, 7056, "coordinate-to-model C_N")

    # Increment constants: S~_1=2*3+1*2/(1-1/2)=10 and
    # S~_2=1*5+2*1/(1-1/2)=9.
    stilde1 = 2 * 3 + 1 * 2 / (1 - ratio)
    stilde2 = 1 * 5 + 2 * 1 / (1 - ratio)
    distance_prefactor = a_ctrl * (stilde1 + stilde2)
    assert_equal(stilde1, 10, "coordinate-to-model S-tilde1")
    assert_equal(stilde2, 9, "coordinate-to-model S-tilde2")
    assert_equal(distance_prefactor, 38, "coordinate-to-model distance prefactor")
    assert_equal(distance_prefactor**p, 1444, "coordinate-to-model C_D")

    rho = 1
    n = 3
    distance_lp_bound = distance_prefactor * Fraction(1, 2) ** (rho * n)
    distance_p_moment = distance_lp_bound**p
    assert_equal(distance_lp_bound, Fraction(19, 4), "coordinate-to-model dyadic distance")
    assert_equal(distance_p_moment, Fraction(361, 16), "coordinate-to-model dyadic p-moment")


def check_multiscale_sector_kernel_summability_arithmetic():
    # Sector gap exponents eta=(1,2,3) give
    # G = 1/(1-1/2) 1/(1-1/4) 1/(1-1/8)=64/21.
    etas = [1, 2, 3]
    geometric_factors = [Fraction(1, 1) / (1 - Fraction(1, 2) ** eta) for eta in etas]
    g = Fraction(1)
    for factor in geometric_factors:
        g *= factor
    assert_equal(geometric_factors, [Fraction(2), Fraction(4, 3), Fraction(8, 7)], "sector geometric factors")
    assert_equal(g, Fraction(64, 21), "sector full geometric factor")

    # G-tilde is the sum of products omitting one factor:
    # 32/21 + 16/7 + 8/3 = 136/21.
    g_tilde = sum(
        math.prod(geometric_factors[k] for k in range(len(etas)) if k != h)
        for h in range(len(etas))
    )
    assert_equal(g_tilde, Fraction(136, 21), "sector shell geometric factor")

    b = Fraction(5)
    sigma = Fraction(7)
    uniform_bound = b * sigma * g
    assert_equal(uniform_bound, Fraction(320, 3), "sector uniform kernel bound")

    eta_star = min(etas)
    n = 4
    increment_bound = b * sigma * g_tilde * Fraction(1, 2) ** (eta_star * (n + 1))
    relaxed_increment_bound = b * sigma * g_tilde * Fraction(1, 2) ** (eta_star * n)
    assert_equal(increment_bound, Fraction(85, 12), "sector sharp increment bound")
    assert_equal(relaxed_increment_bound, Fraction(85, 6), "sector relaxed increment bound")
    if not increment_bound <= relaxed_increment_bound:
        raise AssertionError("sector increment relaxation failed")

    # Exact shell sum at max(r)=5 is below the union bound G-tilde 2^-5.
    n_plus_one = 5
    exact_shell = Fraction(1)
    exact_inner = Fraction(1)
    for eta in etas:
        exact_shell *= sum(Fraction(1, 2) ** (eta * r) for r in range(n_plus_one + 1))
        exact_inner *= sum(Fraction(1, 2) ** (eta * r) for r in range(n_plus_one))
    exact_shell -= exact_inner
    union_shell_bound = g_tilde * Fraction(1, 2) ** n_plus_one
    if not exact_shell <= union_shell_bound:
        raise AssertionError("sector shell union bound failed")


def check_one_loop_relative_scale_gap_arithmetic():
    # Dynamic Phi^4_3 one-loop prototype: Q=5 and both heat/covariance
    # kernels have order 2.  With Holder exponent theta=1, the subtracted
    # j <= i sector has gap a+theta=3 and the j > i sector has gap b=2.
    qdim = Fraction(5)
    a = Fraction(2)
    b = Fraction(2)
    theta = Fraction(1)
    base_exponent = qdim - a - b
    assert_equal(base_exponent, Fraction(1), "one-loop base divergence exponent")

    i = 7
    j = 4
    local_exponent = base_exponent * j - (a + theta) * (i - j)
    assert_equal(local_exponent, Fraction(-5), "one-loop local-sector exponent")
    assert_equal(Fraction(2) ** local_exponent, Fraction(1, 32), "one-loop local-sector bound")

    i_off = 4
    j_off = 7
    off_exponent = base_exponent * i_off - b * (j_off - i_off)
    assert_equal(off_exponent, Fraction(-2), "one-loop off-sector exponent")
    assert_equal(Fraction(2) ** off_exponent, Fraction(1, 4), "one-loop off-sector bound")

    local_gap_sum = Fraction(1, 1) / (1 - Fraction(1, 2) ** (a + theta))
    off_gap_sum = (Fraction(1, 2) ** b) / (1 - Fraction(1, 2) ** b)
    assert_equal(local_gap_sum, Fraction(8, 7), "one-loop local gap sum")
    assert_equal(off_gap_sum, Fraction(1, 3), "one-loop off gap sum")


def main():
    check_wick_polynomials()
    check_wiener_chaos_isometry_and_moments()
    check_tadpole_asymptotics()
    check_phi4_power_counting()
    check_phi4_three_two_loop_mass_coordinate()
    check_phi4_three_finite_cutoff_stability_bound()
    check_phi4_three_multiscale_geometric_bound()
    check_spde_ou_and_smoothing_normalizations()
    check_dpd_sobolev_fixed_point_exponents()
    check_dpd_energy_young_exponents()
    check_invariant_measure_limit_identity()
    check_reconstruction_wavelet_scale_powers()
    check_phi4_three_spde_bphz_counterterm_combinatorics()
    check_phi4_three_negative_sector_coordinate_chart()
    check_modelled_fixed_point_contraction_arithmetic()
    check_random_model_cauchy_criterion_arithmetic()
    check_dyadic_parabolic_convolution_bound_arithmetic()
    check_parabolic_taylor_subtraction_gain_arithmetic()
    check_dyadic_net_supremum_upgrade_arithmetic()
    check_scale_summed_coordinate_upgrade_arithmetic()
    check_coordinate_to_model_convergence_arithmetic()
    check_multiscale_sector_kernel_summability_arithmetic()
    check_one_loop_relative_scale_gap_arithmetic()
    print("All constructive scalar/SPDE Wick, chaos, power-counting, DPD, reconstruction, BPHZ, negative-ledger, negative-coordinate-chart, C1-growth, C2-log-growth, C2-shell, two-loop-sector, fixed-point, random-model convergence, dyadic-kernel, Taylor-gain, dyadic-net supremum, scale-summed-coordinate, coordinate-to-model convergence, multiscale-sector, and one-loop relative-scale checks passed.")


if __name__ == "__main__":
    main()
