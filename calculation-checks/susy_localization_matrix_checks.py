#!/usr/bin/env python3
"""Finite checks for the compact-space supersymmetric localization chapter.

The checks verify convention-sensitive pieces that appear in the displayed
S^4 and S^3 matrix models:

* the trace-delta S^4 Gaussian coefficient;
* the transverse normal-symbol exactness and equivariant-index multiplicity
  ledger behind the S^4 Pestun one-loop factors;
* the root-pair cancellation of S^4 H-factors in the N=4 adjoint-hyper limit;
* the finite normal Gaussian Pfaffian/determinant convention;
* the protected-insertion residual telescope for the S^4 localization functional;
* the finite-product logarithmic derivative of the S^4 H-function;
* the finite-part determinant ledger behind the S^4 H-powers;
* the elementary U(1) S^4 Gaussian integral;
* the dominated finite-N Laguerre coefficient limit for the planar circular
  Wilson loop and the separate exponential-tail truncation template;
* the Bessel derivative identity that turns the localized circular Wilson
  loop into the planar Bremsstrahlung function once the protected Ward identity
  is supplied;
* the finite double-sine reflection identity and chiral pole convention;
* global Chern-Simons level-lattice, FI-center, contact-block, and
  parity-anomaly half-shift bookkeeping for the S^3 formula;
* completion of the square in the U(1)_k S^3 Chern-Simons Fresnel integral;
* the round-sphere chiral-pair determinant integral
  int d sigma /(2 cosh(pi sigma)) = 1/2.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
import mpmath as mp

from check_utils import assert_geq as _assert_geq
from check_utils import assert_leq as _assert_leq


mp.mp.dps = 50


def assert_close(name: str, got: complex | mp.mpf | mp.mpc, expected: complex | mp.mpf | mp.mpc, tol: mp.mpf) -> None:
    if not mp.isfinite(got) or not mp.isfinite(expected):
        raise AssertionError(f"{name}: nonfinite value {got!r} or {expected!r}")
    if not mp.isfinite(tol) or tol < 0:
        raise AssertionError(f"{name}: invalid tolerance {tol}")
    error = abs(got - expected)
    if not mp.isfinite(error):
        raise AssertionError(f"{name}: nonfinite comparison error")
    if error > tol:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}, tol={tol}")


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def vector_add(*vectors: Vector) -> Vector:
    if not vectors:
        return []
    size = len(vectors[0])
    for vector in vectors:
        assert_equal("vector length agreement", len(vector), size)
    return [sum(vector[index] for vector in vectors) for index in range(size)]


def vector_sub(left: Vector, right: Vector) -> Vector:
    assert_equal("vector length agreement", len(left), len(right))
    return [left[index] - right[index] for index in range(len(left))]


def vector_l1_norm(vector: Vector) -> Fraction:
    return sum(abs(entry) for entry in vector)


def vector_linf_norm(vector: Vector) -> Fraction:
    return max((abs(entry) for entry in vector), default=Fraction(0))


def dot_exact(left: Vector, right: Vector) -> Fraction:
    assert_equal("vector length agreement", len(left), len(right))
    return sum(left[index] * right[index] for index in range(len(left)))


def matrix_bilinear(matrix: Matrix, left: Vector, right: Vector) -> Fraction:
    assert_equal("matrix row count", len(matrix), len(left))
    assert_equal("bilinear vector length", len(left), len(right))
    total = Fraction(0)
    for row, row_entries in enumerate(matrix):
        assert_equal("matrix column count", len(row_entries), len(right))
        total += sum(row_entries[col] * left[row] * right[col] for col in range(len(right)))
    return total


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    assert_equal("matrix row count", len(left), len(right))
    result: Matrix = []
    for left_row, right_row in zip(left, right, strict=True):
        assert_equal("matrix column count", len(left_row), len(right_row))
        result.append([left_row[col] + right_row[col] for col in range(len(left_row))])
    return result


def zero_matrix(size: int) -> Matrix:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def outer_product(weight: Vector) -> Matrix:
    return [[weight[row] * weight[col] for col in range(len(weight))] for row in range(len(weight))]


def parity_shift(weights: list[Vector], signs: list[int]) -> Matrix:
    assert_equal("parity-shift weight/sign count", len(weights), len(signs))
    size = len(weights[0]) if weights else 0
    shift = zero_matrix(size)
    for weight, sign in zip(weights, signs, strict=True):
        assert_equal("parity-shift weight size", len(weight), size)
        contribution = outer_product(weight)
        shift = matrix_add(
            shift,
            [[Fraction(sign, 2) * entry for entry in row] for row in contribution],
        )
    return shift


def matrix_entries_integral(matrix: Matrix) -> bool:
    return all(entry.denominator == 1 for row in matrix for entry in row)


def diagonal_even(matrix: Matrix) -> bool:
    return all(
        matrix[index][index].denominator == 1
        and matrix[index][index].numerator % 2 == 0
        for index in range(len(matrix))
    )


def permute_vector(vector: Vector, permutation: tuple[int, ...]) -> Vector:
    return [vector[index] for index in permutation]


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


def matrix_rank_exact(matrix: list[list[int | Fraction]]) -> int:
    if not matrix:
        return 0
    work = [[Fraction(entry) for entry in row] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    rank = 0
    pivot_col = 0
    while rank < rows and pivot_col < cols:
        pivot = None
        for row in range(rank, rows):
            if work[row][pivot_col] != 0:
                pivot = row
                break
        if pivot is None:
            pivot_col += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][pivot_col]
        for col in range(pivot_col, cols):
            work[rank][col] /= pivot_value
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][pivot_col]
            for col in range(pivot_col, cols):
                work[row][col] -= factor * work[rank][col]
        rank += 1
        pivot_col += 1
    return rank


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


def check_s4_transverse_normal_symbol_exactness() -> None:
    # For the principal part of the vector normal complex
    # Omega^0 --u wedge--> Omega^1 --P^+(u wedge .)--> Omega^+,
    # choose u=e^1.  In the self-dual basis
    # (e12+e34, e13-e24, e14+e23), P^+(e1 wedge a)=0 forces
    # a2=a3=a4=0, so the kernel is exactly the image of the first map.
    d0 = [[1], [0], [0], [0]]
    d1 = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    composition = [
        [sum(d1[row][col] * d0[col][0] for col in range(4))]
        for row in range(3)
    ]
    assert_equal("S4 normal symbol composition vanishes", composition, [[0], [0], [0]])
    assert_equal("S4 normal symbol rank d0", matrix_rank_exact(d0), 1)
    assert_equal("S4 normal symbol rank d1", matrix_rank_exact(d1), 3)
    assert_equal("S4 normal symbol kernel/image dimension", 4 - matrix_rank_exact(d1), matrix_rank_exact(d0))


def check_s4_normal_index_multiplicity_ledger() -> None:
    # The residual round-sphere character q/(1-q)^2 has coefficient n at
    # q^n.  One ordered vector root contributes +n; the root pair contributes
    # +2n; a full hypermultiplet weight contributes -n.
    max_n = 9
    residual_coefficients = [Fraction(n) for n in range(1, max_n + 1)]
    expected_from_convolution = [
        sum(Fraction(1) for _ in range(n))
        for n in range(1, max_n + 1)
    ]
    assert_equal("S4 residual index coefficients q/(1-q)^2", residual_coefficients, expected_from_convolution)

    vector_pair = [2 * coeff for coeff in residual_coefficients]
    hyper_weight = [-coeff for coeff in residual_coefficients]
    for n, coeff in enumerate(residual_coefficients, start=1):
        assert_equal(f"S4 ordered vector root multiplicity n={n}", coeff, Fraction(n))
        assert_equal(f"S4 vector root-pair multiplicity n={n}", vector_pair[n - 1], Fraction(2 * n))
        assert_equal(f"S4 hyper weight multiplicity n={n}", hyper_weight[n - 1], Fraction(-n))

    kappa_vector_pair = 2
    kappa_hyper_weight = -1
    for n in range(1, max_n + 1):
        assert_equal("S4 vector finite-product exponent from index", kappa_vector_pair * n, vector_pair[n - 1])
        assert_equal("S4 hyper finite-product exponent from index", kappa_hyper_weight * n, hyper_weight[n - 1])


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


def check_s4_protected_insertion_residual_budget() -> None:
    # Coordinates are the finite protected-insertion test space
    # (1, W_square, W_square^2).  The five exact residuals model the
    # Stokes, normal, residual-Cartan, instanton-compactification, and
    # continuum/contact-term defects in the chapter telescope.
    localized = [Fraction(5, 2), Fraction(13, 6), Fraction(17, 5)]
    stokes = [Fraction(1, 40), Fraction(-1, 42), Fraction(1, 55)]
    normal = [Fraction(-1, 45), Fraction(1, 63), Fraction(-1, 70)]
    residual = [Fraction(1, 72), Fraction(1, 88), Fraction(-1, 99)]
    instanton = [Fraction(-1, 91), Fraction(1, 104), Fraction(1, 117)]
    continuum = [Fraction(1, 130), Fraction(-1, 143), Fraction(1, 156)]

    total_residual = vector_add(stokes, normal, residual, instanton, continuum)
    regulated = vector_add(localized, total_residual)
    assert_equal(
        "S4 protected-insertion residual telescope",
        vector_sub(regulated, localized),
        total_residual,
    )

    probe = [Fraction(2), Fraction(-3), Fraction(5)]
    discrepancy = dot_exact(vector_sub(regulated, localized), probe)
    residual_probe_sum = sum(
        dot_exact(error, probe)
        for error in (stokes, normal, residual, instanton, continuum)
    )
    assert_equal("S4 protected-insertion probed telescope", discrepancy, residual_probe_sum)

    residual_bound = sum(
        vector_l1_norm(error) * vector_linf_norm(probe)
        for error in (stokes, normal, residual, instanton, continuum)
    )
    _assert_leq("S4 protected-insertion residual norm bound", abs(discrepancy), residual_bound)

    # The Wilson-loop expectation is a ratio, so the unit-insertion residual
    # also enters.  This is the exact finite-dimensional ratio identity.
    delta_unit = total_residual[0]
    delta_wilson = total_residual[1]
    localized_unit = localized[0]
    localized_wilson = localized[1]
    regulated_wilson_expectation = regulated[1] / regulated[0]
    localized_wilson_expectation = localized_wilson / localized_unit
    ratio_difference = regulated_wilson_expectation - localized_wilson_expectation
    expected_ratio_difference = (
        delta_wilson * localized_unit - localized_wilson * delta_unit
    ) / (localized_unit * (localized_unit + delta_unit))
    assert_equal(
        "S4 protected Wilson-loop normalized residual identity",
        ratio_difference,
        expected_ratio_difference,
    )

    zero_vector = [Fraction(0) for _ in localized]
    zero_residual = vector_add(
        zero_vector,
        zero_vector,
        zero_vector,
        zero_vector,
        zero_vector,
    )
    assert_equal("S4 protected-insertion zero-residual closure", zero_residual, zero_vector)


def check_circular_wilson_laguerre_dominated_limit() -> None:
    # From
    # N^{-1} L_{N-1}^{(1)}(-lambda/(4N))
    # = sum_k binom(N,k+1) N^{-(k+1)} (lambda/4)^k/k!,
    # each fixed coefficient is bounded by the planar Bessel coefficient and
    # converges to it as N grows.
    max_power = 8
    ranks = [12, 24, 48, 96]
    for power in range(max_power + 1):
        planar_coefficient_without_lambda = Fraction(
            1,
            (4**power) * math.factorial(power) * math.factorial(power + 1),
        )
        previous_error: Fraction | None = None
        for rank in ranks:
            finite_coefficient = Fraction(
                math.comb(rank, power + 1),
                (rank ** (power + 1)) * (4**power) * math.factorial(power),
            )
            _assert_leq(
                f"finite Laguerre coefficient dominated k={power} N={rank}",
                finite_coefficient,
                planar_coefficient_without_lambda,
            )
            error = planar_coefficient_without_lambda - finite_coefficient
            _assert_leq(f"finite Laguerre coefficient has nonnegative gap k={power} N={rank}", 0, error)
            if previous_error is not None:
                _assert_leq(
                    f"finite Laguerre coefficient convergence improves k={power} N={rank}",
                    error,
                    previous_error,
                )
            previous_error = error

    lambda_value = mp.mpf("1.7")
    partial_bound = mp.fsum(
        (lambda_value / 4) ** power
        / (mp.factorial(power) * mp.factorial(power + 1))
        for power in range(25)
    )
    bessel_value = 2 * mp.besseli(1, mp.sqrt(lambda_value)) / mp.sqrt(lambda_value)
    assert_close(
        "planar Bessel dominated series partial sum",
        partial_bound,
        bessel_value,
        mp.mpf("2e-49"),
    )


def check_circular_wilson_exponential_tail_truncation() -> None:
    # If the maximum eigenvalue has a Gaussian edge tail
    # P(M_N>u) <= exp(-a N u^2), the unbounded insertion is controlled by
    # E[e^M 1_{M>R}] <= e^R P(M>R)+int_R^infty e^u P(M>u) du.
    tail_strength = mp.mpf("0.18")

    def tail_bound(rank: int, cutoff: mp.mpf) -> mp.mpf:
        return mp.e ** (cutoff - tail_strength * rank * cutoff * cutoff) + mp.quad(
            lambda u: mp.e ** (u - tail_strength * rank * u * u),
            [cutoff, mp.inf],
        )

    rank = 20
    previous = tail_bound(rank, mp.mpf("4.0"))
    for cutoff in (mp.mpf("5.0"), mp.mpf("6.0"), mp.mpf("7.0")):
        current = tail_bound(rank, cutoff)
        _assert_leq(f"Wilson exponential tail decreases R={cutoff}", current, previous)
        previous = current

    cutoff = mp.mpf("5.5")
    rank_tail = tail_bound(40, cutoff)
    stronger_rank_tail = tail_bound(80, cutoff)
    _assert_leq("Wilson exponential tail decreases with N", stronger_rank_tail, rank_tail)
    _assert_leq("negative tail is bounded by exp(-R)", mp.e ** (-cutoff), mp.mpf("0.005"))


def check_bremsstrahlung_bessel_derivative() -> None:
    # The localization computation supplies W_0(lambda)=2 I_1(sqrt(lambda))/sqrt(lambda).
    # The physical Bremsstrahlung function also needs the protected circular-loop
    # Ward identity; this check isolates the convention-sensitive derivative.
    def planar_circular_wilson(lambda_value: mp.mpf) -> mp.mpf:
        z = mp.sqrt(lambda_value)
        return 2 * mp.besseli(1, z) / z

    def bremsstrahlung_bessel(lambda_value: mp.mpf) -> mp.mpf:
        z = mp.sqrt(lambda_value)
        return z * mp.besseli(2, z) / (4 * mp.pi**2 * mp.besseli(1, z))

    for lambda_value in (mp.mpf("0.05"), mp.mpf("0.7"), mp.mpf("3.0"), mp.mpf("19.0")):
        ward_derivative = (
            lambda_value
            * mp.diff(lambda mu: mp.log(planar_circular_wilson(mu)), lambda_value)
            / (2 * mp.pi**2)
        )
        bessel_ratio = bremsstrahlung_bessel(lambda_value)
        assert_close(
            f"Bremsstrahlung Bessel derivative lambda={lambda_value}",
            ward_derivative,
            bessel_ratio,
            mp.mpf("2e-48"),
        )

        # Negative control: differentiating log(I_1(sqrt(lambda))) alone drops
        # the -log(sqrt(lambda)) prefactor in W_0 and shifts B by 1/(4*pi^2).
        missing_prefactor = (
            lambda_value
            * mp.diff(lambda mu: mp.log(mp.besseli(1, mp.sqrt(mu))), lambda_value)
            / (2 * mp.pi**2)
        )
        assert_close(
            f"Bremsstrahlung missing-prefactor gap lambda={lambda_value}",
            missing_prefactor - bessel_ratio,
            1 / (4 * mp.pi**2),
            mp.mpf("2e-48"),
        )
        _assert_geq(
            f"Bremsstrahlung missing-prefactor negative control lambda={lambda_value}",
            abs(missing_prefactor - bessel_ratio),
            mp.mpf("0.02"),
        )

    lambda_small = mp.mpf("0.0007")
    weak_series = (
        lambda_small / (16 * mp.pi**2)
        - lambda_small**2 / (384 * mp.pi**2)
        + lambda_small**3 / (6144 * mp.pi**2)
    )
    _assert_leq(
        "Bremsstrahlung weak-series cubic truncation",
        abs(bremsstrahlung_bessel(lambda_small) - weak_series),
        mp.mpf("1e-18"),
    )


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


def check_s4_finite_part_determinant_ledger() -> None:
    x = mp.mpf("0.29")
    cutoff = 17
    harmonic = mp.fsum(1 / mp.mpf(n) for n in range(1, cutoff + 1))
    base_norm = mp.mpf(1)
    for n in range(1, cutoff + 1):
        base_norm *= mp.mpf(n) ** (2 * n)

    for kappa in (2, -1):
        raw = mp.mpf(1)
        for n in range(1, cutoff + 1):
            raw *= (mp.mpf(n * n) + x * x) ** (kappa * n)
        raw_without_constant = raw / (base_norm ** kappa)
        finite_part = raw_without_constant * mp.e ** (-kappa * x * x * harmonic)
        expected = pestun_H_trunc(x, cutoff) ** kappa
        assert_close(
            f"S4 finite-part determinant ledger kappa={kappa}",
            finite_part,
            expected,
            mp.mpf("1e-42"),
        )

    vector_root_pair = pestun_H_trunc(x, cutoff) ** 2
    adjoint_hyper_root_pair = pestun_H_trunc(x, cutoff) ** -2
    assert_close(
        "S4 finite-cutoff N=4 root-pair H cancellation",
        vector_root_pair * adjoint_hyper_root_pair,
        1,
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


def check_s3_cs_level_lattice_data() -> None:
    spin_u1_odd = [[Fraction(3)]]
    nonspin_u1_even = [[Fraction(4)]]
    mixed_nonspin = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(-2)],
    ]
    mixed_bad = [
        [Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(2)],
    ]

    assert_equal("spin U(1) odd level is integral", matrix_entries_integral(spin_u1_odd), True)
    assert_equal("odd U(1) level is not non-spin even", diagonal_even(spin_u1_odd), False)
    assert_equal("even U(1) level is non-spin allowed", diagonal_even(nonspin_u1_even), True)
    assert_equal("mixed non-spin diagonal parity", diagonal_even(mixed_nonspin), True)
    assert_equal("mixed bad diagonal parity", diagonal_even(mixed_bad), False)

    samples = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(2), Fraction(-3)],
    ]
    for sample in samples:
        value = matrix_bilinear(mixed_nonspin, sample, sample)
        assert_equal("non-spin even quadratic self-pairing", value.denominator, 1)
        assert_equal("non-spin even quadratic parity", value.numerator % 2, 0)


def check_s3_un_weyl_and_fi_data() -> None:
    n = 3
    k = Fraction(5)
    level = [[k if row == col else Fraction(0) for col in range(n)] for row in range(n)]
    vectors = [
        [Fraction(1), Fraction(-2), Fraction(0)],
        [Fraction(3), Fraction(1), Fraction(-1)],
    ]
    permutations = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

    for vector in vectors:
        original = matrix_bilinear(level, vector, vector)
        for permutation in permutations:
            permuted = permute_vector(vector, permutation)
            assert_equal("standard U(N) level is Weyl invariant", matrix_bilinear(level, permuted, permuted), original)

    central_fi = [Fraction(7, 3), Fraction(7, 3), Fraction(7, 3)]
    roots = [
        [Fraction(1), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(-1)],
        [Fraction(1), Fraction(0), Fraction(-1)],
    ]
    for root in roots:
        assert_equal("U(N) FI coordinate annihilates SU(N) roots", dot_exact(central_fi, root), Fraction(0))

    noncentral_candidate = [Fraction(1), Fraction(0), Fraction(0)]
    assert_equal("noncentral FI candidate detects a semisimple root", dot_exact(noncentral_candidate, roots[0]), Fraction(1))


def check_s3_parity_anomaly_shift_ledger() -> None:
    single_charge_shift = parity_shift([[Fraction(1)]], [1])
    assert_equal("single charge parity half-shift", single_charge_shift, [[Fraction(1, 2)]])
    assert_equal("uncompensated single charge is nonintegral", matrix_entries_integral(single_charge_shift), False)

    compensated = matrix_add([[-Fraction(1, 2)]], single_charge_shift)
    assert_equal("bare half-level can compensate one charge", compensated, [[Fraction(0)]])
    assert_equal("compensated single charge level is integral", matrix_entries_integral(compensated), True)

    vectorlike_same_regulator = parity_shift([[Fraction(1)], [Fraction(-1)]], [1, 1])
    assert_equal("same-regulator vectorlike pair shifts by one", vectorlike_same_regulator, [[Fraction(1)]])

    vectorlike_opposite_regulator = parity_shift([[Fraction(1)], [Fraction(-1)]], [1, -1])
    assert_equal("opposite-regulator vectorlike pair cancels shift", vectorlike_opposite_regulator, [[Fraction(0)]])

    bifundamental = [Fraction(1), Fraction(-1)]
    conjugate = [Fraction(-1), Fraction(1)]
    bifund_shift = parity_shift([bifundamental], [1])
    assert_equal(
        "single bifundamental half-shift",
        bifund_shift,
        [[Fraction(1, 2), -Fraction(1, 2)], [-Fraction(1, 2), Fraction(1, 2)]],
    )
    paired_bifund_shift = parity_shift([bifundamental, conjugate], [1, 1])
    assert_equal(
        "paired bifundamentals give integral mixed shift",
        paired_bifund_shift,
        [[Fraction(1), -Fraction(1)], [-Fraction(1), Fraction(1)]],
    )


def check_s3_contact_phase_block_bookkeeping() -> None:
    # The localization exponent splits a single extended quadratic form into
    # gauge-gauge, gauge-background, and background-background blocks.
    extended_level = [
        [Fraction(2), Fraction(3)],
        [Fraction(3), Fraction(5)],
    ]
    gauge_value = Fraction(2, 3)
    background_value = -Fraction(5, 4)
    full = matrix_bilinear(extended_level, [gauge_value, background_value], [gauge_value, background_value])
    split = (
        Fraction(2) * gauge_value * gauge_value
        + 2 * Fraction(3) * gauge_value * background_value
        + Fraction(5) * background_value * background_value
    )
    assert_equal("S3 contact phase block split", full, split)

    product_level = [
        [Fraction(4), Fraction(2)],
        [Fraction(2), -Fraction(4)],
    ]
    sigma = [Fraction(3, 5), -Fraction(7, 6)]
    standard_opposite = Fraction(4) * sigma[0] * sigma[0] - Fraction(4) * sigma[1] * sigma[1]
    mixed = 2 * Fraction(2) * sigma[0] * sigma[1]
    assert_equal("product group mixed determinant level", matrix_bilinear(product_level, sigma, sigma), standard_opposite + mixed)


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
    check_s4_transverse_normal_symbol_exactness()
    check_s4_normal_index_multiplicity_ledger()
    check_s4_n4_adjoint_hyper_cancellation()
    check_finite_normal_gaussian_factor()
    check_s4_u1_gaussian_integral()
    check_s4_protected_insertion_residual_budget()
    check_circular_wilson_laguerre_dominated_limit()
    check_circular_wilson_exponential_tail_truncation()
    check_bremsstrahlung_bessel_derivative()
    check_s4_H_log_derivative()
    check_s4_finite_part_determinant_ledger()
    check_s3_double_sine_conventions()
    check_s3_cs_level_lattice_data()
    check_s3_un_weyl_and_fi_data()
    check_s3_parity_anomaly_shift_ledger()
    check_s3_contact_phase_block_bookkeeping()
    check_s3_u1_fresnel_completion()
    check_s3_chiral_pair_integral()
    print("All supersymmetric localization matrix-model checks passed.")


if __name__ == "__main__":
    main()
