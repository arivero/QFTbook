#!/usr/bin/env python3
"""Finite checks for the 4D SU(2) lattice gauge companion script."""

from __future__ import annotations

from check_utils import assert_close as _assert_close

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "qft_scripts" / "su2_gauge_4d_metropolis.py"
spec = importlib.util.spec_from_file_location("su2_gauge_4d_metropolis", SCRIPT)
su2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = su2
spec.loader.exec_module(su2)


def assert_close(name: str, got: float, expected: float, tol: float = 1.0e-10) -> None:
    _assert_close(name, got, expected, tol=tol)


def transformed_link(
    links: np.ndarray,
    site: tuple[int, int, int, int],
    mu: int,
    proposal: np.ndarray,
) -> np.ndarray:
    result = links.copy()
    su2.left_multiply_link_in_place(result, site, mu, proposal)
    return result


def check_quaternion_group_operations() -> None:
    rng = np.random.default_rng(20260527)
    identity = np.array([1.0, 0.0, 0.0, 0.0])
    for _ in range(40):
        a = su2.random_su2(rng)
        b = su2.random_su2(rng)
        product = su2.qmul(a, b)
        assert_close("unit norm of product", float(np.linalg.norm(product)), 1.0)
        assert_close("left inverse", float(np.linalg.norm(su2.qmul(su2.qconj(a), a) - identity)), 0.0)
        assert_close("right inverse", float(np.linalg.norm(su2.qmul(a, su2.qconj(a)) - identity)), 0.0)


def check_local_score_change() -> None:
    rng = np.random.default_rng(314159)
    links = su2.random_links(2, rng)
    for _ in range(20):
        site = (
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
        )
        mu = int(rng.integers(4))
        proposal = su2.random_small_su2(rng, 0.7)
        direct = su2.total_plaquette_score(transformed_link(links, site, mu, proposal)) - su2.total_plaquette_score(links)
        local = su2.local_score_change_for_left_multiply(links, site, mu, proposal)
        assert_close("local SU(2) gauge score change", local, direct, tol=1.0e-9)
        links = transformed_link(links, site, mu, proposal)


def check_pairwise_detailed_balance() -> None:
    rng = np.random.default_rng(271828)
    links = su2.random_links(2, rng)
    beta = 1.1
    for _ in range(20):
        site = (
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
            int(rng.integers(2)),
        )
        mu = int(rng.integers(4))
        proposal = su2.random_small_su2(rng, 0.4)
        target = transformed_link(links, site, mu, proposal)
        delta = su2.total_plaquette_score(target) - su2.total_plaquette_score(links)
        forward = min(1.0, math.exp(beta * delta))
        backward = min(1.0, math.exp(-beta * delta))
        lhs = math.exp(beta * su2.total_plaquette_score(links)) * forward
        rhs = math.exp(beta * su2.total_plaquette_score(target)) * backward
        assert_close("pairwise SU(2) detailed balance", lhs, rhs, tol=1.0e-8 * max(1.0, abs(lhs), abs(rhs)))
        links = target


def check_gauge_invariance() -> None:
    rng = np.random.default_rng(12345)
    links = su2.random_links(2, rng)
    gauges = np.empty((2, 2, 2, 2, 4), dtype=float)
    for site in np.ndindex((2, 2, 2, 2)):
        gauges[site] = su2.random_su2(rng)
    transformed = su2.gauge_transform(links, gauges)
    assert_close("SU(2) plaquette action gauge invariance", su2.total_plaquette_score(links), su2.total_plaquette_score(transformed))
    assert_close(
        "SU(2) Wilson loop gauge invariance",
        su2.wilson_loop_rectangle(links, 1, 1),
        su2.wilson_loop_rectangle(transformed, 1, 1),
    )


def check_one_plaquette_loop_identity() -> None:
    rng = np.random.default_rng(161803)
    links = su2.random_links(3, rng)
    plaquette_mean = su2.total_plaquette_score(links) / float(6 * 3**4)
    loop_mean = su2.wilson_loop_rectangle(links, 1, 1)
    assert_close("SU(2) 1x1 Wilson loop equals average plaquette", loop_mean, plaquette_mean)


def main() -> None:
    check_quaternion_group_operations()
    check_local_score_change()
    check_pairwise_detailed_balance()
    check_gauge_invariance()
    check_one_plaquette_loop_identity()
    print("All finite SU(2) gauge Metropolis checks passed.")


if __name__ == "__main__":
    main()
