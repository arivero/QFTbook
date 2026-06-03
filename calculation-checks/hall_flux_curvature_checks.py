#!/usr/bin/env python3
"""Finite checks for flux-torus Hall curvature conventions.

The checks support Volume IX, Chapter 7.  They verify the finite
projector/Kubo curvature identity for a two-level isolated band and the
Chern-number normalization of the standard two-band lattice benchmark
H(k)=sin(k_x) sigma_x + sin(k_y) sigma_y
     +(m+cos(k_x)+cos(k_y)) sigma_z.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import math


Vector = tuple[float, float, float]
Matrix = list[list[complex]]


def assert_close(lhs: float, rhs: float, message: str, tol: float = 1e-9) -> None:
    _assert_close(message, lhs, rhs, tol=tol)


def assert_near_integer(value: float, expected: int, message: str, tol: float = 2e-8) -> None:
    _assert_close(message, value, expected, tol=tol)


def dot(a: Vector, b: Vector) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a: Vector, b: Vector) -> Vector:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(a: Vector) -> float:
    return math.sqrt(dot(a, a))


SIGMA_X: Matrix = [[0, 1], [1, 0]]
SIGMA_Y: Matrix = [[0, -1j], [1j, 0]]
SIGMA_Z: Matrix = [[1, 0], [0, -1]]
IDENTITY: Matrix = [[1, 0], [0, 1]]


def matadd(a: Matrix, b: Matrix, ca: complex = 1, cb: complex = 1) -> Matrix:
    return [
        [ca * a[i][j] + cb * b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def scalar(c: complex, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return matadd(matmul(a, b), matmul(b, a), 1, -1)


def pauli(v: Vector) -> Matrix:
    return matadd(
        matadd(SIGMA_X, SIGMA_Y, v[0], v[1]),
        SIGMA_Z,
        1,
        v[2],
    )


def normalized_derivative(d: Vector, dd: Vector) -> Vector:
    r = norm(d)
    projection = dot(d, dd)
    return (
        dd[0] / r - d[0] * projection / (r**3),
        dd[1] / r - d[1] * projection / (r**3),
        dd[2] / r - d[2] * projection / (r**3),
    )


def lower_projector(d: Vector) -> Matrix:
    r = norm(d)
    n = tuple(component / r for component in d)
    return matadd(IDENTITY, pauli(n), 0.5, -0.5)


def q_projector(d: Vector) -> Matrix:
    r = norm(d)
    n = tuple(component / r for component in d)
    return matadd(IDENTITY, pauli(n), 0.5, 0.5)


def projector_derivative(d: Vector, dd: Vector) -> Matrix:
    dn = normalized_derivative(d, dd)
    return scalar(-0.5, pauli(dn))


def two_band_data(kx: float, ky: float, mass: float) -> tuple[Vector, Vector, Vector]:
    d = (
        math.sin(kx),
        math.sin(ky),
        mass + math.cos(kx) + math.cos(ky),
    )
    dkx = (math.cos(kx), 0.0, -math.sin(kx))
    dky = (0.0, math.cos(ky), -math.sin(ky))
    return d, dkx, dky


def curvature_from_projector(d: Vector, dkx: Vector, dky: Vector) -> float:
    p = lower_projector(d)
    dp_x = projector_derivative(d, dkx)
    dp_y = projector_derivative(d, dky)
    return (1j * trace(matmul(p, commutator(dp_x, dp_y)))).real


def curvature_from_kubo(d: Vector, dkx: Vector, dky: Vector) -> float:
    p = lower_projector(d)
    q = q_projector(d)
    r_gap = norm(d)
    resolvent = scalar(1.0 / (2.0 * r_gap), q)
    ix = pauli(dkx)
    iy = pauli(dky)
    term_xy = matmul(matmul(matmul(matmul(p, ix), resolvent), resolvent), matmul(iy, p))
    term_yx = matmul(matmul(matmul(matmul(p, iy), resolvent), resolvent), matmul(ix, p))
    return (1j * (trace(term_xy) - trace(term_yx))).real


def curvature_from_solid_angle(d: Vector, dkx: Vector, dky: Vector) -> float:
    return 0.5 * dot(d, cross(dkx, dky)) / (norm(d) ** 3)


def check_kubo_curvature_identity() -> None:
    samples = [
        (-1.1, -0.7, -1.0),
        (0.2, 1.4, -0.4),
        (1.1, -2.2, 1.0),
        (2.4, 0.8, 3.0),
    ]
    for kx, ky, mass in samples:
        d, dkx, dky = two_band_data(kx, ky, mass)
        projector_curvature = curvature_from_projector(d, dkx, dky)
        kubo_curvature = curvature_from_kubo(d, dkx, dky)
        solid_angle_curvature = curvature_from_solid_angle(d, dkx, dky)
        assert_close(
            projector_curvature,
            kubo_curvature,
            "finite Kubo formula equals projector curvature",
        )
        assert_close(
            projector_curvature,
            solid_angle_curvature,
            "lower-band curvature has the stated Chern-Weil normalization",
        )


def chern_number_midpoint(mass: float, mesh: int = 101) -> float:
    step = 2.0 * math.pi / mesh
    total = 0.0
    for i in range(mesh):
        kx = -math.pi + (i + 0.5) * step
        for j in range(mesh):
            ky = -math.pi + (j + 0.5) * step
            d, dkx, dky = two_band_data(kx, ky, mass)
            total += curvature_from_solid_angle(d, dkx, dky)
    return total * step * step / (2.0 * math.pi)


def check_two_band_chern_numbers() -> None:
    assert_near_integer(chern_number_midpoint(-3.0), 0, "trivial lower band below the first transition")
    assert_near_integer(chern_number_midpoint(-1.0), 1, "lower band in the -2<m<0 phase has Chern number +1")
    assert_near_integer(chern_number_midpoint(1.0), -1, "lower band in the 0<m<2 phase has Chern number -1")
    assert_near_integer(chern_number_midpoint(3.0), 0, "trivial lower band above the second transition")


def main() -> None:
    check_kubo_curvature_identity()
    check_two_band_chern_numbers()
    print("Finite flux-torus Hall curvature checks passed.")


if __name__ == "__main__":
    main()
