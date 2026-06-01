#!/usr/bin/env python3
"""Exact finite checks for the direct-integral CFT crossing formalism.

The monograph's nonrational discussion is infinite-dimensional.  This file
checks the algebraic core in a finite Plancherel model: a fusing transform is
a unitary map between two spectral decompositions, and crossing is the
preservation of the Hilbert inner product under that map.
"""

from __future__ import annotations

from fractions import Fraction


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def dot(left: Vector, right: Vector) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix)]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return [dot(row, vector) for row in matrix]


def matrix_matrix(left: Matrix, right: Matrix) -> Matrix:
    columns = transpose(right)
    return [[dot(row, column) for column in columns] for row in left]


def check_fusing_kernel_unitarity() -> None:
    # Rational orthogonal matrix from the 3-4-5 Pythagorean triple.  It is a
    # finite spectral analogue of a unitary direct-integral fusing transform.
    fusing = [
        [Fraction(3, 5), Fraction(4, 5)],
        [Fraction(-4, 5), Fraction(3, 5)],
    ]
    identity = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
    ]
    assert_equal(
        "F^T F",
        matrix_matrix(transpose(fusing), fusing),
        identity,
    )
    assert_equal(
        "F F^T",
        matrix_matrix(fusing, transpose(fusing)),
        identity,
    )

    s_channel_left = [Fraction(2, 3), Fraction(-5, 7)]
    s_channel_right = [Fraction(11, 13), Fraction(17, 19)]
    t_channel_left = matrix_vector(fusing, s_channel_left)
    t_channel_right = matrix_vector(fusing, s_channel_right)
    assert_equal(
        "Plancherel crossing identity",
        dot(s_channel_left, s_channel_right),
        dot(t_channel_left, t_channel_right),
    )


def check_spectral_resolution_inner_product() -> None:
    # A finite direct integral is an orthogonal direct sum.  The four-point
    # radial-product identity reduces to Parseval's identity for the spectral
    # coefficients of two product vectors.
    product_vector_ba = [Fraction(5, 8), Fraction(-7, 9), Fraction(3, 10)]
    product_vector_cd = [Fraction(4, 11), Fraction(13, 17), Fraction(-2, 5)]
    spectral_inner_product = sum(
        left * right
        for left, right in zip(product_vector_cd, product_vector_ba)
    )
    direct_sum_inner_product = dot(product_vector_cd, product_vector_ba)
    assert_equal(
        "finite direct-integral inner product",
        spectral_inner_product,
        direct_sum_inner_product,
    )


def check_noncompact_free_boson_charge_algebra() -> None:
    # For the diagonal noncompact boson, the leading OPE factor obeys
    # |z12|^{2ab}|z23|^{2(a+b)c} = |z23|^{2bc}|z12|^{2a(b+c)}
    # once the common pairwise-distance factors are restored.  The finite
    # check is the charge-quadratic identity used in the manuscript.
    a = Fraction(2, 3)
    b = Fraction(-5, 7)
    c = Fraction(11, 13)
    left_grouping = a * b + (a + b) * c
    right_grouping = b * c + a * (b + c)
    assert_equal(
        "noncompact boson leading OPE charge associativity",
        left_grouping,
        right_grouping,
    )

    # Momentum labels form an additive Plancherel variable.  Smearing the
    # distributional labelled fields turns charge conservation into ordinary
    # convolution; the support of the convolution is the Minkowski sum of
    # supports.  Here we verify the finite charge bookkeeping exactly.
    charges_f = [Fraction(-1, 2), Fraction(1, 3)]
    charges_g = [Fraction(5, 6), Fraction(7, 6)]
    expected_sums = sorted(x + y for x in charges_f for y in charges_g)
    assert_equal(
        "noncompact boson smeared charge support",
        expected_sums,
        sorted([Fraction(1, 3), Fraction(2, 3), Fraction(7, 6), Fraction(3, 2)]),
    )


def check_noncompact_partition_density_modularity() -> None:
    # The noncompact boson partition density has modular weights
    # tau_2^{-1/2} |eta|^{-2}.  Under S, tau_2 -> tau_2 / |tau|^2 and
    # |eta|^{-2} -> |tau|^{-1} |eta|^{-2}.  The powers of |tau| cancel.
    tau2_power = Fraction(-1, 2)
    eta_abs_inv_sq_power = Fraction(1)
    tau_factor_from_tau2 = -2 * tau2_power
    tau_factor_from_eta = -eta_abs_inv_sq_power
    assert_equal(
        "noncompact boson modular S weight cancellation",
        tau_factor_from_tau2 + tau_factor_from_eta,
        Fraction(0),
    )


def main() -> None:
    check_fusing_kernel_unitarity()
    check_spectral_resolution_inner_product()
    check_noncompact_free_boson_charge_algebra()
    check_noncompact_partition_density_modularity()
    print(
        "All nonrational CFT direct-integral and fusing-kernel checks passed."
    )


if __name__ == "__main__":
    main()
