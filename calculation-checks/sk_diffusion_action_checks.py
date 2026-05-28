#!/usr/bin/env python3
"""Finite algebra checks for the Schwinger-Keldysh diffusion action."""

from __future__ import annotations

Vector2 = tuple[complex, complex]
Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
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


def mattranspose(matrix: Matrix2) -> Matrix2:
    return ((matrix[0][0], matrix[1][0]), (matrix[0][1], matrix[1][1]))


def matvec(matrix: Matrix2, vector: Vector2) -> Vector2:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def matscale(scalar: complex | float, matrix: Matrix2) -> Matrix2:
    return (
        (scalar * matrix[0][0], scalar * matrix[0][1]),
        (scalar * matrix[1][0], scalar * matrix[1][1]),
    )


def matadd(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matdet(matrix: Matrix2) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matinv(matrix: Matrix2) -> Matrix2:
    determinant = matdet(matrix)
    if abs(determinant) < 1.0e-14:
        raise AssertionError("matrix inversion encountered a nearly singular matrix")
    return (
        (matrix[1][1] / determinant, -matrix[0][1] / determinant),
        (-matrix[1][0] / determinant, matrix[0][0] / determinant),
    )


def assert_vector_close(name: str, got: Vector2, expected: Vector2, tol: float = 1.0e-10) -> None:
    assert_close(f"{name}[0]", got[0], expected[0], tol)
    assert_close(f"{name}[1]", got[1], expected[1], tol)


def assert_matrix_close(name: str, got: Matrix2, expected: Matrix2, tol: float = 1.0e-10) -> None:
    for row in range(2):
        for column in range(2):
            assert_close(f"{name}[{row},{column}]", got[row][column], expected[row][column], tol)


def check_density_response_kernel() -> None:
    chi = 1.7
    sigma = 0.51
    diffusion = sigma / chi
    omega = 0.23
    k = 0.19
    source = 0.8

    # Saddle equation from the a-phase:
    # chi (A0 - i omega phi) + sigma k^2 phi = 0.
    phi = -chi * source / (sigma * k * k - 1j * chi * omega)
    density = chi * (source - 1j * omega * phi)
    kernel = density / source
    expected = chi * diffusion * k * k / (diffusion * k * k - 1j * omega)

    assert_close("density response kernel", kernel, expected)
    assert_close("static source response", chi * diffusion * k * k / (diffusion * k * k), chi)
    assert_close("conserved total charge response", chi * diffusion * 0.0 / (diffusion * 0.0 - 1j * omega), 0.0)

    current_divergence = -1j * sigma * omega * k * k * phi
    assert_close("continuity equation", -1j * omega * density + current_divergence, 0.0)


def check_multicharge_density_response_kernel() -> None:
    chi: Matrix2 = ((2.0, 0.35), (0.35, 1.3))
    sigma: Matrix2 = ((0.76, 0.18), (0.18, 0.49))
    chi_inverse = matinv(chi)
    diffusion = matmul(sigma, chi_inverse)
    identity: Matrix2 = ((1.0, 0.0), (0.0, 1.0))
    omega = 0.37
    k = 0.23
    k2 = k * k
    source: Vector2 = (0.9, -0.4)

    # Phase saddle:
    # (k^2 Sigma - i omega chi) phi = - chi A0.
    saddle_matrix = matadd(matscale(k2, sigma), matscale(-1j * omega, chi))
    phi = matvec(matinv(saddle_matrix), matvec(matscale(-1.0, chi), source))
    density = matvec(chi, (source[0] - 1j * omega * phi[0], source[1] - 1j * omega * phi[1]))

    # Response written in density variables:
    # K = (D k^2 - i omega 1)^(-1) k^2 Sigma.
    kernel = matmul(
        matinv(matadd(matscale(k2, diffusion), matscale(-1j * omega, identity))),
        matscale(k2, sigma),
    )
    expected_density = matvec(kernel, source)
    assert_vector_close("multi-charge density response", density, expected_density)

    current_divergence = matvec(matscale(-1j * omega * k2, sigma), phi)
    assert_vector_close(
        "multi-charge continuity equation",
        (-1j * omega * density[0] + current_divergence[0], -1j * omega * density[1] + current_divergence[1]),
        (0.0, 0.0),
    )

    static_kernel = matmul(matinv(matscale(k2, diffusion)), matscale(k2, sigma))
    zero_momentum_kernel = matmul(
        matinv(matadd(matscale(0.0, diffusion), matscale(-1j * omega, identity))),
        matscale(0.0, sigma),
    )
    assert_matrix_close("multi-charge static kernel", static_kernel, chi)
    assert_matrix_close("multi-charge total-charge response", zero_momentum_kernel, ((0.0, 0.0), (0.0, 0.0)))


def check_multicharge_diffusion_stability() -> None:
    chi: Matrix2 = ((2.0, 0.35), (0.35, 1.3))
    sigma: Matrix2 = ((0.76, 0.18), (0.18, 0.49))
    chi_inverse = matinv(chi)
    diffusion = matmul(sigma, chi_inverse)

    # D is self-adjoint in the chi^{-1} density inner product:
    # chi^{-1} D = chi^{-1} Sigma chi^{-1} is symmetric.
    metric_diffusion = matmul(chi_inverse, diffusion)
    assert_close("chi-inverse diffusion symmetry", metric_diffusion[0][1], metric_diffusion[1][0])

    trace = diffusion[0][0] + diffusion[1][1]
    determinant = matdet(diffusion)
    discriminant = trace * trace - 4.0 * determinant
    if discriminant < -1.0e-12:
        raise AssertionError(f"diffusion eigenvalues are not real: discriminant {discriminant!r}")
    root = discriminant**0.5
    eigenvalues = ((trace + root) / 2.0, (trace - root) / 2.0)
    for index, eigenvalue in enumerate(eigenvalues):
        if eigenvalue < -1.0e-12:
            raise AssertionError(f"diffusion eigenvalue {index} is negative: {eigenvalue!r}")
        assert_close(
            f"diffusion characteristic equation {index}",
            eigenvalue * eigenvalue - trace * eigenvalue + determinant,
            0.0,
        )

        k = 0.41
        pole_frequency = -1j * eigenvalue * k * k
        pole_matrix = matadd(
            matscale(k * k, diffusion),
            matscale(-1j * pole_frequency, ((1.0, 0.0), (0.0, 1.0))),
        )
        assert_close(f"diffusion pole determinant {index}", matdet(pole_matrix), 0.0)


def check_transverse_ohm_response() -> None:
    sigma = 0.73
    omega = 0.41
    vector_source = 1.2

    # For a transverse source with A0=0 and k_i A_i=0:
    # j_i = -sigma partial_t A_i = i omega sigma A_i.
    current = 1j * omega * sigma * vector_source
    electric_field = 1j * omega * vector_source
    assert_close("transverse Ohm response", current, sigma * electric_field)


def check_classical_kms_noise_coefficient() -> None:
    beta = 2.3
    sigma = 0.61
    c = sigma / beta

    # Transform L = -sigma a x + i c a^2 under x -> -x,
    # a -> a + i beta x. Equality with L requires c beta = sigma.
    a_coeff_after = sigma - 2.0 * c * beta
    a_coeff_before = -sigma
    x2_coeff_after = 1j * sigma * beta - 1j * c * beta * beta
    assert_close("KMS ax coefficient", a_coeff_after, a_coeff_before)
    assert_close("KMS x^2 cancellation", x2_coeff_after, 0.0)


def check_multicharge_classical_kms_noise_matrix() -> None:
    beta = 1.9
    sigma: Matrix2 = ((0.74, 0.16), (0.16, 0.52))
    noise_matrix = matscale(1.0 / beta, sigma)
    a: Vector2 = (0.31, -0.27)
    x: Vector2 = (0.42, 0.19)

    def bilinear(left: Vector2, matrix: Matrix2, right: Vector2) -> complex:
        return left[0] * (matrix[0][0] * right[0] + matrix[0][1] * right[1]) + left[1] * (
            matrix[1][0] * right[0] + matrix[1][1] * right[1]
        )

    original = -bilinear(a, sigma, x) + 1j * bilinear(a, noise_matrix, a)
    shifted_a = (a[0] + 1j * beta * x[0], a[1] + 1j * beta * x[1])
    reversed_x = (-x[0], -x[1])
    transformed = -bilinear(shifted_a, sigma, reversed_x) + 1j * bilinear(shifted_a, noise_matrix, shifted_a)
    assert_close("multi-charge KMS transformed Lagrangian", transformed, original)


def check_noise_normalization() -> None:
    temperature = 1.4
    sigma = 0.32
    variance = 2.0 * temperature * sigma
    inverse_gaussian_denominator = 4.0 * temperature * sigma
    assert_close("noise variance", variance, 2.0 * temperature * sigma)
    assert_close("Hubbard-Stratonovich denominator", inverse_gaussian_denominator, 2.0 * variance)


def check_density_fdt_matrix_identity() -> None:
    temperature = 1.35
    omega = 0.47
    k = 0.29
    k2 = k * k
    chi: Matrix2 = ((2.4, 0.41), (0.41, 1.1))
    sigma: Matrix2 = ((0.83, 0.27), (0.27, 0.58))
    identity: Matrix2 = ((1.0, 0.0), (0.0, 1.0))
    diffusion = matmul(sigma, matinv(chi))

    # Use a noncommuting chi/Sigma pair, so the check is genuinely matrix-valued.
    commutator = matadd(matmul(diffusion, sigma), matscale(-1.0, matmul(sigma, diffusion)))
    if abs(commutator[0][1]) < 1.0e-12 and abs(commutator[1][0]) < 1.0e-12:
        raise AssertionError("test matrices accidentally commute")

    resolvent = matinv(matadd(matscale(k2, diffusion), matscale(-1j * omega, identity)))
    advanced_resolvent = matinv(
        matadd(matscale(k2, mattranspose(diffusion)), matscale(1j * omega, identity))
    )
    retarded = matmul(resolvent, matscale(k2, sigma))
    advanced = matmul(matscale(k2, sigma), advanced_resolvent)
    symmetrized = matscale(
        2.0 * temperature * k2,
        matmul(matmul(resolvent, sigma), advanced_resolvent),
    )
    spectral = matscale(1.0 / (2j), matadd(retarded, matscale(-1.0, advanced)))
    assert_matrix_close(
        "matrix density FDT",
        symmetrized,
        matscale(2.0 * temperature / omega, spectral),
    )

    for vector in [(0.3 + 0.2j, -0.7 + 0.1j), (1.1 - 0.4j, 0.6 + 0.9j)]:
        gv = matvec(symmetrized, vector)
        quadratic = vector[0].conjugate() * gv[0] + vector[1].conjugate() * gv[1]
        if quadratic.real < -1.0e-10 or abs(quadratic.imag) > 1.0e-10:
            raise AssertionError(f"density noise kernel should be Hermitian positive: {quadratic!r}")


def main() -> None:
    check_density_response_kernel()
    check_multicharge_density_response_kernel()
    check_multicharge_diffusion_stability()
    check_transverse_ohm_response()
    check_classical_kms_noise_coefficient()
    check_multicharge_classical_kms_noise_matrix()
    check_noise_normalization()
    check_density_fdt_matrix_identity()
    print("All Schwinger-Keldysh diffusion-action checks passed.")


if __name__ == "__main__":
    main()
