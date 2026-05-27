#!/usr/bin/env python3
"""Finite checks for categorical-defect action and dagger-structure algebra."""

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


def identity(size: int) -> Matrix:
    return [
        [Fraction(1) if row == column else Fraction(0) for column in range(size)]
        for row in range(size)
    ]


def zero_matrix(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


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


def main() -> None:
    check_defect_fusion_as_operator_composition()
    check_noninvertible_projection_action()
    check_dagger_composition_and_pairing()
    check_isotopy_matrix_unitarity_for_junction_pairing()
    print("All categorical-defect action and dagger-structure checks passed.")


if __name__ == "__main__":
    main()
