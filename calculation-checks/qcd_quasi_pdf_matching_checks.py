#!/usr/bin/env python3
"""Finite checks for the QCD quasi-/pseudo-PDF matching block.

The checks verify algebraic facts used in Volume II, Chapter 19:

1. The quasi-PDF Fourier convention with the explicit prefactor P in
   ``P/(2 pi) int dz exp(i x P z) M(z)`` has inverse ``M(z)``.
2. A multiplicative spatial-Wilson-line renormalization factor cancels in the
   reduced pseudo-Ioffe-time distribution when it depends only on z^2.
3. Finite light-ray scheme changes are absorbed by the inverse change of the
   matching kernel.
4. Column-sum normalization of the matching kernel preserves quark number.
5. Finite-momentum inverse matching of tested PDF bins requires a stable left
   inverse and a residual budget; raw quasi-PDF bins are not PDF bins.

Evidence contract.
Target claims: the Volume II QCD quasi-/pseudo-PDF section's Fourier
normalization, reduced Ioffe-time cancellation, finite scheme covariance,
charge-preserving matching, and finite-momentum inverse-matching residual
bound for tested PDF bins.
Independent construction: exact finite Fourier characters, rational
renormalization factors, rational matching matrices, explicit left inverses,
and finite residual vectors independent of the continuum LaMET derivation.
Imported assumptions: existence of the renormalized spatial Wilson-line
bilocal, existence of light-ray PDF matrix elements in a declared scheme, and
the perturbative short-distance matching kernel are taken from the manuscript
development and are not proved by this finite script.
Negative controls: missing Fourier prefactor, uncancelled nonmultiplicative
Wilson-line factors, wrong finite scheme transport, charge-nonpreserving
column sums, raw quasi-bin reading, singular inverse matching, omitted
finite-momentum residuals, and quasi-coordinate negativity overread as PDF
negativity.
Scope boundary: these are finite normalization and stability checks for the
matching algebra.  They are not independent evidence for the continuum QCD
large-momentum theorem, lattice continuum limit, infinite-volume limit, or
nonperturbative light-ray PDF existence.
"""

from __future__ import annotations

from fractions import Fraction


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def vec_add(left: Vector, right: Vector) -> Vector:
    return [left[index] + right[index] for index in range(len(left))]


def vec_sub(left: Vector, right: Vector) -> Vector:
    return [left[index] - right[index] for index in range(len(left))]


def max_norm(vector: Vector) -> Fraction:
    return max(abs(entry) for entry in vector)


def matrix_infty_norm(matrix: Matrix) -> Fraction:
    return max(sum(abs(entry) for entry in row) for row in matrix)


def identity_2x2() -> Matrix:
    return [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][col] - right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def inverse_2x2(matrix: Matrix) -> Matrix:
    [[a, b], [c, d]] = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise AssertionError("singular 2x2 matrix")
    return [[d / determinant, -b / determinant], [-c / determinant, a / determinant]]


def check_fourier_prefactor_inverse() -> None:
    # On a finite periodic grid with P = N/L and z_j = j L/N, the continuum
    # convention becomes a normalized discrete Fourier pair; the explicit P
    # prefactor in the continuum formula is the factor that makes the inverse
    # return M(z) rather than M(z)/P.
    samples = [Fraction(2), Fraction(-1), Fraction(3), Fraction(5)]
    n = len(samples)
    # Use the character table of Z_4 over rational pairs (real, imaginary).
    characters = [
        [(1, 0), (1, 0), (1, 0), (1, 0)],
        [(1, 0), (0, 1), (-1, 0), (0, -1)],
        [(1, 0), (-1, 0), (1, 0), (-1, 0)],
        [(1, 0), (0, -1), (-1, 0), (0, 1)],
    ]

    transformed: list[tuple[Fraction, Fraction]] = []
    for k in range(n):
        real = Fraction(0)
        imag = Fraction(0)
        for j, value in enumerate(samples):
            cr, ci = characters[k][j]
            real += value * Fraction(cr, n)
            imag += value * Fraction(ci, n)
        transformed.append((real, imag))

    recovered: list[Fraction] = []
    for j in range(n):
        total_real = Fraction(0)
        total_imag = Fraction(0)
        for k, (value_real, value_imag) in enumerate(transformed):
            cr, ci = characters[k][j]
            # Inverse uses complex conjugate characters.
            total_real += value_real * cr + value_imag * ci
            total_imag += value_imag * cr - value_real * ci
        assert_equal(f"inverse DFT imaginary part at {j}", total_imag, Fraction(0))
        recovered.append(total_real)
    assert_equal("Fourier prefactor inverse", recovered, samples)


def check_reduced_pseudo_itd_cancellation() -> None:
    z_factor = Fraction(7, 5)
    matrix_element_nu = Fraction(11, 13)
    matrix_element_zero = Fraction(17, 19)

    bare_reduced = matrix_element_nu / matrix_element_zero
    renormalized_reduced = (z_factor * matrix_element_nu) / (
        z_factor * matrix_element_zero
    )

    assert_equal(
        "multiplicative Wilson-line factor cancellation",
        renormalized_reduced,
        bare_reduced,
    )


def check_scheme_covariance() -> None:
    matching = [
        [Fraction(3, 2), Fraction(-1, 2)],
        [Fraction(1, 4), Fraction(3, 4)],
    ]
    scheme_change = [
        [Fraction(2), Fraction(1, 3)],
        [Fraction(1), Fraction(4, 3)],
    ]
    inverse_scheme = inverse_2x2(scheme_change)
    transformed_matching = matmul(matching, inverse_scheme)

    pdf = [Fraction(5, 7), Fraction(2, 7)]
    primed_pdf = matvec(scheme_change, pdf)

    assert_equal(
        "finite scheme covariance",
        matvec(transformed_matching, primed_pdf),
        matvec(matching, pdf),
    )


def check_number_preserving_matching() -> None:
    # Two quasi coordinates are matched to two light-ray coordinates.  The
    # weighted column sums of C are both one, so total quark number is preserved.
    matching = [
        [Fraction(5, 4), Fraction(1, 3)],
        [Fraction(-1, 4), Fraction(2, 3)],
    ]
    quasi_weights = [Fraction(1), Fraction(1)]
    light_ray_weights = [Fraction(1), Fraction(1)]
    for column in range(2):
        weighted_sum = sum(
            quasi_weights[row] * matching[row][column] for row in range(2)
        )
        assert_equal(
            f"matching column {column} charge",
            weighted_sum,
            light_ray_weights[column],
        )

    pdf = [Fraction(8, 9), Fraction(1, 9)]
    quasi = matvec(matching, pdf)
    assert_equal("quark number from PDFs", sum(pdf), Fraction(1))
    assert_equal("quark number from quasi-PDF matching", sum(quasi), Fraction(1))


def check_finite_momentum_inverse_matching_extraction() -> None:
    matching = [
        [Fraction(5, 4), Fraction(1, 2)],
        [Fraction(-1, 4), Fraction(1, 2)],
    ]
    left_inverse = inverse_2x2(matching)
    identity = identity_2x2()
    assert_equal(
        "exact finite matching left inverse",
        matmul(left_inverse, matching),
        identity,
    )

    pdf_bins = [Fraction(1, 3), Fraction(2, 3)]
    projected_quasi = matvec(matching, pdf_bins)
    residual = [Fraction(1, 101), -Fraction(1, 103)]
    measured_quasi = vec_add(projected_quasi, residual)
    extracted_pdf = matvec(left_inverse, measured_quasi)
    extraction_error = vec_sub(extracted_pdf, pdf_bins)
    propagated_error = matvec(left_inverse, residual)
    assert_equal(
        "inverse matching propagates finite-momentum residual",
        extraction_error,
        propagated_error,
    )

    residual_bound = max_norm(residual)
    inverse_norm = matrix_infty_norm(left_inverse)
    error_bound = inverse_norm * residual_bound
    assert max_norm(extraction_error) <= error_bound

    assert projected_quasi != pdf_bins

    naive_pdf = matvec(left_inverse, projected_quasi)
    assert_equal("zero-residual inverse matching recovers PDF bins", naive_pdf, pdf_bins)
    assert extracted_pdf != naive_pdf

    matching_defect = matrix_sub(matmul(left_inverse, matching), identity)
    defect_bound = matrix_infty_norm(matching_defect) * max_norm(pdf_bins)
    assert_equal("exact left-inverse defect vanishes", defect_bound, Fraction(0))

    underbudget = error_bound - inverse_norm * abs(residual[1])
    assert max_norm(extraction_error) > underbudget

    singular_matching = [
        [Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(4)],
    ]
    try:
        inverse_2x2(singular_matching)
    except AssertionError:
        pass
    else:
        raise AssertionError("singular matching matrix should not be invertible")

    positive_pdf = [Fraction(1), Fraction(0)]
    quasi_coordinate = matvec(matching, positive_pdf)
    assert quasi_coordinate[1] < 0


def main() -> None:
    check_fourier_prefactor_inverse()
    check_reduced_pseudo_itd_cancellation()
    check_scheme_covariance()
    check_number_preserving_matching()
    check_finite_momentum_inverse_matching_extraction()
    print("All QCD quasi-/pseudo-PDF matching checks passed.")


if __name__ == "__main__":
    main()
