#!/usr/bin/env python3
"""Reader-facing checks for the planar N=4 integrability spine.

This file is deliberately smaller than planar_n4_integrability_checks.py.
It is meant as companion code for readers who want to modify simple finite
examples while following the monograph chapters on the spin chain, Bethe-Yang
equations, the Y-system, and mirror TBA.
"""

from __future__ import annotations

from fractions import Fraction
import cmath
import itertools
import math


def assert_close(name: str, value: complex, expected: complex = 0j, tol: float = 1.0e-10) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def rapidity_from_momentum(momentum: float) -> float:
    """One-loop XXX rapidity u(p)=1/2 cot(p/2)."""

    return 0.5 / math.tan(momentum / 2)


def exchange_amplitude(momentum_1: float, momentum_2: float) -> complex:
    """Two-magnon ordered-wavefunction exchange coefficient."""

    u_1 = rapidity_from_momentum(momentum_1)
    u_2 = rapidity_from_momentum(momentum_2)
    return (u_1 - u_2 - 1j) / (u_1 - u_2 + 1j)


def check_spin_chain_konishi() -> None:
    """Check the length-four two-magnon XXX eigenvector used for Konishi."""

    length = 4
    momentum_1 = 2 * math.pi / 3
    momentum_2 = -2 * math.pi / 3
    amplitude = exchange_amplitude(momentum_1, momentum_2)
    basis = list(itertools.combinations(range(length), 2))
    basis_index = {state: index for index, state in enumerate(basis)}

    wave = []
    for n_1, n_2 in basis:
        direct = cmath.exp(1j * (momentum_1 * n_1 + momentum_2 * n_2))
        exchanged = amplitude * cmath.exp(1j * (momentum_2 * n_1 + momentum_1 * n_2))
        wave.append(direct + exchanged)

    acted = [0j for _ in basis]
    for state, coefficient in zip(basis, wave):
        bits = [0] * length
        for site in state:
            bits[site] = 1
        for site in range(length):
            acted[basis_index[state]] += coefficient
            swapped = bits.copy()
            next_site = (site + 1) % length
            swapped[site], swapped[next_site] = swapped[next_site], swapped[site]
            swapped_state = tuple(index for index, value in enumerate(swapped) if value)
            acted[basis_index[swapped_state]] -= coefficient

    residual = max(abs(value - 6 * expected) for value, expected in zip(acted, wave))
    assert_close("length-four Konishi spin-chain eigenvector", residual)

    translated = []
    for state in basis:
        shifted = tuple(sorted((site + 1) % length for site in state))
        translated.append(wave[basis_index[shifted]])
    translation_residual = max(abs(value - expected) for value, expected in zip(translated, wave))
    assert_close("length-four Konishi cyclicity", translation_residual)


def check_bethe_yang_equations() -> None:
    """Check the one-loop Bethe-Yang orientation for the two Konishi roots."""

    length = 4
    roots = [1 / (2 * math.sqrt(3)), -1 / (2 * math.sqrt(3))]
    phases = [(u + 0.5j) / (u - 0.5j) for u in roots]
    assert_close("Bethe-Yang cyclicity", phases[0] * phases[1], 1)

    for index, root in enumerate(roots):
        lhs = ((root + 0.5j) / (root - 0.5j)) ** length
        rhs = 1 + 0j
        for other_index, other in enumerate(roots):
            if index != other_index:
                rhs *= (root - other + 1j) / (root - other - 1j)
        assert_close(f"Bethe-Yang equation root {index}", lhs, rhs)

    one_loop_energy = sum(1 / (u * u + 0.25) for u in roots)
    assert_close("Konishi one-loop spin-chain energy", one_loop_energy, 6)


def check_y_system_algebra() -> None:
    """Check local Hirota-to-Y-system algebra and source-factor memory."""

    t_center_plus = Fraction(7)
    t_up = Fraction(5)
    t_down = Fraction(3)
    t_left = Fraction(2)
    t_right = Fraction(13)
    t_center_minus = (t_up * t_down + t_left * t_right) / t_center_plus

    y_value = t_up * t_down / (t_left * t_right)
    one_plus_y = (t_center_plus * t_center_minus) / (t_left * t_right)
    one_plus_inverse_y = (t_center_plus * t_center_minus) / (t_up * t_down)
    if one_plus_y != 1 + y_value:
        raise AssertionError("Hirota did not produce 1+Y")
    if one_plus_inverse_y != 1 + 1 / y_value:
        raise AssertionError("Hirota did not produce 1+1/Y")

    def source_factor(u_value: complex, root: complex) -> complex:
        return (u_value - root + 0.5j) / (u_value - root - 0.5j)

    for u_value, root in ((0.3 + 0.2j, -0.7 + 0.1j), (1.4 - 0.15j, 0.2 - 0.35j)):
        shifted_product = source_factor(u_value + 0.5j, root) * source_factor(
            u_value - 0.5j,
            root,
        )
        rational_source = (u_value - root + 1j) / (u_value - root - 1j)
        assert_close("Y-system shifted source factor", shifted_product, rational_source)


def check_mirror_tba_toy_equations() -> None:
    """Check the finite-grid pseudoenergy and A-infinity kernel identities."""

    epsilon = [0.7, 1.1, 1.6]
    kernel = [
        [0.0, 0.2, -0.1],
        [0.3, 0.0, 0.15],
        [-0.05, 0.25, 0.0],
    ]
    log_one_plus_exp_minus = [math.log1p(math.exp(-value)) for value in epsilon]
    driving = [
        epsilon[row] + sum(kernel[row][col] * log_one_plus_exp_minus[col] for col in range(3))
        for row in range(3)
    ]
    y_values = [math.exp(value) for value in epsilon]

    for row in range(3):
        pseudoenergy_rhs = driving[row] - sum(
            kernel[row][col] * math.log1p(math.exp(-epsilon[col]))
            for col in range(3)
        )
        y_rhs = driving[row] - sum(
            kernel[row][col] * math.log(1 + 1 / y_values[col])
            for col in range(3)
        )
        assert_close(f"mirror TBA pseudoenergy row {row}", epsilon[row], pseudoenergy_rhs)
        assert_close(f"mirror TBA Y-form row {row}", math.log(y_values[row]), y_rhs)

    def a_symbol(m_value: int, n_value: int, q_value: float) -> float:
        return (
            (1 + q_value * q_value)
            * (q_value ** abs(m_value - n_value) - q_value ** (m_value + n_value))
            / (1 - q_value * q_value)
        )

    for q_value in (0.25, 0.6):
        s_symbol = q_value / (1 + q_value * q_value)
        for m_value in range(1, 5):
            for n_value in range(1, 5):
                inverse_product = a_symbol(m_value, n_value, q_value)
                inverse_product -= s_symbol * a_symbol(m_value + 1, n_value, q_value)
                if m_value > 1:
                    inverse_product -= s_symbol * a_symbol(m_value - 1, n_value, q_value)
                expected = 1.0 if m_value == n_value else 0.0
                assert_close("mirror A-infinity inverse", inverse_product, expected)


def main() -> None:
    check_spin_chain_konishi()
    check_bethe_yang_equations()
    check_y_system_algebra()
    check_mirror_tba_toy_equations()
    print("All planar N=4 reader companion checks passed.")


if __name__ == "__main__":
    main()
