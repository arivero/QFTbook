#!/usr/bin/env python3
"""Finite checks for continuum-limit and scaling-window normalizations."""

from __future__ import annotations

import math


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-11) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def lattice_hat_p_squared(a: float, p: list[float]) -> float:
    return (4.0 / a**2) * sum(math.sin(0.5 * a * component) ** 2 for component in p)


def check_lattice_laplacian_expansion() -> None:
    a = 1.0e-3
    p = [0.7, -1.2, 0.4]
    p2 = sum(component**2 for component in p)
    p4sum = sum(component**4 for component in p)
    expansion = p2 - (a**2 / 12.0) * p4sum
    assert_close("lattice momentum expansion", lattice_hat_p_squared(a, p), expansion, tol=1.0e-12)


def check_tree_level_symanzik_artifact_and_improvement() -> None:
    a = 1.0e-4
    p = [0.6, -0.8, 1.1]
    mass = 1.4
    p2 = sum(component**2 for component in p)
    p4sum = sum(component**4 for component in p)
    continuum_denominator = p2 + mass * mass

    propagator = 1.0 / (lattice_hat_p_squared(a, p) + mass * mass)
    continuum = 1.0 / continuum_denominator
    artifact_coefficient = (propagator - continuum) / (a * a)
    expected_artifact = p4sum / (12.0 * continuum_denominator * continuum_denominator)
    assert_close("tree-level Symanzik propagator artifact", artifact_coefficient, expected_artifact, tol=1.0e-7)

    hat_components = [(2.0 / a) * math.sin(0.5 * a * component) for component in p]
    improved_kernel = mass * mass + lattice_hat_p_squared(a, p) + (a * a / 12.0) * sum(
        component**4 for component in hat_components
    )
    improved_artifact = (improved_kernel - continuum_denominator) / (a * a)
    assert_close("tree-level improved kernel cancels O(a^2)", improved_artifact, 0.0, tol=1.0e-7)


def check_free_scalar_pole_mass() -> None:
    a = 2.0e-4
    mass = 1.3
    kappa = (2.0 / a) * math.asinh(0.5 * a * mass)
    expansion = mass - (a**2 * mass**3) / 24.0
    assert_close("lattice pole mass expansion", kappa, expansion, tol=1.0e-14)

    xi_lattice = 1.0 / (a * kappa)
    physical_xi = a * xi_lattice
    assert_close("physical correlation length", physical_xi, 1.0 / kappa)
    assert abs(physical_xi - 1.0 / mass) < 1.0e-8


def check_gaussian_relevant_scaling() -> None:
    b = 3.0
    y_mass_squared = 2.0
    dimensionless_mass_squared = 0.004
    blocked = (b**y_mass_squared) * dimensionless_mass_squared
    expected = (b**2) * dimensionless_mass_squared
    assert_close("Gaussian mass-squared RG eigenvalue", blocked, expected)

    y_t = 1.6
    t0 = 1.0e-5
    steps = -math.log(t0) / (y_t * math.log(b))
    xi = b**steps
    assert_close("nu equals inverse thermal eigenvalue", xi, t0 ** (-1.0 / y_t), tol=1.0e-9)


def check_finite_size_scaling_variables() -> None:
    b = 2.0
    steps = 6
    size_in_lattice_units = b**steps
    y_t = 1.6
    omega = 0.83
    microscopic_relevant_coordinate = 2.5e-4
    microscopic_irrelevant_coordinate = 0.37

    endpoint_relevant_coordinate = microscopic_relevant_coordinate * b ** (steps * y_t)
    expected_endpoint = microscopic_relevant_coordinate * size_in_lattice_units**y_t
    assert_close("finite-size scaling endpoint variable", endpoint_relevant_coordinate, expected_endpoint)

    endpoint_irrelevant_coordinate = microscopic_irrelevant_coordinate * b ** (-steps * omega)
    expected_irrelevant = microscopic_irrelevant_coordinate * size_in_lattice_units ** (-omega)
    assert_close("finite-size irrelevant correction", endpoint_irrelevant_coordinate, expected_irrelevant)

    lattice_spacing = 1.0e-3
    physical_mass = 0.7
    physical_size = 3.0
    lattice_size = physical_size / lattice_spacing
    tuned_relevant_coordinate = (lattice_spacing * physical_mass) ** y_t
    finite_volume_scaling_variable = tuned_relevant_coordinate * lattice_size**y_t
    expected_physical_variable = (physical_mass * physical_size) ** y_t
    assert_close("physical finite-volume scaling variable", finite_volume_scaling_variable, expected_physical_variable)


def check_operator_contact_shift() -> None:
    # A finite change of Wick subtraction changes the smeared square by
    # a multiple of the identity coordinate integral int f.
    subtraction_shift = 0.37
    cell_volume = 0.1
    test_values = [1.0, -0.2, 0.5, 0.7]
    identity_coordinate = cell_volume * sum(test_values)
    shifted_operator_difference = -subtraction_shift * identity_coordinate
    expected = -subtraction_shift * cell_volume * sum(test_values)
    assert_close("finite Wick-subtraction contact coordinate", shifted_operator_difference, expected)


def main() -> None:
    check_lattice_laplacian_expansion()
    check_tree_level_symanzik_artifact_and_improvement()
    check_free_scalar_pole_mass()
    check_gaussian_relevant_scaling()
    check_finite_size_scaling_variables()
    check_operator_contact_shift()
    print("All continuum-limit and scaling-window checks passed.")


if __name__ == "__main__":
    main()
