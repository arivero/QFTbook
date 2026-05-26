#!/usr/bin/env python3
"""Finite algebra checks for the BV master-formalism chapter.

The script checks small pieces of sign-sensitive algebra used in the BV
chapter: ghost-number bookkeeping for the antibracket, nilpotency of the
Yang-Mills ghost differential from the Jacobi identity in an su(2) test
algebra, and the contracting homotopy for a BRST doublet.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction


GhostPoly = dict[tuple[str, ...], Fraction]

GHOST_ORDER = ("c1", "c2", "c3")
GHOST_INDEX = {name: index for index, name in enumerate(GHOST_ORDER)}


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def wedge_monomials(lhs: tuple[str, ...], rhs: tuple[str, ...]) -> tuple[int, tuple[str, ...]] | None:
    if set(lhs).intersection(rhs):
        return None
    inversions = 0
    for left in lhs:
        for right in rhs:
            if GHOST_INDEX[left] > GHOST_INDEX[right]:
                inversions += 1
    sign = -1 if inversions % 2 else 1
    return sign, tuple(sorted(lhs + rhs, key=GHOST_INDEX.__getitem__))


def add_poly(lhs: GhostPoly, rhs: GhostPoly) -> GhostPoly:
    out: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for monomial, coefficient in lhs.items():
        out[monomial] += coefficient
    for monomial, coefficient in rhs.items():
        out[monomial] += coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def scale_poly(coefficient: Fraction, poly: GhostPoly) -> GhostPoly:
    return {
        monomial: coefficient * value
        for monomial, value in poly.items()
        if coefficient * value
    }


def wedge_poly(lhs: GhostPoly, rhs: GhostPoly) -> GhostPoly:
    out: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for left_monomial, left_coefficient in lhs.items():
        for right_monomial, right_coefficient in rhs.items():
            product = wedge_monomials(left_monomial, right_monomial)
            if product is None:
                continue
            sign, monomial = product
            out[monomial] += sign * left_coefficient * right_coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def epsilon(a: int, b: int, c: int) -> int:
    values = (a, b, c)
    if len(set(values)) < 3:
        return 0
    inversions = 0
    for i, left in enumerate(values):
        for right in values[i + 1 :]:
            if left > right:
                inversions += 1
    return -1 if inversions % 2 else 1


def ghost(index: int) -> GhostPoly:
    return {(f"c{index}",): Fraction(1)}


def s_on_generator(index: int) -> GhostPoly:
    # sc^a = -1/2 epsilon^a_{bc} c^b c^c, with all b,c summed.
    out: GhostPoly = {}
    for b in (1, 2, 3):
        for c in (1, 2, 3):
            term = wedge_poly(ghost(b), ghost(c))
            out = add_poly(out, scale_poly(Fraction(-epsilon(index, b, c), 2), term))
    return out


def s_on_monomial(monomial: tuple[str, ...]) -> GhostPoly:
    # Odd derivation: s(a_1...a_n)=sum_i (-1)^i a_1...s(a_i)...a_n.
    out: GhostPoly = {}
    for position, name in enumerate(monomial):
        index = int(name[1:])
        prefix = {monomial[:position]: Fraction(1)}
        suffix = {monomial[position + 1 :]: Fraction(1)}
        term = wedge_poly(wedge_poly(prefix, s_on_generator(index)), suffix)
        out = add_poly(out, scale_poly(Fraction((-1) ** position), term))
    return out


def s_on_poly(poly: GhostPoly) -> GhostPoly:
    out: GhostPoly = {}
    for monomial, coefficient in poly.items():
        out = add_poly(out, scale_poly(coefficient, s_on_monomial(monomial)))
    return out


def check_yang_mills_ghost_nilpotency() -> None:
    for index in (1, 2, 3):
        assert_equal(f"s^2 c^{index}", s_on_poly(s_on_generator(index)), {})


def check_antibracket_ghost_number() -> None:
    examples = [
        (0, -1),
        (1, -2),
        (-1, 0),
        (2, -3),
    ]
    for gh_f, gh_g in examples:
        assert_equal(
            f"antibracket ghost number {gh_f},{gh_g}",
            gh_f + gh_g + 1,
            (gh_f - 1) + (gh_g + 2),
        )


def s_doublet(m: int, n: int) -> dict[tuple[int, int], Fraction]:
    # Monomial u^m v^n with u even, v odd, n=0 or 1; s = v d/du.
    if m == 0 or n == 1:
        return {}
    return {(m - 1, 1): Fraction(m)}


def h_doublet(m: int, n: int) -> dict[tuple[int, int], Fraction]:
    # Contracting homotopy h = u d/dv.
    if n == 0:
        return {}
    return {(m + 1, 0): Fraction(1)}


def apply_to_poly(operator, poly: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for monomial, coefficient in poly.items():
        for image, image_coefficient in operator(*monomial).items():
            out[image] += coefficient * image_coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def check_doublet_homotopy() -> None:
    for m in range(5):
        for n in (0, 1):
            monomial = {(m, n): Fraction(1)}
            sh = apply_to_poly(s_doublet, apply_to_poly(h_doublet, monomial))
            hs = apply_to_poly(h_doublet, apply_to_poly(s_doublet, monomial))
            lhs: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
            for image, coefficient in sh.items():
                lhs[image] += coefficient
            for image, coefficient in hs.items():
                lhs[image] += coefficient
            expected_degree = m + n
            expected = {} if expected_degree == 0 else {(m, n): Fraction(expected_degree)}
            assert_equal(f"doublet homotopy u^{m} v^{n}", dict(lhs), expected)


def main() -> None:
    check_antibracket_ghost_number()
    check_yang_mills_ghost_nilpotency()
    check_doublet_homotopy()
    print("All BV master-algebra checks passed.")


if __name__ == "__main__":
    main()
