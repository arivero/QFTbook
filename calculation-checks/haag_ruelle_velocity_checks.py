#!/usr/bin/env python3
"""Finite checks for Haag--Ruelle velocity-support conventions.

The corresponding chapter proves the analytic stationary-phase estimates.
This script verifies the convention-sensitive finite algebra: positive-energy
phase cancellation, relativistic group velocity, tube-separation arithmetic,
and the lower bound on the nonstationary phase gradient away from the velocity
support.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def assert_true(condition, label):
    if not condition:
        raise AssertionError(label)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm_sq(v):
    return dot(v, v)


def check_mass_shell_velocity():
    mass_sq = Fraction(9, 1)
    momentum = (Fraction(4, 1), Fraction(0, 1))
    omega_sq = norm_sq(momentum) + mass_sq
    assert_equal(omega_sq, Fraction(25, 1), "sample omega squared")

    velocity = tuple(component / Fraction(5, 1) for component in momentum)
    assert_equal(velocity, (Fraction(4, 5), Fraction(0, 1)), "group velocity")
    assert_true(norm_sq(velocity) < 1, "massive group velocity is subluminal")


def check_one_particle_phase_cancellation():
    # h_t contributes exp(i omega t - i p.x), while U(t,x) on a ket
    # contributes exp(-i omega t + i p.x) in the monograph convention.
    omega_t = Fraction(7, 3)
    p_dot_x = Fraction(11, 5)
    exponent = (omega_t - p_dot_x) + (-omega_t + p_dot_x)
    assert_equal(exponent, Fraction(0, 1), "one-particle phase cancellation")


def check_velocity_tube_separation():
    v_i = (Fraction(0, 1), Fraction(0, 1))
    v_j = (Fraction(4, 5), Fraction(0, 1))
    delta = Fraction(4, 5)
    epsilon = Fraction(1, 10)
    assert_true(epsilon < delta / 4, "epsilon is inside separation range")

    time = Fraction(10, 1)
    x_over_t = (v_i[0] + epsilon, v_i[1])
    y_over_t = (v_j[0] - epsilon, v_j[1])
    separation = time * abs(x_over_t[0] - y_over_t[0])
    lower_bound = time * delta / 2
    assert_equal(separation, Fraction(6, 1), "tube separation sample")
    assert_true(separation >= lower_bound, "tube separation lower bound")


def check_nonstationary_gradient_bound():
    velocity = (Fraction(1, 3), Fraction(0, 1))
    x_over_t = (Fraction(5, 6), Fraction(0, 1))
    epsilon = Fraction(1, 2)
    gradient = tuple(a - b for a, b in zip(velocity, x_over_t))
    assert_equal(norm_sq(gradient), epsilon * epsilon, "gradient gap squared")
    assert_true(norm_sq(gradient) >= epsilon * epsilon, "gradient gap bound")


def main():
    check_mass_shell_velocity()
    check_one_particle_phase_cancellation()
    check_velocity_tube_separation()
    check_nonstationary_gradient_bound()
    print("All Haag-Ruelle velocity-support checks passed.")


if __name__ == "__main__":
    main()
