#!/usr/bin/env python3
"""Finite algebra checks for the Liouville level-two BPZ null vector."""

from __future__ import annotations

from fractions import Fraction


class Laurent:
    """Laurent polynomial in t=b^2 with rational coefficients."""

    def __init__(self, terms: dict[int, Fraction] | None = None) -> None:
        self.terms = {
            power: coeff
            for power, coeff in (terms or {}).items()
            if coeff != 0
        }

    @staticmethod
    def constant(value: Fraction | int) -> Laurent:
        return Laurent({0: Fraction(value)})

    @staticmethod
    def monomial(power: int, coeff: Fraction | int = 1) -> Laurent:
        return Laurent({power: Fraction(coeff)})

    def __add__(self, other: Laurent) -> Laurent:
        terms = dict(self.terms)
        for power, coeff in other.terms.items():
            terms[power] = terms.get(power, Fraction(0)) + coeff
        return Laurent(terms)

    def __sub__(self, other: Laurent) -> Laurent:
        return self + (-other)

    def __neg__(self) -> Laurent:
        return Laurent({power: -coeff for power, coeff in self.terms.items()})

    def __mul__(self, other: Laurent) -> Laurent:
        terms: dict[int, Fraction] = {}
        for left_power, left_coeff in self.terms.items():
            for right_power, right_coeff in other.terms.items():
                power = left_power + right_power
                terms[power] = terms.get(power, Fraction(0)) + left_coeff * right_coeff
        return Laurent(terms)

    def scale(self, factor: Fraction | int) -> Laurent:
        return Laurent({power: Fraction(factor) * coeff for power, coeff in self.terms.items()})

    def is_zero(self) -> bool:
        return not self.terms

    def __repr__(self) -> str:
        return f"Laurent({self.terms!r})"


def require_zero(name: str, value: Laurent) -> None:
    if not value.is_zero():
        raise AssertionError(f"{name} is not zero: {value!r}")


one = Laurent.constant(1)
t = Laurent.monomial(1)
t_inverse = Laurent.monomial(-1)

# h(-b/2)=(-b/2)(Q+b/2)=-1/2-3 b^2/4.
h = Laurent.constant(Fraction(-1, 2)) + t.scale(Fraction(-3, 4))

# c=1+6(b+b^{-1})^2=13+6t+6t^{-1}.
c = Laurent.constant(13) + t.scale(6) + t_inverse.scale(6)

kappa = t

# Positive-mode action on (L_-1^2 + kappa L_-2)|h>.
l1_coefficient = h.scale(4) + Laurent.constant(2) + kappa.scale(3)
l2_coefficient = h.scale(6) + kappa * (h.scale(4) + c.scale(Fraction(1, 2)))

require_zero("L1 null-vector coefficient", l1_coefficient)
require_zero("L2 null-vector coefficient", l2_coefficient)

# The L1 equation alone fixes kappa=-(4h+2)/3=b^2.
solved_kappa = -(h.scale(4) + Laurent.constant(2)).scale(Fraction(1, 3))
require_zero("solved kappa minus b^2", solved_kappa - t)

print("All Liouville BPZ null-vector checks passed.")
