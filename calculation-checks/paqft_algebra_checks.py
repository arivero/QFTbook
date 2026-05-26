#!/usr/bin/env python3
"""Finite polynomial checks for pAQFT algebra identities.

The script models a one-dimensional version of the Hadamard star product

    F *_H G = sum_n hbar^n H^n/n! D^n F D^n G

on polynomials.  This cannot prove the distributional theorems, but it checks
the algebraic identities used in the chapter: associativity and the
intertwiner for a smooth change H -> H + w.
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


def main() -> None:
    check_associativity()
    check_hadamard_change_intertwiner()
    check_scaling_degree_ambiguity_count()
    print("All pAQFT algebra and scaling-degree checks passed.")


if __name__ == "__main__":
    main()
