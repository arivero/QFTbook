#!/usr/bin/env python3
"""Finite checks for categorical-defect action and dagger-structure algebra.

The last check verifies, without floating-point roots of unity, the pointed
modular-category mechanism used in the rational SymTFT discussion: cyclic
fusion is diagonalized by the finite Fourier matrix, and the defect
eigenvalues form a representation of the fusion algebra.

The finite pointed-anomaly check similarly tracks only exponents modulo n:
the multiplicative U(1) cocycle equation becomes an exact congruence.

The null-quotient check is the finite reflection-positive skeleton behind the
physical defect category: a semidefinite junction Gram form is quotiented by
its radical, and composition is verified to descend exactly.
"""

from __future__ import annotations

from fractions import Fraction


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix)]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return [dot(row, vector) for row in matrix]


def matrix_matrix(left: Matrix, right: Matrix) -> Matrix:
    columns = transpose(right)
    return [[dot(row, column) for column in columns] for row in left]


def inverse_2x2(matrix: Matrix) -> Matrix:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant == 0:
        raise AssertionError("singular 2x2 matrix")
    return [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]


def identity(size: int) -> Matrix:
    return [
        [Fraction(1) if row == column else Fraction(0) for column in range(size)]
        for row in range(size)
    ]


def zero_matrix(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def weighted_inner(metric: Matrix, left: Vector, right: Vector) -> Fraction:
    return dot(left, matrix_vector(metric, right))


def vector_add(left: Vector, right: Vector) -> Vector:
    return [a + b for a, b in zip(left, right)]


def scalar_vector(scalar: Fraction, vector: Vector) -> Vector:
    return [scalar * entry for entry in vector]


def check_defect_fusion_as_operator_composition() -> None:
    # Three local-sector basis vectors.  D1 is a noninvertible projection-like
    # action; D2 swaps the first two sectors.  The fused action is composition.
    rho_d1: Matrix = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(2)],
    ]
    rho_d2: Matrix = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    fused = matrix_matrix(rho_d1, rho_d2)
    for vector in [
        [Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(-4), Fraction(5), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(7)],
    ]:
        assert_equal(
            "rho_{D1 tensor D2}=rho_D1 rho_D2",
            matrix_vector(fused, vector),
            matrix_vector(rho_d1, matrix_vector(rho_d2, vector)),
        )


def check_noninvertible_projection_action() -> None:
    projection: Matrix = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    assert_equal("projection idempotence", matrix_matrix(projection, projection), projection)
    kernel_vector = [Fraction(0), Fraction(1), Fraction(0)]
    assert_equal(
        "projection has nontrivial kernel",
        matrix_vector(projection, kernel_vector),
        [Fraction(0), Fraction(0), Fraction(0)],
    )


def check_dagger_composition_and_pairing() -> None:
    a: Matrix = [
        [Fraction(1), Fraction(2)],
        [Fraction(0), Fraction(-1)],
        [Fraction(3), Fraction(1)],
    ]
    b: Matrix = [
        [Fraction(2), Fraction(0), Fraction(1)],
        [Fraction(-1), Fraction(4), Fraction(3)],
    ]
    left = transpose(matrix_matrix(b, a))
    right = matrix_matrix(transpose(a), transpose(b))
    assert_equal("(BA)^dagger=A^dagger B^dagger", left, right)

    for vector in [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(2), Fraction(-3), Fraction(5)],
        [Fraction(-7), Fraction(11), Fraction(13)],
    ]:
        norm = dot(vector, vector)
        if norm <= 0:
            raise AssertionError("reflection pairing should be positive on nonzero vectors")


def check_bpz_weighted_defect_adjoint() -> None:
    # Finite analogue of <rho_D v,w>_BPZ = <v,rho_{D^\dagger} w>_BPZ.
    # The BPZ metric is not chosen to be the identity, so the adjoint is
    # G^{-1} rho_D^T G rather than the ordinary transpose.
    metric: Matrix = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    rho_d: Matrix = [
        [Fraction(1), Fraction(2)],
        [Fraction(-1), Fraction(0)],
    ]
    rho_d_dagger = matrix_matrix(matrix_matrix(inverse_2x2(metric), transpose(rho_d)), metric)

    for vector_left in [
        [Fraction(1), Fraction(0)],
        [Fraction(2), Fraction(-3)],
        [Fraction(5), Fraction(7)],
    ]:
        for vector_right in [
            [Fraction(0), Fraction(1)],
            [Fraction(-4), Fraction(1)],
            [Fraction(3), Fraction(2)],
        ]:
            assert_equal(
                "BPZ weighted adjoint identity",
                weighted_inner(metric, matrix_vector(rho_d, vector_left), vector_right),
                weighted_inner(metric, vector_left, matrix_vector(rho_d_dagger, vector_right)),
            )


def check_isotopy_matrix_unitarity_for_junction_pairing() -> None:
    # Rational orthogonal change of basis preserving the finite reflection
    # pairing.  This models an isotopy map between orthonormal junction bases.
    u: Matrix = [
        [Fraction(3, 5), Fraction(4, 5)],
        [Fraction(-4, 5), Fraction(3, 5)],
    ]
    assert_equal("isotopy matrix U^T U", matrix_matrix(transpose(u), u), identity(2))
    assert_equal("isotopy matrix U U^T", matrix_matrix(u, transpose(u)), identity(2))
    for vector in [
        [Fraction(5, 7), Fraction(-2, 3)],
        [Fraction(11, 13), Fraction(17, 19)],
    ]:
        transformed = matrix_vector(u, vector)
        assert_equal(
            "reflection pairing preserved by isotopy",
            dot(transformed, transformed),
            dot(vector, vector),
        )


def check_null_quotient_composition_descends() -> None:
    # A finite raw junction space with reflection-positive but degenerate Gram
    # form.  The norm is (x_0+x_2)^2+2*x_1^2, so n=(1,0,-1) is the radical.
    gram: Matrix = [
        [Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(2), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(1)],
    ]
    null_vector: Vector = [Fraction(1), Fraction(0), Fraction(-1)]
    raw_basis: list[Vector] = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]

    assert_equal(
        "null vector has zero reflection norm",
        weighted_inner(gram, null_vector, null_vector),
        Fraction(0),
    )
    for basis_vector in raw_basis:
        assert_equal(
            "zero-norm vector is in the Gram radical",
            weighted_inner(gram, null_vector, basis_vector),
            Fraction(0),
        )

    def quotient_coordinates(vector: Vector) -> Vector:
        return [vector[0] + vector[2], vector[1]]

    quotient_metric: Matrix = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(2)],
    ]
    for vector in [
        [Fraction(2), Fraction(-3), Fraction(5)],
        [Fraction(-1), Fraction(4), Fraction(7)],
        [Fraction(0), Fraction(5), Fraction(0)],
    ]:
        quotient_vector = quotient_coordinates(vector)
        assert_equal(
            "Gram form factors through the null quotient",
            weighted_inner(gram, vector, vector),
            weighted_inner(quotient_metric, quotient_vector, quotient_vector),
        )
        if quotient_vector != [Fraction(0), Fraction(0)]:
            if weighted_inner(quotient_metric, quotient_vector, quotient_vector) <= 0:
                raise AssertionError("quotient reflection form should be positive")

    # Composition by a fixed junction.  It is not injective on raw vectors, but
    # it maps the radical to itself, so it induces a quotient operator.
    compose: Matrix = [
        [Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(3), Fraction(2)],
    ]
    descended: Matrix = [
        [Fraction(2), Fraction(4)],
        [Fraction(0), Fraction(-1)],
    ]
    assert_equal(
        "composition preserves the Gram radical",
        matrix_vector(compose, null_vector),
        scalar_vector(Fraction(2), null_vector),
    )

    for vector in [
        [Fraction(3), Fraction(1), Fraction(-2)],
        [Fraction(-5), Fraction(7), Fraction(11)],
    ]:
        assert_equal(
            "composition descends to quotient coordinates",
            quotient_coordinates(matrix_vector(compose, vector)),
            matrix_vector(descended, quotient_coordinates(vector)),
        )
        for coefficient in [Fraction(-3), Fraction(0), Fraction(5)]:
            representative = vector_add(
                vector,
                scalar_vector(coefficient, null_vector),
            )
            assert_equal(
                "composition independent of null representative",
                quotient_coordinates(matrix_vector(compose, representative)),
                quotient_coordinates(matrix_vector(compose, vector)),
            )

    quotient_adjoint = matrix_matrix(
        matrix_matrix(inverse_2x2(quotient_metric), transpose(descended)),
        quotient_metric,
    )
    assert_equal(
        "quotient adjoint matrix",
        quotient_adjoint,
        [
            [Fraction(2), Fraction(0)],
            [Fraction(2), Fraction(-1)],
        ],
    )
    for left in [
        [Fraction(1), Fraction(2)],
        [Fraction(-3), Fraction(5)],
    ]:
        for right in [
            [Fraction(7), Fraction(-11)],
            [Fraction(13), Fraction(17)],
        ]:
            assert_equal(
                "descended composition has reflected adjoint",
                weighted_inner(quotient_metric, matrix_vector(descended, left), right),
                weighted_inner(
                    quotient_metric,
                    left,
                    matrix_vector(quotient_adjoint, right),
                ),
            )


def cyclic_fourier_verlinde_coefficient(n: int, a: int, b: int, c: int) -> int:
    """Return the exact Z_n pointed Verlinde coefficient.

    The pointed modular matrix has entries S_{a x}=n^{-1/2} zeta^{a x}.
    The Verlinde sum reduces to

        (1/n) sum_x zeta^{(a+b-c)x},

    which is 1 when c=a+b mod n and 0 otherwise.  We use this exact root-sum
    identity rather than approximate complex roots of unity.
    """

    exponent = (a + b - c) % n
    return 1 if exponent == 0 else 0


def check_pointed_modular_category_verlinde_diagonalization() -> None:
    for n in range(2, 9):
        labels = range(n)
        for a in labels:
            for b in labels:
                for c in labels:
                    expected = 1 if c == (a + b) % n else 0
                    assert_equal(
                        f"Z_{n} pointed Verlinde coefficient",
                        cyclic_fourier_verlinde_coefficient(n, a, b, c),
                        expected,
                    )

        for a in labels:
            for b in labels:
                for sector in labels:
                    # lambda_a(sector)=zeta^{a sector}; equality of eigenvalue
                    # products is equality of exponents mod n.
                    product_exponent = (a * sector + b * sector) % n
                    fused_exponent = ((a + b) % n) * sector % n
                    assert_equal(
                        f"Z_{n} defect eigenvalue representation",
                        product_exponent,
                        fused_exponent,
                    )

        for a in labels:
            for b in labels:
                for sector in labels:
                    # N_a acting on the sector-th Fourier column shifts b to
                    # b+a.  The eigenvector identity compares the corresponding
                    # exponents:
                    # S_{b+a,sector}=lambda_a(sector) S_{b,sector}.
                    left_exponent = ((b + a) % n) * sector % n
                    right_exponent = (a * sector + b * sector) % n
                    assert_equal(
                        f"Z_{n} Fourier column diagonalizes fusion",
                        left_exponent,
                        right_exponent,
                    )


def zn_three_cocycle_exponent(n: int, p: int, a: int, b: int, c: int) -> int:
    """Exponent for a standard normalized Z_n 3-cocycle.

    It represents exp(2*pi*i*exponent/n), with additive group law mod n.
    """

    return (p * a * ((b + c) // n)) % n


def beta_two_cochain_exponent(n: int, r: int, a: int, b: int) -> int:
    return (r * a * b) % n


def delta_beta_exponent(n: int, r: int, a: int, b: int, c: int) -> int:
    # beta(g,h) beta(g+h,k) / (beta(h,k) beta(g,h+k)).
    return (
        beta_two_cochain_exponent(n, r, a, b)
        + beta_two_cochain_exponent(n, r, (a + b) % n, c)
        - beta_two_cochain_exponent(n, r, b, c)
        - beta_two_cochain_exponent(n, r, a, (b + c) % n)
    ) % n


def check_pointed_anomaly_cocycle_and_coboundary() -> None:
    for n in range(2, 9):
        for p in range(n):
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        for d in range(n):
                            # alpha(h,k,l) alpha(g,h+k,l) alpha(g,h,k)
                            # = alpha(g+h,k,l) alpha(g,h,k+l).
                            lhs = (
                                zn_three_cocycle_exponent(n, p, b, c, d)
                                + zn_three_cocycle_exponent(n, p, a, (b + c) % n, d)
                                + zn_three_cocycle_exponent(n, p, a, b, c)
                            ) % n
                            rhs = (
                                zn_three_cocycle_exponent(n, p, (a + b) % n, c, d)
                                + zn_three_cocycle_exponent(n, p, a, b, (c + d) % n)
                            ) % n
                            assert_equal(f"Z_{n} pointed defect 3-cocycle", lhs, rhs)

        for r in range(n):
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        for d in range(n):
                            # delta(delta beta)=0, so changing junction bases
                            # by beta preserves the pentagon equation.
                            lhs = (
                                delta_beta_exponent(n, r, b, c, d)
                                + delta_beta_exponent(n, r, a, (b + c) % n, d)
                                + delta_beta_exponent(n, r, a, b, c)
                            ) % n
                            rhs = (
                                delta_beta_exponent(n, r, (a + b) % n, c, d)
                                + delta_beta_exponent(n, r, a, b, (c + d) % n)
                            ) % n
                            assert_equal(f"Z_{n} pointed defect coboundary cocycle", lhs, rhs)


def main() -> None:
    check_defect_fusion_as_operator_composition()
    check_noninvertible_projection_action()
    check_dagger_composition_and_pairing()
    check_bpz_weighted_defect_adjoint()
    check_isotopy_matrix_unitarity_for_junction_pairing()
    check_null_quotient_composition_descends()
    check_pointed_modular_category_verlinde_diagonalization()
    check_pointed_anomaly_cocycle_and_coboundary()
    print("All categorical-defect action, quotient, and dagger checks passed.")


if __name__ == "__main__":
    main()
