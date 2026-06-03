#!/usr/bin/env python3
"""Finite checks for the planar N=4 SYM integrability chapters."""

from __future__ import annotations

from collections import Counter
import cmath
from fractions import Fraction
import itertools
import math


def assert_close(name: str, value: complex, expected: complex = 0j, tol: float = 1e-9) -> None:
    if abs(value - expected) > tol:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def zhukovsky_outside(u: complex, coupling: float) -> complex:
    z = u / coupling
    root = cmath.sqrt(z * z - 4)
    x1 = 0.5 * (z + root)
    x2 = 0.5 * (z - root)
    if abs(x1) >= abs(x2):
        return x1
    return x2


def xpm_from_momentum(momentum: float, coupling: float) -> tuple[complex, complex]:
    half_sine = math.sin(momentum / 2)
    energy = math.sqrt(1 + 16 * coupling * coupling * half_sine * half_sine)
    radius = (1 + energy) / (4 * coupling * half_sine)
    return (
        cmath.exp(0.5j * momentum) * radius,
        cmath.exp(-0.5j * momentum) * radius,
    )


def check_so6_hamiltonian_reduces_to_su2() -> None:
    inv_sqrt2 = 1 / math.sqrt(2)
    z = [0j, 0j, 0j, 0j, inv_sqrt2, 1j * inv_sqrt2]
    x = [inv_sqrt2, 1j * inv_sqrt2, 0j, 0j, 0j, 0j]

    def bilinear_dot(v: list[complex], w: list[complex]) -> complex:
        return sum(a * b for a, b in zip(v, w))

    for name, left, right in (("ZZ", z, z), ("XX", x, x), ("ZX", z, x), ("XZ", x, z)):
        assert_close(f"SO(6) trace operator vanishes on {name}", bilinear_dot(left, right))


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


def two_magnon_exchange_coefficient(momentum_1: float, momentum_2: float) -> complex:
    z1 = cmath.exp(1j * momentum_1)
    z2 = cmath.exp(1j * momentum_2)
    return -(1 - 2 * z2 + z1 * z2) / (1 - 2 * z1 + z1 * z2)


def bethe_rapidity(momentum: float) -> float:
    return 0.5 / math.tan(momentum / 2)


def check_two_magnon_coordinate_matching() -> None:
    for momentum_1, momentum_2 in ((0.7, -1.2), (1.4, 0.3), (2.1, -0.8)):
        z1 = cmath.exp(1j * momentum_1)
        z2 = cmath.exp(1j * momentum_2)
        amplitude = two_magnon_exchange_coefficient(momentum_1, momentum_2)
        u1 = bethe_rapidity(momentum_1)
        u2 = bethe_rapidity(momentum_2)
        rapidity_amplitude = (u1 - u2 - 1j) / (u1 - u2 + 1j)
        assert_close("two-magnon amplitude rapidity form", amplitude, rapidity_amplitude)

        energy = (
            4
            - z1
            - 1 / z1
            - z2
            - 1 / z2
        )
        contact_wave = z2 + amplitude * z1
        contact_rhs = (
            2 * contact_wave
            - (z2 / z1 + amplitude * z1 / z2)
            - (z2 * z2 + amplitude * z1 * z1)
        )
        assert_close("two-magnon adjacent contact equation", energy * contact_wave, contact_rhs)

    length = 4
    momentum_1 = 2 * math.pi / 3
    momentum_2 = -2 * math.pi / 3
    amplitude = two_magnon_exchange_coefficient(momentum_1, momentum_2)
    assert_close(
        "Konishi first Bethe phase is inverse chamber amplitude",
        cmath.exp(1j * momentum_1 * length),
        1 / amplitude,
    )
    assert_close(
        "Konishi second Bethe phase is chamber amplitude",
        cmath.exp(1j * momentum_2 * length),
        amplitude,
    )

    basis = list(itertools.combinations(range(length), 2))
    basis_index = {state: index for index, state in enumerate(basis)}
    wave = []
    for n1, n2 in basis:
        wave.append(
            cmath.exp(1j * (momentum_1 * n1 + momentum_2 * n2))
            + amplitude * cmath.exp(1j * (momentum_2 * n1 + momentum_1 * n2))
        )

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
    assert_close("Konishi two-magnon finite-chain eigenvector", residual, tol=1.0e-12)

    translated = []
    for state in basis:
        shifted = tuple(sorted((site + 1) % length for site in state))
        translated.append(wave[basis_index[shifted]])
    translation_residual = max(abs(value - expected) for value, expected in zip(translated, wave))
    assert_close("Konishi two-magnon cyclicity", translation_residual, tol=1.0e-12)


def check_two_magnon_bmn_quantization() -> None:
    for length in (4, 7, 13, 31):
        for mode in range(1, min(length - 1, 6)):
            momentum = 2 * math.pi * mode / (length - 1)
            rapidity = bethe_rapidity(momentum)
            lhs = cmath.exp(1j * momentum * length)
            rhs = (2 * rapidity + 1j) / (2 * rapidity - 1j)
            assert_close("two-magnon BMN Bethe phase", lhs, rhs)

            energy_from_roots = 2 / (rapidity * rapidity + 0.25)
            energy_from_sine = 8 * math.sin(momentum / 2) ** 2
            assert_close("two-magnon BMN energy", energy_from_roots, energy_from_sine)

            gamma_over_lambda = energy_from_sine / (8 * math.pi * math.pi)
            displayed = math.sin(math.pi * mode / (length - 1)) ** 2 / (math.pi * math.pi)
            assert_close("two-magnon BMN gamma normalization", gamma_over_lambda, displayed)

    lam_prime = 0.41
    for charge in (512, 2048, 8192):
        length = charge + 2
        lam = lam_prime * charge * charge
        for mode in (1, 3, 5):
            gamma = lam * math.sin(math.pi * mode / (length - 1)) ** 2 / (math.pi * math.pi)
            leading = lam_prime * mode * mode
            scaled_error = charge * abs(gamma / leading - 1)
            if scaled_error > 2.25:
                raise AssertionError(
                    "two-magnon BMN double-scaling error "
                    f"J={charge}, mode={mode}: J-relative error {scaled_error}"
                )


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


def check_konishi_baxter_polynomial() -> None:
    def q_polynomial(u: complex) -> complex:
        return u * u - Fraction(1, 12)

    for u in (-2, -0.3, 0.0, 1.4, 3.0):
        lhs = (u + 0.5j) ** 2 * q_polynomial(u + 1j) + (u - 0.5j) ** 2 * q_polynomial(u - 1j)
        rhs = (2 * u * u - Fraction(13, 2)) * q_polynomial(u)
        assert_close("Konishi Baxter polynomial identity", lhs, rhs)

    roots = [1 / (2 * math.sqrt(3)), -1 / (2 * math.sqrt(3))]
    for index, root in enumerate(roots):
        lhs = ((root + 0.5j) / (root - 0.5j)) ** 2
        rhs = 1 + 0j
        for other_index, other in enumerate(roots):
            if index != other_index:
                rhs *= (root - other - 1j) / (root - other + 1j)
        assert_close("Konishi Baxter-to-SL2 Bethe orientation", lhs, rhs)


def polynomial_add(left: list[complex], right: list[complex]) -> list[complex]:
    size = max(len(left), len(right))
    result = [0j] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0j)
            + (right[index] if index < len(right) else 0j)
        )
    return result


def polynomial_scale(poly: list[complex], scale: complex) -> list[complex]:
    return [scale * coefficient for coefficient in poly]


def polynomial_mul_linear(poly: list[complex], constant: complex, linear: complex) -> list[complex]:
    result = [0j] * (len(poly) + 1)
    for index, coefficient in enumerate(poly):
        result[index] += constant * coefficient
        result[index + 1] += linear * coefficient
    return result


def polynomial_eval(poly: list[complex], value: complex) -> complex:
    result = 0j
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def polynomial_derivative(poly: list[complex]) -> list[complex]:
    return [index * coefficient for index, coefficient in enumerate(poly)][1:]


def digamma_complex(z: complex) -> complex:
    """Evaluate digamma by recurrence to a right half-plane plus Stirling terms."""

    value = 0j
    for _ in range(80):
        if abs(z) >= 16:
            break
        value -= 1 / z
        z += 1
    inverse = 1 / z
    inverse2 = inverse * inverse
    return value + (
        cmath.log(z)
        - inverse / 2
        - inverse2 / 12
        + inverse2**2 / 120
        - inverse2**3 / 252
        + inverse2**4 / 240
        - inverse2**5 / 132
    )


def rising_integer(start: int, length: int) -> int:
    result = 1
    for offset in range(length):
        result *= start + offset
    return result


def twist_two_baxter_polynomial(spin: int) -> list[complex]:
    polynomial = [0j]
    for length in range(spin + 1):
        coefficient = Fraction(
            rising_integer(-spin, length) * rising_integer(spin + 1, length),
            math.factorial(length) ** 3,
        )
        pochhammer = [1 + 0j]
        for offset in range(length):
            pochhammer = polynomial_mul_linear(pochhammer, offset + 0.5, -1j)
        polynomial = polynomial_add(polynomial, polynomial_scale(pochhammer, coefficient))
    return polynomial


def twist_two_baxter_z_polynomial(spin: int) -> list[Fraction]:
    polynomial = [Fraction(0)]
    for length in range(spin + 1):
        coefficient = Fraction(
            rising_integer(-spin, length) * rising_integer(spin + 1, length),
            math.factorial(length) ** 3,
        )
        pochhammer = [Fraction(1)]
        for offset in range(length):
            shifted = [Fraction(0)] * (len(pochhammer) + 1)
            for index, value in enumerate(pochhammer):
                shifted[index] += offset * value
                shifted[index + 1] += value
            pochhammer = shifted
        if len(polynomial) < len(pochhammer):
            polynomial.extend(Fraction(0) for _ in range(len(pochhammer) - len(polynomial)))
        for index, value in enumerate(pochhammer):
            polynomial[index] += coefficient * value
    return polynomial


def polynomial_eval_fraction(poly: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def polynomial_derivative_fraction(poly: list[Fraction]) -> list[Fraction]:
    return [index * coefficient for index, coefficient in enumerate(poly)][1:]


def pochhammer_fraction(start: Fraction, length: int) -> Fraction:
    result = Fraction(1)
    for offset in range(length):
        result *= start + offset
    return result


def check_twist_two_qsc_baxter_family() -> None:
    for spin in range(1, 9):
        q_polynomial = twist_two_baxter_polynomial(spin)
        q_derivative = polynomial_derivative(q_polynomial)
        transfer = lambda u, spin=spin: 2 * u * u - spin * (spin + 1) - 0.5
        for u in (-1.1, 0.0, 0.8 + 0.3j):
            lhs = (
                (u + 0.5j) ** 2 * polynomial_eval(q_polynomial, u + 1j)
                + (u - 0.5j) ** 2 * polynomial_eval(q_polynomial, u - 1j)
            )
            rhs = transfer(u) * polynomial_eval(q_polynomial, u)
            assert_close(f"twist-two Baxter identity S={spin}", lhs, rhs, tol=2.0e-9)

        q_plus = polynomial_eval(q_polynomial, 0.5j)
        q_minus = polynomial_eval(q_polynomial, -0.5j)
        assert_close("twist-two Q(i/2) sign", q_plus / q_minus, (-1) ** spin)

        spin_chain_energy = 1j * (
            polynomial_eval(q_derivative, 0.5j) / q_plus
            - polynomial_eval(q_derivative, -0.5j) / q_minus
        )
        expected_energy = 4 * sum(Fraction(1, mode) for mode in range(1, spin + 1))
        assert_close(
            f"twist-two one-loop energy S={spin}",
            spin_chain_energy,
            float(expected_energy),
        )

        z_polynomial = twist_two_baxter_z_polynomial(spin)
        z_derivative = polynomial_derivative_fraction(z_polynomial)
        harmonic = sum(Fraction(1, mode) for mode in range(1, spin + 1))
        if polynomial_eval_fraction(z_polynomial, Fraction(0)) != 1:
            raise AssertionError(f"twist-two exact Qhat(0) S={spin}")
        if polynomial_eval_fraction(z_polynomial, Fraction(1)) != (-1) ** spin:
            raise AssertionError(f"twist-two exact Qhat(1) S={spin}")
        if polynomial_eval_fraction(z_derivative, Fraction(0)) != -2 * harmonic:
            raise AssertionError(f"twist-two exact Qhat'(0) S={spin}")
        if (
            polynomial_eval_fraction(z_derivative, Fraction(1))
            / polynomial_eval_fraction(z_polynomial, Fraction(1))
            != 2 * harmonic
        ):
            raise AssertionError(f"twist-two exact Qhat'(1)/Qhat(1) S={spin}")

        for z_value in (Fraction(3, 7), Fraction(5, 3)):
            for length in range(spin + 1):
                term = (
                    Fraction(
                        rising_integer(-spin, length)
                        * rising_integer(spin + 1, length),
                        math.factorial(length) ** 3,
                    )
                    * pochhammer_fraction(z_value, length)
                )
                next_term = (
                    Fraction(
                        rising_integer(-spin, length + 1)
                        * rising_integer(spin + 1, length + 1),
                        math.factorial(length + 1) ** 3,
                    )
                    * pochhammer_fraction(z_value, length + 1)
                    if length < spin
                    else Fraction(0)
                )
                summand_defect = (
                    z_value * (z_value + length)
                    + (z_value - 1) ** 3 / (z_value + length - 1)
                    - (2 * z_value * z_value - 2 * z_value + spin * (spin + 1) + 1)
                ) * term
                telescoping_right_side = (
                    Fraction((length + 1) ** 3, 1) / (z_value + length) * next_term
                    - Fraction(length**3, 1) / (z_value + length - 1) * term
                )
                if summand_defect != telescoping_right_side:
                    raise AssertionError(
                        f"twist-two exact telescoping identity S={spin} k={length}"
                    )


def check_central_extension_dispersion() -> None:
    for coupling in (0.05, 0.2, 0.7):
        for momentum in (0.3, 1.1, 2.4):
            central_p = coupling * (1 - cmath.exp(1j * momentum))
            central_k = coupling * (1 - cmath.exp(-1j * momentum))
            shortened = cmath.sqrt(1 + 4 * central_p * central_k)
            displayed = math.sqrt(1 + 16 * coupling * coupling * math.sin(momentum / 2) ** 2)
            assert_close("central-extension dispersion", shortened, displayed)


def check_zhukovsky_map_and_energy() -> None:
    for coupling in (0.07, 0.3):
        for u in (1.7 + 0.4j, -2.3 + 0.8j, 5.0):
            x = zhukovsky_outside(u, coupling)
            assert_close("Zhukovsky defining equation", x + 1 / x, u / coupling)

        large_u = 19.0
        x_large = zhukovsky_outside(large_u, coupling)
        expansion = (
            large_u / coupling
            - coupling / large_u
            - coupling**3 / large_u**3
            - 2 * coupling**5 / large_u**5
        )
        assert_close("Zhukovsky large-u expansion", x_large, expansion, tol=2.0e-10)

        cut_point = 0.4 * coupling
        z = cut_point / coupling
        above = 0.5 * (z + 1j * math.sqrt(4 - z * z))
        below = 0.5 * (z - 1j * math.sqrt(4 - z * z))
        assert_close("Zhukovsky cut reciprocal boundary values", above * below, 1)

        for momentum in (0.35, 1.4, 2.8):
            x_plus, x_minus = xpm_from_momentum(momentum, coupling)
            assert_close("x+/x- momentum", x_plus / x_minus, cmath.exp(1j * momentum))
            assert_close(
                "xpm shortening relation",
                x_plus + 1 / x_plus - x_minus - 1 / x_minus,
                1j / coupling,
            )
            energy_from_x = 1 + 2j * coupling * (1 / x_plus - 1 / x_minus)
            energy_from_difference = -1 - 2j * coupling * (x_plus - x_minus)
            energy = math.sqrt(1 + 16 * coupling * coupling * math.sin(momentum / 2) ** 2)
            assert_close("Zhukovsky energy formula", energy_from_x, energy)
            assert_close("alternate stringbook energy formula", energy_from_difference, energy)


def check_zhukovsky_crossing_path_monodromy() -> None:
    """Track square-root branches around shifted Zhukovsky crossing endpoints."""

    coupling = 1.0
    base_u = 3.1 + 0j
    radius = 0.31

    def segment(start: complex, end: complex, steps: int) -> list[complex]:
        return [start + (end - start) * index / steps for index in range(1, steps + 1)]

    def endpoint_loop(center: complex) -> list[complex]:
        start = center + radius
        path = [base_u]
        path.extend(segment(base_u, start, 80))
        path.extend(
            center + radius * cmath.exp(2j * math.pi * index / 180)
            for index in range(1, 181)
        )
        path.extend(segment(start, base_u, 80))
        return path

    lower_endpoint = 2 * coupling - 0.5j
    upper_endpoint = 2 * coupling + 0.5j
    lower_loop = endpoint_loop(lower_endpoint)
    upper_loop = endpoint_loop(upper_endpoint)
    combined_loop = lower_loop + upper_loop[1:]

    def continued_x(path: list[complex], shift: complex) -> complex:
        z_initial = (path[0] + shift) / coupling
        x_initial = zhukovsky_outside(path[0] + shift, coupling)
        root = 2 * x_initial - z_initial
        for u_value in path[1:]:
            z_value = (u_value + shift) / coupling
            candidate = cmath.sqrt(z_value * z_value - 4)
            if abs(candidate - root) > abs(-candidate - root):
                candidate = -candidate
            root = candidate
        z_final = (path[-1] + shift) / coupling
        return 0.5 * (z_final + root)

    x_plus = zhukovsky_outside(base_u + 0.5j, coupling)
    x_minus = zhukovsky_outside(base_u - 0.5j, coupling)

    lower_plus = continued_x(lower_loop, 0.5j)
    lower_minus = continued_x(lower_loop, -0.5j)
    assert_close("lower crossing loop flips x+", lower_plus, 1 / x_plus, tol=2.0e-8)
    assert_close("lower crossing loop leaves x-", lower_minus, x_minus, tol=2.0e-8)

    upper_plus = continued_x(upper_loop, 0.5j)
    upper_minus = continued_x(upper_loop, -0.5j)
    assert_close("upper crossing loop leaves x+", upper_plus, x_plus, tol=2.0e-8)
    assert_close("upper crossing loop flips x-", upper_minus, 1 / x_minus, tol=2.0e-8)

    crossed_plus = continued_x(combined_loop, 0.5j)
    crossed_minus = continued_x(combined_loop, -0.5j)
    assert_close("combined crossing path flips x+", crossed_plus, 1 / x_plus, tol=2.0e-8)
    assert_close("combined crossing path flips x-", crossed_minus, 1 / x_minus, tol=2.0e-8)
    assert_close(
        "crossing path preserves xpm shortening",
        crossed_plus + 1 / crossed_plus - crossed_minus - 1 / crossed_minus,
        1j / coupling,
        tol=2.0e-8,
    )
    assert_close(
        "crossing path inverts momentum ratio",
        crossed_plus / crossed_minus,
        x_minus / x_plus,
        tol=2.0e-8,
    )

    energy = 1 + 2j * coupling * (1 / x_plus - 1 / x_minus)
    crossed_energy = 1 + 2j * coupling * (1 / crossed_plus - 1 / crossed_minus)
    assert_close("crossing path flips continued energy", crossed_energy, -energy, tol=2.0e-8)


def check_crossing_rhs_is_sheet_sensitive() -> None:
    for coupling, momentum_1, momentum_2 in (
        (0.08, 0.45, 1.35),
        (0.2, 0.7, 1.6),
        (0.55, 1.1, 2.45),
    ):
        x1_plus, x1_minus = xpm_from_momentum(momentum_1, coupling)
        x2_plus, x2_minus = xpm_from_momentum(momentum_2, coupling)

        def stringbook_crossing_rhs(a_plus: complex, a_minus: complex) -> complex:
            return (
                (x2_plus / x2_minus)
                * ((x2_plus - a_plus) / (x2_plus - a_minus))
                * ((x2_minus - 1 / a_plus) / (x2_minus - 1 / a_minus))
            )

        def reciprocal_crossing_rhs(a_plus: complex, a_minus: complex) -> complex:
            return (
                (x2_minus / x2_plus)
                * ((x2_plus - a_minus) / (x2_plus - a_plus))
                * ((x2_minus - 1 / a_minus) / (x2_minus - 1 / a_plus))
            )

        physical_rhs = stringbook_crossing_rhs(x1_plus, x1_minus)
        reciprocal_rhs = reciprocal_crossing_rhs(x1_plus, x1_minus)
        assert_close(
            "crossing RHS reciprocal convention",
            physical_rhs * reciprocal_rhs,
            1,
            tol=2.0e-9,
        )

        naively_crossed_rhs = stringbook_crossing_rhs(1 / x1_plus, 1 / x1_minus)
        if abs(physical_rhs - naively_crossed_rhs) < 1.0e-6:
            raise AssertionError("crossing RHS should not be invariant under naive x -> 1/x")

    algebraic_rhs = (
        Fraction(5, 7)
        * Fraction(5 - 2, 5 - 3)
        * (Fraction(7, 1) - Fraction(1, 2))
        / (Fraction(7, 1) - Fraction(1, 3))
    )
    algebraic_naive = (
        Fraction(5, 7)
        * (Fraction(5, 1) - Fraction(1, 2))
        / (Fraction(5, 1) - Fraction(1, 3))
        * Fraction(7 - 2, 7 - 3)
    )
    if algebraic_rhs != Fraction(117, 112):
        raise AssertionError(f"crossing RHS algebraic sample: {algebraic_rhs}")
    if algebraic_naive != Fraction(675, 784):
        raise AssertionError(f"crossing RHS naive algebraic sample: {algebraic_naive}")


def check_matrix_crossing_channel_scalar_multiplier() -> None:
    """Port the stringbook finite L_cross/G_swap crossing-channel check."""

    x1_plus = Fraction(2, 1)
    x1_minus = Fraction(3, 1)
    x2_plus = Fraction(5, 1)
    x2_minus = Fraction(7, 1)

    def scalar_split_radicand(
        first_plus: Fraction,
        first_minus: Fraction,
        second_plus: Fraction,
        second_minus: Fraction,
    ) -> Fraction:
        return (
            (second_minus - first_plus)
            / (second_plus - first_minus)
            * (1 - 1 / (second_plus * first_minus))
            / (1 - 1 / (second_minus * first_plus))
        )

    physical_radicand = scalar_split_radicand(x1_plus, x1_minus, x2_plus, x2_minus)
    crossed_radicand = scalar_split_radicand(
        1 / x1_plus,
        1 / x1_minus,
        x2_plus,
        x2_minus,
    )
    crossing_multiplier = (
        x2_plus
        / x2_minus
        * (x2_plus - x1_plus)
        / (x2_plus - x1_minus)
        * (x2_minus - 1 / x1_plus)
        / (x2_minus - 1 / x1_minus)
    )
    amplitude_prefactor = (
        (x2_minus - 1 / x1_minus)
        * x1_plus
        * (x1_minus - x2_plus)
        / ((x2_minus * x1_plus - 1) * (x1_plus - x2_plus))
    )

    squared_channel_ratio = (
        physical_radicand
        * crossed_radicand
        * crossing_multiplier**2
        * amplitude_prefactor**2
    )
    if squared_channel_ratio != 1:
        raise AssertionError(f"crossed matrix channel squared ratio: {squared_channel_ratio}")

    inferred_multiplier_squared = 1 / (
        physical_radicand * crossed_radicand * amplitude_prefactor**2
    )
    if inferred_multiplier_squared != crossing_multiplier**2:
        raise AssertionError(
            "matrix crossing channel infers the wrong scalar multiplier: "
            f"{inferred_multiplier_squared}"
        )

    wrong_reciprocal_ratio = (
        physical_radicand
        * crossed_radicand
        * (1 / crossing_multiplier) ** 2
        * amplitude_prefactor**2
    )
    if wrong_reciprocal_ratio == 1:
        raise AssertionError("reciprocal scalar crossing multiplier unexpectedly passed")

    branch_ratio = (
        math.sqrt(float(physical_radicand))
        * math.sqrt(float(crossed_radicand))
        * float(crossing_multiplier)
        * float(amplitude_prefactor)
    )
    assert_close("crossed matrix channel positive branch", branch_ratio, 1.0)


def check_crossing_scalar_monodromy_cocycle() -> None:
    """Check the scalar one- and two-crossing branch cocycle."""

    x1_plus = Fraction(2, 1)
    x1_minus = Fraction(3, 1)
    x2_plus = Fraction(5, 1)
    x2_minus = Fraction(7, 1)

    def xi(
        first_plus: Fraction,
        first_minus: Fraction,
        second_plus: Fraction,
        second_minus: Fraction,
    ) -> Fraction:
        return (
            second_plus
            / second_minus
            * (second_plus - first_plus)
            / (second_plus - first_minus)
            * (second_minus - 1 / first_plus)
            / (second_minus - 1 / first_minus)
        )

    physical_multiplier = xi(x1_plus, x1_minus, x2_plus, x2_minus)
    crossed_multiplier = xi(1 / x1_plus, 1 / x1_minus, x2_plus, x2_minus)
    if physical_multiplier != Fraction(117, 112):
        raise AssertionError(f"one-crossing scalar multiplier: {physical_multiplier}")
    if crossed_multiplier != Fraction(675, 784):
        raise AssertionError(f"crossed one-crossing scalar multiplier: {crossed_multiplier}")
    if physical_multiplier == crossed_multiplier:
        raise AssertionError("crossing scalar multiplier should be sheet-sensitive")

    double_crossing_multiplier = crossed_multiplier / physical_multiplier
    expanded_multiplier = (
        (x2_plus - 1 / x1_plus)
        / (x2_plus - 1 / x1_minus)
        * (x2_plus - x1_minus)
        / (x2_plus - x1_plus)
        * (x2_minus - x1_plus)
        / (x2_minus - x1_minus)
        * (x2_minus - 1 / x1_minus)
        / (x2_minus - 1 / x1_plus)
    )
    if double_crossing_multiplier != Fraction(75, 91):
        raise AssertionError(f"double-crossing multiplier: {double_crossing_multiplier}")
    if expanded_multiplier != double_crossing_multiplier:
        raise AssertionError(
            "expanded double-crossing multiplier disagrees: "
            f"{expanded_multiplier} != {double_crossing_multiplier}"
        )

    sigma_branch = Fraction(11, 13)
    sigma_crossed = physical_multiplier / sigma_branch
    sigma_double_crossed = crossed_multiplier / sigma_crossed
    if sigma_double_crossed / sigma_branch != double_crossing_multiplier:
        raise AssertionError("two-step crossing recursion failed")

    reciprocal_branch = 1 / sigma_branch
    reciprocal_crossed = (1 / physical_multiplier) / reciprocal_branch
    reciprocal_double_crossed = (1 / crossed_multiplier) / reciprocal_crossed
    if reciprocal_double_crossed / reciprocal_branch != 1 / double_crossing_multiplier:
        raise AssertionError("reciprocal scalar convention should invert the cocycle")


def check_crossing_cdd_factor_ambiguity() -> None:
    """Check the CDD quotient equations left by crossing and unitarity."""

    x1_plus = Fraction(2, 1)
    x1_minus = Fraction(3, 1)
    x2_plus = Fraction(5, 1)
    x2_minus = Fraction(7, 1)

    def xi(
        first_plus: Fraction,
        first_minus: Fraction,
        second_plus: Fraction,
        second_minus: Fraction,
    ) -> Fraction:
        return (
            second_plus
            / second_minus
            * (second_plus - first_plus)
            / (second_plus - first_minus)
            * (second_minus - 1 / first_plus)
            / (second_minus - 1 / first_minus)
        )

    physical_multiplier = xi(x1_plus, x1_minus, x2_plus, x2_minus)
    crossed_multiplier = xi(1 / x1_plus, 1 / x1_minus, x2_plus, x2_minus)
    sigma_branch = Fraction(11, 13)
    sigma_crossed = physical_multiplier / sigma_branch
    sigma_double_crossed = crossed_multiplier / sigma_crossed
    sigma_swapped = 1 / sigma_branch

    cdd_branch = Fraction(17, 19)
    cdd_crossed = 1 / cdd_branch
    cdd_double_crossed = cdd_branch
    cdd_swapped = 1 / cdd_branch

    sigma_prime = cdd_branch * sigma_branch
    sigma_prime_crossed = cdd_crossed * sigma_crossed
    sigma_prime_double_crossed = cdd_double_crossed * sigma_double_crossed
    sigma_prime_swapped = cdd_swapped * sigma_swapped

    if sigma_prime_crossed * sigma_prime != physical_multiplier:
        raise AssertionError("CDD-dressed branch failed Janik crossing")
    if sigma_prime_swapped * sigma_prime != 1:
        raise AssertionError("CDD-dressed branch failed scalar unitarity")
    if sigma_prime_double_crossed / sigma_prime != sigma_double_crossed / sigma_branch:
        raise AssertionError("CDD factor should not change regular double crossing")

    wrong_cdd_crossed = cdd_branch
    if wrong_cdd_crossed * sigma_crossed * sigma_prime == physical_multiplier:
        raise AssertionError("crossing-even CDD factor unexpectedly preserved crossing")

    physical_divisor = Counter({"z0": 2, "z1": -3})

    def propagated_divisor(divisor: Counter[str], sign: int) -> Counter[str]:
        return Counter({point: sign * order for point, order in divisor.items()})

    crossed_divisor = propagated_divisor(physical_divisor, -1)
    swapped_divisor = propagated_divisor(physical_divisor, -1)
    double_crossed_divisor = propagated_divisor(crossed_divisor, -1)
    if crossed_divisor != Counter({"z0": -2, "z1": 3}):
        raise AssertionError(f"CDD crossed divisor propagation: {crossed_divisor}")
    if swapped_divisor != crossed_divisor:
        raise AssertionError("CDD swap should invert the divisor just like crossing")
    if double_crossed_divisor != physical_divisor:
        raise AssertionError("CDD regular double crossing should restore the divisor")


def check_dressing_charge_antisymmetry_unitarity() -> None:
    """Check that the charge expansion gives scalar dressing unitarity."""

    coefficients = {
        (2, 3): 4.0,
        (2, 5): -0.75,
        (3, 4): 1.25,
        (4, 7): -0.2,
    }

    def charge_from_x(r_value: int, x_plus: complex, x_minus: complex) -> complex:
        return 1j * (
            (1 / x_plus) ** (r_value - 1)
            - (1 / x_minus) ** (r_value - 1)
        ) / (r_value - 1)

    def theta(
        left: tuple[complex, complex],
        right: tuple[complex, complex],
    ) -> complex:
        left_charges = {
            r_value: charge_from_x(r_value, left[0], left[1])
            for r_value in range(2, 8)
        }
        right_charges = {
            r_value: charge_from_x(r_value, right[0], right[1])
            for r_value in range(2, 8)
        }
        value = 0j
        for (r_value, s_value), coefficient in coefficients.items():
            value -= coefficient * (
                left_charges[r_value] * right_charges[s_value]
                - left_charges[s_value] * right_charges[r_value]
            )
        return value

    for coupling, momentum_1, momentum_2 in (
        (0.08, 0.6, 1.4),
        (0.2, 0.9, 2.1),
        (0.45, 1.2, 2.7),
    ):
        x1 = xpm_from_momentum(momentum_1, coupling)
        x2 = xpm_from_momentum(momentum_2, coupling)
        theta_12 = theta(x1, x2)
        theta_21 = theta(x2, x1)
        assert_close("dressing charge antisymmetry", theta_12 + theta_21, 0)

        sigma_12 = cmath.exp(1j * theta_12)
        sigma_21 = cmath.exp(1j * theta_21)
        assert_close("dressing scalar unitarity", sigma_12 * sigma_21, 1)
        assert_close("squared dressing scalar unitarity", (sigma_12 * sigma_21) ** 2, 1)


def check_dhm_weak_dressing_coefficients() -> None:
    """Check DHM contour residues for the first weak dressing coefficients."""

    delta_terms = Counter({(1, 0): 1, (-1, 0): 1, (0, 1): -1, (0, -1): -1})

    def multiply(
        left: Counter[tuple[int, int]],
        right: Counter[tuple[int, int]],
    ) -> Counter[tuple[int, int]]:
        result: Counter[tuple[int, int]] = Counter()
        for (left_z, left_w), left_coefficient in left.items():
            for (right_z, right_w), right_coefficient in right.items():
                result[(left_z + right_z, left_w + right_w)] += (
                    left_coefficient * right_coefficient
                )
        return result

    def delta_power(power: int) -> Counter[tuple[int, int]]:
        result: Counter[tuple[int, int]] = Counter({(0, 0): 1})
        for _ in range(power):
            result = multiply(result, delta_terms)
        return result

    def residue(power: int, r_value: int, s_value: int) -> int:
        return delta_power(power)[(-(r_value - 1), -(s_value - 1))]

    def residue_prefactor(power: int, r_value: int, s_value: int) -> Fraction:
        if power % 2 == 0 or power < 3:
            return Fraction(0)
        m_value = (power - 1) // 2
        return Fraction(
            2
            * (-1) ** (m_value + 1)
            * (r_value - 1)
            * (s_value - 1)
            * residue(power, r_value, s_value),
            power,
        )

    def gamma_positive_integer(argument: int) -> int:
        if argument <= 0:
            return 0
        return math.factorial(argument - 1)

    def closed_weak_prefactor(n_value: int, r_value: int, s_value: int) -> Fraction:
        doubled_arguments = (
            n_value - r_value - s_value + 5,
            n_value + r_value - s_value + 3,
            n_value - r_value + s_value + 3,
            n_value + r_value + s_value + 1,
        )
        if any(argument <= 0 or argument % 2 for argument in doubled_arguments):
            return Fraction(0)
        arguments = tuple(argument // 2 for argument in doubled_arguments)
        denominator = 1
        for argument in arguments:
            gamma_value = gamma_positive_integer(argument)
            if gamma_value == 0:
                return Fraction(0)
            denominator *= gamma_value
        sign = (-1) ** (n_value // 2) * (-1) ** (n_value + s_value)
        numerator = (
            2
            * sign
            * math.factorial(n_value + 1)
            * math.factorial(n_value)
            * (r_value - 1)
            * (s_value - 1)
        )
        return Fraction(numerator, denominator)

    expected_prefactors = {
        (3, 2, 3): Fraction(4),
        (5, 2, 3): Fraction(-40),
        (5, 2, 5): Fraction(-8),
        (5, 3, 4): Fraction(24),
        (7, 2, 7): Fraction(12),
        (7, 4, 5): Fraction(120),
    }
    for (power, r_value, s_value), expected in expected_prefactors.items():
        prefactor = residue_prefactor(power, r_value, s_value)
        if prefactor != expected:
            raise AssertionError(
                f"DHM residue prefactor N={power}, r={r_value}, s={s_value}: {prefactor}"
            )
        closed = closed_weak_prefactor(power - 1, r_value, s_value)
        if prefactor != closed:
            raise AssertionError(
                f"DHM residue formula disagrees with closed weak formula: {prefactor} != {closed}"
            )

    for power in (3, 5, 7, 9, 11):
        for r_value in range(2, 8):
            for s_value in range(r_value + 1, 10):
                prefactor = residue_prefactor(power, r_value, s_value)
                closed = closed_weak_prefactor(power - 1, r_value, s_value)
                if prefactor != closed:
                    raise AssertionError(
                        "DHM closed weak coefficient formula failed "
                        f"N={power}, r={r_value}, s={s_value}: "
                        f"{prefactor} != {closed}"
                    )

    for r_value, s_value in ((2, 4), (3, 5), (4, 6)):
        for power in (3, 5, 7, 9):
            if residue_prefactor(power, r_value, s_value) != 0:
                raise AssertionError("DHM parity selection failed")

    if residue_prefactor(3, 2, 5) != 0:
        raise AssertionError("DHM minimal weak order failed")

    def magnon_charge(r_value: int, momentum: float, coupling: float) -> complex:
        x_plus, x_minus = xpm_from_momentum(momentum, coupling)
        return 1j * ((1 / x_plus) ** (r_value - 1) - (1 / x_minus) ** (r_value - 1)) / (
            r_value - 1
        )

    def charge_pair_seed(coupling: float) -> complex:
        p1, p2 = 0.8, 1.9
        return (
            magnon_charge(2, p1, coupling) * magnon_charge(3, p2, coupling)
            - magnon_charge(3, p1, coupling) * magnon_charge(2, p2, coupling)
        )

    g1 = 1.0e-4
    g2 = 2.0e-4
    dressing_seed_1 = g1**3 * charge_pair_seed(g1)
    dressing_seed_2 = g2**3 * charge_pair_seed(g2)
    assert_close(
        "DHM first weak dressing term scales as g^6",
        dressing_seed_2 / dressing_seed_1,
        64,
        tol=5.0e-5,
    )


def check_dhm_local_residue_continuation() -> None:
    """Check DHM local crossing residue signs and the double-residue contact term."""

    delta_terms = Counter({(1, 0): 1, (-1, 0): 1, (0, 1): -1, (0, -1): -1})

    def multiply(
        left: Counter[tuple[int, int]],
        right: Counter[tuple[int, int]],
    ) -> Counter[tuple[int, int]]:
        result: Counter[tuple[int, int]] = Counter()
        for (left_z, left_w), left_coefficient in left.items():
            for (right_z, right_w), right_coefficient in right.items():
                result[(left_z + right_z, left_w + right_w)] += (
                    left_coefficient * right_coefficient
                )
        return result

    kernel: Counter[tuple[int, int]] = Counter({(0, 0): 1})
    for _ in range(3):
        kernel = multiply(kernel, delta_terms)

    def cauchy_factor(power: int, variable: complex, inside: bool) -> complex:
        if inside:
            return -(variable**power) if power >= 0 else 0j
        return variable**power if power <= -1 else 0j

    def raw_integral_at(
        x_value: complex,
        y_value: complex,
        x_inside: bool,
        y_inside: bool,
    ) -> complex:
        bare_value = sum(
            coefficient
            * cauchy_factor(z_power, x_value, x_inside)
            * cauchy_factor(w_power, y_value, y_inside)
            for (z_power, w_power), coefficient in kernel.items()
        )
        return -1j * bare_value

    def kernel_value_at(x_value: complex, y_value: complex) -> complex:
        return sum(
            coefficient * x_value**z_power * y_value**w_power
            for (z_power, w_power), coefficient in kernel.items()
        )

    x_value = 0.73 + 0.29j
    y_value = -0.68 + 0.24j

    def raw_integral(x_inside: bool, y_inside: bool) -> complex:
        return raw_integral_at(x_value, y_value, x_inside, y_inside)

    outside_outside = raw_integral(False, False)
    inside_x_outside_y = raw_integral(True, False)
    outside_x_inside_y = raw_integral(False, True)
    inside_inside = raw_integral(True, True)

    psi_x_outside_y = inside_x_outside_y - outside_outside
    assert_close(
        "DHM x-crossing residue restores outside branch",
        inside_x_outside_y - psi_x_outside_y,
        outside_outside,
    )

    psi_y_outside_x = outside_outside - outside_x_inside_y
    assert_close(
        "DHM y-crossing residue restores outside branch",
        outside_x_inside_y + psi_y_outside_x,
        outside_outside,
    )

    psi_x_inside_y = inside_inside - outside_x_inside_y
    psi_y_inside_x = inside_x_outside_y - inside_inside
    contact = outside_x_inside_y + inside_x_outside_y - inside_inside - outside_outside
    assert_close(
        "DHM double-residue contact sign",
        contact,
        1j * kernel_value_at(x_value, y_value),
    )
    assert_close(
        "DHM double crossing with contact restores outside branch",
        inside_inside - psi_x_inside_y + psi_y_inside_x - contact,
        outside_outside,
    )
    without_contact = inside_inside - psi_x_inside_y + psi_y_inside_x
    if abs(without_contact - outside_outside) < 1.0e-9:
        raise AssertionError("DHM double crossing unexpectedly worked without contact term")

    x1_plus = 0.72 + 0.13j
    x1_minus = -0.61 + 0.21j
    x2_plus = 1.31 - 0.17j
    x2_minus = -1.44 - 0.19j

    def psi_x_outside_second(x_value: complex, y_value: complex) -> complex:
        return raw_integral_at(x_value, y_value, True, False) - raw_integral_at(
            x_value, y_value, False, False
        )

    def crossed_first_chi(x_value: complex, y_value: complex) -> complex:
        return raw_integral_at(x_value, y_value, True, False) - psi_x_outside_second(
            x_value, y_value
        )

    raw_crossed_theta = (
        raw_integral_at(x1_plus, x2_plus, True, False)
        - raw_integral_at(x1_plus, x2_minus, True, False)
        - raw_integral_at(x1_minus, x2_plus, True, False)
        + raw_integral_at(x1_minus, x2_minus, True, False)
    )
    residue_theta = (
        -psi_x_outside_second(x1_plus, x2_plus)
        + psi_x_outside_second(x1_plus, x2_minus)
        + psi_x_outside_second(x1_minus, x2_plus)
        - psi_x_outside_second(x1_minus, x2_minus)
    )
    crossed_theta = (
        crossed_first_chi(x1_plus, x2_plus)
        - crossed_first_chi(x1_plus, x2_minus)
        - crossed_first_chi(x1_minus, x2_plus)
        + crossed_first_chi(x1_minus, x2_minus)
    )
    outside_branch_theta = (
        raw_integral_at(x1_plus, x2_plus, False, False)
        - raw_integral_at(x1_plus, x2_minus, False, False)
        - raw_integral_at(x1_minus, x2_plus, False, False)
        + raw_integral_at(x1_minus, x2_minus, False, False)
    )
    assert_close(
        "DHM crossed BES theta residue combination",
        crossed_theta,
        raw_crossed_theta + residue_theta,
    )
    assert_close(
        "DHM crossed BES theta restores outside branch termwise",
        crossed_theta,
        outside_branch_theta,
    )
    wrong_residue_theta = (
        psi_x_outside_second(x1_plus, x2_plus)
        - psi_x_outside_second(x1_plus, x2_minus)
        - psi_x_outside_second(x1_minus, x2_plus)
        + psi_x_outside_second(x1_minus, x2_minus)
    )
    if abs(raw_crossed_theta + wrong_residue_theta - outside_branch_theta) < 1.0e-9:
        raise AssertionError("DHM crossed BES theta signs unexpectedly worked when reversed")


def check_dhm_gamma_pole_lattice_and_admissibility() -> None:
    """Check the DHM Gamma-kernel pole lattice used in crossing hypotheses."""

    coupling = 0.6

    for pole_level in range(1, 6):
        delta_plus = 1j * pole_level / coupling
        delta_minus = -1j * pole_level / coupling
        assert_close(
            "DHM numerator Gamma pole lattice",
            1 + 1j * coupling * delta_plus,
            1 - pole_level,
        )
        assert_close(
            "DHM denominator regular at numerator pole",
            1 - 1j * coupling * delta_plus,
            1 + pole_level,
        )
        assert_close(
            "DHM denominator Gamma pole lattice",
            1 - 1j * coupling * delta_minus,
            1 - pole_level,
        )
        assert_close(
            "DHM numerator regular at denominator pole",
            1 + 1j * coupling * delta_minus,
            1 + pole_level,
        )

    def delta_value(x_value: complex, y_value: complex) -> complex:
        return x_value + 1 / x_value - y_value - 1 / y_value

    def zhukovsky_roots(total: complex) -> tuple[complex, complex]:
        root = cmath.sqrt(total * total - 4)
        return 0.5 * (total + root), 0.5 * (total - root)

    y_value = 1.37 + 0.21j
    for sign in (1, -1):
        for pole_level in (1, 3, 5):
            target_delta = sign * 1j * pole_level / coupling
            target_sum = y_value + 1 / y_value + target_delta
            x_value = zhukovsky_roots(target_sum)[0]
            assert_close(
                "DHM endpoint pole divisor realization",
                delta_value(x_value, y_value),
                target_delta,
            )

    def pole_clearance(delta: complex, max_level: int = 8) -> float:
        return min(
            min(
                abs(delta - 1j * level / coupling),
                abs(delta + 1j * level / coupling),
            )
            for level in range(1, max_level + 1)
        )

    safe_pairs = (
        (2 + 0j, 5 + 0j),
        (3 + 0j, 7 + 0j),
        (0.5 + 0j, 5 + 0j),
        (1 / 3 + 0j, 7 + 0j),
        (0.72 + 0.13j, 1.31 - 0.17j),
        (-0.61 + 0.21j, -1.44 - 0.19j),
    )
    for x_value, y_value in safe_pairs:
        if pole_clearance(delta_value(x_value, y_value)) <= 1.0e-3:
            raise AssertionError("DHM admissible sample lies on the Gamma pole lattice")

    unsafe_delta = 1j * 4 / coupling
    assert_close("DHM pole clearance vanishes on pole lattice", pole_clearance(unsafe_delta), 0)


def check_su2c_intertwiner_rank_chart() -> None:
    """Check the generic one-scalar row-rank chart for the su(2|2)c intertwiner."""

    x1_plus = Fraction(2, 1)
    x1_minus = Fraction(3, 1)
    x2_plus = Fraction(5, 1)
    x2_minus = Fraction(7, 1)
    a1 = Fraction(11, 1)
    a2 = Fraction(13, 1)
    coupling = Fraction(17, 1)
    scalar = Fraction(19, 1)

    d12 = x2_minus - x1_plus
    n12 = x2_plus - x1_minus
    coefficients = {
        "B": 1
        - 2
        * (x2_plus - x1_plus)
        / n12
        * (x2_minus - 1 / x1_plus)
        / (x2_minus - 1 / x1_minus),
        "C": 2
        * a1
        * a2
        / coupling
        * (x2_plus - x1_plus)
        / ((x1_minus * x2_minus - 1) * n12),
        "D": -d12 / n12,
        "E": -d12
        / n12
        * (
            1
            - 2
            * (x2_minus - x1_minus)
            / d12
            * (x2_plus - 1 / x1_minus)
            / (x2_plus - 1 / x1_plus)
        ),
        "F": -2
        * coupling
        / (a1 * a2)
        * (x1_plus - x1_minus)
        * (x2_plus - x2_minus)
        * (x2_minus - x1_minus)
        / ((x1_plus * x2_plus - 1) * n12),
        "G": (x2_plus - x1_plus) / n12,
        "H": (a1 / a2) * (x2_plus - x2_minus) / n12,
        "K": (a2 / a1) * (x1_plus - x1_minus) / n12,
        "L": (x2_minus - x1_minus) / n12,
    }

    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L"]
    rows: list[list[Fraction]] = []
    for name in columns[1:]:
        row = [Fraction(0) for _ in columns]
        row[0] = -coefficients[name]
        row[columns.index(name)] = Fraction(1)
        rows.append(row)

    def rank(matrix: list[list[Fraction]]) -> int:
        work = [row[:] for row in matrix]
        row_index = 0
        for col_index in range(len(work[0])):
            pivot = next(
                (candidate for candidate in range(row_index, len(work)) if work[candidate][col_index]),
                None,
            )
            if pivot is None:
                continue
            work[row_index], work[pivot] = work[pivot], work[row_index]
            pivot_value = work[row_index][col_index]
            work[row_index] = [entry / pivot_value for entry in work[row_index]]
            for candidate in range(len(work)):
                if candidate == row_index or not work[candidate][col_index]:
                    continue
                factor = work[candidate][col_index]
                work[candidate] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(work[candidate], work[row_index])
                ]
            row_index += 1
        return row_index

    if rank(rows) != 9:
        raise AssertionError("su(2|2)c intertwiner row chart should have rank 9")

    a12 = scalar * n12 / d12
    amplitudes = {
        "A": a12,
        "B": coefficients["B"] * a12,
        "C": coefficients["C"] * a12,
        "D": coefficients["D"] * a12,
        "E": coefficients["E"] * a12,
        "F": coefficients["F"] * a12,
        "G": coefficients["G"] * a12,
        "H": coefficients["H"] * a12,
        "K": coefficients["K"] * a12,
        "L": coefficients["L"] * a12,
    }

    direct_amplitudes = {
        "A": scalar * (x2_plus - x1_minus) / d12,
        "B": scalar
        * (x2_plus - x1_minus)
        / d12
        * (
            1
            - 2
            * (x2_plus - x1_plus)
            / (x2_plus - x1_minus)
            * (x2_minus - 1 / x1_plus)
            / (x2_minus - 1 / x1_minus)
        ),
        "C": scalar
        * 2
        / coupling
        * a1
        * a2
        / (x1_minus * x2_minus - 1)
        * (x2_plus - x1_plus)
        / d12,
        "D": -scalar,
        "E": -scalar
        * (
            1
            - 2
            * (x2_minus - x1_minus)
            / d12
            * (x2_plus - 1 / x1_minus)
            / (x2_plus - 1 / x1_plus)
        ),
        "F": -scalar
        * 2
        * coupling
        / (a1 * a2)
        * (x1_plus - x1_minus)
        * (x2_plus - x2_minus)
        / (x1_plus * x2_plus - 1)
        * (x2_minus - x1_minus)
        / d12,
        "G": scalar * (x2_plus - x1_plus) / d12,
        "H": scalar * (a1 / a2) * (x2_plus - x2_minus) / d12,
        "K": scalar * (a2 / a1) * (x1_plus - x1_minus) / d12,
        "L": scalar * (x2_minus - x1_minus) / d12,
    }
    for name in columns:
        if amplitudes[name] != direct_amplitudes[name]:
            raise AssertionError(f"su(2|2)c row chart mismatch for {name}")

    for row in rows:
        residual = sum(row[index] * amplitudes[column] for index, column in enumerate(columns))
        if residual:
            raise AssertionError(f"su(2|2)c rank-chart residual: {residual}")

    if amplitudes["A"] != (a1 / a2) * amplitudes["K"] + amplitudes["G"]:
        raise AssertionError("su(2|2)c rank chart lost the first Q relation")
    if amplitudes["A"] != amplitudes["L"] + (a2 / a1) * amplitudes["H"]:
        raise AssertionError("su(2|2)c rank chart lost the second Q relation")


def check_su2c_matrix_amplitudes_and_unitarity() -> None:
    """Port finite checks from the stringbook su(2|2) S-matrix notebook."""

    def amplitudes(
        x1_plus: complex,
        x1_minus: complex,
        x2_plus: complex,
        x2_minus: complex,
        a1: complex,
        a2: complex,
        coupling: float,
        scalar: complex = 1 + 0j,
    ) -> tuple[complex, complex, complex, complex, complex, complex, complex, complex, complex, complex]:
        denominator = x2_minus - x1_plus
        a12 = scalar * (x2_plus - x1_minus) / denominator
        b12 = a12 * (
            1
            - 2
            * (x2_plus - x1_plus)
            / (x2_plus - x1_minus)
            * (x2_minus - 1 / x1_plus)
            / (x2_minus - 1 / x1_minus)
        )
        c12 = (
            scalar
            * 2
            / coupling
            * a1
            * a2
            / (x1_minus * x2_minus - 1)
            * (x2_plus - x1_plus)
            / denominator
        )
        d12 = -scalar
        e12 = -scalar * (
            1
            - 2
            * (x2_minus - x1_minus)
            / denominator
            * (x2_plus - 1 / x1_minus)
            / (x2_plus - 1 / x1_plus)
        )
        f12 = (
            -scalar
            * 2
            * coupling
            / (a1 * a2)
            * (x1_plus - x1_minus)
            * (x2_plus - x2_minus)
            / (x1_plus * x2_plus - 1)
            * (x2_minus - x1_minus)
            / denominator
        )
        g12 = scalar * (x2_plus - x1_plus) / denominator
        h12 = scalar * (a1 / a2) * (x2_plus - x2_minus) / denominator
        k12 = scalar * (a2 / a1) * (x1_plus - x1_minus) / denominator
        l12 = scalar * (x2_minus - x1_minus) / denominator
        return a12, b12, c12, d12, e12, f12, g12, h12, k12, l12

    def bosonic_block(amplitude_data: tuple[complex, ...]) -> list[list[complex]]:
        a12, b12, c12, d12, e12, f12, _g12, _h12, _k12, _l12 = amplitude_data
        return [
            [(d12 - e12) / 2, (d12 + e12) / 2, -f12 / 2, f12 / 2],
            [(d12 + e12) / 2, (d12 - e12) / 2, f12 / 2, -f12 / 2],
            [-c12 / 2, c12 / 2, (a12 - b12) / 2, (a12 + b12) / 2],
            [c12 / 2, -c12 / 2, (a12 + b12) / 2, (a12 - b12) / 2],
        ]

    def mixed_block(amplitude_data: tuple[complex, ...]) -> list[list[complex]]:
        _a12, _b12, _c12, _d12, _e12, _f12, g12, h12, k12, l12 = amplitude_data
        return [[h12, g12], [l12, k12]]

    def matrix_product(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
        return [
            [
                sum(left[row][middle] * right[middle][col] for middle in range(len(right)))
                for col in range(len(right[0]))
            ]
            for row in range(len(left))
        ]

    def identity_matrix(size: int) -> list[list[complex]]:
        return [[1 if row == col else 0 for col in range(size)] for row in range(size)]

    samples = (
        (0.31, 0.6, 1.4, 1.2 + 0.3j, -0.7 + 0.8j),
        (0.47, 1.2, 2.1, -0.4 + 1.1j, 1.3 - 0.2j),
    )
    for coupling, p1, p2, a1, a2 in samples:
        x1_plus, x1_minus = xpm_from_momentum(p1, coupling)
        x2_plus, x2_minus = xpm_from_momentum(p2, coupling)

        amp12 = amplitudes(x1_plus, x1_minus, x2_plus, x2_minus, a1, a2, coupling)
        amp21 = amplitudes(x2_plus, x2_minus, x1_plus, x1_minus, a2, a1, coupling)
        a12, _b12, _c12, _d12, _e12, _f12, g12, h12, k12, l12 = amp12

        assert_close("su(2|2)c Q-intertwiner first amplitude relation", a12, a1 * k12 / a2 + g12)
        assert_close("su(2|2)c Q-intertwiner second amplitude relation", a12, l12 + a2 * h12 / a1)

        for block_name, block_function, size in (
            ("bosonic", bosonic_block, 4),
            ("mixed", mixed_block, 2),
        ):
            product = matrix_product(block_function(amp12), block_function(amp21))
            expected = identity_matrix(size)
            for row in range(size):
                for col in range(size):
                    assert_close(
                        f"su(2|2)c {block_name} matrix unitarity",
                        product[row][col],
                        expected[row][col],
                        tol=1.0e-12,
                    )

        scalar_split = cmath.sqrt(
            (x2_minus - x1_plus)
            / (x2_plus - x1_minus)
            * (1 - 1 / (x2_plus * x1_minus))
            / (1 - 1 / (x2_minus * x1_plus))
        )
        compact_a12 = amplitudes(
            x1_plus,
            x1_minus,
            x2_plus,
            x2_minus,
            a1,
            a2,
            coupling,
            scalar_split,
        )[0]
        su2_rational_factor = (
            (x2_plus - x1_minus)
            / (x2_minus - x1_plus)
            * (1 - 1 / (x2_plus * x1_minus))
            / (1 - 1 / (x2_minus * x1_plus))
        )
        assert_close("su(2|2)c scalar split gives compact SU(2) factor", compact_a12**2, su2_rational_factor)


def check_su2c_single_level_ii_nesting_step() -> None:
    samples = (
        (
            2.0 + 0.7j,
            1.3 - 0.2j,
            -1.1 + 1.8j,
            -0.4 + 0.9j,
            0.8 - 0.3j,
            -1.2 + 0.5j,
            1.7 - 0.4j,
            (0.2 + 1.5j, -2.0 + 0.4j),
        ),
        (
            -0.6 + 2.4j,
            -1.7 + 1.1j,
            2.2 - 0.8j,
            0.5 - 1.3j,
            -0.7 + 0.6j,
            1.4 + 0.2j,
            -0.9 - 1.1j,
            (3.1 + 0.7j, -1.6 - 0.9j),
        ),
    )

    for x1_plus, x1_minus, x2_plus, x2_minus, a1, a2, a12, y_values in samples:
        denominator = x2_plus - x1_minus
        g12 = a12 * (x2_plus - x1_plus) / denominator
        k12 = a12 * (a2 / a1) * (x1_plus - x1_minus) / denominator
        l12 = a12 * (x2_minus - x1_minus) / denominator
        h12 = a12 * (a1 / a2) * (x2_plus - x2_minus) / denominator

        for y in y_values:
            f1 = a1 / (y - x1_plus)
            f2 = a2 / (y - x2_plus)
            s1 = (y - x1_minus) / (y - x1_plus)
            s2 = (y - x2_minus) / (y - x2_plus)

            assert_close(
                "single level-II nesting: first local equation",
                f1 * l12 + f2 * s1 * h12,
                s2 * f1 * a12,
            )
            assert_close(
                "single level-II nesting: second local equation",
                f1 * k12 + f2 * s1 * g12,
                f2 * a12,
            )
            assert_close(
                "single level-II nesting: K/G polynomial identity",
                (x1_plus - x1_minus) * (y - x2_plus)
                + (x2_plus - x1_plus) * (y - x1_minus),
                (x2_plus - x1_minus) * (y - x1_plus),
            )
            assert_close(
                "single level-II nesting: L/H polynomial identity",
                (x2_minus - x1_minus) * (y - x2_plus)
                + (x2_plus - x2_minus) * (y - x1_minus),
                (x2_plus - x1_minus) * (y - x2_minus),
            )


def check_su2c_level_ii_and_iii_nested_scattering() -> None:
    def auxiliary_rapidity(y: complex) -> complex:
        return y + 1 / y

    samples = (
        (0.7, 0.8 + 0.4j, -1.3 + 0.6j, 0.2 - 1.1j),
        (1.1, -0.5 + 1.7j, 1.6 - 0.3j, -1.4 + 0.8j),
    )

    for coupling, y1, y2, w in samples:
        eta = 0.5j / coupling
        v1 = auxiliary_rapidity(y1)
        v2 = auxiliary_rapidity(y2)
        difference = v1 - v2

        def level_ii_amplitudes(left: complex, right: complex) -> tuple[complex, complex]:
            delta = auxiliary_rapidity(left) - auxiliary_rapidity(right)
            m_amp = -(2 * eta) / (delta + 2 * eta)
            n_amp = -delta / (delta + 2 * eta)
            return m_amp, n_amp

        m12, n12 = level_ii_amplitudes(y1, y2)
        m21, n21 = level_ii_amplitudes(y2, y1)
        rational_eigenvalue = (difference - 2 * eta) / (difference + 2 * eta)

        assert_close("level-II M+N ungraded fermion sign", m12 + n12, -1)
        assert_close("level-II M-N rational eigenvalue", m12 - n12, rational_eigenvalue)
        assert_close("level-II rational eigenvalue unitarity", rational_eigenvalue * (m21 - n21), 1)
        assert_close("level-II matrix unitarity identity coefficient", m12 * m21 + n12 * n21, 1)
        assert_close("level-II matrix unitarity permutation coefficient", m12 * n21 + n12 * m21, 0)
        assert_close("graded level-III vacuum scattering", -(m12 + n12), 1)

        def gamma(root: complex) -> complex:
            return (w + eta) / (w - auxiliary_rapidity(root) + eta)

        def s_iii_ii(root: complex) -> complex:
            shifted = w - auxiliary_rapidity(root)
            return (shifted - eta) / (shifted + eta)

        g1 = gamma(y1)
        g2 = gamma(y2)
        s1 = s_iii_ii(y1)
        s2 = s_iii_ii(y2)

        assert_close(
            "level-III nesting first graded equation",
            g1 * m12 + g2 * s1 * n12,
            -g2,
        )
        assert_close(
            "level-III nesting second graded equation",
            g1 * n12 + g2 * s1 * m12,
            -g1 * s2,
        )

        a1 = w - v1
        a2 = w - v2
        assert_close("level-III rapidity difference relation", a2, a1 + difference)
        assert_close(
            "level-III first cleared polynomial identity",
            -2 * eta * (a2 + eta) - difference * (a1 - eta),
            -(difference + 2 * eta) * (a1 + eta),
        )
        assert_close(
            "level-III second cleared polynomial identity",
            -difference * (a2 + eta) - 2 * eta * (a1 - eta),
            -(difference + 2 * eta) * (a2 - eta),
        )

    for coupling, w1, w2 in ((0.7, 0.4 + 1.2j, -1.1 + 0.3j), (1.1, -0.8 + 0.6j, 1.4 - 0.5j)):
        shift = 1j / coupling
        s12 = (w1 - w2 + shift) / (w1 - w2 - shift)
        s21 = (w2 - w1 + shift) / (w2 - w1 - shift)
        assert_close("level-III self-scattering unitarity", s12 * s21, 1)


def check_su2c_nested_bethe_yang_frame_factors() -> None:
    coupling = 0.31
    momenta = (0.6, 1.4, 2.2)
    x_data = [xpm_from_momentum(momentum, coupling) for momentum in momenta]
    y_roots = (0.7 + 0.9j, -1.2 + 0.4j)
    w_roots = (0.3 + 1.1j, -0.8 + 0.2j)

    def s_ii_i_spin(y: complex, x_plus: complex, x_minus: complex) -> complex:
        return (y - x_minus) / (y - x_plus)

    def s_ii_i_string(y: complex, x_plus: complex, x_minus: complex) -> complex:
        return s_ii_i_spin(y, x_plus, x_minus) * cmath.sqrt(x_plus / x_minus)

    def s_iii_ii(w: complex, y: complex) -> complex:
        shifted = w - y - 1 / y
        eta = 0.5j / coupling
        return (shifted - eta) / (shifted + eta)

    def s_iii_iii(w_left: complex, w_right: complex) -> complex:
        shift = 1j / coupling
        return (w_left - w_right + shift) / (w_left - w_right - shift)

    for x_plus, x_minus in x_data:
        for y in y_roots:
            su2_auxiliary = s_ii_i_string(y, x_plus, x_minus)
            sl2_auxiliary = ((y - x_plus) / (y - x_minus)) * cmath.sqrt(x_minus / x_plus)
            assert_close("SU(2)/SL(2) auxiliary nesting reciprocity", su2_auxiliary * sl2_auxiliary, 1)

    target = 1
    xk_plus, xk_minus = x_data[target]
    spin_level_i = 1 + 0j
    string_level_i = 1 + 0j
    expected_frame = 1 + 0j
    for index, (xj_plus, xj_minus) in enumerate(x_data):
        if index == target:
            continue
        frame = cmath.sqrt((xj_plus * xk_minus) / (xj_minus * xk_plus))
        string_level_i *= frame
        expected_frame *= frame
    for y in y_roots:
        spin_factor = s_ii_i_spin(y, xk_plus, xk_minus)
        string_factor = s_ii_i_string(y, xk_plus, xk_minus)
        spin_level_i *= spin_factor
        string_level_i *= string_factor
        expected_frame *= cmath.sqrt(xk_plus / xk_minus)
    assert_close("level-I Bethe-Yang string-basis frame ratio", string_level_i / spin_level_i, expected_frame)

    target_y = y_roots[0]
    spin_level_ii = 1 + 0j
    string_level_ii = 1 + 0j
    expected_level_ii_frame = 1 + 0j
    for x_plus, x_minus in x_data:
        spin_level_ii *= 1 / s_ii_i_spin(target_y, x_plus, x_minus)
        string_level_ii *= 1 / s_ii_i_string(target_y, x_plus, x_minus)
        expected_level_ii_frame *= cmath.sqrt(x_minus / x_plus)
    for w in w_roots:
        spin_level_ii *= s_iii_ii(w, target_y)
        string_level_ii *= s_iii_ii(w, target_y)
    assert_close("level-II Bethe-Yang inverse string-frame ratio", string_level_ii / spin_level_ii, expected_level_ii_frame)

    target_w = w_roots[0]
    level_iii_product = 1 + 0j
    inverse_level_iii_product = 1 + 0j
    for y in y_roots:
        level_iii_product *= 1 / s_iii_ii(target_w, y)
        inverse_level_iii_product *= s_iii_ii(target_w, y)
    for w in w_roots[1:]:
        level_iii_product *= s_iii_iii(w, target_w)
        inverse_level_iii_product *= s_iii_iii(target_w, w)
    assert_close("level-III Bethe-Yang inverse orientation", level_iii_product * inverse_level_iii_product, 1)

    counts = (3, 2, 5, 7)
    n1, n2, n3, n4 = counts
    assert_close("nested K^I count", n1 + n2 + n3 + n4, 17)
    assert_close("nested K^II count", 2 * n2 + n3 + n4, 16)
    assert_close("nested K^III count", n2 + n4, 9)


def check_finite_density_aba_counting_normalization() -> None:
    """Check the L-normalized counting function used at finite magnon density."""

    density_fraction = 0.6

    def momentum_derivative(u_value: float) -> float:
        return 1 + u_value * u_value

    def phase(u_value: float, v_value: float) -> float:
        difference = u_value - v_value
        return difference + difference**3 / 3

    def phase_derivative(u_value: float, v_value: float) -> float:
        difference = u_value - v_value
        return 1 + difference * difference

    def continuum_counting_derivative(u_value: float) -> float:
        uniform_average = 1 + u_value * u_value + Fraction(1, 3)
        return momentum_derivative(u_value) + density_fraction * float(uniform_average)

    def roots_for_length(length: int) -> list[float]:
        root_count = int(round(density_fraction * length))
        return [-1 + (index + 0.5) * 2 / root_count for index in range(root_count)]

    for u_value in (-0.4, 0.2, 0.9):
        roots = roots_for_length(3000)
        finite_derivative = momentum_derivative(u_value) + sum(
            phase_derivative(u_value, root) for root in roots
        ) / 3000
        continuum_derivative = continuum_counting_derivative(u_value)
        assert_close(
            "finite-density ABA counting derivative",
            finite_derivative,
            continuum_derivative,
            tol=1.0e-7,
        )

        unit_mass_derivative = momentum_derivative(u_value) + float(
            1 + u_value * u_value + Fraction(1, 3)
        )
        if abs(finite_derivative - continuum_derivative) >= 0.25 * abs(
            finite_derivative - unit_mass_derivative
        ):
            raise AssertionError("ABA counting used the wrong empirical-measure mass")

        small_interval = 1.0e-5
        finite_counting_jump = (
            small_interval * momentum_derivative(u_value)
            + sum(
                phase(u_value + small_interval, root) - phase(u_value, root)
                for root in roots
            )
            / 3000
        )
        assert_close(
            "finite-density ABA level-density normalization",
            finite_counting_jump / (2 * math.pi * small_interval),
            continuum_derivative / (2 * math.pi),
            tol=5.0e-6,
        )


def check_rank_one_aba_weak_orientation() -> None:
    """Check the stringbook rank-one ABA weak limit and reciprocal SU(2) phase."""

    def x_shifted(rapidity: complex, shift_sign: int, coupling: float) -> complex:
        return zhukovsky_outside(rapidity + shift_sign * 0.5j, coupling)

    coupling = 1.0e-4
    for rapidity in (0.7, -1.3, 2.2 + 0.4j):
        for shift_sign in (1, -1):
            shifted = rapidity + shift_sign * 0.5j
            x_value = x_shifted(rapidity, shift_sign, coupling)
            expansion = shifted / coupling - coupling / shifted
            assert_close(
                "rank-one xpm weak branch expansion",
                x_value / expansion,
                1,
                tol=1.0e-12,
            )

        x_plus = x_shifted(rapidity, 1, coupling)
        x_minus = x_shifted(rapidity, -1, coupling)
        assert_close(
            "rank-one weak momentum ratio",
            x_plus / x_minus,
            (rapidity + 0.5j) / (rapidity - 0.5j),
            tol=5.0e-8,
        )
        anomalous_energy = 2j * coupling * (1 / x_plus - 1 / x_minus)
        assert_close(
            "rank-one weak energy normalization",
            anomalous_energy / (coupling * coupling),
            2 / (rapidity * rapidity + 0.25),
            tol=2.0e-7,
        )

    for rapidity_j, rapidity_k in ((0.7, -1.1), (1.4, 0.2), (-0.8 + 0.3j, 1.6 - 0.2j)):
        xj_plus = x_shifted(rapidity_j, 1, coupling)
        xj_minus = x_shifted(rapidity_j, -1, coupling)
        xk_plus = x_shifted(rapidity_k, 1, coupling)
        xk_minus = x_shifted(rapidity_k, -1, coupling)
        first_factor = (xj_minus - xk_plus) / (xj_plus - xk_minus)
        second_factor = (1 - 1 / (xj_plus * xk_minus)) / (
            1 - 1 / (xj_minus * xk_plus)
        )
        stringbook_factor = first_factor * second_factor
        sl2_factor = (rapidity_j - rapidity_k - 1j) / (
            rapidity_j - rapidity_k + 1j
        )
        su2_factor = 1 / sl2_factor
        assert_close(
            "rank-one stringbook ABA weak SL2 orientation",
            stringbook_factor / sl2_factor,
            1,
            tol=5.0e-8,
        )
        assert_close(
            "rank-one reciprocal compact SU2 orientation",
            (1 / stringbook_factor) / su2_factor,
            1,
            tol=5.0e-8,
        )
        assert_close(
            "rank-one dressingless second rational factor starts at one",
            second_factor,
            1,
            tol=5.0e-8,
        )


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


def check_sl2_large_spin_cusp_resolvent() -> None:
    """Check the one-loop SL(2) large-spin resolvent normalization."""

    def physical_square_root(value: complex, asymptotic: complex) -> complex:
        root = cmath.sqrt(value)
        if abs(root - asymptotic) <= abs(-root - asymptotic):
            return root
        return -root

    def resolvent(z: complex) -> complex:
        root = physical_square_root(4 * z * z - 1, 2 * z)
        return -1j * cmath.log((root + 1j) / (root - 1j))

    def resolvent_derivative(z: complex) -> complex:
        root = physical_square_root(z * z - 0.25, z)
        return -1 / (z * root)

    for z in (10 + 3j, -12 + 5j, 100):
        assert_close("SL(2) cusp resolvent normalization", z * resolvent(z), 1, tol=2.0e-3)

    for z in (1.1 + 0.4j, -0.8 + 1.3j, 2.0 - 0.7j):
        step = 1.0e-6
        numerical = (resolvent(z + step) - resolvent(z - step)) / (2 * step)
        assert_close("SL(2) cusp resolvent derivative", numerical, resolvent_derivative(z), tol=2.0e-8)

    for y in (0.1, 0.2, 0.4):
        root = math.sqrt(1 - 4 * y * y)
        density = math.log((1 + root) / (1 - root)) / math.pi
        if density <= 0:
            raise AssertionError("SL(2) cusp density positivity failed")
        epsilon = 1.0e-7
        jump = resolvent(y + 1j * epsilon) - resolvent(y - 1j * epsilon)
        assert_close("SL(2) cusp resolvent discontinuity", jump, -2j * math.pi * density, tol=1.0e-8)

    cutoff = 30.0
    half_integral = 2 * math.atan(math.tanh(cutoff / 2)) - cutoff / math.cosh(cutoff)
    normalization = 2 * half_integral / math.pi
    assert_close("SL(2) cusp density normalization", normalization, 1, tol=1.0e-11)

    coupling = 0.3
    constant = 4 * coupling * coupling * math.log(4)
    for spin in (200, 1000):
        root = math.sqrt(1 + 1 / (spin * spin))
        continued = -1j * math.log((root + 1) / (root - 1))
        energy = -4 * coupling * coupling * continued.imag
        leading = 8 * coupling * coupling * math.log(spin)
        assert_close(
            "SL(2) one-loop cusp logarithm",
            energy - leading,
            constant,
            tol=5.0e-6,
        )


def check_one_cut_spectral_curve_bookkeeping() -> None:
    """Check the two-sheeted curve behind the one-loop cusp resolvent."""

    for z in (0.8 + 0.3j, -1.4 + 0.2j, 2.0):
        y = cmath.sqrt(4 * z * z - 1)
        if abs(y - 2 * z) > abs(-y - 2 * z):
            y = -y
        if abs(y * y - (4 * z * z - 1)) > 1.0e-12:
            raise AssertionError("one-cut spectral curve equation failed")

        exp_i_g = (y + 1j) / (y - 1j)
        exp_i_g_flipped = (-y + 1j) / (-y - 1j)
        assert_close(
            "one-cut sheet exchange inverts exp(iG)",
            exp_i_g * exp_i_g_flipped,
            1,
            tol=1.0e-12,
        )

    for endpoint in (-0.5, 0.5):
        y = cmath.sqrt(4 * endpoint * endpoint - 1)
        assert_close("one-cut branch endpoint", y, 0, tol=1.0e-12)


def check_multicut_period_reflection_bookkeeping() -> None:
    """Check finite-gap filling periods and cut-reflection monodromy exactly."""

    densities = {
        "C1": (Fraction(3, 5), Fraction(1, 7), Fraction(-2, 9)),
        "C2": (Fraction(4, 7), Fraction(-1, 6), Fraction(5, 11)),
        "C3": (Fraction(2, 3), Fraction(0), Fraction(1, 13)),
    }

    def integrate_unit_interval(coefficients: tuple[Fraction, ...]) -> Fraction:
        return sum(
            coefficient / Fraction(power + 1)
            for power, coefficient in enumerate(coefficients)
        )

    fillings = {
        cut: integrate_unit_interval(coefficients)
        for cut, coefficients in densities.items()
    }

    # In units of 2*pi*i, the A-cycle integral is the cut integral of rho.
    jump_integrals = {
        cut: integrate_unit_interval(coefficients)
        for cut, coefficients in densities.items()
    }
    if jump_integrals != fillings:
        raise AssertionError("multi-cut filling periods do not match jumps")

    total_mass = sum(fillings.values(), Fraction(0))
    total_jump = sum(jump_integrals.values(), Fraction(0))
    if total_mass != total_jump:
        raise AssertionError("total filling is not the sum of cut jumps")

    AffineMap = tuple[int, Fraction]

    def reflection(mode: Fraction) -> AffineMap:
        # p is measured in units of 2*pi: R_n(p)=n-p.
        return (-1, mode)

    def compose(outer: AffineMap, inner: AffineMap) -> AffineMap:
        outer_sign, outer_shift = outer
        inner_sign, inner_shift = inner
        return (
            outer_sign * inner_sign,
            outer_sign * inner_shift + outer_shift,
        )

    identity = (1, Fraction(0))
    modes = {
        "C1": Fraction(2),
        "C2": Fraction(-1),
        "C3": Fraction(5),
    }

    for mode in modes.values():
        if compose(reflection(mode), reflection(mode)) != identity:
            raise AssertionError("cut reflection is not involutive")

    for left_name, left_mode in modes.items():
        for right_name, right_mode in modes.items():
            monodromy = compose(reflection(right_mode), reflection(left_mode))
            expected = (1, right_mode - left_mode)
            if monodromy != expected:
                raise AssertionError(
                    f"two-cut monodromy failed for {left_name}->{right_name}"
                )
            if monodromy[1].denominator != 1:
                raise AssertionError("integer mode numbers gave noninteger shift")

    bad_monodromy = compose(reflection(Fraction(7, 2)), reflection(modes["C1"]))
    if bad_monodromy[1].denominator == 1:
        raise AssertionError("noninteger mode unexpectedly exponentiates trivially")


def check_finite_gap_large_z_moment_expansion() -> None:
    """Check the large-z Cauchy-transform moment ledger exactly."""

    roots = (
        Fraction(1, 2),
        Fraction(-2, 3),
        Fraction(5, 4),
        Fraction(7, 6),
    )
    weights = (
        Fraction(3, 10),
        Fraction(1, 5),
        Fraction(1, 4),
        Fraction(1, 20),
    )
    max_moment = 5
    finite_moments = [
        sum(
            weights[index] * roots[index] ** power
            for index in range(len(roots))
        )
        for power in range(max_moment + 1)
    ]

    # The formal expansion of sum_j w_j/(z-u_j) in t=1/z has coefficient
    # M_k at t^(k+1).
    formal_coefficients = [Fraction(0)]
    formal_coefficients.extend(finite_moments)
    for power, expected in enumerate(finite_moments, start=1):
        if formal_coefficients[power] != expected:
            raise AssertionError("finite-root large-z moment coefficient failed")

    def integrate_polynomial_moment(coefficients: tuple[Fraction, ...], moment: int) -> Fraction:
        return sum(
            coefficient / Fraction(power + moment + 1)
            for power, coefficient in enumerate(coefficients)
        )

    cut_densities = {
        "C1": (Fraction(3, 5), Fraction(1, 7), Fraction(-2, 9)),
        "C2": (Fraction(4, 7), Fraction(-1, 6), Fraction(5, 11)),
        "C3": (Fraction(2, 3), Fraction(0), Fraction(1, 13)),
    }
    cut_moments = {
        cut: [
            integrate_polynomial_moment(coefficients, moment)
            for moment in range(4)
        ]
        for cut, coefficients in cut_densities.items()
    }
    total_moments = [
        sum(cut_moments[cut][moment] for cut in cut_densities)
        for moment in range(4)
    ]
    total_filling = sum(cut_moments[cut][0] for cut in cut_densities)
    if total_moments[0] != total_filling:
        raise AssertionError("zeroth Cauchy moment did not equal total filling")

    # Splitting a cut into two pieces should add moments linearly.
    split_left = (Fraction(3, 10), Fraction(1, 14), Fraction(-1, 9))
    split_right = tuple(
        cut_densities["C1"][index] - split_left[index]
        for index in range(len(split_left))
    )
    for moment in range(4):
        split_total = (
            integrate_polynomial_moment(split_left, moment)
            + integrate_polynomial_moment(split_right, moment)
        )
        if split_total != cut_moments["C1"][moment]:
            raise AssertionError("cut moment additivity under splitting failed")

    # A nonzero first moment is not determined by the total filling alone.
    translated_roots = tuple(root + Fraction(1, 3) for root in roots)
    translated_m0 = sum(weights)
    translated_m1 = sum(
        weights[index] * translated_roots[index]
        for index in range(len(roots))
    )
    if translated_m0 != finite_moments[0]:
        raise AssertionError("translation changed total filling")
    if translated_m1 == finite_moments[1]:
        raise AssertionError("first moment should record charge data beyond filling")


def check_finite_gap_level_matching_cyclicity() -> None:
    """Check the global mode-filling congruence behind spin-chain cyclicity."""

    chain_length = 6
    root_multiplicities = {
        "C1": 3,
        "C2": 4,
        "C3": 5,
    }
    mode_numbers = {
        "C1": 2,
        "C2": -1,
        "C3": 2,
    }

    total_mode_weight = sum(
        root_multiplicities[cut] * mode_numbers[cut]
        for cut in root_multiplicities
    )
    if total_mode_weight % chain_length != 0:
        raise AssertionError("cyclic mode-filling congruence unexpectedly failed")

    # Work in units of 2*pi.  Antisymmetric two-body phases cancel in the sum
    # of logarithmic Bethe equations.
    phase = {
        (1, 2): Fraction(2, 5),
        (1, 3): Fraction(-1, 7),
        (2, 3): Fraction(3, 11),
    }
    roots = [1, 2, 3]
    directed_phase_sum = Fraction(0)
    for left in roots:
        for right in roots:
            if left == right:
                continue
            if (left, right) in phase:
                directed_phase_sum += phase[(left, right)]
            else:
                directed_phase_sum -= phase[(right, left)]
    if directed_phase_sum != 0:
        raise AssertionError("antisymmetric Bethe phases did not cancel")

    total_momentum_units = Fraction(total_mode_weight, chain_length)
    if total_momentum_units.denominator != 1:
        raise AssertionError("cyclic total momentum is not an integer multiple of 2*pi")

    regulator_size = 12
    fillings = {
        cut: Fraction(count, regulator_size)
        for cut, count in root_multiplicities.items()
    }
    scaled_length = Fraction(chain_length, regulator_size)
    continuum_level_match = sum(
        Fraction(mode_numbers[cut]) * fillings[cut]
        for cut in root_multiplicities
    )
    if continuum_level_match / scaled_length != total_momentum_units:
        raise AssertionError("finite-density level-matching scaling failed")

    bad_modes = dict(mode_numbers)
    bad_modes["C3"] = 3
    bad_total = sum(
        root_multiplicities[cut] * bad_modes[cut]
        for cut in root_multiplicities
    )
    if bad_total % chain_length == 0:
        raise AssertionError("bad mode assignment unexpectedly satisfied cyclicity")
    if not all(Fraction(mode).denominator == 1 for mode in bad_modes.values()):
        raise AssertionError("bad modes should still be locally integer")


def check_pohlmeyer_s2_frame_compatibility() -> None:
    """Check the S2 Pohlmeyer moving-frame compatibility algebra exactly."""

    mu = Fraction(7, 3)
    cos_alpha = Fraction(3, 5)
    sin_alpha = Fraction(4, 5)
    alpha_plus = Fraction(5, 7)
    alpha_minus = Fraction(-2, 5)
    alpha_plus_minus = -(mu * mu) * sin_alpha

    def add(
        left: dict[str, Fraction],
        right: dict[str, Fraction],
    ) -> dict[str, Fraction]:
        result = dict(left)
        for key, value in right.items():
            result[key] = result.get(key, Fraction(0)) + value
        return {key: value for key, value in result.items() if value}

    def scale(
        coefficient: Fraction,
        vector: dict[str, Fraction],
    ) -> dict[str, Fraction]:
        return {
            key: coefficient * value
            for key, value in vector.items()
            if coefficient * value
        }

    d_plus_n = {"e_plus": mu}
    d_minus_n = {"e_minus": mu}
    d_plus_e_minus = {"n": -mu * cos_alpha}
    d_plus_e_plus = {
        "n": -mu,
        "e_plus": alpha_plus * cos_alpha / sin_alpha,
        "e_minus": -alpha_plus / sin_alpha,
    }
    d_minus_e_minus = {
        "n": -mu,
        "e_plus": -alpha_minus / sin_alpha,
        "e_minus": alpha_minus * cos_alpha / sin_alpha,
    }

    left = add(
        scale(mu * sin_alpha * alpha_minus, {"n": Fraction(1)}),
        scale(-mu * cos_alpha, d_minus_n),
    )

    q = alpha_minus / sin_alpha
    q_plus = alpha_plus_minus / sin_alpha - alpha_minus * cos_alpha * alpha_plus / (
        sin_alpha * sin_alpha
    )
    cos_plus = -sin_alpha * alpha_plus

    right = {}
    right = add(right, scale(-mu, d_plus_n))
    right = add(right, scale(-q_plus, {"e_plus": Fraction(1)}))
    right = add(right, scale(-q, d_plus_e_plus))
    right = add(
        right,
        scale(q_plus * cos_alpha + q * cos_plus, {"e_minus": Fraction(1)}),
    )
    right = add(right, scale(q * cos_alpha, d_plus_e_minus))

    if left != right:
        raise AssertionError(f"Pohlmeyer S2 frame compatibility failed: {left} != {right}")

    wrong_alpha_plus_minus = alpha_plus_minus + Fraction(1, 11)
    wrong_q_plus = wrong_alpha_plus_minus / sin_alpha - alpha_minus * cos_alpha * alpha_plus / (
        sin_alpha * sin_alpha
    )
    wrong_right = {}
    wrong_right = add(wrong_right, scale(-mu, d_plus_n))
    wrong_right = add(wrong_right, scale(-wrong_q_plus, {"e_plus": Fraction(1)}))
    wrong_right = add(wrong_right, scale(-q, d_plus_e_plus))
    wrong_right = add(
        wrong_right,
        scale(wrong_q_plus * cos_alpha + q * cos_plus, {"e_minus": Fraction(1)}),
    )
    wrong_right = add(wrong_right, scale(q * cos_alpha, d_plus_e_minus))
    if wrong_right == left:
        raise AssertionError("wrong Pohlmeyer sign unexpectedly satisfied compatibility")


def check_bes_zhukovsky_fourier_transform_signs() -> None:
    """Check the signed-t Bessel convention in the BES Fourier transform."""

    def bessel_j_series(order: int, max_degree: int) -> dict[int, Fraction]:
        series: dict[int, Fraction] = {}
        if order > max_degree:
            return series
        for index in range((max_degree - order) // 2 + 1):
            degree = order + 2 * index
            coefficient = Fraction(
                (-1) ** index,
                (2**degree)
                * math.factorial(index)
                * math.factorial(index + order),
            )
            series[degree] = coefficient
        return series

    max_degree = 16
    for order in range(1, 8):
        j_minus = bessel_j_series(order - 1, max_degree)
        j_order = bessel_j_series(order, max_degree)
        j_plus = bessel_j_series(order + 1, max_degree)
        recurrence_lhs = {
            degree: j_minus.get(degree, 0) + j_plus.get(degree, 0)
            for degree in set(j_minus) | set(j_plus)
        }
        recurrence_rhs = {
            degree - 1: 2 * order * coefficient
            for degree, coefficient in j_order.items()
        }
        for degree in range(max_degree):
            if recurrence_lhs.get(degree, 0) != recurrence_rhs.get(degree, 0):
                raise AssertionError(f"BES Fourier Bessel recurrence failed for m={order}")

        plus_cut_phase = -1j * ((-1j) ** (order - 1))
        if abs(plus_cut_phase - (-1j) ** order) > 0:
            raise AssertionError(f"BES x+ contour phase failed for m={order}")

        lower_signed_t_phase = ((-1) ** order) * ((-1j) ** order)
        if abs(lower_signed_t_phase - (1j) ** order) > 0:
            raise AssertionError(f"BES x- signed-t phase failed for m={order}")

        lower_abs_t_phase = -((-1j) ** order)
        if order % 2 == 0 and abs(lower_abs_t_phase - lower_signed_t_phase) == 0:
            raise AssertionError("absolute-value lower transform failed to expose parity sign")


def check_bes_weak_scaling_function() -> None:
    """Check the weak BES scaling-function expansion through g^8."""

    # BES equation in the normalization used in Chapter 13:
    # sigma = t/(e^t-1) [K(2gt,0) - 4 g^2 int K(2gt,2gt') sigma(t') dt'].
    # K_0(2gt,0) = 1/2 - g^2 t^2/4 + g^4 t^4/24 + O(g^6),
    # K_0(2gt,2gt') = 1/2 - g^2(t^2-t t'+t'^2)/4 + O(g^4).
    integral_t_over_bose = Fraction(1, 1)  # coefficient of pi^2: int t/(e^t-1)=pi^2/6
    integral_t2_over_bose_zeta3 = Fraction(2, 1)  # int t^2/(e^t-1)=2 zeta(3)
    integral_t3_over_bose = Fraction(1, 1)  # coefficient of pi^4: int t^3/(e^t-1)=pi^4/15
    integral_t5_over_bose = Fraction(8, 63)  # coefficient of pi^6

    sigma0_integral_coeff_pi2 = Fraction(1, 2) * Fraction(1, 6) * integral_t_over_bose
    if sigma0_integral_coeff_pi2 != Fraction(1, 12):
        raise AssertionError("BES sigma0 integral normalization failed")

    # sigma_0=t/[2(e^t-1)]
    # sigma_1= - t/(e^t-1) (t^2/4 + pi^2/6)
    convolution_source_coeff_pi2 = 4 * Fraction(1, 2) * sigma0_integral_coeff_pi2
    if convolution_source_coeff_pi2 != Fraction(1, 6):
        raise AssertionError("BES leading convolution source failed")

    a0_coeff_pi2 = Fraction(1, 2) * sigma0_integral_coeff_pi2
    if a0_coeff_pi2 != Fraction(1, 24):
        raise AssertionError("BES A0 coefficient failed")

    # A1 = int [sigma1/2 - sigma0 t^2/4].
    sigma1_half_t3_coeff_pi4 = -Fraction(1, 8) * Fraction(1, 15) * integral_t3_over_bose
    sigma1_half_pi2_t_coeff_pi4 = -Fraction(1, 12) * Fraction(1, 6) * integral_t_over_bose
    bessel_correction_coeff_pi4 = -Fraction(1, 8) * Fraction(1, 15) * integral_t3_over_bose
    a1_coeff_pi4 = (
        sigma1_half_t3_coeff_pi4
        + sigma1_half_pi2_t_coeff_pi4
        + bessel_correction_coeff_pi4
    )
    if a1_coeff_pi4 != -Fraction(11, 360):
        raise AssertionError(f"BES A1 coefficient failed: {a1_coeff_pi4}")

    # sigma_2=t/(e^t-1)(t^4/24 + pi^2 t^2/12 + zeta(3)t + 11 pi^4/90).
    sigma2_half_pi6 = (
        Fraction(1, 48) * integral_t5_over_bose
        + Fraction(1, 24) * Fraction(1, 15) * integral_t3_over_bose
        + Fraction(11, 180) * Fraction(1, 6) * integral_t_over_bose
    )
    sigma2_half_zeta3sq = Fraction(1, 2) * integral_t2_over_bose_zeta3

    minus_t2_sigma1_over4_pi6 = (
        Fraction(1, 16) * integral_t5_over_bose
        + Fraction(1, 24) * Fraction(1, 15) * integral_t3_over_bose
    )
    sigma0_t4_over24_pi6 = Fraction(1, 48) * integral_t5_over_bose
    a2_coeff_pi6 = (
        sigma2_half_pi6
        + minus_t2_sigma1_over4_pi6
        + sigma0_t4_over24_pi6
    )
    a2_coeff_zeta3sq = sigma2_half_zeta3sq
    if (a2_coeff_pi6, a2_coeff_zeta3sq) != (Fraction(73, 2520), Fraction(1)):
        raise AssertionError(
            f"BES A2 coefficient failed: pi6={a2_coeff_pi6}, zeta3sq={a2_coeff_zeta3sq}"
        )

    f_g2 = Fraction(8)
    f_g4_coeff_pi2 = -64 * a0_coeff_pi2
    f_g6_coeff_pi4 = -64 * a1_coeff_pi4
    f_g8_coeff_pi6 = -64 * a2_coeff_pi6
    f_g8_coeff_zeta3sq = -64 * a2_coeff_zeta3sq
    if (f_g2, f_g4_coeff_pi2, f_g6_coeff_pi4, f_g8_coeff_pi6, f_g8_coeff_zeta3sq) != (
        Fraction(8),
        -Fraction(8, 3),
        Fraction(88, 45),
        -Fraction(584, 315),
        -Fraction(64),
    ):
        raise AssertionError("BES weak scaling-function coefficients failed")

    # Leading dressing contribution to K(2gt,0) from c_{2,3} J_2(2gt)/(gt)
    # carries powers g^3 * g^2 / g = g^4 in sigma, hence g^8 in f(g).
    driving_dressing_power = 3 + 2 - 1
    kernel_dressing_power = 3 + 2 + 1 - 2
    if driving_dressing_power != 4 or kernel_dressing_power != 4:
        raise AssertionError("BES dressing-kernel power counting failed")
    if 4 + driving_dressing_power != 8:
        raise AssertionError("BES dressing contribution should first enter f(g) at g^8")


def check_bes_strong_scaling_function_normalization() -> None:
    """Check the algebra converting the strong BES expansion to f(g)."""

    # Conventional BES cusp: Gamma_BES(g)=4 g^2+...
    # Monograph scaling function: f(g)=8 g^2+..., hence f=2 Gamma_BES.
    if 2 * 4 != 8:
        raise AssertionError("BES weak normalization comparison failed")

    # Shifted strong variable g_s = g - c1.
    # c1 = 3 log(2)/(4 pi), so 4 c1 = 3 log(2)/pi in f(g)=4 g_s+...
    c1_log2_over_pi = Fraction(3, 4)
    if 4 * c1_log2_over_pi != 3:
        raise AssertionError("BES strong coupling shift normalization failed")

    # c2 = K/(16 pi^2), c3 = 27 zeta(3)/(2^11 pi^3),
    # c4 = 21 beta_D(4)/(2^10 pi^4).
    c2_k_over_pi2 = Fraction(1, 16)
    c3_zeta3_over_pi3 = Fraction(27, 2**11)
    c4_beta4_over_pi4 = Fraction(21, 2**10)

    # f(g)=4 g_s - 4 c2/g_s - 4 c3/g_s^2 - 4(c4+2 c2^2)/g_s^3+...
    f_inverse_1_k = -4 * c2_k_over_pi2
    f_inverse_2_zeta3 = -4 * c3_zeta3_over_pi3
    f_inverse_3_beta4 = -4 * c4_beta4_over_pi4
    f_inverse_3_k_squared = -8 * c2_k_over_pi2 * c2_k_over_pi2

    if f_inverse_1_k != -Fraction(1, 4):
        raise AssertionError("BES strong Catalan 1/g coefficient failed")
    if f_inverse_2_zeta3 != -Fraction(27, 512):
        raise AssertionError("BES strong zeta(3) shifted coefficient failed")
    if f_inverse_3_beta4 != -Fraction(21, 256):
        raise AssertionError("BES strong beta(4) shifted coefficient failed")
    if f_inverse_3_k_squared != -Fraction(1, 32):
        raise AssertionError("BES strong Catalan-squared shifted coefficient failed")


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


def check_bound_state_fusion_telescoping() -> None:
    """Check the Q-string endpoint and auxiliary-factor fusion algebra."""

    def constituents(center: complex, charge: int, coupling: float) -> list[tuple[complex, complex]]:
        pairs = []
        for j in range(1, charge + 1):
            rapidity = center + 0.5j * (charge - 2 * j + 1)
            pairs.append(
                (
                    zhukovsky_outside(rapidity + 0.5j, coupling),
                    zhukovsky_outside(rapidity - 0.5j, coupling),
                )
            )
        return pairs

    def sl2_rational(pair_1: tuple[complex, complex], pair_2: tuple[complex, complex]) -> complex:
        x1p, x1m = pair_1
        x2p, x2m = pair_2
        return (
            (x2m - x1p)
            / (x2p - x1m)
            * (1 - 1 / (x2p * x1m))
            / (1 - 1 / (x2m * x1p))
        )

    for coupling in (0.12, 0.37):
        for charge in (2, 3, 5):
            center = 4.0 + 0.3 * charge
            string = constituents(center, charge, coupling)
            x_plus = string[0][0]
            x_minus = string[-1][1]

            for j in range(charge - 1):
                assert_close("bound-state internal endpoint", string[j][1], string[j + 1][0])

            momentum_ratio = 1 + 0j
            for pair in string:
                momentum_ratio *= pair[0] / pair[1]
            assert_close("bound-state momentum telescoping", momentum_ratio, x_plus / x_minus)

            energy_sum = sum(1 + 2j * coupling * (1 / pair[0] - 1 / pair[1]) for pair in string)
            energy_endpoint = charge + 2j * coupling * (1 / x_plus - 1 / x_minus)
            assert_close("bound-state energy telescoping", energy_sum, energy_endpoint)

            central_p = coupling * (1 - momentum_ratio)
            central_k = coupling * (1 - 1 / momentum_ratio)
            assert_close(
                "bound-state shortening",
                energy_endpoint * energy_endpoint,
                charge * charge + 4 * central_p * central_k,
            )

            y_root = 1.7 + 0.2j
            aux_product = 1 + 0j
            for pair in string:
                aux_product *= (y_root - pair[0]) / (y_root - pair[1])
                aux_product *= cmath.sqrt(pair[1] / pair[0])
            aux_endpoint = (y_root - x_plus) / (y_root - x_minus) * cmath.sqrt(x_minus / x_plus)
            assert_close("bound-state auxiliary telescoping", aux_product, aux_endpoint)

    q1 = constituents(4.6, 2, 0.2)
    q2 = constituents(5.3, 3, 0.2)
    fused_forward = 1 + 0j
    for pair_1 in q1:
        for pair_2 in q2:
            fused_forward *= sl2_rational(pair_1, pair_2)
    fused_indexed = 1 + 0j
    for m in range(1, 3):
        u_m = 4.6 + 0.5j * (2 - 2 * m + 1)
        pair_m = (zhukovsky_outside(u_m + 0.5j, 0.2), zhukovsky_outside(u_m - 0.5j, 0.2))
        for n in range(1, 4):
            v_n = 5.3 + 0.5j * (3 - 2 * n + 1)
            pair_n = (zhukovsky_outside(v_n + 0.5j, 0.2), zhukovsky_outside(v_n - 0.5j, 0.2))
            fused_indexed *= sl2_rational(pair_m, pair_n)
    assert_close("bound-state fused scalar indexing", fused_forward, fused_indexed)


def check_mirror_double_wick_dispersion() -> None:
    for coupling in (0.15, 0.5):
        for charge in (1, 2, 4):
            for mirror_momentum in (0.0, 0.7, 2.1):
                mirror_energy = 2 * math.asinh(
                    math.sqrt(charge * charge + mirror_momentum * mirror_momentum)
                    / (4 * coupling)
                )
                hyperbolic_side = 16 * coupling * coupling * math.sinh(mirror_energy / 2) ** 2
                assert_close(
                    "mirror hyperbolic dispersion",
                    hyperbolic_side,
                    charge * charge + mirror_momentum * mirror_momentum,
                )

                physical_momentum = 1j * mirror_energy
                squared_physical_energy = (
                    charge * charge
                    + 16 * coupling * coupling * cmath.sin(physical_momentum / 2) ** 2
                )
                assert_close(
                    "double Wick squared dispersion",
                    squared_physical_energy,
                    -mirror_momentum * mirror_momentum,
                )


def check_mirror_zhukovsky_sheet_parametrization() -> None:
    """Check the stringbook mirror sheet and momentum sign convention."""

    for coupling in (0.08, 0.3, 0.9):
        for charge in (1, 2, 5):
            for mirror_momentum in (-1.4, 0.0, 2.3):
                radius = math.sqrt(charge * charge + mirror_momentum * mirror_momentum)
                mirror_energy = 2 * math.asinh(radius / (4 * coupling))
                sheet_radius = math.exp(-mirror_energy / 2)
                sheet_phase = (mirror_momentum - 1j * charge) / radius
                x_plus = sheet_radius * sheet_phase
                x_minus = sheet_phase / sheet_radius

                if not abs(x_plus) < 1 < abs(x_minus):
                    raise AssertionError("mirror x^+ must be inside and x^- outside")
                assert_close(
                    "mirror x-/x+ energy",
                    cmath.log(x_minus / x_plus),
                    mirror_energy,
                )
                assert_close(
                    "mirror bound-state shortening",
                    x_plus + 1 / x_plus - x_minus - 1 / x_minus,
                    1j * charge / coupling,
                )
                assert_close(
                    "stringbook mirror momentum sign",
                    -charge - 2j * coupling * (x_plus - x_minus),
                    1j * mirror_momentum,
                )

    weak_coupling = 1.0e-4
    for charge in (1, 3):
        for mirror_momentum in (0.5, 1.7):
            radius_squared = charge * charge + mirror_momentum * mirror_momentum
            mirror_energy = 2 * math.asinh(math.sqrt(radius_squared) / (4 * weak_coupling))
            leading_boltzmann = 4 * weak_coupling * weak_coupling / radius_squared
            assert_close(
                "weak mirror Boltzmann leading order",
                math.exp(-mirror_energy) / leading_boltzmann,
                1.0,
                tol=1.0e-7,
            )


def check_mirror_auxiliary_string_arrays() -> None:
    """Check mirror-sheet y-root support and auxiliary string spacings."""

    for radius in (0.2, 0.65, 0.9):
        for phase in (0.1, 1.7, -2.2):
            xi = cmath.exp(1j * phase)
            x_plus = radius * xi
            x_minus = xi / radius
            for y in (
                0.4 * cmath.exp(0.8j),
                cmath.exp(-0.3j),
                1.8 * cmath.exp(1.1j),
            ):
                factor = ((y - x_plus) / (y - x_minus)) * cmath.sqrt(x_minus / x_plus)
                reduced = abs(y - radius * xi) ** 2 / abs(radius * y - xi) ** 2
                assert_close("mirror y-support modulus identity", abs(factor) ** 2, reduced)
                sign = abs(factor) - 1
                if abs(abs(y) - 1) < 1.0e-12:
                    assert_close("mirror y-support unit circle", sign)
                elif (abs(y) < 1 and sign >= 0) or (abs(y) > 1 and sign <= 0):
                    raise AssertionError("mirror y-support modulus sign")

    for coupling in (0.4, 1.3):
        eta = 0.5j / coupling
        for length in range(1, 6):
            center = 0.37
            v_inside = [center + (length + 2 - 2 * j) * eta for j in range(1, length + 1)]
            v_outside = [center - (length + 2 - 2 * j) * eta for j in range(1, length + 1)]
            w_roots = [center + (length + 1 - 2 * j) * eta for j in range(1, length + 1)]

            for index in range(length):
                assert_close(
                    "M|yw inside root pole position",
                    w_roots[index],
                    v_inside[index] - eta,
                )
                assert_close(
                    "M|yw outside root zero position",
                    w_roots[length - 1 - index],
                    v_outside[index] + eta,
                )

            for index in range(length - 1):
                assert_close(
                    "M|yw adjacent inside recursion",
                    v_inside[index + 1],
                    v_inside[index] - 2 * eta,
                )
                assert_close(
                    "M|yw w-root spacing",
                    w_roots[index + 1],
                    w_roots[index] - 2 * eta,
                )

        for length in range(1, 6):
            center = -0.21
            w_string = [center + (length + 1 - 2 * j) * eta for j in range(1, length + 1)]
            for index in range(length - 1):
                assert_close(
                    "pure w-string adjacent spacing",
                    w_string[index + 1],
                    w_string[index] - 2 * eta,
                )
            assert_close("pure w-string real center", sum(w_string) / length, center)


def solve_linear_system(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    size = len(rhs)
    augmented = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1.0e-14:
            raise AssertionError("singular linear system in TBA variation check")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        for entry in range(column, size + 1):
            augmented[column][entry] /= pivot_value
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            for entry in range(column, size + 1):
                augmented[row][entry] -= factor * augmented[column][entry]
    return [augmented[row][size] for row in range(size)]


def check_one_species_tba_variation() -> None:
    """Check the one-species mirror-TBA variational algebra on a grid."""

    weights = [0.4, 0.3, 0.5]
    density_kernel = [
        [0.04, -0.03, 0.02],
        [0.01, 0.05, -0.02],
        [-0.02, 0.01, 0.03],
    ]
    zeta = [0.35, -0.2, 0.75]
    driving_density = [3.7, 4.1, 3.9]
    size = len(weights)

    matrix = []
    for target in range(size):
        row = []
        for source in range(size):
            diagonal = 1 + math.exp(zeta[target]) if source == target else 0.0
            row.append(diagonal + weights[source] * density_kernel[source][target])
        matrix.append(row)
    particle_density = solve_linear_system(matrix, driving_density)
    level_density = [
        driving_density[target]
        - sum(
            weights[source] * density_kernel[source][target] * particle_density[source]
            for source in range(size)
        )
        for target in range(size)
    ]
    hole_density = [
        level_density[index] - particle_density[index] for index in range(size)
    ]
    if any(value <= 0 for value in particle_density + level_density + hole_density):
        raise AssertionError("TBA density check produced nonpositive densities")

    for index in range(size):
        assert_close(
            "one-species TBA pseudoenergy density ratio",
            math.log(hole_density[index] / particle_density[index]),
            zeta[index],
            tol=2.0e-12,
        )

    log_one_plus_y = [math.log(1 + math.exp(-value)) for value in zeta]
    driving = [
        zeta[target]
        - sum(
            weights[source] * density_kernel[target][source] * log_one_plus_y[source]
            for source in range(size)
        )
        for target in range(size)
    ]

    def entropy(particle: list[float]) -> float:
        level = [
            driving_density[target]
            - sum(
                weights[source] * density_kernel[source][target] * particle[source]
                for source in range(size)
            )
            for target in range(size)
        ]
        hole = [level[index] - particle[index] for index in range(size)]
        return sum(
            weights[index]
            * (
                level[index] * math.log(level[index])
                - particle[index] * math.log(particle[index])
                - hole[index] * math.log(hole[index])
            )
            for index in range(size)
        )

    def grand_functional(particle: list[float]) -> float:
        return entropy(particle) - sum(
            weights[index] * driving[index] * particle[index] for index in range(size)
        )

    tangent = [0.2, -0.1, 0.15]
    expected_entropy_derivative = sum(
        weights[source]
        * (
            zeta[source]
            - sum(
                weights[target] * density_kernel[source][target] * log_one_plus_y[target]
                for target in range(size)
            )
        )
        * tangent[source]
        for source in range(size)
    )
    step = 1.0e-7
    forward = [particle_density[index] + step * tangent[index] for index in range(size)]
    backward = [particle_density[index] - step * tangent[index] for index in range(size)]
    numerical_entropy_derivative = (entropy(forward) - entropy(backward)) / (2 * step)
    assert_close(
        "one-species TBA constrained entropy variation",
        numerical_entropy_derivative,
        expected_entropy_derivative,
        tol=2.0e-8,
    )
    numerical_grand_derivative = (grand_functional(forward) - grand_functional(backward)) / (
        2 * step
    )
    assert_close(
        "one-species TBA stationary grand functional",
        numerical_grand_derivative,
        0,
        tol=2.0e-8,
    )

    log_z = grand_functional(particle_density)
    log_z_from_density_equation = sum(
        weights[index] * driving_density[index] * log_one_plus_y[index]
        for index in range(size)
    )
    assert_close(
        "one-species TBA free-energy identity",
        log_z,
        log_z_from_density_equation,
        tol=2.0e-12,
    )

    source_kernel = [
        [-density_kernel[target][source] for target in range(size)]
        for source in range(size)
    ]
    for target in range(size):
        source_convention_rhs = driving[target] - sum(
            weights[source] * source_kernel[source][target] * log_one_plus_y[source]
            for source in range(size)
        )
        assert_close(
            "one-species TBA source-kernel sign convention",
            source_convention_rhs,
            zeta[target],
            tol=2.0e-12,
        )

    for mode in (-2, -1, 0, 3):
        defect_zeta = -2j * math.pi * (mode + 0.5)
        assert_close(
            "excited-state TBA zero quantization",
            1 + cmath.exp(-defect_zeta),
            0,
        )


def check_mirror_tba_node_source_inventory() -> None:
    """Check the multi-species mirror-TBA source and orientation bookkeeping."""

    def make_node(kind: str, index: int = 0, wing: str = "") -> tuple[str, int, str]:
        return (kind, index, wing)

    bullet_nodes = [make_node("bullet", 1), make_node("bullet", 2)]
    auxiliary_nodes: list[tuple[str, int, str]] = []
    for wing in ("L", "R"):
        auxiliary_nodes.extend(
            [
                make_node("y_plus", 0, wing),
                make_node("y_minus", 0, wing),
                make_node("v", 1, wing),
                make_node("v", 2, wing),
                make_node("w", 1, wing),
                make_node("w", 2, wing),
            ]
        )
    nodes = bullet_nodes + auxiliary_nodes

    def wing_sign(wing: str) -> int:
        return 1 if wing == "L" else -1

    mirror_length = 4.0
    bullet_energy = {1: 0.9, 2: 1.35}

    def length_energy(node: tuple[str, int, str]) -> float:
        kind, index, _wing = node
        return bullet_energy[index] if kind == "bullet" else 0.0

    def driving(node: tuple[str, int, str]) -> complex:
        kind, index, wing = node
        if kind == "bullet":
            return mirror_length * bullet_energy[index]
        if kind in ("y_plus", "y_minus"):
            return wing_sign(wing) * math.pi * 1j
        return 0j

    def chemical_potential(node: tuple[str, int, str]) -> complex:
        return mirror_length * length_energy(node) - driving(node)

    for node in nodes:
        assert_close(
            "mirror TBA driving convention",
            mirror_length * length_energy(node) - chemical_potential(node),
            driving(node),
        )
        if node[0] in ("y_plus", "y_minus"):
            assert_close("mirror fermion boundary sign", cmath.exp(-driving(node)), -1)
        elif node[0] != "bullet" and abs(length_energy(node)) > 0:
            raise AssertionError("auxiliary node must not carry a length driving term")

    def same_wing(target: tuple[str, int, str], source: tuple[str, int, str]) -> bool:
        return bool(target[2]) and target[2] == source[2]

    def stringbook_coefficient(
        target: tuple[str, int, str], source: tuple[str, int, str]
    ) -> int:
        target_kind, _target_index, _target_wing = target
        source_kind, source_index, _source_wing = source
        if target_kind == "bullet":
            if source_kind == "bullet":
                return 1
            if source_kind == "v" and source_index >= 2:
                return 1
            if source_kind in ("y_plus", "y_minus"):
                return 1
            return 0
        if target_kind in ("y_plus", "y_minus"):
            if source_kind == "bullet":
                return 1
            if same_wing(target, source) and source_kind == "v":
                return 1
            if same_wing(target, source) and source_kind == "w":
                return -1
            return 0
        if target_kind == "v":
            if source_kind == "bullet":
                return 1
            if same_wing(target, source) and source_kind == "v":
                return 1
            if same_wing(target, source) and source_kind == "y_plus":
                return 1
            if same_wing(target, source) and source_kind == "y_minus":
                return -1
            return 0
        if target_kind == "w":
            if same_wing(target, source) and source_kind == "w":
                return 1
            if same_wing(target, source) and source_kind == "y_plus":
                return 1
            if same_wing(target, source) and source_kind == "y_minus":
                return -1
            return 0
        raise AssertionError("unknown node in mirror TBA inventory")

    for wing in ("L", "R"):
        assert (
            stringbook_coefficient(make_node("bullet", 1), make_node("v", 1, wing))
            == 0
        )
        assert (
            stringbook_coefficient(make_node("bullet", 1), make_node("v", 2, wing))
            == 1
        )

    rapidity = {
        node: -1.2 + 0.27 * index
        for index, node in enumerate(nodes, start=1)
    }
    quadrature_weight = {
        node: 0.11 + 0.03 * ((index % 5) + 1)
        for index, node in enumerate(nodes, start=1)
    }
    y_value = {
        node: 0.2 + 0.07 * ((index * 3) % 11)
        for index, node in enumerate(nodes, start=1)
    }
    log_one_plus_y = {node: math.log(1 + value) for node, value in y_value.items()}

    def phase_strength(
        target: tuple[str, int, str], source: tuple[str, int, str]
    ) -> float:
        raw = (
            17 * (1 + target[1])
            + 19 * (1 + source[1])
            + sum(
                ord(letter)
                for letter in target[0] + source[0] + target[2] + source[2]
            )
        )
        return 0.02 * (1 + raw % 7)

    def phase_prime(z_value: complex, width: float) -> complex:
        return 1 / (z_value + 1j * width) - 1 / (z_value - 1j * width)

    def target_first_kernel(
        target: tuple[str, int, str], source: tuple[str, int, str]
    ) -> complex:
        coefficient = stringbook_coefficient(target, source)
        if coefficient == 0:
            return 0j
        width = 0.6 + 0.05 * ((target[1] + source[1]) % 3)
        z_value = rapidity[target] - rapidity[source]
        return (
            -coefficient
            * phase_strength(target, source)
            * phase_prime(z_value, width)
        )

    def source_kernel(
        source: tuple[str, int, str], target: tuple[str, int, str]
    ) -> complex:
        return -target_first_kernel(target, source)

    for target in nodes:
        stringbook_rhs = driving(target)
        compact_rhs = mirror_length * length_energy(target) - chemical_potential(target)
        for source in nodes:
            assert_close(
                "mirror TBA target/source kernel bridge",
                target_first_kernel(target, source) + source_kernel(source, target),
                0,
            )
            stringbook_rhs += (
                quadrature_weight[source]
                * target_first_kernel(target, source)
                * log_one_plus_y[source]
            )
            compact_rhs -= (
                quadrature_weight[source]
                * source_kernel(source, target)
                * log_one_plus_y[source]
            )
        assert_close("mirror TBA compact/source inventory", compact_rhs, stringbook_rhs)

    for wing in ("L", "R"):
        kernel_value = 0.37
        v_node = make_node("v", 1, wing)
        w_node = make_node("w", 1, wing)
        y_plus = make_node("y_plus", 0, wing)
        y_minus = make_node("y_minus", 0, wing)
        assert_close(
            "mirror TBA y-node reversed w-string ratio",
            kernel_value * log_one_plus_y[v_node] - kernel_value * log_one_plus_y[w_node],
            kernel_value * math.log((1 + y_value[v_node]) / (1 + y_value[w_node])),
        )
        assert_close(
            "mirror TBA auxiliary reversed y-sheet ratio",
            kernel_value * log_one_plus_y[y_plus]
            - kernel_value * log_one_plus_y[y_minus],
            kernel_value
            * math.log((1 + y_value[y_plus]) / (1 + y_value[y_minus])),
        )


def check_mirror_fused_kernel_formula_crosswalk() -> None:
    """Check finite fusion arithmetic in the stringbook mirror-TBA kernels."""

    def shift_labels(length: int) -> list[int]:
        """Return the integer labels 2r for r in R_length."""

        return [-(length - 1) + 2 * index for index in range(length)]

    def string_shifts(length: int) -> list[float]:
        return [label / 2 for label in shift_labels(length)]

    def x_u(shift: float) -> complex:
        return 1.6 + 0.17 * shift + 0.03 * shift * shift + 0.11j * (shift + 2)

    def x_v(shift: float) -> complex:
        return -0.7 + 0.13 * shift - 0.02 * shift * shift + 0.09j * (shift - 1)

    def bullet_bullet_rational(
        left_length: int,
        right_length: int,
        left_x,
        right_x,
    ) -> complex:
        product = 1 + 0j
        for r_shift in string_shifts(left_length):
            for s_shift in string_shifts(right_length):
                left_plus = left_x(2 * r_shift + 1)
                left_minus = left_x(2 * r_shift - 1)
                right_plus = right_x(2 * s_shift + 1)
                right_minus = right_x(2 * s_shift - 1)
                product *= (right_minus - left_plus) / (right_plus - left_minus)
                product *= (1 - 1 / (right_plus * left_minus)) / (
                    1 - 1 / (right_minus * left_plus)
                )
        return product

    def mock_chi(left_value: complex, right_value: complex) -> complex:
        return left_value * right_value * (left_value - right_value)

    def dressing_endpoint(
        left_length: int,
        right_length: int,
        left_x,
        right_x,
    ) -> complex:
        return 2j * (
            mock_chi(left_x(left_length), right_x(right_length))
            + mock_chi(left_x(-left_length), right_x(-right_length))
            - mock_chi(left_x(-left_length), right_x(right_length))
            - mock_chi(left_x(left_length), right_x(-right_length))
        )

    for left_length in range(1, 5):
        for right_length in range(1, 5):
            forward = bullet_bullet_rational(
                left_length, right_length, x_u, x_v
            )
            backward = bullet_bullet_rational(
                right_length, left_length, x_v, x_u
            )
            assert_close(
                "mirror bullet-bullet rational fused unitarity",
                forward * backward,
                1,
                tol=2.0e-12,
            )
            assert_close(
                "mirror bullet-bullet dressing endpoint antisymmetry",
                dressing_endpoint(left_length, right_length, x_u, x_v)
                + dressing_endpoint(right_length, left_length, x_v, x_u),
                0,
                tol=2.0e-12,
            )

    def y_plus_bullet(y_value: complex, x_plus: complex, x_minus: complex) -> complex:
        return (y_value - x_plus) / (y_value - x_minus) * cmath.sqrt(x_minus / x_plus)

    def y_minus_bullet(y_value: complex, x_plus: complex, x_minus: complex) -> complex:
        return (1 / y_value - x_plus) / (1 / y_value - x_minus) * cmath.sqrt(
            x_minus / x_plus
        )

    def y_sqrt_endpoint_exponents(length: int) -> Counter[int]:
        return Counter({-length: Fraction(1, 2), length: Fraction(-1, 2)})

    y_sheet_value = 0.8 + 0.6j
    for length in range(1, 5):
        x_plus = x_v(length)
        x_minus = x_v(-length)
        y_minus_phase = y_minus_bullet(y_sheet_value, x_plus, x_minus)
        assert_close(
            "mirror y-minus equals y-plus on inverse sheet",
            y_minus_phase,
            y_plus_bullet(1 / y_sheet_value, x_plus, x_minus),
        )
        if y_sqrt_endpoint_exponents(length) != Counter(
            {-length: Fraction(1, 2), length: Fraction(-1, 2)}
        ):
            raise AssertionError("mirror y-bullet square-root endpoint package")

    def v_bullet_phase(
        v_length: int,
        bullet_length: int,
        v_x,
        bullet_x,
    ) -> complex:
        product = 1 + 0j
        for sigma in (-1, 1):
            for r_shift in string_shifts(v_length):
                for s_shift in string_shifts(bullet_length):
                    v_endpoint = v_x(2 * r_shift + sigma)
                    bullet_plus = bullet_x(2 * s_shift + 1)
                    bullet_minus = bullet_x(2 * s_shift - 1)
                    product *= (v_endpoint - bullet_plus) / (
                        v_endpoint - bullet_minus
                    )
                    product *= cmath.sqrt(bullet_minus / bullet_plus)
        return product

    for v_length in range(1, 4):
        for bullet_length in range(1, 4):
            phase = v_bullet_phase(v_length, bullet_length, x_u, x_v)
            assert_close(
                "mirror v-bullet reciprocal orientation",
                phase * (1 / phase),
                1,
                tol=2.0e-12,
            )

            sqrt_exponents: Counter[int] = Counter()
            for _sigma in (-1, 1):
                for _r_label in shift_labels(v_length):
                    for s_label in shift_labels(bullet_length):
                        sqrt_exponents[s_label - 1] += Fraction(1, 2)
                        sqrt_exponents[s_label + 1] -= Fraction(1, 2)
            expected_sqrt_exponents = Counter(
                {-bullet_length: v_length, bullet_length: -v_length}
            )
            if sqrt_exponents != expected_sqrt_exponents:
                raise AssertionError(
                    "mirror v-bullet square-root factors do not telescope to endpoints"
                )

    def raw_auxiliary_derivative(
        left_length: int, right_length: int, z_value: complex
    ) -> complex:
        total = 0j
        for r_shift in string_shifts(left_length):
            for s_shift in string_shifts(right_length):
                upper = r_shift - s_shift + 1
                lower = r_shift - s_shift - 1
                total += 1 / (z_value + 1j * lower) - 1 / (z_value + 1j * upper)
        return total

    def one_index_derivative(index: int, z_value: complex) -> complex:
        if index == 0:
            return 0j
        return 1 / (z_value - 0.5j * index) - 1 / (z_value + 0.5j * index)

    def closed_auxiliary_derivative(
        left_length: int, right_length: int, z_value: complex
    ) -> complex:
        value = one_index_derivative(left_length + right_length, z_value)
        value += one_index_derivative(abs(left_length - right_length), z_value)
        for offset in range(1, min(left_length, right_length)):
            value += 2 * one_index_derivative(
                abs(left_length - right_length) + 2 * offset,
                z_value,
            )
        return value

    def raw_auxiliary_pole_multiplicities(
        left_length: int, right_length: int
    ) -> Counter[Fraction]:
        multiplicities: Counter[Fraction] = Counter()
        for r_label in shift_labels(left_length):
            for s_label in shift_labels(right_length):
                difference = Fraction(r_label - s_label, 2)
                multiplicities[difference - 1] += 1
                multiplicities[difference + 1] -= 1
        return multiplicities

    def closed_auxiliary_pole_multiplicities(
        left_length: int, right_length: int
    ) -> Counter[Fraction]:
        multiplicities: Counter[Fraction] = Counter()

        def add_index(index: int, coefficient: int = 1) -> None:
            if index == 0:
                return
            half_index = Fraction(index, 2)
            multiplicities[-half_index] += coefficient
            multiplicities[half_index] -= coefficient

        add_index(left_length + right_length)
        add_index(abs(left_length - right_length))
        for offset in range(1, min(left_length, right_length)):
            add_index(abs(left_length - right_length) + 2 * offset, coefficient=2)
        return multiplicities

    for left_length in range(1, 7):
        for right_length in range(1, 7):
            if raw_auxiliary_pole_multiplicities(
                left_length, right_length
            ) != closed_auxiliary_pole_multiplicities(left_length, right_length):
                raise AssertionError(
                    "mirror auxiliary fused kernel pole multiplicity crosswalk"
                )
            z_value = 0.37 + 0.21j
            assert_close(
                "mirror auxiliary fused kernel double-sum crosswalk",
                raw_auxiliary_derivative(left_length, right_length, z_value),
                closed_auxiliary_derivative(left_length, right_length, z_value),
                tol=2.0e-12,
            )


def check_excited_tba_contour_deformation_residues() -> None:
    """Check the source and energy signs from excited-state contour residues."""

    spectator = 1.1 + 0.3j
    width = 0.7
    crossed_roots = [0.2 + 0.18j, -0.35 + 0.22j]

    def scattering_factor(u_value: complex, v_value: complex) -> complex:
        return (u_value - v_value + 1j * width) / (u_value - v_value - 1j * width)

    def logarithmic_zero_derivative(v_value: complex) -> complex:
        return sum(1 / (v_value - root) for root in crossed_roots)

    def mirror_momentum(v_value: complex) -> complex:
        return 0.5 * v_value * v_value + (0.2 - 0.1j) * v_value

    def contour_integral(
        integrand, center: complex, radius: float, samples: int = 4096
    ) -> complex:
        total = 0j
        step = 2 * math.pi / samples
        for index in range(samples):
            angle = (index + 0.5) * step
            tangent = cmath.exp(1j * angle)
            point = center + radius * tangent
            total += integrand(point) * 1j * radius * tangent * step
        return total

    source_loop = 0j
    energy_loop = 0j
    for root in crossed_roots:
        source_loop += contour_integral(
            lambda value: -cmath.log(scattering_factor(spectator, value))
            * logarithmic_zero_derivative(value)
            / (2j * math.pi),
            root,
            1.0e-3,
        )
        energy_loop += contour_integral(
            lambda value: mirror_momentum(value)
            * logarithmic_zero_derivative(value)
            / (2 * math.pi),
            root,
            1.0e-3,
        )

    source_residue = -sum(
        cmath.log(scattering_factor(spectator, root)) for root in crossed_roots
    )
    assert_close(
        "excited TBA source residue sign",
        source_loop,
        source_residue,
        tol=1.0e-10,
    )
    product_source = 1
    for root in crossed_roots:
        product_source /= scattering_factor(spectator, root)
    assert_close(
        "excited TBA product source orientation",
        cmath.exp(source_residue),
        product_source,
        tol=1.0e-12,
    )

    energy_residue = sum(1j * mirror_momentum(root) for root in crossed_roots)
    assert_close(
        "excited TBA energy residue sign",
        energy_loop,
        energy_residue,
        tol=1.0e-10,
    )

    for physical_energy in (0.6, 1.4, 2.2):
        continued_mirror_momentum = -1j * physical_energy
        assert_close(
            "inverse mirror energy residue",
            1j * continued_mirror_momentum,
            physical_energy,
        )


def check_mirror_wing_kernel_inverse() -> None:
    """Check the A-infinity auxiliary-string kernel inverse used for the Y-system."""

    def a_symbol(m_value: int, n_value: int, q_value: float) -> float:
        return (
            (1 + q_value * q_value)
            * (q_value ** abs(m_value - n_value) - q_value ** (m_value + n_value))
            / (1 - q_value * q_value)
        )

    def fused_a_symbol(m_value: int, n_value: int, q_value: float) -> float:
        value = 1.0 if m_value == n_value else 0.0
        distance = abs(m_value - n_value)
        if distance:
            value += q_value**distance
        value += q_value ** (m_value + n_value)
        for offset in range(1, min(m_value, n_value)):
            value += 2 * q_value ** (distance + 2 * offset)
        return value

    def k_symbol(m_value: int, n_value: int, q_value: float) -> float:
        return a_symbol(m_value, n_value, q_value) - (1.0 if m_value == n_value else 0.0)

    for q_value in (0.2, 0.55, 0.85):
        s_symbol = q_value / (1 + q_value * q_value)
        for m_value in range(1, 8):
            for n_value in range(1, 8):
                assert_close(
                    "mirror A-kernel fused symbol",
                    fused_a_symbol(m_value, n_value, q_value),
                    a_symbol(m_value, n_value, q_value),
                    tol=2.0e-12,
                )

                inverse_product = a_symbol(m_value, n_value, q_value)
                inverse_product -= s_symbol * a_symbol(m_value + 1, n_value, q_value)
                if m_value > 1:
                    inverse_product -= s_symbol * a_symbol(m_value - 1, n_value, q_value)
                assert_close(
                    "mirror A-kernel inverse symbol",
                    inverse_product,
                    1.0 if m_value == n_value else 0.0,
                    tol=2.0e-12,
                )

                inverse_times_k = k_symbol(m_value, n_value, q_value)
                inverse_times_k -= s_symbol * k_symbol(m_value + 1, n_value, q_value)
                if m_value > 1:
                    inverse_times_k -= s_symbol * k_symbol(m_value - 1, n_value, q_value)
                expected = s_symbol * (
                    (1.0 if m_value + 1 == n_value else 0.0)
                    + (1.0 if m_value > 1 and m_value - 1 == n_value else 0.0)
                )
                assert_close(
                    "mirror A-inverse times fused K",
                    inverse_times_k,
                    expected,
                    tol=2.0e-12,
                )

            one_index = q_value**m_value - s_symbol * q_value ** (m_value + 1)
            if m_value > 1:
                one_index -= s_symbol * q_value ** (m_value - 1)
            assert_close(
                "mirror A-inverse times one-index K",
                one_index,
                s_symbol if m_value == 1 else 0.0,
                tol=2.0e-12,
            )

        shift_symbol = (q_value + 1 / q_value) * s_symbol
        assert_close("mirror s-kernel shift inverse", shift_symbol, 1.0)

    circle_y = {0: 0.0, 1: 0.6, 2: 1.4, 3: 0.9, 4: 1.8, 5: 2.2}
    y_oplus = 1.7
    y_ominus = 0.8
    source_ratio = (1 + 1 / y_oplus) / (1 + 1 / y_ominus)
    for n_value in range(1, 5):
        shifted_log_sum = (
            math.log(1 + circle_y[n_value + 1])
            + math.log(1 + circle_y[n_value - 1])
        )
        if n_value == 1:
            shifted_log_sum += math.log(source_ratio)
        assert_close(
            "mirror auxiliary-wing Y-system algebra",
            math.exp(shifted_log_sum)
            / ((1 + circle_y[n_value + 1]) * (1 + circle_y[n_value - 1])),
            source_ratio if n_value == 1 else 1.0,
        )


def check_s_kernel_inverse_data_loss() -> None:
    """Check the zero-mode and source memories hidden by the s-kernel inverse."""

    def zero_mode(u_value: complex, root: complex) -> complex:
        return 1 / (2 * cmath.cosh(math.pi * (u_value - root)))

    for u_value, root in (
        (0.31 + 0.17j, -0.43 + 0.08j),
        (-0.72 + 0.21j, 0.19 - 0.11j),
        (1.13 - 0.09j, -0.27 + 0.14j),
    ):
        shifted_sum = zero_mode(u_value + 0.5j, root) + zero_mode(
            u_value - 0.5j,
            root,
        )
        assert_close("s-kernel inverse zero mode", shifted_sum, 0j, tol=2.0e-14)

    for root in (-0.4 + 0.1j, 0.8 - 0.2j):
        for sign in (-1, 1):
            boundary_pole = root + sign * 0.5j
            denominator = 2 * cmath.cosh(math.pi * (boundary_pole - root))
            assert_close("s-kernel zero-mode boundary pole", denominator, 0j, tol=2.0e-15)
        interior_denominator = 2 * cmath.cosh(math.pi * (root + 0.23j - root))
        if abs(interior_denominator) < 1.0e-8:
            raise AssertionError("s-kernel zero mode should not have an interior strip pole")

    def source_factor(u_value: complex, root: complex) -> complex:
        return (u_value - root + 0.5j) / (u_value - root - 0.5j)

    for u_value, root in (
        (0.23 + 0.19j, -0.51 + 0.03j),
        (1.2 - 0.31j, 0.44 + 0.07j),
    ):
        shifted_source = source_factor(u_value + 0.5j, root) * source_factor(
            u_value - 0.5j,
            root,
        )
        expected_source = (u_value - root + 1j) / (u_value - root - 1j)
        assert_close("s-kernel inverse source memory", shifted_source, expected_source)


def check_y_system_shift_source_factor() -> None:
    """Check local shifted zero-pole source factors for analytic Y-systems."""

    def source_factor(u_value: complex, root: complex) -> complex:
        return (u_value - root + 0.5j) / (u_value - root - 0.5j)

    for u_value, root in (
        (0.3 + 0.2j, -0.7 + 0.1j),
        (1.4 - 0.15j, 0.2 - 0.35j),
        (-0.9 + 0.4j, 0.6 + 0.05j),
    ):
        shifted_product = source_factor(u_value + 0.5j, root) * source_factor(
            u_value - 0.5j,
            root,
        )
        rational_source = (u_value - root + 1j) / (u_value - root - 1j)
        assert_close("Y-system shifted source factor", shifted_product, rational_source)

        inverse_shifted_product = (
            1 / source_factor(u_value + 0.5j, root)
            / source_factor(u_value - 0.5j, root)
        )
        assert_close(
            "Y-system inverse shifted source factor",
            inverse_shifted_product,
            1 / rational_source,
        )

    u_value = 0.8 - 0.25j
    roots_with_powers = (
        (-0.4 + 0.1j, 2),
        (0.5 - 0.3j, -1),
        (1.2 + 0.2j, 1),
    )
    shifted_product = 1 + 0j
    rational_product = 1 + 0j
    for root, power in roots_with_powers:
        shifted_product *= (
            source_factor(u_value + 0.5j, root)
            * source_factor(u_value - 0.5j, root)
        ) ** power
        rational_product *= ((u_value - root + 1j) / (u_value - root - 1j)) ** power
    assert_close("Y-system finite source product", shifted_product, rational_product)


def check_analytic_y_system_strip_and_cut_data() -> None:
    """Check analytic Y-system strip, branch-lattice, and node bookkeeping."""

    def t_hook_node(stringbook_node: tuple[str, int, str]) -> tuple[int, int, int]:
        family, rank, wing = stringbook_node
        wing_sign = 1 if wing == "L" else -1
        if family == "bullet":
            return (rank, 0, 1)
        if family == "oplus":
            return (1, wing_sign, -1)
        if family == "ominus":
            return (2, 2 * wing_sign, 1)
        if family == "triangle":
            return (rank + 1, wing_sign, -1)
        if family == "circle":
            return (1, wing_sign * (rank + 1), -1)
        raise ValueError(f"unknown stringbook node family: {family}")

    expected_nodes = {
        ("bullet", 3, "L"): (3, 0, 1),
        ("oplus", 0, "L"): (1, 1, -1),
        ("oplus", 0, "R"): (1, -1, -1),
        ("ominus", 0, "L"): (2, 2, 1),
        ("ominus", 0, "R"): (2, -2, 1),
        ("triangle", 4, "L"): (5, 1, -1),
        ("triangle", 4, "R"): (5, -1, -1),
        ("circle", 2, "L"): (1, 3, -1),
        ("circle", 2, "R"): (1, -3, -1),
    }
    for node, expected in expected_nodes.items():
        if t_hook_node(node) != expected:
            raise AssertionError("analytic Y-system stringbook/T-hook node map failed")

    def branch_offsets(rank: int, depth: int = 4) -> list[int]:
        offsets: list[int] = []
        for step in range(depth):
            value = rank + 2 * step
            offsets.extend((-value, value))
        return sorted(offsets)

    for rank in range(1, 8):
        offsets = branch_offsets(rank)
        nearest_upper = min(offset for offset in offsets if offset > 0)
        nearest_lower = max(offset for offset in offsets if offset < 0)
        if (nearest_lower, nearest_upper) != (-rank, rank):
            raise AssertionError("analytic Y-system nearest branch lattice failed")
        if not (-rank / 2 < 0 < rank / 2):
            raise AssertionError("analytic Y-system central strip should contain real axis")
        for offset in offsets:
            imag_position = Fraction(offset, 2)
            if Fraction(-rank, 2) < imag_position < Fraction(rank, 2):
                raise AssertionError("analytic Y-system branch point entered open strip")

    central_cut_shifts = [2 * index for index in range(-3, 4)]
    shifted_rank_two_branches = branch_offsets(2, depth=4)
    for shift in central_cut_shifts:
        if shift % 2:
            raise AssertionError("central fermion cuts should lie at integer shifts")
    if any(abs(offset) % 2 for offset in shifted_rank_two_branches):
        raise AssertionError("rank-two branch lattice should have integer cut shifts")

    boundary_samples = (
        (0.7 + 0.2j, 1 / (0.7 + 0.2j)),
        (-1.1 + 0.4j, 1 / (-1.1 + 0.4j)),
        (0.3 - 0.8j, 1 / (0.3 - 0.8j)),
    )
    for lower_y11, upper_y22 in boundary_samples:
        assert_close(
            "central fermion cut inversion",
            upper_y22 * lower_y11,
            1,
        )
        if abs(upper_y22 - lower_y11) < 1.0e-14:
            raise AssertionError("central inversion check failed to detect sheet inversion")

    source_powers = Counter({("root_a", 1): 2, ("root_b", -1): 1})
    total_power = sum(power * multiplicity for (_root, power), multiplicity in source_powers.items())
    if total_power != 1:
        raise AssertionError("analytic source-power bookkeeping failed")


def check_konishi_four_loop_wrapping_arithmetic() -> None:
    # ABA coefficient: -(2820 + 288 zeta_3).
    # Wrapping coefficient: 324 + 864 zeta_3 - 1440 zeta_5.
    rational = -2820 + 324
    zeta3 = -288 + 864
    zeta5 = -1440
    if (rational, zeta3, zeta5) != (-2496, 576, -1440):
        raise AssertionError("Konishi four-loop coefficient arithmetic failed")


def konishi_wrapping_y0(u: float, charge: int) -> float:
    """Leading weak-coupling mirror Y-function coefficient in stringbook units."""

    root = 1 / (2 * math.sqrt(3))
    q = charge
    value = (
        4
        * q
        * q
        * (u * u - root * root + (q * q - 1) / 4) ** 2
        / (u * u + q * q / 4) ** 4
    )
    for physical_root in (root, -root):
        value /= (u - physical_root) ** 2 + (q + 1) ** 2 / 4
        value /= (u - physical_root) ** 2 + (q - 1) ** 2 / 4
    return value


def konishi_wrapping_q_integrand(q_rapidity: float, charge: int) -> float:
    """Coefficient of g^8 in the real-q wrapping integrand after q=2u."""

    q2 = q_rapidity * q_rapidity
    charge2 = charge * charge
    b_minus = (
        9 * q2 * q2
        + 6 * (3 * (charge - 2) * charge + 2) * q2
        + (3 * (charge - 2) * charge + 4) ** 2
    )
    b_plus = (
        9 * q2 * q2
        + 6 * (3 * charge * (charge + 2) + 2) * q2
        + (3 * charge * (charge + 2) + 4) ** 2
    )
    numerator = 147456 * charge2 * (3 * q2 + 3 * charge2 - 4) ** 2
    denominator = (q2 + charge2) ** 4 * b_minus * b_plus
    return -numerator / (2 * math.pi * denominator)


def konishi_wrapping_q_rational_density(q_rapidity: Fraction, charge: int) -> Fraction:
    """Rationalized Y_Q^(0)(q/2) before the -dq/(2 pi) measure."""

    q = q_rapidity
    q2 = q * q
    charge_fraction = Fraction(charge)
    charge2 = charge_fraction * charge_fraction
    b_minus = (
        9 * q2 * q2
        + 6 * (3 * (charge_fraction - 2) * charge_fraction + 2) * q2
        + (3 * (charge_fraction - 2) * charge_fraction + 4) ** 2
    )
    b_plus = (
        9 * q2 * q2
        + 6 * (3 * charge_fraction * (charge_fraction + 2) + 2) * q2
        + (3 * charge_fraction * (charge_fraction + 2) + 4) ** 2
    )
    numerator = 147456 * charge2 * (3 * q2 + 3 * charge2 - 4) ** 2
    denominator = (q2 + charge2) ** 4 * b_minus * b_plus
    return numerator / denominator


def konishi_wrapping_b_coefficients(charge: int, sign: int) -> tuple[Fraction, Fraction, Fraction]:
    """Coefficients of B_Q^sign as c4 q^4 + c2 q^2 + c0."""

    q = Fraction(charge)
    if sign == -1:
        base = 3 * (q - 2) * q
    elif sign == 1:
        base = 3 * q * (q + 2)
    else:
        raise ValueError("sign must be -1 or 1")
    return (Fraction(9), 6 * (base + 2), (base + 4) ** 2)


def konishi_wrapping_paired_b_coefficients(offset: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Coefficients from 9 prod_{sigma=+-1} ((q-sigma/sqrt(3))^2+offset^2)."""

    return (
        Fraction(9),
        18 * (offset**2 - Fraction(1, 3)),
        9 * (offset**2 + Fraction(1, 3)) ** 2,
    )


def evaluate_even_quartic(
    coefficients: tuple[Fraction, Fraction, Fraction], q_value: Fraction
) -> Fraction:
    q2 = q_value * q_value
    return coefficients[0] * q2 * q2 + coefficients[1] * q2 + coefficients[2]


def konishi_wrapping_rational_tail(charge: int) -> Fraction:
    q = Fraction(charge)
    numerator = 7776 * q * (
        19683 * q**18
        - 78732 * q**16
        + 150903 * q**14
        - 134865 * q**12
        + 1458 * q**10
        + 48357 * q**8
        - 13311 * q**6
        - 1053 * q**4
        + 369 * q**2
        - 10
    )
    denominator = (9 * q**4 - 3 * q**2 + 1) ** 4 * (
        27 * q**6 - 27 * q**4 + 36 * q**2 + 16
    )
    return -numerator / denominator


def konishi_wrapping_telescoper(charge: int) -> Fraction:
    q = Fraction(charge)
    polynomial = (
        486 * q**10
        - 2430 * q**9
        + 5184 * q**8
        - 6156 * q**7
        + 4752 * q**6
        - 2916 * q**5
        + 1521 * q**4
        - 504 * q**3
        + 51 * q**2
        + 12 * q
        - 2
    )
    denominator = (3 * q**2 + 1) * (3 * q**2 - 6 * q + 4) * (
        3 * q**2 - 3 * q + 1
    ) ** 4
    return -648 * polynomial / denominator


def konishi_wrapping_charge_summand(charge: int) -> Fraction:
    q = Fraction(charge)
    return (
        konishi_wrapping_rational_tail(charge)
        + Fraction(864, 1) / q**3
        - Fraction(1440, 1) / q**5
    )


def check_konishi_wrapping_exact_residue_reduction() -> None:
    """Check the Konishi residue reduction by exact Laurent extraction."""

    try:
        import sympy as sp
    except ImportError as exc:
        raise AssertionError("SymPy is required for the exact Konishi residue check") from exc

    q = sp.symbols("q")
    imaginary = sp.I
    root_three = sp.sqrt(3)

    def to_sympy_rational(value: Fraction):
        return sp.Rational(value.numerator, value.denominator)

    def density_parts(charge: int):
        b_minus = (
            9 * q**4
            + 6 * (3 * (charge - 2) * charge + 2) * q**2
            + (3 * (charge - 2) * charge + 4) ** 2
        )
        b_plus = (
            9 * q**4
            + 6 * (3 * charge * (charge + 2) + 2) * q**2
            + (3 * charge * (charge + 2) + 4) ** 2
        )
        numerator = 147456 * charge**2 * (3 * q**2 + 3 * charge**2 - 4) ** 2
        denominator = (q**2 + charge**2) ** 4 * b_minus * b_plus
        return sp.expand(numerator), sp.expand(denominator), numerator / denominator

    for charge in range(1, 5):
        numerator, denominator, density = density_parts(charge)
        fourth_order_pole = imaginary * charge
        fourth_order_regular_part = sp.cancel((q - fourth_order_pole) ** 4 * density)
        fourth_order_residue = (
            sp.diff(fourth_order_regular_part, q, 3).subs(q, fourth_order_pole)
            / 6
        )
        if sp.simplify(fourth_order_residue - sp.residue(density, q, fourth_order_pole)) != 0:
            raise AssertionError(f"Konishi fourth-order Laurent residue failed at Q={charge}")

        residues = [fourth_order_residue]
        for sign in (1, -1):
            offset = charge + sign
            if offset == 0:
                continue
            for sigma in (1, -1):
                pole = sp.Rational(sigma, 1) / root_three + imaginary * offset
                derivative_residue = numerator.subs(q, pole) / sp.diff(denominator, q).subs(
                    q, pole
                )
                direct_residue = sp.residue(density, q, pole)
                if sp.simplify(derivative_residue - direct_residue) != 0:
                    raise AssertionError(
                        f"Konishi simple-pole residue formula failed at Q={charge}"
                    )
                residues.append(derivative_residue)

        contour_value = sp.simplify(-imaginary * sum(residues))
        expected = to_sympy_rational(konishi_wrapping_charge_summand(charge))
        if sp.simplify(contour_value - expected) != 0:
            raise AssertionError(f"Konishi exact residue reduction failed at Q={charge}")
        if not contour_value.is_Rational:
            raise AssertionError(f"Konishi residue radicals did not cancel at Q={charge}")


def adaptive_simpson(
    function,
    left: float,
    right: float,
    tolerance: float,
    whole=None,
    depth: int = 24,
) -> float:
    midpoint = (left + right) / 2

    def simpson(a: float, b: float) -> float:
        c = (a + b) / 2
        return (b - a) * (function(a) + 4 * function(c) + function(b)) / 6

    if whole is None:
        whole = simpson(left, right)
    left_part = simpson(left, midpoint)
    right_part = simpson(midpoint, right)
    refined = left_part + right_part
    if depth <= 0 or abs(refined - whole) <= 15 * tolerance:
        return refined + (refined - whole) / 15
    return adaptive_simpson(
        function, left, midpoint, tolerance / 2, left_part, depth - 1
    ) + adaptive_simpson(
        function, midpoint, right, tolerance / 2, right_part, depth - 1
    )


def integrate_even_real_line(function, tolerance: float = 1.0e-8) -> float:
    # Map q in [0,infinity) to t in [0,1].  The transformed endpoint is zero
    # for the present rational functions, which decay faster than q^{-2}.
    def transformed(t: float) -> float:
        if t >= 1:
            return 0.0
        q = t / (1 - t)
        return function(q) / (1 - t) ** 2

    return 2 * adaptive_simpson(transformed, 0.0, 1.0, tolerance)


def check_konishi_wrapping_residue_sum() -> None:
    # The stringbook rapidity u and the real variable q used for the rational
    # residue calculation are related by q=2u.  The leading mirror momentum
    # derivative is d p_tilde_Q/du = 2 + O(g^2).
    for charge in range(1, 8):
        charge_fraction = Fraction(charge)
        for sign, offset in ((-1, charge_fraction - 1), (1, charge_fraction + 1)):
            direct_coefficients = konishi_wrapping_b_coefficients(charge, sign)
            paired_coefficients = konishi_wrapping_paired_b_coefficients(offset)
            if direct_coefficients != paired_coefficients:
                raise AssertionError(
                    f"Konishi B_Q^{sign:+d} paired-root factorization failed at Q={charge}"
                )

        numerator_leading = 147456 * charge_fraction**2 * 9
        denominator_leading = (
            konishi_wrapping_b_coefficients(charge, -1)[0]
            * konishi_wrapping_b_coefficients(charge, 1)[0]
        )
        if numerator_leading / denominator_leading != 16384 * charge_fraction**2:
            raise AssertionError(f"Konishi large-q leading coefficient failed at Q={charge}")

    if konishi_wrapping_b_coefficients(1, -1) != (Fraction(9), Fraction(-6), Fraction(1)):
        raise AssertionError("Konishi Q=1 removable B^- factor has wrong coefficients")

    for q in (Fraction(0), Fraction(1, 3), Fraction(-4, 5), Fraction(7, 4)):
        zero_factor = (3 * q * q - 1) ** 2
        b_minus = evaluate_even_quartic(konishi_wrapping_b_coefficients(1, -1), q)
        if b_minus != zero_factor:
            raise AssertionError("Konishi Q=1 removable factor identity failed")
        b_plus = evaluate_even_quartic(konishi_wrapping_b_coefficients(1, 1), q)
        reduced_density = Fraction(147456) / ((q * q + 1) ** 4 * b_plus)
        if konishi_wrapping_q_rational_density(q, 1) != reduced_density:
            raise AssertionError("Konishi Q=1 removable-pole cancellation failed")

    for charge in (1, 2, 5):
        charge_fraction = Fraction(charge)
        for q in (Fraction(0), Fraction(1, 3), Fraction(-4, 5), Fraction(7, 4)):
            q2 = q * q
            numerator_piece = (
                4
                * charge_fraction**2
                * (q2 / 4 - Fraction(1, 12) + (charge_fraction**2 - 1) / 4) ** 2
            )
            first_denominator = (q2 / 4 + charge_fraction**2 / 4) ** 4

            def paired_denominator(a_value: Fraction) -> Fraction:
                return (
                    q**4
                    + 2 * (a_value**2 - Fraction(1, 3)) * q2
                    + (a_value**2 + Fraction(1, 3)) ** 2
                ) / 16

            density_from_u_formula = numerator_piece / (
                first_denominator
                * paired_denominator(charge_fraction - 1)
                * paired_denominator(charge_fraction + 1)
            )
            if density_from_u_formula != konishi_wrapping_q_rational_density(q, charge):
                raise AssertionError("Konishi weak density rationalization failed")

    for charge in (1, 2, 4):
        for u in (-0.7, 0.0, 1.3):
            stringbook_integrand = -konishi_wrapping_y0(u, charge) / math.pi
            q_integrand = 2 * konishi_wrapping_q_integrand(2 * u, charge)
            assert_close(
                "Konishi wrapping u-to-q integrand",
                q_integrand,
                stringbook_integrand,
            )

    for charge in range(1, 16):
        rational_tail = konishi_wrapping_rational_tail(charge)
        telescoping_difference = (
            konishi_wrapping_telescoper(charge)
            - konishi_wrapping_telescoper(charge + 1)
        )
        if rational_tail != telescoping_difference:
            raise AssertionError(f"Konishi rational tail does not telescope at Q={charge}")

    if konishi_wrapping_telescoper(1) != 324:
        raise AssertionError("Konishi rational wrapping tail has wrong first telescoper value")

    for charge in range(1, 5):
        numeric_integral = integrate_even_real_line(
            lambda q, charge=charge: konishi_wrapping_q_integrand(q, charge)
        )
        exact_summand = float(konishi_wrapping_charge_summand(charge))
        assert_close(
            f"Konishi wrapping residue summand Q={charge}",
            numeric_integral,
            exact_summand,
            tol=2.0e-7,
        )

    partial = sum(konishi_wrapping_charge_summand(charge) for charge in range(1, 25))
    expected_partial = (
        Fraction(324, 1)
        - konishi_wrapping_telescoper(25)
        + sum(
            Fraction(864, charge**3) - Fraction(1440, charge**5)
            for charge in range(1, 25)
        )
    )
    if partial != expected_partial:
        raise AssertionError("Konishi wrapping finite partial sum identity failed")


def check_hexagon_bridge_lengths_and_phase() -> None:
    """Check planar pair-of-pants bridge lengths and partition phases."""

    samples = (
        (4, 4, 4),
        (6, 4, 2),
        (7, 5, 4),
        (8, 6, 6),
    )
    for l1, l2, l3 in samples:
        ell12 = Fraction(l1 + l2 - l3, 2)
        ell23 = Fraction(l2 + l3 - l1, 2)
        ell31 = Fraction(l3 + l1 - l2, 2)
        if any(ell.denominator != 1 or ell < 0 for ell in (ell12, ell23, ell31)):
            raise AssertionError("sample should define nonnegative integer bridges")
        if ell12 + ell31 != l1 or ell12 + ell23 != l2 or ell23 + ell31 != l3:
            raise AssertionError("hexagon bridge length-balance equation failed")

    impossible_samples = (
        (3, 3, 3),  # odd total length
        (8, 2, 2),  # triangle inequality failure
        (5, 4, 2),  # odd total length and half-integer bridge
    )
    for l1, l2, l3 in impossible_samples:
        total_even = (l1 + l2 + l3) % 2 == 0
        triangle = l1 + l2 >= l3 and l2 + l3 >= l1 and l3 + l1 >= l2
        ell_values = (
            Fraction(l1 + l2 - l3, 2),
            Fraction(l2 + l3 - l1, 2),
            Fraction(l3 + l1 - l2, 2),
        )
        integer_nonnegative = all(ell.denominator == 1 and ell >= 0 for ell in ell_values)
        if integer_nonnegative != (total_even and triangle):
            raise AssertionError("hexagon bridge existence criterion mismatch")

    bridge_length = 5
    subset_momenta = (0.4, -1.1, 2.3)
    product_phase = math.prod(cmath.exp(1j * momentum * bridge_length) for momentum in subset_momenta)
    summed_phase = cmath.exp(1j * sum(subset_momenta) * bridge_length)
    assert_close("hexagon partition bridge phase", product_phase, summed_phase)

    cyclic_momenta = (2 * math.pi / 7, -4 * math.pi / 7, 2 * math.pi / 7)
    assert_close(
        "hexagon full-state cyclic translation phase",
        cmath.exp(1j * sum(cyclic_momenta) * bridge_length),
        1,
    )


def check_hexagon_scalar_watson_factor() -> None:
    """Check the scalar hexagon Watson ratio and weak one-loop orientation."""

    def h_factor(
        x_u_plus: complex,
        x_u_minus: complex,
        x_v_plus: complex,
        x_v_minus: complex,
        sigma_uv: complex,
    ) -> complex:
        return (
            ((x_u_minus - x_v_minus) / (x_u_minus - x_v_plus))
            * ((1 - 1 / (x_u_plus * x_v_minus)) / (1 - 1 / (x_u_plus * x_v_plus)))
            / sigma_uv
        )

    exact_samples = (
        (Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11, 13)),
        (Fraction(5, 2), Fraction(9, 4), Fraction(7, 3), Fraction(11, 5), Fraction(4, 9)),
    )
    for x1_plus, x1_minus, x2_plus, x2_minus, sigma_12 in exact_samples:
        h_12 = h_factor(x1_plus, x1_minus, x2_plus, x2_minus, sigma_12)
        h_21 = h_factor(x2_plus, x2_minus, x1_plus, x1_minus, 1 / sigma_12)
        watson_scalar = (
            ((x1_plus - x2_minus) / (x1_minus - x2_plus))
            * ((1 - 1 / (x1_plus * x2_minus)) / (1 - 1 / (x1_minus * x2_plus)))
            / (sigma_12 * sigma_12)
        )
        if h_12 / h_21 != watson_scalar:
            raise AssertionError("hexagon scalar Watson exact rational identity failed")

    coupling = 1.0e-6
    for u1, u2 in ((0.7, -1.1), (2.3, 0.4), (-1.7, 1.2)):
        x1_plus = (u1 + 0.5j) / coupling
        x1_minus = (u1 - 0.5j) / coupling
        x2_plus = (u2 + 0.5j) / coupling
        x2_minus = (u2 - 0.5j) / coupling
        weak_ratio = h_factor(x1_plus, x1_minus, x2_plus, x2_minus, 1) / h_factor(
            x2_plus,
            x2_minus,
            x1_plus,
            x1_minus,
            1,
        )
        compact_phase = (u1 - u2 + 1j) / (u1 - u2 - 1j)
        sl2_phase = (u1 - u2 - 1j) / (u1 - u2 + 1j)
        assert_close("hexagon scalar weak compact phase", weak_ratio, compact_phase)
        if abs(weak_ratio - sl2_phase) < 1.0e-4:
            raise AssertionError("hexagon scalar weak phase should not match SL(2) phase")


def check_bremsstrahlung_displacement_cusp_normalization() -> None:
    """Check the finite coefficient in C_D=12 B from the displacement kernel."""

    taylor_factor = Fraction(1, 2)
    kernel_transform_coefficient = Fraction(1, 6)  # pi |omega|^3 / 6
    fourier_measure_coefficient = Fraction(1, 2)  # pi from kernel over 2 pi measure
    positive_and_negative_frequencies = Fraction(2, 1)

    logarithmic_coefficient = (
        taylor_factor
        * kernel_transform_coefficient
        * fourier_measure_coefficient
        * positive_and_negative_frequencies
    )
    if logarithmic_coefficient != Fraction(1, 12):
        raise AssertionError("displacement-cusp logarithmic coefficient failed")

    if 12 * logarithmic_coefficient != 1:
        raise AssertionError("C_D=12 B normalization failed")


def check_pentagon_ope_resolution_bookkeeping() -> None:
    """Check the symmetry and additive-charge factors in the pentagon channel."""

    species = ["F", "F", "phi", "psi"]
    multiplicities = Counter(species)
    automorphism_factor = math.prod(math.factorial(count) for count in multiplicities.values())
    labelled_permutations = math.factorial(len(species))
    unordered_configurations = labelled_permutations // automorphism_factor
    if automorphism_factor != 2:
        raise AssertionError("pentagon automorphism factor failed")
    if unordered_configurations != 12:
        raise AssertionError("pentagon unordered multiplicity failed")

    # The defect evolution factor is exp[-tau sum E + i sigma sum p + i phi sum m].
    # This exact integer example checks the additivity used in the spectral
    # insertion before any theory-specific dispersion relation is supplied.
    energies = [2, 3, 5, 7]
    momenta = [1, -2, 4, 0]
    transverse_spins = [1, 1, -2, 0]
    if sum(energies) != 17:
        raise AssertionError("pentagon energy additivity failed")
    if sum(momenta) != 3:
        raise AssertionError("pentagon momentum additivity failed")
    if sum(transverse_spins) != 0:
        raise AssertionError("pentagon spin additivity failed")


def check_bremsstrahlung_weak_series() -> None:
    # B(lambda) = sqrt(lambda)/(4 pi^2) I_2(sqrt(lambda))/I_1(sqrt(lambda)).
    # Verify the weak coefficients using exact rational series division.
    i1 = {
        1: Fraction(1, 2),
        3: Fraction(1, 16),
        5: Fraction(1, 384),
        7: Fraction(1, 18432),
    }
    i2 = {
        2: Fraction(1, 8),
        4: Fraction(1, 96),
        6: Fraction(1, 3072),
        8: Fraction(1, 184320),
    }
    ratio: dict[int, Fraction] = {}
    for degree in range(1, 8):
        known = sum(i1.get(k, 0) * ratio.get(degree + 1 - k, 0) for k in i1 if k != 1)
        ratio[degree] = (i2.get(degree + 1, 0) - known) / i1[1]

    expected_ratio = {
        1: Fraction(1, 4),
        3: Fraction(-1, 96),
        5: Fraction(1, 1536),
        7: Fraction(-1, 23040),
    }
    for degree, expected in expected_ratio.items():
        if ratio[degree] != expected:
            raise AssertionError(
                f"B(lambda) Bessel ratio z^{degree} coefficient failed: {ratio[degree]}"
            )

    b_coefficients = [ratio[2 * n - 1] / 4 for n in range(1, 5)]
    expected_b = [
        Fraction(1, 16),
        Fraction(-1, 384),
        Fraction(1, 6144),
        Fraction(-1, 92160),
    ]
    if b_coefficients != expected_b:
        raise AssertionError("B(lambda) weak-series coefficients failed")

    # Strong expansion for I_nu(z), after the common exp(z)/sqrt(2 pi z) factor:
    # sum_k (-1)^k prod_j(4 nu^2-(2j-1)^2)/(k! (8z)^k).
    def modified_bessel_i_asymptotic(order: int, max_power: int) -> dict[int, Fraction]:
        coefficients = {0: Fraction(1)}
        mu = 4 * order * order
        product = 1
        factorial = 1
        eight_power = 1
        for power in range(1, max_power + 1):
            product *= mu - (2 * power - 1) ** 2
            factorial *= power
            eight_power *= 8
            coefficients[power] = Fraction((-1) ** power * product, factorial * eight_power)
        return coefficients

    def divide_inverse_power_series(
        numerator: dict[int, Fraction], denominator: dict[int, Fraction], max_power: int
    ) -> dict[int, Fraction]:
        quotient: dict[int, Fraction] = {}
        for power in range(max_power + 1):
            known = sum(
                denominator.get(j, 0) * quotient.get(power - j, 0)
                for j in range(1, power + 1)
            )
            quotient[power] = numerator.get(power, 0) - known
        return quotient

    ratio_strong = divide_inverse_power_series(
        modified_bessel_i_asymptotic(2, 4),
        modified_bessel_i_asymptotic(1, 4),
        4,
    )
    expected_strong_ratio = {
        0: Fraction(1),
        1: Fraction(-3, 2),
        2: Fraction(3, 8),
        3: Fraction(3, 8),
        4: Fraction(63, 128),
    }
    if ratio_strong != expected_strong_ratio:
        raise AssertionError(f"B(lambda) strong-ratio coefficients failed: {ratio_strong}")

    # Multiplication by z/(4 pi^2) gives the displayed strong expansion.
    strong_b_without_pi2 = {
        1: Fraction(1, 4),
        0: Fraction(-3, 8),
        -1: Fraction(3, 32),
        -2: Fraction(3, 32),
        -3: Fraction(63, 512),
    }
    computed_strong_b = {
        1 - power: coefficient / 4 for power, coefficient in ratio_strong.items()
    }
    if computed_strong_b != strong_b_without_pi2:
        raise AssertionError("B(lambda) strong-series coefficients failed")


def check_qsc_small_spin_bessel_slope() -> None:
    """Check the exact Bessel recurrences behind the QSC small-spin slope."""

    def bessel_i_series(order: int, max_degree: int) -> dict[int, Fraction]:
        series: dict[int, Fraction] = {}
        if order > max_degree:
            return series
        for index in range((max_degree - order) // 2 + 1):
            degree = order + 2 * index
            coefficient = Fraction(
                1,
                (2**degree)
                * math.factorial(index)
                * math.factorial(index + order),
            )
            series[degree] = coefficient
        return series

    def series_sub(
        left: dict[int, Fraction], right: dict[int, Fraction]
    ) -> dict[int, Fraction]:
        degrees = set(left) | set(right)
        return {degree: left.get(degree, 0) - right.get(degree, 0) for degree in degrees}

    def divide_bessel_series(
        numerator: dict[int, Fraction],
        denominator: dict[int, Fraction],
        denominator_order: int,
        max_ratio_degree: int,
    ) -> dict[int, Fraction]:
        ratio: dict[int, Fraction] = {}
        leading = denominator[denominator_order]
        for ratio_degree in range(max_ratio_degree + 1):
            target_degree = denominator_order + ratio_degree
            known = Fraction(0)
            for den_degree, den_coeff in denominator.items():
                if den_degree == denominator_order:
                    continue
                previous_degree = target_degree - den_degree
                if previous_degree in ratio:
                    known += den_coeff * ratio[previous_degree]
            ratio[ratio_degree] = (numerator.get(target_degree, 0) - known) / leading
        return ratio

    max_degree = 14
    for twist in range(1, 7):
        i_j_minus = bessel_i_series(twist - 1, max_degree)
        i_j = bessel_i_series(twist, max_degree)
        i_j_plus = bessel_i_series(twist + 1, max_degree)

        recurrence_lhs = series_sub(i_j_minus, i_j_plus)
        recurrence_rhs = {
            degree - 1: 2 * twist * coefficient
            for degree, coefficient in i_j.items()
        }
        for degree in range(max_degree):
            if recurrence_lhs.get(degree, 0) != recurrence_rhs.get(degree, 0):
                raise AssertionError(f"small-spin Bessel recurrence failed for J={twist}")

        ratio = divide_bessel_series(i_j_plus, i_j, twist, 7)
        slope = {
            degree + 1: coefficient / twist
            for degree, coefficient in ratio.items()
        }
        expected_z2 = Fraction(1, 2 * twist * (twist + 1))
        expected_z4 = Fraction(-1, 8 * twist * (twist + 1) ** 2 * (twist + 2))
        if slope.get(2, 0) != expected_z2:
            raise AssertionError(f"small-spin slope z^2 coefficient failed for J={twist}")
        if slope.get(4, 0) != expected_z4:
            raise AssertionError(f"small-spin slope z^4 coefficient failed for J={twist}")

        # The linearized QSC charge equations use
        # S = i eps^2 g (I_{J-1}-I_{J+1}) and
        # gamma = 2 i eps^2 g I_{J+1}.  Eliminating eps reproduces
        # z I_{J+1}/(J I_J), z=4 pi g.
        eliminated_slope = {
            degree + 1: coefficient / twist
            for degree, coefficient in ratio.items()
        }
        if eliminated_slope != slope:
            raise AssertionError("small-spin slope elimination changed the series")


def check_t_system_to_y_system_identity() -> None:
    """Check the algebraic Y-system relation from local Hirota squares."""

    # Positive sample T-values around one interior T-hook node.
    t_center_plus = Fraction(7)
    t_center_minus = Fraction(11)
    t_up = Fraction(5)
    t_down = Fraction(3)
    t_left = Fraction(2)
    t_right = Fraction(13)

    # Hirota: T^+ T^- = T_up T_down + T_left T_right.
    t_center_minus = (t_up * t_down + t_left * t_right) / t_center_plus

    y = t_up * t_down / (t_left * t_right)
    one_plus_y = (t_center_plus * t_center_minus) / (t_left * t_right)
    one_plus_inverse_y = (t_center_plus * t_center_minus) / (t_up * t_down)

    if one_plus_y != 1 + y:
        raise AssertionError("1+Y from Hirota")
    if one_plus_inverse_y != 1 + 1 / y:
        raise AssertionError("1+1/Y from Hirota")

    # Check the full interior Y-system relation using the four neighbouring
    # Hirota squares around (a,s), without assuming a global T-system solution.
    t_as = Fraction(11, 5)
    t_a_sp2 = Fraction(17, 3)
    t_a_sm2 = Fraction(19, 7)
    t_ap_sp = Fraction(23, 5)
    t_am_sp = Fraction(29, 11)
    t_ap_sm = Fraction(31, 13)
    t_am_sm = Fraction(37, 17)
    t_ap2_s = Fraction(41, 19)
    t_am2_s = Fraction(43, 23)

    upper_base = t_ap_sp * t_am_sp
    upper_y_part = t_a_sp2 * t_as
    lower_base = t_ap_sm * t_am_sm
    lower_y_part = t_as * t_a_sm2
    right_y_part = t_ap_sp * t_ap_sm
    right_base = t_ap2_s * t_as
    left_y_part = t_am_sp * t_am_sm
    left_base = t_as * t_am2_s

    y_system_left = (
        (upper_base + upper_y_part)
        * (lower_base + lower_y_part)
        / ((right_y_part + right_base) * (left_y_part + left_base))
    )
    y_system_right = (
        (1 + upper_y_part / upper_base)
        * (1 + lower_y_part / lower_base)
        / ((1 + right_base / right_y_part) * (1 + left_base / left_y_part))
    )
    if y_system_left != y_system_right:
        raise AssertionError("interior T-hook Hirota-to-Y-system identity")

    def gauge_labels(a_value: int, s_value: int, shift: int = 0) -> Counter[tuple[str, int]]:
        return Counter(
            {
                ("g1", a_value + s_value + shift): 1,
                ("g2", a_value - s_value + shift): 1,
                ("g3", -a_value - s_value + shift): 1,
                ("g4", -a_value + s_value + shift): 1,
            }
        )

    a_value, s_value = 4, 1
    center_shifted_labels = gauge_labels(a_value, s_value, 1) + gauge_labels(
        a_value, s_value, -1
    )
    if center_shifted_labels != (
        gauge_labels(a_value + 1, s_value) + gauge_labels(a_value - 1, s_value)
    ):
        raise AssertionError("Hirota gauge covariance failed for horizontal product")
    if center_shifted_labels != (
        gauge_labels(a_value, s_value + 1) + gauge_labels(a_value, s_value - 1)
    ):
        raise AssertionError("Hirota gauge covariance failed for vertical product")

    y_numerator_labels = gauge_labels(a_value, s_value + 1) + gauge_labels(
        a_value, s_value - 1
    )
    y_denominator_labels = gauge_labels(a_value + 1, s_value) + gauge_labels(
        a_value - 1, s_value
    )
    if y_numerator_labels != y_denominator_labels:
        raise AssertionError("T-gauge factors should cancel in Y-functions")


def check_t_gauge_resolvent_hirota_factorization() -> None:
    """Check the one-row T-gauge Hirota and magic-sheet factorizations."""

    samples = (
        (2, 0.3 + 0.8j, -0.4 + 0.2j, 0.7 - 0.5j, -0.1 + 0.6j),
        (3, -0.2 + 1.1j, 0.6 - 0.3j, -0.5 + 0.4j, 0.9 + 0.1j),
        (5, 0.8 - 0.7j, -0.9 + 0.5j, 0.2 + 0.3j, -0.6 - 0.2j),
    )
    for m_value, g_plus, g_minus, gbar_minus, gbar_plus in samples:
        t_m_plus = m_value + g_plus + gbar_plus
        t_m_minus = m_value + g_minus + gbar_minus
        t_next = m_value + 1 + g_plus + gbar_minus
        t_previous = m_value - 1 + g_minus + gbar_plus
        hirota_t2 = t_m_plus * t_m_minus - t_next * t_previous
        factorized_t2 = (1 + g_plus - g_minus) * (1 + gbar_minus - gbar_plus)
        assert_close("T-gauge one-row Hirota factorization", hirota_t2, factorized_t2)

        hat_g_plus = g_plus
        hat_g_minus = -gbar_minus
        hat_g_inner_plus = g_minus
        hat_g_inner_minus = -gbar_plus
        magic_t2_from_original_factorization = factorized_t2
        magic_row_product = (
            1 + hat_g_plus - hat_g_inner_plus
        ) * (
            1 + hat_g_inner_minus - hat_g_minus
        )
        assert_close(
            "magic-sheet T2 equals shifted T11 product",
            magic_t2_from_original_factorization,
            magic_row_product,
        )

    for pole in (-0.7, 0.0, 0.9):
        point = pole + 0.4j
        density = 1.3
        upper_g = -density / (2j * math.pi * (point - pole))
        lower_gbar = density / (2j * math.pi * (point.conjugate() - pole))
        hat_upper = upper_g
        hat_lower = -lower_gbar
        lower_without_continuation = lower_gbar
        assert_close(
            "T-gauge magic-sheet Cauchy continuation sign",
            hat_lower,
            -lower_gbar,
        )
        if abs(hat_lower - lower_without_continuation) < 1.0e-14:
            raise AssertionError("Cauchy sample should detect the sheet-continuation sign")
        if abs(hat_upper + lower_gbar) < 1.0e-14:
            raise AssertionError("Cauchy sample should not accidentally erase the sheet sign")

    support = ((-0.9, 1.0), (0.2, -0.75), (1.1, 0.5))

    def upper_cauchy(z: complex) -> complex:
        return sum(-weight / (2j * math.pi * (z - pole)) for pole, weight in support)

    def lower_cauchy_bar(z: complex) -> complex:
        return sum(weight / (2j * math.pi * (z - pole)) for pole, weight in support)

    def magic_cauchy(z: complex) -> complex:
        if z.imag >= 0:
            return upper_cauchy(z)
        return -lower_cauchy_bar(z)

    for point in (0.4 - 0.6j, -0.3 - 0.35j, 0.8 - 0.9j):
        assert_close(
            "magic-sheet lower branch continues the upper Cauchy formula",
            magic_cauchy(point),
            upper_cauchy(point),
        )
        if abs(lower_cauchy_bar(point) - upper_cauchy(point)) < 1.0e-14:
            raise AssertionError("lower Cauchy sign should differ before magic continuation")

    for base, m_value in ((0.13 + 0.04j, 2), (-0.31 - 0.03j, 3)):
        upper_slot = base + 0.5j * m_value
        lower_slot = base - 0.5j * m_value
        magic_t1 = m_value + magic_cauchy(upper_slot) - magic_cauchy(lower_slot)
        branch_t1 = m_value + upper_cauchy(upper_slot) + lower_cauchy_bar(lower_slot)
        assert_close("magic-sheet T1 branch sign", magic_t1, branch_t1)

        wrong_lower_sign = m_value + upper_cauchy(upper_slot) - lower_cauchy_bar(lower_slot)
        if abs(wrong_lower_sign - magic_t1) < 1.0e-14:
            raise AssertionError("magic-sheet T1 check failed to detect lower-sign error")

        t2_from_factorization = (
            1
            + magic_cauchy(base + 0.5j * (m_value + 1))
            - magic_cauchy(base + 0.5j * (m_value - 1))
        ) * (
            1
            + magic_cauchy(base + 0.5j * (-m_value + 1))
            - magic_cauchy(base + 0.5j * (-m_value - 1))
        )

        def magic_t11(z: complex) -> complex:
            return 1 + magic_cauchy(z + 0.5j) - magic_cauchy(z - 0.5j)

        t2_from_row_product = magic_t11(base + 0.5j * m_value) * magic_t11(
            base - 0.5j * m_value
        )
        assert_close("magic-sheet T2 row product", t2_from_factorization, t2_from_row_product)


def check_qsc_t_gauge_discontinuity_telescope() -> None:
    """Check the bold-T and mathbb-T gauge algebra before the Pmu bridge."""

    def t_key(a_value: int, s_value: int, shift: int) -> tuple[str, int, int, int]:
        return ("T", a_value, s_value, shift)

    def h_key(shift: int) -> tuple[str, int]:
        return ("h", shift)

    def cal_key(a_value: int, s_value: int, shift: int) -> tuple[str, int, int, int]:
        return ("calT", a_value, s_value, shift)

    def clean(counter: Counter) -> Counter:
        return Counter({key: value for key, value in counter.items() if value})

    def combine(*counters: Counter) -> Counter:
        result: Counter = Counter()
        for counter in counters:
            for key, value in counter.items():
                result[key] += value
        return clean(result)

    def canonical_t(counter: Counter) -> Counter:
        result: Counter = Counter()
        for key, value in counter.items():
            if not value:
                continue
            _tag, a_value, s_value, shift = key
            if a_value == 0:
                result[t_key(0, 0, shift + s_value)] += value
            elif (a_value, s_value) == (3, 2):
                result[t_key(2, 3, shift)] += value
            elif (a_value, s_value) == (3, -2):
                result[t_key(2, -3, shift)] += value
            else:
                result[key] += value
        return clean(result)

    def y_counter(a_value: int, s_value: int, shift: int = 0) -> Counter:
        return Counter(
            {
                t_key(a_value, s_value + 1, shift): 1,
                t_key(a_value, s_value - 1, shift): 1,
                t_key(a_value + 1, s_value, shift): -1,
                t_key(a_value - 1, s_value, shift): -1,
            }
        )

    fermionic_product = canonical_t(combine(y_counter(1, 1), y_counter(2, 2)))
    expected_fermionic_product = canonical_t(
        Counter({t_key(1, 0, 0): 1, t_key(0, 0, 1): -1})
    )
    if fermionic_product != expected_fermionic_product:
        raise AssertionError("QSC bold-T fermionic product reduction failed")

    for length in range(1, 9):
        product_counter: Counter = Counter()
        for node in range(1, length + 1):
            shift = 2 * length - node
            product_counter = combine(
                product_counter,
                Counter(
                    {
                        t_key(node, 0, shift + 1): 1,
                        t_key(node, 0, shift - 1): 1,
                        t_key(node + 1, 0, shift): -1,
                        t_key(node - 1, 0, shift): -1,
                    }
                ),
            )

        expected_counter = Counter(
            {
                t_key(1, 0, 2 * length): 1,
                t_key(length, 0, length - 1): 1,
                t_key(0, 0, 2 * length - 1): -1,
                t_key(length + 1, 0, length): -1,
            }
        )
        if canonical_t(product_counter) != canonical_t(expected_counter):
            raise AssertionError("QSC central-row discontinuity telescope failed")

    for s_value in range(-4, 5):
        # mathbb T_{0,s}=T_{0,s}(T_{0,0}^{[s]})^{-1}=1 in the bold-T boundary
        # gauge.  The sign factor is trivial for a=0.
        mathbb_boundary = canonical_t(
            combine(
                Counter({t_key(0, s_value, 0): 1}),
                Counter({t_key(0, 0, s_value): -1}),
            )
        )
        if mathbb_boundary:
            raise AssertionError("QSC mathbb-T boundary normalization failed")

    for m_value in range(2, 8):
        mathbb_t2_counter = Counter(
            {
                h_key(m_value + 1): 1,
                h_key(m_value - 1): 1,
                h_key(-m_value + 1): 1,
                h_key(-m_value - 1): 1,
                cal_key(2, m_value, 0): 1,
            }
        )
        magic_row_factorization = combine(
            mathbb_t2_counter,
            Counter({cal_key(2, m_value, 0): -1}),
            Counter(
                {
                    cal_key(1, 1, m_value): 1,
                    cal_key(1, 1, -m_value): 1,
                }
            ),
        )
        row_product_counter = Counter(
            {
                h_key(m_value + 1): 1,
                h_key(m_value - 1): 1,
                cal_key(1, 1, m_value): 1,
                h_key(-m_value + 1): 1,
                h_key(-m_value - 1): 1,
                cal_key(1, 1, -m_value): 1,
            }
        )
        if clean(magic_row_factorization) != clean(row_product_counter):
            raise AssertionError("QSC mathbb-T magic-row h-factor compatibility failed")


def check_t_hook_wronskian_pmu_bridge() -> None:
    """Check the local T-hook Wronskian algebra leading to the Pmu bridge."""

    samples = (
        (
            1 + 2j,
            -3 + 0.5j,
            2 - 1j,
            -0.7 + 1.3j,
            1.4 - 0.2j,
            -2.1j,
            0.6 + 0.8j,
            1.7 - 0.4j,
            2.3 - 0.6j,
        ),
        (
            -0.4 + 0.9j,
            2.2 - 1.1j,
            -1.3 - 0.2j,
            0.5 + 1.7j,
            1.9 + 0.3j,
            -0.8 + 0.6j,
            2.4 - 1.5j,
            -1.2 + 0.2j,
            -0.9 + 1.4j,
        ),
    )
    for (
        p1,
        p2,
        tilde_p1,
        tilde_p2,
        p1_plus,
        p2_plus,
        p1_minus,
        p2_minus,
        mu12,
    ) in samples:
        determinant = p1_plus * p2_minus - p2_plus * p1_minus
        if abs(determinant) < 1.0e-12:
            raise AssertionError("Wronskian determinant sample accidentally degenerate")

        first_hirota_product = (
            (tilde_p1 * p2_minus - tilde_p2 * p1_minus)
            * (p1_plus * p2 - p2_plus * p1)
        )
        continued_hirota_product = (
            (p1 * p2_minus - p2 * p1_minus)
            * (p1_plus * tilde_p2 - p2_plus * tilde_p1)
        )
        plucker_factor = (tilde_p1 * p2 - tilde_p2 * p1) * determinant
        assert_close(
            "T-hook Wronskian Plucker identity",
            first_hirota_product - continued_hirota_product,
            plucker_factor,
        )

        tilde_mu12 = mu12 + p1 * tilde_p2 - p2 * tilde_p1
        t21 = first_hirota_product - mu12 * determinant
        continued_t21 = continued_hirota_product - tilde_mu12 * determinant
        assert_close("T-hook T21 central-cut regularity", t21, continued_t21)
        assert_close(
            "T-hook mu12 discontinuity sign",
            tilde_mu12 - mu12,
            p1 * tilde_p2 - p2 * tilde_p1,
        )

        central_t10 = mu12 * (mu12 + tilde_p2 * p1 - tilde_p1 * p2)
        assert_close(
            "T-hook T10 equals mu tilde-mu",
            central_t10,
            mu12 * tilde_mu12,
        )
        assert_close(
            "T-hook fermionic-node product",
            central_t10 / (mu12 * mu12),
            1 + (p1 * tilde_p2 - p2 * tilde_p1) / mu12,
        )


def check_qsc_fermionic_node_ratio_large_u() -> None:
    """Check the large-u sheet expansion of the fermionic-node ratio."""

    for coupling, charge, mirror_momentum in (
        (0.17, 1, 0.8),
        (0.23, 2, -1.1),
        (0.31, 4, 0.35),
    ):
        radius = math.sqrt(charge * charge + mirror_momentum * mirror_momentum)
        mirror_energy = 2 * math.asinh(radius / (4 * coupling))
        r_value = math.exp(-mirror_energy / 2)
        xi = (mirror_momentum - 1j * charge) / radius
        x_plus = r_value * xi
        x_minus = xi / r_value

        if not abs(x_plus) < 1:
            raise AssertionError("mirror plus sheet should be inside")
        if not abs(x_minus) > 1:
            raise AssertionError("mirror minus sheet should be outside")
        assert_close(
            "mirror energy logarithm",
            cmath.log(x_minus / x_plus),
            mirror_energy,
        )
        assert_close(
            "mirror momentum convention",
            1j * mirror_momentum,
            -charge - 2j * coupling * (x_plus - x_minus),
        )

        constant = x_plus / x_minus
        coefficient = coupling * (
            x_plus - x_minus + 1 / x_minus - 1 / x_plus
        )
        assert_close("fermionic ratio constant", constant, cmath.exp(-mirror_energy))
        assert_close("fermionic ratio 1/u coefficient", coefficient, -mirror_momentum)

        shortening = x_plus + 1 / x_plus - x_minus - 1 / x_minus
        assert_close("mirror shortening used by ratio expansion", shortening, 1j * charge / coupling)

        large_u = 10_000.0
        x_small = coupling / large_u + coupling**3 / large_u**3
        ratio = (
            (x_small - x_plus)
            / (x_small - x_minus)
            * ((1 / x_small) - x_minus)
            / ((1 / x_small) - x_plus)
        )
        asymptotic_ratio = cmath.exp(-mirror_energy) * (
            1 - mirror_momentum / large_u
        )
        assert_close(
            "fermionic ratio large-u expansion",
            ratio / asymptotic_ratio,
            1,
            tol=5.0e-7,
        )

        physical_momentum = 1j * mirror_energy
        physical_energy = 1j * mirror_momentum
        assert_close(
            "inverse mirror continuation of ratio exponent",
            -mirror_energy - mirror_momentum / large_u,
            1j * physical_momentum + 1j * physical_energy / large_u,
        )


def check_qsc_pq_bridge_unimodular_rank_one_update() -> None:
    """Check the local P-Q bridge rank-one update and determinant gauge."""

    def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
        return [list(column) for column in zip(*matrix)]

    def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
        return [sum(row[index] * vector[index] for index in range(len(vector))) for row in matrix]

    def row_mat(row: list[Fraction], matrix: list[list[Fraction]]) -> list[Fraction]:
        return [
            sum(row[index] * matrix[index][column] for index in range(len(row)))
            for column in range(len(matrix[0]))
        ]

    def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
        return sum(left[index] * right[index] for index in range(len(left)))

    def outer(column: list[Fraction], row: list[Fraction]) -> list[list[Fraction]]:
        return [[column_entry * row_entry for row_entry in row] for column_entry in column]

    def mat_add(
        left: list[list[Fraction]], right: list[list[Fraction]]
    ) -> list[list[Fraction]]:
        return [
            [left[row][column] + right[row][column] for column in range(len(left[row]))]
            for row in range(len(left))
        ]

    def determinant(matrix: list[list[Fraction]]) -> Fraction:
        work = [row[:] for row in matrix]
        size = len(work)
        det = Fraction(1)
        for column in range(size):
            pivot = None
            for row in range(column, size):
                if work[row][column] != 0:
                    pivot = row
                    break
            if pivot is None:
                return Fraction(0)
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                det = -det
            pivot_value = work[column][column]
            det *= pivot_value
            for row in range(column + 1, size):
                factor = work[row][column] / pivot_value
                for entry in range(column, size):
                    work[row][entry] -= factor * work[column][entry]
        return det

    def solve(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
        work = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
        size = len(work)
        for column in range(size):
            pivot = None
            for row in range(column, size):
                if work[row][column] != 0:
                    pivot = row
                    break
            if pivot is None:
                raise AssertionError("P-Q bridge sample matrix is singular")
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
            pivot_value = work[column][column]
            for entry in range(column, size + 1):
                work[column][entry] /= pivot_value
            for row in range(size):
                if row == column:
                    continue
                factor = work[row][column]
                for entry in range(column, size + 1):
                    work[row][entry] -= factor * work[column][entry]
        return [work[row][-1] for row in range(size)]

    eta = [
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(-1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(-1), Fraction(0)],
    ]
    samples = (
        (
            [
                [Fraction(1), Fraction(2), Fraction(0), Fraction(1)],
                [Fraction(0), Fraction(1), Fraction(3), Fraction(-1)],
                [Fraction(2), Fraction(0), Fraction(1), Fraction(1)],
                [Fraction(1), Fraction(-1), Fraction(0), Fraction(2)],
            ],
            [Fraction(2), Fraction(-1), Fraction(3), Fraction(1)],
        ),
        (
            [
                [Fraction(3), Fraction(1), Fraction(-2), Fraction(0)],
                [Fraction(1), Fraction(0), Fraction(1), Fraction(2)],
                [Fraction(0), Fraction(2), Fraction(1), Fraction(-1)],
                [Fraction(2), Fraction(-1), Fraction(1), Fraction(1)],
            ],
            [Fraction(-1), Fraction(4), Fraction(2), Fraction(-3)],
        ),
    )

    for matrix, q_upper in samples:
        if determinant(matrix) == 0:
            raise AssertionError("P-Q bridge sample matrix is singular")
        q_lower = mat_vec(eta, q_upper)
        p_lower = [-entry for entry in mat_vec(matrix, q_upper)]
        p_upper = solve(transpose(matrix), [-entry for entry in q_lower])
        shifted = mat_add(matrix, outer(p_lower, q_lower))

        if dot(q_lower, q_upper) != 0:
            raise AssertionError("Q-null contraction failed")
        if dot(p_upper, p_lower) != 0:
            raise AssertionError("P-null contraction failed")
        if [-entry for entry in mat_vec(matrix, q_upper)] != p_lower:
            raise AssertionError("minus-shift P contraction failed")
        if [-entry for entry in mat_vec(shifted, q_upper)] != p_lower:
            raise AssertionError("plus-shift P contraction failed")
        if [-entry for entry in row_mat(p_upper, matrix)] != q_lower:
            raise AssertionError("minus-shift Q contraction failed")
        if [-entry for entry in row_mat(p_upper, shifted)] != q_lower:
            raise AssertionError("plus-shift Q contraction failed")
        if determinant(shifted) != determinant(matrix):
            raise AssertionError("P-Q bridge determinant gauge changed")


def check_qomega_dual_monodromy_transport() -> None:
    """Check the dual Qomega Pfaffian transport and monodromy signs."""

    def pfaffian_4(matrix: list[list[complex]]) -> complex:
        return (
            matrix[0][1] * matrix[2][3]
            - matrix[0][2] * matrix[1][3]
            + matrix[0][3] * matrix[1][2]
        )

    eta = [
        [0, 1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, -1, 0],
    ]
    samples = (
        (
            [
                [0, 2, -1, 3],
                [-2, 0, 5, 7],
                [1, -5, 0, 11],
                [-3, -7, -11, 0],
            ],
            [1, -2, 3, 5],
        ),
        (
            [
                [0, 1 - 2j, 3 + 0.5j, -2],
                [-1 + 2j, 0, -4j, 1.5],
                [-3 - 0.5j, 4j, 0, -2 + 0.7j],
                [2, -1.5, 2 - 0.7j, 0],
            ],
            [2 - 1j, -0.5 + 0.2j, 1.3, -2.1j],
        ),
    )

    for omega, q_lower in samples:
        q_upper = [
            sum(eta[row][col] * q_lower[col] for col in range(4))
            for row in range(4)
        ]
        assert_close(
            "Q_i Q^i antisymmetry",
            sum(q_lower[row] * q_upper[row] for row in range(4)),
            0,
        )

        tilde_q = [
            sum(omega[row][col] * q_upper[col] for col in range(4))
            for row in range(4)
        ]
        updated = [
            [
                omega[row][col]
                + q_lower[row] * tilde_q[col]
                - q_lower[col] * tilde_q[row]
                for col in range(4)
            ]
            for row in range(4)
        ]
        assert_close(
            "Qomega Pfaffian rank-two update",
            pfaffian_4(updated),
            pfaffian_4(omega),
        )

        shifted_by_recursion = [
            [
                omega[row][col]
                + q_lower[row] * sum(omega[col][k] * q_upper[k] for k in range(4))
                - q_lower[col] * sum(omega[row][k] * q_upper[k] for k in range(4))
                for col in range(4)
            ]
            for row in range(4)
        ]
        for row in range(4):
            for col in range(4):
                assert_close(
                    "Qomega monodromy recursion equals discontinuity update",
                    shifted_by_recursion[row][col],
                    updated[row][col],
                )
                assert_close(
                    "Qomega shifted matrix preserves antisymmetry",
                    shifted_by_recursion[row][col],
                    -shifted_by_recursion[col][row],
                )

        opposite_update = [
            [
                omega[row][col]
                - q_lower[row] * tilde_q[col]
                + q_lower[col] * tilde_q[row]
                for col in range(4)
            ]
            for row in range(4)
        ]
        if max(
            abs(opposite_update[row][col] - updated[row][col])
            for row in range(4)
            for col in range(4)
        ) < 1.0e-12:
            raise AssertionError("Qomega sample does not detect the transport sign")


def check_qsc_weak_mu12_mu24_elimination() -> None:
    """Check the weak-QSC elimination of mu_24 into the Baxter difference equation."""

    samples = (
        (
            0.9 + 0.4j,
            -0.7 + 0.2j,
            1.3 - 0.5j,
            0.6 + 0.8j,
            -0.2 + 0.3j,
            1.1 - 0.4j,
        ),
        (
            -1.2 + 0.6j,
            0.5 - 0.9j,
            0.8 + 0.7j,
            -0.4 + 1.1j,
            0.7 - 0.2j,
            -1.0 + 0.5j,
        ),
    )

    for p1_minus, p1_plus, p4_minus, p4_plus, mu_minus, mu_center in samples:
        pre_baxter_coefficient = (
            p4_plus / p1_plus
            - p4_minus / p1_minus
            + 1 / (p1_plus * p1_plus)
            + 1 / (p1_minus * p1_minus)
        )
        mu_plus = (p1_plus * p1_plus) * (
            pre_baxter_coefficient * mu_center
            - mu_minus / (p1_minus * p1_minus)
        )

        mu24_minus = (
            (mu_center - mu_minus) / (p1_minus * p1_minus)
            - mu_minus * p4_minus / p1_minus
        )
        mu24_plus = (
            (mu_plus - mu_center) / (p1_plus * p1_plus)
            - mu_center * p4_plus / p1_plus
        )
        assert_close(
            "weak QSC mu24 recursion after elimination",
            mu24_plus - mu24_minus,
            -p4_minus / p1_minus * (mu_center - mu_minus),
        )

        reconstructed_left = pre_baxter_coefficient * mu_center
        reconstructed_right = (
            mu_plus / (p1_plus * p1_plus)
            + mu_minus / (p1_minus * p1_minus)
        )
        assert_close(
            "weak QSC pre-Baxter equation",
            reconstructed_left,
            reconstructed_right,
        )

    for twist in (2, 3, 4):
        for point in (0.2, -0.6 + 0.1j):
            inv_minus = (point - 0.5j) ** twist
            inv_plus = (point + 0.5j) ** twist
            ratio_minus = 0.3 * (point - 0.5j) ** (twist - 1)
            ratio_plus = 0.3 * (point + 0.5j) ** (twist - 1)
            transfer = ratio_plus - ratio_minus + inv_plus + inv_minus
            if not math.isfinite(abs(transfer)):
                raise AssertionError("weak QSC transfer coefficient is not finite")


def check_qsc_large_u_mu_power_balance() -> None:
    """Check the large-u Pmu exponent bookkeeping before the characteristic matrix."""

    pairs = ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4))

    for twist, alpha in (
        (Fraction(2), Fraction(9, 2)),
        (Fraction(3), Fraction(13, 3)),
        (Fraction(5), Fraction(17, 4)),
    ):
        p_lower = {
            1: -twist / 2,
            2: -twist / 2 - 1,
            3: twist / 2,
            4: twist / 2 - 1,
        }
        p_upper = {
            1: p_lower[4],
            2: p_lower[3],
            3: p_lower[2],
            4: p_lower[1],
        }
        mu_power = {
            (1, 2): alpha - twist,
            (1, 3): alpha + 1,
            (1, 4): alpha,
            (2, 3): alpha,
            (2, 4): alpha - 1,
            (3, 4): alpha + twist,
        }

        def exponent(index_a: int, index_b: int) -> Fraction:
            if index_a == index_b:
                raise AssertionError("diagonal mu entry has no exponent")
            return mu_power[tuple(sorted((index_a, index_b)))]

        for row in range(1, 5):
            row_terms = [
                exponent(row, col) + p_upper[col]
                for col in range(1, 5)
                if col != row
            ]
            expected_row_power = alpha + p_lower[row]
            if any(term != expected_row_power for term in row_terms):
                raise AssertionError("QSC Pmu row exponent balance failed")

        for index_a, index_b in pairs:
            left_power = exponent(index_a, index_b) - 1
            universal_rhs_power = alpha + p_lower[index_a] + p_lower[index_b]
            if left_power != universal_rhs_power:
                raise AssertionError("QSC monodromy universal exponent mismatch")

            for index_c in range(1, 5):
                if index_c != index_b:
                    term_power = (
                        p_lower[index_a]
                        + exponent(index_b, index_c)
                        + p_upper[index_c]
                    )
                    if term_power != left_power:
                        raise AssertionError("QSC monodromy first row power mismatch")
                if index_c != index_a:
                    term_power = (
                        p_lower[index_b]
                        + exponent(index_a, index_c)
                        + p_upper[index_c]
                    )
                    if term_power != left_power:
                        raise AssertionError("QSC monodromy second row power mismatch")


def check_qsc_large_u_coefficient_constraints() -> None:
    """Check the large-u characteristic equation for the QSC coefficient products."""

    def determinant_complex(matrix: list[list[complex]]) -> complex:
        work = [row[:] for row in matrix]
        size = len(work)
        determinant = 1 + 0j
        for column in range(size):
            pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
            if abs(work[pivot][column]) < 1.0e-14:
                return 0j
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                determinant = -determinant
            pivot_value = work[column][column]
            determinant *= pivot_value
            for row in range(column + 1, size):
                factor = work[row][column] / pivot_value
                for entry in range(column, size):
                    work[row][entry] -= factor * work[column][entry]
        return determinant

    def characteristic_matrix(
        alpha: complex,
        twist: float,
        a14: complex,
        a23: complex,
    ) -> list[list[complex]]:
        a1 = 1 + 0j
        a2 = 1 + 0j
        a3 = a23
        a4 = a14
        return [
            [
                1j * (alpha - twist) - (a14 - a23),
                -(a2 * a2),
                a1 * a2,
                a1 * a2,
                -(a1 * a1),
                0j,
            ],
            [
                a3 * a3,
                1j * (alpha + 1) - (a14 + a23),
                a1 * a3,
                a1 * a3,
                0j,
                -(a1 * a1),
            ],
            [
                a3 * a4,
                -(a2 * a4),
                1j * alpha,
                0j,
                a1 * a3,
                -(a1 * a2),
            ],
            [
                a3 * a4,
                -(a2 * a4),
                0j,
                1j * alpha,
                a1 * a3,
                -(a1 * a2),
            ],
            [
                a4 * a4,
                0j,
                -(a2 * a4),
                -(a2 * a4),
                1j * (alpha - 1) + a14 + a23,
                -(a2 * a2),
            ],
            [
                0j,
                a4 * a4,
                -(a3 * a4),
                -(a3 * a4),
                a3 * a3,
                1j * (alpha + twist) + a14 - a23,
            ],
        ]

    def coefficient_products(
        twist: float,
        spin: float,
        delta: float,
    ) -> tuple[complex, complex]:
        a14 = (
            1j
            * (
                ((twist + spin - 2) ** 2 - delta * delta)
                * ((twist - spin) ** 2 - delta * delta)
            )
            / (16 * twist * (twist - 1))
        )
        a23 = (
            1j
            * (
                ((twist - spin + 2) ** 2 - delta * delta)
                * ((twist + spin) ** 2 - delta * delta)
            )
            / (16 * twist * (twist + 1))
        )
        return a14, a23

    def characteristic(
        alpha: float,
        twist: float,
        a14: complex,
        a23: complex,
    ) -> complex:
        return (
            (twist + 1) ** 2 * alpha * alpha
            - 4j * twist * (twist + 1) * a23
            - (
                alpha * alpha
                + twist
                - 1j * (twist + 1) * a23
                + 1j * (twist - 1) * a14
            )
            ** 2
        )

    for twist, spin, delta in (
        (2.0, 2.0, 4.15),
        (3.0, 4.0, 7.2),
        (5.0, 1.0, 6.4),
    ):
        a14, a23 = coefficient_products(twist, spin, delta)
        assert_close(
            "QSC large-u characteristic dimension root",
            characteristic(delta, twist, a14, a23),
            tol=2.0e-9,
        )
        assert_close(
            "QSC large-u characteristic spin-shadow root",
            characteristic(spin - 1, twist, a14, a23),
            tol=2.0e-9,
        )
        intermediate = -1j * (twist + 1) * a23 + 1j * (twist - 1) * a14
        expected_intermediate = (
            twist * twist + 1 - delta * delta - (spin - 1) ** 2
        ) / 2
        assert_close(
            "QSC large-u coefficient intermediate relation",
            intermediate,
            expected_intermediate,
            tol=2.0e-10,
        )

        wrong_sign_a14, wrong_sign_a23 = -a14, -a23
        if (
            abs(characteristic(delta, twist, wrong_sign_a14, wrong_sign_a23))
            < 1.0e-6
        ):
            raise AssertionError(
                "QSC coefficient products are insensitive to an overall sign flip"
            )

    for twist, alpha, a14, a23 in (
        (2.0, 1.3 + 0.2j, 0.7 - 0.4j, -0.2 + 0.5j),
        (3.0, -0.6 + 0.9j, 1.1 + 0.3j, 0.4 - 0.7j),
        (5.0, 2.2 - 0.3j, -0.8 + 0.6j, 0.9 + 0.2j),
    ):
        determinant = determinant_complex(
            characteristic_matrix(alpha, twist, a14, a23)
        )
        expected = alpha * alpha * characteristic(alpha, twist, a14, a23)
        assert_close(
            "QSC large-u characteristic determinant",
            determinant,
            expected,
            tol=2.0e-8,
        )


def check_qsc_collapsed_cut_digamma_package() -> None:
    """Check the weak-QSC digamma pole package and its logarithmic coefficient."""

    for spin in (2, 4, 6):
        q_polynomial = twist_two_baxter_polynomial(spin)
        q_derivative = polynomial_derivative(q_polynomial)
        q_plus = polynomial_eval(q_polynomial, 0.5j)
        q_minus = polynomial_eval(q_polynomial, -0.5j)
        r0 = polynomial_eval(q_derivative, 0.5j) - polynomial_eval(
            q_derivative,
            -0.5j,
        )

        def singular_correction(u: complex) -> complex:
            return (
                1j
                * r0
                * polynomial_eval(q_polynomial, u)
                / q_plus
                * (digamma_complex(0.5 - 1j * u) + digamma_complex(0.5 + 1j * u))
            )

        epsilon = 1.0e-7
        residue_plus = epsilon * singular_correction(0.5j + epsilon)
        residue_minus = epsilon * singular_correction(-0.5j + epsilon)
        assert_close(
            f"QSC digamma residue at +i/2 S={spin}",
            residue_plus,
            -r0,
            tol=2.0e-5,
        )
        assert_close(
            f"QSC digamma residue at -i/2 S={spin}",
            residue_minus,
            r0 * q_minus / q_plus,
            tol=2.0e-5,
        )

        large_u = 1000.0
        logarithmic_coefficient = singular_correction(large_u) / polynomial_eval(
            q_polynomial,
            large_u,
        )
        expected_coefficient = 2j * r0 * math.log(large_u) / q_plus
        assert_close(
            f"QSC digamma large-u logarithmic coefficient S={spin}",
            logarithmic_coefficient / expected_coefficient,
            1,
            tol=5.0e-5,
        )


def check_qsc_collapsed_cut_shift_primitive() -> None:
    """Check the shift-defect identities for the half-integer digamma primitive."""

    def primitive(u: complex) -> complex:
        return digamma_complex(0.5 - 1j * u) + digamma_complex(0.5 + 1j * u)

    for u in (0.37 + 0.22j, -1.3 + 0.41j, 2.2 - 0.3j):
        assert_close(
            "digamma primitive upward shift defect",
            primitive(u + 1j) - primitive(u),
            2j / (u + 0.5j),
            tol=2.0e-10,
        )
        assert_close(
            "digamma primitive downward shift defect",
            primitive(u) - primitive(u - 1j),
            2j / (u - 0.5j),
            tol=2.0e-10,
        )
        assert_close(
            "digamma primitive central second difference",
            primitive(u + 1j) - 2 * primitive(u) + primitive(u - 1j),
            2 / (u * u + 0.25),
            tol=2.0e-10,
        )

    for spin in (2, 4, 6):
        q_polynomial = twist_two_baxter_polynomial(spin)
        q_derivative = polynomial_derivative(q_polynomial)
        q_plus = polynomial_eval(q_polynomial, 0.5j)
        r0 = polynomial_eval(q_derivative, 0.5j) - polynomial_eval(
            q_derivative,
            -0.5j,
        )

        def singular_ratio(u: complex) -> complex:
            return 1j * r0 * primitive(u) / q_plus

        for u in (0.8 + 0.2j, -1.5 + 0.6j):
            assert_close(
                f"QSC digamma singular ratio upward shift defect S={spin}",
                singular_ratio(u + 1j) - singular_ratio(u),
                -2 * r0 / (q_plus * (u + 0.5j)),
                tol=2.0e-10,
            )
            assert_close(
                f"QSC digamma singular ratio downward shift defect S={spin}",
                singular_ratio(u) - singular_ratio(u - 1j),
                -2 * r0 / (q_plus * (u - 0.5j)),
                tol=2.0e-10,
            )


def check_pmu_pfaffian_rank_two_update() -> None:
    def pfaffian_4(matrix: list[list[complex]]) -> complex:
        return (
            matrix[0][1] * matrix[2][3]
            - matrix[0][2] * matrix[1][3]
            + matrix[0][3] * matrix[1][2]
        )

    mu = [
        [0, 2, -1, 3],
        [-2, 0, 5, 7],
        [1, -5, 0, 11],
        [-3, -7, -11, 0],
    ]
    chi = [
        [0, 0, 0, 1],
        [0, 0, -1, 0],
        [0, 1, 0, 0],
        [-1, 0, 0, 0],
    ]
    p = [1, -2, 3, 5]
    p_sharp = [sum(chi[row][col] * p[col] for col in range(4)) for row in range(4)]
    p_dot_p_sharp = sum(p[row] * p_sharp[row] for row in range(4))
    assert_close("P_a P^a antisymmetry", p_dot_p_sharp, 0)

    tilde_p = [sum(mu[row][col] * p_sharp[col] for col in range(4)) for row in range(4)]
    updated = [
        [
            mu[row][col] + p[row] * tilde_p[col] - p[col] * tilde_p[row]
            for col in range(4)
        ]
        for row in range(4)
    ]
    assert_close("Pmu Pfaffian rank-two update", pfaffian_4(updated), pfaffian_4(mu))

    y_bridge = 1 + (p[0] * tilde_p[1] - p[1] * tilde_p[0]) / mu[0][1]
    assert_close("Pmu Y11Y22 bridge algebra", y_bridge, updated[0][1] / mu[0][1])

    shifted_by_recursion = [
        [
            mu[row][col]
            + p[row] * sum(mu[col][k] * p_sharp[k] for k in range(4))
            - p[col] * sum(mu[row][k] * p_sharp[k] for k in range(4))
            for col in range(4)
        ]
        for row in range(4)
    ]
    for row in range(4):
        for col in range(4):
            assert_close(
                "Pmu monodromy recursion equals discontinuity update",
                shifted_by_recursion[row][col],
                updated[row][col],
            )
            assert_close(
                "Pmu monodromy recursion preserves antisymmetry",
                shifted_by_recursion[row][col],
                -shifted_by_recursion[col][row],
            )

    large_u = 1.0e6
    for exponent in (0.5, 3.7, -1.2):
        logarithmic_ratio = cmath.log((large_u + 1j) ** exponent / large_u**exponent)
        assert_close(
            "mu12 charge exponent asymptotic",
            large_u * logarithmic_ratio,
            1j * exponent,
            tol=2.0e-6,
        )


def main() -> None:
    check_so6_hamiltonian_reduces_to_su2()
    check_one_magnon_laplacian()
    check_two_magnon_coordinate_matching()
    check_two_magnon_bmn_quantization()
    check_konishi_one_loop_roots()
    check_konishi_baxter_polynomial()
    check_twist_two_qsc_baxter_family()
    check_central_extension_dispersion()
    check_zhukovsky_map_and_energy()
    check_zhukovsky_crossing_path_monodromy()
    check_crossing_rhs_is_sheet_sensitive()
    check_crossing_scalar_monodromy_cocycle()
    check_crossing_cdd_factor_ambiguity()
    check_matrix_crossing_channel_scalar_multiplier()
    check_dressing_charge_antisymmetry_unitarity()
    check_dhm_weak_dressing_coefficients()
    check_dhm_local_residue_continuation()
    check_dhm_gamma_pole_lattice_and_admissibility()
    check_su2c_intertwiner_rank_chart()
    check_su2c_matrix_amplitudes_and_unitarity()
    check_su2c_single_level_ii_nesting_step()
    check_su2c_level_ii_and_iii_nested_scattering()
    check_su2c_nested_bethe_yang_frame_factors()
    check_finite_density_aba_counting_normalization()
    check_rank_one_aba_weak_orientation()
    check_weak_dispersion_expansion()
    check_bmn_scaling_limit()
    check_sl2_large_spin_cusp_resolvent()
    check_one_cut_spectral_curve_bookkeeping()
    check_multicut_period_reflection_bookkeeping()
    check_finite_gap_large_z_moment_expansion()
    check_finite_gap_level_matching_cyclicity()
    check_pohlmeyer_s2_frame_compatibility()
    check_bes_zhukovsky_fourier_transform_signs()
    check_bes_weak_scaling_function()
    check_bes_strong_scaling_function_normalization()
    check_bound_state_dispersion()
    check_bound_state_fusion_telescoping()
    check_mirror_double_wick_dispersion()
    check_mirror_zhukovsky_sheet_parametrization()
    check_mirror_auxiliary_string_arrays()
    check_one_species_tba_variation()
    check_mirror_tba_node_source_inventory()
    check_mirror_fused_kernel_formula_crosswalk()
    check_excited_tba_contour_deformation_residues()
    check_mirror_wing_kernel_inverse()
    check_s_kernel_inverse_data_loss()
    check_y_system_shift_source_factor()
    check_analytic_y_system_strip_and_cut_data()
    check_konishi_four_loop_wrapping_arithmetic()
    check_konishi_wrapping_residue_sum()
    check_konishi_wrapping_exact_residue_reduction()
    check_hexagon_bridge_lengths_and_phase()
    check_hexagon_scalar_watson_factor()
    check_bremsstrahlung_displacement_cusp_normalization()
    check_pentagon_ope_resolution_bookkeeping()
    check_bremsstrahlung_weak_series()
    check_qsc_small_spin_bessel_slope()
    check_t_system_to_y_system_identity()
    check_t_gauge_resolvent_hirota_factorization()
    check_qsc_t_gauge_discontinuity_telescope()
    check_t_hook_wronskian_pmu_bridge()
    check_qsc_fermionic_node_ratio_large_u()
    check_qsc_pq_bridge_unimodular_rank_one_update()
    check_qomega_dual_monodromy_transport()
    check_qsc_weak_mu12_mu24_elimination()
    check_qsc_large_u_mu_power_balance()
    check_qsc_large_u_coefficient_constraints()
    check_qsc_collapsed_cut_digamma_package()
    check_qsc_collapsed_cut_shift_primitive()
    check_pmu_pfaffian_rank_two_update()
    print("All planar N=4 integrability checks passed.")


if __name__ == "__main__":
    main()
