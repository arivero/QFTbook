#!/usr/bin/env python3
"""Finite checks for the Hawking Bogoliubov coefficient calculation."""

import mpmath as mp


mp.mp.dps = 60


def assert_close(name, lhs, rhs, tol=mp.mpf("1e-45")):
    lhs = mp.mpf(lhs)
    rhs = mp.mpf(rhs)
    scale = max(mp.mpf(1), abs(lhs), abs(rhs))
    if abs(lhs - rhs) > tol * scale:
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

    print("All Hawking Bogoliubov coefficient checks passed.")


if __name__ == "__main__":
    main()
