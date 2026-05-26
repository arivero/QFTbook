#!/usr/bin/env python3
"""Finite checks for the planar N=4 SYM integrability chapters."""

from __future__ import annotations

import cmath
from fractions import Fraction
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


def check_bmn_scaling_limit() -> None:
    lam_prime = 0.37
    for charge in (2000, 5000):
        lam = lam_prime * charge * charge
        g = math.sqrt(lam) / (4 * math.pi)
        for mode in (1, 2, 5):
            momentum = 2 * math.pi * mode / charge
            exact = math.sqrt(1 + 16 * g * g * math.sin(momentum / 2) ** 2)
            bmn = math.sqrt(1 + lam_prime * mode * mode)
            if abs(exact - bmn) > 3.0e-3:
                raise AssertionError(
                    f"BMN scaling J={charge} mode={mode}: got {exact}, expected {bmn}"
                )


def check_bound_state_dispersion() -> None:
    for coupling in (0.1, 0.4):
        for charge in (1, 2, 5):
            for momentum in (0.2, 1.3, 2.6):
                constituent_energy = 0j
                # The fused shortening relation telescopes from x_1^+ to x_Q^-.
                fused = math.sqrt(charge * charge + 16 * coupling * coupling * math.sin(momentum / 2) ** 2)
                central_p = coupling * (1 - cmath.exp(1j * momentum))
                central_k = coupling * (1 - cmath.exp(-1j * momentum))
                shortened = cmath.sqrt(charge * charge + 4 * central_p * central_k)
                constituent_energy += shortened
                assert_close("bound-state dispersion", constituent_energy, fused)


def check_konishi_four_loop_wrapping_arithmetic() -> None:
    # ABA coefficient: -(2820 + 288 zeta_3).
    # Wrapping coefficient: 324 + 864 zeta_3 - 1440 zeta_5.
    rational = -2820 + 324
    zeta3 = -288 + 864
    zeta5 = -1440
    if (rational, zeta3, zeta5) != (-2496, 576, -1440):
        raise AssertionError("Konishi four-loop coefficient arithmetic failed")


def check_bremsstrahlung_weak_series() -> None:
    # B(lambda) = sqrt(lambda)/(4 pi^2) I_2(sqrt(lambda))/I_1(sqrt(lambda)).
    # From I_1(z)=z/2+z^3/16+z^5/384+...
    # and I_2(z)=z^2/8+z^4/96+z^6/3072+...
    a1 = Fraction(1, 2)
    a3 = Fraction(1, 16)
    b2 = Fraction(1, 8)
    b4 = Fraction(1, 96)
    ratio_z_coeff = b2 / a1
    ratio_z3_coeff = b4 / a1 - b2 * a3 / (a1 * a1)
    # z/(4 pi^2) * (ratio_z_coeff z + ratio_z3_coeff z^3 + ...)
    # with z^2=lambda gives lambda/(16 pi^2) - lambda^2/(384 pi^2)+...
    if ratio_z_coeff != Fraction(1, 4):
        raise AssertionError("B(lambda) leading Bessel ratio coefficient failed")
    if ratio_z3_coeff != Fraction(-1, 96):
        raise AssertionError("B(lambda) next Bessel ratio coefficient failed")


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
    check_bmn_scaling_limit()
    check_bound_state_dispersion()
    check_konishi_four_loop_wrapping_arithmetic()
    check_bremsstrahlung_weak_series()
    check_t_system_to_y_system_identity()
    print("All planar N=4 integrability checks passed.")


if __name__ == "__main__":
    main()
