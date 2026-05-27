#!/usr/bin/env python3
"""Exact checks for theta, susceptibility, and Witten-Veneziano normalizations."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{name}: got {simplified!r}, expected 0")


def check_finite_volume_cumulant_identity() -> None:
    theta = sp.symbols("theta")
    charges = [-2, -1, 0, 1, 3]
    weights = [sp.Rational(2, 7), sp.Rational(3, 5), sp.Rational(11, 13), sp.Rational(5, 17), sp.Rational(7, 19)]
    volume = sp.Rational(23, 3)

    partition = sum(weight * sp.exp(sp.I * theta * charge) for charge, weight in zip(charges, weights))
    energy = -sp.log(partition) / volume
    susceptibility_from_derivatives = sp.diff(energy, theta, 2).subs(theta, 0)

    normalization = sum(weights)
    mean = sum(weight * charge for charge, weight in zip(charges, weights)) / normalization
    second = sum(weight * charge * charge for charge, weight in zip(charges, weights)) / normalization
    susceptibility_from_cumulant = (second - mean * mean) / volume

    assert_zero(
        "finite-volume susceptibility cumulant",
        susceptibility_from_derivatives - susceptibility_from_cumulant,
    )


def check_cp_symmetric_first_moment() -> None:
    sector_weights = {
        -3: Fraction(5, 11),
        -2: Fraction(7, 13),
        -1: Fraction(2, 5),
        0: Fraction(17, 19),
        1: Fraction(2, 5),
        2: Fraction(7, 13),
        3: Fraction(5, 11),
    }
    total = sum(sector_weights.values(), Fraction(0))
    mean = sum(Fraction(charge) * weight for charge, weight in sector_weights.items()) / total
    require(mean == 0, "CP-symmetric theta weights should have zero first moment")


def check_witten_veneziano_mass_coefficient() -> None:
    eta, theta, chi, f = sp.symbols("eta theta chi f", positive=True)
    nf = sp.symbols("nf", positive=True, integer=True)

    determinant_phase = sp.sqrt(2 * nf) * eta / f
    potential = sp.Rational(1, 2) * chi * (theta - determinant_phase) ** 2
    mass_squared = sp.diff(potential.subs(theta, 0), eta, 2)
    assert_zero("Witten-Veneziano coefficient", mass_squared - 2 * nf * chi / f**2)


def check_massless_quark_theta_screening() -> None:
    eta, theta, chi, f = sp.symbols("eta theta chi f", positive=True)
    nf_value = sp.Integer(3)
    determinant_phase = sp.sqrt(2 * nf_value) * eta / f
    potential = sp.Rational(1, 2) * chi * (theta - determinant_phase) ** 2
    eta_at_minimum = theta * f / sp.sqrt(2 * nf_value)
    minimized = sp.simplify(potential.subs(eta, eta_at_minimum))
    assert_zero("massless theta screening", minimized)


def check_periodic_branch_relabeling() -> None:
    theta, chi = sp.symbols("theta chi")
    k = sp.symbols("k", integer=True)
    branch_energy = sp.Rational(1, 2) * chi * (theta + 2 * sp.pi * k) ** 2
    shifted = branch_energy.subs({theta: theta + 2 * sp.pi, k: k - 1})
    assert_zero("theta periodicity by branch relabeling", shifted - branch_energy)


def check_branch_mixture_cluster_covariance() -> None:
    weights = [sp.Rational(1, 5), sp.Rational(3, 10), sp.Rational(1, 2)]
    o_values = [sp.Rational(2, 3), sp.Rational(-1, 7), sp.Rational(5, 11)]
    p_values = [sp.Rational(13, 17), sp.Rational(3, 19), sp.Rational(-2, 23)]

    separated_limit = sum(weight * o * p for weight, o, p in zip(weights, o_values, p_values))
    one_point_product = (
        sum(weight * o for weight, o in zip(weights, o_values))
        * sum(weight * p for weight, p in zip(weights, p_values))
    )
    covariance = separated_limit - one_point_product

    mean_o = sum(weight * o for weight, o in zip(weights, o_values))
    mean_p = sum(weight * p for weight, p in zip(weights, p_values))
    covariance_direct = sum(
        weight * (o - mean_o) * (p - mean_p)
        for weight, o, p in zip(weights, o_values, p_values)
    )
    assert_zero("branch mixture cluster covariance", covariance - covariance_direct)

    pure_weights = [sp.Integer(0), sp.Integer(1), sp.Integer(0)]
    pure_covariance = (
        sum(weight * o * p for weight, o, p in zip(pure_weights, o_values, p_values))
        - sum(weight * o for weight, o in zip(pure_weights, o_values))
        * sum(weight * p for weight, p in zip(pure_weights, p_values))
    )
    assert_zero("pure branch clusters", pure_covariance)


def check_unique_branch_thermodynamic_selection() -> None:
    volume, gap1, gap2, correction = sp.symbols("volume gap1 gap2 correction", positive=True)
    z_min = sp.exp(-volume * correction / volume)
    z_1 = sp.exp(-volume * gap1)
    z_2 = sp.exp(-volume * gap2)
    nonminimal_ratio = sp.simplify((z_1 + z_2) / z_min)
    require(
        nonminimal_ratio.subs({volume: 10, gap1: 2, gap2: 3, correction: sp.Rational(1, 7)}) < sp.Rational(1, 1000000),
        "nonminimal branch ratios should be exponentially suppressed",
    )


def main() -> None:
    check_finite_volume_cumulant_identity()
    check_cp_symmetric_first_moment()
    check_witten_veneziano_mass_coefficient()
    check_massless_quark_theta_screening()
    check_periodic_branch_relabeling()
    check_branch_mixture_cluster_covariance()
    check_unique_branch_thermodynamic_selection()
    print("All QCD theta and Witten-Veneziano normalization checks passed.")


if __name__ == "__main__":
    main()
