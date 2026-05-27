#!/usr/bin/env python3
"""Finite checks for the symmetric-product orbifold section."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
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


def nontrivial_cycle_lengths(permutation: tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    lengths: list[int] = []
    for point in range(len(permutation)):
        if point in seen:
            continue
        current = point
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        if length > 1:
            lengths.append(length)
    return sorted(lengths)


def all_cycles(degree: int, length: int) -> list[tuple[int, ...]]:
    cycles = []
    for support in combinations(range(degree), length):
        first = min(support)
        remaining = [point for point in support if point != first]
        for tail in permutations(remaining):
            cycles.append(cycle_permutation(degree, [first, *tail]))
    return cycles


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


def single_cycle_class_size(total_copies: int, length: int) -> int:
    return factorial(total_copies) // (length * factorial(total_copies - length))


def cycle_type_class_size(total_copies: int, nontrivial_lengths: list[int]) -> int:
    fixed_points = total_copies - sum(nontrivial_lengths)
    return symmetric_group_order(total_copies) // centralizer_order(
        [*nontrivial_lengths, *([1] * fixed_points)]
    )


def primitive_joining_factorization_count(left_length: int, right_length: int) -> int:
    joined_length = left_length + right_length - 1
    joined_cycle = cycle_permutation(joined_length, list(range(joined_length)))
    count = 0
    for left_cycle in all_cycles(joined_length, left_length):
        candidate_right = compose(inverse(left_cycle), joined_cycle)
        if nontrivial_cycle_lengths(candidate_right) == [right_length]:
            count += 1
    return count


def primitive_joining_group_factor_square(
    total_copies: int,
    left_length: int,
    right_length: int,
) -> Fraction:
    joined_length = left_length + right_length - 1
    return Fraction(
        joined_length * joined_length
        * single_cycle_class_size(total_copies, joined_length),
        single_cycle_class_size(total_copies, left_length)
        * single_cycle_class_size(total_copies, right_length),
    )


def transposition_join_factorization_count(cycle_length: int) -> int:
    joined_length = cycle_length + 1
    joined_cycle = cycle_permutation(joined_length, list(range(joined_length)))
    count = 0
    for transposition in all_cycles(joined_length, 2):
        candidate_cycle = compose(transposition, joined_cycle)
        expected_lengths = [cycle_length] if cycle_length > 1 else []
        if nontrivial_cycle_lengths(candidate_cycle) == expected_lengths:
            count += 1
    return count


def transposition_join_group_factor_square(total_copies: int, cycle_length: int) -> Fraction:
    joined_length = cycle_length + 1
    return Fraction(
        joined_length * joined_length
        * single_cycle_class_size(total_copies, joined_length),
        single_cycle_class_size(total_copies, 2)
        * single_cycle_class_size(total_copies, cycle_length),
    )


def transposition_split_factorization_count(
    total_copies: int,
    first_length: int,
    second_length: int,
) -> int:
    if first_length == 1 and second_length == 1:
        raise ValueError("the identity endpoint channel is not part of this finite check")

    if first_length == 1 or second_length == 1:
        nontrivial_length = max(first_length, second_length)
        output = cycle_permutation(total_copies, list(range(nontrivial_length)))
    else:
        output = compose(
            cycle_permutation(total_copies, list(range(first_length))),
            cycle_permutation(total_copies, list(range(first_length, first_length + second_length))),
        )

    joined_length = first_length + second_length
    count = 0
    for transposition in all_cycles(total_copies, 2):
        candidate_cycle = compose(transposition, output)
        if nontrivial_cycle_lengths(candidate_cycle) == [joined_length]:
            count += 1
    return count


def transposition_split_group_factor_square(
    total_copies: int,
    first_length: int,
    second_length: int,
) -> Fraction:
    joined_length = first_length + second_length
    if first_length == 1 or second_length == 1:
        output_lengths = [max(first_length, second_length)]
    else:
        output_lengths = [first_length, second_length]
    factorization_count = transposition_split_factorization_count(
        total_copies,
        first_length,
        second_length,
    )
    return Fraction(
        factorization_count * factorization_count
        * cycle_type_class_size(total_copies, output_lengths),
        single_cycle_class_size(total_copies, 2)
        * single_cycle_class_size(total_copies, joined_length),
    )


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


def check_conjugacy_class_joining_normalization() -> None:
    for total_copies in range(3, 10):
        for length in range(2, total_copies + 1):
            assert_equal(
                f"single-cycle class size S_{total_copies}, length={length}",
                single_cycle_class_size(total_copies, length),
                symmetric_group_order(total_copies) // centralizer_order(
                    [length, *([1] * (total_copies - length))]
                ),
            )

    for left_length in range(2, 6):
        for right_length in range(2, 6):
            joined_length = left_length + right_length - 1
            assert_equal(
                f"primitive joining factorizations K={left_length}, L={right_length}",
                primitive_joining_factorization_count(left_length, right_length),
                joined_length,
            )
            for total_copies in range(joined_length, joined_length + 5):
                expected_square = Fraction(
                    left_length
                    * right_length
                    * joined_length
                    * factorial(total_copies - left_length)
                    * factorial(total_copies - right_length),
                    factorial(total_copies) * factorial(total_copies - joined_length),
                )
                assert_equal(
                    f"class-normalized primitive joining factor K={left_length}, L={right_length}, M={total_copies}",
                    primitive_joining_group_factor_square(
                        total_copies,
                        left_length,
                        right_length,
                    ),
                    expected_square,
                )

    assert_equal(
        "S3 transposition-transposition to three-cycle group factor squared",
        primitive_joining_group_factor_square(3, 2, 2),
        Fraction(2, 1),
    )
    assert_equal(
        "S6 length-two/length-three to length-four group factor squared",
        primitive_joining_group_factor_square(6, 2, 3),
        Fraction(12, 5),
    )


def check_transposition_join_split_factors() -> None:
    for cycle_length in range(2, 8):
        assert_equal(
            f"transposition joins fixed point to length {cycle_length}",
            transposition_join_factorization_count(cycle_length),
            cycle_length + 1,
        )
        for total_copies in range(cycle_length + 1, cycle_length + 6):
            expected_square = Fraction(
                2 * cycle_length * (cycle_length + 1) * (total_copies - cycle_length),
                total_copies * (total_copies - 1),
            )
            assert_equal(
                f"transposition join group factor K={cycle_length}, M={total_copies}",
                transposition_join_group_factor_square(total_copies, cycle_length),
                expected_square,
            )

    for joined_length in range(4, 9):
        for first_length in range(2, joined_length - 1):
            second_length = joined_length - first_length
            for total_copies in range(joined_length, joined_length + 4):
                expected_count = first_length * second_length
                expected_square = Fraction(
                    2 * joined_length * first_length * second_length,
                    (1 if first_length != second_length else 2)
                    * total_copies
                    * (total_copies - 1),
                )
                assert_equal(
                    f"transposition split count a={first_length}, b={second_length}, M={total_copies}",
                    transposition_split_factorization_count(
                        total_copies,
                        first_length,
                        second_length,
                    ),
                    expected_count,
                )
                assert_equal(
                    f"transposition split group factor a={first_length}, b={second_length}, M={total_copies}",
                    transposition_split_group_factor_square(
                        total_copies,
                        first_length,
                        second_length,
                    ),
                    expected_square,
                )

    for joined_length in range(3, 9):
        nontrivial_length = joined_length - 1
        for total_copies in range(joined_length, joined_length + 5):
            expected_count = nontrivial_length * (total_copies - nontrivial_length)
            expected_square = Fraction(
                2 * joined_length * nontrivial_length * (total_copies - nontrivial_length),
                total_copies * (total_copies - 1),
            )
            assert_equal(
                f"endpoint split count b={nontrivial_length}, M={total_copies}",
                transposition_split_factorization_count(
                    total_copies,
                    1,
                    nontrivial_length,
                ),
                expected_count,
            )
            assert_equal(
                f"endpoint split group factor b={nontrivial_length}, M={total_copies}",
                transposition_split_group_factor_square(
                    total_copies,
                    1,
                    nontrivial_length,
                ),
                expected_square,
            )
            assert_equal(
                f"endpoint split equals adjoint join b={nontrivial_length}, M={total_copies}",
                transposition_split_group_factor_square(
                    total_copies,
                    1,
                    nontrivial_length,
                ),
                transposition_join_group_factor_square(total_copies, nontrivial_length),
            )


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
    check_conjugacy_class_joining_normalization()
    check_transposition_join_split_factors()
    check_connected_cover_hecke_count()
    check_twist_cover_riemann_hurwitz()
    check_primitive_joining_cover_polynomial()
    print("All symmetric-product orbifold checks passed.")


if __name__ == "__main__":
    main()
