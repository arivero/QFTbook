#!/usr/bin/env python3
"""Finite algebra checks for cohomological metric-independence signs.

The checks model the de Rham version of the Q Ward identity used in Volume
VIII, Chapter 1.  Polynomial differential forms on the unit square are enough
to verify the graded Leibniz sign, Q^2=0, Stokes' boundary term, and the
vanishing of a Q-exact deformation when the boundary contribution is zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product


N = 2


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


@dataclass(frozen=True)
class Poly:
    terms: tuple[tuple[tuple[int, int], Fraction], ...]

    @staticmethod
    def monomial(power: tuple[int, int], coeff: Fraction | int = 1) -> "Poly":
        coeff = Fraction(coeff)
        if coeff == 0:
            return Poly(())
        return Poly(((power, coeff),))

    @staticmethod
    def zero() -> "Poly":
        return Poly(())

    @staticmethod
    def one() -> "Poly":
        return Poly.monomial((0, 0), 1)

    def as_dict(self) -> dict[tuple[int, int], Fraction]:
        out: dict[tuple[int, int], Fraction] = {}
        for power, coeff in self.terms:
            out[power] = out.get(power, Fraction(0)) + coeff
        return {power: coeff for power, coeff in out.items() if coeff}

    @staticmethod
    def from_dict(data: dict[tuple[int, int], Fraction]) -> "Poly":
        return Poly(tuple(sorted((power, coeff) for power, coeff in data.items() if coeff)))

    def __add__(self, other: "Poly") -> "Poly":
        data = self.as_dict()
        for power, coeff in other.terms:
            data[power] = data.get(power, Fraction(0)) + coeff
        return Poly.from_dict(data)

    def __neg__(self) -> "Poly":
        return Poly(tuple((power, -coeff) for power, coeff in self.terms))

    def __sub__(self, other: "Poly") -> "Poly":
        return self + (-other)

    def __mul__(self, other: "Poly") -> "Poly":
        data: dict[tuple[int, int], Fraction] = {}
        for (p0, p1), c in self.terms:
            for (q0, q1), d in other.terms:
                power = (p0 + q0, p1 + q1)
                data[power] = data.get(power, Fraction(0)) + c * d
        return Poly.from_dict(data)

    def scale(self, coeff: Fraction | int) -> "Poly":
        coeff = Fraction(coeff)
        return Poly(tuple((power, coeff * value) for power, value in self.terms if coeff * value))

    def derivative(self, variable: int) -> "Poly":
        data: dict[tuple[int, int], Fraction] = {}
        for power, coeff in self.terms:
            exponent = power[variable]
            if exponent == 0:
                continue
            new_power = list(power)
            new_power[variable] -= 1
            new_power_tuple = (new_power[0], new_power[1])
            data[new_power_tuple] = data.get(new_power_tuple, Fraction(0)) + coeff * exponent
        return Poly.from_dict(data)

    def restrict(self, variable: int, value: int) -> "Poly":
        data: dict[tuple[int, int], Fraction] = {}
        for power, coeff in self.terms:
            factor = Fraction(value) ** power[variable]
            new_power = list(power)
            new_power[variable] = 0
            new_power_tuple = (new_power[0], new_power[1])
            data[new_power_tuple] = data.get(new_power_tuple, Fraction(0)) + coeff * factor
        return Poly.from_dict(data)

    def integrate_unit_interval(self, variable: int) -> "Poly":
        data: dict[tuple[int, int], Fraction] = {}
        for power, coeff in self.terms:
            exponent = power[variable]
            new_power = list(power)
            new_power[variable] = 0
            new_power_tuple = (new_power[0], new_power[1])
            data[new_power_tuple] = data.get(new_power_tuple, Fraction(0)) + coeff / (exponent + 1)
        return Poly.from_dict(data)

    def integrate_square(self) -> Fraction:
        value = Fraction(0)
        for (p0, p1), coeff in self.terms:
            value += coeff / ((p0 + 1) * (p1 + 1))
        return value


@dataclass(frozen=True)
class Form:
    terms: tuple[tuple[int, Poly], ...]

    @staticmethod
    def zero() -> "Form":
        return Form(())

    @staticmethod
    def from_dict(data: dict[int, Poly]) -> "Form":
        return Form(tuple(sorted((mask, poly) for mask, poly in data.items() if poly.terms)))

    @staticmethod
    def basis(mask: int, poly: Poly) -> "Form":
        return Form.from_dict({mask: poly})

    def as_dict(self) -> dict[int, Poly]:
        out: dict[int, Poly] = {}
        for mask, poly in self.terms:
            out[mask] = out.get(mask, Poly.zero()) + poly
        return {mask: poly for mask, poly in out.items() if poly.terms}

    def __add__(self, other: "Form") -> "Form":
        data = self.as_dict()
        for mask, poly in other.terms:
            data[mask] = data.get(mask, Poly.zero()) + poly
        return Form.from_dict(data)

    def __neg__(self) -> "Form":
        return Form(tuple((mask, poly.scale(-1)) for mask, poly in self.terms))

    def __sub__(self, other: "Form") -> "Form":
        return self + (-other)

    def scale(self, coeff: Fraction | int) -> "Form":
        return Form(tuple((mask, poly.scale(coeff)) for mask, poly in self.terms))

    def degree(self) -> int:
        degrees = {mask.bit_count() for mask, _ in self.terms}
        if len(degrees) != 1:
            raise ValueError("form is not homogeneous")
        return next(iter(degrees))


def wedge_sign(left: int, right: int) -> int:
    inversions = 0
    for i in range(N):
        if left & (1 << i):
            for j in range(i):
                if right & (1 << j):
                    inversions += 1
    return -1 if inversions % 2 else 1


def wedge(left: Form, right: Form) -> Form:
    data: dict[int, Poly] = {}
    for left_mask, left_poly in left.terms:
        for right_mask, right_poly in right.terms:
            if left_mask & right_mask:
                continue
            mask = left_mask | right_mask
            poly = (left_poly * right_poly).scale(wedge_sign(left_mask, right_mask))
            data[mask] = data.get(mask, Poly.zero()) + poly
    return Form.from_dict(data)


def exterior_d(form: Form) -> Form:
    data: dict[int, Poly] = {}
    for mask, poly in form.terms:
        for variable in range(N):
            if mask & (1 << variable):
                continue
            dx = Form.basis(1 << variable, Poly.one())
            term = wedge(dx, Form.basis(mask, poly.derivative(variable)))
            for term_mask, term_poly in term.terms:
                data[term_mask] = data.get(term_mask, Poly.zero()) + term_poly
    return Form.from_dict(data)


def integrate_top_square(form: Form) -> Fraction:
    data = form.as_dict()
    return data.get(0b11, Poly.zero()).integrate_square()


def boundary_integral_square(one_form: Form) -> Fraction:
    data = one_form.as_dict()
    p_dx = data.get(0b01, Poly.zero())
    q_dy = data.get(0b10, Poly.zero())
    bottom = p_dx.restrict(1, 0).integrate_unit_interval(0).as_dict().get((0, 0), Fraction(0))
    right = q_dy.restrict(0, 1).integrate_unit_interval(1).as_dict().get((0, 0), Fraction(0))
    top = -p_dx.restrict(1, 1).integrate_unit_interval(0).as_dict().get((0, 0), Fraction(0))
    left = -q_dy.restrict(0, 0).integrate_unit_interval(1).as_dict().get((0, 0), Fraction(0))
    return bottom + right + top + left


def check_q_squared_zero() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    sample = (
        Form.basis(0, x * x + y)
        + Form.basis(0b01, x * y)
        + Form.basis(0b10, x + y * y)
    )
    assert_equal("d^2=0", exterior_d(exterior_d(sample)), Form.zero())


def check_graded_leibniz() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    alpha = Form.basis(0b01, x + y)
    beta = Form.basis(0b10, x * y + Poly.one())
    lhs = exterior_d(wedge(alpha, beta))
    rhs = wedge(exterior_d(alpha), beta) + wedge(alpha, exterior_d(beta)).scale((-1) ** alpha.degree())
    assert_equal("graded Leibniz sign", lhs, rhs)


def check_stokes_boundary_term() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    eta = Form.basis(0b01, x * x * y + y) + Form.basis(0b10, x * y * y - x)
    assert_equal("Stokes on unit square", integrate_top_square(exterior_d(eta)), boundary_integral_square(eta))


def check_q_exact_deformation_without_boundary_term() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    bump = x * (Poly.one() - x) * y * (Poly.one() - y)
    v = Form.basis(0b01, bump) + Form.basis(0b10, bump)
    dv = exterior_d(v)
    assert_equal("Q-exact deformation boundary term", boundary_integral_square(v), Fraction(0))
    assert_equal("Q-exact deformation top integral", integrate_top_square(dv), Fraction(0))
    for t in [Fraction(0), Fraction(1), Fraction(7, 3)]:
        # In two dimensions exp(-t dV) has top component -t dV.
        top_component = integrate_top_square(dv.scale(-t))
        assert_equal(f"Q-exact deformation independence t={t}", top_component, Fraction(0))


def main() -> None:
    check_q_squared_zero()
    check_graded_leibniz()
    check_stokes_boundary_term()
    check_q_exact_deformation_without_boundary_term()
    print("All cohomological metric-independence and descent checks passed.")


if __name__ == "__main__":
    main()
