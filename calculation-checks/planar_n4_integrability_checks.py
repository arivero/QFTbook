#!/usr/bin/env python3
"""Finite checks for the planar N=4 SYM integrability chapters."""

from __future__ import annotations

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
    check_weak_dispersion_expansion()
    check_bmn_scaling_limit()
    check_bound_state_dispersion()
    check_mirror_double_wick_dispersion()
    check_konishi_four_loop_wrapping_arithmetic()
    check_konishi_wrapping_residue_sum()
    check_bremsstrahlung_weak_series()
    check_t_system_to_y_system_identity()
    check_pmu_pfaffian_rank_two_update()
    print("All planar N=4 integrability checks passed.")


if __name__ == "__main__":
    main()
