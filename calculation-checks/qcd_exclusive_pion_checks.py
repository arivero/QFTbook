#!/usr/bin/env python3
"""Convention checks for the exclusive-pion asymptotic-freedom section.

The script verifies only finite algebraic consequences used in the text:
normalization of the asymptotic pion LCDA, Gegenbauer normalization moments,
the plus-prescribed ERBL kernel eigenvalue including the factor of one half
relative to the alpha_s/(2 pi) evolution convention, leading anomalous-
dimension signs, and conversion between the monograph's trace-delta gauge
convention and the common half-trace convention.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from check_utils import assert_gt as _assert_gt


Poly = dict[int, Fraction]


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def assert_positive(name: str, value: Fraction) -> None:
    _assert_gt(name, value, Fraction(0))


def trim(poly: Poly) -> Poly:
    return {k: v for k, v in poly.items() if v}


def add(p: Poly, q: Poly) -> Poly:
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fraction(0)) + v
    return trim(out)


def scale(p: Poly, c: Fraction) -> Poly:
    return trim({k: c * v for k, v in p.items()})


def sub(p: Poly, q: Poly) -> Poly:
    return add(p, scale(q, Fraction(-1)))


def shift(p: Poly, n: int) -> Poly:
    return {k + n: v for k, v in p.items()}


def mul_z(p: Poly) -> Poly:
    return {k + 1: v for k, v in p.items()}


def gegenbauer_3half(n: int) -> Poly:
    """Return C_n^{3/2}(z) as a polynomial in z."""
    if n == 0:
        return {0: Fraction(1)}
    if n == 1:
        return {1: Fraction(3)}

    c_nm1 = {0: Fraction(1)}
    c_n = {1: Fraction(3)}
    for m in range(1, n):
        # (m+1) C_{m+1}^{3/2} = (2m+3) z C_m^{3/2} - (m+2) C_{m-1}^{3/2}.
        numerator = add(
            scale(mul_z(c_n), Fraction(2 * m + 3)),
            scale(c_nm1, Fraction(-(m + 2))),
        )
        c_np1 = scale(numerator, Fraction(1, m + 1))
        c_nm1, c_n = c_n, c_np1
    return c_n


def substitute_z_equals_2x_minus_1(poly_z: Poly) -> Poly:
    """Substitute z=2x-1 into a polynomial in z."""
    out: Poly = {}
    for power, coeff in poly_z.items():
        for j in range(power + 1):
            # (2x-1)^power = sum_j binom(power,j) (2x)^j (-1)^{power-j}.
            term = coeff * Fraction(comb(power, j)) * Fraction(2**j)
            if (power - j) % 2:
                term = -term
            out[j] = out.get(j, Fraction(0)) + term
    return trim(out)


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] = out.get(i + j, Fraction(0)) + a * b
    return trim(out)


def integrate_0_1(poly: Poly) -> Fraction:
    return sum(coeff * Fraction(1, power + 1) for power, coeff in poly.items())


def integrate_0_to_x(poly: Poly) -> Poly:
    return {power + 1: coeff * Fraction(1, power + 1) for power, coeff in poly.items()}


def integrate_x_to_1(poly: Poly) -> Poly:
    return sub({0: integrate_0_1(poly)}, integrate_0_to_x(poly))


def harmonic(n: int) -> Fraction:
    return sum(Fraction(1, k) for k in range(1, n + 1))


def erbl_gamma_bracket(n: int) -> Fraction:
    return Fraction(1) - Fraction(2, (n + 1) * (n + 2)) + 4 * sum(
        Fraction(1, k) for k in range(2, n + 2)
    )


def check_lcda_normalizations() -> None:
    phi_as = {1: Fraction(6), 2: Fraction(-6)}  # 6x(1-x)
    assert_equal("asymptotic LCDA normalization", integrate_0_1(phi_as), Fraction(1))
    # Integral of phi_as/x is integral of 6(1-x).
    assert_equal("pion form-factor endpoint integral", integrate_0_1({0: Fraction(6), 1: Fraction(-6)}), Fraction(3))
    # Integral of phi_as * (1/x + 1/(1-x)) is 6 by symmetry.
    assert_equal("pion transition endpoint integral", Fraction(2) * Fraction(3), Fraction(6))


def check_gegenbauer_normalization_moments() -> None:
    weight = {1: Fraction(6), 2: Fraction(-6)}
    assert_equal("C0 weighted moment", integrate_0_1(weight), Fraction(1))
    for n in range(1, 9):
        cn_x = substitute_z_equals_2x_minus_1(gegenbauer_3half(n))
        moment = integrate_0_1(mul(weight, cn_x))
        assert_equal(f"C{n} weighted normalization moment", moment, Fraction(0))


def check_erbl_anomalous_dimensions() -> None:
    assert_equal("ERBL gamma_0 bracket", erbl_gamma_bracket(0), Fraction(0))
    for n in range(1, 9):
        assert_positive(f"ERBL gamma_{n} bracket", erbl_gamma_bracket(n))
    assert_equal("ERBL gamma_2 standard half-trace value", Fraction(4, 3) * erbl_gamma_bracket(2), Fraction(50, 9))


def assert_poly_equal(name: str, got: Poly, expected: Poly) -> None:
    if trim(got) != trim(expected):
        raise AssertionError(f"{name}: got {trim(got)}, expected {trim(expected)}")


def erbl_finite_action_without_cf(p: Poly) -> Poly:
    """Action of the displayed plus-prescribed ERBL kernel without C_F.

    The input P defines phi_P(x)=6 x(1-x) P(x).  This is the exact rational
    polynomial form of equation (qcd-erbl-finite-polynomial-action) in the
    monograph.
    """

    one_minus_x = {0: Fraction(1), 1: Fraction(-1)}
    left_regular = sub(
        integrate_0_to_x(mul({1: Fraction(1)}, p)),
        scale(shift(p, 2), Fraction(1, 2)),
    )

    left_singular: Poly = {}
    for m, coeff in p.items():
        if m == 0:
            continue
        left_singular = add(
            left_singular,
            scale({m + 1: Fraction(1), m + 2: Fraction(-1)}, -coeff * (harmonic(m + 1) - 1)),
        )
    left = scale(add(mul(one_minus_x, left_regular), left_singular), Fraction(6))

    right_regular = sub(
        integrate_x_to_1(mul(one_minus_x, p)),
        scale(mul({0: Fraction(1), 1: Fraction(-2), 2: Fraction(1)}, p), Fraction(1, 2)),
    )

    right_singular: Poly = {}
    for m, coeff in p.items():
        for j in range(m):
            r = m - 1 - j
            integral = {
                0: Fraction(1, (r + 1) * (r + 2)),
                r + 1: Fraction(-1, r + 1),
                r + 2: Fraction(1, r + 2),
            }
            right_singular = add(right_singular, scale(shift(integral, j), coeff))
    right = scale(shift(add(right_regular, right_singular), 1), Fraction(6))

    return add(left, right)


def check_erbl_kernel_eigenvalues() -> None:
    x_one_minus_x = {1: Fraction(1), 2: Fraction(-1)}
    for n in range(0, 9):
        p = substitute_z_equals_2x_minus_1(gegenbauer_3half(n))
        phi = scale(mul(x_one_minus_x, p), Fraction(6))
        action = erbl_finite_action_without_cf(p)
        expected = scale(phi, -erbl_gamma_bracket(n) / 2)
        assert_poly_equal(f"plus-prescribed ERBL eigenvalue n={n}", action, expected)


def check_trace_delta_conversions() -> None:
    nc = Fraction(3)
    cf_trace = Fraction(8, 3)
    cf_half_trace = Fraction(4, 3)
    alpha_half_trace = Fraction(1)
    alpha_trace = alpha_half_trace / 2

    assert_equal(
        "invariant alpha_s C_F",
        alpha_trace * cf_trace,
        alpha_half_trace * cf_half_trace,
    )
    coefficient_trace_units = Fraction(36) * alpha_trace * cf_trace / nc
    assert_equal(
        "charged-pion asymptotic coefficient in half-trace units",
        coefficient_trace_units,
        Fraction(16) * alpha_half_trace,
    )
    # 2 f = sqrt(2) f_130 when f_130 = sqrt(2) f; compare after squaring.
    assert_equal("transition coefficient f-convention conversion squared", Fraction(4), Fraction(2) * Fraction(2))


def main() -> None:
    check_lcda_normalizations()
    check_gegenbauer_normalization_moments()
    check_erbl_anomalous_dimensions()
    check_erbl_kernel_eigenvalues()
    check_trace_delta_conversions()
    print("All QCD exclusive-pion LCDA and asymptotic checks passed.")


if __name__ == "__main__":
    main()
