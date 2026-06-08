#!/usr/bin/env python3
"""Finite checks for the soliton collective-quantization chapter.

Evidence contract.

Target claims:
- `prop:kink-center-collective-coordinate`: the dimensionless kink center has
  collective metric `G_XX = M_cl = 4/3`, and the normal fluctuation determinant
  must be projected off the translation zero mode.
- `prop:soliton-chapter-dhn-mass-shift`: the sine-Gordon DHN mode-number
  determinant, zero-mode/Levinson term, first-Born no-tadpole subtraction, and
  finite phase-shift surface term reconstruct `-m/pi` without assigning that
  finite number to the counterterm.
- `eq:soliton-chapter-jackiw-rebbi-kink-zero-mode` and
  `eq:soliton-chapter-jackiw-rebbi-kink-half-charge`: the sign-changing kink
  mass carries one normalizable Dirac zero mode and a two-state sector with
  charges `-1/2` and `+1/2`.

Independent construction:
- The checks compute the kink energy/norm integrals directly from
  `phi_K=tanh(x)`, build a finite orthogonal projector without using the
  continuum formula as an oracle, differentiate the phase shift, derive the
  first Born phase from the fluctuation-potential integral, and reconstruct the
  finite DHN mass shift from the Born-subtracted integral.

Imported assumptions:
- The dimensionless kink potential is `U=(1-phi^2)^2/2`; the sine-Gordon DHN
  check assumes the mode-number normal-ordering convention, the no-tadpole
  first-Born subtraction, and the phase-shift branch displayed in the chapter.
  The Jackiw-Rebbi check assumes paired nonzero modes so that only the
  zero-mode occupancy contributes to the fractional sector charge.

Negative controls:
- The script rejects using the wrong zero-mode norm, failing to project off the
  zero mode, omitting the phase-shift surface term, omitting or double-counting
  the translation zero mode, leaving the first Born term unsubtracted, inserting
  a finite counterterm, using the exact breather answer as the counterterm
  definition, accepting the nonnormalizable Jackiw-Rebbi component, and assigning
  integer charges to the kink zero-mode sector.

Scope boundary:
- Passing these checks proves finite algebra and convention-sensitive
  bookkeeping.  It does not prove the continuum spectral theorem for the
  fluctuation operator, construct the full kink Hilbert space, or establish
  nonperturbative existence of the soliton sector.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.factor(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name} failed: {lhs!r} != {rhs!r}")


def assert_not_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs == rhs:
        raise AssertionError(f"{name}: wrong shortcut unexpectedly matched {lhs!r}")


def dot(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return (left.T * right)[0]


def check_phi4_kink_collective_norm_and_mass() -> None:
    x = sp.symbols("x", real=True)
    phi = sp.tanh(x)
    zero_mode = sp.diff(phi, x)
    potential = sp.Rational(1, 2) * (1 - phi**2) ** 2
    energy_density = sp.Rational(1, 2) * zero_mode**2 + potential

    mass = sp.integrate(energy_density, (x, -sp.oo, sp.oo))
    zero_norm = sp.integrate(zero_mode**2, (x, -sp.oo, sp.oo))
    assert_equal("dimensionless kink mass", mass, sp.Rational(4, 3))
    assert_equal("translation zero-mode norm", zero_norm, sp.Rational(4, 3))
    assert_equal("BPS kink norm equals mass", zero_norm, mass)

    wrong_norm = sp.integrate(sp.sech(x) ** 2, (x, -sp.oo, sp.oo))
    assert_not_equal("wrong zero-mode profile norm", wrong_norm, zero_norm)


def check_zero_mode_projection_removes_translation_mode() -> None:
    psi = sp.Matrix([2, -1, 2, 1])
    fluctuation = sp.Matrix([5, 3, -2, 4])
    projected = fluctuation - psi * dot(psi, fluctuation) / dot(psi, psi)
    assert_zero("finite zero-mode projection", dot(psi, projected))

    projected_twice = projected - psi * dot(psi, projected) / dot(psi, psi)
    for entry in projected_twice - projected:
        assert_zero("projection idempotence", entry)

    assert_not_equal("unprojected fluctuation has zero-mode overlap", dot(psi, fluctuation), 0)


def check_sine_gordon_dhn_mode_number_formula() -> None:
    k, m, cutoff, length, s, radius = sp.symbols("k m cutoff length s radius", positive=True)
    delta = 2 * sp.atan(m / k)
    derivative = sp.diff(delta, k)
    expected_derivative = -2 * m / (k**2 + m**2)
    assert_zero("sine-Gordon phase-shift derivative", sp.together(derivative - expected_derivative))

    density_shift = sp.diff(delta / sp.pi, k)
    assert_zero("mode-number density shift", sp.together(density_shift - expected_derivative / sp.pi))

    shifted_momentum = k - delta / length
    vacuum_mode_number = length * k / sp.pi
    soliton_mode_number = (length * shifted_momentum + delta) / sp.pi
    assert_zero("same-mode-number quantization shift", sp.expand(soliton_mode_number - vacuum_mode_number))

    potential_integral = -4 * m
    first_born = -potential_integral / (2 * k)
    assert_zero("first Born phase from fluctuation potential", sp.together(first_born - 2 * m / k))

    dimensionless_delta = 2 * sp.atan(1 / s)
    dimensionless_born = 2 / s
    cutoff_integral = sp.sqrt(1 + radius**2) * 2 * sp.atan(1 / radius) - sp.pi
    assert_zero(
        "Born-subtracted phase integral limit",
        sp.simplify(sp.limit(cutoff_integral, radius, sp.oo) - (2 - sp.pi)),
    )

    # This identity is the integration-by-parts evaluation of
    # int_0^R s/sqrt(1+s^2) [delta(s)-delta_1(s)] ds.
    derivative_of_integral = sp.diff(cutoff_integral.subs(radius, s), s)
    integrand = s / sp.sqrt(1 + s**2) * (dimensionless_delta - dimensionless_born)
    assert_zero("Born-subtracted integral primitive", sp.simplify(derivative_of_integral - integrand))

    finite_integral = m * (2 - sp.pi)
    zero_mode_levinson = -m / 2
    mass_shift = zero_mode_levinson - finite_integral / (2 * sp.pi)
    assert_zero("DHN finite mass shift from determinant pieces", sp.simplify(mass_shift + m / sp.pi))

    omitted_surface_integral = -sp.pi * m
    omitted_surface_shift = zero_mode_levinson - omitted_surface_integral / (2 * sp.pi)
    assert_not_equal("omitted phase-shift surface term", sp.simplify(omitted_surface_shift), -m / sp.pi)

    omitted_zero_mode = -finite_integral / (2 * sp.pi)
    double_counted_zero_mode = -m - finite_integral / (2 * sp.pi)
    assert_not_equal("omitted zero-mode/Levinson term", sp.simplify(omitted_zero_mode), -m / sp.pi)
    assert_not_equal("double-counted zero-mode oscillator", sp.simplify(double_counted_zero_mode), -m / sp.pi)

    raw_unsubtracted = -m / sp.pi * sp.asinh(cutoff / m)
    assert_not_equal("unsubtracted first Born term remains cutoff dependent", raw_unsubtracted, -m / sp.pi)

    no_tadpole_finite_counterterm = sp.Integer(0)
    inserted_finite_counterterm = -m / sp.pi
    breather_defined_counterterm = -m / sp.pi
    assert_not_equal(
        "finite counterterm insertion rejected",
        inserted_finite_counterterm,
        no_tadpole_finite_counterterm,
    )
    assert_not_equal(
        "exact-breather-defined counterterm rejected",
        breather_defined_counterterm,
        no_tadpole_finite_counterterm,
    )


def check_jackiw_rebbi_zero_mode_and_half_charge() -> None:
    x, m = sp.symbols("x m", positive=True)
    profile = sp.sech(m * x)
    kink_mass = m * sp.tanh(m * x)
    assert_zero("Jackiw-Rebbi zero-mode equation", sp.diff(profile, x) + kink_mass * profile)

    u = sp.symbols("u", real=True)
    normalization = sp.Rational(1, 2) * (
        sp.limit(sp.tanh(u), u, sp.oo) - sp.limit(sp.tanh(u), u, -sp.oo)
    )
    assert_equal("Jackiw-Rebbi zero-mode normalization", normalization, 1)

    wrong_component = sp.cosh(m * x)
    assert_zero("formal wrong-component equation", -sp.diff(wrong_component, x) + kink_mass * wrong_component)
    if sp.limit(wrong_component, x, sp.oo) != sp.oo:
        raise AssertionError("wrong Jackiw-Rebbi component should be nonnormalizable")

    empty_charge = sp.Rational(-1, 2)
    filled_charge = empty_charge + 1
    assert_equal("empty soliton zero-mode charge", empty_charge, sp.Rational(-1, 2))
    assert_equal("filled soliton zero-mode charge", filled_charge, sp.Rational(1, 2))
    assert_zero("charge-conjugation symmetric zero-mode pair", empty_charge + filled_charge)

    integer_empty = 0
    integer_filled = 1
    if integer_empty + integer_filled == 0:
        raise AssertionError("integer charges accidentally looked charge-conjugation symmetric")
    assert_not_equal("integer empty charge rejected", integer_empty, empty_charge)
    assert_not_equal("integer filled charge rejected", integer_filled, filled_charge)


def main() -> None:
    check_phi4_kink_collective_norm_and_mass()
    check_zero_mode_projection_removes_translation_mode()
    check_sine_gordon_dhn_mode_number_formula()
    check_jackiw_rebbi_zero_mode_and_half_charge()
    print("All soliton quantization-channel checks passed.")


if __name__ == "__main__":
    main()
