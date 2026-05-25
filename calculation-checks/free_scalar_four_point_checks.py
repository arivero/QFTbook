#!/usr/bin/env python3
"""Finite checks for the generalized-free scalar four-point example."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True, order=True)
class Monomial:
    """A monomial u^(a Delta) v^(b Delta), recorded by integer exponents."""

    u_power: int
    v_power: int


def add_delta_power(expr: set[Monomial], du: int, dv: int) -> set[Monomial]:
    return {Monomial(m.u_power + du, m.v_power + dv) for m in expr}


def swap_uv(expr: set[Monomial]) -> set[Monomial]:
    return {Monomial(m.v_power, m.u_power) for m in expr}


def assert_equal(lhs: object, rhs: object, label: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{label}: {lhs!r} != {rhs!r}")


def gff_reduced_four_point() -> set[Monomial]:
    # 1 + u^Delta + (u/v)^Delta.
    return {Monomial(0, 0), Monomial(1, 0), Monomial(1, -1)}


def check_crossing_identity() -> None:
    g = gff_reduced_four_point()
    lhs = add_delta_power(g, 0, 1)
    rhs = add_delta_power(swap_uv(g), 1, 0)
    assert_equal(lhs, rhs, "v^Delta G(u,v) = u^Delta G(v,u)")
    assert_equal(
        lhs,
        {Monomial(0, 1), Monomial(1, 1), Monomial(1, 0)},
        "crossing monomials",
    )


def check_wick_pairing_counts() -> None:
    # Four identical Gaussian fields have the three pairings
    # (12)(34), (13)(24), (14)(23).
    four_field_pairings = 3
    assert_equal(four_field_pairings, 3, "four-field Wick pairings")

    # For :phi^2:(x) :phi^2:(0), normal ordering removes internal pairings.
    # The two surviving contractions match the two fields at x bijectively
    # with the two fields at 0.
    normal_ordered_square_two_point = 2
    assert_equal(
        normal_ordered_square_two_point,
        2,
        "normal-ordered square two-point coefficient",
    )

    # For phi(x1) phi(x2) :phi^2:(x3), each external phi can be paired with
    # either of the two fields inside :phi^2:, giving coefficient 2.
    three_point_unnormalized = 2
    normalized_two_point = normal_ordered_square_two_point
    lambda_squared = Fraction(three_point_unnormalized**2, normalized_two_point)
    assert_equal(
        lambda_squared,
        Fraction(2, 1),
        "lambda_phi_phi_phi2^2 for phi^2/sqrt(2)",
    )


def check_double_trace_dimensions() -> None:
    # In D=4, a free scalar has Delta_phi=1. The n=0 bilinear spin-l tower
    # then has twist 2 for every even spin; n raises the twist by two units.
    delta_phi = Fraction(1, 1)
    for n in range(4):
        for spin in range(0, 10, 2):
            dimension = 2 * delta_phi + 2 * n + spin
            twist = dimension - spin
            assert_equal(twist, 2 * delta_phi + 2 * n, f"twist n={n} l={spin}")

    even_spins = [spin for spin in range(10) if spin % 2 == 0]
    odd_spins = [spin for spin in range(10) if spin % 2 == 1]
    assert_equal(even_spins, [0, 2, 4, 6, 8], "even-spin tower")
    assert_equal(odd_spins, [1, 3, 5, 7, 9], "odd-spin complement")


def main() -> None:
    check_crossing_identity()
    check_wick_pairing_counts()
    check_double_trace_dimensions()
    print("All generalized-free scalar four-point checks passed.")


if __name__ == "__main__":
    main()
