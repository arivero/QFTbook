#!/usr/bin/env python3
"""Finite split/nuclearity normality checks.

These checks accompany the Volume IV discussion of the nuclearity-to-split
mechanism.  They verify, in finite matrix algebras, the product-state
normality algebra and the separated finite-rank expansion that models the
normal functional produced by a nuclear map.
"""

from fractions import Fraction


Matrix = list[list[Fraction]]
Vector = list[Fraction]


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_positive(name: str, value: Fraction) -> None:
    if value <= 0:
        raise AssertionError(f"{name}: expected positive value, got {value!r}")


def assert_less_equal(name: str, actual: Fraction, bound: Fraction) -> None:
    if actual > bound:
        raise AssertionError(f"{name}: expected {actual!r} <= {bound!r}")


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    mid = len(right)
    cols = len(right[0])
    return [
        [sum(left[i][k] * right[k][j] for k in range(mid)) for j in range(cols)]
        for i in range(rows)
    ]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def kron(left: Matrix, right: Matrix) -> Matrix:
    out: Matrix = []
    for left_row in left:
        for right_row in right:
            out.append([
                left_entry * right_entry
                for left_entry in left_row
                for right_entry in right_row
            ])
    return out


def trace(matrix: Matrix) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def diag(entries: list[Fraction]) -> Matrix:
    return [
        [entry if i == j else Fraction(0) for j, entry in enumerate(entries)]
        for i, entry in enumerate(entries)
    ]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(a * b for a, b in zip(left, right))


def matrix_state(density: Matrix, observable: Matrix) -> Fraction:
    return trace(matmul(density, observable))


def matrix_sup_norm(matrix: Matrix) -> Fraction:
    return max(abs(entry) for row in matrix for entry in row)


def vector_l1_norm(vector: Vector) -> Fraction:
    return sum(abs(entry) for entry in vector)


def check_product_state_extension() -> None:
    rho_1 = diag([Fraction(1, 3), Fraction(2, 3)])
    rho_2 = diag([Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)])
    rho_product = kron(rho_1, rho_2)

    a = [[Fraction(1), Fraction(2)], [Fraction(0), Fraction(3)]]
    b = [
        [Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(0), Fraction(2)],
    ]

    separated = matrix_state(rho_1, a) * matrix_state(rho_2, b)
    tensor_state = matrix_state(rho_product, kron(a, b))
    assert_equal("product state equals tensor density state", tensor_state, separated)

    a_1 = [[Fraction(1), Fraction(1)], [Fraction(0), Fraction(2)]]
    a_2 = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(1)]]
    b_1 = [
        [Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(2), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(1)],
    ]
    b_2 = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(1), Fraction(2)],
    ]
    c = add(kron(a_1, b_1), kron(a_2, b_2))
    positive_observable = matmul(transpose(c), c)
    value = matrix_state(rho_product, positive_observable)
    assert_positive("normal product state positivity on C^* C", value)


def theta(matrix: Matrix) -> Vector:
    damping = [Fraction(1, 2), Fraction(1, 3)]
    omega = [Fraction(1), Fraction(2)]
    return [
        damping[i] * sum(matrix[i][j] * omega[j] for j in range(2))
        for i in range(2)
    ]


def finite_rank_terms(matrix: Matrix) -> list[tuple[Fraction, Vector]]:
    damping = [Fraction(1, 2), Fraction(1, 3)]
    omega = [Fraction(1), Fraction(2)]
    terms: list[tuple[Fraction, Vector]] = []
    for i in range(2):
        for j in range(2):
            basis_vector = [Fraction(0), Fraction(0)]
            basis_vector[i] = damping[i] * omega[j]
            terms.append((matrix[i][j], basis_vector))
    return terms


def check_finite_rank_nuclear_expansion() -> None:
    a = [[Fraction(2), Fraction(-1)], [Fraction(3), Fraction(4)]]
    reconstructed = [Fraction(0), Fraction(0)]
    for coefficient, vector in finite_rank_terms(a):
        reconstructed = [value + coefficient * vector[i] for i, value in enumerate(reconstructed)]
    assert_equal("finite-rank nuclear expansion reconstructs theta(A)", reconstructed, theta(a))

    nuclear_bound = sum(vector_l1_norm(vector) for _, vector in finite_rank_terms([[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]]))
    assert_equal("finite-rank l1 nuclear bound", nuclear_bound, Fraction(5, 2))
    assert_less_equal(
        "finite-rank nuclear bound controls theta(A)",
        vector_l1_norm(theta(a)),
        nuclear_bound * matrix_sup_norm(a),
    )

    b_prime = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(5)]]
    eta = [Fraction(7), Fraction(11)]
    direct = dot(eta, matvec(b_prime, theta(a)))
    expanded = sum(
        coefficient * dot(eta, matvec(b_prime, vector))
        for coefficient, vector in finite_rank_terms(a)
    )
    assert_equal("separated bilinear functional expansion", expanded, direct)


def main() -> None:
    check_product_state_extension()
    check_finite_rank_nuclear_expansion()
    print("All split/nuclearity normality finite checks passed.")


if __name__ == "__main__":
    main()
