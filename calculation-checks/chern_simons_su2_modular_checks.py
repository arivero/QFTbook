#!/usr/bin/env python3
"""Finite checks for the SU(2)_k Chern-Simons modular data."""

from __future__ import annotations

import math


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    if abs(got - expected) > tol:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def su2_s_matrix(k: int) -> list[list[float]]:
    K = k + 2
    scale = math.sqrt(2.0 / K)
    return [
        [scale * math.sin((a + 1) * (b + 1) * math.pi / K) for b in range(k + 1)]
        for a in range(k + 1)
    ]


def quantum_dimension(k: int, a: int) -> float:
    K = k + 2
    return math.sin((a + 1) * math.pi / K) / math.sin(math.pi / K)


def verlinde_coeff(k: int, a: int, b: int, c: int) -> int:
    s = su2_s_matrix(k)
    raw = sum(s[a][x] * s[b][x] * s[c][x] / s[0][x] for x in range(k + 1))
    rounded = round(raw)
    assert_close(f"Verlinde integrality k={k} {a}{b}{c}", raw, rounded, tol=1.0e-9)
    return int(rounded)


def su2_truncated_rule(k: int, a: int, b: int, c: int) -> int:
    if (a + b + c) % 2 != 0:
        return 0
    if abs(a - b) <= c <= min(a + b, 2 * k - a - b):
        return 1
    return 0


def check_s_orthogonality() -> None:
    for k in range(1, 11):
        s = su2_s_matrix(k)
        for a in range(k + 1):
            for c in range(k + 1):
                got = sum(s[a][b] * s[c][b] for b in range(k + 1))
                expected = 1.0 if a == c else 0.0
                assert_close(f"S orthogonality k={k} a={a} c={c}", got, expected)


def check_quantum_dimensions_and_hopf_links() -> None:
    for k in range(1, 11):
        s = su2_s_matrix(k)
        s00 = s[0][0]
        total_dimension_squared = sum(quantum_dimension(k, a) ** 2 for a in range(k + 1))
        assert_close(f"total dimension k={k}", total_dimension_squared, 1.0 / (s00 * s00))
        for a in range(k + 1):
            assert_close(f"unknot dimension k={k} a={a}", s[0][a] / s00, quantum_dimension(k, a))

        if k == 1:
            assert_close("SU(2)_1 nontrivial Hopf", s[1][1] / s00, -1.0)
        if k == 2:
            assert_close("SU(2)_2 spin-half dimension", quantum_dimension(k, 1), math.sqrt(2.0))


def check_verlinde_rule() -> None:
    for k in range(1, 9):
        for a in range(k + 1):
            for b in range(k + 1):
                for c in range(k + 1):
                    assert_close(
                        f"Verlinde rule k={k} {a}{b}{c}",
                        verlinde_coeff(k, a, b, c),
                        su2_truncated_rule(k, a, b, c),
                    )


def check_verlinde_dimensions() -> None:
    for k in range(1, 12):
        s = su2_s_matrix(k)
        sphere_dim = sum(s[0][x] ** 2 for x in range(k + 1))
        torus_dim = sum(1.0 for _ in range(k + 1))
        assert_close(f"sphere dimension k={k}", sphere_dim, 1.0)
        assert_close(f"torus dimension k={k}", torus_dim, k + 1)


def main() -> None:
    check_s_orthogonality()
    check_quantum_dimensions_and_hopf_links()
    check_verlinde_rule()
    check_verlinde_dimensions()
    print("All SU(2)_k Chern-Simons modular-data checks passed.")


if __name__ == "__main__":
    main()
