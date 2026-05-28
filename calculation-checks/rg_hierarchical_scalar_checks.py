#!/usr/bin/env python3
"""Exact checks for the hierarchical scalar RG linearization.

Volume XI, Chapter 7 uses the hierarchical scalar map as a theorem-level
benchmark for scalar non-Gaussian Wilsonian fixed points.  These finite
checks verify the exact Gaussian Wick-coordinate eigenvalue and the
engineering exponent bookkeeping used in that discussion.
"""

from fractions import Fraction
from math import comb, factorial


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def trim(poly):
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result) if result else (Fraction(0),)


def wick_polynomial_coefficients(n, variance):
    """Return coefficients of :x^n:_variance in increasing powers of x."""

    coeffs = [Fraction(0) for _ in range(n + 1)]
    for pair_count in range(n // 2 + 1):
        power = n - 2 * pair_count
        coeff = Fraction(factorial(n), factorial(pair_count) * factorial(power))
        coeff *= Fraction(-1, 2) ** pair_count
        coeff *= variance ** pair_count
        coeffs[power] += coeff
    return trim(coeffs)


def gaussian_moment(power, variance):
    if power % 2:
        return Fraction(0)
    moment = Fraction(1)
    for value in range(1, power, 2):
        moment *= value
    return moment * variance ** (power // 2)


def integrate_scaled_shift(poly, scale_squared, fluctuation_variance):
    """Compute E_z p(a x + z) for even p, using a^2 exactly."""

    out = [Fraction(0) for _ in range(len(poly))]
    for source_power, source_coeff in enumerate(poly):
        if source_coeff == 0:
            continue
        for target_power in range(source_power + 1):
            z_power = source_power - target_power
            moment = gaussian_moment(z_power, fluctuation_variance)
            if moment == 0:
                continue
            if target_power % 2:
                raise AssertionError("odd target powers should not occur for even Wick checks")
            scale_factor = scale_squared ** (target_power // 2)
            out[target_power] += (
                source_coeff
                * comb(source_power, target_power)
                * scale_factor
                * moment
            )
    return trim(out)


def multiply_poly(poly, scalar):
    return trim(tuple(scalar * coeff for coeff in poly))


def engineering_exponent(dimension, half_power):
    return dimension - half_power * (dimension - 2)


def pow_int(base, exponent):
    if exponent >= 0:
        return base ** exponent
    return Fraction(1, base ** (-exponent))


def check_wick_coordinate_eigenvalues():
    # Take c_* = 1 and choose gamma = 1-a^2, so that
    # a Phi + zeta has covariance c_* when Phi has covariance c_*.
    variance = Fraction(1)
    for scale_squared in [Fraction(1, 2), Fraction(1, 4), Fraction(1, 9)]:
        fluctuation_variance = variance * (1 - scale_squared)
        for degree in [2, 4, 6, 8]:
            wick = wick_polynomial_coefficients(degree, variance)
            integrated = integrate_scaled_shift(wick, scale_squared, fluctuation_variance)
            expected = multiply_poly(wick, scale_squared ** (degree // 2))
            assert_equal(
                f"Wick eigenvalue degree {degree} at a^2={scale_squared}",
                integrated,
                expected,
            )


def check_engineering_exponents():
    d3_expected = {
        1: Fraction(2),
        2: Fraction(1),
        3: Fraction(0),
        4: Fraction(-1),
        5: Fraction(-2),
    }
    d4_expected = {
        1: Fraction(2),
        2: Fraction(0),
        3: Fraction(-2),
        4: Fraction(-4),
    }
    for half_power, expected in d3_expected.items():
        assert_equal(
            f"D=3 exponent for phi^{2 * half_power}",
            engineering_exponent(Fraction(3), half_power),
            expected,
        )
    for half_power, expected in d4_expected.items():
        assert_equal(
            f"D=4 exponent for phi^{2 * half_power}",
            engineering_exponent(Fraction(4), half_power),
            expected,
        )

    epsilon = Fraction(1, 10)
    near_four = Fraction(4) - epsilon
    assert_equal(
        "quartic is epsilon-relevant near four dimensions",
        engineering_exponent(near_four, 2),
        epsilon,
    )
    assert_true(
        "sextic remains irrelevant near four dimensions",
        engineering_exponent(near_four, 3) < 0,
    )


def check_engineering_eigenvalues():
    scale = Fraction(2)
    assert_equal(
        "D=3 mass eigenvalue",
        pow_int(scale, engineering_exponent(Fraction(3), 1)),
        Fraction(4),
    )
    assert_equal(
        "D=3 quartic eigenvalue",
        pow_int(scale, engineering_exponent(Fraction(3), 2)),
        Fraction(2),
    )
    assert_equal(
        "D=3 sextic eigenvalue",
        pow_int(scale, engineering_exponent(Fraction(3), 3)),
        Fraction(1),
    )
    assert_equal(
        "D=4 quartic eigenvalue",
        pow_int(scale, engineering_exponent(Fraction(4), 2)),
        Fraction(1),
    )
    assert_equal(
        "D=4 sextic eigenvalue",
        pow_int(scale, engineering_exponent(Fraction(4), 3)),
        Fraction(1, 4),
    )


def main():
    check_wick_coordinate_eigenvalues()
    check_engineering_exponents()
    check_engineering_eigenvalues()
    print("All hierarchical scalar RG checks passed.")


if __name__ == "__main__":
    main()
