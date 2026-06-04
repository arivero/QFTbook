#!/usr/bin/env python3
"""Finite polynomial checks for pAQFT algebra identities.

The script models a one-dimensional version of the Hadamard star product

    F *_H G = sum_n hbar^n H^n/n! D^n F D^n G

on polynomials.  This cannot prove the distributional theorems, but it checks
the algebraic identities used in the chapter: associativity and the
intertwiner for a smooth change H -> H + w.

Evidence contract.
Target claims: the finite algebra subclaims in Volume XII Chapter 10,
including Hadamard star-product associativity, smooth-Hadamard-change
intertwining, scaling-degree ambiguity counts, and the lambda-phi-four
Hadamard-coordinate/local-Wick-renormalization example.
Independent construction: exact polynomial derivatives, contraction sums,
Taylor-extension counts, and Wick-power transport coefficients are computed
directly in a finite polynomial model rather than copied from the prose
formulae.
Imported assumptions: the one-component polynomial model, formal hbar
grading, smooth diagonal Hadamard coordinate difference, local finite Wick
renormalization scalar, and the chapter's normalization of the quartic
interaction lambda Phi^4/4! are finite inputs.
Negative controls: wrong scaling-degree uniqueness thresholds, missing
quartic tadpole factors, omitted vacuum bubble terms, untyped
coordinate-transport expectation shifts, and incorrect mass/curvature
coordinate factors are rejected by exact rational comparisons.
Scope boundary: a pass checks finite pAQFT algebra and coefficient
bookkeeping; it does not prove microlocal extension theorems, continuum
Hadamard state existence, perturbative convergence, interacting stress-tensor
existence, or nonperturbative curved-spacetime QFT.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

Poly = dict[int, Fraction]
HPoly = dict[int, Poly]


def clean_poly(poly: Poly) -> Poly:
    return {degree: coeff for degree, coeff in poly.items() if coeff}


def clean_hpoly(poly: HPoly) -> HPoly:
    return {h: clean_poly(p) for h, p in poly.items() if clean_poly(p)}


def monomial(power: int, coeff: Fraction = Fraction(1)) -> HPoly:
    return {0: {power: coeff}}


def add_poly(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for degree, coeff in b.items():
        out[degree] = out.get(degree, Fraction(0)) + coeff
    return clean_poly(out)


def scale_poly(poly: Poly, coeff: Fraction) -> Poly:
    return clean_poly({degree: coeff * value for degree, value in poly.items()})


def scale_hpoly(poly: HPoly, coeff: Fraction) -> HPoly:
    return clean_hpoly({
        hpower: scale_poly(p, coeff)
        for hpower, p in poly.items()
    })


def mul_poly(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for da, ca in a.items():
        for db, cb in b.items():
            out[da + db] = out.get(da + db, Fraction(0)) + ca * cb
    return clean_poly(out)


def deriv_poly(poly: Poly, order: int) -> Poly:
    out = dict(poly)
    for _ in range(order):
        out = {
            degree - 1: coeff * degree
            for degree, coeff in out.items()
            if degree > 0
        }
    return clean_poly(out)


def add_hpoly(a: HPoly, b: HPoly) -> HPoly:
    out = dict(a)
    for hpower, poly in b.items():
        out[hpower] = add_poly(out.get(hpower, {}), poly)
    return clean_hpoly(out)


def star(a: HPoly, b: HPoly, kernel: Fraction) -> HPoly:
    out: HPoly = {}
    max_degree = max(
        [0]
        + [degree for poly in a.values() for degree in poly]
        + [degree for poly in b.values() for degree in poly]
    )
    for ha, pa in a.items():
        for hb, pb in b.items():
            for order in range(max_degree + 1):
                da = deriv_poly(pa, order)
                db = deriv_poly(pb, order)
                if not da or not db:
                    continue
                coeff = kernel**order / Fraction(factorial(order))
                hpower = ha + hb + order
                term = scale_poly(mul_poly(da, db), coeff)
                out[hpower] = add_poly(out.get(hpower, {}), term)
    return clean_hpoly(out)


def second_laplacian(poly: HPoly, w: Fraction) -> HPoly:
    out: HPoly = {}
    for hpower, p in poly.items():
        term = scale_poly(deriv_poly(p, 2), w)
        if term:
            out[hpower] = add_poly(out.get(hpower, {}), term)
    return clean_hpoly(out)


def alpha(poly: HPoly, w: Fraction) -> HPoly:
    out = poly
    term = poly
    for order in range(1, 16):
        term = second_laplacian(term, w)
        if not term:
            break
        coeff = Fraction(1, 2) ** order / Fraction(factorial(order))
        shifted = {
            hpower + order: scale_poly(p, coeff)
            for hpower, p in term.items()
        }
        out = add_hpoly(out, shifted)
    return clean_hpoly(out)


def assert_equal(got: HPoly, expected: HPoly, label: str) -> None:
    if clean_hpoly(got) != clean_hpoly(expected):
        raise AssertionError(f"{label}: got {got}, expected {expected}")


def quasifree_expectation(poly: HPoly, wick_square: Fraction) -> Fraction:
    total = Fraction(0)
    for hpower, terms in poly.items():
        hbar_factor = Fraction(1)  # hbar is kept as a grading and set to one here.
        for degree, coeff in terms.items():
            if degree == 0:
                moment = Fraction(1)
            elif degree == 2:
                moment = wick_square
            elif degree == 4:
                moment = 3 * wick_square * wick_square
            else:
                raise AssertionError(f"unsupported quasifree moment degree {degree}")
            total += hbar_factor * coeff * moment
    return total


def check_associativity() -> None:
    h = Fraction(3, 5)
    f = monomial(3)        # phi^3
    g = monomial(2)        # phi^2
    k = monomial(4, Fraction(2))
    left = star(star(f, g, h), k, h)
    right = star(f, star(g, k, h), h)
    assert_equal(left, right, "Hadamard star product associativity")


def check_hadamard_change_intertwiner() -> None:
    h = Fraction(2, 7)
    w = Fraction(5, 11)
    f = add_hpoly(monomial(4), monomial(1, Fraction(3)))
    g = add_hpoly(monomial(3, Fraction(2)), monomial(0, Fraction(-1)))
    left = alpha(star(f, g, h), w)
    right = star(alpha(f, w), alpha(g, w), h + w)
    assert_equal(left, right, "Hadamard smooth-change intertwiner")


def check_scaling_degree_ambiguity_count() -> None:
    def ambiguity_count(dimension: int, scaling_degree_floor: int) -> int:
        r = scaling_degree_floor - dimension
        if r < 0:
            return 0
        return comb(dimension + r, r)

    if ambiguity_count(4, 3) != 0:
        raise AssertionError("sd < dimension should give a unique extension")
    if ambiguity_count(4, 4) != 1:
        raise AssertionError("logarithmic divergence should allow delta only")
    if ambiguity_count(4, 6) != 15:
        raise AssertionError("derivatives through order two in R^4 count 15")


def check_lambda_phi4_hadamard_scheme_transport() -> None:
    w = Fraction(7, 13)
    coupling = Fraction(5, 11)

    transported_quartic = scale_hpoly(alpha(monomial(4), w), coupling / 24)
    expected_quartic: HPoly = {
        0: {4: coupling / 24},
        1: {2: coupling * w / 4},
        2: {0: coupling * w * w / 8},
    }
    assert_equal(
        transported_quartic,
        expected_quartic,
        "lambda phi^4 Hadamard-coordinate transport",
    )

    wrong_tadpole_factor = coupling * w / 8
    if transported_quartic[1][2] == wrong_tadpole_factor:
        raise AssertionError("quartic tadpole factor should be 6/4!, not 3/4!")
    if transported_quartic.get(2, {}).get(0, Fraction(0)) == 0:
        raise AssertionError("quartic coordinate transport should retain the vacuum term")

    transported_wick_square = alpha(monomial(2), w)
    assert_equal(
        transported_wick_square,
        {0: {2: Fraction(1)}, 1: {0: w}},
        "Wick-square Hadamard-coordinate transport",
    )

    omega_h_square = Fraction(11, 5)
    omega_hprime_square = omega_h_square - w
    transported_value = quasifree_expectation(transported_wick_square, omega_hprime_square)
    original_value = quasifree_expectation(monomial(2), omega_h_square)
    if transported_value != original_value:
        raise AssertionError("coordinate transport with transported state should be invariant")

    untyped_same_state_shift = (
        quasifree_expectation(transported_wick_square, omega_h_square)
        - original_value
    )
    if untyped_same_state_shift == transported_value - original_value:
        raise AssertionError("untyped expectation-shift interpretation was not rejected")
    if untyped_same_state_shift != w:
        raise AssertionError("same-state coordinate comparison should expose the c-number pitfall")

    local_wick_shift = Fraction(3, 10)
    fixed_state_wick_square = add_hpoly(monomial(2), {1: {0: local_wick_shift}})
    fixed_state_shift = (
        quasifree_expectation(fixed_state_wick_square, omega_h_square)
        - original_value
    )
    if fixed_state_shift != local_wick_shift:
        raise AssertionError("fixed-state Wick-renormalization shift coefficient is incorrect")

    a_m = Fraction(2, 5)
    a_r = Fraction(3, 7)
    if coupling * a_m / 2 != Fraction(1, 11):
        raise AssertionError("mass-coordinate shift coefficient is incorrect")
    if coupling * a_r / 2 != Fraction(15, 154):
        raise AssertionError("curvature-coupling shift coefficient is incorrect")

    vacuum_m4 = coupling * a_m * a_m / 8
    vacuum_m2r = coupling * a_m * a_r / 4
    vacuum_r2 = coupling * a_r * a_r / 8
    if vacuum_m4 != Fraction(1, 110):
        raise AssertionError("m^4 geometric-source coordinate is incorrect")
    if vacuum_m2r != Fraction(3, 154):
        raise AssertionError("m^2 R geometric-source coordinate is incorrect")
    if vacuum_r2 != Fraction(45, 4312):
        raise AssertionError("R^2 geometric-source coordinate is incorrect")


def main() -> None:
    check_associativity()
    check_hadamard_change_intertwiner()
    check_scaling_degree_ambiguity_count()
    check_lambda_phi4_hadamard_scheme_transport()
    print("All pAQFT algebra and scaling-degree checks passed.")


if __name__ == "__main__":
    main()
