#!/usr/bin/env python3
"""Finite checks for nonequilibrium steady states and open-system limits."""

from __future__ import annotations

import math
from fractions import Fraction


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-11) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def trace(a: list[list[complex]]) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def add(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def check_reservoir_entropy_production() -> None:
    beta_l, beta_r = 0.8, 1.1
    mu_l, mu_r = 0.2, -0.1
    force = [beta_r - beta_l, -(beta_r * mu_r - beta_l * mu_l)]
    onsager = [[2.0, 0.3], [0.3, 0.7]]
    currents = [
        onsager[0][0] * force[0] + onsager[0][1] * force[1],
        onsager[1][0] * force[0] + onsager[1][1] * force[1],
    ]
    entropy = force[0] * currents[0] + force[1] * currents[1]
    determinant = onsager[0][0] * onsager[1][1] - onsager[0][1] ** 2
    assert onsager[0][0] > 0.0 and determinant > 0.0
    assert entropy > 0.0

    direct = (beta_r - beta_l) * currents[0] - (beta_r * mu_r - beta_l * mu_l) * currents[1]
    assert_close("reservoir entropy formula", entropy, direct)


def check_gksl_trace_preservation() -> None:
    rho = [[0.6 + 0j, 0.1 - 0.2j], [0.1 + 0.2j, 0.4 + 0j]]
    jump = [[0j, 1.3 + 0.2j], [0j, 0j]]
    jump_dag = dagger(jump)
    ldagl = matmul(jump_dag, jump)
    dissipator = add(
        matmul(matmul(jump, rho), jump_dag),
        scale(-0.5, add(matmul(ldagl, rho), matmul(rho, ldagl))),
    )
    assert_close("single-jump trace preservation", trace(dissipator), 0.0)


def check_finite_local_detailed_balance_entropy() -> None:
    # Two-state, two-reservoir jump model with rates chosen to satisfy
    # log(W_01/W_10) = -beta (Delta E - mu Delta Q).
    probabilities = [Fraction(3, 5), Fraction(2, 5)]
    rates = [
        (Fraction(1, 3), Fraction(2, 9)),
        (Fraction(5, 7), Fraction(4, 7)),
    ]

    total_entropy = 0.0
    system_entropy_derivative = 0.0
    reservoir_entropy = 0.0
    for w01, w10 in rates:
        forward = probabilities[0] * w01
        backward = probabilities[1] * w10
        current = forward - backward
        total_entropy += 0.5 * float(
            current * math.log(float(forward / backward))
            + (-current) * math.log(float(backward / forward))
        )
        system_entropy_derivative += 0.5 * float(
            current * math.log(float(probabilities[0] / probabilities[1]))
            + (-current) * math.log(float(probabilities[1] / probabilities[0]))
        )
        reservoir_entropy += 0.5 * float(
            current * math.log(float(w01 / w10))
            + (-current) * math.log(float(w10 / w01))
        )

    assert total_entropy >= -1.0e-14
    assert_close("finite local detailed balance entropy split", total_entropy, system_entropy_derivative + reservoir_entropy)


def check_jump_path_measure_ratio() -> None:
    p0 = {0: 0.6, 1: 0.4}
    q0 = {0: 0.55, 1: 0.45}
    total_time = 1.0
    states = [0, 1, 0]
    jump_times = [0.3, 0.8]
    reservoirs = ["A", "B"]
    rates = {
        "A": {(0, 1): 2.0, (1, 0): 1.0},
        "B": {(0, 1): 0.5, (1, 0): 3.0},
    }

    def escape(state: int) -> float:
        return sum(rates[reservoir][(state, other)] for reservoir in rates for other in (0, 1) if other != state)

    def forward_density() -> float:
        intervals = [jump_times[0], jump_times[1] - jump_times[0], total_time - jump_times[1]]
        probability = p0[states[0]]
        for state, duration in zip(states, intervals, strict=True):
            probability *= math.exp(-escape(state) * duration)
        for step, reservoir in enumerate(reservoirs, start=1):
            probability *= rates[reservoir][(states[step - 1], states[step])]
        return probability

    def reverse_density() -> float:
        reversed_states = list(reversed(states))
        reversed_jump_times = [total_time - jump_times[1], total_time - jump_times[0]]
        reversed_reservoirs = list(reversed(reservoirs))
        intervals = [
            reversed_jump_times[0],
            reversed_jump_times[1] - reversed_jump_times[0],
            total_time - reversed_jump_times[1],
        ]
        probability = q0[reversed_states[0]]
        for state, duration in zip(reversed_states, intervals, strict=True):
            probability *= math.exp(-escape(state) * duration)
        for step, reservoir in enumerate(reversed_reservoirs, start=1):
            probability *= rates[reservoir][(reversed_states[step - 1], reversed_states[step])]
        return probability

    log_ratio = math.log(forward_density() / reverse_density())
    expected = math.log(p0[states[0]] / q0[states[-1]])
    for step, reservoir in enumerate(reservoirs, start=1):
        expected += math.log(rates[reservoir][(states[step - 1], states[step])] / rates[reservoir][(states[step], states[step - 1])])
    assert_close("finite jump path-measure ratio", log_ratio, expected)


def check_discrete_jarzynski_identity() -> None:
    beta = 1.3
    lambdas = [0.2, 0.9, 1.4]

    def energy(state: int, lam: float) -> float:
        return 0.0 if state == 0 else lam

    def partition(lam: float) -> float:
        return sum(math.exp(-beta * energy(state, lam)) for state in (0, 1))

    def gibbs(lam: float) -> list[float]:
        z = partition(lam)
        return [math.exp(-beta * energy(state, lam)) / z for state in (0, 1)]

    def heat_bath_kernel(lam: float) -> list[list[float]]:
        stationary = gibbs(lam)
        return [stationary[:], stationary[:]]

    initial = gibbs(lambdas[0])
    kernels = [heat_bath_kernel(lambdas[1]), heat_bath_kernel(lambdas[2])]
    average = 0.0
    for i0 in (0, 1):
        for i1 in (0, 1):
            for i2 in (0, 1):
                probability = initial[i0] * kernels[0][i0][i1] * kernels[1][i1][i2]
                work = (
                    energy(i0, lambdas[1])
                    - energy(i0, lambdas[0])
                    + energy(i1, lambdas[2])
                    - energy(i1, lambdas[1])
                )
                average += probability * math.exp(-beta * work)

    free_energy_factor = partition(lambdas[2]) / partition(lambdas[0])
    assert_close("finite driven Jarzynski identity", average, free_energy_factor)


def check_two_level_kms_stationary_ratio() -> None:
    beta = 1.4
    gap = 0.9
    gamma_down = 0.73
    gamma_up = math.exp(-beta * gap) * gamma_down
    p_excited = gamma_up / (gamma_up + gamma_down)
    p_ground = gamma_down / (gamma_up + gamma_down)
    assert_close("KMS stationary ratio", p_excited / p_ground, math.exp(-beta * gap))


def check_ou_einstein_relation() -> None:
    gamma = 0.37
    chi = 1.8
    temperature = 0.9
    diffusion_n = gamma * chi * temperature
    variance = diffusion_n / gamma
    assert_close("OU equilibrium variance", variance, chi * temperature)

    n_minus_n0 = 0.6
    log_derivative = -n_minus_n0 / (chi * temperature)
    probability_current = -gamma * n_minus_n0 - diffusion_n * log_derivative
    assert_close("OU stationary probability current", probability_current, 0.0)


def check_positive_noise_kernel() -> None:
    kernel = [[1.2, 0.25], [0.25, 0.9]]
    test = [0.4, -1.1]
    quadratic = sum(test[i] * kernel[i][j] * test[j] for i in range(2) for j in range(2))
    determinant = kernel[0][0] * kernel[1][1] - kernel[0][1] ** 2
    assert kernel[0][0] > 0.0 and determinant > 0.0
    assert quadratic > 0.0


def main() -> None:
    check_reservoir_entropy_production()
    check_gksl_trace_preservation()
    check_finite_local_detailed_balance_entropy()
    check_jump_path_measure_ratio()
    check_discrete_jarzynski_identity()
    check_two_level_kms_stationary_ratio()
    check_ou_einstein_relation()
    check_positive_noise_kernel()
    print("All nonequilibrium open-system checks passed.")


if __name__ == "__main__":
    main()
