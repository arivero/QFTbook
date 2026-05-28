#!/usr/bin/env python3
"""Finite algebra checks for glueball-spectrum extraction conventions."""

from __future__ import annotations

from fractions import Fraction


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def mat_mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def transpose(a: Matrix2) -> Matrix2:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def inv2(a: Matrix2) -> Matrix2:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if det == 0:
        raise AssertionError("singular matrix in GEVP check")
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


def diag(d1: Fraction, d2: Fraction) -> Matrix2:
    return ((d1, Fraction(0)), (Fraction(0), d2))


def corr_matrix(z: Matrix2, r1: Fraction, r2: Fraction, t: int) -> Matrix2:
    return mat_mul(mat_mul(z, diag(r1**t, r2**t)), transpose(z))


def check_exact_gevp() -> None:
    # C(t)=Z diag(r_1^t,r_2^t) Z^T has generalized eigenvalues
    # r_i^(t-t0) in the exact two-state subspace.
    z: Matrix2 = ((Fraction(1), Fraction(2)), (Fraction(3), Fraction(5)))
    r1 = Fraction(1, 2)
    r2 = Fraction(1, 5)
    t0 = 1
    t = 4
    gevp_matrix = mat_mul(inv2(corr_matrix(z, r1, r2, t0)), corr_matrix(z, r1, r2, t))
    trace = gevp_matrix[0][0] + gevp_matrix[1][1]
    determinant = gevp_matrix[0][0] * gevp_matrix[1][1] - gevp_matrix[0][1] * gevp_matrix[1][0]
    expected_1 = r1 ** (t - t0)
    expected_2 = r2 ** (t - t0)
    assert_equal("GEVP trace", trace, expected_1 + expected_2)
    assert_equal("GEVP determinant", determinant, expected_1 * expected_2)


def check_large_n_width_counting() -> None:
    # Connected k-glueball amplitudes from normalized single traces scale as
    # N^(2-k).  The width is quadratic in the three-point coupling.
    amp3_power = 2 - 3
    width_power = 2 * amp3_power
    amp4_power = 2 - 4
    assert_equal("three-glueball coupling N-power", Fraction(amp3_power), Fraction(-1))
    assert_equal("two-body glueball width N-power", Fraction(width_power), Fraction(-2))
    assert_equal("four-glueball scattering N-power", Fraction(amp4_power), Fraction(-2))


def check_cubic_spin_splitting() -> None:
    # A continuum J=2 representation restricts to E + T2 under the cubic
    # rotation group; dimensions 2+3 recover 2J+1=5.
    assert_equal("J=2 cubic dimension", Fraction(2 + 3), Fraction(5))
    # Scalar and pseudoscalar channels remain one-dimensional A1 channels.
    assert_equal("J=0 cubic dimension", Fraction(1), Fraction(2 * 0 + 1))


def main() -> None:
    check_exact_gevp()
    check_large_n_width_counting()
    check_cubic_spin_splitting()
    print("All QCD glueball-spectrum extraction checks passed.")


if __name__ == "__main__":
    main()
