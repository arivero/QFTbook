#!/usr/bin/env python3
"""Finite checks for the semiclassical backreaction chapter.

These checks verify algebraic identities that are easy to lose by a sign or
normalization: traces of the curvature-squared Euler tensors in four
dimensions, the KMS fluctuation-dissipation factor, positivity of the noise
covariance, finite response-window metric fluctuation bounds, the first-order
lambda-phi-four potential-insertion source coordinate, the retained
lambda-phi-four potential-noise coordinate using the full separated two-point
function, retained Ward diagnostics for interacting source/noise coordinates,
and the low-energy root selected by reduction of order in a toy
higher-derivative equation.

Evidence contract.
Target claims: the finite algebra and response-window subclaims in Volume
XII Chapter 11, including curvature-squared trace normalizations,
fluctuation-dissipation factors, noise-covariance positivity, retained
metric-response bounds, the lambda-phi-four potential-insertion source
coordinate, the retained potential-noise Wick contraction with full separated
two-point cross covariance and metric pushforward, the restricted
finite-renormalization ledger for that coordinate, the finite retained
Ward-diagnostic/projected-noise algebra for interacting sources, and the
low-energy root selected by reduction of order.
Independent construction: the checks recompute traces, KMS factors,
matrix pushforwards, exact retained-sector inverses, Wick-contraction
coefficients, cosmological-coordinate shifts, independent finite counterterm
controls, signed/absolute norm bounds, Ward maps, kernel projectors, projected
covariances, and toy roots directly from finite formulas rather than importing
chapter display strings.
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
noise, unprojected longitudinal noise, and cutoff-scale higher-derivative roots
are rejected.
Scope boundary: a pass checks coefficient, positivity, and response-bound
bookkeeping for the retained potential-insertion coordinate; it does not
construct the full interacting stress-tensor expectation, prove existence of
interacting Hadamard states, construct renormalized stress-tensor products,
solve stochastic semiclassical equations, or address nonperturbative quantum
gravity dynamics.
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


def trace(matrix: Matrix) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def squared_norm(column: Matrix) -> Fraction:
    return sum(column[i][0] * column[i][0] for i in range(len(column)))


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
    check_finite_response_window_bounds()
    check_lambda_phi4_potential_source_coordinate()
    check_lambda_phi4_potential_noise_kernel()
    check_retained_interacting_source_ward_diagnostics()
    check_reduction_of_order_toy_model()
    print("All semiclassical backreaction checks passed.")


if __name__ == "__main__":
    main()
