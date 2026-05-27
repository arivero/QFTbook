#!/usr/bin/env python3
r"""Exact checks for cross-section and partial-wave normalizations.

The Volume I cross-section chapter uses a mostly-plus metric, relativistic
state normalization, the \(16\pi\) ordered partial-wave convention, and the
flux \(\mathcal F=4\sqrt{(p_1\cdot p_2)^2-m_1^2m_2^2}\).  This script checks
finite rational identities behind those conventions.
"""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def kallen(s, a, b):
    return s * s + a * a + b * b - 2 * s * a - 2 * s * b - 2 * a * b


def check_kallen_and_flux():
    p = Fraction(3)
    e1 = Fraction(5)
    e2 = Fraction(3)
    m1_sq = e1 * e1 - p * p
    m2_sq = e2 * e2 - p * p
    sqrt_s = e1 + e2
    s = sqrt_s * sqrt_s

    assert_equal(m1_sq, Fraction(16), "sample massive incoming mass squared")
    assert_equal(m2_sq, Fraction(0), "sample massless incoming mass squared")
    assert_equal(kallen(s, m1_sq, m2_sq), 4 * s * p * p, "Kallen COM momentum")

    p1_dot_p2 = -e1 * e2 - p * p
    invariant_square = p1_dot_p2 * p1_dot_p2 - m1_sq * m2_sq
    assert_equal(invariant_square, (sqrt_s * p) ** 2, "invariant flux square")
    assert_equal(4 * sqrt_s * p, Fraction(96), "COM flux")

    v_rel = p / e1 + p / e2
    assert_equal(4 * e1 * e2 * v_rel, Fraction(96), "relative-speed flux")


def check_two_body_phase_space_and_phi4():
    q = Fraction(3)
    p = Fraction(3)
    sqrt_s = Fraction(8)
    s = sqrt_s * sqrt_s
    phase_space_without_pi_sq = q / (16 * sqrt_s)
    differential_without_pi_sq = phase_space_without_pi_sq / (4 * sqrt_s * p)
    assert_equal(phase_space_without_pi_sq, Fraction(3, 128), "two-body dPhi2 coefficient")
    assert_equal(differential_without_pi_sq, Fraction(1, 4096), "differential cross-section coefficient")

    # Identical final scalars with constant tree amplitude M=-g:
    # (1/2) * 4*pi /(64*pi^2*s) = 1/(32*pi*s).
    identical_total_without_one_pi = Fraction(1, 32 * s)
    assert_equal(identical_total_without_one_pi, Fraction(1, 2048), "identical phi4 total coefficient")


def check_partial_wave_unitarity():
    beta = Fraction(3, 4)

    # Elastic point delta=pi/2: S=-1, b=(S-1)/(2i)=i.
    b_real = Fraction(0)
    b_imag = Fraction(1)
    a_imag = b_imag / beta
    assert_equal(a_imag, Fraction(4, 3), "elastic partial-wave amplitude")
    assert_equal(a_imag, beta * a_imag * a_imag, "Im a = beta |a|^2")
    assert_equal(b_real * b_real + (b_imag - Fraction(1, 2)) ** 2, Fraction(1, 4), "unitarity circle")

    # Inelastic point eta=1/2, delta=0: S=1/2 and b=i/4.
    eta = Fraction(1, 2)
    b_real = Fraction(0)
    b_imag = Fraction(1, 4)
    assert_equal(b_imag - (b_real * b_real + b_imag * b_imag), (1 - eta * eta) / 4, "inelastic deficit")
    assert_equal(b_real * b_real + (b_imag - Fraction(1, 2)) ** 2 <= Fraction(1, 4), True, "unitarity disk")


def check_partial_wave_cross_section_coefficient():
    p = Fraction(3)
    beta = Fraction(3, 4)
    s = Fraction(64)

    # From M=16*pi sum(2l+1)a_l P_l and dσ/dΩ=|M|^2/(64*pi^2*s),
    # angular orthogonality gives coefficient 16*pi/s before |a_l|^2.
    coefficient_before_a_sq_without_pi = Fraction(16, 1) / s
    convert_a_to_s = Fraction(1, 1) / (4 * beta * beta)
    coefficient_before_s_minus_one_without_pi = coefficient_before_a_sq_without_pi * convert_a_to_s
    assert_equal(coefficient_before_s_minus_one_without_pi, Fraction(1, 9), "partial-wave sigma coefficient")
    assert_equal(Fraction(1, 1) / (p * p), Fraction(1, 9), "pi over p squared coefficient")


def main():
    check_kallen_and_flux()
    check_two_body_phase_space_and_phi4()
    check_partial_wave_unitarity()
    check_partial_wave_cross_section_coefficient()
    print("All cross-section and partial-wave normalization checks passed.")


if __name__ == "__main__":
    main()
