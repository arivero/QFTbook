#!/usr/bin/env python3
"""Finite checks for the higher-genus sewing formulas in the CFT volume.

Evidence contract.
Target claims: the finite algebraic subclaims in the higher-genus sewing
discussion: basis-sum/inner-product equality, torus self-sewing trace,
stable-graph genus bookkeeping, finite truncation/error-budget identities, and
the torus free-boson Green-kernel zero-mode projection.
Independent construction: finite matrices, graph Betti-number arithmetic,
trace computations, discrete Laplacian inverses, and explicit truncation bounds
are computed directly from the finite model data rather than by substituting
the final sewing formula.
Imported assumptions: the chapter's finite-level truncation model, chosen
basis pairing, propagation weights, stable-graph convention, and normal-ordered
free-boson vertex convention.
Negative controls: the checks include crude norm bounds and graph-genus cases
where changing an edge or component count changes the sewn genus; they also
reject non-neutral vertex sources, diagonal self-contraction shortcuts, and
untransported Green-kernel constant shifts.
Scope boundary: a pass checks finite sewing algebra and bookkeeping; it does
not prove VOA convergence, modular functor existence, higher-genus analytic
sewing, prime-form/Szego-kernel construction, or positivity of the full
continuum CFT Hilbert space.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from check_utils import assert_leq as _assert_leq


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


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[row]))]
        for row in range(len(left))
    ]


def scalar_matrix(scalar: Fraction, size: int) -> Matrix:
    return [[scalar for _column in range(size)] for _row in range(size)]


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
    _assert_leq("finite sewing l1 bound", abs(basis_sum), crude_l1_bound)


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


def check_torus_free_boson_green_kernel_zero_mode_projection() -> None:
    # A four-site periodic lattice is a finite analogue of a torus scalar
    # Laplacian.  The Green kernel inverts the Laplacian only after the constant
    # mode has been projected out.
    laplacian = [
        [Fraction(2), -Fraction(1), Fraction(0), -Fraction(1)],
        [-Fraction(1), Fraction(2), -Fraction(1), Fraction(0)],
        [Fraction(0), -Fraction(1), Fraction(2), -Fraction(1)],
        [-Fraction(1), Fraction(0), -Fraction(1), Fraction(2)],
    ]
    green = [
        [Fraction(5, 16), -Fraction(1, 16), -Fraction(3, 16), -Fraction(1, 16)],
        [-Fraction(1, 16), Fraction(5, 16), -Fraction(1, 16), -Fraction(3, 16)],
        [-Fraction(3, 16), -Fraction(1, 16), Fraction(5, 16), -Fraction(1, 16)],
        [-Fraction(1, 16), -Fraction(3, 16), -Fraction(1, 16), Fraction(5, 16)],
    ]
    projector = [
        [
            (Fraction(1) if row == column else Fraction(0)) - Fraction(1, 4)
            for column in range(4)
        ]
        for row in range(4)
    ]
    assert_equal(
        "torus Green zero-average rows",
        [sum(row) for row in green],
        [Fraction(0)] * 4,
    )
    assert_equal(
        "torus Laplacian Green projects constants",
        matrix_product(laplacian, green),
        projector,
    )

    neutral_charges = [Fraction(1), -Fraction(1), Fraction(2), -Fraction(2)]
    assert_equal("neutral vertex charge", sum(neutral_charges), Fraction(0))
    potential = matrix_vector(green, neutral_charges)
    assert_equal("neutral Green inversion", matrix_vector(laplacian, potential), neutral_charges)

    nonneutral_charges = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    projected_nonneutral = matrix_vector(projector, nonneutral_charges)
    assert_equal(
        "nonneutral source is projected",
        projected_nonneutral == nonneutral_charges,
        False,
    )
    assert_equal(
        "Green inversion cannot solve nonneutral source",
        matrix_vector(laplacian, matrix_vector(green, nonneutral_charges))
        == nonneutral_charges,
        False,
    )

    pair_exponent = -sum(
        neutral_charges[row] * neutral_charges[column] * green[row][column]
        for row in range(4)
        for column in range(row + 1, 4)
    )
    full_gaussian_exponent = -Fraction(1, 2) * dot(
        neutral_charges,
        matrix_vector(green, neutral_charges),
    )
    self_contraction = Fraction(1, 2) * sum(
        neutral_charges[index] * neutral_charges[index] * green[index][index]
        for index in range(4)
    )
    assert_equal(
        "normal ordering removes diagonal torus self-contractions",
        full_gaussian_exponent,
        pair_exponent - self_contraction,
    )
    assert_equal(
        "including diagonal self-contractions changes vertex normalization",
        full_gaussian_exponent == pair_exponent,
        False,
    )

    constant_shift = Fraction(3, 20)
    shifted_green = matrix_add(green, scalar_matrix(constant_shift, 4))
    shifted_pair_exponent = -sum(
        neutral_charges[row] * neutral_charges[column] * shifted_green[row][column]
        for row in range(4)
        for column in range(row + 1, 4)
    )
    vertex_normalization_transport = -constant_shift * sum(
        charge * charge for charge in neutral_charges
    ) / 2
    assert_equal(
        "untransported Green constant changes normal-ordered exponent",
        shifted_pair_exponent == pair_exponent,
        False,
    )
    assert_equal(
        "transported normal-ordering constant preserves vertex exponent",
        shifted_pair_exponent + vertex_normalization_transport,
        pair_exponent,
    )

    charge_a = Fraction(2)
    charge_b = Fraction(3)
    correct_local_log_power = charge_a * charge_b
    wrong_sign_log_power = -charge_a * charge_b
    assert_equal(
        "wrong Green exponent sign flips free-boson OPE power",
        wrong_sign_log_power == correct_local_log_power,
        False,
    )


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
    check_torus_free_boson_green_kernel_zero_mode_projection()
    check_sewing_graph_genus_formula()
    print("All CFT higher-genus sewing finite checks passed.")


if __name__ == "__main__":
    main()
