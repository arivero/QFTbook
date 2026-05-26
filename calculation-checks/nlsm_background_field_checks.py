#!/usr/bin/env python3
"""Finite checks for NLSM background-field source bookkeeping."""

from __future__ import annotations

from fractions import Fraction


Vector = tuple[Fraction, Fraction]
Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def dot(left: Vector, right: Vector) -> Fraction:
    return left[0] * right[0] + left[1] * right[1]


def sub(left: Vector, right: Vector) -> Vector:
    return left[0] - right[0], left[1] - right[1]


def inverse_2x2(matrix: Matrix) -> Matrix:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        (matrix[1][1] / det, -matrix[0][1] / det),
        (-matrix[1][0] / det, matrix[0][0] / det),
    )


def gaussian_exponent(matrix: Matrix, linear: Vector, xi: Vector) -> Fraction:
    return -dot(xi, mat_vec(matrix, xi)) / 2 + dot(linear, xi)


def check_mean_zero_source_and_square_completion() -> None:
    fluctuation_operator: Matrix = (
        (Fraction(5), Fraction(2)),
        (Fraction(2), Fraction(3)),
    )
    first_variation: Vector = (Fraction(7, 3), Fraction(-5, 4))
    source: Vector = (Fraction(11, 6), Fraction(13, 10))
    linear = sub(source, first_variation)
    inverse = inverse_2x2(fluctuation_operator)
    mean = mat_vec(inverse, linear)

    assert_equal(
        "mean field is A inverse times source minus first variation",
        mat_vec(fluctuation_operator, mean),
        linear,
    )
    assert_equal(
        "mean vanishes when source equals first variation",
        mat_vec(inverse, sub(first_variation, first_variation)),
        (Fraction(0), Fraction(0)),
    )

    xi: Vector = (Fraction(3, 7), Fraction(-2, 5))
    shifted = sub(xi, mean)
    completed_square = (
        -dot(shifted, mat_vec(fluctuation_operator, shifted)) / 2
        + dot(linear, mean) / 2
    )
    assert_equal(
        "Gaussian square-completion sign",
        gaussian_exponent(fluctuation_operator, linear, xi),
        completed_square,
    )


def main() -> None:
    check_mean_zero_source_and_square_completion()
    print("All NLSM background-field source checks passed.")


if __name__ == "__main__":
    main()
