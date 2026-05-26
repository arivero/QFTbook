#!/usr/bin/env python3
r"""Finite checks for the soft-drop IRC classification.

The checks encode the elementary collinear counterexample for mMDT
(\(\beta_{\rm SD}=0\)) and the contrasting \(\beta_{\rm SD}>0\) threshold
behavior used in the jet-substructure chapter.
"""

from __future__ import annotations

from fractions import Fraction


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


def main() -> None:
    check_beta_zero_four_momentum_counterexample()
    check_positive_beta_collinear_limit()
    print("All soft-drop IRC classification checks passed.")


if __name__ == "__main__":
    main()
