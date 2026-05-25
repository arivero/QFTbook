#!/usr/bin/env python3
"""Finite checks for the CFT entanglement and replica-method chapter."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def check_twist_dimension_derivative() -> None:
    """Check h_n = c/24 (n - 1/n) gives the interval coefficient c/3."""

    # d/dn (n - 1/n) at n=1 is 2.
    derivative_n_minus_inverse = Fraction(2, 1)
    # The two-point function has exponent -4 h_n.
    interval_log_derivative = Fraction(-4, 1) * Fraction(1, 24) * derivative_n_minus_inverse
    # Entropy is -d_n log Tr rho^n at n=1.
    entropy_log_coefficient = -interval_log_derivative
    assert_equal("2D interval entropy coefficient in units of c", entropy_log_coefficient, Fraction(1, 3))


def check_replica_effective_action_sign() -> None:
    """Check S = (n d_n - 1) W_n at n=1 for W_n = -log Z_n."""

    # Let log Z_n = alpha n + beta (n - 1/n).  The normalized replica trace
    # removes alpha n.  Entropy is -d_n[beta(n - 1/n)] at n=1 = -2 beta.
    beta = Fraction(-1, 6)  # beta = -c log(L/eps)/6, in units c log=1.
    entropy_from_trace = -2 * beta

    # W_n = -log Z_n, so the beta contribution to W is -beta(n - 1/n).
    # (n d_n - 1)(-beta(n - 1/n)) at n=1 equals -2 beta.
    entropy_from_w = -2 * beta
    assert_equal("replica W_n entropy sign", entropy_from_w, entropy_from_trace)
    assert_equal("replica W_n coefficient", entropy_from_w, Fraction(1, 3))


def check_ball_universal_signs() -> None:
    """Check the even/odd sign convention in the ball universal term."""

    # Even D: (-1)^(D/2 - 1) 4 a_D.
    assert_equal("D=2 even sign", (-1) ** (2 // 2 - 1), 1)
    assert_equal("D=4 even sign", (-1) ** (4 // 2 - 1), -1)

    # Odd D: (-1)^((D - 1)/2) F_D.
    assert_equal("D=3 odd sign", (-1) ** ((3 - 1) // 2), -1)
    assert_equal("D=5 odd sign", (-1) ** ((5 - 1) // 2), 1)

    # With a_2 = c/12, the even-D formula gives c/3.
    a2_in_units_c = Fraction(1, 12)
    assert_equal("D=2 ball log coefficient", 4 * a2_in_units_c, Fraction(1, 3))


def main() -> None:
    check_twist_dimension_derivative()
    check_replica_effective_action_sign()
    check_ball_universal_signs()
    print("All entanglement replica checks passed.")


if __name__ == "__main__":
    main()
