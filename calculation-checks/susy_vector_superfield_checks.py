#!/usr/bin/env python3
"""Exact checks for 4D N=1 vector-superfield component conventions.

The check verifies the convention-sensitive bosonic coefficient of
W^alpha W_alpha in Abelian Wess-Zumino gauge.  It uses the monograph
normalization theta^2 = theta^alpha theta_alpha = 2 theta^1 theta^2 and the
mostly-plus sigma-matrix convention sigma^0 = -1, bar sigma^0 = -1,
bar sigma^i = - sigma^i.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


@dataclass(frozen=True)
class Cq:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other):
        other = cq(other)
        return Cq(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Cq(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-cq(other))

    def __rsub__(self, other):
        return cq(other) + (-self)

    def __mul__(self, other):
        other = cq(other)
        return Cq(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = cq(other)
        norm = other.real * other.real + other.imag * other.imag
        if norm == 0:
            raise ZeroDivisionError("division by zero in Cq")
        return Cq(
            (self.real * other.real + self.imag * other.imag) / norm,
            (self.imag * other.real - self.real * other.imag) / norm,
        )


def cq(value) -> Cq:
    if isinstance(value, Cq):
        return value
    return Cq(Fraction(value), Fraction(0))


I = Cq(Fraction(0), Fraction(1))
ZERO = Cq()
ONE = Cq(Fraction(1), Fraction(0))


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


class Form:
    def __init__(self, terms=None):
        self.terms = {
            mask: cq(coeff)
            for mask, coeff in (terms or {}).items()
            if cq(coeff) != ZERO
        }

    @staticmethod
    def scalar(value):
        return Form({0: cq(value)})

    @staticmethod
    def basis(index):
        return Form({1 << index: ONE})

    def __add__(self, other):
        result = dict(self.terms)
        for mask, coeff in other.terms.items():
            result[mask] = result.get(mask, ZERO) + coeff
        return Form(result)

    def __neg__(self):
        return Form({mask: -coeff for mask, coeff in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, value):
        value = cq(value)
        return Form({mask: value * coeff for mask, coeff in self.terms.items()})

    def wedge(self, other):
        result = {}
        for left_mask, left_coeff in self.terms.items():
            for right_mask, right_coeff in other.terms.items():
                if left_mask & right_mask:
                    continue
                inversions = 0
                for left_index in range(2):
                    if not (left_mask & (1 << left_index)):
                        continue
                    for right_index in range(left_index):
                        if right_mask & (1 << right_index):
                            inversions += 1
                sign = -1 if inversions % 2 else 1
                new_mask = left_mask | right_mask
                result[new_mask] = result.get(new_mask, ZERO) + (
                    cq(sign) * left_coeff * right_coeff
                )
        return Form(result)


THETA_UP = [Form.basis(0), Form.basis(1)]
THETA_SQUARE_MASK = 0b11


def theta_lower(index: int) -> Form:
    # epsilon_{12}=1 gives theta_1=theta^2 and theta_2=-theta^1.
    if index == 0:
        return THETA_UP[1]
    if index == 1:
        return THETA_UP[0].scale(-1)
    raise ValueError("spinor index must be 0 or 1")


def raise_lower_spinor_inverse(lower_components: list[Form]) -> list[Form]:
    # Since epsilon^{12}=epsilon_{12}=1, the inverse of lowering is
    # -epsilon^{alpha beta}; this is the sign that is easy to miss.
    return [lower_components[1].scale(-1), lower_components[0]]


def coefficient_of_theta_square(form: Form) -> Cq:
    # theta^2=2 theta^1 theta^2.
    return form.terms.get(THETA_SQUARE_MASK, ZERO) / 2


def matmul(left, right):
    return [
        [
            sum(left[row][k] * right[k][col] for k in range(2))
            for col in range(2)
        ]
        for row in range(2)
    ]


def matsub(left, right):
    return [
        [left[row][col] - right[row][col] for col in range(2)]
        for row in range(2)
    ]


def matscale(value, matrix):
    value = cq(value)
    return [[value * entry for entry in row] for row in matrix]


def pauli_matrices():
    return [
        [[ZERO, ONE], [ONE, ZERO]],
        [[ZERO, -I], [I, ZERO]],
        [[ONE, ZERO], [ZERO, -ONE]],
    ]


PAULI = pauli_matrices()
SIGMA = [[[-ONE, ZERO], [ZERO, -ONE]]] + PAULI
BAR_SIGMA = [[[-ONE, ZERO], [ZERO, -ONE]]] + [
    matscale(-1, matrix) for matrix in PAULI
]


def sigma_munu(mu: int, nu: int):
    return matscale(
        Fraction(1, 4),
        matsub(matmul(SIGMA[mu], BAR_SIGMA[nu]), matmul(SIGMA[nu], BAR_SIGMA[mu])),
    )


SIGMA_MUNU = {
    (mu, nu): sigma_munu(mu, nu)
    for mu in range(4)
    for nu in range(4)
}


FIELD_PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ETA = [-1, 1, 1, 1]


def epsilon4(indices):
    if len(set(indices)) != 4:
        return 0
    inversions = sum(
        1
        for right in range(4)
        for left in range(right)
        if indices[left] > indices[right]
    )
    return -1 if inversions % 2 else 1


def field_component(fields, mu: int, nu: int) -> Fraction:
    if mu == nu:
        return Fraction(0)
    if mu < nu:
        return fields.get((mu, nu), Fraction(0))
    return -fields.get((nu, mu), Fraction(0))


def f_squared(fields) -> Fraction:
    return sum(
        2 * ETA[mu] * ETA[nu] * fields.get((mu, nu), Fraction(0)) ** 2
        for mu, nu in FIELD_PAIRS
    )


def epsilon_ff(fields) -> Fraction:
    total = Fraction(0)
    for mu, nu, rho, sigma in product(range(4), repeat=4):
        total += (
            epsilon4((mu, nu, rho, sigma))
            * field_component(fields, mu, nu)
            * field_component(fields, rho, sigma)
        )
    return total


def w_alpha_linear_bosonic(alpha: int, d_value: Fraction, fields) -> Form:
    result = theta_lower(alpha).scale(d_value)
    # The displayed W_alpha uses Einstein summation over antisymmetric
    # F_{mu nu}.  Summing only mu<nu therefore carries an extra factor of 2.
    for mu, nu in FIELD_PAIRS:
        matrix = SIGMA_MUNU[(mu, nu)]
        for beta in range(2):
            result = result + theta_lower(beta).scale(
                -2 * I * matrix[alpha][beta] * fields.get((mu, nu), Fraction(0))
            )
    return result


def w_square_theta2_bosonic(d_value: Fraction, fields) -> Cq:
    lower = [w_alpha_linear_bosonic(alpha, d_value, fields) for alpha in range(2)]
    upper = raise_lower_spinor_inverse(lower)
    product_form = Form.scalar(0)
    for alpha in range(2):
        product_form = product_form + upper[alpha].wedge(lower[alpha])
    return coefficient_of_theta_square(product_form)


def expected_w_square_theta2_bosonic(d_value: Fraction, fields) -> Cq:
    return cq(d_value * d_value - Fraction(1, 2) * f_squared(fields)) - (
        I * Fraction(1, 4) * epsilon_ff(fields)
    )


def check_spinor_index_inverse_for_theta():
    lowered = [theta_lower(0), theta_lower(1)]
    raised = raise_lower_spinor_inverse(lowered)
    assert_equal(raised[0].terms, THETA_UP[0].terms, "inverse raising recovers theta^1")
    assert_equal(raised[1].terms, THETA_UP[1].terms, "inverse raising recovers theta^2")

    contraction = THETA_UP[0].wedge(theta_lower(0)) + THETA_UP[1].wedge(theta_lower(1))
    assert_equal(
        contraction.terms,
        {THETA_SQUARE_MASK: cq(2)},
        "theta^alpha theta_alpha equals theta^2",
    )


def check_vector_field_strength_theta2_coefficient():
    test_cases = [
        (Fraction(1), {}),
        (Fraction(0), {(0, 1): Fraction(1)}),
        (Fraction(0), {(1, 2): Fraction(1)}),
        (Fraction(0), {(0, 1): Fraction(1), (2, 3): Fraction(1)}),
        (
            Fraction(3, 2),
            {
                (0, 1): Fraction(2, 3),
                (0, 2): Fraction(-3, 5),
                (0, 3): Fraction(5, 7),
                (1, 2): Fraction(-4, 9),
                (1, 3): Fraction(7, 11),
                (2, 3): Fraction(3, 13),
            },
        ),
    ]
    for d_value, fields in test_cases:
        assert_equal(
            w_square_theta2_bosonic(d_value, fields),
            expected_w_square_theta2_bosonic(d_value, fields),
            f"W^alpha W_alpha theta^2 coefficient for D={d_value}, F={fields}",
        )


def check_real_gauge_kinetic_term_after_hc():
    g_squared = Fraction(5, 3)
    d_value = Fraction(-7, 4)
    fields = {
        (0, 1): Fraction(1, 2),
        (0, 2): Fraction(-2, 3),
        (1, 2): Fraction(5, 6),
        (2, 3): Fraction(-3, 7),
    }
    chiral = w_square_theta2_bosonic(d_value, fields)
    plus_hc_real_part = 2 * chiral.real
    lagrangian = Fraction(1, 4) * plus_hc_real_part / g_squared
    expected = (
        Fraction(1, 2) * d_value * d_value / g_squared
        - Fraction(1, 4) * f_squared(fields) / g_squared
    )
    assert_equal(lagrangian, expected, "real gauge kinetic term after adding h.c.")


def main():
    check_spinor_index_inverse_for_theta()
    check_vector_field_strength_theta2_coefficient()
    check_real_gauge_kinetic_term_after_hc()
    print("All supersymmetric vector-superfield component checks passed.")


if __name__ == "__main__":
    main()
