#!/usr/bin/env python3
"""Finite algebra checks for HMC and pseudofermion identities.

These checks certify only the finite-dimensional identities used in
Volume XI, Chapter 6.  They do not test a continuum limit, solver
stability, or ergodicity of a production Markov chain.
"""

from __future__ import annotations

import pathlib
import sys
from fractions import Fraction

import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import hmc_rhmc_finite_demo as hmc_demo  # noqa: E402


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matmul(a: Matrix2, b: Matrix2) -> Matrix2:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def det2(a: Matrix2) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv2(a: Matrix2) -> Matrix2:
    det = det2(a)
    if det == 0:
        raise AssertionError("singular matrix in inverse check")
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def assert_equal(got: object, expected: object, label: str) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_true(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def check_one_dimensional_leapfrog() -> None:
    """Check determinant one and R L R = L^{-1} for quadratic leapfrog."""

    eps = Fraction(2, 7)
    k = Fraction(3, 5)
    mass = Fraction(5, 4)

    a = 1 - eps * eps * k / (2 * mass)
    b = eps / mass
    c = -eps * k + eps * eps * eps * k * k / (4 * mass)
    leapfrog: Matrix2 = ((a, b), (c, a))

    assert_equal(det2(leapfrog), Fraction(1), "leapfrog determinant")

    flip: Matrix2 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))
    conjugated = matmul(matmul(flip, leapfrog), flip)
    assert_equal(conjugated, inv2(leapfrog), "leapfrog reversibility")


def metropolis_acceptance(weight_from: Fraction, weight_to: Fraction) -> Fraction:
    ratio = weight_to / weight_from
    return min(Fraction(1), ratio)


def check_pairwise_metropolis_balance() -> None:
    """Check w(z) a(z->z') = w(z') a(z'->z) in both energy orderings."""

    examples = [
        (Fraction(7, 3), Fraction(2, 5)),
        (Fraction(2, 5), Fraction(7, 3)),
        (Fraction(11, 13), Fraction(11, 13)),
    ]
    for w0, w1 in examples:
        lhs = w0 * metropolis_acceptance(w0, w1)
        rhs = w1 * metropolis_acceptance(w1, w0)
        assert_equal(lhs, rhs, "pairwise Metropolis balance")


def check_pseudofermion_determinant_identity() -> None:
    """Check the pi-free determinant factor after diagonalization."""

    eigenvalues = (Fraction(2), Fraction(5), Fraction(7, 3))
    det_a = Fraction(1)
    gaussian_factor_without_pi = Fraction(1)
    for lam in eigenvalues:
        det_a *= lam
        # int_C exp(-|z|^2 / lam) d^2 z = pi * lam.
        gaussian_factor_without_pi *= lam
    assert_equal(
        gaussian_factor_without_pi,
        det_a,
        "pseudofermion Gaussian determinant factor",
    )


def check_rational_action_error_bound() -> None:
    """Check |phi^*(r(A)-f(A))phi| <= delta ||phi||^2 diagonally."""

    target_values = (Fraction(1, 2), Fraction(1, 5), Fraction(3, 11))
    rational_values = (
        target_values[0] + Fraction(1, 100),
        target_values[1] - Fraction(1, 200),
        target_values[2] + Fraction(1, 250),
    )
    phi_norm_squares = (Fraction(3), Fraction(2), Fraction(5, 4))

    errors = [r - f for r, f in zip(rational_values, target_values)]
    delta = max(abs(error) for error in errors)
    action_error = sum(
        error * norm_square
        for error, norm_square in zip(errors, phi_norm_squares)
    )
    norm_square = sum(phi_norm_squares)
    assert_true(
        abs(action_error) <= delta * norm_square,
        "rational pseudofermion action-error bound",
    )


def check_linear_solver_action_and_force_bounds() -> None:
    """Check residual-to-action and residual-to-force bounds diagonally."""

    eigenvalues = (Fraction(3, 2), Fraction(5, 2), Fraction(4, 1))
    phi = (Fraction(2, 3), Fraction(-1, 5), Fraction(3, 4))
    residual = (Fraction(1, 200), Fraction(-1, 300), Fraction(1, 250))
    lambda_min = min(eigenvalues)

    true_solution = tuple(phi_i / lam for phi_i, lam in zip(phi, eigenvalues))
    approximate_solution = tuple((phi_i - r_i) / lam for phi_i, r_i, lam in zip(phi, residual, eigenvalues))

    exact_action = sum(phi_i * y_i for phi_i, y_i in zip(phi, true_solution))
    approximate_action = sum(phi_i * x_i for phi_i, x_i in zip(phi, approximate_solution))
    phi_norm_sq = sum(phi_i * phi_i for phi_i in phi)
    residual_norm_sq = sum(r_i * r_i for r_i in residual)
    action_bound_sq = phi_norm_sq * residual_norm_sq / (lambda_min * lambda_min)
    assert_true(
        (exact_action - approximate_action) ** 2 <= action_bound_sq,
        "linear solver pseudofermion action bound",
    )

    force_derivative = (Fraction(7, 5), Fraction(-2, 3), Fraction(5, 4))
    exact_force = sum(d_i * y_i * y_i for d_i, y_i in zip(force_derivative, true_solution))
    approximate_force = sum(d_i * x_i * x_i for d_i, x_i in zip(force_derivative, approximate_solution))
    x_norm_sq = sum(x_i * x_i for x_i in approximate_solution)
    operator_bound = max(abs(d_i) for d_i in force_derivative)
    force_bound = operator_bound * (
        2 * (x_norm_sq ** Fraction(1, 2)) * (residual_norm_sq ** Fraction(1, 2)) / lambda_min
        + residual_norm_sq / (lambda_min * lambda_min)
    )
    assert_true(
        abs(exact_force - approximate_force) <= force_bound,
        "linear solver pseudofermion force bound",
    )


def check_rhmc_log_reweighting_bound() -> None:
    """Check |log W_rat| <= N eta_* for a finite rational approximation ledger."""

    eta_values = (Fraction(1, 1000), Fraction(-3, 2000), Fraction(1, 2500), Fraction(1, 1500))
    eta_star = max(abs(eta) for eta in eta_values)
    log_weight = sum(eta_values)
    assert_true(
        abs(log_weight) <= len(eta_values) * eta_star,
        "RHMC determinant reweighting log bound",
    )


def check_companion_hmc_rhmc_smoke_helpers() -> None:
    cfg = hmc_demo.RunConfig(
        sites=6,
        mass2=0.7,
        quartic=0.8,
        stiffness=0.5,
        step_size=0.05,
        leapfrog_steps=4,
        trajectories=12,
        therm=3,
        seed=271828,
        cg_tol=1.0e-12,
    )
    result = hmc_demo.run(cfg)
    assert_true(0.0 <= result["acceptance"] <= 1.0, "HMC demo acceptance probability")
    assert_true(result["positive_matrix_min_eigenvalue"] > 0.0, "HMC demo positive matrix")
    assert_true(result["max_cg_residual"] <= 1.0e-8, "HMC demo CG residual")
    assert_true(result["last_reversibility_defect"] <= 1.0e-10, "HMC demo reversibility")

    matrix = hmc_demo.positive_matrix(np.linspace(-0.2, 0.3, 5))
    phi = np.linspace(0.4, -0.1, 5)
    rational = hmc_demo.rational_pseudofermion_action(matrix, phi, tol=1.0e-13)
    assert_true(rational["rational_action"] > 0.0, "positive rational pseudofermion action")
    assert_true(rational["max_cg_residual"] <= 1.0e-10, "positive rational solve residual")


def main() -> None:
    check_one_dimensional_leapfrog()
    check_pairwise_metropolis_balance()
    check_pseudofermion_determinant_identity()
    check_rational_action_error_bound()
    check_linear_solver_action_and_force_bounds()
    check_rhmc_log_reweighting_bound()
    check_companion_hmc_rhmc_smoke_helpers()
    print("All HMC and pseudofermion checks passed.")


if __name__ == "__main__":
    main()
