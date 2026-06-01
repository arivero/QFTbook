#!/usr/bin/env python3
"""Exact finite checks for the non-global soft-dipole datum.

The manuscript uses a finite angular-cell version of the large-N soft-dipole
evolution to separate global Sudakov veto terms from the first non-global
coefficient.  These rational checks verify the real-virtual cancellation for
unmeasured cells, the second-order expansion coefficient, and the special
additive case in which the non-global term vanishes.
"""

from __future__ import annotations

from fractions import Fraction


Dipole = tuple[str, str]
Rates = dict[tuple[str, str, str], Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def veto_rate(dipole: Dipole, measured: tuple[str, ...], rates: Rates) -> Fraction:
    i, j = dipole
    return sum((rates.get((i, j, cell), Fraction(0)) for cell in measured), Fraction(0))


def bms_rhs(
    dipole: Dipole,
    values: dict[Dipole, Fraction],
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    i, j = dipole
    direct = -veto_rate(dipole, measured, rates) * values[dipole]
    nonlinear = Fraction(0)
    for cell in unmeasured:
        nonlinear += rates.get((i, j, cell), Fraction(0)) * (
            values[(i, cell)] * values[(cell, j)] - values[dipole]
        )
    return direct + nonlinear


def non_global_coefficient(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    i, j = dipole
    a_ij = veto_rate(dipole, measured, rates)
    return sum(
        (
            rates.get((i, j, cell), Fraction(0))
            * (veto_rate((i, cell), measured, rates) + veto_rate((cell, j), measured, rates) - a_ij)
            for cell in unmeasured
        ),
        Fraction(0),
    )


def second_order_coefficient(
    dipole: Dipole,
    measured: tuple[str, ...],
    unmeasured: tuple[str, ...],
    rates: Rates,
) -> Fraction:
    a_ij = veto_rate(dipole, measured, rates)
    return (a_ij**2 - non_global_coefficient(dipole, measured, unmeasured, rates)) / 2


def check_unmeasured_real_virtual_cancellation() -> None:
    measured: tuple[str, ...] = ()
    unmeasured = ("u",)
    rates: Rates = {("a", "b", "u"): Fraction(5, 7)}
    values = {
        ("a", "b"): Fraction(1),
        ("a", "u"): Fraction(1),
        ("u", "b"): Fraction(1),
    }
    assert_equal(
        "unmeasured real-virtual cancellation at G=1",
        bms_rhs(("a", "b"), values, measured, unmeasured, rates),
        Fraction(0),
    )
    assert_equal("no measured cells gives zero non-global coefficient", non_global_coefficient(("a", "b"), measured, unmeasured, rates), Fraction(0))


def check_second_order_non_global_coefficient() -> None:
    measured = ("m",)
    unmeasured = ("u",)
    rates: Rates = {
        ("a", "b", "m"): Fraction(3, 5),
        ("a", "b", "u"): Fraction(2, 7),
        ("a", "u", "m"): Fraction(11, 13),
        ("u", "b", "m"): Fraction(5, 17),
    }
    a_ab = Fraction(3, 5)
    expected_non_global = Fraction(2, 7) * (Fraction(11, 13) + Fraction(5, 17) - a_ab)
    assert_equal("finite non-global coefficient", non_global_coefficient(("a", "b"), measured, unmeasured, rates), expected_non_global)
    assert_equal(
        "second-order gap expansion coefficient",
        second_order_coefficient(("a", "b"), measured, unmeasured, rates),
        (a_ab**2 - expected_non_global) / 2,
    )

    values_at_zero = {
        ("a", "b"): Fraction(1),
        ("a", "u"): Fraction(1),
        ("u", "b"): Fraction(1),
    }
    assert_equal(
        "first derivative at zero",
        bms_rhs(("a", "b"), values_at_zero, measured, unmeasured, rates),
        -a_ab,
    )


def check_additive_measurement_boundary() -> None:
    measured = ("m",)
    unmeasured = ("u",)
    rates: Rates = {
        ("a", "b", "m"): Fraction(3, 5),
        ("a", "b", "u"): Fraction(2, 7),
        ("a", "u", "m"): Fraction(1, 5),
        ("u", "b", "m"): Fraction(2, 5),
    }
    assert_equal(
        "additive veto rates remove the non-global coefficient",
        non_global_coefficient(("a", "b"), measured, unmeasured, rates),
        Fraction(0),
    )
    assert_equal(
        "additive case leaves global Sudakov square",
        second_order_coefficient(("a", "b"), measured, unmeasured, rates),
        Fraction(9, 50),
    )


def main() -> None:
    check_unmeasured_real_virtual_cancellation()
    check_second_order_non_global_coefficient()
    check_additive_measurement_boundary()
    print("All QCD non-global soft-dipole checks passed.")


if __name__ == "__main__":
    main()
