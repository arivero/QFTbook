#!/usr/bin/env python3
"""Exact coefficient checks for the QCD-string effective-spectrum section."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction

import sympy as sp

from check_utils import assert_lt as _assert_lt


def assert_equal(name: str, got: Fraction, expected: Fraction) -> None:
    if got != expected:
        raise AssertionError(f"{name} failed: got {got}, expected {expected}")


def assert_less(name: str, left: Fraction, right: Fraction) -> None:
    _assert_lt(name, left, right)


def assert_zero(name: str, expr: sp.Expr) -> None:
    simplified = sp.simplify(sp.trigsimp(expr))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified!r}")


def check_open_and_closed_casimir_coefficients() -> None:
    zeta_minus_one = Fraction(-1, 12)

    # One open Dirichlet scalar has E = (pi/(2 L)) zeta_R(-1).
    open_per_scalar = Fraction(1, 2) * zeta_minus_one
    assert_equal("open Luscher coefficient per transverse scalar", open_per_scalar, Fraction(-1, 24))

    # One periodic closed scalar has two oscillators for each n >= 1, so
    # E = (2 pi/L) zeta_R(-1).
    closed_per_scalar = Fraction(2, 1) * zeta_minus_one
    assert_equal("closed Luscher coefficient per transverse scalar", closed_per_scalar, Fraction(-1, 6))


def check_nambu_goto_reference_expansion() -> None:
    # The expansion sqrt(1 - x) = 1 - x/2 - x^2/8 + O(x^3) is applied to
    # x_open = pi c/(12 sigma L^2) and x_closed = pi c/(3 sigma L^2).
    open_luscher_denominator = Fraction(2, 1) * 12
    open_l3_denominator = Fraction(8, 1) * 12 * 12
    assert_equal("open NG 1/L coefficient denominator", Fraction(-1, open_luscher_denominator), Fraction(-1, 24))
    assert_equal("open NG 1/L^3 coefficient denominator", Fraction(-1, open_l3_denominator), Fraction(-1, 1152))

    closed_luscher_denominator = Fraction(2, 1) * 3
    closed_l3_denominator = Fraction(8, 1) * 3 * 3
    assert_equal("closed NG 1/L coefficient denominator", Fraction(-1, closed_luscher_denominator), Fraction(-1, 6))
    assert_equal("closed NG 1/L^3 coefficient denominator", Fraction(-1, closed_l3_denominator), Fraction(-1, 72))


def colored_partition_degeneracies(colors: int, max_level: int) -> list[int]:
    coeffs = [0] * (max_level + 1)
    coeffs[0] = 1
    for mode in range(1, max_level + 1):
        for _ in range(colors):
            for level in range(mode, max_level + 1):
                coeffs[level] += coeffs[level - mode]
    return coeffs


def check_open_oscillator_degeneracies() -> None:
    # For D=4 there are two transverse colors.  The generating function is
    # product_{n >= 1} (1 - q^n)^(-2), whose first coefficients are displayed
    # in the monograph.
    assert colored_partition_degeneracies(colors=2, max_level=4) == [1, 2, 5, 10, 20]


def generate_open_fock_states(level: int) -> list[dict[tuple[int, int], int]]:
    modes = [(n, pol) for n in range(1, level + 1) for pol in (1, -1)]
    states: list[dict[tuple[int, int], int]] = []

    def rec(index: int, remaining: int, state: dict[tuple[int, int], int]) -> None:
        if index == len(modes):
            if remaining == 0:
                states.append(dict(state))
            return
        n, pol = modes[index]
        for occ in range(remaining // n + 1):
            if occ:
                state[(n, pol)] = occ
            elif (n, pol) in state:
                del state[(n, pol)]
            rec(index + 1, remaining - occ * n, state)
        state.pop((n, pol), None)

    rec(0, level, {})
    return states


def reflected_state(state: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    return {(n, -pol): occ for (n, pol), occ in state.items()}


def state_key(state: dict[tuple[int, int], int]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted((n, pol, occ) for (n, pol), occ in state.items()))


def greek_label(lambda_abs: int) -> str:
    labels = {0: "Sigma", 1: "Pi", 2: "Delta", 3: "Phi", 4: "Lambda4"}
    return labels[lambda_abs]


def decompose_open_dinfty_channels(level: int) -> Counter[tuple[str, str, str | None]]:
    states = generate_open_fock_states(level)
    counter: Counter[tuple[str, str, str | None]] = Counter()
    zero_helicity: dict[tuple[tuple[int, int, int], ...], dict[tuple[int, int], int]] = {}

    for state in states:
        helicity = sum(pol * occ for (_n, pol), occ in state.items())
        gu = "g" if sum(n * occ for (n, _pol), occ in state.items()) % 2 == 0 else "u"
        if helicity != 0:
            counter[(greek_label(abs(helicity)), gu, None)] += 1
        else:
            zero_helicity[state_key(state)] = state

    visited: set[tuple[tuple[int, int, int], ...]] = set()
    for key, state in zero_helicity.items():
        if key in visited:
            continue
        gu = "g" if sum(n * occ for (n, _pol), occ in state.items()) % 2 == 0 else "u"
        refl_key = state_key(reflected_state(state))
        visited.add(key)
        visited.add(refl_key)
        if refl_key == key:
            counter[("Sigma", gu, "+")] += 1
        else:
            counter[("Sigma", gu, "+")] += 1
            counter[("Sigma", gu, "-")] += 1
    return counter


def check_open_dinfty_channel_decomposition() -> None:
    assert decompose_open_dinfty_channels(0) == Counter({("Sigma", "g", "+"): 1})
    assert decompose_open_dinfty_channels(1) == Counter({("Pi", "u", None): 2})
    assert decompose_open_dinfty_channels(2) == Counter(
        {
            ("Sigma", "g", "+"): 1,
            ("Pi", "g", None): 2,
            ("Delta", "g", None): 2,
        }
    )
    assert decompose_open_dinfty_channels(3) == Counter(
        {
            ("Sigma", "u", "+"): 1,
            ("Sigma", "u", "-"): 1,
            ("Pi", "u", None): 4,
            ("Delta", "u", None): 2,
            ("Phi", "u", None): 2,
        }
    )
    assert decompose_open_dinfty_channels(4) == Counter(
        {
            ("Sigma", "g", "+"): 3,
            ("Sigma", "g", "-"): 1,
            ("Pi", "g", None): 6,
            ("Delta", "g", None): 6,
            ("Phi", "g", None): 2,
            ("Lambda4", "g", None): 2,
        }
    )


def check_k_string_comparison_formulas() -> None:
    for n_c in range(3, 13):
        c_fund = Fraction(n_c * n_c - 1, n_c)
        for k_value in range(1, n_c):
            c_anti = Fraction(k_value * (n_c - k_value) * (n_c + 1), n_c)
            casimir_ratio = c_anti / c_fund
            assert_equal(
                f"antisymmetric Casimir ratio N={n_c}, k={k_value}",
                casimir_ratio,
                Fraction(k_value * (n_c - k_value), n_c - 1),
            )
            assert_equal(
                f"Casimir charge conjugation N={n_c}, k={k_value}",
                casimir_ratio,
                Fraction((n_c - k_value) * k_value, n_c - 1),
            )

            sine_ratio = sp.sin(sp.pi * k_value / n_c) / sp.sin(sp.pi / n_c)
            sine_conj = sp.sin(sp.pi * (n_c - k_value) / n_c) / sp.sin(sp.pi / n_c)
            assert_zero(f"sine charge conjugation N={n_c}, k={k_value}", sine_ratio - sine_conj)

    x, k = sp.symbols("x k", positive=True)
    sine_series = sp.series(sp.sin(sp.pi * k * x) / sp.sin(sp.pi * x), x, 0, 5).removeO()
    expected_sine = k - sp.pi**2 * k * (k**2 - 1) * x**2 / 6
    assert_zero("sine large-N constant term", sine_series.coeff(x, 0) - expected_sine.coeff(x, 0))
    assert_zero("sine large-N x^2 coefficient", sine_series.coeff(x, 2) - expected_sine.coeff(x, 2))

    casimir_x = k * (1 / x - k) / (1 / x - 1)
    casimir_series = sp.series(casimir_x, x, 0, 3).removeO()
    expected_casimir = k - k * (k - 1) * x
    assert_zero(
        "Casimir large-N x coefficient",
        casimir_series.coeff(x, 1) - expected_casimir.coeff(x, 1),
    )

    special_values = [
        (4, 2, Fraction(4, 3), sp.sqrt(2)),
        (5, 2, Fraction(3, 2), (1 + sp.sqrt(5)) / 2),
        (6, 2, Fraction(8, 5), sp.sqrt(3)),
        (6, 3, Fraction(9, 5), sp.Integer(2)),
        (8, 2, Fraction(12, 7), sp.sqrt(2 + sp.sqrt(2))),
        (8, 3, Fraction(15, 7), 1 + sp.sqrt(2)),
        (8, 4, Fraction(16, 7), sp.sqrt(4 + 2 * sp.sqrt(2))),
    ]
    for n_c, k_value, expected_casimir_value, expected_sine_value in special_values:
        assert_equal(
            f"displayed Casimir value N={n_c}, k={k_value}",
            Fraction(k_value * (n_c - k_value), n_c - 1),
            expected_casimir_value,
        )
        displayed_sine = sp.sin(sp.pi * k_value / n_c) / sp.sin(sp.pi / n_c)
        assert_zero(
            f"displayed sine value N={n_c}, k={k_value}",
            displayed_sine - expected_sine_value,
        )


def check_excited_level_expansion_coefficients() -> None:
    c_perp = Fraction(2, 1)

    # Open NG:
    # E = sigma L + pi A/L - pi^2 A^2/(2 sigma L^3) + ...
    open_level = Fraction(3, 1)
    open_a = open_level - c_perp / 24
    assert_equal("open excited 1/L coefficient", open_a, Fraction(35, 12))
    assert_equal("open excited 1/L^3 coefficient without pi^2/sigma", -open_a * open_a / 2, Fraction(-1225, 288))

    # Closed NG:
    # E = sigma L + 2 pi A/L + 2 pi^2(q^2 - A^2)/(sigma L^3) + ...
    n_left = Fraction(3, 1)
    n_right = Fraction(1, 1)
    q_momentum = Fraction(2, 1)
    closed_a = n_left + n_right - c_perp / 12
    assert_equal("closed level matching", n_left - n_right, q_momentum)
    assert_equal("closed excited 1/L coefficient without pi", 2 * closed_a, Fraction(23, 3))
    assert_equal(
        "closed excited 1/L^3 coefficient without pi^2/sigma",
        2 * (q_momentum * q_momentum - closed_a * closed_a),
        Fraction(-385, 18),
    )


def steiner_length_squared_from_sides(
    sum_squares: Fraction,
    four_sqrt_three_area: Fraction,
) -> Fraction:
    """Return L_Y^2 = (a^2+b^2+c^2+4 sqrt(3) Delta)/2."""

    return (sum_squares + four_sqrt_three_area) / 2


def check_baryonic_y_string_geometry() -> None:
    # Equilateral side length a=1:
    # Delta = sqrt(3)/4, so 4 sqrt(3) Delta = 3.
    equilateral_sum_squares = Fraction(3, 1)
    equilateral_four_sqrt_three_area = Fraction(3, 1)
    equilateral_y_squared = steiner_length_squared_from_sides(
        equilateral_sum_squares,
        equilateral_four_sqrt_three_area,
    )
    assert_equal(
        "equilateral Y-string length squared",
        equilateral_y_squared,
        Fraction(3, 1),
    )

    # The pairwise Delta comparison length is (a+b+c)/2 = 3/2 for a=1.
    delta_squared = Fraction(9, 4)
    assert_less(
        "equilateral Delta comparison shorter than Y length",
        delta_squared,
        equilateral_y_squared,
    )

    # At the 120-degree boundary with adjacent sides 1,1 and opposite side
    # sqrt(3), the Steiner formula gives L_Y^2 = 4, matching the collapsed
    # two-side network of length 2.
    threshold_sum_squares = Fraction(1, 1) + Fraction(1, 1) + Fraction(3, 1)
    threshold_four_sqrt_three_area = Fraction(3, 1)
    threshold_y_squared = steiner_length_squared_from_sides(
        threshold_sum_squares,
        threshold_four_sqrt_three_area,
    )
    assert_equal(
        "120-degree collapsed Y-string length squared",
        threshold_y_squared,
        Fraction(4, 1),
    )


def check_hagedorn_coefficient() -> None:
    # The saddle gives beta_H^2 sigma = pi c/3.  For open strings one uses
    # log rho ~ 2 pi sqrt(c N/6) and E^2 ~ 2 pi sigma N.  For closed strings
    # one uses twice the entropy, log rho ~ 4 pi sqrt(c N/6), and
    # E^2 ~ 8 pi sigma N.  The rational coefficient multiplying pi c/sigma is
    # the same in both cases.
    open_coefficient = Fraction(4, 1) * Fraction(1, 6) / Fraction(2, 1)
    closed_coefficient = Fraction(16, 1) * Fraction(1, 6) / Fraction(8, 1)
    assert_equal("open Hagedorn beta coefficient", open_coefficient, Fraction(1, 3))
    assert_equal("closed Hagedorn beta coefficient", closed_coefficient, Fraction(1, 3))


def main() -> None:
    check_open_and_closed_casimir_coefficients()
    check_nambu_goto_reference_expansion()
    check_open_oscillator_degeneracies()
    check_open_dinfty_channel_decomposition()
    check_k_string_comparison_formulas()
    check_excited_level_expansion_coefficients()
    check_baryonic_y_string_geometry()
    check_hagedorn_coefficient()
    print("All QCD-string effective-spectrum checks passed.")


if __name__ == "__main__":
    main()
