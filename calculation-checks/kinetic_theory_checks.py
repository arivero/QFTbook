#!/usr/bin/env python3
"""Finite algebra checks for the kinetic-theory controlled-limit chapter."""

from __future__ import annotations

import math

import sympy as sp


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-11) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def distribution(beta: float, energy: float, chemical: float, eta: int) -> float:
    return 1.0 / (math.exp(beta * (energy - chemical)) - eta)


def one_plus_eta_f(beta: float, energy: float, chemical: float, eta: int) -> tuple[float, float]:
    f = distribution(beta, energy, chemical, eta)
    return 1.0 + eta * f, math.exp(beta * (energy - chemical)) * f


def check_detailed_balance() -> None:
    beta = 1.3
    energies = [1.1, 0.9, 0.7, 1.3]
    charges = [1.0, -0.2, 0.4, 0.4]
    mu = 0.17
    etas = [1, -1, 1, -1]
    f = [distribution(beta, e, mu * q, eta) for e, q, eta in zip(energies, charges, etas)]

    for index, (e, q, eta) in enumerate(zip(energies, charges, etas)):
        lhs, rhs = one_plus_eta_f(beta, e, mu * q, eta)
        assert_close(f"one-plus-eta identity {index}", lhs, rhs)

    loss = f[0] * f[1] * (1.0 + etas[2] * f[2]) * (1.0 + etas[3] * f[3])
    gain = f[2] * f[3] * (1.0 + etas[0] * f[0]) * (1.0 + etas[1] * f[1])
    assert_close("detailed balance", loss, gain)


def check_h_theorem_integrand() -> None:
    pairs = [(0.8, 0.3), (0.2, 1.4), (2.0, 2.0)]
    for index, (x, y) in enumerate(pairs):
        entropy_integrand = (x - y) * math.log(x / y)
        if entropy_integrand < -1.0e-14:
            raise AssertionError(f"H-theorem integrand {index} negative: {entropy_integrand}")


def check_linearized_collision_positive_form() -> None:
    weight = 0.37
    chi = [0.2, -0.4, 0.1, 0.6]
    delta = chi[0] + chi[1] - chi[2] - chi[3]
    quadratic_form = weight * delta * delta / 4.0
    assert quadratic_form >= 0.0

    alpha, beta, gamma = 0.3, -0.7, 0.5
    energies = [1.1, 0.9, 0.7, 1.3]
    charges = [1.0, -0.2, 0.4, 0.4]
    invariant = [alpha + beta * e + gamma * q for e, q in zip(energies, charges)]
    invariant_delta = invariant[0] + invariant[1] - invariant[2] - invariant[3]
    assert_close("collision invariant null vector", invariant_delta, 0.0)


def check_finite_collision_algebra_exact() -> None:
    etas = [1, -1, 1, -1]
    # Work with a_i = f_i / (1 + eta_i f_i).  The selected values satisfy
    # a_0 a_1 = a_2 a_3, hence detailed balance for 0+1 <-> 2+3.
    a_values = [sp.Rational(1, 3), sp.Rational(1, 5), sp.Rational(1, 6), sp.Rational(2, 5)]
    f0 = [
        a / (1 - eta * a)
        for a, eta in zip(a_values, etas)
    ]
    loss0 = f0[0] * f0[1] * (1 + etas[2] * f0[2]) * (1 + etas[3] * f0[3])
    gain0 = f0[2] * f0[3] * (1 + etas[0] * f0[0]) * (1 + etas[1] * f0[1])
    if sp.simplify(loss0 - gain0) != 0:
        raise AssertionError("finite detailed balance failed")

    t = sp.symbols("t")
    chi = [sp.Rational(2, 7), sp.Rational(-1, 3), sp.Rational(5, 11), sp.Rational(1, 13)]
    f = [base + t * base * (1 + eta * base) * variation for base, eta, variation in zip(f0, etas, chi)]
    loss = f[0] * f[1] * (1 + etas[2] * f[2]) * (1 + etas[3] * f[3])
    gain = f[2] * f[3] * (1 + etas[0] * f[0]) * (1 + etas[1] * f[1])
    linear_rate = sp.diff(loss - gain, t).subs(t, 0)
    expected_linear_rate = loss0 * (chi[0] + chi[1] - chi[2] - chi[3])
    if sp.simplify(linear_rate - expected_linear_rate) != 0:
        raise AssertionError("finite linearized collision rate failed")

    p_values = [sp.Rational(3, 2), sp.Rational(5, 4), sp.Rational(7, 4), sp.Rational(1, 1)]
    assert sp.simplify(p_values[0] + p_values[1] - p_values[2] - p_values[3]) == 0
    alpha = sp.Rational(4, 9)
    beta = sp.Rational(-2, 5)
    invariant = [alpha + beta * momentum for momentum in p_values]
    invariant_delta = invariant[0] + invariant[1] - invariant[2] - invariant[3]
    if sp.simplify(invariant_delta) != 0:
        raise AssertionError("finite collision invariant failed")


def check_relaxation_time_shear_integral() -> None:
    temperature = 0.8
    tau = 1.6
    pressure = temperature**4 / (math.pi * math.pi)

    integral_p2 = 12.0 * temperature**5 / (math.pi * math.pi)
    eta = tau * integral_p2 / (15.0 * temperature)
    assert_close("RTA shear viscosity", eta, 4.0 * pressure * tau / 5.0)

    pressure_integral = (1.0 / 3.0) * (1.0 / (2.0 * math.pi * math.pi)) * 6.0 * temperature**4
    assert_close("massless Boltzmann pressure", pressure_integral, pressure)


def main() -> None:
    check_detailed_balance()
    check_h_theorem_integrand()
    check_linearized_collision_positive_form()
    check_finite_collision_algebra_exact()
    check_relaxation_time_shear_integral()
    print("All kinetic-theory controlled-limit checks passed.")


if __name__ == "__main__":
    main()
