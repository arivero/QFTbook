#!/usr/bin/env python3
"""Exact finite checks for minimized N-subjettiness continuity.

The checks use the beta=2, N=1 case on a one-dimensional angular patch.  In
that case the minimizing axis is the weighted mean and tau is the normalized
weighted variance, so the soft and collinear estimates in the jet-substructure
chapter reduce to exact rational identities.
"""

from __future__ import annotations

from fractions import Fraction


Point = tuple[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def mass(points: tuple[Point, ...]) -> Fraction:
    return sum(weight for weight, _ in points)


def weighted_mean(points: tuple[Point, ...]) -> Fraction:
    total = mass(points)
    return sum(weight * position for weight, position in points) / total


def raw_variance(points: tuple[Point, ...]) -> Fraction:
    mean = weighted_mean(points)
    return sum(weight * (position - mean) ** 2 for weight, position in points)


def tau1_beta2(points: tuple[Point, ...], radius: Fraction = Fraction(1, 1)) -> Fraction:
    return raw_variance(points) / (mass(points) * radius**2)


def check_soft_addition_bound() -> None:
    base: tuple[Point, ...] = ((Fraction(2), Fraction(0)), (Fraction(3), Fraction(1)))
    epsilon = Fraction(1, 10)
    soft_point = Fraction(1, 2)
    enlarged = base + ((epsilon, soft_point),)

    change = abs(tau1_beta2(enlarged) - tau1_beta2(base))
    bound = 2 * epsilon / mass(base)
    assert_true("soft addition obeys 2 epsilon / m0 bound", change <= bound)


def check_collinear_recombination_identity() -> None:
    theta = Fraction(1, 20)
    ea = Fraction(1, 1)
    eb = Fraction(2, 1)
    x_a = Fraction(1, 2)
    x_b = x_a + theta
    parent = (ea * x_a + eb * x_b) / (ea + eb)

    spectators: tuple[Point, ...] = ((Fraction(5, 1), Fraction(0, 1)),)
    split_event = spectators + ((ea, x_a), (eb, x_b))
    recombined_event = spectators + ((ea + eb, parent),)

    raw_drop = raw_variance(split_event) - raw_variance(recombined_event)
    expected_raw_drop = ea * eb / (ea + eb) * theta**2
    assert_equal("within-cluster variance drop", raw_drop, expected_raw_drop)

    tau_drop = tau1_beta2(split_event) - tau1_beta2(recombined_event)
    expected_tau_drop = expected_raw_drop / mass(split_event)
    assert_equal("normalized collinear tau drop", tau_drop, expected_tau_drop)


def check_value_not_axis_choice() -> None:
    # Two equal point-masses can be represented by either ordered axis pair in
    # tau_2.  The minimized value is zero independently of that discrete
    # labeling choice; the observable is the value, not an axis label.
    points: tuple[Point, ...] = ((Fraction(1), Fraction(0)), (Fraction(1), Fraction(1)))
    value_axes_01 = sum(weight * min((position - Fraction(0)) ** 2, (position - Fraction(1)) ** 2) for weight, position in points)
    value_axes_10 = sum(weight * min((position - Fraction(1)) ** 2, (position - Fraction(0)) ** 2) for weight, position in points)
    assert_equal("tau2 minimized value for swapped axes", value_axes_01, value_axes_10)
    assert_equal("tau2 two-point minimized value", value_axes_01, Fraction(0))


def main() -> None:
    check_soft_addition_bound()
    check_collinear_recombination_identity()
    check_value_not_axis_choice()
    print("All minimized N-subjettiness continuity checks passed.")


if __name__ == "__main__":
    main()
