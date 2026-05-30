#!/usr/bin/env python3
"""Finite standard-form checks for Tomita--Takesaki conventions."""

from __future__ import annotations

import cmath
from math import sqrt


Matrix = list[list[complex]]


def assert_close(name: str, got: complex, expected: complex, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def adjoint(a: Matrix) -> Matrix:
    n = len(a)
    return [[a[j][i].conjugate() for j in range(n)] for i in range(n)]


def left(a: Matrix, x: Matrix) -> Matrix:
    return matmul(a, x)


def right(x: Matrix, a: Matrix) -> Matrix:
    return matmul(x, a)


def diag_power(lambdas: list[float], power: complex) -> Matrix:
    return [
        [cmath.exp(power * cmath.log(lambdas[i])) if i == j else 0.0 for j in range(len(lambdas))]
        for i in range(len(lambdas))
    ]


def basis(n: int, i: int, j: int) -> Matrix:
    return [[1.0 if (r, c) == (i, j) else 0.0 for c in range(n)] for r in range(n)]


def check_entrywise(name: str, got: Matrix, expected: Matrix, tol: float = 1.0e-10) -> None:
    for i in range(len(got)):
        for j in range(len(got)):
            assert_close(f"{name} ({i},{j})", got[i][j], expected[i][j], tol)


def check_tomita_polar_data() -> None:
    lambdas = [0.2, 0.3, 0.5]
    n = len(lambdas)
    rho_half = diag_power(lambdas, 0.5)
    rho_minus_half = diag_power(lambdas, -0.5)
    rho = diag_power(lambdas, 1.0)
    rho_inv = diag_power(lambdas, -1.0)

    for i in range(n):
        for j in range(n):
            eij = basis(n, i, j)
            tomita = matmul(rho_minus_half, matmul(adjoint(eij), rho_half))
            expected_tomita = [
                [sqrt(lambdas[i] / lambdas[j]) if (r, c) == (j, i) else 0.0 for c in range(n)]
                for r in range(n)
            ]
            check_entrywise("Tomita on matrix unit", tomita, expected_tomita)

            delta = matmul(rho, matmul(eij, rho_inv))
            expected_delta = [
                [lambdas[i] / lambdas[j] if (r, c) == (i, j) else 0.0 for c in range(n)]
                for r in range(n)
            ]
            check_entrywise("modular operator on matrix unit", delta, expected_delta)

            polar = adjoint(matmul(rho_half, matmul(eij, rho_minus_half)))
            check_entrywise("S = J Delta^(1/2)", polar, tomita)


def check_commutant_and_modular_automorphism() -> None:
    lambdas = [0.17, 0.31, 0.52]
    n = len(lambdas)
    a = [
        [0.3, 0.2 + 0.1j, -0.4],
        [0.7j, -0.2, 0.5 - 0.3j],
        [0.1, -0.6j, 0.8],
    ]
    x = [
        [0.4, 0.1 - 0.2j, 0.3],
        [-0.5j, 0.7, -0.1],
        [0.2 + 0.4j, -0.3, 0.6],
    ]

    j_left_j = adjoint(left(a, adjoint(x)))
    right_a_star = right(x, adjoint(a))
    check_entrywise("J L_A J = R_A*", j_left_j, right_a_star)

    t = 0.37
    rho_it = diag_power(lambdas, 1j * t)
    rho_minus_it = diag_power(lambdas, -1j * t)
    sigma_a = matmul(rho_it, matmul(a, rho_minus_it))
    delta_it_left_a_delta_minus_it = matmul(rho_it, matmul(a, matmul(rho_minus_it, x)))
    check_entrywise(
        "Delta^it L_A Delta^-it = L_sigma(A)",
        delta_it_left_a_delta_minus_it,
        left(sigma_a, x),
    )


def modular_alpha(matrix: Matrix, lambdas: list[float], z: complex) -> Matrix:
    rho_minus_iz = diag_power(lambdas, -1j * z)
    rho_iz = diag_power(lambdas, 1j * z)
    return matmul(rho_minus_iz, matmul(matrix, rho_iz))


def state(matrix: Matrix, lambdas: list[float]) -> complex:
    rho = diag_power(lambdas, 1.0)
    return trace(matmul(rho, matrix))


def check_kms_for_inverse_modular_flow() -> None:
    lambdas = [0.2, 0.3, 0.5]
    a = [
        [1.0, 0.3 + 0.2j, -0.4],
        [0.1 - 0.5j, -0.7, 0.6j],
        [0.2, -0.3j, 0.4],
    ]
    b = [
        [0.2, -0.1j, 0.5],
        [0.7 + 0.2j, -0.1, 0.3],
        [-0.6j, 0.4 - 0.2j, 0.9],
    ]

    for t in (-1.1, 0.0, 0.8):
        lower = state(matmul(a, modular_alpha(b, lambdas, t)), lambdas)
        explicit_lower = trace(matmul(diag_power(lambdas, 1.0), matmul(a, modular_alpha(b, lambdas, t))))
        assert_close("lower modular KMS boundary", lower, explicit_lower)

        upper = trace(
            matmul(
                diag_power(lambdas, 1.0),
                matmul(a, modular_alpha(b, lambdas, t + 1j)),
            )
        )
        target = state(matmul(modular_alpha(b, lambdas, t), a), lambdas)
        assert_close("upper modular KMS boundary", upper, target)


def main() -> None:
    check_tomita_polar_data()
    check_commutant_and_modular_automorphism()
    check_kms_for_inverse_modular_flow()
    print("All finite Tomita standard-form checks passed.")


if __name__ == "__main__":
    main()
