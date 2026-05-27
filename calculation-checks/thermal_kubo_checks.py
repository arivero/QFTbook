#!/usr/bin/env python3
"""Finite checks for the thermal Kubo and spectral-function conventions."""

from __future__ import annotations

import math


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def matadd(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    size = len(a)
    return [[a[i][j] + b[i][j] for j in range(size)] for i in range(size)]


def matscale(c: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[c * a[i][j] for j in range(len(a))] for i in range(len(a))]


def trace(a: list[list[complex]]) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def thermal_expectation(rho: list[list[complex]], a: list[list[complex]]) -> complex:
    return trace(matmul(rho, a))


IDENTITY = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
SIGMA_X = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
SIGMA_Z = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]


def two_level_weights(beta: float, delta: float) -> dict[str, float]:
    """Delta-function weights for A=sigma_x in a two-level system.

    The Hamiltonian has energies 0 and delta.  The dictionary records the
    coefficients multiplying 2*pi*delta(omega +/- delta).
    """

    boltzmann = math.exp(-beta * delta)
    z = 1.0 + boltzmann
    return {
        "greater_plus": 1.0 / z,
        "greater_minus": boltzmann / z,
        "less_plus": boltzmann / z,
        "less_minus": 1.0 / z,
        "rho_plus": (1.0 - boltzmann) / z,
        "rho_minus": -(1.0 - boltzmann) / z,
    }


def coth(x: float) -> float:
    return math.cosh(x) / math.sinh(x)


def check_two_level_kms_and_fdt() -> None:
    for beta, delta in ((0.7, 1.3), (2.1, 0.4), (1.0, 3.0)):
        w = two_level_weights(beta, delta)

        assert_close(
            "KMS detailed balance at positive frequency",
            w["less_plus"],
            math.exp(-beta * delta) * w["greater_plus"],
        )
        assert_close(
            "KMS detailed balance at negative frequency",
            w["less_minus"],
            math.exp(beta * delta) * w["greater_minus"],
        )

        sym_plus = 0.5 * (w["greater_plus"] + w["less_plus"])
        sym_minus = 0.5 * (w["greater_minus"] + w["less_minus"])
        assert_close(
            "FDT at positive frequency",
            sym_plus,
            0.5 * coth(0.5 * beta * delta) * w["rho_plus"],
        )
        assert_close(
            "FDT at negative frequency",
            sym_minus,
            0.5 * coth(-0.5 * beta * delta) * w["rho_minus"],
        )

        assert w["rho_plus"] > 0.0
        assert w["rho_minus"] < 0.0
        assert_close("odd spectral weights", w["rho_plus"], -w["rho_minus"])


def retarded_shear_model(omega: float, eta: float, tau: float) -> complex:
    """A causal one-pole model with Im G_R(omega) = -eta*omega + O(omega^3)."""

    return (-1j * eta * omega) / (1.0 - 1j * omega * tau)


def check_retarded_sign_and_transport_slope() -> None:
    eta = 0.73
    tau = 1.9
    for omega in (1.0e-4, 2.0e-4, 5.0e-4):
        gr = retarded_shear_model(omega, eta, tau)
        rho = -2.0 * gr.imag
        assert rho > 0.0
        assert_close("spectral slope gives eta", rho / (2.0 * omega), eta, tol=2.0e-6)
        assert_close("minus imaginary slope gives eta", -gr.imag / omega, eta, tol=2.0e-6)


def check_contact_term_does_not_change_spectral_slope() -> None:
    eta = 0.41
    tau = 0.6
    contact_static = 3.7
    contact_quadratic = -0.2
    omega = 3.0e-4
    nonlocal_gr = retarded_shear_model(omega, eta, tau)
    full_kernel = nonlocal_gr + contact_static + contact_quadratic * omega * omega
    assert_close(
        "real contact term leaves spectral density unchanged",
        -2.0 * full_kernel.imag,
        -2.0 * nonlocal_gr.imag,
    )
    assert_close("contact-independent transport slope", -full_kernel.imag / omega, eta, tol=2.0e-7)


def check_vector_potential_response_sign() -> None:
    sigma_dc = 0.58
    tau = 1.1
    omega = 2.0e-4
    response_kernel = retarded_shear_model(omega, sigma_dc, tau)
    conductivity = -response_kernel / (1j * omega)
    assert_close("positive conductivity from -K/(i omega)", conductivity.real, sigma_dc, tol=1.0e-7)


def check_mazur_projection_and_drude_weight() -> None:
    beta = 0.8
    gap = 1.3
    volume = 5.0
    current_conserved_part = 0.37
    current_oscillating_part = -0.22

    weights = [math.exp(-beta * gap / 2.0), math.exp(beta * gap / 2.0)]
    partition = sum(weights)
    rho = [[weights[0] / partition, 0j], [0j, weights[1] / partition]]
    mean_sigma_z = thermal_expectation(rho, SIGMA_Z).real
    q = matadd(SIGMA_Z, matscale(-mean_sigma_z, IDENTITY))
    current = matadd(matscale(current_conserved_part, q), matscale(current_oscillating_part, SIGMA_X))

    def sym_inner(a: list[list[complex]], b: list[list[complex]]) -> float:
        anticommutator = matadd(matmul(a, b), matmul(b, a))
        return (thermal_expectation(rho, anticommutator).real) / (2.0 * volume)

    covariance = sym_inner(q, q)
    overlap = sym_inner(current, q)
    mazur_projection_norm = overlap * overlap / covariance
    expected_persistent = current_conserved_part * current_conserved_part * covariance
    assert_close("Mazur projection gives conserved current component", mazur_projection_norm, expected_persistent)

    # In the chapter convention, a symmetrized zero-frequency term
    # (2*pi/beta) D delta(omega) gives a persistent time-domain constant D/beta.
    drude_weight = beta * expected_persistent
    persistent_from_drude = drude_weight / beta
    assert_close("Drude weight matches persistent symmetrized correlator", persistent_from_drude, expected_persistent)


def main() -> None:
    check_two_level_kms_and_fdt()
    check_retarded_sign_and_transport_slope()
    check_contact_term_does_not_change_spectral_slope()
    check_vector_potential_response_sign()
    check_mazur_projection_and_drude_weight()
    print("All thermal Kubo convention checks passed.")


if __name__ == "__main__":
    main()
