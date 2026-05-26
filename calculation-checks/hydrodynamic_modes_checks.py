#!/usr/bin/env python3
"""Finite algebra checks for Volume X hydrodynamic Ward-identity modes."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def shear_pole(eta: float, enthalpy: float, k: float) -> complex:
    return -1j * eta * k * k / enthalpy


def sound_roots(cs2: float, attenuation: float, k: float) -> tuple[complex, complex]:
    # Roots of omega^2 - c_s^2 k^2 + i Gamma omega k^2 = 0.
    b = 1j * attenuation * k * k
    c = -cs2 * k * k
    root = cmath.sqrt(b * b - 4.0 * c)
    return ((-b + root) / 2.0, (-b - root) / 2.0)


def check_shear_mode() -> None:
    eta = 0.63
    enthalpy = 2.7
    k = 0.004
    omega = shear_pole(eta, enthalpy, k)
    assert_close("shear dispersion equation", -1j * omega * enthalpy + eta * k * k, 0.0)
    assert omega.imag < 0.0
    assert_close("shear diffusion constant", -omega.imag / (k * k), eta / enthalpy)


def check_sound_mode_expansion() -> None:
    d = 3
    eta = 0.41
    zeta = 0.08
    enthalpy = 1.9
    cs2 = 0.31
    k = 1.0e-4
    gamma = (zeta + 2.0 * eta * (d - 1.0) / d) / enthalpy
    roots = sound_roots(cs2, gamma, k)
    cs = math.sqrt(cs2)
    expected = (cs * k - 0.5j * gamma * k * k, -cs * k - 0.5j * gamma * k * k)
    assert_close("sound plus expansion", roots[0], expected[0], tol=2.0e-12)
    assert_close("sound minus expansion", roots[1], expected[1], tol=2.0e-12)
    for root in roots:
        assert root.imag < 0.0
        assert_close(
            "sound quadratic equation",
            root * root - cs2 * k * k + 1j * gamma * root * k * k,
            0.0,
            tol=1.0e-18,
        )


def check_entropy_production_coefficients() -> None:
    temperature = 1.7
    eta = 0.5
    zeta = 0.2
    theta = -0.3
    # Symmetric traceless shear sample in three spatial dimensions.
    sigma2 = 0.11**2 + (-0.04) ** 2 + (-0.07) ** 2 + 2.0 * 0.03**2
    grad_alpha = [0.2, -0.1]
    conductivity = [[0.7, 0.05], [0.05, 0.4]]
    charge_term = temperature * sum(
        conductivity[i][j] * grad_alpha[i] * grad_alpha[j]
        for i in range(2)
        for j in range(2)
    )
    entropy_production = eta * sigma2 / (2.0 * temperature) + zeta * theta * theta / temperature + charge_term
    assert entropy_production > 0.0

    determinant = conductivity[0][0] * conductivity[1][1] - conductivity[0][1] ** 2
    assert conductivity[0][0] >= 0.0
    assert determinant >= 0.0


def check_diffusion_einstein_relation_and_pole() -> None:
    sigma = 0.76
    chi = 1.9
    diffusion = sigma / chi
    k = 0.003
    omega = -1j * diffusion * k * k
    assert_close("diffusion pole denominator", diffusion * k * k - 1j * omega, 0.0)
    assert omega.imag < 0.0

    # Static limit of chi * D k^2/(D k^2 - i omega) at omega=0.
    static_response = chi * diffusion * k * k / (diffusion * k * k)
    assert_close("static susceptibility from diffusion correlator", static_response, chi)


def main() -> None:
    check_shear_mode()
    check_sound_mode_expansion()
    check_entropy_production_coefficients()
    check_diffusion_einstein_relation_and_pole()
    print("All hydrodynamic Ward-identity mode checks passed.")


if __name__ == "__main__":
    main()
