#!/usr/bin/env python3
"""Finite checks for Monte Carlo variance and sign-problem formulae.

The script verifies algebra used in Volume XI, Chapter 6:

* the exact finite-N Markov-chain autocorrelation variance identity;
* the phase-reweighting identity and the average-phase relative variance;
* the distinction between gamma5-Hermiticity, determinant reality, and
  determinant positivity after flavor pairing.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(label: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(left)
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(size))
            for j in range(size)
        ]
        for i in range(size)
    ]


def matpow(matrix: list[list[Fraction]], power: int) -> list[list[Fraction]]:
    size = len(matrix)
    result = [
        [Fraction(1 if i == j else 0) for j in range(size)]
        for i in range(size)
    ]
    base = matrix
    n = power
    while n:
        if n & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n >>= 1
    return result


def check_autocorrelation_variance_identity() -> None:
    transition = [
        [Fraction(3, 4), Fraction(1, 4)],
        [Fraction(1, 2), Fraction(1, 2)],
    ]
    stationary = [Fraction(2, 3), Fraction(1, 3)]
    observable = [Fraction(1), Fraction(-2)]
    mean = sum(p * f for p, f in zip(stationary, observable))
    assert_equal("chosen observable has zero mean", mean, Fraction(0))

    def covariance(lag: int) -> Fraction:
        power = matpow(transition, lag)
        return sum(
            stationary[i] * observable[i] * power[i][j] * observable[j]
            for i in range(2)
            for j in range(2)
        )

    sample_size = 7
    exact_double_sum = Fraction(0)
    for r in range(sample_size):
        for s in range(sample_size):
            exact_double_sum += covariance(abs(r - s))
    exact_variance = exact_double_sum / sample_size**2

    compressed = (
        sample_size * covariance(0)
        + 2
        * sum((sample_size - lag) * covariance(lag) for lag in range(1, sample_size))
    ) / sample_size**2
    assert_equal("finite-N autocorrelation variance", compressed, exact_variance)


def check_phase_reweighting_identity_and_variance() -> None:
    probabilities = [Fraction(3, 5), Fraction(2, 5)]
    phases = [1, -1]
    observable = [Fraction(2), Fraction(5)]

    average_phase = sum(p * phase for p, phase in zip(probabilities, phases))
    numerator = sum(
        p * value * phase
        for p, value, phase in zip(probabilities, observable, phases)
    )
    reweighted = numerator / average_phase

    unnormalized_weights = [Fraction(3), Fraction(-2)]
    target = sum(w * value for w, value in zip(unnormalized_weights, observable))
    target /= sum(unnormalized_weights)
    assert_equal("finite reweighting identity", reweighted, target)

    sample_size = 8
    relative_variance = (1 - average_phase**2) / (sample_size * average_phase**2)
    assert_equal("average phase", average_phase, Fraction(1, 5))
    assert_equal("average-phase relative variance", relative_variance, Fraction(3))

    delta_squared = Fraction(1, 4)
    required_samples = (1 / average_phase**2 - 1) / delta_squared
    assert_equal("sample lower bound at delta=1/2", required_samples, Fraction(96))


def check_gamma5_hermiticity_reality_not_positivity() -> None:
    # Gamma = diag(1,-1).  The matrix [[a,b],[-conj(b),d]] obeys
    # Gamma D Gamma = D^\dagger when a and d are real.
    matrix = [[1, 1], [-1, -10]]
    gamma = [1, -1]
    gamma_d_gamma = [
        [gamma[i] * matrix[i][j] * gamma[j] for j in range(2)]
        for i in range(2)
    ]
    dagger = [[matrix[j][i] for j in range(2)] for i in range(2)]
    assert_equal("finite gamma5-Hermiticity model", gamma_d_gamma, dagger)

    a = 1
    b_abs_squared = 1
    d = -10
    determinant = a * d + b_abs_squared
    if determinant >= 0:
        raise AssertionError("example should show reality without positivity")

    two_flavor_weight = determinant**2
    conjugate_pair_weight = determinant * determinant
    assert_equal("two degenerate flavors are nonnegative", two_flavor_weight, 81)
    assert_equal("conjugate pair is nonnegative", conjugate_pair_weight, 81)


def main() -> None:
    check_autocorrelation_variance_identity()
    check_phase_reweighting_identity_and_variance()
    check_gamma5_hermiticity_reality_not_positivity()
    print("Monte Carlo sign-problem checks passed.")


if __name__ == "__main__":
    main()
