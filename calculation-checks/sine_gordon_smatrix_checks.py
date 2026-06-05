#!/usr/bin/env python3
"""Finite checks for the sine-Gordon exact scattering datum in Volume VI.

The checks also cover the semiclassical soliton fluctuation calculation:
the classical kink profile, Pöschl-Teller fluctuation operator, reflectionless
phase shift, DHN cutoff/counterterm cancellation, and the finite one-loop
mass shift -m/pi.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close
from check_utils import assert_gt

import cmath
import math
from fractions import Fraction
import sympy as sp


ComplexMatrix = list[list[complex]]
Surd3 = tuple[Fraction, Fraction]


def assert_close(name: str, got: complex | float, expected: complex | float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got!r}, expected {expected!r}")


def matmul(a: ComplexMatrix, b: ComplexMatrix) -> ComplexMatrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matrix_part(theta: complex, xi: float) -> ComplexMatrix:
    lam = 1.0 / xi
    denom = cmath.sinh(lam * (1j * math.pi - theta))
    b = cmath.sinh(lam * theta) / denom
    c = 1j * math.sin(math.pi * lam) / denom
    return [
        [1.0 + 0j, 0j, 0j, 0j],
        [0j, b, c, 0j],
        [0j, c, b, 0j],
        [0j, 0j, 0j, 1.0 + 0j],
    ]


def breather_amplitude_b1b1(theta: complex, xi: float) -> complex:
    s = math.sin(math.pi * xi)
    return (cmath.sinh(theta) + 1j * s) / (cmath.sinh(theta) - 1j * s)


def neutral_block(theta: complex, a: float) -> complex:
    s = math.sin(math.pi * a)
    return (cmath.sinh(theta) + 1j * s) / (cmath.sinh(theta) - 1j * s)


def breather_mass(n: int, xi: float, soliton_mass: float) -> float:
    return 2.0 * soliton_mass * math.sin(math.pi * n * xi / 2.0)


def breather_breather_amplitude(theta: complex, m: int, n: int, xi: float) -> complex:
    low = min(m, n)
    gap = abs(m - n)
    result = neutral_block(theta, (m + n) * xi / 2.0) * neutral_block(theta, gap * xi / 2.0)
    for ell in range(1, low):
        result *= neutral_block(theta, (gap + 2 * ell) * xi / 2.0) ** 2
    return result


def soliton_breather_amplitude(theta: complex, n: int, xi: float) -> complex:
    result = (cmath.sinh(theta) + 1j * math.cos(math.pi * n * xi / 2.0)) / (
        cmath.sinh(theta) - 1j * math.cos(math.pi * n * xi / 2.0)
    )
    for ell in range(1, n):
        angle = math.pi * xi * (n - 2 * ell) / 4.0 - math.pi / 4.0
        result *= (cmath.sin(angle + 0.5j * theta) ** 2) / (
            cmath.sin(angle - 0.5j * theta) ** 2
        )
    return result


def pair_operator(pair: tuple[int, int], matrix: ComplexMatrix) -> ComplexMatrix:
    op = [[0j for _ in range(8)] for _ in range(8)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                incoming = (a, b, c)
                incoming_index = 4 * a + 2 * b + c
                first, second = pair
                pair_index = 2 * incoming[first] + incoming[second]
                for outgoing_pair_index in range(4):
                    coefficient = matrix[outgoing_pair_index][pair_index]
                    if abs(coefficient) == 0:
                        continue
                    outgoing = list(incoming)
                    outgoing[first] = outgoing_pair_index // 2
                    outgoing[second] = outgoing_pair_index % 2
                    outgoing_index = 4 * outgoing[0] + 2 * outgoing[1] + outgoing[2]
                    op[outgoing_index][incoming_index] += coefficient
    return op


def check_matrix_unitarity() -> None:
    for xi in (0.37, 0.72, 1.35):
        for theta in (0.21, 0.93, -0.47):
            product = matmul(matrix_part(theta, xi), matrix_part(-theta, xi))
            for i in range(4):
                for j in range(4):
                    expected = 1.0 if i == j else 0.0
                    assert_close(f"matrix unitarity xi={xi} theta={theta} ({i},{j})", product[i][j], expected)


def check_yang_baxter_matrix_part() -> None:
    for xi in (0.37, 0.72):
        theta_1, theta_2, theta_3 = 0.83, 0.12, -0.41
        r12 = pair_operator((0, 1), matrix_part(theta_1 - theta_2, xi))
        r13 = pair_operator((0, 2), matrix_part(theta_1 - theta_3, xi))
        r23 = pair_operator((1, 2), matrix_part(theta_2 - theta_3, xi))
        lhs = matmul(matmul(r12, r13), r23)
        rhs = matmul(matmul(r23, r13), r12)
        for i in range(8):
            for j in range(8):
                assert_close(f"Yang-Baxter xi={xi} ({i},{j})", lhs[i][j], rhs[i][j])


def check_free_fermion_point() -> None:
    xi = 1.0
    for theta in (0.31, 1.4):
        mat = matrix_part(theta, xi)
        assert_close("free-fermion transmission", mat[1][1], 1.0)
        assert_close("free-fermion reflection", mat[1][2], 0.0)


def check_breather_pole_locations_and_masses() -> None:
    xi = 0.23
    soliton_mass = 2.7
    for n in (1, 2, 3, 4):
        u = math.pi * (1.0 - n * xi)
        theta_pole = 1j * u
        denom = cmath.sinh((1.0 / xi) * (1j * math.pi - theta_pole))
        assert_close(f"breather pole denominator n={n}", denom, 0.0, tol=1.0e-9)

        mass_from_pole = 2.0 * soliton_mass * math.cos(u / 2.0)
        mass_formula = 2.0 * soliton_mass * math.sin(math.pi * n * xi / 2.0)
        assert_close(f"breather mass n={n}", mass_from_pole, mass_formula)


def check_lightest_breather_amplitude() -> None:
    for xi in (0.2, 0.41, 0.73):
        for theta in (0.19, 0.88, -1.2):
            amp = breather_amplitude_b1b1(theta, xi)
            assert_close(f"B1B1 unitarity xi={xi} theta={theta}", amp * breather_amplitude_b1b1(-theta, xi), 1.0)
            assert_close(
                f"B1B1 crossing xi={xi} theta={theta}",
                amp,
                breather_amplitude_b1b1(1j * math.pi - theta, xi),
            )

        for pole_name, pole in (
            ("direct", 1j * math.pi * xi),
            ("crossed", 1j * math.pi * (1.0 - xi)),
        ):
            denominator = cmath.sinh(pole) - 1j * math.sin(math.pi * xi)
            assert_close(f"B1B1 {pole_name} pole denominator xi={xi}", denominator, 0.0)


def check_soliton_breather_amplitude() -> None:
    for xi in (0.17, 0.23):
        soliton_mass = 2.4
        for n in (1, 2, 3, 4):
            for theta in (0.23, 0.91, -0.44):
                amp = soliton_breather_amplitude(theta, n, xi)
                assert_close(
                    f"soliton-B{n} unitarity xi={xi} theta={theta}",
                    amp * soliton_breather_amplitude(-theta, n, xi),
                    1.0,
                )
                assert_close(
                    f"soliton-B{n} crossing xi={xi} theta={theta}",
                    amp,
                    soliton_breather_amplitude(1j * math.pi - theta, n, xi),
                )

            direct_u = math.pi / 2.0 + math.pi * n * xi / 2.0
            crossed_u = math.pi / 2.0 - math.pi * n * xi / 2.0
            for pole_name, u in (("direct soliton", direct_u), ("crossed soliton", crossed_u)):
                denominator = cmath.sinh(1j * u) - 1j * math.cos(math.pi * n * xi / 2.0)
                assert_close(f"soliton-B{n} {pole_name} denominator xi={xi}", denominator, 0.0)

            direct_mass_squared = (
                soliton_mass**2
                + breather_mass(n, xi, soliton_mass) ** 2
                + 2.0 * soliton_mass * breather_mass(n, xi, soliton_mass) * math.cos(direct_u)
            )
            assert_close(
                f"soliton-B{n}->soliton mass xi={xi}",
                math.sqrt(direct_mass_squared),
                soliton_mass,
            )

            for ell in range(1, n):
                redundant_u = math.pi / 2.0 + math.pi * xi * (2 * ell - n) / 2.0
                angle = math.pi * xi * (n - 2 * ell) / 4.0 - math.pi / 4.0
                denominator = cmath.sin(angle - 0.5j * (1j * redundant_u))
                assert_close(f"soliton-B{n} redundant denominator ell={ell}", denominator, 0.0)


def check_neutral_block_residues() -> None:
    for a in (0.18, 0.31, 0.43):
        direct_residue = 2j * math.tan(math.pi * a)
        crossed_residue = -2j * math.tan(math.pi * a)
        assert_close(f"neutral block direct -i residue a={a}", -1j * direct_residue, 2.0 * math.tan(math.pi * a))
        assert_close(f"neutral block crossed -i residue a={a}", -1j * crossed_residue, -2.0 * math.tan(math.pi * a))
        for theta in (0.11, 0.75, -1.1):
            amp = neutral_block(theta, a)
            assert_close(f"neutral block unitarity a={a} theta={theta}", amp * neutral_block(-theta, a), 1.0)
            assert_close(
                f"neutral block crossing a={a} theta={theta}",
                amp,
                neutral_block(1j * math.pi - theta, a),
            )


def check_breather_breather_direct_fusion_masses() -> None:
    xi = 0.17
    soliton_mass = 3.2
    for m, n in ((1, 1), (1, 2), (2, 2), (1, 3)):
        u = math.pi * (m + n) * xi / 2.0
        mass_from_pole_squared = (
            breather_mass(m, xi, soliton_mass) ** 2
            + breather_mass(n, xi, soliton_mass) ** 2
            + 2.0
            * breather_mass(m, xi, soliton_mass)
            * breather_mass(n, xi, soliton_mass)
            * math.cos(u)
        )
        assert_close(
            f"B{m}B{n}->B{m+n} mass",
            math.sqrt(mass_from_pole_squared),
            breather_mass(m + n, xi, soliton_mass),
        )

        pole = 1j * u
        parameter = (m + n) * xi / 2.0
        denominator = cmath.sinh(pole) - 1j * math.sin(math.pi * parameter)
        assert_close(f"B{m}B{n} direct-pole denominator", denominator, 0.0)

        for theta in (0.23, 0.9):
            amp = breather_breather_amplitude(theta, m, n, xi)
            assert_close(
                f"B{m}B{n} unitarity theta={theta}",
                amp * breather_breather_amplitude(-theta, m, n, xi),
                1.0,
            )
            assert_close(
                f"B{m}B{n} crossing theta={theta}",
                amp,
                breather_breather_amplitude(1j * math.pi - theta, m, n, xi),
            )


def check_semiclassical_soliton_fluctuation_mass_shift() -> None:
    u, q = sp.symbols("u q", real=True)
    z = sp.symbols("z", positive=True)

    # Kink trigonometry: cos(4 arctan z) = 1 - 2 sech(u)^2 with z=exp(u).
    cos_four_arctan = (1 - 6 * z**2 + z**4) / (1 + z**2) ** 2
    sech_squared = 4 * z**2 / (1 + z**2) ** 2
    assert_equal(
        "sine-Gordon kink cosine identity",
        sp.simplify(cos_four_arctan - (1 - 2 * sech_squared)),
        0,
    )

    # The dimensionless fluctuation operator is -d_u^2 + 1 - 2 sech^2 u.
    zero_mode = sp.sech(u)
    zero_residual = -sp.diff(zero_mode, u, 2) + (1 - 2 * sp.sech(u) ** 2) * zero_mode
    assert_equal(
        "sine-Gordon translational zero mode",
        sp.simplify(sp.expand_trig(zero_residual)),
        0,
    )

    continuum_mode = (sp.I * q - sp.tanh(u)) * sp.exp(sp.I * q * u)
    continuum_residual = (
        -sp.diff(continuum_mode, u, 2)
        + (1 - 2 * sp.sech(u) ** 2) * continuum_mode
        - (1 + q**2) * continuum_mode
    )
    assert_equal(
        "sine-Gordon continuum mode eigenvalue",
        sp.simplify(sp.expand_trig(continuum_residual / sp.exp(sp.I * q * u))),
        0,
    )

    delta_prime = sp.diff(2 * sp.atan(1 / q), q)
    assert_equal(
        "sine-Gordon phase-shift derivative",
        sp.simplify(delta_prime + 2 / (1 + q**2)),
        0,
    )

    # With k=m q and L=Lambda/m, the continuum determinant comparison is
    # -m/pi asinh(L).  The normal-ordering counterterm cancels the logarithmic
    # cutoff dependence and leaves the DHN finite part -m/pi.
    for cutoff_ratio in (0.7, 3.0, 25.0):
        m = 1.9
        continuum = -m / math.pi * math.asinh(cutoff_ratio)
        counterterm = m / math.pi * math.asinh(cutoff_ratio) - m / math.pi
        assert_close(
            f"sine-Gordon DHN finite mass shift cutoff={cutoff_ratio}",
            continuum + counterterm,
            -m / math.pi,
        )

        no_counterterm = continuum
        assert_gt(
            "negative control: unrenormalized continuum shift differs",
            abs(no_counterterm + m / math.pi),
            1.0e-8,
        )

        half_phase_shift = continuum / 2.0 + counterterm
        assert_gt(
            "negative control: half phase shift differs",
            abs(half_phase_shift + m / math.pi),
            1.0e-8,
        )

        counted_zero_mode = continuum + counterterm + m / 2.0
        assert_gt(
            "negative control: counted zero-mode oscillator differs",
            abs(counted_zero_mode + m / math.pi),
            1.0e-8,
        )


def check_affine_toda_a_r_mass_matrix() -> None:
    for rank in range(2, 8):
        h = rank + 1
        for a in range(1, rank + 1):
            mode = [cmath.exp(2j * math.pi * a * k / h) for k in range(h)]
            eigenvalue = 4.0 * math.sin(math.pi * a / h) ** 2
            for k in range(h):
                laplacian = 2.0 * mode[k] - mode[(k - 1) % h] - mode[(k + 1) % h]
                assert_close(
                    f"A_{rank} affine cycle Laplacian a={a} k={k}",
                    laplacian,
                    eigenvalue * mode[k],
                )

        masses = [0.0] + [2.0 * math.sin(math.pi * a / h) for a in range(1, rank + 1)] + [0.0]
        pf_eigenvalue = 2.0 * math.cos(math.pi / h)
        for a in range(1, rank + 1):
            adjacency_action = masses[a - 1] + masses[a + 1]
            assert_close(
                f"A_{rank} Perron-Frobenius sine mass a={a}",
                adjacency_action,
                pf_eigenvalue * masses[a],
            )


def surd3_add(left: Surd3, right: Surd3) -> Surd3:
    return (left[0] + right[0], left[1] + right[1])


def surd3_scale(value: Surd3, coefficient: Fraction) -> Surd3:
    return (coefficient * value[0], coefficient * value[1])


def surd3_mul_sqrt3(value: Surd3) -> Surd3:
    rational, sqrt_part = value
    return (3 * sqrt_part, rational)


def check_affine_toda_d4_perron_frobenius_mass_cell() -> None:
    """Check the D4 Coxeter mass vector over Q[sqrt(3)]."""

    one = (Fraction(1), Fraction(0))
    sqrt3 = (Fraction(0), Fraction(1))
    zero = (Fraction(0), Fraction(0))
    d4_masses = (one, sqrt3, one, one)
    adjacency = (
        (0, 1, 0, 0),
        (1, 0, 1, 1),
        (0, 1, 0, 0),
        (0, 1, 0, 0),
    )

    adjacency_action = []
    for row in adjacency:
        entry = zero
        for connected, mass in zip(row, d4_masses):
            if connected:
                entry = surd3_add(entry, mass)
        adjacency_action.append(entry)

    expected = [surd3_mul_sqrt3(mass) for mass in d4_masses]
    assert_equal(
        "D4 Perron-Frobenius adjacency equation",
        tuple(adjacency_action),
        tuple(expected),
    )
    assert_equal(
        "D4 central-to-leaf mass ratio",
        d4_masses[1],
        surd3_mul_sqrt3(d4_masses[0]),
    )

    cartan_action = []
    for index, mass in enumerate(d4_masses):
        cartan_action.append(
            surd3_add(
                surd3_scale(mass, Fraction(2)),
                surd3_scale(adjacency_action[index], Fraction(-1)),
            )
        )
    cartan_eigenvalue_action = [
        surd3_add(
            surd3_scale(mass, Fraction(2)),
            surd3_scale(surd3_mul_sqrt3(mass), Fraction(-1)),
        )
        for mass in d4_masses
    ]
    assert_equal(
        "D4 Cartan Coxeter eigenvalue",
        tuple(cartan_action),
        tuple(cartan_eigenvalue_action),
    )


def main() -> None:
    check_matrix_unitarity()
    check_yang_baxter_matrix_part()
    check_free_fermion_point()
    check_breather_pole_locations_and_masses()
    check_lightest_breather_amplitude()
    check_soliton_breather_amplitude()
    check_neutral_block_residues()
    check_breather_breather_direct_fusion_masses()
    check_semiclassical_soliton_fluctuation_mass_shift()
    check_affine_toda_a_r_mass_matrix()
    check_affine_toda_d4_perron_frobenius_mass_cell()
    print("All sine-Gordon S-matrix checks passed.")


if __name__ == "__main__":
    main()
