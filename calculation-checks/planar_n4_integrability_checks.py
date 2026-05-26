#!/usr/bin/env python3
"""Finite checks for the planar N=4 SYM integrability chapters."""

from __future__ import annotations

import cmath
import math


def assert_close(name: str, value: complex, expected: complex = 0j, tol: float = 1e-9) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def check_one_magnon_laplacian() -> None:
    for length in (4, 6, 8):
        for mode in range(1, length):
            momentum = 2 * math.pi * mode / length
            wave = [cmath.exp(1j * momentum * site) for site in range(length)]
            acted = [
                2 * wave[site] - wave[(site - 1) % length] - wave[(site + 1) % length]
                for site in range(length)
            ]
            energy = 4 * math.sin(momentum / 2) ** 2
            residual = max(abs(acted[site] - energy * wave[site]) for site in range(length))
            assert_close(f"one-magnon XXX energy L={length} mode={mode}", residual)


def check_konishi_one_loop_roots() -> None:
    length = 4
    root = 1 / (2 * math.sqrt(3))
    roots = [root, -root]
    phases = [(u + 0.5j) / (u - 0.5j) for u in roots]
    cyclicity = phases[0] * phases[1]
    assert_close("Konishi cyclicity", cyclicity, 1)

    for j, u in enumerate(roots):
        lhs = ((u + 0.5j) / (u - 0.5j)) ** length
        rhs = 1 + 0j
        for k, other in enumerate(roots):
            if j != k:
                rhs *= (u - other + 1j) / (u - other - 1j)
        assert_close(f"Konishi Bethe equation root {j}", lhs, rhs)

    energy = sum(1 / (u * u + 0.25) for u in roots)
    assert_close("Konishi one-loop spin-chain energy", energy, 6)


def check_central_extension_dispersion() -> None:
    for coupling in (0.05, 0.2, 0.7):
        for momentum in (0.3, 1.1, 2.4):
            central_p = coupling * (1 - cmath.exp(1j * momentum))
            central_k = coupling * (1 - cmath.exp(-1j * momentum))
            shortened = cmath.sqrt(1 + 4 * central_p * central_k)
            displayed = math.sqrt(1 + 16 * coupling * coupling * math.sin(momentum / 2) ** 2)
            assert_close("central-extension dispersion", shortened, displayed)


def check_weak_dispersion_expansion() -> None:
    g = 1.0e-4
    for momentum in (0.4, 1.2, 2.7):
        s2 = math.sin(momentum / 2) ** 2
        exact = math.sqrt(1 + 16 * g * g * s2) - 1
        truncated = 8 * g * g * s2 - 32 * g**4 * s2**2 + 256 * g**6 * s2**3
        if abs(exact - truncated) > 1.0e-15:
            raise AssertionError(
                f"weak dispersion expansion: got {exact!r}, truncated {truncated!r}"
            )


def check_t_system_to_y_system_identity() -> None:
    """Check the algebraic Y-system relation from a local Hirota square."""

    # Positive sample T-values around one interior T-hook node.
    t_center_plus = 7.0
    t_center_minus = 11.0
    t_up = 5.0
    t_down = 3.0
    t_left = 2.0
    t_right = 13.0

    # Hirota: T^+ T^- = T_up T_down + T_left T_right.
    t_center_minus = (t_up * t_down + t_left * t_right) / t_center_plus

    y = t_up * t_down / (t_left * t_right)
    one_plus_y = (t_center_plus * t_center_minus) / (t_left * t_right)
    one_plus_inverse_y = (t_center_plus * t_center_minus) / (t_up * t_down)

    assert_close("1+Y from Hirota", one_plus_y, 1 + y)
    assert_close("1+1/Y from Hirota", one_plus_inverse_y, 1 + 1 / y)


def main() -> None:
    check_one_magnon_laplacian()
    check_konishi_one_loop_roots()
    check_central_extension_dispersion()
    check_weak_dispersion_expansion()
    check_t_system_to_y_system_identity()
    print("All planar N=4 integrability checks passed.")


if __name__ == "__main__":
    main()
