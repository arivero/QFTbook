#!/usr/bin/env python3
"""Finite checks for the O(N) sigma-model S-matrix and large-N gap algebra."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np

from check_utils import assert_array_close, assert_close, assert_finite_array, finite_matmul, finite_max_abs


def expect_assertion(name: str, thunk) -> None:
    try:
        thunk()
    except AssertionError:
        return
    raise AssertionError(f"{name}: expected AssertionError")


def sigma2(theta: complex, n: int) -> complex:
    lam = 1.0 / (n - 2.0)
    z = -1j * theta / (2.0 * math.pi)
    value = (
        mp.gamma(lam + z)
        * mp.gamma(0.5 + z)
        * mp.gamma(0.5 + lam - z)
        * mp.gamma(1.0 - z)
        / (
            mp.gamma(0.5 + lam + z)
            * mp.gamma(z)
            * mp.gamma(1.0 + lam - z)
            * mp.gamma(0.5 - z)
        )
    )
    return complex(value)


def sigmas(theta: complex, n: int) -> tuple[complex, complex, complex]:
    s2 = sigma2(theta, n)
    s1 = -(2.0 * math.pi * 1j / (n - 2.0)) * s2 / (1j * math.pi - theta)
    s3 = -(2.0 * math.pi * 1j / (n - 2.0)) * s2 / theta
    return s1, s2, s3


def channel_eigenvalues(theta: complex, n: int) -> tuple[complex, complex, complex]:
    s1, s2, s3 = sigmas(theta, n)
    singlet = n * s1 + s2 + s3
    symmetric_traceless = s2 + s3
    antisymmetric = s2 - s3
    return singlet, symmetric_traceless, antisymmetric


def smatrix(theta: complex, n: int) -> np.ndarray:
    """Return S_{ij}^{kl}(theta) as a matrix on V tensor V."""

    s1, s2, s3 = sigmas(theta, n)
    matrix = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            col = i * n + j
            for k in range(n):
                for ell in range(n):
                    value = 0.0j
                    if i == j and k == ell:
                        value += s1
                    if i == k and j == ell:
                        value += s2
                    if i == ell and j == k:
                        value += s3
                    matrix[k * n + ell, col] = value
    return assert_finite_array(f"O(N) S-matrix theta={theta} N={n}", matrix, ndim=2)


def finite_kron(name: str, left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return assert_finite_array(
        name,
        np.kron(assert_finite_array(f"{name} left", left), assert_finite_array(f"{name} right", right)),
        ndim=2,
    )


def op12(two_body: np.ndarray, n: int) -> np.ndarray:
    return finite_kron("O(N) op12", two_body, np.eye(n, dtype=complex))


def op23(two_body: np.ndarray, n: int) -> np.ndarray:
    return finite_kron("O(N) op23", np.eye(n, dtype=complex), two_body)


def op13(two_body: np.ndarray, n: int) -> np.ndarray:
    flip23 = op23(flip(n), n)
    return finite_matmul(
        "O(N) op13 right conjugation",
        finite_matmul("O(N) op13 left conjugation", flip23, op12(two_body, n)),
        flip23,
    )


def flip(n: int) -> np.ndarray:
    matrix = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            matrix[j * n + i, i * n + j] = 1.0
    return assert_finite_array(f"O(N) flip N={n}", matrix, ndim=2)


def check_sigma2_scalar_identity() -> None:
    for n in (5, 8):
        a = 2.0 * math.pi / (n - 2.0)
        for theta in (0.27, 0.91, 1.43):
            expected = theta * theta / (theta * theta + a * a)
            assert_close(
                f"sigma2 scalar product N={n} theta={theta}",
                sigma2(theta, n) * sigma2(-theta, n),
                expected,
            )


def check_channel_unitarity() -> None:
    for n in (5, 8):
        for theta in (0.31, 0.82, 1.37):
            values = channel_eigenvalues(theta, n)
            reflected = channel_eigenvalues(-theta, n)
            for label, got, rev in zip(("0", "S", "A"), values, reflected, strict=True):
                assert_close(f"channel unitarity {label} N={n} theta={theta}", got * rev, 1.0)


def check_crossing_relations() -> None:
    for n in (5, 8):
        for theta in (0.29, 1.17):
            s1, s2, s3 = sigmas(theta, n)
            crossed_s1, crossed_s2, crossed_s3 = sigmas(1j * math.pi - theta, n)
            assert_close(f"sigma2 crossing N={n} theta={theta}", s2, crossed_s2)
            assert_close(f"sigma1-sigma3 crossing N={n} theta={theta}", s1, crossed_s3)
            assert_close(f"sigma3-sigma1 crossing N={n} theta={theta}", s3, crossed_s1)


def check_yang_baxter_identity() -> None:
    for n in (4, 5):
        for theta, phi in ((0.37, 0.82), (0.61, 1.13)):
            s_theta = smatrix(theta, n)
            s_phi = smatrix(phi, n)
            s_sum = smatrix(theta + phi, n)
            lhs = finite_matmul(
                f"Yang-Baxter lhs final N={n} theta={theta} phi={phi}",
                finite_matmul(
                    f"Yang-Baxter lhs first N={n} theta={theta} phi={phi}",
                    op12(s_theta, n),
                    op13(s_sum, n),
                ),
                op23(s_phi, n),
            )
            rhs = finite_matmul(
                f"Yang-Baxter rhs final N={n} theta={theta} phi={phi}",
                finite_matmul(
                    f"Yang-Baxter rhs first N={n} theta={theta} phi={phi}",
                    op23(s_phi, n),
                    op13(s_sum, n),
                ),
                op12(s_theta, n),
            )
            assert_array_close(f"Yang-Baxter identity N={n} theta={theta} phi={phi}", lhs, rhs)


def check_nonfinite_matrix_negative_controls() -> None:
    bad_input = np.eye(2, dtype=complex)
    bad_input[0, 1] = math.inf
    expect_assertion(
        "O(N) matrix product rejects nonfinite input",
        lambda: finite_matmul("O(N) bad finite input", bad_input, np.eye(2, dtype=complex)),
    )
    huge = np.full((2, 2), 1.0e308, dtype=float)
    expect_assertion(
        "O(N) matrix product rejects nonfinite output",
        lambda: finite_matmul("O(N) bad finite output", huge, huge),
    )
    expect_assertion(
        "O(N) max abs rejects nonfinite input",
        lambda: finite_max_abs("O(N) bad max abs", np.array([1.0, math.nan])),
    )


def check_large_n_gap_and_beta() -> None:
    cutoff = 17.0
    lam = 0.8
    mass = cutoff / math.sqrt(math.exp(4.0 * math.pi / lam) - 1.0)
    integral = math.log((cutoff * cutoff + mass * mass) / (mass * mass)) / (4.0 * math.pi)
    assert_close("large-N cutoff gap equation", integral, 1.0 / lam)

    mu = 11.0
    physical_mass = 0.4
    running = 2.0 * math.pi / math.log(mu / physical_mass)
    beta_from_formula = -running * running / (2.0 * math.pi)
    step = 1.0e-7
    running_plus = 2.0 * math.pi / math.log((mu * math.exp(step)) / physical_mass)
    numerical_beta = (running_plus - running) / step
    assert_close("large-N beta function", numerical_beta, beta_from_formula, tol=1.0e-6)


def main() -> None:
    check_sigma2_scalar_identity()
    check_channel_unitarity()
    check_crossing_relations()
    check_yang_baxter_identity()
    check_nonfinite_matrix_negative_controls()
    check_large_n_gap_and_beta()
    print("All O(N) sigma-model and large-N gap checks passed.")


if __name__ == "__main__":
    main()
