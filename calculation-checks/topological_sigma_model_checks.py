#!/usr/bin/env python3
"""Exact checks for the topological sigma-model chapter.

These checks are intentionally finite-dimensional.  They verify algebraic
and pointwise identities used in the chapter without importing numerical
floating-point approximations.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def assert_equal(actual, expected, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


def dot(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> Fraction:
    return u[0] * v[0] + u[1] * v[1]


def j_target(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (-v[1], v[0])


def add(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (u[0] + v[0], u[1] + v[1])


def omega(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> Fraction:
    return u[0] * v[1] - u[1] * v[0]


def check_energy_identity() -> None:
    samples = [
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))),
        ((Fraction(2), Fraction(3)), (Fraction(5), Fraction(-7))),
        ((Fraction(-1), Fraction(4)), (Fraction(6), Fraction(2))),
        ((Fraction(3, 2), Fraction(-5, 3)), (Fraction(7, 4), Fraction(1, 5))),
    ]
    for u, v in samples:
        energy = Fraction(1, 2) * (dot(u, u) + dot(v, v))
        dbar_norm = Fraction(1, 2) * dot(add(u, j_target(v)), add(u, j_target(v)))
        assert_equal(energy, omega(u, v) + dbar_norm, "A-model pointwise energy identity")


class QuantumProjectiveSpace:
    """Small quantum cohomology of CP^m with H^(m+1)=q."""

    def __init__(self, m: int) -> None:
        if m < 1:
            raise ValueError("m must be positive")
        self.m = m

    def basis(self, power: int) -> dict[tuple[int, int], Fraction]:
        return {(0, power): Fraction(1)}

    def reduce_monomial(self, q_power: int, h_power: int) -> tuple[int, int]:
        extra_q, reduced_h = divmod(h_power, self.m + 1)
        return (q_power + extra_q, reduced_h)

    def multiply(
        self,
        left: dict[tuple[int, int], Fraction],
        right: dict[tuple[int, int], Fraction],
    ) -> dict[tuple[int, int], Fraction]:
        out: dict[tuple[int, int], Fraction] = {}
        for (q1, h1), c1 in left.items():
            for (q2, h2), c2 in right.items():
                key = self.reduce_monomial(q1 + q2, h1 + h2)
                out[key] = out.get(key, Fraction(0)) + c1 * c2
        return {key: value for key, value in out.items() if value}

    def pair(
        self,
        left: dict[tuple[int, int], Fraction],
        right: dict[tuple[int, int], Fraction],
    ) -> dict[int, Fraction]:
        """Return the q-polynomial P(q) = int_CP^m left*right."""
        out: dict[int, Fraction] = {}
        for (q1, h1), c1 in left.items():
            for (q2, h2), c2 in right.items():
                q_power, h_power = self.reduce_monomial(q1 + q2, h1 + h2)
                if h_power == self.m:
                    out[q_power] = out.get(q_power, Fraction(0)) + c1 * c2
        return {key: value for key, value in out.items() if value}

    def power_of_h(self, exponent: int) -> dict[tuple[int, int], Fraction]:
        result = {(0, 0): Fraction(1)}
        h = self.basis(1)
        for _ in range(exponent):
            result = self.multiply(result, h)
        return result


def check_quantum_projective_space() -> None:
    for m in (1, 2, 3, 4):
        qh = QuantumProjectiveSpace(m)
        relation = qh.power_of_h(m + 1)
        assert_equal(relation, {(1, 0): Fraction(1)}, f"CP^{m} quantum relation H^(m+1)=q")

        for a, b, c in product(range(m + 1), repeat=3):
            left = qh.multiply(qh.multiply(qh.basis(a), qh.basis(b)), qh.basis(c))
            right = qh.multiply(qh.basis(a), qh.multiply(qh.basis(b), qh.basis(c)))
            assert_equal(left, right, f"CP^{m} associativity for H^{a},H^{b},H^{c}")

        for a, b, c in product(range(m + 1), repeat=3):
            three_point = qh.pair(qh.multiply(qh.basis(a), qh.basis(b)), qh.basis(c))
            for q_degree, coefficient in three_point.items():
                assert_equal(coefficient, Fraction(1), "projective-space three-point coefficient")
                assert_equal(
                    a + b + c,
                    m + (m + 1) * q_degree,
                    f"CP^{m} degree selection for <H^{a},H^{b},H^{c}>",
                )


def check_projective_degree_one_instanton_ledger() -> None:
    for m in range(1, 7):
        qh = QuantumProjectiveSpace(m)
        line_moduli_dimension = 2 * m - 2
        marked_point_dimension = 3
        degree_one_three_mark_dimension = line_moduli_dimension + marked_point_dimension
        assert_equal(
            degree_one_three_mark_dimension,
            2 * m + 1,
            f"CP^{m} degree-one line plus three marked points dimension",
        )
        assert_equal(
            degree_one_three_mark_dimension,
            m + (m + 1),
            f"CP^{m} expected dimension of Mbar_0,3(P^m,1)",
        )

        for a, b, c in product(range(m + 1), repeat=3):
            three_point = qh.pair(qh.multiply(qh.basis(a), qh.basis(b)), qh.basis(c))
            degree_one_coefficient = three_point.get(1, Fraction(0))
            expected = Fraction(1) if a + b + c == 2 * m + 1 else Fraction(0)
            assert_equal(
                degree_one_coefficient,
                expected,
                f"CP^{m} degree-one invariant selection for ({a},{b},{c})",
            )

        for a, b in product(range(m + 1), repeat=2):
            if a + b == m + 1:
                assert_equal(
                    qh.multiply(qh.basis(a), qh.basis(b)),
                    {(1, 0): Fraction(1)},
                    f"CP^{m} product H^{a}*H^{b}=q when powers sum to m+1",
                )


def check_virtual_dimension_formula() -> None:
    for m, genus, marks, degree in product(range(1, 6), range(0, 4), range(0, 7), range(0, 5)):
        fixed_index = 2 * (m * (1 - genus) + (m + 1) * degree)
        stable_dimension = 2 * ((1 - genus) * (m - 3) + marks + (m + 1) * degree)
        curve_moduli_dimension = 6 * genus - 6 + 2 * marks
        assert_equal(
            stable_dimension,
            fixed_index + curve_moduli_dimension,
            "stable-map dimension equals fixed-domain index plus curve moduli dimension",
        )


def check_b_model_degree_condition() -> None:
    m = 3
    good_polyvector_degrees = (1, 1, 1)
    good_dolbeault_degrees = (0, 1, 2)
    assert_equal(sum(good_polyvector_degrees), m, "B-model total polyvector degree")
    assert_equal(sum(good_dolbeault_degrees), m, "B-model total Dolbeault degree")

    bad_polyvector_degrees = (2, 1, 1)
    bad_dolbeault_degrees = (0, 1, 1)
    assert sum(bad_polyvector_degrees) != m
    assert sum(bad_dolbeault_degrees) != m


def main() -> None:
    check_energy_identity()
    check_quantum_projective_space()
    check_projective_degree_one_instanton_ledger()
    check_virtual_dimension_formula()
    check_b_model_degree_condition()
    print("All topological sigma-model checks passed.")


if __name__ == "__main__":
    main()
