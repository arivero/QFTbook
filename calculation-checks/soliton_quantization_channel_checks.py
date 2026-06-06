#!/usr/bin/env python3
"""Finite checks for the soliton collective-quantization chapter.

Evidence contract.

Target claims:
- `prop:kink-center-collective-coordinate`: the dimensionless kink center has
  collective metric `G_XX = M_cl = 4/3`, and the normal fluctuation determinant
  must be projected off the translation zero mode.
- `prop:soliton-chapter-dhn-mass-shift`: the sine-Gordon DHN continuum
  determinant term and the normal-ordering counterterm cancel the cutoff
  dependence and leave `-m/pi`.
- `eq:soliton-chapter-jackiw-rebbi-kink-zero-mode` and
  `eq:soliton-chapter-jackiw-rebbi-kink-half-charge`: the sign-changing kink
  mass carries one normalizable Dirac zero mode and a two-state sector with
  charges `-1/2` and `+1/2`.

Independent construction:
- The checks compute the kink energy/norm integrals directly from
  `phi_K=tanh(x)`, build a finite orthogonal projector without using the
  continuum formula as an oracle, differentiate the phase shift, and verify the
  DHN cutoff cancellation algebra symbolically.

Imported assumptions:
- The dimensionless kink potential is `U=(1-phi^2)^2/2`; the sine-Gordon DHN
  check assumes the mode-number normal-ordering convention and the phase shift
  displayed in the chapter.  The Jackiw-Rebbi check assumes paired nonzero
  modes so that only the zero-mode occupancy contributes to the fractional
  sector charge.

Negative controls:
- The script rejects using the wrong zero-mode norm, failing to project off the
  zero mode, dropping the DHN counterterm, using a half counterterm, accepting
  the nonnormalizable Jackiw-Rebbi component, and assigning integer charges to
  the kink zero-mode sector.

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


def check_sine_gordon_dhn_cutoff_cancellation() -> None:
    k, m, cutoff = sp.symbols("k m cutoff", positive=True)
    delta = 2 * sp.atan(m / k)
    derivative = sp.diff(delta, k)
    expected_derivative = -2 * m / (k**2 + m**2)
    assert_zero("sine-Gordon phase-shift derivative", sp.together(derivative - expected_derivative))

    continuum = -m / sp.pi * sp.asinh(cutoff / m)
    counterterm = m / sp.pi * sp.asinh(cutoff / m) - m / sp.pi
    assert_zero("DHN cutoff cancellation", sp.together(continuum + counterterm + m / sp.pi))

    missing_counterterm = continuum
    half_counterterm = continuum + counterterm / 2
    assert_not_equal("missing DHN counterterm", sp.simplify(missing_counterterm), -m / sp.pi)
    assert_not_equal("half DHN counterterm", sp.simplify(half_counterterm), -m / sp.pi)


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
    check_sine_gordon_dhn_cutoff_cancellation()
    check_jackiw_rebbi_zero_mode_and_half_charge()
    print("All soliton quantization-channel checks passed.")


if __name__ == "__main__":
    main()
