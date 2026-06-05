#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- In the fixed-length Z2 gauge-Higgs model, plaquettes, hopping terms, and
  Higgs-ended open Wilson lines are exactly gauge invariant at finite volume.
- The finite high-temperature expansion keeps only parity-even monomials:
  plaquette surfaces may end on matter lines, which is the finite algebraic
  mechanism behind charge-one screening.
- Fundamental matter removes the exact center one-form diagnostic, while
  center-neutral matter leaves it intact.
- A Fradkin-Shenker corridor is a connected union of theorem-controlled
  polymer domains; finite-volume analyticity alone is weaker than the uniform
  thermodynamic statement.

Independent construction:
- The script enumerates all spins in a 2x2 periodic Z2 gauge-Higgs model,
  checks gauge invariance under arbitrary local gauge transformations, and
  compares a direct finite spin sum with the parity-filtered expansion.
- It separately checks center N-ality screening and a toy connected-domain
  model for strong, bridge, and Higgs polymer regions.

Imported assumptions:
- The actual Fradkin-Shenker/Osterwalder-Seiler theorem supplies the
  volume-uniform polymer bounds, constants, analyticity neighborhoods, and
  thermodynamic limits.  The toy domain constants here are only consistency
  checks of the declared mechanism map.

Negative controls:
- A bare open Wilson line without Higgs endpoint fields is gauge variant.
- Center-neutral matter cannot screen a fundamental center charge.
- A finite polynomial identity is not treated as an infinite-volume phase
  theorem.

Scope boundary:
- These checks verify finite gauge-invariance, parity-selection, screening,
  and corridor-bookkeeping claims.  They do not prove cluster expansion
  convergence, exponential clustering, mass gaps, continuum limits, or the
  Fradkin-Shenker/Osterwalder-Seiler theorem.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import exp, tanh


Vertex = tuple[int, int]
Edge = tuple[Vertex, str]


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_equal(lhs: object, rhs: object, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: expected {rhs!r}, got {lhs!r}")


def vertices(size: int = 2) -> list[Vertex]:
    return [(x, y) for x in range(size) for y in range(size)]


def edges(size: int = 2) -> list[Edge]:
    return [((x, y), direction) for x in range(size) for y in range(size) for direction in ("x", "y")]


def edge_target(edge: Edge, size: int = 2) -> Vertex:
    (x, y), direction = edge
    if direction == "x":
        return ((x + 1) % size, y)
    return (x, (y + 1) % size)


def plaquette_edges(origin: Vertex, size: int = 2) -> list[Edge]:
    x, y = origin
    return [
        ((x, y), "x"),
        (((x + 1) % size, y), "y"),
        ((x, (y + 1) % size), "x"),
        ((x, y), "y"),
    ]


def all_spin_assignments(keys: list[object]) -> list[dict[object, int]]:
    return [dict(zip(keys, values, strict=True)) for values in product((-1, 1), repeat=len(keys))]


def plaquette_value(link_spins: dict[Edge, int], origin: Vertex) -> int:
    value = 1
    for edge in plaquette_edges(origin):
        value *= link_spins[edge]
    return value


def hopping_value(site_spins: dict[Vertex, int], link_spins: dict[Edge, int], edge: Edge) -> int:
    source = edge[0]
    target = edge_target(edge)
    return site_spins[source] * link_spins[edge] * site_spins[target]


def open_higgs_line(site_spins: dict[Vertex, int], link_spins: dict[Edge, int], path: list[Edge]) -> int:
    source = path[0][0]
    target = edge_target(path[-1])
    value = site_spins[source] * site_spins[target]
    for edge in path:
        value *= link_spins[edge]
    return value


def bare_open_line(link_spins: dict[Edge, int], path: list[Edge]) -> int:
    value = 1
    for edge in path:
        value *= link_spins[edge]
    return value


def gauge_transform(
    site_spins: dict[Vertex, int],
    link_spins: dict[Edge, int],
    eta: dict[Vertex, int],
) -> tuple[dict[Vertex, int], dict[Edge, int]]:
    transformed_sites = {vertex: eta[vertex] * spin for vertex, spin in site_spins.items()}
    transformed_links = {
        edge: eta[edge[0]] * spin * eta[edge_target(edge)]
        for edge, spin in link_spins.items()
    }
    return transformed_sites, transformed_links


def check_finite_gauge_invariance() -> None:
    verts = vertices()
    eds = edges()
    site_spins = {vertex: (-1 if vertex[0] == vertex[1] else 1) for vertex in verts}
    link_spins = {edge: (-1 if edge[1] == "x" else 1) for edge in eds}
    eta = {(x, y): (-1 if x == 0 else 1) for x, y in verts}
    transformed_sites, transformed_links = gauge_transform(site_spins, link_spins, eta)

    for origin in verts:
        assert_equal(
            plaquette_value(transformed_links, origin),
            plaquette_value(link_spins, origin),
            "plaquette is gauge invariant",
        )
    for edge in eds:
        assert_equal(
            hopping_value(transformed_sites, transformed_links, edge),
            hopping_value(site_spins, link_spins, edge),
            "Higgs hopping term is gauge invariant",
        )

    path = [((0, 0), "x")]
    assert_equal(
        open_higgs_line(transformed_sites, transformed_links, path),
        open_higgs_line(site_spins, link_spins, path),
        "Higgs-ended open Wilson line is gauge invariant",
    )
    assert_true(
        bare_open_line(transformed_links, path) != bare_open_line(link_spins, path),
        "bare open Wilson line is a gauge-variant negative control",
    )


def monomial_is_even(
    plaquette_subset: tuple[Vertex, ...],
    edge_subset: tuple[Edge, ...],
    extra_plaquettes: tuple[Vertex, ...] = (),
) -> bool:
    site_parity = {vertex: 0 for vertex in vertices()}
    link_parity = {edge: 0 for edge in edges()}
    for origin in plaquette_subset + extra_plaquettes:
        for edge in plaquette_edges(origin):
            link_parity[edge] ^= 1
    for edge in edge_subset:
        source = edge[0]
        target = edge_target(edge)
        site_parity[source] ^= 1
        site_parity[target] ^= 1
        link_parity[edge] ^= 1
    return all(value == 0 for value in site_parity.values()) and all(value == 0 for value in link_parity.values())


def parity_filtered_coefficients(extra_plaquettes: tuple[Vertex, ...] = ()) -> dict[tuple[int, int], int]:
    verts = vertices()
    eds = edges()
    coeffs: dict[tuple[int, int], int] = {}
    for p_count in range(len(verts) + 1):
        for plaquette_subset in combinations(verts, p_count):
            for e_count in range(len(eds) + 1):
                for edge_subset in combinations(eds, e_count):
                    if monomial_is_even(plaquette_subset, edge_subset, extra_plaquettes):
                        key = (p_count, e_count)
                        coeffs[key] = coeffs.get(key, 0) + 1
    return coeffs


def evaluate_coefficients(coeffs: dict[tuple[int, int], int], u: Fraction, v: Fraction) -> Fraction:
    return sum(Fraction(count) * u**p_count * v**e_count for (p_count, e_count), count in coeffs.items())


def direct_normalized_sum(u: Fraction, v: Fraction, extra_plaquette: Vertex | None = None) -> Fraction:
    total = Fraction(0)
    eds = edges()
    for site_spins in all_spin_assignments(vertices()):
        for link_spins in all_spin_assignments(eds):
            term = Fraction(1)
            if extra_plaquette is not None:
                term *= plaquette_value(link_spins, extra_plaquette)
            for origin in vertices():
                term *= 1 + u * plaquette_value(link_spins, origin)
            for edge in eds:
                term *= 1 + v * hopping_value(site_spins, link_spins, edge)
            total += term
    return total / Fraction(2 ** (len(vertices()) + len(eds)))


def check_high_temperature_parity_expansion() -> None:
    u = Fraction(1, 5)
    v = Fraction(1, 7)
    partition_poly = evaluate_coefficients(parity_filtered_coefficients(), u, v)
    partition_direct = direct_normalized_sum(u, v)
    assert_equal(partition_poly, partition_direct, "partition expansion equals parity-filtered finite spin sum")

    origin = (0, 0)
    numerator_poly = evaluate_coefficients(parity_filtered_coefficients((origin,)), u, v)
    numerator_direct = direct_normalized_sum(u, v, extra_plaquette=origin)
    assert_equal(numerator_poly, numerator_direct, "plaquette numerator has the same parity-selection rule")

    assert_true(
        numerator_poly / partition_poly != numerator_poly,
        "finite expectation is a ratio, so finite polynomiality is not an infinite-volume theorem",
    )


def generated_subgroup(modulus: int, charges: list[int]) -> set[int]:
    subgroup = {0}
    changed = True
    while changed:
        changed = False
        for value in list(subgroup):
            for charge in charges:
                candidate = (value + charge) % modulus
                if candidate not in subgroup:
                    subgroup.add(candidate)
                    changed = True
    return subgroup


def surviving_center_one_form(modulus: int, matter_nalities: list[int]) -> set[int]:
    return {
        center_power
        for center_power in range(modulus)
        if all((center_power * nality) % modulus == 0 for nality in matter_nalities)
    }


def check_screening_and_one_form_bookkeeping() -> None:
    assert_equal(generated_subgroup(2, [1]), {0, 1}, "Z2 fundamental matter screens fundamental charge")
    assert_equal(generated_subgroup(2, [0]), {0}, "Z2 center-neutral matter leaves fundamental charge unscreened")
    assert_equal(surviving_center_one_form(2, [1]), {0}, "fundamental matter removes exact Z2 one-form symmetry")
    assert_equal(surviving_center_one_form(2, [0]), {0, 1}, "adjoint/neutral matter preserves Z2 one-form symmetry")

    assert_equal(generated_subgroup(4, [2]), {0, 2}, "charge-two matter screens only even Z4 charges")
    assert_true(1 not in generated_subgroup(4, [2]), "charge-two matter cannot screen a fundamental Z4 charge")
    assert_equal(surviving_center_one_form(4, [2]), {0, 2}, "charge-two matter leaves a residual Z2 one-form symmetry")


def in_strong_domain(beta: float, kappa: float, constant: float) -> bool:
    return constant * (abs(tanh(beta)) + abs(tanh(kappa))) < 1.0


def in_bridge_domain(beta: float, constant: float) -> bool:
    return constant * abs(tanh(beta)) < 1.0


def in_higgs_domain(beta: float, kappa: float, constant: float) -> bool:
    return constant * (abs(tanh(beta)) + exp(-2.0 * kappa)) < 1.0


def check_corridor_domain_bookkeeping() -> None:
    constant = 3.0
    small_beta = 0.05
    strong_corner = (small_beta, 0.05)
    higgs_corner = (small_beta, 3.0)
    assert_true(in_strong_domain(*strong_corner, constant), "strong corner lies in the strong polymer domain")
    assert_true(in_higgs_domain(*higgs_corner, constant), "large-kappa corner lies in the Higgs defect domain")

    kappas = [i / 10 for i in range(0, 31)]
    assert_true(
        all(in_bridge_domain(small_beta, constant) for _ in kappas),
        "small plaquette activity gives a bridge uniform in kappa",
    )
    assert_true(
        in_bridge_domain(small_beta, constant)
        and in_strong_domain(*strong_corner, constant)
        and in_higgs_domain(*higgs_corner, constant),
        "strong, bridge, and Higgs domains form a connected corridor in the toy domain map",
    )


def main() -> None:
    check_finite_gauge_invariance()
    check_high_temperature_parity_expansion()
    check_screening_and_one_form_bookkeeping()
    check_corridor_domain_bookkeeping()
    print("Gauge-Higgs Fradkin-Shenker finite bookkeeping checks passed.")


if __name__ == "__main__":
    main()
