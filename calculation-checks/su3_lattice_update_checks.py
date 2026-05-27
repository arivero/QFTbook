#!/usr/bin/env python3
"""Exact checks for finite SU(3) lattice subgroup-update conventions."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


I = sp.I
ZERO = sp.Integer(0)
ONE = sp.Integer(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matrix_unit(i: int, j: int) -> sp.Matrix:
    matrix = sp.zeros(3)
    matrix[i, j] = ONE
    return matrix


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def embedded_quarter_turn(i: int, j: int) -> sp.Matrix:
    """An SU(2) element embedded in the (i,j) color plane."""

    matrix = sp.eye(3)
    matrix[i, i] = ZERO
    matrix[j, j] = ZERO
    matrix[i, j] = ONE
    matrix[j, i] = -ONE
    return matrix


def x_generator(i: int, j: int) -> sp.Matrix:
    return matrix_unit(i, j) - matrix_unit(j, i)


def y_generator(i: int, j: int) -> sp.Matrix:
    return I * (matrix_unit(i, j) + matrix_unit(j, i))


def h_generator(i: int, j: int) -> sp.Matrix:
    return I * (matrix_unit(i, i) - matrix_unit(j, j))


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def check_embedded_su2_elements() -> None:
    identity = sp.eye(3)
    for pair in [(0, 1), (0, 2), (1, 2)]:
        element = embedded_quarter_turn(*pair)
        require(dagger(element) * element == identity, f"unitarity failed for {pair}")
        require(sp.simplify(element.det() - 1) == 0, f"determinant failed for {pair}")


def check_su2_subalgebra_commutators() -> None:
    for pair in [(0, 1), (0, 2), (1, 2)]:
        x = x_generator(*pair)
        y = y_generator(*pair)
        h = h_generator(*pair)
        require(commutator(x, y) == 2 * h, f"[X,Y] failed for {pair}")
        require(commutator(h, x) == 2 * y, f"[H,X] failed for {pair}")
        require(commutator(h, y) == -2 * x, f"[H,Y] failed for {pair}")


def check_su3_span() -> None:
    basis = [
        x_generator(0, 1),
        y_generator(0, 1),
        x_generator(0, 2),
        y_generator(0, 2),
        x_generator(1, 2),
        y_generator(1, 2),
        h_generator(0, 1),
        h_generator(1, 2),
    ]
    flattened = [sp.Matrix(matrix).reshape(9, 1) for matrix in basis]
    rank = sp.Matrix.hstack(*flattened).rank()
    require(rank == 8, "embedded SU(2) Lie algebras should span su(3)")
    for matrix in basis:
        require(dagger(matrix) == -matrix, "basis element is not anti-Hermitian")
        require(sp.trace(matrix) == 0, "basis element is not traceless")


def check_local_staple_gauge_covariance() -> None:
    u = embedded_quarter_turn(0, 1)
    g_left = embedded_quarter_turn(0, 2)
    g_right = embedded_quarter_turn(1, 2)
    v = sp.Matrix(
        [
            [1 + 2 * I, 3 - I, 2],
            [-2 + I, 1, 4 + I],
            [3, -I, -1 + I],
        ]
    )

    transformed_u = g_left * u * g_right.inv()
    transformed_v = g_right * v * g_left.inv()
    original_trace = sp.trace(u * v)
    transformed_trace = sp.trace(transformed_u * transformed_v)
    require(
        sp.simplify(original_trace - transformed_trace) == 0,
        "local staple trace is not gauge covariant",
    )


def check_metropolis_pairwise_balance() -> None:
    proposal = Fraction(7, 11)

    for weight_a, weight_b in [(Fraction(2), Fraction(5)), (Fraction(5), Fraction(2))]:
        forward = weight_a * proposal * min(Fraction(1), weight_b / weight_a)
        backward = weight_b * proposal * min(Fraction(1), weight_a / weight_b)
        require(forward == backward, "Metropolis pairwise balance failed")


def main() -> None:
    check_embedded_su2_elements()
    check_su2_subalgebra_commutators()
    check_su3_span()
    check_local_staple_gauge_covariance()
    check_metropolis_pairwise_balance()
    print("All SU(3) lattice subgroup-update checks passed.")


if __name__ == "__main__":
    main()
