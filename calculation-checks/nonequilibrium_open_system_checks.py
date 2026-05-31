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


def check_msrjd_gaussian_fourier_kernel() -> None:
    delta_t = 0.17
    diffusion = 0.8
    increment = -0.43

    gaussian = math.exp(-(increment**2) / (4.0 * delta_t * diffusion)) / math.sqrt(
        4.0 * math.pi * delta_t * diffusion
    )
    fourier_gaussian = (
        math.sqrt(math.pi / (delta_t * diffusion))
        * math.exp(-(increment**2) / (4.0 * delta_t * diffusion))
        / (2.0 * math.pi)
    )
    assert_close("one-dimensional MSRJD Fourier kernel", fourier_gaussian, gaussian)

    matrix = [[1.2, 0.25], [0.25, 0.9]]
    vector = [0.3, -0.7]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
    inverse = [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]
    quadratic = sum(vector[i] * inverse[i][j] * vector[j] for i in range(2) for j in range(2))
    path_kernel = math.exp(-quadratic / (4.0 * delta_t)) / math.sqrt(
        (4.0 * math.pi * delta_t) ** 2 * determinant
    )
    transformed_kernel = (
        math.pi
        * math.exp(-quadratic / (4.0 * delta_t))
        / ((2.0 * math.pi) ** 2 * delta_t * math.sqrt(determinant))
    )
    assert_close("two-dimensional MSRJD determinant normalization", transformed_kernel, path_kernel)


def check_langevin_generator_expansion() -> None:
    x = 0.4
    delta_t = 0.015
    diffusion = 0.35
    drift = -0.7 * x + 0.2

    mean = x + delta_t * drift
    variance = 2.0 * delta_t * diffusion
    expected_cubic = mean**3 + 3.0 * mean * variance
    finite_difference = (expected_cubic - x**3) / delta_t

    generator_on_cubic = drift * (3.0 * x**2) + diffusion * (6.0 * x)
    exact_remainder = (
        delta_t * (3.0 * x * drift**2 + 6.0 * diffusion * drift)
        + (delta_t**2) * drift**3
    )
    assert_close("finite-step Langevin generator expansion", finite_difference, generator_on_cubic + exact_remainder)


def check_doi_peliti_two_species_generator() -> None:
    total_number = 3
    rate_ab = Fraction(2, 5)
    rate_ba = Fraction(3, 7)
    size = total_number + 1

    direct = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    doi_peliti = [[Fraction(0) for _ in range(size)] for _ in range(size)]

    for n_a in range(size):
        n_b = total_number - n_a
        if n_a:
            rate = rate_ab * n_a
            direct[n_a - 1][n_a] += rate
            direct[n_a][n_a] -= rate
        if n_b:
            rate = rate_ba * n_b
            direct[n_a + 1][n_a] += rate
            direct[n_a][n_a] -= rate

    reactions = [
        ((1, 0), (0, 1), rate_ab),
        ((0, 1), (1, 0), rate_ba),
    ]

    def falling(value: int, power: int) -> int:
        result = 1
        for offset in range(power):
            result *= value - offset
        return result

    for n_a in range(size):
        n_b = total_number - n_a
        for nu, nu_prime, rate_constant in reactions:
            factor = falling(n_a, nu[0]) * falling(n_b, nu[1])
            if factor == 0:
                continue
            target_a = n_a - nu[0] + nu_prime[0]
            target_b = n_b - nu[1] + nu_prime[1]
            assert target_a + target_b == total_number
            rate = rate_constant * factor
            doi_peliti[target_a][n_a] += rate
            doi_peliti[n_a][n_a] -= rate

    assert doi_peliti == direct
    for column in range(size):
        assert sum(doi_peliti[row][column] for row in range(size)) == 0


def check_doi_peliti_symbol_and_large_deviation_hamiltonian() -> None:
    rate_ab = Fraction(2, 5)
    rate_ba = Fraction(3, 7)
    z_a = Fraction(4, 3)
    z_b = Fraction(5, 6)

    symbol_at_projection = rate_ab * (1 - 1) * z_a + rate_ba * (1 - 1) * z_b
    assert symbol_at_projection == 0

    drift_a = -rate_ab * z_a + rate_ba * z_b
    drift_b = rate_ab * z_a - rate_ba * z_b
    assert drift_a + drift_b == 0

    n_a, n_b = 2, 1
    p_a, p_b = 0.23, -0.11

    def test_function(a_count: int, b_count: int) -> float:
        return math.exp(p_a * a_count + p_b * b_count)

    current = test_function(n_a, n_b)
    direct = 0.0
    direct += float(rate_ab * n_a) * (test_function(n_a - 1, n_b + 1) - current) / current
    direct += float(rate_ba * n_b) * (test_function(n_a + 1, n_b - 1) - current) / current
    hamiltonian = float(rate_ab * n_a) * (math.exp(p_b - p_a) - 1.0) + float(rate_ba * n_b) * (
        math.exp(p_a - p_b) - 1.0
    )
    assert_close("Doi-Peliti exponential-test Hamiltonian", direct, hamiltonian)


def check_tilted_jump_generator_and_gc_symmetry() -> None:
    rates = [[0.0, 1.2], [0.7, 0.0]]
    state_weights = [0.2, -0.1]
    jump_weights = [[0.0, 0.4], [-0.3, 0.0]]
    lam = 0.6
    test = [1.1, -0.4]

    tilted = []
    for i in range(2):
        value = lam * state_weights[i] * test[i]
        for j in range(2):
            if i == j:
                continue
            value += rates[i][j] * (math.exp(lam * jump_weights[i][j]) * test[j] - test[i])
        tilted.append(value)

    short_time_coefficients = [
        lam * state_weights[0] * test[0]
        + rates[0][1] * (math.exp(lam * jump_weights[0][1]) * test[1] - test[0]),
        lam * state_weights[1] * test[1]
        + rates[1][0] * (math.exp(lam * jump_weights[1][0]) * test[0] - test[1]),
    ]
    for i, (got, expected) in enumerate(zip(tilted, short_time_coefficients, strict=True)):
        assert_close(f"finite tilted Feynman-Kac generator row {i}", got, expected)

    clockwise_rate = 2.0
    counterclockwise_rate = 0.5
    q = 0.37
    entropy_step = math.log(clockwise_rate / counterclockwise_rate)
    escape = clockwise_rate + counterclockwise_rate

    def entropy_increment(i: int, j: int) -> float:
        if j == (i + 1) % 3:
            return entropy_step
        if j == (i - 1) % 3:
            return -entropy_step
        raise AssertionError("not a nearest-neighbor ring jump")

    def ring_rate(i: int, j: int) -> float:
        if j == (i + 1) % 3:
            return clockwise_rate
        if j == (i - 1) % 3:
            return counterclockwise_rate
        return 0.0

    def entropy_tilted_matrix(parameter: float) -> list[list[float]]:
        matrix = [[0.0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            matrix[i][i] = -escape
            for j in range(3):
                if i == j:
                    continue
                matrix[i][j] = ring_rate(i, j) * math.exp(-parameter * entropy_increment(i, j))
        return matrix

    l_q = entropy_tilted_matrix(q)
    l_one_minus_q = entropy_tilted_matrix(1.0 - q)
    for i in range(3):
        for j in range(3):
            assert_close("finite Gallavotti-Cohen similarity", l_q[i][j], l_one_minus_q[j][i])

    scgf_q = clockwise_rate ** (1.0 - q) * counterclockwise_rate**q
    scgf_q += counterclockwise_rate ** (1.0 - q) * clockwise_rate**q - escape
    reflected = clockwise_rate**q * counterclockwise_rate ** (1.0 - q)
    reflected += counterclockwise_rate**q * clockwise_rate ** (1.0 - q) - escape
    assert_close("finite ring entropy SCGF symmetry", scgf_q, reflected)
    assert_close(
        "finite ring entropy SCGF normalization at q=0",
        clockwise_rate + counterclockwise_rate - escape,
        0.0,
    )
    assert_close(
        "finite ring entropy SCGF normalization at q=1",
        counterclockwise_rate + clockwise_rate - escape,
        0.0,
    )
    entropy_rate = (clockwise_rate - counterclockwise_rate) * entropy_step
    assert entropy_rate > 0.0


def check_empirical_flow_level25_cost() -> None:
    clockwise_rate = 2.0
    counterclockwise_rate = 0.5
    rho = [1.0 / 3.0] * 3
    flow = [[0.0 for _ in range(3)] for _ in range(3)]
    rates = [[0.0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        flow[i][(i + 1) % 3] = 0.8
        flow[i][(i - 1) % 3] = 0.3
        rates[i][(i + 1) % 3] = clockwise_rate
        rates[i][(i - 1) % 3] = counterclockwise_rate

    for i in range(3):
        outgoing = sum(flow[i][j] for j in range(3) if j != i)
        incoming = sum(flow[j][i] for j in range(3) if j != i)
        assert_close(f"empirical flow conservation at vertex {i}", outgoing, incoming)

    cost = 0.0
    auxiliary_rates = [[0.0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            auxiliary_rates[i][j] = flow[i][j] / rho[i]
            mean_flow = rho[i] * rates[i][j]
            cost += flow[i][j] * math.log(flow[i][j] / mean_flow) - flow[i][j] + mean_flow
    assert cost > 0.0

    rn_density = 0.0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            rn_density += flow[i][j] * math.log(rates[i][j] / auxiliary_rates[i][j])
            rn_density -= rho[i] * (rates[i][j] - auxiliary_rates[i][j])
    assert_close("empirical-flow Radon-Nikodym cost sign", rn_density, -cost)

    typical_cost = 0.0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            typical_flow = rho[i] * rates[i][j]
            typical_cost += typical_flow * math.log(typical_flow / (rho[i] * rates[i][j]))
            typical_cost += -typical_flow + rho[i] * rates[i][j]
    assert_close("typical empirical-flow cost", typical_cost, 0.0)

    a, b = 1.7, 0.4
    p = 0.62
    minimizing_flow = math.sqrt(p * (1.0 - p) * a * b)
    direct_two_state = minimizing_flow * math.log(minimizing_flow / (p * a))
    direct_two_state += -minimizing_flow + p * a
    direct_two_state += minimizing_flow * math.log(minimizing_flow / ((1.0 - p) * b))
    direct_two_state += -minimizing_flow + (1.0 - p) * b
    contracted = (math.sqrt(p * a) - math.sqrt((1.0 - p) * b)) ** 2
    assert_close("two-state level-2 empirical-measure contraction", direct_two_state, contracted)
    stationary_p = b / (a + b)
    stationary_cost = (math.sqrt(stationary_p * a) - math.sqrt((1.0 - stationary_p) * b)) ** 2
    assert_close("two-state stationary level-2 cost", stationary_cost, 0.0)


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
    check_msrjd_gaussian_fourier_kernel()
    check_langevin_generator_expansion()
    check_doi_peliti_two_species_generator()
    check_doi_peliti_symbol_and_large_deviation_hamiltonian()
    check_tilted_jump_generator_and_gc_symmetry()
    check_empirical_flow_level25_cost()
    check_two_level_kms_stationary_ratio()
    check_ou_einstein_relation()
    check_positive_noise_kernel()
    print("All nonequilibrium open-system checks passed.")


if __name__ == "__main__":
    main()
