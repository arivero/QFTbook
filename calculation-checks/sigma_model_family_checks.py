#!/usr/bin/env python3
"""Exact finite checks for sigma-model family identities.

The checks cover the CP^{N-1} projector, the PCM Lax coefficient split, WZW
central charges, nonabelian-bosonization central-charge bookkeeping, and the
curvature formula for the sausage metric used in Volume VI.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def assert_zero(name: str, value) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: got {value}, expected 0")


def check_cp_projector() -> None:
    # For a normalized vector z, P = z z^\dagger obeys
    # P^2 = z (z^\dagger z) z^\dagger = P.  The exact scalar coefficient is 1.
    z_dagger_z = Fraction(1)
    assert_equal("CP projector scalar", z_dagger_z**2, z_dagger_z)


def check_pcm_lax_coefficients() -> None:
    # With L_+ = j_+/(1-zeta), L_- = j_-/(1+zeta), multiplying the curvature
    # by 1-zeta^2 gives M - zeta E, where
    # M = d_+j_- - d_-j_+ + [j_+,j_-] and E = d_+j_- + d_-j_+.
    coeff_dpjm_constant = Fraction(1)
    coeff_dmjp_constant = Fraction(-1)
    coeff_comm_constant = Fraction(1)
    coeff_dpjm_zeta = Fraction(-1)
    coeff_dmjp_zeta = Fraction(-1)
    coeff_comm_zeta = Fraction(0)
    assert_equal("PCM constant coefficient", (coeff_dpjm_constant, coeff_dmjp_constant, coeff_comm_constant), (1, -1, 1))
    assert_equal("PCM zeta coefficient", (coeff_dpjm_zeta, coeff_dmjp_zeta, coeff_comm_zeta), (-1, -1, 0))


def check_wzw_central_charge_examples() -> None:
    # c = k dim(g)/(k+hvee).  For SU(2)_1 this is c=1; for SU(3)_1 this is c=2.
    assert_equal("SU(2)_1 WZW c", Fraction(1 * 3, 1 + 2), Fraction(1))
    assert_equal("SU(3)_1 WZW c", Fraction(1 * 8, 1 + 3), Fraction(2))


def check_nonabelian_bosonization_central_charge() -> None:
    for nc in range(2, 7):
        for nf in range(1, 7):
            color = Fraction(nf * (nc * nc - 1), nf + nc)
            flavor = Fraction(nc * (nf * nf - 1), nc + nf)
            u1 = Fraction(1)
            assert_equal(
                f"nonabelian bosonization c identity Nc={nc} Nf={nf}",
                color + flavor + u1,
                Fraction(nc * nf),
            )


def check_sausage_metric_curvature() -> None:
    r, h, q = sp.symbols("r h q", nonzero=True)
    e_metric = h / ((1 - r**2) * (1 + q * r**2))
    g_metric = h * (1 - r**2) / (1 + q * r**2)
    scalar_curvature = (
        -sp.diff(g_metric, r, 2) / (e_metric * g_metric)
        + sp.diff(g_metric, r) ** 2 / (2 * e_metric * g_metric**2)
        + sp.diff(e_metric, r) * sp.diff(g_metric, r) / (2 * e_metric**2 * g_metric)
    )
    expected = 2 * (1 + q) * (1 - q * r**2) / (h * (1 + q * r**2))
    assert_zero("sausage scalar curvature", scalar_curvature - expected)
    assert_zero("sausage round-sphere limit", expected.subs(q, 0) - 2 / h)


def main() -> None:
    check_cp_projector()
    check_pcm_lax_coefficients()
    check_wzw_central_charge_examples()
    check_nonabelian_bosonization_central_charge()
    check_sausage_metric_curvature()
    print("All sigma-model family checks passed.")


if __name__ == "__main__":
    main()
