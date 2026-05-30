#!/usr/bin/env python3
"""Finite checks for the pointed Walker-Wang boundary mechanism."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Charge = tuple[int, int]


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


def main() -> None:
    check_toric_code_radical_is_trivial()
    check_symmetric_z2_radical_is_all()
    check_cyclic_nondegenerate_examples()
    check_boundary_fusion_group_law()
    print("Pointed Walker-Wang boundary mechanism checks passed.")


if __name__ == "__main__":
    main()
