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
    assert_equal(x, Fraction(-11, 20), "Phi4_3 X homogeneity")
    assert_equal(x3, Fraction(-33, 20), "Phi4_3 X^3 homogeneity")
    assert_equal(ix3, Fraction(7, 20), "Phi4_3 I(X^3) homogeneity")
    assert_equal(two_loop_tree, Fraction(-3, 4), "Phi4_3 two-loop tree homogeneity")
    if not two_loop_tree < 0:
        raise AssertionError("Phi4_3 two-loop tree is not negative")

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
    check_modelled_fixed_point_contraction_arithmetic()
    check_random_model_cauchy_criterion_arithmetic()
    check_dyadic_parabolic_convolution_bound_arithmetic()
    check_parabolic_taylor_subtraction_gain_arithmetic()
    print("All constructive scalar/SPDE Wick, chaos, power-counting, DPD, reconstruction, BPHZ, fixed-point, random-model convergence, dyadic-kernel, and Taylor-gain checks passed.")


if __name__ == "__main__":
    main()
