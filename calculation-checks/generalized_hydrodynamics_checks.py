#!/usr/bin/env python3
"""Finite algebra checks for the generalized-hydrodynamics bridge."""

from __future__ import annotations

from fractions import Fraction


def assert_close(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def solve_2x2(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        raise AssertionError("singular two-by-two dressing matrix")
    return [
        (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / det,
        (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / det,
    ]


def check_two_species_dressing_current_identity() -> None:
    # Finite-grid version of h^dr = h + K n h^dr.
    kernel = [
        [Fraction(1, 5), Fraction(-1, 7)],
        [Fraction(2, 9), Fraction(1, 6)],
    ]
    filling = [Fraction(1, 3), Fraction(2, 5)]
    p_prime = [Fraction(7, 3), Fraction(5, 2)]
    e_prime = [Fraction(4, 3), Fraction(-3, 2)]
    charge = [Fraction(2, 1), Fraction(-1, 3)]

    dressing_matrix = [
        [
            (Fraction(1) if i == j else Fraction(0)) - kernel[i][j] * filling[j]
            for j in range(2)
        ]
        for i in range(2)
    ]
    p_dr = solve_2x2(dressing_matrix, p_prime)
    e_dr = solve_2x2(dressing_matrix, e_prime)
    charge_dr = solve_2x2(dressing_matrix, charge)

    for i in range(2):
        reconstructed = charge[i] + sum(kernel[i][j] * filling[j] * charge_dr[j] for j in range(2))
        assert_close(f"dressing equation component {i}", charge_dr[i], reconstructed)

    # Ignore the common 2*pi factor: rho_i = n_i (p'_i)^dr and
    # rho_i v_i^eff = n_i (E'_i)^dr.
    root_density = [filling[i] * p_dr[i] for i in range(2)]
    velocity = [e_dr[i] / p_dr[i] for i in range(2)]
    current_from_velocity = sum(charge[i] * root_density[i] * velocity[i] for i in range(2))
    current_from_dressed_energy = sum(charge[i] * filling[i] * e_dr[i] for i in range(2))
    assert_close("GHD charge current identity", current_from_velocity, current_from_dressed_energy)


def check_hard_rod_effective_velocity_solution() -> None:
    length = Fraction(1, 3)
    velocities = [Fraction(-2, 1), Fraction(1, 1), Fraction(5, 1)]
    densities = [Fraction(1, 10), Fraction(1, 5), Fraction(1, 8)]
    total_density = sum(densities)
    assert length * total_density < 1

    bare_current = sum(rho * velocity for rho, velocity in zip(densities, velocities, strict=True))
    effective = [
        (velocity - length * bare_current) / (1 - length * total_density)
        for velocity in velocities
    ]
    effective_current = sum(rho * velocity for rho, velocity in zip(densities, effective, strict=True))
    assert_close("hard-rod effective current equals bare velocity density", effective_current, bare_current)

    for i, velocity in enumerate(velocities):
        rhs = velocity + length * sum(
            densities[j] * (effective[i] - effective[j]) for j in range(len(velocities))
        )
        assert_close(f"hard-rod effective velocity equation {i}", effective[i], rhs)


def main() -> None:
    check_two_species_dressing_current_identity()
    check_hard_rod_effective_velocity_solution()
    print("All generalized-hydrodynamics finite algebra checks passed.")


if __name__ == "__main__":
    main()
