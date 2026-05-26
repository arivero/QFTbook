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

print(
    "All Liouville BPZ, screening, connection-matrix, "
    "and DOZZ-shift checks passed."
)
