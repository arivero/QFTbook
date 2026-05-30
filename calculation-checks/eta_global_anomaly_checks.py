#!/usr/bin/env python3
"""Exact checks for eta-invariant and SU(2) global-anomaly conventions."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def su2_trace_delta_index(n: int) -> int:
    """Trace-delta Dynkin index for isospin j=n/2."""

    return n * (n + 1) * (n + 2) // 6


def pfaffian_sign_from_representations(ns: list[int]) -> int:
    parity = sum(su2_trace_delta_index(n) for n in ns) % 2
    return -1 if parity else 1


def check_su2_index_table() -> None:
    first_values = [su2_trace_delta_index(n) for n in range(1, 6)]
    assert_equal("first SU(2) trace-delta indices", first_values, [1, 4, 10, 20, 35])


def check_witten_parity_criterion() -> None:
    for n in range(0, 64):
        got = su2_trace_delta_index(n) % 2
        expected = 1 if n % 4 == 1 else 0
        assert_equal(f"Witten parity criterion n={n}", got, expected)


def check_pfaffian_sign_multiplicativity() -> None:
    assert_equal("one fundamental doublet", pfaffian_sign_from_representations([1]), -1)
    assert_equal("two fundamental doublets", pfaffian_sign_from_representations([1, 1]), 1)
    assert_equal("doublet plus isospin 5/2", pfaffian_sign_from_representations([1, 5]), 1)
    assert_equal("triplet and isospin 3/2", pfaffian_sign_from_representations([2, 3]), 1)


def check_su2_cubic_weight_sum_vanishes() -> None:
    for n in range(0, 16):
        doubled_weights = list(range(-n, n + 1, 2))
        assert_equal(f"SU(2) cubic weight sum n={n}", sum(weight**3 for weight in doubled_weights), 0)


def check_orientation_reversal_eta_bookkeeping() -> None:
    samples = [
        (Fraction(3, 7), 0),
        (Fraction(-5, 4), 2),
        (Fraction(11, 6), 5),
    ]
    for eta, kernel_dim in samples:
        xi = (eta + kernel_dim) / 2
        xi_reversed = (-eta + kernel_dim) / 2
        assert_equal(
            f"xi(-B) relation eta={eta} h={kernel_dim}",
            xi_reversed,
            -xi + kernel_dim,
        )


def check_aps_cylinder_congruence() -> None:
    examples = [
        (Fraction(5, 3), Fraction(2, 3), 2),
        (Fraction(-1, 5), Fraction(9, 5), -1),
        (Fraction(7, 4), Fraction(-1, 4), 3),
    ]
    for bulk_integral, xi0, fredholm_index in examples:
        # APS on [0,1] x Y gives
        # index = bulk - xi1 + xi0 modulo the integer endpoint-kernel term.
        xi1 = bulk_integral + xi0 - fredholm_index
        difference = xi1 - xi0 - bulk_integral
        assert_equal("APS cylinder difference is integral", difference.denominator, 1)


def orbit_action(a: int, g: int, orbit_size: int) -> int:
    return (a + g) % orbit_size


def anomaly_cocycle_exponent(a: int, g: int, orbit_size: int, phase_modulus: int) -> int:
    """A finite action-groupoid 1-cocycle in additive exponent notation.

    The value represents exp(2*pi*i*exponent/phase_modulus).  The dependence
    on the base object models a local trivialization; only based-loop values
    survive coboundary changes.
    """

    ag = orbit_action(a, g, orbit_size)
    potential_a = (a * a + 2 * a + 1) % phase_modulus
    potential_ag = (ag * ag + 2 * ag + 1) % phase_modulus
    return (potential_a - potential_ag) % phase_modulus


def trivialization_exponent(a: int, orbit_size: int, phase_modulus: int) -> int:
    return (3 * a * a + a + 1) % phase_modulus


def coboundary_shifted_exponent(a: int, g: int, orbit_size: int, phase_modulus: int) -> int:
    ag = orbit_action(a, g, orbit_size)
    return (
        anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
        + trivialization_exponent(a, orbit_size, phase_modulus)
        - trivialization_exponent(ag, orbit_size, phase_modulus)
    ) % phase_modulus


def check_action_groupoid_anomaly_cocycle_and_descent() -> None:
    for orbit_size in range(1, 8):
        for phase_modulus in range(2, 11):
            for a in range(orbit_size):
                for g in range(orbit_size):
                    for h in range(orbit_size):
                        gh = (g + h) % orbit_size
                        ag = orbit_action(a, g, orbit_size)
                        lhs = anomaly_cocycle_exponent(a, gh, orbit_size, phase_modulus)
                        rhs = (
                            anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
                            + anomaly_cocycle_exponent(ag, h, orbit_size, phase_modulus)
                        ) % phase_modulus
                        assert_equal(
                            f"action-groupoid anomaly cocycle orbit={orbit_size} phase={phase_modulus}",
                            lhs,
                            rhs,
                        )

                        shifted_lhs = coboundary_shifted_exponent(a, gh, orbit_size, phase_modulus)
                        shifted_rhs = (
                            coboundary_shifted_exponent(a, g, orbit_size, phase_modulus)
                            + coboundary_shifted_exponent(ag, h, orbit_size, phase_modulus)
                        ) % phase_modulus
                        assert_equal(
                            f"coboundary-shifted anomaly cocycle orbit={orbit_size} phase={phase_modulus}",
                            shifted_lhs,
                            shifted_rhs,
                        )

            for a in range(orbit_size):
                based_g = 0
                original = anomaly_cocycle_exponent(a, based_g, orbit_size, phase_modulus)
                shifted = coboundary_shifted_exponent(a, based_g, orbit_size, phase_modulus)
                assert_equal(
                    f"based-loop holonomy invariant orbit={orbit_size} phase={phase_modulus}",
                    shifted,
                    original,
                )

            for a in range(orbit_size):
                for g in range(orbit_size):
                    first = anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
                    second = (2 * anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)) % phase_modulus
                    tensor_product = (first + first) % phase_modulus
                    assert_equal(
                        f"tensoring anomaly lines adds exponents orbit={orbit_size} phase={phase_modulus}",
                        tensor_product,
                        second,
                    )


def check_stabilizer_holonomy_character_obstruction() -> None:
    for group_order in range(2, 12):
        for phase_modulus in range(2, 12):
            for charge in range(phase_modulus):
                # A based loop in the quotient groupoid is a stabilizer
                # element.  For the trivial action, the groupoid cocycle is a
                # character of the stabilizer written in additive exponents.
                for g in range(group_order):
                    for h in range(group_order):
                        lhs = charge * ((g + h) % group_order) % phase_modulus
                        rhs = (charge * g + charge * h) % phase_modulus
                        if (charge * group_order) % phase_modulus == 0:
                            assert_equal(
                                f"stabilizer holonomy character G={group_order} phase={phase_modulus}",
                                lhs,
                                rhs,
                            )

                descends = all((charge * g) % phase_modulus == 0 for g in range(group_order))
                expected_descends = charge % phase_modulus == 0
                assert_equal(
                    f"trivial stabilizer character is exact iff holonomy trivial G={group_order}",
                    descends,
                    expected_descends,
                )


def main() -> None:
    check_su2_index_table()
    check_witten_parity_criterion()
    check_pfaffian_sign_multiplicativity()
    check_su2_cubic_weight_sum_vanishes()
    check_orientation_reversal_eta_bookkeeping()
    check_aps_cylinder_congruence()
    check_action_groupoid_anomaly_cocycle_and_descent()
    check_stabilizer_holonomy_character_obstruction()
    print("Eta-invariant and SU(2) global-anomaly checks passed.")


if __name__ == "__main__":
    main()
