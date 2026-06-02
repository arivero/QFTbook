#!/usr/bin/env python3
"""Finite spectral checks for Wightman clustering versus vacuum uniqueness.

The script checks only the algebraic zero-momentum projection step in
Volume IV, Chapter 1.  It does not prove the analytic Jost/Rajchman theorem
used to remove the continuous and nonzero-atom spectral parts.
"""

from __future__ import annotations

from fractions import Fraction

Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def dot(x: Vector, y: Vector) -> Fraction:
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def matvec(a: Matrix, x: Vector) -> Vector:
    return tuple(sum(row[j] * x[j] for j in range(len(x))) for row in a)


def basis_vector(index: int, dimension: int) -> Vector:
    return tuple(Fraction(1 if i == index else 0) for i in range(dimension))


def zero_momentum_projection(dimension: int, zero_rank: int) -> Matrix:
    return tuple(
        tuple(Fraction(1 if i == j and i < zero_rank else 0) for j in range(dimension))
        for i in range(dimension)
    )


def rank_one_vacuum_projection(dimension: int) -> Matrix:
    return zero_momentum_projection(dimension, 1)


def cluster_bilinear_identity_holds(projection: Matrix) -> bool:
    """Check <x,P0 y> = <x,Omega><Omega,y> on a finite spanning set."""

    dimension = len(projection)
    vacuum = basis_vector(0, dimension)
    for i in range(dimension):
        x = basis_vector(i, dimension)
        for j in range(dimension):
            y = basis_vector(j, dimension)
            left = dot(x, matvec(projection, y))
            right = dot(x, vacuum) * dot(vacuum, y)
            if left != right:
                return False
    return True


def first_cluster_obstruction(projection: Matrix) -> tuple[int, int, Fraction, Fraction] | None:
    """Return the first basis-pair witnessing failure of cluster bilinearity."""

    dimension = len(projection)
    vacuum = basis_vector(0, dimension)
    for i in range(dimension):
        x = basis_vector(i, dimension)
        for j in range(dimension):
            y = basis_vector(j, dimension)
            left = dot(x, matvec(projection, y))
            right = dot(x, vacuum) * dot(vacuum, y)
            if left != right:
                return i, j, left, right
    return None


def spectral_atom_contribution(projection: Matrix, x: Vector, y: Vector) -> Fraction:
    """Contribution of the zero-momentum atom to <x,U(a)y>."""

    return dot(x, matvec(projection, y))


def check_cluster_identity_equivalent_to_rank_one_vacuum() -> None:
    for dimension in range(2, 8):
        p_vac = rank_one_vacuum_projection(dimension)
        assert_true(
            f"rank-one vacuum projection gives cluster bilinear identity dim={dimension}",
            cluster_bilinear_identity_holds(p_vac),
        )

        for zero_rank in range(2, dimension + 1):
            p0 = zero_momentum_projection(dimension, zero_rank)
            assert_true(
                f"extra zero-momentum vector violates cluster bilinear identity dim={dimension} rank={zero_rank}",
                not cluster_bilinear_identity_holds(p0),
            )
            obstruction = first_cluster_obstruction(p0)
            assert_equal(
                f"first obstruction is the extra zero vector dim={dimension} rank={zero_rank}",
                obstruction,
                (1, 1, Fraction(1), Fraction(0)),
            )


def check_zero_atom_product_contribution() -> None:
    dimension = 5
    p_vac = rank_one_vacuum_projection(dimension)
    vacuum = basis_vector(0, dimension)
    samples = [
        (tuple(Fraction(i + 1) for i in range(dimension)), tuple(Fraction(2 * i - 3) for i in range(dimension))),
        (basis_vector(2, dimension), tuple(Fraction(i * i - 1) for i in range(dimension))),
        (tuple(Fraction((-1) ** i, i + 1) for i in range(dimension)), basis_vector(0, dimension)),
    ]
    for x, y in samples:
        expected_product = dot(x, vacuum) * dot(vacuum, y)
        assert_equal(
            f"zero atom equals vacuum product x={x} y={y}",
            spectral_atom_contribution(p_vac, x, y),
            expected_product,
        )


def check_removed_zero_atom_has_no_zero_projection() -> None:
    dimension = 6
    p_vac = rank_one_vacuum_projection(dimension)
    samples = [
        tuple(Fraction(i) for i in range(dimension)),
        tuple(Fraction((-1) ** i * (i + 1)) for i in range(dimension)),
        basis_vector(4, dimension),
    ]
    for y in samples:
        vacuum_component = matvec(p_vac, y)
        y_without_vacuum = tuple(y_i - vacuum_i for y_i, vacuum_i in zip(y, vacuum_component))
        assert_equal(
            f"vacuum-subtracted vector has no zero atom y={y}",
            matvec(p_vac, y_without_vacuum),
            tuple(Fraction(0) for _ in range(dimension)),
        )


def main() -> None:
    check_cluster_identity_equivalent_to_rank_one_vacuum()
    check_zero_atom_product_contribution()
    check_removed_zero_atom_has_no_zero_projection()
    print("Wightman cluster spectral projection checks passed.")


if __name__ == "__main__":
    main()
