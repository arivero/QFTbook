#!/usr/bin/env python3
r"""Finite checks for the OS-to-Wightman analytic continuation conventions.

The OS reconstruction chapter uses the monograph's mostly-plus convention.
Positive-energy support gives a Wightman tube

    z = xi - i eta,    eta in V_+,

not a literal imaginary part in V_+.  These checks keep the Euclidean
ordered-time map and the abstract Fourier-Laplace cone variable aligned with
that convention.  The final check records the finite insertion induction used
in the OS-II argument-domain exhaustion: a \(k\)-gap argument box is obtained
by inserting one bridge angle at a time.
"""

from __future__ import annotations

from fractions import Fraction


Vector = tuple[Fraction, Fraction, Fraction, Fraction]


def vec(*entries: int) -> Vector:
    return tuple(Fraction(entry) for entry in entries)  # type: ignore[return-value]


def minkowski_dot(a: Vector, b: Vector) -> Fraction:
    """Mostly-plus inner product: -a0 b0 + ai bi."""

    return -a[0] * b[0] + sum(a[i] * b[i] for i in range(1, 4))


def assert_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def check_forward_cone_damping() -> None:
    p = vec(5, 3, 0, 0)
    eta = vec(4, 1, 0, 0)
    dot = minkowski_dot(p, eta)
    assert_equal("mostly-plus future dot product", dot, Fraction(-17))
    assert_true("xi - i eta damps positive energy", dot < 0)
    assert_true("xi + i eta would grow positive energy", -dot > 0)


def check_ordered_euclidean_time_map() -> None:
    epsilon_1 = Fraction(5, 1)
    epsilon_2 = Fraction(2, 1)
    t_1 = Fraction(11, 1)
    t_2 = Fraction(7, 1)

    real_difference = t_1 - t_2
    tube_depth = epsilon_1 - epsilon_2
    literal_imaginary_part = -tube_depth

    assert_equal("ordered real time difference", real_difference, Fraction(4))
    assert_equal("future tube depth", tube_depth, Fraction(3))
    assert_equal("literal imaginary part is negative depth", literal_imaginary_part, Fraction(-3))
    assert_true("ordered epsilons give future tube depth", tube_depth > 0)


def check_abstract_cone_variable_conversion() -> None:
    p = vec(5, 3, 0, 0)
    eta = vec(4, 1, 0, 0)
    y = tuple(-component for component in eta)  # literal imaginary variable x + i y

    assert_equal("abstract dual variable has positive cone pairing", minkowski_dot(p, y), Fraction(17))
    assert_equal("physical tube depth has negative cone pairing", minkowski_dot(p, eta), Fraction(-17))


def check_argument_box_insertion_exhaustion() -> None:
    half_width = Fraction(10, 1)
    epsilon = Fraction(1, 1)
    available_width = half_width - epsilon

    # In units where pi/2 is represented by half_width, the OS-II proof uses
    # only strict sub-boxes.  The insertion recurrence starts from the one-gap
    # interval and adds one arbitrary bridge coordinate at each step.
    max_k = 8
    stages: dict[int, tuple[Fraction, int]] = {1: (half_width, 1)}
    for k in range(2, max_k + 1):
        previous_width, previous_stage = stages[k - 1]
        bridge_width = half_width
        stages[k] = (min(bridge_width, previous_width), previous_stage + 1)

    for k in range(1, max_k + 1):
        width, stage = stages[k]
        assert_true(f"OS-II argument box width for k={k}", width >= available_width)
        assert_equal(f"OS-II insertion stage bound for k={k}", stage, k)

    # A sample target argument vector in the strict k-box remains in the
    # constructed box after the k insertion steps.
    target = tuple(Fraction(i - 4, 1) for i in range(max_k))
    assert_true("sample target lies in strict box", all(abs(v) <= available_width for v in target))
    assert_true("sample target lies in inserted box", all(abs(v) <= stages[max_k][0] for v in target))


def main() -> None:
    check_forward_cone_damping()
    check_ordered_euclidean_time_map()
    check_abstract_cone_variable_conversion()
    check_argument_box_insertion_exhaustion()
    print("All OS tube-sign, Euclidean-time ordering, and argument-domain checks passed.")


if __name__ == "__main__":
    main()
