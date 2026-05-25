#!/usr/bin/env python3
"""Finite checks for Narain lattice cocycles and modular-condition logic."""

from itertools import product


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def mat_vec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def bilinear(matrix, left, right):
    return sum(left[i] * mat_vec(matrix, right)[i] for i in range(len(left)))


def add(left, right):
    return [a + b for a, b in zip(left, right)]


def cocycle(matrix, left, right):
    exponent = 0
    rank = len(left)
    for i in range(rank):
        for j in range(i):
            exponent += matrix[i][j] * left[i] * right[j]
    return -1 if exponent % 2 else 1


def determinant_integer(matrix):
    """Bareiss exact integer determinant."""

    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot = None
        for row in range(k, n):
            if a[row][k] != 0:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def hyperbolic_lattice(rank):
    zero = [[0 for _ in range(rank)] for _ in range(rank)]
    identity = [[1 if i == j else 0 for j in range(rank)] for i in range(rank)]
    return [zero[i] + identity[i] for i in range(rank)] + [
        identity[i] + zero[i] for i in range(rank)
    ]


def e8_cartan_matrix():
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        matrix[i][i] = 2
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]
    for i, j in edges:
        matrix[i][j] = -1
        matrix[j][i] = -1
    return matrix


def verify_even_unimodular(matrix):
    for i in range(len(matrix)):
        require(matrix[i][i] % 2 == 0, "diagonal entries must be even")
    require(abs(determinant_integer(matrix)) == 1, "lattice must be unimodular")


def verify_cocycle_identities(matrix, vectors):
    for left in vectors:
        for middle in vectors:
            for right in vectors:
                require(
                    cocycle(matrix, left, add(middle, right))
                    * cocycle(matrix, middle, right)
                    == cocycle(matrix, left, middle)
                    * cocycle(matrix, add(left, middle), right),
                    "cocycle associativity failed",
                )
    for left in vectors:
        for right in vectors:
            exchange_sign = -1 if bilinear(matrix, left, right) % 2 else 1
            require(
                cocycle(matrix, right, left)
                == exchange_sign * cocycle(matrix, left, right),
                "cocycle exchange law failed",
            )
            require(
                bilinear(matrix, left, left) % 2 == 0,
                "self-pairing must be even",
            )


def verify_toroidal_pairing_formula():
    # Dimensionless T^2 coordinates, alpha'=1, G=I, and B_{12}=b.
    b_field = [[0, 3], [-3, 0]]
    vectors = [list(v) for v in product(range(-2, 3), repeat=2)]
    for momentum in vectors:
        for winding in vectors:
            shifted = [
                momentum[i] - sum(b_field[i][j] * winding[j] for j in range(2))
                for i in range(2)
            ]
            self_difference = 2 * sum(shifted[i] * winding[i] for i in range(2))
            require(
                self_difference == 2 * sum(momentum[i] * winding[i] for i in range(2)),
                "antisymmetric B-field must cancel in k_L^2-k_R^2",
            )
            for momentum2 in vectors:
                for winding2 in vectors:
                    shifted2 = [
                        momentum2[i]
                        - sum(b_field[i][j] * winding2[j] for j in range(2))
                        for i in range(2)
                    ]
                    pairing = sum(shifted[i] * winding2[i] for i in range(2))
                    pairing += sum(shifted2[i] * winding[i] for i in range(2))
                    expected = sum(momentum[i] * winding2[i] for i in range(2))
                    expected += sum(momentum2[i] * winding[i] for i in range(2))
                    require(pairing == expected, "Narain pairing formula failed")


def even_unimodular_lattice_can_exist(n_left, n_right):
    return (n_left - n_right) % 8 == 0


def scalar_partition_function_can_be_modular_invariant(n_left, n_right):
    return (n_left - n_right) % 24 == 0


for gram_matrix in [hyperbolic_lattice(1), hyperbolic_lattice(2), e8_cartan_matrix()]:
    verify_even_unimodular(gram_matrix)

verify_cocycle_identities(
    hyperbolic_lattice(1),
    [list(v) for v in product(range(-2, 3), repeat=2)],
)
verify_cocycle_identities(
    hyperbolic_lattice(2),
    [list(v) for v in product(range(-1, 2), repeat=4)],
)
e8_samples = [[0 for _ in range(8)]]
e8_samples += [[1 if i == j else 0 for i in range(8)] for j in range(8)]
e8_samples += [[1 if i in (j, (j + 1) % 8) else 0 for i in range(8)] for j in range(8)]
e8_samples += [[1 for _ in range(8)]]
verify_cocycle_identities(e8_cartan_matrix(), e8_samples)
verify_toroidal_pairing_formula()

require(even_unimodular_lattice_can_exist(1, 1), "Gamma^{1,1} should exist")
require(even_unimodular_lattice_can_exist(8, 0), "E8 lattice should exist")
require(
    not scalar_partition_function_can_be_modular_invariant(8, 0),
    "c=8 chiral lattice has a gravitational-anomaly T phase",
)
require(
    scalar_partition_function_can_be_modular_invariant(24, 0),
    "c=24 chiral bosonic partition functions can have trivial T phase",
)
require(
    scalar_partition_function_can_be_modular_invariant(5, 5),
    "ordinary nonchiral torus sigma models have no c_L-c_R anomaly",
)

print("All Narain lattice cocycle and modular-condition checks passed.")
