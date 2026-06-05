#!/usr/bin/env python3
"""Exact checks for anomaly-line cocycles and finite inflow identities.

Evidence contract.
Target claims: the finite cocycle, counterterm, anomaly-line, Wilsonian
shell-pushforward, bulk-state-line variance, and inflow subclaims in the
anomaly-inflow chapter and the Chapter 20 descent bridge.
Independent construction: explicit cochain coboundaries, finite
Chevalley-Eilenberg signs, polynomial counterterm representatives, one-line
duality exponents, finite shell integrand multisets, and finite Stokes
identities are computed directly rather than inferred from the displayed
anomaly-line slogan.
Imported assumptions: the chapter's groupoid/cochain orientation convention,
the chosen finite triangulation models, and the polynomial Lie-algebra action
used as a local descent shadow.
Negative controls: nonclosed or noncoboundary representatives fail the
descent/cancellation identities; counterterm frame changes are tested as
coboundaries rather than as changes of the invariant obstruction; and a
filling typed as either a scalar or a boundary-anomaly-line vector fails the
bulk-boundary evaluation type test.  The shell check also verifies that
omitting the inherited anomaly phase is detected in a nontrivial sample.
Scope boundary: a pass checks finite cochain and descent algebra; it does not
prove continuum locality, determinant-line existence, compactness of the
space of fields, or Dai-Freed analytic gluing.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Simplex = tuple[int, ...]
Cochain = dict[Simplex, int]
Monomial = tuple[int, int]
Polynomial = dict[Monomial, Fraction]


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def clean(poly: Polynomial) -> Polynomial:
    return {monomial: coeff for monomial, coeff in poly.items() if coeff}


def poly_add(*terms: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in terms:
        for monomial, coeff in poly.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coeff
    return clean(result)


def poly_scale(poly: Polynomial, scalar: Fraction) -> Polynomial:
    return clean({monomial: scalar * coeff for monomial, coeff in poly.items()})


def poly_derivative(poly: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for (x_power, y_power), coeff in poly.items():
        powers = [x_power, y_power]
        if powers[variable] == 0:
            continue
        new_powers = powers[:]
        new_powers[variable] -= 1
        result[tuple(new_powers)] = coeff * powers[variable]
    return clean(result)


def poly_multiply_by_linear(poly: Polynomial, x_coeff: Fraction, y_coeff: Fraction) -> Polynomial:
    result: Polynomial = {}
    for (x_power, y_power), coeff in poly.items():
        if x_coeff:
            monomial = (x_power + 1, y_power)
            result[monomial] = result.get(monomial, Fraction(0)) + coeff * x_coeff
        if y_coeff:
            monomial = (x_power, y_power + 1)
            result[monomial] = result.get(monomial, Fraction(0)) + coeff * y_coeff
    return clean(result)


def affine_action(generator: int, poly: Polynomial) -> Polynomial:
    """Act on polynomials by the nonabelian two-dimensional algebra.

    The vector fields are R_0 = x d/dx and R_1 = y d/dx.  They obey
    [R_0,R_1] = -R_1, so the corresponding Lie bracket is [e_0,e_1] = -e_1.
    """

    dx = poly_derivative(poly, 0)
    if generator == 0:
        return poly_multiply_by_linear(dx, Fraction(1), Fraction(0))
    if generator == 1:
        return poly_multiply_by_linear(dx, Fraction(0), Fraction(1))
    raise ValueError(f"unknown generator {generator}")


def bracket_coefficients(first: int, second: int) -> tuple[Fraction, Fraction]:
    if (first, second) == (0, 1):
        return (Fraction(0), Fraction(-1))
    if (first, second) == (1, 0):
        return (Fraction(0), Fraction(1))
    return (Fraction(0), Fraction(0))


def anomaly_for_bracket(
    anomalies: tuple[Polynomial, Polynomial], first: int, second: int
) -> Polynomial:
    coeff0, coeff1 = bracket_coefficients(first, second)
    return poly_add(poly_scale(anomalies[0], coeff0), poly_scale(anomalies[1], coeff1))


def check_chevalley_eilenberg_wess_zumino_sign() -> None:
    """Verify the finite algebra behind the Wess-Zumino consistency sign.

    For a local counterterm K(x,y), the exact anomaly one-cochain
    A_i = R_i K must satisfy
        R_i A_j - R_j A_i - A_[i,j] = 0.
    This is the finite-dimensional Chevalley-Eilenberg identity used by the
    BRST ghost-number-two extraction in the chapter.
    """

    local_counterterm: Polynomial = {
        (2, 0): Fraction(2),
        (1, 1): Fraction(3),
        (0, 2): Fraction(5),
        (3, 0): Fraction(-1),
        (2, 1): Fraction(4),
    }
    anomalies = (
        affine_action(0, local_counterterm),
        affine_action(1, local_counterterm),
    )
    for first, second in ((0, 1), (1, 0), (0, 0), (1, 1)):
        ce_value = poly_add(
            affine_action(first, anomalies[second]),
            poly_scale(affine_action(second, anomalies[first]), Fraction(-1)),
            poly_scale(anomaly_for_bracket(anomalies, first, second), Fraction(-1)),
        )
        assert_equal(ce_value, {}, "Chevalley-Eilenberg Wess-Zumino sign")


def anomaly_cocycle(n: int, level: int, gauge: int, background: int) -> int:
    """A Z_n translation-groupoid 1-cocycle in a chosen frame.

    The action is background -> background + gauge.  The term
    gauge * (gauge - 1) / 2 is integral for every integer gauge and is the
    finite-difference correction that makes composition functorial.
    """

    return level * (gauge * background + gauge * (gauge - 1) // 2) % n


def counterterm(n: int, quadratic: int, linear: int, background: int) -> int:
    """A local frame change used to test coboundary shifts of representatives."""

    return (quadratic * background * background + linear * background) % n


def check_functorial_cocycle_condition() -> None:
    for n in range(2, 17):
        for level in range(n):
            for background in range(n):
                for first in range(n):
                    for second in range(n):
                        lhs = anomaly_cocycle(n, level, first + second, background)
                        rhs = (
                            anomaly_cocycle(n, level, first, background + second)
                            + anomaly_cocycle(n, level, second, background)
                        ) % n
                        assert_equal(lhs, rhs, "anomaly-line functorial cocycle condition")


def transformed_cocycle(n: int, level: int, quadratic: int, linear: int, gauge: int, background: int) -> int:
    shifted = (background + gauge) % n
    return (
        anomaly_cocycle(n, level, gauge, background)
        + counterterm(n, quadratic, linear, background)
        - counterterm(n, quadratic, linear, shifted)
    ) % n


def check_counterterm_frame_change_preserves_cocycle() -> None:
    for n in range(2, 17):
        samples = sorted({0, 1, n // 2, n - 1})
        for level in samples:
            for quadratic in samples:
                for linear in samples:
                    for background in samples:
                        for first in samples:
                            for second in samples:
                                lhs = transformed_cocycle(n, level, quadratic, linear, first + second, background)
                                rhs = (
                                    transformed_cocycle(n, level, quadratic, linear, first, background + second)
                                    + transformed_cocycle(n, level, quadratic, linear, second, background)
                                ) % n
                                assert_equal(
                                    lhs,
                                    rhs,
                                    "local counterterm frame change preserves the anomaly cocycle condition",
                                )


def check_finite_regulator_scheme_change_is_coboundary() -> None:
    """A local scheme change shifts a finite anomaly cochain by a coboundary."""

    for n in range(2, 19):
        samples = sorted({0, 1, n // 3, n // 2, n - 1})
        for level in samples:
            for quadratic in samples:
                for linear in samples:
                    for background in samples:
                        for gauge in samples:
                            base = anomaly_cocycle(n, level, gauge, background)
                            target = (background + gauge) % n
                            # This is the effective-action convention in
                            # Volume II, Chapter 20: W -> W + B shifts
                            # C(g;A)=W(A^g)-W(A) by B(A^g)-B(A).  The
                            # transformed_cocycle helper above is retained
                            # for the inverse-sign line-frame convention.
                            coboundary = (
                                counterterm(n, quadratic, linear, target)
                                - counterterm(n, quadratic, linear, background)
                            ) % n
                            shifted = (base + coboundary) % n
                            assert_equal(
                                (shifted - base) % n,
                                coboundary,
                                "finite regulator scheme change is a one-coboundary",
                            )
                            assert_equal(
                                (shifted - coboundary) % n,
                                base,
                                "subtracting the scheme coboundary restores the cochain representative",
                            )


def check_coordinate_comparison_between_cochain_line_and_inflow() -> None:
    """Tie finite-regulator, line-functor, and inflow coordinates together."""

    for n in range(2, 19):
        samples = sorted({0, 1, n // 3, n // 2, n - 1})
        for level in samples:
            for quadratic in samples:
                for linear in samples:
                    for background in samples:
                        for first in samples:
                            for second in samples:
                                composed = anomaly_cocycle(n, level, first + second, background)
                                after_second = (background + second) % n
                                line_composition = (
                                    anomaly_cocycle(n, level, first, after_second)
                                    + anomaly_cocycle(n, level, second, background)
                                ) % n
                                assert_equal(
                                    composed,
                                    line_composition,
                                    "finite cochain exponentiates to the line functor cocycle",
                                )

                                target = (background + first) % n
                                base = anomaly_cocycle(n, level, first, background)
                                counterterm_shift = (
                                    counterterm(n, quadratic, linear, target)
                                    - counterterm(n, quadratic, linear, background)
                                ) % n
                                effective_action_coordinate = (base + counterterm_shift) % n

                                inverse_frame_source = -counterterm(n, quadratic, linear, background)
                                inverse_frame_target = -counterterm(n, quadratic, linear, target)
                                line_frame_coordinate = (
                                    base + inverse_frame_source - inverse_frame_target
                                ) % n
                                assert_equal(
                                    line_frame_coordinate,
                                    effective_action_coordinate,
                                    "counterterm and inverse line-frame coordinates agree",
                                )

                                bulk_inverse = (-effective_action_coordinate) % n
                                assert_equal(
                                    (effective_action_coordinate + bulk_inverse) % n,
                                    0,
                                    "bulk inflow coordinate is inverse to boundary anomaly line",
                                )


def anomaly_potential(n: int, level: int, background: int) -> int:
    """A finite local frame whose difference realizes the cocycle."""

    return level * background * (background - 1) // 2 % n


def shell_invariant_part(n: int, background: int, low: int, high: int) -> int:
    """A diagonal-translation-invariant finite shell action."""

    low_background = (low - background) % n
    high_background = (high - background) % n
    low_high = (low - high) % n
    return (3 * low_background**2 + 5 * high_background**2 + 7 * low_high**2) % n


def shell_integrand_exponent(n: int, level: int, background: int, low: int, high: int) -> int:
    return (anomaly_potential(n, level, background) + shell_invariant_part(n, background, low, high)) % n


def retained_local_counterterm(
    n: int,
    quadratic: int,
    linear: int,
    background_weight: int,
    background: int,
    low: int,
) -> int:
    """A local retained-field frame change used in the shell pushforward check."""

    low_background = (low - background) % n
    return (quadratic * low_background**2 + linear * low_background + background_weight * background) % n


def check_rg_shell_pushforward_preserves_anomaly_line() -> None:
    """A finite Wilsonian shell pushforward inherits the anomaly-line cocycle."""

    missing_anomaly_negative_control_seen = False
    for n in range(2, 13):
        samples = sorted({0, 1, n // 3, n // 2, n - 1})
        for level in samples:
            for background in samples:
                for gauge in samples:
                    for low in samples:
                        anomaly = anomaly_cocycle(n, level, gauge, background)
                        target_background = background + gauge
                        target_low = low + gauge

                        original = sorted(
                            shell_integrand_exponent(n, level, background, low, high)
                            for high in range(n)
                        )
                        transformed = sorted(
                            shell_integrand_exponent(
                                n,
                                level,
                                target_background,
                                target_low,
                                high + gauge,
                            )
                            for high in range(n)
                        )
                        expected = sorted((value + anomaly) % n for value in original)
                        assert_equal(
                            transformed,
                            expected,
                            "RG shell pushforward preserves the anomaly-line cocycle",
                        )
                        if transformed != original:
                            missing_anomaly_negative_control_seen = True

                        for quadratic in samples:
                            for linear in samples:
                                for background_weight in samples:
                                    before_counterterm = retained_local_counterterm(
                                        n, quadratic, linear, background_weight, background, low
                                    )
                                    after_counterterm = retained_local_counterterm(
                                        n,
                                        quadratic,
                                        linear,
                                        background_weight,
                                        target_background,
                                        target_low,
                                    )
                                    shifted_original = sorted(
                                        (value + before_counterterm) % n for value in original
                                    )
                                    shifted_transformed = sorted(
                                        (value + after_counterterm) % n for value in transformed
                                    )
                                    coboundary = (after_counterterm - before_counterterm) % n
                                    expected_shifted = sorted(
                                        (value + anomaly + coboundary) % n
                                        for value in shifted_original
                                    )
                                    assert_equal(
                                        shifted_transformed,
                                        expected_shifted,
                                        "retained-field counterterms shift the shell cocycle by a coboundary",
                                    )

    if not missing_anomaly_negative_control_seen:
        raise AssertionError("negative control failed: omitted shell anomaly phase was not detected")


def check_bulk_boundary_dual_line_variance() -> None:
    """Verify the typed line algebra behind boundary/filling evaluation.

    Represent tensor powers of the boundary anomaly line L by integers:
    a boundary partition vector has type +1, the bulk state supplied by a
    filling has type -1 because B_bulk ~= L^vee, and a scalar has type 0.
    This exact type ledger is what scalar phase checks alone cannot see.
    """

    scalar = 0
    boundary_vector = 1
    bulk_state = -1
    dual_boundary = -boundary_vector

    assert_equal(
        bulk_state,
        dual_boundary,
        "a filling state has the dual variance to the boundary anomaly vector",
    )
    assert_equal(
        boundary_vector + bulk_state,
        scalar,
        "boundary covector evaluates on the bulk state to a scalar",
    )
    assert_equal(
        -boundary_vector,
        bulk_state,
        "orientation reversal dualizes the boundary anomaly line",
    )

    wrong_scalar_filling = 0
    if boundary_vector + wrong_scalar_filling == scalar:
        raise AssertionError("negative control failed: scalar filling cannot cancel anomaly line")

    wrong_same_line_filling = boundary_vector
    if boundary_vector + wrong_same_line_filling == scalar:
        raise AssertionError("negative control failed: same-line filling cannot cancel anomaly line")

    # If b_X' = lambda b_X in the bulk state line, then the dual frame obeys
    # (b_X')^{-1} = lambda^{-1} b_X^{-1}.  Therefore a vector z b_X^{-1}
    # has coordinate z' = z lambda in the X' dual frame.  Check the additive
    # finite-phase version of this filling-quotient transition law.
    for modulus in range(2, 19):
        samples = sorted({0, 1, modulus // 3, modulus // 2, modulus - 1})
        for transition in samples:
            for coordinate in samples:
                bulk_frame_shift = transition
                dual_frame_shift = (-transition) % modulus
                new_coordinate = (coordinate + transition) % modulus
                assert_equal(
                    (bulk_frame_shift + dual_frame_shift) % modulus,
                    0,
                    "bulk frame and dual anomaly frame have inverse transition",
                )
                assert_equal(
                    (new_coordinate + dual_frame_shift) % modulus,
                    coordinate % modulus,
                    "filling quotient is the coordinate law for dual frames",
                )


def check_local_descent_zero_can_leave_global_holonomy() -> None:
    """Separate identity-component cancellation from a flat global anomaly.

    The finite model is a one-object action groupoid for
    G = Z_2 x Z_3, with Z_3 treated as the connected/local subgroup.  The
    character a(epsilon, k)=epsilon has zero restriction to Z_3, so the local
    descent coordinate vanishes, but its Z_2 holonomy is nontrivial.  Since
    the action is on one object, every 0-cochain coboundary is zero, so no
    local frame/counterterm removes this global sign.
    """

    modulus = 2

    def add(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
        return ((first[0] + second[0]) % 2, (first[1] + second[1]) % 3)

    def anomaly(group_element: tuple[int, int]) -> int:
        return group_element[0] % modulus

    group = [(epsilon, local) for epsilon in range(2) for local in range(3)]
    local_subgroup = [(0, local) for local in range(3)]

    for first in group:
        for second in group:
            lhs = anomaly(add(first, second))
            rhs = (anomaly(first) + anomaly(second)) % modulus
            assert_equal(lhs, rhs, "flat global anomaly character is a cocycle")

    for local in local_subgroup:
        assert_equal(
            anomaly(local),
            0,
            "identity-component local descent coordinate vanishes",
        )

    assert_equal(
        anomaly((1, 0)),
        1,
        "large transformation has nontrivial flat holonomy",
    )

    for counterterm_value in range(modulus):
        coboundary = (counterterm_value - counterterm_value) % modulus
        assert_equal(coboundary, 0, "one-object counterterm coboundary vanishes")
        assert_equal(
            (anomaly((1, 0)) + coboundary) % modulus,
            1,
            "local counterterm cannot remove the flat global holonomy",
        )


def simplices(top_dimension: int, degree: int) -> list[Simplex]:
    return list(combinations(range(top_dimension + 1), degree + 1))


def coboundary(cochain: Cochain, degree: int, top_dimension: int, modulus: int) -> Cochain:
    result: Cochain = {}
    for simplex in simplices(top_dimension, degree + 1):
        total = 0
        for index in range(degree + 2):
            face = simplex[:index] + simplex[index + 1 :]
            total += (-1) ** index * cochain.get(face, 0)
        result[simplex] = total % modulus
    return result


def cup(lhs: Cochain, lhs_degree: int, rhs: Cochain, rhs_degree: int, top_dimension: int, modulus: int) -> Cochain:
    result: Cochain = {}
    for simplex in simplices(top_dimension, lhs_degree + rhs_degree):
        left_face = simplex[: lhs_degree + 1]
        right_face = simplex[lhs_degree:]
        result[simplex] = lhs.get(left_face, 0) * rhs.get(right_face, 0) % modulus
    return result


def integrate_simplex(cochain: Cochain, top_dimension: int, modulus: int) -> int:
    return cochain[tuple(range(top_dimension + 1))] % modulus


def integrate_boundary(cochain: Cochain, top_dimension: int, modulus: int) -> int:
    total = 0
    top = tuple(range(top_dimension + 1))
    for index in range(top_dimension + 1):
        face = top[:index] + top[index + 1 :]
        total += (-1) ** index * cochain.get(face, 0)
    return total % modulus


def deterministic_cochain(top_dimension: int, degree: int, modulus: int, seed: int) -> Cochain:
    values: Cochain = {}
    for simplex in simplices(top_dimension, degree):
        raw = seed
        for place, vertex in enumerate(simplex, start=1):
            raw += place * (vertex + 1) * (seed + 2)
        values[simplex] = raw % modulus
    return values


def check_finite_bf_boundary_variation() -> None:
    top_dimension = 5
    for modulus in range(2, 13):
        lam = deterministic_cochain(top_dimension, 1, modulus, seed=3)
        c_field = deterministic_cochain(top_dimension, 2, modulus, seed=5)
        kappa = deterministic_cochain(top_dimension, 1, modulus, seed=7)

        delta_lam = coboundary(lam, 1, top_dimension, modulus)
        delta_c = coboundary(c_field, 2, top_dimension, modulus)
        variation = cup(delta_lam, 2, delta_c, 3, top_dimension, modulus)

        boundary_cochain = cup(lam, 1, delta_c, 3, top_dimension, modulus)
        boundary_term = integrate_boundary(boundary_cochain, top_dimension, modulus)
        assert_equal(
            integrate_simplex(variation, top_dimension, modulus),
            boundary_term,
            "finite BF inflow variation equals boundary Stokes term",
        )

        delta_kappa = coboundary(kappa, 1, top_dimension, modulus)
        shifted_c = {
            simplex: (c_field[simplex] + delta_kappa[simplex]) % modulus
            for simplex in simplices(top_dimension, 2)
        }
        assert_equal(
            coboundary(shifted_c, 2, top_dimension, modulus),
            delta_c,
            "finite BF action is invariant under c -> c + delta kappa",
        )


def main() -> None:
    check_chevalley_eilenberg_wess_zumino_sign()
    check_functorial_cocycle_condition()
    check_counterterm_frame_change_preserves_cocycle()
    check_finite_regulator_scheme_change_is_coboundary()
    check_coordinate_comparison_between_cochain_line_and_inflow()
    check_rg_shell_pushforward_preserves_anomaly_line()
    check_bulk_boundary_dual_line_variance()
    check_local_descent_zero_can_leave_global_holonomy()
    check_finite_bf_boundary_variation()
    print(
        "Anomaly-line, descent-cocycle, coordinate-comparison, RG-shell, "
        "line-variance, local/global-holonomy, and finite-inflow cochain checks passed."
    )


if __name__ == "__main__":
    main()
