#!/usr/bin/env python3
"""Symbolic checks for the QCD Borel/Laplace current-sum-rule block.

These checks verify the algebra used in Volume II, Chapter 19:

1. The Borel transform of the subtracted dispersion kernel is
   exp(-s/M2)/M2.
2. Subtraction polynomials are annihilated once the derivative order is
   larger than the degree.
3. Inverse powers (Q2)^(-m) map to 1/((m-1)! (M2)^m).
4. The logarithmic Borel mass estimator is the spectral weighted average of
   the retained squared masses.
5. The plateau slope for a positive retained spectral measure is the weighted
   variance of s.
6. The continuum-threshold derivative contains the boundary spectral weight and
   the factor (s0 - m_eff^2).
7. A pole plus finite low-energy remainder obeys the stated mass-estimator
   error bound, and the bound fails if the R0 remainder is silently dropped.
8. The aggregate window residual in the zeroth moment must be propagated
   through the logarithmic mass quotient.
9. A flat mass curve obtained by retuning the continuum threshold is a
   two-scale cancellation, not an independent plateau.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{name}: got {simplified!r}, expected 0")


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name}: condition failed")


def check_borel_dispersion_kernel() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    s, m2 = sp.symbols("s m2", positive=True)
    q2 = n * m2
    nth_kernel = n * q2**n / (s + q2) ** (n + 1)
    limit = sp.limit(nth_kernel, n, sp.oo)
    assert_zero("Borel dispersion kernel", limit - sp.exp(-s / m2) / m2)


def check_polynomial_subtractions_are_killed() -> None:
    q2 = sp.symbols("q2")
    polynomial = 7 * q2**4 - 3 * q2**2 + 11
    killed = sp.diff(polynomial, q2, 5)
    assert_zero("subtraction polynomial killed", killed)


def check_inverse_power_borel_transform() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    m2 = sp.symbols("m2", positive=True)
    for power in range(1, 7):
        expression = (
            sp.gamma(power + n)
            / (sp.gamma(power) * sp.gamma(n))
            * (n * m2) ** (-power)
        )
        limit = sp.limit(expression, n, sp.oo)
        expected = 1 / (sp.factorial(power - 1) * m2**power)
        assert_zero(f"inverse power {power}", limit - expected)


def check_borel_mass_weighted_average() -> None:
    tau = sp.symbols("tau", positive=True)
    weights = [sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(11, 13)]
    masses_squared = [sp.Rational(3, 2), sp.Rational(5, 2), sp.Rational(7, 2)]
    spectral_sum = sum(
        weight * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    )
    estimator = -sp.diff(sp.log(spectral_sum), tau)
    weighted_average = sum(
        weight * mass_sq * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    ) / spectral_sum
    assert_zero("Borel mass weighted average", estimator - weighted_average)

    single_atom = weights[0] * sp.exp(-tau * masses_squared[0])
    assert_equal(
        "single atom mass estimator",
        sp.simplify(-sp.diff(sp.log(single_atom), tau)),
        masses_squared[0],
    )


def check_borel_plateau_variance_diagnostic() -> None:
    tau = sp.symbols("tau", positive=True)
    weights = [sp.Rational(2, 5), sp.Rational(3, 7), sp.Rational(5, 11)]
    masses_squared = [sp.Rational(4, 3), sp.Rational(7, 3), sp.Rational(11, 3)]
    spectral_sum = sum(
        weight * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    )
    first_moment = sum(
        weight * mass_sq * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    )
    second_moment = sum(
        weight * mass_sq**2 * sp.exp(-tau * mass_sq)
        for weight, mass_sq in zip(weights, masses_squared)
    )
    estimator = first_moment / spectral_sum
    variance = second_moment / spectral_sum - estimator**2
    assert_zero("Borel plateau variance", -sp.diff(estimator, tau) - variance)
    assert_true(
        "nontrivial retained spectrum has positive variance",
        sp.simplify(variance.subs(tau, 0)) > 0,
    )

    single_atom = weights[0] * sp.exp(-tau * masses_squared[0])
    single_estimator = -sp.diff(sp.log(single_atom), tau)
    assert_zero("single atom plateau slope", sp.diff(single_estimator, tau))


def check_continuum_threshold_sensitivity() -> None:
    l0, l1, s0, boundary_weight = sp.symbols(
        "l0 l1 s0 boundary_weight", positive=True
    )
    m_eff_sq = l1 / l0
    derivative = (s0 * boundary_weight * l0 - l1 * boundary_weight) / l0**2
    expected = boundary_weight * (s0 - m_eff_sq) / l0
    assert_zero("continuum-threshold sensitivity", derivative - expected)

    values = {
        l0: sp.Rational(5, 2),
        l1: sp.Rational(7, 3),
        s0: sp.Rational(11, 5),
        boundary_weight: sp.Rational(13, 17),
    }
    exact = sp.simplify(expected.subs(values))
    missing_factor_shortcut = sp.simplify((boundary_weight / l0).subs(values))
    assert_true(
        "threshold derivative shortcut fails",
        exact != missing_factor_shortcut,
    )


def check_pole_remainder_mass_bound() -> None:
    pole_weight = sp.Rational(5, 3)
    mass_sq = sp.Rational(7, 2)
    residual_l0 = -sp.Rational(1, 20)
    residual_l1 = sp.Rational(1, 30)
    estimator = (pole_weight * mass_sq + residual_l1) / (
        pole_weight + residual_l0
    )
    deviation = sp.Abs(sp.simplify(estimator - mass_sq))
    bound = (sp.Abs(residual_l1) + mass_sq * sp.Abs(residual_l0)) / (
        pole_weight - sp.Abs(residual_l0)
    )
    assert_true("pole-remainder mass bound", sp.simplify(deviation <= bound))

    missing_l0_bound = sp.Abs(residual_l1) / (pole_weight - sp.Abs(residual_l0))
    assert_true(
        "dropping the L0 remainder underestimates the error",
        sp.simplify(deviation > missing_l0_bound),
    )


def check_window_residual_mass_bound() -> None:
    l0 = sp.Rational(9, 4)
    l1 = sp.Rational(7, 3)
    delta_l0 = sp.Rational(1, 20)
    delta_l1 = sp.Rational(0)

    retained_mass = l1 / l0
    exact_mass = (l1 + delta_l1) / (l0 + delta_l0)
    deviation = sp.Abs(sp.simplify(exact_mass - retained_mass))
    bound = (sp.Abs(delta_l1) + sp.Abs(retained_mass) * sp.Abs(delta_l0)) / (
        l0 - sp.Abs(delta_l0)
    )
    assert_true("window residual mass bound", sp.simplify(deviation <= bound))

    missing_l0_bound = sp.Abs(delta_l1) / (l0 - sp.Abs(delta_l0))
    assert_true(
        "dropping the window L0 residual hides a mass shift",
        sp.simplify(deviation > missing_l0_bound),
    )


def check_retuned_threshold_plateau_degeneracy() -> None:
    l0 = sp.Rational(5, 2)
    l1 = sp.Rational(7, 3)
    l2 = sp.Rational(13, 4)
    s0 = sp.Rational(11, 5)
    boundary_weight = sp.Rational(13, 17)

    m_eff_sq = l1 / l0
    tau_derivative = -(l2 * l0 - l1**2) / l0**2
    threshold_derivative = boundary_weight * (s0 - m_eff_sq) / l0

    assert_true("nonzero tau slope before retuning", tau_derivative != 0)
    assert_true(
        "nonzero threshold sensitivity before retuning",
        threshold_derivative != 0,
    )

    required_threshold_velocity = -tau_derivative / threshold_derivative
    total_derivative = tau_derivative + required_threshold_velocity * threshold_derivative
    assert_zero("retuned threshold can flatten the displayed curve", total_derivative)
    assert_true(
        "retuned plateau uses a moving threshold",
        required_threshold_velocity != 0,
    )
    assert_true(
        "fixed threshold curve is not flat",
        tau_derivative != total_derivative,
    )


def main() -> None:
    check_borel_dispersion_kernel()
    check_polynomial_subtractions_are_killed()
    check_inverse_power_borel_transform()
    check_borel_mass_weighted_average()
    check_borel_plateau_variance_diagnostic()
    check_continuum_threshold_sensitivity()
    check_pole_remainder_mass_bound()
    check_window_residual_mass_bound()
    check_retuned_threshold_plateau_degeneracy()
    print("All QCD Borel/Laplace sum-rule checks passed.")


if __name__ == "__main__":
    main()
