#!/usr/bin/env python3
"""Finite checks for the small-x/BFKL convention block in Volume II.

The manuscript writes the leading dipole/BFKL kernel in the trace-delta
Yang-Mills convention

    tr_fund(t^a t^b)=delta^{ab},       C_A=2 N_c,
    S_YM=-1/(4 g^2) int tr F^2.

These checks verify convention-invariant coefficient products, the transverse
inversion covariance of the dipole kernel measure, and the elementary
Mellin-eigenvalue constants of the leading BFKL characteristic function.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    reduced = sp.simplify(expr)
    if reduced != 0:
        raise AssertionError(f"{name}: got {reduced!r}, expected 0")


def dist2(p: tuple[Fraction, Fraction], q: tuple[Fraction, Fraction]) -> Fraction:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def invert(p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    radius2 = p[0] ** 2 + p[1] ** 2
    return (p[0] / radius2, p[1] / radius2)


def check_trace_delta_kernel_coefficient() -> None:
    g_delta_sq = Fraction(5, 11)
    n_c = Fraction(7, 1)
    c_a_delta = 2 * n_c

    g_half_sq = 2 * g_delta_sq
    c_a_half = n_c

    assert_equal(
        "BFKL color-coupling product",
        g_delta_sq * c_a_delta,
        g_half_sq * c_a_half,
    )


def check_transverse_inversion_covariance() -> None:
    x = (Fraction(1, 1), Fraction(2, 1))
    y = (Fraction(4, 1), Fraction(1, 1))
    z = (Fraction(3, 1), Fraction(5, 1))

    kernel = dist2(x, y) / (dist2(x, z) * dist2(z, y))

    xi, yi, zi = invert(x), invert(y), invert(z)
    transformed_kernel = dist2(xi, yi) / (dist2(xi, zi) * dist2(zi, yi))
    jacobian = Fraction(1, 1) / (z[0] ** 2 + z[1] ** 2) ** 2

    assert_equal("dipole kernel inversion covariance", transformed_kernel * jacobian, kernel)


def check_bfkl_characteristic_values() -> None:
    gamma = sp.symbols("gamma")
    chi = 2 * sp.polygamma(0, 1) - sp.polygamma(0, gamma) - sp.polygamma(0, 1 - gamma)

    assert_zero("BFKL saddle value", chi.subs(gamma, sp.Rational(1, 2)) - 4 * sp.log(2))
    assert_zero("BFKL saddle first derivative", sp.diff(chi, gamma).subs(gamma, sp.Rational(1, 2)))
    assert_zero(
        "BFKL saddle second derivative",
        sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) - 28 * sp.zeta(3),
    )

    nu = sp.symbols("nu")
    quadratic_coefficient = -sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) / 2
    assert_zero("BFKL diffusion coefficient", quadratic_coefficient + 14 * sp.zeta(3))

    gamma_line = sp.Rational(1, 2) + sp.I * nu
    series = 4 * sp.log(2) - 14 * sp.zeta(3) * nu**2
    assert_zero(
        "BFKL nu-expansion through quadratic order",
        sp.series(chi.subs(gamma, gamma_line) - series, nu, 0, 3).removeO(),
    )


def main() -> None:
    check_trace_delta_kernel_coefficient()
    check_transverse_inversion_covariance()
    check_bfkl_characteristic_values()
    print("All QCD small-x/BFKL kernel convention checks passed.")


if __name__ == "__main__":
    main()
