#!/usr/bin/env python3
"""Finite-kernel checks for track-function RG identities.

The monograph derives normalization, first-moment, and moment-tower identities
for the paired real--virtual track-function evolution in a finite-kernel
model.  This script verifies the same identities for discrete rational track
measures and discrete splitting kernels.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb
from typing import Dict, Iterable, Mapping, Tuple

Species = str
Distribution = Mapping[Fraction, Fraction]
Kernel = Tuple[Species, Species, Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def norm(dist: Distribution) -> Fraction:
    return sum(dist.values(), Fraction(0))


def moment(dist: Distribution) -> Fraction:
    return sum(x * weight for x, weight in dist.items())


def moment_power(dist: Distribution, power: int) -> Fraction:
    return sum((x**power) * weight for x, weight in dist.items())


def convolution_gain(
    left: Distribution,
    right: Distribution,
    z: Fraction,
    rate: Fraction,
) -> Dict[Fraction, Fraction]:
    gain: Dict[Fraction, Fraction] = defaultdict(Fraction)
    for x1, w1 in left.items():
        for x2, w2 in right.items():
            x = z * x1 + (Fraction(1) - z) * x2
            gain[x] += rate * w1 * w2
    return dict(gain)


def add_scaled(
    out: Dict[Fraction, Fraction],
    dist: Distribution,
    scale: Fraction,
) -> None:
    for x, weight in dist.items():
        out[x] += scale * weight


def derivative_distribution(
    species: Species,
    tracks: Mapping[Species, Distribution],
    kernels: Mapping[Species, Iterable[Kernel]],
) -> Dict[Fraction, Fraction]:
    derivative: Dict[Fraction, Fraction] = defaultdict(Fraction)
    gamma = Fraction(0)
    for daughter_left, daughter_right, z, rate in kernels[species]:
        gamma += rate
        gain = convolution_gain(tracks[daughter_left], tracks[daughter_right], z, rate)
        add_scaled(derivative, gain, Fraction(1))
    add_scaled(derivative, tracks[species], -gamma)
    return dict(derivative)


def predicted_moment_derivative(
    species: Species,
    tracks: Mapping[Species, Distribution],
    kernels: Mapping[Species, Iterable[Kernel]],
) -> Fraction:
    m_parent = moment(tracks[species])
    total = Fraction(0)
    for daughter_left, daughter_right, z, rate in kernels[species]:
        total += rate * (
            z * moment(tracks[daughter_left])
            + (Fraction(1) - z) * moment(tracks[daughter_right])
            - m_parent
        )
    return total


def predicted_moment_tower_derivative(
    species: Species,
    tracks: Mapping[Species, Distribution],
    kernels: Mapping[Species, Iterable[Kernel]],
    power: int,
) -> Fraction:
    parent_moment = moment_power(tracks[species], power)
    total = Fraction(0)
    for daughter_left, daughter_right, z, rate in kernels[species]:
        composed = sum(
            Fraction(comb(power, a))
            * (z**a)
            * ((Fraction(1) - z) ** (power - a))
            * moment_power(tracks[daughter_left], a)
            * moment_power(tracks[daughter_right], power - a)
            for a in range(power + 1)
        )
        total += rate * (composed - parent_moment)
    return total


def check_normalization_and_moment_identities() -> None:
    tracks = {
        "q": {Fraction(1): Fraction(1, 3), Fraction(1, 2): Fraction(2, 3)},
        "g": {Fraction(0): Fraction(1, 4), Fraction(3, 4): Fraction(3, 4)},
    }
    kernels = {
        "q": (
            ("q", "g", Fraction(2, 3), Fraction(3)),
            ("g", "q", Fraction(1, 4), Fraction(1)),
        ),
        "g": (
            ("q", "q", Fraction(1, 2), Fraction(2)),
            ("g", "g", Fraction(1, 3), Fraction(5)),
        ),
    }

    for species, dist in tracks.items():
        assert_equal(f"{species} track normalization", norm(dist), Fraction(1))

    for species in ("q", "g"):
        deriv = derivative_distribution(species, tracks, kernels)
        assert_equal(f"{species} normalization derivative", norm(deriv), Fraction(0))
        assert_equal(
            f"{species} first-moment derivative",
            moment(deriv),
            predicted_moment_derivative(species, tracks, kernels),
        )
        for power in range(5):
            assert_equal(
                f"{species} moment-tower derivative power={power}",
                moment_power(deriv, power),
                predicted_moment_tower_derivative(species, tracks, kernels, power),
            )


def main() -> None:
    check_normalization_and_moment_identities()
    print("All track-function moment checks passed.")


if __name__ == "__main__":
    main()
