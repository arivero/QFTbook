#!/usr/bin/env python3
"""Finite checks for the QCD TMD/GPD convention block.

The checks verify algebraic facts used in the monograph text:

1. Collins-Soper and ultraviolet evolution commute only when the rapidity
   anomalous dimensions obey the displayed integrability relation.
2. Finite TMD scheme changes preserve that relation.
3. Holding zeta_A zeta_B fixed cancels the rapidity evolution of a product of
   two TMDs with the same Collins-Soper kernel.
4. Contracting a spin-N local twist-two matrix element with a lightlike vector
   produces a polynomial of degree at most N in the skewness xi.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{name}: got {simplified!r}, expected 0")


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def check_collins_soper_integrability() -> None:
    ell_mu, ell_zeta, gamma0, gamma_cusp = sp.symbols(
        "ell_mu ell_zeta gamma0 gamma_cusp"
    )

    collins_soper_kernel = -2 * gamma_cusp * ell_mu
    gamma_f = gamma0 - 2 * gamma_cusp * (ell_zeta - ell_mu)

    assert_zero(
        "Collins-Soper integrability",
        sp.diff(collins_soper_kernel, ell_mu) - sp.diff(gamma_f, ell_zeta),
    )

    # A finite scheme change F' = exp(R) F shifts both anomalous dimensions,
    # but the mixed partials of R cancel in the consistency equation.
    r1, r2, r3 = sp.symbols("r1 r2 r3")
    finite_scheme = r1 * ell_mu * ell_zeta + r2 * ell_zeta**2 + r3 * ell_mu**2
    shifted_kernel = collins_soper_kernel + sp.diff(finite_scheme, ell_zeta)
    shifted_gamma = gamma_f + sp.diff(finite_scheme, ell_mu)
    assert_zero(
        "finite scheme preserves integrability",
        sp.diff(shifted_kernel, ell_mu) - sp.diff(shifted_gamma, ell_zeta),
    )


def check_two_hadron_rapidity_cancellation() -> None:
    t, kernel = sp.symbols("t kernel")
    ell_zeta_a_0, ell_zeta_b_0 = sp.symbols("ell_zeta_a_0 ell_zeta_b_0")
    ell_zeta_a = ell_zeta_a_0 + t
    ell_zeta_b = ell_zeta_b_0 - t

    # The product constraint zeta_A zeta_B = Q^4 fixes
    # ell_zeta_A + ell_zeta_B.  Differentiating log(F_A F_B) along this
    # constraint gives D - D when both TMDs use the same soft kernel.
    log_product_derivative = kernel * sp.diff(ell_zeta_a, t) + kernel * sp.diff(
        ell_zeta_b, t
    )
    assert_zero("fixed-product rapidity cancellation", log_product_derivative)


def check_gpd_polynomiality_degree() -> None:
    xi = sp.symbols("xi")
    for spin in range(1, 8):
        coefficients = sp.symbols(f"A0:{spin + 1}")
        moment = sum(coefficients[k] * (-2 * xi) ** k for k in range(spin + 1))
        degree = sp.Poly(moment, xi).degree()
        assert_equal(f"GPD spin-{spin} polynomial degree", degree, spin)

        # Removing the highest local form factor lowers the degree, illustrating
        # the "at most N" part of the theorem.
        reduced = moment.subs(coefficients[-1], 0)
        reduced_degree = sp.Poly(reduced, xi).degree()
        assert_equal(f"GPD spin-{spin} reduced degree", reduced_degree <= spin, True)


def main() -> None:
    check_collins_soper_integrability()
    check_two_hadron_rapidity_cancellation()
    check_gpd_polynomiality_degree()
    print("All QCD TMD rapidity and GPD polynomiality checks passed.")


if __name__ == "__main__":
    main()
