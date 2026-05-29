#!/usr/bin/env python3
"""Checks for Vol VI nested Bethe, QQ, and Hirota identities."""

from __future__ import annotations

import itertools
import math
from collections.abc import Callable


I = 1j


def assert_close(name: str, lhs: complex, rhs: complex, tol: float = 2.0e-10) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{name}: {lhs!r} != {rhs!r}")


def determinant(matrix: list[list[complex]]) -> complex:
    n = len(matrix)
    if n == 0:
        return 1.0 + 0.0j
    if n == 1:
        return matrix[0][0]
    total = 0.0 + 0.0j
    for col in range(n):
        minor = [
            [matrix[row][c] for c in range(n) if c != col]
            for row in range(1, n)
        ]
        total += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return total


def check_su3_worked_example() -> None:
    sqrt3 = math.sqrt(3.0)
    u1 = -sqrt3 / 2.0
    u2 = sqrt3 / 2.0
    v = 0.0
    z = (u2 + I / 2.0) / (u2 - I / 2.0)
    assert_close("SU(3) z phase", z, complex(math.cos(math.pi / 3), math.sin(math.pi / 3)))
    assert_close("SU(3) left phase", z**6, 1.0)

    second_level = ((v - u1 - I / 2.0) / (v - u1 + I / 2.0)) * (
        (v - u2 - I / 2.0) / (v - u2 + I / 2.0)
    )
    assert_close("SU(3) second-level equation", second_level, 1.0)

    first_rhs = ((u2 - u1 + I) / (u2 - u1 - I)) * (
        (u2 - v - I / 2.0) / (u2 - v + I / 2.0)
    )
    assert_close("SU(3) first-level RHS", first_rhs, 1.0)
    energy = 1.0 / (u1 * u1 + 0.25) + 1.0 / (u2 * u2 + 0.25)
    assert_close("SU(3) energy", energy, 2.0)


def cartan(n: int, r: int, s: int) -> int:
    return 2 * (r == s) - (abs(r - s) == 1)


def nested_cartan_rhs(roots: dict[int, list[complex]], r: int, j: int) -> complex:
    u = roots[r][j]
    prod = 1.0 + 0.0j
    for s, values in roots.items():
        a_rs = cartan(len(roots) + 1, r, s)
        for k, v in enumerate(values):
            if s == r and k == j:
                continue
            prod *= (u - v + I * a_rs / 2.0) / (u - v - I * a_rs / 2.0)
    return prod


def explicit_nested_rhs(roots: dict[int, list[complex]], r: int, j: int) -> complex:
    u = roots[r][j]
    prod = 1.0 + 0.0j
    for k, v in enumerate(roots[r]):
        if k != j:
            prod *= (u - v + I) / (u - v - I)
    for s in (r - 1, r + 1):
        if s in roots:
            for v in roots[s]:
                prod *= (u - v - I / 2.0) / (u - v + I / 2.0)
    return prod


def check_cartan_nested_formula() -> None:
    roots = {
        1: [-0.7 + 0.13j, 0.4 - 0.22j],
        2: [-0.1 + 0.31j],
        3: [0.9 + 0.17j, 1.6 - 0.08j],
        4: [-1.2 + 0.27j],
    }
    for r, values in roots.items():
        for j in range(len(values)):
            assert_close(
                f"Cartan nested RHS r={r} j={j}",
                nested_cartan_rhs(roots, r, j),
                explicit_nested_rhs(roots, r, j),
            )


def q_value(roots: dict[int, list[complex]], r: int, u: complex) -> complex:
    if r not in roots:
        return 1.0 + 0.0j
    prod = 1.0 + 0.0j
    for root in roots[r]:
        prod *= u - root
    return prod


def check_dressed_vacuum_pole_factorization() -> None:
    roots = {
        1: [-0.9 + 0.2j, 0.35 - 0.17j, 1.1 + 0.08j],
        2: [-0.3 - 0.11j, 0.7 + 0.19j],
        3: [0.15 + 0.23j],
    }
    for r, values in roots.items():
        for j, u in enumerate(values):
            residue_ratio = -q_value(roots, r, u + I) / q_value(roots, r, u - I)
            residue_ratio *= q_value(roots, r - 1, u - I / 2.0) / q_value(
                roots, r - 1, u + I / 2.0
            )
            residue_ratio *= q_value(roots, r + 1, u - I / 2.0) / q_value(
                roots, r + 1, u + I / 2.0
            )
            assert_close(
                f"dressed-vacuum pole factorization r={r} j={j}",
                residue_ratio,
                nested_cartan_rhs(roots, r, j),
            )


def shifted(f: Callable[[complex], complex], k: int) -> Callable[[complex], complex]:
    return lambda u: f(u + I * k / 2.0)


def base_q(index: int) -> Callable[[complex], complex]:
    coeffs = [
        (1.0 + 0.2j, -0.3 + 0.1j, 0.17 - 0.05j),
        (0.8 - 0.1j, 0.5 + 0.3j, -0.11 + 0.07j),
        (1.1 + 0.4j, -0.2 - 0.2j, 0.09 + 0.13j),
        (0.6 + 0.5j, 0.4 - 0.15j, -0.2 + 0.03j),
    ][index]
    return lambda u: coeffs[0] + coeffs[1] * u + coeffs[2] * u * u


def q_det(subset: tuple[int, ...], u: complex) -> complex:
    m = len(subset)
    if m == 0:
        return 1.0 + 0.0j
    matrix: list[list[complex]] = []
    for a in subset:
        row: list[complex] = []
        q = base_q(a)
        for s in range(1, m + 1):
            shift = m + 1 - 2 * s
            row.append(shifted(q, shift)(u))
        matrix.append(row)
    return determinant(matrix)


def check_qq_system() -> None:
    all_indices = tuple(range(4))
    sample_points = [0.2 + 0.1j, -0.4 + 0.3j, 1.1 - 0.2j]
    for u in sample_points:
        for size in range(3):
            for subset in itertools.combinations(all_indices, size):
                remaining = [a for a in all_indices if a not in subset]
                for a, b in itertools.combinations(remaining, 2):
                    A = tuple(sorted(subset))
                    Aa = tuple(sorted(A + (a,)))
                    Ab = tuple(sorted(A + (b,)))
                    Aab = tuple(sorted(A + (a, b)))
                    lhs = q_det(Aab, u) * q_det(A, u)
                    rhs = q_det(Aa, u + I / 2.0) * q_det(Ab, u - I / 2.0) - q_det(
                        Aa, u - I / 2.0
                    ) * q_det(Ab, u + I / 2.0)
                    assert_close(f"QQ A={A} a={a} b={b} u={u}", lhs, rhs)


def check_hirota_to_y_system() -> None:
    def t(a: int, s: int, shift: int) -> complex:
        return (
            2.0
            + 0.37 * a
            - 0.19 * s
            + 0.11 * shift
            + I * (0.23 + 0.07 * a + 0.13 * s - 0.05 * shift)
        )

    def y(a: int, s: int, shift: int = 0) -> complex:
        return t(a, s + 1, shift) * t(a, s - 1, shift) / (
            t(a + 1, s, shift) * t(a - 1, s, shift)
        )

    def one_plus_y_from_hirota(a: int, s: int) -> complex:
        return t(a, s, 1) * t(a, s, -1) / (t(a + 1, s, 0) * t(a - 1, s, 0))

    def one_plus_inverse_y_from_hirota(a: int, s: int) -> complex:
        return t(a, s, 1) * t(a, s, -1) / (t(a, s + 1, 0) * t(a, s - 1, 0))

    a, s = 3, 2
    lhs = y(a, s, 1) * y(a, s, -1)
    rhs = one_plus_y_from_hirota(a, s + 1) * one_plus_y_from_hirota(a, s - 1)
    rhs /= one_plus_inverse_y_from_hirota(a + 1, s) * one_plus_inverse_y_from_hirota(a - 1, s)
    assert_close("Hirota local Y-system identity", lhs, rhs)


def main() -> None:
    check_su3_worked_example()
    check_cartan_nested_formula()
    check_dressed_vacuum_pole_factorization()
    check_qq_system()
    check_hirota_to_y_system()
    print("All nested-integrability calculation checks passed.")


if __name__ == "__main__":
    main()
