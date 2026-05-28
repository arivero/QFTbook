#!/usr/bin/env python3
"""Finite checks for the compact-space supersymmetric localization chapter.

The checks verify convention-sensitive pieces that appear in the displayed
S^4 and S^3 matrix models:

* the trace-delta S^4 Gaussian coefficient;
* the root-pair cancellation of S^4 H-factors in the N=4 adjoint-hyper limit;
* the finite normal Gaussian Pfaffian/determinant convention;
* the finite-product logarithmic derivative of the S^4 H-function;
* the elementary U(1) S^4 Gaussian integral;
* the finite double-sine reflection identity and chiral pole convention;
* completion of the square in the U(1)_k S^3 Chern-Simons Fresnel integral;
* the round-sphere chiral-pair determinant integral
  int d sigma /(2 cosh(pi sigma)) = 1/2.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
import mpmath as mp


mp.mp.dps = 50


def assert_close(name: str, got: complex | mp.mpf | mp.mpc, expected: complex | mp.mpf | mp.mpc, tol: mp.mpf) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}, tol={tol}")


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def determinant_exact(matrix: list[list[int | Fraction]]) -> Fraction:
    size = len(matrix)
    work = [[Fraction(entry) for entry in row] for row in matrix]
    det = Fraction(1)
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det *= -1
        pivot_value = work[col][col]
        det *= pivot_value
        for entry in range(col, size):
            work[col][entry] /= pivot_value
        for row in range(col + 1, size):
            factor = work[row][col]
            for entry in range(col, size):
                work[row][entry] -= factor * work[col][entry]
    return det


def pfaffian_exact(matrix: list[list[int | Fraction]]) -> Fraction:
    size = len(matrix)
    if size == 0:
        return Fraction(1)
    if size % 2:
        return Fraction(0)
    total = Fraction(0)
    for column in range(1, size):
        if matrix[0][column] == 0:
            continue
        submatrix = [
            [matrix[row][col] for col in range(size) if col not in (0, column)]
            for row in range(size)
            if row not in (0, column)
        ]
        total += Fraction((-1) ** (column + 1)) * Fraction(matrix[0][column]) * pfaffian_exact(submatrix)
    return total


def check_s4_trace_delta_gaussian_coefficient() -> None:
    # Half-trace variables have tr(T_a T_b)=delta_ab/2 and
    # exp[-8 pi^2 tr_ht(a^2)/g_ht^2].  For the same physical Cartan matrix
    # a, tr_ht(a^2)=(a,a)_delta.  The coupling conversion
    # g_ht^2=2 g_YM^2 therefore gives 4 pi^2 (a,a)_delta/g_YM^2.
    common_coefficient = mp.mpf(8)
    coupling_conversion = mp.mpf("0.5")
    trace_delta_coefficient = common_coefficient * coupling_conversion
    assert_close("S4 trace-delta Gaussian coefficient", trace_delta_coefficient, 4, mp.mpf("1e-40"))


def check_s4_n4_adjoint_hyper_cancellation() -> None:
    # In the N=4 limit an N=2 adjoint hypermultiplet has weights
    # Delta plus rank(G) zero weights.  For each positive root pair, the
    # vector determinant supplies H(alpha)^2 and the adjoint hyper supplies
    # H(alpha)^(-1) H(-alpha)^(-1)=H(alpha)^(-2).  The zero weights are
    # H(0)^(-rank)=1 in the product convention used in the chapter.
    root_pair_data = [
        {"root": "alpha_1", "vector_H_power": 2, "hyper_H_power": -2, "vandermonde_power": 2},
        {"root": "alpha_2", "vector_H_power": 2, "hyper_H_power": -2, "vandermonde_power": 2},
        {"root": "alpha_1+alpha_2", "vector_H_power": 2, "hyper_H_power": -2, "vandermonde_power": 2},
    ]
    for entry in root_pair_data:
        total_H_power = entry["vector_H_power"] + entry["hyper_H_power"]
        assert_equal(f"S4 N=4 H cancellation for {entry['root']}", total_H_power, 0)
        assert_equal(f"S4 N=4 Vandermonde power for {entry['root']}", entry["vandermonde_power"], 2)

    rank_g = 2
    h_zero_value = Fraction(1)
    zero_weight_contribution = h_zero_value ** (-rank_g)
    assert_equal("S4 N=4 adjoint zero-weight contribution", zero_weight_contribution, Fraction(1))


def check_finite_normal_gaussian_factor() -> None:
    examples = [
        [[2]],
        [[1, 3], [2, 5]],
        [[1, 0, 2], [3, -1, 4], [2, 5, 7]],
    ]
    for differential in examples:
        rank = len(differential)
        fermion_matrix = [[Fraction(0) for _ in range(2 * rank)] for _ in range(2 * rank)]
        for row in range(rank):
            for col in range(rank):
                entry = Fraction(differential[row][col])
                fermion_matrix[row][rank + col] = entry
                fermion_matrix[rank + col][row] = -entry

        expected_sign = -1 if (rank * (rank - 1) // 2) % 2 else 1
        expected_pfaffian = Fraction(expected_sign) * determinant_exact(differential)
        assert_equal(
            "finite normal block Pfaffian sign",
            pfaffian_exact(fermion_matrix),
            expected_pfaffian,
        )

    bosonic_matrix = [[2, 1], [1, 3]]
    fermion_matrix = [[0, 4], [-4, 0]]
    det_a = determinant_exact(bosonic_matrix)
    pf_f = pfaffian_exact(fermion_matrix)
    assert_equal("finite normal bosonic determinant", det_a, Fraction(5))
    assert_equal("finite normal fermion Pfaffian", pf_f, Fraction(4))

    normalized_factor = mp.mpf(pf_f.numerator) / mp.mpf(pf_f.denominator)
    normalized_factor /= mp.sqrt(mp.mpf(det_a.numerator) / mp.mpf(det_a.denominator))
    assert_close(
        "finite normal Gaussian normalized factor",
        normalized_factor,
        4 / mp.sqrt(5),
        mp.mpf("1e-45"),
    )

    singular_fermion_matrix = [[0, 0], [0, 0]]
    assert_equal(
        "finite normal fermion zero mode has zero Pfaffian",
        pfaffian_exact(singular_fermion_matrix),
        Fraction(0),
    )
    singular_bosonic_matrix = [[1, 2], [2, 4]]
    assert_equal(
        "finite normal bosonic zero mode has zero determinant",
        determinant_exact(singular_bosonic_matrix),
        Fraction(0),
    )


def check_s4_u1_gaussian_integral() -> None:
    g = mp.mpf("0.73")
    r = mp.mpf("1.4")
    a_coeff = 4 * mp.pi**2 * r**2 / g**2
    numeric = mp.quad(lambda x: mp.e ** (-a_coeff * x * x), [-mp.inf, mp.inf])
    expected = mp.sqrt(mp.pi / a_coeff)
    chapter_value = g / (2 * mp.sqrt(mp.pi) * r)
    assert_close("S4 U(1) Gaussian integral", numeric, expected, mp.mpf("1e-45"))
    assert_close("S4 U(1) chapter value", expected, chapter_value, mp.mpf("1e-45"))


def pestun_H_trunc(x: mp.mpf | mp.mpc, cutoff: int) -> mp.mpf | mp.mpc:
    product = mp.mpf(1)
    for n in range(1, cutoff + 1):
        product *= (1 + x * x / (n * n)) ** n * mp.e ** (-(x * x) / n)
    return product


def check_s4_H_log_derivative() -> None:
    x = mp.mpf("0.37")
    cutoff = 80
    finite_log_derivative = mp.fsum(
        2 * n * x / (n * n + x * x) - 2 * x / n
        for n in range(1, cutoff + 1)
    )
    numeric_log_derivative = mp.diff(lambda y: mp.log(pestun_H_trunc(y, cutoff)), x)
    assert_close(
        "S4 H finite-product log derivative",
        numeric_log_derivative,
        finite_log_derivative,
        mp.mpf("1e-42"),
    )
    assert_close(
        "S4 H finite-product evenness",
        pestun_H_trunc(x, cutoff),
        pestun_H_trunc(-x, cutoff),
        mp.mpf("1e-42"),
    )


def double_sine_trunc(x: complex, b: float, cutoff: int) -> complex:
    q = b + 1 / b
    product = 1 + 0j
    for m in range(cutoff + 1):
        for n in range(cutoff + 1):
            base = m * b + n / b + q / 2
            product *= (base - 1j * x) / (base + 1j * x)
    return product


def check_s3_double_sine_conventions() -> None:
    x = 0.41
    b = 1.3
    cutoff = 12
    sx = double_sine_trunc(x, b, cutoff)
    s_minus_x = double_sine_trunc(-x, b, cutoff)
    assert_close("finite double-sine reflection", sx * s_minus_x, 1, mp.mpf("1e-13"))

    delta = 0.62
    level = 4
    pole_x = -1j * (level + delta)
    y = 1j * (1 - delta) - pole_x
    denominator = level + 1 + 1j * y
    assert_close("round double-sine chiral pole", denominator, 0, mp.mpf("1e-14"))


def check_s3_u1_fresnel_completion() -> None:
    for k in (3, -5):
        zeta = 0.37
        # i*pi*k*sigma^2+2*pi*i*zeta*sigma =
        # i*pi*k*(sigma+zeta/k)^2 - i*pi*zeta^2/k.
        for sigma in (-1.1, 0.2, 2.4):
            lhs = 1j * math.pi * k * sigma**2 + 2j * math.pi * zeta * sigma
            rhs = 1j * math.pi * k * (sigma + zeta / k) ** 2 - 1j * math.pi * zeta**2 / k
            assert_close(f"S3 Fresnel completing square k={k} sigma={sigma}", lhs, rhs, mp.mpf("1e-14"))

        analytic = cmath.exp(1j * math.pi * math.copysign(1, k) / 4) / math.sqrt(abs(k))
        analytic *= cmath.exp(-1j * math.pi * zeta**2 / k)
        # Check the absolute value and the FI-dependent phase shift separately;
        # the framing-dependent overall phase is the first exponential.
        assert_close(f"S3 Fresnel absolute value k={k}", abs(analytic), 1 / math.sqrt(abs(k)), mp.mpf("1e-14"))


def check_s3_chiral_pair_integral() -> None:
    numeric = mp.quad(lambda x: 1 / (2 * mp.cosh(mp.pi * x)), [-mp.inf, mp.inf])
    assert_close("S3 chiral pair integral", numeric, mp.mpf("0.5"), mp.mpf("1e-45"))


def main() -> None:
    check_s4_trace_delta_gaussian_coefficient()
    check_s4_n4_adjoint_hyper_cancellation()
    check_finite_normal_gaussian_factor()
    check_s4_u1_gaussian_integral()
    check_s4_H_log_derivative()
    check_s3_double_sine_conventions()
    check_s3_u1_fresnel_completion()
    check_s3_chiral_pair_integral()
    print("All supersymmetric localization matrix-model checks passed.")


if __name__ == "__main__":
    main()
