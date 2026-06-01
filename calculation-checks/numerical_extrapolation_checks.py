#!/usr/bin/env python3
"""Exact checks for finite-regulator extrapolation formulae.

The companion manuscript section proves the formulae symbolically.  This file
keeps the displayed Richardson and finite-weight extrapolation coefficients
under exact rational regression tests.
"""

import pathlib
import sys
from fractions import Fraction

import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "qft_scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import finite_regulator_extrapolation as finite_extrapolation  # noqa: E402


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name, left, right):
    if left > right:
        raise AssertionError(f"{name}: got {left!r} > {right!r}")


def assert_close(name, actual, expected, tol=1.0e-11):
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_matrix_close(name, actual, expected, tol=1.0e-11):
    error = float(np.max(np.abs(actual - expected)))
    if error > tol:
        raise AssertionError(f"{name}: max error {error:.3e}")


def lagrange_value(nodes, values, x):
    total = Fraction(0)
    for j, node_j in enumerate(nodes):
        factor = Fraction(1)
        for k, node_k in enumerate(nodes):
            if j == k:
                continue
            factor *= (x - node_k) / (node_j - node_k)
        total += values[j] * factor
    return total


def solve_linear_system(matrix, rhs):
    n = len(rhs)
    aug = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if aug[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise AssertionError("singular matrix in extrapolation weights")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [entry / pivot_value for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            scale = aug[row][col]
            if scale == 0:
                continue
            aug[row] = [
                aug[row][entry] - scale * aug[col][entry]
                for entry in range(n + 1)
            ]
    return [aug[row][-1] for row in range(n)]


def extrapolation_weights(scales, m, omega):
    matrix = []
    rhs = []
    for power in range(m + 1):
        matrix.append([scale ** (-power * omega) for scale in scales])
        rhs.append(Fraction(1) if power == 0 else Fraction(0))
    return solve_linear_system(matrix, rhs)


def check_finite_data_do_not_determine_limit():
    cutoffs = [Fraction(2), Fraction(3), Fraction(5)]
    outputs = [Fraction(7), Fraction(-1), Fraction(4)]
    nodes = [Fraction(0)] + [Fraction(1, cutoff) for cutoff in cutoffs]
    for proposed_limit in [Fraction(-11), Fraction(0), Fraction(19, 3)]:
        values = [proposed_limit] + outputs
        assert_equal(
            "interpolated proposed limit",
            lagrange_value(nodes, values, Fraction(0)),
            proposed_limit,
        )
        for cutoff, output in zip(cutoffs, outputs):
            assert_equal(
                f"interpolated finite output K={cutoff}",
                lagrange_value(nodes, values, Fraction(1, cutoff)),
                output,
            )


def check_two_cutoff_richardson():
    target = Fraction(5)
    leading = Fraction(7)
    residual_coeff = Fraction(-3)
    omega = 1
    eta = 2
    cutoff = Fraction(11)

    def value(k):
        return target + leading / k + residual_coeff / (k * k)

    richardson = (2**omega * value(2 * cutoff) - value(cutoff)) / (2**omega - 1)
    expected_error = -residual_coeff / (2 * cutoff * cutoff)
    assert_equal("Richardson target error", richardson - target, expected_error)

    c_bound = abs(residual_coeff)
    theorem_bound = Fraction(2**omega, 2**eta) * c_bound / (2**omega - 1)
    theorem_bound += c_bound / (2**omega - 1)
    theorem_bound /= cutoff**eta
    assert_leq("Richardson bound", abs(richardson - target), theorem_bound)


def check_integer_power_weights():
    scales = [Fraction(1), Fraction(2), Fraction(3)]
    m = 2
    omega = 1
    weights = extrapolation_weights(scales, m, omega)
    assert_equal("weight normalization", sum(weights), Fraction(1))
    for power in [1, 2]:
        moment = sum(
            weight * scale ** (-power * omega)
            for weight, scale in zip(weights, scales)
        )
        assert_equal(f"vanishing moment {power}", moment, Fraction(0))

    target = Fraction(13, 5)
    coeffs = [Fraction(0), Fraction(2), Fraction(-5), Fraction(17)]
    cutoff = Fraction(7)

    def value(k):
        return target + coeffs[1] / k + coeffs[2] / (k * k) + coeffs[3] / (k**3)

    extrapolated = sum(
        weight * value(scale * cutoff)
        for weight, scale in zip(weights, scales)
    )
    expected_error = coeffs[3] * sum(
        weight * scale ** (-(m + 1) * omega)
        for weight, scale in zip(weights, scales)
    ) / (cutoff ** ((m + 1) * omega))
    assert_equal("integer-power extrapolated error", extrapolated - target, expected_error)

    c_bound = abs(coeffs[3])
    theorem_bound = c_bound / (cutoff ** ((m + 1) * omega)) * sum(
        abs(weight) * scale ** (-(m + 1) * omega)
        for weight, scale in zip(weights, scales)
    )
    assert_leq("integer-power extrapolation bound", abs(extrapolated - target), theorem_bound)


def check_correlated_fit_coordinates():
    cutoffs = np.array([6.0, 8.0, 10.0, 14.0, 18.0])
    q = 1.0 / cutoffs
    design = np.column_stack([np.ones_like(q), q, q * q])
    true_coefficients = np.array([2.75, -1.1, 0.6])
    remainder = np.array([0.004, -0.003, 0.002, -0.001, 0.0005])
    fluctuation = np.array([0.010, -0.006, 0.004, -0.002, 0.001])
    data = design @ true_coefficients + remainder + fluctuation

    covariance = np.array(
        [
            [0.040, 0.010, 0.006, 0.003, 0.001],
            [0.010, 0.030, 0.008, 0.004, 0.002],
            [0.006, 0.008, 0.025, 0.006, 0.003],
            [0.003, 0.004, 0.006, 0.020, 0.005],
            [0.001, 0.002, 0.003, 0.005, 0.018],
        ],
        dtype=float,
    )
    if float(np.linalg.eigvalsh(covariance)[0]) <= 0.0:
        raise AssertionError("correlated-fit covariance test matrix is not positive definite")

    inverse_covariance = np.linalg.inv(covariance)
    gram = design.T @ inverse_covariance @ design
    propagator = np.linalg.inv(gram) @ design.T @ inverse_covariance
    fitted = propagator @ data

    assert_matrix_close(
        "correlated fit exact error decomposition",
        fitted - true_coefficients,
        propagator @ (remainder + fluctuation),
    )
    assert_matrix_close(
        "correlated fit coefficient covariance",
        propagator @ covariance @ propagator.T,
        np.linalg.inv(gram),
    )

    intercept_weights = propagator[0, :]
    systematic_bound = float(np.sum(np.abs(intercept_weights) * np.abs(remainder)))
    systematic_shift = float(intercept_weights @ remainder)
    assert_leq("correlated fit systematic envelope", abs(systematic_shift), systematic_bound)

    intercept_variance = float(intercept_weights @ covariance @ intercept_weights)
    assert_close(
        "correlated fit intercept variance",
        intercept_variance,
        float(np.linalg.inv(gram)[0, 0]),
    )

    residual = data - design @ fitted
    chi_square = float(residual @ inverse_covariance @ residual)
    if not np.isfinite(chi_square) or chi_square < 0.0:
        raise AssertionError("correlated fit chi-square coordinate is not finite and nonnegative")


def check_public_correlated_extrapolation_script():
    dataset = finite_extrapolation.smoke_dataset()
    windows = finite_extrapolation.parse_windows("0:5,1:6,0:6", int(dataset.regulators.size))
    result = finite_extrapolation.run(dataset, fit_order=2, base_exponent=1.0, windows=windows)
    assert_equal("public extrapolation window count", len(result["windows"]), 3)
    assert_leq("public extrapolation window spread", 0.0, result["window_intercept_spread"])

    first = result["windows"][0]
    regulators = dataset.regulators[:5]
    q = regulators ** -1.0
    design = np.column_stack([np.ones_like(q), q, q * q])
    covariance = dataset.covariance[:5, :5]
    inverse_covariance = np.linalg.inv(covariance)
    gram = design.T @ inverse_covariance @ design
    propagator = np.linalg.inv(gram) @ design.T @ inverse_covariance
    expected_coefficients = propagator @ dataset.values[:5]
    assert_matrix_close(
        "public extrapolation coefficients",
        np.array(first["coefficients"]),
        expected_coefficients,
    )
    assert_close(
        "public extrapolation intercept variance",
        first["intercept_stat_error"] ** 2,
        float(np.linalg.inv(gram)[0, 0]),
        tol=1.0e-10,
    )
    expected_systematic = float(np.sum(np.abs(propagator[0, :]) * dataset.remainder_envelopes[:5]))
    assert_close("public extrapolation systematic coordinate", first["intercept_systematic_bound"], expected_systematic)


def main():
    check_finite_data_do_not_determine_limit()
    check_two_cutoff_richardson()
    check_integer_power_weights()
    check_correlated_fit_coordinates()
    check_public_correlated_extrapolation_script()
    print("All numerical extrapolation checks passed.")


if __name__ == "__main__":
    main()
