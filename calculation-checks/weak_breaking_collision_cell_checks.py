#!/usr/bin/env python3
"""Finite collision-cell checks for weak integrability breaking."""

from __future__ import annotations

from fractions import Fraction
from math import log


def assert_exact(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_close(name: str, got: float, expected: float, tol: float = 1e-12) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got:.16e}, expected {expected:.16e}")


def build_detailed_balance_rates() -> tuple[list[Fraction], list[list[Fraction]]]:
    stationary = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
    conductance = [
        [Fraction(0), Fraction(3, 7), Fraction(1, 5)],
        [Fraction(3, 7), Fraction(0), Fraction(2, 9)],
        [Fraction(1, 5), Fraction(2, 9), Fraction(0)],
    ]
    rates = [
        [
            Fraction(0) if i == j else conductance[i][j] / stationary[i]
            for j in range(3)
        ]
        for i in range(3)
    ]
    return stationary, rates


def apply_generator(probability: list[Fraction], rates: list[list[Fraction]]) -> list[Fraction]:
    derivative: list[Fraction] = []
    for target in range(len(probability)):
        gain = sum(
            probability[source] * rates[source][target]
            for source in range(len(probability))
            if source != target
        )
        loss = probability[target] * sum(
            rates[target][dest] for dest in range(len(probability)) if dest != target
        )
        derivative.append(gain - loss)
    return derivative


def check_detailed_balance_and_conserved_charge() -> None:
    stationary, rates = build_detailed_balance_rates()
    probability = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    occupations = [
        [Fraction(2), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    energy_per_particle = [Fraction(1), Fraction(2), Fraction(2)]
    higher_integrable_charge = [Fraction(0), Fraction(1), Fraction(3)]

    for i in range(3):
        for j in range(3):
            assert_exact(
                f"detailed balance {i}->{j}",
                stationary[i] * rates[i][j],
                stationary[j] * rates[j][i],
            )

    probability_derivative = apply_generator(probability, rates)
    assert_exact("total probability conservation", sum(probability_derivative), Fraction(0))

    occupation_collision = []
    for bin_index in range(3):
        value = sum(
            probability[source]
            * rates[source][target]
            * (occupations[target][bin_index] - occupations[source][bin_index])
            for source in range(3)
            for target in range(3)
        )
        occupation_collision.append(value)

    energy_collision = sum(
        energy_per_particle[bin_index] * occupation_collision[bin_index]
        for bin_index in range(3)
    )
    assert_exact("projected exact energy conservation", energy_collision, Fraction(0))

    higher_charge_collision = sum(
        higher_integrable_charge[bin_index] * occupation_collision[bin_index]
        for bin_index in range(3)
    )
    if higher_charge_collision == 0:
        raise AssertionError("weak-breaking example should relax the higher charge")


def check_entropy_production_identity() -> None:
    stationary, rates = build_detailed_balance_rates()
    probability = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    probability_derivative = apply_generator(probability, rates)
    ratio = [float(probability[i] / stationary[i]) for i in range(3)]

    direct_derivative = sum(
        float(probability_derivative[i]) * log(ratio[i]) for i in range(3)
    )
    symmetrized_derivative = -0.5 * sum(
        float(stationary[i] * rates[i][j])
        * (ratio[i] - ratio[j])
        * (log(ratio[i]) - log(ratio[j]))
        for i in range(3)
        for j in range(3)
    )
    assert_close("entropy production identity", direct_derivative, symmetrized_derivative)
    if symmetrized_derivative > 1e-14:
        raise AssertionError("relative entropy should be nonincreasing")


def main() -> None:
    check_detailed_balance_and_conserved_charge()
    check_entropy_production_identity()
    print("All weak-breaking collision-cell checks passed.")


if __name__ == "__main__":
    main()
