#!/usr/bin/env python3
"""Exact checks for track-energy correlator bookkeeping.

The script verifies finite algebra used in the QCD energy-correlator
discussion: selected calorimetric measures, track-EEC moment identities, and
the binomial moment ledger for a collinear track-function split.
"""

from fractions import Fraction
from math import comb


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def check_selected_measure_moments():
    # Three massless particles in a center-of-mass event.
    z = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    directions = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    ]
    tau = [Fraction(1), Fraction(0), Fraction(1)]  # selected charged tracks

    selected_energy = sum(t * e for t, e in zip(tau, z))
    selected_momentum = tuple(
        sum(tau[r] * z[r] * directions[r][mu] for r in range(3))
        for mu in range(3)
    )

    zeroth = sum(tau[r] * tau[s] * z[r] * z[s] for r in range(3) for s in range(3))
    first = sum(
        tau[r] * tau[s] * z[r] * z[s] * dot(directions[r], directions[s])
        for r in range(3)
        for s in range(3)
    )
    contact = sum(t * t * e * e for t, e in zip(tau, z))

    assert_equal("track EEC zeroth moment", zeroth, selected_energy**2)
    assert_equal("track EEC first moment", first, dot(selected_momentum, selected_momentum))
    assert_equal("track contact weight", contact, Fraction(5, 18))


def split_moment(z, moments_j, moments_k, n):
    return sum(
        Fraction(comb(n, a))
        * z**a
        * (1 - z) ** (n - a)
        * moments_j[a]
        * moments_k[n - a]
        for a in range(n + 1)
    )


def check_track_function_split_moments():
    z = Fraction(2, 5)
    moments_j = {
        0: Fraction(1),
        1: Fraction(3, 7),
        2: Fraction(2, 9),
        3: Fraction(5, 33),
    }
    moments_k = {
        0: Fraction(1),
        1: Fraction(1, 4),
        2: Fraction(1, 10),
        3: Fraction(1, 20),
    }

    assert_equal("split zeroth moment", split_moment(z, moments_j, moments_k, 0), Fraction(1))

    expected_first = z * moments_j[1] + (1 - z) * moments_k[1]
    assert_equal("split first moment", split_moment(z, moments_j, moments_k, 1), expected_first)

    contact = z**2 * moments_j[2] + (1 - z) ** 2 * moments_k[2]
    separated = 2 * z * (1 - z) * moments_j[1] * moments_k[1]
    expected_second = contact + separated
    assert_equal("split second moment", split_moment(z, moments_j, moments_k, 2), expected_second)

    # For a full calorimeter all moments equal one, and the separated track
    # weight becomes the ordinary EEC weight 2 z (1-z).
    full = {0: Fraction(1), 1: Fraction(1), 2: Fraction(1)}
    full_separated = 2 * z * (1 - z) * full[1] * full[1]
    assert_equal("full calorimeter separated weight", full_separated, 2 * z * (1 - z))
    assert_equal("full calorimeter second moment", split_moment(z, full, full, 2), Fraction(1))


def main():
    check_selected_measure_moments()
    check_track_function_split_moments()
    print("All track energy-correlator checks passed.")


if __name__ == "__main__":
    main()
