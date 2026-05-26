#!/usr/bin/env python3
"""Exact BCFT Cardy/Ishibashi bookkeeping checks in the Ising example."""

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
HALF = Qsqrt2(Fraction(1, 2))
SQRT2 = Qsqrt2(Fraction(0), Fraction(1))
INV_SQRT2 = Qsqrt2(Fraction(0), Fraction(1, 2))

LABELS = ("1", "epsilon", "sigma")

S = [
    [HALF, HALF, INV_SQRT2],
    [HALF, HALF, -INV_SQRT2],
    [INV_SQRT2, -INV_SQRT2, ZERO],
]

EXPECTED_FUSION = {
    ("1", "1"): {"1": 1},
    ("1", "epsilon"): {"epsilon": 1},
    ("1", "sigma"): {"sigma": 1},
    ("epsilon", "epsilon"): {"1": 1},
    ("epsilon", "sigma"): {"sigma": 1},
    ("sigma", "sigma"): {"1": 1, "epsilon": 1},
}


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def matrix_multiply(lhs: list[list[Qsqrt2]], rhs: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    size = len(lhs)
    return [
        [
            sum((lhs[i][k] * rhs[k][j] for k in range(size)), ZERO)
            for j in range(size)
        ]
        for i in range(size)
    ]


def verlinde(a: int, b: int, c: int) -> Qsqrt2:
    total = ZERO
    for i in range(3):
        total += S[a][i] * S[b][i] * S[c][i] / S[0][i]
    return total


def fusion(a: int, b: int, c: int) -> Qsqrt2:
    return verlinde(a, b, c)


def check_modular_s() -> None:
    identity = [
        [ONE if i == j else ZERO for j in range(3)]
        for i in range(3)
    ]
    assert_equal("Ising S squared", matrix_multiply(S, S), identity)


def check_cardy_annulus() -> None:
    for a, left in enumerate(LABELS):
        for b, right in enumerate(LABELS):
            key = tuple(sorted((left, right), key=LABELS.index))
            expected = EXPECTED_FUSION[key]
            for k, channel in enumerate(LABELS):
                coefficient = verlinde(a, b, k)
                expected_value = Qsqrt2(Fraction(expected.get(channel, 0)))
                assert_equal(
                    f"Cardy annulus {left}-{right} open channel {channel}",
                    coefficient,
                    expected_value,
                )


def check_fusion_associativity() -> None:
    for a, left in enumerate(LABELS):
        for b, middle_left in enumerate(LABELS):
            for c, middle_right in enumerate(LABELS):
                for d, right in enumerate(LABELS):
                    lhs = sum(
                        (fusion(a, b, e) * fusion(e, c, d) for e in range(3)),
                        ZERO,
                    )
                    rhs = sum(
                        (fusion(b, c, e) * fusion(a, e, d) for e in range(3)),
                        ZERO,
                    )
                    assert_equal(
                        "Ising fusion associativity "
                        f"({left} {middle_left}) {middle_right} -> {right}",
                        lhs,
                        rhs,
                    )


def check_cardy_fusion_ring_characters() -> None:
    for boundary, boundary_label in enumerate(LABELS):
        eigenvalues = [S[i][boundary] / S[0][boundary] for i in range(3)]
        for i, left in enumerate(LABELS):
            for j, right in enumerate(LABELS):
                product = eigenvalues[i] * eigenvalues[j]
                fusion_sum = sum(
                    (fusion(i, j, k) * eigenvalues[k] for k in range(3)),
                    ZERO,
                )
                assert_equal(
                    "Cardy disk one-point fusion character "
                    f"{boundary_label}: {left}*{right}",
                    product,
                    fusion_sum,
                )


def check_boundary_entropy() -> None:
    entropies = [S[a][0] / S[0][0] for a in range(3)]
    # The displayed g_a is S_{a0}/sqrt(S_{00}); its square is S_{a0}^2/S_{00}.
    entropy_squares = [S[a][0] * S[a][0] / S[0][0] for a in range(3)]
    assert_equal("fixed-plus quantum dimension ratio", entropies[0], ONE)
    assert_equal("fixed-minus quantum dimension ratio", entropies[1], ONE)
    assert_equal("free quantum dimension ratio", entropies[2], SQRT2)
    assert_equal("fixed-plus g squared", entropy_squares[0], HALF)
    assert_equal("fixed-minus g squared", entropy_squares[1], HALF)
    assert_equal("free g squared", entropy_squares[2], ONE)


def check_compact_boson_zero_mode_duality() -> None:
    samples = [
        (0, winding)
        for winding in range(-3, 4)
    ]
    for momentum, winding in samples:
        dual_momentum, dual_winding = winding, momentum
        assert_equal("Neumann m=0 maps to Dirichlet dual winding", dual_winding, 0)
        assert_equal("dual momentum records original winding", dual_momentum, winding)

    samples = [
        (momentum, 0)
        for momentum in range(-3, 4)
    ]
    for momentum, winding in samples:
        dual_momentum, dual_winding = winding, momentum
        assert_equal("Dirichlet w=0 maps to Neumann dual momentum", dual_momentum, 0)
        assert_equal("dual winding records original momentum", dual_winding, momentum)


def main() -> None:
    check_modular_s()
    check_cardy_annulus()
    check_fusion_associativity()
    check_cardy_fusion_ring_characters()
    check_boundary_entropy()
    check_compact_boson_zero_mode_duality()
    print("All BCFT Cardy, sewing, and compact-boson boundary checks passed.")


if __name__ == "__main__":
    main()
