#!/usr/bin/env python3
"""Finite gauge-blocking checks for the rigorous RG chapter.

The manuscript uses path products of fine links as a finite-regulator model
of a gauge-compatible Wilsonian blocking map.  This script checks the exact
group algebra in the smallest nonabelian test case, S_3, together with finite
locality, reflection-positivity, and reconstruction-budget arithmetic for the
gauge-blocking continuum-control datum.  It also checks the finite endpoint
algebra for matter bilinear sources with Wilson-line transporters: the
transported bilinear is gauge invariant, the untransported endpoint pairing
is not, and the connecting path is part of the observable label.
The path-deformation check verifies the exact finite identity
U_{P'}=U_{P'\bar P}U_P and the corresponding inserted-loop formula for the
difference of Wilson-line transported sources.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product

Perm = tuple[int, int, int]
Edge = tuple[int, int]
FineConfig = dict[Edge, Perm]
CoarseConfig = tuple[Perm, Perm, Perm]
Vector = tuple[Fraction, Fraction, Fraction]

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


def oriented_link_value(config: FineConfig, edge: Edge) -> Perm:
    if edge in config:
        return config[edge]
    reverse = (edge[1], edge[0])
    if reverse in config:
        return inv(config[reverse])
    raise KeyError(edge)


def path_product_oriented(config: FineConfig, path: tuple[Edge, ...]) -> Perm:
    total = IDENTITY
    for edge in path:
        total = mul(total, oriented_link_value(config, edge))
    return total


def reverse_path(path: tuple[Edge, ...]) -> tuple[Edge, ...]:
    return tuple((target, source) for source, target in reversed(path))


def act(perm: Perm, vector: Vector) -> Vector:
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for index, value in enumerate(vector):
        result[perm[index]] = value
    return tuple(result)  # type: ignore[return-value]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(a * b for a, b in zip(left, right, strict=True))


def vector_sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def transported_bilinear(
    config: FineConfig,
    path: tuple[Edge, ...],
    left_endpoint: Vector,
    right_endpoint: Vector,
) -> Fraction:
    return dot(
        left_endpoint,
        act(path_product_oriented(config, path), right_endpoint),
    )


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


def check_transported_matter_bilinear_source() -> None:
    config = {
        E01: (1, 2, 0),
        E12: (0, 2, 1),
        E23: (2, 0, 1),
        E30: (1, 0, 2),
    }
    path_03 = (E01, E12, E23)
    alternate_path_03 = ((0, 3),)
    left_endpoint = (Fraction(1, 2), Fraction(-2), Fraction(3, 5))
    right_endpoint = (Fraction(7, 3), Fraction(1), Fraction(-4, 7))

    base = transported_bilinear(config, path_03, left_endpoint, right_endpoint)
    for gauges in product(ELEMENTS, repeat=4):
        gauge = dict(zip((0, 1, 2, 3), gauges, strict=True))
        transformed_config = fine_gauge_transform(config, gauge)
        transformed_left = act(gauge[0], left_endpoint)
        transformed_right = act(gauge[3], right_endpoint)
        assert_equal(
            "Wilson-line transported endpoint bilinear is gauge invariant",
            transported_bilinear(
                transformed_config,
                path_03,
                transformed_left,
                transformed_right,
            ),
            base,
        )

    untransported_base = dot(left_endpoint, right_endpoint)
    witness_found = False
    for g0, g3 in product(ELEMENTS, repeat=2):
        transformed_pairing = dot(act(g0, left_endpoint), act(g3, right_endpoint))
        if transformed_pairing != untransported_base:
            witness_found = True
            break
    assert_true("untransported endpoint pairing fails gauge invariance", witness_found)

    alternate = transported_bilinear(
        config,
        alternate_path_03,
        left_endpoint,
        right_endpoint,
    )
    assert_true(
        "transported bilinear depends on the declared connector path",
        alternate != base,
    )


def check_transported_path_deformation_loop_insertion() -> None:
    config = {
        E01: (1, 2, 0),
        E12: (0, 2, 1),
        E23: (2, 0, 1),
        E30: (1, 0, 2),
    }
    base_path = (E01, E12, E23)
    alternate_path = ((0, 3),)
    left_endpoint = (Fraction(1, 2), Fraction(-2), Fraction(3, 5))
    right_endpoint = (Fraction(7, 3), Fraction(1), Fraction(-4, 7))

    base_holonomy = path_product_oriented(config, base_path)
    alternate_holonomy = path_product_oriented(config, alternate_path)
    loop_path = alternate_path + reverse_path(base_path)
    loop_holonomy = path_product_oriented(config, loop_path)
    assert_equal(
        "connector deformation holonomy identity",
        mul(loop_holonomy, base_holonomy),
        alternate_holonomy,
    )

    base_vector = act(base_holonomy, right_endpoint)
    alternate_vector = act(alternate_holonomy, right_endpoint)
    inserted_loop_vector = vector_sub(
        act(mul(loop_holonomy, base_holonomy), right_endpoint),
        act(base_holonomy, right_endpoint),
    )
    assert_equal(
        "connector deformation inserted-loop vector",
        inserted_loop_vector,
        vector_sub(alternate_vector, base_vector),
    )
    assert_equal(
        "connector deformation source difference",
        dot(left_endpoint, inserted_loop_vector),
        transported_bilinear(config, alternate_path, left_endpoint, right_endpoint)
        - transported_bilinear(config, base_path, left_endpoint, right_endpoint),
    )

    trivial_loop = path_product_oriented(config, base_path + reverse_path(base_path))
    assert_equal("same connector gives trivial deformation loop", trivial_loop, IDENTITY)
    assert_equal(
        "trivial deformation has no inserted-loop source change",
        dot(
            left_endpoint,
            vector_sub(
                act(mul(trivial_loop, base_holonomy), right_endpoint),
                act(base_holonomy, right_endpoint),
            ),
        ),
        Fraction(0),
    )


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

    bad_ratio = Fraction(1)
    bad_declared_bound = Fraction(10)
    bad_partial_norm = sum(
        Fraction(diameter + 1) * bad_ratio**diameter
        for diameter in range(6)
    )
    assert_true(
        "nondecaying polymer tail violates fixed locality bound",
        bad_partial_norm > bad_declared_bound,
    )


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


def check_gauge_reconstruction_error_budget() -> None:
    """Check the finite reconstruction bound C epsilon + eta."""

    locality_norm = Fraction(1, 40)
    reconstruction_constant = Fraction(5)
    residual_reconstruction_error = Fraction(1, 60)
    declared_bound = reconstruction_constant * locality_norm + residual_reconstruction_error
    actual_window_error = Fraction(2, 15)

    assert_equal("gauge reconstruction declared bound", declared_bound, Fraction(17, 120))
    assert_true("gauge reconstruction error controlled", actual_window_error <= declared_bound)

    omitted_residual_bound = reconstruction_constant * locality_norm
    assert_true(
        "gauge reconstruction residual term is load-bearing",
        actual_window_error > omitted_residual_bound,
    )


def check_gauge_path_deformation_reconstruction_budget() -> None:
    """Check the finite path-deformation source-window error budget."""

    local_loop_coordinate = Fraction(1, 100)
    connector_constant = Fraction(3)
    residual_path_error = Fraction(1, 50)
    declared_bound = connector_constant * local_loop_coordinate + residual_path_error
    actual_path_window_error = Fraction(1, 25)

    assert_equal("gauge path-deformation reconstruction bound", declared_bound, Fraction(1, 20))
    assert_true(
        "gauge path-deformation source difference controlled",
        actual_path_window_error <= declared_bound,
    )
    assert_true(
        "path-deformation residual term is load-bearing",
        actual_path_window_error > connector_constant * local_loop_coordinate,
    )

    stagnant_loop_coordinate = Fraction(1, 8)
    stagnant_bound = connector_constant * stagnant_loop_coordinate + residual_path_error
    assert_true(
        "uncontrolled local loop coordinate prevents path identification",
        stagnant_bound > Fraction(1, 4),
    )


def main() -> None:
    check_path_blocking_equivariance()
    check_blocked_wilson_loop()
    check_pushforward_measure_invariance()
    check_gauge_invariant_source_window_descends()
    check_open_link_source_is_not_gauge_invariant()
    check_transported_matter_bilinear_source()
    check_transported_path_deformation_loop_insertion()
    check_fine_weight_gauge_invariance()
    check_weighted_polymer_tail_bound()
    check_reflection_positive_compression()
    check_gauge_reconstruction_error_budget()
    check_gauge_path_deformation_reconstruction_budget()
    print("All finite lattice gauge-blocking checks passed.")


if __name__ == "__main__":
    main()
