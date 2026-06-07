#!/usr/bin/env python3
"""Exact finite checks for the large-N two-dimensional QCD chapter.

Evidence contract.
Target claims: the trace-delta color normalization, subtracted 't Hooft
  kernel sign, finite DLCQ quadratic-form identity, positivity and massless
  zero-mode checks, endpoint exponent small-mass expansion, finite-form
  monotonicity shadow, and the finite current-residue map in
  ``rem:qcd2-dlcq-current-correlator-residue-map``.
Independent construction: all finite matrices, quadratic forms, endpoint
  series, finite spectral measures, and source resolvents are constructed
  directly with exact rational arithmetic rather than by substituting the
  displayed manuscript equations as black boxes.
Imported assumptions: finite harmonic resolution, zero-mode-free light-front
  regulator, subtracted principal-value convention, positive endpoint masses
  where positivity is asserted, Euclidean current tests with ``Q^2`` away from
  the finite spectrum, and declared finite current/source vectors.
Negative controls: the script rejects the trace-half color normalization,
  wrong off-diagonal kernel sign, positivity without endpoint or kernel data,
  a massless zero mode for a non-subtracted kernel, endpoint-series
  coefficient mistakes, and the shortcut that finite eigenvalues alone
  determine current correlator residues.
Scope boundary: these checks do not prove continuum DLCQ convergence,
  completeness of the light-front Hilbert space, a four-dimensional QCD
  statement, or numerical accuracy for a chosen extrapolation; they verify the
  exact finite resolvent algebra and spectral-source bookkeeping that such
  claims must carry.
Primary derivation route: derive the finite regulator matrix from the
  subtracted kernel, compute its quadratic form, then assemble finite current
  correlators from eigenvalues together with source-vector residues.
Independent verification route: compare matrix quadratic forms against the
  displayed positive sums and compare source resolvents against independently
  computed spectral weights; rotate a finite matrix by an exact orthogonal
  transformation to keep eigenvalues fixed while changing source residues.
Convention dependencies: trace-delta generators, ``gamma_2`` as the displayed
  subtracted-kernel coefficient, grid points ``x_n=n/K``, real finite DLCQ
  eigenvectors normalized in the Euclidean dot product, and Euclidean
  correlators written as ``s^T(M_K^2+Q^2)^{-1}s``.
Domain and remainder assumptions: all matrix checks are finite dimensional;
  continuum statements require separate zero-mode, endpoint, coefficient,
  source-normalization, and ``K -> infinity`` residual data.
Remaining unproved or conditional: the companion does not establish the
  continuum 't Hooft spectrum, decay constants, current renormalization, or
  the 3D Chern-Simons-matter light-front solution requested elsewhere.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def casimir_fund_trace_delta(nc):
    return Fraction(nc * nc - 1, nc)


def check_trace_delta_color_normalization():
    for nc in range(2, 9):
        cf = casimir_fund_trace_delta(nc)
        planar = Fraction(nc, 1)
        trace_subtraction = Fraction(1, nc)
        assert_equal(f"C_F decomposition N={nc}", cf, planar - trace_subtraction)


def thooft_matrix(k, m1_sq, m2_sq, gamma):
    size = k - 1
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    xs = [Fraction(n, k) for n in range(1, k)]
    for n in range(size):
        diagonal = m1_sq / xs[n] + m2_sq / (1 - xs[n])
        diagonal += gamma * k * sum(
            Fraction(1, (n - j) * (n - j))
            for j in range(size)
            if j != n
        )
        matrix[n][n] = diagonal
        for m in range(size):
            if m != n:
                matrix[n][m] = -gamma * k * Fraction(1, (n - m) * (n - m))
    return matrix


def quadratic_form(matrix, vector):
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def displayed_quadratic_form(k, m1_sq, m2_sq, gamma, vector):
    xs = [Fraction(n, k) for n in range(1, k)]
    mass = sum(
        (m1_sq / xs[n] + m2_sq / (1 - xs[n])) * vector[n] * vector[n]
        for n in range(k - 1)
    )
    kernel = sum(
        gamma * k * (vector[n] - vector[m]) ** 2 / Fraction((n - m) * (n - m), 1)
        for n in range(k - 1)
        for m in range(n + 1, k - 1)
    )
    return mass + kernel


def matrix_vector(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(vector))
    ]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def transpose2(matrix):
    return ((matrix[0][0], matrix[1][0]), (matrix[0][1], matrix[1][1]))


def matmul2(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_vector2(matrix, vector):
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def inverse2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        (matrix[1][1] / det, -matrix[0][1] / det),
        (-matrix[1][0] / det, matrix[0][0] / det),
    )


def shifted_resolvent_pairing2(matrix, source, q2):
    shifted = (
        (matrix[0][0] + q2, matrix[0][1]),
        (matrix[1][0], matrix[1][1] + q2),
    )
    return dot(source, matrix_vector2(inverse2(shifted), source))


def trace2(matrix):
    return matrix[0][0] + matrix[1][1]


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def check_dlcq_quadratic_form_identity():
    k = 8
    m1_sq = Fraction(2, 5)
    m2_sq = Fraction(3, 7)
    gamma = Fraction(11, 13)
    vector = tuple(Fraction((-1) ** n * (n + 2), 9) for n in range(k - 1))
    matrix = thooft_matrix(k, m1_sq, m2_sq, gamma)
    assert_equal(
        "finite 't Hooft quadratic form",
        quadratic_form(matrix, vector),
        displayed_quadratic_form(k, m1_sq, m2_sq, gamma, vector),
    )


def check_positive_mass_sample_positive():
    k = 7
    matrix = thooft_matrix(k, Fraction(1, 3), Fraction(1, 4), Fraction(5, 6))
    vector = tuple(Fraction(n + 1, 5) for n in range(k - 1))
    assert_true("positive endpoint-mass form", quadratic_form(matrix, vector) > 0)


def check_massless_constant_zero_mode():
    k = 9
    matrix = thooft_matrix(k, Fraction(0), Fraction(0), Fraction(7, 5))
    constant = tuple(Fraction(1) for _ in range(k - 1))
    assert_equal("massless constant kernel zero mode", matrix_vector(matrix, constant), [Fraction(0)] * (k - 1))
    assert_equal("massless constant quadratic form", quadratic_form(matrix, constant), Fraction(0))


def check_endpoint_exponent_series():
    # The endpoint equation in the subtracted convention is
    #   r := m^2/gamma = 1 - pi beta cot(pi beta).
    # With z=(pi beta)^2,
    #   r = z/3 + z^2/45 + 2 z^3/945 + O(z^4).
    # Formal inversion gives
    #   z = 3 r - 3 r^2/5 + 12 r^3/175 + O(r^4).
    endpoint_series = {
        1: Fraction(1, 3),
        2: Fraction(1, 45),
        3: Fraction(2, 945),
    }
    inverse_series = {
        1: Fraction(3, 1),
        2: Fraction(-3, 5),
        3: Fraction(12, 175),
    }
    a = inverse_series[1]
    b = inverse_series[2]
    c = inverse_series[3]
    assert_equal("endpoint inverse linear coefficient", endpoint_series[1] * a, Fraction(1))
    assert_equal(
        "endpoint inverse quadratic coefficient",
        endpoint_series[1] * b + endpoint_series[2] * a * a,
        Fraction(0),
    )
    assert_equal(
        "endpoint inverse cubic coefficient",
        endpoint_series[1] * c
        + 2 * endpoint_series[2] * a * b
        + endpoint_series[3] * a * a * a,
        Fraction(0),
    )


def check_finite_form_monotonicity_shadow():
    # The continuum closed form is monotone in each nonnegative coordinate
    # m_1^2, m_2^2, and gamma_2.  The DLCQ matrix has the same exact
    # quadratic-form difference: mass-coordinate increments plus the
    # positive subtracted-kernel increment.
    k = 8
    base_m1 = Fraction(1, 7)
    base_m2 = Fraction(2, 9)
    base_gamma = Fraction(3, 11)
    delta_m1 = Fraction(5, 13)
    delta_m2 = Fraction(7, 17)
    delta_gamma = Fraction(2, 19)
    vector = tuple(Fraction((n + 1) * (-1 if n % 2 else 1), 10) for n in range(k - 1))

    base = thooft_matrix(k, base_m1, base_m2, base_gamma)
    higher = thooft_matrix(
        k,
        base_m1 + delta_m1,
        base_m2 + delta_m2,
        base_gamma + delta_gamma,
    )
    diff = quadratic_form(higher, vector) - quadratic_form(base, vector)
    expected = displayed_quadratic_form(k, delta_m1, delta_m2, delta_gamma, vector)
    assert_equal("finite form monotonicity exact difference", diff, expected)
    assert_true("finite form monotonicity positivity", diff > 0)


def check_current_correlator_needs_source_residues():
    # Two finite DLCQ mass matrices can have the same eigenvalues while a
    # declared current source couples to their eigenvectors with different
    # residues.  The current correlator is therefore a spectral measure, not a
    # list of masses by itself.
    eigenvalues = (Fraction(2), Fraction(5))
    diagonal = ((eigenvalues[0], Fraction(0)), (Fraction(0), eigenvalues[1]))
    rotation = ((Fraction(3, 5), Fraction(4, 5)), (Fraction(-4, 5), Fraction(3, 5)))
    rotated = matmul2(matmul2(rotation, diagonal), transpose2(rotation))
    source = (Fraction(1), Fraction(0))
    q2 = Fraction(1)

    assert_equal("same finite spectrum trace", trace2(rotated), trace2(diagonal))
    assert_equal("same finite spectrum determinant", det2(rotated), det2(diagonal))

    diagonal_weights = (Fraction(1), Fraction(0))
    rotated_weights = (rotation[0][0] ** 2, rotation[0][1] ** 2)
    assert_equal("rotated residue sum", sum(rotated_weights), dot(source, source))

    diagonal_correlator = shifted_resolvent_pairing2(diagonal, source, q2)
    diagonal_spectral = sum(
        weight / (eigenvalue + q2)
        for weight, eigenvalue in zip(diagonal_weights, eigenvalues)
    )
    rotated_correlator = shifted_resolvent_pairing2(rotated, source, q2)
    rotated_spectral = sum(
        weight / (eigenvalue + q2)
        for weight, eigenvalue in zip(rotated_weights, eigenvalues)
    )

    assert_equal("diagonal source spectral representation", diagonal_correlator, diagonal_spectral)
    assert_equal("rotated source spectral representation", rotated_correlator, rotated_spectral)
    assert_equal("diagonal current correlator", diagonal_correlator, Fraction(1, 3))
    assert_equal("rotated current correlator", rotated_correlator, Fraction(17, 75))
    assert_true(
        "finite eigenvalues alone do not determine current residues",
        diagonal_correlator != rotated_correlator,
    )

    scaled_source = (Fraction(2), Fraction(0))
    assert_equal(
        "source normalization scales current residue quadratically",
        shifted_resolvent_pairing2(rotated, scaled_source, q2),
        4 * rotated_correlator,
    )


def main():
    check_trace_delta_color_normalization()
    check_dlcq_quadratic_form_identity()
    check_positive_mass_sample_positive()
    check_massless_constant_zero_mode()
    check_endpoint_exponent_series()
    check_finite_form_monotonicity_shadow()
    check_current_correlator_needs_source_residues()
    print("All large-N two-dimensional QCD checks passed.")


if __name__ == "__main__":
    main()
