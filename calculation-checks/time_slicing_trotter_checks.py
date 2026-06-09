#!/usr/bin/env python3
"""Finite checks for Trotter time slicing and symbol-ordering boundaries.

Volume I, Chapter 4 separates exact Trotter products from approximate
exponentiated-symbol time slices.  These checks verify the finite algebra
behind that boundary: the harmonic-oscillator Mehler kernel is the heat kernel
selected by the exact Schrodinger product, order-epsilon symbol terms
accumulate over T/epsilon slices, and variable-coefficient kinetic operators
require reference-measure and ordering counterterms.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def require_zero(label: str, expression) -> None:
    simplified = sp.simplify(sp.factor(sp.cancel(expression)))
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")


def require_nonzero(label: str, expression) -> None:
    simplified = sp.simplify(sp.factor(sp.cancel(expression)))
    if simplified == 0:
        raise AssertionError(f"{label} should have produced a nonzero obstruction")


def check_harmonic_oscillator_mehler_heat_kernel() -> None:
    tau, x, y = sp.symbols("tau x y", positive=True)
    log_kernel = -sp.log(2 * sp.pi * sp.sinh(tau)) / 2
    log_kernel -= ((x**2 + y**2) * sp.cosh(tau) - 2 * x * y) / (2 * sp.sinh(tau))

    dx_log = sp.diff(log_kernel, x)
    dxx_over_kernel = sp.diff(log_kernel, x, 2) + dx_log**2
    h_over_kernel = -sp.Rational(1, 2) * dxx_over_kernel + x**2 / 2
    require_zero(
        "Mehler kernel solves Euclidean oscillator heat equation",
        sp.diff(log_kernel, tau) + h_over_kernel,
    )


def check_order_epsilon_symbol_term_accumulates() -> None:
    total_time = Fraction(5, 3)
    quantum_shift = Fraction(7, 11)
    for slices in (1, 2, 5, 17):
        epsilon = total_time / slices
        accumulated = sum(epsilon * quantum_shift for _ in range(slices))
        if accumulated != total_time * quantum_shift:
            raise AssertionError("order-epsilon term failed to accumulate exactly")


def weyl_a_p_squared(a, psi, q, hbar):
    return -hbar**2 * (
        a * sp.diff(psi, q, 2)
        + sp.diff(a, q) * sp.diff(psi, q)
        + sp.diff(a, q, 2) * psi / 4
    )


def check_weyl_scalar_counterterm_for_variable_kinetic() -> None:
    q, hbar = sp.symbols("q hbar")
    a = 1 + q**2
    psi = 1 + q + q**3

    symmetric_kinetic = -hbar**2 * sp.diff(a * sp.diff(psi, q), q) / 2
    weyl_without_counterterm = weyl_a_p_squared(a, psi, q, hbar) / 2
    weyl_with_counterterm = weyl_without_counterterm + hbar**2 * sp.diff(a, q, 2) * psi / 8

    require_zero(
        "Weyl scalar counterterm restores p a(q) p / 2",
        weyl_with_counterterm - symmetric_kinetic,
    )
    require_nonzero(
        "omitting Weyl scalar counterterm changes Hamiltonian",
        weyl_without_counterterm - symmetric_kinetic,
    )


def check_reference_measure_linear_momentum_term() -> None:
    q, hbar = sp.symbols("q hbar")
    sigma = q**2
    psi = 1 + q + q**2
    p_psi = -sp.I * hbar * sp.diff(psi, q)

    laplace_beltrami_kinetic = -hbar**2 * sp.exp(-2 * sigma) * (
        sp.diff(psi, q, 2) - sp.diff(sigma, q) * sp.diff(psi, q)
    ) / 2
    right_symbol_kinetic = (
        sp.exp(-2 * sigma) * (-hbar**2 * sp.diff(psi, q, 2)) / 2
        + sp.I * hbar * sp.exp(-2 * sigma) * sp.diff(sigma, q) * p_psi / 2
    )

    require_zero(
        "reference-measure right symbol needs linear momentum term",
        right_symbol_kinetic - laplace_beltrami_kinetic,
    )
    require_nonzero(
        "dropping linear momentum term changes curved-measure kinetic operator",
        sp.exp(-2 * sigma) * (-hbar**2 * sp.diff(psi, q, 2)) / 2
        - laplace_beltrami_kinetic,
    )


def main() -> None:
    check_harmonic_oscillator_mehler_heat_kernel()
    check_order_epsilon_symbol_term_accumulates()
    check_weyl_scalar_counterterm_for_variable_kinetic()
    check_reference_measure_linear_momentum_term()
    print("All time-slicing Trotter and ordering-boundary checks passed.")


if __name__ == "__main__":
    main()
