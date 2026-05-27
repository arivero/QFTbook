#!/usr/bin/env python3
"""Finite checks for LSZ residue and momentum-convention algebra.

The LSZ chapter proves distributional statements after wave-packet smearing.
This script checks only the finite sign and normalization algebra that is easy
to drift: mostly-plus denominator factorization, partial fractions, per-leg
amputation, all-incoming momentum bookkeeping, and source-derivative phases.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def i_power(exponent):
    cycle = [1, "i", -1, "-i"]
    return cycle[exponent % 4]


def check_denominator_factorization():
    k0 = Fraction(7, 1)
    omega = Fraction(5, 1)
    denominator = -(k0 * k0) + omega * omega
    factored = -(k0 - omega) * (k0 + omega)
    assert_equal(denominator, Fraction(-24, 1), "sample denominator")
    assert_equal(factored, denominator, "mostly-plus denominator factorization")


def check_partial_fraction_sign():
    k0 = Fraction(7, 1)
    omega = Fraction(5, 1)
    denominator = -(k0 - omega) * (k0 + omega)
    lhs = Fraction(1, 1) / denominator
    bracket = Fraction(1, 1) / (k0 - omega) - Fraction(1, 1) / (k0 + omega)
    rhs = -bracket / (2 * omega)
    assert_equal(lhs, rhs, "partial fraction sign for invariant denominator")

    z_phi = Fraction(9, 1)
    coefficient_of_i_bracket = z_phi / (2 * omega)
    assert_equal(coefficient_of_i_bracket, Fraction(9, 10), "two-point i-bracket coefficient")


def check_lsz_per_leg_cancellation():
    # i(k^2+m^2) times -i Z/(k^2+m^2-i0) gives Z at the external pole.
    z_phi = Fraction(9, 1)
    i_times_minus_i = 1
    invariant_coefficient = i_times_minus_i * z_phi
    assert_equal(invariant_coefficient, z_phi, "per-leg invariant amputation gives Z")

    z_sqrt = Fraction(3, 1)
    normalized = invariant_coefficient / z_sqrt
    assert_equal(normalized, z_sqrt, "one external LSZ factor leaves sqrt residue")


def check_all_incoming_momentum_convention():
    q1 = (Fraction(5, 1), Fraction(3, 1))
    q2 = (Fraction(4, 1), Fraction(-1, 1))
    p1 = (Fraction(6, 1), Fraction(2, 1))
    p2 = (Fraction(3, 1), Fraction(0, 1))
    all_incoming_sum = tuple(q1[i] + q2[i] - p1[i] - p2[i] for i in range(2))
    physical_difference = tuple((q1[i] + q2[i]) - (p1[i] + p2[i]) for i in range(2))
    assert_equal(all_incoming_sum, physical_difference, "all-incoming LSZ momentum convention")
    assert_equal(all_incoming_sum, (Fraction(0, 1), Fraction(0, 1)), "sample momentum conservation")


def check_source_derivative_phase():
    for n in range(8):
        # i^{-n} i^n = 1, represented by adding exponents modulo four.
        assert_equal(i_power((-n) + n), 1, f"Lorentzian source prefactor n={n}")
        assert_equal(i_power(n + (-n)), 1, f"alternate source prefactor n={n}")


def main():
    check_denominator_factorization()
    check_partial_fraction_sign()
    check_lsz_per_leg_cancellation()
    check_all_incoming_momentum_convention()
    check_source_derivative_phase()
    print("All LSZ residue and convention checks passed.")


if __name__ == "__main__":
    main()
