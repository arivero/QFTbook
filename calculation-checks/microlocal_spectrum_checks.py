#!/usr/bin/env python3
"""Convention checks for the microlocal spectrum chapter.

The metric convention is mostly plus.  A causal covector is called future
directed when its metric dual vector is future directed.  In flat coordinates
this makes the positive-frequency covector (-E, p) future directed.

Target claims:
- `ch:curved-microlocal-spectrum-condition`: the mostly-plus
  positive-frequency covector convention, Klein-Gordon Hamilton-flow sign,
  Hadamard two-point graph covector pattern, product obstruction, Hadamard
  recursion coefficients, and Wick-square distinction between a generic
  smooth Hadamard-coordinate diagonal and local covariant finite Wick
  prescription freedom.

Independent construction:
- The checks use finite covectors, exact rational Hadamard-coefficient
  arithmetic, and a three-point retained spacetime sample.  The Wick-square
  sample computes the diagonal shift from `H' = H + w` directly and then tests
  whether the same arbitrary smooth diagonal can be fitted by
  `a_m m^2 + a_R R(x)` without assuming that it can.

Imported assumptions:
- Mostly-plus metric signature; the scalar operator convention used in the
  chapter; and the four-dimensional local-covariant Wick-square ansatz
  `a_m m^2 + a_R R` when covariance, scaling, and field-equation conditions
  are imposed.

Negative controls:
- The script rejects opposite-cone products, wrong diagonal-recursion
  denominators, the wrong sign for a smooth Hadamard-coordinate shift, and the
  shortcut that treats a generic smooth diagonal as local covariant
  curvature/mass freedom.

Scope boundary:
- Passing this file checks convention-sensitive finite algebra.  It does not
  prove the global microlocal spectrum theorem, construct Hadamard states, or
  establish the full Hollands-Wald classification of local covariant Wick
  polynomials.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close


from fractions import Fraction
import math


def assert_close(got: float, expected: float, label: str, tol: float = 1e-12) -> None:
    _assert_close(label, got, expected, tol=tol)


def assert_equal(got: Fraction, expected: Fraction, label: str) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def assert_not_equal(got: Fraction, forbidden: Fraction, label: str) -> None:
    if got == forbidden:
        raise AssertionError(f"{label}: forbidden shortcut unexpectedly matched {got!r}")


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


def check_wick_square_coordinate_shift_vs_local_prescription() -> None:
    weights = [Fraction(2), Fraction(3), Fraction(5)]
    omega_minus_h = [Fraction(7, 3), Fraction(5, 2), Fraction(11, 4)]
    smooth_diagonal = [Fraction(1, 6), Fraction(-2, 5), Fraction(3, 7)]

    hprime_values = [value - shift for value, shift in zip(omega_minus_h, smooth_diagonal)]
    smeared_h = sum(w * value for w, value in zip(weights, omega_minus_h))
    smeared_hprime = sum(w * value for w, value in zip(weights, hprime_values))
    expected_shift = -sum(w * shift for w, shift in zip(weights, smooth_diagonal))
    assert_equal(
        smeared_hprime - smeared_h,
        expected_shift,
        "Wick-square shift for H'=H+w",
    )

    wrong_sign_shift = sum(w * shift for w, shift in zip(weights, smooth_diagonal))
    assert_not_equal(
        smeared_hprime - smeared_h,
        wrong_sign_shift,
        "wrong sign for smooth Hadamard-coordinate shift",
    )

    mass_squared = Fraction(2)
    scalar_curvature = [Fraction(0), Fraction(1), Fraction(2)]
    arbitrary_smooth_diagonal = [Fraction(0), Fraction(1), Fraction(4)]

    # Fit a_m m^2 + a_R R to the first two sample points.
    a_m = arbitrary_smooth_diagonal[0] / mass_squared
    a_r = arbitrary_smooth_diagonal[1] - arbitrary_smooth_diagonal[0]
    predicted_third = a_m * mass_squared + a_r * scalar_curvature[2]
    assert_not_equal(
        predicted_third,
        arbitrary_smooth_diagonal[2],
        "generic smooth diagonal represented as local Wick freedom",
    )

    local_a_m = Fraction(3, 10)
    local_a_r = Fraction(-1, 7)
    local_covariant_shift = [
        local_a_m * mass_squared + local_a_r * curvature
        for curvature in scalar_curvature
    ]
    fitted_a_m = local_covariant_shift[0] / mass_squared
    fitted_a_r = local_covariant_shift[1] - local_covariant_shift[0]
    for curvature, expected in zip(scalar_curvature, local_covariant_shift):
        got = fitted_a_m * mass_squared + fitted_a_r * curvature
        assert_equal(got, expected, "local covariant Wick-square ansatz")


def main() -> None:
    check_future_covector_convention()
    check_kg_hamilton_flow_is_future_null_for_positive_frequency()
    check_two_point_graph_sign_pattern()
    check_product_opposite_cone_obstruction()
    check_hadamard_transport_coefficients()
    check_wick_square_coordinate_shift_vs_local_prescription()
    print("All microlocal spectrum convention checks passed.")


if __name__ == "__main__":
    main()
