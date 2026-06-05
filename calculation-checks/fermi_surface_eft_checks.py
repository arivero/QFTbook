#!/usr/bin/env python3
"""Finite checks for the general Fermi-surface EFT section.

These checks are deliberately modest.  They verify the algebraic and
finite-shell normalizations used in the monograph: density-of-states matching,
the Cooper logarithm and its shell remainder scale, BCS eigenvalue flow, Landau
response normalization, and the finite-volume flux-insertion momentum shift.
They are not a proof of Fermi-liquid theory or of any non-Fermi-liquid fixed
point.
"""

from __future__ import annotations

from fractions import Fraction
import math

Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def assert_close(actual: float, expected: float, *, tol: float = 1e-12) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"{actual!r} != {expected!r}")


def sphere_area(d: int) -> float:
    """Area of the unit (d-1)-sphere in R^d."""

    return 2.0 * math.pi ** (d / 2.0) / math.gamma(d / 2.0)


def parabolic_density(d: int, *, k_f: float, mass: float, degeneracy: int) -> float:
    return degeneracy * sphere_area(d) * k_f**d / (d * (2.0 * math.pi) ** d)


def parabolic_density_of_states(
    d: int, *, k_f: float, mass: float, degeneracy: int
) -> float:
    v_f = k_f / mass
    return degeneracy * sphere_area(d) * k_f ** (d - 1) / (
        (2.0 * math.pi) ** d * v_f
    )


def check_parabolic_density_of_states_match() -> None:
    """dn/dmu from the microscopic Fermi ball equals the patch surface measure."""

    for d in (2, 3):
        k_f = 1.7
        mass = 2.3
        degeneracy = 2
        dn_dk = (
            degeneracy
            * sphere_area(d)
            * k_f ** (d - 1)
            / (2.0 * math.pi) ** d
        )
        dmu_dk = k_f / mass
        microscopic = dn_dk / dmu_dk
        patch = parabolic_density_of_states(
            d, k_f=k_f, mass=mass, degeneracy=degeneracy
        )
        assert_close(microscopic, patch)

        # A finite small-shift check of the declared asymptotic relation.
        delta_mu = 1.0e-5
        mu = k_f * k_f / (2.0 * mass)
        shifted_k = math.sqrt(2.0 * mass * (mu + delta_mu))
        finite_delta = parabolic_density(
            d, k_f=shifted_k, mass=mass, degeneracy=degeneracy
        ) - parabolic_density(d, k_f=k_f, mass=mass, degeneracy=degeneracy)
        leading_patch_delta = patch * delta_mu
        relative_error = abs(finite_delta - leading_patch_delta) / abs(
            leading_patch_delta
        )
        if relative_error >= 1.0e-4:
            raise AssertionError(relative_error)


def check_cooper_shell_log_and_remainder_scale() -> None:
    """The symmetric T=0 Cooper shell gives d ell plus O(Lambda/E_F)."""

    ell = 0.031
    lam = 0.2
    e_f = 10.0
    jacobian_slope_bound = 1.7

    exact_log = math.log(lam / (lam * math.exp(-ell)))
    assert_close(exact_log, ell)

    # If J(xi)=J0 + O(|xi|/E_F), the correction is bounded by
    # C/E_F * int_shell dxi = C Lambda(1-exp(-ell))/E_F on the two-sided shell.
    correction_bound = (
        jacobian_slope_bound * lam * (1.0 - math.exp(-ell)) / e_f
    )
    declared_scale = jacobian_slope_bound * (lam / e_f) * ell
    if correction_bound > declared_scale * (1.0 + ell):
        raise AssertionError((correction_bound, declared_scale))


def matmul2(a: Matrix2, b: Matrix2) -> Matrix2:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def inv2(a: Matrix2) -> Matrix2:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if det == 0:
        raise AssertionError("singular 2x2 matrix")
    return ((a[1][1] / det, -a[0][1] / det), (-a[1][0] / det, a[0][0] / det))


def check_bcs_matrix_flow_and_attractive_instability() -> None:
    """For dU/dell=-U^2, eigenvalues obey lambda/(1+lambda ell)."""

    u0 = ((Fraction(-1, 6), Fraction(-1, 3)), (Fraction(-1, 3), Fraction(-1, 6)))
    ell = Fraction(1, 1)
    identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    denominator = (
        (identity[0][0] + ell * u0[0][0], identity[0][1] + ell * u0[0][1]),
        (identity[1][0] + ell * u0[1][0], identity[1][1] + ell * u0[1][1]),
    )
    flowed = matmul2(u0, inv2(denominator))

    # The even and odd eigenvalues of [[a,b],[b,a]] are a+b=-1/2 and a-b=1/6.
    expected_even = Fraction(-1, 2) / (1 + Fraction(-1, 2) * ell)
    expected_odd = Fraction(1, 6) / (1 + Fraction(1, 6) * ell)
    actual_even = flowed[0][0] + flowed[0][1]
    actual_odd = flowed[0][0] - flowed[0][1]
    if actual_even != expected_even or actual_odd != expected_odd:
        raise AssertionError((flowed, expected_even, expected_odd))

    attractive_lambda = Fraction(-1, 2)
    instability_ell = -1 / attractive_lambda
    if instability_ell != 2:
        raise AssertionError(instability_ell)

    repulsive_lambda = Fraction(1, 6)
    repulsive_later = repulsive_lambda / (1 + repulsive_lambda * 10)
    if not (0 < repulsive_later < repulsive_lambda):
        raise AssertionError(repulsive_later)


def check_landau_response_and_pomeranchuk_threshold() -> None:
    """The response formula diverges exactly at the l=0 stability boundary."""

    nu_star = Fraction(7, 3)
    f0s = Fraction(2, 5)
    compressibility_factor = nu_star / (1 + f0s)
    if compressibility_factor != Fraction(5, 3):
        raise AssertionError(compressibility_factor)

    stable = [Fraction(-9, 10), Fraction(0), Fraction(3, 1)]
    unstable = [Fraction(-1, 1), Fraction(-6, 5)]
    for f0 in stable:
        if not (1 + f0 > 0):
            raise AssertionError(f0)
    for f0 in unstable:
        if not (1 + f0 <= 0):
            raise AssertionError(f0)


def check_flux_insertion_momentum_arithmetic() -> None:
    """Large-gauge transformation shifts crystal momentum by 2*pi*N/Lx."""

    lx = 8
    particle_number = 19
    shift_units = particle_number % lx  # units of 2*pi/Lx
    if shift_units != 3:
        raise AssertionError(shift_units)

    # A topological sector can absorb part of the exact shift.  The finite
    # identity is unchanged, but the visible Fermi-volume interpretation changes.
    topological_absorbed_units = 1
    visible_units = (shift_units - topological_absorbed_units) % lx
    if visible_units != 2:
        raise AssertionError(visible_units)

    # Broken translations enlarge the unit cell: momentum is interpreted modulo
    # the reduced Brillouin zone rather than as the original one-cell count.
    broken_unit_cell = 2
    reduced_zone_period_units = lx // broken_unit_cell
    folded_visible_units = visible_units % reduced_zone_period_units
    if folded_visible_units != 2:
        raise AssertionError(folded_visible_units)
    if (visible_units + topological_absorbed_units) % lx != shift_units:
        raise AssertionError("momentum balance was not conserved")


def main() -> None:
    check_parabolic_density_of_states_match()
    check_cooper_shell_log_and_remainder_scale()
    check_bcs_matrix_flow_and_attractive_instability()
    check_landau_response_and_pomeranchuk_threshold()
    check_flux_insertion_momentum_arithmetic()
    print("All finite Fermi-surface EFT checks passed.")


if __name__ == "__main__":
    main()
