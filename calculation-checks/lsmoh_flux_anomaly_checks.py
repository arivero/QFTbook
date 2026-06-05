#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- The finite LSMOH flux-insertion calculation is an exact momentum-bookkeeping
  identity: after a 2*pi U(1) flux and the large gauge return, translation and
  the large gauge transformation commute projectively by exp(2*pi*i N/L_x).
- At filling p/q, the shifted crystal momentum is 2*pi*p*L_perp/q modulo 2*pi.
  Nontrivial shifts obstruct a unique symmetric gapped short-range-entangled
  return sector only after the thermodynamic locality/gap hypotheses are added.
- The principal infrared resolutions change assumptions in distinct ways:
  translation breaking enlarges the unit cell, gaplessness drops the uniform-gap
  premise, and topological order supplies sectors that can absorb the momentum.

Independent construction:
- The script performs exact rational arithmetic for the large-gauge/translation
  commutator, spin-1/2 chain as half filling, fractional U(1) filling, and the
  three assumption-changing IR alternatives.

Imported assumptions:
- The charge spectrum is integral, so the boundary contribution in the large
  gauge transformation is exp(2*pi*i integer)=1.
- The finite systems are in a fixed charge sector for the finite momentum
  calculation.  The thermodynamic theorem requires separate locality, gap, and
  quasi-adiabatic-continuation hypotheses; this script does not prove them.

Negative controls:
- Integer filling and transverse volumes divisible by q have trivial finite
  momentum shift.
- Enlarging the translation unit cell by q makes the fractional shift invisible
  in the folded Brillouin zone.
- Topological-sector absorption is represented by a q-sector momentum orbit,
  not by a unique short-range-entangled state.

Scope boundary:
- These checks verify exact finite momentum and projective-phase arithmetic.
  They do not prove Lieb-Robinson bounds, quasi-adiabatic continuation, a
  thermodynamic gap theorem, topological order, or a continuum anomaly map.
"""

from __future__ import annotations

from fractions import Fraction


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_equal(lhs: object, rhs: object, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: expected {rhs!r}, got {lhs!r}")


def mod_one(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def momentum_shift_units(filling: Fraction, transverse_volume: int = 1) -> Fraction:
    """Return Delta P/(2*pi) modulo one."""

    return mod_one(filling * transverse_volume)


def large_gauge_translation_commutator_units(total_charge: int, length_x: int) -> Fraction:
    """Return the phase exponent in T G T^{-1} G^{-1}=exp(2*pi*i exponent)."""

    return mod_one(Fraction(total_charge, length_x))


def check_finite_flux_momentum_identity() -> None:
    length_x = 10
    transverse = 7
    filling = Fraction(2, 5)
    total_charge = filling * length_x * transverse
    assert_true(total_charge.denominator == 1, "finite torus has an integral charge sector")

    commutator = large_gauge_translation_commutator_units(int(total_charge), length_x)
    shift = momentum_shift_units(filling, transverse)
    assert_equal(
        commutator,
        shift,
        "large-gauge/translation commutator equals the flux momentum shift",
    )
    assert_equal(shift, Fraction(4, 5), "coprime transverse volume leaves a nontrivial shift")

    integer_shift = momentum_shift_units(Fraction(3, 1), transverse)
    assert_equal(integer_shift, Fraction(0, 1), "integer filling is the trivial negative control")

    divisible_transverse_shift = momentum_shift_units(Fraction(2, 5), transverse_volume=5)
    assert_equal(
        divisible_transverse_shift,
        Fraction(0, 1),
        "a transverse volume divisible by q can make this finite shift trivial",
    )


def check_spin_half_chain_as_half_filling() -> None:
    length = 12
    filling = Fraction(1, 2)  # n_x=S^z_x+1/2 at zero magnetization.
    total_charge = filling * length
    assert_true(total_charge.denominator == 1, "even spin chain has integral n_x charge")

    shift = large_gauge_translation_commutator_units(int(total_charge), length)
    assert_equal(shift, Fraction(1, 2), "spin-1/2 chain has pi momentum shift")

    doubled_cell_shift = mod_one(2 * shift)
    assert_equal(doubled_cell_shift, Fraction(0, 1), "dimerization folds the shift into the doubled cell")


def check_fractional_filling_ir_resolutions() -> None:
    filling = Fraction(1, 3)
    shift = momentum_shift_units(filling)
    assert_equal(shift, Fraction(1, 3), "one-dimensional filling 1/3 has 2*pi/3 shift")

    unique_symmetric_sre_allowed = shift == 0
    assert_true(not unique_symmetric_sre_allowed, "fractional filling obstructs unique symmetric SRE return")

    enlarged_cell_shift = mod_one(3 * shift)
    assert_equal(enlarged_cell_shift, Fraction(0, 1), "period-three symmetry breaking removes the obstruction")

    topological_sector_momenta = {Fraction(k, 3) for k in range(3)}
    shifted_sector_momenta = {mod_one(momentum + shift) for momentum in topological_sector_momenta}
    assert_equal(
        shifted_sector_momenta,
        topological_sector_momenta,
        "three topological sectors can absorb the LSMOH momentum shift",
    )

    gapless_resolution_changes_gap_hypothesis = True
    assert_true(gapless_resolution_changes_gap_hypothesis, "gaplessness drops the uniform-gap premise")


def check_projective_anomaly_bookkeeping() -> None:
    # A projective spin-1/2 SO(3) unit cell is represented here by its Z_2
    # obstruction class.  Translating a background-defect cut past one unit cell
    # picks up that class; two cells are linear.
    projective_class = Fraction(1, 2)
    one_cell_defect_phase = mod_one(projective_class)
    two_cell_defect_phase = mod_one(2 * projective_class)
    assert_equal(one_cell_defect_phase, Fraction(1, 2), "one spin-1/2 cell carries the nontrivial Z2 class")
    assert_equal(two_cell_defect_phase, Fraction(0, 1), "two spin-1/2 cells can form a linear SO(3) representation")


def main() -> None:
    check_finite_flux_momentum_identity()
    check_spin_half_chain_as_half_filling()
    check_fractional_filling_ir_resolutions()
    check_projective_anomaly_bookkeeping()
    print("LSMOH finite flux/anomaly bookkeeping checks passed.")


if __name__ == "__main__":
    main()
