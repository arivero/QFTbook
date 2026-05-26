#!/usr/bin/env python3
"""Exact Ising modular-data checks for the VOA/modular-sewing chapter."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Qsqrt2:
    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __sub__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational - other.rational, self.sqrt2 - other.sqrt2)

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.rational, -self.sqrt2)

    def __mul__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )

    def inverse(self) -> Qsqrt2:
        denominator = self.rational * self.rational - 2 * self.sqrt2 * self.sqrt2
        if denominator == 0:
            raise ZeroDivisionError(self)
        return Qsqrt2(self.rational / denominator, -self.sqrt2 / denominator)

    def __truediv__(self, other: Qsqrt2) -> Qsqrt2:
        return self * other.inverse()


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
SQRT2 = Qsqrt2(Fraction(0), Fraction(1))
HALF = Qsqrt2(Fraction(1, 2))


LABELS = ("1", "sigma", "epsilon")

S = [
    [HALF, Qsqrt2(Fraction(0), Fraction(1, 2)), HALF],
    [Qsqrt2(Fraction(0), Fraction(1, 2)), ZERO, Qsqrt2(Fraction(0), Fraction(-1, 2))],
    [HALF, Qsqrt2(Fraction(0), Fraction(-1, 2)), HALF],
]

EXPECTED_FUSION = {
    ("1", "1"): {"1": 1},
    ("1", "sigma"): {"sigma": 1},
    ("1", "epsilon"): {"epsilon": 1},
    ("sigma", "sigma"): {"1": 1, "epsilon": 1},
    ("sigma", "epsilon"): {"sigma": 1},
    ("epsilon", "epsilon"): {"1": 1},
}


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def matrix_multiply(lhs: list[list[Qsqrt2]], rhs: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    size = len(lhs)
    return [
        [
            sum((lhs[i][k] * rhs[k][j] for k in range(size)), ZERO)
            for j in range(size)
        ]
        for i in range(size)
    ]


def check_s_squared_identity() -> None:
    product = matrix_multiply(S, S)
    identity = [
        [ONE if i == j else ZERO for j in range(3)]
        for i in range(3)
    ]
    assert_equal("Ising S^2", product, identity)


def verlinde(a: int, b: int, c: int) -> Qsqrt2:
    total = ZERO
    for m in range(3):
        total += S[a][m] * S[b][m] * S[c][m] / S[0][m]
    return total


def check_verlinde_fusion() -> None:
    for i, left in enumerate(LABELS):
        for j, right in enumerate(LABELS):
            key = tuple(sorted((left, right), key=LABELS.index))
            expected = EXPECTED_FUSION[key]
            for k, target in enumerate(LABELS):
                coefficient = verlinde(i, j, k)
                expected_value = Qsqrt2(Fraction(expected.get(target, 0)))
                assert_equal(f"Verlinde {left} x {right} -> {target}", coefficient, expected_value)


def check_quantum_dimensions() -> None:
    dimensions = [S[i][0] / S[0][0] for i in range(3)]
    assert_equal("vacuum quantum dimension", dimensions[0], ONE)
    assert_equal("sigma quantum dimension", dimensions[1], SQRT2)
    assert_equal("epsilon quantum dimension", dimensions[2], ONE)
    global_dimension_squared = sum((d * d for d in dimensions), ZERO)
    assert_equal("Ising global dimension squared", global_dimension_squared, Qsqrt2(Fraction(4)))


def check_character_exponents() -> None:
    central_charge = Fraction(1, 2)
    weights = {
        "1": Fraction(0),
        "sigma": Fraction(1, 16),
        "epsilon": Fraction(1, 2),
    }
    shifted = {
        label: weight - central_charge / 24
        for label, weight in weights.items()
    }
    assert_equal("vacuum shifted exponent", shifted["1"], Fraction(-1, 48))
    assert_equal("sigma shifted exponent", shifted["sigma"], Fraction(1, 24))
    assert_equal("epsilon shifted exponent", shifted["epsilon"], Fraction(23, 48))


def main() -> None:
    check_s_squared_identity()
    check_verlinde_fusion()
    check_quantum_dimensions()
    check_character_exponents()
    print("All CFT VOA/modular-data checks passed.")


if __name__ == "__main__":
    main()
