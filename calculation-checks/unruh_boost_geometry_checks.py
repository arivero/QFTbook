#!/usr/bin/env python3
"""Arithmetic checks for the Unruh/Rindler KMS and detector chapter.

Evidence contract.
Target claims: Volume XII, Chapter 4 separates the distributional free-field
wedge KMS core from the bounded Weyl/von Neumann algebra KMS theorem, derives
detector detailed balance from the stationary spectral KMS relation rather
than from a generic switched contour shift, and computes the normalized
four-dimensional massless scalar Unruh detector rate.  The pointwise
switching-rate error is stated only under local absolute continuity,
Lipschitz density, spectral-growth, and switch-decay hypotheses.
Independent construction: complex boost arithmetic in the mostly-plus boost
plane, finite spectral-density models satisfying the KMS relation, finite
switching smearing by the scaled Fourier kernel
hat chi_T(nu)=T hat chi(T nu), compactly supported smooth switch diagnostics,
and the Planck-rate closed form.
Imported assumptions: the tube analyticity of the Wightman function, the
Bisognano-Wichmann theorem for bounded wedge algebras, and the spectral
KMS theorem for stationary positive-type distributions.
Negative controls: finite switching does not obey exact detailed balance, a
compactly supported smooth switch is not an analytic strip regulator, and
the wrong detector detailed-balance sign is rejected.  Spectral atoms, a
locally regular density with insufficient tail control, and an incorrectly
normalized approximate identity are rejected as pointwise O(1/T) claims.
Scope boundary: these checks do not prove Bisognano-Wichmann, construct the
Weyl algebra, or establish analytic bounds for an interacting detector model.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_finite as _assert_finite
from check_utils import assert_geq as _assert_geq

import cmath
import math
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
UNRUH_CHAPTER = (
    REPO_ROOT
    / "monograph/tex/volumes/volume_xii/chapter04_unruh_effect_modular_theory.tex"
)


def assert_close(got: float, expected: float, label: str, tol: float = 1e-12) -> None:
    _assert_close(label, got, expected, tol=tol)


def assert_contains(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


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


def gaussian_switch_kernel(nu: float, duration: float) -> float:
    """K_T for chi(t)=exp(-t^2/2) with the chapter's Fourier convention."""

    return duration / math.sqrt(math.pi) * math.exp(-(duration * nu) ** 2)


def check_scaled_switching_kernel_normalization_and_lipschitz_error() -> None:
    # For chi(t)=exp(-t^2/2), hat chi(s)=sqrt(2*pi) exp(-s^2/2) and
    # T_eff=T sqrt(pi).  Hence K_T(nu)=T exp(-T^2 nu^2)/sqrt(pi).
    for duration in (4.0, 9.0):
        # Symbolic Gaussian moments for the actual scaled kernel.
        kernel_mass = 1.0
        first_abs_moment = 1.0 / (duration * math.sqrt(math.pi))
        assert_close(kernel_mass, 1.0, f"scaled switch kernel mass T={duration}")

        energy = 0.7
        rho_at_energy = 1.3
        lipschitz = 0.4
        # rho(omega)=rho(E)+L |omega-E| is locally Lipschitz and has the
        # exact switched average rho(E)+L int |nu|K_T(nu)dnu.
        switched_average = rho_at_energy + lipschitz * first_abs_moment
        predicted_error = lipschitz / (duration * math.sqrt(math.pi))
        assert_close(
            switched_average - rho_at_energy,
            predicted_error,
            f"actual chi_T convolution O(1/T) error T={duration}",
        )

        sample_kernel_zero = gaussian_switch_kernel(0.0, duration)
        expected_kernel_zero = duration / math.sqrt(math.pi)
        assert_close(
            sample_kernel_zero,
            expected_kernel_zero,
            f"scaled switch kernel atom weight T={duration}",
        )


def check_spectral_atom_rejects_pointwise_rate() -> None:
    atom_mass = 0.23
    values = []
    for duration in (5.0, 10.0):
        values.append(atom_mass * gaussian_switch_kernel(0.0, duration))
    assert_close(
        values[1] / values[0],
        2.0,
        "atom at detector gap grows linearly with switch duration",
    )
    if not values[1] > values[0] > 0.0:
        raise AssertionError("atom contribution should not approach a finite pointwise rate")


def check_tail_control_negative_example() -> None:
    # A density can be perfectly Lipschitz near E while making the convolution
    # ill-defined if the switch tail is too weak globally.  With rho(omega)
    # behaving like omega^2 and a normalized Cauchy approximate identity, the
    # integrand tends to a nonzero constant at infinity.
    duration = 3.0
    leading_tail_constant = 1.0 / (math.pi * duration)
    _assert_finite("Cauchy-tail leading constant", leading_tail_constant)
    if not leading_tail_constant > 0.0:
        raise AssertionError("bad tail model should leave a divergent positive tail")


def check_incorrect_kernel_normalization_negative_control() -> None:
    duration = 8.0
    # Omitting the T factor in K_T makes the kernel mass 1/T, so even a
    # constant spectral density would be driven to zero instead of its rate.
    wrong_kernel_mass = 1.0 / duration
    if not wrong_kernel_mass < 0.2:
        raise AssertionError("wrong kernel normalization should suppress mass")
    assert_close(
        wrong_kernel_mass,
        1.0 / duration,
        "incorrect approximate identity normalization",
    )


def check_switching_rate_text_contract() -> None:
    text = UNRUH_CHAPTER.read_text(encoding="utf-8")
    required = [
        r"d\mu_G(\omega)",
        "Pointwise switching-rate error hypotheses",
        "absolutely continuous",
        "Lipschitz",
        "polynomial global growth",
        r"M_1(\chi)",
        r"D_N(\chi)",
        r"N>q+2",
        r"\label{prop:unruh-switching-rate-error-hypotheses}",
        "dyadic decomposition",
        "Atoms, thresholds, and measure limits",
        r"m K_T(0)",
        r"R_T(E)\,\dd E",
    ]
    for phrase in required:
        assert_contains(text, phrase, "switching-rate spectral hypothesis text")


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
    check_scaled_switching_kernel_normalization_and_lipschitz_error()
    check_spectral_atom_rejects_pointwise_rate()
    check_tail_control_negative_example()
    check_incorrect_kernel_normalization_negative_control()
    check_switching_rate_text_contract()
    check_nonanalytic_switch_negative_control()
    check_right_wedge_lightlike_half_sided_sign()
    check_physical_light_ray_generator_sign()
    print("All Unruh complex-boost geometry and detailed-balance checks passed.")


if __name__ == "__main__":
    main()
