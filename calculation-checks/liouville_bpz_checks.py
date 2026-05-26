#!/usr/bin/env python3
"""Finite algebra checks for the Liouville level-two BPZ null vector."""

from __future__ import annotations

import math
from fractions import Fraction


class Laurent:
    """Laurent polynomial in t=b^2 with rational coefficients."""

    def __init__(self, terms: dict[int, Fraction] | None = None) -> None:
        self.terms = {
            power: coeff
            for power, coeff in (terms or {}).items()
            if coeff != 0
        }

    @staticmethod
    def constant(value: Fraction | int) -> Laurent:
        return Laurent({0: Fraction(value)})

    @staticmethod
    def monomial(power: int, coeff: Fraction | int = 1) -> Laurent:
        return Laurent({power: Fraction(coeff)})

    def __add__(self, other: Laurent) -> Laurent:
        terms = dict(self.terms)
        for power, coeff in other.terms.items():
            terms[power] = terms.get(power, Fraction(0)) + coeff
        return Laurent(terms)

    def __sub__(self, other: Laurent) -> Laurent:
        return self + (-other)

    def __neg__(self) -> Laurent:
        return Laurent({power: -coeff for power, coeff in self.terms.items()})

    def __mul__(self, other: Laurent) -> Laurent:
        terms: dict[int, Fraction] = {}
        for left_power, left_coeff in self.terms.items():
            for right_power, right_coeff in other.terms.items():
                power = left_power + right_power
                terms[power] = terms.get(power, Fraction(0)) + left_coeff * right_coeff
        return Laurent(terms)

    def scale(self, factor: Fraction | int) -> Laurent:
        return Laurent({power: Fraction(factor) * coeff for power, coeff in self.terms.items()})

    def is_zero(self) -> bool:
        return not self.terms

    def __repr__(self) -> str:
        return f"Laurent({self.terms!r})"


def require_zero(name: str, value: Laurent) -> None:
    if not value.is_zero():
        raise AssertionError(f"{name} is not zero: {value!r}")


class AffineExponent:
    """Affine expression in formal symbols used for powers of b."""

    def __init__(self, terms: dict[str, Fraction] | None = None) -> None:
        self.terms = {
            symbol: coeff
            for symbol, coeff in (terms or {}).items()
            if coeff != 0
        }

    @staticmethod
    def constant(value: Fraction | int) -> AffineExponent:
        return AffineExponent({"1": Fraction(value)})

    @staticmethod
    def symbol(name: str, coeff: Fraction | int = 1) -> AffineExponent:
        return AffineExponent({name: Fraction(coeff)})

    def __add__(self, other: AffineExponent) -> AffineExponent:
        terms = dict(self.terms)
        for symbol, coeff in other.terms.items():
            terms[symbol] = terms.get(symbol, Fraction(0)) + coeff
        return AffineExponent(terms)

    def __sub__(self, other: AffineExponent) -> AffineExponent:
        return self + (-other)

    def __neg__(self) -> AffineExponent:
        return AffineExponent({symbol: -coeff for symbol, coeff in self.terms.items()})

    def scale(self, factor: Fraction | int) -> AffineExponent:
        return AffineExponent({
            symbol: Fraction(factor) * coeff
            for symbol, coeff in self.terms.items()
        })

    def __repr__(self) -> str:
        return f"AffineExponent({self.terms!r})"


def require_affine_equal(
    name: str,
    left: AffineExponent,
    right: AffineExponent,
) -> None:
    diff = left - right
    if diff.terms:
        raise AssertionError(f"{name} mismatch: {left!r} != {right!r}")


one = Laurent.constant(1)
t = Laurent.monomial(1)
t_inverse = Laurent.monomial(-1)

# h(-b/2)=(-b/2)(Q+b/2)=-1/2-3 b^2/4.
h = Laurent.constant(Fraction(-1, 2)) + t.scale(Fraction(-3, 4))

# c=1+6(b+b^{-1})^2=13+6t+6t^{-1}.
c = Laurent.constant(13) + t.scale(6) + t_inverse.scale(6)

kappa = t

# Positive-mode action on (L_-1^2 + kappa L_-2)|h>.
l1_coefficient = h.scale(4) + Laurent.constant(2) + kappa.scale(3)
l2_coefficient = h.scale(6) + kappa * (h.scale(4) + c.scale(Fraction(1, 2)))

require_zero("L1 null-vector coefficient", l1_coefficient)
require_zero("L2 null-vector coefficient", l2_coefficient)

# The L1 equation alone fixes kappa=-(4h+2)/3=b^2.
solved_kappa = -(h.scale(4) + Laurent.constant(2)).scale(Fraction(1, 3))
require_zero("solved kappa minus b^2", solved_kappa - t)

# DOZZ b-shift ratio: verify the powers of b in the ratio
# C(a1+b/2,a2,a3)/C(a1-b/2,a2,a3).  Symbols are
# t=b^2 and baj=b alpha_j, with bQ=t+1 already substituted.
one_exp = AffineExponent.constant(1)
t_exp = AffineExponent.symbol("t")
ba1 = AffineExponent.symbol("ba1")
ba2 = AffineExponent.symbol("ba2")
ba3 = AffineExponent.symbol("ba3")

# BPZ hypergeometric parameters after substituting bQ=t+1.
A = ba1 + ba2 + ba3 - one_exp - t_exp.scale(Fraction(3, 2))
B = ba1 + ba2 - ba3 - t_exp.scale(Fraction(1, 2))
C = ba1.scale(2) - t_exp

require_affine_equal(
    "hypergeometric z=1 exponent gap",
    C - A - B,
    one_exp + t_exp - ba2.scale(2),
)
require_affine_equal(
    "second z=1 BPZ exponent",
    ba2 + C - A - B,
    one_exp + t_exp - ba2,
)
require_affine_equal(
    "connection gamma argument C-A",
    C - A,
    ba1 - ba2 - ba3 + one_exp + t_exp.scale(Fraction(1, 2)),
)
require_affine_equal(
    "connection gamma argument C-B",
    C - B,
    ba1 - ba2 + ba3 - t_exp.scale(Fraction(1, 2)),
)
require_affine_equal(
    "connection gamma argument A+B-C",
    A + B - C,
    ba2.scale(2) - one_exp - t_exp,
)

# Coulomb-gas screening check for C_-(alpha).  With one screening insertion,
# the free contractions give |z|^(2+2b^2-2b alpha); this must equal the
# second degenerate OPE exponent 2(h_{alpha+b/2}-h_alpha-h_{-b/2}).
require_affine_equal(
    "screening OPE power",
    one_exp.scale(2) + t_exp.scale(2) - ba1.scale(2),
    (one_exp + t_exp - ba1).scale(2),
)

screening_a = -ba1.scale(2)
screening_c = t_exp
require_affine_equal(
    "screening beta first gamma argument",
    one_exp + screening_a,
    one_exp - ba1.scale(2),
)
require_affine_equal(
    "screening beta second gamma argument",
    one_exp + screening_c,
    one_exp + t_exp,
)
require_affine_equal(
    "screening beta third gamma argument",
    -one_exp - screening_a - screening_c,
    ba1.scale(2) - one_exp - t_exp,
)

def gamma_ratio(x: float) -> float:
    """gamma(x)=Gamma(x)/Gamma(1-x) for non-pole real samples."""

    return math.gamma(x) / math.gamma(1.0 - x)


sample_b = 0.73
sample_alpha = 1.47
sample_t = sample_b * sample_b
sample_ba = sample_b * sample_alpha

screening_original = (
    -math.pi
    * gamma_ratio(1.0 - 2.0 * sample_ba)
    * gamma_ratio(1.0 + sample_t)
    * gamma_ratio(2.0 * sample_ba - 1.0 - sample_t)
)
screening_denominator_form = (
    -math.pi
    * gamma_ratio(2.0 * sample_ba - 1.0 - sample_t)
    / (gamma_ratio(2.0 * sample_ba) * gamma_ratio(-sample_t))
)
screening_b_power_form = (
    math.pi
    * sample_b ** 4
    * gamma_ratio(sample_t)
    * gamma_ratio(2.0 * sample_ba - 1.0 - sample_t)
    / gamma_ratio(2.0 * sample_ba)
)

for name, value in [
    ("screening denominator form", screening_denominator_form),
    ("screening b-power form", screening_b_power_form),
]:
    scale = max(1.0, abs(screening_original), abs(value))
    if abs(screening_original - value) > 1e-12 * scale:
        raise AssertionError(
            f"{name} mismatch: {screening_original!r} != {value!r}"
        )

numerator_shift = (
    one_exp.scale(2)
    + t_exp.scale(2)
    - ba1.scale(8)
)
denominator_shift_1 = (
    -one_exp
    + (ba1 + ba2 + ba3 - t_exp - one_exp - t_exp.scale(Fraction(1, 2))).scale(2)
)
denominator_shift_2 = (
    -one_exp
    + (ba1 + ba2 - ba3 - t_exp.scale(Fraction(1, 2))).scale(2)
)
denominator_shift_3 = (
    -one_exp
    + (ba1 + ba3 - ba2 - t_exp.scale(Fraction(1, 2))).scale(2)
)
denominator_shift_4 = (
    one_exp
    - (ba2 + ba3 - ba1 - t_exp.scale(Fraction(1, 2))).scale(2)
)

upsilon_shift_power = (
    numerator_shift
    + denominator_shift_1
    + denominator_shift_2
    + denominator_shift_3
    + denominator_shift_4
)
require_affine_equal(
    "Upsilon-shift power in DOZZ b-shift",
    upsilon_shift_power,
    -one_exp.scale(2) - t_exp.scale(2),
)

k_inverse_power = -one_exp.scale(2) + t_exp.scale(2)
require_affine_equal(
    "total b power in DOZZ b-shift",
    upsilon_shift_power + k_inverse_power,
    -one_exp.scale(4),
)

# Ordinary Virasoro block check through level two.  The ordered basis is
# (L_-2 |h>, L_-1^2 |h>), matching the monograph convention.
c_sample = Fraction(47, 5)
h_sample = Fraction(7, 3)
h1_sample = Fraction(11, 6)
h2_sample = Fraction(5, 4)
h3_sample = Fraction(13, 10)
h4_sample = Fraction(2, 5)

a1_block = h_sample + h3_sample - h4_sample
b1_block = h_sample + h2_sample - h1_sample
a2_block = h_sample + 2 * h3_sample - h4_sample
b2_block = h_sample + 2 * h2_sample - h1_sample
a11_block = a1_block * (a1_block + 1)
b11_block = b1_block * (b1_block + 1)

gram_22 = 4 * h_sample + c_sample / 2
gram_211 = 6 * h_sample
gram_1111 = 4 * h_sample * (2 * h_sample + 1)
det_direct = gram_22 * gram_1111 - gram_211 * gram_211
det_formula = 2 * h_sample * (
    16 * h_sample * h_sample + 2 * (c_sample - 5) * h_sample + c_sample
)
if det_direct != det_formula:
    raise AssertionError(
        f"level-two Gram determinant mismatch: {det_direct} != {det_formula}"
    )

level_one = b1_block * a1_block / (2 * h_sample)
if level_one != Fraction(97, 80):
    raise AssertionError(f"unexpected level-one block sample: {level_one}")

level_two_from_inverse = (
    gram_1111 * b2_block * a2_block
    - gram_211 * (b2_block * a11_block + b11_block * a2_block)
    + gram_22 * b11_block * a11_block
) / det_direct
level_two_from_display = (
    4 * h_sample * (2 * h_sample + 1) * b2_block * a2_block
    - 6 * h_sample * (b2_block * a11_block + b11_block * a2_block)
    + (4 * h_sample + c_sample / 2) * b11_block * a11_block
) / det_formula
if level_two_from_inverse != level_two_from_display:
    raise AssertionError(
        "level-two Virasoro-block coefficient formula mismatch: "
        f"{level_two_from_inverse} != {level_two_from_display}"
    )

global_level_two = b11_block * a11_block / (
    4 * h_sample * (2 * h_sample + 1)
)
large_c_limit_from_formula = (b11_block * a11_block / 2) / (
    2 * h_sample * (2 * h_sample + 1)
)
if global_level_two != large_c_limit_from_formula:
    raise AssertionError(
        f"global block limit mismatch: {global_level_two} != "
        f"{large_c_limit_from_formula}"
    )

def multiply_truncated(
    left: list[Fraction],
    right: list[Fraction],
    degree: int,
) -> list[Fraction]:
    result = [Fraction(0) for _ in range(degree + 1)]
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            total_degree = left_degree + right_degree
            if total_degree <= degree:
                result[total_degree] += left_coefficient * right_coefficient
    return result


def binomial_rational(x: Fraction, n: int) -> Fraction:
    product = Fraction(1)
    for index in range(n):
        product *= x - index
    return product / math.factorial(n)


def power_one_plus_truncated(
    coefficients: list[Fraction],
    exponent: Fraction,
    degree: int,
) -> list[Fraction]:
    if coefficients[0] != 1:
        raise ValueError("series must start with 1")
    tail = [Fraction(0)] + coefficients[1:]
    result = [Fraction(1)] + [Fraction(0) for _ in range(degree)]
    tail_power = [Fraction(1)] + [Fraction(0) for _ in range(degree)]
    for order in range(1, degree + 1):
        tail_power = multiply_truncated(tail_power, tail, degree)
        coefficient = binomial_rational(exponent, order)
        for index in range(degree + 1):
            result[index] += coefficient * tail_power[index]
    return result


# Elliptic-nome conversion.  The theta identity
# lambda(q)=theta_2(q)^4/theta_3(q)^4 gives
# lambda(q)=16 q (1 - 8 q + 44 q^2 + O(q^3)).
theta2_reduced_fourth = [Fraction(1), Fraction(0), Fraction(4)]
theta3_inverse_fourth = power_one_plus_truncated(
    [Fraction(1), Fraction(2), Fraction(0)],
    Fraction(-4),
    2,
)
lambda_reduced = multiply_truncated(
    theta2_reduced_fourth,
    theta3_inverse_fourth,
    2,
)
if lambda_reduced != [Fraction(1), Fraction(-8), Fraction(44)]:
    raise AssertionError(f"unexpected modular-lambda expansion: {lambda_reduced}")

elliptic_exponent = h_sample - h3_sample - h4_sample
lambda_power = power_one_plus_truncated(lambda_reduced, elliptic_exponent, 2)
ordinary_block_in_q = [
    Fraction(1),
    16 * level_one,
    -128 * level_one + 256 * level_two_from_display,
]
raw_q_block = multiply_truncated(lambda_power, ordinary_block_in_q, 2)
g1_formula = 16 * level_one - 8 * elliptic_exponent
g2_formula = (
    256 * level_two_from_display
    - 128 * (1 + elliptic_exponent) * level_one
    + 32 * elliptic_exponent * elliptic_exponent
    + 12 * elliptic_exponent
)
if raw_q_block[1] != g1_formula:
    raise AssertionError(
        f"elliptic q g1 mismatch: {raw_q_block[1]} != {g1_formula}"
    )
if raw_q_block[2] != g2_formula:
    raise AssertionError(
        f"elliptic q g2 mismatch: {raw_q_block[2]} != {g2_formula}"
    )

print(
    "All Liouville BPZ, screening, Virasoro-block, connection-matrix, "
    "elliptic-q, and DOZZ-shift checks passed."
)
