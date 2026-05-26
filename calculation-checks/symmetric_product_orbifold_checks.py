#!/usr/bin/env python3
"""Finite checks for the symmetric-product orbifold section."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import factorial


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def centralizer_order(cycle_lengths: list[int]) -> int:
    counts = Counter(cycle_lengths)
    result = 1
    for length, multiplicity in counts.items():
        result *= (length**multiplicity) * factorial(multiplicity)
    return result


def symmetric_group_order(n: int) -> int:
    return factorial(n)


def twist_weight(c_seed: Fraction, length: int) -> Fraction:
    return c_seed * Fraction(length * length - 1, 24 * length)


def cycle_type_weight(c_seed: Fraction, cycle_lengths: list[int]) -> Fraction:
    return sum(twist_weight(c_seed, length) for length in cycle_lengths)


def check_centralizer_orders() -> None:
    assert_equal("S3 transposition centralizer", centralizer_order([2, 1]), 2)
    assert_equal("S3 three-cycle centralizer", centralizer_order([3]), 3)
    assert_equal("S4 double-transposition centralizer", centralizer_order([2, 2]), 8)

    n = 4
    class_sizes = [
        symmetric_group_order(n) // centralizer_order(cycles)
        for cycles in ([1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4])
    ]
    assert_equal("S4 conjugacy classes exhaust group", sum(class_sizes), symmetric_group_order(n))


def check_central_charge_and_weights() -> None:
    c_seed = Fraction(6, 1)
    assert_equal("Sym^5 central charge", 5 * c_seed, Fraction(30, 1))
    assert_equal("length-two c=6 twist weight", twist_weight(c_seed, 2), Fraction(3, 8))
    assert_equal("length-three c=6 twist weight", twist_weight(c_seed, 3), Fraction(2, 3))
    assert_equal(
        "cycle type (3)(2) c=6 weight",
        cycle_type_weight(c_seed, [3, 2]),
        Fraction(25, 24),
    )


def check_join_weight_shift() -> None:
    c_seed = Fraction(6, 1)
    shift_1_1_to_2 = twist_weight(c_seed, 2) - 2 * twist_weight(c_seed, 1)
    assert_equal("join two fixed points to a transposition", shift_1_1_to_2, Fraction(3, 8))

    shift_2_1_to_3 = twist_weight(c_seed, 3) - twist_weight(c_seed, 2)
    assert_equal("join length two and one to length three", shift_2_1_to_3, Fraction(7, 24))


def check_normalized_two_cycle_count() -> None:
    n = 6
    transpositions = n * (n - 1) // 2
    assert_equal("number of transpositions in S6", transpositions, 15)
    # The normalization 1/sqrt(number of transpositions) gives unit two-point
    # function when individual transposition twists are orthonormal.
    assert_equal("two-cycle normalization denominator squared", transpositions, 15)


def main() -> None:
    check_centralizer_orders()
    check_central_charge_and_weights()
    check_join_weight_shift()
    check_normalized_two_cycle_count()
    print("All symmetric-product orbifold checks passed.")


if __name__ == "__main__":
    main()
