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


def dot3(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def transverse_projection(a: tuple[float, float, float], n: tuple[float, float, float]) -> tuple[float, float, float]:
    an = dot3(a, n)
    return tuple(a_i - an * n_i for a_i, n_i in zip(a, n))


def soft_velocity_vector(
    velocity: tuple[float, float, float],
    n: tuple[float, float, float],
) -> tuple[float, float, float]:
    denominator = 1.0 - dot3(velocity, n)
    return tuple(component / denominator for component in transverse_projection(velocity, n))


def soft_angular_integrand(
    velocity_a: tuple[float, float, float],
    velocity_b: tuple[float, float, float],
    n: tuple[float, float, float],
) -> float:
    soft_a = soft_velocity_vector(velocity_a, n)
    soft_b = soft_velocity_vector(velocity_b, n)
    difference = tuple(a - b for a, b in zip(soft_a, soft_b))
    return dot3(difference, difference)


def angular_soft_coefficient(
    velocity_a: tuple[float, float, float],
    velocity_b: tuple[float, float, float],
    n_theta: int = 40,
    n_phi: int = 80,
) -> float:
    total = 0.0
    dz = 2.0 / n_theta
    dphi = 2.0 * math.pi / n_phi
    for i in range(n_theta):
        z = -1.0 + (i + 0.5) * dz
        radius = math.sqrt(max(0.0, 1.0 - z * z))
        for j in range(n_phi):
            phi = (j + 0.5) * dphi
            n = (radius * math.cos(phi), radius * math.sin(phi), z)
            total += soft_angular_integrand(velocity_a, velocity_b, n) * dz * dphi
    return total


def check_soft_profile_velocity_separation() -> None:
    samples = [
        ((0.2, 0.0, 0.0), (0.2, 0.0, 0.0), 0.0),
        ((0.2, 0.0, 0.0), (0.4, 0.0, 0.0), None),
        ((0.1, -0.2, 0.0), (0.1, -0.2, 0.0), 0.0),
        ((0.1, -0.2, 0.0), (-0.15, 0.05, 0.25), None),
    ]
    for velocity_a, velocity_b, expected in samples:
        coefficient = angular_soft_coefficient(velocity_a, velocity_b)
        label = f"soft angular coefficient {velocity_a} {velocity_b}"
        if expected is not None:
            assert_close(label, coefficient, expected, tol=1.0e-12)
        elif coefficient <= 1.0e-4:
            raise AssertionError(f"{label} failed: coefficient should be positive, got {coefficient!r}")

    charge = 0.7
    ir_cutoff = 1.0e-3
    uv_cutoff = 0.8
    coefficient = angular_soft_coefficient((0.2, 0.0, 0.0), (0.4, 0.0, 0.0))
    norm_difference = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (2.0 * (2.0 * math.pi) ** 3)
    expected = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (16.0 * math.pi**3)
    assert_close("soft coherent norm log prefactor", norm_difference, expected)


def inner_complex(a: tuple[complex, ...], b: tuple[complex, ...]) -> complex:
    return sum(x.conjugate() * y for x, y in zip(a, b))


def norm_sq_complex(a: tuple[complex, ...]) -> float:
    return inner_complex(a, a).real


def sigma_complex(a: tuple[complex, ...], b: tuple[complex, ...]) -> float:
    return 2.0 * inner_complex(a, b).imag


def coherent_weyl_characteristic(F: tuple[complex, ...], f: tuple[complex, ...]) -> complex:
    return cmath.exp(1j * sigma_complex(F, f)) * math.exp(-0.5 * norm_sq_complex(f))


def check_weyl_characteristic_and_overlap_decay() -> None:
    F = (1.0 + 0.3j, -0.4 + 0.7j, 0.2 - 0.1j)
    G = (-0.2 + 0.8j, 0.1 - 0.5j, 0.6 + 0.4j)
    f = (0.3 - 0.1j, -0.6 + 0.2j, 0.05 + 0.4j)

    expected_modulus = math.exp(-0.5 * norm_sq_complex(f))
    assert_close("coherent Weyl state modulus", abs(coherent_weyl_characteristic(F, f)), expected_modulus)

    difference = tuple(x - y for x, y in zip(F, G))
    coherent_overlap_abs = math.exp(-0.5 * norm_sq_complex(difference))
    expected_overlap_abs = math.exp(-0.5 * norm_sq_complex(difference))
    assert_close("coherent-vector overlap formula", coherent_overlap_abs, expected_overlap_abs)

    charge = 1.0
    uv_cutoff = 1.0
    coefficient = angular_soft_coefficient((0.2, 0.0, 0.0), (0.4, 0.0, 0.0))
    def overlap(ir_cutoff: float) -> float:
        norm_sq = charge * charge * coefficient * math.log(uv_cutoff / ir_cutoff) / (2.0 * (2.0 * math.pi) ** 3)
        return math.exp(-0.5 * norm_sq)

    if not overlap(1.0e-6) < overlap(1.0e-3) < overlap(1.0e-1):
        raise AssertionError("IR coherent overlap should decrease as the infrared cutoff is removed")


def main() -> None:
    check_boosted_flux_integral()
    check_velocity_read_from_flux_extrema()
    check_worldline_current_denominator()
    check_half_line_fourier_transform()
    check_soft_profile_velocity_separation()
    check_weyl_characteristic_and_overlap_decay()
    print("All charged flux and Wilson-line dressing checks passed.")


if __name__ == "__main__":
    main()
