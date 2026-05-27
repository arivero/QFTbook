#!/usr/bin/env python3
"""Exact convention checks for cosmological particle-creation formulas."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def conformal_coupling(d: int) -> Fraction:
    return Fraction(d - 2, 4 * (d - 1))


def check_conformal_cancellation() -> None:
    for d in range(2, 13):
        xi = conformal_coupling(d)
        p = Fraction(d - 2, 2)
        curvature_hprime_coeff = xi * (d - 1) * 2
        curvature_hsquare_coeff = xi * (d - 1) * (d - 2)
        assert_equal(f"H' cancellation d={d}", curvature_hprime_coeff, p)
        assert_equal(f"H^2 cancellation d={d}", curvature_hsquare_coeff, p * p)


def de_sitter_nu_squared(d: int, mass_over_h_squared: Fraction, xi: Fraction) -> Fraction:
    return Fraction((d - 1) ** 2, 4) - mass_over_h_squared - xi * d * (d - 1)


def check_de_sitter_nu_values() -> None:
    for d in range(2, 13):
        assert_equal(
            f"conformal massless de Sitter nu^2 d={d}",
            de_sitter_nu_squared(d, Fraction(0), conformal_coupling(d)),
            Fraction(1, 4),
        )
    assert_equal(
        "four-dimensional minimally coupled massless nu^2",
        de_sitter_nu_squared(4, Fraction(0), Fraction(0)),
        Fraction(9, 4),
    )


def check_de_sitter_frequency_coefficient() -> None:
    samples = [
        (3, Fraction(2, 5), Fraction(1, 8)),
        (4, Fraction(7, 3), Fraction(1, 6)),
        (7, Fraction(5, 2), Fraction(3, 20)),
    ]
    for d, mass_over_h_squared, xi in samples:
        p = Fraction(d - 2, 2)
        coefficient = mass_over_h_squared + xi * d * (d - 1) - p * (p + 1)
        nu2 = de_sitter_nu_squared(d, mass_over_h_squared, xi)
        assert_equal(
            f"de Sitter frequency coefficient d={d}",
            coefficient,
            -(nu2 - Fraction(1, 4)),
        )


def check_sudden_quench_bogoliubov() -> None:
    samples = [(Fraction(1), Fraction(4)), (Fraction(2, 3), Fraction(7, 5)), (Fraction(5), Fraction(2))]
    for omega_i, omega_f in samples:
        alpha_squared = (omega_f + omega_i) ** 2 / (4 * omega_i * omega_f)
        beta_squared = (omega_f - omega_i) ** 2 / (4 * omega_i * omega_f)
        assert_equal(f"Bogoliubov normalization {omega_i}->{omega_f}", alpha_squared - beta_squared, 1)


def check_adiabatic_riccati_power_law() -> None:
    # For W=c/eta, the exact Riccati equation gives
    # Omega^2=(c^2+1/4)/eta^2.
    samples = [(Fraction(3, 2), Fraction(5, 7)), (Fraction(4), Fraction(2, 3))]
    for c, eta in samples:
        w = c / eta
        wp_over_w = -1 / eta
        wpp_over_w = 2 / (eta * eta)
        omega_squared = w * w + Fraction(1, 2) * wpp_over_w - Fraction(3, 4) * wp_over_w * wp_over_w
        assert_equal(
            f"adiabatic Riccati power law c={c} eta={eta}",
            omega_squared,
            (c * c + Fraction(1, 4)) / (eta * eta),
        )


def check_detector_positive_type_finite_model() -> None:
    gram = [
        [Fraction(5), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]
    vectors = [
        (Fraction(1), Fraction(0)),
        (Fraction(3), Fraction(-2)),
        (Fraction(-1), Fraction(4)),
    ]
    for x, y in vectors:
        quadratic = gram[0][0] * x * x + 2 * gram[0][1] * x * y + gram[1][1] * y * y
        if quadratic < 0:
            raise AssertionError(f"positive-type detector Gram form failed: {quadratic}")


def main() -> None:
    check_conformal_cancellation()
    check_de_sitter_nu_values()
    check_de_sitter_frequency_coefficient()
    check_sudden_quench_bogoliubov()
    check_adiabatic_riccati_power_law()
    check_detector_positive_type_finite_model()
    print("Cosmological particle-creation convention checks passed.")


if __name__ == "__main__":
    main()
