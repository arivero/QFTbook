#!/usr/bin/env python3
"""Finite checks for smooth-cutoff Wilsonian Gaussian pushforwards.

Volume II's Wilsonian chapter uses a smooth covariance split
``C_Lambda = C_Lambda' + C_hat``.  For smooth cutoffs the two summands can act
on the same Fourier mode, so the finite-regulator construction is a
product-space Gaussian followed by the addition map, not a direct mode-space
sum.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Sequence

Vector = Sequence[Fraction]
Matrix = Sequence[Sequence[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def quadratic_form(vector: Vector, matrix: Matrix) -> Fraction:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def pushforward_variance(addition_row: Vector, product_covariance: Matrix) -> Fraction:
    return quadratic_form(addition_row, product_covariance)


def diagonal(entries: Sequence[Fraction]) -> list[list[Fraction]]:
    return [
        [entry if row == col else Fraction(0) for col, _ in enumerate(entries)]
        for row, entry in enumerate(entries)
    ]


def check_one_mode_addition_pushforward() -> None:
    low_variance = Fraction(2, 5)
    shell_variance = Fraction(7, 10)
    total_variance = low_variance + shell_variance

    product_covariance = diagonal((low_variance, shell_variance))
    addition = (Fraction(1), Fraction(1))

    assert_equal(
        "addition-map covariance",
        pushforward_variance(addition, product_covariance),
        total_variance,
    )

    direct_sum_field_covariance = product_covariance
    assert_true(
        "direct sum is a two-coordinate field",
        len(direct_sum_field_covariance) != 1,
    )
    assert_equal(
        "first coordinate variance remains low variance",
        direct_sum_field_covariance[0][0],
        low_variance,
    )
    assert_true(
        "direct sum covariance is not the scalar total covariance",
        direct_sum_field_covariance != [[total_variance]],
    )


def check_smooth_transition_overlap() -> None:
    denominators = (Fraction(2), Fraction(5), Fraction(10))
    chi_lambda = (Fraction(1), Fraction(3, 4), Fraction(1, 4))
    chi_lambda_prime = (Fraction(1), Fraction(1, 4), Fraction(0))

    low_covariance = tuple(
        chi / denom for chi, denom in zip(chi_lambda_prime, denominators)
    )
    shell_covariance = tuple(
        (chi_hi - chi_lo) / denom
        for chi_hi, chi_lo, denom in zip(chi_lambda, chi_lambda_prime, denominators)
    )
    total_covariance = tuple(chi / denom for chi, denom in zip(chi_lambda, denominators))

    assert_equal(
        "covariance split per mode",
        tuple(low + shell for low, shell in zip(low_covariance, shell_covariance)),
        total_covariance,
    )
    transition_index = 1
    assert_true(
        "smooth transition has overlapping covariance summands",
        low_covariance[transition_index] > 0
        and shell_covariance[transition_index] > 0,
    )

    plateau_source = (Fraction(3), Fraction(0), Fraction(0))
    transition_source = (Fraction(0), Fraction(5), Fraction(0))
    shell_covariance_matrix = diagonal(shell_covariance)

    assert_equal(
        "plateau source annihilates shell covariance",
        quadratic_form(plateau_source, shell_covariance_matrix),
        Fraction(0),
    )
    assert_true(
        "transition source does not annihilate shell covariance",
        quadratic_form(transition_source, shell_covariance_matrix) > 0,
    )


def check_semidefinite_support_convention() -> None:
    shell_covariance = diagonal((Fraction(0), Fraction(1, 3)))
    null_source = (Fraction(4), Fraction(0))
    active_source = (Fraction(0), Fraction(4))

    assert_equal(
        "zero-variance shell direction is supported at zero",
        quadratic_form(null_source, shell_covariance),
        Fraction(0),
    )
    assert_equal(
        "positive shell range has finite variance",
        quadratic_form(active_source, shell_covariance),
        Fraction(16, 3),
    )


def main() -> None:
    check_one_mode_addition_pushforward()
    check_smooth_transition_overlap()
    check_semidefinite_support_convention()
    print("All Wilsonian smooth-cutoff pushforward checks passed.")


if __name__ == "__main__":
    main()
