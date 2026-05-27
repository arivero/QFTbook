#!/usr/bin/env python3
"""Finite checks for the point-split stress-tensor examples."""

from fractions import Fraction

import mpmath as mp
import sympy as sp


mp.mp.dps = 60


def assert_close(name, lhs, rhs, tol=mp.mpf("1e-45")):
    lhs = mp.mpf(lhs)
    rhs = mp.mpf(rhs)
    scale = max(mp.mpf(1), abs(lhs), abs(rhs))
    if abs(lhs - rhs) > tol * scale:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def assert_equal(name, lhs, rhs):
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def check_flat_hadamard_transport_identity():
    z0, z1, z2, z3 = sp.symbols("z0 z1 z2 z3")
    coordinates = [z0, z1, z2, z3]
    inverse_metric = [-1, 1, 1, 1]
    sigma = sp.Rational(1, 2) * (-z0**2 + z1**2 + z2**2 + z3**2)

    grad_sigma_squared = sum(
        inverse_metric[index] * sp.diff(sigma, coordinate) ** 2
        for index, coordinate in enumerate(coordinates)
    )
    box_sigma = sum(
        inverse_metric[index] * sp.diff(sigma, coordinate, 2)
        for index, coordinate in enumerate(coordinates)
    )

    assert_equal("flat Synge identity", sp.simplify(grad_sigma_squared - 2 * sigma), 0)
    assert_equal("flat box sigma", sp.simplify(box_sigma), 4)

    u_h = sp.Integer(1)
    leading_transport = (
        2
        * sum(
            inverse_metric[index] * sp.diff(sigma, coordinate) * sp.diff(u_h, coordinate)
            for index, coordinate in enumerate(coordinates)
        )
        + (box_sigma - 4) * u_h
    )
    assert_equal("flat Hadamard U transport", sp.simplify(leading_transport), 0)


def main():
    check_flat_hadamard_transport_identity()

    w_state = Fraction(7, 5)
    w_prime_state = Fraction(11, 13)
    h_singular = Fraction(2, 3)
    smooth_shift = Fraction(5, 17)
    wick_state = w_state - h_singular
    wick_prime_state = w_prime_state - h_singular
    wick_shifted_subtraction = w_state - (h_singular + smooth_shift)
    assert_equal("point-split state difference", wick_state - wick_prime_state, w_state - w_prime_state)
    assert_equal("point-split smooth subtraction sign", wick_shifted_subtraction, wick_state - smooth_shift)

    bose_integral = mp.quad(lambda x: x**3 / mp.expm1(x), [0, mp.inf])
    assert_close("Bose integral", bose_integral, mp.pi**4 / 15)

    for beta in [mp.mpf("0.7"), mp.mpf("1.0"), mp.mpf("2.3")]:
        rho = (1 / (2 * mp.pi**2)) * beta**(-4) * bose_integral
        expected_rho = mp.pi**2 / (30 * beta**4)
        pressure = rho / 3

        assert_close("thermal energy density", rho, expected_rho)
        assert_close("massless flat trace", -rho + 3 * pressure, 0)

    # Plane-wave eigenvalues of the point-split differential operators.
    # D_00 gives omega^2 on each massless plane wave; D_ii gives k_i^2.
    for kx, ky, kz in [
        (mp.mpf("1.0"), mp.mpf("2.0"), mp.mpf("3.0")),
        (mp.mpf("0.4"), mp.mpf("-0.8"), mp.mpf("1.1")),
    ]:
        k_squared = kx**2 + ky**2 + kz**2
        omega = mp.sqrt(k_squared)
        d00 = (omega**2 + k_squared) / 2
        spatial_trace_part = (omega**2 - k_squared) / 2
        assert_close("D00 massless plane-wave eigenvalue", d00, omega**2)
        assert_close("on-shell spatial trace term", spatial_trace_part, 0)

    # Four-dimensional de Sitter curvature invariants with R=12 H^2.
    H = mp.mpf("1.37")
    riem_sq = 24 * H**4
    ricci_sq = 36 * H**4
    scalar_curvature = 12 * H**2
    euler_density = riem_sq - 4 * ricci_sq + scalar_curvature**2
    assert_close("de Sitter Euler density", euler_density, 24 * H**4)

    a_scalar = mp.mpf(1) / 360
    trace = -(a_scalar * euler_density) / (16 * mp.pi**2)
    stress_constant = trace / 4
    assert_close("conformal scalar de Sitter trace", trace, -H**4 / (240 * mp.pi**2))
    assert_close(
        "conformal scalar de Sitter stress constant",
        stress_constant,
        -H**4 / (960 * mp.pi**2),
    )

    print("All point-splitting stress-tensor checks passed.")


if __name__ == "__main__":
    main()
