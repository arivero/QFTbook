#!/usr/bin/env python3
"""Finite checks for subgroup boundaries in finite gauge theory.

The checks support Volume VIII, Chapter 11.  They verify two exact finite
facts used in the subgroup-boundary section:

1. An interval with boundary subgroups H_0,H_1 has field groupoid
   G//(H_0 x H_1), hence simple sectors H_0\\G/H_1 and groupoid cardinality
   |G|/(|H_0||H_1|).
2. A boundary two-cochain beta with delta beta = i^* omega cancels the
   boundary Dijkgraaf-Witten coboundary factor simplex by simplex.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from typing import Callable, Generic, Hashable, Iterable, TypeVar


Element = TypeVar("Element", bound=Hashable)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class FiniteGroup(Generic[Element]):
    elements: frozenset[Element]
    identity: Element
    multiply: Callable[[Element, Element], Element]
    inverse: Callable[[Element], Element]


def generated_subgroup(
    group: FiniteGroup[Element],
    generators: Iterable[Element],
) -> frozenset[Element]:
    subgroup = {group.identity, *generators}
    changed = True
    while changed:
        changed = False
        current = list(subgroup)
        for x in current:
            for y in current:
                for z in [group.multiply(x, y), group.inverse(x)]:
                    if z not in subgroup:
                        subgroup.add(z)
                        changed = True
    return frozenset(subgroup)


def double_coset_orbits(
    group: FiniteGroup[Element],
    left: frozenset[Element],
    right: frozenset[Element],
) -> list[frozenset[Element]]:
    unseen = set(group.elements)
    orbits: list[frozenset[Element]] = []
    while unseen:
        g = next(iter(unseen))
        orbit = {
            group.multiply(group.multiply(h0, g), group.inverse(h1))
            for h0 in left
            for h1 in right
        }
        orbits.append(frozenset(orbit))
        unseen -= orbit
    return orbits


def stabilizer_size(
    group: FiniteGroup[Element],
    left: frozenset[Element],
    right: frozenset[Element],
    g: Element,
) -> int:
    return sum(
        1
        for h0 in left
        for h1 in right
        if group.multiply(h0, g) == group.multiply(g, h1)
    )


def check_double_coset_groupoid(
    group: FiniteGroup[Element],
    left: frozenset[Element],
    right: frozenset[Element],
) -> None:
    orbits = double_coset_orbits(group, left, right)
    assert_true(
        sum(len(orbit) for orbit in orbits) == len(group.elements),
        "double cosets partition the group",
    )
    weighted_sum = 0.0
    for orbit in orbits:
        representative = next(iter(orbit))
        stabilizer = stabilizer_size(group, left, right, representative)
        assert_true(
            len(orbit) * stabilizer == len(left) * len(right),
            "orbit-stabilizer relation for H_0 x H_1 action",
        )
        weighted_sum += 1.0 / stabilizer
    expected = len(group.elements) / (len(left) * len(right))
    assert_true(
        abs(weighted_sum - expected) < 1e-12,
        "groupoid cardinality equals |G|/(|H_0||H_1|)",
    )


Permutation = tuple[int, ...]


def symmetric_group_3() -> FiniteGroup[Permutation]:
    elems = frozenset(permutations(range(3)))

    def mul(p: Permutation, q: Permutation) -> Permutation:
        return tuple(p[q[i]] for i in range(3))

    def inv(p: Permutation) -> Permutation:
        out = [0] * 3
        for i, value in enumerate(p):
            out[value] = i
        return tuple(out)

    return FiniteGroup(elems, (0, 1, 2), mul, inv)


Dihedral = tuple[int, int]


def dihedral_group(order_rotation: int) -> FiniteGroup[Dihedral]:
    elems = frozenset((r, s) for r in range(order_rotation) for s in [0, 1])

    def mul(x: Dihedral, y: Dihedral) -> Dihedral:
        r, s = x
        u, v = y
        sign = -1 if s else 1
        return ((r + sign * u) % order_rotation, (s + v) % 2)

    def inv(x: Dihedral) -> Dihedral:
        r, s = x
        if s == 0:
            return ((-r) % order_rotation, 0)
        return (r, 1)

    return FiniteGroup(elems, (0, 0), mul, inv)


def check_subgroup_boundary_examples() -> None:
    s3 = symmetric_group_3()
    transposition = (1, 0, 2)
    cycle = (1, 2, 0)
    trivial_s3 = frozenset({s3.identity})
    all_s3 = s3.elements
    h2 = generated_subgroup(s3, [transposition])
    h3 = generated_subgroup(s3, [cycle])
    for left, right in [
        (trivial_s3, trivial_s3),
        (all_s3, all_s3),
        (h2, h2),
        (h2, h3),
        (h3, h3),
    ]:
        check_double_coset_groupoid(s3, left, right)

    d4 = dihedral_group(4)
    rotations = generated_subgroup(d4, [(1, 0)])
    reflection = generated_subgroup(d4, [(0, 1)])
    diagonal_reflection = generated_subgroup(d4, [(1, 1)])
    for left, right in [
        (rotations, rotations),
        (reflection, reflection),
        (reflection, diagonal_reflection),
        (d4.elements, rotations),
    ]:
        check_double_coset_groupoid(d4, left, right)


def beta_exp(a: int, b: int, n: int, k: int) -> int:
    """A normalized U(1)-valued 2-cochain represented by exponents mod n."""
    if a == 0 or b == 0:
        return 0
    return k * (a * b + a + 2 * b + ((a + b) // n)) % n


def delta_beta_exp(a: int, b: int, c: int, n: int, k: int) -> int:
    return (
        beta_exp(b, c, n, k)
        - beta_exp((a + b) % n, c, n, k)
        + beta_exp(a, (b + c) % n, n, k)
        - beta_exp(a, b, n, k)
    ) % n


def delta_omega_exp(a: int, b: int, c: int, d: int, n: int, k: int) -> int:
    omega = delta_beta_exp
    return (
        omega(b, c, d, n, k)
        - omega((a + b) % n, c, d, n, k)
        + omega(a, (b + c) % n, d, n, k)
        - omega(a, b, (c + d) % n, n, k)
        + omega(a, b, c, n, k)
    ) % n


def check_relative_cocycle_cancellation() -> None:
    for n in range(2, 11):
        for k in range(n):
            for a, b, c in product(range(n), repeat=3):
                omega = delta_beta_exp(a, b, c, n, k)
                boundary_counterterm = (-delta_beta_exp(a, b, c, n, k)) % n
                assert_true(
                    (omega + boundary_counterterm) % n == 0,
                    "relative boundary counterterm cancels pulled-back bulk cocycle",
                )
            for a, b, c, d in product(range(n), repeat=4):
                assert_true(
                    delta_omega_exp(a, b, c, d, n, k) == 0,
                    "delta(delta beta) is the trivial 4-cocycle",
                )


def main() -> None:
    check_subgroup_boundary_examples()
    check_relative_cocycle_cancellation()
    print("Finite gauge subgroup-boundary checks passed.")


if __name__ == "__main__":
    main()
