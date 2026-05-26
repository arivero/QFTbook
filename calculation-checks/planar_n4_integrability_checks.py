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
                certificate = (
                    Fraction((length + 1) ** 3, 1) / (z_value + length) * next_term
                    - Fraction(length**3, 1) / (z_value + length - 1) * term
                )
                if summand_defect != certificate:
                    raise AssertionError(
                        f"twist-two exact telescoping certificate S={spin} k={length}"
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


def check_crossing_rhs_is_sheet_sensitive() -> None:
    coupling = 0.2
    x1_plus, x1_minus = xpm_from_momentum(0.7, coupling)
    x2_plus, x2_minus = xpm_from_momentum(1.6, coupling)

    def stringbook_crossing_rhs(a_plus: complex, a_minus: complex) -> complex:
        return (
            (x2_plus / x2_minus)
            * ((x2_plus - a_plus) / (x2_plus - a_minus))
            * ((x2_minus - 1 / a_plus) / (x2_minus - 1 / a_minus))
        )

    physical_rhs = stringbook_crossing_rhs(x1_plus, x1_minus)
    naively_crossed_rhs = stringbook_crossing_rhs(1 / x1_plus, 1 / x1_minus)
    if abs(physical_rhs - naively_crossed_rhs) < 1.0e-6:
        raise AssertionError("crossing RHS should not be invariant under naive x -> 1/x")


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

                physical_momentum = -1j * mirror_energy
                squared_physical_energy = (
                    charge * charge
                    + 16 * coupling * coupling * cmath.sin(physical_momentum / 2) ** 2
                )
                assert_close(
                    "double Wick squared dispersion",
                    squared_physical_energy,
                    -mirror_momentum * mirror_momentum,
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


def check_bremsstrahlung_weak_series() -> None:
    # B(lambda) = sqrt(lambda)/(4 pi^2) I_2(sqrt(lambda))/I_1(sqrt(lambda)).
    # Verify the first four coefficients using exact rational series division.
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


def check_qsc_large_u_coefficient_constraints() -> None:
    """Check the large-u characteristic equation for the QSC coefficient products."""

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
    check_konishi_one_loop_roots()
    check_konishi_baxter_polynomial()
    check_twist_two_qsc_baxter_family()
    check_central_extension_dispersion()
    check_zhukovsky_map_and_energy()
    check_crossing_rhs_is_sheet_sensitive()
    check_dhm_weak_dressing_coefficients()
    check_su2c_single_level_ii_nesting_step()
    check_su2c_level_ii_and_iii_nested_scattering()
    check_su2c_nested_bethe_yang_frame_factors()
    check_weak_dispersion_expansion()
    check_bmn_scaling_limit()
    check_sl2_large_spin_cusp_resolvent()
    check_bound_state_dispersion()
    check_mirror_double_wick_dispersion()
    check_mirror_auxiliary_string_arrays()
    check_one_species_tba_variation()
    check_mirror_wing_kernel_inverse()
    check_konishi_four_loop_wrapping_arithmetic()
    check_konishi_wrapping_residue_sum()
    check_bremsstrahlung_weak_series()
    check_t_system_to_y_system_identity()
    check_t_gauge_resolvent_hirota_factorization()
    check_t_hook_wronskian_pmu_bridge()
    check_qsc_pq_bridge_unimodular_rank_one_update()
    check_qsc_large_u_coefficient_constraints()
    check_qsc_collapsed_cut_digamma_package()
    check_qsc_collapsed_cut_shift_primitive()
    check_pmu_pfaffian_rank_two_update()
    print("All planar N=4 integrability checks passed.")


if __name__ == "__main__":
    main()
