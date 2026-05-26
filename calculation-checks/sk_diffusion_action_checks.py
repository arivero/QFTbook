#!/usr/bin/env python3
"""Finite algebra checks for the Schwinger-Keldysh diffusion action."""

from __future__ import annotations


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_density_response_kernel() -> None:
    chi = 1.7
    sigma = 0.51
    diffusion = sigma / chi
    omega = 0.23
    k = 0.19
    source = 0.8

    # Saddle equation from the a-phase:
    # chi (A0 - i omega phi) + sigma k^2 phi = 0.
    phi = -chi * source / (sigma * k * k - 1j * chi * omega)
    density = chi * (source - 1j * omega * phi)
    kernel = density / source
    expected = chi * diffusion * k * k / (diffusion * k * k - 1j * omega)

    assert_close("density response kernel", kernel, expected)
    assert_close("static source response", chi * diffusion * k * k / (diffusion * k * k), chi)
    assert_close("conserved total charge response", chi * diffusion * 0.0 / (diffusion * 0.0 - 1j * omega), 0.0)

    current_divergence = -1j * sigma * omega * k * k * phi
    assert_close("continuity equation", -1j * omega * density + current_divergence, 0.0)


def check_transverse_ohm_response() -> None:
    sigma = 0.73
    omega = 0.41
    vector_source = 1.2

    # For a transverse source with A0=0 and k_i A_i=0:
    # j_i = -sigma partial_t A_i = i omega sigma A_i.
    current = 1j * omega * sigma * vector_source
    electric_field = 1j * omega * vector_source
    assert_close("transverse Ohm response", current, sigma * electric_field)


def check_classical_kms_noise_coefficient() -> None:
    beta = 2.3
    sigma = 0.61
    c = sigma / beta

    # Transform L = -sigma a x + i c a^2 under x -> -x,
    # a -> a + i beta x. Equality with L requires c beta = sigma.
    a_coeff_after = sigma - 2.0 * c * beta
    a_coeff_before = -sigma
    x2_coeff_after = 1j * sigma * beta - 1j * c * beta * beta
    assert_close("KMS ax coefficient", a_coeff_after, a_coeff_before)
    assert_close("KMS x^2 cancellation", x2_coeff_after, 0.0)


def check_noise_normalization() -> None:
    temperature = 1.4
    sigma = 0.32
    variance = 2.0 * temperature * sigma
    inverse_gaussian_denominator = 4.0 * temperature * sigma
    assert_close("noise variance", variance, 2.0 * temperature * sigma)
    assert_close("Hubbard-Stratonovich denominator", inverse_gaussian_denominator, 2.0 * variance)


def main() -> None:
    check_density_response_kernel()
    check_transverse_ohm_response()
    check_classical_kms_noise_coefficient()
    check_noise_normalization()
    print("All Schwinger-Keldysh diffusion-action checks passed.")


if __name__ == "__main__":
    main()
