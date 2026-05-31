#!/usr/bin/env python3
"""Finite checks for Lieb-Robinson and spectral-flow algebra.

The checks cover the finite-regulator locality machinery in Volume IX,
Chapter 7: overlap-chain counting for the path-count Lieb-Robinson estimate,
the elementary exponential tail bound, finite two-level spectral-flow
transport, and the time-window split behind quasi-local generator tails.
"""

from __future__ import annotations

import math


Matrix = list[list[complex]]


def assert_close(lhs: float, rhs: float, message: str, tol: float = 1e-10) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


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


def main() -> None:
    check_overlap_path_count()
    check_exponential_tail_bound()
    check_two_level_spectral_flow()
    check_quasilocal_tail_split()
    print("Finite lattice locality and spectral-flow checks passed.")


if __name__ == "__main__":
    main()
