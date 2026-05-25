#!/usr/bin/env python3
"""Finite checks for the scaling Lee-Yang TBA example in Volume VI."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def li2_series(x: float, terms: int = 2000) -> float:
    total = 0.0
    power = x
    for k in range(1, terms + 1):
        total += power / (k * k)
        power *= x
    return total


def rogers_l(x: float) -> float:
    return li2_series(x) + 0.5 * math.log(x) * math.log(1.0 - x)


def lee_yang_s(theta: complex) -> complex:
    s = math.sin(math.pi / 3.0)
    return (cmath.sinh(theta) + 1j * s) / (cmath.sinh(theta) - 1j * s)


def lee_yang_kernel(theta: float) -> float:
    return -(2.0 * math.sqrt(3.0) * math.cosh(theta)) / (math.pi * (2.0 * math.cosh(2.0 * theta) + 1.0))


def check_unitarity_and_crossing() -> None:
    for theta in (0.2, 0.9, -1.3):
        assert_close(f"Lee-Yang unitarity theta={theta}", lee_yang_s(theta) * lee_yang_s(-theta), 1.0)
        assert_close(
            f"Lee-Yang crossing theta={theta}",
            lee_yang_s(theta),
            lee_yang_s(1j * math.pi - theta),
        )


def check_kernel_integral() -> None:
    # With x = sinh(theta), the integral is
    #   -s/pi * integral_R dx/(x^2+s^2) = -1.
    s = math.sin(math.pi / 3.0)
    primitive_at_infty = math.pi / (2.0 * s)
    primitive_at_minus_infty = -math.pi / (2.0 * s)
    exact_integral = -(s / math.pi) * (primitive_at_infty - primitive_at_minus_infty)
    assert_close("Lee-Yang kernel integral", exact_integral, -1.0)

    # A small numerical guard catches sign mistakes in the displayed kernel.
    step = 0.002
    cutoff = 20.0
    n_steps = int(2 * cutoff / step)
    midpoint_sum = sum(lee_yang_kernel(-cutoff + (j + 0.5) * step) * step for j in range(n_steps))
    assert_close("Lee-Yang kernel numerical integral", midpoint_sum, -1.0, tol=5.0e-7)


def check_plateau_and_dilogarithm() -> None:
    golden = (1.0 + math.sqrt(5.0)) / 2.0
    assert_close("Lee-Yang plateau equation", golden, 1.0 + 1.0 / golden)

    x = 1.0 / (golden * golden)
    assert_close("Rogers L(phi^-2)", rogers_l(x), math.pi**2 / 15.0, tol=1.0e-12)
    assert_close("Lee-Yang effective central charge", 6.0 * rogers_l(x) / math.pi**2, 2.0 / 5.0, tol=1.0e-12)


def main() -> None:
    check_unitarity_and_crossing()
    check_kernel_integral()
    check_plateau_and_dilogarithm()
    print("All Lee-Yang TBA checks passed.")


if __name__ == "__main__":
    main()
