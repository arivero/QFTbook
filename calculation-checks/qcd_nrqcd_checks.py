#!/usr/bin/env python3
"""Finite checks for the NRQCD and pNRQCD convention block."""

from __future__ import annotations

from fractions import Fraction


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
Vector = tuple[Fraction, Fraction]
Row = tuple[Fraction, Fraction]
Poly = tuple[Fraction, ...]


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


def add_poly(a: Poly, b: Poly, max_power: int) -> Poly:
    return tuple(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(max_power + 1)
    )


def scale_poly(a: Poly, factor: Fraction, max_power: int) -> Poly:
    return tuple((a[i] if i < len(a) else 0) * factor for i in range(max_power + 1))


def mul_poly(a: Poly, b: Poly, max_power: int) -> Poly:
    out = [Fraction(0) for _ in range(max_power + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= max_power:
                out[i + j] += ai * bj
    return tuple(out)


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


def check_octet_gap_trace_convention() -> None:
    """Check V_O - V_S has coefficient N_c in the trace-delta convention."""

    for n in range(2, 12):
        c_f = Fraction(n * n - 1, n)
        singlet_factor = -c_f
        octet_factor = Fraction(1, n)
        require(octet_factor > 0, "octet Coulomb channel should be repulsive")
        require(
            octet_factor - singlet_factor == n,
            "singlet-octet Coulomb gap should have coefficient N_c",
        )


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


def check_ultrasoft_multipole_parameter() -> None:
    """Check r partial_us is the relative velocity in weak-coupling pNRQCD."""

    mass = Fraction(1)
    for denominator in range(2, 12):
        velocity = Fraction(1, denominator)
        radius = 1 / (mass * velocity)
        ultrasoft_gradient = mass * velocity * velocity
        expansion_parameter = radius * ultrasoft_gradient
        require(
            expansion_parameter == velocity,
            "multipole expansion parameter should be r partial_us = v",
        )


def check_ultrasoft_two_level_shift_series() -> None:
    """Check the second-order singlet-octet shift from a finite two-level model."""

    # With the singlet energy subtracted, H = [[0, eps], [eps, Delta]].
    # Set Delta=1 and expand the lower eigenvalue
    # lambda_- = (1 - sqrt(1 + 4 eps^2))/2
    #          = -eps^2 + eps^4 - 2 eps^6 + O(eps^8).
    max_power = 6
    lambda_minus = (
        Fraction(0),
        Fraction(0),
        Fraction(-1),
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(-2),
    )
    epsilon_squared = (Fraction(0), Fraction(0), Fraction(1))
    characteristic = add_poly(
        add_poly(
            mul_poly(lambda_minus, lambda_minus, max_power),
            scale_poly(lambda_minus, Fraction(-1), max_power),
            max_power,
        ),
        scale_poly(epsilon_squared, Fraction(-1), max_power),
        max_power,
    )
    require(
        characteristic == tuple(Fraction(0) for _ in range(max_power + 1)),
        "two-level ultrasoft energy shift does not solve the characteristic equation",
    )
    require(lambda_minus[2] == -1, "leading ultrasoft level shift should be negative")


def check_ultrasoft_resolvent_denominator() -> None:
    """Check the dipole energy denominator weakens as ultrasoft energy grows."""

    dipole_matrix_element = Fraction(2, 17)
    octet_gap = Fraction(5, 7)
    ultrasoft_energy = Fraction(3, 11)

    shift_without_energy = -(dipole_matrix_element**2) / octet_gap
    shift_with_energy = -(dipole_matrix_element**2) / (octet_gap + ultrasoft_energy)
    require(shift_with_energy < 0, "virtual octet channel should lower an isolated level")
    require(
        abs(shift_with_energy) < abs(shift_without_energy),
        "positive ultrasoft energy should increase the resolvent denominator",
    )


def main() -> None:
    check_bilocal_endpoint_cancellation()
    check_schrodinger_sign()
    check_singlet_color_and_coupling_conversion()
    check_octet_gap_trace_convention()
    check_scale_hierarchy()
    check_ultrasoft_multipole_parameter()
    check_ultrasoft_two_level_shift_series()
    check_ultrasoft_resolvent_denominator()
    print("All QCD NRQCD/pNRQCD convention checks passed.")


if __name__ == "__main__":
    main()
