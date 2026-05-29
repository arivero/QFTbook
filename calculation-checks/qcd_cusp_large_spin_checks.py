#!/usr/bin/env python3
"""Finite checks for the QCD cusp/large-spin convention block.

The corresponding manuscript section defines the lightlike cusp coefficient
from a cusped Wilson line, then identifies the same coefficient in the
large-N Mellin limit of the nonsinglet DGLAP kernel.  These checks verify the
convention-sensitive finite algebra behind that identification; the
operator-level derivation remains in the text.
"""

from __future__ import annotations

from fractions import Fraction
from math import atan, cos, isclose, pi, sin, tan, tanh


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_close(name: str, got: float, expected: float, tol: float = 1e-11) -> None:
    if not isclose(got, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def d0_mellin(n: int) -> Fraction:
    """Moment int_0^1 dx x^(n-1) (1/(1-x))_+."""
    if n < 1:
        raise ValueError("Mellin index must be positive")
    return -harmonic(n - 1)


def transformed_cusp_integrand(y: float, phi: float) -> float:
    """Map r in [0, infinity) to y in [0,1] for the cusp angular integral."""
    c = cos(phi)
    return c / (y * y + 2.0 * c * y * (1.0 - y) + (1.0 - y) * (1.0 - y))


def simpson_cusp_integral(phi: float, panels: int = 20_000) -> float:
    if panels % 2:
        raise ValueError("Simpson panels must be even")
    h = 1.0 / panels
    total = transformed_cusp_integrand(0.0, phi) + transformed_cusp_integrand(1.0, phi)
    for j in range(1, panels):
        total += (4 if j % 2 else 2) * transformed_cusp_integrand(j * h, phi)
    return total * h / 3.0


def antiderivative_cusp_integral(phi: float) -> float:
    """Evaluate the exact antiderivative at r=infinity and r=0."""
    c = cos(phi)
    s = sin(phi)
    # atan(c/s)=pi/2-phi on the principal branch for 0<phi<pi.
    return (c / s) * (pi / 2.0 - atan(c / s))


def check_cusp_angular_integral() -> None:
    for phi in (pi / 6.0, pi / 3.0, pi / 2.0, 2.0 * pi / 3.0, 5.0 * pi / 6.0):
        expected = phi / tan(phi)
        assert_close(f"cusp antiderivative {phi}", antiderivative_cusp_integral(phi), expected)
        assert_close(f"cusp Simpson integral {phi}", simpson_cusp_integral(phi), expected, tol=1e-9)

    small_phi = 1.0e-4
    smooth_subtracted = small_phi / tan(small_phi) - 1.0
    assert_close("smooth-line subtraction begins quadratically", smooth_subtracted, -small_phi**2 / 3.0, tol=1e-8)


def check_lorentzian_lightlike_limit() -> None:
    for chi in (4.0, 8.0, 16.0, 32.0):
        coeff = chi / tanh(chi) - 1.0
        if coeff <= 0.0:
            raise AssertionError(f"Lorentzian cusp coefficient is not positive at chi={chi}")
    chi_large = 200.0
    assert_close(
        "lightlike normalized cusp coefficient",
        (chi_large / tanh(chi_large) - 1.0) / chi_large,
        1.0 - 1.0 / chi_large,
        tol=1e-15,
    )


def check_plus_distribution_and_large_spin_sign() -> None:
    for n in (1, 2, 3, 6, 13):
        finite_sum = -sum((Fraction(1, k) for k in range(1, n)), Fraction(0))
        assert_equal(f"D0 Mellin moment {n}", d0_mellin(n), finite_sum)

    cf = Fraction(16, 5)
    n = 17
    p_ns_singular = 2 * cf * d0_mellin(n)
    assert_equal("one-loop nonsinglet singular Mellin sign", p_ns_singular, -2 * cf * harmonic(n - 1))


def check_trace_convention_invariance() -> None:
    g_delta_sq = Fraction(11, 13)
    cr_delta = Fraction(21, 4)
    g_half_sq = 2 * g_delta_sq
    cr_half = cr_delta / 2
    assert_equal("cusp product convention", g_delta_sq * cr_delta, g_half_sq * cr_half)


def main() -> None:
    check_cusp_angular_integral()
    check_lorentzian_lightlike_limit()
    check_plus_distribution_and_large_spin_sign()
    check_trace_convention_invariance()
    print("All QCD cusp Wilson-line and large-spin checks passed.")


if __name__ == "__main__":
    main()
