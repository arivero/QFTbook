#!/usr/bin/env python3
"""Finite arithmetic checks for orbifold twist-field weights."""

from fractions import Fraction


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def cyclic_permutation_weight(c_seed, length):
    return Fraction(c_seed, 24) * (Fraction(length, 1) - Fraction(1, length))


def complex_rotation_weight(alpha):
    return Fraction(1, 2) * alpha * (1 - alpha)


def hurwitz_zeta_minus_one(argument):
    return -Fraction(1, 2) * (argument * argument - argument + Fraction(1, 6))


def complex_rotation_weight_from_zeta(alpha):
    return (
        Fraction(1, 2) * hurwitz_zeta_minus_one(alpha)
        + Fraction(1, 2) * hurwitz_zeta_minus_one(1 - alpha)
        - hurwitz_zeta_minus_one(1)
    )


for c_seed in [1, 6, 12, 24]:
    for length in range(2, 11):
        h = cyclic_permutation_weight(c_seed, length)
        schwarzian = Fraction(1, 2) * (1 - Fraction(1, length * length))
        from_cover = Fraction(c_seed, 12) * length * schwarzian
        require(
            h == from_cover,
            f"cover Schwarzian mismatch for c={c_seed}, K={length}",
        )

require(
    cyclic_permutation_weight(6, 2) == Fraction(3, 8),
    "N=(4,4) seed c=6 length-two bare twist should have h=3/8",
)
require(
    cyclic_permutation_weight(12, 2) == Fraction(3, 4),
    "seed c=12 length-two bare twist should have h=3/4",
)
require(
    cyclic_permutation_weight(12, 3) == Fraction(4, 3),
    "seed c=12 length-three bare twist should have h=4/3",
)

for denominator in range(2, 15):
    for numerator in range(1, denominator):
        alpha = Fraction(numerator, denominator)
        require(
            complex_rotation_weight(alpha)
            == complex_rotation_weight(1 - alpha),
            f"alpha <-> 1-alpha symmetry failed for {alpha}",
        )
        require(
            complex_rotation_weight_from_zeta(alpha) == complex_rotation_weight(alpha),
            f"Hurwitz-zeta oscillator shift failed for {alpha}",
        )

require(
    hurwitz_zeta_minus_one(1) == Fraction(-1, 12),
    "untwisted zeta-regularized oscillator sum should be -1/12",
)

require(
    complex_rotation_weight(Fraction(1, 2)) / 2 == Fraction(1, 16),
    "real Z2 reflection twist should have h=1/16",
)
require(
    complex_rotation_weight(Fraction(1, 3)) == Fraction(1, 9),
    "complex Z3 rotation twist should have h=1/9",
)
require(
    complex_rotation_weight(Fraction(1, 4)) == Fraction(3, 32),
    "complex Z4 rotation twist should have h=3/32",
)

print("All orbifold twist-weight checks passed.")
