#!/usr/bin/env python3
"""Exact checks for the back-to-back EEC leading Sudakov factor.

The QCD energy-correlator section derives the fixed-coupling leading
Sudakov exponent

    S_LL = (1/2) Gamma_cusp^q L_b^2

from the cusp-evolution integral between mu_b and Q.  This script verifies
the rational coefficient of the logarithmic integral and the trace-delta
versus half-trace convention conversion for the one-loop cusp coefficient.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def poly_integral_0_to_l(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Return coefficients of the antiderivative from 0 to L."""

    result = [Fraction(0) for _ in range(len(poly) + 1)]
    for power, coeff in enumerate(poly):
        result[power + 1] = coeff / Fraction(power + 1)
    return tuple(result)


def poly_derivative(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if len(poly) <= 1:
        return (Fraction(0),)
    return tuple(Fraction(power) * coeff for power, coeff in enumerate(poly[1:], start=1))


def check_sudakov_log_integral() -> None:
    # The cusp integral is int_0^L u du = L^2/2.
    integrand_u = (Fraction(0), Fraction(1))
    integral = poly_integral_0_to_l(integrand_u)
    assert_equal("Sudakov integral coefficient", integral, (Fraction(0), Fraction(0), Fraction(1, 2)))
    assert_equal("Sudakov derivative", poly_derivative(integral), integrand_u)


def check_trace_convention_cusp_invariance() -> None:
    # In the monograph trace-delta convention
    # C_F = (N_c^2-1)/N_c.  In the common half-trace convention
    # C_F^ht = C_F/2 and g_ht^2 = 2 g^2, so g^2 C_F is invariant.
    for n_c in (2, 3, 5, 7):
        c_f_trace_delta = Fraction(n_c * n_c - 1, n_c)
        c_f_half_trace = c_f_trace_delta / 2
        g_squared_units = Fraction(1)
        g_ht_squared_units = Fraction(2)
        assert_equal(
            f"one-loop cusp convention product SU({n_c})",
            g_squared_units * c_f_trace_delta,
            g_ht_squared_units * c_f_half_trace,
        )


def check_fixed_coupling_solution() -> None:
    # If W(L)=exp[-Gamma L^2/2], then d log W/dL = -Gamma L.
    # Track only the polynomial multiplying Gamma.
    log_w_polynomial = (Fraction(0), Fraction(0), Fraction(-1, 2))
    assert_equal(
        "fixed-coupling Sudakov differential equation",
        poly_derivative(log_w_polynomial),
        (Fraction(0), Fraction(-1)),
    )


def main() -> None:
    check_sudakov_log_integral()
    check_trace_convention_cusp_invariance()
    check_fixed_coupling_solution()
    print("All EEC Sudakov checks passed.")


if __name__ == "__main__":
    main()
