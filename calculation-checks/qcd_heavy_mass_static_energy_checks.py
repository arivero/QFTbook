#!/usr/bin/env python3
"""Checks for heavy-quark mass schemes and static-energy conventions."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_static_energy_scheme_shift() -> None:
    """Check 2(m+dm)+(V-2dm)+U = 2m+V+U."""

    mass = Fraction(17, 5)
    potential = Fraction(-11, 7)
    ultrasoft = Fraction(3, 13)
    delta_mass = Fraction(19, 23)

    original = 2 * mass + potential + ultrasoft
    shifted = 2 * (mass + delta_mass) + (potential - 2 * delta_mass) + ultrasoft
    require(shifted == original, "static-energy mass/potential shift is not invariant")


def check_hamiltonian_eigenvalue_shift() -> None:
    """Check H' = H - 2 dm implies 2m'+E' = 2m+E."""

    mass = Fraction(29, 11)
    eigenvalue = Fraction(-5, 3)
    delta_mass = Fraction(7, 17)

    shifted_mass = mass + delta_mass
    shifted_eigenvalue = eigenvalue - 2 * delta_mass
    require(
        2 * shifted_mass + shifted_eigenvalue == 2 * mass + eigenvalue,
        "quarkonium mass combination is not scheme invariant",
    )


def check_potential_subtracted_mass_coefficient() -> None:
    """Check the leading PS subtraction coefficient.

    The radial integral gives
        int_{|q|<mu} d^3q/(2 pi)^3 1/q^2 = mu/(2 pi^2).
    The PS definition multiplies this by g^2 C_F/2, hence
        delta m_PS = g^2 C_F mu/(4 pi^2).
    We check the rational coefficient multiplying g^2 C_F mu / pi^2.
    """

    radial_integral_coefficient = Fraction(1, 2)
    ps_prefactor = Fraction(1, 2)
    ps_coefficient = ps_prefactor * radial_integral_coefficient
    require(ps_coefficient == Fraction(1, 4), "wrong leading PS subtraction coefficient")


def check_trace_convention_invariant_product() -> None:
    """Check g^2 C_F = g_ht^2 C_F_ht for the monograph convention."""

    for n_colors in range(2, 15):
        c_f = Fraction(n_colors * n_colors - 1, n_colors)
        c_f_ht = c_f / 2
        g_sq = Fraction(31, 37)
        g_ht_sq = 2 * g_sq
        require(
            g_sq * c_f == g_ht_sq * c_f_ht,
            f"trace convention product failed for N={n_colors}",
        )


def check_static_potential_fourier_sign() -> None:
    """Check that a negative singlet color factor gives an attractive potential."""

    color_factor = Fraction(-8, 3)
    coupling = Fraction(5, 1)
    fourier_kernel = Fraction(1, 4)  # coefficient of 1/(pi r), pi suppressed.
    potential_coefficient = coupling * color_factor * fourier_kernel
    require(potential_coefficient < 0, "singlet Coulomb coefficient should be attractive")


def main() -> None:
    check_static_energy_scheme_shift()
    check_hamiltonian_eigenvalue_shift()
    check_potential_subtracted_mass_coefficient()
    check_trace_convention_invariant_product()
    check_static_potential_fourier_sign()
    print("All QCD heavy-mass and static-energy checks passed.")


if __name__ == "__main__":
    main()
