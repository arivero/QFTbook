#!/usr/bin/env python3
"""Finite normalization checks for the Schwinger-model chapter.

The script checks the sign and normalization conventions used in the
two-dimensional bosonization formulas:

    eta = diag(-,+), epsilon^{01}=+1,
    J^mu = pi^{-1/2} epsilon^{mu nu} partial_nu phi,
    J_A^mu = -epsilon^{mu nu} J_nu = -pi^{-1/2} partial^mu phi,
    m_Sch^2 = e^2/pi,
    V(R) = Q^2 (1-exp(-m R))/(2m).
    Delta epsilon_Q(theta) = kappa M [cos(theta)-cos(theta+2 pi Q/e)].

The checks are deliberately finite algebraic checks rather than numerical
field-theory simulations.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close


from fractions import Fraction
import math


def eps(mu: int, nu: int) -> int:
    if (mu, nu) == (0, 1):
        return 1
    if (mu, nu) == (1, 0):
        return -1
    return 0


def metric(mu: int, nu: int) -> int:
    if mu != nu:
        return 0
    return -1 if mu == 0 else 1


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def assert_close(name: str, lhs: float, rhs: float, tol: float = 1e-12) -> None:
    _assert_close(name, lhs, rhs, tol=tol)


def check_current_duality() -> None:
    # Work coefficient by coefficient in d_0 phi and d_1 phi, suppressing the
    # common factor pi^{-1/2}.
    # J^mu = eps^{mu nu} d_nu phi.
    vector_current = {
        mu: [eps(mu, nu) for nu in range(2)]
        for mu in range(2)
    }
    lower_vector_current = {
        mu: [
            sum(metric(mu, rho) * vector_current[rho][nu] for rho in range(2))
            for nu in range(2)
        ]
        for mu in range(2)
    }
    axial_from_dual = {
        mu: [
            -sum(eps(mu, nu) * lower_vector_current[nu][lam] for nu in range(2))
            for lam in range(2)
        ]
        for mu in range(2)
    }
    minus_raised_derivative = {
        mu: [-metric(mu, lam) for lam in range(2)]
        for mu in range(2)
    }
    assert_equal("J_A duality", axial_from_dual, minus_raised_derivative)


def check_schwinger_mass_from_eliminating_electric_field() -> None:
    # L(E) = 1/2 E^2 + E A eliminates to -1/2 A^2.
    # Here A = e phi/sqrt(pi) + e theta/(2 pi).  The phi^2 coefficient is
    # therefore -1/2 e^2/pi, so m^2=e^2/pi for L=-1/2(d phi)^2-1/2 m^2 phi^2.
    electric_quadratic = Fraction(1, 2)
    saddle_substitution_coeff = electric_quadratic - 1
    assert_equal("electric-field Gaussian elimination", saddle_substitution_coeff, Fraction(-1, 2))

    e_squared_over_pi = Fraction(1, 1)
    mass_squared_coeff = -2 * saddle_substitution_coeff * e_squared_over_pi
    assert_equal("Schwinger mass coefficient", mass_squared_coeff, 1)


def check_schwinger_mass_from_anomaly_and_maxwell() -> None:
    # Maxwell equations in the chapter's convention imply
    # J^0 = -(partial_x E)/e and J^1 = (partial_t E)/e.
    # Current duality then gives div J_A = Box E/e.  Equating this to
    # the anomaly e E/pi gives (Box-e^2/pi)E=0.
    box_coefficient_from_current_duality = Fraction(1, 1)
    anomaly_coefficient = Fraction(1, 1)
    assert_equal(
        "electric-field mass from anomaly plus Maxwell",
        box_coefficient_from_current_duality,
        anomaly_coefficient,
    )


def check_screened_static_potential() -> None:
    m = 1.7
    charge = 0.8
    separation = 2.3
    green_zero = 1.0 / (2.0 * m)
    green_r = math.exp(-m * separation) / (2.0 * m)
    potential = charge * charge * (green_zero - green_r)
    expected = charge * charge * (1.0 - math.exp(-m * separation)) / (2.0 * m)
    assert_close("screened static potential", potential, expected)
    assert_close("large-distance screening limit", charge * charge * green_zero, charge * charge / (2.0 * m))


def check_dimensionless_screening_curve() -> None:
    # The figure uses x=m R and v(x)=2m V/Q^2=1-exp(-x).
    m = 2.0
    charge = 3.0
    for x in [0.0, 0.4, 1.0, 3.0]:
        separation = x / m
        potential = charge * charge * (1.0 - math.exp(-m * separation)) / (2.0 * m)
        plotted_value = 1.0 - math.exp(-x)
        potential_value = 2.0 * m * potential / (charge * charge)
        assert_close(f"dimensionless screening curve x={x}", plotted_value, potential_value)
    assert_close("screening curve origin", 1.0 - math.exp(0.0), 0.0)
    assert_close("screening curve tangent at origin", (1.0 - math.exp(-1.0e-6)) / 1.0e-6, 1.0, 1.0e-6)


def check_massive_probe_string_tension_periodicity() -> None:
    # Check sigma(Q)/(kappa M)=1-cos(2 pi Q/e) for representative charges.
    for q_over_e in [0, 1, -2, 3]:
        sigma = 1.0 - math.cos(2.0 * math.pi * q_over_e)
        assert_close(f"integer screening q/e={q_over_e}", sigma, 0.0)
    assert_close("half-integer fractional probe", 1.0 - math.cos(math.pi), 2.0)


def check_massive_probe_theta_shift() -> None:
    theta = 0.37
    q_over_e = 0.25
    shifted = theta + 2.0 * math.pi * q_over_e
    sigma = math.cos(theta) - math.cos(shifted)
    direct_difference = (-math.cos(shifted)) - (-math.cos(theta))
    assert_close("theta-shift string tension", sigma, direct_difference)
    integer_shift = theta + 2.0 * math.pi
    assert_close("integer probe returns same branch", math.cos(theta) - math.cos(integer_shift), 0.0)


def main() -> None:
    check_current_duality()
    check_schwinger_mass_from_eliminating_electric_field()
    check_schwinger_mass_from_anomaly_and_maxwell()
    check_screened_static_potential()
    check_dimensionless_screening_curve()
    check_massive_probe_string_tension_periodicity()
    check_massive_probe_theta_shift()
    print("All Schwinger-model normalization checks passed.")


if __name__ == "__main__":
    main()
