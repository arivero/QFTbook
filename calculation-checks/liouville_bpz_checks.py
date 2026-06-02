#!/usr/bin/env python3
"""Finite algebra checks for Liouville BPZ and Virasoro-block conventions."""

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


def add_two_laurent(
    *polynomials: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {
        monomial: coefficient
        for monomial, coefficient in result.items()
        if coefficient != 0
    }


def multiply_two_laurent(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            monomial = (left_x + right_x, left_y + right_y)
            result[monomial] = (
                result.get(monomial, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return {
        monomial: coefficient
        for monomial, coefficient in result.items()
        if coefficient != 0
    }


def require_two_laurent_equal(
    name: str,
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> None:
    diff = add_two_laurent(left, {monomial: -value for monomial, value in right.items()})
    if diff:
        raise AssertionError(f"{name} mismatch: {diff!r}")


one = Laurent.constant(1)
t = Laurent.monomial(1)
t_inverse = Laurent.monomial(-1)


def check_probabilistic_seiberg_thresholds() -> None:
    """Check the normalization map behind the probabilistic Seiberg bounds.

    In the subcritical GMC construction gamma=2b with 0<gamma<2.  The
    first-moment threshold for the singular local mass is alpha_prob<2/gamma,
    while the actual Seiberg threshold is alpha_prob<Q_gamma with
    Q_gamma=2/gamma+gamma/2 = b+b^{-1}.  The latter is the physics condition
    alpha<Q/2 because alpha_prob=2 alpha.
    """

    for b in (Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)):
        gamma = 2 * b
        q_gamma = Fraction(2, 1) / gamma + gamma / 2
        physics_q = b + Fraction(1, 1) / b
        if q_gamma != physics_q:
            raise AssertionError(f"GMC Q normalization mismatch for b={b}")

        first_moment_threshold = Fraction(2, 1) / gamma
        if not first_moment_threshold < q_gamma:
            raise AssertionError("subcritical first-moment threshold should be stricter")

        alpha_prob_between_thresholds = (first_moment_threshold + q_gamma) / 2
        if alpha_prob_between_thresholds < first_moment_threshold:
            raise AssertionError("test alpha should violate the first-moment bound")
        if not alpha_prob_between_thresholds < q_gamma:
            raise AssertionError("test alpha should satisfy the Seiberg bound")

        alpha_physics = alpha_prob_between_thresholds / 2
        if not alpha_physics < physics_q / 2:
            raise AssertionError("physics alpha<Q/2 translation failed")


check_probabilistic_seiberg_thresholds()

# h(-b/2)=(-b/2)(Q+b/2)=-1/2-3 b^2/4.
h = Laurent.constant(Fraction(-1, 2)) + t.scale(Fraction(-3, 4))
dual_h = Laurent.constant(Fraction(-1, 2)) + t_inverse.scale(Fraction(-3, 4))

# c=1+6(b+b^{-1})^2=13+6t+6t^{-1}.
c = Laurent.constant(13) + t.scale(6) + t_inverse.scale(6)

kappa = t
dual_kappa = t_inverse

# Positive-mode action on (L_-1^2 + kappa L_-2)|h>.
l1_coefficient = h.scale(4) + Laurent.constant(2) + kappa.scale(3)
l2_coefficient = h.scale(6) + kappa * (h.scale(4) + c.scale(Fraction(1, 2)))

require_zero("L1 null-vector coefficient", l1_coefficient)
require_zero("L2 null-vector coefficient", l2_coefficient)

# The L1 equation alone fixes kappa=-(4h+2)/3=b^2.
solved_kappa = -(h.scale(4) + Laurent.constant(2)).scale(Fraction(1, 3))
require_zero("solved kappa minus b^2", solved_kappa - t)

# The dual degenerate field V_{-1/(2b)} has the independent null vector
# (L_-1^2 + b^{-2} L_-2)|h^vee>.  This is not a new convention; it is the
# same Virasoro calculation with t=b^2 inverted.
dual_l1_coefficient = (
    dual_h.scale(4) + Laurent.constant(2) + dual_kappa.scale(3)
)
dual_l2_coefficient = (
    dual_h.scale(6)
    + dual_kappa * (dual_h.scale(4) + c.scale(Fraction(1, 2)))
)
require_zero("dual L1 null-vector coefficient", dual_l1_coefficient)
require_zero("dual L2 null-vector coefficient", dual_l2_coefficient)

solved_dual_kappa = -(dual_h.scale(4) + Laurent.constant(2)).scale(
    Fraction(1, 3)
)
require_zero("solved dual kappa minus b^{-2}", solved_dual_kappa - t_inverse)

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

# The dual screening ledger is the independent b -> 1/b version used for the
# V_{-1/(2b)} BPZ shift.  Symbols are u=b^{-2} and ab1=alpha/b.
u_exp = AffineExponent.symbol("u")
ab1 = AffineExponent.symbol("ab1")

require_affine_equal(
    "dual screening OPE power",
    one_exp.scale(2) + u_exp.scale(2) - ab1.scale(2),
    (one_exp + u_exp - ab1).scale(2),
)

dual_screening_a = -ab1.scale(2)
dual_screening_c = u_exp
require_affine_equal(
    "dual screening beta first gamma argument",
    one_exp + dual_screening_a,
    one_exp - ab1.scale(2),
)
require_affine_equal(
    "dual screening beta second gamma argument",
    one_exp + dual_screening_c,
    one_exp + u_exp,
)
require_affine_equal(
    "dual screening beta third gamma argument",
    -one_exp - dual_screening_a - dual_screening_c,
    ab1.scale(2) - one_exp - u_exp,
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

sample_u = 1.0 / sample_t
sample_ab = sample_alpha / sample_b
dual_screening_original = (
    -math.pi
    * gamma_ratio(1.0 - 2.0 * sample_ab)
    * gamma_ratio(1.0 + sample_u)
    * gamma_ratio(2.0 * sample_ab - 1.0 - sample_u)
)
dual_screening_b_power_form = (
    math.pi
    * sample_b ** -4
    * gamma_ratio(sample_u)
    * gamma_ratio(2.0 * sample_ab - 1.0 - sample_u)
    / gamma_ratio(2.0 * sample_ab)
)

scale = max(
    1.0,
    abs(dual_screening_original),
    abs(dual_screening_b_power_form),
)
if abs(dual_screening_original - dual_screening_b_power_form) > 1e-12 * scale:
    raise AssertionError(
        "dual screening b-power form mismatch: "
        f"{dual_screening_original!r} != {dual_screening_b_power_form!r}"
    )

def require_close(name: str, left: float, right: float) -> None:
    scale = max(1.0, abs(left), abs(right))
    if abs(left - right) > 1e-11 * scale:
        raise AssertionError(f"{name} mismatch: {left!r} != {right!r}")


def check_degenerate_connection_shift(
    b: float,
    alpha1: float,
    alpha2: float,
    alpha3: float,
    mu: float,
) -> None:
    """Numerically verify the BPZ connection-matrix shift equation."""

    Q = b + 1.0 / b
    A_value = b * (alpha1 + alpha2 + alpha3 - Q - b / 2.0)
    B_value = b * (alpha1 + alpha2 - alpha3 - b / 2.0)
    C_value = 1.0 + b * (2.0 * alpha1 - Q)
    M_minus_minus = (
        math.gamma(C_value)
        * math.gamma(C_value - A_value - B_value)
        / (math.gamma(C_value - A_value) * math.gamma(C_value - B_value))
    )
    M_minus_plus = (
        math.gamma(C_value)
        * math.gamma(A_value + B_value - C_value)
        / (math.gamma(A_value) * math.gamma(B_value))
    )
    M_plus_minus = (
        math.gamma(2.0 - C_value)
        * math.gamma(C_value - A_value - B_value)
        / (math.gamma(1.0 - A_value) * math.gamma(1.0 - B_value))
    )
    M_plus_plus = (
        math.gamma(2.0 - C_value)
        * math.gamma(A_value + B_value - C_value)
        / (
            math.gamma(A_value - C_value + 1.0)
            * math.gamma(B_value - C_value + 1.0)
        )
    )
    c_minus = (
        math.pi
        * mu
        * b ** 4
        * gamma_ratio(b * b)
        * gamma_ratio(2.0 * b * alpha1 - 1.0 - b * b)
        / gamma_ratio(2.0 * b * alpha1)
    )
    connection_ratio = -(
        M_minus_minus * M_minus_plus
    ) / (c_minus * M_plus_minus * M_plus_plus)
    dozz_shift_ratio = (
        gamma_ratio(2.0 * b * alpha1)
        * gamma_ratio(2.0 * b * alpha1 - b * b)
        * gamma_ratio(b * (alpha2 + alpha3 - alpha1 - b / 2.0))
        / (
            math.pi
            * mu
            * gamma_ratio(b * b)
            * b ** 4
            * gamma_ratio(b * (alpha1 + alpha2 + alpha3 - Q - b / 2.0))
            * gamma_ratio(b * (alpha1 + alpha2 - alpha3 - b / 2.0))
            * gamma_ratio(b * (alpha1 + alpha3 - alpha2 - b / 2.0))
        )
    )
    require_close(
        "BPZ connection-matrix shift equation",
        connection_ratio,
        dozz_shift_ratio,
    )


check_degenerate_connection_shift(0.63, 1.40, 1.25, 1.10, 0.73)
check_degenerate_connection_shift(0.70, 1.60, 1.30, 1.20, 0.73)


def fzzt_one_point(alpha: float, b: float, s: float, mu: float) -> float:
    Q = b + 1.0 / b
    K = math.pi * mu * gamma_ratio(b * b)
    return (
        (2.0 / b)
        * K ** ((Q - 2.0 * alpha) / (2.0 * b))
        * math.gamma(2.0 * b * alpha - b * b)
        * math.gamma(2.0 * alpha / b - 1.0 / (b * b) - 1.0)
        * math.cosh((2.0 * alpha - Q) * math.pi * s)
    )


def check_fzzt_shift_ratios(alpha: float, b: float, s: float, mu: float) -> None:
    Q = b + 1.0 / b
    K = math.pi * mu * gamma_ratio(b * b)

    direct_b = fzzt_one_point(alpha + b / 2.0, b, s, mu) / fzzt_one_point(
        alpha - b / 2.0,
        b,
        s,
        mu,
    )
    expected_b = (
        K ** -1.0
        * math.gamma(2.0 * b * alpha)
        / math.gamma(2.0 * b * alpha - 2.0 * b * b)
        * math.gamma(2.0 * alpha / b - 1.0 / (b * b))
        / math.gamma(2.0 * alpha / b - 1.0 / (b * b) - 2.0)
        * math.cosh(math.pi * s * (2.0 * alpha + b - Q))
        / math.cosh(math.pi * s * (2.0 * alpha - b - Q))
    )
    require_close("FZZT b-shift ratio", direct_b, expected_b)

    direct_dual = fzzt_one_point(
        alpha + 1.0 / (2.0 * b),
        b,
        s,
        mu,
    ) / fzzt_one_point(alpha - 1.0 / (2.0 * b), b, s, mu)
    expected_dual = (
        K ** (-1.0 / (b * b))
        * math.gamma(2.0 * b * alpha + 1.0 - b * b)
        / math.gamma(2.0 * b * alpha - 1.0 - b * b)
        * math.gamma(2.0 * alpha / b - 1.0)
        / math.gamma(2.0 * alpha / b - 2.0 / (b * b) - 1.0)
        * math.cosh(math.pi * s * (2.0 * alpha + 1.0 / b - Q))
        / math.cosh(math.pi * s * (2.0 * alpha - 1.0 / b - Q))
    )
    require_close("FZZT b^{-1}-shift ratio", direct_dual, expected_dual)


check_fzzt_shift_ratios(1.38, 0.63, 0.41, 0.73)
check_fzzt_shift_ratios(1.64, 0.70, 0.29, 0.91)


# Exact Laurent check for the normalized FZZT boundary finite-difference
# mechanism.  Write X=exp(pi s(2 alpha-Q)) and Y=exp(pi s delta), where
# delta is b or b^{-1}.  Then H=(X+X^{-1})/2 and the degenerate shifts send
# X to XY and XY^{-1}.  The identity checked below is
# H(alpha+delta/2)+H(alpha-delta/2)=2 cosh(pi s delta) H(alpha).
half = Fraction(1, 2)
hyperbolic_h = {(1, 0): half, (-1, 0): half}
hyperbolic_plus = {(1, 1): half, (-1, -1): half}
hyperbolic_minus = {(1, -1): half, (-1, 1): half}
two_cosh_delta = {(0, 1): Fraction(1), (0, -1): Fraction(1)}
require_two_laurent_equal(
    "FZZT normalized boundary finite difference",
    add_two_laurent(hyperbolic_plus, hyperbolic_minus),
    multiply_two_laurent(two_cosh_delta, hyperbolic_h),
)

# The finite-difference equations have two exponential branches before the
# Liouville reflection relation selects the even combination.  The same
# Laurent model checks that X and X^{-1} are both eigenfunctions with
# eigenvalue Y+Y^{-1}, while the odd combination is reflection-odd.
exp_plus = {(1, 0): Fraction(1)}
exp_minus = {(-1, 0): Fraction(1)}
require_two_laurent_equal(
    "FZZT positive exponential branch",
    add_two_laurent({(1, 1): Fraction(1)}, {(1, -1): Fraction(1)}),
    multiply_two_laurent(two_cosh_delta, exp_plus),
)
require_two_laurent_equal(
    "FZZT negative exponential branch",
    add_two_laurent({(-1, -1): Fraction(1)}, {(-1, 1): Fraction(1)}),
    multiply_two_laurent(two_cosh_delta, exp_minus),
)

reflection_h = {
    (-x_power, y_power): coeff
    for (x_power, y_power), coeff in hyperbolic_h.items()
}
require_two_laurent_equal("FZZT reflection-even branch", reflection_h, hyperbolic_h)
odd_h = {(1, 0): half, (-1, 0): -half}
reflection_odd = {
    (-x_power, y_power): coeff
    for (x_power, y_power), coeff in odd_h.items()
}
require_two_laurent_equal(
    "FZZT reflection-odd branch",
    reflection_odd,
    {monomial: -coefficient for monomial, coefficient in odd_h.items()},
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


def determinant_3_by_3(matrix: list[list[Fraction]]) -> Fraction:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def solve_3_by_3(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    determinant = determinant_3_by_3(matrix)
    if determinant == 0:
        raise AssertionError("singular 3 by 3 matrix in sample block check")
    solution: list[Fraction] = []
    for column in range(3):
        replaced = [row[:] for row in matrix]
        for row in range(3):
            replaced[row][column] = vector[row]
        solution.append(determinant_3_by_3(replaced) / determinant)
    return solution


a3_block = h_sample + 3 * h3_sample - h4_sample
b3_block = h_sample + 3 * h2_sample - h1_sample
a21_block = a2_block * (a1_block + 2)
b21_block = b2_block * (b1_block + 2)
a111_block = a1_block * (a1_block + 1) * (a1_block + 2)
b111_block = b1_block * (b1_block + 1) * (b1_block + 2)

gram_33 = 6 * h_sample + 2 * c_sample
gram_321 = 10 * h_sample
gram_3111 = 24 * h_sample
gram_2121 = h_sample * (c_sample + 8 * h_sample + 8)
gram_21111 = 12 * h_sample * (3 * h_sample + 1)
gram_111111 = 24 * h_sample * (h_sample + 1) * (2 * h_sample + 1)

level_three_gram = [
    [gram_33, gram_321, gram_3111],
    [gram_321, gram_2121, gram_21111],
    [gram_3111, gram_21111, gram_111111],
]
level_three_det = determinant_3_by_3(level_three_gram)
level_three_det_formula = (
    48
    * h_sample
    * h_sample
    * (16 * h_sample * h_sample + 2 * (c_sample - 5) * h_sample + c_sample)
    * (3 * h_sample * h_sample + (c_sample - 7) * h_sample + c_sample + 2)
)
if level_three_det != level_three_det_formula:
    raise AssertionError(
        "level-three Gram determinant mismatch: "
        f"{level_three_det} != {level_three_det_formula}"
    )

level_three_right = [a3_block, a21_block, a111_block]
level_three_left = [b3_block, b21_block, b111_block]
level_three_solution = solve_3_by_3(level_three_gram, level_three_right)
level_three_from_projector = sum(
    level_three_left[index] * level_three_solution[index]
    for index in range(3)
)
expected_level_three_sample = Fraction(1382428354989, 471923200000)
if level_three_from_projector != expected_level_three_sample:
    raise AssertionError(
        "level-three Virasoro-block coefficient mismatch: "
        f"{level_three_from_projector} != {expected_level_three_sample}"
    )

global_level_three = b111_block * a111_block / (
    24 * h_sample * (h_sample + 1) * (2 * h_sample + 1)
)
expected_global_level_three = Fraction(21274913, 17408000)
if global_level_three != expected_global_level_three:
    raise AssertionError(
        f"level-three global block denominator mismatch: "
        f"{global_level_three} != {expected_global_level_three}"
    )


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
    "All Liouville GMC-threshold, BPZ, dual-BPZ, screening, dual-screening, "
    "Virasoro-block through level three, connection-matrix, FZZT-shift, "
    "FZZT finite-difference, elliptic-q, and DOZZ-shift checks passed."
)
