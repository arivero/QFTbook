#!/usr/bin/env python3
"""Finite scalar-form and character checks for lattice reflection positivity.

These checks support the scalar and Osterwalder-Seiler character-expansion
proofs in Volume XI Chapter 3.  They verify the antilinear scalar reflection
form, finite crossing-kernel square bookkeeping, and finite instances of the
positive Fourier and SU(2) character coefficients used for Wilson plaquette
reflection positivity.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

from fractions import Fraction
import math


def assert_close(label: str, got: float, expected: float, tol: float = 1.0e-12) -> None:
    _assert_close(label, got, expected, tol=tol)


def assert_equal(label: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{label}: got {got!r}, expected {expected!r}")


def gaussian_moment(order: int) -> Fraction:
    if order % 2 == 1:
        return Fraction(0)
    value = 1
    for factor in range(1, order // 2 + 1):
        value *= 2 * factor - 1
    return Fraction(value)


def check_scalar_antilinear_reflection_form() -> None:
    # Theta already conjugates constants.  The reflection-positive form is
    # <Theta F F>; adding an outer conjugation gives the wrong sign for F=i.
    f_constant = 1j
    theta_f = f_constant.conjugate()
    correct_form = theta_f * f_constant
    double_conjugated_form = theta_f.conjugate() * f_constant
    assert_close("scalar RP constant F=i correct real part", correct_form.real, 1.0)
    assert_close("scalar RP constant F=i correct imaginary part", correct_form.imag, 0.0)
    assert_close(
        "scalar RP double-conjugation negative control",
        double_conjugated_form.real,
        -1.0,
    )

    # For one crossing bond with standard Gaussian half-measure and
    # F(x)=i+2x, the kernel expansion gives sum_n c^n/n! |E[F(X)X^n]|^2.
    # This finite shadow checks the absolute-square structure after termwise
    # integration.
    coupling = Fraction(1, 3)
    partial_sum = Fraction(0)
    for order in range(5):
        real_part = 2 * gaussian_moment(order + 1)
        imaginary_part = gaussian_moment(order)
        square = real_part * real_part + imaginary_part * imaginary_part
        partial_sum += coupling**order * square / math.factorial(order)
    assert_equal(
        "scalar crossing-kernel reflected-square partial sum",
        partial_sum,
        Fraction(565, 216),
    )
    if partial_sum <= 0:
        raise AssertionError("scalar reflected-square expansion lost positivity")

    # The proof's absolute-convergence route uses c|xy| <= c(x^2+y^2)/2, so
    # the crossing-square halves assigned to the two sides dominate the
    # absolute kernel before polynomial moments are taken.
    c = Fraction(3, 5)
    x = Fraction(2)
    y = Fraction(-3)
    lhs = c * abs(x * y)
    rhs = c * (x * x + y * y) / 2
    assert_equal("scalar crossing-kernel domination slack", rhs - lhs, Fraction(3, 10))
    if not lhs <= rhs:
        raise AssertionError("crossing-kernel absolute domination failed")


def bessel_i_nonnegative_integer(n: int, beta: float, terms: int = 80) -> float:
    """Compute I_n(beta) from its positive power series."""

    if n < 0:
        n = -n
    total = 0.0
    half_beta = beta / 2.0
    for r in range(terms):
        total += half_beta ** (2 * r + n) / (
            math.factorial(r) * math.factorial(r + n)
        )
    return total


def su2_character(two_j: int, theta: float) -> float:
    """SU(2) spin-j character with two_j = 2j."""

    denominator = math.sin(theta)
    if abs(denominator) < 1.0e-12:
        return float(two_j + 1)
    return math.sin((two_j + 1) * theta) / denominator


def check_u1_bessel_coefficients() -> None:
    beta = 1.3
    for n in range(-8, 9):
        coeff = bessel_i_nonnegative_integer(n, beta)
        if coeff <= 0:
            raise AssertionError(f"U(1) coefficient I_{n} is not positive")
        assert_close(
            f"U(1) I_{{-{abs(n)}}}=I_{{{abs(n)}}}",
            coeff,
            bessel_i_nonnegative_integer(abs(n), beta),
        )

    theta = 0.73
    truncated = sum(
        bessel_i_nonnegative_integer(n, beta) * complex(math.cos(n * theta), math.sin(n * theta))
        for n in range(-22, 23)
    )
    assert_close("U(1) Fourier reconstruction real part", truncated.real, math.exp(beta * math.cos(theta)), 1.0e-11)
    assert_close("U(1) Fourier reconstruction imaginary part", truncated.imag, 0.0, 1.0e-14)


def check_su2_wilson_coefficients() -> None:
    beta = 0.9
    for two_j in range(0, 14):
        lhs = bessel_i_nonnegative_integer(two_j, beta) - bessel_i_nonnegative_integer(two_j + 2, beta)
        rhs = 2.0 * (two_j + 1) * bessel_i_nonnegative_integer(two_j + 1, beta) / beta
        if lhs <= 0:
            raise AssertionError(f"SU(2) spin {two_j}/2 coefficient is not positive")
        assert_close(f"SU(2) Bessel recurrence coefficient {two_j}", lhs, rhs)

    theta = 0.61
    truncated = sum(
        (
            bessel_i_nonnegative_integer(two_j, beta)
            - bessel_i_nonnegative_integer(two_j + 2, beta)
        )
        * su2_character(two_j, theta)
        for two_j in range(0, 26)
    )
    assert_close("SU(2) Wilson character reconstruction", truncated, math.exp(beta * math.cos(theta)), 1.0e-11)


def check_su2_tensor_product_multiplicities() -> None:
    # The identity chi_j chi_k = sum_{l=|j-k|}^{j+k} chi_l, with l advancing
    # by integer spin steps, is the finite SU(2) version of nonnegative
    # tensor-product multiplicities.
    theta_values = [0.31, 0.83, 1.47, 2.22]
    for two_j in range(0, 7):
        for two_k in range(0, 7):
            low = abs(two_j - two_k)
            high = two_j + two_k
            for theta in theta_values:
                lhs = su2_character(two_j, theta) * su2_character(two_k, theta)
                rhs = sum(su2_character(two_l, theta) for two_l in range(low, high + 1, 2))
                assert_close(f"SU(2) tensor product {two_j}/2 x {two_k}/2", lhs, rhs, 1.0e-11)


def main() -> None:
    check_scalar_antilinear_reflection_form()
    check_u1_bessel_coefficients()
    check_su2_wilson_coefficients()
    check_su2_tensor_product_multiplicities()
    print("All scalar-form and lattice reflection-positivity character checks passed.")


if __name__ == "__main__":
    main()
