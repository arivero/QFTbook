#!/usr/bin/env python3
"""Convention checks for the microlocal spectrum chapter.

The metric convention is mostly plus.  A causal covector is called future
directed when its metric dual vector is future directed.  In flat coordinates
this makes the positive-frequency covector (-E, p) future directed.
"""

from __future__ import annotations

from fractions import Fraction
import math


def assert_close(got: float, expected: float, label: str, tol: float = 1e-12) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_equal(got: Fraction, expected: Fraction, label: str) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def covector_square(k0: float, k1: float) -> float:
    return -(k0 * k0) + k1 * k1


def sharp(k0: float, k1: float) -> tuple[float, float]:
    # Mostly-plus inverse metric diag(-1,1) in the boost plane.
    return (-k0, k1)


def hamilton_vector_for_kg(k0: float, k1: float) -> tuple[float, float]:
    # p=-k0^2+k1^2, so dx/ds = partial p / partial k.
    return (-2 * k0, 2 * k1)


def check_future_covector_convention() -> None:
    p = 0.7
    energy = abs(p)
    k0, k1 = -energy, p
    v0, v1 = sharp(k0, k1)
    assert v0 > 0
    assert_close(covector_square(k0, k1), 0.0, "null covector")
    assert_close(-(v0 * v0) + v1 * v1, 0.0, "dual null vector")


def check_kg_hamilton_flow_is_future_null_for_positive_frequency() -> None:
    p = -1.3
    energy = abs(p)
    k0, k1 = -energy, p
    xdot0, xdot1 = hamilton_vector_for_kg(k0, k1)
    assert xdot0 > 0
    assert_close(-(xdot0 * xdot0) + xdot1 * xdot1, 0.0, "Hamilton flow null")
    # The Hamilton vector is twice the metric dual covector.
    v0, v1 = sharp(k0, k1)
    assert_close(xdot0, 2 * v0, "Hamilton/dual time component")
    assert_close(xdot1, 2 * v1, "Hamilton/dual space component")


def check_two_point_graph_sign_pattern() -> None:
    p = 0.4
    energy = abs(p)
    future_covector = (-energy, p)
    k1 = future_covector
    k2 = tuple(-x for x in future_covector)
    assert k1[0] < 0
    assert k2[0] > 0
    total = (k1[0] + k2[0], k1[1] + k2[1])
    assert_close(total[0], 0.0, "two-point graph covector conservation time")
    assert_close(total[1], 0.0, "two-point graph covector conservation space")


def check_product_opposite_cone_obstruction() -> None:
    positive = {(1, 0)}
    negative = {(-1, 0)}

    def has_opposite_pair(cone_a: set[tuple[int, int]], cone_b: set[tuple[int, int]]) -> bool:
        return any((-a[0], -a[1]) in cone_b for a in cone_a)

    if has_opposite_pair(positive, positive):
        raise AssertionError("same half-cone should not obstruct product")
    if not has_opposite_pair(positive, negative):
        raise AssertionError("opposite half-cones should obstruct product")


def check_hadamard_transport_coefficients() -> None:
    # In four dimensions [Box sigma]=4.  The v_0 transport equation gives
    # 2 v_0(x,x) = P U|_diag, and Box U|_diag = R/6.  Therefore the curvature
    # coefficient in v_0 is (xi - 1/6)/2.
    box_sigma_diag = Fraction(4)
    v0_denominator = box_sigma_diag - Fraction(2)
    assert_equal(v0_denominator, Fraction(2), "v0 diagonal denominator")

    mass_coeff = Fraction(1, 1) / v0_denominator
    xi_coeff = Fraction(1, 1) / v0_denominator
    curvature_from_box_u = Fraction(-1, 6) / v0_denominator
    assert_equal(mass_coeff, Fraction(1, 2), "v0 mass coefficient")
    assert_equal(xi_coeff, Fraction(1, 2), "v0 xi coefficient")
    assert_equal(curvature_from_box_u, Fraction(-1, 12), "v0 curvature shift")

    for j in range(6):
        diag_coeff = Fraction(1, (j + 1) * (4 + 2 * j))
        expected = Fraction(1, 2 * (j + 1) * (j + 2))
        assert_equal(diag_coeff, expected, f"v_{j + 1} recursion denominator")


def main() -> None:
    check_future_covector_convention()
    check_kg_hamilton_flow_is_future_null_for_positive_frequency()
    check_two_point_graph_sign_pattern()
    check_product_opposite_cone_obstruction()
    check_hadamard_transport_coefficients()
    print("All microlocal spectrum convention checks passed.")


if __name__ == "__main__":
    main()
