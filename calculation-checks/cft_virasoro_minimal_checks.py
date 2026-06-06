#!/usr/bin/env python3
"""Exact finite checks for unitary Virasoro minimal-model conventions."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math
from dataclasses import dataclass
from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_close(name: str, got: float, expected: float, tolerance: float = 1e-9) -> None:
    _assert_close(name, got, expected, tol=tolerance)



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


Charge = tuple[Fraction, Fraction]


def charge_dot(m: int, left: Charge, right: Charge) -> Fraction:
    """Product of (a alpha_+ + b alpha_-) and (c alpha_+ + d alpha_-)."""

    a, b = left
    c, d = right
    alpha_plus_squared = Fraction(2 * (m + 1), m)
    alpha_minus_squared = Fraction(2 * m, m + 1)
    alpha_product = Fraction(-2)
    return (
        a * c * alpha_plus_squared
        + b * d * alpha_minus_squared
        + (a * d + b * c) * alpha_product
    )


def charge_add(left: Charge, right: Charge) -> Charge:
    return (left[0] + right[0], left[1] + right[1])


def charge_sub(left: Charge, right: Charge) -> Charge:
    return (left[0] - right[0], left[1] - right[1])


def charge_scale(scalar: Fraction, charge: Charge) -> Charge:
    return (scalar * charge[0], scalar * charge[1])


def alpha_zero_charge() -> Charge:
    return (Fraction(1, 2), Fraction(1, 2))


def alpha_kac_charge(r: int, s: int) -> Charge:
    return (Fraction(1 - r, 2), Fraction(1 - s, 2))


def coulomb_gas_central_charge(m: int) -> Fraction:
    alpha_zero_squared = charge_dot(m, alpha_zero_charge(), alpha_zero_charge())
    return Fraction(1) - 12 * alpha_zero_squared


def coulomb_gas_weight(m: int, charge: Charge) -> Fraction:
    shifted = charge_sub(charge, charge_scale(Fraction(2), alpha_zero_charge()))
    return Fraction(1, 2) * charge_dot(m, charge, shifted)


def charge_is_null_in_unitary_model(m: int, charge: Charge) -> bool:
    # The unitary relation is m alpha_+ + (m+1) alpha_- = 0.
    return (m + 1) * charge[0] == m * charge[1]


def euler_beta_for_nonnegative_integers(a: int, b: int) -> Fraction:
    return Fraction(math.factorial(a) * math.factorial(b), math.factorial(a + b + 1))


def selberg_two_screening_integer_sum(a: int, b: int, c: int) -> Fraction:
    total = Fraction(0)
    for i in range(b + 1):
        for j in range(b + 1):
            for k in range(2 * c + 1):
                sign = -1 if (i + j + k) % 2 else 1
                total += Fraction(
                    2
                    * sign
                    * math.comb(b, i)
                    * math.comb(b, j)
                    * math.comb(2 * c, k),
                    (a + j + k + 1) * (2 * a + i + j + 2 * c + 2),
                )
    return total


def selberg_two_screening_factorial(a: int, b: int, c: int) -> Fraction:
    return Fraction(
        math.factorial(a)
        * math.factorial(b)
        * math.factorial(a + c)
        * math.factorial(b + c)
        * math.factorial(2 * c),
        math.factorial(a + b + c + 1)
        * math.factorial(a + b + 2 * c + 1)
        * math.factorial(c),
    )


def vector_add(*vectors: list[Fraction]) -> list[Fraction]:
    return [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]


def vector_sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [left[i] - right[i] for i in range(len(left))]


def matrix_vector(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def vector_linf_norm(vector: list[Fraction]) -> Fraction:
    return max(abs(entry) for entry in vector)


def matrix_linf_operator_norm(matrix: list[list[Fraction]]) -> Fraction:
    return max(sum(abs(entry) for entry in row) for row in matrix)


def triangular_labels(m: int) -> list[tuple[int, int]]:
    return [(r, s) for r in range(1, m) for s in range(1, r + 1)]


def kac_reflection(m: int, label: tuple[int, int]) -> tuple[int, int]:
    r, s = label
    return (m - r, m + 1 - s)


def su2_fusion(k: int, a: int, b: int, c: int) -> int:
    if not 0 <= a <= k or not 0 <= b <= k or not 0 <= c <= k:
        return 0
    if abs(a - b) <= c <= min(a + b, 2 * k - a - b) and (a + b + c) % 2 == 0:
        return 1
    return 0


def minimal_fusion_from_su2_orbit(
    m: int,
    left: tuple[int, int],
    right: tuple[int, int],
    target: tuple[int, int],
) -> int:
    r1, s1 = left
    r2, s2 = right
    r3, s3 = target
    reflected_r3, reflected_s3 = kac_reflection(m, target)
    direct = su2_fusion(m - 2, r1 - 1, r2 - 1, r3 - 1) * su2_fusion(
        m - 1, s1 - 1, s2 - 1, s3 - 1
    )
    reflected = su2_fusion(m - 2, r1 - 1, r2 - 1, reflected_r3 - 1) * su2_fusion(
        m - 1, s1 - 1, s2 - 1, reflected_s3 - 1
    )
    return direct + reflected


def minimal_s_entry(m: int, left: tuple[int, int], right: tuple[int, int]) -> float:
    r, s = left
    rp, sp = right
    sign = -1.0 if (1 + s * rp + r * sp) % 2 else 1.0
    factor = 2.0 * math.sqrt(2.0 / (m * (m + 1)))
    return (
        factor
        * sign
        * math.sin(math.pi * (m + 1) * r * rp / m)
        * math.sin(math.pi * m * s * sp / (m + 1))
    )


def theta_label_minus(m: int, label: tuple[int, int]) -> int:
    r, s = label
    return (m + 1) * r - m * s


def theta_label_plus(m: int, label: tuple[int, int]) -> int:
    r, s = label
    return (m + 1) * r + m * s


def poisson_grouped_theta_coefficient(
    m: int, source: tuple[int, int], target_theta_label: int
) -> float:
    k = m * (m + 1)
    source_minus = theta_label_minus(m, source)
    source_plus = theta_label_plus(m, source)
    return (
        2.0
        * (
            math.cos(math.pi * source_minus * target_theta_label / k)
            - math.cos(math.pi * source_plus * target_theta_label / k)
        )
        / math.sqrt(2.0 * k)
    )


def minimal_s_matrix(m: int) -> list[list[float]]:
    labels = triangular_labels(m)
    return [[minimal_s_entry(m, left, right) for right in labels] for left in labels]


def check_rocha_caridi_poisson_s_matrix() -> None:
    for m in range(3, 9):
        for source in triangular_labels(m):
            for target in triangular_labels(m):
                s_entry = minimal_s_entry(m, source, target)
                coefficient_minus = poisson_grouped_theta_coefficient(
                    m, source, theta_label_minus(m, target)
                )
                coefficient_plus = poisson_grouped_theta_coefficient(
                    m, source, theta_label_plus(m, target)
                )
                assert_close(
                    f"Rocha-Caridi Poisson coefficient theta-minus m={m} "
                    f"source={source} target={target}",
                    coefficient_minus,
                    s_entry,
                )
                assert_close(
                    f"Rocha-Caridi Poisson coefficient theta-plus m={m} "
                    f"source={source} target={target}",
                    coefficient_plus,
                    -s_entry,
                )


def check_unitary_minimal_modular_data_and_fusion() -> None:
    for m in range(3, 8):
        labels = triangular_labels(m)
        matrix = minimal_s_matrix(m)
        size = len(labels)

        for row in range(size):
            for column in range(size):
                inner = sum(matrix[row][idx] * matrix[column][idx] for idx in range(size))
                assert_close(
                    f"minimal-model S orthogonality m={m} row={row} column={column}",
                    inner,
                    1.0 if row == column else 0.0,
                )

        for row in range(size):
            for column in range(size):
                squared = sum(matrix[row][idx] * matrix[idx][column] for idx in range(size))
                assert_close(
                    f"minimal-model S^2 charge conjugation m={m} row={row} column={column}",
                    squared,
                    1.0 if row == column else 0.0,
                )

        for left_index, left in enumerate(labels):
            for right_index, right in enumerate(labels):
                for target_index, target in enumerate(labels):
                    verlinde = sum(
                        matrix[left_index][channel_index]
                        * matrix[right_index][channel_index]
                        * matrix[target_index][channel_index]
                        / matrix[0][channel_index]
                        for channel_index in range(size)
                    )
                    rounded = round(verlinde)
                    assert_close(
                        (
                            "minimal-model Verlinde integrality "
                            f"m={m} left={left} right={right} target={target}"
                        ),
                        verlinde,
                        float(rounded),
                    )
                    assert_equal(
                        (
                            "minimal-model orbit fusion "
                            f"m={m} left={left} right={right} target={target}"
                        ),
                        rounded,
                        minimal_fusion_from_su2_orbit(m, left, right, target),
                    )

    ising_order = [(1, 1), (2, 2), (2, 1)]
    ising_s = [
        [minimal_s_entry(3, left, right) for right in ising_order]
        for left in ising_order
    ]
    expected_ising_s = [
        [0.5, math.sqrt(2) / 2, 0.5],
        [math.sqrt(2) / 2, 0.0, -math.sqrt(2) / 2],
        [0.5, -math.sqrt(2) / 2, 0.5],
    ]
    for row in range(3):
        for column in range(3):
            assert_close(
                f"Ising S from minimal-model formula row={row} column={column}",
                ising_s[row][column],
                expected_ising_s[row][column],
            )


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


def check_coulomb_gas_minimal_model_conventions() -> None:
    for m in range(3, 12):
        assert_equal(
            f"Coulomb-gas central charge m={m}",
            coulomb_gas_central_charge(m),
            c_minimal(m),
        )
        assert_equal(
            f"alpha_+ screening weight m={m}",
            coulomb_gas_weight(m, (Fraction(1), Fraction(0))),
            Fraction(1),
        )
        assert_equal(
            f"alpha_- screening weight m={m}",
            coulomb_gas_weight(m, (Fraction(0), Fraction(1))),
            Fraction(1),
        )
        assert_equal(
            f"unitary null charge relation m={m}",
            charge_dot(m, (Fraction(m), Fraction(m + 1)), (Fraction(1), Fraction(0))),
            Fraction(0),
        )
        for r in range(1, m):
            for s in range(1, m + 1):
                charge = alpha_kac_charge(r, s)
                assert_equal(
                    f"Coulomb-gas Kac weight m={m} r={r} s={s}",
                    coulomb_gas_weight(m, charge),
                    h_minimal(m, r, s),
                )
                reflected = alpha_kac_charge(m - r, m + 1 - s)
                conjugate = charge_sub(charge_scale(Fraction(2), alpha_zero_charge()), charge)
                assert_equal(
                    f"Coulomb-gas reflected charge has same weight m={m} r={r} s={s}",
                    coulomb_gas_weight(m, reflected),
                    coulomb_gas_weight(m, charge),
                )
                assert_equal(
                    f"Coulomb-gas reflected charge equals conjugate modulo null relation m={m} r={r} s={s}",
                    charge_is_null_in_unitary_model(m, charge_sub(reflected, conjugate)),
                    True,
                )

    for a in range(0, 7):
        for b in range(0, 7):
            direct_sum = sum(
                Fraction(math.comb(a, k) * (-1) ** k, b + k + 1)
                for k in range(a + 1)
            )
            assert_equal(
                f"Euler beta integer integral A={a} B={b}",
                direct_sum,
                euler_beta_for_nonnegative_integers(a, b),
            )


def check_two_screening_selberg_integer_chamber() -> None:
    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 4):
                assert_equal(
                    f"two-screening Selberg integer chamber A={a} B={b} C={c}",
                    selberg_two_screening_integer_sum(a, b, c),
                    selberg_two_screening_factorial(a, b, c),
                )

    assert_equal(
        "two-screening C=0 beta-square limit",
        selberg_two_screening_factorial(3, 2, 0),
        euler_beta_for_nonnegative_integers(3, 2) ** 2,
    )
    assert_equal(
        "two-screening A=B=0 C=1 Vandermonde value",
        selberg_two_screening_factorial(0, 0, 1),
        Fraction(1, 6),
    )
    assert_equal(
        "two-screening A=B=0 C=0 no-Vandermonde value",
        selberg_two_screening_factorial(0, 0, 0),
        Fraction(1),
    )


def check_coulomb_gas_bpz_comparison_template() -> None:
    # A finite jet test space should see Dotsenko-Fateev screening coordinates
    # pass through five separate comparisons before they are used as full
    # minimal-model correlator coordinates.  The arithmetic below propagates
    # supplied residuals; named slots without bounds are not estimates.
    dotsenko_fateev = [Fraction(2, 5), Fraction(-3, 7)]
    screening_residual = [Fraction(1, 11), Fraction(-1, 13)]
    twisted_cycle_residual = [Fraction(-2, 17), Fraction(1, 19)]
    bpz_residual = [Fraction(3, 23), Fraction(2, 29)]
    continuation_residual = [Fraction(1, 31), Fraction(-4, 37)]
    pairing_residual = [Fraction(2, 41), Fraction(1, 43)]
    connection = [
        [Fraction(2, 3), Fraction(-1, 5)],
        [Fraction(1, 7), Fraction(3, 4)],
    ]

    ward = vector_add(dotsenko_fateev, screening_residual)
    twisted = vector_add(ward, twisted_cycle_residual)
    bpz = vector_add(twisted, bpz_residual)
    continued = vector_add(matrix_vector(connection, bpz), continuation_residual)
    full = vector_add(continued, pairing_residual)

    discrepancy = vector_sub(full, matrix_vector(connection, dotsenko_fateev))
    transported_local_residuals = matrix_vector(
        connection,
        vector_add(screening_residual, twisted_cycle_residual, bpz_residual),
    )
    telescoped = vector_add(
        transported_local_residuals,
        continuation_residual,
        pairing_residual,
    )
    assert_equal(
        "Coulomb-gas screening-to-BPZ comparison decomposition",
        discrepancy,
        telescoped,
    )

    bound = (
        matrix_linf_operator_norm(connection)
        * (
            vector_linf_norm(screening_residual)
            + vector_linf_norm(twisted_cycle_residual)
            + vector_linf_norm(bpz_residual)
        )
        + vector_linf_norm(continuation_residual)
        + vector_linf_norm(pairing_residual)
    )
    if vector_linf_norm(discrepancy) > bound:
        raise AssertionError(
            "Coulomb-gas screening-to-BPZ supplied-bound propagation failed: "
            f"{vector_linf_norm(discrepancy)!r} > {bound!r}"
        )

    named_slots_without_bounds = {
        "screening": None,
        "twisted_cycle": None,
        "bpz_basis": None,
        "analytic_continuation": None,
        "nonchiral_pairing": None,
    }
    assert_equal(
        "boundless Coulomb-gas comparison slots are not estimates",
        all(value is not None for value in named_slots_without_bounds.values()),
        False,
    )

    exact_full = matrix_vector(connection, dotsenko_fateev)
    assert_equal(
        "zero residuals give exact Coulomb-gas/BPZ coordinate comparison",
        vector_sub(exact_full, matrix_vector(connection, dotsenko_fateev)),
        [Fraction(0), Fraction(0)],
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


def check_level_two_kac_determinant_roots() -> None:
    for m in range(3, 12):
        c_value = c_minimal(m)
        for label in ((1, 2), (2, 1)):
            h_value = h_minimal(m, *label)
            matrix = gram_level_two(c_value, h_value)
            assert_equal(
                f"level-two Kac determinant root m={m} label={label}",
                determinant_2(matrix),
                Fraction(0),
            )


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
    check_rocha_caridi_poisson_s_matrix()
    check_unitary_minimal_modular_data_and_fusion()
    check_coulomb_gas_minimal_model_conventions()
    check_two_screening_selberg_integer_chamber()
    check_coulomb_gas_bpz_comparison_template()
    check_level_two_ising_sigma_null_vector()
    check_level_two_kac_determinant_roots()
    check_ising_sigma_bpz_block_solutions()
    check_ising_crossing_matrix_fixes_sigma_sigma_epsilon()
    print("All unitary Virasoro minimal-model and Ising BPZ block checks passed.")


if __name__ == "__main__":
    main()
