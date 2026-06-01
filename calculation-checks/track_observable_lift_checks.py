#!/usr/bin/env python3
"""Exact checks for finite track-observable lifting identities."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from typing import Mapping


Distribution = Mapping[Fraction, Fraction]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def moment(dist: Distribution, power: int) -> Fraction:
    return sum((x**power) * weight for x, weight in dist.items())


def compose_moment(left: Distribution, right: Distribution, z: Fraction, power: int) -> Fraction:
    total = Fraction(0)
    for x1, w1 in left.items():
        for x2, w2 in right.items():
            total += (z * x1 + (Fraction(1) - z) * x2) ** power * w1 * w2
    return total


def lifted_two_point(
    energies: list[Fraction],
    species: list[str],
    tracks: Mapping[str, Distribution],
    kernel: Mapping[tuple[int, int], Fraction],
) -> Fraction:
    total = Fraction(0)
    for a, energy_a in enumerate(energies):
        for b, energy_b in enumerate(energies):
            if a == b:
                track_factor = moment(tracks[species[a]], 2)
            else:
                track_factor = moment(tracks[species[a]], 1) * moment(tracks[species[b]], 1)
            total += energy_a * energy_b * kernel[(a, b)] * track_factor
    return total


def enumerate_lifted_two_point(
    energies: list[Fraction],
    species: list[str],
    tracks: Mapping[str, Distribution],
    kernel: Mapping[tuple[int, int], Fraction],
) -> Fraction:
    total = Fraction(0)
    n = len(energies)

    def rec(index: int, xs: list[Fraction], weight: Fraction) -> None:
        nonlocal total
        if index == n:
            value = Fraction(0)
            for a, energy_a in enumerate(energies):
                for b, energy_b in enumerate(energies):
                    value += energy_a * xs[a] * energy_b * xs[b] * kernel[(a, b)]
            total += weight * value
            return
        for x, probability in tracks[species[index]].items():
            rec(index + 1, xs + [x], weight * probability)

    rec(0, [], Fraction(1))
    return total


def lifted_k_point(
    energies: list[Fraction],
    species: list[str],
    tracks: Mapping[str, Distribution],
    kernel: Mapping[tuple[int, ...], Fraction],
    arity: int,
) -> Fraction:
    total = Fraction(0)
    for labels in product(range(len(energies)), repeat=arity):
        energy_factor = Fraction(1)
        for label in labels:
            energy_factor *= energies[label]

        track_factor = Fraction(1)
        for label, multiplicity in Counter(labels).items():
            track_factor *= moment(tracks[species[label]], multiplicity)

        total += energy_factor * kernel[labels] * track_factor
    return total


def enumerate_lifted_k_point(
    energies: list[Fraction],
    species: list[str],
    tracks: Mapping[str, Distribution],
    kernel: Mapping[tuple[int, ...], Fraction],
    arity: int,
) -> Fraction:
    total = Fraction(0)
    n = len(energies)

    def rec(index: int, xs: list[Fraction], weight: Fraction) -> None:
        nonlocal total
        if index == n:
            value = Fraction(0)
            for labels in product(range(n), repeat=arity):
                factor = kernel[labels]
                for label in labels:
                    factor *= energies[label] * xs[label]
                value += factor
            total += weight * value
            return
        for x, probability in tracks[species[index]].items():
            rec(index + 1, xs + [x], weight * probability)

    rec(0, [], Fraction(1))
    return total


def check_diagonal_track_moment() -> None:
    tracks = {"q": {Fraction(0): Fraction(1, 4), Fraction(1, 2): Fraction(1, 2), Fraction(1): Fraction(1, 4)}}
    energies = [Fraction(5)]
    species = ["q"]
    kernel = {(0, 0): Fraction(7)}
    expected = Fraction(5) * Fraction(5) * Fraction(7) * moment(tracks["q"], 2)
    assert_equal("diagonal two-point lift", lifted_two_point(energies, species, tracks, kernel), expected)
    assert_equal(
        "diagonal enumeration",
        enumerate_lifted_two_point(energies, species, tracks, kernel),
        expected,
    )
    if moment(tracks["q"], 2) == moment(tracks["q"], 1) ** 2:
        raise AssertionError("test distribution should distinguish second moment from squared first moment")


def check_two_particle_lift() -> None:
    tracks = {
        "q": {Fraction(1, 4): Fraction(1, 3), Fraction(1): Fraction(2, 3)},
        "g": {Fraction(0): Fraction(1, 5), Fraction(3, 5): Fraction(4, 5)},
    }
    energies = [Fraction(3), Fraction(2)]
    species = ["q", "g"]
    kernel = {
        (0, 0): Fraction(5),
        (0, 1): Fraction(7),
        (1, 0): Fraction(11),
        (1, 1): Fraction(13),
    }
    assert_equal(
        "two-particle finite track lift",
        lifted_two_point(energies, species, tracks, kernel),
        enumerate_lifted_two_point(energies, species, tracks, kernel),
    )


def check_three_point_track_lift() -> None:
    tracks = {
        "q": {Fraction(0): Fraction(1, 6), Fraction(1, 2): Fraction(1, 3), Fraction(1): Fraction(1, 2)},
        "g": {Fraction(1, 5): Fraction(2, 5), Fraction(4, 5): Fraction(3, 5)},
    }
    energies = [Fraction(2), Fraction(5)]
    species = ["q", "g"]
    arity = 3
    kernel = {
        labels: Fraction(1 + labels[0] + 2 * labels[1] + 3 * labels[2], 7)
        for labels in product(range(len(energies)), repeat=arity)
    }

    exact = lifted_k_point(energies, species, tracks, kernel, arity)
    enumerated = enumerate_lifted_k_point(energies, species, tracks, kernel, arity)
    assert_equal("three-point finite track lift", exact, enumerated)

    naive_first_moment_only = Fraction(0)
    for labels in product(range(len(energies)), repeat=arity):
        factor = kernel[labels]
        for label in labels:
            factor *= energies[label] * moment(tracks[species[label]], 1)
        naive_first_moment_only += factor
    if naive_first_moment_only == exact:
        raise AssertionError("first-moment replacement should miss diagonal track-moment terms")


def check_collinear_composition_moments() -> None:
    left = {Fraction(0): Fraction(1, 3), Fraction(3, 4): Fraction(2, 3)}
    right = {Fraction(1, 5): Fraction(1, 2), Fraction(1): Fraction(1, 2)}
    z = Fraction(2, 5)
    first_formula = z * moment(left, 1) + (Fraction(1) - z) * moment(right, 1)
    second_formula = (
        z * z * moment(left, 2)
        + (Fraction(1) - z) ** 2 * moment(right, 2)
        + 2 * z * (Fraction(1) - z) * moment(left, 1) * moment(right, 1)
    )
    assert_equal("composed first moment", compose_moment(left, right, z, 1), first_formula)
    assert_equal("composed second moment", compose_moment(left, right, z, 2), second_formula)


def main() -> None:
    check_diagonal_track_moment()
    check_two_particle_lift()
    check_three_point_track_lift()
    check_collinear_composition_moments()
    print("All finite track-observable lift checks passed.")


if __name__ == "__main__":
    main()
