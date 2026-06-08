#!/usr/bin/env python3
"""Finite checks for the lattice-to-continuum bridge chapter.

The checks verify the finite algebra used in Volume XI, Chapter 8: cell
averages, finite-graph random-walk resolvents, the finite-graph Dirichlet
form convention, closedness of reflection positivity, and tensor-product
locality.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Matrix = list[list[Fraction]]


def assert_equal(label: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def identity(size: int) -> Matrix:
    return [[Fraction(1 if i == j else 0) for j in range(size)] for i in range(size)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matvec(matrix: Matrix, vector: list[Fraction]) -> list[Fraction]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def quadratic_form(matrix: Matrix, vector: list[Fraction]) -> Fraction:
    return sum(vector[i] * value for i, value in enumerate(matvec(matrix, vector)))


def matadd(left: Matrix, right: Matrix, sign: int = 1) -> Matrix:
    return [
        [left[i][j] + sign * right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def matscale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return [[scalar * entry for entry in row] for row in matrix]


def matpow(matrix: Matrix, power: int) -> Matrix:
    result = identity(len(matrix))
    base = matrix
    n = power
    while n:
        if n & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n >>= 1
    return result


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    aug = [row[:] + identity(size)[i] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if aug[row][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [entry / pivot_value for entry in aug[col]]
        for row in range(size):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * size)
                ]
    return [row[size:] for row in aug]


def determinant_2(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def check_cell_average_product() -> None:
    # On n cells in [0,1], the cell average of f(x)=x is (k+1/2)/n.
    # Hence the cell-average square differs from int_0^1 x^2 dx by -1/(12n^2).
    n = 6
    lattice_sum = sum(Fraction(2 * k + 1, 2 * n) ** 2 for k in range(n)) / n
    assert_equal(
        "cell-average x*x error",
        lattice_sum - Fraction(1, 3),
        -Fraction(1, 12 * n * n),
    )


def cycle_adjacency(size: int) -> Matrix:
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        matrix[i][(i - 1) % size] = Fraction(1)
        matrix[i][(i + 1) % size] = Fraction(1)
    return matrix


def cycle_edges(size: int) -> list[tuple[int, int]]:
    return [(i, (i + 1) % size) for i in range(size)]


def edge_dirichlet_form(vector: list[Fraction], edges: list[tuple[int, int]]) -> Fraction:
    return sum((vector[left] - vector[right]) ** 2 for left, right in edges)


def enumerate_cycle_paths(size: int, start: int, end: int, length: int) -> int:
    count = 0
    for steps in product([-1, 1], repeat=length):
        position = start
        for step in steps:
            position = (position + step) % size
        if position == end:
            count += 1
    return count


def check_random_walk_resolvent() -> None:
    size = 4
    degree = 2
    mass_squared = Fraction(3)
    adjacency = cycle_adjacency(size)
    k_matrix = matadd(matscale(mass_squared + degree, identity(size)), adjacency, sign=-1)
    covariance = inverse(k_matrix)
    assert_equal("massive graph inverse", matmul(k_matrix, covariance), identity(size))

    b_matrix = matscale(Fraction(1, mass_squared + degree), adjacency)
    neumann_inverse = inverse(matadd(identity(size), b_matrix, sign=-1))
    resolvent = matscale(Fraction(1, mass_squared + degree), neumann_inverse)
    assert_equal("Neumann resolvent identity", covariance, resolvent)

    fourth_power = matpow(adjacency, 4)
    path_count = enumerate_cycle_paths(size, start=0, end=0, length=4)
    assert_equal("path count equals adjacency power", fourth_power[0][0], path_count)


def check_finite_graph_dirichlet_form() -> None:
    size = 5
    degree = 2
    mass_squared = Fraction(5, 3)
    adjacency = cycle_adjacency(size)
    laplacian = matadd(matscale(degree, identity(size)), adjacency, sign=-1)
    k_matrix = matadd(matscale(mass_squared + degree, identity(size)), adjacency, sign=-1)
    vector = [Fraction(2), Fraction(-1), Fraction(3), Fraction(0), Fraction(1)]

    mass_term = mass_squared * sum(entry * entry for entry in vector)
    edge_term = edge_dirichlet_form(vector, cycle_edges(size))
    assert_equal("cycle graph Laplacian Dirichlet form", quadratic_form(laplacian, vector), edge_term)
    assert_equal("massive graph quadratic form", quadratic_form(k_matrix, vector), mass_term + edge_term)

    half_weighted_unoriented = mass_term + Fraction(1, 2) * edge_term
    if quadratic_form(k_matrix, vector) == half_weighted_unoriented:
        raise AssertionError("negative control failed: half-weighted unoriented edge sum matched K_m")


def check_reflection_positivity_closedness() -> None:
    epsilon = Fraction(1, 7)
    gram = [[Fraction(1), 1 - epsilon], [1 - epsilon, Fraction(1)]]
    limit_gram = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]]
    if determinant_2(gram) <= 0:
        raise AssertionError("approximating Gram matrix should be positive definite")
    assert_equal("limit Gram determinant", determinant_2(limit_gram), Fraction(0))
    for c0, c1 in [(Fraction(1), Fraction(-1)), (Fraction(2), Fraction(3))]:
        quadratic = (
            c0 * c0 * limit_gram[0][0]
            + c0 * c1 * limit_gram[0][1]
            + c1 * c0 * limit_gram[1][0]
            + c1 * c1 * limit_gram[1][1]
        )
        if quadratic < 0:
            raise AssertionError("limit Gram matrix should be positive semidefinite")


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            left[i][j] * right[k][ell]
            for j in range(len(left[0]))
            for ell in range(len(right[0]))
        ]
        for i in range(len(left))
        for k in range(len(right))
    ]


def check_spin_tensor_locality() -> None:
    one = identity(2)
    sigma_x = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    sigma_z = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
    left_local = kronecker(sigma_x, one)
    right_local = kronecker(one, sigma_z)
    commutator = matadd(matmul(left_local, right_local), matmul(right_local, left_local), sign=-1)
    assert_equal("disjoint tensor factors commute", commutator, [[Fraction(0)] * 4 for _ in range(4)])


def main() -> None:
    check_cell_average_product()
    check_random_walk_resolvent()
    check_finite_graph_dirichlet_form()
    check_reflection_positivity_closedness()
    check_spin_tensor_locality()
    print("Lattice-to-continuum bridge checks passed.")


if __name__ == "__main__":
    main()
