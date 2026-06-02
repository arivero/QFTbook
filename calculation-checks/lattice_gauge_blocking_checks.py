#!/usr/bin/env python3
"""Finite gauge-blocking checks for the rigorous RG chapter.

The manuscript uses path products of fine links as a finite-regulator model
of a gauge-compatible Wilsonian blocking map.  This script checks the exact
group algebra in the smallest nonabelian test case, S_3.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product

Perm = tuple[int, int, int]
Edge = tuple[int, int]
FineConfig = dict[Edge, Perm]
CoarseConfig = tuple[Perm, Perm, Perm]

IDENTITY: Perm = (0, 1, 2)
ELEMENTS: tuple[Perm, ...] = tuple(permutations(range(3)))  # type: ignore[assignment]

E01: Edge = (0, 1)
E12: Edge = (1, 2)
E23: Edge = (2, 3)
E30: Edge = (3, 0)
FINE_EDGES: tuple[Edge, ...] = (E01, E12, E23, E30)


def mul(left: Perm, right: Perm) -> Perm:
    """Group multiplication, with permutations acting on the right argument first."""

    return tuple(left[right[i]] for i in range(3))  # type: ignore[return-value]


def inv(perm: Perm) -> Perm:
    inverse = [0, 0, 0]
    for i, image in enumerate(perm):
        inverse[image] = i
    return tuple(inverse)  # type: ignore[return-value]


def fixed_points(perm: Perm) -> int:
    return sum(1 for i, image in enumerate(perm) if i == image)


def conjugate(g: Perm, x: Perm) -> Perm:
    return mul(mul(g, x), inv(g))


def path_product(config: FineConfig, path: tuple[Edge, ...]) -> Perm:
    total = IDENTITY
    for edge in path:
        total = mul(total, config[edge])
    return total


def fine_gauge_transform(config: FineConfig, gauge: dict[int, Perm]) -> FineConfig:
    transformed: FineConfig = {}
    for source, target in FINE_EDGES:
        transformed[(source, target)] = mul(
            mul(gauge[source], config[(source, target)]),
            inv(gauge[target]),
        )
    return transformed


def block(config: FineConfig) -> CoarseConfig:
    """Coarse links for the triangle 0 -> 2 -> 3 -> 0."""

    return (
        path_product(config, (E01, E12)),
        config[E23],
        config[E30],
    )


def coarse_gauge_transform(coarse: CoarseConfig, gauge: dict[int, Perm]) -> CoarseConfig:
    u02, u23, u30 = coarse
    return (
        mul(mul(gauge[0], u02), inv(gauge[2])),
        mul(mul(gauge[2], u23), inv(gauge[3])),
        mul(mul(gauge[3], u30), inv(gauge[0])),
    )


def coarse_loop(coarse: CoarseConfig) -> Perm:
    u02, u23, u30 = coarse
    return mul(mul(u02, u23), u30)


def source_class_values(coarse: CoarseConfig) -> tuple[int, int]:
    """Two gauge-invariant source coordinates built from the closed loop."""

    loop = coarse_loop(coarse)
    return fixed_points(loop), fixed_points(mul(loop, loop))


def source_polynomial(coarse: CoarseConfig) -> Fraction:
    """Finite source polynomial used to test descent to gauge orbits.

    It is the second Taylor polynomial of an exponential source with rational
    source parameters.  Exact rational arithmetic is enough for the descent
    check, because every Taylor coefficient of a class-function source is
    separately gauge invariant.
    """

    first_class, second_class = source_class_values(coarse)
    source_linear = (
        Fraction(1, 5) * Fraction(first_class - 1)
        - Fraction(2, 7) * Fraction(second_class - 1)
    )
    return Fraction(1) + source_linear + source_linear * source_linear / 2


def fine_plaquette(config: FineConfig) -> Perm:
    return path_product(config, FINE_EDGES)


def gauge_invariant_weight(config: FineConfig) -> int:
    """Positive class-function weight for an S_3 plaquette."""

    return 3 + fixed_points(fine_plaquette(config))


def all_fine_configs() -> list[FineConfig]:
    configs: list[FineConfig] = []
    for values in product(ELEMENTS, repeat=len(FINE_EDGES)):
        configs.append(dict(zip(FINE_EDGES, values, strict=True)))
    return configs


def assert_equal(name: str, left: object, right: object) -> None:
    if left != right:
        raise AssertionError(f"{name}: {left!r} != {right!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def check_path_blocking_equivariance() -> None:
    config = {
        E01: (1, 2, 0),
        E12: (2, 0, 1),
        E23: (0, 2, 1),
        E30: (1, 0, 2),
    }
    fine_gauge = {
        0: (2, 1, 0),
        1: (1, 0, 2),
        2: (0, 2, 1),
        3: (2, 0, 1),
    }
    coarse_gauge = {0: fine_gauge[0], 2: fine_gauge[2], 3: fine_gauge[3]}
    assert_equal(
        "path blocking is gauge equivariant",
        block(fine_gauge_transform(config, fine_gauge)),
        coarse_gauge_transform(block(config), coarse_gauge),
    )


def check_blocked_wilson_loop() -> None:
    for config in all_fine_configs():
        blocked = block(config)
        assert_equal(
            "blocked loop equals concatenated fine plaquette",
            coarse_loop(blocked),
            fine_plaquette(config),
        )
        for h0, h2, h3 in product(ELEMENTS, repeat=3):
            transformed = coarse_gauge_transform(blocked, {0: h0, 2: h2, 3: h3})
            assert_equal(
                "Wilson character is invariant under coarse gauge conjugation",
                fixed_points(coarse_loop(transformed)),
                fixed_points(coarse_loop(blocked)),
            )


def check_pushforward_measure_invariance() -> None:
    pushforward: defaultdict[CoarseConfig, int] = defaultdict(int)
    for config in all_fine_configs():
        pushforward[block(config)] += gauge_invariant_weight(config)

    for coarse, weight in list(pushforward.items()):
        for h0, h2, h3 in product(ELEMENTS, repeat=3):
            transformed = coarse_gauge_transform(coarse, {0: h0, 2: h2, 3: h3})
            assert_equal(
                "blocked pushforward measure is coarse-gauge invariant",
                pushforward[transformed],
                weight,
            )


def check_gauge_invariant_source_window_descends() -> None:
    pushforward: defaultdict[CoarseConfig, int] = defaultdict(int)
    for config in all_fine_configs():
        pushforward[block(config)] += gauge_invariant_weight(config)

    deformed_pushforward = {
        coarse: Fraction(weight) * source_polynomial(coarse)
        for coarse, weight in pushforward.items()
    }

    for coarse in pushforward:
        base_values = source_class_values(coarse)
        base_source = source_polynomial(coarse)
        for h0, h2, h3 in product(ELEMENTS, repeat=3):
            transformed = coarse_gauge_transform(coarse, {0: h0, 2: h2, 3: h3})
            assert_equal(
                "closed-loop source coordinates descend to gauge orbits",
                source_class_values(transformed),
                base_values,
            )
            assert_equal(
                "source polynomial descends to gauge orbits",
                source_polynomial(transformed),
                base_source,
            )
            assert_equal(
                "source-deformed pushforward remains coarse-gauge invariant",
                deformed_pushforward[transformed],
                deformed_pushforward[coarse],
            )


def check_open_link_source_is_not_gauge_invariant() -> None:
    witness_found = False
    for coarse in product(ELEMENTS, repeat=3):
        base_value = fixed_points(coarse[0])
        for h0, h2, h3 in product(ELEMENTS, repeat=3):
            transformed = coarse_gauge_transform(coarse, {0: h0, 2: h2, 3: h3})
            if fixed_points(transformed[0]) != base_value:
                witness_found = True
                break
        if witness_found:
            break
    assert_true("an open-link source fails coarse gauge invariance", witness_found)


def check_fine_weight_gauge_invariance() -> None:
    config = {
        E01: (1, 2, 0),
        E12: (0, 2, 1),
        E23: (2, 0, 1),
        E30: (1, 0, 2),
    }
    base_weight = gauge_invariant_weight(config)
    for gauges in product(ELEMENTS, repeat=4):
        gauge = dict(zip((0, 1, 2, 3), gauges, strict=True))
        assert_equal(
            "fine plaquette class-function weight is gauge invariant",
            gauge_invariant_weight(fine_gauge_transform(config, gauge)),
            base_weight,
        )


def check_weighted_polymer_tail_bound() -> None:
    """Check the finite arithmetic behind the exponential locality norm."""

    # Toy line polymers containing the origin have multiplicity diameter+1.
    # The manuscript's weighted norm uses an exponential weight.  Here the
    # weighted ratio is chosen rationally: exp(zeta) * alpha = 1/3.
    weighted_ratio = Fraction(1, 3)
    norm_bound = Fraction(1, 1) / (1 - weighted_ratio) ** 2

    for cutoff in range(1, 8):
        partial_norm = sum(
            Fraction(diameter + 1) * weighted_ratio**diameter
            for diameter in range(cutoff + 1)
        )
        assert_true(
            f"finite weighted polymer norm cutoff {cutoff}",
            partial_norm <= norm_bound,
        )

    radius = 4
    tail = sum(
        Fraction(diameter + 1) * weighted_ratio**diameter
        for diameter in range(radius, 18)
    )

    def infinite_tail_from(first_diameter: int) -> Fraction:
        return weighted_ratio**first_diameter * (
            Fraction(first_diameter + 1) / (1 - weighted_ratio)
            + weighted_ratio / (1 - weighted_ratio) ** 2
        )

    assert_equal(
        "finite polymer tail majorant",
        tail + infinite_tail_from(18),
        infinite_tail_from(radius),
    )
    assert_true("polymer tail is smaller than full norm", tail < norm_bound)


def check_reflection_positive_compression() -> None:
    """Finite positive-cone check for blocked positive-time observables."""

    fine_vectors = [
        (Fraction(1), Fraction(0), Fraction(1)),
        (Fraction(2), Fraction(1), Fraction(0)),
        (Fraction(-1), Fraction(1), Fraction(1)),
    ]

    def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
        return sum(a * b for a, b in zip(left, right, strict=True))

    fine_gram = [
        [dot(fine_vectors[i], fine_vectors[j]) for j in range(3)]
        for i in range(3)
    ]
    blocking_matrix = [
        [Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(1)],
        [Fraction(0), Fraction(-1)],
    ]

    coarse_gram = [[Fraction(0) for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            coarse_gram[a][b] = sum(
                blocking_matrix[i][a] * fine_gram[i][j] * blocking_matrix[j][b]
                for i in range(3)
                for j in range(3)
            )

    assert_true("coarse reflection matrix diagonal 0", coarse_gram[0][0] >= 0)
    assert_true("coarse reflection matrix diagonal 1", coarse_gram[1][1] >= 0)
    determinant = (
        coarse_gram[0][0] * coarse_gram[1][1]
        - coarse_gram[0][1] * coarse_gram[1][0]
    )
    assert_true("coarse reflection matrix determinant", determinant >= 0)

    for c0, c1 in product(range(-3, 4), repeat=2):
        coeffs = (Fraction(c0), Fraction(c1))
        quadratic_form = sum(
            coeffs[a] * coarse_gram[a][b] * coeffs[b]
            for a in range(2)
            for b in range(2)
        )
        assert_true("compressed reflection-positive quadratic form", quadratic_form >= 0)


def main() -> None:
    check_path_blocking_equivariance()
    check_blocked_wilson_loop()
    check_pushforward_measure_invariance()
    check_gauge_invariant_source_window_descends()
    check_open_link_source_is_not_gauge_invariant()
    check_fine_weight_gauge_invariance()
    check_weighted_polymer_tail_bound()
    check_reflection_positive_compression()
    print("All finite lattice gauge-blocking checks passed.")


if __name__ == "__main__":
    main()
