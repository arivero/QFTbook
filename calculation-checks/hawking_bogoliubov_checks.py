#!/usr/bin/env python3
"""Finite checks for the Hawking Bogoliubov coefficient calculation."""

import mpmath as mp


mp.mp.dps = 60


def assert_close(name, lhs, rhs, tol=mp.mpf("1e-45")):
    lhs = mp.mpf(lhs)
    rhs = mp.mpf(rhs)
    if not mp.isfinite(lhs) or not mp.isfinite(rhs):
        raise AssertionError(f"{name}: nonfinite value {lhs} or {rhs}")
    if not mp.isfinite(tol) or tol < 0:
        raise AssertionError(f"{name}: invalid tolerance {tol}")
    scale = max(mp.mpf(1), abs(lhs), abs(rhs))
    error = abs(lhs - rhs)
    threshold = tol * scale
    if not mp.isfinite(error) or not mp.isfinite(threshold):
        raise AssertionError(f"{name}: nonfinite comparison error")
    if error > threshold:
        raise AssertionError(f"{name}: {lhs} != {rhs}")


def main():
    samples = [
        (mp.mpf("0.7"), mp.mpf("0.2"), mp.mpf("1.3")),
        (mp.mpf("1.0"), mp.mpf("0.9"), mp.mpf("2.0")),
        (mp.mpf("2.5"), mp.mpf("3.1"), mp.mpf("0.8")),
    ]

    for kappa, omega, omega_prime in samples:
        a = omega / kappa
        gamma_abs_squared = abs(mp.gamma(1j * a)) ** 2
        gamma_identity = mp.pi / (a * mp.sinh(mp.pi * a))
        assert_close("Gamma imaginary-axis norm", gamma_abs_squared, gamma_identity)

        common = (1 / (2 * mp.pi * kappa)) ** 2 * (omega / omega_prime)
        alpha_squared = common * mp.e ** (mp.pi * a) * gamma_abs_squared
        beta_squared = common * mp.e ** (-mp.pi * a) * gamma_abs_squared

        assert_close(
            "alpha/beta thermal ratio",
            alpha_squared / beta_squared,
            mp.e ** (2 * mp.pi * a),
        )

        planck_beta = (
            1
            / (2 * mp.pi * kappa * omega_prime)
            / (mp.e ** (2 * mp.pi * omega / kappa) - 1)
        )
        assert_close("beta coefficient Planck factor", beta_squared, planck_beta)

        normalization_density = alpha_squared - beta_squared
        assert_close(
            "continuum Bogoliubov normalization density",
            normalization_density,
            1 / (2 * mp.pi * kappa * omega_prime),
        )

        u = mp.mpf("4.0")
        C = mp.mpf("1.7")
        v0_minus_v = C * mp.e ** (-kappa * u)
        blueshift_from_ray = omega / (kappa * v0_minus_v)
        blueshift_exponential = omega * mp.e ** (kappa * u) / (kappa * C)
        assert_close("late-time precursor blueshift", blueshift_from_ray, blueshift_exponential)

        beta_h = 2 * mp.pi / kappa
        bin_width = mp.mpf("0.13")
        bin_left = mp.mpf("0.41")
        bin_right = bin_left + bin_width
        bin_average_closed = (
            mp.log((1 - mp.e ** (-beta_h * bin_right)) / (1 - mp.e ** (-beta_h * bin_left)))
            / (beta_h * bin_width)
        )
        bin_average_integral = (
            mp.quad(lambda w: 1 / (mp.e ** (beta_h * w) - 1), [bin_left, bin_right])
            / bin_width
        )
        assert_close("wave-packet Planck bin average", bin_average_closed, bin_average_integral)

        p_prime = C * kappa * mp.e ** (-kappa * u)
        p_double_prime = -C * kappa**2 * mp.e ** (-kappa * u)
        p_triple_prime = C * kappa**3 * mp.e ** (-kappa * u)
        schwarzian = p_triple_prime / p_prime - mp.mpf("1.5") * (p_double_prime / p_prime) ** 2
        assert_close("exponential ray-tracing Schwarzian", schwarzian, -kappa**2 / 2)

        c = mp.mpf("1.0")
        flux_from_schwarzian = -c * schwarzian / (24 * mp.pi)
        flux_from_planck = c * mp.pi / (12 * beta_h**2)
        flux_from_kappa = c * kappa**2 / (48 * mp.pi)
        assert_close("two-dimensional Hawking flux from Schwarzian", flux_from_schwarzian, flux_from_kappa)
        assert_close("two-dimensional Hawking flux from Planck integral", flux_from_planck, flux_from_kappa)

        mass = mp.mpf("3.7")
        schwarzschild_kappa = 1 / (4 * mass)
        schwarzschild_temp = schwarzschild_kappa / (2 * mp.pi)
        assert_close("Schwarzschild temperature convention", schwarzschild_temp, 1 / (8 * mp.pi * mass))

    print("All Hawking Bogoliubov coefficient checks passed.")


if __name__ == "__main__":
    main()
