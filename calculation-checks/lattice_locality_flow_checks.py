#!/usr/bin/env python3
"""Finite checks for Lieb-Robinson and spectral-flow algebra.

Evidence contract.
Target claims: the finite-regulator locality machinery in Volume IX,
Chapter 7, the quasi-local spectral-flow mechanism behind gapped phase
equivalence, and the exclusion of continuity-only phase criteria.
Independent construction: explicit overlap-chain counting on a finite line,
the factorial-to-exponential tail inequality, two-level projection transport,
the time-window split for quasi-local generator tails, and finite model
diagnostics with continuous correlators or free energy but failed uniform
stability.  A growing-support negative control separates pointwise convergence
on every fixed local algebra from transport of boundary/logical/extended
observable sequences.  A symmetry-breaking finite-band example separates a
bare parameter value from the selected ground-state set or phase face and
checks that selected-face transport needs a covariant selector.
Imported assumptions: finite-dimensional local Hilbert spaces, the chapter's
filter convention for quasi-adiabatic continuation, and the use of these
finite checks as arithmetic companions to the imported thermodynamic
automorphic-equivalence theorem.
Negative controls: a mass parameter tending to zero keeps each fixed-distance
correlator continuous while losing every positive gap lower bound and sending
the correlation length to infinity; a value-only topology on a critical free
energy misses a divergent susceptibility; automorphisms can converge on every
fixed local observable while a sequence whose support moves to the boundary or
grows with the volume has no controlled transported limit; a gapped
finite-volume ground band can contain two extremal branches, so the parameter
value alone does not select a phase carrier; the full ground-state set can be
transported while a noncovariantly chosen endpoint face is not the image of the
initial face.
Scope boundary: these checks do not prove the infinite-volume
Lieb-Robinson/spectral-flow theorem, establish a continuum gauge-theory phase
equivalence, or classify gapless universality classes.
"""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import itertools
import math


Matrix = list[list[complex]]


def assert_close(lhs: float, rhs: float, message: str, tol: float = 1e-10) -> None:
    _assert_close(message, lhs, rhs, tol=tol)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matadd(a: Matrix, b: Matrix, ca: complex = 1, cb: complex = 1) -> Matrix:
    return [
        [ca * a[i][j] + cb * b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return matadd(matmul(a, b), matmul(b, a), 1, -1)


def frobenius_norm(a: Matrix) -> float:
    return math.sqrt(sum(abs(entry) ** 2 for row in a for entry in row))


def line_interaction_supports(length: int) -> list[frozenset[int]]:
    return [frozenset((i, i + 1)) for i in range(length - 1)]


def overlap_degree(supports: list[frozenset[int]]) -> int:
    return max(sum(1 for other in supports if support & other) for support in supports)


def boundary_supports(supports: list[frozenset[int]], region: set[int]) -> list[int]:
    return [idx for idx, support in enumerate(supports) if support & region]


def supports_touching_y(supports: list[frozenset[int]], region: set[int]) -> set[int]:
    return {idx for idx, support in enumerate(supports) if support & region}


def overlap_adjacency(supports: list[frozenset[int]]) -> dict[int, list[int]]:
    return {
        i: [j for j, other in enumerate(supports) if supports[i] & other]
        for i in range(len(supports))
    }


def shortest_overlap_chain_length(length: int, x_region: set[int], y_region: set[int]) -> int:
    supports = line_interaction_supports(length)
    starts = boundary_supports(supports, x_region)
    targets = supports_touching_y(supports, y_region)
    adjacency = overlap_adjacency(supports)
    frontier = [(start, 1) for start in starts]
    seen = set(starts)
    while frontier:
        node, depth = frontier.pop(0)
        if node in targets:
            return depth
        for nxt in adjacency[node]:
            if nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt, depth + 1))
    raise AssertionError("no overlap path in connected line")


def count_overlap_chains(length: int, x_region: set[int], y_region: set[int], chain_length: int) -> int:
    supports = line_interaction_supports(length)
    starts = boundary_supports(supports, x_region)
    targets = supports_touching_y(supports, y_region)
    adjacency = overlap_adjacency(supports)
    if chain_length == 0:
        return 0
    current = {start: 1 for start in starts}
    for _ in range(1, chain_length):
        nxt_counts: dict[int, int] = {}
        for node, count in current.items():
            for nxt in adjacency[node]:
                nxt_counts[nxt] = nxt_counts.get(nxt, 0) + count
        current = nxt_counts
    return sum(count for node, count in current.items() if node in targets)


def check_overlap_path_count() -> None:
    for length in range(4, 10):
        supports = line_interaction_supports(length)
        degree = overlap_degree(supports)
        x_region = {0}
        y_region = {length - 1}
        boundary = len(boundary_supports(supports, x_region))
        distance = shortest_overlap_chain_length(length, x_region, y_region)
        assert_true(distance == length - 1, "nearest-neighbor line has expected overlap distance")
        for chain_length in range(1, length + 3):
            count = count_overlap_chains(length, x_region, y_region, chain_length)
            if chain_length < distance:
                assert_true(count == 0, "chains shorter than d_phi do not reach the target")
            assert_true(
                count <= boundary * (degree ** max(chain_length - 1, 0)),
                "overlap-chain count is bounded by boundary times overlap-degree powers",
            )


def tail_sum(a: float, distance: int, terms: int = 80) -> float:
    return sum((a**n) / math.factorial(n) for n in range(distance, terms))


def check_exponential_tail_bound() -> None:
    for a in [0.1, 1.7, 5.0]:
        for distance in [1, 3, 7, 12]:
            for mu in [0.25, 0.7, 1.3]:
                lhs = tail_sum(a, distance)
                rhs = math.exp(-mu * distance + a * math.exp(mu))
                assert_true(lhs <= rhs * (1 + 1e-12), "factorial tail obeys exponential LR bound")


def two_level_h(theta: float) -> Matrix:
    return [
        [math.cos(theta), math.sin(theta)],
        [math.sin(theta), -math.cos(theta)],
    ]


def two_level_dh(theta: float) -> Matrix:
    return [
        [-math.sin(theta), math.cos(theta)],
        [math.cos(theta), math.sin(theta)],
    ]


def identity2() -> Matrix:
    return [[1, 0], [0, 1]]


def scalar_mul(c: complex, a: Matrix) -> Matrix:
    return [[c * entry for entry in row] for row in a]


def check_two_level_spectral_flow() -> None:
    for theta in [0.0, 0.2, 0.9, 1.4]:
        h = two_level_h(theta)
        dh = two_level_dh(theta)
        identity = identity2()
        p = matadd(identity, h, 0.5, -0.5)  # lower band of H with eigenvalue -1
        q = matadd(identity, h, 0.5, 0.5)
        dp = scalar_mul(-0.5, dh)

        # Gap between the two bands is 2.  The filter convention gives
        # D_{out,in}= i V_{out,in}/2 and the adjoint block with the opposite sign.
        qvp = matmul(matmul(q, dh), p)
        pvq = matmul(matmul(p, dh), q)
        d_generator = matadd(qvp, pvq, 0.5j, -0.5j)
        rhs = scalar_mul(1j, commutator(d_generator, p))
        assert_close(frobenius_norm(matadd(dp, rhs, 1, -1)), 0.0, "finite quasi-adiabatic generator transports the isolated band")

        k_generator = commutator(dp, p)
        rhs_k = commutator(k_generator, p)
        assert_close(frobenius_norm(matadd(dp, rhs_k, 1, -1)), 0.0, "projection commutator generator transports the band")


def exponential_filter_abs(beta: float, t: float) -> float:
    return 0.5 * beta * math.exp(-beta * abs(t))


def filter_tail(beta: float, threshold: float) -> float:
    return math.exp(-beta * threshold)


def massive_correlator(mass: float, distance: float) -> float:
    return math.exp(-mass * distance)


def critical_free_energy(parameter: float) -> float:
    if parameter == 0.0:
        return 0.0
    return parameter * parameter * math.log(parameter * parameter)


def critical_susceptibility(parameter: float) -> float:
    return 2.0 * math.log(parameter * parameter) + 6.0


def check_quasilocal_tail_split() -> None:
    beta = 1.3
    velocity = 2.0
    mu = 0.8
    for radius in [4.0, 8.0, 12.0]:
        threshold = radius / (2 * velocity)
        inside_bound_factor = math.exp(-mu * radius / 2)
        # For |t| <= R/(2v), exp[-mu(R-v|t|)] <= exp[-mu R/2].
        for sample in [0.0, threshold / 3, threshold]:
            lhs = math.exp(-mu * (radius - velocity * sample))
            assert_true(lhs <= inside_bound_factor * (1 + 1e-12), "inside time-window LR leakage has the claimed radius factor")
        # The normalized exponential filter has exact two-sided tail.
        assert_close(
            2 * sum(exponential_filter_abs(beta, threshold + k * 0.001) * 0.001 for k in range(20000)),
            filter_tail(beta, threshold),
            "numerical exponential-filter tail matches analytic tail",
            tol=2e-3,
        )


def check_uniform_gap_is_not_pointwise_continuity() -> None:
    distances = [1.0, 2.0, 5.0, 10.0]
    small_mass = 1.0e-4

    for distance in distances:
        massless_value = massive_correlator(0.0, distance)
        nearby_value = massive_correlator(small_mass, distance)
        assert_true(
            abs(nearby_value - massless_value) < 2.0e-3,
            "finite-distance correlators can be continuous at a gap closing",
        )

    gaps_along_path = [1.0 / n for n in range(1, 200)] + [0.0]
    assert_true(min(gaps_along_path) == 0.0, "critical path loses a positive gap lower bound")
    assert_true(
        not all(gap >= 0.05 for gap in gaps_along_path),
        "continuity-only criterion incorrectly supplied a uniform gap",
    )

    correlation_lengths = [1.0 / gap for gap in gaps_along_path if gap > 0.0]
    assert_true(
        correlation_lengths[-1] > 100.0 * correlation_lengths[0],
        "closing gap produces an unbounded correlation-length sequence",
    )


def check_weak_topology_ignores_susceptibility_divergence() -> None:
    parameters = [10.0 ** (-k) for k in range(1, 8)]
    values = [abs(critical_free_energy(parameter)) for parameter in parameters]
    susceptibilities = [abs(critical_susceptibility(parameter)) for parameter in parameters]

    assert_true(values[-1] < values[0], "critical free energy can remain continuous")
    assert_true(values[-1] < 1.0e-10, "weak value topology sees the critical point as close")
    assert_true(
        susceptibilities[-1] > 3.0 * susceptibilities[0],
        "derivative-sensitive diagnostics detect the critical singularity",
    )
    assert_true(
        abs(critical_free_energy(parameters[-1]) - critical_free_energy(0.0)) < 1.0e-10,
        "value-only pseudometric misses the derivative singularity",
    )


def check_fixed_local_convergence_does_not_transport_growing_support() -> None:
    """Boundary flips are invisible locally but not on volume-dependent probes.

    Think of conjugation by a Pauli Z on the last site of a finite chain.  It
    fixes every X operator supported in a prescribed left interval once the
    volume is large enough, while it sends the boundary X operator to -X.
    Thus pointwise convergence on the quasi-local algebra near the origin does
    not control a boundary/logical observable sequence.
    """

    fixed_support = {0, 1, 2}

    def boundary_flip_error(length: int, support: set[int]) -> float:
        return 2.0 if (length - 1) in support else 0.0

    for length in range(6, 20):
        assert_close(
            boundary_flip_error(length, fixed_support),
            0.0,
            "boundary flip is invisible on every fixed local support",
        )

    moving_boundary_errors = [
        boundary_flip_error(length, {length - 1})
        for length in range(6, 20)
    ]
    assert_true(
        all(error == 2.0 for error in moving_boundary_errors),
        "moving boundary observable is not controlled by fixed-local convergence",
    )

    growing_string_errors = [
        boundary_flip_error(length, set(range(length)))
        for length in range(6, 20)
    ]
    assert_true(
        all(error == 2.0 for error in growing_string_errors),
        "growing-support string needs its own uniform transport estimate",
    )


def check_parameter_value_does_not_select_coexisting_phase_face() -> None:
    """Full band transport and selected-face transport are distinct claims."""

    coupling = 1.0
    boundary_strength = 0.01

    def configurations(length: int) -> list[tuple[int, ...]]:
        return list(itertools.product((-1, 1), repeat=length))

    def periodic_ising_energy(config: tuple[int, ...]) -> float:
        length = len(config)
        return -coupling * sum(
            config[site] * config[(site + 1) % length]
            for site in range(length)
        )

    def magnetization(config: tuple[int, ...]) -> float:
        return sum(config) / len(config)

    def boundary_selector_score(config: tuple[int, ...], boundary_spin: int) -> float:
        # A vanishing boundary field selects a thermodynamic branch without
        # changing the periodic bulk Hamiltonian used for the full band.
        return boundary_strength * boundary_spin * sum(config)

    def select_by_boundary(
        ground_configs: list[tuple[int, ...]],
        boundary_spin: int,
    ) -> set[float]:
        best_score = max(
            boundary_selector_score(config, boundary_spin)
            for config in ground_configs
        )
        return {
            magnetization(config)
            for config in ground_configs
            if abs(boundary_selector_score(config, boundary_spin) - best_score) < 1.0e-12
        }

    for length in range(4, 9):
        configs = configurations(length)
        energies = {config: periodic_ising_energy(config) for config in configs}
        ground_energy = min(energies.values())
        ground_configs = [
            config
            for config, energy in energies.items()
            if abs(energy - ground_energy) < 1.0e-12
        ]
        excited_energies = [
            energy
            for energy in energies.values()
            if energy > ground_energy + 1.0e-12
        ]
        full_ground_set = {magnetization(config) for config in ground_configs}
        gap_above_union = min(excited_energies) - ground_energy

        assert_true(
            full_ground_set == {-1.0, 1.0},
            "periodic finite Ising band has exactly two extremal branches",
        )
        assert_close(
            gap_above_union,
            4.0 * coupling,
            "positive gap above the full ground band does not select a branch",
        )
        assert_true(
            select_by_boundary(ground_configs, 1) == {1.0},
            "plus boundary selects plus face",
        )
        assert_true(
            select_by_boundary(ground_configs, -1) == {-1.0},
            "minus boundary selects minus face",
        )

    plus_face = frozenset({1.0})
    minus_face = frozenset({-1.0})
    full_band_set = frozenset({-1.0, 1.0})

    def spin_flip_state_set(states: frozenset[float]) -> frozenset[float]:
        return frozenset(-state for state in states)

    assert_true(
        spin_flip_state_set(full_band_set) == full_band_set,
        "BMNS-type full-set transport can hold setwise",
    )
    assert_true(
        spin_flip_state_set(plus_face) == minus_face,
        "covariant selector transports plus face to minus face under spin flip",
    )
    noncovariant_endpoint_plus = plus_face
    assert_true(
        spin_flip_state_set(plus_face) != noncovariant_endpoint_plus,
        "a noncovariantly chosen endpoint plus face is not the transported face",
    )

    plus_magnetization = next(iter(plus_face))
    minus_magnetization = next(iter(minus_face))
    symmetric_mixture_magnetization = 0.5 * (plus_magnetization + minus_magnetization)
    assert_close(
        symmetric_mixture_magnetization,
        0.0,
        "the whole ground-state convex set is not an extremal branch",
    )
    assert_true(
        plus_face != minus_face,
        "a selected face is extra selector data beyond the parameter value",
    )


def main() -> None:
    check_overlap_path_count()
    check_exponential_tail_bound()
    check_two_level_spectral_flow()
    check_quasilocal_tail_split()
    check_uniform_gap_is_not_pointwise_continuity()
    check_weak_topology_ignores_susceptibility_divergence()
    check_fixed_local_convergence_does_not_transport_growing_support()
    check_parameter_value_does_not_select_coexisting_phase_face()
    print("Finite lattice locality and spectral-flow checks passed.")


if __name__ == "__main__":
    main()
