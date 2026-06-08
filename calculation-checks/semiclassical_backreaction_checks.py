#!/usr/bin/env python3
"""Finite checks for the semiclassical backreaction chapter.

These checks verify algebraic identities that are easy to lose by a sign or
normalization: traces of the curvature-squared Euler tensors in four
dimensions, the KMS fluctuation-dissipation factor, positivity of the noise
covariance, finite response-window metric fluctuation bounds, the first-order
large-species scaling of mean backreaction versus metric fluctuations, the
large-species scaling of retained stress-source cumulants, the
finite scheme-transport identity linking local stress-tensor curvature
ambiguities to gravitational EFT coordinates, local linear response, and
connected noise, the first-order lambda-phi-four potential-insertion source
coordinate, the retained lambda-phi-four potential-noise coordinate using the
full separated two-point function, retained Ward diagnostics for interacting
source/noise coordinates,
the finite retained Ward-completion laboratory connecting those diagnostics to
metric response and missing-noise budgets,
the full retained interacting stress-tensor/noise package with component
cross-covariances and finite composite-operator mixing, the closed-time-path
influence-functional consistency of the interacting mean, retarded response,
and noise package,
the homogeneous FLRW interacting-source closure tying a time-dependent
potential coordinate to the pressure, Friedmann/Raychaudhuri, and
stress-noise Ward data,
the small-gain stability and fluctuation-validity check for the linearized
interacting backreaction operator, the finite nonlinear fixed-point chart for
the retained semiclassical equation,
the retained metric-observable output layer including fluctuation bias,
observable covariance, chart-exit/tail budgets, and signal-to-noise tests, the
observable-chain boundary
separating a formal mean equation from a physical retained metric prediction,
and the low-energy root selected by reduction of order in a toy
higher-derivative equation.

Evidence contract.
Target claims: the finite algebra and response-window subclaims in Volume
XII Chapter 11, including curvature-squared trace normalizations,
fluctuation-dissipation factors, noise-covariance positivity, retained
metric-response bounds, the large-N_sp species scaling of the rescaled mean
source, source-noise covariance, and higher connected stress-source cumulants,
the finite scheme-transport invariance of the semiclassical residual and its
linearized/contact/noise consequences,
the lambda-phi-four potential-insertion source coordinate, the retained
potential-noise Wick contraction with full separated two-point cross covariance
and metric pushforward, the restricted
finite-renormalization decomposition for that coordinate, the finite retained
Ward-diagnostic/projected-noise algebra for interacting sources, the worked
two-coordinate Ward-completion laboratory relating conserved source projection
and retained metric/noise pushforward to the missing interacting covariance,
and the
full interacting package algebra in which component cross-covariances and
finite operator-mixing terms are required before Ward tests are applied to the
noise, the closed-time-path package tests tying Ward identities, retarded
support, positivity, and fluctuation-dissipation compatibility together, the
homogeneous FLRW source/noise closure in which the correction pressure and
state-transport terms make a time-dependent potential density compatible with
both Friedmann and Raychaudhuri responses and with Ward-clean Hubble noise, the
small-gain feedback inverse and noise-amplification bound for the full retained
backreaction operator, the finite nonlinear self-map/contraction and
mean/noise-validity budgets, including residual size and residual Lipschitz
controls, for a retained backreaction chart, the retained
metric-observable mean shift, quadratic fluctuation bias, covariance, and
chart-exit/tail controlled signal-to-noise inequality, the observable-chain
boundary data that must be present before a retained metric observable is
claimed, and the low-energy root
selected by reduction of order.
Independent construction: the checks recompute traces, KMS factors,
matrix pushforwards, exact retained-sector inverses, Wick-contraction
coefficients, cosmological-coordinate shifts, independent finite counterterm
controls, signed/absolute norm bounds, Ward maps, kernel projectors, projected
covariances, explicit finite Ward repairs, Ward-reduced source responses,
projected diagnostic covariances, missing Ward-clean fluctuation budgets,
finite stress/gravity coordinate transports, linear local-response transports,
c-number connected-noise cancellations,
finite influence-functional quadratic forms, retarded-support tests,
fluctuation-dissipation ratios, small-gain inverses, response/noise bounds,
FLRW pressure closures, Hubble-response consistency checks, and Ward-clean
homogeneous stress-noise covariances,
species sums, 1/N_sp gravitational-coupling scaling, source-cumulant scaling,
nonlinear fixed-point radii, residual size and residual Lipschitz
budgets, state-transport Lipschitz constants, noise-validity inequalities, and
metric-observable linear/quadratic forms and covariances, ordered
observable-chain stages with their required side data, finite Gaussian
chart-exit bounds, out-of-chart integrability gates, and toy roots
directly from finite formulas rather than importing chapter display strings.
Imported assumptions: the tests use finite-dimensional retained sectors,
centered quasifree Wick combinatorics, formal first- and second-order lambda
coordinates, positive finite noise matrices, full-rank finite Ward maps, and the
chapter's convention E_grav = <T_ren>.
Negative controls: singular retained response matrices, wrong Wick
contraction factors, omitted local-Wick-renormalization quadratic terms, wrong
cosmological-coordinate signs, erased independent quartic/stress-tensor finite
counterterms, signed negative density norm bounds, dropped connected
potential-noise terms, using the smooth Wick remainder instead of the full
separated two-point function, premature real-part projection, retained
disconnected noise pieces, pretending a transverse counterterm cancels a Ward
violation, wrong-sign Ward repairs, identifying the least-norm projection with
the physical completion, identifying projected partial noise with full physical
noise, unprojected longitudinal noise, stress-only or gravity-only finite
scheme transport, local-response transport on only one side, deterministic
curvature shifts added to connected noise, feeding a nonconserved retained
source to the metric response, and undercounting a Ward-clean missing-noise
fluctuation budget, cutoff-scale higher-derivative roots,
component-variance-only noise packages, missing finite-renormalization cross
terms, c-number counterterms incorrectly added to connected noise, advanced
response kernels, independent noise spectra violating the KMS factor, and
spurious closed-time-path h_c h_c terms are rejected, as are singular feedback
operators, overlarge small-gain feedback, unconserved sources/noise, and
conserved-but-unstable retained data, signed nonlinear residual cancellations,
time-dependent potential energy inserted without correction pressure,
Friedmann/Raychaudhuri inconsistency, potential-only stochastic stress noise,
and Hubble-noise estimates that ignore the Ward-clean pressure and derivative
fluctuations,
omitted state-transport Lipschitz constants, omitted residual Lipschitz
constants, bounded non-Lipschitz residuals with multiple fixed points, overlarge
quadratic nonlinear feedback, linear-noise-only validity estimates,
omitted observable fluctuation bias, coordinate probes that do not annihilate
pure-gauge directions, and partial metric covariances that undercount
observable variance, formal-equation-only chains, mean-only chains, noise-only
chains, wrong-order observable chains, missing chart-exit/tail data, treating
missing signal-to-noise as invalidity instead of loss of self-averaging,
fixed-G_N large-species scaling, coherent N_sp^2 noise scaling, correlated
species noise, and wrong higher-source-cumulant suppression estimates.
Scope boundary: a pass checks coefficient, positivity, and response-bound
bookkeeping for the retained potential-insertion coordinate and the finite
algebra of a full retained stress-tensor package; it does not construct the
pAQFT interacting stress tensor, prove existence of interacting Hadamard
states, construct renormalized stress-tensor products, build a non-Gaussian
stochastic hierarchy or higher-metric-cumulant response map, solve stochastic
semiclassical equations, prove that a retained observable exists in the
infinite-dimensional theory, or address nonperturbative quantum gravity
dynamics.
Primary derivation route: derive each retained response, covariance, Ward,
fixed-point, observable, chart-exit, and reduction-of-order identity directly
from finite matrices, finite Gaussian laws, Wick contraction coefficients, and
exact rational inequalities.
Independent verification route: compare the chapter formulas against explicit
finite countermodels: singular response matrices, nonconserved sources,
projected partial covariances, omitted residual variation, divergent
out-of-chart Gaussian remainders, and noise-dominated but still valid
observable laws.
Convention dependencies: the gravitational equation convention is
E_grav=<T_ren>; retained metric vectors use the same gauge/constraint
reduction as the response operator; the observable Gaussian law is
H=h_*+Z with covariance C_h; signal-to-noise means self-averaging or
detectability, not stochastic-law validity.
Domain and remainder assumptions: finite retained sectors, positive covariance
matrices, chart radii, residual Lipschitz constants, Gaussian tail or stopping
budgets, and declared bounds for omitted connected noise and higher observable
remainders are supplied as hypotheses of the retained calculation.
Remaining unproved or conditional: the checks do not prove the
infinite-dimensional semiclassical Einstein-Langevin existence theorem,
Hadamard-state propagation, global metric-chart persistence, interacting
pAQFT stress-tensor construction, or non-Gaussian higher-cumulant closure.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_geq as _assert_geq
from check_utils import assert_gt as _assert_gt

import cmath
import math
from fractions import Fraction


Matrix = tuple[tuple[Fraction, ...], ...]


def assert_close(
    got: complex,
    expected: complex,
    label: str,
    tol: float = 1e-10,
) -> None:
    _assert_close(label, got, expected, tol=tol)


def assert_equal(label: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0])))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def det2(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det3(matrix: Matrix) -> Fraction:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def inverse2(matrix: Matrix) -> Matrix:
    determinant = det2(matrix)
    if determinant == 0:
        raise AssertionError("attempted to invert a singular two-by-two matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(1) if row == col else Fraction(0) for col in range(size))
        for row in range(size)
    )


def zero_matrix(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(cols)) for _ in range(rows))


def matadd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left[0])))
        for row in range(len(left))
    )


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(len(left[0])))
        for row in range(len(left))
    )


def matsum(matrices: tuple[Matrix, ...]) -> Matrix:
    if not matrices:
        raise AssertionError("empty matrix sum")
    result = zero_matrix(len(matrices[0]), len(matrices[0][0]))
    for matrix in matrices:
        result = matadd(result, matrix)
    return result


def trace(matrix: Matrix) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def squared_norm(column: Matrix) -> Fraction:
    return sum(column[i][0] * column[i][0] for i in range(len(column)))


def frobenius_norm_sq(matrix: Matrix) -> Fraction:
    return sum(entry * entry for row in matrix for entry in row)


def quadratic_form(matrix: Matrix, column: Matrix) -> Fraction:
    return matmul(matmul(transpose(column), matrix), column)[0][0]


def check_curvature_squared_traces() -> None:
    dimension = 4

    # H^(1) = 2 R R_mn - 1/2 g_mn R^2 + 2 g_mn Box R - 2 nabla_m nabla_n R.
    r2_coeff = 2 - dimension / 2
    box_r_coeff = 2 * dimension - 2
    assert_close(r2_coeff, 0.0, "R^2 trace algebra in D=4")
    assert_close(box_r_coeff, 6.0, "H1 trace Box R coefficient")

    # H^(2) = 2 R_mrns R^rs - 1/2 g_mn Ric^2
    #       + nabla_m nabla_n R - Box R_mn - 1/2 g_mn Box R.
    ricci2_coeff = 2 - dimension / 2
    box_r_coeff_h2 = 1 - 1 - dimension / 2
    assert_close(ricci2_coeff, 0.0, "Ricci^2 trace algebra in D=4")
    assert_close(box_r_coeff_h2, -2.0, "H2 trace Box R coefficient")


def check_kms_fluctuation_dissipation() -> None:
    beta = 1.7
    omega = 0.9
    c_ab = 2.3
    c_ba_minus = math.exp(-beta * omega) * c_ab
    noise = 0.5 * (c_ab + c_ba_minus)
    rho = c_ab - c_ba_minus
    expected_noise = 0.5 / math.tanh(0.5 * beta * omega) * rho
    assert_close(noise, expected_noise, "KMS fluctuation-dissipation factor")


def check_noise_covariance_positivity() -> None:
    covariance = ((2.0, 0.7), (0.7, 1.0))
    determinant = covariance[0][0] * covariance[1][1] - covariance[0][1] ** 2
    if covariance[0][0] <= 0 or determinant <= 0:
        raise AssertionError("test covariance should be positive definite")
    for x, y in [(1.0, -3.0), (2.0, 5.0), (-0.25, 0.75)]:
        value = (
            covariance[0][0] * x * x
            + 2 * covariance[0][1] * x * y
            + covariance[1][1] * y * y
        )
        _assert_geq("noise quadratic form nonnegative", value, 0.0, tol=1e-12)


def check_einstein_langevin_pushforward_covariance() -> None:
    # Finite-dimensional analogue of Cov(h) = G N G^T.
    noise = ((2.0, 0.4), (0.4, 1.1))
    green = ((1.2, -0.3), (0.5, 0.8), (-0.7, 0.2))
    covariance = tuple(
        tuple(
            sum(green[i][a] * noise[a][b] * green[j][b] for a in range(2) for b in range(2))
            for j in range(3)
        )
        for i in range(3)
    )

    for i in range(3):
        for j in range(3):
            assert_close(covariance[i][j], covariance[j][i], "metric covariance symmetry")

    for test in [(1.0, -2.0, 0.5), (0.3, 0.4, -0.6), (-1.2, 0.0, 0.7)]:
        pulled = tuple(sum(green[i][a] * test[i] for i in range(3)) for a in range(2))
        direct_metric_variance = sum(
            test[i] * covariance[i][j] * test[j] for i in range(3) for j in range(3)
        )
        noise_variance = sum(pulled[a] * noise[a][b] * pulled[b] for a in range(2) for b in range(2))
        assert_close(direct_metric_variance, noise_variance, "pushforward covariance quadratic form")
        if direct_metric_variance < -1e-12:
            raise AssertionError("pushforward metric covariance should be positive semidefinite")


def check_large_species_semiclassical_scaling() -> None:
    # Independent identical sectors: <T_N> = N <T_1>, Noise_N = N Noise_1.
    # Keeping kappa_bar = N kappa_N fixed makes the mean source finite and the
    # metric covariance O(1/N).
    species_count = 25
    kappa_bar = Fraction(3, 5)
    kappa_n = kappa_bar / species_count
    one_sector_mean_source = Fraction(2, 3)
    one_sector_noise_trace = Fraction(5, 6)

    mean_source = kappa_n * species_count * one_sector_mean_source
    assert_equal("large-N finite mean source", mean_source, Fraction(2, 5))

    source_noise_trace = (
        kappa_n * kappa_n * species_count * one_sector_noise_trace
    )
    assert_equal("large-N source-noise trace", source_noise_trace, Fraction(3, 250))
    if species_count * source_noise_trace != kappa_bar * kappa_bar * one_sector_noise_trace:
        raise AssertionError("large-N source noise should scale exactly as 1/N")

    response_bound_sq = Fraction(4)
    metric_noise_trace_bound = response_bound_sq * source_noise_trace
    assert_equal(
        "large-N metric covariance trace bound",
        metric_noise_trace_bound,
        Fraction(6, 125),
    )
    if metric_noise_trace_bound >= Fraction(1, 16):
        raise AssertionError("test large-N metric covariance should fit the chart")

    one_sector_third_cumulant = Fraction(7, 8)
    rescaled_source_third_cumulant = (
        kappa_n**3 * species_count * one_sector_third_cumulant
    )
    assert_equal(
        "large-N third source cumulant",
        rescaled_source_third_cumulant,
        Fraction(189, 625000),
    )
    if (
        species_count
        * species_count
        * rescaled_source_third_cumulant
        != kappa_bar**3 * one_sector_third_cumulant
    ):
        raise AssertionError("third connected source cumulant should scale as 1/N^2")

    fixed_gn_mean_source = kappa_bar * species_count * one_sector_mean_source
    fixed_gn_noise_trace = (
        kappa_bar * kappa_bar * species_count * one_sector_noise_trace
    )
    if fixed_gn_mean_source <= mean_source:
        raise AssertionError("negative control failed: fixed G_N did not grow the mean")
    if fixed_gn_noise_trace <= source_noise_trace:
        raise AssertionError("negative control failed: fixed G_N did not grow the noise")

    coherent_noise_trace = (
        kappa_n * kappa_n * species_count * species_count * one_sector_noise_trace
    )
    assert_equal("coherent species noise trace", coherent_noise_trace, Fraction(3, 10))
    if coherent_noise_trace <= 10 * source_noise_trace:
        raise AssertionError("negative control failed: coherent N^2 noise looked suppressed")

    pair_correlation_trace = Fraction(1, 10)
    correlated_source_noise_trace = kappa_n * kappa_n * (
        species_count * one_sector_noise_trace
        + species_count * (species_count - 1) * pair_correlation_trace
    )
    assert_equal(
        "correlated species source-noise trace",
        correlated_source_noise_trace,
        Fraction(291, 6250),
    )
    if correlated_source_noise_trace <= 3 * source_noise_trace:
        raise AssertionError("negative control failed: pair correlations were harmless")

    wrong_third_cumulant = (
        kappa_bar**3 * one_sector_third_cumulant / species_count
    )
    if wrong_third_cumulant <= rescaled_source_third_cumulant:
        raise AssertionError("negative control failed: wrong third-source-cumulant scaling passed")


def check_finite_response_window_bounds() -> None:
    # Exact retained-sector analogue of h = D^{-1} j and C_h = D^{-1} N D^{-*}.
    response_inverse: Matrix = (
        (Fraction(1, 2), Fraction(1, 4)),
        (Fraction(-1, 4), Fraction(1, 2)),
    )
    response_matrix: Matrix = (
        (Fraction(8, 5), Fraction(-4, 5)),
        (Fraction(4, 5), Fraction(8, 5)),
    )
    identity = matmul(response_matrix, response_inverse)
    if identity != ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))):
        raise AssertionError("retained response inverse is not the exact inverse")

    if det2(response_matrix) <= 0:
        raise AssertionError("retained response matrix should be invertible in the tested window")

    singular_response: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
    if det2(singular_response) != 0:
        raise AssertionError("negative control should detect a singular retained response")

    source: Matrix = ((Fraction(2, 7),), (Fraction(-1, 7),))
    mean_metric = matmul(response_inverse, source)
    source_norm_sq = squared_norm(source)
    mean_norm_sq = squared_norm(mean_metric)

    # The exact operator-norm square of response_inverse is 5/16; use a
    # deliberately coarser bound to model a certified response-window estimate.
    certified_norm_sq = Fraction(9, 25)
    if mean_norm_sq > certified_norm_sq * source_norm_sq:
        raise AssertionError("finite response mean bound failed")

    noise: Matrix = (
        (Fraction(3, 5), Fraction(1, 10)),
        (Fraction(1, 10), Fraction(2, 5)),
    )
    if noise[0][0] <= 0 or det2(noise) <= 0:
        raise AssertionError("retained noise matrix should be positive definite")

    metric_covariance = matmul(matmul(response_inverse, noise), transpose(response_inverse))
    if metric_covariance != transpose(metric_covariance):
        raise AssertionError("retained metric covariance should be symmetric")
    if metric_covariance[0][0] < 0 or det2(metric_covariance) < 0:
        raise AssertionError("retained metric covariance should be positive semidefinite")

    covariance_trace = trace(metric_covariance)
    noise_trace = trace(noise)
    if covariance_trace > certified_norm_sq * noise_trace:
        raise AssertionError("finite response noise trace bound failed")


def check_finite_scheme_transport_consistency() -> None:
    # Conserved local basis coordinates for (g, G, H1, H2).  A finite
    # stress-tensor ambiguity is only a coordinate change when the same local
    # tensor is transported into the gravitational EFT coordinates.
    gravity_coordinates: Matrix = (
        (Fraction(5, 3),),
        (Fraction(7, 5),),
        (Fraction(-2, 9),),
        (Fraction(4, 11),),
    )
    stress_mean: Matrix = (
        (Fraction(1, 6),),
        (Fraction(-3, 10),),
        (Fraction(5, 12),),
        (Fraction(-7, 8),),
    )
    residual = matsub(gravity_coordinates, stress_mean)

    m_squared = Fraction(3, 2)
    m_fourth = m_squared * m_squared
    finite_coefficients = (
        Fraction(1, 9),
        Fraction(-2, 21),
        Fraction(2, 5),
        Fraction(3, 13),
    )
    finite_shift: Matrix = (
        (finite_coefficients[0] * m_fourth,),
        (finite_coefficients[1] * m_squared,),
        (finite_coefficients[2],),
        (finite_coefficients[3],),
    )
    expected_shift: Matrix = (
        (Fraction(1, 4),),
        (Fraction(-1, 7),),
        (Fraction(2, 5),),
        (Fraction(3, 13),),
    )
    if finite_shift != expected_shift:
        raise AssertionError("local curvature finite-shift coordinates changed")

    transported_gravity = matadd(gravity_coordinates, finite_shift)
    transported_stress = matadd(stress_mean, finite_shift)
    transported_residual = matsub(transported_gravity, transported_stress)
    if transported_residual != residual:
        raise AssertionError("finite scheme transport should leave E_grav - <T> invariant")

    stress_only_residual = matsub(gravity_coordinates, transported_stress)
    if stress_only_residual == residual:
        raise AssertionError("negative control failed: stress-only scheme shift looked invariant")
    if stress_only_residual != matsub(residual, finite_shift):
        raise AssertionError("stress-only scheme shift should move the residual by -A")

    gravity_only_residual = matsub(transported_gravity, stress_mean)
    if gravity_only_residual == residual:
        raise AssertionError("negative control failed: gravity-only coordinate shift looked invariant")
    if gravity_only_residual != matadd(residual, finite_shift):
        raise AssertionError("gravity-only coordinate shift should move the residual by +A")

    # The same cancellation must occur after linearization: the variation of the
    # c-number local stress shift is a local contact term and must be matched by
    # the variation of the transported gravitational coordinate.
    gravitational_derivative: Matrix = (
        (Fraction(3), Fraction(1, 2)),
        (Fraction(1, 3), Fraction(5, 2)),
    )
    stress_local_derivative: Matrix = (
        (Fraction(1, 4), Fraction(-1, 5)),
        (Fraction(2, 7), Fraction(1, 3)),
    )
    local_derivative_shift: Matrix = (
        (Fraction(1, 6), Fraction(1, 10)),
        (Fraction(-1, 9), Fraction(2, 15)),
    )
    linear_residual = matsub(gravitational_derivative, stress_local_derivative)
    transported_linear_residual = matsub(
        matadd(gravitational_derivative, local_derivative_shift),
        matadd(stress_local_derivative, local_derivative_shift),
    )
    if transported_linear_residual != linear_residual:
        raise AssertionError("linearized local scheme transport should cancel in the response operator")

    omitted_gravity_contact = matsub(
        gravitational_derivative,
        matadd(stress_local_derivative, local_derivative_shift),
    )
    if omitted_gravity_contact == linear_residual:
        raise AssertionError("negative control failed: omitted gravity-side contact shift was invisible")

    omitted_stress_contact = matsub(
        matadd(gravitational_derivative, local_derivative_shift),
        stress_local_derivative,
    )
    if omitted_stress_contact == linear_residual:
        raise AssertionError("negative control failed: omitted stress-side contact shift was invisible")

    retarded_commutator: Matrix = (
        (Fraction(2, 5), Fraction(1, 7)),
        (Fraction(0), Fraction(1, 3)),
    )
    wrong_commutator_shift = matadd(retarded_commutator, local_derivative_shift)
    if wrong_commutator_shift == retarded_commutator:
        raise AssertionError("test c-number shift should make a wrong commutator change visible")

    # A deterministic c-number curvature shift changes the mean and the raw
    # second moment, but it cancels from the connected covariance.
    mean: Matrix = (
        (Fraction(2, 3),),
        (Fraction(-1, 5),),
    )
    connected_noise: Matrix = (
        (Fraction(3, 4), Fraction(1, 6)),
        (Fraction(1, 6), Fraction(2, 5)),
    )
    if connected_noise[0][0] <= 0 or det2(connected_noise) <= 0:
        raise AssertionError("test connected noise should be positive definite")

    second_moment = matadd(connected_noise, matmul(mean, transpose(mean)))
    c_number_shift: Matrix = (
        (Fraction(5, 7),),
        (Fraction(-3, 8),),
    )
    shifted_mean = matadd(mean, c_number_shift)
    shifted_second_moment = matadd(
        second_moment,
        matadd(
            matadd(
                matmul(mean, transpose(c_number_shift)),
                matmul(c_number_shift, transpose(mean)),
            ),
            matmul(c_number_shift, transpose(c_number_shift)),
        ),
    )
    shifted_connected_noise = matsub(
        shifted_second_moment,
        matmul(shifted_mean, transpose(shifted_mean)),
    )
    if shifted_connected_noise != connected_noise:
        raise AssertionError("c-number curvature shift should cancel from connected noise")

    wrong_noise = matadd(connected_noise, matmul(c_number_shift, transpose(c_number_shift)))
    if wrong_noise == connected_noise:
        raise AssertionError("negative control failed: deterministic shift did not alter wrong noise")
    if trace(wrong_noise) <= trace(connected_noise):
        raise AssertionError("negative control failed: wrong c-number noise did not enlarge trace")


def check_lambda_phi4_potential_source_coordinate() -> None:
    # Centered quasifree Wick combinatorics gives <Phi_H^4> = 3 Sigma^2.
    coupling = Fraction(4, 9)
    wick_variance = Fraction(3, 2)
    wick_four = 3 * wick_variance * wick_variance
    potential_density = coupling * wick_four / 24
    if potential_density != Fraction(1, 8):
        raise AssertionError(
            "lambda phi^4 potential source coordinate should be lambda Sigma^2/8"
        )

    missing_wick_pairings = coupling * wick_variance * wick_variance / 24
    if potential_density == missing_wick_pairings:
        raise AssertionError("negative control failed: Wick factor 3 was lost")

    kappa = Fraction(6, 5)  # kappa = 8 pi G_N in the chapter notation.
    cosmological_shift = kappa * potential_density
    if cosmological_shift != Fraction(3, 20):
        raise AssertionError("cosmological-coordinate shift should be +kappa rho_lambda")
    if -cosmological_shift == kappa * potential_density:
        raise AssertionError("negative control failed: cosmological-coordinate sign was not tested")

    local_wick_shift = Fraction(1, 2)
    shifted_density = coupling * (wick_variance + local_wick_shift) ** 2 / 8
    density_change = shifted_density - potential_density
    if density_change != Fraction(7, 72):
        raise AssertionError(
            "local Wick-renormalization density shift should include the quadratic term"
        )
    linear_only_change = coupling * wick_variance * local_wick_shift / 4
    if density_change == linear_only_change:
        raise AssertionError("negative control failed: omitted quadratic scheme term")

    independent_phi4_counterterm = Fraction(5, 72)
    independent_stress_counterterm = Fraction(-1, 40)
    full_scheme_density = (
        shifted_density
        + independent_phi4_counterterm
        + independent_stress_counterterm
    )
    if full_scheme_density != Fraction(4, 15):
        raise AssertionError("independent finite counterterm bookkeeping changed unexpectedly")
    if full_scheme_density == shifted_density:
        raise AssertionError("negative control failed: Wick-square shift alone fixed the full source")

    certified_norm = Fraction(3, 5)
    q_norm = Fraction(7, 11)
    negative_density = -potential_density
    signed_rhs = certified_norm * negative_density * q_norm
    absolute_rhs = certified_norm * abs(negative_density) * q_norm
    if not (signed_rhs < 0 < absolute_rhs):
        raise AssertionError("negative density should invalidate a signed norm bound")
    if absolute_rhs != -signed_rhs:
        raise AssertionError("absolute-value norm bound should repair the signed-density failure")

    source_profile: Matrix = (
        (-potential_density * Fraction(5, 6),),
        (potential_density * Fraction(1, 3),),
    )
    response_inverse: Matrix = (
        (Fraction(1, 2), Fraction(1, 4)),
        (Fraction(-1, 4), Fraction(1, 2)),
    )
    mean_metric = matmul(response_inverse, source_profile)
    certified_norm_sq = Fraction(9, 25)
    if squared_norm(mean_metric) > certified_norm_sq * squared_norm(source_profile):
        raise AssertionError("potential source response exceeds certified retained bound")


def check_lambda_phi4_potential_noise_kernel() -> None:
    coupling = Fraction(2, 3)
    sigma_x = Fraction(3, 5)
    sigma_y = Fraction(5, 7)
    full_two_point_xy = Fraction(2, 11)
    smooth_remainder_xy = Fraction(1, 17)

    disconnected = 9 * sigma_x * sigma_x * sigma_y * sigma_y
    connected = (
        72 * sigma_x * sigma_y * full_two_point_xy * full_two_point_xy
        + 24 * full_two_point_xy**4
    )
    full_wick_four_product = disconnected + connected
    if full_wick_four_product - disconnected != connected:
        raise AssertionError("connected Wick-four covariance subtraction failed")

    dropped_mixed_term = 24 * full_two_point_xy**4
    if dropped_mixed_term == connected:
        raise AssertionError("negative control failed: mixed Sigma Sigma W^2 term was dropped")
    if full_wick_four_product == connected:
        raise AssertionError("negative control failed: disconnected Wick-four term was retained")

    remainder_only_connected = (
        72 * sigma_x * sigma_y * smooth_remainder_xy * smooth_remainder_xy
        + 24 * smooth_remainder_xy**4
    )
    if remainder_only_connected == connected:
        raise AssertionError("negative control failed: full separated two-point function was omitted")

    state_wick_sigma = Fraction(0)
    state_wick_remainder = Fraction(0)
    state_wick_two_point = Fraction(3, 7)
    state_wick_connected = (
        72 * state_wick_sigma * state_wick_sigma * state_wick_two_point**2
        + 24 * state_wick_two_point**4
    )
    state_wick_remainder_only = (
        72 * state_wick_sigma * state_wick_sigma * state_wick_remainder**2
        + 24 * state_wick_remainder**4
    )
    if state_wick_connected == 0:
        raise AssertionError("same-state Wick coordinate should retain separated fourth-power noise")
    if state_wick_remainder_only != 0:
        raise AssertionError("same-state Wick remainder control should be zero")
    if state_wick_connected == state_wick_remainder_only:
        raise AssertionError("negative control failed: same-state Wick coordinate erased cross noise")

    complex_re = Fraction(2, 5)
    complex_im = Fraction(1, 3)
    complex_square_real = complex_re * complex_re - complex_im * complex_im
    complex_square_imag = 2 * complex_re * complex_im
    complex_fourth_real = (
        complex_square_real * complex_square_real
        - complex_square_imag * complex_square_imag
    )
    symmetrized_real_after = (
        72 * sigma_x * sigma_y * complex_square_real
        + 24 * complex_fourth_real
    )
    premature_real_projection = (
        72 * sigma_x * sigma_y * complex_re * complex_re
        + 24 * complex_re**4
    )
    if symmetrized_real_after == premature_real_projection:
        raise AssertionError("negative control failed: real part was taken before powers")

    potential_noise_cell = coupling * coupling * connected / (24 * 24)
    expected_cell = coupling * coupling * (
        sigma_x * sigma_y * full_two_point_xy * full_two_point_xy / 8
        + full_two_point_xy**4 / 24
    )
    if potential_noise_cell != expected_cell:
        raise AssertionError("lambda phi^4 potential-noise coefficient changed")

    doubled_coupling_noise = (2 * coupling) * (2 * coupling) * connected / (24 * 24)
    if doubled_coupling_noise != 4 * potential_noise_cell:
        raise AssertionError("potential noise should scale quadratically in lambda")

    covariance: Matrix = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(3)),
    )
    sigmas = (covariance[0][0], covariance[1][1])
    wick_four_covariance: Matrix = tuple(
        tuple(
            72 * sigmas[i] * sigmas[j] * covariance[i][j] ** 2
            + 24 * covariance[i][j] ** 4
            for j in range(2)
        )
        for i in range(2)
    )
    if wick_four_covariance[0][0] <= 0 or det2(wick_four_covariance) <= 0:
        raise AssertionError("finite Wick-four covariance should be positive definite")

    profiles: Matrix = (
        (Fraction(1, 5), Fraction(2, 7)),
        (Fraction(3, 11), Fraction(-1, 13)),
    )
    retained_noise: Matrix = tuple(
        tuple(
            coupling
            * coupling
            * sum(
                profiles[a][i] * wick_four_covariance[i][j] * profiles[b][j]
                for i in range(2)
                for j in range(2)
            )
            / (24 * 24)
            for b in range(2)
        )
        for a in range(2)
    )
    if retained_noise != transpose(retained_noise):
        raise AssertionError("retained potential-noise matrix should be symmetric")
    if retained_noise[0][0] <= 0 or det2(retained_noise) <= 0:
        raise AssertionError("retained potential-noise matrix should be positive definite")

    response_inverse: Matrix = (
        (Fraction(1, 2), Fraction(1, 4)),
        (Fraction(-1, 4), Fraction(1, 2)),
    )
    metric_covariance = matmul(
        matmul(response_inverse, retained_noise),
        transpose(response_inverse),
    )
    if metric_covariance != transpose(metric_covariance):
        raise AssertionError("potential-noise metric covariance should be symmetric")
    if metric_covariance[0][0] < 0 or det2(metric_covariance) < 0:
        raise AssertionError("potential-noise metric covariance should be positive")
    if trace(metric_covariance) > trace(retained_noise):
        raise AssertionError("unit certified response norm should bound potential-noise trace")


def check_retained_interacting_source_ward_diagnostics() -> None:
    # Finite analogue of the conservation condition B j_full = 0.
    ward: Matrix = (
        (Fraction(1), Fraction(-1), Fraction(2)),
        (Fraction(0), Fraction(1), Fraction(1)),
    )
    potential_source: Matrix = (
        (Fraction(3, 10),),
        (Fraction(-1, 5),),
        (Fraction(1, 4),),
    )
    ward_violation = matmul(ward, potential_source)
    if ward_violation == zero_matrix(2, 1):
        raise AssertionError("negative control failed: potential source was already conserved")

    ward_gram = matmul(ward, transpose(ward))
    if det2(ward_gram) == 0:
        raise AssertionError("finite Ward map should have full row rank")
    ward_gram_inverse = inverse2(ward_gram)
    longitudinal_projector = matmul(
        matmul(transpose(ward), ward_gram_inverse),
        ward,
    )
    transverse_projector = matsub(identity(3), longitudinal_projector)

    if matmul(transverse_projector, transverse_projector) != transverse_projector:
        raise AssertionError("retained Ward projector should be idempotent")
    if matmul(ward, transverse_projector) != zero_matrix(2, 3):
        raise AssertionError("retained Ward projector should land in ker B")

    diagnostic_source = matmul(transverse_projector, potential_source)
    least_norm_repair = matsub(diagnostic_source, potential_source)
    if least_norm_repair == zero_matrix(3, 1):
        raise AssertionError("inhomogeneous potential source needs a nonzero least-norm repair")
    if matmul(ward, diagnostic_source) != zero_matrix(2, 1):
        raise AssertionError("Ward-diagnostic projected source should be conserved")

    wrong_sign_source = matsub(potential_source, least_norm_repair)
    if matmul(ward, wrong_sign_source) == zero_matrix(2, 1):
        raise AssertionError("negative control failed: wrong-sign Ward repair conserved source")

    transverse_counterterm: Matrix = (
        (Fraction(-3, 7),),
        (Fraction(-1, 7),),
        (Fraction(1, 7),),
    )
    if matmul(ward, transverse_counterterm) != zero_matrix(2, 1):
        raise AssertionError("test transverse counterterm should lie in ker B")
    if matmul(ward, matadd(potential_source, transverse_counterterm)) == zero_matrix(2, 1):
        raise AssertionError("negative control failed: transverse ambiguity cancelled Ward violation")

    simple_ward: Matrix = ((Fraction(1), Fraction(0)),)
    simple_projector: Matrix = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    simple_raw_source: Matrix = ((Fraction(1),), (Fraction(0),))
    physical_completion: Matrix = ((Fraction(-1),), (Fraction(5, 7),))
    physical_source = matadd(simple_raw_source, physical_completion)
    projected_simple_source = matmul(simple_projector, simple_raw_source)
    if matmul(simple_ward, physical_source) != zero_matrix(1, 1):
        raise AssertionError("test physical completion should satisfy the Ward constraint")
    if projected_simple_source != zero_matrix(2, 1):
        raise AssertionError("least-norm diagnostic should erase this raw longitudinal source")
    if projected_simple_source == physical_source:
        raise AssertionError("negative control failed: projection was identified with physical completion")

    raw_partial_noise: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    physical_full_noise: Matrix = (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    projected_partial_noise = matmul(
        matmul(simple_projector, raw_partial_noise),
        transpose(simple_projector),
    )
    if projected_partial_noise != zero_matrix(2, 2):
        raise AssertionError("projected raw partial noise should vanish in this counterexample")
    if matmul(simple_ward, physical_full_noise) != zero_matrix(1, 2):
        raise AssertionError("full physical noise should have no longitudinal row")
    if matmul(physical_full_noise, transpose(simple_ward)) != zero_matrix(2, 1):
        raise AssertionError("full physical noise should have no longitudinal column")
    if (
        matmul(matmul(simple_projector, physical_full_noise), transpose(simple_projector))
        != physical_full_noise
    ):
        raise AssertionError("projector should act as identity on already Ward-clean full noise")
    if projected_partial_noise == physical_full_noise:
        raise AssertionError("negative control failed: partial projected noise became full noise")

    partial_noise: Matrix = (
        (Fraction(5, 2), Fraction(1, 3), Fraction(1, 4)),
        (Fraction(1, 3), Fraction(3, 2), Fraction(-1, 5)),
        (Fraction(1, 4), Fraction(-1, 5), Fraction(4, 3)),
    )
    if (
        partial_noise[0][0] <= 0
        or det2((partial_noise[0][:2], partial_noise[1][:2])) <= 0
        or det3(partial_noise) <= 0
    ):
        raise AssertionError("test partial noise matrix should be positive definite")

    diagnostic_noise = matmul(
        matmul(transverse_projector, partial_noise),
        transpose(transverse_projector),
    )
    if diagnostic_noise != transpose(diagnostic_noise):
        raise AssertionError("Ward-diagnostic noise should be symmetric")
    if matmul(ward, diagnostic_noise) != zero_matrix(2, 3):
        raise AssertionError("Ward-diagnostic noise should have no longitudinal row")
    if matmul(diagnostic_noise, transpose(ward)) != zero_matrix(3, 2):
        raise AssertionError("Ward-diagnostic noise should have no longitudinal column")
    if trace(diagnostic_noise) > trace(partial_noise):
        raise AssertionError("orthogonal Ward projection should not increase diagnostic trace")

    if matmul(ward, partial_noise) == zero_matrix(2, 3):
        raise AssertionError("negative control failed: unprojected partial noise was Ward-clean")

    for test_vector in [
        ((Fraction(1),), (Fraction(2),), (Fraction(-1),)),
        ((Fraction(0),), (Fraction(1),), (Fraction(3),)),
        ((Fraction(2),), (Fraction(-1),), (Fraction(1),)),
    ]:
        if quadratic_form(diagnostic_noise, test_vector) < 0:
            raise AssertionError("Ward-diagnostic noise should be positive semidefinite")

    response_inverse: Matrix = (
        (Fraction(1, 2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 3), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1, 4)),
    )
    metric_covariance = matmul(
        matmul(response_inverse, diagnostic_noise),
        transpose(response_inverse),
    )
    if metric_covariance != transpose(metric_covariance):
        raise AssertionError("diagnostic metric covariance should be symmetric")
    if trace(metric_covariance) > trace(diagnostic_noise):
        raise AssertionError("contractive response should bound diagnostic noise trace")


def check_flrw_interacting_source_noise_closure() -> None:
    # Homogeneous FLRW retained cell for a time-dependent lambda phi^4
    # potential coordinate.  The correction pressure is what lets the same
    # source satisfy both Friedmann and Raychaudhuri response equations.
    hubble = Fraction(2)
    kappa = Fraction(3, 7)
    potential_density = Fraction(3, 5)
    potential_density_dot = Fraction(1, 4)
    potential_pressure = -potential_density

    potential_ward_residual = potential_density_dot + 3 * hubble * (
        potential_density + potential_pressure
    )
    if potential_ward_residual != potential_density_dot:
        raise AssertionError("potential-only Ward residual should be the density drift")
    if potential_ward_residual == 0:
        raise AssertionError("negative control failed: time-dependent potential source conserved")

    correction_density = Fraction(1, 10)
    correction_density_dot = -Fraction(1, 20)
    correction_pressure = -correction_density - (
        potential_density_dot + correction_density_dot
    ) / (3 * hubble)
    if correction_pressure != -Fraction(2, 15):
        raise AssertionError("FLRW correction pressure closure changed")

    full_density = potential_density + correction_density
    full_density_dot = potential_density_dot + correction_density_dot
    full_pressure = potential_pressure + correction_pressure
    full_ward_residual = full_density_dot + 3 * hubble * (
        full_density + full_pressure
    )
    if full_ward_residual != 0:
        raise AssertionError("Ward-closed FLRW interacting source should conserve")

    naive_full_pressure = -full_density
    naive_residual = full_density_dot + 3 * hubble * (
        full_density + naive_full_pressure
    )
    if naive_residual == 0:
        raise AssertionError("negative control failed: p=-rho shortcut conserved")

    # In a de Sitter retained cell, differentiating Friedmann and using
    # Raychaudhuri agree exactly iff the perturbing stress source conserves.
    friedmann_hubble_shift = kappa * full_density / (6 * hubble)
    if friedmann_hubble_shift != Fraction(1, 40):
        raise AssertionError("FLRW Friedmann Hubble shift changed")
    friedmann_hubble_dot = kappa * full_density_dot / (6 * hubble)
    raychaudhuri_hubble_dot = -kappa * (full_density + full_pressure) / 2
    if friedmann_hubble_dot != raychaudhuri_hubble_dot:
        raise AssertionError("Ward-closed source should match Friedmann and Raychaudhuri")
    if friedmann_hubble_dot != Fraction(1, 140):
        raise AssertionError("FLRW Hubble-drift response changed")

    potential_friedmann_hubble_dot = (
        kappa * potential_density_dot / (6 * hubble)
    )
    potential_raychaudhuri_hubble_dot = -kappa * (
        potential_density + potential_pressure
    ) / 2
    if potential_raychaudhuri_hubble_dot != 0:
        raise AssertionError("potential equation of state should give zero Raychaudhuri drift")
    if potential_friedmann_hubble_dot == potential_raychaudhuri_hubble_dot:
        raise AssertionError("negative control failed: drifting vacuum energy was metric-compatible")

    # Stochastic homogeneous source coordinates are
    # (xi_{dot rho}, xi_rho, xi_p).  The Ward map is
    # xi_{dot rho} + 3 H (xi_rho + xi_p).
    ward: Matrix = ((Fraction(1), 3 * hubble, 3 * hubble),)
    state_covariance: Matrix = (
        (Fraction(2), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(1)),
    )
    if det2(state_covariance) <= 0:
        raise AssertionError("test FLRW noise state covariance should be positive")

    ward_clean_noise_map: Matrix = (
        (Fraction(0), -3 * hubble),
        (Fraction(1), Fraction(1)),
        (Fraction(-1), Fraction(0)),
    )
    if matmul(ward, ward_clean_noise_map) != zero_matrix(1, 2):
        raise AssertionError("FLRW stress-noise map should satisfy the Ward condition")
    full_noise = matmul(
        matmul(ward_clean_noise_map, state_covariance),
        transpose(ward_clean_noise_map),
    )
    expected_full_noise: Matrix = (
        (Fraction(36), Fraction(-8), Fraction(2)),
        (Fraction(-8), Fraction(11, 3), Fraction(-7, 3)),
        (Fraction(2), Fraction(-7, 3), Fraction(2)),
    )
    if full_noise != expected_full_noise:
        raise AssertionError("Ward-clean FLRW stress-noise covariance changed")
    if matmul(ward, full_noise) != zero_matrix(1, 3):
        raise AssertionError("FLRW stress noise should have no Ward row")
    if matmul(full_noise, transpose(ward)) != zero_matrix(3, 1):
        raise AssertionError("FLRW stress noise should have no Ward column")

    for test_vector in [
        ((Fraction(1),), (Fraction(0),), (Fraction(0),)),
        ((Fraction(0),), (Fraction(1),), (Fraction(-1),)),
        ((Fraction(2),), (Fraction(1),), (Fraction(3),)),
    ]:
        if quadratic_form(full_noise, test_vector) < 0:
            raise AssertionError("FLRW Ward-clean noise should be positive semidefinite")

    potential_noise_amplitude = Fraction(5, 3)
    potential_noise_map: Matrix = (
        (Fraction(1),),
        (Fraction(1),),
        (Fraction(-1),),
    )
    if matmul(ward, potential_noise_map) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: potential-only noise was Ward-clean")
    potential_noise = tuple(
        tuple(
            potential_noise_amplitude
            * potential_noise_map[row][0]
            * potential_noise_map[col][0]
            for col in range(3)
        )
        for row in range(3)
    )
    if matmul(ward, potential_noise) == zero_matrix(1, 3):
        raise AssertionError("negative control failed: potential-only noise passed Ward row test")

    friedmann_hubble_noise: Matrix = ((kappa / (6 * hubble),), (Fraction(0),), (Fraction(0),))
    raychaudhuri_hubble_noise: Matrix = (
        (Fraction(0),),
        (-kappa / 2,),
        (-kappa / 2,),
    )
    route_difference = matsub(friedmann_hubble_noise, raychaudhuri_hubble_noise)
    if transpose(route_difference) != ((Fraction(1, 28), Fraction(3, 14), Fraction(3, 14)),):
        raise AssertionError("FLRW Hubble-noise route difference changed")

    full_route_disagreement = quadratic_form(full_noise, route_difference)
    if full_route_disagreement != 0:
        raise AssertionError("Ward-clean noise should make Hubble-noise routes agree")

    potential_route_disagreement = quadratic_form(potential_noise, route_difference)
    if potential_route_disagreement != Fraction(5, 2352):
        raise AssertionError("potential-only Hubble-noise mismatch changed")
    if potential_route_disagreement == 0:
        raise AssertionError("negative control failed: potential-only Hubble noise was consistent")

    hubble_observable: Matrix = ((Fraction(0),), (kappa / (6 * hubble),), (Fraction(0),))
    full_hubble_variance = quadratic_form(full_noise, hubble_observable)
    potential_hubble_variance = quadratic_form(potential_noise, hubble_observable)
    if full_hubble_variance != Fraction(11, 2352):
        raise AssertionError("Ward-clean FLRW Hubble variance changed")
    if potential_hubble_variance != Fraction(5, 2352):
        raise AssertionError("potential-only FLRW Hubble variance changed")
    if potential_hubble_variance >= full_hubble_variance:
        raise AssertionError("negative control failed: pressure/derivative noise was not needed")


def check_retained_ward_completion_laboratory() -> None:
    # Worked two-coordinate analogue of the retained source/noise laboratory.
    ward: Matrix = ((Fraction(1), Fraction(-1)),)
    raw_source: Matrix = ((Fraction(3),), (Fraction(1),))
    ward_violation = matmul(ward, raw_source)
    if ward_violation != ((Fraction(2),),):
        raise AssertionError("test raw source should have the declared Ward violation")

    ward_gram = matmul(ward, transpose(ward))
    ward_gram_inverse: Matrix = ((Fraction(1, 2),),)
    if ward_gram != ((Fraction(2),),):
        raise AssertionError("one-constraint Ward Gram changed")
    projector = matsub(
        identity(2),
        matmul(matmul(transpose(ward), ward_gram_inverse), ward),
    )
    expected_projector: Matrix = (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    if projector != expected_projector:
        raise AssertionError("two-coordinate Ward projector changed")
    if matmul(projector, projector) != projector:
        raise AssertionError("two-coordinate Ward projector should be idempotent")

    diagnostic_source = matmul(projector, raw_source)
    expected_diagnostic_source: Matrix = ((Fraction(2),), (Fraction(2),))
    if diagnostic_source != expected_diagnostic_source:
        raise AssertionError("least-norm retained source changed")
    if matmul(ward, diagnostic_source) != zero_matrix(1, 1):
        raise AssertionError("least-norm retained source should be Ward-clean")

    least_norm_repair = matsub(diagnostic_source, raw_source)
    if least_norm_repair != ((Fraction(-1),), (Fraction(1),)):
        raise AssertionError("least-norm retained repair changed")
    wrong_sign_source = matsub(raw_source, least_norm_repair)
    if matmul(ward, wrong_sign_source) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: wrong-sign repair was conserved")

    transverse_completion: Matrix = ((Fraction(5, 3),), (Fraction(5, 3),))
    if matmul(ward, transverse_completion) != zero_matrix(1, 1):
        raise AssertionError("test transverse completion should be Ward-clean")
    if matmul(ward, matadd(raw_source, transverse_completion)) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: transverse completion fixed longitudinal source")

    response_inverse: Matrix = (
        (Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(1, 3)),
    )
    diagnostic_response = matmul(response_inverse, diagnostic_source)
    if diagnostic_response != ((Fraction(4, 3),), (Fraction(4, 3),)):
        raise AssertionError("Ward-reduced retained response changed")
    if matmul(ward, raw_source) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: nonconserved raw source entered response sector")

    raw_noise: Matrix = (
        (Fraction(5), Fraction(1)),
        (Fraction(1), Fraction(2)),
    )
    if raw_noise[0][0] <= 0 or det2(raw_noise) <= 0:
        raise AssertionError("test raw partial noise should be positive definite")
    if matmul(ward, raw_noise) == zero_matrix(1, 2):
        raise AssertionError("negative control failed: raw partial noise was Ward-clean")

    diagnostic_noise = matmul(matmul(projector, raw_noise), transpose(projector))
    expected_diagnostic_noise: Matrix = (
        (Fraction(9, 4), Fraction(9, 4)),
        (Fraction(9, 4), Fraction(9, 4)),
    )
    if diagnostic_noise != expected_diagnostic_noise:
        raise AssertionError("projected retained diagnostic noise changed")
    if matmul(ward, diagnostic_noise) != zero_matrix(1, 2):
        raise AssertionError("diagnostic noise should have no longitudinal row")
    if matmul(diagnostic_noise, transpose(ward)) != zero_matrix(2, 1):
        raise AssertionError("diagnostic noise should have no longitudinal column")
    for test_vector in [
        ((Fraction(1),), (Fraction(1),)),
        ((Fraction(1),), (Fraction(-1),)),
        ((Fraction(2),), (Fraction(3),)),
    ]:
        if quadratic_form(diagnostic_noise, test_vector) < 0:
            raise AssertionError("diagnostic retained noise should be positive semidefinite")

    missing_ward_clean_noise: Matrix = (
        (Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(1, 3)),
    )
    if matmul(ward, missing_ward_clean_noise) != zero_matrix(1, 2):
        raise AssertionError("missing physical noise should be Ward-clean")
    if matmul(missing_ward_clean_noise, transpose(ward)) != zero_matrix(2, 1):
        raise AssertionError("missing physical noise should have no longitudinal column")

    full_noise = matadd(diagnostic_noise, missing_ward_clean_noise)
    if trace(full_noise) != Fraction(31, 6):
        raise AssertionError("full Ward-clean noise budget changed")
    diagnostic_metric_covariance = matmul(
        matmul(response_inverse, diagnostic_noise),
        transpose(response_inverse),
    )
    full_metric_covariance = matmul(
        matmul(response_inverse, full_noise),
        transpose(response_inverse),
    )
    if trace(diagnostic_metric_covariance) != Fraction(2):
        raise AssertionError("diagnostic metric covariance trace changed")
    if trace(full_metric_covariance) != Fraction(62, 27):
        raise AssertionError("full metric covariance trace changed")
    if trace(diagnostic_metric_covariance) >= trace(full_metric_covariance):
        raise AssertionError("negative control failed: missing noise did not enlarge fluctuation budget")


def check_interacting_stress_tensor_noise_package() -> None:
    # A finite retained analogue of T_int = sum_i T_i.  The total operator
    # map is Ward-clean, while individual pieces are not.
    ward: Matrix = (
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(-1)),
    )
    state_covariance: Matrix = (
        (Fraction(2), Fraction(1, 3)),
        (Fraction(1, 3), Fraction(3)),
    )
    if det2(state_covariance) <= 0:
        raise AssertionError("test state covariance should be positive")

    potential_map: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    bogoliubov_map: Matrix = (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(1)),
        (Fraction(0), Fraction(1)),
    )
    counterterm_map: Matrix = (
        (Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(1)),
    )
    component_maps = (potential_map, bogoliubov_map, counterterm_map)
    total_map = matsum(component_maps)
    if matmul(ward, total_map) != zero_matrix(2, 2):
        raise AssertionError("full interacting stress-tensor map should be Ward-clean")
    for component in component_maps:
        if matmul(ward, component) == zero_matrix(2, 2):
            raise AssertionError("test components should expose nonconserved partial pieces")

    def covariance_from_map(operator_map: Matrix) -> Matrix:
        return matmul(matmul(operator_map, state_covariance), transpose(operator_map))

    def cross_covariance(left_map: Matrix, right_map: Matrix) -> Matrix:
        return matmul(matmul(left_map, state_covariance), transpose(right_map))

    full_noise = covariance_from_map(total_map)
    component_variance_only = matsum(tuple(covariance_from_map(m) for m in component_maps))
    component_cross_terms = matsum(
        tuple(
            cross_covariance(component_maps[i], component_maps[j])
            for i in range(len(component_maps))
            for j in range(len(component_maps))
            if i != j
        )
    )
    if full_noise != matadd(component_variance_only, component_cross_terms):
        raise AssertionError("full noise should be the double component-covariance sum")
    if component_variance_only == full_noise:
        raise AssertionError("negative control failed: component variances alone gave full noise")
    if matmul(ward, full_noise) != zero_matrix(2, 3):
        raise AssertionError("full interacting noise should have no longitudinal row")
    if matmul(full_noise, transpose(ward)) != zero_matrix(3, 2):
        raise AssertionError("full interacting noise should have no longitudinal column")
    if matmul(ward, component_variance_only) == zero_matrix(2, 3):
        raise AssertionError("negative control failed: diagonal component noise was Ward-clean")

    for test_vector in [
        ((Fraction(1),), (Fraction(0),), (Fraction(-1),)),
        ((Fraction(2),), (Fraction(-3),), (Fraction(1),)),
        ((Fraction(1),), (Fraction(1),), (Fraction(1),)),
    ]:
        if quadratic_form(full_noise, test_vector) < 0:
            raise AssertionError("full interacting noise should be positive semidefinite")

    state_mean: Matrix = ((Fraction(3),), (Fraction(5),))
    c_number_counterterm: Matrix = (
        (Fraction(2),),
        (Fraction(2),),
        (Fraction(2),),
    )
    full_mean_source = matadd(matmul(total_map, state_mean), c_number_counterterm)
    if matmul(ward, full_mean_source) != zero_matrix(2, 1):
        raise AssertionError("c-number shifted full source should remain Ward-clean")

    wrong_c_number_noise = matadd(full_noise, matmul(c_number_counterterm, transpose(c_number_counterterm)))
    if wrong_c_number_noise == full_noise:
        raise AssertionError("test c-number counterterm should visibly change a wrong noise formula")
    if matmul(ward, wrong_c_number_noise) != zero_matrix(2, 3):
        raise AssertionError("conserved c-number counterterm should not spoil the Ward row test")
    if matmul(wrong_c_number_noise, transpose(ward)) != zero_matrix(3, 2):
        raise AssertionError("conserved c-number counterterm should not spoil the Ward column test")

    finite_operator_mixing: Matrix = (
        (Fraction(0), Fraction(1, 2)),
        (Fraction(0), Fraction(1, 2)),
        (Fraction(0), Fraction(1, 2)),
    )
    if matmul(ward, finite_operator_mixing) != zero_matrix(2, 2):
        raise AssertionError("test finite operator mixing should preserve the Ward map")
    mixed_map = matadd(total_map, finite_operator_mixing)
    mixed_noise = covariance_from_map(mixed_map)
    mixing_covariance = covariance_from_map(finite_operator_mixing)
    mixing_cross_terms = matadd(
        cross_covariance(total_map, finite_operator_mixing),
        cross_covariance(finite_operator_mixing, total_map),
    )
    if mixed_noise != matadd(matadd(full_noise, mixing_cross_terms), mixing_covariance):
        raise AssertionError("finite operator mixing noise requires cross terms")
    if mixed_noise == matadd(full_noise, mixing_covariance):
        raise AssertionError("negative control failed: finite mixing cross terms were omitted")
    if matmul(ward, mixed_noise) != zero_matrix(2, 3):
        raise AssertionError("finite-mixed full noise should satisfy the Ward row condition")
    if matmul(mixed_noise, transpose(ward)) != zero_matrix(3, 2):
        raise AssertionError("finite-mixed full noise should satisfy the Ward column condition")


def check_interacting_influence_functional_consistency() -> None:
    # The mean source, retarded feedback kernel, and connected noise should be
    # derivative data of one retained closed-time-path influence functional.
    ward: Matrix = ((Fraction(1), -Fraction(1)),)
    source: Matrix = ((Fraction(3),), (Fraction(3),))
    retarded_response: Matrix = (
        (Fraction(1, 5), Fraction(1, 5)),
        (Fraction(1, 5), Fraction(1, 5)),
    )
    noise: Matrix = (
        (Fraction(2), Fraction(2)),
        (Fraction(2), Fraction(2)),
    )

    if matmul(ward, source) != zero_matrix(1, 1):
        raise AssertionError("interacting CTP source should be Ward-clean")
    if matmul(ward, retarded_response) != zero_matrix(1, 2):
        raise AssertionError("interacting CTP retarded kernel should have no longitudinal row")
    if matmul(retarded_response, transpose(ward)) != zero_matrix(2, 1):
        raise AssertionError("interacting CTP retarded kernel should have no longitudinal column")
    if matmul(ward, noise) != zero_matrix(1, 2):
        raise AssertionError("interacting CTP noise should have no longitudinal row")
    if matmul(noise, transpose(ward)) != zero_matrix(2, 1):
        raise AssertionError("interacting CTP noise should have no longitudinal column")

    physical_test: Matrix = ((Fraction(2),), (Fraction(2),))
    longitudinal_test: Matrix = ((Fraction(1),), (-Fraction(1),))
    if quadratic_form(noise, physical_test) <= 0:
        raise AssertionError("interacting CTP noise should be positive on physical tests")
    if quadratic_form(noise, longitudinal_test) != 0:
        raise AssertionError("interacting CTP noise should vanish on pure Ward tests")

    center: Matrix = ((Fraction(5),), (Fraction(7),))
    difference: Matrix = ((Fraction(1),), (Fraction(2),))

    def influence_quadratic(h_delta: Matrix, h_center: Matrix) -> tuple[Fraction, Fraction]:
        real_part = (
            matmul(transpose(h_delta), source)[0][0]
            + matmul(matmul(transpose(h_delta), retarded_response), h_center)[0][0]
        )
        imaginary_part = Fraction(1, 2) * quadratic_form(noise, h_delta)
        return real_part, imaginary_part

    assert_equal(
        "closed-time-path normalization removes equal-branch influence",
        influence_quadratic(zero_matrix(2, 1), center),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "pure Ward difference direction decouples from CTP package",
        influence_quadratic(longitudinal_test, center),
        (Fraction(0), Fraction(0)),
    )
    real_part, imaginary_part = influence_quadratic(difference, center)
    assert_equal("interacting CTP real quadratic coordinate", real_part, Fraction(81, 5))
    assert_equal("interacting CTP imaginary noise coordinate", imaginary_part, Fraction(9))

    h_c_only_term = quadratic_form(
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))),
        center,
    )
    if h_c_only_term == 0:
        raise AssertionError("test h_c h_c term should be visible")
    assert_equal(
        "spurious h_c h_c term would violate CTP normalization",
        h_c_only_term == influence_quadratic(zero_matrix(2, 1), center)[1],
        False,
    )

    def is_retarded_time_kernel(kernel: Matrix) -> bool:
        return all(
            kernel[row][col] == 0
            for row in range(len(kernel))
            for col in range(row + 1, len(kernel[0]))
        )

    retarded_time_kernel: Matrix = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(2), Fraction(3), Fraction(0)),
        (Fraction(4), Fraction(5), Fraction(6)),
    )
    advanced_polluted_kernel: Matrix = (
        (Fraction(1), Fraction(0), Fraction(7)),
        (Fraction(2), Fraction(3), Fraction(0)),
        (Fraction(4), Fraction(5), Fraction(6)),
    )
    assert_equal(
        "finite CTP response has retarded support",
        is_retarded_time_kernel(retarded_time_kernel),
        True,
    )
    assert_equal(
        "advanced response pollution is rejected",
        is_retarded_time_kernel(advanced_polluted_kernel),
        False,
    )

    spectral_density = Fraction(6, 7)
    coth_half_beta_omega = Fraction(5, 3)
    kms_noise = Fraction(1, 2) * coth_half_beta_omega * spectral_density
    assert_equal("interacting CTP KMS noise spectrum", kms_noise, Fraction(5, 7))
    independently_chosen_noise = Fraction(4, 7)
    assert_equal(
        "independent noise spectrum violates retained FDT package",
        independently_chosen_noise == kms_noise,
        False,
    )


def check_backreaction_small_gain_stability() -> None:
    # Finite retained model for D_full = D0 - R_ret and
    # D_full^{-1} = (I - D0^{-1} R_ret)^{-1} D0^{-1}.
    gravitational_operator: Matrix = (
        (Fraction(3), Fraction(0)),
        (Fraction(0), Fraction(4)),
    )
    gravitational_inverse = inverse2(gravitational_operator)
    retarded_feedback: Matrix = (
        (Fraction(1, 5), Fraction(1, 10)),
        (Fraction(1, 20), Fraction(1, 6)),
    )
    full_operator = matsub(gravitational_operator, retarded_feedback)
    full_inverse = inverse2(full_operator)

    feedback_map = matmul(gravitational_inverse, retarded_feedback)
    neumann_inverse = inverse2(matsub(identity(2), feedback_map))
    small_gain_inverse = matmul(neumann_inverse, gravitational_inverse)
    if small_gain_inverse != full_inverse:
        raise AssertionError("small-gain inverse should equal the exact full inverse")
    if matmul(full_operator, small_gain_inverse) != identity(2):
        raise AssertionError("full feedback inverse should invert D_full")

    certified_m0 = Fraction(1, 2)
    certified_eta = Fraction(1, 4)
    if frobenius_norm_sq(gravitational_inverse) > certified_m0 * certified_m0:
        raise AssertionError("gravitational inverse exceeds the certified M0 bound")
    if frobenius_norm_sq(feedback_map) > certified_eta * certified_eta:
        raise AssertionError("retarded feedback exceeds the certified small-gain bound")
    certified_full_bound = certified_m0 / (1 - certified_eta)

    ward: Matrix = ((Fraction(1), Fraction(-1)),)
    source: Matrix = ((Fraction(2, 7),), (Fraction(2, 7),))
    if matmul(ward, source) != zero_matrix(1, 1):
        raise AssertionError("test source should be Ward-clean")
    nonconserved_source: Matrix = ((Fraction(2, 7),), (Fraction(1, 7),))
    if matmul(ward, nonconserved_source) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: nonconserved source passed Ward test")

    mean_metric = matmul(full_inverse, source)
    if squared_norm(mean_metric) > certified_full_bound * certified_full_bound * squared_norm(source):
        raise AssertionError("small-gain mean-response bound failed")

    ward_clean_noise: Matrix = (
        (Fraction(5, 6), Fraction(5, 6)),
        (Fraction(5, 6), Fraction(5, 6)),
    )
    if matmul(ward, ward_clean_noise) != zero_matrix(1, 2):
        raise AssertionError("test full noise should have no longitudinal row")
    if matmul(ward_clean_noise, transpose(ward)) != zero_matrix(2, 1):
        raise AssertionError("test full noise should have no longitudinal column")
    if quadratic_form(ward_clean_noise, ((Fraction(1),), (Fraction(1),))) <= 0:
        raise AssertionError("Ward-clean noise should have positive retained variance")
    if quadratic_form(ward_clean_noise, ((Fraction(1),), (Fraction(-1),))) != 0:
        raise AssertionError("Ward-clean noise should vanish on the longitudinal test vector")

    unclean_noise: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    if matmul(ward, unclean_noise) == zero_matrix(1, 2):
        raise AssertionError("negative control failed: unclean noise passed Ward row test")
    if unclean_noise == ward_clean_noise:
        raise AssertionError("negative control failed: clean and unclean noise coincided")

    metric_covariance = matmul(matmul(full_inverse, ward_clean_noise), transpose(full_inverse))
    if metric_covariance != transpose(metric_covariance):
        raise AssertionError("small-gain metric covariance should be symmetric")
    for test_vector in [
        ((Fraction(1),), (Fraction(0),)),
        ((Fraction(1),), (Fraction(-2),)),
        ((Fraction(3),), (Fraction(5),)),
    ]:
        if quadratic_form(metric_covariance, test_vector) < 0:
            raise AssertionError("small-gain metric covariance should be positive semidefinite")
    if trace(metric_covariance) > certified_full_bound * certified_full_bound * trace(ward_clean_noise):
        raise AssertionError("small-gain noise-amplification trace bound failed")

    retained_noise_trace = Fraction(1, 4)
    missing_noise_trace = trace(ward_clean_noise) - retained_noise_trace
    if missing_noise_trace <= 0:
        raise AssertionError("test retained noise should leave a positive missing trace budget")
    wrong_truncated_bound = certified_full_bound * certified_full_bound * retained_noise_trace
    correct_residual_bound = certified_full_bound * certified_full_bound * (
        retained_noise_trace + missing_noise_trace
    )
    if trace(metric_covariance) > correct_residual_bound:
        raise AssertionError("residual-augmented noise trace bound failed")
    if trace(metric_covariance) <= wrong_truncated_bound:
        raise AssertionError("negative control failed: missing noise trace was not needed")

    singular_feedback = gravitational_operator
    singular_full_operator = matsub(gravitational_operator, singular_feedback)
    if det2(singular_full_operator) != 0:
        raise AssertionError("negative control should produce a singular feedback operator")

    large_feedback: Matrix = (
        (Fraction(4), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    large_feedback_map = matmul(gravitational_inverse, large_feedback)
    if frobenius_norm_sq(large_feedback_map) < Fraction(1):
        raise AssertionError("negative control should violate the small-gain hypothesis")

    unstable_operator: Matrix = (
        (Fraction(1, 50), Fraction(0)),
        (Fraction(0), Fraction(4)),
    )
    unstable_inverse = inverse2(unstable_operator)
    unstable_metric_covariance = matmul(
        matmul(unstable_inverse, ward_clean_noise),
        transpose(unstable_inverse),
    )
    if matmul(ward, ward_clean_noise) != zero_matrix(1, 2):
        raise AssertionError("test conserved noise was unexpectedly not Ward-clean")
    if trace(unstable_metric_covariance) <= 100 * trace(ward_clean_noise):
        raise AssertionError("conserved noise can still be amplified beyond validity")


def check_nonlinear_backreaction_fixed_point_chart() -> None:
    # Exact retained analogue of the finite-window nonlinear map
    # h = h_lin + G_full(Q_2(h,h) + S_st(h) + R_nl(h)).
    m_full = Fraction(2, 3)
    radius = Fraction(1, 2)
    h_linear_norm = Fraction(1, 5)
    quadratic_bound = Fraction(1, 4)
    state_lipschitz = Fraction(1, 8)
    residual_bound = Fraction(1, 20)
    residual_lipschitz = Fraction(1, 8)

    nonlinear_budget = (
        quadratic_bound * radius * radius
        + state_lipschitz * radius
        + residual_bound
    )
    self_map_bound = h_linear_norm + m_full * nonlinear_budget
    if self_map_bound != Fraction(19, 60):
        raise AssertionError("nonlinear retained self-map budget changed")
    if self_map_bound > radius:
        raise AssertionError("nonlinear retained map should stay inside the chart")

    contraction = m_full * (
        2 * quadratic_bound * radius + state_lipschitz + residual_lipschitz
    )
    if contraction != Fraction(1, 3):
        raise AssertionError("nonlinear contraction constant changed")
    if contraction >= 1:
        raise AssertionError("nonlinear retained map should be contractive")

    correction_bound = m_full * nonlinear_budget / (1 - contraction)
    if correction_bound != Fraction(7, 40):
        raise AssertionError("nonlinear correction bound changed")
    if h_linear_norm + correction_bound > radius:
        raise AssertionError("nonlinear correction should keep the solution in the chart")

    ward: Matrix = ((Fraction(1), Fraction(-1)),)
    retained_nonlinear_source: Matrix = ((Fraction(3, 10),), (Fraction(3, 10),))
    if matmul(ward, retained_nonlinear_source) != zero_matrix(1, 1):
        raise AssertionError("test nonlinear source should be Ward-clean")
    nonconserved_nonlinear_source: Matrix = ((Fraction(3, 10),), (Fraction(1, 5),))
    if matmul(ward, nonconserved_nonlinear_source) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: nonconserved nonlinear source passed")

    bad_quadratic_bound = Fraction(2)
    bad_quadratic_contraction = m_full * (
        2 * bad_quadratic_bound * radius + state_lipschitz + residual_lipschitz
    )
    if bad_quadratic_contraction <= 1:
        raise AssertionError("negative control failed: overlarge nonlinear feedback accepted")

    omitted_state_lipschitz_contraction = m_full * (
        2 * quadratic_bound * radius + residual_lipschitz
    )
    bad_state_lipschitz = Fraction(3, 2)
    actual_state_contraction = m_full * (
        2 * quadratic_bound * radius + bad_state_lipschitz + residual_lipschitz
    )
    if omitted_state_lipschitz_contraction >= 1:
        raise AssertionError("test omitted-state contraction should look falsely safe")
    if actual_state_contraction <= 1:
        raise AssertionError("negative control failed: omitted state transport was harmless")

    omitted_residual_lipschitz_contraction = m_full * (
        2 * quadratic_bound * radius + state_lipschitz
    )
    bad_residual_lipschitz = Fraction(3, 2)
    actual_residual_contraction = m_full * (
        2 * quadratic_bound * radius + state_lipschitz + bad_residual_lipschitz
    )
    if omitted_residual_lipschitz_contraction >= 1:
        raise AssertionError("test omitted-residual contraction should look falsely safe")
    if actual_residual_contraction <= 1:
        raise AssertionError("negative control failed: omitted residual variation was harmless")

    counterexample_radius = Fraction(1)
    counterexample_residual_bound = Fraction(1, 2)
    sup_only_self_map_bound = counterexample_residual_bound
    sup_only_contraction = Fraction(0)
    if sup_only_self_map_bound > counterexample_radius:
        raise AssertionError("test bounded residual should be a self-map")
    if sup_only_contraction >= 1:
        raise AssertionError("test sup-only contraction should look falsely safe")

    def sqrt_fraction(value: Fraction) -> Fraction:
        numerator_root = math.isqrt(value.numerator)
        denominator_root = math.isqrt(value.denominator)
        if (
            numerator_root * numerator_root != value.numerator
            or denominator_root * denominator_root != value.denominator
        ):
            raise AssertionError("test fraction does not have an exact square root")
        return Fraction(numerator_root, denominator_root)

    def bounded_non_lipschitz_residual(h_value: Fraction) -> Fraction:
        if h_value == 0:
            return Fraction(0)
        sign = 1 if h_value > 0 else -1
        return sign * Fraction(1, 2) * sqrt_fraction(abs(h_value))

    counterexample_fixed_points = (
        Fraction(0),
        Fraction(1, 4),
        Fraction(-1, 4),
    )
    if any(
        bounded_non_lipschitz_residual(point) != point
        for point in counterexample_fixed_points
    ):
        raise AssertionError("bounded non-Lipschitz residual fixed points changed")
    if len(set(counterexample_fixed_points)) != 3:
        raise AssertionError("negative control failed: residual counterexample was unique")

    near_zero_ratios = []
    for denominator_root in (4, 8, 16, 32):
        h_value = Fraction(1, denominator_root * denominator_root)
        ratio = abs(
            bounded_non_lipschitz_residual(h_value)
            - bounded_non_lipschitz_residual(Fraction(0))
        ) / h_value
        near_zero_ratios.append(ratio)
    if near_zero_ratios != [Fraction(2), Fraction(4), Fraction(8), Fraction(16)]:
        raise AssertionError("negative control failed: residual ratios did not grow")

    signed_residual = Fraction(-1, 2)
    signed_self_map_bound = h_linear_norm + m_full * (
        quadratic_bound * radius * radius
        + state_lipschitz * radius
        + signed_residual
    )
    absolute_residual_self_map_bound = h_linear_norm + m_full * (
        quadratic_bound * radius * radius
        + state_lipschitz * radius
        + abs(signed_residual)
    )
    if signed_self_map_bound > radius:
        raise AssertionError("test signed residual should appear falsely safe")
    if absolute_residual_self_map_bound <= radius:
        raise AssertionError("negative control failed: residual cancellation was not rejected")

    linear_noise_trace = Fraction(1, 30)
    missing_noise_trace = Fraction(1, 20)
    nonlinear_noise_tail = Fraction(1, 15)
    noise_amplification = m_full * m_full / ((1 - contraction) * (1 - contraction))
    full_noise_validity_bound = (
        linear_noise_trace
        + noise_amplification * missing_noise_trace
        + nonlinear_noise_tail
    )
    if full_noise_validity_bound != Fraction(3, 20):
        raise AssertionError("nonlinear noise validity budget changed")
    validity_scale = Fraction(1, 5)
    if full_noise_validity_bound >= validity_scale:
        raise AssertionError("test nonlinear noise budget should fit the declared chart")

    too_small_metric_scale = Fraction(1, 9)
    if linear_noise_trace >= too_small_metric_scale:
        raise AssertionError("test linear-only noise should look falsely safe")
    if full_noise_validity_bound <= too_small_metric_scale:
        raise AssertionError("negative control failed: nonlinear/missing noise budget was omitted")


def check_retained_metric_observable_output() -> None:
    # Finite retained metric observable
    # X = X0 + ell_X^T h + 1/2 h^T Q_X h + R_X(h).
    h_mean: Matrix = ((Fraction(1, 3),), (Fraction(1, 6),))
    metric_covariance: Matrix = (
        (Fraction(1, 20), Fraction(1, 60)),
        (Fraction(1, 60), Fraction(1, 30)),
    )
    if metric_covariance != transpose(metric_covariance):
        raise AssertionError("metric covariance should be symmetric")
    for test_vector in (
        ((Fraction(1),), (Fraction(0),)),
        ((Fraction(0),), (Fraction(1),)),
        ((Fraction(3),), (Fraction(-2),)),
    ):
        if quadratic_form(metric_covariance, test_vector) < 0:
            raise AssertionError("metric covariance should be positive semidefinite")

    ell_x: Matrix = ((Fraction(2),), (Fraction(1),))
    pure_gauge_direction: Matrix = ((Fraction(1),), (Fraction(-2),))
    if matmul(transpose(ell_x), pure_gauge_direction) != zero_matrix(1, 1):
        raise AssertionError("test observable should annihilate the pure-gauge direction")
    coordinate_probe: Matrix = ((Fraction(1),), (Fraction(0),))
    if matmul(transpose(coordinate_probe), pure_gauge_direction) == zero_matrix(1, 1):
        raise AssertionError("negative control failed: coordinate probe looked gauge invariant")

    q_x: Matrix = (
        (Fraction(1, 2), Fraction(1, 4)),
        (Fraction(1, 4), Fraction(1, 3)),
    )
    linear_shift = matmul(transpose(ell_x), h_mean)[0][0]
    quadratic_shift = Fraction(1, 2) * quadratic_form(q_x, h_mean)
    fluctuation_bias = Fraction(1, 2) * trace(matmul(q_x, metric_covariance))
    mean_shift = linear_shift + quadratic_shift + fluctuation_bias
    assert_equal("observable linear shift", linear_shift, Fraction(5, 6))
    assert_equal("observable quadratic mean shift", quadratic_shift, Fraction(5, 108))
    assert_equal("observable fluctuation bias", fluctuation_bias, Fraction(1, 45))
    assert_equal("observable retained mean shift", mean_shift, Fraction(487, 540))

    deterministic_only_shift = linear_shift + quadratic_shift
    if deterministic_only_shift == mean_shift:
        raise AssertionError("negative control failed: fluctuation bias was invisible")
    if mean_shift - deterministic_only_shift != fluctuation_bias:
        raise AssertionError("observable fluctuation bias should be exactly the missing term")

    q_norm_bound = Fraction(1)
    omitted_metric_covariance_trace = Fraction(1, 100)
    chart_remainder = Fraction(1, 100)
    observable_higher_tail = Fraction(1, 200)

    chart_radius = Fraction(2)
    certified_mean_norm_bound = Fraction(1, 2)
    if squared_norm(h_mean) >= certified_mean_norm_bound * certified_mean_norm_bound:
        raise AssertionError("test mean metric should fit inside the certified chart margin")
    chart_margin = chart_radius - certified_mean_norm_bound
    chart_exit_probability_bound = trace(metric_covariance) / (chart_margin * chart_margin)
    assert_equal("observable Gaussian chart-exit Markov bound", chart_exit_probability_bound, Fraction(1, 27))

    observable_sup_bound = Fraction(27, 200)
    stopped_exit_bound = 2 * observable_sup_bound * chart_exit_probability_bound
    assert_equal("observable stopped-process exit contribution", stopped_exit_bound, Fraction(1, 100))

    residual_mean_bound = (
        chart_remainder
        + Fraction(1, 2) * q_norm_bound * omitted_metric_covariance_trace
        + observable_higher_tail
        + stopped_exit_bound
    )
    assert_equal("observable residual mean bound", residual_mean_bound, Fraction(3, 100))
    wrong_residual_mean_bound = chart_remainder + observable_higher_tail
    if residual_mean_bound - wrong_residual_mean_bound != Fraction(3, 200):
        raise AssertionError("covariance and chart-exit residuals should enter the mean bound")
    if wrong_residual_mean_bound >= residual_mean_bound:
        raise AssertionError("negative control failed: covariance/chart-exit residual was not needed")

    small_metric_variance = Fraction(1, 100)
    fast_out_of_chart_growth = Fraction(100)
    if 2 * fast_out_of_chart_growth * small_metric_variance < 1:
        raise AssertionError("negative control setup should have divergent Gaussian square-exponential moment")
    gentle_out_of_chart_growth = Fraction(10)
    if 2 * gentle_out_of_chart_growth * small_metric_variance >= 1:
        raise AssertionError("test integrable out-of-chart growth should pass the Gaussian moment gate")

    variance_x = quadratic_form(metric_covariance, ell_x)
    assert_equal("observable variance from metric covariance", variance_x, Fraction(3, 10))
    variance_quad_residual = Fraction(1, 100)
    variance_tail_residual = Fraction(1, 100)
    variance_exit_residual = Fraction(1, 50)
    variance_budget = variance_x + variance_quad_residual + variance_tail_residual + variance_exit_residual
    assert_equal("observable variance budget", variance_budget, Fraction(17, 50))
    if mean_shift * mean_shift <= variance_budget:
        raise AssertionError("test observable should be signal-dominated after noise is included")

    noise_dominated_valid_budget = mean_shift * mean_shift + Fraction(1, 5)
    law_has_exit_control = chart_exit_probability_bound < 1 and stopped_exit_bound > 0
    if not law_has_exit_control:
        raise AssertionError("observable law should have chart-exit control")
    if mean_shift * mean_shift >= noise_dominated_valid_budget:
        raise AssertionError("negative control setup should be noise dominated")

    partial_metric_covariance: Matrix = (
        (Fraction(1, 50), Fraction(0)),
        (Fraction(0), Fraction(1, 100)),
    )
    partial_variance = quadratic_form(partial_metric_covariance, ell_x)
    if partial_variance >= variance_x:
        raise AssertionError("negative control setup should undercount observable variance")
    if mean_shift * mean_shift <= partial_variance:
        raise AssertionError("test partial covariance should look falsely precise")
    if variance_x <= partial_variance:
        raise AssertionError("negative control failed: missing covariance was not needed")

    ell_y: Matrix = ((Fraction(1),), (Fraction(-1),))
    covariance_xy = matmul(matmul(transpose(ell_x), metric_covariance), ell_y)[0][0]
    covariance_yx = matmul(matmul(transpose(ell_y), metric_covariance), ell_x)[0][0]
    assert_equal("observable covariance symmetry", covariance_xy, covariance_yx)
    assert_equal("observable cross covariance", covariance_xy, Fraction(1, 20))


def check_semiclassical_observable_chain_boundary() -> None:
    stages = (
        "qft_state_stress",
        "gravity_coordinates",
        "state_transport",
        "source_noise_response",
        "mean_metric_covariance",
        "metric_observable",
    )
    required_stages = frozenset(stages)
    required_side_data = frozenset(
        {
            "renormalization_scheme",
            "response_window",
            "gauge_constraint_reduction",
            "chart_exit_tail_control",
        }
    )
    ordering_edges = (
        ("qft_state_stress", "source_noise_response"),
        ("gravity_coordinates", "source_noise_response"),
        ("state_transport", "source_noise_response"),
        ("source_noise_response", "mean_metric_covariance"),
        ("mean_metric_covariance", "metric_observable"),
    )

    def valid_prediction_passes(chain: tuple[str, ...], side_data: frozenset[str]) -> bool:
        position = {stage: index for index, stage in enumerate(chain)}
        if not required_stages.issubset(position):
            return False
        if not required_side_data.issubset(side_data):
            return False
        return all(position[left] < position[right] for left, right in ordering_edges)

    def self_averaging_passes(chain: tuple[str, ...], side_data: frozenset[str]) -> bool:
        return valid_prediction_passes(chain, side_data) and "signal_to_noise" in side_data

    full_side_data = required_side_data | frozenset({"finite_residual_budgets", "signal_to_noise"})
    valid_side_data_without_snr = full_side_data - frozenset({"signal_to_noise"})
    if not valid_prediction_passes(stages, valid_side_data_without_snr):
        raise AssertionError("complete observable chain should pass")
    if not self_averaging_passes(stages, full_side_data):
        raise AssertionError("signal-to-noise data should support self-averaging claim")
    assert_equal("observable-chain terminal stage", stages[-1], "metric_observable")
    assert_equal("observable-chain stage count", len(stages), 6)

    formal_equation_only = ("qft_state_stress", "gravity_coordinates")
    if valid_prediction_passes(formal_equation_only, full_side_data):
        raise AssertionError("negative control failed: formal equation became prediction")

    mean_only_chain = stages[:-1]
    if valid_prediction_passes(mean_only_chain, full_side_data):
        raise AssertionError("negative control failed: mean metric lacked observable output")

    noise_without_metric_chain = (
        "qft_state_stress",
        "gravity_coordinates",
        "state_transport",
        "source_noise_response",
        "metric_observable",
    )
    if valid_prediction_passes(noise_without_metric_chain, full_side_data):
        raise AssertionError("negative control failed: noise skipped metric covariance")

    wrong_order_chain = (
        "metric_observable",
        "qft_state_stress",
        "gravity_coordinates",
        "state_transport",
        "source_noise_response",
        "mean_metric_covariance",
    )
    if valid_prediction_passes(wrong_order_chain, full_side_data):
        raise AssertionError("negative control failed: wrong-order observable chain passed")

    missing_exit_tail_control = full_side_data - frozenset({"chart_exit_tail_control"})
    if valid_prediction_passes(stages, missing_exit_tail_control):
        raise AssertionError("negative control failed: observable omitted chart-exit/tail control")

    missing_signal_to_noise = full_side_data - frozenset({"signal_to_noise"})
    if not valid_prediction_passes(stages, missing_signal_to_noise):
        raise AssertionError("negative control failed: missing signal-to-noise invalidated the probability law")
    if self_averaging_passes(stages, missing_signal_to_noise):
        raise AssertionError("negative control failed: missing signal-to-noise still claimed self-averaging")


def check_reduction_of_order_toy_model() -> None:
    # Toy equation: x'' + omega0^2 x + epsilon x'''' = 0.
    # For x ~ exp(lambda t), epsilon lambda^4 + lambda^2 + omega0^2 = 0.
    omega0 = 1.3
    eps = 1.0e-4
    # Low-energy perturbative root has lambda^2 = -omega0^2 - eps omega0^4 + O(eps^2).
    reduced_lambda_sq = -(omega0**2) - eps * omega0**4

    # Exact roots for z=lambda^2 solve eps z^2 + z + omega0^2=0.
    discriminant = 1 - 4 * eps * omega0**2
    z_low = (-1 + math.sqrt(discriminant)) / (2 * eps)
    z_high = (-1 - math.sqrt(discriminant)) / (2 * eps)
    assert_close(z_low, reduced_lambda_sq, "low-energy reduced root", tol=1e-3)
    _assert_gt("discarded higher-derivative root cutoff scale", abs(z_high), 0.1 / eps)

    lambda_low = cmath.sqrt(z_low)
    assert_close(lambda_low.real, 0.0, "low-energy root real part", tol=1e-9)


def main() -> None:
    check_curvature_squared_traces()
    check_kms_fluctuation_dissipation()
    check_noise_covariance_positivity()
    check_einstein_langevin_pushforward_covariance()
    check_large_species_semiclassical_scaling()
    check_finite_response_window_bounds()
    check_finite_scheme_transport_consistency()
    check_lambda_phi4_potential_source_coordinate()
    check_lambda_phi4_potential_noise_kernel()
    check_retained_interacting_source_ward_diagnostics()
    check_flrw_interacting_source_noise_closure()
    check_retained_ward_completion_laboratory()
    check_interacting_stress_tensor_noise_package()
    check_interacting_influence_functional_consistency()
    check_backreaction_small_gain_stability()
    check_nonlinear_backreaction_fixed_point_chart()
    check_retained_metric_observable_output()
    check_semiclassical_observable_chain_boundary()
    check_reduction_of_order_toy_model()
    print("All semiclassical backreaction checks passed.")


if __name__ == "__main__":
    main()
