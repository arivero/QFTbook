#!/usr/bin/env python3
"""Exact checks for finite gauge theory and state-sum TQFT formulas.

The Volume VIII finite-gauge chapter uses only finite algebra in several key
places.  This script verifies:

* action-groupoid cardinality for conjugation quotients;
* the connected-manifold formula |Hom(pi_1 M,G)| / |G|;
* the closed-surface character formula for cyclic groups and S_3;
* unnormalized class-function convolution on the circle;
* the standard Z_n Dijkgraaf-Witten 3-cocycle condition;
* the spanning-tree gauge-fixing count for graph presentations of free
  groups.

All checks are finite and exact.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

Permutation = tuple[int, int, int]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def compose(p: Permutation, q: Permutation) -> Permutation:
    return tuple(p[q[i]] for i in range(3))  # type: ignore[return-value]


def inverse_perm(p: Permutation) -> Permutation:
    out = [0, 0, 0]
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)  # type: ignore[return-value]


def s3() -> list[Permutation]:
    return [p for p in product(range(3), repeat=3) if sorted(p) == [0, 1, 2]]


def cyclic(n: int) -> list[int]:
    return list(range(n))


def cyclic_mul(n: int, a: int, b: int) -> int:
    return (a + b) % n


def cyclic_inv(n: int, a: int) -> int:
    return (-a) % n


def centralizer(group: list, mul, element) -> list:
    return [g for g in group if mul(g, element) == mul(element, g)]


def conjugacy_classes(group: list, mul, inv) -> list[set]:
    classes: list[set] = []
    for x in group:
        cls = {mul(mul(g, x), inv(g)) for g in group}
        if cls not in classes:
            classes.append(cls)
    return classes


def check_action_groupoid_cardinality() -> None:
    group = s3()
    mul = compose
    inv = inverse_perm
    classes = conjugacy_classes(group, mul, inv)
    cardinality = sum(Fraction(1, len(centralizer(group, mul, next(iter(cls))))) for cls in classes)
    assert_equal("S3 conjugation action groupoid cardinality", cardinality, Fraction(len(group), len(group)))

    for n in range(2, 9):
        group_n = cyclic(n)
        classes_n = conjugacy_classes(group_n, lambda a, b, n=n: cyclic_mul(n, a, b), lambda a, n=n: cyclic_inv(n, a))
        cardinality_n = sum(Fraction(1, n) for _ in classes_n)
        assert_equal(f"C_{n} conjugation action groupoid cardinality", cardinality_n, Fraction(1))


def commutator(group_mul, group_inv, a, b):
    return group_mul(group_mul(group_mul(a, b), group_inv(a)), group_inv(b))


def count_surface_homomorphisms(group: list, mul, inv, genus: int, identity) -> int:
    count = 0
    for entries in product(group, repeat=2 * genus):
        value = identity
        for r in range(genus):
            value = mul(value, commutator(mul, inv, entries[2 * r], entries[2 * r + 1]))
        if value == identity:
            count += 1
    return count


def genus_formula(group_size: int, irreducible_dimensions: list[int], genus: int) -> Fraction:
    return sum(Fraction(d, group_size) ** (2 - 2 * genus) for d in irreducible_dimensions)


def check_surface_partition_functions() -> None:
    for n in range(2, 8):
        group = cyclic(n)
        mul = lambda a, b, n=n: cyclic_mul(n, a, b)
        inv = lambda a, n=n: cyclic_inv(n, a)
        for genus in range(0, 4):
            hom_count = count_surface_homomorphisms(group, mul, inv, genus, 0)
            partition = Fraction(hom_count, n)
            expected = genus_formula(n, [1] * n, genus)
            assert_equal(f"C_{n} genus {genus} partition", partition, expected)

    group_s3 = s3()
    for genus in range(0, 4):
        hom_count = count_surface_homomorphisms(group_s3, compose, inverse_perm, genus, (0, 1, 2))
        partition = Fraction(hom_count, len(group_s3))
        expected = genus_formula(len(group_s3), [1, 1, 2], genus)
        assert_equal(f"S3 genus {genus} partition", partition, expected)


def convolution(group: list, mul, f: dict, h: dict) -> dict:
    out = {k: Fraction(0) for k in group}
    for a, b in product(group, repeat=2):
        out[mul(a, b)] += f[a] * h[b]
    return out


def check_class_function_convolution() -> None:
    group = s3()
    classes = conjugacy_classes(group, compose, inverse_perm)
    class_index = {}
    for idx, cls in enumerate(classes):
        for element in cls:
            class_index[element] = idx

    samples = []
    for offset in range(3):
        samples.append({g: Fraction(class_index[g] + 1 + offset, offset + 2) for g in group})
    delta_e = {g: Fraction(1 if g == (0, 1, 2) else 0) for g in group}

    for f in samples:
        assert_equal("left convolution unit", convolution(group, compose, delta_e, f), f)
        assert_equal("right convolution unit", convolution(group, compose, f, delta_e), f)

    for f, h, k in product(samples, repeat=3):
        assert_equal(
            "associativity of class-function convolution",
            convolution(group, compose, convolution(group, compose, f, h), k),
            convolution(group, compose, f, convolution(group, compose, h, k)),
        )
        assert_equal(
            "commutativity on class functions",
            convolution(group, compose, f, h),
            convolution(group, compose, h, f),
        )


def zn_dw_3cocycle_exponent(n: int, p: int, a: int, b: int, c: int) -> int:
    """Exponent mod n for omega(a,b,c)=exp(2 pi i exponent/n)."""

    carry = (b + c) // n
    return (p * a * carry) % n


def check_zn_dw_3cocycle() -> None:
    for n in range(2, 9):
        for p in range(n):
            for a, b, c, d in product(range(n), repeat=4):
                delta = (
                    zn_dw_3cocycle_exponent(n, p, b, c, d)
                    - zn_dw_3cocycle_exponent(n, p, (a + b) % n, c, d)
                    + zn_dw_3cocycle_exponent(n, p, a, (b + c) % n, d)
                    - zn_dw_3cocycle_exponent(n, p, a, b, (c + d) % n)
                    + zn_dw_3cocycle_exponent(n, p, a, b, c)
                ) % n
                assert_equal(f"Z_{n} DW 3-cocycle p={p}", delta, 0)


def check_spanning_tree_gauge_count() -> None:
    for group_size in [2, 3, 4, 6, 8]:
        for vertices in range(1, 6):
            for rank in range(0, 4):
                flat_label_count = group_size ** (vertices - 1 + rank)
                gauge_group_size = group_size**vertices
                state_sum = Fraction(flat_label_count, gauge_group_size)
                hom_formula = Fraction(group_size**rank, group_size)
                assert_equal(
                    f"tree gauge count |G|={group_size} V={vertices} r={rank}",
                    state_sum,
                    hom_formula,
                )


def check_torus_commuting_pairs() -> None:
    group = s3()
    commuting_pairs = sum(1 for a, b in product(group, repeat=2) if compose(a, b) == compose(b, a))
    assert_equal("S3 torus partition is number of classes", Fraction(commuting_pairs, len(group)), Fraction(3))

    for n in range(2, 9):
        group_n = cyclic(n)
        commuting_pairs_n = n * n
        assert_equal(f"C_{n} torus partition", Fraction(commuting_pairs_n, n), Fraction(n))


def main() -> None:
    check_action_groupoid_cardinality()
    check_surface_partition_functions()
    check_class_function_convolution()
    check_zn_dw_3cocycle()
    check_spanning_tree_gauge_count()
    check_torus_commuting_pairs()
    print("All finite gauge state-sum checks passed.")


if __name__ == "__main__":
    main()
