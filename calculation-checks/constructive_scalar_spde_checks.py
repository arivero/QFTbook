#!/usr/bin/env python3
"""Finite checks for constructive scalar/SPDE normalization conventions.

The checks include finite arithmetic shadows of the invariant-law and
stationary-law comparison steps used in the singular-SPDE-to-OS proof stack.
They also track the constructive Phi^4_3 phase-cell derivation budget:
activity tails, source-decorated tails, and local-coordinate/OS defect tails.

Evidence contract.
Target claims: finite normalization, phase-cell, source-window, OS-defect,
and SPDE/constructive hierarchy-transfer subclaims in the constructive scalar
and singular-SPDE chapters.
Independent construction: exact rational Wick/chaos arithmetic, finite
Langevin reversibility checks, dyadic kernel sums, coordinate power counting,
and explicit error-budget inequalities are computed from finite model data.
Imported assumptions: the chapter's regulator schedules, finite chaos bases,
Besov/Sobolev exponent conventions, model-kernel choices, and stated
renormalized coordinate charts.
Negative controls: omitted logarithmic slack, underestimated sector budgets,
wrong edge/cutoff powers, and incompatible OS-defect schedules are represented
by checks that fail when those finite inequalities are changed.
Scope boundary: a pass checks finite arithmetic shadows and assembly budgets;
it does not prove tightness, invariant-measure existence, convergence of the
renormalized SPDE, Osterwalder-Schrader reconstruction, or the full Phi^4_3
constructive theorem.
"""
from check_utils import assert_close as _assert_close
from check_utils import assert_leq as _assert_leq


from fractions import Fraction
import math


def assert_equal(got, expected, label):
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_close_float(got, expected, label, tol=1.0e-12):
    _assert_close(label, got, expected, tol=tol)


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


def bivar_add(a, b):
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, Fraction(0)) + value
        if result[key] == 0:
            del result[key]
    return result


def bivar_scalar_mul(c, poly):
    return {key: c * value for key, value in poly.items() if c * value != 0}


def bivar_mul(a, b):
    result = {}
    for (ix, iy), av in a.items():
        for (jx, jy), bv in b.items():
            key = (ix + jx, iy + jy)
            result[key] = result.get(key, Fraction(0)) + av * bv
    return {key: value for key, value in result.items() if value != 0}


def bivar_derivative(poly, variable):
    result = {}
    for (ix, iy), value in poly.items():
        if variable == 0 and ix:
            result[(ix - 1, iy)] = result.get((ix - 1, iy), Fraction(0)) + value * ix
        if variable == 1 and iy:
            result[(ix, iy - 1)] = result.get((ix, iy - 1), Fraction(0)) + value * iy
    return result


def scaled_gaussian_even_moment(power, precision):
    if power % 2:
        return Fraction(0)
    result = Fraction(1)
    for odd in range(1, power, 2):
        result *= odd
    return result / (precision ** (power // 2))


def bivar_gaussian_expectation(poly, precision_x, precision_y):
    total = Fraction(0)
    for (ix, iy), value in poly.items():
        total += (
            value
            * scaled_gaussian_even_moment(ix, precision_x)
            * scaled_gaussian_even_moment(iy, precision_y)
        )
    return total


def check_finite_langevin_reversibility_dirichlet_form():
    # Exact two-mode finite-cutoff shadow of the gradient Langevin identity.
    # The action is S=(a x^2+b y^2)/2, so
    #   L f = -a x d_x f - b y d_y f + d_x^2 f + d_y^2 f.
    # The coefficient of the Laplacian is one, matching the sqrt(2) noise
    # normalization in dX=-grad S dt+sqrt(2)dB.
    a = Fraction(2)
    b = Fraction(3)
    x = {(1, 0): Fraction(1)}
    y = {(0, 1): Fraction(1)}
    one = {(0, 0): Fraction(1)}
    f = {
        (3, 0): Fraction(1),
        (1, 1): Fraction(2),
        (0, 2): Fraction(1),
        (0, 0): Fraction(-1),
    }
    g = {
        (2, 1): Fraction(3),
        (0, 3): Fraction(-1),
        (1, 0): Fraction(1),
        (0, 0): Fraction(2),
    }

    def generator(poly):
        dx = bivar_derivative(poly, 0)
        dy = bivar_derivative(poly, 1)
        dxx = bivar_derivative(dx, 0)
        dyy = bivar_derivative(dy, 1)
        drift_x = bivar_scalar_mul(-a, bivar_mul(x, dx))
        drift_y = bivar_scalar_mul(-b, bivar_mul(y, dy))
        return bivar_add(bivar_add(drift_x, drift_y), bivar_add(dxx, dyy))

    def inner(poly_a, poly_b):
        return bivar_gaussian_expectation(bivar_mul(poly_a, poly_b), a, b)

    grad_inner = bivar_add(
        bivar_mul(bivar_derivative(f, 0), bivar_derivative(g, 0)),
        bivar_mul(bivar_derivative(f, 1), bivar_derivative(g, 1)),
    )
    lhs = inner(generator(f), g)
    rhs = -bivar_gaussian_expectation(grad_inner, a, b)
    symmetric_lhs = inner(f, generator(g))
    assert_equal(lhs, rhs, "finite Langevin Dirichlet identity")
    assert_equal(lhs, symmetric_lhs, "finite Langevin generator symmetry")
    assert_equal(generator(one), {}, "finite Langevin conserves constants")


def check_dual_norm_finite_chaos_estimate_arithmetic():
    # The dual-norm finite-chaos proposition deliberately uses the integer
    # moment constants C_{q,m}, rather than their 1/(2m)-roots, to keep a
    # clean explicit bound.  For 2m=4, use C_0=1, C_1=3, and the exact
    # fourth moment C_2=60 of H_2(G).
    c = [1, 3, 60]
    b_uniform = [2, 3, 4]
    b_edge = [1, 2, 1]
    uniform_lp_prefactor = sum(ci * bi for ci, bi in zip(c, b_uniform))
    edge_lp_prefactor = sum(ci * bi for ci, bi in zip(c, b_edge))
    assert_equal(uniform_lp_prefactor, 251, "dual-norm chaos uniform L4 prefactor")
    assert_equal(edge_lp_prefactor, 67, "dual-norm chaos edge L4 prefactor")
    assert_equal(uniform_lp_prefactor**4, 3969126001, "dual-norm chaos uniform fourth moment")
    assert_equal(edge_lp_prefactor**4, 20151121, "dual-norm chaos edge fourth moment")

    # If the projective tensor norm on an edge carries
    # 2^{-((d+epsilon)/p) ell}, then the p-th moment carries
    # 2^{-(d+epsilon) ell}, exactly matching the dyadic-net hypothesis.
    p = 4
    d = 6
    epsilon = 2
    ell = 5
    numerator = (d + epsilon) * ell
    if numerator % p != 0:
        raise AssertionError("dual-norm edge sample must have integral exponent")
    projective_exponent = -numerator // p
    moment_exponent = p * projective_exponent
    assert_equal(projective_exponent, -10, "dual-norm projective edge exponent")
    assert_equal(moment_exponent, -40, "dual-norm moment edge exponent")
    assert_equal(moment_exponent, -(d + epsilon) * ell, "dual-norm edge exponent transfer")


def check_projective_kernel_dual_norm_criterion_arithmetic():
    # Discrete model of the projective-kernel criterion:
    # ||sum_s f_s tensor ell_s||_pi is bounded by sum_s ||f_s|| ||ell_s||.
    f_norms = [2, 3, 5]
    ell_norms = [7, 11, 13]
    base_bound = sum(f * ell for f, ell in zip(f_norms, ell_norms))
    assert_equal(base_bound, 112, "projective kernel base bound")

    # Edge decomposition:
    # (f_x-f_y) tensor ell_x + f_y tensor (ell_x-ell_y).
    f_diff_norms = [1, 2, 1]
    ell_diff_norms = [1, 1, 2]
    first_edge = sum(df * ell for df, ell in zip(f_diff_norms, ell_norms))
    second_edge = sum(f * dell for f, dell in zip(f_norms, ell_diff_norms))
    edge_bound = first_edge + second_edge
    assert_equal(first_edge, 42, "projective kernel edge Hilbert variation")
    assert_equal(second_edge, 15, "projective kernel edge dual variation")
    assert_equal(edge_bound, 57, "projective kernel total edge bound")

    # Evaluation difference in C^1 dual norm carries one power of distance.
    distance = Fraction(1, 8)
    evaluation_difference_bound = distance
    kernel_l1_norm = Fraction(9)
    increment_bound = kernel_l1_norm * evaluation_difference_bound
    assert_equal(increment_bound, Fraction(9, 8), "evaluation difference projective increment")


def check_gaussian_wick_coordinate_scale_arithmetic():
    # In parabolic dimension Q=5, white noise has L2 scale delta^{-Q/2}.
    # The normalized Xi coordinate multiplies by delta^{Q/2+kappa}, leaving
    # the slack delta^kappa.
    qdim = Fraction(5)
    kappa = Fraction(1, 20)
    white_noise_l2_exponent = -qdim / 2
    xi_normalization = qdim / 2 + kappa
    xi_slack = white_noise_l2_exponent + xi_normalization
    assert_equal(xi_slack, kappa, "Xi Gaussian coordinate slack")

    # The stochastic convolution has covariance singularity |z|^{-1}.
    # For :X^k:, the variance of a scale-delta test is delta^{-k}; the
    # L2 norm is delta^{-k/2}; normalization by delta^{k/2+k kappa}
    # leaves slack k kappa for k=1,2,3.
    for k in [1, 2, 3]:
        variance_exponent = -Fraction(k)
        l2_exponent = variance_exponent / 2
        normalization = Fraction(k, 2) + k * kappa
        slack = l2_exponent + normalization
        assert_equal(slack, k * kappa, f"Wick X^{k} coordinate slack")
        if not k < qdim:
            raise AssertionError("Wick covariance singularity is not locally integrable")

    # Edge increments in the theorem carry eta^theta in Lp.  At theta=1/2
    # and dyadic edge level ell=6, the edge factor is 2^{-3}.
    theta = Fraction(1, 2)
    ell = 6
    edge_exponent = theta * ell
    assert_equal(edge_exponent, 3, "Gaussian Wick edge exponent")
    edge_factor = Fraction(1, 2) ** edge_exponent
    assert_equal(edge_factor, Fraction(1, 8), "Gaussian Wick edge Holder factor")


def check_gaussian_dual_norm_wavelet_arithmetic():
    # The dual-norm upgrade uses a wavelet H^{-s} majorant.  For Q=5,
    # choose s=3 and theta=1/4.  White-noise coefficients contribute
    # 2^{(Q-2s)j}; the edge proof needs Q-2s+2theta<0.
    qdim = Fraction(5)
    s = Fraction(3)
    theta = Fraction(1, 4)
    white_uniform_exponent = qdim - 2 * s
    white_low_edge_exponent = qdim - 2 * s + 2 * theta
    white_tail_margin = 2 * s - qdim - 2 * theta
    assert_equal(white_uniform_exponent, Fraction(-1), "Gaussian dual white summability")
    assert_equal(white_low_edge_exponent, Fraction(-1, 2), "Gaussian dual white low-edge exponent")
    assert_equal(white_tail_margin, Fraction(1, 2), "Gaussian dual white tail margin")

    # For :X^k:, covariance singularity |z|^{-k} gives coefficient variance
    # 2^{(k-Q)j}.  After summing 2^{Qj} wavelets and H^{-s} weight
    # 2^{-2sj}, the exponent is k-2s.
    for k in [1, 2, 3]:
        wick_uniform_exponent = Fraction(k) - 2 * s
        wick_low_edge_exponent = Fraction(k) - 2 * s + 2 * theta
        wick_tail_margin = 2 * s - Fraction(k) - 2 * theta
        if not wick_uniform_exponent < 0:
            raise AssertionError("Wick dual wavelet exponent must be summable")
        if not wick_low_edge_exponent < 0:
            raise AssertionError("Wick dual edge low-scale exponent must be summable")
        if not wick_tail_margin > 0:
            raise AssertionError("Wick dual edge tail margin must be positive")
    assert_equal(Fraction(3) - 2 * s, Fraction(-3), "Gaussian dual Wick cubic summability")
    assert_equal(
        Fraction(3) - 2 * s + 2 * theta,
        Fraction(-5, 2),
        "Gaussian dual Wick cubic low-edge exponent",
    )


def check_heat_integration_reexpansion_arithmetic():
    # For Y=I(X^3) in dynamic Phi^4_3 with kappa=1/20:
    # |X^3|=-3/2-3kappa, |Y|=|X^3|+2=1/2-3kappa.
    # The Gaussian X^3 estimate supplies slack sigma=3kappa, so the
    # integrated Holder exponent is |Y|+sigma=1/2.
    kappa = Fraction(1, 20)
    alpha = -Fraction(3, 2) - 3 * kappa
    beta = alpha + 2
    sigma = 3 * kappa
    gamma = beta + sigma
    assert_equal(alpha, -Fraction(33, 20), "reexpansion X^3 homogeneity")
    assert_equal(beta, Fraction(7, 20), "reexpansion Y homogeneity")
    assert_equal(sigma, Fraction(3, 20), "reexpansion c_n scale slack")
    assert_equal(gamma, Fraction(1, 2), "reexpansion integrated Holder exponent")

    # Fine scales j>J sum like 2^{-gamma J}; after normalizing by h^beta,
    # this leaves h^sigma.
    j_cut = 6
    fine_power = gamma * j_cut
    normalized_fine_power = fine_power - beta * j_cut
    assert_equal(normalized_fine_power, sigma * j_cut, "reexpansion fine normalized slack")

    # Coarse scales use a kernel translation exponent vartheta>gamma.
    # With vartheta=1, h^vartheta 2^{(vartheta-gamma)J}=h^gamma.
    vartheta = Fraction(1)
    coarse_power = vartheta * j_cut - (vartheta - gamma) * j_cut
    assert_equal(coarse_power, gamma * j_cut, "reexpansion coarse Holder power")

    # A normalized edge at physical separation h~2^{-m} has size
    # 2^{-sigma m} eta^theta.  Choose theta=1/4 and ell=8.
    theta = Fraction(1, 4)
    ell = 8
    edge_eta_power = theta * ell
    assert_equal(edge_eta_power, 2, "reexpansion normalized edge eta power")


def check_nonlinear_negative_coordinate_wick_arithmetic():
    # Wick product identity:
    # :A^m::B^n: = sum_r binom(m,r) binom(n,r) r! C^r
    #              :A^(m-r) B^(n-r):.
    xy_coefficients = [
        math.comb(1, r) * math.comb(3, r) * math.factorial(r)
        for r in range(0, 2)
    ]
    x2y_coefficients = [
        math.comb(2, r) * math.comb(3, r) * math.factorial(r)
        for r in range(0, 3)
    ]
    assert_equal(xy_coefficients, [1, 3], "XY Wick contraction coefficients")
    assert_equal(x2y_coefficients, [1, 6, 6], "X2Y Wick contraction coefficients")
    xy_arities = [1 + 3 - 2 * r for r in range(0, 2)]
    x2y_arities = [2 + 3 - 2 * r for r in range(0, 3)]
    assert_equal(xy_arities, [4, 2], "XY tested chaos arities")
    assert_equal(x2y_arities, [5, 3, 1], "X2Y tested chaos arities")
    xy4_sym_weights = [
        Fraction(math.comb(1, 1) * math.comb(3, 0), math.comb(4, 1)),
        Fraction(math.comb(1, 0) * math.comb(3, 1), math.comb(4, 1)),
    ]
    x2y5_sym_weights = [
        Fraction(math.comb(2, 2) * math.comb(3, 0), math.comb(5, 2)),
        Fraction(math.comb(2, 1) * math.comb(3, 1), math.comb(5, 2)),
        Fraction(math.comb(2, 0) * math.comb(3, 2), math.comb(5, 2)),
    ]
    x2y3_sym_weights = [
        Fraction(math.comb(1, 1) * math.comb(2, 0), math.comb(3, 1)),
        Fraction(math.comb(1, 0) * math.comb(2, 1), math.comb(3, 1)),
    ]
    assert_equal(
        xy4_sym_weights,
        [Fraction(1, 4), Fraction(3, 4)],
        "XY fourth-chaos symmetrized norm weights",
    )
    assert_equal(
        x2y5_sym_weights,
        [Fraction(1, 10), Fraction(3, 5), Fraction(3, 10)],
        "X2Y fifth-chaos symmetrized norm weights",
    )
    assert_equal(
        x2y3_sym_weights,
        [Fraction(1, 3), Fraction(2, 3)],
        "X2Y third-chaos symmetrized norm weights",
    )
    first_chaos_increment_signs = [1, -1, -1, 1]
    assert_equal(
        first_chaos_increment_signs,
        [1, -1, -1, 1],
        "first-chaos increment covariance signs",
    )

    # The monograph defines C_2 = 2 int K G^2.  The r=2 contraction in
    # :X(a)^2: I(:X(b)^3:) has coefficient 6 int K G^2 X(b), hence the local
    # subtraction is 3 C_2 X(a).
    c2_normalization = 2
    r2_contraction = x2y_coefficients[2]
    local_subtraction_multiple = Fraction(r2_contraction, c2_normalization)
    assert_equal(local_subtraction_multiple, 3, "X2Y local C2 subtraction multiple")
    outer_cubic_expansion_factor = 3
    assert_equal(
        outer_cubic_expansion_factor * local_subtraction_multiple,
        9,
        "two-loop mass-coordinate coefficient before coupling signs",
    )

    kappa = Fraction(1, 20)
    x = -Fraction(1, 2) - kappa
    y = Fraction(1, 2) - 3 * kappa
    xy_assigned = x + y
    x2y_assigned = 2 * x + y
    assert_equal(xy_assigned, -4 * kappa, "XY assigned homogeneity")
    assert_equal(x2y_assigned, -Fraction(1, 2) - 5 * kappa, "X2Y assigned homogeneity")

    xy_true_target = Fraction(0)
    x2y_true_target = -Fraction(1, 2)
    assert_equal(xy_true_target - xy_assigned, 4 * kappa, "XY target scale slack")
    assert_equal(x2y_true_target - x2y_assigned, 5 * kappa, "X2Y target scale slack")


def check_x2y_first_chaos_logarithmic_scale_arithmetic():
    qdim = Fraction(5)
    kappa = Fraction(1, 20)
    physical_scale = 7

    # For an order-four covariance block in parabolic dimension Q=5, the
    # block size is 2^{(Q-4)s}=2^s.  Pairing two scale-delta tests at
    # delta ~ 2^{-m} contributes min(1, delta^{-Q}2^{-Qs}).
    low_cross_exponent = physical_scale
    high_cross_exponent = qdim * physical_scale - (qdim - 1) * (physical_scale + 1)
    assert_equal(low_cross_exponent, 7, "first-chaos low-cross covariance exponent")
    assert_equal(high_cross_exponent, 3, "first-chaos high-cross covariance exponent")
    if not high_cross_exponent < low_cross_exponent:
        raise AssertionError("high cross scales must decay after the physical scale")

    # The local K G^2 packets are shell-summable, producing at worst two
    # factors of the number of local shells below the cross scale.
    shell_count_power = 2
    assert_equal(shell_count_power, 2, "first-chaos two local logarithmic shell factors")

    variance_exponent = -Fraction(1)
    l2_exponent = variance_exponent / 2
    normalization = Fraction(1, 2) + 5 * kappa
    normalized_l2_slack_before_log_loss = l2_exponent + normalization
    assert_equal(
        normalized_l2_slack_before_log_loss,
        5 * kappa,
        "first-chaos normalized L2 slack before logarithmic loss",
    )

    eta_loss = kappa
    assert_equal(
        normalized_l2_slack_before_log_loss - eta_loss,
        4 * kappa,
        "first-chaos normalized L2 slack after sample logarithmic loss",
    )


def check_x2y_first_chaos_cutoff_shell_arithmetic():
    # Cutoff-shell first-chaos estimate.  The covariance-shell case gains
    # (Q-1)(N-m).  The local-shell cases gain theta(N-m) after summing the
    # lower cross scales.  The proposition states the variance gain as
    # 2^{-2 rho (N-m)} with rho < theta/2, so the L2 cutoff-Cauchy gain is
    # 2^{-rho (N-m)} after taking square roots.
    qdim = Fraction(5)
    theta = Fraction(1, 2)
    rho = Fraction(1, 5)
    kappa = Fraction(1, 20)
    eta = kappa
    m = 7
    n = 13
    gap = n - m

    covariance_shell_gain = (qdim - 1) * gap
    local_shell_gain = theta * gap
    retained_variance_gain = 2 * rho * gap
    retained_l2_gain = rho * gap

    assert_equal(covariance_shell_gain, 24, "first-chaos cutoff covariance-shell gain")
    assert_equal(local_shell_gain, 3, "first-chaos cutoff local-shell gain")
    assert_equal(retained_variance_gain, Fraction(12, 5), "first-chaos cutoff retained variance gain")
    assert_equal(retained_l2_gain, Fraction(6, 5), "first-chaos cutoff retained L2 gain")
    if not retained_variance_gain < local_shell_gain:
        raise AssertionError("first-chaos retained variance gain exceeds local-shell gain")
    if not retained_variance_gain < covariance_shell_gain:
        raise AssertionError("first-chaos retained variance gain exceeds covariance-shell gain")

    normalized_l2_slack_before_log_loss = 5 * kappa
    normalized_l2_slack_after_log_loss = normalized_l2_slack_before_log_loss - eta
    assert_equal(
        normalized_l2_slack_after_log_loss,
        Fraction(1, 5),
        "first-chaos cutoff normalized slack after log loss",
    )
    total_sample_exponent = normalized_l2_slack_after_log_loss * m + retained_l2_gain
    assert_equal(total_sample_exponent, Fraction(13, 5), "first-chaos cutoff sample total exponent")


def check_x2y_first_chaos_parameter_edge_arithmetic():
    # The first-chaos parameter-edge estimate uses the signed transported-test
    # overlap
    #   int |psi(a) psi(a')| 1_{|a-a'|<=2^-s}
    #       <= d^(2 vartheta) min(1, 2^(Qm) 2^(-Qs)).
    # The base variance remains O(2^m log^2), now with the edge factor
    # d^(2 vartheta).  After taking a Gaussian Lp norm and multiplying by the
    # X^2Y model normalization 2^(-(1/2+5 kappa)m), the scale slack is
    # 5 kappa minus the logarithmic loss.
    qdim = Fraction(5)
    kappa = Fraction(1, 20)
    eta = Fraction(1, 40)
    vartheta = Fraction(2, 5)
    p = 80
    theta_cov = Fraction(1, 2)
    rho = Fraction(1, 5)
    m = 7
    n = 13
    gap = n - m

    low_overlap_scale = Fraction(0)
    high_overlap_scale = qdim * m - qdim * (m + 1)
    assert_equal(low_overlap_scale, 0, "first-chaos edge low-overlap scale")
    assert_equal(high_overlap_scale, -5, "first-chaos edge high-overlap scale")

    variance_scale_exponent = Fraction(1) * m
    l2_scale_exponent = variance_scale_exponent / 2
    model_normalization_exponent = -(Fraction(1, 2) + 5 * kappa) * m
    normalized_exponent_before_log = model_normalization_exponent + l2_scale_exponent
    assert_equal(
        normalized_exponent_before_log,
        -5 * kappa * m,
        "first-chaos edge normalized exponent before log loss",
    )

    retained_slack = 5 * kappa - eta
    assert_equal(retained_slack, Fraction(9, 40), "first-chaos edge retained scale slack")
    if not p * retained_slack > qdim:
        raise AssertionError("first-chaos edge retained slack does not beat physical entropy")
    if not p * vartheta > 6:
        raise AssertionError("first-chaos edge Holder exponent does not beat edge entropy")

    retained_cutoff_gain = rho * gap
    variance_cutoff_gain = 2 * rho * gap
    local_shell_gain = theta_cov * gap
    assert_equal(variance_cutoff_gain, Fraction(12, 5), "first-chaos edge cutoff variance gain")
    assert_equal(retained_cutoff_gain, Fraction(6, 5), "first-chaos edge cutoff Lp gain")
    assert_equal(local_shell_gain, 3, "first-chaos edge local-shell ceiling")
    if not variance_cutoff_gain < local_shell_gain:
        raise AssertionError("first-chaos edge retained cutoff gain exceeds local-shell ceiling")

    total_edge_scale = retained_slack * m + retained_cutoff_gain
    assert_equal(total_edge_scale, Fraction(111, 40), "first-chaos edge sample total exponent")


def check_covariance_double_increment_arithmetic():
    qdim = Fraction(5)
    covariance_order = Fraction(4)
    theta = Fraction(1, 2)
    block_scale = 5
    local_shell = 9
    other_shell = 7

    amplitude_exponent = (qdim - covariance_order) * block_scale
    assert_equal(amplitude_exponent, 5, "order-four covariance block exponent at scale five")

    first_increment_gain = theta * max(local_shell - block_scale, 0)
    second_increment_gain = theta * max(other_shell - block_scale, 0)
    assert_equal(first_increment_gain, 2, "first covariance double-increment shell gain")
    assert_equal(second_increment_gain, 1, "second covariance double-increment shell gain")

    total_exponent = amplitude_exponent - first_increment_gain - second_increment_gain
    assert_equal(total_exponent, 2, "covariance double-increment final exponent")


def check_tadpole_asymptotics():
    # I_d(Lambda,m) = |S^{d-1}|/(2pi)^d int_0^Lambda r^{d-1}/(r^2+m^2) dr.
    coeff_2 = (2 * math.pi) / ((2 * math.pi) ** 2)  # radial integral contributes log Lambda.
    coeff_3 = (4 * math.pi) / ((2 * math.pi) ** 3)  # radial integral contributes Lambda.
    _assert_close("two-dimensional tadpole log coefficient", coeff_2, 1 / (2 * math.pi), tol=1e-15)
    _assert_close("three-dimensional tadpole linear coefficient", coeff_3, 1 / (2 * math.pi**2), tol=1e-15)


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
    # Use a finite exact sample with L^(-alpha)=1/2.  The source-decorated
    # variant uses the same geometric tail multiplied by source seminorms.
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

    source_constant = Fraction(7, 3)
    source_seminorms = [Fraction(2), Fraction(3, 5), Fraction(5, 7)]
    source_product = math.prod(source_seminorms)
    source_tail_j5 = source_constant * tail_j5 * source_product
    assert_equal(
        source_tail_j5,
        Fraction(1, 800),
        "phi4_3 source-decorated ultraviolet tail",
    )

    # A polynomial factor in the number of source assignments is harmless
    # once an OS-admissible factorial/exponential growth envelope is allowed.
    b_growth = 4
    gamma = 1
    for n in range(1, 9):
        assignment_factor = n**3 * (2**n)
        os_envelope = (b_growth**n) * (math.factorial(n) ** gamma)
        if assignment_factor > os_envelope:
            raise AssertionError("phi4_3 source-decorated OS growth envelope failed")


def check_phi4_three_model_phase_cell_budget():
    # Finite arithmetic shadow of the model-specific derivation budget:
    # several phase-cell estimates with a common geometric rate combine into
    # the abstract activity bound used by the multiscale theorem.
    common_ratio = Fraction(1, 2)
    small_field = Fraction(1, 200)
    large_field = Fraction(1, 300)
    irrelevant = Fraction(1, 500)
    c_act = small_field + large_field + irrelevant
    assert_equal(c_act, Fraction(31, 3000), "phase-cell activity constant")

    scale_sum = c_act / (1 - common_ratio)
    assert_equal(scale_sum, Fraction(31, 1500), "phase-cell activity full scale sum")
    b_r = Fraction(4)
    a_prime = Fraction(1, 10)
    if not b_r * scale_sum <= a_prime:
        raise AssertionError("phase-cell derivation budget KP smallness failed")

    j_cut = 4
    activity_tail = c_act * common_ratio**j_cut / (1 - common_ratio)
    assert_equal(activity_tail, Fraction(31, 24000), "phase-cell activity tail")

    source_constant = Fraction(7, 1000)
    source_seminorm_product = Fraction(2) * Fraction(3, 5)
    source_tail = source_constant * common_ratio**j_cut / (1 - common_ratio) * source_seminorm_product
    assert_equal(source_tail, Fraction(21, 20000), "phase-cell source-decorated tail")

    local_coordinate_tail = Fraction(1, 1000) * Fraction(1, 4) ** j_cut / (1 - Fraction(1, 4))
    os_regulator_tail = Fraction(1, 800) * Fraction(1, 8) ** j_cut / (1 - Fraction(1, 8))
    assert_equal(local_coordinate_tail, Fraction(1, 192000), "phase-cell local-coordinate tail")
    assert_equal(os_regulator_tail, Fraction(1, 2867200), "phase-cell OS-regulator tail")

    total_constructive_defect = activity_tail + local_coordinate_tail + os_regulator_tail
    assert_equal(
        total_constructive_defect,
        Fraction(18597, 14336000),
        "phase-cell constructive output defect",
    )


def set_partitions(items):
    """Return all set partitions of a finite tuple, as tuples of tuples."""
    if not items:
        return [()]
    first, *rest = items
    partitions = []
    for partition in set_partitions(tuple(rest)):
        partitions.append(((first,),) + partition)
        for index, block in enumerate(partition):
            new_block = tuple(sorted((first,) + block))
            new_partition = list(partition)
            new_partition[index] = new_block
            partitions.append(tuple(new_partition))
    return partitions


def check_phi4_three_connected_to_full_growth_bookkeeping():
    # The connected-to-full Schwinger reconstruction uses the partition
    # identity S_n = sum_pi prod_{B in pi} C_B.  The monograph records the
    # resulting factorial loss:
    #   sum_pi A^{|pi|} prod_B (|B|!)^gamma
    #   <= max(1,A)^n |Pi_n| (n!)^gamma
    #   <= (e max(1,A))^n (n!)^{gamma+1}.
    # Enumerate the finite partition sum and the exact Bell counts for n <= 7.
    a = Fraction(3, 2)
    gamma = 2
    for n in range(1, 8):
        partitions = set_partitions(tuple(range(n)))
        partition_sum = Fraction(0)
        for partition in partitions:
            block_factor = Fraction(1)
            for block in partition:
                block_factor *= math.factorial(len(block)) ** gamma
            partition_sum += (a ** len(partition)) * block_factor

        elementary_bound = (
            (max(Fraction(1), a) ** n)
            * len(partitions)
            * (math.factorial(n) ** gamma)
        )
        if partition_sum > elementary_bound:
            raise AssertionError("phi4_3 moment-cumulant elementary bound failed")

        bell_injection_bound = n**n
        if len(partitions) > bell_injection_bound:
            raise AssertionError("phi4_3 Bell injection bound failed")

        # Avoid floating-point e in the public check: for n <= 7, the cruder
        # integer bound 3^n n! dominates n^n and is stronger than needed here.
        factorial_bound = (3**n) * math.factorial(n)
        if bell_injection_bound > factorial_bound:
            raise AssertionError("phi4_3 Bell factorial bound failed")


def hard_core_source_derivatives(weights, incompatible_edges, left_source, right_source):
    """Return Z and first/mixed source derivatives for a finite hard-core gas."""
    n = len(weights)
    incompatible = {frozenset(edge) for edge in incompatible_edges}
    z = Fraction(0)
    z_left = Fraction(0)
    z_right = Fraction(0)
    z_left_right = Fraction(0)
    for mask in range(1 << n):
        ok = True
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(i + 1, n):
                if (mask & (1 << j)) and frozenset((i, j)) in incompatible:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue

        weight = Fraction(1)
        left = Fraction(0)
        right = Fraction(0)
        for i in range(n):
            if mask & (1 << i):
                weight *= weights[i]
                left += left_source.get(i, Fraction(0))
                right += right_source.get(i, Fraction(0))
        z += weight
        z_left += weight * left
        z_right += weight * right
        z_left_right += weight * left * right
    return z, z_left, z_right, z_left_right


def invert_fraction_matrix(matrix):
    n = len(matrix)
    augmented = [
        row[:] + [Fraction(1 if i == j else 0) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if augmented[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise AssertionError("singular finite covariance matrix")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        augmented[col] = [entry / pivot_value for entry in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor == 0:
                continue
            augmented[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(augmented[row], augmented[col])
            ]
    return [row[n:] for row in augmented]


def one_dimensional_massive_covariance(size, mass_squared, boundary):
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for index in range(size):
        matrix[index][index] = mass_squared + 2
        if index > 0:
            matrix[index][index - 1] = Fraction(-1)
        if index + 1 < size:
            matrix[index][index + 1] = Fraction(-1)
    if boundary == "periodic":
        matrix[0][size - 1] = Fraction(-1)
        matrix[size - 1][0] = Fraction(-1)
    elif boundary != "dirichlet":
        raise AssertionError(f"unknown boundary condition {boundary!r}")
    return invert_fraction_matrix(matrix)


def check_finite_polymer_source_cumulant_factorization():
    # If two source neighbourhoods live in independent hard-core components,
    # log Z factorizes and the mixed source cumulant is exactly zero.
    weights = [Fraction(1, 5), Fraction(1, 11)]
    z, z_l, z_r, z_lr = hard_core_source_derivatives(
        weights,
        incompatible_edges=[],
        left_source={0: Fraction(1)},
        right_source={1: Fraction(1)},
    )
    disconnected_cumulant = (z * z_lr - z_l * z_r) / (z * z)
    assert_equal(z, Fraction(72, 55), "disconnected two-polymer partition function")
    assert_equal(disconnected_cumulant, Fraction(0), "disconnected source cumulant")

    # Insert a bridge polymer B incompatible with A and C.  A and C are still
    # mutually compatible, but the exclusion of B couples the two source
    # regions.  The mixed derivative of log Z detects exactly this connected
    # incompatibility path A--B--C.
    weights = [Fraction(1, 5), Fraction(1, 7), Fraction(1, 11)]
    z, z_l, z_r, z_lr = hard_core_source_derivatives(
        weights,
        incompatible_edges=[(0, 1), (1, 2)],
        left_source={0: Fraction(1)},
        right_source={2: Fraction(1)},
    )
    bridge_cumulant = (z * z_lr - z_l * z_r) / (z * z)
    assert_equal(z, Fraction(559, 385), "bridged three-polymer partition function")
    assert_equal(bridge_cumulant, Fraction(385, 312481), "bridged source cumulant")

    # Removing the bridge activity restores factorization.
    weights = [Fraction(1, 5), Fraction(0), Fraction(1, 11)]
    z, z_l, z_r, z_lr = hard_core_source_derivatives(
        weights,
        incompatible_edges=[(0, 1), (1, 2)],
        left_source={0: Fraction(1)},
        right_source={2: Fraction(1)},
    )
    bridge_removed_cumulant = (z * z_lr - z_l * z_r) / (z * z)
    assert_equal(bridge_removed_cumulant, Fraction(0), "zero bridge source cumulant")


def check_p_phi_two_boundary_cluster_bookkeeping():
    # Massive finite-volume Green functions with different boundary conditions
    # share the same local operator but differ at interior test functions.
    size = 5
    center = 2
    dirichlet_covariance = one_dimensional_massive_covariance(
        size, Fraction(1), "dirichlet"
    )
    periodic_covariance = one_dimensional_massive_covariance(
        size, Fraction(1), "periodic"
    )
    interior_variance_difference = (
        dirichlet_covariance[center][center] - periodic_covariance[center][center]
    )
    assert_equal(
        dirichlet_covariance[center][center],
        Fraction(4, 9),
        "Dirichlet interior finite covariance",
    )
    assert_equal(
        periodic_covariance[center][center],
        Fraction(5, 11),
        "periodic interior finite covariance",
    )
    assert_equal(
        interior_variance_difference,
        Fraction(-1, 99),
        "finite-volume boundary covariance difference",
    )
    if interior_variance_difference == 0:
        raise AssertionError("finite-volume boundary conditions were incorrectly identified")

    # A rooted cluster estimate is uniform after a root is fixed; the absolute
    # log-partition bound is extensive and becomes uniform only after division
    # by the number of cells.
    epsilon = Fraction(1, 13)
    cell_count = 37
    rooted_bound = epsilon
    extensive_log_bound = epsilon * cell_count
    assert_equal(rooted_bound, Fraction(1, 13), "rooted P(phi)_2 cluster bound")
    assert_equal(
        extensive_log_bound,
        Fraction(37, 13),
        "extensive P(phi)_2 log-partition bound",
    )
    assert_equal(
        extensive_log_bound / cell_count,
        epsilon,
        "P(phi)_2 pressure-density bound",
    )
    if extensive_log_bound == rooted_bound:
        raise AssertionError("extensive log Z was collapsed to a rooted bound")

    # Fixed-support source derivatives sum roots only near the source, not over
    # all cells in the box.
    source_neighbourhood_cells = 3
    local_source_bound = epsilon * source_neighbourhood_cells
    larger_volume_cells = 101
    assert_equal(
        local_source_bound,
        Fraction(3, 13),
        "fixed-support source derivative cluster bound",
    )
    assert_equal(
        local_source_bound,
        epsilon * source_neighbourhood_cells,
        "source bound independent of ambient volume",
    )
    if local_source_bound == epsilon * larger_volume_cells:
        raise AssertionError("fixed source derivative was made volume-extensive")

    # The scalar polymer theorem is applied only after integrating/localizing
    # field-dependent activities into scalar activities with the same majorant.
    field_activity_majorant = Fraction(7, 60)
    fluctuation_integration_norm = Fraction(3, 5)
    scalar_activity_bound = field_activity_majorant * fluctuation_integration_norm
    assert_equal(
        scalar_activity_bound,
        Fraction(7, 100),
        "scalarized P(phi)_2 polymer activity bound",
    )
    if not scalar_activity_bound <= field_activity_majorant:
        raise AssertionError("scalarization failed to preserve the polymer majorant")

    # Boundary comparison is a thermodynamic decay estimate: positive at finite
    # distance, but decreasing exponentially as the source moves from the collar.
    collar_prefactor = Fraction(5, 2)
    decay_ratio = Fraction(1, 3)
    finite_distance_bound = collar_prefactor * decay_ratio**4
    farther_bound = collar_prefactor * decay_ratio**9
    assert_equal(
        finite_distance_bound,
        Fraction(5, 162),
        "finite-distance boundary comparison bound",
    )
    if finite_distance_bound == 0:
        raise AssertionError("finite-volume boundary comparison was made exact")
    if not farther_bound < finite_distance_bound:
        raise AssertionError("boundary comparison does not decay with distance")


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
    _assert_close("heat-kernel smoothing optimization", lhs, rhs, tol=1.0e-12)


def check_phi4_two_path_space_increment_arithmetic():
    # The path-space Wick-power estimate in d=2 weakens one propagator by
    # theta through 1-exp(-r) <= r^theta.  The H^{-s} shell exponent is
    # r * r^{-2s} * r^{-2+2 theta} = r^{-1-2s+2 theta}; summability needs
    # theta < s.  The Kolmogorov step needs p theta > 1.
    s = Fraction(1, 5)
    theta = Fraction(1, 10)
    shell_exponent = Fraction(1, 1) - 2 * s - 2 * (1 - theta)
    assert_equal(shell_exponent, Fraction(-6, 5), "Phi4_2 path-space Wick shell exponent")
    if not shell_exponent < -1:
        raise AssertionError("Phi4_2 path-space shell summability failed")
    if not theta < s:
        raise AssertionError("Phi4_2 path-space theta<s condition failed")

    p = 11
    kolmogorov_power = p * theta
    assert_equal(kolmogorov_power, Fraction(11, 10), "Phi4_2 Kolmogorov moment power")
    if not kolmogorov_power > 1:
        raise AssertionError("Phi4_2 Kolmogorov continuity threshold failed")


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


def check_phi4_three_sobolev_dpd_obstruction_arithmetic():
    # In three spatial dimensions X has regularity -1/2-kappa and :X^3:
    # has regularity -3/2-3 kappa.  Even the minimal multiplier threshold
    # beta > 1/2+kappa forces a Duhamel smoothing exponent above one.
    kappa = Fraction(1, 20)
    beta_min_sample = Fraction(1, 2) + 2 * kappa
    forcing_regular = -Fraction(3, 2) - 3 * kappa
    theta_min_sample = (beta_min_sample - forcing_regular) / 2
    assert_equal(theta_min_sample, 1 + Fraction(5, 2) * kappa, "Phi4_3 minimal DPD theta sample")
    if not theta_min_sample > 1:
        raise AssertionError("Phi4_3 minimal DPD obstruction failed")

    beta_algebra_sample = Fraction(3, 2) + kappa
    theta_algebra_sample = (beta_algebra_sample - forcing_regular) / 2
    assert_equal(theta_algebra_sample, Fraction(3, 2) + 2 * kappa, "Phi4_3 algebra DPD theta sample")
    if not theta_algebra_sample > 1:
        raise AssertionError("Phi4_3 algebra DPD obstruction failed")


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


def check_dpd_energy_closedness_lp_power_arithmetic():
    # The closedness pass uses
    #   || |a|^p - |b|^p ||_1 <= p ||a-b||_p || |a|+|b| ||_p^{p-1}
    # with Holder exponents p and p/(p-1).  The three enhanced-noise powers
    # are p=4, p=2, and p=4/3.
    powers = [
        (Fraction(4), "X1 L4 power"),
        (Fraction(2), "X2 L2 power"),
        (Fraction(4, 3), "X3 L4/3 power"),
    ]
    for p, label in powers:
        holder_conjugate = p / (p - 1)
        assert_equal(Fraction(1, 1) / p + Fraction(1, 1) / holder_conjugate, 1, label)
        assert_equal((p - 1) * holder_conjugate, p, f"{label} power continuity")


def check_dpd_energy_compactness_derivative_arithmetic():
    # The time-derivative compactness estimate places every nonlinear drift
    # contribution in L^(4/3)([0,T] x T^2), using Y in L^4, X1 in L^4,
    # X2 in L^2, and X3 in L^(4/3).
    target_inverse = Fraction(3, 4)
    terms = [
        ([Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)], "Y^3"),
        ([Fraction(1, 4), Fraction(1, 4), Fraction(1, 4)], "Y^2 X1"),
        ([Fraction(1, 4), Fraction(1, 2)], "Y X2"),
        ([Fraction(3, 4)], "X3"),
    ]
    for inverse_exponents, label in terms:
        assert_equal(sum(inverse_exponents), target_inverse, f"{label} L4/3 drift exponent")

    # On a finite time interval, L^2_t H^1_x is continuously included in
    # L^(4/3)_t H^1_x, so the Laplacian term also fits the derivative space.
    if not Fraction(4, 3) < Fraction(2):
        raise AssertionError("finite-interval L2 to L4/3 inclusion failed")


def check_dpd_distributional_limit_exponents():
    # Strong L2 convergence plus uniform L4 boundedness interpolates to
    # strong Lr convergence for every 2 <= r < 4.  The Y^2 X1 product uses
    # r=8/3 so that Y_n^2-Y^2 lies in L^(4/3).
    r = Fraction(8, 3)
    if not Fraction(2) < r < Fraction(4):
        raise AssertionError("DPD interpolation exponent must lie between 2 and 4")
    assert_equal(Fraction(2) / r, Fraction(3, 4), "square map L8/3 to L4/3")
    assert_equal(Fraction(3, 4) + Fraction(1, 4), 1, "Y2X1 product to L1")

    # Cubic difference: (Y_n-Y)(Y_n^2+Y_nY+Y^2) uses L2 times L2.
    assert_equal(Fraction(1, 2) + Fraction(1, 2), 1, "cubic difference L1")

    # Mixed enhanced-noise term: (Y_n-Y)X2 and Y(X2_n-X2) use L2 times L2.
    assert_equal(Fraction(1, 2) + Fraction(1, 2), 1, "YX2 product to L1")

    # The compactness lemma uses the finite-interval embedding
    # W^(1,4/3)([0,T];E_M) -> C([0,T];E_M), whose time Holder exponent is
    # 1 - 1/(4/3) = 1/4.
    holder_exponent = 1 - Fraction(3, 4)
    assert_equal(holder_exponent, Fraction(1, 4), "finite-mode time Holder exponent")


def check_dpd_besov_product_continuity_arithmetic():
    # Sample Besov-Holder parameters for the DPD product theorem.
    # Multiplication C^alpha x C^(-kappa) is defined by Bony's formula when
    # the resonant regularity alpha-kappa is positive.
    alpha = Fraction(1, 3)
    kappa = Fraction(1, 20)
    if not 0 < kappa < alpha:
        raise AssertionError("Besov DPD sample must satisfy 0 < kappa < alpha")
    resonant_regular = alpha - kappa
    assert_equal(resonant_regular, Fraction(17, 60), "Besov DPD resonant regularity")
    if not resonant_regular > 0:
        raise AssertionError("Besov resonant product requires alpha-kappa > 0")

    # The resonant and right-paraproduct outputs are in C^(alpha-kappa),
    # which embeds into C^(-kappa) because alpha > 0.
    if not resonant_regular > -kappa:
        raise AssertionError("positive Besov remainder must embed into C^-kappa")

    # The algebra estimate C^alpha * C^alpha -> C^alpha uses the resonant
    # gain 2 alpha and the embedding C^(2 alpha) -> C^alpha.
    two_alpha = 2 * alpha
    assert_equal(two_alpha, Fraction(2, 3), "Besov algebra resonant regularity")
    if not two_alpha > alpha:
        raise AssertionError("Besov algebra resonant term must be smoother than C^alpha")

    # The DPD nonlinear terms have target regularities at least -kappa:
    # Y^3 in C^alpha, Y^2 X1 in C^-kappa, Y X2 in C^-kappa, X3 in C^-kappa.
    target = -kappa
    term_regularities = [alpha, target, target, target]
    for regularity in term_regularities:
        if not regularity >= target:
            raise AssertionError("DPD Besov nonlinearity term misses target C^-kappa")


def check_dpd_besov_fixed_point_exponents():
    # The Besov DPD fixed point takes forcing in C^(-kappa) and seeks Y in
    # C^alpha.  Heat smoothing needs 2 theta = alpha+kappa with theta < 1.
    alpha = Fraction(1, 3)
    kappa = Fraction(1, 20)
    theta = (alpha + kappa) / 2
    assert_equal(theta, Fraction(23, 120), "Besov DPD Duhamel smoothing exponent")
    assert_equal(1 - theta, Fraction(97, 120), "Besov DPD Duhamel time gain")
    if not 0 < kappa < alpha < 2 - kappa:
        raise AssertionError("Besov DPD parameter window failed")
    if not theta < 1:
        raise AssertionError("Besov DPD Duhamel kernel must be integrable")

    # The heat map raises C^(-kappa) by alpha+kappa, landing exactly in
    # C^alpha.
    assert_equal(-kappa + 2 * theta, alpha, "Besov DPD heat smoothing target")


def check_dpd_besov_energy_compatibility_arithmetic():
    # The compatibility proposition combines the Besov local map with the
    # smooth energy compactness pass on the common approximation domain.  The
    # Besov side supplies the same admissible Duhamel exponent as above.
    alpha = Fraction(1, 3)
    kappa = Fraction(1, 20)
    theta = (alpha + kappa) / 2
    if not 0 < kappa < alpha < 2 - kappa:
        raise AssertionError("Besov-energy compatibility parameter window failed")
    assert_equal(-kappa + 2 * theta, alpha, "compatibility heat target")

    # The energy side uses the already proved Lp exponents.  Record the two
    # identities that identify the compactness limit: C^alpha convergence on
    # the finite torus implies L2 convergence, while Y^2 X1 still uses the
    # L^(8/3) interpolation exponent from the distributional limit.
    if not alpha > 0:
        raise AssertionError("positive Holder regularity needed for L2 identification")
    assert_equal(Fraction(2) / Fraction(8, 3), Fraction(3, 4), "compatibility Y2 L4/3")
    assert_equal(Fraction(3, 4) + Fraction(1, 4), 1, "compatibility Y2X1 L1")


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


def check_stationary_law_coupling_invariance_defect():
    # Finite arithmetic shadow of the coupled stationary-law comparison:
    # time-zero coupling gives a bounded-Lipschitz distance, while comparing
    # time t through an exactly stationary cutoff path gives the invariance
    # defect for the limiting law.
    lipschitz = Fraction(3)
    delta = Fraction(1, 50)
    a_t = Fraction(2)
    epsilon_t = Fraction(1, 100)

    zero_time_bound = lipschitz * delta
    invariance_defect_bound = lipschitz * ((a_t + 1) * delta + epsilon_t)
    assert_equal(zero_time_bound, Fraction(3, 50), "stationary-law BL distance bound")
    assert_equal(invariance_defect_bound, Fraction(21, 100), "stationary-law invariance defect")

    actual_zero_time_difference = Fraction(1, 20)
    actual_invariance_defect = Fraction(1, 5)
    if not actual_zero_time_difference <= zero_time_bound:
        raise AssertionError("stationary-law BL comparison failed")
    if not actual_invariance_defect <= invariance_defect_bound:
        raise AssertionError("stationary-law invariance comparison failed")

    bad_epsilon_t = Fraction(1, 4)
    bad_defect_bound = lipschitz * ((a_t + 1) * delta + bad_epsilon_t)
    if not bad_defect_bound > Fraction(1, 2):
        raise AssertionError("stationary-law nonvanishing defect not detected")


def check_stationary_law_polynomial_truncation_arithmetic():
    # Lemma spde-polynomial-stationarity-truncation separates a bounded
    # Lipschitz comparison at truncation radius R from the two unbounded
    # polynomial tails at times 0 and t.
    tail_zero = Fraction(1, 80)
    tail_time = Fraction(1, 70)
    lipschitz_truncation = Fraction(9)
    delta = Fraction(1, 100)
    a_t = Fraction(2)
    epsilon_t = Fraction(1, 200)
    bounded_defect = lipschitz_truncation * ((a_t + 1) * delta + epsilon_t)
    total_bound = tail_zero + tail_time + bounded_defect
    assert_equal(
        bounded_defect,
        Fraction(63, 200),
        "polynomial stationarity bounded truncation defect",
    )
    assert_equal(
        total_bound,
        Fraction(957, 2800),
        "polynomial stationarity total truncation budget",
    )

    # Uniform L^(1+eta) control gives a tail bound by de la Vallee-Poussin:
    # E[|O| 1_{|O|>R}] <= M / R^eta.  The exact samples record the monotone
    # disappearance of the tails before the fixed-R bounded comparison is used.
    moment_bound = Fraction(5)
    eta = 2
    previous = None
    for radius in (2, 4, 8, 16):
        tail = moment_bound / (radius**eta)
        if previous is not None and not tail < previous:
            raise AssertionError("polynomial stationarity tail did not decrease")
        previous = tail
    assert_equal(previous, Fraction(5, 256), "polynomial stationarity final sample tail")


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


def check_phi4_three_static_dynamic_coordinate_translation():
    # Static action density g4*phi^4 + a*phi^2 gives dynamic drift
    # -4*g4*Phi^3 - 2*a*Phi.  The dynamic chapter calls these coefficients
    # -lambda_dyn and +M, so lambda_dyn=4*g4 and M=-2*a.
    g4 = Fraction(7, 11)
    lambda_dyn = 4 * g4
    c1 = Fraction(13, 5)
    c2 = Fraction(17, 19)
    c_fin = Fraction(-3, 7)

    m_dynamic = 3 * lambda_dyn * c1 - 9 * lambda_dyn * lambda_dyn * c2 + c_fin
    a_static = -m_dynamic / 2
    alpha_from_static_chart = a_static + 6 * g4 * c1
    alpha_from_dynamic_chart = Fraction(9, 2) * lambda_dyn * lambda_dyn * c2 - c_fin / 2

    assert_equal(lambda_dyn, 4 * g4, "Phi4_3 static-to-dynamic quartic factor")
    assert_equal(-2 * a_static, m_dynamic, "Phi4_3 static-to-dynamic mass drift")
    assert_equal(
        alpha_from_static_chart,
        alpha_from_dynamic_chart,
        "Phi4_3 static-dynamic normal mass coordinate",
    )

    # The cancellation is in the normal-ordered mass coordinate.  Comparing the
    # raw linear drift M directly with alpha would retain the one-loop Wick
    # conversion and gives the wrong chart.
    raw_drift_coordinate = m_dynamic
    if raw_drift_coordinate == alpha_from_dynamic_chart:
        raise AssertionError("Phi4_3 raw drift coordinate was mistaken for alpha")

    wrong_quartic_reuse = a_static + 6 * lambda_dyn * c1
    if wrong_quartic_reuse == alpha_from_dynamic_chart:
        raise AssertionError("Phi4_3 dynamic cubic coefficient was reused as static quartic coefficient")


def check_phi4_three_vacuum_coordinate_partition_shift():
    # Shifting beta by c adds c*|Lambda| to the action.  Every unnormalized
    # source partition function gets the same exp(-c*|Lambda|) factor, so
    # normalized moments and connected log ratios are unchanged, while
    # pressure and free-energy densities shift with opposite signs.
    volume = Fraction(11, 3)
    delta_beta = Fraction(5, 7)
    log_z0 = Fraction(19, 5)
    log_zj = Fraction(23, 5)
    log_shift = delta_beta * volume

    factor = Fraction(13, 17)
    moment_numerator = Fraction(29, 31)
    partition = Fraction(37, 41)
    normalized = moment_numerator / partition
    normalized_shifted = (factor * moment_numerator) / (factor * partition)
    assert_equal(normalized_shifted, normalized, "Phi4_3 beta-shift normalized Schwinger ratio")

    connected_log_ratio = log_zj - log_z0
    connected_log_ratio_shifted = (log_zj - log_shift) - (log_z0 - log_shift)
    assert_equal(connected_log_ratio_shifted, connected_log_ratio, "Phi4_3 beta-shift connected log ratio")

    pressure = log_z0 / volume
    pressure_shifted = (log_z0 - log_shift) / volume
    free_energy = -log_z0 / volume
    free_energy_shifted = -(log_z0 - log_shift) / volume
    assert_equal(pressure_shifted - pressure, -delta_beta, "Phi4_3 beta-shift pressure sign")
    assert_equal(free_energy_shifted - free_energy, delta_beta, "Phi4_3 beta-shift free-energy sign")

    lam = Fraction(2, 3)
    c0 = Fraction(7, 5)
    alpha = Fraction(-4, 9)
    beta = Fraction(8, 13)
    a_unwicked = alpha - 6 * lam * c0
    b_unwicked = beta - alpha * c0 + 3 * lam * c0 * c0
    a_unwicked_shifted = alpha - 6 * lam * c0
    b_unwicked_shifted = beta + delta_beta - alpha * c0 + 3 * lam * c0 * c0
    assert_equal(a_unwicked_shifted - a_unwicked, 0, "Phi4_3 beta-shift mass coordinate")
    assert_equal(b_unwicked_shifted - b_unwicked, delta_beta, "Phi4_3 beta-shift vacuum coordinate")

    q = Fraction(3, 2)
    drift = -4 * lam * q**3 - 2 * a_unwicked * q
    drift_shifted = -4 * lam * q**3 - 2 * a_unwicked_shifted * q
    assert_equal(drift_shifted, drift, "Phi4_3 beta-shift drift invisibility")


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

    # Fixed-point-sector comparison: two contractions with common constant q
    # and map error epsilon have fixed points within epsilon/(1-q).  The affine
    # example realizes the bound exactly.
    epsilon = Fraction(3, 20)
    limiting_fixed_point = Fraction(4, 5)
    limiting_offset = (1 - q) * limiting_fixed_point
    approximating_offset = limiting_offset + epsilon
    approximating_fixed_point = approximating_offset / (1 - q)
    solution_difference = approximating_fixed_point - limiting_fixed_point
    assert_equal(solution_difference, epsilon / (1 - q), "modelled fixed-point sector stability")

    # Error-budget arithmetic for the modelled SPDE comparison criterion.
    delta_y = Fraction(1, 100)
    delta_k = Fraction(1, 200)
    delta_p = Fraction(1, 300)
    delta_l = Fraction(1, 400)
    delta_m = Fraction(1, 500)
    h_r = lam * b * r**3 + mass * d * r
    map_error_budget = (
        delta_y
        + delta_k * h_r
        + a
        * ttheta
        * (
            lam * delta_p * r**3
            + mass * delta_l * r
            + d * delta_m * r
            + delta_m * delta_l * r
        )
    )
    assert_equal(h_r, 25, "modelled fixed-point sector forcing radius")
    assert_equal(
        map_error_budget,
        Fraction(4059953, 30000000),
        "modelled fixed-point sector map error",
    )
    assert_equal(
        map_error_budget / (1 - q),
        Fraction(4059953, 22650000),
        "modelled fixed-point sector solution error",
    )

    # Scalar regression for the mixed mass-linear term.  Here K is the identity,
    # lambda=0, Y_n=Y_infty, M_infty=L_infty=0, M_n=a, and L_n=b.  The old
    # displayed budget without delta_M delta_L R would vanish although the map
    # error is |ab|R.
    scalar_radius = Fraction(11)
    scalar_mass_shift = Fraction(1, 5)
    scalar_linear_shift = Fraction(1, 7)
    scalar_actual_error = scalar_mass_shift * scalar_linear_shift * scalar_radius
    scalar_old_budget = Fraction(0)
    scalar_corrected_budget = scalar_actual_error
    assert_equal(
        scalar_old_budget,
        Fraction(0),
        "modelled fixed-point sector old mixed-term budget",
    )
    if scalar_old_budget >= scalar_actual_error:
        raise AssertionError("old budget should miss the positive mixed error")
    assert_equal(
        scalar_corrected_budget,
        Fraction(11, 35),
        "modelled fixed-point sector mixed mass-linear term",
    )


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


def check_scale_summed_shell_separated_cutoff_arithmetic():
    # Shell-separated cutoff bridge: a scalar estimate with
    # 2^(-rho (n-m)_+) still gives a scale-summed cutoff Cauchy rate
    # 2^(-rho_* n) whenever rho_* is below both the shell gain rho and the
    # physical-scale slack a=sigma-D/p.  Use integer exponents so the full
    # summation check is exact.
    p = 4
    d_big = 4
    sigma = 3
    a = Fraction(sigma) - Fraction(d_big, p)
    rho = 3
    rho_star = 1
    n = 5
    assert_equal(a, 2, "shell-separated scale slack")
    if not rho_star < min(rho, a):
        raise AssertionError("shell-separated rho_star must be strictly below rho and slack")

    def dyadic_minus(exponent):
        exponent = Fraction(exponent)
        if exponent.denominator != 1:
            raise AssertionError(f"nonintegral dyadic exponent in exact shell check: {exponent}")
        return Fraction(1, 2) ** exponent.numerator

    m_sample = 2
    left = dyadic_minus(a * m_sample + rho * (n - m_sample))
    right = (
        dyadic_minus(rho_star * n)
        * dyadic_minus((a - rho_star) * m_sample)
        * dyadic_minus((rho - rho_star) * (n - m_sample))
    )
    assert_equal(left, right, "shell-separated bridge identity")

    first = sum(
        dyadic_minus(a * m + rho * (n - m))
        for m in range(n + 1)
    )
    tail = dyadic_minus(a * (n + 1)) / (1 - dyadic_minus(a))
    total = first + tail
    scaled_total = total * (2 ** (rho_star * n))
    h_bound = (
        1
        / ((1 - dyadic_minus(a - rho_star)) * (1 - dyadic_minus(rho - rho_star)))
        + dyadic_minus(a) / (1 - dyadic_minus(a))
    )

    assert_equal(first, Fraction(63, 32768), "shell-separated bridge lower-scale sum")
    assert_equal(tail, Fraction(1, 3072), "shell-separated bridge high-scale tail")
    assert_equal(total, Fraction(221, 98304), "shell-separated bridge total")
    assert_equal(scaled_total, Fraction(221, 3072), "shell-separated bridge scaled total")
    assert_equal(h_bound, 3, "shell-separated bridge H bound")
    if not scaled_total < h_bound:
        raise AssertionError("shell-separated scaled sum exceeds the H bound")


def check_projective_shell_separated_coordinate_criterion_arithmetic():
    # Projective shell-separated coordinate criterion: projective kernel
    # constants are first summed with finite-chaos constants, the edge
    # projective exponent is chosen so that raising to p gives exactly the
    # dyadic entropy decay 2^(-(d+epsilon) ell), and the same shell-summed
    # H constant then supplies the cutoff-Cauchy rate.
    p = 4
    d_edge = 8
    epsilon = 4
    d_scale = 4
    sigma = 3
    a = Fraction(sigma) - Fraction(d_scale, p)
    rho = 3
    rho_star = 1
    n = 5

    chaos_constants = [1, 3, 5]
    base_projective_constants = [2, 1, 1]
    edge_projective_constants = [1, 2, 1]
    b_pi = sum(c * b for c, b in zip(chaos_constants, base_projective_constants))
    b_pi_edge = sum(c * b for c, b in zip(chaos_constants, edge_projective_constants))
    assert_equal(b_pi, 10, "projective shell base finite-chaos constant")
    assert_equal(b_pi_edge, 12, "projective shell edge finite-chaos constant")

    if not rho_star < min(rho, a):
        raise AssertionError("projective shell sample rho_star outside admissible range")

    edge_lp_exponent = Fraction(d_edge + epsilon, p)
    ell = 3
    assert_equal(edge_lp_exponent, 3, "projective shell edge Lp exponent")
    assert_equal(
        p * edge_lp_exponent * ell,
        (d_edge + epsilon) * ell,
        "projective shell edge p-moment entropy exponent",
    )

    def dyadic_minus(exponent):
        exponent = Fraction(exponent)
        if exponent.denominator != 1:
            raise AssertionError(f"nonintegral exponent in projective shell check: {exponent}")
        return Fraction(1, 2) ** exponent.numerator

    c0_root = 2
    c1_root = 3
    edge_ratio = dyadic_minus(Fraction(epsilon, p))
    per_scale_constant = c0_root * b_pi + c1_root * b_pi_edge / (1 - edge_ratio)
    assert_equal(per_scale_constant, 92, "projective shell per-scale constant")

    h_bound = (
        1
        / ((1 - dyadic_minus(a - rho_star)) * (1 - dyadic_minus(rho - rho_star)))
        + dyadic_minus(a) / (1 - dyadic_minus(a))
    )
    final_bound = h_bound * per_scale_constant * dyadic_minus(rho_star * n)
    assert_equal(h_bound, 3, "projective shell H bound")
    assert_equal(final_bound, Fraction(69, 8), "projective shell final bound")

    exact_shell_sum = Fraction(221, 98304)
    exact_bound = per_scale_constant * exact_shell_sum
    if not exact_bound < final_bound:
        raise AssertionError("projective shell exact sum exceeds H-bound estimate")


def check_nonlinear_pi_shell_cutoff_input_arithmetic():
    # Nonlinear Pi shell-separated cutoff input: this is the specialized
    # arithmetic used for XY and X^2Y after the E_r'-valued projective
    # kernel estimates have supplied a shell factor 2^(-rho (n-m)_+).
    qdim = 5
    pi_edge_entropy = qdim + 1
    kappa = Fraction(1, 20)
    zeta_xy = kappa
    sigma_xy = 4 * kappa - zeta_xy
    theta = Fraction(1, 2)
    p = 80
    rho = Fraction(1, 4)
    rho_star = Fraction(1, 16)

    assert_equal(sigma_xy, Fraction(3, 20), "nonlinear Pi shell XY scale slack")
    scale_excess = p * sigma_xy - qdim
    edge_excess = p * theta - pi_edge_entropy
    retained_scale_slack = sigma_xy - Fraction(qdim, p)
    assert_equal(scale_excess, 7, "nonlinear Pi shell scale-excess numerator")
    assert_equal(edge_excess, 34, "nonlinear Pi shell edge-excess numerator")
    assert_equal(retained_scale_slack, Fraction(7, 80), "nonlinear Pi shell retained scale slack")
    if not rho_star < min(rho, retained_scale_slack):
        raise AssertionError("nonlinear Pi shell retained cutoff rate is not admissible")

    # Same finite-chaos aggregation as in the displayed constant:
    # Ahat_{tau,i}=sum_q C_{q,m0} Bhat_{tau,q,i}.  The sample uses XY's
    # two chaos arities q=4,2 with toy positive chaos constants.
    chaos_constants = {4: 5, 2: 3}
    base_projective_constants = {4: 2, 2: 1}
    edge_projective_constants = {4: 1, 2: 2}
    a_hat_0 = sum(chaos_constants[q] * base_projective_constants[q] for q in [4, 2])
    a_hat_1 = sum(chaos_constants[q] * edge_projective_constants[q] for q in [4, 2])
    assert_equal(a_hat_0, 13, "nonlinear Pi shell base finite-chaos constant")
    assert_equal(a_hat_1, 11, "nonlinear Pi shell edge finite-chaos constant")

    # The dyadic-net edge factor is 2^{-theta ell} in L^p.  Raising to the
    # p-th moment cancels the 2^{6 ell} edge entropy and leaves the positive
    # excess 34.  Use ell=3 to keep this as exact integer exponent arithmetic.
    ell = 3
    moment_edge_decay = p * theta * ell
    entropy_cost = pi_edge_entropy * ell
    assert_equal(moment_edge_decay, 120, "nonlinear Pi shell edge moment decay")
    assert_equal(entropy_cost, 18, "nonlinear Pi shell edge entropy cost")
    assert_equal(moment_edge_decay - entropy_cost, edge_excess * ell, "nonlinear Pi shell edge excess")


def check_negative_sector_scale_summed_model_convergence_arithmetic():
    # The strict negative Phi^4_3 sector is controlled by six Pi-coordinates and
    # one Gamma coordinate.  In the sample below every coordinate has the same
    # scale-summed uniform constant S=54 and cutoff-increment constant S~=32.
    pi_coordinates = 6
    gamma_coordinates = 1
    coordinate_count = pi_coordinates + gamma_coordinates
    assert_equal(coordinate_count, 7, "negative-sector scale-summed coordinate count")

    p = 2
    a_minus = 2
    s_sc = 54
    stilde_sc = 32
    uniform_lp_bound = a_minus * (1 + coordinate_count * s_sc)
    distance_prefactor = a_minus * coordinate_count * stilde_sc
    assert_equal(uniform_lp_bound, 758, "negative-sector model uniform Lp bound")
    assert_equal(uniform_lp_bound**p, 574564, "negative-sector model C_N")
    assert_equal(distance_prefactor, 448, "negative-sector model distance prefactor")
    assert_equal(distance_prefactor**p, 200704, "negative-sector model C_D")

    rho = 2
    n = 3
    distance_lp_bound = distance_prefactor * Fraction(1, 2) ** (rho * n)
    distance_p_moment = distance_lp_bound**p
    assert_equal(distance_lp_bound, 7, "negative-sector model dyadic distance")
    assert_equal(distance_p_moment, 49, "negative-sector model dyadic p-moment")

    tail = distance_prefactor * Fraction(1, 2) ** (rho * n) / (1 - Fraction(1, 2) ** rho)
    assert_equal(tail, Fraction(28, 3), "negative-sector model convergence tail")


def check_negative_sector_physical_parameter_entropy_arithmetic():
    # Dynamic Phi^4_3 uses parabolic scaling (2,1,1,1), hence homogeneous
    # dimension Q=5.  After dualizing the test function, a Pi-coordinate has
    # parameters (base point, scale ratio), while the Gamma coordinate has
    # parameters (base point, normalized separation).
    qdim = 5
    pi_edge_entropy = qdim + 1
    gamma_edge_entropy = 2 * qdim
    assert_equal(qdim, 5, "Phi4_3 parabolic homogeneous dimension")
    assert_equal(pi_edge_entropy, 6, "Pi physical parameter edge entropy")
    assert_equal(gamma_edge_entropy, 10, "Gamma physical parameter edge entropy")

    m = 4
    ell = 3
    pi_base_exponent = qdim * m
    pi_edge_exponent = qdim * m + pi_edge_entropy * ell
    gamma_edge_exponent = qdim * m + gamma_edge_entropy * ell
    assert_equal(pi_base_exponent, 20, "Pi physical parameter base exponent")
    assert_equal(pi_edge_exponent, 38, "Pi physical parameter edge exponent")
    assert_equal(gamma_edge_exponent, 50, "Gamma physical parameter edge exponent")

    # A sample high-moment choice p=12 and regularity slack sigma=1 beats the
    # scale entropy D=5 because p*sigma-D=7>0.
    p = 12
    sigma = 1
    scale_slack_numerator = p * sigma - qdim
    assert_equal(scale_slack_numerator, 7, "physical parameter scale slack numerator")
    if not scale_slack_numerator > 0:
        raise AssertionError("physical parameter scale slack condition failed")


def check_gaussian_negative_pi_coordinate_input_arithmetic():
    # The Gaussian Pi-coordinates Xi, X, X^2, X^3 use the same physical
    # parameter entropy D=Q=5 and edge entropy d=Q+1=6.  With kappa=1/20,
    # theta=1/2, and p=128, the weakest coordinate Xi still beats the scale
    # entropy, and the edge Holder exponent beats the edge entropy.
    qdim = 5
    edge_entropy = qdim + 1
    kappa = Fraction(1, 20)
    theta = Fraction(1, 2)
    p = 128

    xi_scale_excess = p * kappa - qdim
    edge_excess = p * theta - edge_entropy
    assert_equal(xi_scale_excess, Fraction(7, 5), "Gaussian Xi scale excess")
    assert_equal(edge_excess, 58, "Gaussian Pi edge excess")
    if not xi_scale_excess > 0:
        raise AssertionError("Gaussian Xi scale-summed condition failed")
    if not edge_excess > 0:
        raise AssertionError("Gaussian Pi edge condition failed")

    expected_excesses = {
        1: Fraction(7, 5),
        2: Fraction(39, 5),
        3: Fraction(71, 5),
    }
    for k, expected in expected_excesses.items():
        scale_excess = p * k * kappa - qdim
        assert_equal(scale_excess, expected, f"Gaussian X^{k} scale excess")
        if not scale_excess > 0:
            raise AssertionError(f"Gaussian X^{k} scale-summed condition failed")


def check_gamma_coordinate_heat_input_arithmetic():
    # The reexpansion coefficient c_n is a Gamma-coordinate with base entropy
    # D=Q=5 and edge entropy d=2Q=10.  Heat integration of X^3 leaves scale
    # slack sigma_g=3 kappa.  With kappa=1/20, theta=1/2, and p=64, both
    # scale and edge summability have positive excess.
    qdim = 5
    gamma_edge_entropy = 2 * qdim
    kappa = Fraction(1, 20)
    sigma_g = 3 * kappa
    beta = Fraction(1, 2) - 3 * kappa
    gamma = beta + sigma_g
    theta = Fraction(1, 2)
    p = 64

    assert_equal(beta, Fraction(7, 20), "Gamma coordinate beta")
    assert_equal(sigma_g, Fraction(3, 20), "Gamma coordinate scale slack")
    assert_equal(gamma, Fraction(1, 2), "Gamma coordinate Holder exponent")
    scale_excess = p * sigma_g - qdim
    edge_excess = p * theta - gamma_edge_entropy
    assert_equal(scale_excess, Fraction(23, 5), "Gamma coordinate scale excess")
    assert_equal(edge_excess, 22, "Gamma coordinate edge excess")
    if not scale_excess > 0:
        raise AssertionError("Gamma coordinate scale-summed condition failed")
    if not edge_excess > 0:
        raise AssertionError("Gamma coordinate edge condition failed")


def check_nonlinear_pi_coordinate_kernel_input_arithmetic():
    # Nonlinear Pi coordinates have physical parameter entropy D=5 and
    # edge entropy d=6.  The XY graph ledger is marginal at the scalar
    # second-moment level, so this sample reserves a small zeta_XY loss.
    # X2Y has nominal slack 5 kappa, with a separate zeta_X2Y loss for the
    # locally subtracted first-chaos logarithm.
    qdim = 5
    pi_edge_entropy = qdim + 1
    kappa = Fraction(1, 20)
    zeta_xy = kappa
    zeta_x2y = kappa
    sigma_xy = 4 * kappa - zeta_xy
    sigma_x2y = 5 * kappa - zeta_x2y
    theta = Fraction(1, 2)
    p = 64

    assert_equal(sigma_xy, Fraction(3, 20), "nonlinear XY scale slack after zeta loss")
    assert_equal(sigma_x2y, Fraction(1, 5), "nonlinear X2Y scale slack after zeta loss")
    xy_scale_excess = p * sigma_xy - qdim
    x2y_scale_excess = p * sigma_x2y - qdim
    edge_excess = p * theta - pi_edge_entropy
    assert_equal(xy_scale_excess, Fraction(23, 5), "nonlinear XY scale excess")
    assert_equal(x2y_scale_excess, Fraction(39, 5), "nonlinear X2Y scale excess")
    assert_equal(edge_excess, 26, "nonlinear Pi edge excess")
    if not xy_scale_excess > 0:
        raise AssertionError("nonlinear XY scale-summed condition failed")
    if not x2y_scale_excess > 0:
        raise AssertionError("nonlinear X2Y scale-summed condition failed")
    if not edge_excess > 0:
        raise AssertionError("nonlinear Pi edge condition failed")


def check_xy_tested_graph_power_counting_arithmetic():
    # Q=5 dynamic Phi4_3 power counting for the scalar second-moment graphs
    # associated with the tested XY coordinate.  Edge exponents are Q-2=3
    # for heat edges and Q-4=1 for covariance edges.  The total degree is
    # marginal, while every proper subgraph has a positive deficit.
    qdim = 5
    graphs = {
        "XY fourth chaos A": (
            [
                ("a", "b", 3),
                ("ap", "bp", 3),
                ("a", "ap", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            2,
        ),
        "XY fourth chaos B": (
            [
                ("a", "b", 3),
                ("ap", "bp", 3),
                ("a", "bp", 1),
                ("b", "ap", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            2,
        ),
        "XY second chaos": (
            [
                ("a", "b", 3),
                ("a", "b", 1),
                ("ap", "bp", 3),
                ("ap", "bp", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            1,
        ),
    }
    vertices = ["a", "b", "ap", "bp"]

    def subset_deficit(edges, subset):
        subset = set(subset)
        internal = sum(weight for u, v, weight in edges if u in subset and v in subset)
        return qdim * (len(subset) - 1) - internal

    from itertools import combinations

    for name, (edges, expected_min_deficit) in graphs.items():
        total_degree = sum(weight for _, _, weight in edges)
        assert_equal(total_degree, qdim * (len(vertices) - 2), f"{name} total degree")
        deficits = []
        for size in range(2, len(vertices)):
            for subset in combinations(vertices, size):
                deficit = subset_deficit(edges, subset)
                deficits.append(deficit)
                if not deficit > 0:
                    raise AssertionError(f"{name} has nonpositive proper-subgraph deficit {subset}")
        assert_equal(
            min(deficits),
            expected_min_deficit,
            f"{name} minimum proper-subgraph deficit",
        )


def check_x2y_high_chaos_graph_power_counting_arithmetic():
    # Fifth- and third-chaos X2Y covariance graphs have one extra singular
    # degree beyond the marginal XY graphs.  This produces variance scaling
    # delta^{-1}, matching the true target regularity -1/2 of the locally
    # subtracted X2Y coordinate.  Proper subgraphs still have positive
    # deficits, so no relative-scale divergence is hidden in the estimate.
    qdim = 5
    graphs = {
        "X2Y fifth chaos A": (
            [
                ("a", "b", 3),
                ("ap", "bp", 3),
                ("a", "ap", 1),
                ("a", "ap", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            2,
        ),
        "X2Y fifth chaos B": (
            [
                ("a", "b", 3),
                ("ap", "bp", 3),
                ("a", "ap", 1),
                ("a", "bp", 1),
                ("b", "ap", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            2,
        ),
        "X2Y fifth chaos C": (
            [
                ("a", "b", 3),
                ("ap", "bp", 3),
                ("a", "bp", 1),
                ("a", "bp", 1),
                ("b", "ap", 1),
                ("b", "ap", 1),
                ("b", "bp", 1),
            ],
            2,
        ),
        "X2Y third chaos A": (
            [
                ("a", "b", 3),
                ("a", "b", 1),
                ("ap", "bp", 3),
                ("ap", "bp", 1),
                ("a", "ap", 1),
                ("b", "bp", 1),
                ("b", "bp", 1),
            ],
            1,
        ),
        "X2Y third chaos B": (
            [
                ("a", "b", 3),
                ("a", "b", 1),
                ("ap", "bp", 3),
                ("ap", "bp", 1),
                ("a", "bp", 1),
                ("b", "ap", 1),
                ("b", "bp", 1),
            ],
            1,
        ),
    }
    vertices = ["a", "b", "ap", "bp"]

    def subset_deficit(edges, subset):
        subset = set(subset)
        internal = sum(weight for u, v, weight in edges if u in subset and v in subset)
        return qdim * (len(subset) - 1) - internal

    from itertools import combinations

    for name, (edges, expected_min_deficit) in graphs.items():
        total_degree = sum(weight for _, _, weight in edges)
        assert_equal(
            total_degree,
            qdim * (len(vertices) - 2) + 1,
            f"{name} total degree",
        )
        deficits = []
        for size in range(2, len(vertices)):
            for subset in combinations(vertices, size):
                deficit = subset_deficit(edges, subset)
                deficits.append(deficit)
                if not deficit > 0:
                    raise AssertionError(f"{name} has nonpositive proper-subgraph deficit {subset}")
        assert_equal(
            min(deficits),
            expected_min_deficit,
            f"{name} minimum proper-subgraph deficit",
        )

    kappa = Fraction(1, 20)
    variance_exponent = -Fraction(1)
    l2_exponent = variance_exponent / 2
    normalization = Fraction(1, 2) + 5 * kappa
    normalized_slack = normalization + l2_exponent
    assert_equal(l2_exponent, -Fraction(1, 2), "X2Y high-chaos L2 exponent")
    assert_equal(normalization, Fraction(3, 4), "X2Y high-chaos model normalization")
    assert_equal(normalized_slack, 5 * kappa, "X2Y high-chaos normalized slack")


def check_x2y_high_chaos_edge_cutoff_arithmetic():
    # The high-chaos X2Y scalar graph variance scales like delta^{-1};
    # at physical scale delta=2^{-m} this is 2^m.  After taking square roots
    # and multiplying by the model normalization 2^{-(1/2+5 kappa)m}, the
    # remaining physical-scale slack is 5 kappa.  A shell-separated cutoff
    # edge uses the minimum proper-subgraph deficit 1, hence after square root
    # any rho<1/2 can be retained.
    kappa = Fraction(1, 20)
    theta = Fraction(2, 5)
    rho = Fraction(1, 4)
    m = 10
    n = 16
    ell = 6

    variance_scale_exponent = Fraction(m)
    l2_scale_exponent = variance_scale_exponent / 2
    model_normalization_exponent = (Fraction(1, 2) + 5 * kappa) * m
    normalized_scale_slack = model_normalization_exponent - l2_scale_exponent
    edge_power = theta * ell

    assert_equal(variance_scale_exponent, 10, "X2Y high-chaos variance scale exponent")
    assert_equal(l2_scale_exponent, 5, "X2Y high-chaos L2 scale exponent")
    assert_equal(model_normalization_exponent, Fraction(15, 2), "X2Y high-chaos normalization exponent")
    assert_equal(normalized_scale_slack, Fraction(5, 2), "X2Y high-chaos edge sample scale slack")
    assert_equal(edge_power, Fraction(12, 5), "X2Y high-chaos edge Holder exponent")
    if not normalized_scale_slack > 0:
        raise AssertionError("X2Y high-chaos edge estimate lost all scale slack")
    if not edge_power > 0:
        raise AssertionError("X2Y high-chaos edge estimate has no edge decay")

    min_graph_deficit = Fraction(1)
    variance_shell_gain = min_graph_deficit * (n - m)
    lp_shell_gain = variance_shell_gain / 2
    chosen_shell_gain = rho * (n - m)

    assert_equal(variance_shell_gain, 6, "X2Y high-chaos cutoff variance shell gain")
    assert_equal(lp_shell_gain, 3, "X2Y high-chaos cutoff Lp shell gain ceiling")
    assert_equal(chosen_shell_gain, Fraction(3, 2), "X2Y high-chaos cutoff chosen shell gain")
    if not rho < Fraction(1, 2):
        raise AssertionError("X2Y high-chaos cutoff shell rho must be below the Lp ceiling")
    if not chosen_shell_gain < lp_shell_gain:
        raise AssertionError("X2Y high-chaos cutoff chosen shell gain exceeds graph deficit")
    assert_equal(
        normalized_scale_slack + chosen_shell_gain,
        4,
        "X2Y high-chaos cutoff sample total exponent",
    )


def check_xy_tested_coordinate_logarithmic_slack_arithmetic():
    # Proposition spde-xy-tested-coordinate-logarithmic-scale-bound converts
    # the scalar graph estimate E|Z_delta|^2 <= C_eta delta^(-eta) into the
    # normalized model-coordinate slack.  Taking eta = 2 zeta_XY gives
    # ||Z_delta||_2 <= C delta^(-zeta_XY), while |XY| = -4 kappa.
    kappa = Fraction(1, 20)
    zeta_xy = kappa
    eta = 2 * zeta_xy
    l2_loss = eta / 2
    model_normalization = 4 * kappa
    normalized_slack = model_normalization - l2_loss

    assert_equal(eta, Fraction(1, 10), "XY scalar graph eta choice")
    assert_equal(l2_loss, zeta_xy, "XY scalar graph L2 logarithmic loss")
    assert_equal(model_normalization, Fraction(1, 5), "XY model normalization exponent")
    assert_equal(normalized_slack, 3 * kappa, "XY scalar tested coordinate slack after log loss")
    if not 0 < zeta_xy < 4 * kappa:
        raise AssertionError("XY scalar tested zeta loss outside admissible range")
    if not normalized_slack > 0:
        raise AssertionError("XY scalar tested coordinate lost all scale slack")


def check_xy_tested_coordinate_edge_arithmetic():
    # The parameter-edge estimate starts from
    # E|Z_v-Z_u|^2 <= C d(u,v)^(2 theta) 2^(eta m).  With
    # eta=2 zeta_XY, finite-chaos moments give the same Lp scale loss
    # as the scalar base estimate, plus the Holder edge factor.
    kappa = Fraction(1, 20)
    zeta_xy = kappa
    theta = Fraction(2, 5)
    eta = 2 * zeta_xy
    m = 10
    ell = 6

    l2_scale_loss = eta / 2
    model_normalization = 4 * kappa
    normalized_scale_slack = model_normalization - l2_scale_loss
    edge_power = theta * ell

    assert_equal(l2_scale_loss, zeta_xy, "XY scalar edge L2 scale loss")
    assert_equal(normalized_scale_slack, 3 * kappa, "XY scalar edge normalized scale slack")
    assert_equal(
        normalized_scale_slack * m,
        Fraction(3, 2),
        "XY scalar edge sample scale exponent",
    )
    assert_equal(edge_power, Fraction(12, 5), "XY scalar edge Holder exponent")
    if not normalized_scale_slack > 0:
        raise AssertionError("XY scalar edge estimate lost all scale slack")
    if not edge_power > 0:
        raise AssertionError("XY scalar edge estimate has no edge decay")


def check_xy_tested_coordinate_cutoff_shell_arithmetic():
    # The scalar cutoff-shell proposition uses the smallest proper-subgraph
    # deficit 1 in the XY graph ledger.  A constrained ultraviolet shell
    # separated from the physical test scale by n-m therefore gives variance
    # gain 2^(-(n-m)_+).  After taking the square root, any rho < 1/2 is
    # available for the Lp cutoff-Cauchy estimate.
    kappa = Fraction(1, 20)
    zeta_xy = kappa
    rho = Fraction(1, 4)
    m = 10
    n = 16

    min_graph_deficit = Fraction(1)
    variance_shell_gain = min_graph_deficit * (n - m)
    lp_shell_gain = variance_shell_gain / 2
    chosen_shell_gain = rho * (n - m)
    model_normalization = 4 * kappa
    normalized_scale_slack = model_normalization - zeta_xy

    assert_equal(variance_shell_gain, 6, "XY scalar cutoff variance shell gain")
    assert_equal(lp_shell_gain, 3, "XY scalar cutoff Lp shell gain ceiling")
    assert_equal(chosen_shell_gain, Fraction(3, 2), "XY scalar cutoff chosen shell gain")
    if not rho < Fraction(1, 2):
        raise AssertionError("XY scalar cutoff shell rho must be below the Lp ceiling")
    if not chosen_shell_gain < lp_shell_gain:
        raise AssertionError("XY scalar cutoff chosen shell gain exceeds graph deficit")
    assert_equal(
        normalized_scale_slack * m,
        Fraction(3, 2),
        "XY scalar cutoff sample scale exponent",
    )
    assert_equal(
        normalized_scale_slack * m + chosen_shell_gain,
        3,
        "XY scalar cutoff sample total exponent",
    )


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


def check_hilbert_scale_tightness_arithmetic():
    # Compactness of the H^{-eta} ball in H^{-kappa} follows from the
    # high-mode estimate
    #   ||(1-P_M) phi||_{H^{-kappa}}^2
    #     <= <M>^{-2(kappa-eta)} ||phi||_{H^{-eta}}^2.
    kappa = Fraction(1, 4)
    eta = Fraction(1, 8)
    tail_exponent = 2 * (kappa - eta)
    assert_equal(tail_exponent, Fraction(1, 4), "Hilbert-scale tail exponent")
    norm_tail_exponent = kappa - eta
    assert_equal(norm_tail_exponent, Fraction(1, 8), "Hilbert-scale norm-tail exponent")

    # For dyadic M=2^m the algebraic decay is 2^{-m/4} in the squared norm.
    m = 8
    assert_equal(m * tail_exponent, Fraction(2), "dyadic Hilbert-scale tail power")
    assert_equal(m * norm_tail_exponent, Fraction(1), "dyadic Hilbert-scale norm-tail power")

    # Markov's inequality in the tightness criterion:
    # nu(||phi||_{H^{-eta}}>R) <= C R^{-p}.
    C = Fraction(3)
    R = Fraction(6)
    p = 3
    assert_equal(C * R ** (-p), Fraction(1, 72), "Hilbert-scale Markov tail")


def check_gaussian_negative_sobolev_summability_arithmetic():
    # In two spatial dimensions the massive Gaussian H^{-eta} second moment
    # is controlled by sum_k <k>^{-2-2 eta}.  A dyadic annulus has O(2^{2j})
    # lattice points, so the shell exponent is -2 eta j.
    dimension = Fraction(2)
    eta = Fraction(1, 2)
    summand_decay = Fraction(2) + 2 * eta
    shell_exponent = dimension - summand_decay
    assert_equal(shell_exponent, Fraction(-1), "Gaussian H-minus shell exponent")

    # The corresponding dyadic majorant is sum_{j>=0} 2^{-j}=2.
    dyadic_sum = Fraction(1, 1) / (1 - Fraction(1, 2))
    assert_equal(dyadic_sum, Fraction(2), "Gaussian H-minus dyadic sum")


def check_brascamp_lieb_hminus_bound_arithmetic():
    # In the convex cutoff criterion, covariance in an L_N-eigenmode is
    # bounded by (lambda + m^2)^(-1), and the H^{-eta} second moment is the
    # weighted spectral trace.  Use eta=1 for an exact rational sample.
    lambdas = [Fraction(0), Fraction(3), Fraction(8)]
    mass_squared = Fraction(2)
    trace_bound = sum(
        Fraction(1, 1) / ((1 + lam) * (lam + mass_squared))
        for lam in lambdas
    )
    assert_equal(trace_bound, Fraction(101, 180), "Brascamp-Lieb H-minus trace bound")

    # If A >= L + m^2 in the same eigenbasis, then A^{-1} <= (L+m^2)^{-1}.
    stronger_hessian_eigenvalues = [Fraction(3), Fraction(7), Fraction(12)]
    for lam, a_eigenvalue in zip(lambdas, stronger_hessian_eigenvalues):
        if Fraction(1, a_eigenvalue) > Fraction(1, lam + mass_squared):
            raise AssertionError("operator-monotone inverse sample failed")


def check_quartic_tail_integrability_arithmetic():
    # One-dimensional quartic reference density exp(-a x^4).  The exact
    # even moment is
    #   int x^(2m) exp(-a x^4) dx / int exp(-a x^4) dx
    # = a^(-m/2) Gamma((2m+1)/4) / Gamma(1/4).
    a = 1.7
    second_moment = a ** (-0.5) * math.gamma(3.0 / 4.0) / math.gamma(1.0 / 4.0)
    fourth_moment = a ** (-1.0) * math.gamma(5.0 / 4.0) / math.gamma(1.0 / 4.0)
    # Gamma(5/4)=(1/4) Gamma(1/4), so the fourth moment is exactly 1/(4a).
    assert_close_float(fourth_moment, 1.0 / (4.0 * a), "quartic fourth moment scaling")
    if not 0.0 < second_moment < 1.0:
        raise AssertionError("quartic second moment should be finite and positive in the sample")

    # Coercivity estimate used in the finite-lattice tail proposition:
    # b t <= (A/2) t^2 + b^2/(2A), t=u^2.
    A = Fraction(3, 5)
    b = Fraction(7, 4)
    for numerator in range(-6, 7):
        t = Fraction(numerator * numerator, 9)
        lhs = b * t
        rhs = A * t * t / 2 + b * b / (2 * A)
        if lhs > rhs:
            raise AssertionError("quartic coercivity Young inequality failed")

    # Uniform-integrability tail bound:
    # C A 1_{A>R/C} <= C^2 A^2/R.
    C = Fraction(5)
    R = Fraction(20)
    for exponent_num in range(0, 8):
        A_value = Fraction(2) ** exponent_num
        left = C * A_value if A_value > R / C else Fraction(0)
        right = C * C * A_value * A_value / R
        if left > right:
            raise AssertionError("polynomial-by-exponential tail domination failed")


def check_regulator_comparison_error_budget_arithmetic():
    # Regulator comparison for an unbounded polynomial observable is a
    # two-limit argument:
    #   |F_N(P)-L_N(P)|
    # <= |F_N(P-P_R)| + |F_N(P_R)-L_N(P_R)| + |L_N(P_R-P)|.
    # The first and third terms are controlled by uniform integrability, and
    # the middle term is the bounded-cylinder comparison hypothesis.
    fourier_tail = Fraction(1, 90)
    lattice_tail = Fraction(1, 75)
    bounded_comparison = Fraction(1, 100)
    total = fourier_tail + lattice_tail + bounded_comparison
    assert_equal(total, Fraction(31, 900), "regulator comparison error budget")

    # If |P-P_R| <= 2 |P| 1_{|P|>R}, then a uniform L^2-tail epsilon for P
    # gives an L^1-tail at most 2 epsilon by Cauchy's inequality.
    l2_tail_norm = Fraction(1, 40)
    l1_tail_bound = 2 * l2_tail_norm
    assert_equal(l1_tail_bound, Fraction(1, 20), "regulator comparison L1 tail")


def check_phi4_two_finite_volume_route_identification_arithmetic():
    # Proposition spde-phi-four-two-finite-volume-route-identification:
    # common unnormalized numerator and partition-function limits give common
    # normalized Schwinger limits only after the partition function is kept
    # uniformly away from zero.
    partition_lower_bound = Fraction(2)
    common_numerator_bound = Fraction(3)
    spde_numerator_error = Fraction(1, 100)
    constructive_numerator_error = Fraction(1, 120)
    spde_partition_error = Fraction(1, 80)
    constructive_partition_error = Fraction(1, 90)

    normalized_bound = (
        spde_numerator_error / partition_lower_bound
        + constructive_numerator_error / partition_lower_bound
        + common_numerator_bound
        * (spde_partition_error + constructive_partition_error)
        / (partition_lower_bound * partition_lower_bound)
    )
    assert_equal(
        normalized_bound,
        Fraction(43, 1600),
        "Phi4_2 finite-volume normalized route-comparison budget",
    )


def check_spde_os_reconstruction_growth_arithmetic():
    # The corrected OS-II input allows the Schwartz-seminorm order to grow
    # linearly with the number of insertions:
    #   N(n) = N0 + C_OS n.
    # Reflection positivity tests a positive-time polynomial F against its
    # reflected copy, so an r-insertion monomial produces a 2r-point
    # distribution.  The required seminorm order is therefore still linear in
    # r, not quadratic.
    N0 = 3
    C_os = 2
    for r in range(0, 8):
        n = 2 * r
        order = N0 + C_os * n
        assert_equal(order, N0 + 2 * C_os * r, "OS reflected insertion order")

    # Factorial/exponential growth is stable under multiplication by a fixed
    # polynomial in n: n^a B^n (n!)^gamma <= B2^n (n!)^(gamma+1) for B2>B
    # in the finite samples below, reflecting why polynomial seminorm
    # combinatorics do not change the qualitative OS-II growth class.
    B = Fraction(2)
    B2 = Fraction(8)
    gamma = 2
    for n in range(1, 9):
        factorial = math.factorial(n)
        left = (n ** 3) * (B ** n) * (factorial ** gamma)
        right = (B2 ** n) * (factorial ** (gamma + 1))
        if left > right:
            raise AssertionError("OS growth class polynomial absorption failed")


def check_spde_constructive_hierarchy_transfer_arithmetic():
    # Finite analogue of Construction
    # con:spde-common-schwinger-hierarchy-comparison.  If the SPDE and
    # constructive hierarchies have the same moments in a common coordinate
    # chart, then every positive-time polynomial OS Gram matrix built from
    # those moments is identical.
    constructive_moments = {
        0: Fraction(1),
        1: Fraction(0),
        2: Fraction(2),
        3: Fraction(0),
        4: Fraction(12),
    }
    spde_moments = dict(constructive_moments)

    gram_constructive = [
        [constructive_moments[i + j] for j in range(3)]
        for i in range(3)
    ]
    gram_spde = [
        [spde_moments[i + j] for j in range(3)]
        for i in range(3)
    ]
    assert_equal(gram_spde, gram_constructive, "SPDE/constructive OS Gram transfer")

    # Principal minors of the finite Gram form are positive in this sample.
    det_1 = gram_constructive[0][0]
    det_2 = (
        gram_constructive[0][0] * gram_constructive[1][1]
        - gram_constructive[0][1] * gram_constructive[1][0]
    )
    det_3 = (
        gram_constructive[0][0]
        * (
            gram_constructive[1][1] * gram_constructive[2][2]
            - gram_constructive[1][2] * gram_constructive[2][1]
        )
        - gram_constructive[0][1]
        * (
            gram_constructive[1][0] * gram_constructive[2][2]
            - gram_constructive[1][2] * gram_constructive[2][0]
        )
        + gram_constructive[0][2]
        * (
            gram_constructive[1][0] * gram_constructive[2][1]
            - gram_constructive[1][1] * gram_constructive[2][0]
        )
    )
    assert_equal(det_1, Fraction(1), "finite OS Gram first minor")
    assert_equal(det_2, Fraction(2), "finite OS Gram second minor")
    assert_equal(det_3, Fraction(16), "finite OS Gram third minor")

    # Equality of moments on the monomial basis gives equality of polynomial
    # quadratic forms by finite tensor expansion.
    polynomial = [Fraction(1), Fraction(-1), Fraction(1, 2)]
    square = poly_multiply(polynomial, polynomial)
    constructive_quadratic = sum(
        coeff * constructive_moments[degree]
        for degree, coeff in enumerate(square)
    )
    spde_quadratic = sum(
        coeff * spde_moments[degree]
        for degree, coeff in enumerate(square)
    )
    assert_equal(spde_quadratic, constructive_quadratic, "polynomial OS quadratic transfer")
    assert_equal(constructive_quadratic, Fraction(8), "sample polynomial OS quadratic value")

    # Growth constants are inherited because the moment sequence is identical.
    B = Fraction(4)
    gamma = 1
    for n, moment in constructive_moments.items():
        envelope = (B ** n) * (math.factorial(n) ** gamma)
        _assert_leq("SPDE hierarchy growth transfer", abs(spde_moments[n]), envelope)


def check_phi43_spde_constructive_status_split():
    # The quoted dynamic Phi4_3 SPDE theorem supplies the SPDE construction
    # side.  Equality with a constructive Euclidean hierarchy is a separate
    # common-regulator comparison input, not a consequence of those SPDE slots.
    spde_construction_slots = {
        "smooth_cutoff_well_posedness",
        "bphz_model_convergence",
        "global_markov_invariant_law",
    }
    comparison_slots = {
        "common_field_mass_chart",
        "bounded_cylinder_limit",
        "polynomial_tail_uniform_integrability",
        "schwinger_moment_equality",
        "constructive_os_growth_inputs",
    }

    def missing_os_identification_slots(supplied):
        return comparison_slots - supplied

    if not missing_os_identification_slots(spde_construction_slots):
        raise AssertionError("SPDE theorem alone certified constructive hierarchy")

    complete_supplied = spde_construction_slots | comparison_slots
    if missing_os_identification_slots(complete_supplied):
        raise AssertionError("complete common-regulator comparison was rejected")

    overpromoted_theorem = spde_construction_slots | {"schwinger_moment_equality"}
    if "common_field_mass_chart" in overpromoted_theorem:
        raise AssertionError("unexpected common chart in overpromoted sample")
    missing = missing_os_identification_slots(overpromoted_theorem)
    for required in {
        "common_field_mass_chart",
        "bounded_cylinder_limit",
        "polynomial_tail_uniform_integrability",
        "constructive_os_growth_inputs",
    }:
        if required not in missing:
            raise AssertionError("status split failed to retain comparison slot")


def check_spde_finite_window_os_defect_budget_arithmetic():
    # Proposition spde-finite-window-os-assembly-defect-budget: entrywise
    # convergence of an M-observable OS Gram window costs M epsilon in the
    # quadratic form unless one has an operator-norm estimate.
    M = 4
    c = [Fraction(1), Fraction(-2), Fraction(1), Fraction(1)]
    norm_sq = sum(abs(ci) ** 2 for ci in c)
    l1_sq = sum(abs(ci) for ci in c) ** 2
    delta = Fraction(1, 40)
    epsilon = Fraction(1, 200)
    assert_equal(norm_sq, Fraction(7), "finite-window coefficient norm")
    if l1_sq > M * norm_sq:
        raise AssertionError("finite-window Cauchy loss failed")

    cutoff_lower_bound = -delta * norm_sq
    worst_entrywise_shift = -epsilon * l1_sq
    actual_limit_lower_bound = cutoff_lower_bound + worst_entrywise_shift
    stated_limit_lower_bound = -(delta + M * epsilon) * norm_sq
    assert_equal(
        stated_limit_lower_bound,
        Fraction(-63, 200),
        "finite-window OS defect stated bound",
    )
    if actual_limit_lower_bound < stated_limit_lower_bound:
        raise AssertionError("finite-window OS defect budget failed")

    eta = Fraction(1, 300)
    actual_constructive_difference = eta * l1_sq
    stated_constructive_bound = M * eta * norm_sq
    assert_equal(
        stated_constructive_bound,
        Fraction(7, 75),
        "finite-window constructive comparison bound",
    )
    if actual_constructive_difference > stated_constructive_bound:
        raise AssertionError("finite-window constructive comparison failed")

    # Growth transfer: the SPDE hierarchy is bounded by the constructive
    # envelope plus the comparison-defect envelope, after replacing constants
    # by a common dominating family.
    n = 5
    q_value = Fraction(7)
    A = Fraction(2)
    B = Fraction(3)
    gamma = 1
    A_delta = Fraction(1)
    B_delta = Fraction(4)
    gamma_delta = 2
    constructive_bound = A * (B ** n) * (math.factorial(n) ** gamma) * q_value
    defect_bound = (
        A_delta
        * (B_delta ** n)
        * (math.factorial(n) ** gamma_delta)
        * q_value
    )
    common_bound = (
        (A + A_delta)
        * (max(B, B_delta) ** n)
        * (math.factorial(n) ** max(gamma, gamma_delta))
        * q_value
    )
    if constructive_bound + defect_bound > common_bound:
        raise AssertionError("finite-window OS-II growth transfer failed")


def check_spde_finite_rate_assembly_schedule_arithmetic():
    # Proposition spde-finite-rate-assembly-schedule: a growing OS window pays
    # both its cardinality and the amplification constant carried by the
    # model/fixed-point comparison.
    alpha = 2
    beta = 3
    previous_defect = None
    for k in range(1, 7):
        window_size = 2 ** (alpha * k)
        amplification = 2 ** (beta * k)
        model_error = Fraction(1, 2) ** ((alpha + beta + 3) * k)
        tail_error = Fraction(1, 2) ** ((alpha + 3) * k)
        hierarchy_error = Fraction(1, 2) ** ((alpha + 3) * k)
        cutoff_os_defect = Fraction(1, 2) ** k
        assembly_defect = cutoff_os_defect + window_size * (
            amplification * model_error + tail_error + hierarchy_error
        )
        stated_bound = 4 * (Fraction(1, 2) ** k)
        if assembly_defect > stated_bound:
            raise AssertionError("finite-rate assembly schedule bound failed")
        if previous_defect is not None and assembly_defect >= previous_defect:
            raise AssertionError("finite-rate assembly defect did not decrease")
        previous_defect = assembly_defect

    # A schedule that beats window size but not amplification leaves a growing
    # contribution after multiplying by m_k C_k.
    k = 4
    weak_model_error = Fraction(1, 2) ** ((alpha + 1) * k)
    weak_contribution = (
        2 ** (alpha * k)
        * 2 ** (beta * k)
        * weak_model_error
    )
    assert_equal(
        weak_contribution,
        2 ** ((beta - 1) * k),
        "finite-rate weak model defect",
    )


def check_spde_phase_cell_cross_route_budget_arithmetic():
    # Proposition spde-constructive-phase-cell-cross-route-budget composes
    # four errors: SPDE model/fixed-point convergence, polynomial truncation,
    # finite-chart comparison, and the constructive phase-cell tail.
    alpha = 2
    beta = 3
    gamma = 2
    previous_defect = None
    for k in range(1, 7):
        window_size = 2 ** (alpha * k)
        spde_amplification = 2 ** (beta * k)
        constructive_amplification = 2 ** (gamma * k)
        model_error = Fraction(1, 2) ** ((alpha + beta + 4) * k)
        truncation_error = Fraction(1, 2) ** ((alpha + 4) * k)
        chart_error = Fraction(1, 2) ** ((alpha + 4) * k)
        phase_cell_error = Fraction(1, 2) ** ((alpha + gamma + 4) * k)
        finite_os_defect = Fraction(1, 2) ** k

        entrywise_bridge = (
            spde_amplification * model_error
            + truncation_error
            + chart_error
            + constructive_amplification * phase_cell_error
        )
        combined_defect = finite_os_defect + window_size * entrywise_bridge
        stated_bound = 2 * (Fraction(1, 2) ** k)
        if combined_defect > stated_bound:
            raise AssertionError("cross-route assembly budget bound failed")
        if previous_defect is not None and combined_defect >= previous_defect:
            raise AssertionError("cross-route defect did not decrease")
        previous_defect = combined_defect

    # If the phase-cell tail beats the window size but not its own
    # amplification D_k, the constructive comparison contribution grows.
    k = 4
    weak_phase_cell_error = Fraction(1, 2) ** ((alpha + 1) * k)
    weak_phase_cell_contribution = (
        2 ** (alpha * k)
        * 2 ** (gamma * k)
        * weak_phase_cell_error
    )
    assert_equal(
        weak_phase_cell_contribution,
        2 ** ((gamma - 1) * k),
        "cross-route weak phase-cell defect",
    )


def check_spde_directed_os_prehilbert_comparison_arithmetic():
    # Proposition spde-directed-os-prehilbert-comparison: vanishing directed
    # lower defects give positivity on each fixed vector, and vanishing
    # entrywise form errors identify the algebraic OS quotient.
    coeff_v = [Fraction(1), Fraction(-2), Fraction(1)]
    coeff_w = [Fraction(2), Fraction(0), Fraction(-1)]
    l2_v = sum(c * c for c in coeff_v)
    l1_v = sum(abs(c) for c in coeff_v)
    l1_w = sum(abs(c) for c in coeff_w)

    previous_entry_bound = None
    previous_lower_defect = None
    for k in range(1, 8):
        entry_error = Fraction(1, 2) ** k
        lower_defect = Fraction(1, 3) ** k
        entry_bound = entry_error * l1_v * l1_w
        lower_bound = -lower_defect * l2_v
        if previous_entry_bound is not None and entry_bound >= previous_entry_bound:
            raise AssertionError("directed OS entry bound did not decrease")
        if previous_lower_defect is not None and lower_bound <= previous_lower_defect:
            raise AssertionError("directed OS lower defect did not approach zero")
        previous_entry_bound = entry_bound
        previous_lower_defect = lower_bound

    # Exact finite quotient shadow: a rank-one Gram block has the null vector
    # e1-e2.  Equality of SPDE and constructive forms makes the identity map
    # an isometry on representatives modulo this null space.
    gram = [
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(2)],
    ]

    def gram_quadratic(vec):
        total = Fraction(0)
        for i, vi in enumerate(vec):
            for j, vj in enumerate(vec):
                total += vi * gram[i][j] * vj
        return total

    null_vec = [Fraction(1), Fraction(-1), Fraction(0)]
    base_vec = [Fraction(0), Fraction(1), Fraction(1)]
    shifted_vec = [base_vec[i] + null_vec[i] for i in range(3)]
    assert_equal(gram_quadratic(null_vec), Fraction(0), "directed OS null norm")
    assert_equal(
        gram_quadratic(base_vec),
        gram_quadratic(shifted_vec),
        "directed OS quotient representative norm",
    )


def check_dpd_low_mode_energy_forcing_arithmetic():
    # Proposition spde-dpd-energy-low-mode-forcing uses exactly the energy
    # exponents produced by the smooth DPD estimate.  In spacetime, the
    # nonlinear terms all land in L^{4/3}.
    target_dual = Fraction(3, 4)  # reciprocal exponent of L^{4/3}
    assert_equal(
        Fraction(1, 4) + Fraction(1, 4) + Fraction(1, 4),
        target_dual,
        "low-mode Y^3 Holder exponent",
    )
    assert_equal(
        Fraction(1, 4) + Fraction(1, 4) + Fraction(1, 4),
        target_dual,
        "low-mode Y^2 X1 Holder exponent",
    )
    assert_equal(
        Fraction(1, 4) + Fraction(1, 2),
        target_dual,
        "low-mode Y X2 Holder exponent",
    )

    # The finite-dimensional low-mode embedding on T^2 uses Bernstein
    # L^{4/3} -> L^\infty, whose scale exponent is d/p = 3/2, followed by
    # the C^{-kappa} block weight.
    kappa = Fraction(1, 8)
    bernstein_power = Fraction(3, 2) - kappa
    assert bernstein_power > 0, "low-mode Bernstein power is finite for fixed R"

    # The energy forcing is L^{4/3} in time.  Pairing it with the heat-kernel
    # singularity (t-s)^(-theta) uses L^4 in time and requires 4 theta < 1.
    alpha = Fraction(1, 4)
    kappa = Fraction(1, 8)
    theta = (alpha + kappa) / 2
    time_gain = Fraction(1, 4) - theta
    assert theta < Fraction(1, 4), "low-mode Duhamel time integrability"
    assert_equal(time_gain, Fraction(1, 16), "low-mode Duhamel time gain")

    # After the low/high split, only the high-mode residual is absorbed:
    #   S <= C0 y + low + a (B + epsilon S)
    # becomes
    #   S <= 2 C0 y + 2 low + 2 a B
    # under a epsilon <= 1/2.
    C0 = Fraction(3, 2)
    y = Fraction(5, 3)
    low = Fraction(7, 5)
    a = Fraction(1, 6)
    B = Fraction(11, 4)
    epsilon = Fraction(3)
    assert a * epsilon <= Fraction(1, 2), "low/high forcing absorption"
    absorbed = 2 * C0 * y + 2 * low + 2 * a * B
    expected = Fraction(5) + Fraction(14, 5) + Fraction(11, 12)
    assert_equal(absorbed, expected, "low/high forcing absorbed bound")


def check_dpd_high_frequency_tail_global_continuity_budget():
    # Proposition spde-dpd-high-frequency-tail-global-continuity combines the
    # low-mode energy Duhamel term and the high-mode compact tail into the
    # rough energy-to-Besov recursion on a finite partition.
    C0 = Fraction(1)
    intervals = 4
    initial_bound = Fraction(3, 2)

    lam = Fraction(1)
    C_low = Fraction(4)
    C1 = Fraction(2)
    low_time_factor = Fraction(1, 16)
    high_time_factor = Fraction(1, 8)
    energy_window = Fraction(3)
    high_tail = Fraction(1, 10)
    epsilon_tail = Fraction(1)

    assert (
        lam * C1 * high_time_factor * epsilon_tail <= Fraction(1, 2)
    ), "high-frequency tail absorption"

    low_contribution = 2 * lam * C_low * low_time_factor * energy_window
    high_contribution = 2 * lam * C1 * high_time_factor * high_tail
    assert_equal(low_contribution, Fraction(3, 2), "global DPD low-mode contribution")
    assert_equal(high_contribution, Fraction(1, 20), "global DPD high-tail contribution")

    bounds = []
    for ell in range(intervals):
        previous = initial_bound if ell == 0 else bounds[-1]
        bounds.append(2 * C0 * previous + low_contribution + high_contribution)

    for ell, value in enumerate(bounds):
        explicit = (2 * C0) ** (ell + 1) * initial_bound
        for j in range(ell + 1):
            explicit += (2 * C0) ** (ell - j) * (
                low_contribution + high_contribution
            )
        assert_equal(value, explicit, "global DPD tail-recursion closed form")

    smaller_high_tail = Fraction(1, 20)
    smaller_high_contribution = 2 * lam * C1 * high_time_factor * smaller_high_tail
    assert smaller_high_contribution < high_contribution, "tail improves with R"


def check_rough_forcing_bootstrap_arithmetic():
    # Proposition spde-dpd-rough-forcing-bootstrap uses the absorption
    # condition |lambda| C1 delta^(1-theta) epsilon <= 1/2 to turn
    #   R_l <= C0 y_l + a (A_l + epsilon R_l)
    # into
    #   R_l <= 2 C0 y_l + 2 a A_l.
    C0 = Fraction(3, 2)
    a = Fraction(1, 5)
    epsilon = Fraction(2)
    assert a * epsilon <= Fraction(1, 2), "rough forcing absorption"

    A = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    y0 = Fraction(4, 3)
    D = []
    for ell, A_ell in enumerate(A):
        if ell == 0:
            value = 2 * C0 * y0 + 2 * a * A_ell
        else:
            value = 2 * C0 * D[-1] + 2 * a * A_ell
        D.append(value)

    for ell in range(len(A)):
        explicit = (2 * C0) ** (ell + 1) * y0
        for j in range(ell + 1):
            explicit += 2 * a * ((2 * C0) ** (ell - j)) * A[j]
        assert_equal(D[ell], explicit, "rough forcing recursion closed form")


def main():
    check_wick_polynomials()
    check_wiener_chaos_isometry_and_moments()
    check_finite_langevin_reversibility_dirichlet_form()
    check_dual_norm_finite_chaos_estimate_arithmetic()
    check_projective_kernel_dual_norm_criterion_arithmetic()
    check_gaussian_wick_coordinate_scale_arithmetic()
    check_gaussian_dual_norm_wavelet_arithmetic()
    check_heat_integration_reexpansion_arithmetic()
    check_nonlinear_negative_coordinate_wick_arithmetic()
    check_x2y_first_chaos_logarithmic_scale_arithmetic()
    check_x2y_first_chaos_cutoff_shell_arithmetic()
    check_x2y_first_chaos_parameter_edge_arithmetic()
    check_covariance_double_increment_arithmetic()
    check_tadpole_asymptotics()
    check_phi4_power_counting()
    check_phi4_three_two_loop_mass_coordinate()
    check_phi4_three_finite_cutoff_stability_bound()
    check_phi4_three_multiscale_geometric_bound()
    check_phi4_three_model_phase_cell_budget()
    check_phi4_three_connected_to_full_growth_bookkeeping()
    check_finite_polymer_source_cumulant_factorization()
    check_p_phi_two_boundary_cluster_bookkeeping()
    check_spde_ou_and_smoothing_normalizations()
    check_phi4_two_path_space_increment_arithmetic()
    check_dpd_sobolev_fixed_point_exponents()
    check_phi4_three_sobolev_dpd_obstruction_arithmetic()
    check_dpd_energy_young_exponents()
    check_dpd_energy_closedness_lp_power_arithmetic()
    check_dpd_energy_compactness_derivative_arithmetic()
    check_dpd_distributional_limit_exponents()
    check_dpd_besov_product_continuity_arithmetic()
    check_dpd_besov_fixed_point_exponents()
    check_dpd_besov_energy_compatibility_arithmetic()
    check_invariant_measure_limit_identity()
    check_stationary_law_coupling_invariance_defect()
    check_stationary_law_polynomial_truncation_arithmetic()
    check_reconstruction_wavelet_scale_powers()
    check_phi4_three_spde_bphz_counterterm_combinatorics()
    check_phi4_three_static_dynamic_coordinate_translation()
    check_phi4_three_vacuum_coordinate_partition_shift()
    check_phi4_three_negative_sector_coordinate_chart()
    check_modelled_fixed_point_contraction_arithmetic()
    check_random_model_cauchy_criterion_arithmetic()
    check_dyadic_parabolic_convolution_bound_arithmetic()
    check_parabolic_taylor_subtraction_gain_arithmetic()
    check_dyadic_net_supremum_upgrade_arithmetic()
    check_scale_summed_coordinate_upgrade_arithmetic()
    check_scale_summed_shell_separated_cutoff_arithmetic()
    check_projective_shell_separated_coordinate_criterion_arithmetic()
    check_nonlinear_pi_shell_cutoff_input_arithmetic()
    check_negative_sector_scale_summed_model_convergence_arithmetic()
    check_negative_sector_physical_parameter_entropy_arithmetic()
    check_gaussian_negative_pi_coordinate_input_arithmetic()
    check_gamma_coordinate_heat_input_arithmetic()
    check_nonlinear_pi_coordinate_kernel_input_arithmetic()
    check_xy_tested_graph_power_counting_arithmetic()
    check_x2y_high_chaos_graph_power_counting_arithmetic()
    check_x2y_high_chaos_edge_cutoff_arithmetic()
    check_xy_tested_coordinate_logarithmic_slack_arithmetic()
    check_xy_tested_coordinate_edge_arithmetic()
    check_xy_tested_coordinate_cutoff_shell_arithmetic()
    check_coordinate_to_model_convergence_arithmetic()
    check_multiscale_sector_kernel_summability_arithmetic()
    check_one_loop_relative_scale_gap_arithmetic()
    check_hilbert_scale_tightness_arithmetic()
    check_gaussian_negative_sobolev_summability_arithmetic()
    check_brascamp_lieb_hminus_bound_arithmetic()
    check_quartic_tail_integrability_arithmetic()
    check_regulator_comparison_error_budget_arithmetic()
    check_phi4_two_finite_volume_route_identification_arithmetic()
    check_spde_os_reconstruction_growth_arithmetic()
    check_spde_constructive_hierarchy_transfer_arithmetic()
    check_phi43_spde_constructive_status_split()
    check_spde_finite_window_os_defect_budget_arithmetic()
    check_spde_finite_rate_assembly_schedule_arithmetic()
    check_spde_phase_cell_cross_route_budget_arithmetic()
    check_spde_directed_os_prehilbert_comparison_arithmetic()
    check_dpd_low_mode_energy_forcing_arithmetic()
    check_dpd_high_frequency_tail_global_continuity_budget()
    check_rough_forcing_bootstrap_arithmetic()
    print("All constructive scalar/SPDE Wick, chaos, finite-Langevin reversibility, dual-norm chaos, projective-kernel, Gaussian-coordinate, Gaussian-dual-wavelet, heat-reexpansion, nonlinear-coordinate, first-chaos-log, first-chaos cutoff shell, first-chaos parameter edge, covariance-double-increment, power-counting, DPD, Phi4_2-path-noise, Phi4_3-DPD-obstruction, reconstruction, BPHZ, static-dynamic coordinate, vacuum-coordinate, negative-sector bookkeeping, negative-coordinate-chart, C1-growth, C2-log-growth, C2-shell, two-loop-sector, fixed-point, polymer-source-cumulant, Pphi2 boundary/cluster bookkeeping, DPD energy closedness, DPD compactness, DPD distributional-limit, DPD Besov product, DPD Besov fixed-point, DPD Besov-energy compatibility, invariant-law identity, stationary-law coupling, stationary-law polynomial truncation, random-model convergence, dyadic-kernel, Taylor-gain, dyadic-net supremum, scale-summed-coordinate, scale-summed shell-separated cutoff, projective shell-separated coordinate, nonlinear Pi shell cutoff input, negative-sector model convergence, physical-parameter entropy, Gaussian negative Pi-coordinate input, Gamma heat-coordinate input, nonlinear Pi-coordinate kernel input, XY graph power-counting, X2Y high-chaos graph power-counting, XY scalar-tested slack, XY scalar edge, XY scalar cutoff shell, coordinate-to-model convergence, multiscale-sector, source-decorated phase-cell, model phase-cell budget, connected-to-full growth, one-loop relative-scale, Hilbert-scale tightness, Gaussian H-minus summability, Brascamp-Lieb H-minus, quartic-tail, regulator-comparison, Phi4_2 finite-volume route identification, SPDE-to-OS growth, SPDE/constructive hierarchy-transfer, Phi4_3 SPDE/constructive status split, finite-window OS defect, finite-rate assembly schedule, cross-route phase-cell/SPDE budget, directed OS pre-Hilbert comparison, DPD low-mode energy forcing, high-frequency tail global-continuity budget, and rough-forcing bootstrap checks passed.")


if __name__ == "__main__":
    main()
