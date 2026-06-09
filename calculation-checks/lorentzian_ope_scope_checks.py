#!/usr/bin/env python3
"""Finite scope checks for Lorentzian OPE continuation claims.

Evidence contract.

Target claims:
* the two radial variables rho and rhobar are the scalar four-point channel
  variables, not a complete coordinate system for general n-point Wightman
  functions;
* spinning or tensor-valued correlators require additional tensor-structure
  and polarization majorants after complex continuation.

Independent construction:
* the script recomputes the four- and five-point conformal-invariant counts in
  four dimensions and builds finite tensor/coefficient counterexamples rather
  than reading the surrounding prose.

Imported assumptions:
* the conformal group in four dimensions has dimension 15; four generic
  Euclidean points have a one-dimensional residual transverse rotation
  stabilizer, while five generic points have no continuous stabilizer.

Negative controls:
* a scalar five-point configuration is rejected by any two-cross-ratio
  criterion;
* a toy spinning/tensor coefficient vector is rejected by scalar rho data
  alone;
* a finite complex-rotation norm factor shows why q^Delta without a compact
  angular/tensor majorant can fail.

Scope boundary:
* these checks do not prove the scalar four-point forward-tube theorem or
  Wightman distributional convergence; they guard the finite kinematic scope of
  the theorem statement.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name} failed")


def conformal_group_dimension(spacetime_dimension: int) -> int:
    return (spacetime_dimension + 1) * (spacetime_dimension + 2) // 2


def scalar_four_point_invariants_4d() -> int:
    point_coordinates = 4 * 4
    conformal_group = conformal_group_dimension(4)
    residual_transverse_rotation = 1
    return point_coordinates - conformal_group + residual_transverse_rotation


def scalar_n_point_invariants_4d(point_count: int) -> int:
    if point_count < 5:
        raise ValueError("use scalar_four_point_invariants_4d for the four-point case")
    return 4 * point_count - conformal_group_dimension(4)


def check_two_rho_variables_are_four_point_scope() -> None:
    assert_equal("four-dimensional conformal group dimension", conformal_group_dimension(4), 15)
    assert_equal("scalar four-point conformal invariants", scalar_four_point_invariants_4d(), 2)
    assert_equal("scalar five-point conformal invariants", scalar_n_point_invariants_4d(5), 5)
    assert_equal("scalar six-point conformal invariants", scalar_n_point_invariants_4d(6), 9)
    assert_true(
        "two rho variables do not parametrize scalar five-point geometry",
        scalar_n_point_invariants_4d(5) > scalar_four_point_invariants_4d(),
    )


def check_tensor_structure_data_are_extra_coordinates() -> None:
    scalar_radial_data = (Fraction(1, 3), Fraction(1, 4))
    first_tensor_structure = (Fraction(1), Fraction(0))
    second_tensor_structure = (Fraction(0), Fraction(1))

    correlator_a = (scalar_radial_data, first_tensor_structure)
    correlator_b = (scalar_radial_data, second_tensor_structure)

    assert_equal("same scalar rho data", correlator_a[0], correlator_b[0])
    assert_true("different tensor structures at fixed rho data", correlator_a[1] != correlator_b[1])


def check_complex_angular_majorant_is_separate_from_q_delta() -> None:
    q = Fraction(3, 5)
    complex_rotation_norm = Fraction(2)
    level = 8

    scalar_tail = q**level
    continued_tensor_tail = (q * complex_rotation_norm) ** level

    assert_true("scalar radial tail decays", scalar_tail < Fraction(1, 10))
    assert_true(
        "complex angular factor can overwhelm q^Delta",
        continued_tensor_tail > 1,
    )


def main() -> None:
    check_two_rho_variables_are_four_point_scope()
    check_tensor_structure_data_are_extra_coordinates()
    check_complex_angular_majorant_is_separate_from_q_delta()
    print("All Lorentzian OPE scope checks passed.")


if __name__ == "__main__":
    main()
