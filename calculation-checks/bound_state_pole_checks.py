#!/usr/bin/env python3
"""Finite checks for bound-state pole factorization algebra.

These checks accompany Volume II, Chapter 3.  They verify the algebraic
pieces used in the spectral/LSZ pole discussion: finite-rank residue
factorization, Legendre projection of a spin-J residue, the scalar-QED
P_1 angular numerator, and the below-threshold denominator conversion
P^2+M^2 = M^2-s in the mostly-plus convention.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def trim(poly):
    coeffs = list(poly)
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
    return tuple(coeffs) if coeffs else (Fraction(0),)


def poly_add(left, right):
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def poly_mul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_integral_minus_one_to_one(poly):
    total = Fraction(0)
    for power, coeff in enumerate(poly):
        if power % 2 == 0:
            total += coeff * Fraction(2, power + 1)
    return total


LEGENDRE = {
    0: (Fraction(1),),
    1: (Fraction(0), Fraction(1)),
    2: (Fraction(-1, 2), Fraction(0), Fraction(3, 2)),
    3: (Fraction(0), Fraction(-3, 2), Fraction(0), Fraction(5, 2)),
    4: (Fraction(3, 8), Fraction(0), Fraction(-30, 8), Fraction(0), Fraction(35, 8)),
}


def check_legendre_orthogonality():
    for ell, p_ell in LEGENDRE.items():
        for spin, p_spin in LEGENDRE.items():
            integral = poly_integral_minus_one_to_one(poly_mul(p_ell, p_spin))
            expected = Fraction(2, 2 * spin + 1) if ell == spin else Fraction(0)
            assert_equal(f"Legendre projection ell={ell}, spin={spin}", integral, expected)


def check_spin_residue_partial_wave_selection():
    # If M(s,z) has pole residue C P_J(z), then the ordered 16 pi convention
    # gives residue C/(16 pi (2J+1)) in a_J and no residue in other channels.
    # We omit the common symbolic factor C/pi and check the rational moments.
    spin = 2
    for ell, p_ell in LEGENDRE.items():
        moment = Fraction(1, 32) * poly_integral_minus_one_to_one(
            poly_mul(p_ell, LEGENDRE[spin])
        )
        expected = Fraction(1, 16 * (2 * spin + 1)) if ell == spin else Fraction(0)
        assert_equal(f"partial-wave residue selection ell={ell}", moment, expected)


def check_scalar_qed_p1_numerator():
    # The center-of-mass scalar-QED numerator is proportional to 4 k^2 z.
    # Its Legendre decomposition has only the P_1 component.
    numerator = (Fraction(0), Fraction(4))
    for ell, p_ell in LEGENDRE.items():
        projection = Fraction(1, 2) * (2 * ell + 1) * poly_integral_minus_one_to_one(
            poly_mul(p_ell, numerator)
        )
        expected = Fraction(4) if ell == 1 else Fraction(0)
        assert_equal(f"scalar-QED numerator P_{ell}", projection, expected)


def check_finite_rank_residue_factorization():
    # Matrix elements through a finite spectral projection Pi_B factorize as
    # sum_lambda out_lambda * in_lambda.  In matrix form the residue rank is at
    # most the degeneracy d_B.
    out = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(-1)]]
    inn = [[Fraction(5), Fraction(7)], [Fraction(11), Fraction(13)]]
    residue = [
        [
            sum(out[row][lam] * inn[lam][col] for lam in range(2))
            for col in range(2)
        ]
        for row in range(2)
    ]
    expected = [
        [Fraction(27), Fraction(33)],
        [Fraction(4), Fraction(8)],
    ]
    assert_equal("finite-rank residue matrix", residue, expected)

    determinant = residue[0][0] * residue[1][1] - residue[0][1] * residue[1][0]
    # Here the two channel vectors are independent, so the rank is exactly two.
    assert_true("finite-rank residue determinant nonzero", determinant != 0)

    rank_one_out = [[Fraction(2)], [Fraction(3)]]
    rank_one_in = [[Fraction(5), Fraction(7)]]
    rank_one = [
        [rank_one_out[row][0] * rank_one_in[0][col] for col in range(2)]
        for row in range(2)
    ]
    rank_one_det = rank_one[0][0] * rank_one[1][1] - rank_one[0][1] * rank_one[1][0]
    assert_equal("rank-one pole residue determinant", rank_one_det, Fraction(0))


def check_mostly_plus_denominator_conversion():
    mass_sq = Fraction(9)
    s_value = Fraction(5)
    p_squared = -s_value
    assert_equal("mostly-plus denominator", p_squared + mass_sq, mass_sq - s_value)
    assert_true("below-threshold pole lies below two-particle threshold", mass_sq < Fraction(16))


def main():
    check_legendre_orthogonality()
    check_spin_residue_partial_wave_selection()
    check_scalar_qed_p1_numerator()
    check_finite_rank_residue_factorization()
    check_mostly_plus_denominator_conversion()
    print("All bound-state pole factorization checks passed.")


if __name__ == "__main__":
    main()
