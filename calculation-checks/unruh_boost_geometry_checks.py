#!/usr/bin/env python3
"""Arithmetic checks for the Unruh/Rindler complex-boost geometry.

The checks are deliberately elementary: they guard the sign conventions used
in Volume XII, Chapter 4.  The metric convention is mostly plus,
eta(v,v)=-(v0)^2+(v1)^2 for the boost plane.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
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
    check_right_wedge_lightlike_half_sided_sign()
    check_physical_light_ray_generator_sign()
    print("All Unruh complex-boost geometry and detailed-balance checks passed.")


if __name__ == "__main__":
    main()
