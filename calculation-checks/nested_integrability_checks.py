#!/usr/bin/env python3
"""Checks for Vol VI nested Bethe, QQ, and Hirota identities."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import itertools
import math
from collections import defaultdict
from collections.abc import Callable
from fractions import Fraction


I = 1j


def assert_close(name: str, lhs: complex, rhs: complex, tol: float = 2.0e-10) -> None:
    _assert_close(name, lhs, rhs, tol=tol)


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


def check_backlund_restricted_qsystem() -> None:
    """Check that Q-functions containing a fixed color form a smaller Q-system."""

    all_indices = tuple(range(4))
    sample_points = [-0.3 + 0.2j, 0.6 - 0.4j, 1.2 + 0.15j]

    def restricted(removed: int, subset: tuple[int, ...], u: complex) -> complex:
        return q_det(tuple(sorted(subset + (removed,))), u)

    for removed in all_indices:
        remaining_indices = tuple(i for i in all_indices if i != removed)
        for u in sample_points:
            for size in range(len(remaining_indices) - 1):
                for subset in itertools.combinations(remaining_indices, size):
                    remaining = [a for a in remaining_indices if a not in subset]
                    for a, b in itertools.combinations(remaining, 2):
                        A = tuple(sorted(subset))
                        Aa = tuple(sorted(A + (a,)))
                        Ab = tuple(sorted(A + (b,)))
                        Aab = tuple(sorted(A + (a, b)))
                        lhs = restricted(removed, Aab, u) * restricted(removed, A, u)
                        rhs = restricted(removed, Aa, u + I / 2.0) * restricted(
                            removed, Ab, u - I / 2.0
                        ) - restricted(removed, Aa, u - I / 2.0) * restricted(
                            removed, Ab, u + I / 2.0
                        )
                        assert_close(
                            f"Bäcklund restricted QQ removed={removed} A={A} a={a} b={b} u={u}",
                            lhs,
                            rhs,
                        )


def check_sov_single_zero_shift() -> None:
    """Check the RTT SoV zero-shift factors used in the separated equation."""

    roots = [-0.7 + 0.2j, 0.15 - 0.4j, 1.1 + 0.05j]
    b0 = 1.3 - 0.25j
    sample_points = [-1.2 + 0.31j, 0.6 - 0.19j, 1.7 + 0.43j]

    def b_polynomial(v: complex, zeros: list[complex]) -> complex:
        value = b0
        for root in zeros:
            value *= v - root
        return value

    for alpha, root in enumerate(roots):
        other_roots = [value for index, value in enumerate(roots) if index != alpha]
        for v in sample_points:
            if abs(v - root) < 1.0e-12:
                continue
            a_shift_factor = (root - v - I) / (root - v)
            d_shift_factor = (root - v + I) / (root - v)
            a_target = b_polynomial(v, other_roots + [root - I])
            d_target = b_polynomial(v, other_roots + [root + I])
            assert_close(
                f"SoV A-shift alpha={alpha} v={v}",
                b_polynomial(v, roots) * a_shift_factor,
                a_target,
            )
            assert_close(
                f"SoV D-shift alpha={alpha} v={v}",
                b_polynomial(v, roots) * d_shift_factor,
                d_target,
            )


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


def check_t_system_gauge_freedom() -> None:
    """Verify exact T-gauge covariance of Hirota and invariance of Y-functions."""

    def g(which: int, shift: int) -> Fraction:
        offsets = [5, 7, 11, 13]
        return Fraction(shift * shift + offsets[which], 2 * offsets[which] + 1)

    def gauge(a: int, s: int, shift: int = 0) -> Fraction:
        return (
            g(0, shift + a + s)
            * g(1, shift + a - s)
            * g(2, shift - a + s)
            * g(3, shift - a - s)
        )

    def t_value(a: int, s: int, shift: int = 0) -> Fraction:
        return Fraction((a + 5) ** 2 + 3 * (s + 4) ** 2 + 5 * (shift + 3) ** 2 + 1, 17)

    def t_tilde(a: int, s: int, shift: int = 0) -> Fraction:
        return gauge(a, s, shift) * t_value(a, s, shift)

    for a in range(1, 4):
        for s in range(-2, 3):
            common = gauge(a, s, 1) * gauge(a, s, -1)
            if common != gauge(a + 1, s, 0) * gauge(a - 1, s, 0):
                raise AssertionError(f"T-gauge a-direction cocycle failed at a={a} s={s}")
            if common != gauge(a, s + 1, 0) * gauge(a, s - 1, 0):
                raise AssertionError(f"T-gauge s-direction cocycle failed at a={a} s={s}")

            residual = (
                t_value(a, s, 1) * t_value(a, s, -1)
                - t_value(a + 1, s, 0) * t_value(a - 1, s, 0)
                - t_value(a, s + 1, 0) * t_value(a, s - 1, 0)
            )
            residual_tilde = (
                t_tilde(a, s, 1) * t_tilde(a, s, -1)
                - t_tilde(a + 1, s, 0) * t_tilde(a - 1, s, 0)
                - t_tilde(a, s + 1, 0) * t_tilde(a, s - 1, 0)
            )
            if residual_tilde != common * residual:
                raise AssertionError(f"T-gauge Hirota covariance failed at a={a} s={s}")

            y_value = t_value(a, s + 1) * t_value(a, s - 1) / (
                t_value(a + 1, s) * t_value(a - 1, s)
            )
            y_tilde = t_tilde(a, s + 1) * t_tilde(a, s - 1) / (
                t_tilde(a + 1, s) * t_tilde(a - 1, s)
            )
            if y_tilde != y_value:
                raise AssertionError(f"T-gauge Y-invariance failed at a={a} s={s}")


def check_baxter_casoratian_transport() -> None:
    """Check the finite-difference Wronskian transport for two Baxter solutions."""

    def a(site: int) -> Fraction:
        return Fraction(site + 3, 2)

    def d(site: int) -> Fraction:
        return Fraction(2 * site + 5, 3)

    def lam(site: int) -> Fraction:
        return Fraction(3 * site + 7, 4)

    def solution(q_minus_one: Fraction, q_zero: Fraction, max_site: int) -> dict[int, Fraction]:
        values = {-1: q_minus_one, 0: q_zero}
        for site in range(max_site):
            values[site + 1] = (
                lam(site) * values[site] - a(site) * values[site - 1]
            ) / d(site)
        return values

    q1 = solution(Fraction(2, 3), Fraction(5, 7), 8)
    q2 = solution(Fraction(-1, 5), Fraction(4, 9), 8)

    for site in range(0, 8):
        for name, q in (("q1", q1), ("q2", q2)):
            lhs = lam(site) * q[site]
            rhs = a(site) * q[site - 1] + d(site) * q[site + 1]
            if lhs != rhs:
                raise AssertionError(f"Baxter recurrence failed for {name} at {site}")

        w_plus = q1[site + 1] * q2[site] - q2[site + 1] * q1[site]
        w_minus = q1[site] * q2[site - 1] - q2[site] * q1[site - 1]
        if d(site) * w_plus != a(site) * w_minus:
            raise AssertionError(f"Baxter Casoratian transport failed at {site}")


Spin = int
QoscState = tuple[int, Spin, Spin]
QoscVector = dict[QoscState, Fraction]


def add_fraction(out: defaultdict[QoscState, Fraction], state: QoscState, value: Fraction) -> None:
    if value:
        out[state] += value


def qosc_lowering_coefficient(qparam: Fraction, level: int) -> Fraction:
    return Fraction(1) - qparam ** (2 * level)


def qosc_l_action(qparam: Fraction, spectral: Fraction, site: int, state: QoscState) -> QoscVector:
    """Action of L_F^(+)(spectral) on oscillator level and one spin.

    The spin labels are 0=+ and 1=-, and the matrix convention is

        [[q^D, a], [-x a^dagger, q^{-D} + x q^{D+1}]].

    This is an exact rational check for the component RLL convention used in
    Volume VI, Chapter 5B.
    """

    level, spin_1, spin_2 = state
    spin = spin_1 if site == 1 else spin_2
    out: defaultdict[QoscState, Fraction] = defaultdict(Fraction)

    def emit(new_level: int, new_spin: Spin, coefficient: Fraction) -> None:
        if site == 1:
            add_fraction(out, (new_level, new_spin, spin_2), coefficient)
        else:
            add_fraction(out, (new_level, spin_1, new_spin), coefficient)

    if spin == 0:
        emit(level, 0, qparam**level)
        emit(level + 1, 1, -spectral)
    else:
        emit(level - 1, 0, qosc_lowering_coefficient(qparam, level))
        emit(level, 1, qparam ** (-level) + spectral * qparam ** (level + 1))
    return dict(out)


def six_vertex_r_action(qparam: Fraction, ratio: Fraction, state: QoscState) -> QoscVector:
    """Six-vertex R action in the chapter's q-oscillator normalization."""

    level, spin_1, spin_2 = state
    out: defaultdict[QoscState, Fraction] = defaultdict(Fraction)

    entries: dict[tuple[tuple[Spin, Spin], tuple[Spin, Spin]], Fraction] = {
        ((0, 0), (0, 0)): qparam + qparam**-1 * ratio,
        ((1, 1), (1, 1)): qparam + qparam**-1 * ratio,
        ((0, 1), (0, 1)): Fraction(1) + ratio,
        ((1, 0), (1, 0)): Fraction(1) + ratio,
        ((1, 0), (0, 1)): -(qparam - qparam**-1) * ratio,
        ((0, 1), (1, 0)): qparam - qparam**-1,
    }
    for (out_spins, in_spins), coefficient in entries.items():
        if in_spins == (spin_1, spin_2):
            add_fraction(out, (level, out_spins[0], out_spins[1]), coefficient)
    return dict(out)


def apply_qosc_sequence(
    vector: QoscVector,
    actions: list[Callable[[QoscState], QoscVector]],
) -> QoscVector:
    current: defaultdict[QoscState, Fraction] = defaultdict(Fraction)
    for state, coefficient in vector.items():
        add_fraction(current, state, coefficient)
    for action in actions:
        nxt: defaultdict[QoscState, Fraction] = defaultdict(Fraction)
        for state, coefficient in current.items():
            for new_state, new_coefficient in action(state).items():
                add_fraction(nxt, new_state, coefficient * new_coefficient)
        current = nxt
    return {state: value for state, value in current.items() if value}


def check_qoscillator_l_operator_rll() -> None:
    """Verify the trigonometric rank-one q-oscillator local RLL relation.

    The exact identity checked is

        R_12(-x/y) L_13(x) L_23(y) = L_23(y) L_13(x) R_12(-x/y)

    on Fock levels n=0,...,5 and all four spin inputs.  Because the
    coefficients are rational functions of q, x, and y and the text proves the
    component formulas for an arbitrary level n, this exact finite-basis check
    is a convention regression test rather than a replacement for the proof.
    """

    qparam = Fraction(37, 29)
    x = Fraction(5, 11)
    y = Fraction(7, 13)
    ratio = -x / y

    for level in range(6):
        for spin_1, spin_2 in itertools.product((0, 1), repeat=2):
            state = (level, spin_1, spin_2)
            seed = {state: Fraction(1)}
            lhs = apply_qosc_sequence(
                seed,
                [
                    lambda st: six_vertex_r_action(qparam, ratio, st),
                    lambda st: qosc_l_action(qparam, x, 1, st),
                    lambda st: qosc_l_action(qparam, y, 2, st),
                ],
            )
            rhs = apply_qosc_sequence(
                seed,
                [
                    lambda st: qosc_l_action(qparam, y, 2, st),
                    lambda st: qosc_l_action(qparam, x, 1, st),
                    lambda st: six_vertex_r_action(qparam, ratio, st),
                ],
            )
            if lhs != rhs:
                raise AssertionError(
                    f"q-oscillator RLL mismatch at level={level}, "
                    f"spins={(spin_1, spin_2)}: {lhs!r} != {rhs!r}"
                )


def main() -> None:
    check_su3_worked_example()
    check_cartan_nested_formula()
    check_dressed_vacuum_pole_factorization()
    check_qq_system()
    check_backlund_restricted_qsystem()
    check_sov_single_zero_shift()
    check_hirota_to_y_system()
    check_t_system_gauge_freedom()
    check_baxter_casoratian_transport()
    check_qoscillator_l_operator_rll()
    print("All nested-integrability calculation checks passed.")


if __name__ == "__main__":
    main()
