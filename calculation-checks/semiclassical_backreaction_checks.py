#!/usr/bin/env python3
"""Finite checks for the semiclassical backreaction chapter.

These checks verify algebraic identities that are easy to lose by a sign or
normalization: traces of the curvature-squared Euler tensors in four
dimensions, the KMS fluctuation-dissipation factor, positivity of the noise
covariance, and the low-energy root selected by reduction of order in a toy
higher-derivative equation.
"""

from __future__ import annotations

import cmath
import math


def assert_close(got: complex, expected: complex, label: str, tol: float = 1e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def check_curvature_squared_traces() -> None:
    dimension = 4

    # H^(1) = 2 R R_mn - 1/2 g_mn R^2 + 2 g_mn Box R - 2 nabla_m nabla_n R.
    r2_coeff = 2 - dimension / 2
    box_r_coeff = 2 * dimension - 2
    assert_close(r2_coeff, 0.0, "R^2 trace algebra in D=4")
    assert_close(box_r_coeff, 6.0, "H1 trace Box R coefficient")

    # H^(2) = 2 R_mrns R^rs - 1/2 g_mn Ric^2
    #       + nabla_m nabla_n R - Box R_mn - 1/2 g_mn Box R.
    ricci2_coeff = 2 - dimension / 2
    box_r_coeff_h2 = 1 - 1 - dimension / 2
    assert_close(ricci2_coeff, 0.0, "Ricci^2 trace algebra in D=4")
    assert_close(box_r_coeff_h2, -2.0, "H2 trace Box R coefficient")


def check_kms_fluctuation_dissipation() -> None:
    beta = 1.7
    omega = 0.9
    c_ab = 2.3
    c_ba_minus = math.exp(-beta * omega) * c_ab
    noise = 0.5 * (c_ab + c_ba_minus)
    rho = c_ab - c_ba_minus
    expected_noise = 0.5 / math.tanh(0.5 * beta * omega) * rho
    assert_close(noise, expected_noise, "KMS fluctuation-dissipation factor")


def check_noise_covariance_positivity() -> None:
    covariance = ((2.0, 0.7), (0.7, 1.0))
    determinant = covariance[0][0] * covariance[1][1] - covariance[0][1] ** 2
    if covariance[0][0] <= 0 or determinant <= 0:
        raise AssertionError("test covariance should be positive definite")
    for x, y in [(1.0, -3.0), (2.0, 5.0), (-0.25, 0.75)]:
        value = (
            covariance[0][0] * x * x
            + 2 * covariance[0][1] * x * y
            + covariance[1][1] * y * y
        )
        if value < -1e-12:
            raise AssertionError("noise quadratic form should be nonnegative")


def check_reduction_of_order_toy_model() -> None:
    # Toy equation: x'' + omega0^2 x + epsilon x'''' = 0.
    # For x ~ exp(lambda t), epsilon lambda^4 + lambda^2 + omega0^2 = 0.
    omega0 = 1.3
    eps = 1.0e-4
    # Low-energy perturbative root has lambda^2 = -omega0^2 - eps omega0^4 + O(eps^2).
    reduced_lambda_sq = -(omega0**2) - eps * omega0**4

    # Exact roots for z=lambda^2 solve eps z^2 + z + omega0^2=0.
    discriminant = 1 - 4 * eps * omega0**2
    z_low = (-1 + math.sqrt(discriminant)) / (2 * eps)
    z_high = (-1 - math.sqrt(discriminant)) / (2 * eps)
    assert_close(z_low, reduced_lambda_sq, "low-energy reduced root", tol=1e-3)
    if abs(z_high) < 0.1 / eps:
        raise AssertionError("discarded higher-derivative root should live at cutoff scale")

    lambda_low = cmath.sqrt(z_low)
    if abs(lambda_low.real) > 1e-9:
        raise AssertionError("low-energy root should remain oscillatory in the stable toy model")


def main() -> None:
    check_curvature_squared_traces()
    check_kms_fluctuation_dissipation()
    check_noise_covariance_positivity()
    check_reduction_of_order_toy_model()
    print("All semiclassical backreaction checks passed.")


if __name__ == "__main__":
    main()
