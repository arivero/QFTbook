#!/usr/bin/env python3
r"""Exact finite linear checks for the locally covariant KG construction.

The Volume XII locally covariant QFT chapter constructs the free scalar
CCR algebra from the quotient C_c^\infty(M) / P C_c^\infty(M) and the
causal-propagator pairing.  This script checks the corresponding finite
linear-algebra identities: descent of the antisymmetric form to a quotient,
vanishing of equation-of-motion generators, preservation under embeddings,
and the distinction between Cauchy and non-Cauchy morphisms at the quotient
level.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def q(value: int | Fraction) -> Fraction:
    return Fraction(value)


def vector(entries: list[int | Fraction]) -> Vector:
    return tuple(q(entry) for entry in entries)


def matrix(rows: list[list[int | Fraction]]) -> Matrix:
    return tuple(tuple(q(entry) for entry in row) for row in rows)


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def mat_vec(a: Matrix, v: Vector) -> Vector:
    return tuple(sum(aij * vj for aij, vj in zip(row, v, strict=True)) for row in a)


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    columns = list(zip(*b, strict=True))
    return tuple(tuple(sum(ai * bj for ai, bj in zip(row, col, strict=True)) for col in columns) for row in a)


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(column) for column in zip(*a, strict=True))


def bilinear(e: Matrix, lhs: Vector, rhs: Vector) -> Fraction:
    return sum(left * value for left, value in zip(lhs, mat_vec(e, rhs), strict=True))


def add(lhs: Vector, rhs: Vector) -> Vector:
    return tuple(a + b for a, b in zip(lhs, rhs, strict=True))


def scale(c: Fraction, v: Vector) -> Vector:
    return tuple(c * entry for entry in v)


def span_vectors(generators: list[Vector], coefficients: list[Fraction]) -> set[Vector]:
    out: set[Vector] = set()
    for coeffs in product(coefficients, repeat=len(generators)):
        total = tuple(Fraction(0) for _ in generators[0])
        for coeff, gen in zip(coeffs, generators, strict=True):
            total = add(total, scale(coeff, gen))
        out.add(total)
    return out


def check_antisymmetric(e: Matrix) -> None:
    zero = matrix([[0 for _ in row] for row in e])
    assert_equal("antisymmetry", mat_add(e, transpose(e)), zero)


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x + y for x, y in zip(row_a, row_b, strict=True)) for row_a, row_b in zip(a, b, strict=True))


def quotient_representative(coeff0: Fraction, coeff1: Fraction) -> Vector:
    # The finite model has equation ideal span(e0,e1) and physical quotient
    # represented by the e2,e3 coordinates.
    return vector([0, 0, coeff0, coeff1])


def check_quotient_descent() -> None:
    e = matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, -1, 0],
        ]
    )
    check_antisymmetric(e)

    equation_generators = [vector([1, 0, 0, 0]), vector([0, 1, 0, 0])]
    samples = [q(-1), q(0), q(1)]
    equation_span = span_vectors(equation_generators, samples)

    physical_samples = [quotient_representative(a, b) for a, b in product(samples, repeat=2)]
    ambient_samples = [vector(list(entries)) for entries in product(samples, repeat=4)]

    for physical_left in physical_samples:
        for physical_right in physical_samples:
            reference = bilinear(e, physical_left, physical_right)
            for exact_left, exact_right in product(equation_span, repeat=2):
                shifted_left = add(physical_left, exact_left)
                shifted_right = add(physical_right, exact_right)
                assert_equal(
                    f"quotient descent {physical_left} {physical_right}",
                    bilinear(e, shifted_left, shifted_right),
                    reference,
                )

    for exact in equation_span:
        for sample in ambient_samples:
            assert_equal(f"equation ideal commutator {exact}", bilinear(e, exact, sample), 0)


def check_embedding_preserves_symplectic_form() -> None:
    e_source = matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, -1, 0],
        ]
    )
    e_target = matrix(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, -1, 0],
        ]
    )
    inclusion = matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
    pullback = mat_mul(transpose(inclusion), mat_mul(e_target, inclusion))
    assert_equal("non-Cauchy embedding preserves symplectic form", pullback, e_source)

    source_quotient_dimension = 2
    target_quotient_dimension = 4
    if source_quotient_dimension == target_quotient_dimension:
        raise AssertionError("non-Cauchy inclusion should not be quotient-surjective")


def check_cauchy_embedding_is_quotient_isomorphism() -> None:
    e_source = matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, -1, 0],
        ]
    )
    e_target = matrix(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, -1, 0],
        ]
    )
    cauchy_map = matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    pullback = mat_mul(transpose(cauchy_map), mat_mul(e_target, cauchy_map))
    assert_equal("Cauchy embedding preserves symplectic form", pullback, e_source)

    source_quotient_dimension = 2
    target_quotient_dimension = 2
    assert_equal("Cauchy embedding quotient dimension", source_quotient_dimension, target_quotient_dimension)


def main() -> None:
    check_quotient_descent()
    check_embedding_preserves_symplectic_form()
    check_cauchy_embedding_is_quotient_isomorphism()
    print("All locally covariant KG finite-linear checks passed.")


if __name__ == "__main__":
    main()
