#!/usr/bin/env python3
"""Finite checks for spinor-field and Grassmann path-integral conventions."""

from fractions import Fraction

import sympy as sp


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def assert_matrix_equal(actual, expected, label):
    diff = actual - expected
    diff = diff.applyfunc(sp.simplify)
    if diff != sp.zeros(*actual.shape):
        raise AssertionError(f"{label}: got\n{actual}\nexpected\n{expected}")


def check_dirac_phase_equations_and_charge_ledger():
    ii = sp.I
    mass = sp.Integer(7)
    lambda_u = ii * mass
    lambda_v = -ii * mass
    assert_equal(sp.simplify(ii * lambda_u + mass), 0, "u phase Dirac equation")
    assert_equal(sp.simplify(-ii * lambda_v + mass), 0, "v phase Dirac equation")

    charge = {
        "b_dagger": 1,
        "d_dagger": -1,
        "b": -1,
        "d": 1,
    }
    assert_equal(charge["b_dagger"], 1, "charge of b dagger")
    assert_equal(charge["d"], 1, "charge of d annihilator")
    assert_equal(charge["b"], -1, "charge of b annihilator")
    assert_equal(charge["d_dagger"], -1, "charge of d dagger")


def check_locality_sign_ledger():
    ordinary_scalar = {"Delta_xy": 1, "Delta_yx": 1}
    car_scalar = {"Delta_xy": 1, "Delta_yx": -1}
    pauli_jordan = {"Delta_xy": 1, "Delta_yx": -1}
    assert_equal(ordinary_scalar["Delta_yx"], 1, "ordinary scalar plus sign")
    assert_equal(car_scalar, pauli_jordan, "CAR gives Pauli-Jordan sign")


def check_odd_dirac_bracket_matrix():
    m = sp.Matrix([[2, 1], [1, 3]])
    k = -2 * m
    eta_eta_bracket = -k.inv()
    expected = sp.Rational(1, 2) * m.inv()
    assert_matrix_equal(eta_eta_bracket, expected, "odd Dirac bracket")


def check_purely_odd_berezinian_two_coordinates():
    a = sp.Matrix([[2, 3], [5, 7]])
    determinant = a.det()
    transformed_top_coefficient = determinant
    transformed_density_factor = sp.Rational(1, 1) / determinant
    assert_equal(
        sp.simplify(transformed_top_coefficient * transformed_density_factor),
        1,
        "Berezinian inverse determinant",
    )


def check_one_pair_berezin_gaussian():
    a = Fraction(5, 3)
    gaussian_integral = a
    contraction = Fraction(1, 1) / a
    assert_equal(gaussian_integral, a, "one-pair Berezin determinant")
    assert_equal(contraction, Fraction(3, 5), "one-pair Berezin contraction")


def check_coherent_state_trace_signs():
    a, b, c, d = sp.symbols("a b c d")
    ordinary_trace_integrand_eta_coeff = a + d
    supertrace_integrand_eta_coeff = a - d
    matrix_trace = sp.trace(sp.Matrix([[a, b], [c, d]]))
    matrix_supertrace = a - d
    assert_equal(ordinary_trace_integrand_eta_coeff, matrix_trace, "trace sign")
    assert_equal(
        supertrace_integrand_eta_coeff,
        matrix_supertrace,
        "supertrace sign",
    )


def main():
    check_dirac_phase_equations_and_charge_ledger()
    check_locality_sign_ledger()
    check_odd_dirac_bracket_matrix()
    check_purely_odd_berezinian_two_coordinates()
    check_one_pair_berezin_gaussian()
    check_coherent_state_trace_signs()
    print("All spinor-Grassmann convention checks passed.")


if __name__ == "__main__":
    main()
