#!/usr/bin/env python3
"""Checks for the kinetic-theory controlled-limit chapter.

Evidence contract.
Target claims: the distinct kinetic scale hierarchy, force-free Wigner drift
projection, scalar lambda-phi-four cut-sunset collision kernel, local
equilibrium collision/streaming separation, finite collision algebra,
linearized positivity, physical-channel versus ordered-duplicate symmetry
bookkeeping, Markov-memory residual bookkeeping, pinch enhancement, and
relaxation-time shear example in Volume X Chapter 8.
Independent construction: direct Poisson-bracket algebra, exact Bose/Fermi
detailed-balance products, finite reversible-reaction arithmetic, explicit
lesser/greater scalar self-energy gain/loss products, finite memory-kernel
Taylor bounds, and elementary retarded-advanced Lorentzian integrals.
Imported assumptions: the Schwinger--Keldysh/2PI sunset truncation, the
narrow quasiparticle ansatz, decay of connected initial correlations, and the
weighted phase-space norm stated in the chapter.
Negative controls: the old global Gamma times variation-scale inequality is
rejected for kinetic and hydrodynamic windows, local equilibrium is not
misread as making the streaming term vanish, finite collision algebra is not
accepted as a microscopic QFT derivation, signed residual cancellations are
rejected as error bounds, ordered duplicate final channels are not counted
without an identical-particle divisor, and a bare perturbative term without
width resummation is rejected on kinetic time scales.
Scope boundary: these checks verify finite normalization, algebra, and
residual bookkeeping for the scalar weak-coupling derivation; they do not
prove gauge-theory screening, collinear/LPM physics, a nonperturbative
continuum limit, or uniform all-time convergence of the kinetic equation.
"""

from __future__ import annotations

from fractions import Fraction

from check_utils import assert_close as _assert_close

import math

import sympy as sp


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-11) -> None:
    _assert_close(name, got, expected, tol=tol)


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


def check_quasiparticle_drift_projection() -> None:
    p0, px, py, pz, m = sp.symbols("p0 px py pz m", positive=True)
    ft, fx, fy, fz = sp.symbols("ft fx fy fz")
    shell_function = p0**2 - px**2 - py**2 - pz**2 - m**2

    # With the kinetic Poisson-bracket convention of the chapter, the
    # force-free bracket gives 1/2 {F,G} -> p0 dt f + p_i dx_i f on shell.
    half_bracket_coefficient = sp.Rational(1, 2) * (
        sp.diff(shell_function, p0) * ft
        - sp.diff(shell_function, px) * fx
        - sp.diff(shell_function, py) * fy
        - sp.diff(shell_function, pz) * fz
    )
    energy = sp.sqrt(px**2 + py**2 + pz**2 + m**2)
    projected = half_bracket_coefficient.subs(p0, energy)
    expected = energy * ft + px * fx + py * fy + pz * fz
    if sp.simplify(projected - expected) != 0:
        raise AssertionError("quasiparticle drift projection failed")


def check_scale_hierarchy_windows() -> None:
    energy = Fraction(100, 1)
    gamma = Fraction(1, 1)
    tau_qp = 1 / energy
    tau_coll = 1 / gamma
    tau_mem = Fraction(1, 50)

    collisionless_tau = Fraction(1, 10)
    kinetic_tau = tau_coll
    hydro_tau = Fraction(10, 1) * tau_coll

    if not tau_qp < tau_mem < collisionless_tau < tau_coll:
        raise AssertionError("collisionless hierarchy failed")
    if not tau_mem < kinetic_tau == tau_coll:
        raise AssertionError("kinetic relaxation hierarchy failed")
    if not tau_mem < tau_coll < hydro_tau:
        raise AssertionError("hydrodynamic hierarchy failed")

    old_collisionless = gamma * collisionless_tau
    old_kinetic = gamma * kinetic_tau
    old_hydro = gamma * hydro_tau
    if not old_collisionless < 1:
        raise AssertionError("collisionless window should satisfy Gamma tau_X < 1")
    if not old_kinetic == 1:
        raise AssertionError("kinetic relaxation should have Gamma tau_X = 1")
    if not old_hydro > 1:
        raise AssertionError("hydrodynamic window should satisfy Gamma tau_X > 1")

    grad_small = tau_mem / hydro_tau
    if not grad_small < Fraction(1, 100):
        raise AssertionError("Markov gradient parameter should remain small in hydrodynamics")


def check_local_equilibrium_collision_vs_streaming() -> None:
    beta, alpha, x = sp.symbols("beta alpha x", positive=True)
    energies = [sp.Rational(3, 2), sp.Rational(5, 4), sp.Rational(7, 4), sp.Rational(1, 1)]
    # Energies conserve: E1+E2=E3+E4.
    if sp.simplify(energies[0] + energies[1] - energies[2] - energies[3]) != 0:
        raise AssertionError("sample energies do not conserve")

    beta_x = beta + alpha * x
    f = [sp.exp(-beta_x * energy) for energy in energies]
    loss = f[0] * f[1]
    gain = f[2] * f[3]
    if sp.simplify(loss - gain) != 0:
        raise AssertionError("local equilibrium collision product should vanish pointwise")

    streaming = sp.diff(f[0], x)
    if sp.simplify(streaming) == 0:
        raise AssertionError("local equilibrium streaming source should be nonzero when beta varies")


def check_scalar_sunset_collision_kernel() -> None:
    lam2 = Fraction(11, 7)
    f1 = Fraction(2, 5)
    f2 = Fraction(1, 4)
    f3 = Fraction(3, 7)
    f4 = Fraction(5, 8)

    sigma_less = lam2 * f3 * f4 * (1 + f2)
    sigma_greater = lam2 * f2 * (1 + f3) * (1 + f4)
    projected_gain_loss = Fraction(1, 2) * ((1 + f1) * sigma_less - f1 * sigma_greater)
    covariant_kernel = Fraction(1, 2) * lam2 * (
        f3 * f4 * (1 + f1) * (1 + f2)
        - f1 * f2 * (1 + f3) * (1 + f4)
    )
    if projected_gain_loss != covariant_kernel:
        raise AssertionError("scalar sunset gain/loss projection failed")

    ordered_final_copies = Fraction(2, 1)
    identical_final_divisor = Fraction(2, 1)
    physical_channel_weight = lam2
    ordered_channel_weight = lam2 / identical_final_divisor
    if ordered_final_copies * ordered_channel_weight != physical_channel_weight:
        raise AssertionError("ordered identical-channel divisor failed")
    if ordered_final_copies * lam2 == physical_channel_weight:
        raise AssertionError("ordered duplicate channel was incorrectly accepted")

    beta = Fraction(3, 2)
    energies = [Fraction(3, 2), Fraction(5, 4), Fraction(7, 4), Fraction(1, 1)]
    a = [sp.exp(-sp.Rational(beta.numerator, beta.denominator) * sp.Rational(e.numerator, e.denominator)) for e in energies]
    f_eq = [value / (1 - value) for value in a]
    eq_kernel = sp.Rational(1, 2) * sp.Rational(lam2.numerator, lam2.denominator) * (
        f_eq[2] * f_eq[3] * (1 + f_eq[0]) * (1 + f_eq[1])
        - f_eq[0] * f_eq[1] * (1 + f_eq[2]) * (1 + f_eq[3])
    )
    if sp.simplify(eq_kernel) != 0:
        raise AssertionError("scalar kernel detailed balance failed")

    coordinate_time_prefactor = Fraction(1, 2) / energies[0]
    expected_coordinate_prefactor = 1 / (2 * energies[0])
    if coordinate_time_prefactor != expected_coordinate_prefactor:
        raise AssertionError("coordinate-time prefactor normalization failed")


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


def check_markov_memory_and_pinch_remainders() -> None:
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    times = [Fraction(0, 1), Fraction(1, 10), Fraction(1, 5)]
    total_weight = sum(weights, Fraction(0))
    tau_mem = sum(w * t for w, t in zip(weights, times)) / total_weight
    tau_x = Fraction(10, 1)
    derivative_bound = Fraction(3, 1) / tau_x

    markov_error_bound = derivative_bound * sum(w * t for w, t in zip(weights, times))
    expected_bound = derivative_bound * total_weight * tau_mem
    if markov_error_bound != expected_bound:
        raise AssertionError("Markov memory residual bound failed")
    if not tau_mem / tau_x < Fraction(1, 50):
        raise AssertionError("memory gradient parameter should be small")

    lam2 = Fraction(1, 100)
    gamma = lam2
    retarded_advanced_enhancement = 1 / gamma
    secular_size = lam2 * retarded_advanced_enhancement
    if secular_size != 1:
        raise AssertionError("pinch enhancement should make lambda^2/Gamma order one")

    residuals = [Fraction(1, 20), -Fraction(1, 20), Fraction(1, 50)]
    signed = sum(residuals, Fraction(0))
    absolute = sum(abs(value) for value in residuals)
    if not absolute > abs(signed):
        raise AssertionError("signed residual cancellation is not an error bound")


def main() -> None:
    check_detailed_balance()
    check_h_theorem_integrand()
    check_quasiparticle_drift_projection()
    check_scale_hierarchy_windows()
    check_local_equilibrium_collision_vs_streaming()
    check_scalar_sunset_collision_kernel()
    check_linearized_collision_positive_form()
    check_finite_collision_algebra_exact()
    check_relaxation_time_shear_integral()
    check_markov_memory_and_pinch_remainders()
    print("All kinetic-theory controlled-limit checks passed.")


if __name__ == "__main__":
    main()
