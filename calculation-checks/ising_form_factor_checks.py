#!/usr/bin/env python3
"""Finite checks for the free-Majorana/Ising form-factor examples."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def energy_form_factor(theta_1: complex, theta_2: complex, kappa: complex = 1.0) -> complex:
    return kappa * cmath.sinh((theta_1 - theta_2) / 2.0)


def tanh_product(thetas: list[complex]) -> complex:
    result = 1.0 + 0.0j
    for i, theta_i in enumerate(thetas):
        for theta_j in thetas[i + 1 :]:
            result *= cmath.tanh((theta_i - theta_j) / 2.0)
    return result


def sigma_form_factor(thetas: list[complex], v: complex = 1.0) -> complex:
    n = len(thetas)
    if n % 2 == 0:
        return 0.0 + 0.0j
    k = (n - 1) // 2
    return v * (1j**k) * tanh_product(thetas)


def swapped(values: list[complex], i: int) -> list[complex]:
    out = values[:]
    out[i], out[i + 1] = out[i + 1], out[i]
    return out


def check_energy_density_form_factor() -> None:
    theta_1 = 0.73
    theta_2 = -0.41
    assert_close(
        "energy exchange",
        energy_form_factor(theta_1, theta_2),
        -energy_form_factor(theta_2, theta_1),
    )
    assert_close(
        "energy cyclicity",
        energy_form_factor(theta_1 + 2j * math.pi, theta_2),
        energy_form_factor(theta_2, theta_1),
    )


def check_energy_two_particle_reconstruction() -> None:
    mass = 1.7
    kappa = 2.3
    theta_1 = 0.94
    theta_2 = -0.38
    alpha = theta_1 - theta_2

    def momentum(theta: float) -> tuple[float, float]:
        return (mass * math.cosh(theta), mass * math.sinh(theta))

    p_1 = momentum(theta_1)
    p_2 = momentum(theta_2)
    total = (p_1[0] + p_2[0], p_1[1] + p_2[1])
    invariant_s = total[0] ** 2 - total[1] ** 2
    assert_close(
        "two-particle invariant mass",
        invariant_s,
        4.0 * mass**2 * math.cosh(alpha / 2.0) ** 2,
    )

    ff_squared = abs(energy_form_factor(theta_1, theta_2, kappa)) ** 2
    assert_close(
        "energy form factor as invariant numerator",
        ff_squared,
        kappa**2 * (invariant_s - 4.0 * mass**2) / (4.0 * mass**2),
    )

    jacobian = math.sqrt(invariant_s) * mass * abs(math.sinh(alpha / 2.0))
    delta_integral_after_identical_particle_cancellation = ff_squared / jacobian
    spectral_density = kappa**2 / (2.0 * mass**2) * math.sqrt(1.0 - 4.0 * mass**2 / invariant_s)
    assert_close(
        "two-particle spectral density normalization",
        delta_integral_after_identical_particle_cancellation,
        spectral_density,
    )

    starting_euclidean_prefactor = 1.0 / (2.0 * (2.0 * math.pi) ** 2)
    after_bessel_reduction_full_alpha = 2.0 * starting_euclidean_prefactor
    after_even_alpha_reduction = 2.0 * after_bessel_reduction_full_alpha
    assert_close(
        "Euclidean Bessel prefactor",
        after_even_alpha_reduction,
        1.0 / (2.0 * math.pi**2),
    )


def check_sigma_exchange_and_cyclicity() -> None:
    thetas = [1.31, 0.62, -0.17, -0.84, -1.55]
    for i in range(len(thetas) - 1):
        assert_close(
            f"sigma Watson exchange slot {i}",
            sigma_form_factor(thetas),
            -sigma_form_factor(swapped(thetas, i)),
        )

    shifted = [thetas[0] + 2j * math.pi, *thetas[1:]]
    cycled = [*thetas[1:], thetas[0]]
    assert_close("sigma odd cyclicity", sigma_form_factor(shifted), sigma_form_factor(cycled))


def check_sigma_kinematic_residue() -> None:
    theta = 0.37
    for spectators in ([0.91], [1.44, 0.52, -0.66], [1.7, 0.83, 0.11, -0.47, -1.28]):
        n = len(spectators)
        big_n = n + 2
        residue = 2.0 * (1j ** ((big_n - 1) // 2)) * tanh_product([complex(x) for x in spectators])
        lhs = -1j * residue
        rhs = (1.0 - (-1.0) ** n) * sigma_form_factor([complex(x) for x in spectators])
        assert_close(f"sigma analytic kinematic residue n={n}", lhs, rhs)

        eps = 1.0e-7
        near_pair = [theta + 1j * math.pi + eps, theta, *spectators]
        numerical_residue = eps * sigma_form_factor([complex(x) for x in near_pair])
        assert_close(f"sigma numerical kinematic residue n={n}", numerical_residue, residue, tol=1.0e-6)


def main() -> None:
    check_energy_density_form_factor()
    check_energy_two_particle_reconstruction()
    check_sigma_exchange_and_cyclicity()
    check_sigma_kinematic_residue()
    print("All Ising form-factor checks passed.")


if __name__ == "__main__":
    main()
