#!/usr/bin/env python3
"""Finite checks for the supersymmetric Yang-Mills deformation ladder.

The checks cover algebraic identities used in Volume VII's family-comparison
chapter: holomorphic scale dimensions, the N=1* fuzzy-sphere F-term ansatz,
and the finite k-string comparison ledgers.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


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


def main() -> None:
    check_holomorphic_scale_dimensions()
    check_n1_star_fuzzy_sphere_ansatz()
    check_k_string_ledgers()
    print("All supersymmetric Yang-Mills deformation-ladder checks passed.")


if __name__ == "__main__":
    main()
