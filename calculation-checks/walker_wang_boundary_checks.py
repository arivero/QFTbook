#!/usr/bin/env python3
"""Finite checks for the Walker-Wang boundary mechanism.

The chapter proves the pointed radical criterion and adds a non-pointed
Mueger-center test in the Ising modular category.  These checks are exact
finite convention checks for those displayed examples; they do not replace
the categorical state-sum theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Charge = tuple[int, int]


@dataclass(frozen=True)
class Qsqrt2:
    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __sub__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(self.rational - other.rational, self.sqrt2 - other.sqrt2)

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.rational, -self.sqrt2)

    def __mul__(self, other: "Qsqrt2") -> "Qsqrt2":
        return Qsqrt2(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )

    def scale(self, coeff: Fraction | int) -> "Qsqrt2":
        coeff = Fraction(coeff)
        return Qsqrt2(coeff * self.rational, coeff * self.sqrt2)


ZERO_Q2 = Qsqrt2()
ONE_Q2 = Qsqrt2(Fraction(1))
HALF_Q2 = Qsqrt2(Fraction(1, 2))
SQRT2_Q2 = Qsqrt2(Fraction(0), Fraction(1))
INV_SQRT2_Q2 = Qsqrt2(Fraction(0), Fraction(1, 2))


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def frac(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def toric_q(charge: Charge) -> Fraction:
    e, m = charge
    return Fraction((e % 2) * (m % 2), 2)


def toric_add(left: Charge, right: Charge) -> Charge:
    return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)


def polarize(q, add, a, x) -> Fraction:
    return frac(q(add(a, x)) - q(a) - q(x))


def radical(elements, q, add) -> list:
    out = []
    for a in elements:
        if all(polarize(q, add, a, x) == 0 for x in elements):
            out.append(a)
    return out


def check_toric_code_radical_is_trivial() -> None:
    elements = [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert_equal("toric b(e,m)", polarize(toric_q, toric_add, (1, 0), (0, 1)), Fraction(1, 2))
    assert_equal("toric b(e,e)", polarize(toric_q, toric_add, (1, 0), (1, 0)), Fraction(0))
    assert_equal("toric b(m,m)", polarize(toric_q, toric_add, (0, 1), (0, 1)), Fraction(0))
    assert_equal("toric radical", radical(elements, toric_q, toric_add), [(0, 0)])


def check_symmetric_z2_radical_is_all() -> None:
    elements = [0, 1]

    def add(a: int, b: int) -> int:
        return (a + b) % 2

    def q(_: int) -> Fraction:
        return Fraction(0)

    assert_equal("symmetric Z2 radical", radical(elements, q, add), elements)


def check_cyclic_nondegenerate_examples() -> None:
    for n in range(2, 15):
        elements = list(range(n))

        def add(a: int, b: int, n: int = n) -> int:
            return (a + b) % n

        for p in range(1, n):
            if gcd(p, n) != 1:
                continue

            def q(a: int, n: int = n, p: int = p) -> Fraction:
                return frac(Fraction(p * a * a, 2 * n))

            assert_equal(f"Z_{n} p={p} radical", radical(elements, q, add), [0])


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def check_boundary_fusion_group_law() -> None:
    elements = [(0, 0), (1, 0), (0, 1), (1, 1)]
    for a, b, c in product(elements, repeat=3):
        assert_equal("boundary fusion associativity", toric_add(toric_add(a, b), c), toric_add(a, toric_add(b, c)))
    for a in elements:
        assert_equal("boundary fusion identity", toric_add((0, 0), a), a)
        assert_equal("boundary fusion self inverse", toric_add(a, a), (0, 0))


def transparent_from_modular_s(s_matrix: list[list[Qsqrt2]], dimensions: list[Qsqrt2]) -> list[int]:
    transparent: list[int] = []
    for a, row in enumerate(s_matrix):
        # The expected normalized S-row is d_a d_x / D.  For the Ising
        # example D=2, so multiplication by 1/2 is exact in Q(sqrt(2)).
        expected = [(dimensions[a] * dimensions[x]).scale(Fraction(1, 2)) for x in range(len(dimensions))]
        if all(row[x] == expected[x] for x in range(len(dimensions))):
            transparent.append(a)
    return transparent


def check_ising_muger_center_is_trivial() -> None:
    # Ordered basis: 1, psi, sigma.
    ising_s = [
        [HALF_Q2, HALF_Q2, INV_SQRT2_Q2],
        [HALF_Q2, HALF_Q2, -INV_SQRT2_Q2],
        [INV_SQRT2_Q2, -INV_SQRT2_Q2, ZERO_Q2],
    ]
    dimensions = [ONE_Q2, ONE_Q2, SQRT2_Q2]
    transparent = transparent_from_modular_s(ising_s, dimensions)
    assert_equal("Ising transparent simples", transparent, [0])
    assert_equal(
        "Ising psi row fails at sigma",
        ising_s[1][2],
        -(dimensions[1] * dimensions[2]).scale(Fraction(1, 2)),
    )
    assert_equal(
        "Ising sigma row expected at psi",
        (dimensions[2] * dimensions[1]).scale(Fraction(1, 2)),
        INV_SQRT2_Q2,
    )


def main() -> None:
    check_toric_code_radical_is_trivial()
    check_symmetric_z2_radical_is_all()
    check_cyclic_nondegenerate_examples()
    check_boundary_fusion_group_law()
    check_ising_muger_center_is_trivial()
    print("Walker-Wang boundary mechanism checks passed.")


if __name__ == "__main__":
    main()
