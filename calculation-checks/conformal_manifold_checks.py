#!/usr/bin/env python3
"""Finite checks for conformal-manifold source-coordinate conventions.

The manuscript derivation is analytic and distributional.  This companion
checks only the finite linear algebra used for rank counts, quotient metrics,
and coordinate transformations of the Zamolodchikov metric.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: {lhs!r} != {rhs!r}")


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return []
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def rank(matrix: Matrix) -> int:
    data = [row[:] for row in matrix]
    if not data:
        return 0
    rows = len(data)
    cols = len(data[0])
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if data[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        pivot_value = data[pivot_row][col]
        data[pivot_row] = [entry / pivot_value for entry in data[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = data[row][col]
            if factor != 0:
                data[row] = [
                    data[row][j] - factor * data[pivot_row][j]
                    for j in range(cols)
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def dimension_count(
    source_dimension: int,
    beta_jacobian: Matrix,
    redundancy_generators: Matrix,
) -> int:
    return source_dimension - rank(beta_jacobian) - rank(redundancy_generators)


def quadratic_form(matrix: Matrix, vector: list[Fraction]) -> Fraction:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def check_source_coordinate_rank_counts() -> None:
    # Klebanov-Witten local chart: three holomorphic source coordinates and
    # one independent beta-function constraint in the symmetry-preserving
    # source-coordinate system.
    n = Fraction(5)
    kw_beta = [[n, n, Fraction(1)]]
    assert_equal("KW rank-one beta map", rank(kw_beta), 1)
    assert_equal("KW conformal locus dimension", dimension_count(3, kw_beta, []), 2)

    # N=4 Yang-Mills: the local tau coordinate is unobstructed before global
    # electric-magnetic identifications.
    assert_equal("N=4 local tau dimension", dimension_count(1, [], []), 1)

    # Standard ABJM at fixed integer (N,k): the standard N=6 datum has no
    # continuous tangent coordinate once the quantized level and fixed
    # superpotential coefficient are treated as part of the QFT specification.
    assert_equal("standard ABJM fixed-datum dimension", dimension_count(0, [], []), 0)

    # A generic source-coordinate system with an independent redundancy vector has the
    # expected quotient dimension only when the redundancy is tangent to the
    # beta-zero locus.  The finite check records the linear algebra after that
    # hypothesis has been verified.
    beta = [[Fraction(1), Fraction(1), Fraction(0), Fraction(0)]]
    redundant = [[Fraction(0), Fraction(0), Fraction(1), Fraction(0)]]
    assert_equal("one constraint one redundancy", dimension_count(4, beta, redundant), 2)


def check_zamolodchikov_metric_transform() -> None:
    metric = [
        [Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(3)],
    ]
    jacobian = [
        [Fraction(1), Fraction(2)],
        [Fraction(0), Fraction(1)],
    ]
    transformed = matmul(transpose(jacobian), matmul(metric, jacobian))
    expected = [
        [Fraction(2), Fraction(5)],
        [Fraction(5), Fraction(15)],
    ]
    assert_equal("Zamolodchikov metric coordinate transform", transformed, expected)

    for vector in ([Fraction(1), Fraction(0)], [Fraction(2), Fraction(-1)]):
        image = [
            sum(jacobian[i][j] * vector[j] for j in range(2))
            for i in range(2)
        ]
        assert_equal(
            f"quadratic form tensoriality {vector}",
            quadratic_form(transformed, vector),
            quadratic_form(metric, image),
        )


def check_redundant_null_quotient_metric() -> None:
    metric = [
        [Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    null = [Fraction(0), Fraction(0), Fraction(1)]
    assert_equal("redundant direction has zero norm", quadratic_form(metric, null), 0)
    assert_equal(
        "redundant direction pairs trivially",
        [sum(metric[i][j] * null[j] for j in range(3)) for i in range(3)],
        [Fraction(0), Fraction(0), Fraction(0)],
    )
    quotient_metric = [row[:2] for row in metric[:2]]
    assert_equal("quotient metric first principal minor", quotient_metric[0][0], 2)
    determinant = quotient_metric[0][0] * quotient_metric[1][1] - quotient_metric[0][1] ** 2
    assert_equal("quotient metric determinant", determinant, 3)


def main() -> None:
    check_source_coordinate_rank_counts()
    check_zamolodchikov_metric_transform()
    check_redundant_null_quotient_metric()
    print("All conformal-manifold finite checks passed.")


if __name__ == "__main__":
    main()
