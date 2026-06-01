#!/usr/bin/env python3
"""Finite checks for the jet shape-function convolution layer.

These checks do not prove an SCET factorization theorem.  They verify the
finite algebra used in the shape-function section: a normalized soft spectral
coordinate preserves the total endpoint cross section under convolution,
shifts the first event-shape moment by its first soft moment divided by Q, and
has the expected paired translation covariance under finite subtraction-scheme
changes.
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


def main() -> None:
    check_spectral_pairing()
    check_convolution_normalization_and_moment()
    check_scheme_translation_covariance()
    print("All shape-function convolution checks passed.")


if __name__ == "__main__":
    main()
