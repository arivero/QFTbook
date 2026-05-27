#!/usr/bin/env python3
"""Finite checks for the higher-genus sewing formulas in the CFT volume."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return [dot(row, vector) for row in matrix]


def matrix_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def diagonal(values: Vector) -> Matrix:
    return [
        [
            values[row] if row == column else Fraction(0)
            for column in range(len(values))
        ]
        for row in range(len(values))
    ]


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    columns = [list(column) for column in zip(*right)]
    return [[dot(row, column) for column in columns] for row in left]


@dataclass(frozen=True)
class Graph:
    vertex_genera: list[int]
    edge_count: int
    connected_components: int = 1

    def first_betti_number(self) -> int:
        return self.edge_count - len(self.vertex_genera) + self.connected_components

    def geometric_genus(self) -> int:
        return sum(self.vertex_genera) + self.first_betti_number()


def check_one_channel_sewing_equals_inner_product() -> None:
    # Finite-level model for the basis sum
    # sum_alpha <u1,e_alpha> lambda_alpha <e_alpha,u2>.
    u1 = [Fraction(2, 3), Fraction(-1, 5), Fraction(7, 11)]
    u2 = [Fraction(3, 4), Fraction(5, 6), Fraction(-2, 7)]
    propagation_weights = [Fraction(1, 2), Fraction(1, 8), Fraction(1, 32)]
    propagator = diagonal(propagation_weights)

    basis_sum = sum(
        u1[index] * propagation_weights[index] * u2[index]
        for index in range(len(u1))
    )
    inner_product = dot(u1, matrix_vector(propagator, u2))
    assert_equal("one-channel sewn basis sum", basis_sum, inner_product)

    trace_norm = sum(propagation_weights)
    crude_l1_bound = sum(abs(entry) for entry in u1) * trace_norm * sum(
        abs(entry) for entry in u2
    )
    if abs(basis_sum) > crude_l1_bound:
        raise AssertionError("finite sewing bound violated")


def check_torus_trace_from_self_sewing() -> None:
    # A finite-level analogue of Tr(Y(v,1) q^(L0-c/24)).
    vertex_operator = [
        [Fraction(5, 3), Fraction(2, 7), Fraction(0)],
        [Fraction(-1, 4), Fraction(11, 5), Fraction(3, 8)],
        [Fraction(9, 10), Fraction(0), Fraction(-2, 9)],
    ]
    propagation_weights = [Fraction(1, 3), Fraction(1, 9), Fraction(1, 27)]
    propagator = diagonal(propagation_weights)

    sewn_sum = sum(
        propagation_weights[index] * vertex_operator[index][index]
        for index in range(len(propagation_weights))
    )
    trace_formula = matrix_trace(matrix_product(vertex_operator, propagator))
    assert_equal("torus trace from self-sewing", sewn_sum, trace_formula)

    identity_operator = diagonal([Fraction(1), Fraction(1), Fraction(1)])
    character = sum(propagation_weights)
    identity_trace = matrix_trace(matrix_product(identity_operator, propagator))
    assert_equal("character from vacuum self-sewing", identity_trace, character)


def check_sewing_graph_genus_formula() -> None:
    # Two spheres joined by one edge: genus 0.
    assert_equal(
        "sphere pair joined by an edge",
        Graph(vertex_genera=[0, 0], edge_count=1).geometric_genus(),
        0,
    )
    # One sphere with a self-sewing loop: torus.
    assert_equal(
        "self-sewn sphere",
        Graph(vertex_genera=[0], edge_count=1).geometric_genus(),
        1,
    )
    # Two one-holed tori with two independent sewn edges: genus 3.
    assert_equal(
        "two tori with two sewn channels",
        Graph(vertex_genera=[1, 1], edge_count=2).geometric_genus(),
        3,
    )
    # A three-vertex connected pants graph with five internal edges has
    # b1 = 3 and genus equal to the sum of vertex genera plus three.
    assert_equal(
        "multi-cycle sewing graph",
        Graph(vertex_genera=[0, 2, 1], edge_count=5).geometric_genus(),
        6,
    )


def main() -> None:
    check_one_channel_sewing_equals_inner_product()
    check_torus_trace_from_self_sewing()
    check_sewing_graph_genus_formula()
    print("All CFT higher-genus sewing finite checks passed.")


if __name__ == "__main__":
    main()
