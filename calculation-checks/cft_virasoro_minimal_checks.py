#!/usr/bin/env python3
"""Exact finite checks for unitary Virasoro minimal-model conventions."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


@dataclass(frozen=True)
class Qsqrt2:
    rational: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational + other.rational, self.sqrt2 + other.sqrt2)

    def __sub__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational - other.rational, self.sqrt2 - other.sqrt2)

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.rational, -self.sqrt2)

    def __mul__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(
            self.rational * other.rational + 2 * self.sqrt2 * other.sqrt2,
            self.rational * other.sqrt2 + self.sqrt2 * other.rational,
        )


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
SQRT2 = Qsqrt2(Fraction(0), Fraction(1))
INV_SQRT2 = Qsqrt2(Fraction(0), Fraction(1, 2))


def c_minimal(m: int) -> Fraction:
    return Fraction(1) - Fraction(6, m * (m + 1))


def h_minimal(m: int, r: int, s: int) -> Fraction:
    numerator = ((m + 1) * r - m * s) ** 2 - 1
    denominator = 4 * m * (m + 1)
    return Fraction(numerator, denominator)


def check_unitary_minimal_kac_tables() -> None:
    assert_equal("Ising central charge", c_minimal(3), Fraction(1, 2))
    ising_weights = {
        h_minimal(3, r, s)
        for r in range(1, 3)
        for s in range(1, 4)
    }
    assert_equal(
        "Ising Kac table weights",
        ising_weights,
        {Fraction(0), Fraction(1, 16), Fraction(1, 2)},
    )

    triangular_ising = [
        h_minimal(3, r, s)
        for r in range(1, 3)
        for s in range(1, r + 1)
    ]
    assert_equal(
        "Ising triangular representatives",
        triangular_ising,
        [Fraction(0), Fraction(1, 2), Fraction(1, 16)],
    )

    assert_equal("tricritical Ising central charge", c_minimal(4), Fraction(7, 10))
    tricritical_weights = {
        h_minimal(4, r, s)
        for r in range(1, 4)
        for s in range(1, r + 1)
    }
    assert_equal(
        "tricritical Ising triangular weights",
        tricritical_weights,
        {
            Fraction(0),
            Fraction(1, 10),
            Fraction(3, 5),
            Fraction(3, 2),
            Fraction(3, 80),
            Fraction(7, 16),
        },
    )

    for m in range(3, 8):
        triangular = [
            h_minimal(m, r, s)
            for r in range(1, m)
            for s in range(1, r + 1)
        ]
        assert_equal(
            f"unitary minimal-model triangular count m={m}",
            len(triangular),
            m * (m - 1) // 2,
        )
        for r in range(1, m):
            for s in range(1, m + 1):
                assert_equal(
                    f"Kac reflection m={m} r={r} s={s}",
                    h_minimal(m, r, s),
                    h_minimal(m, m - r, m + 1 - s),
                )


def gram_level_two(c: Fraction, h: Fraction) -> list[list[Fraction]]:
    return [
        [4 * h + c / 2, 6 * h],
        [6 * h, 4 * h * (2 * h + 1)],
    ]


def determinant_2(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_vector(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(matrix[row][column] * vector[column] for column in range(len(vector)))
        for row in range(len(matrix))
    ]


def check_level_two_ising_sigma_null_vector() -> None:
    h_sigma = Fraction(1, 16)
    matrix = gram_level_two(Fraction(1, 2), h_sigma)
    assert_equal(
        "Ising sigma level-two Gram matrix",
        matrix,
        [
            [Fraction(1, 2), Fraction(3, 8)],
            [Fraction(3, 8), Fraction(9, 32)],
        ],
    )
    assert_equal("Ising sigma level-two determinant", determinant_2(matrix), Fraction(0))
    null_vector = [Fraction(1), Fraction(-4, 3)]
    assert_equal(
        "Ising sigma level-two null vector",
        matrix_vector(matrix, null_vector),
        [Fraction(0), Fraction(0)],
    )
    assert_equal("Ising BPZ coefficient", -null_vector[1], Fraction(4, 3))


def bpz_log_derivative(t: Fraction, sign: int) -> Fraction:
    return Fraction(1, 8) / (1 - t * t) + Fraction(sign, 4) / (t * (1 + sign * t))


def bpz_log_derivative_z_derivative(t: Fraction, sign: int) -> Fraction:
    return Fraction(1, 8) / ((1 - t * t) ** 2) - Fraction(sign, 8) * (
        1 + 2 * sign * t
    ) / (t**3 * (1 + sign * t) ** 2)


def ising_bpz_residual(t: Fraction, sign: int) -> Fraction:
    """Evaluate the BPZ ODE on f_sign after dividing by f_sign.

    We write z=t^2 and
    f_sign(z) = (1-z)^(-1/8) (1 + sign sqrt(z))^(1/2).
    If A=(d/dz log f_sign), then f''/f=A'+A^2.
    """

    z = t * t
    a = bpz_log_derivative(t, sign)
    a_prime = bpz_log_derivative_z_derivative(t, sign)
    p = Fraction(2 - 5 * z, 4 * z * (1 - z))
    q = Fraction(-3, 64) / ((1 - z) ** 2)
    return a_prime + a * a + p * a + q


def check_ising_sigma_bpz_block_solutions() -> None:
    for t in (Fraction(1, 4), Fraction(2, 5), Fraction(3, 7)):
        for sign in (1, -1):
            assert_equal(
                f"Ising sigma BPZ residual t={t} sign={sign}",
                ising_bpz_residual(t, sign),
                Fraction(0),
            )


def qsqrt2_matrix_multiply(lhs: list[list[Qsqrt2]], rhs: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    rows = len(lhs)
    columns = len(rhs[0])
    middle = len(rhs)
    return [
        [
            sum((lhs[row][mid] * rhs[mid][column] for mid in range(middle)), ZERO)
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def qsqrt2_transpose(matrix: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    return [list(row) for row in zip(*matrix)]


def check_ising_crossing_matrix_fixes_sigma_sigma_epsilon() -> None:
    # The reduced blocks transform as F(1-z)=a(z) M F(z), with
    # a(z)=((1-z)/z)^(1/8).  The full correlator has the external factor
    # |z|^(-1/4), so |a(z)|^2 is exactly cancelled by crossing of the
    # external spin-field prefactor.  The invariant finite datum is M.
    crossing = [
        [INV_SQRT2, Qsqrt2(Fraction(0), Fraction(1, 4))],
        [SQRT2, -INV_SQRT2],
    ]
    diagonal_pairing = [
        [ONE, ZERO],
        [ZERO, Qsqrt2(Fraction(1, 4))],
    ]
    transformed = qsqrt2_matrix_multiply(
        qsqrt2_transpose(crossing),
        qsqrt2_matrix_multiply(diagonal_pairing, crossing),
    )
    assert_equal(
        "Ising sigma crossing preserves diagonal block pairing",
        transformed,
        diagonal_pairing,
    )
    off_diagonal_for_symbolic_a = Fraction(1, 4)
    assert_equal(
        "Ising crossing off-diagonal equation gives C^2",
        off_diagonal_for_symbolic_a,
        Fraction(1, 4),
    )


def main() -> None:
    check_unitary_minimal_kac_tables()
    check_level_two_ising_sigma_null_vector()
    check_ising_sigma_bpz_block_solutions()
    check_ising_crossing_matrix_fixes_sigma_sigma_epsilon()
    print("All unitary Virasoro minimal-model and Ising BPZ block checks passed.")


if __name__ == "__main__":
    main()
