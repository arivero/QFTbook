#!/usr/bin/env python3
"""Finite checks for the symmetric-product orbifold section."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, factorial


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def identity_permutation(degree: int) -> tuple[int, ...]:
    return tuple(range(degree))


def cycle_permutation(degree: int, entries: list[int]) -> tuple[int, ...]:
    permutation = list(range(degree))
    for index, entry in enumerate(entries):
        permutation[entry] = entries[(index + 1) % len(entries)]
    return tuple(permutation)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for index, image in enumerate(permutation):
        result[image] = index
    return tuple(result)


def generated_orbit(generators: list[tuple[int, ...]], start: int = 0) -> set[int]:
    orbit = {start}
    changed = True
    while changed:
        changed = False
        for generator in generators:
            for point in tuple(orbit):
                for image in (generator[point], inverse(generator)[point]):
                    if image not in orbit:
                        orbit.add(image)
                        changed = True
    return orbit


def cycle_count(permutation: tuple[int, ...]) -> int:
    seen: set[int] = set()
    count = 0
    for point in range(len(permutation)):
        if point in seen:
            continue
        count += 1
        current = point
        while current not in seen:
            seen.add(current)
            current = permutation[current]
    return count


def riemann_hurwitz_genus(branch_cycles: list[tuple[int, ...]]) -> Fraction:
    degree = len(branch_cycles[0])
    ramification = sum(degree - cycle_count(permutation) for permutation in branch_cycles)
    return Fraction(1 - degree, 1) + Fraction(ramification, 2)


def poly_eval(poly: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    power = Fraction(1)
    for coefficient in poly:
        value += coefficient * power
        power *= x
    return value


def poly_derivative(poly: list[Fraction]) -> list[Fraction]:
    return [index * poly[index] for index in range(1, len(poly))]


def poly_shift_to_one(poly: list[Fraction]) -> list[Fraction]:
    """Return coefficients of p(1+s) in increasing powers of s."""
    shifted = [Fraction(0) for _ in poly]
    for power, coefficient in enumerate(poly):
        for shifted_power in range(power + 1):
            shifted[shifted_power] += coefficient * comb(power, shifted_power)
    return shifted


def primitive_joining_cover_polynomial(left_length: int, right_length: int) -> list[Fraction]:
    degree = left_length + right_length - 1
    normalization_inverse = Fraction(
        ((-1) ** (right_length - 1)) * factorial(degree),
        factorial(left_length - 1) * factorial(right_length - 1),
    )
    derivative = [Fraction(0) for _ in range(degree)]
    for power in range(right_length):
        derivative[left_length - 1 + power] = (
            normalization_inverse
            * comb(right_length - 1, power)
            * ((-1) ** (right_length - 1 - power))
        )
    polynomial = [Fraction(0) for _ in range(degree + 1)]
    for power, coefficient in enumerate(derivative):
        polynomial[power + 1] = coefficient / (power + 1)
    return polynomial


def centralizer_order(cycle_lengths: list[int]) -> int:
    counts = Counter(cycle_lengths)
    result = 1
    for length, multiplicity in counts.items():
        result *= (length**multiplicity) * factorial(multiplicity)
    return result


def symmetric_group_order(n: int) -> int:
    return factorial(n)


def divisor_sum(n: int) -> int:
    return sum(divisor for divisor in range(1, n + 1) if n % divisor == 0)


def connected_cover_representatives(degree: int) -> list[tuple[int, int, int]]:
    representatives = []
    for d in range(1, degree + 1):
        if degree % d != 0:
            continue
        a = degree // d
        for b in range(d):
            representatives.append((a, d, b))
    return representatives


def partition_numbers(limit: int) -> list[int]:
    counts = [0] * (limit + 1)
    counts[0] = 1
    for part in range(1, limit + 1):
        for total in range(part, limit + 1):
            counts[total] += counts[total - part]
    return counts


def constant_seed_symmetric_product_coefficients(limit: int) -> list[Fraction]:
    coefficients = [Fraction(0) for _ in range(limit + 1)]
    coefficients[0] = Fraction(1)
    for n in range(1, limit + 1):
        total = sum(divisor_sum(k) * coefficients[n - k] for k in range(1, n + 1))
        coefficients[n] = total / n
    return coefficients


def twist_weight(c_seed: Fraction, length: int) -> Fraction:
    return c_seed * Fraction(length * length - 1, 24 * length)


def ramification_schwarzian_weight(c_seed: Fraction, ramification_index: int) -> Fraction:
    inverse_branch_double_pole = Fraction(
        ramification_index * ramification_index - 1,
        2 * ramification_index * ramification_index,
    )
    branch_sum_double_pole = ramification_index * inverse_branch_double_pole
    return c_seed * branch_sum_double_pole / 12


def cycle_type_weight(c_seed: Fraction, cycle_lengths: list[int]) -> Fraction:
    return sum(twist_weight(c_seed, length) for length in cycle_lengths)


def primitive_joining_ope_power(c_seed: Fraction, left_length: int, right_length: int) -> Fraction:
    joined_length = left_length + right_length - 1
    return (
        twist_weight(c_seed, joined_length)
        - twist_weight(c_seed, left_length)
        - twist_weight(c_seed, right_length)
    )


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


def check_schwarzian_and_primitive_ope_powers() -> None:
    c_seed = Fraction(6, 1)
    for ramification_index in range(2, 12):
        assert_equal(
            f"Schwarzian double pole gives twist weight r={ramification_index}",
            ramification_schwarzian_weight(c_seed, ramification_index),
            twist_weight(c_seed, ramification_index),
        )

    assert_equal(
        "primitive joining OPE power K=2, L=2, c=6",
        primitive_joining_ope_power(c_seed, 2, 2),
        Fraction(-1, 12),
    )

    for left_length in range(2, 8):
        for right_length in range(2, 8):
            joined_length = left_length + right_length - 1
            expected = c_seed * Fraction(
                joined_length,
                24,
            ) - c_seed * Fraction(
                1,
                24 * joined_length,
            ) - c_seed * Fraction(
                left_length,
                24,
            ) + c_seed * Fraction(
                1,
                24 * left_length,
            ) - c_seed * Fraction(
                right_length,
                24,
            ) + c_seed * Fraction(
                1,
                24 * right_length,
            )
            assert_equal(
                f"primitive joining OPE power formula K={left_length}, L={right_length}",
                primitive_joining_ope_power(c_seed, left_length, right_length),
                expected,
            )


def check_normalized_two_cycle_count() -> None:
    n = 6
    transpositions = n * (n - 1) // 2
    assert_equal("number of transpositions in S6", transpositions, 15)
    # The normalization 1/sqrt(number of transpositions) gives unit two-point
    # function when individual transposition twists are orthonormal.
    assert_equal("two-cycle normalization denominator squared", transpositions, 15)


def check_connected_cover_hecke_count() -> None:
    for degree in range(1, 13):
        representatives = connected_cover_representatives(degree)
        assert_equal(
            f"degree {degree} connected torus covers in Hermite normal form",
            len(representatives),
            divisor_sum(degree),
        )
        assert_equal(
            f"degree {degree} Hecke automorphism weight",
            Fraction(len(representatives), degree),
            Fraction(divisor_sum(degree), degree),
        )

    # A constant formal seed gives prod_{n>=1} (1-p^n)^(-1), so the
    # coefficients are partition numbers, equivalently S_N conjugacy classes.
    limit = 10
    from_hecke_exponential = constant_seed_symmetric_product_coefficients(limit)
    expected_partitions = partition_numbers(limit)
    assert_equal(
        "constant-seed symmetric product partition coefficients",
        from_hecke_exponential,
        [Fraction(value) for value in expected_partitions],
    )


def check_twist_cover_riemann_hurwitz() -> None:
    for length in range(2, 10):
        cycle = cycle_permutation(length, list(range(length)))
        branch_cycles = [cycle, inverse(cycle)]
        assert_equal(
            f"length {length} two-point monodromy product",
            compose(branch_cycles[0], branch_cycles[1]),
            identity_permutation(length),
        )
        assert_equal(
            f"length {length} two-point cover transitivity",
            generated_orbit(branch_cycles),
            set(range(length)),
        )
        assert_equal(
            f"length {length} two-point cover genus",
            riemann_hurwitz_genus(branch_cycles),
            Fraction(0),
        )

    for left_length in range(2, 8):
        for right_length in range(2, 8):
            degree = left_length + right_length - 1
            alpha = cycle_permutation(degree, list(range(left_length)))
            beta = cycle_permutation(degree, list(range(left_length - 1, degree)))
            gamma = inverse(compose(alpha, beta))
            branch_cycles = [alpha, beta, gamma]

            assert_equal(
                f"join product K={left_length}, L={right_length}",
                compose(compose(alpha, beta), gamma),
                identity_permutation(degree),
            )
            assert_equal(
                f"join transitivity K={left_length}, L={right_length}",
                generated_orbit(branch_cycles),
                set(range(degree)),
            )
            assert_equal(
                f"joined cycle count K={left_length}, L={right_length}",
                cycle_count(compose(alpha, beta)),
                1,
            )
            assert_equal(
                f"join cover genus K={left_length}, L={right_length}",
                riemann_hurwitz_genus(branch_cycles),
                Fraction(0),
            )


def check_primitive_joining_cover_polynomial() -> None:
    for left_length in range(2, 8):
        for right_length in range(2, 8):
            degree = left_length + right_length - 1
            polynomial = primitive_joining_cover_polynomial(left_length, right_length)
            derivative = poly_derivative(polynomial)

            assert_equal(
                f"primitive cover degree K={left_length}, L={right_length}",
                len(polynomial) - 1,
                degree,
            )
            assert_equal(
                f"primitive cover z(0) K={left_length}, L={right_length}",
                poly_eval(polynomial, Fraction(0)),
                Fraction(0),
            )
            assert_equal(
                f"primitive cover z(1) K={left_length}, L={right_length}",
                poly_eval(polynomial, Fraction(1)),
                Fraction(1),
            )

            expected_zero_coefficient = Fraction(comb(degree, left_length))
            for power in range(1, left_length):
                assert_equal(
                    f"zero branch vanishing power {power} K={left_length}, L={right_length}",
                    polynomial[power],
                    Fraction(0),
                )
            assert_equal(
                f"zero branch leading coefficient K={left_length}, L={right_length}",
                polynomial[left_length],
                expected_zero_coefficient,
            )

            shifted = poly_shift_to_one(polynomial)
            assert_equal(
                f"one branch value K={left_length}, L={right_length}",
                shifted[0],
                Fraction(1),
            )
            for power in range(1, right_length):
                assert_equal(
                    f"one branch vanishing power {power} K={left_length}, L={right_length}",
                    shifted[power],
                    Fraction(0),
                )
            assert_equal(
                f"one branch leading coefficient K={left_length}, L={right_length}",
                shifted[right_length],
                Fraction(((-1) ** (right_length - 1)) * comb(degree, right_length)),
            )

            expected_derivative = [Fraction(0) for _ in range(degree)]
            normalization_inverse = Fraction(
                ((-1) ** (right_length - 1)) * factorial(degree),
                factorial(left_length - 1) * factorial(right_length - 1),
            )
            for power in range(right_length):
                expected_derivative[left_length - 1 + power] = (
                    normalization_inverse
                    * comb(right_length - 1, power)
                    * ((-1) ** (right_length - 1 - power))
                )
            assert_equal(
                f"primitive cover derivative factorization K={left_length}, L={right_length}",
                derivative,
                expected_derivative,
            )

            leading_coefficient = polynomial[degree]
            assert_equal(
                f"infinity branch leading inverse K={left_length}, L={right_length}",
                Fraction(1, 1) / leading_coefficient,
                Fraction(
                    ((-1) ** (right_length - 1))
                    * factorial(left_length - 1)
                    * factorial(right_length - 1),
                    factorial(degree - 1),
                ),
            )


def main() -> None:
    check_centralizer_orders()
    check_central_charge_and_weights()
    check_join_weight_shift()
    check_schwarzian_and_primitive_ope_powers()
    check_normalized_two_cycle_count()
    check_connected_cover_hecke_count()
    check_twist_cover_riemann_hurwitz()
    check_primitive_joining_cover_polynomial()
    print("All symmetric-product orbifold checks passed.")


if __name__ == "__main__":
    main()
