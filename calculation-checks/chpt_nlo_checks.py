#!/usr/bin/env python3
"""Finite arithmetic checks for the NLO chiral perturbation theory section."""

from __future__ import annotations

from fractions import Fraction


def assert_eq(name: str, value: Fraction | int, expected: Fraction | int) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def check_gasser_leutwyler_basis_count() -> None:
    labels = tuple(range(1, 11))
    assert_eq("Gasser-Leutwyler L_i count", len(labels), 10)
    assert_eq("first L_i label", labels[0], 1)
    assert_eq("last L_i label", labels[-1], 10)


def check_su2_pion_mass_scale_cancellation() -> None:
    """Check d/d log(mu) of the NLO M_pi^2 bracket vanishes.

    The bracket is

        1 + M^2/(32 pi^2 f^2) log(M^2/mu^2)
          + 2 l_3^r(mu) M^2/f^2,

    with mu d l_3^r / d mu = 1/(32 pi^2).  We strip the common factor
    M^2/(pi^2 f^2).
    """

    log_derivative = Fraction(-2, 32)
    local_derivative = 2 * Fraction(1, 32)
    assert_eq("SU(2) pion mass NLO scale cancellation", log_derivative + local_derivative, 0)


def check_su3_gamma_table_entries_used_by_sources() -> None:
    gamma = {
        1: Fraction(3, 32),
        2: Fraction(3, 16),
        3: Fraction(0, 1),
        4: Fraction(1, 8),
        5: Fraction(3, 8),
        6: Fraction(11, 144),
        7: Fraction(0, 1),
        8: Fraction(5, 48),
        9: Fraction(1, 4),
        10: Fraction(-1, 4),
    }
    assert_eq("ten Gamma_i entries", len(gamma), 10)
    assert_eq("Gamma_3 vanishes", gamma[3], 0)
    assert_eq("Gamma_7 vanishes", gamma[7], 0)
    assert_eq("Gamma_9 plus Gamma_10", gamma[9] + gamma[10], 0)


def main() -> None:
    check_gasser_leutwyler_basis_count()
    check_su2_pion_mass_scale_cancellation()
    check_su3_gamma_table_entries_used_by_sources()
    print("All NLO chiral-perturbation-theory checks passed.")


if __name__ == "__main__":
    main()
