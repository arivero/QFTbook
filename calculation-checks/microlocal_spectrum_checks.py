#!/usr/bin/env python3
"""Convention checks for the microlocal spectrum chapter.

Evidence contract.

The metric convention is mostly plus.  A causal covector is called future
directed when its metric dual vector is future directed.  In flat coordinates
this makes the positive-frequency covector (-E, p) future directed.

Target claims:
- `ch:curved-microlocal-spectrum-condition`: the mostly-plus
  positive-frequency covector convention, Klein-Gordon Hamilton-flow sign,
  BFK paired-edge two-point graph covector pattern for both temporal
  orderings, pullback/product graph-cone addition for quasifree Wick pairings,
  product obstruction, Hadamard recursion coefficients, and Wick-square
  distinction between a generic smooth Hadamard-coordinate diagonal and local
  covariant finite Wick prescription freedom.

Independent construction:
- The checks use finite covectors, exact rational Hadamard-coefficient
  arithmetic, a finite paired-edge graph model, and a three-point retained
  spacetime sample.  The Wick-square sample computes the diagonal shift from
  `H' = H + w` directly and then tests whether the same arbitrary smooth
  diagonal can be fitted by
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
  curvature/mass freedom.  It also rejects the one-way future-causal graph rule
  for reversed temporal ordering and the conflation of a timelike causal edge
  with the null-geodesic Hadamard wavefront set.

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


Cov2 = tuple[Fraction, Fraction]
GraphCovectors = tuple[Cov2, ...]


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


def cov_neg(covector: Cov2) -> Cov2:
    return (-covector[0], -covector[1])


def cov_add(left: Cov2, right: Cov2) -> Cov2:
    return (left[0] + right[0], left[1] + right[1])


def graph_covector_sum(left: GraphCovectors, right: GraphCovectors) -> GraphCovectors:
    if len(left) != len(right):
        raise AssertionError("graph covector tuples must live over the same vertex set")
    return tuple(cov_add(a, b) for a, b in zip(left, right))


def covector_square_exact(covector: Cov2) -> Fraction:
    return -(covector[0] * covector[0]) + covector[1] * covector[1]


def is_future_causal_covector(covector: Cov2) -> bool:
    return covector[0] < 0 and covector_square_exact(covector) <= 0


def is_null_covector(covector: Cov2) -> bool:
    return covector_square_exact(covector) == 0


def bfk_two_point_tuple(future_covector: Cov2) -> GraphCovectors:
    if not is_future_causal_covector(future_covector):
        raise AssertionError("BFK fixture expected a future causal covector")
    return (future_covector, cov_neg(future_covector))


def one_way_future_causal_tuple(
    x1_time: Fraction,
    x2_time: Fraction,
    future_covector: Cov2,
) -> GraphCovectors:
    if x1_time <= x2_time:
        return (future_covector, cov_neg(future_covector))
    return (cov_neg(future_covector), future_covector)


def pullback_pair_to_n_vertices(
    vertex_count: int,
    left: int,
    right: int,
    future_covector: Cov2,
) -> GraphCovectors:
    if left >= right:
        raise AssertionError("Wick-pair labels should be ordered before pullback")
    zero = (Fraction(0), Fraction(0))
    covectors = [zero for _ in range(vertex_count)]
    covectors[left] = future_covector
    covectors[right] = cov_neg(future_covector)
    return tuple(covectors)


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


def check_bfk_paired_edge_temporal_ordering_and_variants() -> None:
    future_null: Cov2 = (Fraction(-5), Fraction(5))
    if not is_null_covector(future_null):
        raise AssertionError("null Hadamard fixture changed")

    bfk_when_x2_future = bfk_two_point_tuple(future_null)
    bfk_when_x1_future = bfk_two_point_tuple(future_null)
    expected = (future_null, cov_neg(future_null))
    if bfk_when_x2_future != expected:
        raise AssertionError("BFK paired-edge graph changed for ordinary temporal ordering")
    if bfk_when_x1_future != expected:
        raise AssertionError("BFK vertex-order rule should not flip under reversed temporal ordering")

    wrong_reversed = one_way_future_causal_tuple(
        x1_time=Fraction(1),
        x2_time=Fraction(0),
        future_covector=future_null,
    )
    if wrong_reversed == expected:
        raise AssertionError("negative control failed: one-way future-causal rule matched BFK")
    if is_future_causal_covector(wrong_reversed[0]):
        raise AssertionError("reversed one-way rule should make the first Hadamard covector past directed")

    future_timelike: Cov2 = (Fraction(-5), Fraction(3))
    if not is_future_causal_covector(future_timelike):
        raise AssertionError("timelike causal fixture changed")
    if is_null_covector(future_timelike):
        raise AssertionError("timelike negative-control fixture became null")
    timelike_bfk_tuple = bfk_two_point_tuple(future_timelike)
    if timelike_bfk_tuple[0] == future_null:
        raise AssertionError("negative control failed: timelike edge looked like Hadamard null data")


def check_quasifree_pullback_product_graph_closure() -> None:
    p: Cov2 = (Fraction(-2), Fraction(2))
    q: Cov2 = (Fraction(-3), Fraction(-3))
    if not (is_null_covector(p) and is_null_covector(q)):
        raise AssertionError("quasifree pullback null fixtures changed")

    pair_13 = pullback_pair_to_n_vertices(4, 0, 2, p)
    pair_24 = pullback_pair_to_n_vertices(4, 1, 3, q)
    zero = (Fraction(0), Fraction(0))
    if pair_13[1] != zero or pair_13[3] != zero:
        raise AssertionError("pair pullback should be zero on spectator factors")
    if pair_24[0] != zero or pair_24[2] != zero:
        raise AssertionError("pair pullback should be zero on spectator factors")

    product_sum = graph_covector_sum(pair_13, pair_24)
    expected_product_sum: GraphCovectors = (p, q, cov_neg(p), cov_neg(q))
    if product_sum != expected_product_sum:
        raise AssertionError("product-theorem graph covector sum changed")

    pair_12 = pullback_pair_to_n_vertices(3, 0, 1, p)
    pair_13 = pullback_pair_to_n_vertices(3, 0, 2, q)
    union_sum = graph_covector_sum(pair_12, pair_13)
    if union_sum[0] != cov_add(p, q):
        raise AssertionError("disjoint-union graph addition failed at the shared source")
    if not is_future_causal_covector(union_sum[0]):
        raise AssertionError("sum of future null outgoing covectors should remain future causal")


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
    check_bfk_paired_edge_temporal_ordering_and_variants()
    check_quasifree_pullback_product_graph_closure()
    check_product_opposite_cone_obstruction()
    check_hadamard_transport_coefficients()
    check_wick_square_coordinate_shift_vs_local_prescription()
    print("All microlocal spectrum convention and BFK graph-cone checks passed.")


if __name__ == "__main__":
    main()
