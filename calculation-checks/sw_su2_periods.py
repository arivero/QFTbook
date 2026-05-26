#!/usr/bin/env python3
"""Numerical and exact checks for the pure SU(2) Seiberg-Witten section.

The checks use the chapter normalization with Lambda=1:

    a(u)  = sqrt(2(u+1)) 2F1(-1/2,1/2;1;2/(u+1)),
    aD(u) = i (u-1) 2F1(1/2,1/2;2;(1-u)/2)/2.

They verify monodromy matrices, the Picard-Fuchs equation, the electric
large-u asymptotic, the logarithmic large-u growth of the dual period, and
the linear vanishing of the monopole period at u=1.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def assert_close(name: str, value: complex, expected: complex, tol: mp.mpf) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value}, expected {expected}, tol={tol}")


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [a[0][0] * b[0][j] + a[0][1] * b[1][j] for j in range(2)],
        [a[1][0] * b[0][j] + a[1][1] * b[1][j] for j in range(2)],
    ]


def charge_monodromy(n_m: int, n_e: int) -> list[list[int]]:
    return [
        [1 + 2 * n_m * n_e, 2 * n_e * n_e],
        [-2 * n_m * n_m, 1 - 2 * n_m * n_e],
    ]


def a_period(u: mp.mpf | mp.mpc) -> mp.mpc:
    return mp.sqrt(2 * (u + 1)) * mp.hyper([mp.mpf("-0.5"), mp.mpf("0.5")], [1], 2 / (u + 1))


def aD_period(u: mp.mpf | mp.mpc) -> mp.mpc:
    return 0.5j * (u - 1) * mp.hyper([mp.mpf("0.5"), mp.mpf("0.5")], [2], (1 - u) / 2)


def check_monodromies() -> None:
    m_monopole = charge_monodromy(1, 0)
    m_dyon = charge_monodromy(1, -1)
    m_infinity = [[-1, 2], [0, -1]]
    if m_monopole != [[1, 0], [-2, 1]]:
        raise AssertionError(f"monopole monodromy mismatch: {m_monopole}")
    if m_dyon != [[-1, 2], [-2, 3]]:
        raise AssertionError(f"dyon monodromy mismatch: {m_dyon}")
    if matmul(m_monopole, m_dyon) != m_infinity:
        raise AssertionError("finite monodromy product does not give M_infinity")


def check_picard_fuchs() -> None:
    for label, fn in (("a", a_period), ("aD", aD_period)):
        for u in (mp.mpf("3.7"), mp.mpf("8.25")):
            residual = (u * u - 1) * mp.diff(fn, u, 2) + fn(u) / 4
            assert_close(f"{label} Picard-Fuchs residual at u={u}", residual, 0, mp.mpf("1e-42"))


def check_large_u_asymptotics() -> None:
    u = mp.mpf("1e6")
    a_val = a_period(u)
    assert_close("a/sqrt(2u) at large u", a_val / mp.sqrt(2 * u), 1, mp.mpf("1e-12"))

    leading_dual = 1j * a_val * mp.log(a_val * a_val) / mp.pi
    ratio = aD_period(u) / leading_dual
    if abs(ratio - 1) > mp.mpf("0.05"):
        raise AssertionError(f"aD logarithmic asymptotic ratio too far from 1: {ratio}")


def check_monopole_vanishing() -> None:
    for s in (mp.mpf("1e-3"), mp.mpf("1e-4")):
        ratio = aD_period(1 + s) / s
        assert_close(f"aD/(u-1) near u=1, s={s}", ratio, 0.5j, mp.mpf("4e-5"))


def main() -> None:
    check_monodromies()
    check_picard_fuchs()
    check_large_u_asymptotics()
    check_monopole_vanishing()
    print("All SU(2) Seiberg-Witten period and monodromy checks passed.")


if __name__ == "__main__":
    main()
