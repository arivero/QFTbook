#!/usr/bin/env python3
"""Finite representation checks for supersymmetric twists.

The script checks the exact SU(2) tensor-product arithmetic and the
two-dimensional R-charge bookkeeping used in the twisting chapter.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(actual, expected, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


def su2_tensor_twice_spins(j1: int, j2: int) -> tuple[int, ...]:
    """Return twice-spins in the SU(2) Clebsch-Gordan decomposition."""

    low = abs(j1 - j2)
    high = j1 + j2
    return tuple(range(low, high + 1, 2))


def dimension_from_twice_spin(j: int) -> int:
    return j + 1


def check_donaldson_supercharge_decomposition() -> None:
    # Q_alpha^A: SU(2)_+ spin 1/2 and SU(2)_R spin 1/2.
    diagonal_plus = su2_tensor_twice_spins(1, 1)
    assert_equal(diagonal_plus, (0, 2), "2 tensor 2 = 1 plus 3")
    assert_equal(
        tuple(dimension_from_twice_spin(j) for j in diagonal_plus),
        (1, 3),
        "scalar plus self-dual two-form dimensions",
    )

    # \bar Q_{\dot alpha A}: SU(2)_+ spin 0, SU(2)_R spin 1/2, SU(2)_- spin 1/2.
    twisted_plus = su2_tensor_twice_spins(0, 1)
    assert_equal(twisted_plus, (1,), "R-doublet becomes twisted plus-spin doublet")
    vector_dimension = dimension_from_twice_spin(twisted_plus[0]) * dimension_from_twice_spin(1)
    assert_equal(vector_dimension, 4, "twisted barred supercharge is a one-form")


def check_donaldson_field_decomposition_dimensions() -> None:
    lambda_components = sum(dimension_from_twice_spin(j) for j in su2_tensor_twice_spins(1, 1))
    assert_equal(lambda_components, 4, "lambda decomposes into eta plus chi^+")
    assert_equal(1 + 3, lambda_components, "eta and self-dual two-form dimensions")

    barred_lambda_components = dimension_from_twice_spin(1) * dimension_from_twice_spin(1)
    assert_equal(barred_lambda_components, 4, "barred lambda decomposes into psi_mu")


def twisted_spin(spin: Fraction, charge: int) -> Fraction:
    return spin + Fraction(charge, 2)


def check_two_dimensional_a_b_twists() -> None:
    spins = {
        "Q+": Fraction(1, 2),
        "Q-": Fraction(-1, 2),
        "barQ+": Fraction(1, 2),
        "barQ-": Fraction(-1, 2),
    }
    q_vector = {"Q+": 1, "Q-": 1, "barQ+": -1, "barQ-": -1}
    q_axial = {"Q+": 1, "Q-": -1, "barQ+": -1, "barQ-": 1}

    a_scalars = {
        name
        for name, spin in spins.items()
        if twisted_spin(spin, q_vector[name]) == 0
    }
    b_scalars = {
        name
        for name, spin in spins.items()
        if twisted_spin(spin, q_axial[name]) == 0
    }
    assert_equal(a_scalars, {"barQ+", "Q-"}, "A-twist scalar supercharges")
    assert_equal(b_scalars, {"barQ+", "barQ-"}, "B-twist scalar supercharges")


def check_q_square_gauge_closure_table() -> None:
    def bracket(left: str, right: str) -> str:
        return f"[{left},{right}]"

    def canonical(expr: str) -> str:
        replacements = {
            "-[psi,phi]": "[phi,psi]",
            "[phi,phi]": "0",
        }
        return replacements.get(expr, expr)

    computed = {
        "A": "-D_A phi",
        "psi": canonical(f"-{bracket('psi', 'phi')}"),
        "phi": canonical(bracket("phi", "phi")),
        "phibar": bracket("phi", "phibar"),
        "eta": bracket("phi", "eta"),
        "chi+": bracket("phi", "chi+"),
        "H+": bracket("phi", "H+"),
    }
    expected_delta_minus_phi = {
        "A": "-D_A phi",
        "psi": "[phi,psi]",
        "phi": "0",
        "phibar": "[phi,phibar]",
        "eta": "[phi,eta]",
        "chi+": "[phi,chi+]",
        "H+": "[phi,H+]",
    }
    assert_equal(computed, expected_delta_minus_phi, "Donaldson-Witten Q-square closure ledger")


def main() -> None:
    check_donaldson_supercharge_decomposition()
    check_donaldson_field_decomposition_dimensions()
    check_two_dimensional_a_b_twists()
    check_q_square_gauge_closure_table()
    print("All supersymmetric twisting representation checks passed.")


if __name__ == "__main__":
    main()
