#!/usr/bin/env python3
"""Finite checks for Chern-Simons normalizations and SU(2)_k modular data."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math
from fractions import Fraction


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def su2_s_matrix(k: int) -> list[list[float]]:
    K = k + 2
    scale = math.sqrt(2.0 / K)
    return [
        [scale * math.sin((a + 1) * (b + 1) * math.pi / K) for b in range(k + 1)]
        for a in range(k + 1)
    ]


def quantum_dimension(k: int, a: int) -> float:
    K = k + 2
    return math.sin((a + 1) * math.pi / K) / math.sin(math.pi / K)


def verlinde_coeff(k: int, a: int, b: int, c: int) -> int:
    s = su2_s_matrix(k)
    raw = sum(s[a][x] * s[b][x] * s[c][x] / s[0][x] for x in range(k + 1))
    rounded = round(raw)
    assert_close(f"Verlinde integrality k={k} {a}{b}{c}", raw, rounded, tol=1.0e-9)
    return int(rounded)


def su2_truncated_rule(k: int, a: int, b: int, c: int) -> int:
    if (a + b + c) % 2 != 0:
        return 0
    if abs(a - b) <= c <= min(a + b, 2 * k - a - b):
        return 1
    return 0


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


CENTRAL_MODE = (-1, 0)


def add_fraction(
    terms: dict[tuple[int, int], Fraction],
    key: tuple[int, int],
    value: Fraction,
) -> None:
    if value == 0:
        return
    terms[key] = terms.get(key, Fraction(0)) + value
    if terms[key] == 0:
        del terms[key]


def add_terms(
    *pieces: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for piece in pieces:
        for key, value in piece.items():
            add_fraction(out, key, value)
    return out


def su2_epsilon(a: int, b: int, c: int) -> int:
    if len({a, b, c}) < 3:
        return 0
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    return -1


def affine_su2_bracket_basis(
    left: tuple[int, int],
    right: tuple[int, int],
    level: Fraction,
) -> dict[tuple[int, int], Fraction]:
    a, m = left
    b, n = right
    if a == CENTRAL_MODE[0] or b == CENTRAL_MODE[0]:
        return {}

    out: dict[tuple[int, int], Fraction] = {}
    for c in range(3):
        eps = su2_epsilon(a, b, c)
        if eps:
            add_fraction(out, (c, m + n), Fraction(eps))
    if a == b and m + n == 0:
        add_fraction(out, CENTRAL_MODE, level * m)
    return out


def affine_su2_bracket_linear(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
    level: Fraction,
) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for left_key, left_coeff in left.items():
        for right_key, right_coeff in right.items():
            bracket = affine_su2_bracket_basis(left_key, right_key, level)
            for key, value in bracket.items():
                add_fraction(out, key, left_coeff * right_coeff * value)
    return out


def check_finite_gauge_transgression_coefficient() -> None:
    # With A^g=gAg^{-1}-dg g^{-1}, the pure Maurer-Cartan term in
    # cs(A^g)-cs(A) is (1/3) tr(theta^3).  The action prefactor k/(4*pi)
    # and the winding normalization (24*pi^2) give 2*pi*k*n.
    coefficient_in_units_of_pi_k = Fraction(1, 4) * Fraction(1, 3) * 24
    assert_equal("Chern-Simons winding coefficient", coefficient_in_units_of_pi_k, Fraction(2))


def check_wess_zumino_extension_ambiguity() -> None:
    # Two WZ extensions differ by the closed three-manifold integral
    # (k/(12*pi)) int tr(g^{-1}dg)^3.  The same winding normalization
    # (24*pi^2) gives a 2*pi*k*n phase ambiguity, so the boundary WZ
    # extension condition is the bulk integral-level condition.
    coefficient_in_units_of_pi_k = Fraction(1, 12) * 24
    assert_equal("Wess-Zumino extension ambiguity", coefficient_in_units_of_pi_k, Fraction(2))


def check_abelian_transgression_derivative_sign() -> None:
    # In the Abelian limit theta^2=dtheta=0 and A^g=A-theta.  Directly
    # expanding (A-theta) d(A-theta)-A dA gives -theta dA.  Since
    # d(theta A)=dtheta A-theta dA, the local transgression must contain
    # +d(theta A), not -d(theta A).
    direct_theta_d_a = Fraction(-1)
    plus_d_theta_a_theta_d_a = Fraction(-1)
    minus_d_theta_a_theta_d_a = Fraction(1)
    assert_equal("Abelian transgression derivative sign", direct_theta_d_a, plus_d_theta_a_theta_d_a)
    if direct_theta_d_a == minus_d_theta_a_theta_d_a:
        raise AssertionError("wrong-sign Chern-Simons derivative term was not detected")


def check_holomorphic_polarization_variation() -> None:
    # Boundary variation coefficients in units of k/(pi) for the independent
    # monomials A_z delta A_bar and A_bar delta A_z.
    bulk_z_dbar = Fraction(1, 4)
    bulk_bar_dz = Fraction(-1, 4)
    pol_z_dbar = Fraction(1, 4)
    pol_bar_dz = Fraction(1, 4)
    assert_equal("polarized variation A_z delta Abar", bulk_z_dbar + pol_z_dbar, Fraction(1, 2))
    assert_equal("polarized variation Abar delta Az", bulk_bar_dz + pol_bar_dz, Fraction(0))


def check_polyakov_wiegmann_cross_coefficients() -> None:
    # Cross terms in units of k/pi.  The kinetic part contributes
    # (X_z Y_bar + X_bar Y_z)/4.  The WZ boundary term contributes
    # (-X_z Y_bar + X_bar Y_z)/4.
    kinetic_xz_ybar = Fraction(1, 4)
    kinetic_xbar_yz = Fraction(1, 4)
    wz_xz_ybar = Fraction(-1, 4)
    wz_xbar_yz = Fraction(1, 4)
    assert_equal("PW canceled cross term", kinetic_xz_ybar + wz_xz_ybar, Fraction(0))
    assert_equal("PW surviving cross coefficient", kinetic_xbar_yz + wz_xbar_yz, Fraction(1, 2))


def check_affine_current_mode_residue_extraction() -> None:
    # From J(z)J(w) ~ k/(z-w)^2 + ... and J_m = Res z^m J(z),
    # Res_{z=w} z^m/(z-w)^2 = m w^{m-1}.  The outer residue against w^n
    # is nonzero exactly when m+n=0, giving k*m, not k*n or k*(m+n).
    level = Fraction(5)
    for m in range(-4, 5):
        for n in range(-4, 5):
            inner_double_coefficient = Fraction(m)
            outer_double_power = m - 1 + n
            residue = level * inner_double_coefficient if outer_double_power == -1 else Fraction(0)
            expected = level * m if m + n == 0 else Fraction(0)
            assert_equal(f"affine central residue m={m} n={n}", residue, expected)
            if m + n == 0 and m != 0:
                wrong_symmetric_coefficient = level * (m + n)
                if residue == wrong_symmetric_coefficient:
                    raise AssertionError("symmetric affine central coefficient was not detected")

            inner_simple_power = m
            simple_pole_mode = inner_simple_power + n
            assert_equal(f"affine simple-pole mode m={m} n={n}", simple_pole_mode, m + n)


def check_affine_su2_central_extension_jacobi() -> None:
    # Work in a real su(2) basis [T_a,T_b]=epsilon_ab^c T_c, suppressing the
    # common factor of i used in the chapter.  The exact finite check verifies
    # the loop-algebra central cocycle k*m*delta_{ab}*delta_{m+n,0}.
    level = Fraction(3)
    basis = [(a, m) for a in range(3) for m in range(-2, 3)]

    assert_equal(
        "affine central coefficient +m",
        affine_su2_bracket_basis((0, 2), (0, -2), level),
        {CENTRAL_MODE: Fraction(6)},
    )
    assert_equal(
        "affine central coefficient antisymmetry",
        affine_su2_bracket_basis((0, -2), (0, 2), level),
        {CENTRAL_MODE: Fraction(-6)},
    )

    for x in basis:
        for y in basis:
            xy = affine_su2_bracket_basis(x, y, level)
            yx = affine_su2_bracket_basis(y, x, level)
            assert_equal(f"affine antisymmetry x={x} y={y}", add_terms(xy, yx), {})

    for x in basis:
        x_vec = {x: Fraction(1)}
        for y in basis:
            y_vec = {y: Fraction(1)}
            for z in basis:
                z_vec = {z: Fraction(1)}
                yz = affine_su2_bracket_linear(y_vec, z_vec, level)
                zx = affine_su2_bracket_linear(z_vec, x_vec, level)
                xy = affine_su2_bracket_linear(x_vec, y_vec, level)
                jacobi = add_terms(
                    affine_su2_bracket_linear(x_vec, yz, level),
                    affine_su2_bracket_linear(y_vec, zx, level),
                    affine_su2_bracket_linear(z_vec, xy, level),
                )
                assert_equal(f"affine Jacobi x={x} y={y} z={z}", jacobi, {})


def check_s_orthogonality() -> None:
    for k in range(1, 11):
        s = su2_s_matrix(k)
        for a in range(k + 1):
            for c in range(k + 1):
                got = sum(s[a][b] * s[c][b] for b in range(k + 1))
                expected = 1.0 if a == c else 0.0
                assert_close(f"S orthogonality k={k} a={a} c={c}", got, expected)


def check_quantum_dimensions_and_hopf_links() -> None:
    for k in range(1, 11):
        s = su2_s_matrix(k)
        s00 = s[0][0]
        total_dimension_squared = sum(quantum_dimension(k, a) ** 2 for a in range(k + 1))
        assert_close(f"total dimension k={k}", total_dimension_squared, 1.0 / (s00 * s00))
        for a in range(k + 1):
            assert_close(f"unknot dimension k={k} a={a}", s[0][a] / s00, quantum_dimension(k, a))

        if k == 1:
            assert_close("SU(2)_1 nontrivial Hopf", s[1][1] / s00, -1.0)
        if k == 2:
            assert_close("SU(2)_2 spin-half dimension", quantum_dimension(k, 1), math.sqrt(2.0))


def check_verlinde_rule() -> None:
    for k in range(1, 9):
        for a in range(k + 1):
            for b in range(k + 1):
                for c in range(k + 1):
                    assert_close(
                        f"Verlinde rule k={k} {a}{b}{c}",
                        verlinde_coeff(k, a, b, c),
                        su2_truncated_rule(k, a, b, c),
                    )


def check_verlinde_dimensions() -> None:
    for k in range(1, 12):
        s = su2_s_matrix(k)
        sphere_dim = sum(s[0][x] ** 2 for x in range(k + 1))
        torus_dim = sum(1.0 for _ in range(k + 1))
        assert_close(f"sphere dimension k={k}", sphere_dim, 1.0)
        assert_close(f"torus dimension k={k}", torus_dim, k + 1)


def main() -> None:
    check_finite_gauge_transgression_coefficient()
    check_wess_zumino_extension_ambiguity()
    check_abelian_transgression_derivative_sign()
    check_holomorphic_polarization_variation()
    check_polyakov_wiegmann_cross_coefficients()
    check_affine_current_mode_residue_extraction()
    check_affine_su2_central_extension_jacobi()
    check_s_orthogonality()
    check_quantum_dimensions_and_hopf_links()
    check_verlinde_rule()
    check_verlinde_dimensions()
    print("All Chern-Simons normalization, affine-current, and SU(2)_k modular-data checks passed.")


if __name__ == "__main__":
    main()
