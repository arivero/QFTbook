#!/usr/bin/env python3
"""Finite checks for Abelian finite-gauge boundary line condensation.

The checks support Volume VIII, Chapter 11.  They verify the finite algebra
of the untwisted three-dimensional Z_N gauge-theory line labels:
braiding, spin, electric/magnetic Lagrangian boundaries, endpoint absorption,
and the cylinder-sector count |C/(L_0+L_1)|=|L_0 cap L_1|.
"""

from __future__ import annotations


Line = tuple[int, int]  # (magnetic flux, electric character exponent)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def lines(n: int) -> set[Line]:
    return {(m, e) for m in range(n) for e in range(n)}


def add(x: Line, y: Line, n: int) -> Line:
    return ((x[0] + y[0]) % n, (x[1] + y[1]) % n)


def neg(x: Line, n: int) -> Line:
    return ((-x[0]) % n, (-x[1]) % n)


def braiding_exponent(x: Line, y: Line, n: int) -> int:
    return (x[1] * y[0] + y[1] * x[0]) % n


def spin_exponent(x: Line, n: int) -> int:
    return (x[0] * x[1]) % n


def electric_boundary(n: int) -> set[Line]:
    return {(0, e) for e in range(n)}


def magnetic_boundary(n: int) -> set[Line]:
    return {(m, 0) for m in range(n)}


def subgroup_sum(left: set[Line], right: set[Line], n: int) -> set[Line]:
    return {add(x, y, n) for x in left for y in right}


def orthogonal(subgroup: set[Line], n: int) -> set[Line]:
    return {
        x
        for x in lines(n)
        if all(braiding_exponent(x, y, n) == 0 for y in subgroup)
    }


def is_bosonic_lagrangian(subgroup: set[Line], n: int) -> bool:
    return (
        len(subgroup) == n
        and orthogonal(subgroup, n) == subgroup
        and all(spin_exponent(x, n) == 0 for x in subgroup)
    )


def quotient_size(total: set[Line], subgroup: set[Line]) -> int:
    assert_true(len(total) % len(subgroup) == 0, "subgroup cardinality divides total cardinality")
    return len(total) // len(subgroup)


def check_lagrangian_boundaries() -> None:
    for n in range(2, 15):
        electric = electric_boundary(n)
        magnetic = magnetic_boundary(n)
        assert_true(is_bosonic_lagrangian(electric, n), "electric boundary is bosonic Lagrangian")
        assert_true(is_bosonic_lagrangian(magnetic, n), "magnetic boundary is bosonic Lagrangian")
        for subgroup in [electric, magnetic]:
            for x in subgroup:
                for y in subgroup:
                    assert_true(
                        braiding_exponent(x, y, n) == 0,
                        "condensed lines have trivial mutual braiding",
                    )
                assert_true(spin_exponent(x, n) == 0, "condensed lines have trivial spin")


def check_non_bosonic_diagonal_is_rejected() -> None:
    for n in [2, 4, 6, 8, 10, 12]:
        diagonal = {(a, a) for a in range(n)}
        if orthogonal(diagonal, n) == diagonal:
            assert_true(
                not is_bosonic_lagrangian(diagonal, n),
                "diagonal subgroup with nontrivial spin is not a bosonic boundary",
            )


def check_cylinder_sector_count() -> None:
    for n in range(2, 15):
        total = lines(n)
        electric = electric_boundary(n)
        magnetic = magnetic_boundary(n)
        for left, right, expected in [
            (electric, electric, n),
            (magnetic, magnetic, n),
            (electric, magnetic, 1),
            (magnetic, electric, 1),
        ]:
            absorbed = subgroup_sum(left, right, n)
            intersection = left & right
            assert_true(
                quotient_size(total, absorbed) == len(intersection),
                "finite cylinder quotient size equals boundary intersection size",
            )
            assert_true(
                quotient_size(total, absorbed) == expected,
                "rough/smooth cylinder sector count has expected Z_N value",
            )


def check_endpoint_absorption_equivalence() -> None:
    for n in range(2, 10):
        total = lines(n)
        left = electric_boundary(n)
        right = magnetic_boundary(n)
        absorbed = subgroup_sum(left, right, n)
        assert_true(absorbed == total, "mixed electric/magnetic boundaries absorb every line")
        same_boundary_absorbed = subgroup_sum(left, left, n)
        coset_representatives = {(m, 0) for m in range(n)}
        for line in total:
            representative = (line[0], 0)
            assert_true(
                add(line, neg(representative, n), n) in same_boundary_absorbed,
                "same electric boundaries leave only magnetic flux modulo endpoint absorption",
            )
        assert_true(len(coset_representatives) == quotient_size(total, same_boundary_absorbed), "representatives match quotient size")


def main() -> None:
    check_lagrangian_boundaries()
    check_non_bosonic_diagonal_is_rejected()
    check_cylinder_sector_count()
    check_endpoint_absorption_equivalence()
    print("Finite gauge boundary line-condensation checks passed.")


if __name__ == "__main__":
    main()
