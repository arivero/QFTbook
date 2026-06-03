#!/usr/bin/env python3
"""Checks for scalar bootstrap blocks in two-dimensional integrable scattering.

The finite matrix check also guards the residue-projection convention in the
bound-state fusion identity of Volume VI, Chapter 2.
"""
from check_utils import assert_close as _assert_close
from check_utils import assert_gt as _assert_gt

import cmath
import math
from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_close(label: str, actual: complex, expected: complex, tol: float = 2.0e-12) -> None:
    _assert_close(label, actual, expected, tol=tol)


def assert_equal(label: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def require_distinct(label: str, left, right) -> None:
    if left == right:
        raise AssertionError(
            f"{label}: degenerate finite test did not distinguish the cases"
        )


def zero_matrix(rows: int, cols: int) -> Matrix:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def identity(n: int) -> Matrix:
    out = zero_matrix(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matrix_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def block(theta: complex, x: float) -> complex:
    return cmath.sinh((theta + 1j * math.pi * x) / 2) / cmath.sinh(
        (theta - 1j * math.pi * x) / 2
    )


def block_residue_at_physical_pole(x: float) -> complex:
    return 2j * math.sin(math.pi * x)


def crossing_pair_residue_at_x_pole(x: float) -> complex:
    theta0 = 1j * math.pi * x
    return block_residue_at_physical_pole(x) * block(theta0, 1 - x)


def crossing_pair_residue_at_one_minus_x_pole(x: float) -> complex:
    theta0 = 1j * math.pi * (1 - x)
    return block_residue_at_physical_pole(1 - x) * block(theta0, x)


def check_elementary_block_unitarity_and_crossing_pair() -> None:
    for x in (0.2, 0.35, 0.7):
        for theta in (0.4 + 0.17j, -0.9 + 0.23j, 1.1 - 0.19j):
            assert_close(
                f"elementary block unitarity x={x} theta={theta}",
                block(theta, x) * block(-theta, x),
                1.0 + 0.0j,
            )
            assert_close(
                f"elementary crossing relation x={x} theta={theta}",
                block(1j * math.pi - theta, x),
                -block(theta, 1 - x),
            )
            pair = block(theta, x) * block(theta, 1 - x)
            assert_close(
                f"crossing pair unitarity x={x} theta={theta}",
                pair * block(-theta, x) * block(-theta, 1 - x),
                1.0 + 0.0j,
            )
            assert_close(
                f"crossing pair crossing x={x} theta={theta}",
                pair,
                block(1j * math.pi - theta, x) * block(1j * math.pi - theta, 1 - x),
            )


def check_residue_signs() -> None:
    for x in (0.2, 0.35, 0.7):
        direct = -1j * block_residue_at_physical_pole(x)
        _assert_gt(f"single block direct residue real part x={x}", direct.real, 0.0)
        assert_close(f"single block direct residue imaginary part x={x}", direct.imag, 0.0, tol=1.0e-13)

        residue_x = -1j * crossing_pair_residue_at_x_pole(x)
        residue_one_minus_x = -1j * crossing_pair_residue_at_one_minus_x_pole(x)
        assert_close(
            f"crossing-pair residue at x pole x={x}",
            residue_x,
            -2 * math.tan(math.pi * x),
        )
        assert_close(
            f"crossing-pair residue at one-minus-x pole x={x}",
            residue_one_minus_x,
            2 * math.tan(math.pi * x),
        )
        assert_close(
            f"opposite crossing-pair residue signs x={x}",
            residue_x + residue_one_minus_x,
            0.0 + 0.0j,
        )


def check_fusing_angle_momentum_identity() -> None:
    theta = 0.37
    alpha = 0.41
    beta = 0.73
    mass_b = 1.3
    mass_a = mass_b * math.sin(beta) / math.sin(alpha)
    mass_e = mass_a * math.cos(alpha) + mass_b * math.cos(beta)
    u = alpha + beta

    imaginary_coefficient = mass_a * math.sin(alpha) - mass_b * math.sin(beta)
    assert_close("fusing imaginary momentum cancellation", imaginary_coefficient, 0.0)
    assert_close(
        "fusing mass law of cosines",
        mass_e**2,
        mass_a**2 + mass_b**2 + 2.0 * mass_a * mass_b * math.cos(u),
    )

    def momentum(mass: float, rapidity: complex) -> tuple[complex, complex]:
        return (mass * cmath.cosh(rapidity), mass * cmath.sinh(rapidity))

    pa = momentum(mass_a, theta + 1j * alpha)
    pb = momentum(mass_b, theta - 1j * beta)
    pe = momentum(mass_e, theta)
    assert_close("fused energy component", pa[0] + pb[0], pe[0])
    assert_close("fused momentum component", pa[1] + pb[1], pe[1])


def check_fusion_residue_projection_convention() -> None:
    # A nonorthogonal finite bound-state inclusion/projection.  The residue
    # convention is -i Res S_ab = Gamma_in Gamma_out.
    gamma_in = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(1)],
    ]
    gamma_out = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
    ]
    projection = matmul(gamma_in, gamma_out)
    assert_equal(
        "bound-state residue normalization",
        matmul(gamma_out, gamma_in),
        identity(2),
    )
    assert_equal(
        "bound-state residue projection idempotent",
        matmul(projection, projection),
        projection,
    )

    s_ak = [
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(2), Fraction(-1), Fraction(1)],
    ]
    s_bk = [
        [Fraction(2), Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(3), Fraction(1)],
    ]
    holomorphic_regular_part = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    b0 = matmul(s_ak, s_bk)

    minus_i_residue_unresolved = matmul(b0, projection)
    projected_residue = matmul(matmul(gamma_out, minus_i_residue_unresolved), gamma_in)
    fused_amplitude = matmul(matmul(gamma_out, b0), gamma_in)
    expected_fused_amplitude = [
        [Fraction(5), Fraction(3)],
        [Fraction(2), Fraction(5)],
    ]
    assert_equal("fusion residue projected amplitude", projected_residue, expected_fused_amplitude)
    assert_equal(
        "fusion residue equals bound-state scattering coordinate",
        fused_amplitude,
        expected_fused_amplitude,
    )

    regular_contamination = matmul(
        matmul(
            gamma_out,
            matrix_add(
                matmul(b0, projection),
                matmul(holomorphic_regular_part, projection),
            ),
        ),
        gamma_in,
    )
    require_distinct(
        "fusion residue excludes holomorphic regular coefficient",
        regular_contamination,
        expected_fused_amplitude,
    )
    require_distinct(
        "fusion residue sign convention",
        matrix_scale(Fraction(-1), expected_fused_amplitude),
        expected_fused_amplitude,
    )


def main() -> None:
    check_elementary_block_unitarity_and_crossing_pair()
    check_residue_signs()
    check_fusing_angle_momentum_identity()
    check_fusion_residue_projection_convention()
    print("All integrable scattering bootstrap checks passed.")


if __name__ == "__main__":
    main()
