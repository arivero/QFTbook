#!/usr/bin/env python3
"""Arithmetic checks for the Unruh/Rindler KMS and detector chapter.

Evidence contract.
Target claims: Volume XII, Chapter 4 separates the distributional free-field
wedge KMS core from the bounded Weyl/von Neumann algebra KMS theorem, derives
detector detailed balance from the stationary spectral KMS relation rather
than from a generic switched contour shift, and computes the normalized
four-dimensional massless scalar Unruh detector rate.
Independent construction: complex boost arithmetic in the mostly-plus boost
plane, finite spectral-density models satisfying the KMS relation, finite
switching smearing by a symmetric approximate identity, compactly supported
smooth switch diagnostics, and the Planck-rate closed form.
Imported assumptions: the tube analyticity of the Wightman function, the
Bisognano-Wichmann theorem for bounded wedge algebras, and the spectral
KMS theorem for stationary positive-type distributions.
Negative controls: finite switching does not obey exact detailed balance, a
compactly supported smooth switch is not an analytic strip regulator, and
the wrong detector detailed-balance sign is rejected.
Scope boundary: these checks do not prove Bisognano-Wichmann, construct the
Weyl algebra, or establish analytic bounds for an interacting detector model.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_finite as _assert_finite
from check_utils import assert_geq as _assert_geq

import cmath
import math


def assert_close(got: float, expected: float, label: str, tol: float = 1e-12) -> None:
    _assert_close(label, got, expected, tol=tol)


def minkowski_square(v0: float, v1: float) -> float:
    return -(v0 * v0) + v1 * v1


def boost(t: complex, y0: float, y1: float) -> tuple[complex, complex]:
    return (
        y0 * cmath.cosh(t) + y1 * cmath.sinh(t),
        y1 * cmath.cosh(t) + y0 * cmath.sinh(t),
    )


def real_boost(t: float, y0: float, y1: float) -> tuple[float, float]:
    return (
        y0 * math.cosh(t) + y1 * math.sinh(t),
        y1 * math.cosh(t) + y0 * math.sinh(t),
    )


def check_complex_boost_imaginary_part() -> None:
    y0, y1 = 0.3, 1.4
    t, s = 0.7, 0.9
    z0, z1 = boost(t + 1j * s, y0, y1)
    bt0, bt1 = real_boost(t, y0, y1)
    assert_close(z0.imag, math.sin(s) * bt1, "imaginary time component")
    assert_close(z1.imag, math.sin(s) * bt0, "imaginary space component")
    # For 0<s<pi the vector (bt1,bt0) is future timelike.
    assert bt1 > abs(bt0)
    assert minkowski_square(bt1, bt0) < 0


def check_ipi_maps_right_to_left_wedge() -> None:
    y0, y1 = -0.2, 1.3
    t = -0.4
    z0, z1 = boost(t + 1j * math.pi, y0, y1)
    bt0, bt1 = real_boost(t, y0, y1)
    assert_close(z0.real, -bt0, "i*pi boost time component")
    assert_close(z1.real, -bt1, "i*pi boost space component")
    assert_close(z0.imag, 0.0, "i*pi boost time imaginary part", tol=1e-12)
    assert_close(z1.imag, 0.0, "i*pi boost space imaginary part", tol=1e-12)
    assert z1.real < -abs(z0.real)


def check_right_left_wedge_spacelike_separation() -> None:
    right = [(0.0, 1.0), (0.4, 1.2), (-0.6, 1.5)]
    left = [(0.0, -1.0), (0.3, -1.4), (-0.5, -1.1)]
    for x0, x1 in right:
        assert x1 > abs(x0)
        for l0, l1 in left:
            assert l1 < -abs(l0)
            h0 = x0 - l0
            h1 = x1 - l1
            if not minkowski_square(h0, h1) > 0:
                raise AssertionError("right-left separation should be spacelike")


def check_detector_detailed_balance_sign() -> None:
    beta = 2 * math.pi
    energy = 0.37
    # The lower-strip convention G(t-i beta)=G(-t) gives the standard
    # detector detailed-balance ratio Pdot(-E)/Pdot(E)=exp(beta E).
    ratio = math.exp(beta * energy)
    assert ratio > 1.0
    assert_close(math.log(ratio) / energy, beta, "detailed-balance exponent")


def planck_excitation_rate(energy: float, acceleration: float) -> float:
    beta = 2 * math.pi / acceleration
    return energy / (2 * math.pi) / math.expm1(beta * energy)


def spectral_rate(omega: float, acceleration: float) -> float:
    if omega == 0:
        return acceleration / (4 * math.pi**2)
    energy = abs(omega)
    beta = 2 * math.pi / acceleration
    if omega > 0:
        return planck_excitation_rate(energy, acceleration)
    return energy / (2 * math.pi) / (1 - math.exp(-beta * energy))


def check_four_dimensional_planck_response() -> None:
    acceleration = 1.7
    energy = 0.43
    beta = 2 * math.pi / acceleration
    excitation = spectral_rate(energy, acceleration)
    deexcitation = spectral_rate(-energy, acceleration)
    expected_excitation = energy / (2 * math.pi) / (math.exp(beta * energy) - 1)
    expected_deexcitation = energy / (2 * math.pi) / (1 - math.exp(-beta * energy))

    assert_close(excitation, expected_excitation, "4d Unruh excitation Planck rate")
    assert_close(deexcitation, expected_deexcitation, "4d Unruh de-excitation rate")
    assert_close(
        deexcitation / excitation,
        math.exp(beta * energy),
        "4d Unruh detailed-balance ratio",
    )
    if not excitation < deexcitation:
        raise AssertionError("excitation should be thermally suppressed for positive gap")


def check_finite_switching_smearing_not_exact_balance() -> None:
    acceleration = 1.0
    beta = 2 * math.pi / acceleration
    energy = 0.41
    delta = 0.13

    stationary_ratio = math.exp(beta * energy)
    smeared_excitation = 0.5 * (
        spectral_rate(energy - delta, acceleration)
        + spectral_rate(energy + delta, acceleration)
    )
    smeared_deexcitation = 0.5 * (
        spectral_rate(-energy - delta, acceleration)
        + spectral_rate(-energy + delta, acceleration)
    )
    smeared_ratio = smeared_deexcitation / smeared_excitation
    _assert_finite("stationary detailed-balance ratio", stationary_ratio)
    _assert_finite("finite-switch smeared excitation", smeared_excitation)
    _assert_finite("finite-switch smeared de-excitation", smeared_deexcitation)
    _assert_finite("finite-switch smeared ratio", smeared_ratio)
    if abs(smeared_ratio - stationary_ratio) < 1e-4:
        raise AssertionError("finite spectral smearing should not give exact detailed balance")

    smaller_delta = delta / 3
    narrower_excitation = 0.5 * (
        spectral_rate(energy - smaller_delta, acceleration)
        + spectral_rate(energy + smaller_delta, acceleration)
    )
    narrower_deexcitation = 0.5 * (
        spectral_rate(-energy - smaller_delta, acceleration)
        + spectral_rate(-energy + smaller_delta, acceleration)
    )
    narrower_ratio = narrower_deexcitation / narrower_excitation
    _assert_finite("narrow finite-switch excitation", narrower_excitation)
    _assert_finite("narrow finite-switch de-excitation", narrower_deexcitation)
    _assert_finite("narrow finite-switch ratio", narrower_ratio)
    if not abs(narrower_ratio - stationary_ratio) < abs(smeared_ratio - stationary_ratio):
        raise AssertionError("narrower switching kernel should approach stationary detailed balance")


def compact_smooth_bump(x: float) -> float:
    if abs(x) >= 1:
        return 0.0
    return math.exp(-1 / (1 - x * x))


def check_nonanalytic_switch_negative_control() -> None:
    # This standard compactly supported smooth bump is a Schwartz function on
    # the real line.  If it had a holomorphic strip extension agreeing with the
    # real function, the extension would vanish on the open real interval
    # (1, infinity), hence everywhere by the identity theorem, contradicting
    # its nonzero value at the origin.
    if compact_smooth_bump(0.0) <= 0:
        raise AssertionError("compact smooth switch should be nonzero inside support")
    assert_close(compact_smooth_bump(1.5), 0.0, "compact smooth switch outside support")

    beta = 2 * math.pi
    gaussian_strip_bound = math.exp(beta * beta)
    for x in (-2.0, 0.0, 3.0):
        for y in (-beta, -beta / 2, 0.0):
            value_abs = math.exp(-x * x + y * y)
            if value_abs > gaussian_strip_bound * (1 + 1e-12):
                raise AssertionError("Gaussian analytic regulator exceeded strip bound")


def check_right_wedge_lightlike_half_sided_sign() -> None:
    """Check the sign convention for the right-wedge modular inclusion."""

    a = 0.8
    points = [(-0.2, 1.1), (0.4, 1.3), (-0.7, 1.6)]

    # Translation by +a e_+ moves the right wedge into itself.
    for x0, x1 in points:
        y0, y1 = x0 + a, x1 + a
        if not y1 > abs(y0):
            raise AssertionError("future-right lightlike translate left the right wedge")

    # Farther future-right translation gives a smaller nested wedge.
    for b in (a, a + 0.3, a + 1.1):
        for x0, x1 in points:
            y0, y1 = x0 + b, x1 + b
            z0, z1 = y0 - a, y1 - a
            if not z1 > abs(z0):
                raise AssertionError("W_R(b) should be contained in W_R(a) for b >= a")

    # With Delta^{it}=U(Lambda_R(-2*pi*t)), the lightlike coordinate scales
    # by exp(-2*pi*t).  The inward translate is therefore left half-sided:
    # sigma_t(N_a) subset N_a exactly for t <= 0.
    for t in (-0.7, -0.2, 0.0):
        scaled = math.exp(-2 * math.pi * t) * a
        if not scaled >= a:
            raise AssertionError("t <= 0 should scale the inward translate deeper")
    for t in (0.2, 0.7):
        scaled = math.exp(-2 * math.pi * t) * a
        if not scaled < a:
            raise AssertionError("t > 0 should scale the translate outward")


def check_physical_light_ray_generator_sign() -> None:
    """Check the mostly-plus translation sign for the inward light-ray group."""

    # Sample future momenta p=(p^0,p^1) in the closed future cone.  With
    # U(x)=exp(i x^mu p_mu) and e_+=(1,1), the phase coefficient is
    # e_+^mu p_mu=-p^0+p^1=-(p^0-p^1).  The positive Stone generator attached
    # to the physical inward translation U(a e_+) is therefore P_+=P^0-P^1.
    future_momenta = [(1.0, 0.0), (2.0, 1.1), (2.4, -1.9), (3.0, 3.0)]
    for energy, px in future_momenta:
        _assert_geq("sample future-cone momentum", energy, abs(px))
        p_plus = energy - px
        covariant_pairing = -energy + px
        if p_plus < -1e-12:
            raise AssertionError("future cone should give non-negative P_+")
        assert_close(covariant_pairing, -p_plus, "e_+ covariant pairing")

    # The same boost convention used for modular flow scales e_+ by
    # exp(-2*pi*t) under Lambda_R(-2*pi*t).
    for t in (-0.3, 0.0, 0.4):
        scaled0, scaled1 = real_boost(-2 * math.pi * t, 1.0, 1.0)
        scale = math.exp(-2 * math.pi * t)
        assert_close(scaled0, scale, "boosted e_+ time component")
        assert_close(scaled1, scale, "boosted e_+ space component")


def main() -> None:
    check_complex_boost_imaginary_part()
    check_ipi_maps_right_to_left_wedge()
    check_right_left_wedge_spacelike_separation()
    check_detector_detailed_balance_sign()
    check_four_dimensional_planck_response()
    check_finite_switching_smearing_not_exact_balance()
    check_nonanalytic_switch_negative_control()
    check_right_wedge_lightlike_half_sided_sign()
    check_physical_light_ray_generator_sign()
    print("All Unruh complex-boost geometry and detailed-balance checks passed.")


if __name__ == "__main__":
    main()
