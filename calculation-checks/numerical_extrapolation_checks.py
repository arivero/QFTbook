#!/usr/bin/env python3
"""Exact checks for finite-regulator extrapolation formulae.

The companion manuscript section proves the formulae symbolically.  This file
keeps the displayed Richardson and finite-weight extrapolation coefficients
under exact rational regression tests.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_leq(name, left, right):
    if left > right:
        raise AssertionError(f"{name}: got {left!r} > {right!r}")


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


def main():
    check_finite_data_do_not_determine_limit()
    check_two_cutoff_richardson()
    check_integer_power_weights()
    print("All numerical extrapolation checks passed.")


if __name__ == "__main__":
    main()
