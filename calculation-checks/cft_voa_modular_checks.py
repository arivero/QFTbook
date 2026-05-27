#!/usr/bin/env python3
"""Exact Ising modular-data checks for the VOA/modular-sewing chapter."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


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

    def inverse(self) -> Qsqrt2:
        denominator = self.rational * self.rational - 2 * self.sqrt2 * self.sqrt2
        if denominator == 0:
            raise ZeroDivisionError(self)
        return Qsqrt2(self.rational / denominator, -self.sqrt2 / denominator)

    def __truediv__(self, other: Qsqrt2) -> Qsqrt2:
        return self * other.inverse()


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
SQRT2 = Qsqrt2(Fraction(0), Fraction(1))
HALF = Qsqrt2(Fraction(1, 2))


LABELS = ("1", "sigma", "epsilon")
TOP_WEIGHTS = {
    "1": Fraction(0),
    "sigma": Fraction(1, 16),
    "epsilon": Fraction(1, 2),
}

S = [
    [HALF, Qsqrt2(Fraction(0), Fraction(1, 2)), HALF],
    [Qsqrt2(Fraction(0), Fraction(1, 2)), ZERO, Qsqrt2(Fraction(0), Fraction(-1, 2))],
    [HALF, Qsqrt2(Fraction(0), Fraction(-1, 2)), HALF],
]

EXPECTED_FUSION = {
    ("1", "1"): {"1": 1},
    ("1", "sigma"): {"sigma": 1},
    ("1", "epsilon"): {"epsilon": 1},
    ("sigma", "sigma"): {"1": 1, "epsilon": 1},
    ("sigma", "epsilon"): {"sigma": 1},
    ("epsilon", "epsilon"): {"1": 1},
}


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def matrix_multiply(lhs: list[list[Qsqrt2]], rhs: list[list[Qsqrt2]]) -> list[list[Qsqrt2]]:
    size = len(lhs)
    return [
        [
            sum((lhs[i][k] * rhs[k][j] for k in range(size)), ZERO)
            for j in range(size)
        ]
        for i in range(size)
    ]


def check_s_squared_identity() -> None:
    product = matrix_multiply(S, S)
    identity = [
        [ONE if i == j else ZERO for j in range(3)]
        for i in range(3)
    ]
    assert_equal("Ising S^2", product, identity)


def verlinde(a: int, b: int, c: int) -> Qsqrt2:
    total = ZERO
    for m in range(3):
        total += S[a][m] * S[b][m] * S[c][m] / S[0][m]
    return total


def check_verlinde_fusion() -> None:
    for i, left in enumerate(LABELS):
        for j, right in enumerate(LABELS):
            key = tuple(sorted((left, right), key=LABELS.index))
            expected = EXPECTED_FUSION[key]
            for k, target in enumerate(LABELS):
                coefficient = verlinde(i, j, k)
                expected_value = Qsqrt2(Fraction(expected.get(target, 0)))
                assert_equal(f"Verlinde {left} x {right} -> {target}", coefficient, expected_value)


def check_quantum_dimensions() -> None:
    dimensions = [S[i][0] / S[0][0] for i in range(3)]
    assert_equal("vacuum quantum dimension", dimensions[0], ONE)
    assert_equal("sigma quantum dimension", dimensions[1], SQRT2)
    assert_equal("epsilon quantum dimension", dimensions[2], ONE)
    global_dimension_squared = sum((d * d for d in dimensions), ZERO)
    assert_equal("Ising global dimension squared", global_dimension_squared, Qsqrt2(Fraction(4)))
    assert_equal(
        "Ising conformal-net mu-index from sectors",
        global_dimension_squared,
        Qsqrt2(Fraction(4)),
    )
    assert_equal(
        "Ising global dimension from S00",
        ONE / (S[0][0] * S[0][0]),
        global_dimension_squared,
    )


def check_character_exponents() -> None:
    central_charge = Fraction(1, 2)
    shifted = {
        label: weight - central_charge / 24
        for label, weight in TOP_WEIGHTS.items()
    }
    assert_equal("vacuum shifted exponent", shifted["1"], Fraction(-1, 48))
    assert_equal("sigma shifted exponent", shifted["sigma"], Fraction(1, 24))
    assert_equal("epsilon shifted exponent", shifted["epsilon"], Fraction(23, 48))


def diagonal_qsqrt2_matrix(entries: list[int]) -> list[list[Qsqrt2]]:
    return [
        [
            Qsqrt2(Fraction(entries[row])) if row == column else ZERO
            for column in range(len(entries))
        ]
        for row in range(len(entries))
    ]


def check_ising_t_spin_selection_and_diagonal_invariant() -> None:
    central_charge = Fraction(1, 2)
    shifted = [
        TOP_WEIGHTS[label] - central_charge / 24
        for label in LABELS
    ]

    allowed_by_t = {
        (left, right)
        for left, left_exponent in enumerate(shifted)
        for right, right_exponent in enumerate(shifted)
        if (left_exponent - right_exponent).denominator == 1
    }
    assert_equal(
        "Ising T spin-selection pairs",
        allowed_by_t,
        {(0, 0), (1, 1), (2, 2)},
    )

    # After the T-constraint, M = diag(1,a,b).  The (1,sigma) and
    # (1,epsilon) entries of MS=SM are respectively
    # (1-a) S_{1,sigma}=0 and (1-b) S_{1,epsilon}=0.  The nonzero
    # coefficients below are the exact arithmetic content forcing a=b=1.
    sigma_forcing_coefficient = S[0][1]
    epsilon_forcing_coefficient = S[0][2]
    assert_equal(
        "Ising S coefficient forcing sigma multiplicity",
        sigma_forcing_coefficient,
        Qsqrt2(Fraction(0), Fraction(1, 2)),
    )
    assert_equal(
        "Ising S coefficient forcing epsilon multiplicity",
        epsilon_forcing_coefficient,
        HALF,
    )
    if sigma_forcing_coefficient == ZERO or epsilon_forcing_coefficient == ZERO:
        raise AssertionError("Ising S-constraint does not force diagonal multiplicities")

    identity = diagonal_qsqrt2_matrix([1, 1, 1])
    assert_equal(
        "Ising diagonal invariant commutes with S",
        matrix_multiply(identity, S),
        matrix_multiply(S, identity),
    )


def check_cardy_tauberian_saddle_constants() -> None:
    """Check the Legendre-dual coefficient in the Cardy density formula.

    Suppress the common factor pi^2.  The modular high-temperature coefficient
    is A = c_tot/6.  If S(E)=2 sqrt(A E), the saddle sits at
    E_* = A/beta^2 and gives S(E_*) - beta E_* = A/beta.
    """

    for central_charge in (Fraction(1, 2), Fraction(1), Fraction(24)):
        modular_coefficient = central_charge / 6
        entropy_coefficient_squared = 4 * modular_coefficient
        saddle_energy_coefficient = modular_coefficient
        entropy_at_saddle_coefficient = 2 * modular_coefficient
        boltzmann_at_saddle_coefficient = saddle_energy_coefficient
        assert_equal(
            f"Cardy entropy coefficient squared c={central_charge}",
            entropy_coefficient_squared,
            2 * central_charge / 3,
        )
        assert_equal(
            f"Cardy saddle recovers modular coefficient c={central_charge}",
            entropy_at_saddle_coefficient - boltzmann_at_saddle_coefficient,
            modular_coefficient,
        )


def polynomial_multiply(lhs: list[Fraction], rhs: list[Fraction]) -> list[Fraction]:
    product = [Fraction(0) for _ in range(len(lhs) + len(rhs) - 1)]
    for i, left in enumerate(lhs):
        for j, right in enumerate(rhs):
            product[i + j] += left * right
    return product


def polynomial_eval(coefficients: list[Fraction], x: Fraction) -> Fraction:
    total = Fraction(0)
    power = Fraction(1)
    for coefficient in coefficients:
        total += coefficient * power
        power *= x
    return total


def lagrange_idempotent(root: Fraction, roots: list[Fraction]) -> list[Fraction]:
    coefficients = [Fraction(1)]
    denominator = Fraction(1)
    for other in roots:
        if other == root:
            continue
        coefficients = polynomial_multiply(coefficients, [-other, Fraction(1)])
        denominator *= root - other
    return [coefficient / denominator for coefficient in coefficients]


def check_ising_zhu_polynomial() -> None:
    roots = [TOP_WEIGHTS[label] for label in LABELS]
    polynomial = [Fraction(1)]
    for root in roots:
        polynomial = polynomial_multiply(polynomial, [-root, Fraction(1)])

    expected = [Fraction(0), Fraction(1, 32), Fraction(-9, 16), Fraction(1)]
    assert_equal("Ising Zhu polynomial coefficients", polynomial, expected)
    for label, root in zip(LABELS, roots):
        assert_equal(
            f"Ising Zhu polynomial at {label} top weight",
            polynomial_eval(polynomial, root),
            Fraction(0),
        )

    idempotents = {
        label: lagrange_idempotent(root, roots)
        for label, root in zip(LABELS, roots)
    }
    expected_idempotents = {
        "1": [Fraction(1), Fraction(-18), Fraction(32)],
        "sigma": [Fraction(0), Fraction(128, 7), Fraction(-256, 7)],
        "epsilon": [Fraction(0), Fraction(-2, 7), Fraction(32, 7)],
    }
    assert_equal(
        "Ising Zhu idempotent coefficients",
        idempotents,
        expected_idempotents,
    )
    for left_label, coefficients in idempotents.items():
        for right_label, root in zip(LABELS, roots):
            expected_value = Fraction(1) if left_label == right_label else Fraction(0)
            assert_equal(
                f"Zhu idempotent {left_label} on {right_label}",
                polynomial_eval(coefficients, root),
                expected_value,
            )
        square = polynomial_multiply(coefficients, coefficients)
        for root in roots:
            assert_equal(
                f"Zhu idempotent square at {root}",
                polynomial_eval(square, root),
                polynomial_eval(coefficients, root),
            )

    max_degree = max(len(coefficients) for coefficients in idempotents.values())
    total_idempotent = [Fraction(0) for _ in range(max_degree)]
    for coefficients in idempotents.values():
        for index, coefficient in enumerate(coefficients):
            total_idempotent[index] += coefficient
    assert_equal(
        "sum of Ising Zhu idempotents",
        total_idempotent,
        [Fraction(1), Fraction(0), Fraction(0)],
    )


def main() -> None:
    check_s_squared_identity()
    check_verlinde_fusion()
    check_quantum_dimensions()
    check_character_exponents()
    check_ising_t_spin_selection_and_diagonal_invariant()
    check_cardy_tauberian_saddle_constants()
    check_ising_zhu_polynomial()
    print("All CFT VOA/modular-data, Zhu-algebra, and conformal-net index checks passed.")


if __name__ == "__main__":
    main()
