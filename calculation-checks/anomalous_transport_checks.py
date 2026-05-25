#!/usr/bin/env python3
"""Coefficient checks for the anomalous-transport chapter."""

from __future__ import annotations

import math


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-12) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_chiral_magnetic_coefficients() -> None:
    mu_v = 0.7
    mu_a = 0.23
    mu_r = mu_v + mu_a
    mu_l = mu_v - mu_a
    pi2 = math.pi * math.pi

    right = mu_r / (4.0 * pi2)
    left = -mu_l / (4.0 * pi2)
    vector = right + left
    axial = right - left

    assert_close("source-normalized vector CME", vector, mu_a / (2.0 * pi2))
    assert_close("source-normalized axial CME", axial, mu_v / (2.0 * pi2))

    charge = 1.9
    physical_vector = charge * charge * vector
    assert_close("electromagnetic CME charge factor", physical_vector, charge * charge * mu_a / (2.0 * pi2))


def check_equilibrium_cs_variation() -> None:
    mu_a = 0.41
    pi2 = math.pi * math.pi
    cs_coefficient = mu_a / (4.0 * pi2)
    current_coefficient = 2.0 * cs_coefficient
    assert_close("CS variation gives CME", current_coefficient, mu_a / (2.0 * pi2))


def check_chiral_vortical_coefficients() -> None:
    mu_v = 0.61
    mu_a = 0.19
    temp = 0.37
    mu_r = mu_v + mu_a
    mu_l = mu_v - mu_a
    pi2 = math.pi * math.pi

    right = mu_r * mu_r / (4.0 * pi2) + temp * temp / 12.0
    left = -(mu_l * mu_l / (4.0 * pi2) + temp * temp / 12.0)
    vector = right + left
    axial = right - left

    assert_close("vector CVE", vector, mu_v * mu_a / pi2)
    assert_close("axial CVE", axial, (mu_v * mu_v + mu_a * mu_a) / (2.0 * pi2) + temp * temp / 6.0)

    vector_temperature_piece = temp * temp / 12.0 - temp * temp / 12.0
    assert_close("no vector T^2 term for Dirac pair", vector_temperature_piece, 0.0)


def main() -> None:
    check_chiral_magnetic_coefficients()
    check_equilibrium_cs_variation()
    check_chiral_vortical_coefficients()
    print("All anomalous-transport coefficient checks passed.")


if __name__ == "__main__":
    main()
