#!/usr/bin/env python3
"""Exact checks for the back-to-back EEC Sudakov and recoil bookkeeping.

The QCD energy-correlator section derives the fixed-coupling leading
Sudakov exponent

    S_LL = (1/2) Gamma_cusp^q L_b^2

from the cusp-evolution integral between mu_b and Q.  This script verifies
the rational coefficient of the logarithmic integral and the trace-delta
versus half-trace convention conversion for the one-loop cusp coefficient.

Evidence contract.
Target claims:
  - Eq. (qcd-eec-leading-sudakov-factor): the fixed-coupling cusp integral
    gives the coefficient L_b^2/2 with the displayed sign convention.
  - Controlled approximation (qcd-eec-tested-back-to-back-recoil): a tested
    recoil chart pulls detector tests back by zeta=-1+q_T^2/Q^2 and its
    residual budget must retain perturbative, matching, large-b, and power
    components separately.
Independent construction:
  - Polynomial antiderivatives compute the cusp integral and the q_T^2 test
    pullback directly, without substituting the target formulas.
  - The residual check uses exact signed rational defects and an l1 bound.
Imported assumptions:
  - Fixed coupling, omitted non-cusp anomalous dimensions, the declared
    trace-delta generator convention, and a one-dimensional q_T^2 endpoint
    chart for the tested recoil functional.
Negative controls:
  - The half-trace conversion would fail if g^2 C_F were not invariant.
  - The wrong angular pullback zeta=-1-q_T^2/Q^2 gives a different first
    moment.
  - Dropping the large-b/nonperturbative residual can make the tested bound
    false.
Scope boundary:
  - These checks do not prove TMD factorization, running-coupling resummation,
    soft/Glauber cancellation, convergence of the Fourier integral, or a
    nonperturbative large-b model.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from check_utils import assert_gt, assert_leq


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


def integrate_recoil_test_pullback(
    zeta_poly: tuple[Fraction, ...],
    q2_max: Fraction,
    q2_scale: Fraction,
    *,
    sign: int = 1,
) -> Fraction:
    """Integrate phi(-1 + sign*s/Q^2) ds over 0 <= s <= q2_max."""

    total = Fraction(0)
    for power, coeff in enumerate(zeta_poly):
        for k in range(power + 1):
            binomial_coeff = Fraction(comb(power, k))
            zeta_coeff = coeff * binomial_coeff * Fraction(-1) ** (power - k) * Fraction(sign) ** k
            total += zeta_coeff * q2_max ** (k + 1) / (Fraction(k + 1) * q2_scale**k)
    return total


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


def check_back_to_back_test_pullback() -> None:
    # In the recoil endpoint chart q_T^2 = Q^2 (1 + zeta), so detector tests
    # pull back as phi_Q(s)=phi(-1+s/Q^2).  Check the first two moments by
    # exact polynomial integration in s=q_T^2.
    q2_scale = Fraction(25)
    q2_max = Fraction(5)
    constant_test = (Fraction(1),)
    zeta_test = (Fraction(0), Fraction(1))
    quadratic_test = (Fraction(3, 7), Fraction(-2, 5), Fraction(11, 13))

    assert_equal(
        "recoil constant-test pullback",
        integrate_recoil_test_pullback(constant_test, q2_max, q2_scale),
        q2_max,
    )
    assert_equal(
        "recoil zeta-test pullback",
        integrate_recoil_test_pullback(zeta_test, q2_max, q2_scale),
        -q2_max + q2_max**2 / (2 * q2_scale),
    )

    correct = integrate_recoil_test_pullback(quadratic_test, q2_max, q2_scale)
    wrong_sign = integrate_recoil_test_pullback(quadratic_test, q2_max, q2_scale, sign=-1)
    if correct == wrong_sign:
        raise AssertionError("wrong recoil angular pullback should not preserve a generic test")


def check_back_to_back_residual_budget() -> None:
    # A measured-bin recoil error is a signed sum of several distinct defects.
    # The declared l1 budget bounds the total.  Omitting the large-b component
    # is not a harmless convention change: for this exact finite example the
    # remaining terms no longer bound the actual residual.
    factorization = Fraction(1, 11)
    rg_truncation = Fraction(-1, 13)
    overlap_matching = Fraction(1, 17)
    large_b = Fraction(5, 7)
    power = Fraction(-1, 19)

    residual = factorization + rg_truncation + overlap_matching + large_b + power
    full_bound = (
        abs(factorization)
        + abs(rg_truncation)
        + abs(overlap_matching)
        + abs(large_b)
        + abs(power)
    )
    assert_leq("back-to-back measured-bin residual budget", abs(residual), full_bound)

    incomplete_bound = full_bound - abs(large_b)
    assert_gt(
        "dropping the large-b residual invalidates this budget",
        abs(residual),
        incomplete_bound,
    )


def main() -> None:
    check_sudakov_log_integral()
    check_trace_convention_cusp_invariance()
    check_fixed_coupling_solution()
    check_back_to_back_test_pullback()
    check_back_to_back_residual_budget()
    print("All EEC Sudakov checks passed.")


if __name__ == "__main__":
    main()
