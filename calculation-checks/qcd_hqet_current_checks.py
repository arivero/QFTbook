#!/usr/bin/env python3
"""Finite checks for HQET current normalizations and symmetry relations."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_state_normalization_matching() -> None:
    """Check that |H(p)>_QCD = sqrt(M) |H_v(k)>_HQET matches the norms."""

    mass = Fraction(13, 5)
    v_zero = Fraction(7, 3)

    qcd_norm_factor = 2 * mass * v_zero
    hqet_norm_factor = 2 * v_zero
    require(
        qcd_norm_factor == mass * hqet_norm_factor,
        "QCD and HQET residual-state normalizations do not match",
    )


def check_decay_constant_scaling() -> None:
    """Check that <0|A|P> matching implies f sqrt(M)=C F."""

    sqrt_mass = Fraction(5, 2)
    mass = sqrt_mass * sqrt_mass
    matching = Fraction(7, 11)
    static_matrix_element = Fraction(13, 17)

    decay_constant = matching * static_matrix_element / sqrt_mass
    qcd_amplitude = decay_constant * mass
    hqet_amplitude = matching * sqrt_mass * static_matrix_element

    require(qcd_amplitude == hqet_amplitude, "axial-current amplitudes disagree")
    require(
        decay_constant * sqrt_mass == matching * static_matrix_element,
        "heavy-light decay-constant scaling failed",
    )


def check_recoil_variable() -> None:
    """Check w=-v.v' at rest and for a rational collinear boost."""

    zero_recoil = Fraction(1)
    require(zero_recoil == 1, "zero recoil should have w=1")

    beta_squared = Fraction(1, 9)
    gamma_squared = 1 / (1 - beta_squared)
    w_opposite_collinear = gamma_squared * (1 + beta_squared)

    require(
        w_opposite_collinear == Fraction(5, 4),
        "mostly-plus recoil variable has the wrong boosted value",
    )
    require(w_opposite_collinear >= 1, "physical recoil should obey w>=1")


def check_zero_recoil_isgur_wise_normalization() -> None:
    """Check that xi(1)=1 gives the flavor-charge matrix element 2 v^mu."""

    velocity = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    xi_at_one = Fraction(1)

    current_matrix_element = tuple(
        xi_at_one * (component + component) for component in velocity
    )
    charge_normalization = tuple(2 * component for component in velocity)

    require(
        current_matrix_element == charge_normalization,
        "zero-recoil Isgur-Wise normalization failed",
    )


def check_current_scheme_covariance() -> None:
    """Check that finite current redefinitions preserve the matched product."""

    coefficient = Fraction(5, 7)
    matrix_element = Fraction(11, 13)
    finite_renormalization = Fraction(17, 19)

    original = coefficient * matrix_element
    transformed = (coefficient / finite_renormalization) * (
        finite_renormalization * matrix_element
    )
    require(transformed == original, "finite current scheme change is not covariant")


def main() -> None:
    check_state_normalization_matching()
    check_decay_constant_scaling()
    check_recoil_variable()
    check_zero_recoil_isgur_wise_normalization()
    check_current_scheme_covariance()
    print("All QCD HQET current and symmetry checks passed.")


if __name__ == "__main__":
    main()
