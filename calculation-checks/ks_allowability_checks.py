#!/usr/bin/env python3
"""Finite checks for the Kontsevich-Segal allowability criterion."""

from __future__ import annotations

import cmath
from itertools import combinations
from math import pi


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def principal_arg(z: complex) -> float:
    arg = cmath.phase(z)
    if arg <= -pi:
        arg += 2 * pi
    return arg


def allowable_by_angles(lambdas: list[complex]) -> bool:
    return sum(abs(principal_arg(z)) for z in lambdas) < pi


def subset_coefficients(lambdas: list[complex]) -> list[complex]:
    det_sqrt = cmath.sqrt(complex(1))
    for z in lambdas:
        det_sqrt *= cmath.sqrt(z)
    if det_sqrt.real < 0:
        det_sqrt *= -1
    if abs(det_sqrt.real) < 1e-12 and det_sqrt.imag < 0:
        det_sqrt *= -1

    coeffs: list[complex] = []
    indices = range(len(lambdas))
    for size in range(len(lambdas) + 1):
        for subset in combinations(indices, size):
            coeff = det_sqrt
            for idx in subset:
                coeff /= lambdas[idx]
            coeffs.append(coeff)
    return coeffs


def positive_form_coefficients(lambdas: list[complex]) -> bool:
    return all(coeff.real > 1e-12 for coeff in subset_coefficients(lambdas))


def check_basic_signatures() -> None:
    euclidean = [1, 2, 3, 4]
    lorentzian = [-1, 1, 1, 1]
    eps = 0.1
    regulated_plus = [-(1 - 1j * eps), 1, 1, 1]
    regulated_minus = [-(1 + 1j * eps), 1, 1, 1]
    two_time = [-(1 - 1j * eps), -(1 - 1j * eps), 1, 1]

    assert_true("Euclidean metric is allowable", allowable_by_angles(euclidean))
    assert_true("Lorentzian boundary is not interior", not allowable_by_angles(lorentzian))
    assert_true("positive i-epsilon side is allowable", allowable_by_angles(regulated_plus))
    assert_true("negative i-epsilon side is allowable", allowable_by_angles(regulated_minus))
    assert_true("two-time signature remains outside", not allowable_by_angles(two_time))


def check_form_coefficients() -> None:
    examples = [
        [1, 1, 1, 1],
        [complex(1, 0.2), complex(2, -0.1), 3, 4],
        [-(1 - 0.1j), 1, 1, 1],
        [cmath.exp(0.2j), cmath.exp(-0.25j), cmath.exp(0.1j)],
    ]
    for lambdas in examples:
        assert_true(
            f"angle criterion agrees with q-form positivity for {lambdas}",
            allowable_by_angles(lambdas) == positive_form_coefficients(lambdas),
        )


def check_subset_angle_bound() -> None:
    lambdas = [cmath.exp(0.31j), cmath.exp(-0.27j), cmath.exp(0.19j)]
    assert_true("test metric is allowable", allowable_by_angles(lambdas))
    for coeff in subset_coefficients(lambdas):
        assert_true("subset coefficient has positive real part", coeff.real > 0)


def main() -> None:
    check_basic_signatures()
    check_form_coefficients()
    check_subset_angle_bound()
    print("All Kontsevich-Segal allowability checks passed.")


if __name__ == "__main__":
    main()
