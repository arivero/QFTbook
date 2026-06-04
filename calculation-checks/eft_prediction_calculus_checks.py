#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- The heavy scalar tree kernel expands as a local derivative series with a
  controlled low-momentum remainder.
- The one-loop hard threshold term cancels the artificial matching-scale
  dependence against full-theory and low-theory running at the retained order.
- A local field redefinition preserves source-dependent observables only when
  the Jacobian, source transform, and observable transform are carried
  together.
- A multi-parameter EFT power counting is an error organization only when
  logs do not lower order and omitted terms are assigned to an explicit
  residual ledger.

Independent construction:
- The heavy-kernel identity is checked as an exact rational identity and as a
  dimensionful bound on the declared low-momentum domain.
- The matching-scale cancellation is checked by differentiating a symbolic
  one-loop matched coordinate.
- The field-redefinition identity is checked by exact Gaussian moments with a
  nonzero source.
- The power-counting ledger is checked by a small independent filtration and
  residual-budget arithmetic.

Imported assumptions:
- Euclidean low-energy kinematics with q^2 >= 0 and q^2 <= Q^2 << M^2.
- The quartic coordinate is normalized so the heavy beta contribution is the
  coefficient b_H in d lambda_full / d log(mu) = beta_light + b_H.
- The field-redefinition check is a finite-dimensional Gaussian analogue of
  the regulated functional-integral change of variables.

Negative controls:
- Reversing the heavy-kernel remainder sign fails the exact identity.
- Omitting the hard threshold logarithm leaves matching-scale dependence.
- Dropping either the Jacobian or the source transformation spoils the
  source-dependent field-redefinition identity.
- Letting logarithms reduce the power-counting weight admits a term that the
  declared residual ledger must reject.

Scope boundary:
- This script checks finite algebra and bookkeeping for the EFT prediction
  calculus.  It does not prove nonperturbative decoupling, regulator removal,
  asymptotic convergence, or a continuum scattering construction.
"""

from __future__ import annotations

import sympy as sp

from check_utils import assert_close, assert_gt, assert_leq


def assert_zero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: expected zero, got {sp.simplify(value)!r}")


def assert_nonzero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) == 0:
        raise AssertionError(f"{name}: expected a nonzero negative control")


def check_heavy_kernel_expansion() -> None:
    x = sp.symbols("x")
    for order in range(5):
        truncated = sum((-x) ** r for r in range(order + 1))
        remainder = (-x) ** (order + 1) / (1 + x)
        exact = 1 / (1 + x)
        assert_zero(f"geometric heavy-kernel remainder N={order}", truncated + remainder - exact)
        assert_nonzero(
            f"wrong-sign heavy-kernel remainder N={order}",
            truncated - remainder - exact,
        )

    M, q2 = sp.symbols("M q2", positive=True)
    order = 3
    dimensionful = 1 / (M**2 + q2)
    dimensionful_truncated = sum((-q2) ** r / M ** (2 * r + 2) for r in range(order + 1))
    dimensionful_remainder = (-q2) ** (order + 1) / (M ** (2 * order + 2) * (M**2 + q2))
    assert_zero(
        "dimensionful heavy-kernel expansion",
        dimensionful_truncated + dimensionful_remainder - dimensionful,
    )

    for ratio in (0.05, 0.1, 0.25):
        mass = 11.0
        q2_value = (ratio * mass) ** 2
        remainder_value = abs(float(dimensionful_remainder.subs({M: mass, q2: q2_value})))
        bound = q2_value ** (order + 1) / mass ** (2 * order + 4)
        assert_leq(f"low-momentum heavy-kernel bound Q/M={ratio}", remainder_value, bound)

    eta = sp.symbols("eta", nonzero=True)
    quartic_lambda_shift = sp.factor(sp.factorial(4) * (-eta**2 / (8 * M**2)))
    assert_zero("tree exchange converted to lambda/4! convention", quartic_lambda_shift + 3 * eta**2 / M**2)
    kernel_q2_coefficient = sp.expand(-eta**2 / 8 * (1 / M**2 - q2 / M**4)).coeff(q2)
    assert_zero("positive derivative operator sign", kernel_q2_coefficient - eta**2 / (8 * M**4))


def check_matching_scale_cancellation() -> None:
    L_M, L_low, lam_M, beta_light, b_H, c_H = sp.symbols(
        "L_M L_low lam_M beta_light b_H c_H"
    )
    beta_full = beta_light + b_H
    hard_threshold = -b_H * L_M + c_H
    running_to_low = beta_light * (L_low - L_M)
    matched_low_coordinate = lam_M + beta_full * L_M + hard_threshold + running_to_low

    expected = lam_M + beta_light * L_low + c_H
    assert_zero("one-loop matching-scale cancellation", matched_low_coordinate - expected)
    assert_zero("derivative with respect to matching log", sp.diff(matched_low_coordinate, L_M))

    missing_threshold = lam_M + beta_full * L_M + running_to_low
    assert_nonzero("missing hard threshold leaves scale dependence", sp.diff(missing_threshold, L_M))
    wrong_threshold = lam_M + beta_full * L_M - hard_threshold + running_to_low
    assert_nonzero("wrong hard threshold sign leaves scale dependence", sp.diff(wrong_threshold, L_M))


def gaussian_source_moment(power: int, source: sp.Symbol) -> sp.Expr:
    """Return the normalized Gaussian moment integral without sqrt(2*pi)."""

    return sp.diff(sp.exp(source**2 / 2), source, power)


def integrate_polynomial_against_source_gaussian(poly: sp.Expr, variable: sp.Symbol, source: sp.Symbol) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), variable)
    total = 0
    for (power,), coefficient in expanded.terms():
        total += coefficient * gaussian_source_moment(power, source)
    return sp.simplify(total)


def check_source_aware_field_redefinition() -> None:
    y, J = sp.symbols("y J")
    action_prime = y
    observable = y**2 + y
    observable_prime = sp.diff(observable, y)
    field_shift = y + y**2
    jacobian = sp.diff(field_shift, y)

    first_order_change = (
        jacobian * observable
        + field_shift * observable_prime
        + J * field_shift * observable
        - action_prime * field_shift * observable
    )
    exact_integral = integrate_polynomial_against_source_gaussian(first_order_change, y, J)
    assert_zero("field redefinition with source and Jacobian", exact_integral)

    without_source_transform = first_order_change - J * field_shift * observable
    without_source_integral = integrate_polynomial_against_source_gaussian(without_source_transform, y, J)
    assert_nonzero("omitting source transform breaks identity", without_source_integral)

    without_jacobian = first_order_change - jacobian * observable
    without_jacobian_integral = integrate_polynomial_against_source_gaussian(without_jacobian, y, J)
    assert_nonzero("omitting Jacobian breaks identity", without_jacobian_integral)


def eft_weight(term: dict[str, int]) -> int:
    return 2 * term["loops"] + term["canonical_excess"] + term["velocity_excess"]


def bad_weight_that_treats_logs_as_suppression(term: dict[str, int]) -> int:
    return eft_weight(term) - term["log_power"]


def check_power_counting_and_residual_ledger() -> None:
    target_order = 4
    retained_terms = [
        {"name": "tree_dim6", "loops": 0, "canonical_excess": 2, "velocity_excess": 0, "log_power": 0},
        {"name": "one_loop_dim4", "loops": 1, "canonical_excess": 0, "velocity_excess": 0, "log_power": 2},
        {"name": "velocity_insert", "loops": 0, "canonical_excess": 1, "velocity_excess": 2, "log_power": 1},
    ]
    generated_counterterms = [
        {"name": "dim6_counterterm", "loops": 1, "canonical_excess": 2, "velocity_excess": 0, "log_power": 3},
        {"name": "dim8_residual", "loops": 1, "canonical_excess": 4, "velocity_excess": 0, "log_power": 5},
    ]

    for term in retained_terms:
        assert_leq(f"retained term weight {term['name']}", eft_weight(term), target_order)

    retained_counterterm = generated_counterterms[0]
    residual_counterterm = generated_counterterms[1]
    assert_leq("closed counterterm remains retained", eft_weight(retained_counterterm), target_order)
    assert_gt("first omitted counterterm assigned to residual", eft_weight(residual_counterterm), target_order)
    assert_leq(
        "bad log counting would incorrectly retain omitted counterterm",
        bad_weight_that_treats_logs_as_suppression(residual_counterterm),
        target_order,
    )

    components = {
        "tree_kernel": 0.0025,
        "one_loop_truncation": 0.0012,
        "first_omitted_counterterm": 0.0008,
    }
    declared_bound = 0.0046
    actual_residual = sum(components.values())
    assert_leq("residual ledger covers all components", actual_residual, declared_bound)
    assert_gt(
        "dropping omitted counterterm undercounts residual",
        actual_residual,
        declared_bound - components["first_omitted_counterterm"],
    )
    assert_close("explicit residual arithmetic", actual_residual, 0.0045, atol=1.0e-15)


def main() -> None:
    check_heavy_kernel_expansion()
    check_matching_scale_cancellation()
    check_source_aware_field_redefinition()
    check_power_counting_and_residual_ledger()
    print("All EFT prediction-calculus checks passed.")


if __name__ == "__main__":
    main()
