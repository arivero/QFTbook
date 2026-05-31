#!/usr/bin/env python3
"""Finite checks for hydrodynamic fluctuations and long-time tails."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_diffusion_static_covariance() -> None:
    temperature = 1.37
    chi = 2.4
    sigma = 0.84
    diffusion = sigma / chi
    k2 = 0.31
    pole_width = diffusion * k2
    numerator = 2.0 * temperature * sigma * k2

    # Integral d omega/(2 pi) numerator/(omega^2 + pole_width^2)
    equal_time = numerator / (2.0 * pole_width)
    assert_close("diffusive equal-time covariance", equal_time, temperature * chi)


def check_diffusion_fdt() -> None:
    temperature = 0.9
    chi = 1.8
    sigma = 0.63
    diffusion = sigma / chi
    omega = 0.17
    k2 = 0.42
    denom = (diffusion * k2) ** 2 + omega**2
    sym = 2.0 * temperature * sigma * k2 / denom
    imag_retarded = chi * diffusion * k2 * omega / denom
    assert_close("classical diffusion FDT", sym, (2.0 * temperature / omega) * imag_retarded)


def finite_bond_current_cost(current: float, rate_plus: float, rate_minus: float) -> float:
    delta = math.sqrt(current * current + 4.0 * rate_plus * rate_minus)
    return current * math.log((current + delta) / (2.0 * rate_plus)) - delta + rate_plus + rate_minus


def check_finite_bond_current_contraction() -> None:
    rate_plus = 2.3
    rate_minus = 0.7
    current = 0.4
    delta = math.sqrt(current * current + 4.0 * rate_plus * rate_minus)
    q_plus = 0.5 * (delta + current)
    q_minus = 0.5 * (delta - current)

    assert_close("bond-current minimizer difference", q_plus - q_minus, current)
    assert_close("bond-current minimizer product", q_plus * q_minus, rate_plus * rate_minus)

    direct_cost = (
        q_plus * math.log(q_plus / rate_plus)
        - q_plus
        + rate_plus
        + q_minus * math.log(q_minus / rate_minus)
        - q_minus
        + rate_minus
    )
    closed_cost = finite_bond_current_cost(current, rate_plus, rate_minus)
    assert_close("finite bond-current contraction", closed_cost, direct_cost)

    typical_current = rate_plus - rate_minus
    assert_close(
        "finite bond-current cost minimum",
        finite_bond_current_cost(typical_current, rate_plus, rate_minus),
        0.0,
    )

    entropy_force = math.log(rate_plus / rate_minus)
    asymmetry = finite_bond_current_cost(current, rate_plus, rate_minus) - finite_bond_current_cost(
        -current, rate_plus, rate_minus
    )
    assert_close("finite bond-current GC asymmetry", asymmetry, -current * entropy_force)

    eps = 1.0e-5
    second_derivative = (
        finite_bond_current_cost(typical_current + eps, rate_plus, rate_minus)
        + finite_bond_current_cost(typical_current - eps, rate_plus, rate_minus)
        - 2.0 * finite_bond_current_cost(typical_current, rate_plus, rate_minus)
    ) / eps**2
    expected_second_derivative = 1.0 / (rate_plus + rate_minus)
    assert_close(
        "finite bond-current quadratic curvature",
        second_derivative,
        expected_second_derivative,
        tol=1.0e-5,
    )

    small_delta = 1.0e-4
    gaussian_cost = small_delta**2 / (2.0 * (rate_plus + rate_minus))
    exact_increment = finite_bond_current_cost(
        typical_current + small_delta,
        rate_plus,
        rate_minus,
    )
    assert_close(
        "finite bond-current Gaussian coefficient",
        exact_increment / gaussian_cost,
        1.0,
        tol=1.0e-4,
    )


def check_time_domain_tail() -> None:
    lam = 0.41
    temperature = 1.2
    chi = 1.7
    diffusion = 0.33
    time = 4.5
    spatial_dim = 3
    gaussian_integral = (8.0 * math.pi * diffusion * time) ** (-spatial_dim / 2.0)
    tail = 2.0 * lam**2 * (temperature * chi) ** 2 * gaussian_integral

    # Direct formula specialized to d=3.
    expected = 2.0 * lam**2 * (temperature * chi) ** 2 / ((8.0 * math.pi * diffusion * time) ** 1.5)
    assert_close("time-domain long-time tail", tail, expected)


def check_frequency_nonanalytic_coefficients() -> None:
    diffusion = 0.57
    coeff_d1 = math.gamma(0.5) / ((4.0 * math.pi) ** 0.5 * (2.0 * diffusion) ** 0.5)
    expected_d1 = 1.0 / (2.0 * (2.0 * diffusion) ** 0.5)
    assert_close("d=1 loop coefficient", coeff_d1, expected_d1)

    coeff_d3 = math.gamma(-0.5) / ((4.0 * math.pi) ** 1.5 * (2.0 * diffusion) ** 1.5)
    expected_d3 = -1.0 / (4.0 * math.pi * (2.0 * diffusion) ** 1.5)
    assert_close("d=3 loop coefficient", coeff_d3, expected_d3)

    cutoff = 200.0
    z_small = 1.0e-8
    a = 2.0 * diffusion
    integral_d2 = math.log((z_small + a * cutoff * cutoff) / z_small) / (4.0 * math.pi * a)
    local_part = math.log(a * cutoff * cutoff) / (4.0 * math.pi * a)
    log_coefficient = (integral_d2 - local_part) / math.log(z_small)
    expected_log_coefficient = -1.0 / (4.0 * math.pi * a)
    assert_close("d=2 cutoff logarithm coefficient", log_coefficient, expected_log_coefficient, tol=1.0e-8)


def check_cutoff_integral_d3_separation() -> None:
    diffusion = 0.73
    cutoff = 300.0
    z = 1.0e-6
    a = 2.0 * diffusion
    root = math.sqrt(z / a)
    integral = (cutoff - root * math.atan(cutoff / root)) / (2.0 * math.pi**2 * a)
    analytic = cutoff / (2.0 * math.pi**2 * a)
    coeff = (integral - analytic) / math.sqrt(z)
    expected = -1.0 / (4.0 * math.pi * a ** 1.5)
    assert_close("d=3 cutoff nonanalytic coefficient", coeff, expected, tol=1.0e-7)

    # Retarded branch check: z = -i omega + 0 has the principal square root.
    omega = 0.2
    z_ret = -1j * omega + 1.0e-15
    branch_value = cmath.sqrt(z_ret)
    assert branch_value.real > 0.0 and branch_value.imag < 0.0


def check_stress_noise_tensor_positivity() -> None:
    temperature = 1.1
    eta = 0.8
    zeta = 0.25
    spatial_dim = 3
    tensor = [
        [0.7, -0.2, 0.3],
        [-0.2, 0.1, 0.4],
        [0.3, 0.4, -0.5],
    ]
    trace = sum(tensor[i][i] for i in range(spatial_dim))
    traceless_sq = 0.0
    full_sq = 0.0
    for i in range(spatial_dim):
        for j in range(spatial_dim):
            full_sq += tensor[i][j] ** 2
            traceless = tensor[i][j] - (trace / spatial_dim if i == j else 0.0)
            traceless_sq += traceless**2

    projector_contraction = 0.0
    for i in range(spatial_dim):
        for j in range(spatial_dim):
            for k in range(spatial_dim):
                for l in range(spatial_dim):
                    delta_ik = 1.0 if i == k else 0.0
                    delta_jl = 1.0 if j == l else 0.0
                    delta_il = 1.0 if i == l else 0.0
                    delta_jk = 1.0 if j == k else 0.0
                    delta_ij = 1.0 if i == j else 0.0
                    delta_kl = 1.0 if k == l else 0.0
                    noise = 2.0 * temperature * (
                        eta * (delta_ik * delta_jl + delta_il * delta_jk - 2.0 * delta_ij * delta_kl / spatial_dim)
                        + zeta * delta_ij * delta_kl
                    )
                    projector_contraction += tensor[i][j] * noise * tensor[k][l]

    expected = 4.0 * temperature * eta * traceless_sq + 2.0 * temperature * zeta * trace**2
    assert_close("stress-noise projector contraction", projector_contraction, expected)
    assert projector_contraction > 0.0 and full_sq > 0.0


def main() -> None:
    check_diffusion_static_covariance()
    check_diffusion_fdt()
    check_finite_bond_current_contraction()
    check_time_domain_tail()
    check_frequency_nonanalytic_coefficients()
    check_cutoff_integral_d3_separation()
    check_stress_noise_tensor_positivity()
    print("All hydrodynamic fluctuation and long-time-tail checks passed.")


if __name__ == "__main__":
    main()
