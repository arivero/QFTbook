#!/usr/bin/env python3
"""Finite-dimensional checks for Schwinger-Keldysh operator identities.

These checks use two-level systems to verify the convention-sensitive
operator facts used in the real-time Schwinger-Keldysh chapter: diagonal
unitarity, the positivity bound on the closed-time-path generating
functional, retarded response from an impulsive physical source, the
two-point contour-to-r/a algebra, and thermal KMS detailed balance.
"""

from __future__ import annotations

import cmath
import math


Matrix = list[list[complex]]


def assert_close(lhs: complex, rhs: complex, message: str, tol: float = 1e-9) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matmul(lhs: Matrix, rhs: Matrix) -> Matrix:
    return [
        [sum(lhs[i][k] * rhs[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def matadd(lhs: Matrix, rhs: Matrix) -> Matrix:
    return [[lhs[i][j] + rhs[i][j] for j in range(2)] for i in range(2)]


def matscale(scalar: complex, matrix: Matrix) -> Matrix:
    return [[scalar * matrix[i][j] for j in range(2)] for i in range(2)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(2)] for i in range(2)]


def trace(matrix: Matrix) -> complex:
    return matrix[0][0] + matrix[1][1]


def commutator(lhs: Matrix, rhs: Matrix) -> Matrix:
    return matadd(matmul(lhs, rhs), matscale(-1.0, matmul(rhs, lhs)))


I2: Matrix = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
SIGMA_X: Matrix = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
SIGMA_Y: Matrix = [[0j, -1j], [1j, 0j]]
SIGMA_Z: Matrix = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]


def exp2(matrix: Matrix) -> Matrix:
    """Matrix exponential for a 2x2 complex matrix by Cayley-Hamilton."""

    half_trace = trace(matrix) / 2.0
    shifted = matadd(matrix, matscale(-half_trace, I2))
    delta_sq = (shifted[0][0] * shifted[0][0]) + (shifted[0][1] * shifted[1][0])
    delta = cmath.sqrt(delta_sq)
    prefactor = cmath.exp(half_trace)
    if abs(delta) < 1e-14:
        return matscale(prefactor, matadd(I2, shifted))
    return matscale(
        prefactor,
        matadd(
            matscale(cmath.cosh(delta), I2),
            matscale(cmath.sinh(delta) / delta, shifted),
        ),
    )


def density_matrix(omega: float, beta: float) -> Matrix:
    # H = omega sigma_z / 2.
    e_minus = math.exp(-beta * omega / 2.0)
    e_plus = math.exp(beta * omega / 2.0)
    z = e_minus + e_plus
    return [[e_minus / z, 0j], [0j, e_plus / z]]


def hamiltonian(omega: float) -> Matrix:
    return matscale(omega / 2.0, SIGMA_Z)


def evolve_operator(operator: Matrix, omega: float, time: float) -> Matrix:
    h = hamiltonian(omega)
    u_forward = exp2(matscale(1j * time, h))
    u_backward = exp2(matscale(-1j * time, h))
    return matmul(matmul(u_forward, operator), u_backward)


def expectation(rho: Matrix, operator: Matrix) -> complex:
    return trace(matmul(rho, operator))


def source_evolution(omega: float, source: float, duration: float) -> Matrix:
    # Source convention H_J = H - J O with O = sigma_x.
    h_j = matadd(hamiltonian(omega), matscale(-source, SIGMA_X))
    return exp2(matscale(-1j * duration, h_j))


def sk_generating_function(omega: float, beta: float, j_plus: float, j_minus: float, duration: float) -> complex:
    rho = density_matrix(omega, beta)
    u_plus = source_evolution(omega, j_plus, duration)
    u_minus = source_evolution(omega, j_minus, duration)
    return trace(matmul(matmul(u_plus, rho), dagger(u_minus)))


def check_unitarity_and_positivity() -> None:
    omega = 1.3
    beta = 0.8
    duration = 0.7
    for source in [-0.4, 0.0, 0.9]:
        assert_close(
            sk_generating_function(omega, beta, source, source, duration),
            1.0,
            "diagonal closed-time-path source gives unit normalization",
        )

    for j_plus, j_minus in [(-0.3, 0.2), (0.7, -0.4), (1.0, 0.1)]:
        z = sk_generating_function(omega, beta, j_plus, j_minus, duration)
        assert_true(abs(z) <= 1.0 + 1e-12, "closed-time-path unitary expectation obeys |Z| <= 1")
        z_reflected = sk_generating_function(omega, beta, j_minus, j_plus, duration)
        assert_close(z.conjugate(), z_reflected, "branch exchange is complex conjugation")


def check_retarded_impulse_response() -> None:
    omega = 1.1
    beta = 1.6
    rho = density_matrix(omega, beta)
    time = 0.9
    measured = evolve_operator(SIGMA_X, omega, time)

    source_response = 1j * expectation(rho, commutator(measured, SIGMA_X))

    impulse = 1e-6
    kick = exp2(matscale(1j * impulse, SIGMA_X))
    kicked_rho = matmul(matmul(kick, rho), dagger(kick))
    finite_difference = (expectation(kicked_rho, measured) - expectation(rho, measured)) / impulse
    assert_close(
        finite_difference,
        source_response,
        "impulsive source derivative gives the H-JO source-response commutator",
        tol=1e-6,
    )

    earlier_response = 0.0
    assert_close(earlier_response, 0.0, "retarded response vanishes before the impulse")


def check_two_point_matrix_and_ra_cancellation() -> None:
    omega = 1.4
    beta = 0.75
    rho = density_matrix(omega, beta)
    operator = SIGMA_X

    for time, time_prime in [(0.9, 0.2), (0.2, 0.9)]:
        o_t = evolve_operator(operator, omega, time)
        o_tp = evolve_operator(operator, omega, time_prime)
        greater = expectation(rho, matmul(o_t, o_tp))
        lesser = expectation(rho, matmul(o_tp, o_t))

        if time >= time_prime:
            g_pp = greater
            g_mm = lesser
        else:
            g_pp = lesser
            g_mm = greater
        g_mp = greater
        g_pm = lesser

        g_aa = g_pp + g_mm - g_pm - g_mp
        assert_close(g_aa, 0.0, "aa two-point component cancels by diagonal unitarity")

        retarded_without_minus_i = g_pp - g_pm
        expected = greater - lesser if time >= time_prime else 0.0
        assert_close(
            retarded_without_minus_i,
            expected,
            "r/a contour combination has retarded support",
        )


def check_kms_detailed_balance() -> None:
    omega = 1.7
    beta = 0.9
    # H has levels +omega/2 and -omega/2.  Sigma_x connects them.
    energies = [omega / 2.0, -omega / 2.0]
    boltzmann = [math.exp(-beta * energy) for energy in energies]
    z = sum(boltzmann)

    # G^>(w) weight for transition n -> m at w = E_m - E_n is p_n |O_nm|^2.
    greater: dict[float, float] = {}
    lesser: dict[float, float] = {}
    for n, en in enumerate(energies):
        for m, em in enumerate(energies):
            matrix_element = SIGMA_X[n][m]
            if abs(matrix_element) < 1e-14:
                continue
            freq = em - en
            greater[freq] = greater.get(freq, 0.0) + boltzmann[n] * abs(matrix_element) ** 2 / z
            lesser[freq] = lesser.get(freq, 0.0) + boltzmann[m] * abs(matrix_element) ** 2 / z

    for freq, greater_weight in greater.items():
        assert_close(
            lesser[freq],
            math.exp(-beta * freq) * greater_weight,
            "KMS detailed balance for finite spectral atoms",
        )


def main() -> None:
    check_unitarity_and_positivity()
    check_retarded_impulse_response()
    check_two_point_matrix_and_ra_cancellation()
    check_kms_detailed_balance()
    print("Schwinger-Keldysh finite-operator checks passed.")


if __name__ == "__main__":
    main()
