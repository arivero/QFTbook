#!/usr/bin/env python3
"""Exact checks for 4D N=1 superfield differential operators.

This script is an independent Python companion to the Mathematica-style
superspace notebooks in the stringbook.  It represents superfields as finite
Grassmann polynomials with formal x-jets and checks the operator algebra
directly, rather than relying on component ansatz substitutions.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


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


def cq(value) -> Cq:
    if isinstance(value, Cq):
        return value
    return Cq(Fraction(value), Fraction(0))


ZERO = Cq()
ONE = Cq(Fraction(1), Fraction(0))
I = Cq(Fraction(0), Fraction(1))
CONST = ("const",)


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


class Expr:
    """Linear expressions in formal x-jets tensored with four odd variables."""

    def __init__(self, terms=None):
        self.terms = {
            (label, mask): cq(coeff)
            for (label, mask), coeff in (terms or {}).items()
            if cq(coeff) != ZERO
        }

    @staticmethod
    def zero():
        return Expr()

    @staticmethod
    def scalar(value):
        return Expr({(CONST, 0): cq(value)})

    @staticmethod
    def coeff(label):
        return Expr({(label, 0): ONE})

    @staticmethod
    def odd(index):
        return Expr({(CONST, 1 << index): ONE})

    def __add__(self, other):
        result = dict(self.terms)
        for key, coeff in other.terms.items():
            result[key] = result.get(key, ZERO) + coeff
        return Expr(result)

    def __radd__(self, other):
        if other == 0:
            return self
        return Expr.scalar(other) + self

    def __neg__(self):
        return Expr({key: -coeff for key, coeff in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, value):
        value = cq(value)
        return Expr({key: value * coeff for key, coeff in self.terms.items()})

    def left_mul_odd(self, index):
        bit = 1 << index
        result = {}
        for (label, mask), coeff in self.terms.items():
            if mask & bit:
                continue
            lower_bits = mask & (bit - 1)
            sign = -1 if lower_bits.bit_count() % 2 else 1
            key = (label, mask | bit)
            result[key] = result.get(key, ZERO) + cq(sign) * coeff
        return Expr(result)

    def left_derivative_odd(self, index):
        bit = 1 << index
        result = {}
        for (label, mask), coeff in self.terms.items():
            if not (mask & bit):
                continue
            lower_bits = mask & (bit - 1)
            sign = -1 if lower_bits.bit_count() % 2 else 1
            key = (label, mask ^ bit)
            result[key] = result.get(key, ZERO) + cq(sign) * coeff
        return Expr(result)

    def partial_x(self, mu):
        result = {}
        for (label, mask), coeff in self.terms.items():
            for new_label, factor in partial_label(label, mu):
                key = (new_label, mask)
                result[key] = result.get(key, ZERO) + factor * coeff
        return Expr(result)

    def __eq__(self, other):
        return self.terms == other.terms

    def __repr__(self):
        return f"Expr({self.terms!r})"


def partial_label(label, mu):
    if label == CONST:
        return []
    if label[0] == "x":
        return [(CONST, ONE)] if label[1] == mu else []
    if label[0] == "jet":
        name, multiindex = label[1], label[2]
        shifted = list(multiindex)
        shifted[mu] += 1
        return [(("jet", name, tuple(shifted)), ONE)]
    raise ValueError(f"unknown coefficient label: {label!r}")


def pauli_matrices():
    return [
        [[ZERO, ONE], [ONE, ZERO]],
        [[ZERO, -I], [I, ZERO]],
        [[ONE, ZERO], [ZERO, -ONE]],
    ]


PAULI = pauli_matrices()
SIGMA = [[[-ONE, ZERO], [ZERO, -ONE]]] + PAULI


def theta(alpha):
    return Expr.odd(alpha)


def theta_bar(dot):
    return Expr.odd(2 + dot)


def left_multiply(left, right):
    result = Expr.zero()
    for (label, mask), coeff in left.terms.items():
        if label != CONST:
            raise ValueError("left factor must have scalar coefficient")
        term = right
        for index in range(4):
            if mask & (1 << index):
                term = term.left_mul_odd(index)
        result = result + term.scale(coeff)
    return result


def theta_sigma_thetabar(mu):
    total = Expr.zero()
    for alpha in range(2):
        for dot in range(2):
            monomial = left_multiply(theta(alpha), theta_bar(dot))
            total = total + monomial.scale(SIGMA[mu][alpha][dot])
    return total


def y(mu):
    return Expr.coeff(("x", mu)) + theta_sigma_thetabar(mu).scale(I)


def ybar(mu):
    return Expr.coeff(("x", mu)) - theta_sigma_thetabar(mu).scale(I)


def q(alpha, expr):
    total = expr.left_derivative_odd(alpha)
    for mu in range(4):
        for dot in range(2):
            total = total + expr.partial_x(mu).left_mul_odd(2 + dot).scale(
                -I * SIGMA[mu][alpha][dot]
            )
    return total


def qbar(dot, expr):
    total = -expr.left_derivative_odd(2 + dot)
    for mu in range(4):
        for alpha in range(2):
            total = total + expr.partial_x(mu).left_mul_odd(alpha).scale(
                I * SIGMA[mu][alpha][dot]
            )
    return total


def d(alpha, expr):
    total = expr.left_derivative_odd(alpha)
    for mu in range(4):
        for dot in range(2):
            total = total + expr.partial_x(mu).left_mul_odd(2 + dot).scale(
                I * SIGMA[mu][alpha][dot]
            )
    return total


def dbar(dot, expr):
    total = -expr.left_derivative_odd(2 + dot)
    for mu in range(4):
        for alpha in range(2):
            total = total + expr.partial_x(mu).left_mul_odd(alpha).scale(
                -I * SIGMA[mu][alpha][dot]
            )
    return total


def generic_even_superfield():
    # The coefficient labels are independent formal x-jets.  Including all
    # sixteen odd monomials catches the Koszul signs in the operator algebra.
    terms = {}
    for mask in range(16):
        label = ("jet", f"f_{mask}", (0, 0, 0, 0))
        terms[(label, mask)] = ONE
    return Expr(terms)


def spacetime_derivative_rhs(expr, alpha, dot, factor):
    total = Expr.zero()
    for mu in range(4):
        total = total + expr.partial_x(mu).scale(factor * SIGMA[mu][alpha][dot])
    return total


def check_left_derivative_product_sign():
    product = left_multiply(theta(0), theta_bar(1))
    assert_equal(
        product.left_derivative_odd(3),
        -theta(0),
        "left derivative of theta theta_bar carries Koszul sign",
    )


def check_chiral_and_antichiral_coordinates():
    for mu in range(4):
        for dot in range(2):
            assert_equal(dbar(dot, y(mu)), Expr.zero(), f"Dbar_{dot} y^{mu}=0")
        for alpha in range(2):
            assert_equal(d(alpha, ybar(mu)), Expr.zero(), f"D_{alpha} ybar^{mu}=0")

    for alpha in range(2):
        for dot in range(2):
            assert_equal(dbar(dot, theta(alpha)), Expr.zero(), "Dbar theta=0")
            assert_equal(d(alpha, theta_bar(dot)), Expr.zero(), "D theta_bar=0")


def check_supertranslation_and_covariant_derivative_algebras():
    field = generic_even_superfield()

    for alpha in range(2):
        for beta in range(2):
            assert_equal(
                q(alpha, q(beta, field)) + q(beta, q(alpha, field)),
                Expr.zero(),
                f"{{Q_{alpha},Q_{beta}}}=0",
            )
            assert_equal(
                d(alpha, d(beta, field)) + d(beta, d(alpha, field)),
                Expr.zero(),
                f"{{D_{alpha},D_{beta}}}=0",
            )

    for dot in range(2):
        for edot in range(2):
            assert_equal(
                qbar(dot, qbar(edot, field)) + qbar(edot, qbar(dot, field)),
                Expr.zero(),
                f"{{Qbar_{dot},Qbar_{edot}}}=0",
            )
            assert_equal(
                dbar(dot, dbar(edot, field)) + dbar(edot, dbar(dot, field)),
                Expr.zero(),
                f"{{Dbar_{dot},Dbar_{edot}}}=0",
            )

    for alpha in range(2):
        for dot in range(2):
            assert_equal(
                q(alpha, qbar(dot, field)) + qbar(dot, q(alpha, field)),
                spacetime_derivative_rhs(field, alpha, dot, 2 * I),
                f"{{Q_{alpha},Qbar_{dot}}}=2 i sigma partial",
            )
            assert_equal(
                d(alpha, dbar(dot, field)) + dbar(dot, d(alpha, field)),
                spacetime_derivative_rhs(field, alpha, dot, -2 * I),
                f"{{D_{alpha},Dbar_{dot}}}=-2 i sigma partial",
            )

    for alpha in range(2):
        for beta in range(2):
            assert_equal(
                q(alpha, d(beta, field)) + d(beta, q(alpha, field)),
                Expr.zero(),
                f"{{Q_{alpha},D_{beta}}}=0",
            )
    for dot in range(2):
        for edot in range(2):
            assert_equal(
                qbar(dot, dbar(edot, field)) + dbar(edot, qbar(dot, field)),
                Expr.zero(),
                f"{{Qbar_{dot},Dbar_{edot}}}=0",
            )
    for alpha in range(2):
        for dot in range(2):
            assert_equal(
                q(alpha, dbar(dot, field)) + dbar(dot, q(alpha, field)),
                Expr.zero(),
                f"{{Q_{alpha},Dbar_{dot}}}=0",
            )
            assert_equal(
                qbar(dot, d(alpha, field)) + d(alpha, qbar(dot, field)),
                Expr.zero(),
                f"{{Qbar_{dot},D_{alpha}}}=0",
            )


def main():
    check_left_derivative_product_sign()
    check_chiral_and_antichiral_coordinates()
    check_supertranslation_and_covariant_derivative_algebras()
    print("All superfield operator-algebra checks passed.")


if __name__ == "__main__":
    main()
