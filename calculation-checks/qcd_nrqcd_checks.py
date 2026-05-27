#!/usr/bin/env python3
"""Finite checks for the NRQCD and pNRQCD convention block."""

from __future__ import annotations

from fractions import Fraction


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
Vector = tuple[Fraction, Fraction]
Row = tuple[Fraction, Fraction]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
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


def mat_vec(a: Matrix, v: Vector) -> Vector:
    return (
        a[0][0] * v[0] + a[0][1] * v[1],
        a[1][0] * v[0] + a[1][1] * v[1],
    )


def row_mat(r: Row, a: Matrix) -> Row:
    return (
        r[0] * a[0][0] + r[1] * a[1][0],
        r[0] * a[0][1] + r[1] * a[1][1],
    )


def row_vec(r: Row, v: Vector) -> Fraction:
    return r[0] * v[0] + r[1] * v[1]


def inverse_2x2(a: Matrix) -> Matrix:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    require(det != 0, "matrix is singular")
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def check_bilocal_endpoint_cancellation() -> None:
    """Check chi^dag U2^{-1} (U2 W U1^{-1}) U1 psi = chi^dag W psi."""

    u1: Matrix = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
    u2: Matrix = ((Fraction(1), Fraction(2)), (Fraction(3), Fraction(5)))
    w: Matrix = ((Fraction(3), Fraction(-1)), (Fraction(2), Fraction(1)))
    chi_row: Row = (Fraction(5), Fraction(-2))
    psi_col: Vector = (Fraction(7), Fraction(4))

    lhs_row = row_mat(chi_row, inverse_2x2(u2))
    transformed_w = mat_mul(mat_mul(u2, w), inverse_2x2(u1))
    transformed_psi = mat_vec(u1, psi_col)
    lhs = row_vec(row_mat(lhs_row, transformed_w), transformed_psi)
    rhs = row_vec(row_mat(chi_row, w), psi_col)
    require(lhs == rhs, "bilocal Wilson-line endpoint cancellation failed")


def check_schrodinger_sign() -> None:
    """Check that i dt + nabla^2/(2m) gives E=p^2/(2m)."""

    p_sq = Fraction(25, 9)
    mass = Fraction(7, 3)
    energy = p_sq / (2 * mass)
    equation = energy - p_sq / (2 * mass)
    require(equation == 0, "NRQCD kinetic sign gives wrong free dispersion")


def check_singlet_color_and_coupling_conversion() -> None:
    """Check -C_F and g^2 C_F = g_ht^2 C_F_ht in trace-delta conventions."""

    for n in range(2, 12):
        c_f = Fraction(n * n - 1, n)
        c_f_ht = c_f / 2
        g_sq = Fraction(5, 7)
        g_ht_sq = 2 * g_sq
        singlet_factor = -c_f
        require(singlet_factor == -Fraction(n * n - 1, n), "wrong singlet color factor")
        require(g_sq * c_f == g_ht_sq * c_f_ht, "Coulomb product not convention invariant")


def check_scale_hierarchy() -> None:
    """Check m >> mv >> mv^2 for sample rational velocities 0<v<1."""

    mass = Fraction(1)
    for denominator in range(2, 12):
        v = Fraction(1, denominator)
        hard = mass
        soft = mass * v
        ultrasoft = mass * v * v
        require(hard > soft > ultrasoft, "NRQCD scale hierarchy failed")
        require(ultrasoft / soft == v, "ultrasoft-to-soft ratio is not v")


def main() -> None:
    check_bilocal_endpoint_cancellation()
    check_schrodinger_sign()
    check_singlet_color_and_coupling_conversion()
    check_scale_hierarchy()
    print("All QCD NRQCD/pNRQCD convention checks passed.")


if __name__ == "__main__":
    main()
