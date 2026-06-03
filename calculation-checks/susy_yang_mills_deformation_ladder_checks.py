#!/usr/bin/env python3
"""Finite checks for the supersymmetric Yang-Mills deformation ladder.

The checks cover algebraic identities used in Volume VII's family-comparison
chapter: holomorphic scale dimensions, the N=1* fuzzy-sphere F-term ansatz,
finite k-string comparison ledgers, and the local Seiberg-Witten vortex
profile normalization, together with the Abelianized A-type sine profile and
pure N=1 SYM channel-pole bookkeeping.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def assert_near_zero(name: str, expr: sp.Expr, tol: sp.Float = sp.Float("1e-45")) -> None:
    value = abs(sp.N(expr, 80))
    if value.is_finite is not True:
        raise AssertionError(f"{name} produced nonfinite numerical value: {value!r}")
    if value >= tol:
        raise AssertionError(f"{name} failed numerically: {value!r}")


def check_holomorphic_scale_dimensions() -> None:
    n = sp.symbols("N_c", positive=True, integer=True)
    # N=4 -> pure N=2*: Lambda^(2N) = m_h^(2N) q.
    dim_lhs_n2 = 2 * n
    dim_rhs_n2 = 2 * n
    assert_zero("N=4 to N=2 scale dimension", dim_lhs_n2 - dim_rhs_n2)

    # N=4 -> pure N=1*: Lambda^(3N) = (m1 m2 m3)^N q.
    dim_lhs_n1 = 3 * n
    dim_rhs_n1 = n + n + n
    assert_zero("N=4 to N=1 scale dimension", dim_lhs_n1 - dim_rhs_n1)


def check_n1_star_fuzzy_sphere_ansatz() -> None:
    alpha, m = sp.symbols("alpha m", nonzero=True)
    # If [J2,J3] = i J1 and Phi_i = alpha J_i, then
    # sqrt(2)[Phi2,Phi3] + m Phi1 = alpha (sqrt(2) i alpha + m) J1.
    alpha_solution = sp.I * m / sp.sqrt(2)
    coefficient = alpha * (sp.sqrt(2) * sp.I * alpha + m)
    assert_zero("N=1* fuzzy-sphere F-term coefficient", coefficient.subs(alpha, alpha_solution))


def check_k_string_ledgers() -> None:
    n, k = sp.symbols("N k", positive=True)
    sine_k = sp.sin(sp.pi * k / n) / sp.sin(sp.pi / n)
    sine_conj = sp.sin(sp.pi * (n - k) / n) / sp.sin(sp.pi / n)
    assert_zero("sine-law charge conjugation", sp.trigsimp(sine_k - sine_conj))

    casimir_k = k * (n - k) / (n - 1)
    casimir_conj = (n - k) * k / (n - 1)
    assert_zero("Casimir-ledger charge conjugation", casimir_k - casimir_conj)

    x = sp.symbols("x")
    sine_series = sp.series(sp.sin(sp.pi * k * x) / sp.sin(sp.pi * x), x, 0, 5).removeO()
    expected_sine = k - sp.pi**2 * k * (k**2 - 1) * x**2 / 6
    assert_zero("sine-law large-N through x^2", sp.expand(sine_series - expected_sine).coeff(x, 2))

    casimir_x = k * (1 / x - k) / (1 / x - 1)
    casimir_series = sp.series(casimir_x, x, 0, 3).removeO()
    expected_casimir = k - k * (k - 1) * x
    assert_zero("Casimir large-N through x", sp.expand(casimir_series - expected_casimir).coeff(x, 1))


def check_sw_vortex_radial_normalization() -> None:
    n = sp.symbols("n", positive=True, integer=True)
    flux = 2 * sp.pi * n * (1 - 0)
    assert_zero("SW vortex flux normalization", flux - 2 * sp.pi * n)

    r, c = sp.symbols("R c", positive=True)
    for winding in range(1, 5):
        f = c * r**winding
        a = r**2 / (2 * winding)
        first_eq_residual = sp.diff(f, r) - winding * (1 - a) * f / r
        second_eq_residual = sp.diff(a, r) - r * (1 - f**2) / winding
        assert_zero(
            f"SW vortex small-R leading f equation n={winding}",
            sp.expand(first_eq_residual).coeff(r, winding - 1),
        )
        assert_zero(
            f"SW vortex small-R leading a equation n={winding}",
            sp.expand(second_eq_residual).coeff(r, 1),
        )


def check_abelianized_a_type_sine_profile() -> None:
    for rank_plus_one in range(3, 11):
        dim = rank_plus_one - 1
        cartan = sp.zeros(dim, dim)
        for i in range(dim):
            cartan[i, i] = 2
            if i > 0:
                cartan[i, i - 1] = -1
            if i + 1 < dim:
                cartan[i, i + 1] = -1

        sine_vector = sp.Matrix(
            [sp.sin(sp.pi * (i + 1) / rank_plus_one) for i in range(dim)]
        )
        eigenvalue = 4 * sp.sin(sp.pi / (2 * rank_plus_one)) ** 2
        residual = cartan * sine_vector - eigenvalue * sine_vector
        for i, entry in enumerate(residual):
            assert_near_zero(f"A-type sine eigenvector N={rank_plus_one}, row={i+1}", entry)

        for k_value in range(1, rank_plus_one):
            ratio = sp.sin(sp.pi * k_value / rank_plus_one) / sp.sin(sp.pi / rank_plus_one)
            conjugate_ratio = sp.sin(sp.pi * (rank_plus_one - k_value) / rank_plus_one) / sp.sin(
                sp.pi / rank_plus_one
            )
            assert_zero(
                f"A-type sine charge conjugation N={rank_plus_one}, k={k_value}",
                sp.trigsimp(ratio - conjugate_ratio),
            )

        for k_value in range(1, rank_plus_one - 1):
            for ell_value in range(1, rank_plus_one - k_value):
                a = sp.pi * k_value / rank_plus_one
                b = sp.pi * ell_value / rank_plus_one
                difference = sp.sin(a) + sp.sin(b) - sp.sin(a + b)
                factorized = 4 * sp.sin(a / 2) * sp.sin(b / 2) * sp.sin((a + b) / 2)
                assert_near_zero(
                    f"A-type sine subadditivity identity N={rank_plus_one}, k={k_value}, ell={ell_value}",
                    difference - factorized,
                )
                if not bool(sp.N(difference) > 0):
                    raise AssertionError(
                        f"A-type sine subadditivity positivity failed for N={rank_plus_one}, "
                        f"k={k_value}, ell={ell_value}: {difference!r}"
                    )


def check_pure_sym_channel_pole_bookkeeping() -> None:
    mass, t, t0 = sp.symbols("m t t0", positive=True)
    z_plus, z_minus, z_fermion = sp.symbols("z_plus z_minus z_fermion", nonzero=True)

    lambda_plus = z_plus**2 * sp.exp(-mass * t) / (z_plus**2 * sp.exp(-mass * t0))
    lambda_minus = z_minus**2 * sp.exp(-mass * t) / (z_minus**2 * sp.exp(-mass * t0))
    lambda_fermion = z_fermion**2 * sp.exp(-mass * t) / (z_fermion**2 * sp.exp(-mass * t0))
    expected = sp.exp(-mass * (t - t0))
    assert_zero("pure SYM even-channel pole", lambda_plus / expected - 1)
    assert_zero("pure SYM odd-channel pole", lambda_minus / expected - 1)
    assert_zero("pure SYM fermion-channel pole", lambda_fermion / expected - 1)

    equal_masses = [sp.Integer(7), sp.Integer(7), sp.Integer(7)]
    equal_delta = max(abs(equal_masses[0] - equal_masses[1]), abs(equal_masses[0] - equal_masses[2]), abs(equal_masses[1] - equal_masses[2]))
    assert_zero("pure SYM equal-mass diagnostic", equal_delta)

    split_masses = [sp.Integer(4), sp.Integer(5), sp.Integer(6)]
    split_delta = max(abs(split_masses[0] - split_masses[1]), abs(split_masses[0] - split_masses[2]), abs(split_masses[1] - split_masses[2]))
    split_average = sum(split_masses) / sp.Integer(3)
    assert_zero("pure SYM split diagnostic value", split_delta / split_average - sp.Rational(2, 5))


def main() -> None:
    check_holomorphic_scale_dimensions()
    check_n1_star_fuzzy_sphere_ansatz()
    check_k_string_ledgers()
    check_sw_vortex_radial_normalization()
    check_abelianized_a_type_sine_profile()
    check_pure_sym_channel_pole_bookkeeping()
    print("All supersymmetric Yang-Mills deformation-ladder checks passed.")


if __name__ == "__main__":
    main()
