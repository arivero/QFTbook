#!/usr/bin/env python3
"""Finite checks for the 't Hooft-line local model and line arithmetic.

The script checks the algebraic identities used in Volume IX, Chapter 3.  It
does not attempt to construct a continuum gauge measure.  The verified objects
are the Dirac-monopole patching identities, the finite linking pairing, the
theta-angle Witten-effect automorphism, and the gauge-equivalence arithmetic
for Cartan surface singularities.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Charge = tuple[int, int]


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def monopole_patch_difference(magnetic_charge: int) -> int:
    """Coefficient of dphi in A_N - A_S for the embedded Dirac monopole."""

    north = Fraction(magnetic_charge, 2)
    south = Fraction(-magnetic_charge, 2)
    return int(north - south)


def monopole_flux(magnetic_charge: int) -> Fraction:
    """Integral of F/(2*pi) for F = (m/2) sin(theta) dtheta wedge dphi."""

    sphere_area_factor = 4
    return Fraction(magnetic_charge, 2) * Fraction(sphere_area_factor, 2)


def check_dirac_monopole_patching() -> None:
    for magnetic_charge in range(-12, 13):
        assert_equal(
            f"patch difference m={magnetic_charge}",
            monopole_patch_difference(magnetic_charge),
            magnetic_charge,
        )
        assert_equal(
            f"flux m={magnetic_charge}",
            monopole_flux(magnetic_charge),
            Fraction(magnetic_charge, 1),
        )
        for electric_charge in range(-12, 13):
            phase_winding = electric_charge * magnetic_charge
            assert_true(
                f"Dirac phase integral e={electric_charge} m={magnetic_charge}",
                isinstance(phase_winding, int),
            )


def dirac_pairing_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    e, m = lhs
    ep, mp = rhs
    return (e * mp - ep * m) % n


def witten_t(n: int, charge: Charge, theta_periods: int = 1) -> Charge:
    e, m = charge
    return ((e + theta_periods * m) % n, m)


def check_witten_effect_preserves_pairing() -> None:
    for n in range(2, 20):
        charges = [(e, m) for e in range(n) for m in range(n)]
        for periods in range(-3, 4):
            for lhs, rhs in product(charges, repeat=2):
                before = dirac_pairing_numerator(n, lhs, rhs)
                after = dirac_pairing_numerator(
                    n,
                    witten_t(n, lhs, periods),
                    witten_t(n, rhs, periods),
                )
                assert_equal(
                    f"T preserves pairing N={n} p={periods} lhs={lhs} rhs={rhs}",
                    after,
                    before,
                )


def surface_alpha_equivalent(n: int, alpha_num: int, alpha_prime_num: int) -> bool:
    """Equivalence on a rank-one torus with alpha measured in units of 1/n."""

    return (alpha_prime_num - alpha_num) % n == 0


def check_surface_alpha_shifts() -> None:
    for n in range(2, 20):
        for alpha, shift in product(range(n), range(-2 * n, 2 * n + 1)):
            shifted = (alpha + shift * n) % n
            assert_true(
                f"surface alpha cocharacter shift n={n} alpha={alpha} shift={shift}",
                surface_alpha_equivalent(n, alpha, shifted),
            )
        for alpha, beta in product(range(n), repeat=2):
            expected = alpha == beta
            assert_equal(
                f"surface alpha inequivalent classes n={n} alpha={alpha} beta={beta}",
                surface_alpha_equivalent(n, alpha, beta),
                expected,
            )


def check_linking_phase_bilinearity() -> None:
    for n in range(2, 10):
        charges = [(e, m) for e in range(n) for m in range(n)]
        for lhs, rhs, third in product(charges, repeat=3):
            summed = ((lhs[0] + rhs[0]) % n, (lhs[1] + rhs[1]) % n)
            left = dirac_pairing_numerator(n, summed, third)
            right = (
                dirac_pairing_numerator(n, lhs, third)
                + dirac_pairing_numerator(n, rhs, third)
            ) % n
            assert_equal(
                f"linking phase bilinear n={n} lhs={lhs} rhs={rhs} third={third}",
                left,
                right,
            )


def main() -> None:
    check_dirac_monopole_patching()
    check_linking_phase_bilinearity()
    check_witten_effect_preserves_pairing()
    check_surface_alpha_shifts()
    print("All 't Hooft-line local-model checks passed.")


if __name__ == "__main__":
    main()
