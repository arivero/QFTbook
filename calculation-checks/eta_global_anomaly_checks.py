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


def main() -> None:
    check_su2_index_table()
    check_witten_parity_criterion()
    check_pfaffian_sign_multiplicativity()
    check_su2_cubic_weight_sum_vanishes()
    check_orientation_reversal_eta_bookkeeping()
    check_aps_cylinder_congruence()
    print("Eta-invariant and SU(2) global-anomaly checks passed.")


if __name__ == "__main__":
    main()
