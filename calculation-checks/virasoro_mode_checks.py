#!/usr/bin/env python3
"""Finite algebra checks for the two-dimensional Virasoro-mode derivation."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def central_residue_coefficient(n):
    """Coefficient multiplying c before the final w-contour integral."""
    return Fraction((n + 1) * n * (n - 1), 12)


def virasoro_central_coefficient(n, m):
    """Coefficient of c in [L_n,L_m] from the TT OPE."""
    if n + m == 0:
        return central_residue_coefficient(n)
    return Fraction(0)


def virasoro_mode_coefficient(n, m):
    """Coefficient of L_{n+m} from the two noncentral TT OPE terms."""
    double_pole = 2 * (n + 1)
    derivative_term_after_parts = -(n + m + 2)
    return double_pole + derivative_term_after_parts


for n in range(-12, 13):
    for m in range(-12, 13):
        require(
            virasoro_mode_coefficient(n, m) == n - m,
            f"noncentral coefficient failed for n={n}, m={m}",
        )
        expected = Fraction(n**3 - n, 12) if n + m == 0 else Fraction(0)
        require(
            virasoro_central_coefficient(n, m) == expected,
            f"central coefficient failed for n={n}, m={m}",
        )


# For the cylinder map z = exp(-i w), equivalently w = i log z,
# w'/w'', w''' give {w,z}=1/(2 z^2).  The finite transformation
# T_w=(dw/dz)^(-2)(T_z-c {w,z}/12) therefore contributes +c/24.
schwarzian_w_z_times_z_squared = Fraction(1, 2)
inverse_square_factor_times_z_squared = Fraction(-1)
cylinder_shift = (
    -inverse_square_factor_times_z_squared
    * Fraction(1, 12)
    * schwarzian_w_z_times_z_squared
)
require(cylinder_shift == Fraction(1, 24), "plane-cylinder shift is not +c/24")

print("All Virasoro-mode residue and cylinder-shift checks passed.")
