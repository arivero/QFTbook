#!/usr/bin/env python3
"""Checks for the spectral zeta determinant examples in Volume I."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math
from fractions import Fraction


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def periodic_resolvent_sum(beta: float, omega: float, cutoff: int) -> float:
    return sum(
        1.0 / ((2.0 * math.pi * n / beta) ** 2 + omega**2)
        for n in range(-cutoff, cutoff + 1)
    )


def closed_periodic_resolvent_sum(beta: float, omega: float) -> float:
    return beta / (2.0 * omega) / math.tanh(beta * omega / 2.0)


def logdet_oscillator(beta: float, omega: float) -> float:
    return 2.0 * math.log(2.0 * math.sinh(beta * omega / 2.0))


def check_resolvent_identity() -> None:
    """Numerically check the partial-fraction identity used in the text."""

    for beta, omega in [(0.7, 1.3), (2.0, 0.4), (3.5, 2.2)]:
        cutoff = 20000
        got = periodic_resolvent_sum(beta, omega, cutoff=cutoff)
        expected = closed_periodic_resolvent_sum(beta, omega)
        tail_bound = beta**2 / (2.0 * math.pi**2 * cutoff)
        if not (0.0 <= expected - got <= tail_bound):
            raise AssertionError(
                f"periodic resolvent beta={beta} omega={omega} failed: "
                f"partial={got:.16g}, closed={expected:.16g}, tail_bound={tail_bound:.16g}"
            )


def check_logdet_derivative() -> None:
    """Check d/domega log det_zeta A = beta coth(beta omega/2)."""

    for beta, omega in [(1.0, 0.8), (2.3, 1.1), (4.0, 0.35)]:
        step = 1.0e-6
        got = (logdet_oscillator(beta, omega + step) - logdet_oscillator(beta, omega - step)) / (2.0 * step)
        expected = beta / math.tanh(beta * omega / 2.0)
        assert_close(f"logdet derivative beta={beta} omega={omega}", got, expected, tol=2.0e-9)


def check_partition_function_identity() -> None:
    """Check the determinant result equals the canonical oscillator trace."""

    for beta, omega in [(0.5, 1.7), (1.4, 0.9), (3.2, 2.1)]:
        determinant = 4.0 * math.sinh(beta * omega / 2.0) ** 2
        zeta_partition = determinant ** (-0.5)
        canonical = math.exp(-beta * omega / 2.0) / (1.0 - math.exp(-beta * omega))
        assert_close(f"oscillator partition beta={beta} omega={omega}", zeta_partition, canonical)


def check_circle_casimir_value() -> None:
    """Check zeta_R(-1) = -1/12 gives E0 = -pi/(6L)."""

    zeta_minus_one = -Fraction(1, 12)
    coefficient = 2 * zeta_minus_one
    assert_equal("circle Casimir rational coefficient", coefficient, -Fraction(1, 6))

    for length in [0.8, 1.0, 5.0]:
        got = (2.0 * math.pi / length) * float(zeta_minus_one)
        expected = -math.pi / (6.0 * length)
        assert_close(f"circle Casimir L={length}", got, expected)


def check_scale_dependence_sign() -> None:
    """Check log det_zeta(A/mu^r) shifts by -zeta_A(0) log(mu^r)."""

    zeta_at_zero = Fraction(3, 5)
    order = 2
    # Changing mu from 1 to e changes log(mu^r) by r.
    expected_shift = -zeta_at_zero * order
    assert_equal("zeta determinant scale sign", expected_shift, -Fraction(6, 5))


def main() -> None:
    check_resolvent_identity()
    check_logdet_derivative()
    check_partition_function_identity()
    check_circle_casimir_value()
    check_scale_dependence_sign()
    print("All zeta-determinant checks passed.")


if __name__ == "__main__":
    main()
