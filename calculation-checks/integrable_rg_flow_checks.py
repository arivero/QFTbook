#!/usr/bin/env python3
"""Exact arithmetic checks for Volume VI integrable RG-flow conventions."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def minimal_c(m: int) -> Fraction:
    return Fraction(1, 1) - Fraction(6, m * (m + 1))


def kac_weight(m: int, r: int, s: int) -> Fraction:
    numerator = ((m + 1) * r - m * s) ** 2 - 1
    denominator = 4 * m * (m + 1)
    return Fraction(numerator, denominator)


def check_phi_13_data() -> None:
    for m in range(3, 20):
        h_13 = kac_weight(m, 1, 3)
        delta_13 = 2 * h_13
        y_13 = Fraction(2, 1) - delta_13
        assert_equal(f"h_13 for m={m}", h_13, Fraction(m - 1, m + 1))
        assert_equal(
            f"Delta_13 for m={m}",
            delta_13,
            Fraction(2 * (m - 1), m + 1),
        )
        assert_equal(f"y_13 for m={m}", y_13, Fraction(4, m + 1))


def check_minimal_model_c_drops() -> None:
    for m in range(4, 20):
        drop = minimal_c(m) - minimal_c(m - 1)
        assert_equal(
            f"minimal-model c drop m={m}",
            drop,
            Fraction(12, m * (m * m - 1)),
        )

    assert_equal("Ising central charge", minimal_c(3), Fraction(1, 2))
    assert_equal("tricritical Ising central charge", minimal_c(4), Fraction(7, 10))
    assert_equal(
        "tricritical-to-Ising c drop",
        minimal_c(4) - minimal_c(3),
        Fraction(1, 5),
    )
    assert_equal("three-state Potts central charge", minimal_c(5), Fraction(4, 5))
    assert_equal(
        "Potts-to-tricritical-Ising c drop",
        minimal_c(5) - minimal_c(4),
        Fraction(1, 10),
    )


def check_kac_identification_for_phi_13() -> None:
    for m in range(3, 20):
        identified = (m - 1, m - 2)
        assert_equal(
            f"Kac identification h_13 m={m}",
            kac_weight(m, 1, 3),
            kac_weight(m, identified[0], identified[1]),
        )


def check_source_scaling_linearization() -> None:
    # lambda(mu) = mu^{-y} g has mu d_lambda/d_mu = -y lambda.
    for m in range(3, 20):
        y = Fraction(4, m + 1)
        derivative_over_lambda = -y
        length_flow_over_lambda = y
        assert_equal(
            f"source beta sign m={m}",
            derivative_over_lambda,
            -Fraction(4, m + 1),
        )
        assert_equal(
            f"length-flow sign m={m}",
            length_flow_over_lambda,
            Fraction(4, m + 1),
        )


def check_massless_dispersion_identities() -> None:
    # Use rational e^theta samples q.  Right movers have E=p=M q/2;
    # left movers have E=-p=M/(2q).  Both are exactly null.
    for q in (Fraction(1, 3), Fraction(2, 1), Fraction(5, 2)):
        m_scale = Fraction(7, 1)
        e_right = m_scale * q / 2
        p_right = e_right
        e_left = m_scale / (2 * q)
        p_left = -e_left
        assert_equal(
            f"right mover null q={q}",
            e_right * e_right - p_right * p_right,
            Fraction(0, 1),
        )
        assert_equal(
            f"left mover null q={q}",
            e_left * e_left - p_left * p_left,
            Fraction(0, 1),
        )


def main() -> None:
    check_phi_13_data()
    check_minimal_model_c_drops()
    check_kac_identification_for_phi_13()
    check_source_scaling_linearization()
    check_massless_dispersion_identities()
    print("All integrable RG-flow checks passed.")


if __name__ == "__main__":
    main()
