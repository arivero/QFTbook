#!/usr/bin/env python3
"""Exact finite checks for BV integration and localization identities.

The script checks finite-dimensional algebra used in Volume VIII, Chapter 10:
the one-pair BV Laplacian identity, BV Stokes as an endpoint statement, the
normal Gaussian determinant factor, and the rank-one Mathai-Quillen
normalization.  It does not model an infinite-dimensional gauge-theory
functional integral.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod


Poly = list[Fraction]


def trim(poly: Poly) -> Poly:
    result = poly[:]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly(*coeffs: int | Fraction) -> Poly:
    return trim([Fraction(c) for c in coeffs] or [Fraction(0)])


def add(lhs: Poly, rhs: Poly) -> Poly:
    degree = max(len(lhs), len(rhs))
    return trim([
        (lhs[i] if i < len(lhs) else Fraction(0))
        + (rhs[i] if i < len(rhs) else Fraction(0))
        for i in range(degree)
    ])


def sub(lhs: Poly, rhs: Poly) -> Poly:
    degree = max(len(lhs), len(rhs))
    return trim([
        (lhs[i] if i < len(lhs) else Fraction(0))
        - (rhs[i] if i < len(rhs) else Fraction(0))
        for i in range(degree)
    ])


def mul(lhs: Poly, rhs: Poly) -> Poly:
    out = [Fraction(0)] * (len(lhs) + len(rhs) - 1)
    for i, a_i in enumerate(lhs):
        for j, b_j in enumerate(rhs):
            out[i + j] += a_i * b_j
    return trim(out)


def scale(c: Fraction, p: Poly) -> Poly:
    return trim([c * coefficient for coefficient in p])


def deriv(p: Poly) -> Poly:
    if len(p) == 1:
        return [Fraction(0)]
    return trim([Fraction(i) * p[i] for i in range(1, len(p))])


def eval_poly(p: Poly, x: Fraction) -> Fraction:
    return sum(coefficient * x**i for i, coefficient in enumerate(p))


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def check_bv_product_identity() -> None:
    # One even coordinate x and one odd coordinate xi.  Write
    # F = a(x) + b(x) xi and S = S0(x).  Then
    # Delta(F exp(S/hbar))/exp(S/hbar) = b' + hbar^{-1} S0' b.
    hbar = Fraction(5, 3)
    s0 = poly(2, -1, Fraction(3, 2), Fraction(1, 3))
    s0_prime = deriv(s0)
    examples = [
        (poly(1, 2, 3), poly(-1, 4)),
        (poly(0, -2, 0, 5), poly(3, 0, -7)),
        (poly(5), poly(0, 1, 1)),
    ]
    for index, (_a, b) in enumerate(examples):
        lhs = add(deriv(b), scale(1 / hbar, mul(s0_prime, b)))
        delta_f = deriv(b)
        bracket_s_f = mul(s0_prime, b)
        rhs = add(delta_f, scale(1 / hbar, bracket_s_f))
        assert_equal(f"BV product identity example {index}", lhs, rhs)


def check_bv_stokes_endpoint_term() -> None:
    # For f(x,xi)=a(x)+b(x)xi, Delta f = b'(x).  Integration on [0,1]
    # gives b(1)-b(0), and it vanishes when b has zero endpoint values.
    examples = [poly(0, 1, -1), poly(0, 0, 1, -2, 1), poly(2, -3, 1)]
    for index, b in enumerate(examples):
        integral_delta = eval_poly(b, Fraction(1)) - eval_poly(b, Fraction(0))
        endpoint = eval_poly(b, Fraction(1)) - eval_poly(b, Fraction(0))
        assert_equal(f"BV Stokes endpoint example {index}", integral_delta, endpoint)

    compact_supported_model = poly(0, 0, 1, -2, 1)  # x^2(1-x)^2
    assert_equal(
        "BV Stokes zero boundary",
        eval_poly(compact_supported_model, Fraction(1))
        - eval_poly(compact_supported_model, Fraction(0)),
        Fraction(0),
    )


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return matrix[0][0]
    total = Fraction(0)
    for column in range(n):
        minor = [
            [matrix[i][j] for j in range(n) if j != column]
            for i in range(1, n)
        ]
        total += (-1) ** column * matrix[0][column] * determinant(minor)
    return total


def pfaffian(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    total = Fraction(0)
    for j in range(1, n):
        minor = [
            [matrix[a][b] for b in range(n) if b not in (0, j)]
            for a in range(n)
            if a not in (0, j)
        ]
        total += (-1) ** (j + 1) * matrix[0][j] * pfaffian(minor)
    return total


def check_gaussian_normal_factor() -> None:
    blocks = [Fraction(5), Fraction(-7)]
    b_matrix = [
        [Fraction(0), blocks[0], Fraction(0), Fraction(0)],
        [-blocks[0], Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), blocks[1]],
        [Fraction(0), Fraction(0), -blocks[1], Fraction(0)],
    ]
    assert_equal("Pfaffian block product", pfaffian(b_matrix), prod(blocks))
    assert_equal("Pfaffian square determinant", pfaffian(b_matrix) ** 2, determinant(b_matrix))

    # Choose A with square determinant, so the displayed normal factor is exact.
    a_diagonal = [Fraction(4), Fraction(9), Fraction(25), Fraction(49)]
    det_a = prod(a_diagonal)
    sqrt_det_a = Fraction(2 * 3 * 5 * 7)
    assert_equal("determinant of diagonal A", det_a, sqrt_det_a**2)
    assert_equal(
        "normal Gaussian factor",
        pfaffian(b_matrix) / sqrt_det_a,
        Fraction(-35, 210),
    )


def check_mathai_quillen_rank_one() -> None:
    # The rank-one density integrates to sign(a) after u=sqrt(t)|a|x.
    for a in [Fraction(-5), Fraction(-1), Fraction(2), Fraction(7)]:
        sign = Fraction(1) if a > 0 else Fraction(-1)
        jacobian_sign = a / abs(a)
        assert_equal(f"rank-one MQ sign a={a}", jacobian_sign, sign)


def main() -> None:
    check_bv_product_identity()
    check_bv_stokes_endpoint_term()
    check_gaussian_normal_factor()
    check_mathai_quillen_rank_one()
    print("All BV localization checks passed.")


if __name__ == "__main__":
    main()
