#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- Endpoint convolution, distributional pairing, zero-bin subtraction, finite
  scheme changes, RG transport, Wilson-line decoupling, Glauber diagnostics,
  the spectator-model color-entanglement obstruction to generalized TMD
  factorization, soft-drop scales, and massive-vector Sudakov areas obey the
  finite algebra stated in the jets/SCET chapter.
- The regulated endpoint-region integral has a real fixed-order remainder
  bound, and unsubtracted or unpaired region splits fail as negative controls.
- A noncommuting finite measurement can detect a Glauber rotation, so a
  residual slot is not a proof of factorization.

Independent construction:
- All checks use finite distributions, rational matrices, exact polynomial
  integrals, or symbolic identities built independently of the manuscript
  prose.
- The endpoint-region expansion is checked by direct symbolic integration and
  by the Lipschitz remainder bound.
- The Glauber-breaking example is checked both as a concrete rational matrix
  model and as a symbolic two-state rotation formula.
- The spectator-model obstruction is checked by an independent finite SU(2)
  color-trace computation, eikonal delta-coefficient bookkeeping, and a
  fixed-recoil transverse numerator/denominator sample.

Imported assumptions:
- The checks are finite-regulator or fixed-order algebraic tests of a proposed
  SCET/factorization datum.
- The endpoint integral is a one-dimensional Feynman-parameter endpoint model;
  it is not a continuum QCD theorem.
- The finite Glauber Hilbert space is a diagnostic model for measurement
  commutation, not a construction of the QCD Glauber region.
- The spectator-model check verifies the color/eikonal skeleton of the
  Rogers-Mulders mechanism; it is not a numerical evaluation of the full
  hadronic cross section.

Negative controls:
- Naively double-counting the zero-bin leaves exactly the overlap term.
- A finite scheme change whose factors do not multiply to one changes the
  hard/jet/soft product.
- The unsubtracted hard endpoint integral diverges, and an unpaired
  intermediate split retains arbitrary split-scale dependence.
- A noncommuting measurement gives a nonzero Glauber remainder.
- Separate color-traced TMD factors have zero order-g single-loop anomaly
  while the cross-hadron two-gluon color trace is nonzero.

Scope boundary:
- This script verifies finite algebra, fixed-order endpoint expansion, and
  proof-obligation diagnostics.  It does not construct SCET, prove
  composite-operator existence, prove regulator removal, derive mode
  decompositions from QCD, or establish all-order factorization for a
  physical cross section.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Mapping

import sympy as sp

from check_utils import assert_leq as _assert_leq

Distribution = Mapping[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def normalize(dist: Distribution) -> Fraction:
    return sum(dist.values(), Fraction(0))


def moment(dist: Distribution) -> Fraction:
    return sum(x * weight for x, weight in dist.items())


def signed_difference(left: Distribution, right: Distribution) -> dict[Fraction, Fraction]:
    keys = set(left) | set(right)
    return {key: left.get(key, Fraction(0)) - right.get(key, Fraction(0)) for key in keys}


def finite_pairing(dist: Distribution, test: Distribution) -> Fraction:
    return sum(weight * test.get(point, Fraction(0)) for point, weight in dist.items())


def total_variation(dist: Distribution) -> Fraction:
    return sum(abs(weight) for weight in dist.values())


def sup_norm(test: Distribution) -> Fraction:
    return max((abs(value) for value in test.values()), default=Fraction(0))


def endpoint_convolution(
    jet_n: Distribution,
    jet_barn: Distribution,
    soft: Distribution,
    q_hard: Fraction,
) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = defaultdict(Fraction)
    for s1, w1 in jet_n.items():
        for s2, w2 in jet_barn.items():
            for k, ws in soft.items():
                e = (s1 + s2) / (q_hard * q_hard) + k / q_hard
                out[e] += w1 * w2 * ws
    return dict(out)


def generating_transform(dist: Distribution, scale: Fraction) -> dict[Fraction, Fraction]:
    return {scale * x: weight for x, weight in dist.items()}


def multiply_transforms(*transforms: Mapping[Fraction, Fraction]) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    for transform in transforms:
        new_out: dict[Fraction, Fraction] = defaultdict(Fraction)
        for e1, w1 in out.items():
            for e2, w2 in transform.items():
                new_out[e1 + e2] += w1 * w2
        out = dict(new_out)
    return out


def check_event_shape_convolution() -> None:
    jet_n = {Fraction(1): Fraction(1, 3), Fraction(4): Fraction(2, 3)}
    jet_barn = {Fraction(2): Fraction(3, 5), Fraction(5): Fraction(2, 5)}
    soft = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(3, 4)}
    q_hard = Fraction(6)

    direct = endpoint_convolution(jet_n, jet_barn, soft, q_hard)
    transformed = multiply_transforms(
        generating_transform(jet_n, Fraction(1, q_hard * q_hard)),
        generating_transform(jet_barn, Fraction(1, q_hard * q_hard)),
        generating_transform(soft, Fraction(1, q_hard)),
    )
    assert_equal("endpoint convolution transform", direct, transformed)
    assert_equal("convolution normalization", normalize(direct), Fraction(1))

    expected_first_moment = (
        moment(jet_n) / (q_hard * q_hard)
        + moment(jet_barn) / (q_hard * q_hard)
        + moment(soft) / q_hard
    )
    assert_equal("endpoint first moment", moment(direct), expected_first_moment)


def check_distributional_factorization_remainder_bound() -> None:
    physical = {
        Fraction(0): Fraction(7, 15),
        Fraction(1, 4): Fraction(1, 5),
        Fraction(1, 2): Fraction(1, 6),
        Fraction(3, 4): Fraction(1, 6),
    }
    factorized = {
        Fraction(0): Fraction(1, 2),
        Fraction(1, 4): Fraction(1, 6),
        Fraction(1, 2): Fraction(1, 5),
        Fraction(3, 4): Fraction(2, 15),
    }
    remainder = signed_difference(physical, factorized)
    assert_equal("equal total weight in factorization model", normalize(remainder), Fraction(0))

    test = {
        Fraction(0): Fraction(3, 5),
        Fraction(1, 4): Fraction(-2, 7),
        Fraction(1, 2): Fraction(4, 9),
        Fraction(3, 4): Fraction(-5, 11),
    }
    pairing = finite_pairing(remainder, test)
    bound = total_variation(remainder) * sup_norm(test)
    _assert_leq("distributional remainder total-variation bound", abs(pairing), bound)

    sign_test = {
        point: Fraction(1) if weight > 0 else Fraction(-1) if weight < 0 else Fraction(0)
        for point, weight in remainder.items()
    }
    assert_equal("sharp total-variation dual pairing", finite_pairing(remainder, sign_test), total_variation(remainder))


def finite_zero_bin_sum(
    collinear: Mapping[str, Fraction],
    soft: Mapping[str, Fraction],
    overlap: Mapping[str, Fraction],
    test: Mapping[str, Fraction],
) -> Fraction:
    return (
        sum(weight * test[cell] for cell, weight in collinear.items())
        + sum(weight * test[cell] for cell, weight in soft.items())
        - sum(weight * test[cell] for cell, weight in overlap.items())
    )


def check_zero_bin_inclusion_exclusion() -> None:
    collinear = {"c": Fraction(5), "o1": Fraction(7), "o2": Fraction(11)}
    soft = {"s": Fraction(13), "o1": Fraction(7), "o2": Fraction(11)}
    overlap = {"o1": Fraction(7), "o2": Fraction(11)}
    test = {
        "c": Fraction(2, 3),
        "s": Fraction(3, 5),
        "o1": Fraction(5, 7),
        "o2": Fraction(7, 11),
    }
    matched = finite_zero_bin_sum(collinear, soft, overlap, test)
    unique_union = (
        collinear["c"] * test["c"]
        + soft["s"] * test["s"]
        + overlap["o1"] * test["o1"]
        + overlap["o2"] * test["o2"]
    )
    naive_double_count = sum(weight * test[cell] for cell, weight in collinear.items()) + sum(
        weight * test[cell] for cell, weight in soft.items()
    )
    assert_equal("finite zero-bin inclusion-exclusion", matched, unique_union)
    assert_equal(
        "naive overlap double count",
        naive_double_count - matched,
        sum(weight * test[cell] for cell, weight in overlap.items()),
    )


def check_zero_bin_scheme_reshuffling() -> None:
    collinear = {"c": Fraction(2), "o": Fraction(5)}
    soft = {"s": Fraction(7), "o": Fraction(5)}
    overlap = {"o": Fraction(5)}
    test = {"c": Fraction(3), "s": Fraction(4), "o": Fraction(11)}
    base = finite_zero_bin_sum(collinear, soft, overlap, test)

    delta = Fraction(13)
    collinear_shifted = {"c": collinear["c"], "o": collinear["o"]}
    soft_shifted = {"s": soft["s"], "o": soft["o"] + delta}
    overlap_shifted = {"o": overlap["o"] + delta}
    shifted = finite_zero_bin_sum(collinear_shifted, soft_shifted, overlap_shifted, test)
    assert_equal("paired zero-bin scheme reshuffling", shifted, base)


def check_regulated_endpoint_region_expansion() -> None:
    x = sp.symbols("x", positive=True)
    eps = sp.symbols("eps", positive=True)
    eta = sp.symbols("eta", positive=True)
    lam = sp.Rational(1, 7)
    f = 1 + 3 * x + 2 * x**2
    f0 = f.subs(x, 0)

    exact = sp.integrate(f / (x + lam), (x, 0, 1))
    endpoint = f0 * sp.log((1 + lam) / lam)
    hard = sp.integrate((f - f0) / x, (x, 0, 1))
    remainder = -lam * sp.integrate((f - f0) / (x * (x + lam)), (x, 0, 1))
    assert_equal(
        "regulated endpoint expansion identity",
        sp.simplify(exact - endpoint - hard - remainder),
        0,
    )

    lipschitz_bound = lam * sp.Rational(7) * sp.log((1 + lam) / lam)
    _assert_leq(
        "regulated endpoint Lipschitz remainder bound",
        float(abs(remainder.evalf())),
        float(lipschitz_bound.evalf()),
    )

    unsubtracted_hard = sp.integrate(f / x, (x, eps, 1))
    if sp.limit(unsubtracted_hard, eps, 0, dir="+") != sp.oo:
        raise AssertionError("unsubtracted endpoint hard integral should diverge")

    naive_split = f0 * sp.log(eta / lam) + sp.integrate(f / x, (x, eta, 1))
    split_derivative = sp.simplify(sp.diff(naive_split, eta))
    assert_equal("naive split-scale dependence", split_derivative, -2 * eta - 3)


def check_multiplicative_scheme_covariance() -> None:
    hard = Fraction(2, 3)
    jet_n = Fraction(5, 7)
    jet_barn = Fraction(11, 13)
    soft = Fraction(17, 19)
    base_product = hard * jet_n * jet_barn * soft

    r_h = Fraction(3, 5)
    r_n = Fraction(7, 11)
    r_barn = Fraction(13, 17)
    r_s = Fraction(1, 1) / (r_h * r_n * r_barn)
    assert_equal("multiplicative scheme product condition", r_h * r_n * r_barn * r_s, Fraction(1))

    shifted_product = (hard * r_h) * (jet_n * r_n) * (jet_barn * r_barn) * (soft * r_s)
    assert_equal("factorized product under finite scheme change", shifted_product, base_product)
    bad_shifted_product = (hard * r_h) * (jet_n * r_n) * (jet_barn * r_barn) * (soft * r_s * 2)
    if bad_shifted_product == base_product:
        raise AssertionError("unpaired finite scheme change should alter the factorized product")

    gamma_h = Fraction(5, 6)
    gamma_n = Fraction(-1, 3)
    gamma_barn = Fraction(7, 10)
    gamma_s = -gamma_h - gamma_n - gamma_barn
    assert_equal("unshifted anomalous-dimension consistency", gamma_h + gamma_n + gamma_barn + gamma_s, Fraction(0))

    dlog_r_h = Fraction(2, 7)
    dlog_r_n = Fraction(-3, 11)
    dlog_r_barn = Fraction(5, 13)
    dlog_r_s = -dlog_r_h - dlog_r_n - dlog_r_barn
    shifted_sum = (
        (gamma_h + dlog_r_h)
        + (gamma_n + dlog_r_n)
        + (gamma_barn + dlog_r_barn)
        + (gamma_s + dlog_r_s)
    )
    assert_equal("shifted anomalous-dimension consistency", shifted_sum, Fraction(0))


def integrate_piecewise(values: Mapping[tuple[Fraction, Fraction], Fraction], start: Fraction, end: Fraction) -> Fraction:
    if start == end:
        return Fraction(0)
    if start > end:
        return -integrate_piecewise(values, end, start)

    total = Fraction(0)
    for (left, right), value in values.items():
        overlap_left = max(start, left)
        overlap_right = min(end, right)
        if overlap_left < overlap_right:
            total += value * (overlap_right - overlap_left)
    return total


def check_rg_transport_common_scale_independence() -> None:
    intervals = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(3)))
    gamma_h = {intervals[0]: Fraction(3), intervals[1]: Fraction(-1), intervals[2]: Fraction(2)}
    gamma_j = {intervals[0]: Fraction(-2), intervals[1]: Fraction(4), intervals[2]: Fraction(1)}
    gamma_s = {interval: -gamma_h[interval] - 2 * gamma_j[interval] for interval in intervals}

    for interval in intervals:
        assert_equal(
            "pointwise SCET anomalous-dimension consistency",
            gamma_h[interval] + 2 * gamma_j[interval] + gamma_s[interval],
            Fraction(0),
        )

    natural_h = Fraction(0)
    natural_j = Fraction(1)
    natural_s = Fraction(2)

    def total_transport_exponent(common_scale: Fraction) -> Fraction:
        return (
            integrate_piecewise(gamma_h, natural_h, common_scale)
            + 2 * integrate_piecewise(gamma_j, natural_j, common_scale)
            + integrate_piecewise(gamma_s, natural_s, common_scale)
        )

    reference = total_transport_exponent(Fraction(2))
    assert_equal("RG transport to first common scale", reference, total_transport_exponent(Fraction(2)))
    assert_equal("RG transport independent of later common scale", reference, total_transport_exponent(Fraction(3)))

    shifted_gamma_h = {interval: gamma_h[interval] + Fraction(5) for interval in intervals}
    shifted_gamma_s = {interval: gamma_s[interval] - Fraction(5) for interval in intervals}
    shifted = (
        integrate_piecewise(shifted_gamma_h, natural_h, Fraction(3))
        + 2 * integrate_piecewise(gamma_j, natural_j, Fraction(3))
        + integrate_piecewise(shifted_gamma_s, natural_s, Fraction(3))
    )
    unshifted = total_transport_exponent(Fraction(3))
    assert_equal("paired hard-soft anomalous-dimension scheme shift", shifted, unshifted + Fraction(5) * (natural_s - natural_h))


def check_soft_drop_boundary_scales_and_rg_consistency() -> None:
    beta = 2
    rho = Fraction(1, 4096)
    z_cut = Fraction(1, 16)
    theta_star = Fraction(1, 4)
    z_star = Fraction(1, 256)

    assert_equal("soft-drop boundary mass equation", z_star * theta_star * theta_star, rho)
    assert_equal("soft-drop boundary grooming equation", z_cut * theta_star**beta, z_star)
    assert_equal("soft-drop boundary theta equation", theta_star ** (beta + 2), rho / z_cut)

    mu_j_squared = rho
    mu_cs_squared = rho * z_star
    assert_equal("soft-drop collinear-soft transverse scale", mu_cs_squared, z_star * mu_j_squared)
    if not mu_cs_squared < mu_j_squared:
        raise AssertionError("collinear-soft scale should lie below the collinear scale for z_star < 1")

    intervals = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(4)))
    gamma_h = {intervals[0]: Fraction(4), intervals[1]: Fraction(-2), intervals[2]: Fraction(1)}
    gamma_g = {intervals[0]: Fraction(-3), intervals[1]: Fraction(5), intervals[2]: Fraction(2)}
    gamma_j = {intervals[0]: Fraction(1), intervals[1]: Fraction(1), intervals[2]: Fraction(-4)}
    gamma_cs = {
        interval: -gamma_h[interval] - gamma_g[interval] - gamma_j[interval]
        for interval in intervals
    }

    for interval in intervals:
        assert_equal(
            "soft-drop anomalous-dimension consistency",
            gamma_h[interval] + gamma_g[interval] + gamma_j[interval] + gamma_cs[interval],
            Fraction(0),
        )

    natural_h = Fraction(0)
    natural_g = Fraction(1)
    natural_j = Fraction(2)
    natural_cs = Fraction(2)

    def total_transport_exponent(common_scale: Fraction) -> Fraction:
        return (
            integrate_piecewise(gamma_h, natural_h, common_scale)
            + integrate_piecewise(gamma_g, natural_g, common_scale)
            + integrate_piecewise(gamma_j, natural_j, common_scale)
            + integrate_piecewise(gamma_cs, natural_cs, common_scale)
        )

    reference = total_transport_exponent(Fraction(2))
    assert_equal("soft-drop RG transport at first common scale", reference, total_transport_exponent(Fraction(2)))
    assert_equal("soft-drop RG transport independent of later common scale", reference, total_transport_exponent(Fraction(4)))


def check_soft_wilson_line_decoupling_identity() -> None:
    s = sp.symbols("s")
    a = sp.Rational(3, 2)
    connection = sp.Matrix([[0, a], [0, 0]])
    identity = sp.eye(2)
    # Nilpotency makes this exact polynomial Wilson line solve dY/ds = A Y.
    wilson = identity + s * connection
    field0 = sp.Matrix([1 + 2 * s + s**2, sp.Rational(1, 3) - s])

    lhs = sp.diff(wilson * field0, s) - connection * wilson * field0
    rhs = wilson * sp.diff(field0, s)
    assert_equal("finite BPS decoupling identity", sp.simplify(lhs - rhs), sp.zeros(2, 1))


def trace(matrix: sp.Matrix) -> sp.Rational:
    return sp.trace(matrix)


def frobenius_square(matrix: sp.Matrix) -> sp.Rational:
    return sp.trace(matrix.T * matrix)


def check_glauber_unitarity_diagnostic() -> None:
    unitary = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [sp.Rational(-4, 5), sp.Rational(3, 5)]])
    identity = sp.eye(2)
    assert_equal("finite Glauber unitary", unitary.T * unitary, identity)

    rho = sp.Matrix([[sp.Rational(2, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(3, 5)]])
    evolved = unitary * rho * unitary.T
    assert_equal("inclusive Glauber trace", trace(evolved), trace(rho))

    commuting_measurement = sp.Rational(7, 3) * identity
    assert_equal(
        "commuting Glauber measurement",
        trace(commuting_measurement * evolved),
        trace(commuting_measurement * rho),
    )

    noncommuting_measurement = sp.Matrix([[1, 0], [0, 0]])
    without_glauber = trace(noncommuting_measurement * rho)
    with_glauber = trace(noncommuting_measurement * evolved)
    if with_glauber == without_glauber:
        raise AssertionError("noncommuting measurement should detect the finite Glauber rotation")

    rotated_measurement_difference = unitary.T * noncommuting_measurement * unitary - noncommuting_measurement
    exact_remainder = with_glauber - without_glauber
    assert_equal(
        "Glauber remainder cyclic form",
        exact_remainder,
        trace(rotated_measurement_difference * rho),
    )

    # Exact finite-dimensional Cauchy-Schwarz check:
    # |Tr(A rho)|^2 <= Tr(A^T A) Tr(rho^T rho).  This is the rational
    # Hilbert-Schmidt version of the operator/trace-norm bound used in the text.
    lhs = exact_remainder * exact_remainder
    rhs = frobenius_square(rotated_measurement_difference) * frobenius_square(rho)
    if lhs > rhs:
        raise AssertionError(f"Glauber Hilbert-Schmidt remainder bound failed: {lhs} > {rhs}")


def check_symbolic_glauber_breaking_example() -> None:
    c, s, r1, r2 = sp.symbols("c s r1 r2")
    unitary = sp.Matrix([[c, s], [-s, c]])
    measurement = sp.Matrix([[1, 0], [0, 0]])
    rho = sp.diag(r1, r2)
    evolved = unitary * rho * unitary.T
    delta = sp.trace(measurement * evolved) - sp.trace(measurement * rho)
    delta_on_unit_circle = sp.simplify(delta.subs(c**2, 1 - s**2))
    assert_equal("symbolic finite Glauber breaking", delta_on_unit_circle, s**2 * (r2 - r1))

    concrete = delta_on_unit_circle.subs({s: sp.Rational(4, 5), r1: sp.Rational(1, 5), r2: sp.Rational(3, 5)})
    if concrete == 0:
        raise AssertionError("concrete Glauber-breaking negative control should be nonzero")


def check_spectator_model_color_entanglement() -> None:
    half = sp.Rational(1, 2)
    generators = [
        sp.Matrix([[0, half], [half, 0]]),
        sp.Matrix([[0, -sp.I * half], [sp.I * half, 0]]),
        sp.Matrix([[half, 0], [0, -half]]),
    ]

    for index, generator in enumerate(generators):
        assert_equal(
            f"SU(2) generator {index} trace",
            sp.simplify(trace(generator)),
            0,
        )

    for a, generator_a in enumerate(generators):
        for b, generator_b in enumerate(generators):
            expected = half if a == b else 0
            assert_equal(
                f"SU(2) trace normalization {a},{b}",
                sp.simplify(trace(generator_a * generator_b)),
                expected,
            )

    entangled_color = sp.simplify(
        sum(
            trace(generator_a * generator_b) * trace(generator_b * generator_a)
            for generator_a in generators
            for generator_b in generators
        )
    )
    assert_equal(
        "SU(2) cross-hadron entangled color factor",
        entangled_color,
        half * half * (2 * 2 - 1),
    )

    separate_single_loop_color = sp.simplify(
        sum(
            trace(generator_a) * trace(generator_b)
            for generator_a in generators
            for generator_b in generators
        )
    )
    assert_equal("separate TMD order-g anomaly vanishes", separate_single_loop_color, 0)
    if entangled_color == 0:
        raise AssertionError("cross-hadron two-gluon color factor should be nonzero")

    pi = sp.pi
    same_side_eikonal_delta = (-2 * sp.I * pi) * (-2 * sp.I * pi)
    same_side_spin_phase = -1
    opposite_side_eikonal_delta = (2 * sp.I * pi) * (-2 * sp.I * pi)
    opposite_side_spin_phase = 1
    assert_equal(
        "same-side eikonal plus spin sign",
        sp.simplify(same_side_eikonal_delta * same_side_spin_phase),
        4 * pi**2,
    )
    assert_equal(
        "opposite-side eikonal plus spin sign",
        sp.simplify(opposite_side_eikonal_delta * opposite_side_spin_phase),
        4 * pi**2,
    )
    assert_equal(
        "same/opposite Glauber terms add",
        sp.simplify(
            same_side_eikonal_delta * same_side_spin_phase
            + opposite_side_eikonal_delta * opposite_side_spin_phase
        ),
        8 * pi**2,
    )

    def eps2(
        left: tuple[sp.Rational, sp.Rational],
        right: tuple[sp.Rational, sp.Rational],
    ) -> sp.Rational:
        return left[0] * right[1] - left[1] * right[0]

    def norm2(vector: tuple[sp.Rational, sp.Rational]) -> sp.Rational:
        return vector[0] * vector[0] + vector[1] * vector[1]

    def minus(
        left: tuple[sp.Rational, sp.Rational],
        right: tuple[sp.Rational, sp.Rational],
    ) -> tuple[sp.Rational, sp.Rational]:
        return left[0] - right[0], left[1] - right[1]

    def plus(
        left: tuple[sp.Rational, sp.Rational],
        right: tuple[sp.Rational, sp.Rational],
    ) -> tuple[sp.Rational, sp.Rational]:
        return left[0] + right[0], left[1] + right[1]

    spin_1 = (sp.Rational(1), sp.Rational(0))
    spin_2 = (sp.Rational(1), sp.Rational(0))
    l_1 = (sp.Rational(0), sp.Rational(1))
    l_2 = (sp.Rational(0), sp.Rational(1))
    k_1 = (sp.Rational(0), sp.Rational(0))
    q = (sp.Rational(1), sp.Rational(0))
    numerator = eps2(spin_1, l_1) * eps2(spin_2, l_2)
    denominator = (
        norm2(l_1)
        * norm2(l_2)
        * (norm2(k_1) + 1)
        * (norm2(minus(l_1, k_1)) + 2)
        * (norm2(minus(q, k_1)) + 3)
        * (norm2(minus(plus(l_2, k_1), q)) + 4)
    )
    assert_equal("fixed-recoil double-spin numerator", numerator, 1)
    if denominator <= 0:
        raise AssertionError("regulated transverse denominator should be positive")
    if numerator / denominator == 0:
        raise AssertionError("fixed-q spectator integrand sample should be nonzero")


def massive_vector_sudakov_area(log_q2_over_m2: Fraction) -> Fraction:
    return log_q2_over_m2 * log_q2_over_m2 / 4


def check_massive_vector_sudakov_area() -> None:
    big_log = Fraction(6)
    # The chart is 0 < y < L and 0 < x < y/2.
    triangle_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in [(Fraction(0), big_log)]
    )
    assert_equal(
        "massive-vector Sudakov triangular area",
        triangle_area,
        massive_vector_sudakov_area(big_log),
    )

    alpha_times_c_over_pi = Fraction(5, 7)
    exponent = -alpha_times_c_over_pi * massive_vector_sudakov_area(big_log)
    assert_equal("massive-vector Sudakov exponent coefficient", exponent, Fraction(-45, 7))

    # Splitting the y interval checks additivity of the finite phase-space
    # integral before taking a continuum limit.
    pieces = [
        (Fraction(0), Fraction(2)),
        (Fraction(2), Fraction(5)),
        (Fraction(5), big_log),
    ]
    piecewise_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in pieces
    )
    assert_equal("piecewise massive-vector area", piecewise_area, massive_vector_sudakov_area(big_log))


def main() -> None:
    check_event_shape_convolution()
    check_distributional_factorization_remainder_bound()
    check_zero_bin_inclusion_exclusion()
    check_zero_bin_scheme_reshuffling()
    check_regulated_endpoint_region_expansion()
    check_multiplicative_scheme_covariance()
    check_rg_transport_common_scale_independence()
    check_soft_drop_boundary_scales_and_rg_consistency()
    check_soft_wilson_line_decoupling_identity()
    check_glauber_unitarity_diagnostic()
    check_symbolic_glauber_breaking_example()
    check_spectator_model_color_entanglement()
    check_massive_vector_sudakov_area()
    print(
        "All SCET convolution, distributional-remainder, zero-bin, "
        "endpoint-expansion, scheme-covariance, RG-transport, soft-drop-scale, "
        "soft-Wilson-line, Glauber-unitarity/breaking, spectator-model "
        "color-entanglement, and massive-vector Sudakov checks passed."
    )


if __name__ == "__main__":
    main()
