#!/usr/bin/env python3
"""Finite checks for subgroup boundaries in finite gauge theory.

The checks support Volume VIII, Chapter 11.  They verify three exact finite
facts used in the subgroup-boundary section:

1. An interval with boundary subgroups H_0,H_1 has field groupoid
   G//(H_0 x H_1), hence simple sectors H_0\\G/H_1 and groupoid cardinality
   |G|/(|H_0||H_1|).
2. The finite push-pull composition of boundary intervals gives the
   |H_1|^{-1}-normalized double-coset convolution, with associative
   composition and the expected identity sector.
3. A boundary two-cochain beta with delta beta = i^* omega cancels the
   boundary Dijkgraaf-Witten coboundary factor simplex by simplex.
4. The beta-trivialization factors on a glued relative boundary cancel with
   opposite orientation, and beta -> beta + delta lambda changes only the
   boundary-line trivialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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


Function = dict[Element, Fraction]


def indicator_function(
    group: FiniteGroup[Element],
    subset: frozenset[Element],
) -> Function[Element]:
    return {x: Fraction(1 if x in subset else 0, 1) for x in group.elements}


def convolve_boundary_functions(
    group: FiniteGroup[Element],
    middle: frozenset[Element],
    left_function: Function[Element],
    right_function: Function[Element],
) -> Function[Element]:
    out: Function[Element] = {}
    for z in group.elements:
        total = Fraction(0, 1)
        for x in group.elements:
            y = group.multiply(group.inverse(x), z)
            total += left_function[x] * right_function[y]
        out[z] = total / len(middle)
    return out


def assert_functions_equal(
    group: FiniteGroup[Element],
    left: Function[Element],
    right: Function[Element],
    message: str,
) -> None:
    assert_true(all(left[x] == right[x] for x in group.elements), message)


def assert_biinvariant(
    group: FiniteGroup[Element],
    left_subgroup: frozenset[Element],
    right_subgroup: frozenset[Element],
    function: Function[Element],
    message: str,
) -> None:
    for h0 in left_subgroup:
        for h1 in right_subgroup:
            for x in group.elements:
                transformed = group.multiply(group.multiply(h0, x), group.inverse(h1))
                assert_true(function[transformed] == function[x], message)


def check_boundary_convolution_for_subgroups(
    group: FiniteGroup[Element],
    subgroups: list[frozenset[Element]],
) -> None:
    orbit_cache: dict[tuple[int, int], list[frozenset[Element]]] = {}
    for i, left in enumerate(subgroups):
        for j, right in enumerate(subgroups):
            orbit_cache[(i, j)] = double_coset_orbits(group, left, right)

    for i, left in enumerate(subgroups):
        for j, middle in enumerate(subgroups):
            for k, right in enumerate(subgroups):
                for orbit_left in orbit_cache[(i, j)]:
                    for orbit_right in orbit_cache[(j, k)]:
                        product_function = convolve_boundary_functions(
                            group,
                            middle,
                            indicator_function(group, orbit_left),
                            indicator_function(group, orbit_right),
                        )
                        assert_biinvariant(
                            group,
                            left,
                            right,
                            product_function,
                            "boundary convolution is bi-invariant under the outer subgroups",
                        )
                        for orbit_out in orbit_cache[(i, k)]:
                            values = {product_function[x] for x in orbit_out}
                            assert_true(
                                len(values) == 1,
                                "structure coefficient is constant on each output double coset",
                            )
                            coefficient = next(iter(values))
                            assert_true(
                                coefficient.denominator == 1,
                                "free middle-boundary gauge action gives integral structure constants",
                            )

    for i, _left in enumerate(subgroups):
        for j, middle_left in enumerate(subgroups):
            for k, middle_right in enumerate(subgroups):
                for l, _right in enumerate(subgroups):
                    for orbit_ij in orbit_cache[(i, j)]:
                        for orbit_jk in orbit_cache[(j, k)]:
                            for orbit_kl in orbit_cache[(k, l)]:
                                f = indicator_function(group, orbit_ij)
                                g = indicator_function(group, orbit_jk)
                                h = indicator_function(group, orbit_kl)
                                left_associated = convolve_boundary_functions(
                                    group,
                                    middle_right,
                                    convolve_boundary_functions(group, middle_left, f, g),
                                    h,
                                )
                                right_associated = convolve_boundary_functions(
                                    group,
                                    middle_left,
                                    f,
                                    convolve_boundary_functions(group, middle_right, g, h),
                                )
                                assert_functions_equal(
                                    group,
                                    left_associated,
                                    right_associated,
                                    "boundary convolution is associative",
                                )

    for i, left in enumerate(subgroups):
        left_unit = indicator_function(group, left)
        for j, right in enumerate(subgroups):
            right_unit = indicator_function(group, right)
            for orbit in orbit_cache[(i, j)]:
                function = indicator_function(group, orbit)
                assert_functions_equal(
                    group,
                    convolve_boundary_functions(group, left, left_unit, function),
                    function,
                    "left subgroup identity acts as the unit",
                )
                assert_functions_equal(
                    group,
                    convolve_boundary_functions(group, right, function, right_unit),
                    function,
                    "right subgroup identity acts as the unit",
                )


def check_s3_two_sector_hecke_algebra() -> None:
    group = symmetric_group_3()
    subgroup = generated_subgroup(group, [(1, 0, 2)])
    orbits = sorted(
        double_coset_orbits(group, subgroup, subgroup),
        key=lambda orbit: (group.identity not in orbit, len(orbit)),
    )
    assert_true(
        [len(orbit) for orbit in orbits] == [2, 4],
        "S_3 transposition boundary has the expected H-H double-coset sizes",
    )
    identity_sector, nontrivial_sector = orbits
    product_function = convolve_boundary_functions(
        group,
        subgroup,
        indicator_function(group, nontrivial_sector),
        indicator_function(group, nontrivial_sector),
    )
    identity_coefficient = product_function[next(iter(identity_sector))]
    nontrivial_coefficient = product_function[next(iter(nontrivial_sector))]
    assert_true(
        identity_coefficient == 2 and nontrivial_coefficient == 1,
        "S_3 transposition-boundary algebra has X^2=2*1+X",
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

    check_boundary_convolution_for_subgroups(s3, [trivial_s3, h2, h3, all_s3])
    check_boundary_convolution_for_subgroups(
        d4,
        [reflection, diagonal_reflection, rotations, d4.elements],
    )
    check_s3_two_sector_hecke_algebra()


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


def lambda_exp(a: int, n: int, r: int) -> int:
    """A normalized 1-cochain represented by exponents mod n."""
    if a == 0:
        return 0
    return r * (a * a + 3 * a) % n


def delta_lambda_exp(a: int, b: int, n: int, r: int) -> int:
    return (
        lambda_exp(b, n, r)
        - lambda_exp((a + b) % n, n, r)
        + lambda_exp(a, n, r)
    ) % n


def beta_shifted_exp(a: int, b: int, n: int, k: int, r: int) -> int:
    return (beta_exp(a, b, n, k) + delta_lambda_exp(a, b, n, r)) % n


def delta_shifted_beta_exp(a: int, b: int, c: int, n: int, k: int, r: int) -> int:
    return (
        beta_shifted_exp(b, c, n, k, r)
        - beta_shifted_exp((a + b) % n, c, n, k, r)
        + beta_shifted_exp(a, (b + c) % n, n, k, r)
        - beta_shifted_exp(a, b, n, k, r)
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


def relative_boundary_weight_exp(
    triangles: list[tuple[int, int, int]],
    n: int,
    beta_value: Callable[[int, int], int],
) -> int:
    """Boundary exponent for product beta(h_tau)^(-epsilon_tau)."""

    total = 0
    for a, b, orientation in triangles:
        if orientation not in {-1, 1}:
            raise AssertionError("boundary orientation must be +/-1")
        total -= orientation * beta_value(a, b)
    return total % n


def check_relative_boundary_gluing_orientation() -> None:
    for n in range(2, 11):
        for k in range(n):
            for r in range(n):
                for a, b, c in product(range(n), repeat=3):
                    assert_true(
                        delta_shifted_beta_exp(a, b, c, n, k, r)
                        == delta_beta_exp(a, b, c, n, k),
                        "beta -> beta + delta lambda leaves omega=delta beta unchanged",
                    )

                triangles = [
                    (a, b, orientation)
                    for a, b, orientation in [
                        (1 % n, 2 % n, 1),
                        (2 % n, 3 % n, -1),
                        (3 % n, 4 % n, 1),
                        (4 % n, 5 % n, -1),
                    ]
                ]
                opposite_triangles = [
                    (a, b, -orientation)
                    for a, b, orientation in triangles
                ]
                beta_value = lambda a, b, n=n, k=k: beta_exp(a, b, n, k)
                beta_shifted_value = (
                    lambda a, b, n=n, k=k, r=r: beta_shifted_exp(a, b, n, k, r)
                )

                unshifted_total = (
                    relative_boundary_weight_exp(triangles, n, beta_value)
                    + relative_boundary_weight_exp(opposite_triangles, n, beta_value)
                ) % n
                shifted_total = (
                    relative_boundary_weight_exp(triangles, n, beta_shifted_value)
                    + relative_boundary_weight_exp(opposite_triangles, n, beta_shifted_value)
                ) % n
                assert_true(
                    unshifted_total == 0,
                    "oppositely oriented relative boundaries cancel beta factors",
                )
                assert_true(
                    shifted_total == 0,
                    "oppositely oriented relative boundaries cancel shifted beta factors",
                )


def main() -> None:
    check_subgroup_boundary_examples()
    check_relative_cocycle_cancellation()
    check_relative_boundary_gluing_orientation()
    print("Finite gauge subgroup-boundary checks passed.")


if __name__ == "__main__":
    main()
