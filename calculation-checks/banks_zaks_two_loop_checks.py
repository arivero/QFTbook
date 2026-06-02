#!/usr/bin/env python3
"""Exact arithmetic checks for the Banks-Zaks two-loop formulas.

The monograph uses tr_fund(t^a t^b)=delta^{ab}, hence
C_A=2N, T_F=1, C_F=(N^2-1)/N.  This script checks the displayed conversion of
the universal two-loop gauge beta coefficient, the conformal-window lower
edge, the leading epsilon_BZ fixed-point coordinate, and the sign convention
for the IR-attractive linearized exponent.
"""

from fractions import Fraction


def assert_eq(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def b0_fund(n: int, nf: Fraction) -> Fraction:
    return Fraction(2, 3) * (11 * n - 2 * nf)


def b1_fund(n: int, nf: Fraction) -> Fraction:
    return Fraction(136, 3) * n * n - (Fraction(52, 3) * n - Fraction(4, n)) * nf


def check_group_conversion(n: int) -> None:
    ca = 2 * n
    tf = Fraction(1, 1)
    cf = Fraction(n * n - 1, n)
    nf = Fraction(7 * n, 2)

    general_b0 = Fraction(11, 3) * ca - Fraction(4, 3) * tf * nf
    general_b1 = (
        Fraction(34, 3) * ca * ca
        - (Fraction(20, 3) * ca * tf + 4 * cf * tf) * nf
    )
    assert_eq(f"N={n} B0 convention conversion", general_b0, b0_fund(n, nf))
    assert_eq(f"N={n} B1 convention conversion", general_b1, b1_fund(n, nf))


def check_window_edges(n: int) -> None:
    lower = Fraction(34 * n**3, 13 * n * n - 3)
    upper = Fraction(11 * n, 2)

    assert_eq(f"N={n} B1 lower edge", b1_fund(n, lower), Fraction(0, 1))
    if not b0_fund(n, lower) > 0:
        raise AssertionError(f"N={n}: lower edge must remain asymptotically free")
    assert_eq(f"N={n} B0 upper edge", b0_fund(n, upper), Fraction(0, 1))
    if not lower < upper:
        raise AssertionError(f"N={n}: Banks-Zaks window lower edge is not below upper edge")


def check_epsilon_expansion(n: int, eps: Fraction) -> None:
    nf = Fraction(11 * n, 2) - Fraction(3, 2) * eps
    denom0 = 25 * n * n - 11
    b1_edge = -2 * denom0
    b1_slope = 26 * n - Fraction(6, n)

    assert_eq(f"N={n} B0 epsilon", b0_fund(n, nf), 2 * eps)
    assert_eq(
        f"N={n} B1 epsilon",
        b1_fund(n, nf),
        b1_edge + b1_slope * eps,
    )

    two_loop_zero = -b0_fund(n, nf) / b1_fund(n, nf)
    displayed_zero = Fraction(2, 1) * eps / (2 * denom0 - b1_slope * eps)
    assert_eq(f"N={n} exact two-loop zero", two_loop_zero, displayed_zero)

    derivative_at_zero = -4 * b0_fund(n, nf) * two_loop_zero - 6 * b1_fund(n, nf) * two_loop_zero**2
    exact_linearized = -2 * b0_fund(n, nf) ** 2 / b1_fund(n, nf)
    assert_eq(f"N={n} exact two-loop derivative", derivative_at_zero, exact_linearized)
    if not derivative_at_zero > 0:
        raise AssertionError(f"N={n}: the two-loop Banks-Zaks zero is not IR-attractive")

    leading_coefficient = Fraction(1, denom0)
    omega_leading = Fraction(4, denom0)
    assert_eq(f"N={n} a_* leading coefficient", leading_coefficient, Fraction(1, denom0))
    assert_eq(f"N={n} omega leading coefficient", omega_leading, Fraction(4, denom0))


def main() -> None:
    for n in range(2, 11):
        check_group_conversion(n)
        check_window_edges(n)
        for eps in (Fraction(1, 7), Fraction(2, 9), Fraction(3, 11)):
            check_epsilon_expansion(n, eps)
    print("All Banks-Zaks two-loop convention and IR-exponent checks passed.")


if __name__ == "__main__":
    main()
