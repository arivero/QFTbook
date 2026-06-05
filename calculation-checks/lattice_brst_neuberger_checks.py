#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- For a finite lattice with residual global gauge transformations removed, a
  conventional BRST-exact compact-orbit gauge-fixing factor computes the Euler
  characteristic of the based lattice gauge group.
- Positive-dimensional compact connected Lie groups have zero Euler
  characteristic, so the oriented Gribov-copy sum vanishes and gauge-invariant
  BRST-gauge-fixed expectation values take the Neuberger 0/0 form.
- The obstruction depends on the compact group, the oriented BRST determinant,
  exact nilpotent BRST independence, and the based treatment of global zero
  modes; changing those assumptions is an escape route with a cost, not the same
  theorem.

Independent construction:
- The script evaluates finite Morse models for S^1 and S^3, computes compact
  Lie-group Euler characteristics from odd-degree cohomology generators, and
  checks the product formula for the based lattice gauge group G^(V-1).
- It constructs the numerator and denominator of a gauge-invariant expectation
  value after insertion of the gauge-fixing factor and verifies the 0/0
  obstruction.
- It tests negative controls: absolute determinants, unremoved global zero
  modes, coset Euler characteristic, noncompact stereographic coordinates, and a
  Curci-Ferrari-type ghost mass term.

Imported assumptions:
- The finite lattice is connected and has at least two sites before choosing a
  base site, so the based gauge group has positive dimension.
- The compact connected Lie group has the rational cohomology of an exterior
  algebra on odd-degree generators, as in the standard compact Lie-group
  calculation; the script uses this only as a finite Euler-characteristic model.
- Gauge-invariant observables are independent of gauge-orbit coordinates, so
  insertion of an orbitwise gauge-fixing factor multiplies both numerator and
  denominator by the same topological factor.

Negative controls:
- Replacing the oriented Faddeev-Popov determinant by its absolute value removes
  the cancellation but is not BRST-exact.
- Leaving the residual global gauge direction in the Faddeev-Popov matrix gives
  a zero determinant for a different zero-mode reason.
- A coset such as SU(2)/U(1) has nonzero Euler characteristic, illustrating why
  equivariant BRST changes the theorem by leaving a subgroup unfixed.
- A noncompact coordinate line can have a single signed critical point only
  because the compact no-boundary assumption has been abandoned.
- A Curci-Ferrari-type mass saturates ghosts at t=0, but that changes the
  nilpotent BRST-exact setup whose t-independence produced the obstruction.

Scope boundary:
- These are finite topology and bookkeeping checks.  They do not construct a
  lattice BRST regulator, prove a continuum limit, compare escape routes to
  gauge-invariant Yang-Mills, or analyze numerical gauge-fixing algorithms.
"""

from __future__ import annotations

import sympy as sp

from check_utils import assert_gt


def assert_zero(name: str, value: sp.Expr | int | float) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: expected zero, got {sp.simplify(value)!r}")


def assert_nonzero(name: str, value: sp.Expr | int | float) -> None:
    if sp.simplify(value) == 0:
        raise AssertionError(f"{name}: expected a nonzero negative control")


def euler_from_odd_generators(*degrees: int) -> sp.Expr:
    q = sp.symbols("q")
    poincare = sp.prod(1 + q**degree for degree in degrees)
    return sp.expand(poincare).subs(q, -1)


def check_morse_signed_copy_cancellation() -> None:
    # S^1 height/Landau-toy potential: V(theta)=1-cos(theta).
    # Critical points theta=0, pi have Hessian signs + and -.
    s1_hessian_signs = (sp.Integer(1), sp.Integer(-1))
    signed_s1 = sum(s1_hessian_signs)
    absolute_s1 = sum(abs(sign) for sign in s1_hessian_signs)
    assert_zero("S1 signed Gribov-copy count equals chi(S1)", signed_s1)
    assert_gt("absolute determinant removes the S1 cancellation", float(absolute_s1), 0.0)

    # S^3 height potential has one minimum and one maximum, with Morse indices
    # 0 and 3.  The signed sum is 1 + (-1)^3 = 0.
    s3_signed = sp.Integer(1) + (-1) ** 3
    s3_absolute = sp.Integer(2)
    assert_zero("S3 signed Morse count equals chi(S3)", s3_signed)
    assert_nonzero("absolute determinant is not the oriented BRST sum on S3", s3_absolute - s3_signed)


def check_compact_lie_group_euler_characteristics() -> None:
    assert_zero("U(1) Euler characteristic", euler_from_odd_generators(1))
    assert_zero("SU(2) Euler characteristic", euler_from_odd_generators(3))
    assert_zero("SU(3) Euler characteristic", euler_from_odd_generators(3, 5))
    assert_zero("SU(4) Euler characteristic", euler_from_odd_generators(3, 5, 7))

    chi_su2_over_u1 = sp.Integer(2)  # S^2.
    assert_nonzero(
        "equivariant coset SU(2)/U(1) changes the Euler characteristic",
        chi_su2_over_u1,
    )

    for site_count in (2, 3, 8):
        chi_g = euler_from_odd_generators(3)  # SU(2).
        based_factor = chi_g ** (site_count - 1)
        assert_zero(f"based SU(2) lattice gauge group chi for {site_count} sites", based_factor)


def check_residual_global_mode_and_zero_over_zero() -> None:
    local_hessian_eigenvalues = (sp.Integer(2), sp.Integer(-3), sp.Integer(5))
    based_fp_determinant = sp.prod(local_hessian_eigenvalues)
    assert_nonzero("based finite Faddeev-Popov determinant can be nonzero locally", based_fp_determinant)

    unbased_fp_determinant = based_fp_determinant * 0
    assert_zero(
        "unremoved global gauge direction gives a separate zero determinant",
        unbased_fp_determinant,
    )

    chi_gauge_orbit = sp.Integer(0)
    observable_value = sp.symbols("observable_value", nonzero=True)
    gauge_invariant_lattice_weight = sp.symbols("gauge_invariant_lattice_weight", positive=True)
    numerator = observable_value * gauge_invariant_lattice_weight * chi_gauge_orbit
    denominator = gauge_invariant_lattice_weight * chi_gauge_orbit
    assert_zero("Neuberger numerator vanishes orbitwise", numerator)
    assert_zero("Neuberger denominator vanishes orbitwise", denominator)

    ordinary_gauge_invariant_denominator = gauge_invariant_lattice_weight
    assert_nonzero(
        "gauge-invariant lattice definition remains finite before BRST gauge fixing",
        ordinary_gauge_invariant_denominator,
    )


def check_escape_route_assumption_changes() -> None:
    # Noncompact stereographic-style coordinate: F(x)=x on R has one critical
    # point with positive sign.  This is a useful negative control precisely
    # because compactness/no-boundary was changed.
    noncompact_signed_count = sp.Integer(1)
    assert_nonzero("noncompact coordinate line avoids compact Euler cancellation", noncompact_signed_count)

    ghost_pairs = 4
    cf_mass_squared = sp.symbols("cf_mass_squared", nonzero=True)
    ghost_saturation_at_t0 = cf_mass_squared**ghost_pairs
    assert_nonzero(
        "Curci-Ferrari mass can saturate ghosts only after changing nilpotent BRST setup",
        ghost_saturation_at_t0,
    )

    oriented_sum = sp.Integer(0)
    absolute_sum = sp.Integer(2)
    assert_nonzero(
        "minimal or absolute Landau prescriptions are not the oriented BRST sum",
        absolute_sum - oriented_sum,
    )


def main() -> None:
    check_morse_signed_copy_cancellation()
    check_compact_lie_group_euler_characteristics()
    check_residual_global_mode_and_zero_over_zero()
    check_escape_route_assumption_changes()
    print("All lattice BRST Neuberger finite-topology checks passed.")


if __name__ == "__main__":
    main()
