#!/usr/bin/env python3
"""Finite checks for Steinmann channel overlap and sequential cuts.

The accompanying Volume II analyticity section distinguishes compatible
double cuts from forbidden overlapping-channel double cuts.  These checks keep
the finite set-theoretic definitions, the causal-order obstruction, and the
toy double-spectral discontinuity algebra synchronized with the text.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Channel = frozenset[int]
Universe = frozenset[int]


def assert_equal(label: str, actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: got {actual!r}, expected {expected!r}")


def assert_true(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)


def complement(channel: Channel, universe: Universe) -> Channel:
    return frozenset(universe - channel)


def is_proper_channel(channel: Channel, universe: Universe) -> bool:
    return 2 <= len(channel) <= len(universe) - 2


def representatives(channel: Channel, universe: Universe) -> tuple[Channel, Channel]:
    return channel, complement(channel, universe)


def overlap(channel_a: Channel, channel_b: Channel, universe: Universe) -> bool:
    sectors = (
        channel_a & channel_b,
        channel_a - channel_b,
        channel_b - channel_a,
        universe - (channel_a | channel_b),
    )
    return all(bool(sector) for sector in sectors)


def disjoint_or_nested(channel_a: Channel, channel_b: Channel) -> bool:
    return (
        channel_a.isdisjoint(channel_b)
        or channel_a <= channel_b
        or channel_b <= channel_a
    )


def compatible(channel_a: Channel, channel_b: Channel, universe: Universe) -> bool:
    return any(
        disjoint_or_nested(rep_a, rep_b)
        for rep_a in representatives(channel_a, universe)
        for rep_b in representatives(channel_b, universe)
    )


def sector_decomposition(
    channel_a: Channel, channel_b: Channel, universe: Universe
) -> dict[str, Channel]:
    return {
        "X": channel_a & channel_b,
        "Y": channel_a - channel_b,
        "Z": channel_b - channel_a,
        "W": universe - (channel_a | channel_b),
    }


def orientation_edges(
    channel: Channel,
    universe: Universe,
    sectors: dict[str, Channel],
    orientation: int,
) -> set[tuple[str, str]]:
    if orientation not in (1, -1):
        raise ValueError("orientation must be +1 or -1")

    later = channel if orientation == 1 else complement(channel, universe)
    earlier = complement(channel, universe) if orientation == 1 else channel
    nonempty = {label: sector for label, sector in sectors.items() if sector}
    return {
        (left_label, right_label)
        for left_label, left_sector in nonempty.items()
        for right_label, right_sector in nonempty.items()
        if left_sector <= later and right_sector <= earlier
    }


def has_cycle(edges: set[tuple[str, str]]) -> bool:
    nodes = {node for edge in edges for node in edge}
    graph = {node: set() for node in nodes}
    for source, target in edges:
        graph[source].add(target)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for target in graph[node]:
            if visit(target):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in nodes)


def orientation_pair_has_cycle(
    channel_a: Channel,
    channel_b: Channel,
    universe: Universe,
    orientation_a: int,
    orientation_b: int,
) -> bool:
    sectors = sector_decomposition(channel_a, channel_b, universe)
    edges = orientation_edges(channel_a, universe, sectors, orientation_a)
    edges |= orientation_edges(channel_b, universe, sectors, orientation_b)
    return has_cycle(edges)


def double_disc_density_coefficient(
    channel_a: Channel, channel_b: Channel, universe: Universe, density: Fraction
) -> Fraction:
    if overlap(channel_a, channel_b, universe):
        return Fraction(0)
    return density


def check_overlap_and_compatibility_definitions() -> None:
    universe_5 = frozenset(range(1, 6))
    channel_12 = frozenset({1, 2})
    channel_23 = frozenset({2, 3})
    channel_34 = frozenset({3, 4})
    channel_123 = frozenset({1, 2, 3})

    for channel in (channel_12, channel_23, channel_34, channel_123):
        assert_true(
            f"proper channel {sorted(channel)}",
            is_proper_channel(channel, universe_5),
        )

    assert_true("12 and 23 overlap", overlap(channel_12, channel_23, universe_5))
    assert_true(
        "overlap is complement-invariant in first argument",
        overlap(complement(channel_12, universe_5), channel_23, universe_5),
    )
    assert_equal(
        "overlapping channels are not compatible",
        compatible(channel_12, channel_23, universe_5),
        False,
    )

    assert_equal(
        "12 and 34 do not overlap",
        overlap(channel_12, channel_34, universe_5),
        False,
    )
    assert_true("12 and 34 are compatible", compatible(channel_12, channel_34, universe_5))
    assert_equal(
        "nested 12 and 123 do not overlap",
        overlap(channel_12, channel_123, universe_5),
        False,
    )
    assert_true(
        "nested 12 and 123 are compatible",
        compatible(channel_12, channel_123, universe_5),
    )


def check_causal_order_cycles() -> None:
    universe_5 = frozenset(range(1, 6))
    channel_12 = frozenset({1, 2})
    channel_23 = frozenset({2, 3})
    channel_34 = frozenset({3, 4})

    cycle_table = {
        orientations: orientation_pair_has_cycle(
            channel_12, channel_23, universe_5, *orientations
        )
        for orientations in product((1, -1), repeat=2)
    }
    assert_equal(
        "every overlapping orientation pair has a causal cycle",
        cycle_table,
        {
            (1, 1): True,
            (1, -1): True,
            (-1, 1): True,
            (-1, -1): True,
        },
    )

    assert_equal(
        "disjoint compatible cuts have an acyclic sheet choice",
        orientation_pair_has_cycle(channel_12, channel_34, universe_5, 1, -1),
        False,
    )
    assert_true(
        "some disjoint sheet choices can still be cyclic",
        orientation_pair_has_cycle(channel_12, channel_34, universe_5, 1, 1),
    )


def check_double_spectral_coefficients() -> None:
    universe_5 = frozenset(range(1, 6))
    channel_12 = frozenset({1, 2})
    channel_23 = frozenset({2, 3})
    channel_34 = frozenset({3, 4})
    density = Fraction(5, 7)

    assert_equal(
        "compatible double spectral density survives",
        double_disc_density_coefficient(channel_12, channel_34, universe_5, density),
        density,
    )
    assert_equal(
        "overlapping Steinmann density is forced to zero",
        double_disc_density_coefficient(channel_12, channel_23, universe_5, density),
        Fraction(0),
    )

    naive_overlap_coefficient = density
    assert_true(
        "naive overlapping double Cauchy ansatz would violate Steinmann",
        naive_overlap_coefficient
        != double_disc_density_coefficient(channel_12, channel_23, universe_5, density),
    )


def main() -> None:
    check_overlap_and_compatibility_definitions()
    check_causal_order_cycles()
    check_double_spectral_coefficients()
    print("All Steinmann channel and sequential-discontinuity checks passed.")


if __name__ == "__main__":
    main()
