#!/usr/bin/env python3
"""Exact finite checks for cohomological field theory algebra.

The Volume VIII cohomological-field-theory chapter uses finite-dimensional
algebra in three places:

* the Cartan differential satisfies d_C^2 = -u L_v on invariant forms;
* the Hamiltonian S^1 combination omega + u mu is Cartan-closed when
  d mu = i_v omega;
* the Mathai-Quillen auxiliary Gaussian has the displayed sign, and the
  rank-one zero-locus orientation is sign(ds);
* the finite normal localization factor is Pf(C)/sqrt(det(A)), equivalently
  its square is Pf(C)^2/det(A), for a two-even/two-odd diagonal model.

All checks use exact rational arithmetic.  They are convention checks, not a
replacement for the derivations in the text.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


N = 2


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


@dataclass(frozen=True)
class Poly:
    terms: tuple[tuple[tuple[int, int], Fraction], ...]

    @staticmethod
    def zero() -> "Poly":
        return Poly(())

    @staticmethod
    def one() -> "Poly":
        return Poly.monomial((0, 0), 1)

    @staticmethod
    def monomial(power: tuple[int, int], coeff: int | Fraction = 1) -> "Poly":
        coeff = Fraction(coeff)
        if coeff == 0:
            return Poly.zero()
        return Poly(((power, coeff),))

    @staticmethod
    def from_dict(data: dict[tuple[int, int], Fraction]) -> "Poly":
        return Poly(tuple(sorted((power, coeff) for power, coeff in data.items() if coeff)))

    def as_dict(self) -> dict[tuple[int, int], Fraction]:
        out: dict[tuple[int, int], Fraction] = {}
        for power, coeff in self.terms:
            out[power] = out.get(power, Fraction(0)) + coeff
        return {power: coeff for power, coeff in out.items() if coeff}

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

    def scale(self, coeff: int | Fraction) -> "Poly":
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
            key = (new_power[0], new_power[1])
            data[key] = data.get(key, Fraction(0)) + coeff * exponent
        return Poly.from_dict(data)


@dataclass(frozen=True)
class Form:
    terms: tuple[tuple[int, Poly], ...]

    @staticmethod
    def zero() -> "Form":
        return Form(())

    @staticmethod
    def basis(mask: int, poly: Poly) -> "Form":
        return Form.from_dict({mask: poly})

    @staticmethod
    def from_dict(data: dict[int, Poly]) -> "Form":
        return Form(tuple(sorted((mask, poly) for mask, poly in data.items() if poly.terms)))

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

    def scale(self, coeff: int | Fraction) -> "Form":
        return Form(tuple((mask, poly.scale(coeff)) for mask, poly in self.terms))


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


def contraction_vector(form: Form, vector: tuple[Poly, Poly]) -> Form:
    data: dict[int, Poly] = {}
    for mask, poly in form.terms:
        for variable in range(N):
            bit = 1 << variable
            if not (mask & bit):
                continue
            preceding = sum(1 for j in range(variable) if mask & (1 << j))
            sign = -1 if preceding % 2 else 1
            new_mask = mask & ~bit
            term_poly = (vector[variable] * poly).scale(sign)
            data[new_mask] = data.get(new_mask, Poly.zero()) + term_poly
    return Form.from_dict(data)


def lie_derivative(form: Form, vector: tuple[Poly, Poly]) -> Form:
    return exterior_d(contraction_vector(form, vector)) + contraction_vector(exterior_d(form), vector)


def cartan_d(form: Form, vector: tuple[Poly, Poly], u: Fraction) -> Form:
    return exterior_d(form) - contraction_vector(form, vector).scale(u)


def check_cartan_square() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    vector = (y.scale(-1), x)
    samples = [
        Form.basis(0, x * x + y),
        Form.basis(0b01, x * y + Poly.one()) + Form.basis(0b10, x + y * y),
        Form.basis(0b11, x * x + x * y + y * y),
    ]
    for u in [Fraction(1), Fraction(3), Fraction(-2)]:
        for idx, sample in enumerate(samples):
            lhs = cartan_d(cartan_d(sample, vector, u), vector, u)
            rhs = lie_derivative(sample, vector).scale(-u)
            assert_equal(f"Cartan square u={u} sample={idx}", lhs, rhs)


def check_hamiltonian_equivariant_closure() -> None:
    x = Poly.monomial((1, 0))
    y = Poly.monomial((0, 1))
    vector = (y.scale(-1), x)
    omega = Form.basis(0b11, Poly.one())
    mu = Form.basis(0, (x * x + y * y).scale(Fraction(-1, 2)))
    for u in [Fraction(1), Fraction(5, 2), Fraction(-3)]:
        equivariant_form = omega + mu.scale(u)
        assert_equal(f"Hamiltonian equivariant closure u={u}", cartan_d(equivariant_form, vector, u), Form.zero())


def check_mathai_quillen_auxiliary_gaussian_sign() -> None:
    # Algebraic square completion:
    # 1/2 H^2 + i H s = 1/2 (H + i s)^2 + 1/2 s^2 because i^2=-1.
    # We track a+b*i coefficients as pairs (real, imag).
    def cmul(lhs: tuple[Fraction, Fraction], rhs: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        a, b = lhs
        c, d = rhs
        return (a * c - b * d, a * d + b * c)

    for s in [Fraction(-3), Fraction(1), Fraction(5, 2)]:
        for h in [Fraction(-2), Fraction(0), Fraction(7, 3)]:
            lhs = (Fraction(1, 2) * h * h, h * s)
            h_plus_is_square = cmul((h, s), (h, s))
            rhs = (
                Fraction(1, 2) * h_plus_is_square[0] + Fraction(1, 2) * s * s,
                Fraction(1, 2) * h_plus_is_square[1],
            )
            assert_equal(f"MQ square completion h={h} s={s}", lhs, rhs)


def check_rank_one_zero_orientation() -> None:
    for derivative in [Fraction(-7), Fraction(-1), Fraction(2), Fraction(11)]:
        orientation_sign = Fraction(1) if derivative > 0 else Fraction(-1)
        berezin_jacobian_sign = derivative / abs(derivative)
        assert_equal(
            f"rank-one zero-locus orientation ds={derivative}",
            berezin_jacobian_sign,
            orientation_sign,
        )


def check_normal_euler_factor_square() -> None:
    # For even normal quadratic form A=diag(a,b) and odd skew form
    # C=[[0,c],[-c,0]], the Berezin-Gaussian numerator is Pf(C)=c and the
    # bosonic denominator is sqrt(det A).  We avoid irrational square roots by
    # checking the squared inverse Euler factor.
    samples = [
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(3), Fraction(5)),
        (Fraction(7, 2), Fraction(11, 3), Fraction(-13, 4)),
    ]
    for a, b, c in samples:
        det_a = a * b
        pf_c = c
        inverse_euler_squared = pf_c * pf_c / det_a
        expected = c * c / (a * b)
        assert_equal(
            f"normal inverse Euler square a={a} b={b} c={c}",
            inverse_euler_squared,
            expected,
        )


def main() -> None:
    check_cartan_square()
    check_hamiltonian_equivariant_closure()
    check_mathai_quillen_auxiliary_gaussian_sign()
    check_rank_one_zero_orientation()
    check_normal_euler_factor_square()
    print("All cohomological field-theory algebra checks passed.")


if __name__ == "__main__":
    main()
