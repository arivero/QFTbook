#!/usr/bin/env python3
r"""Finite checks for the soft-drop IRC classification and tree margins.

The checks encode the elementary collinear counterexample for mMDT
(\(\beta_{\rm SD}=0\)) and the contrasting \(\beta_{\rm SD}>0\) threshold
behavior used in the jet-substructure chapter.  They also exercise the
finite-tree decision-margin bookkeeping used to make "away from grooming
boundaries" precise.
"""

from __future__ import annotations

from fractions import Fraction
from typing import NamedTuple


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def soft_drop_passes(z: Fraction, z_cut: Fraction, theta_num: Fraction, beta: int) -> bool:
    """Return z > z_cut theta^beta for rational samples."""

    threshold = z_cut * (theta_num**beta)
    return z > threshold


def groomed_energy_fraction_two_branch(z_soft: Fraction, z_cut: Fraction, theta_num: Fraction, beta: int) -> Fraction:
    """Two collinear branches with total energy one and softer fraction z_soft."""

    if soft_drop_passes(z_soft, z_cut, theta_num, beta):
        return Fraction(1)
    return Fraction(1) - z_soft


class Split(NamedTuple):
    left: str
    right: str
    theta: Fraction


Tree = dict[str, Split]


def leaves_below(node: str, tree: Tree) -> tuple[str, ...]:
    if node not in tree:
        return (node,)
    split = tree[node]
    return leaves_below(split.left, tree) + leaves_below(split.right, tree)


def branch_energy(node: str, tree: Tree, leaf_energies: dict[str, Fraction]) -> Fraction:
    return sum(leaf_energies[leaf] for leaf in leaves_below(node, tree))


def soft_drop_retained_leaves(
    root: str,
    tree: Tree,
    leaf_energies: dict[str, Fraction],
    z_cut: Fraction,
    beta: int,
) -> tuple[str, ...]:
    node = root
    while node in tree:
        split = tree[node]
        left_energy = branch_energy(split.left, tree, leaf_energies)
        right_energy = branch_energy(split.right, tree, leaf_energies)
        total = left_energy + right_energy
        z = min(left_energy, right_energy) / total
        if soft_drop_passes(z, z_cut, split.theta, beta):
            return leaves_below(node, tree)
        node = split.left if left_energy > right_energy else split.right
    return (node,)


def decision_margin(
    node: str,
    tree: Tree,
    leaf_energies: dict[str, Fraction],
    z_cut: Fraction,
    beta: int,
) -> Fraction:
    split = tree[node]
    left_energy = branch_energy(split.left, tree, leaf_energies)
    right_energy = branch_energy(split.right, tree, leaf_energies)
    total = left_energy + right_energy
    z = min(left_energy, right_energy) / total
    return abs(z - z_cut * split.theta**beta)


def check_beta_zero_four_momentum_counterexample() -> None:
    z_cut = Fraction(1, 10)
    z_soft = Fraction(1, 20)
    theta = Fraction(1, 10**6)
    retained = groomed_energy_fraction_two_branch(z_soft, z_cut, theta, beta=0)
    assert_equal("mMDT groomed energy fraction after collinear split", retained, Fraction(19, 20))
    assert_true("mMDT groomed four-vector differs from parent", retained != Fraction(1))


def check_positive_beta_collinear_limit() -> None:
    z_cut = Fraction(1, 10)
    z_soft = Fraction(1, 20)
    theta = Fraction(1, 10**6)
    retained = groomed_energy_fraction_two_branch(z_soft, z_cut, theta, beta=1)
    assert_equal("positive-beta collinear pair retained", retained, Fraction(1))


def check_fixed_tree_decision_margins() -> None:
    tree: Tree = {
        "root": Split("A", "B", Fraction(1)),
        "A": Split("A1", "A2", Fraction(1, 5)),
    }
    z_cut = Fraction(1, 4)
    beta = 1

    base = {"A1": Fraction(60), "A2": Fraction(30), "B": Fraction(10)}
    assert_equal(
        "base retained leaves after failing root and passing A",
        soft_drop_retained_leaves("root", tree, base, z_cut, beta),
        ("A1", "A2"),
    )
    assert_equal("root decision margin", decision_margin("root", tree, base, z_cut, beta), Fraction(3, 20))
    assert_equal("A decision margin", decision_margin("A", tree, base, z_cut, beta), Fraction(17, 60))

    perturbed = {"A1": Fraction(61), "A2": Fraction(29), "B": Fraction(11)}
    assert_equal(
        "same retained leaves under a small off-boundary perturbation",
        soft_drop_retained_leaves("root", tree, perturbed, z_cut, beta),
        ("A1", "A2"),
    )

    boundary_crossing = {"A1": Fraction(60), "A2": Fraction(30), "B": Fraction(40)}
    assert_equal(
        "retained leaves change after crossing the root soft-drop boundary",
        soft_drop_retained_leaves("root", tree, boundary_crossing, z_cut, beta),
        ("A1", "A2", "B"),
    )


def main() -> None:
    check_beta_zero_four_momentum_counterexample()
    check_positive_beta_collinear_limit()
    check_fixed_tree_decision_margins()
    print("All soft-drop IRC classification checks passed.")


if __name__ == "__main__":
    main()
