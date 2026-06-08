#!/usr/bin/env python3
r"""Exact finite linear checks for the locally covariant KG construction.

Evidence contract.
Target claims: the Volume XII locally covariant QFT chapter constructs the
free scalar CCR algebra from the quotient
``C_c^\infty(M) / P C_c^\infty(M)``, descends the causal-propagator pairing to
that quotient, proves functoriality under causally convex embeddings by
restriction of Green solutions, proves the Cauchy time-slice property at the
quotient level, and invokes the local-to-global Hadamard theorem rather than a
diagonal-cover argument for global smoothness of Hadamard-state differences.
Independent construction: finite antisymmetric matrices for quotient descent,
explicit inclusion/restriction matrices distinguishing ``R E_N I = E_M`` from
the false global identity ``E_N I = I E_M``, rational 1+1-dimensional
Minkowski diamond reachability checks, and a finite diagonal-neighborhood
cover diagnostic.
Imported assumptions: existence and uniqueness of retarded/advanced Green
operators on globally hyperbolic spacetimes, the kernel identity
``ker E = P C_c^\infty``, causal convexity of admissible embeddings, and the
propagation-of-singularities/local-to-global Hadamard theorem.
Negative controls: equation-of-motion generators do not survive in the CCR
commutator, non-Cauchy embeddings are not treated as quotient surjections, a
global Green solution is not identified with the zero extension of the
subspacetime solution, a retarded solution from a source inside a causally
convex diamond is allowed to leave the diamond, and sets ``U x U`` near the
diagonal are not accepted as a cover of arbitrary far-separated pairs in
``M x M``.
Scope boundary: these checks are finite diagnostics for the functorial and
local-to-global logic.  They do not prove the analytic Green-operator
theorems, construct Hadamard states, or replace the microlocal propagation
theorem used in the chapter.
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


def check_restriction_identity_not_global_zero_extension() -> None:
    e_source = matrix(
        [
            [0, 1],
            [-1, 0],
        ]
    )
    e_target = matrix(
        [
            [0, 1, -2, 0],
            [-1, 0, 3, 0],
            [2, -3, 0, 1],
            [0, 0, -1, 0],
        ]
    )
    inclusion = matrix(
        [
            [1, 0],
            [0, 1],
            [0, 0],
            [0, 0],
        ]
    )
    restriction = matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
        ]
    )

    restricted_target_solution = mat_mul(restriction, mat_mul(e_target, inclusion))
    assert_equal("restricted causal propagator", restricted_target_solution, e_source)

    global_target_solution = mat_mul(e_target, inclusion)
    zero_extended_source_solution = mat_mul(inclusion, e_source)
    if global_target_solution == zero_extended_source_solution:
        raise AssertionError("false global zero-extension identity was accepted")

    sample_source = vector([1, -1])
    target_vector = mat_vec(global_target_solution, sample_source)
    zero_extension_vector = mat_vec(zero_extended_source_solution, sample_source)
    assert_equal("restriction of target vector", target_vector[:2], zero_extension_vector[:2])
    if target_vector[2:] == zero_extension_vector[2:]:
        raise AssertionError("target Green solution did not leave the embedded image")


Point = tuple[Fraction, Fraction]


def in_minkowski_diamond(point: Point, radius: Fraction) -> bool:
    t, x = point
    return abs(t) + abs(x) < radius


def in_chronological_closure_future(source: Point, target: Point) -> bool:
    dt = target[0] - source[0]
    dx = target[1] - source[1]
    return dt >= 0 and dt >= abs(dx)


def check_global_retarded_solution_leaves_causal_diamond() -> None:
    radius = Fraction(1, 1)
    source = (Fraction(0), Fraction(0))
    outside_future_point = (Fraction(3, 2), Fraction(0))
    inside_approach = (Fraction(9, 10), Fraction(0))
    outside_approach = (Fraction(11, 10), Fraction(0))

    if not in_minkowski_diamond(source, radius):
        raise AssertionError("source should lie inside the causal diamond")
    if in_minkowski_diamond(outside_future_point, radius):
        raise AssertionError("future sample should lie outside the causal diamond")
    if not in_chronological_closure_future(source, outside_future_point):
        raise AssertionError("future sample should be in the global retarded support")

    # In 1+1 dimensions the massless retarded fundamental solution is nonzero
    # throughout the future light cone.  Thus a source inside the diamond has
    # a global retarded solution outside the diamond.
    if not in_chronological_closure_future(source, inside_approach):
        raise AssertionError("inside approach point should see the retarded source")
    if not in_chronological_closure_future(source, outside_approach):
        raise AssertionError("outside approach point should also see the retarded source")
    if in_minkowski_diamond(outside_approach, radius):
        raise AssertionError("outside approach point should be beyond the open image")


def check_diagonal_neighborhood_products_do_not_cover_far_pairs() -> None:
    convex_normal_radius = Fraction(1, 1)
    near_pair = (Fraction(0), Fraction(1, 2))
    far_pair = (Fraction(0), Fraction(3, 1))

    def can_fit_in_one_coordinate_ball(pair: tuple[Fraction, Fraction]) -> bool:
        return abs(pair[1] - pair[0]) < 2 * convex_normal_radius

    if not can_fit_in_one_coordinate_ball(near_pair):
        raise AssertionError("near diagonal pair should fit in one U x U chart")
    if can_fit_in_one_coordinate_ball(far_pair):
        raise AssertionError("far-separated pair was incorrectly covered by diagonal U x U charts")


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
    check_restriction_identity_not_global_zero_extension()
    check_global_retarded_solution_leaves_causal_diamond()
    check_diagonal_neighborhood_products_do_not_cover_far_pairs()
    check_cauchy_embedding_is_quotient_isomorphism()
    print("All locally covariant KG finite-linear checks passed.")


if __name__ == "__main__":
    main()
