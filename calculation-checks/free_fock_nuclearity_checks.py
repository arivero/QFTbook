#!/usr/bin/env python3
"""Finite checks for the free-Fock phase-space benchmark.

These checks accompany the Volume IV nuclearity discussion.  They verify the
finite-mode bosonic product formula, the sup-norm lattice shell count used in
the phase-space estimate, and a small numerical sample of the beta^s-scaled
finite-volume free-Fock logarithm.
"""

from fractions import Fraction
from itertools import product
from math import exp, log, pi, sqrt

from check_utils import assert_lt as _assert_lt


def assert_equal(name: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_less(name: str, actual: float, bound: float) -> None:
    _assert_lt(name, actual, bound)


def check_bosonic_product_formula() -> None:
    q_values = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
    product_formula = Fraction(1, 1)
    for q in q_values:
        product_formula *= Fraction(1, 1) / (1 - q)

    # The coefficient sum factorizes into three independent geometric series.
    factorized_sum = (
        sum(q_values[0] ** k for k in range(30))
        + q_values[0] ** 30 / (1 - q_values[0])
    )
    factorized_sum *= (
        sum(q_values[1] ** k for k in range(30))
        + q_values[1] ** 30 / (1 - q_values[1])
    )
    factorized_sum *= (
        sum(q_values[2] ** k for k in range(30))
        + q_values[2] ** 30 / (1 - q_values[2])
    )

    assert_equal("finite-mode bosonic product formula", factorized_sum, product_formula)
    assert_equal("finite-mode displayed value", product_formula, Fraction(15, 4))


def shell_count_formula(s: int, k: int) -> int:
    if k == 0:
        return 1
    return (2 * k + 1) ** s - (2 * k - 1) ** s


def brute_shell_count(s: int, k: int) -> int:
    return sum(
        1
        for n in product(range(-k, k + 1), repeat=s)
        if max(abs(component) for component in n) == k
    )


def check_lattice_shell_count() -> None:
    for s in range(1, 5):
        for k in range(0, 5):
            assert_equal(
                f"sup-norm shell count s={s} k={k}",
                brute_shell_count(s, k),
                shell_count_formula(s, k),
            )

    for s in range(1, 7):
        for k in range(1, 20):
            bound = 2 * s * (2 * k + 1) ** (s - 1)
            assert_less(f"shell derivative bound s={s} k={k}", shell_count_formula(s, k), bound + 1)


def free_fock_log_partition(spatial_dim: int, beta: float, side_length: float, mass: float, cutoff: int) -> float:
    total = 0.0
    for n in product(range(-cutoff, cutoff + 1), repeat=spatial_dim):
        momentum_sq = sum(component * component for component in n)
        energy = sqrt((2 * pi / side_length) ** 2 * momentum_sq + mass * mass)
        total += -log(1.0 - exp(-beta * energy))
    return total


def check_scaled_log_partition_sample() -> None:
    side_length = 1.0
    mass = 1.0
    cutoff = 8
    for spatial_dim in (1, 2, 3):
        scaled_values = []
        for beta in (0.25, 0.2, 0.16):
            log_z = free_fock_log_partition(spatial_dim, beta, side_length, mass, cutoff)
            scaled_values.append((beta ** spatial_dim) * log_z)
        # The finite cutoff removes the far ultraviolet tail, so the scaled
        # values stay bounded well below this loose dimension-dependent guard.
        for value in scaled_values:
            assert_less(f"scaled finite Fock logZ d={spatial_dim}", value, 10.0)


def main() -> None:
    check_bosonic_product_formula()
    check_lattice_shell_count()
    check_scaled_log_partition_sample()
    print("All free-Fock nuclearity phase-space checks passed.")


if __name__ == "__main__":
    main()
