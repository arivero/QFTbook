#!/usr/bin/env python3
"""Finite checks for the jet shape-function convolution layer.

These checks do not prove an SCET factorization theorem.  They verify the
finite algebra used in the shape-function section: a normalized soft spectral
coordinate preserves the total endpoint cross section under convolution,
shifts the first event-shape moment by its first soft moment divided by Q, and
has the expected paired translation covariance under finite subtraction-scheme
changes.  The checks also verify the second-order smeared-test expansion: the
first soft moment gives the leading endpoint shift, while the second soft
moment controls the Taylor remainder and is needed for quadratic endpoint
tests.
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


def main() -> None:
    check_spectral_pairing()
    check_convolution_normalization_and_moment()
    check_scheme_translation_covariance()
    check_smeared_shift_expansion_and_fit_controls()
    print("All shape-function convolution checks passed.")


if __name__ == "__main__":
    main()
