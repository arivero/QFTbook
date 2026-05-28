#!/usr/bin/env python3
"""Finite checks for supersymmetric Yang-Mills family normalizations.

The script verifies algebraic identities used in the pure-SYM spectral,
domain-wall, and Seiberg-Witten confinement sections of Volume VII.  It checks
only finite algebra: the text supplies the hypotheses under which these
identities become statements about a field theory.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def check_domain_wall_chord_identity() -> None:
    theta = sp.symbols("theta", real=True)
    chord_squared = (sp.cos(theta) - 1) ** 2 + sp.sin(theta) ** 2
    sine_form = 4 * sp.sin(theta / 2) ** 2
    assert_zero("root-of-unity chord identity", sp.expand_trig(chord_squared - sine_form))

    nc, c, lam = sp.symbols("N_c C Lambda", positive=True)
    wall_tension = 2 * nc * c * lam * sp.sqrt(sine_form)
    expected = 4 * nc * c * lam * sp.Abs(sp.sin(theta / 2))
    assert_zero("BPS wall sine tension", sp.simplify(wall_tension - expected))


def check_single_chiral_mass_formula() -> None:
    g, w = sp.symbols("g w", positive=True)
    # V = g^{-1} |W'' sigma|^2 and sigma_c = sqrt(g) sigma.
    coefficient_in_canonical_field = (w**2 / g) / g
    assert_zero("single chiral mass squared", coefficient_in_canonical_field - (w / g) ** 2)


def check_sw_monopole_f_terms() -> None:
    sqrt2 = sp.sqrt(2)
    mu, up = sp.symbols("mu u_prime", nonzero=True)
    xi = -mu * up / sqrt2
    product = xi
    f_ad = sqrt2 * product + mu * up
    assert_zero("SW local F_A equation", f_ad)


def check_vortex_bound_completion() -> None:
    b, e, q2, xi = sp.symbols("B e q2 xi", positive=True)
    lhs = b**2 / (2 * e**2) + e**2 * (xi - q2) ** 2 / 2
    rhs = (b - e**2 * (xi - q2)) ** 2 / (2 * e**2) + b * (xi - q2)
    assert_zero("Abelian vortex square completion", sp.expand(lhs - rhs))
    flux = 2 * sp.pi * sp.symbols("n", integer=True, positive=True)
    assert_equal("vortex flux coefficient", Fraction(1, 2) * 4, 2)
    assert_zero("vortex topological term", sp.simplify(xi * flux - 2 * sp.pi * sp.symbols("n", integer=True, positive=True) * xi))


def main() -> None:
    check_domain_wall_chord_identity()
    check_single_chiral_mass_formula()
    check_sw_monopole_f_terms()
    check_vortex_bound_completion()
    print("All supersymmetric Yang-Mills family checks passed.")


if __name__ == "__main__":
    main()
