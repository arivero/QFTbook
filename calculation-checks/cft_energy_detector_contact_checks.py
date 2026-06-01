#!/usr/bin/env python3
"""Exact finite checks for CFT energy-detector contact bookkeeping.

The checks model a finite positive calorimetric measure on the detector
sphere.  They verify the algebra behind the diagonal contact terms used in
the CFT light-ray/energy-correlator chapter.  The finite model is not a
substitute for the operator-valued-distribution construction; it fixes the
partition and moment bookkeeping that the continuum construction must
preserve.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Atom = tuple[Fraction, str]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def detector_value(atoms: list[Atom], values: list[Fraction]) -> Fraction:
    if len(atoms) != len(values):
        raise ValueError("one detector-test value is required for each atom")
    return sum(energy * value for (energy, _), value in zip(atoms, values))


def two_detector_product(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    return detector_value(atoms, f) * detector_value(atoms, g)


def two_detector_off_diagonal(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, (energy_i, _) in enumerate(atoms):
        for j, (energy_j, _) in enumerate(atoms):
            if i != j:
                total += energy_i * energy_j * f[i] * g[j]
    return total


def two_detector_diagonal(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    return sum(energy * energy * fi * gi for (energy, _), fi, gi in zip(atoms, f, g))


def set_partitions(items: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """Return all set partitions of the ordered tuple items."""

    if not items:
        return [()]
    first, *rest_list = items
    rest = tuple(rest_list)
    partitions: list[tuple[tuple[int, ...], ...]] = []
    for partition in set_partitions(rest):
        partitions.append(((first,),) + partition)
        for block_index, block in enumerate(partition):
            new_block = tuple(sorted((first,) + block))
            new_partition = list(partition)
            new_partition[block_index] = new_block
            partitions.append(tuple(sorted(new_partition)))
    unique: list[tuple[tuple[int, ...], ...]] = []
    for partition in partitions:
        normalized = tuple(sorted(tuple(block) for block in partition))
        if normalized not in unique:
            unique.append(normalized)
    return unique


def injective_block_assignments(num_atoms: int, num_blocks: int) -> list[tuple[int, ...]]:
    if num_blocks == 0:
        return [()]
    assignments: list[tuple[int, ...]] = []
    for combo in combinations(range(num_atoms), num_blocks):
        # Generate all permutations without importing itertools.permutations for
        # these tiny fixed checks.
        if num_blocks == 1:
            assignments.append(combo)
        elif num_blocks == 2:
            a, b = combo
            assignments.extend(((a, b), (b, a)))
        elif num_blocks == 3:
            a, b, c = combo
            assignments.extend(((a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)))
        else:
            raise ValueError("this finite check only uses up to three blocks")
    return assignments


def partition_decomposition(atoms: list[Atom], test_values: list[list[Fraction]]) -> Fraction:
    k = len(test_values)
    total = Fraction(0)
    for partition in set_partitions(tuple(range(k))):
        for assignment in injective_block_assignments(len(atoms), len(partition)):
            term = Fraction(1)
            for block, atom_index in zip(partition, assignment):
                energy = atoms[atom_index][0]
                term *= energy ** len(block)
                for detector_index in block:
                    term *= test_values[detector_index][atom_index]
            total += term
    return total


def check_two_detector_diagonal_split() -> None:
    atoms: list[Atom] = [(Fraction(2, 5), "n1"), (Fraction(1, 3), "n2"), (Fraction(4, 15), "n3")]
    f = [Fraction(1, 2), Fraction(-2, 3), Fraction(5, 7)]
    g = [Fraction(3, 11), Fraction(4, 9), Fraction(-1, 5)]
    full = two_detector_product(atoms, f, g)
    off_diagonal = two_detector_off_diagonal(atoms, f, g)
    diagonal = two_detector_diagonal(atoms, f, g)
    assert_equal("two-detector diagonal split", off_diagonal + diagonal, full)


def check_disjoint_support_removes_diagonal() -> None:
    atoms: list[Atom] = [(Fraction(1, 2), "north"), (Fraction(1, 4), "east"), (Fraction(1, 4), "south")]
    f = [Fraction(2), Fraction(0), Fraction(-3)]
    g = [Fraction(0), Fraction(5), Fraction(0)]
    assert_equal("pointwise disjoint tests have no diagonal", two_detector_diagonal(atoms, f, g), Fraction(0))
    assert_equal(
        "disjoint-support product equals off diagonal",
        two_detector_product(atoms, f, g),
        two_detector_off_diagonal(atoms, f, g),
    )


def check_total_energy_ward_identity() -> None:
    atoms: list[Atom] = [(Fraction(1, 6), "a"), (Fraction(1, 2), "b"), (Fraction(1, 3), "c")]
    ones = [Fraction(1)] * len(atoms)
    total_energy = detector_value(atoms, ones)
    assert_equal("normalized total energy", total_energy, Fraction(1))
    assert_equal("two-detector total energy square", two_detector_product(atoms, ones, ones), total_energy ** 2)
    assert_equal(
        "off diagonal plus contact gives total-energy square",
        two_detector_off_diagonal(atoms, ones, ones) + two_detector_diagonal(atoms, ones, ones),
        total_energy ** 2,
    )
    separated_only = two_detector_off_diagonal(atoms, ones, ones)
    contact = two_detector_diagonal(atoms, ones, ones)
    assert_equal("separated-only observable needs displayed contact", separated_only + contact, Fraction(1))


def check_three_detector_partition_decomposition() -> None:
    atoms: list[Atom] = [(Fraction(1, 5), "a"), (Fraction(3, 10), "b"), (Fraction(1, 2), "c")]
    tests = [
        [Fraction(2), Fraction(-1, 3), Fraction(4, 7)],
        [Fraction(5, 6), Fraction(3, 8), Fraction(-2)],
        [Fraction(-1, 4), Fraction(7, 9), Fraction(1, 11)],
    ]
    product = Fraction(1)
    for values in tests:
        product *= detector_value(atoms, values)
    assert_equal("three-detector partition decomposition", partition_decomposition(atoms, tests), product)


def main() -> None:
    check_two_detector_diagonal_split()
    check_disjoint_support_removes_diagonal()
    check_total_energy_ward_identity()
    check_three_detector_partition_decomposition()
    print("All CFT energy-detector contact checks passed.")


if __name__ == "__main__":
    main()
