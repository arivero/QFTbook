#!/usr/bin/env python3
r"""Finite checks for the jet shape-function convolution layer.

These checks do not prove an SCET factorization theorem.  They verify the
finite algebra used in the shape-function section: a normalized soft spectral
coordinate preserves the total endpoint cross section under convolution,
shifts the first event-shape moment by its first soft moment divided by Q, and
has the expected paired translation covariance under finite subtraction-scheme
changes.  The checks also verify the second-order smeared-test expansion: the
first soft moment gives the leading endpoint shift, while the second soft
moment controls the Taylor remainder and is needed for quadratic endpoint
tests.  The moment-truncation check verifies the next physics guardrail: two
soft spectral distributions can share normalization, \(\Omega_1\), and
\(\Omega_2\), while giving different endpoint-bin occupancies.

Evidence contract.

Target claims:
  Volume II, Chapter 19b treats a leading shape function as a renormalized
  Wilson-line measurement distribution paired with endpoint tests, uses the
  leading convolution to transport perturbative event-shape spectra, records
  the scheme-dependent first-moment shift, and requires an observable-level
  residual when a finite moment fit replaces the full shape distribution.

Independent construction:
  The checks build finite positive spectral measures directly, convolve them
  with finite perturbative endpoint measures, pair the result with explicit
  test functions, and compare moment-matched shape distributions against
  local endpoint-bin tests.  They do not read a displayed convolution formula
  as the expected answer.

Imported assumptions:
  The SCET leading-power factorization theorem for the chosen event shape,
  renormalization of the lightlike Wilson-line measurement operator,
  existence of the declared endpoint test-function topology, perturbative
  coefficient control, and power/hadronization remainders are imported QFT
  inputs.

Negative controls:
  The suite rejects using an unmatched fitted first soft moment for the
  endpoint mean, treating first-moment fits as sufficient for quadratic
  smearings, treating first-two-moment fits as sufficient for localized
  endpoint bins, and shifting the shape coordinate without the paired
  perturbative subtraction-scheme translation.

Scope boundary:
  These are exact finite spectral-measure, convolution, moment, scheme, and
  moment-truncation checks.  They are not a proof of SCET factorization, a
  derivation of the Wilson-line soft matrix element, a Euclidean-to-lightlike
  matching theorem, or a phenomenological fit to collider data.

Primary derivation route:
  The manuscript route defines the Wilson-line shape coordinate by test
  pairing, inserts it into the endpoint convolution, derives total-rate and
  first-moment diagnostics, records paired subtraction-scheme translations,
  and then expands smooth endpoint tests to expose the moment-truncation
  residual.

Independent verification route:
  The executable route starts from rational finite measures.  It verifies
  spectral normalization and moments, exact convolution normalization, the
  first endpoint moment shift, paired scheme-translation covariance,
  second-order Taylor remainders for smooth tests, and a moment-matched
  negative control for local endpoint-bin occupancy.

Convention dependencies:
  The event shape \(e\) is dimensionless, the soft measurement coordinate
  \(\ell\) shifts it by \(\ell/Q\), distributions are paired against endpoint
  tests rather than pointwise densities unless a density chart is declared,
  and subtraction-scheme translations move the same \(\delta\ell\) between
  the perturbative coefficient and shape coordinate.

Domain and remainder assumptions:
  The finite checks apply to positive finite spectral measures and exact
  rational endpoint tests.  The manuscript claims still require a declared
  endpoint Banach space, smoothness or bin-resolution assumptions on the test
  family, perturbative coefficient bounds, and a residual budget for omitted
  power corrections and unmodelled shape directions.

Remaining unproved or conditional:
  The checks leave open the event-shape-specific SCET theorem, the
  renormalized Wilson-line distribution construction, Euclidean reconstruction
  of the lightlike shape coordinate, and quantitative bounds on the
  phenomenological residual \(B_{\rm shape}^{(m)}\) for a chosen fit family.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Callable, Mapping

Distribution = Mapping[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def norm(dist: Distribution) -> Fraction:
    return sum(dist.values(), Fraction(0))


def moment(dist: Distribution) -> Fraction:
    return sum(point * weight for point, weight in dist.items())


def second_moment(dist: Distribution) -> Fraction:
    return sum(point * point * weight for point, weight in dist.items())


def power_moment(dist: Distribution, power: int) -> Fraction:
    return sum(point**power * weight for point, weight in dist.items())


def pair(dist: Distribution, test_function: Callable[[Fraction], Fraction]) -> Fraction:
    return sum(weight * test_function(point) for point, weight in dist.items())


def convolve_endpoint(
    perturbative: Distribution,
    shape: Distribution,
    q_hard: Fraction,
) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = defaultdict(Fraction)
    for e_pert, weight_pert in perturbative.items():
        for ell, weight_shape in shape.items():
            out[e_pert + ell / q_hard] += weight_pert * weight_shape
    return dict(out)


def translate(dist: Distribution, shift: Fraction) -> dict[Fraction, Fraction]:
    return {point + shift: weight for point, weight in dist.items()}


def check_spectral_pairing() -> None:
    # A finite positive measurement operator has eigenvalues ell and
    # Wilson-line-state spectral weights.  Pairing with h(ell) is the finite
    # version of <F_e,h>.
    shape = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(1, 2), Fraction(6): Fraction(1, 4)}
    test = lambda ell: Fraction(2) + ell + ell * ell / Fraction(6)

    assert_equal("finite spectral normalization", norm(shape), Fraction(1))
    assert_equal("finite spectral first moment", moment(shape), Fraction(3))
    assert_equal(
        "test-function spectral pairing",
        pair(shape, test),
        Fraction(2) + Fraction(3) + Fraction(9, 4),
    )


def check_convolution_normalization_and_moment() -> None:
    perturbative = {Fraction(1, 30): Fraction(2, 5), Fraction(1, 10): Fraction(3, 5)}
    shape = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(1, 2), Fraction(6): Fraction(1, 4)}
    q_hard = Fraction(12)

    convolved = convolve_endpoint(perturbative, shape, q_hard)
    assert_equal("shape convolution normalization", norm(convolved), norm(perturbative) * norm(shape))

    expected_first_moment = moment(perturbative) * norm(shape) + norm(perturbative) * moment(shape) / q_hard
    assert_equal("shape convolution first moment", moment(convolved), expected_first_moment)


def check_scheme_translation_covariance() -> None:
    perturbative = {Fraction(1, 30): Fraction(2, 5), Fraction(1, 10): Fraction(3, 5)}
    shape = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(1, 2), Fraction(6): Fraction(1, 4)}
    q_hard = Fraction(12)
    delta_ell = Fraction(3, 2)

    baseline = convolve_endpoint(perturbative, shape, q_hard)
    shifted_shape = translate(shape, delta_ell)
    shifted_perturbative = translate(perturbative, -delta_ell / q_hard)
    shifted = convolve_endpoint(shifted_perturbative, shifted_shape, q_hard)

    assert_equal("paired scheme-translation covariance", shifted, baseline)


def check_smeared_shift_expansion_and_fit_controls() -> None:
    perturbative = {Fraction(1, 30): Fraction(2, 5), Fraction(1, 10): Fraction(3, 5)}
    shape = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(1, 2), Fraction(6): Fraction(1, 4)}
    q_hard = Fraction(12)
    omega_1 = moment(shape)
    omega_2 = second_moment(shape)
    convolved = convolve_endpoint(perturbative, shape, q_hard)

    test = lambda e: Fraction(2) - e + 3 * e * e
    test_prime = lambda e: Fraction(-1) + 6 * e
    second_derivative_bound = Fraction(6)

    exact = pair(convolved, test)
    first_order_shift = pair(
        perturbative,
        lambda e: test(e) + omega_1 * test_prime(e) / q_hard,
    )
    remainder = exact - first_order_shift
    expected_quadratic_remainder = (
        norm(perturbative) * omega_2 * second_derivative_bound / (2 * q_hard * q_hard)
    )
    assert_equal(
        "shape-function smeared second-order remainder",
        remainder,
        expected_quadratic_remainder,
    )

    shape_same_first_a = {Fraction(0): Fraction(1, 2), Fraction(6): Fraction(1, 2)}
    shape_same_first_b = {Fraction(3): Fraction(1)}
    assert_equal("same first soft moment control", moment(shape_same_first_a), moment(shape_same_first_b))
    assert_equal("same normalization control", norm(shape_same_first_a), norm(shape_same_first_b))
    quadratic_a = pair(convolve_endpoint(perturbative, shape_same_first_a, q_hard), lambda e: e * e)
    quadratic_b = pair(convolve_endpoint(perturbative, shape_same_first_b, q_hard), lambda e: e * e)
    assert_equal(
        "same first moment does not fix quadratic endpoint smear",
        quadratic_a - quadratic_b,
        (
            second_moment(shape_same_first_a)
            - second_moment(shape_same_first_b)
        ) / (q_hard * q_hard),
    )

    wrong_fit_shape = {Fraction(0): Fraction(1, 2), Fraction(4): Fraction(1, 2)}
    correct_linear = pair(convolved, lambda e: e)
    wrong_linear = moment(perturbative) + moment(wrong_fit_shape) / q_hard
    assert_equal(
        "mismatched fitted first moment shifts the endpoint mean",
        correct_linear - wrong_linear,
        (omega_1 - moment(wrong_fit_shape)) / q_hard,
    )


def check_moment_matched_shapes_do_not_fix_endpoint_bins() -> None:
    perturbative = {Fraction(0): Fraction(1)}
    shape_two_point = {Fraction(0): Fraction(1, 2), Fraction(2): Fraction(1, 2)}
    shape_three_point = {
        Fraction(0): Fraction(1, 3),
        Fraction(1): Fraction(1, 2),
        Fraction(3): Fraction(1, 6),
    }
    q_hard = Fraction(12)

    for power in range(3):
        assert_equal(
            f"shape moment match through power {power}",
            power_moment(shape_two_point, power),
            power_moment(shape_three_point, power),
        )

    convolved_two_point = convolve_endpoint(perturbative, shape_two_point, q_hard)
    convolved_three_point = convolve_endpoint(perturbative, shape_three_point, q_hard)
    for power in range(3):
        assert_equal(
            f"convolved endpoint polynomial match through degree {power}",
            pair(convolved_two_point, lambda e, power=power: e**power),
            pair(convolved_three_point, lambda e, power=power: e**power),
        )

    cubic_difference = pair(convolved_three_point, lambda e: e**3) - pair(
        convolved_two_point,
        lambda e: e**3,
    )
    assert_equal(
        "same first two shape moments leave cubic endpoint residual",
        cubic_difference,
        (power_moment(shape_three_point, 3) - power_moment(shape_two_point, 3)) / q_hard**3,
    )

    endpoint_bin = lambda e: Fraction(1) if e <= Fraction(1, 12) else Fraction(0)
    bin_difference = pair(convolved_three_point, endpoint_bin) - pair(convolved_two_point, endpoint_bin)
    assert_equal("same first two shape moments leave endpoint-bin residual", bin_difference, Fraction(1, 3))


def main() -> None:
    check_spectral_pairing()
    check_convolution_normalization_and_moment()
    check_scheme_translation_covariance()
    check_smeared_shift_expansion_and_fit_controls()
    check_moment_matched_shapes_do_not_fix_endpoint_bins()
    print("All shape-function convolution checks passed.")


if __name__ == "__main__":
    main()
