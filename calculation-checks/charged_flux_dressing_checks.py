#!/usr/bin/env python3
"""Finite checks for charged Wilson-line dressing and flux formulas."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def dot_mostly_plus(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
    return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def boosted_flux_density(q: float, beta: float, z: float) -> float:
    return q / (4.0 * math.pi) * (1.0 - beta * beta) / (1.0 - beta * z) ** 2


def boosted_flux_integral(q: float, beta: float) -> float:
    if beta == 0.0:
        return q
    integral_without_q = (
        2.0
        * math.pi
        * (1.0 - beta * beta)
        * (1.0 / (beta * (1.0 - beta)) - 1.0 / (beta * (1.0 + beta)))
    )
    return q / (4.0 * math.pi) * integral_without_q


def check_boosted_flux_integral() -> None:
    for q in (-3.0, -0.5, 0.25, 2.0):
        for beta in (0.0, 0.1, 0.4, 0.8):
            assert_close(f"boosted Coulomb total flux q={q} beta={beta}", boosted_flux_integral(q, beta), q)


def check_velocity_read_from_flux_extrema() -> None:
    q = 1.7
    for beta in (0.05, 0.2, 0.6, 0.9):
        maximum = boosted_flux_density(q, beta, 1.0)
        minimum = boosted_flux_density(q, beta, -1.0)
        expected_ratio = ((1.0 + beta) / (1.0 - beta)) ** 2
        assert_close(f"flux extrema ratio beta={beta}", maximum / minimum, expected_ratio)


def check_worldline_current_denominator() -> None:
    mass = 2.3
    charge = -0.7
    eps = 0.13
    omega = 0.31
    velocity = (0.2, -0.35, 0.1)
    speed_sq = sum(component * component for component in velocity)
    gamma = 1.0 / math.sqrt(1.0 - speed_sq)
    p = (gamma * mass, *(gamma * mass * component for component in velocity))
    u = tuple(component / mass for component in p)

    n = (0.0, 0.6, 0.8)
    k = (omega, *(omega * component for component in n))
    polarization = (0.0, 1.0, 0.0, 0.0)
    assert_close("photon null", dot_mostly_plus(k, k), 0.0)
    assert_close("polarization transverse", dot_mostly_plus(k, polarization), 0.0)

    current_contraction = charge * dot_mostly_plus(u, polarization) / (eps - 1j * dot_mostly_plus(u, k))
    momentum_contraction = charge * dot_mostly_plus(p, polarization) / (
        eps * mass - 1j * dot_mostly_plus(p, k)
    )
    assert_close("worldline current equals momentum eikonal denominator", current_contraction, momentum_contraction)


def check_half_line_fourier_transform() -> None:
    eps = 0.37
    a = -0.42
    analytic = 1.0 / (eps - 1j * a)
    large_t = 100.0
    cutoff_integral = (cmath.exp((-eps + 1j * a) * large_t) - 1.0) / (-eps + 1j * a)
    assert_close("regulated half-line transform", cutoff_integral, analytic, tol=1.0e-15)


def main() -> None:
    check_boosted_flux_integral()
    check_velocity_read_from_flux_extrema()
    check_worldline_current_denominator()
    check_half_line_fourier_transform()
    print("All charged flux and Wilson-line dressing checks passed.")


if __name__ == "__main__":
    main()
