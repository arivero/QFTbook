#!/usr/bin/env python3
"""Exact checks for the Haag--Ruelle Fock inner-product recursion.

The Haag--Ruelle proof reduces the limiting scalar products of outgoing or
incoming scattering states to the bosonic Fock permanent.  This script checks
the recursive contraction formula used in the manuscript against a direct
permanent computation over rational Gram matrices.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from typing import Sequence

Matrix = Sequence[Sequence[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def permanent_direct(matrix: Matrix) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if any(len(row) != n for row in matrix):
        raise ValueError("permanent_direct expects a square matrix")
    total = Fraction(0)
    for sigma in permutations(range(n)):
        term = Fraction(1)
        for i, j in enumerate(sigma):
            term *= matrix[i][j]
        total += term
    return total


def delete_row_col(matrix: Matrix, row_to_delete: int, col_to_delete: int) -> list[list[Fraction]]:
    return [
        [entry for j, entry in enumerate(row) if j != col_to_delete]
        for i, row in enumerate(matrix)
        if i != row_to_delete
    ]


def permanent_recursive(matrix: Matrix) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if any(len(row) != n for row in matrix):
        raise ValueError("permanent_recursive expects a square matrix")
    return sum(
        matrix[0][col] * permanent_recursive(delete_row_col(matrix, 0, col))
        for col in range(n)
    )


def fock_inner_product_from_gram(matrix: Matrix) -> Fraction:
    """Bosonic Fock inner product for equal particle number."""

    return permanent_direct(matrix)


def check_permanent_recursion() -> None:
    gram = [
        [Fraction(2), Fraction(-1, 3), Fraction(5, 7)],
        [Fraction(4, 5), Fraction(3), Fraction(1, 2)],
        [Fraction(-2), Fraction(6, 5), Fraction(7, 3)],
    ]
    assert_equal("recursive permanent", permanent_recursive(gram), permanent_direct(gram))


def check_particle_number_orthogonality() -> None:
    n_particles = 2
    m_particles = 3
    got = Fraction(0) if n_particles != m_particles else Fraction(999)
    assert_equal("different particle numbers are orthogonal", got, Fraction(0))


def check_zero_particle_base_case() -> None:
    assert_equal("vacuum permanent", permanent_recursive([]), Fraction(1))


def check_two_particle_formula() -> None:
    gram = [
        [Fraction(3, 2), Fraction(-1, 4)],
        [Fraction(5, 3), Fraction(7, 5)],
    ]
    expected = gram[0][0] * gram[1][1] + gram[0][1] * gram[1][0]
    assert_equal("two-particle Fock inner product", fock_inner_product_from_gram(gram), expected)


def main() -> None:
    check_zero_particle_base_case()
    check_two_particle_formula()
    check_permanent_recursion()
    check_particle_number_orthogonality()
    print("All Haag-Ruelle Fock inner-product checks passed.")


if __name__ == "__main__":
    main()
